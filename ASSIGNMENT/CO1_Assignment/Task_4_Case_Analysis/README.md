# Task 4 – Best, Average and Worst-Case Analysis (4 marks)

## Linear search
| Case | Input condition | Operations | Why |
|---|---|---|---|
| Best | key is `A[0]` | 1 | First comparison succeeds; the loop exits immediately |
| Average | key present, uniformly likely at any of n positions | (n+1)/2 | On average the scan covers half the list. Measured: 483,964 at n=10⁶ (theory 500,000.5; the difference is sampling noise of the random keys) |
| Worst | key in last position **or absent** | n | Nothing allows early exit, every element is inspected. Measured: exactly 1,000,000 |

## Binary search
| Case | Input condition | Operations | Why |
|---|---|---|---|
| Best | key equals the middle element of the whole array | 1 | The very first probe succeeds |
| Average | key present, every position equally likely | ≈ log₂ n − 1 | Half of all elements sit at the deepest two levels of the implicit decision tree, so the typical key is found only one level above the bottom. Measured 18.91 at n=10⁶ vs log₂(10⁶) − 1 = 18.93 |
| Worst | key absent (or found at a leaf of the decision tree) | ⌊log₂ n⌋ + 1 | The range is halved until it is empty, so the full depth is traversed. Measured 19.95 vs 20 |

Binary search is *input-insensitive*: the best case (a single specific key) is rare and the average and worst cases differ by ~1 comparison; its performance depends on n only.

## Hash-table search
| Case | Input condition | Operations | Why |
|---|---|---|---|
| Best | key's bucket holds exactly that key (chain length 1), or the bucket is empty for an absent key | 1 (0 for an empty bucket) | No collision |
| Average | uniform hash, load factor α = 0.75 | successful ≈ 1 + α/2 = 1.375 (measured 1.40); unsuccessful ≈ α = 0.75 (measured 0.79) | Chain length is Poisson-like with mean α; an unsuccessful search must scan the whole chain, a successful one on average half of it. About e^{-0.75} ≈ 47% of buckets are empty and cost no comparison at all, which is why misses can be *cheaper* than hits |
| Worst | all keys hash to the same bucket (degenerate / adversarial hash) | n | One chain contains all records and the search degrades to linear search. Not observed: maximum chain was 7 at n=10⁶ |

## Preprocessing cases
* Sort: Θ(n log n) in all cases for merge sort; Timsort (used in the code) is Θ(n) on already-sorted input and Θ(n log n) otherwise – the best case matters if the registration list arrives (mostly) in order.
* Hash build: Θ(n) in all cases (expected); worst case with a bad hash is Θ(n) insertions still – only *searches* degrade.
