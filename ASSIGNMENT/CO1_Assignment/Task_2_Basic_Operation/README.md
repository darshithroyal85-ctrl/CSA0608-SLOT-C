# Task 2 – Identify the Basic Operation (2 marks)

A basic operation is the operation executed most often *and* whose count is proportional to total running time. In every search algorithm the work is dominated by **key comparisons** – each comparison is followed by a constant amount of bookkeeping (index update, branch), so total time = (number of comparisons) × constant.

| Algorithm | Basic operation | Where it occurs | How its count grows with n |
|---|---|---|---|
| Linear | `A[i] = x` | Inside the `for` loop body, once per iteration | Up to n times; the loop runs until the key is found, so the count depends directly on the key's position – grows **linearly** with n |
| Binary (recursive) | `A[mid] = x` (3-way comparison of the key with the middle element) | Once per recursive call | Each call halves the range, so the number of calls (= comparisons) is ⌊log₂ n⌋ + 1 at most – grows **logarithmically**: 1,000 → ≈10, 1,000,000 → ≈20 |
| Hash | `key = x` (stored key vs. search key) | Inside the loop that walks the chain of one bucket | The chain length is the load factor α = n/m (a constant, 0.75) on average, *not* a function of n – grows **not at all** (expected) |

**Why comparisons are appropriate.**
* Every algorithm must perform them to decide membership; they cannot be skipped.
* They are machine-independent, so the count can be derived mathematically (Task 3) and measured exactly (Task 9) and compared against wall-clock time (Task 10).
* For the hash approach the hash computation `h(x)` is a constant-cost step done once per search, so it does not alter the growth rate; the chain comparisons capture the only part that could depend on n (through collisions).
* For binary search the sort used in preprocessing is also a comparison sort, so comparisons remain the right unit to charge for preprocessing; for hash preprocessing the basic operation is the *insertion* (one hash + one append).
