"""Correctness tests: all three algorithms must agree with a Python set/dict oracle."""
import random
from algorithms import *

def run():
    random.seed(7)
    results = []
    # edge cases
    for n in (0, 1, 2, 3, 10):
        data = random.sample(range(10**9, 10**10), n)
        srt = sort_records(data)
        ht = build_hash_index(data)
        present = set(data)
        probes = list(data) + [10**9 - 1, 10**10 + 5, 12345678901]
        for key in probes:
            i1, _ = linear_search(data, key)
            i2, _ = binary_search_recursive(srt, key)
            i2b, _ = binary_search_iterative(srt, key)
            i3, _ = ht.search(key)
            ok = ((i1 != -1) == (key in present) == (i2 != -1) == (i2b != -1) == (i3 != -1))
            if i1 != -1: ok &= data[i1] == key
            if i2 != -1: ok &= srt[i2] == key
            if i3 != -1: ok &= data[i3] == key
            assert ok, (n, key)
        results.append(f"n={n:<4} edge test PASSED ({len(probes)} probes)")
    # randomised bulk tests
    for n in (1000, 10000):
        data = random.sample(range(10**9, 10**10), n)
        srt = sort_records(data); ht = build_hash_index(data); present = set(data)
        probes = random.sample(data, 500) + [random.randrange(10**9, 10**10) for _ in range(500)]
        probes += [data[0], data[-1], min(data), max(data)]
        for key in probes:
            found = key in present
            assert (linear_search(data, key)[0] != -1) == found
            assert (binary_search_recursive(srt, key)[0] != -1) == found
            assert (ht.search(key)[0] != -1) == found
        results.append(f"n={n:<6} randomised test PASSED ({len(probes)} probes, hits+misses+boundaries)")
    return results

if __name__ == "__main__":
    print("CORRECTNESS TEST SUITE")
    print("=" * 60)
    for line in run(): print(line)
    print("ALL TESTS PASSED: Linear, Binary(recursive), Binary(iterative), Hash agree with oracle.")
