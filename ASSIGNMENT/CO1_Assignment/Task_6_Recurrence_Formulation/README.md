# Task 6 – Recurrence Relation for the Recursive Approach (3 marks)

Recursive approach: **BinarySearch(A, x, low, high)** (Task 1, Approach 2).

| Component | Identification (from the algorithm) |
|---|---|
| Input size of the original problem | n = high − low + 1 = number of elements still under consideration |
| Size of the recursive subproblem | After computing mid = ⌊(low+high)/2⌋ the algorithm recurses on either `[low, mid−1]` (size ⌊(n−1)/2⌋ = ⌊n/2⌋ − [n even]) or `[mid+1, high]` (size ⌊n/2⌋). In both cases the size is **at most ⌊n/2⌋** |
| Number of recursive calls | **One** – the two branches are mutually exclusive (`if x < A[mid] … else …`); the other half is never examined |
| Work outside the recursive call | Computing `mid` and comparing `x` with `A[mid]` → a constant number of operations: **Θ(1)** (one basic operation) |
| Base case(s) | `low > high` (n = 0): return −1 with no comparison; and n = 1: exactly one comparison then the next calls hit n = 0 |

**Deriving the recurrence.** The time for a problem of size n equals the time for the work done in the current call (constant c) plus the time for the one subproblem of size ⌊n/2⌋:

> **T(n) = T(⌊n/2⌋) + c,  for n > 1,   T(1) = c₀ (T(0) = 0 or constant)**

For comparison counts (worst case, key absent / at deepest level):

> **C(n) = C(⌊n/2⌋) + 1,  C(1) = 1**

**Preprocessing recurrence (merge sort, for completeness).** Sorting makes two recursive calls on halves and merges them with Θ(n) work: S(n) = 2S(⌊n/2⌋) + Θ(n), S(1) = Θ(1).

**Why this is not just a textbook formula.** The coefficient a = 1 (one call) comes from the `if/else` structure, the size ⌊n/2⌋ from the choice of mid, and f(n) = Θ(1) from the fact that the algorithm only compares one element before recursing; changing the algorithm (e.g. ternary split, or scanning half of the range in each call) would change the recurrence.
