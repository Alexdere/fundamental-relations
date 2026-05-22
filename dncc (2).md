# The Definitely Not Collatz Conjecture (DNCC)

*"1 is not a natural number. Let this be my tombstone."*

---

## Preamble

The integer 1 is the multiplicative identity of ℤ. It is neither prime nor composite. The Fundamental Theorem of Arithmetic begins "every integer **greater than 1**..." — the theorem itself kicks 1 out. We exclude it from the operative domain not out of convenience but out of honesty.

Addition on the natural numbers is the projection of a higher-dimensional rotation onto a flattened number line (cf. projective geometry: translations as rotations fixing the point at infinity). The Collatz map, which combines multiplication by 3 with addition of 1 (a disguised rotation), operates on the naturals as a **rotary map** — algebraic rotation composed with 2-adic descent.

---

## Definitions

**The Collatz operator.** T: ℤ_{≥2} → ℤ_{≥1}, defined by T(n) = n/2 if n even, T(n) = 3n+1 if n odd.

**Odd-step operator.** S₁(m) = 3m + 1, for odd m ≥ 3.

**Even-step operator.** S₂(m) = m/2, for even m ≥ 2.

**Odd-to-odd map.** f(m) = (3m+1)/2^{v₂(3m+1)}, the compressed Collatz step between consecutive odd numbers.

---

## The Conjecture

**DNCC (Descent Form):**

> For every integer n ≥ 2, there exists k ≥ 1 such that Tᵏ(n) < n.

Everything falls. No cycles to discuss. Descent cannot cycle.

---

## Equivalence to Classical Collatz

**Theorem.** DNCC ⟺ Standard Collatz Conjecture.

**(⟹)** DNCC gives a strictly decreasing sequence n > n₁ > n₂ > ⋯ in ℤ_{≥1}. By well-ordering, it terminates at 1. ∎

**(⟸)** Every trajectory reaching 1 passes through values < n. ∎

---

## Part I: The Mod 5 Rotation (No Locked Orbits)

### S₁ mod 5

S₁ acts on residues mod 5 as the permutation **(0 → 1 → 4 → 3 → 0)** with **fixed point 2**.

This is because 3 is a primitive root mod 5. The +1 shifts the center of rotation to the solution of 3m+1 ≡ m (mod 5), giving m ≡ 2.

### S₂ mod 5

Division by 2 ≡ multiplication by 3 mod 5: same permutation **(1 → 3 → 4 → 2 → 1)**, fixed point 0.

### Theorem (No Structurally Isolated Cycles)

**At any modular resolution (mod 5 × mod 2ᵏ), the Collatz transition graph is fully connected. No proper subset of states is closed under both S₁ and S₂.**

**Proof.** The S₁ permutation (0 1 4 3) on (ℤ/5ℤ)× is a single 4-cycle. Any S₁-closed subset containing one element of {0,1,3,4} must contain all four. S₁ maps residue 3 → 0, forcing inclusion of residue 0. S₂ applies the same cyclic generator, adding no new closed subsets. At mod 2ᵏ refinement, S₁ remains deterministic and S₂ branches — each even state maps to two possible states — ensuring every state has paths to both odd and even layers. The only closed set is the full state space. ∎

### Exit Ramp Structure

The odd numbers m where 3m+1 = 2ʲ (direct descent to the drain) follow m = (4ˡ − 1)/3 for l ≥ 1:

| l | m | m mod 5 | 3m+1 |
|---|---|---------|------|
| 1 | 1 | 1 | 4 = 2² |
| 2 | 5 | 0 | 16 = 2⁴ |
| 3 | 21 | 1 | 64 = 2⁶ |
| 4 | 85 | 0 | 256 = 2⁸ |
| 5 | 341 | 1 | 1024 = 2¹⁰ |

Exit ramps alternate between residues 0 and 1 mod 5 — the entry arc of the rotation. Residue 2 (the S₁ fixed point) feeds into residue 1 via S₂ (since 2·3 ≡ 1 mod 5). The gravitational flow: eye (res 2) → exit arc (res 0,1) → drain.

---

## Part II: The +1 Perturbation (The Futile Circle)

### The Cycle Equation

A non-trivial cycle visiting L odd numbers m₁, m₂, ..., m_L with division counts k₁, ..., k_L (where kᵢ ≥ 1 is the 2-adic valuation at step i, K = Σkᵢ) requires:

**m₁ = N_L / (2^K − 3^L)**

where the numerator, built entirely from the +1 contributions, is:

**N_L = Σᵢ₌₁ᴸ 3^(L−i) · 2^(Σⱼ₌₁^{i−1} kⱼ)**

Without the +1, the cycle equation becomes 3^L = 2^K, which is impossible by unique factorization. **The +1 is the sole reason cycles are even theoretically possible.** It creates N_L, the accumulated rotational correction, and the entire problem reduces to whether N_L can ever be divisible by 2^K − 3^L.

### Theorem (No 1-Cycles)

**No non-trivial cycle of length L = 1 exists.**

**Proof.** For L = 1: m = 1/(2^k − 3). Positivity requires k ≥ 2. At k = 2: m = 1 (the multiplicative identity — not a natural number under DNCC, and the trivial cycle under classical Collatz). For k ≥ 3: 2^k − 3 ≥ 5, so m = 1/(2^k − 3) < 1. No positive integer solution exists. ∎

### Theorem (No 2-Cycles)

**No non-trivial cycle of length L = 2 exists.**

**Proof.** For L = 2: m = (3 + 2^{k₁}) / (2^K − 9), where K = k₁ + k₂, k₁ ≥ 1, k₂ ≥ 1.

Positivity requires 2^K > 9, so K ≥ 4.

**Case K = 4:** Check all splits.
- k₁=1, k₂=3: (3+2)/7 = 5/7 ∉ ℤ
- k₁=2, k₂=2: (3+4)/7 = 1 (trivial, m=1)
- k₁=3, k₂=1: (3+8)/7 = 11/7 ∉ ℤ

**Case K ≥ 5:** The maximum numerator is 3 + 2^{K−1} (when k₁ = K−1). The denominator is 2^K − 9. For K ≥ 5:

2^K − 9 > 2^{K−1} + 3 ⟺ 2^{K−1} > 12 ⟺ K ≥ 5 ✓

So numerator < denominator, giving m < 1. No positive integer solution. ∎

### The Growth Bound (Why the +1 Circle is Futile)

**Lemma (Direct Lower Bound).** For any non-trivial cycle of length L with total division count K, the smallest cycle element satisfies:

**m ≥ 3^(L−1) / (2^K − 3^L)**

**Proof.** The numerator N_L = Σᵢ₌₁ᴸ 3^(L−i) · 2^(Σⱼ₌₁^{i−1} kⱼ). The i=1 term alone gives 3^(L−1) · 2^0 = 3^(L−1). Since all terms are positive, N_L ≥ 3^(L−1). Therefore m = N_L/(2^K − 3^L) ≥ 3^(L−1)/(2^K − 3^L). ∎

**Why this bound bites.** The continued fraction of log₂3 = [1; 1, 1, 2, 2, 3, 1, 5, 2, 23, ...] generates convergents K/L that minimize 2^K − 3^L. At each convergent, 2^K/3^L ≈ 1 + ε for small ε, so 2^K − 3^L ≈ ε · 3^L. The bound becomes:

**m ≥ 3^(L−1)/(ε · 3^L) = 1/(3ε)**

Since the convergence rate ε shrinks only polynomially in L (bounded by the continued fraction approximation quality), while the bound 1/(3ε) grows, any non-trivial cycle must have astronomically large elements. Computationally verified: no cycles with L ≤ 68 (Simons & de Weger, 2005), no Collatz trajectories failing below 2^68 (Barina, 2020). These are independent results that together kill all small cases.

### Mod 5 Affine Constraint on Cycles

The full odd-to-odd map mod 5 is not a pure rotation — it is an **affine** map. Between odd numbers mᵢ and mᵢ₊₁, the S₁ step (×3, +1) is followed by kᵢ applications of S₂ (×3 mod 5 each). The combined map is:

mᵢ₊₁ ≡ 3^(kᵢ+1) · mᵢ + 3^kᵢ (mod 5)

Composing L such maps, the total multiplicative coefficient is **3^(K+L) mod 5**, and the total translation is an accumulated sum **B** depending on all kᵢ values.

**Lemma (Affine Closure).** For a cycle with L odd steps and total division count K, the cycle closes mod 5 iff:

**(a)** If **4 | (K+L)**: the multiplicative part is trivial (3^(K+L) ≡ 1 mod 5), so the accumulated translation must vanish: **B ≡ 0 mod 5**. This constrains the admissible (k₁,...,k_L) tuples — not all division sequences are compatible.

**(b)** If **4 ∤ (K+L)**: the affine map has **exactly one fixed point** mod 5, given by m ≡ B/(1 − 3^(K+L)) mod 5. The starting odd number is locked to a single residue class.

**Proof.** The composed map is φ(m) ≡ 3^(K+L)·m + B mod 5. Fixed points satisfy (3^(K+L) − 1)·m ≡ −B mod 5. Since 5 is prime and 3 has order 4 mod 5: if 4 | (K+L), the coefficient vanishes and B must be 0; otherwise, 3^(K+L) − 1 is invertible mod 5 and m is uniquely determined. ∎

In both cases, the mod 5 structure eliminates candidate cycles: case (a) kills division sequences where B ≢ 0, and case (b) restricts the starting residue to one of five classes. The trivial cycle (L=1, K=2, K+L=3) falls under case (b): the unique fixed point is m ≡ 1 mod 5, matching m=1. ✓

---

## Part III: The Wall

Everything above is proven. What remains is a single, precisely defined claim:

### The Wall (Exact Statement)

**For all integers L ≥ 1 and all tuples (k₁, ..., k_L) with each kᵢ ≥ 1 and K = Σkᵢ > L·log₂3:**

**The quantity N_L / (2^K − 3^L) is never a positive integer, where N_L = Σᵢ₌₁ᴸ 3^{L−i} · 2^{Σⱼ₌₁^{i−1} kⱼ}.**

This is the wall. Not "do all numbers reach 1." Not "are there cycles." Just: **this specific rational number is never an integer.**

### What We Know About the Wall

**From below (computation):** Verified for all L ≤ 68. No solution exists.

**From above (growth bound):** m grows exponentially with L, so any cycle lives at astronomically large numbers. But "astronomically large" ≠ "impossible."

**From the mod 5 rotation:** The numerator N_L carries mod 5 structure inherited from the rotation. The denominator 2^K − 3^L has mod 5 value determined by K+L mod 4 (since 5 | (2^K − 3^L) iff 4 | (K+L)). When 5 divides the denominator, 5 must also divide N_L. This constrains which (k₁,...,k_L) tuples are even candidates.

**From the continued fraction:** The convergents of log₂3 determine the "narrowest gaps" — the (K,L) pairs where 2^K − 3^L is smallest. These are the critical cases. The wall reduces to showing that N_L misses these gaps at every convergent.

### What Would Break the Wall

To prove DNCC, one must show **one** of the following:

**(A) Divisibility obstruction:** N_L mod p ≠ 0 mod (2^K − 3^L) for some prime p, at every (K,L). The mod 5 rotation provides partial obstructions. A complete obstruction from a single prime (or finite set of primes) would suffice.

**(B) Growth domination:** A proof that N_L/(2^K − 3^L) is always either < 1 or non-integer. The growth bound nearly achieves this — it shows the ratio → ∞, meaning any cycle element must be huge, but "huge" and "nonexistent" are different claims.

**(C) 2-adic rigidity:** A proof that the 2-adic valuation structure of N_L is incompatible with the 2-adic structure of 2^K − 3^L for all (k₁,...,k_L). This would use the "gearing" framework — showing the mod 5 rotation and the 2-adic descent are permanently incommensurate.

**(D) Ergodic/measure-theoretic:** Following Tao (2019), strengthen "almost all trajectories descend" to "all trajectories descend." The gap between measure-zero and empty is the gap between Tao's result and DNCC.

---

## Status

| Component | Status |
|-----------|--------|
| Descent ⟺ Collatz equivalence | **Proven** ✓ |
| No structurally isolated cycles (mod 5 × mod 2ᵏ) | **Proven** ✓ |
| No 1-cycles | **Proven** ✓ |
| No 2-cycles | **Proven** ✓ |
| No L-cycles for L ≤ 68 | **Proven** (Simons–de Weger 2005) |
| No trajectories failing below 2^68 | **Proven** (Barina 2020) |
| Mod 5 affine constraint on cycle parameters | **Proven** ✓ |
| +1 perturbation lower bound: m ≥ 3^(L−1)/(2^K − 3^L) | **Proven** ✓ |
| N_L/(2^K − 3^L) ∉ ℤ⁺ for all L | **THE WALL** |

---

*Filed under: Definitely Not Collatz. The +1 rotates in its futile circle. The numbers fall. The wall stands — thin, rigid, precisely defined, and awaiting the hammer that is definitely not a proof of any existing conjecture.*
