# The Collatz–Cascade Bridge

**Structural connections between the Collatz conjecture and the algebraic field ℚ(√2)**

---

## What This Is

A collection of exact algebraic identities and structural observations connecting the Collatz conjecture (3n+1 problem) to the quadratic field ℚ(√2) and its complex extension ℚ(√2, i). This is a **research direction**, not a proof of the conjecture. The identities are proven; the gap to a full proof is honestly documented.

This work emerged from an exploratory framework project investigating the structural role of √2 in number theory. The Collatz connection was discovered through the observation that the geometric mean of the two basic Collatz step ratios lives natively in ℚ(√2).

## Key Results

### Proven Identities

| Identity | Significance |
|---|---|
| √(3/2 · 3/4) = 3/(2√2) ∈ ℚ(√2) | The Collatz geometric mean lives in the cascade's home field |
| 3/2 − √2 = (1 − 1/√2)² | The Collatz growth ratio minus √2 equals the cascade displacement squared |
| 9/8 = 1 + (1/2)³ | The square of the geometric mean equals 1 + Pell defect at depth 3 |
| ln(3) = (3/2)·ln(2) + (1/2)·ln(9/8) | Decomposes ln(3) into cascade-native components |
| Aₙ² − 2Bₙ² = (1/2)ⁿ ≠ 0 ∀n | The generalized Pell defect never vanishes (proven by conjugate identity) |

### Structural Observations (novel, not previously in literature to our knowledge)

1. **The 3/(2√2) bridge**: The geometric mean of the Collatz step ratios 3/2 (growth) and 3/4 (shrinkage) is 3/(2√2) = 3√2/4, placing the Collatz balance point natively in ℚ(√2).

2. **Baker as "transcendental Pell"**: Baker's theorem (lower bounds on linear forms in logarithms, used since the 1970s for Collatz cycle elimination) and the Pell defect (Aₙ² − 2Bₙ² = (1/2)ⁿ) are structurally parallel — both are irrationality consequences saying "approach yes, meet no." We identify them as two readings of the same √2-rooted rigidity.

3. **The √2 connector**: The cascade operator ω = (1+i)/2 generates both π (= 4·arg(ω)) and ln(2) (= −2·ln|ω|). Since 3/(2√2) ∈ ℚ(√2) and |ω| = 1/√2, both the algebraic constraint (Pell) and the transcendental constraint (Baker) on Collatz cycles trace to √2 through ω.

4. **The ln(3) decomposition**: ln(3) = (3/2)·ln(2) + (1/2)·ln(9/8), where ln(9/8) = ln(1 + (1/2)³) is a series in powers of 1/2 — deeply structured by the Pell algebra.

5. **Coherence audit**: Systematic verification of which constraints from ℚ(√2, i) validly pull back to ℤ-Collatz. Result: 8 of 10 components are valid; the complex phase constraint does not apply to the standard integer problem (the trivial cycle {1} has K=2, violating K ≡ 0 mod 8).

### Computational Results

- All 24 convergent families of log₂(3) (the "most dangerous" cycle parameters from continued fraction theory) are eliminated by the current verification bound (2⁶⁸, Barina 2020).
- The hardest family needs only B ≈ 10¹⁵·⁴ — five orders of magnitude below verified bounds.
- The mod-8 halving pattern (a 2-adic constraint on ℤ) independently restricts achievable cycle parameters.

## The Honest Gap

The wall is one sentence: **we have no upper bound on the partial quotients of the continued fraction of log₂(3).**

If a partial quotient far out in the expansion is anomalously large, it creates an anomalously good rational approximation to log₂(3), potentially surviving the death spiral. This is the same wall that blocks all current approaches to Collatz (including Tao 2019, which proves "almost all" orbits descend but not "all").

The framework narrows the gap and provides structural language for attacking it, but does not close it.

## File Structure

```
collatz_cascade_synthesis_2026-05-20.md   — Full write-up (the main document)
collatz_engine.py                         — Computational engine: tiers, Baker bounds, death spiral
collatz_coherence.py                      — Coherence audit: what pulls back from ℚ(√2,i) to ℤ
collatz_deep_analysis.py                  — Convergent growth rates, asymptotic race analysis
README.md                                 — This file
```

## How to Use This

If you work on the Collatz conjecture and find the ℚ(√2) connection interesting, the main things to check are:

1. **Is the 3/(2√2) bridge known?** We haven't found it in the literature, but the Collatz literature is vast. If you know of prior work connecting the Collatz balance to ℚ(√2), please open an issue.

2. **Can the √2 propagation route work?** The chain √2 → ω → ln(2) → Baker connects the algebraic (Pell) and transcendental (Baker) constraints through a single operator. Can Pell rigidity propagate through this chain to give a uniform bound?

3. **Does the 2-adic mod-8 structure, combined with Baker, strengthen cycle elimination?** The halving pattern constrains which (L, K) pairs are achievable. This constraint is independent of Baker and might improve bounds.

## Context

This emerged from an ongoing exploratory project on the structural role of √2, i, and the cascade operator ω = (1+i)/2 in number theory. The project has produced other results (connections to prime gap distributions, the Pell algebra, spectral decompositions) documented separately. The Collatz connection was found on 2026-05-20 through the 3/(2√2) observation.

## License

Public domain. Use freely, cite if useful.
