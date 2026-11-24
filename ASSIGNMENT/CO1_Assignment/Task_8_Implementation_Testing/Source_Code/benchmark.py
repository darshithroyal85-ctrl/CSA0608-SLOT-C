"""
Benchmark harness. Same dataset (fixed seed) is shared by all algorithms at each n.
Scenarios per n:
  best    : key is the first element examined by each algorithm
              (linear: records[0]; binary: the middle element; hash: key alone in its bucket)
  average : 1000 random keys that EXIST (hash/binary), fewer for linear at large n
  worst   : unsuccessful search (key absent) -> full scan / full depth / longest chain
Outputs: ../results.csv  (all measurements)
"""
import random, time, csv, statistics, os, sys
from algorithms import *

SIZES = [1_000, 10_000, 100_000, 1_000_000]
SEED = 2026
OUT = os.path.join(os.path.dirname(__file__), "..", "results.csv")

def timeit(fn, keys, reps=1):
    t0 = time.perf_counter()
    for _ in range(reps):
        for k in keys: fn(k)
    return (time.perf_counter() - t0) / (reps * len(keys))   # seconds per search

def main():
    rows = []
    for n in SIZES:
        rnd = random.Random(SEED + n)
        data = rnd.sample(range(10**9, 10**10), n)          # unique 10-digit registration numbers
        present = set(data)
        # ---- preprocessing
        t0 = time.perf_counter(); srt = sort_records(data); t_sort = time.perf_counter() - t0
        t0 = time.perf_counter(); ht = build_hash_index(data); t_hash = time.perf_counter() - t0
        # ---- query sets
        n_avg = 1000 if n <= 100_000 else 300
        n_lin = {1000: 2000, 10000: 1000, 100000: 200, 1000000: 40}[n]
        avg_keys = rnd.sample(data, 1000)
        miss_keys = []
        while len(miss_keys) < 1000:
            k = rnd.randrange(10**9, 10**10)
            if k not in present: miss_keys.append(k)
        best_lin = data[0]; best_bin = srt[(len(srt)-1)//2]
        # best case for hash: a key whose bucket chain has length 1 (first probe hits)
        best_hash = next(k for k in data if len(ht.buckets[ht._h(k)]) == 1)
        # ---- comparisons (operation counts, exact)
        def mean_cmp(fn, keys): return statistics.mean(fn(k)[1] for k in keys)
        def max_cmp(fn, keys): return max(fn(k)[1] for k in keys)
        lin = lambda k: linear_search(data, k)
        bin_ = lambda k: binary_search_recursive(srt, k)
        has = lambda k: ht.search(k)
        la = avg_keys[:n_lin if n_lin < 1000 else 1000]
        lm = miss_keys[:n_lin if n_lin < 1000 else 1000]
        cmp = {
          ("Linear","best"): linear_search(data,best_lin)[1],
          ("Linear","average"): mean_cmp(lin, la),
          ("Linear","worst"): mean_cmp(lin, lm),
          ("Binary","best"): binary_search_recursive(srt,best_bin)[1],
          ("Binary","average"): mean_cmp(bin_, avg_keys),
          ("Binary","worst"): mean_cmp(bin_, miss_keys),
          ("Hash","best"): ht.search(best_hash)[1],
          ("Hash","average"): mean_cmp(has, avg_keys),
          ("Hash","worst"): mean_cmp(has, miss_keys),
        }
        chain_max = max(len(b) for b in ht.buckets)
        # ---- timing (seconds per single search)
        tm = {
          ("Linear","best"): timeit(lambda k: linear_search(data,k), [best_lin]*2000),
          ("Linear","average"): timeit(lambda k: linear_search(data,k), la[:n_lin]),
          ("Linear","worst"): timeit(lambda k: linear_search(data,k), lm[:n_lin]),
          ("Binary","best"): timeit(lambda k: binary_search_recursive(srt,k), [best_bin]*5000),
          ("Binary","average"): timeit(lambda k: binary_search_recursive(srt,k), avg_keys, 3),
          ("Binary","worst"): timeit(lambda k: binary_search_recursive(srt,k), miss_keys, 3),
          ("Hash","best"): timeit(lambda k: ht.search(k), [best_hash]*5000),
          ("Hash","average"): timeit(lambda k: ht.search(k), avg_keys, 3),
          ("Hash","worst"): timeit(lambda k: ht.search(k), miss_keys, 3),
        }
        # iterative-binary cross-check timing
        t_bi = timeit(lambda k: binary_search_iterative(srt,k), avg_keys, 3)
        for (alg, case), c in cmp.items():
            pre = {"Linear":0.0,"Binary":t_sort,"Hash":t_hash}[alg]
            rows.append(dict(n=n, algorithm=alg, case=case, comparisons=round(c,3),
                             time_per_search_us=round(tm[(alg,case)]*1e6,3),
                             preprocessing_s=round(pre,5), chain_max=chain_max if alg=="Hash" else "",
                             binary_iterative_avg_us=round(t_bi*1e6,3) if alg=="Binary" else ""))
        print(f"n={n:>9,} done | sort {t_sort:.3f}s | hash build {t_hash:.3f}s | max chain {chain_max}", flush=True)
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

if __name__ == "__main__":
    main()
