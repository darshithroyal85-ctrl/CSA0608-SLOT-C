# Task 5 – Asymptotic Analysis (3 marks)

## Notation per algorithm (single search)
| Algorithm | Best | Average | Worst | Tight bound |
|---|---|---|---|---|
| Linear | Ω(1) | Θ(n) | O(n) | Θ(n) for avg/worst; **no single Θ** covers all inputs – the running time is Ω(1) and O(n) |
| Binary (after sort) | Ω(1) | Θ(log n) | O(log n) | Θ(log n) (avg & worst) |
| Hash | Ω(1) | Θ(1) *expected* | O(n) (all keys collide) | Θ(1) expected |

## Preprocessing
| Preprocessing | Notation | Justification |
|---|---|---|
| Sort | Θ(n log n) | merge-sort recurrence T(n) = 2T(n/2) + Θ(n) – Master Theorem case 2 |
| Hash build | Θ(n) | n insertions × Θ(1) |

## Formal checks (definitions)
* Linear avg: (n+1)/2 ≥ n/2 for n ≥ 1 and ≤ n, so c₁ = ½, c₂ = 1, n₀ = 1 ⇒ Θ(n).
* Binary worst: ⌊log₂ n⌋ + 1 ≤ 2 log₂ n for n ≥ 2 and ≥ log₂ n ⇒ Θ(log n).
* Hash expected: 1 + α/2 = 1.375 ≤ 2, a constant ⇒ Θ(1).

## Growth hierarchy
1 ≺ log n ≺ n ≺ n log n:  Hash (1) ≺ Binary (log n) ≺ Linear (n); preprocessing: Hash (n) ≺ Sort (n log n).

## Meaning for 1,000 → 1,000,000 records (×1000)
| Algorithm | Theory: growth factor of comparisons | Interpretation |
|---|---|---|
| Linear | × 1,000 (500 → 500,000) | 1000× more data = 1000× slower; a search that is instantaneous on a department database takes a visible fraction of a second on the university database, and the cost multiplies by the number of requests |
| Binary | × ≈2 (≈10 → ≈20) | Data grows a thousand-fold, work only doubles; each additional factor of 2 in data adds *one* comparison |
| Hash | × 1 | Search cost is flat; but total preprocessing grows ×1000 (Θ(n)) versus ×≈2000 for the sort (n log n) |

For the application: linear search is only viable for tiny tables or one-off searches; both binary and hash scale to 10⁶+ and well beyond (10⁹ records would cost only 30 comparisons for binary search). The asymptotic constants matter only inside a class (e.g. hash is ~5× faster than binary at 10⁶ in practice – Task 10).
