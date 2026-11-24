# Task 8 – Implementation and Testing (4 marks)

**Language / environment:** Python 3.12 (CPython), single thread, `time.perf_counter()`; all algorithms in one module so that they are tested under identical conditions.

| File | Purpose |
|---|---|
| `Source_Code/algorithms.py` | Linear search, recursive binary search (+ iterative twin used as a cross-check), sort preprocessing, hash table (chaining) and its build routine – all instrumented to return the number of key comparisons |
| `Source_Code/test_correctness.py` | Correctness test-suite (oracle = Python `set`) |
| `Source_Code/benchmark.py` | Experimental harness → `results.csv` |
| `test_output.txt`, `benchmark_log.txt`, `results.csv` | Captured outputs |

## Datasets
* n ∈ {1,000; 10,000; 100,000; 1,000,000}
* Unique 10-digit registration numbers drawn with `random.Random(2026 + n).sample(range(10⁹, 10¹⁰), n)` (fixed seed ⇒ reproducible). Records are in random (unsorted) order for linear search/hash; a sorted copy (`sorted()`) is used for binary search. The **same data set** is shared by all three algorithms at each n.

## Test cases (correctness)
| Category | Cases |
|---|---|
| Edge sizes | n = 0, 1, 2, 3, 10 (empty database, single record, odd/even sizes) |
| Key positions | first element, last element, minimum, maximum, random present keys |
| Unsuccessful | keys below the minimum, above the maximum, random absent keys |
| Bulk randomised | n = 1,000 and 10,000 with 1,000 mixed probes each |
| Agreement | all four implementations (linear, binary recursive, binary iterative, hash) must return "found/not found" identically to the oracle, and any returned index must hold the key |

**Result:** all tests passed (see `test_output.txt` and `Report/Output_Screenshots/correctness_tests_output.png`).

## Experimental procedure
For each n and each algorithm:
1. Time the preprocessing (sort / build hash) once.
2. **Best case:** linear → `A[0]`; binary → the exact middle element; hash → a key alone in its bucket.
3. **Average case:** random *existing* keys (1,000 for n ≤ 10⁵; fewer for linear at large n: 1000/1000/200/40 queries for n = 10³…10⁶ so the experiment finishes in reasonable time).
4. **Worst case:** random *absent* keys (unsuccessful search – full scan / full tree depth / full chain).
5. Record exact comparison counts and mean time per search (µs).

Reproduce:
```
cd Task_8_Implementation_Testing/Source_Code
python3 test_correctness.py
python3 benchmark.py                      # ≈ 1 minute
python3 ../../Task_9_Experimental_Performance/make_graphs.py
```
