# Task 3 – Mathematical Derivation of Time Complexity (6 marks)

Input size: **n** = number of records. Basic operation: key comparison (Task 2). Let C(n) denote the number of comparisons for **one search**, and q the number of searches performed.

---
## 3.1 Linear search
**Worst case** (key in last position, or absent): the loop body executes for i = 0 … n-1:

C_worst(n) = Σ_{i=0}^{n-1} 1 = **n**

**Best case**: key at index 0 → C_best = 1.

**Average case.** Let p be the probability the key is present (successful search) and, if present, equally likely at each of the n positions. A key at position i (1-based) costs i comparisons:

C_avg(n) = p · (1/n) Σ_{i=1}^{n} i + (1-p) · n = p · (n+1)/2 + (1-p) · n

* Successful search only (p = 1): C_avg = (n+1)/2
* Unsuccessful only (p = 0): C_avg = n

Time function: T(n) = c · C(n) → T_worst(n) = c·n, a linear function.
**Preprocessing:** 0. **Total for q searches:** q·(n+1)/2 (avg) … q·n (worst) = Θ(q·n).

---
## 3.2 Binary search (recursive)
Let C(n) count comparisons on a sorted array of n elements. One comparison is made, then at most one recursive call on ≤ ⌊n/2⌋ elements:

C_worst(n) = C_worst(⌊n/2⌋) + 1, C_worst(1) = 1  (derived in Tasks 6–7)

Solution: C_worst(n) = **⌊log₂ n⌋ + 1**.
* n = 1,000 → 10; n = 1,000,000 → 20.

**Best case:** key at the first mid → 1 comparison.

**Average (successful).** Take n = 2^k − 1 so the decision tree is a perfect binary tree of k levels; level i has 2^{i-1} nodes and each costs i comparisons:

C_avg(n) = (1/n) Σ_{i=1}^{k} i·2^{i-1} = ((k−1)·2^k + 1)/n ≈ k − 1 = **log₂(n+1) − 1 ≈ log₂ n − 1**

(using Σ_{i=1}^{k} i·2^{i-1} = (k−1)2^k + 1.) For an unsuccessful search almost every path reaches full depth: C ≈ ⌊log₂ n⌋ + 1.

**Preprocessing (sorting).** A comparison sort needs ≥ ⌈log₂ n!⌉ ≈ n·log₂ n − 1.44 n comparisons; merge sort satisfies M(n) = 2M(n/2) + (n−1), giving M(n) ≤ n·log₂ n − n + 1, i.e. Θ(n log n).

**Total for q searches:** T_total(n, q) = Θ(n log n) + q·Θ(log n) = Θ((n + q) log n).

---
## 3.3 Hash table (separate chaining, load factor α = n/m = 0.75)
**Preprocessing.** Each of the n insertions costs one hash evaluation + one append, a constant: B(n) = n·c₁ → **Θ(n)** expected (the n elements are inserted once; no resizing needed because m is chosen in advance).

**Search.** Under simple uniform hashing each key is equally likely to land in any of the m buckets, so the expected chain length is n/m = α.
* Unsuccessful search: examines the entire chain → E[C] = **α** = 0.75
* Successful search: the sought element is, on average, in the middle of its chain; the expected number of comparisons is 1 + (α/2) − α/(2n) ≈ **1 + α/2 = 1.375**
Both are independent of n ⇒ T_search(n) = **Θ(1)** expected.

**Worst case.** If all n keys collide into one bucket, the chain has length n ⇒ C_worst = n, i.e. O(n). With a good hash this is extremely unlikely (experiment: maximum chain = 7 at n = 1,000,000).

**Total for q searches:** T_total(n, q) = Θ(n) + q·Θ(1) = Θ(n + q).

---
## 3.4 Combined cost (preprocessing + searching)

| Approach | Preprocessing | One search (avg) | q searches |
|---|---|---|---|
| Linear | 0 | (n+1)/2 | Θ(q·n) |
| Binary | Θ(n log n) | ≈ log₂ n − 1 | Θ(n log n + q log n) |
| Hash | Θ(n) | 1 + α/2 | Θ(n + q) |

**Break-even reasoning.** Binary beats linear when n·log₂ n + q·log₂ n < q·n/2, i.e. q > ≈ 2 log₂ n (≈ 40 searches for n = 10⁶ if sorting were as costly as n log n comparisons; measured, see Task 9/12, ≈ 16 searches). Hash beats binary when n + q < n log n + q log n, i.e. for all q at large n in comparison counts, although hash insertion is more expensive *per element* than a sort comparison, so the measured break-even is a few hundred thousand searches (Task 12).
