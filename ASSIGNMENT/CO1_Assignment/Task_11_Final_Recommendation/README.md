# Task 11 – Final Design Recommendation (4 marks)

## Recommendation (original scenario: "frequent" lookups, update pattern not specified)
**Keep the registration numbers in a sorted array and use binary search** (Approach 2). The preprocessing sort is paid once and amortised across all subsequent searches.

## Evidence and justification
| Criterion | Linear | **Binary (recommended)** | Hash |
|---|---|---|---|
| Preprocessing (n = 10⁶, measured) | 0 | **0.41 s** | 1.88 s |
| Avg. search (n = 10⁶) | 25,864 µs | **4.76 µs** (19 comparisons) | 0.91 µs (1.4 cmp) |
| Worst-case guarantee | n | **⌊log₂ n⌋+1 = 20 – deterministic** | O(n) (never seen, needs a good hash) |
| Extra memory | none | **none (in place)** | ≈ 1.33 n buckets + chain nodes |
| Supports ordered queries (range, "next registration", prefix such as one batch/year) | no | **yes** | no |
| Break-even vs linear | – | **≈ 16 searches** (0.407 s / (25,864 − 4.76) µs) | ≈ 73 searches |

* **Theory:** Θ(n log n) once + Θ(log n) per search – grows by only one comparison per doubling.
* **Experiment:** one sort (0.4 s for 10⁶ records) pays for itself after ≈ 16 searches; after that binary search is ≈ 5,400× faster than scanning.
* **Why not linear:** O(n) per search at 10⁶ records costs 26 ms on average, 65 ms worst – the cost multiplies with the number of requests and grows linearly with the database.
* **Why binary rather than hash in the *general* case:** hash search is ≈ 5× faster in constant factor, but (i) needs 4.6× more preprocessing time here and extra memory, (ii) offers only an *expected* bound, (iii) cannot answer ordered or range queries, and (iv) its extra speed only matters once the number of searches is large (break-even vs binary ≈ 384,000 searches at n = 10⁶). Without knowing the request volume, the sorted array is the most balanced, lowest-risk choice.

## Preprocessing cost
Θ(n log n) comparisons; 0.0002 s (10³), 0.002 s (10⁴), 0.03 s (10⁵), 0.41 s (10⁶). Already-sorted input (registration numbers issued sequentially) is handled in ≈ Θ(n) by Timsort.

## Trade-offs and limitations
* Inserting a new record into a sorted array costs Θ(n) (shifting) – acceptable only if inserts are rare or batched (merge a sorted batch of k new records in Θ(n + k)); if inserts were frequent a balanced search tree / B-tree (Θ(log n) per insert and search) would be needed.
* Requires random access (array) rather than a linked list.
* Recursive implementation uses Θ(log n) stack (≤ 20 frames at 10⁶); an iterative version is 2× faster in CPython.

## Does it stay practical as the database grows?
Yes: 10⁹ records would need only 30 comparisons per search and about 30 × 10⁹ comparisons to sort once. Linear search would need 10⁹ operations per request, which is unworkable.
