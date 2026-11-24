# Task 7 – Solving the Recurrence (4 marks)

Recurrence from Task 6: **C(n) = C(⌊n/2⌋) + 1, C(1) = 1**   (T(n) = T(⌊n/2⌋) + c in general).

## Method 1 – Backward substitution (iteration), n = 2^k
Chosen because the recurrence has a single, regular recursive term with a constant additive cost: unrolling reveals the pattern directly. We assume n = 2^k (smoothness rule: the result extends to all n).

C(n)   = C(n/2) + 1
       = [C(n/4) + 1] + 1 = C(n/4) + 2
       = C(n/8) + 3
       …
       = C(n/2^i) + i

The base case is reached when n/2^i = 1, i.e. i = k = log₂ n:

C(n) = C(1) + log₂ n = 1 + log₂ n

Hence C(n) = **log₂ n + 1** for n = 2^k, and for general n **⌊log₂ n⌋ + 1** ⇒ **Θ(log n)**.

## Method 2 – Master Theorem (verification)
Form T(n) = a·T(n/b) + f(n) with a = 1, b = 2, f(n) = Θ(1) = Θ(n^d), d = 0.
Applicability: a ≥ 1, b > 1 and f(n) is polynomially bounded – satisfied.
Compare f(n) with n^{log_b a} = n^{log₂ 1} = n⁰ = 1.
f(n) = Θ(1) = Θ(n^{log_b a}) → **Case 2**: T(n) = Θ(n^{log_b a} · log n) = Θ(1·log n) = **Θ(log n)**. ✔ matches substitution.

## Method 3 – Substitution (induction proof of the closed form)
Claim: C(n) = ⌊log₂ n⌋ + 1 for all n ≥ 1.
* Base: C(1) = 1 = ⌊log₂ 1⌋ + 1 ✔
* Step: assume true for all m < n. C(n) = C(⌊n/2⌋) + 1 = ⌊log₂ ⌊n/2⌋⌋ + 1 + 1 = (⌊log₂ n⌋ − 1) + 2 = ⌊log₂ n⌋ + 1 ✔ (using ⌊log₂ ⌊n/2⌋⌋ = ⌊log₂ n⌋ − 1 for n ≥ 2).

## Preprocessing recurrence (merge sort): S(n) = 2S(n/2) + n
a = 2, b = 2, f(n) = Θ(n); n^{log₂2} = n; f(n) = Θ(n) → Master Theorem case 2 → **S(n) = Θ(n log n)**.

## Interpretation
* The result Θ(log n) means that **doubling the database adds only one comparison**: n = 1,000 → 10; 10,000 → 14; 100,000 → 17; 1,000,000 → 20 (confirmed experimentally: worst-case counts 9.97, 13.37, 16.67, 19.95).
* The recursion depth is also ⌊log₂ n⌋ + 1 ≤ 20 for 10⁶ records, so recursion causes **no stack-overflow risk**; space complexity is Θ(log n) for the call stack (the iterative form needs Θ(1)).
* Overall cost with preprocessing: Θ(n log n) + q·Θ(log n).
