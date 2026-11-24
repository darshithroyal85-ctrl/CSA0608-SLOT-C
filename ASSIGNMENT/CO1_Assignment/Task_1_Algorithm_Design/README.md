# Task 1 – Algorithm Design (5 marks)

**Problem.** Given a collection of *n* unique registration numbers (10-digit integers, e.g. `2021345678`), decide whether a key *x* exists and return its position. *n* ∈ {1,000; 10,000; 100,000; 1,000,000+}. Preprocessing time is charged to each algorithm.

Three algorithms from three different **design paradigms** were chosen (iterative vs. recursive versions of the same idea are *not* counted as separate approaches):

| # | Approach | Design strategy | Style | Preprocessing |
|---|----------|-----------------|-------|---------------|
| 1 | Sequential (linear) search | **Brute force** | Iterative | None |
| 2 | Binary search | **Decrease-and-conquer** (divide by half, solve one half) | Recursive | Sort the records – Θ(n log n) |
| 3 | Hash-table search (separate chaining) | **Transform-and-conquer / space–time trade-off** | Iterative (chain walk) | Build the table – Θ(n) expected |

---
## Approach 1 – Sequential (Linear) Search
**Idea.** Compare *x* with every record, left to right, until a match or the end of the list.
**Why selected.** It is the natural baseline: zero preprocessing, works on unsorted data, trivially correct. It shows what the other strategies must beat and when they are *not* worth their preprocessing cost (very few searches).

```
ALGORITHM LinearSearch(A[0..n-1], x)
    for i ← 0 to n-1 do
        if A[i] = x then return i          // basic operation
    return -1
```

## Approach 2 – Binary Search (recursive)
**Idea.** If the array is sorted, compare *x* with the middle element. Equal → done; smaller → the key can only be in the left half; larger → right half. Each comparison discards half of the remaining candidates.
**Preprocessing.** Sort the registration numbers once (Timsort/merge-sort family, Θ(n log n) comparisons).
**Why selected.** It exploits an *ordering property* that the problem offers for free (registration numbers are totally ordered integers); it is the standard decrease-and-conquer example and gives a recurrence to be formulated and solved (Tasks 6–7).

```
ALGORITHM Preprocess(A[0..n-1])           // once
    sort A ascending                       // Θ(n log n)

ALGORITHM BinarySearch(A, x, low, high)    // initial call: (A, x, 0, n-1)
    if low > high then return -1           // base case: empty range
    mid ← ⌊(low + high) / 2⌋
    if A[mid] = x then return mid          // basic operation
    if x < A[mid] then return BinarySearch(A, x, low, mid-1)
    else               return BinarySearch(A, x, mid+1, high)
```

## Approach 3 – Hash-Table Search (separate chaining)
**Idea.** Instead of *searching*, *compute* where the key must be: `h(x) = ⌊m · frac(x·φ)⌋` (multiplicative / Fibonacci hashing) maps the key to one of *m* buckets; only the short list in that bucket is examined. With *m = n / 0.75* the load factor is α = 0.75.
**Preprocessing.** Insert all *n* records into the table: n × O(1) = Θ(n) expected.
**Why selected.** It trades memory (≈ 1.33 n bucket slots) for speed, giving expected O(1) lookups independent of *n* – the fundamentally different "index structure" strategy, and a serious candidate for a read-heavy system (Task 12).

```
ALGORITHM BuildIndex(A[0..n-1])            // once
    m ← ⌈n / 0.75⌉ ; create m empty lists
    for i ← 0 to n-1 do
        append (A[i], i) to bucket[h(A[i])]        // O(1) each

ALGORITHM HashSearch(x)
    b ← h(x)
    for each (key, pos) in bucket[b] do
        if key = x then return pos         // basic operation
    return -1
```

## Preprocessing summary
| Approach | Preprocessing | Extra memory |
|---|---|---|
| Linear | none | O(1) |
| Binary | sort, Θ(n log n) | O(1) extra (in place) / O(n) if copy |
| Hash | build, Θ(n) expected | Θ(n) (≈1.33 n buckets) |

Implementation: `Task_8_Implementation_Testing/Source_Code/algorithms.py`.
