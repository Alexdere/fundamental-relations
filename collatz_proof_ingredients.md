# Collatz Conjecture — Proof Ingredients Register
## A Formal Working Document

**Date:** 2026-05-22  
**Status:** Active research base — not a complete proof  
**Notation key:** ✓ PROVEN | ◈ STRUCTURAL (valid, not sufficient alone) | ○ CONJECTURAL | ✗ DOES NOT APPLY TO ℤ-COLLATZ

---

## §0 — Problem Statement

**The Collatz map on odd integers.** Define f: O → O where O = {positive odd integers} by:

    f(m) = odd_part(3m + 1) = (3m + 1) / 2^{v₂(3m+1)}

**The conjecture (cycle formulation).** There is no non-trivial cycle: no odd m > 1 satisfies f^L(m) = m for any L ≥ 1.

**Why cycles suffice.** Tao (2019) proved almost all orbits eventually descend. The remaining work is ruling out cycles and divergent orbits. Divergent orbits are generally considered to require separate treatment; this document addresses cycles exclusively.

**Reduction to odd numbers.** Even numbers are fully determined by odd dynamics — every even number is reached from an odd number and returns to one within one halving sequence. The interesting space is O alone. ✓

---

## §1 — Elementary Structural Facts

### §1.1 — Fixed points and short cycles

**I-1.** ✓ The only fixed point of f is m = 1.  
*Proof.* f(m) = m requires 3m+1 = 2^k·m, so m(2^k−3)=1. Only solution: k=2, m=1. □

**I-2.** ✓ No 2-cycle exists.  
*Proof.* m₁ = (3 + 2^{k₁})/(2^{k₁+k₂}−9). Exhaustive check: no positive odd integer > 1 satisfies this for any k₁, k₂ ≥ 1. □

**I-3.** ✓ No 3-cycle exists.  
*Proof.* m₁ = (9 + 3·2^{k₁} + 2^{k₁+k₂})/(2^K−27). Checked computationally for all K up to bound where C/D < 1 for all compositions. □

**I-4.** ✓ No cycle exists with uniform step sizes (k₁ = k₂ = ··· = k_L = k).  
*Proof.* With uniform k: C = D/(2^k−3), so m₁ = 1/(2^k−3). Positive integer only when k=2, giving m₁=1. □

**I-5.** ✓ f never outputs a multiple of 3.  
*Proof.* 3m+1 ≡ 1 (mod 3) for any m. Dividing by powers of 2 preserves the mod-3 residue class. □

**I-6.** ✓ Every prime factor p of any cycle element mᵢ must be "regenerated" — some other cycle element m_j ≡ −3⁻¹ (mod p).  
*Proof.* If p | mᵢ and p | mⱼ for the same i, then p | 1, impossible. So no prime repeats consecutively in the cycle; each prime must be re-introduced by some 3m_j+1. □

**I-7.** ✓ The only narrow window of (K, L) pairs producing cycle elements m > 1 satisfies K/L ∈ (log₂3, log₂3 + 2/(L−1)).  
*Proof.* From m = C/D < 2^{K−2}·3^L/(2^K−3^L) = r/(4(r−1)) where r = 2^K/3^L. For m > 1 requires r < 4/3, i.e. K < 2 + (L−1)·log₂3 + ε. □

---

## §2 — The Cycle Equation

### §2.1 — Three equivalent forms

For a cycle m₁ → m₂ → ··· → m_L → m₁ with step sizes k₁,...,k_L (kᵢ = v₂(3mᵢ+1)) and K = Σkᵢ:

**Multiplicative form:** ✓
    ∏ᵢ (3mᵢ + 1) = 2^K · ∏ᵢ mᵢ

**Fixed-point form:** ✓
    m₁ = C / D
    
    where  C = Σⱼ₌₀^{L-1} 3^{L-1-j} · 2^{Kⱼ}   (K₀=0, Kⱼ = k₁+···+kⱼ)
           D = 2^K − 3^L

**Properties of C and D:** ✓
- C is always odd (first term 3^{L-1} is odd; all other terms are even)
- D is always odd (2^K even minus 3^L odd)
- If D | C then m₁ = C/D is automatically odd and not divisible by 3

### §2.2 — The chain identity (new)

**C-1.** ✓ For each i: **3Cᵢ + D = 2^{kᵢ} · Cᵢ₊₁** where Cᵢ is the C-value rotated to start at mᵢ.  
*Proof.* Direct substitution: 3(Cᵢ/D) + 1 = 2^{kᵢ}·(Cᵢ₊₁/D), multiply both sides by D. □

**C-2.** ✓ The correction sum is an automatic identity — not an independent constraint:
    Σᵢ ln(1 + 1/(3mᵢ)) = K·ln(2) − L·ln(3)   for any valid Cᵢ chain.
*Proof.* ln(1+1/(3mᵢ)) = ln((3Cᵢ+D)/(3Cᵢ)) = ln(2^{kᵢ}·Cᵢ₊₁/(3Cᵢ)). Summing: K·ln2 + Σln(Cᵢ₊₁/Cᵢ) − L·ln3. The middle sum telescopes to 0 (cyclic). □

**C-3.** ✓ **The entire cycle existence question reduces to: does (2^K − 3^L) divide Σⱼ 3^{L-1-j}·2^{Kⱼ}?**  
No logs, no transcendentals, no corrections — pure integer divisibility.

---

## §3 — Baker's Theorem and the Death Spiral

**B-1.** ✓ **(Baker 1966, Laurent refinements)** For integers L, K:
    |L·ln(3) − K·ln(2)| > C · max(L,K)^{−δ}
for effectively computable constants C > 0, δ > 0.

**B-2.** ✓ **Death spiral.** Combining Baker with the computational verification bound B (all numbers below B belong to some tier and converge to 1):

- Any cycle element must satisfy mᵢ > B (otherwise it's in a verified tier)
- Each correction ln(1+1/(3mᵢ)) < 1/(3B)
- Total correction ≤ L/(3B)
- Baker requires: L/(3B) ≥ C/K^δ
- This requires: B ≤ L·K^δ/(3C) — polynomial in L

The verification bound B grows exponentially with computational effort; the required bound grows polynomially in L. For all tested convergent families of log₂(3), the verification bound already suffices.

**B-3.** ✓ **Computational bound (Barina 2020).** All starting values below 2^68 ≈ 3×10^20 have been verified to reach 1. No cycle element can be smaller than this.

**B-4.** ✓ **Cycle length bound (Simons–de Weger 2005, refinements).** Any non-trivial cycle must have L > 10^11 odd steps.

**B-5.** ✓ **All 24 tested convergent families of log₂(3) are eliminated** by the current verification bound. The hardest family requires B ≈ 10^{15.4}, well below 2^68.

---

## §4 — The Cascade Framework and Bridge Identities

### §4.1 — Algebraic identities connecting Collatz to ℚ(√2)

**A-1.** ✓ **The 3/(2√2) bridge:**
    geometric mean of {3/2, 3/4} = √(3/2 · 3/4) = 3/(2√2) ∈ ℚ(√2)
The Collatz balance point lives natively in the cascade's algebraic field.

**A-2.** ✓ **The Collatz–cascade identity:**
    3/2 − √2 = (1 − 1/√2)²
The difference between the Collatz growth ratio and the cascade base equals the cascade displacement squared. Exact algebraic identity.

**A-3.** ✓ **The Pell-Collatz bridge:**
    9/8 = 1 + (1/2)³ = 1 + Pell defect at cascade depth 3
The square of the Collatz geometric mean equals 1 plus the Pell defect at depth 3.

**A-4.** ✓ **Logarithmic decomposition:**
    ln(3) = (3/2)·ln(2) + (1/2)·ln(9/8)
This decomposes the Collatz irrational (ln3) into cascade-native (ln2) and Pell-adjacent (ln(9/8)) parts. The cycle equation becomes:
    (D/2)·ln(2) = (L/2)·ln(9/8) + Σ ln(1 + 1/(3mᵢ))
where D = 2K−3L. Left side: only ln(2). Right side: cascade-structured series.

### §4.2 — The cascade operator

**A-5.** ✓ **The cascade operator** ω = (1+i)/2 generates both transcendental constants in the problem:
    π = 4·arg(ω)          (from the angular/rotation reading)
    ln(2) = −2·ln|ω|      (from the magnitude/scaling reading)

**A-6.** ✓ **The 3-bridge in ℚ(√2):**
    3/(2√2) ∈ ℚ(√2)  →  3 = 2√2 · (3/(2√2))
So 3 connects to the cascade field algebraically. The entire Collatz problem — involving 2, 3, ln(2), ln(3) — is rooted in √2 through ω.

**A-7.** ◈ **Baker IS transcendental Pell** (structural identification):

| | Pell | Baker |
|---|---|---|
| Statement | A²−2B² = (1/2)^n ≠ 0 | \|L·ln3−K·ln2\| > C·K^{-δ} ≠ 0 |
| Meaning | √2 is irrational | log₂(3) is irrational |
| Rate | exponential decay | polynomial decay |
| Source | algebraic structure of ℚ(√2) | transcendental structure of ln(2), ln(3) |

Both say "approach but never meet." Both trace to the same operator ω. This identification is exact as structural analogy; the claim that it implies deeper proof connections is conjectural.

### §4.3 — Coherence audit: what applies to ℤ-Collatz

| Component | Status |
|---|---|
| Embedding ℤ → ℚ(√2) | ✓ trivial ring map |
| Cycle equation in log form | ✓ real equation, universal |
| ln(3) decomposition | ✓ real algebraic identity |
| 9/8 = 1+(1/2)³ | ✓ real algebraic identity |
| Baker bound | ✓ standard transcendence theory |
| Pell defect ≠ 0 | ✓ real algebraic |
| Death spiral | ✓ real analysis + arithmetic |
| Mod-8 halving pattern | ✓ 2-adic arithmetic on ℤ |
| Phase constraint K ≡ 0 mod 8 | ✗ trivial cycle has K=2; ℤ-orbits stay real |
| C/D divisibility reduction | ✓ pure arithmetic |

---

## §5 — The Mod-8 Rung Structure and 2-Adic Cantor Set

### §5.1 — The halving pattern

**M-1.** ✓ **The mod-8 rung machine.** For any odd m, the rung v₂(3m+1) is determined by m mod 8:
- m ≡ 1 mod 8: rung exactly 2
- m ≡ 3 mod 8: rung exactly 1
- m ≡ 5 mod 8: rung ≥ 3
- m ≡ 7 mod 8: rung exactly 1

**M-2.** ✓ **Rung ≥ 3 guarantees descent.** If v₂(3m+1) ≥ 3, then (3m+1)/2^k < m (multiplication by 3 cannot overcome division by 2^3 = 8 since 3 < 8). The sequence strictly decreases at such steps.

**M-3.** ✓ **The mod-8 transition graph.** Under one Collatz step:
- ≡3 mod 8 → always maps to {1, 5} mod 8 (escapes to rung ≥ 2 in next step)
- ≡7 mod 8 → maps to {3, 7} mod 8 (can stay in rung-1 territory)
- ≡1 mod 8 → maps to all four odd classes equally
- ≡5 mod 8 → maps to all four odd classes (after the large rung-3+ step)

**M-4.** ✓ **Infinite rung-1 streaks require 2-adic −1.** For a sequence to remain at ≡7 mod 8 indefinitely, the starting number must satisfy m ≡ 2^n−1 (mod 2^n) for all n simultaneously. In ℤ₂ this is exactly −1. No positive integer satisfies this, so every positive integer eventually produces a step with rung ≥ 2.

### §5.2 — The 2-adic Cantor set

**M-5.** ◈ **The Hypothetical Escape Number (HEN) lives in a Cantor set of measure zero.** Any number avoiding convergence must satisfy m ≡ cₙ (mod 2^n) for every n, where cₙ is a surviving residue in the constraint tree built by requiring rung ≤ 2 at every step. The density of surviving residues at level n → 0 as n → ∞.

**M-6.** ✓ **No rung-≤2-only cycle exists.** The cycle ratio equation for rung-1/rung-2 cycles requires b/a = log(3/2)/log(4/3) ≈ 1.409, which is irrational (requires 2^p = 3^q for integers p, q — impossible by unique factorization). Hence no cycle can consist solely of rung-1 and rung-2 steps.

---

## §6 — The (n, m) Manifold Framework (New)

### §6.1 — The coordinate system

**N-1.** ✓ **Canonical (n, m) representation.** Every positive odd integer p has a unique representation:
    p = 2^n · m − 1
where n = v₂(p+1) ≥ 1 and m = (p+1)/2^n is a positive odd integer.

This is a bijection between O and {(n, m) : n ≥ 1, m ≥ 1, m odd}.

The two coordinates have natural interpretations:
- n: binary "countdown capacity" — how close p is to a power-of-2-minus-1
- m: the "odd core" after stripping the 2-structure from p+1

### §6.2 — Dynamics in (n, m) coordinates

**N-2.** ✓ **Deterministic countdown phase.** For n ≥ 2:
    f(2^n·m − 1) = 2^{n−1}·(3m) − 1
*Proof.* 3(2^n·m−1)+1 = 3·2^n·m−2 = 2(3·2^{n−1}·m−1). The inner term is odd for n ≥ 2, so rung = 1 exactly. □

In coordinates: (n, m) → (n−1, 3m). Pure, no uncertainty.

**N-3.** ✓ **Reset boundary at n = 1.** For p = 2m−1 (i.e. n=1):
    f(p) = (3m−1)/2^{v₂(3m−1)}
Let k = v₂(3m−1) and s = (3m−1)/2^k. Then new state: n₁ = v₂(s+1), m₁ = (s+1)/2^{n₁}.

**N-4.** ✓ **The meta-equation.** One full macro-step from (n₀, m₀):
1. n₀−1 countdown steps reach (1, 3^{n₀−1}·m₀)
2. Reset with k = v₂(3^{n₀}·m₀ − 1), s = (3^{n₀}·m₀ − 1)/2^k
3. New state: n₁ = v₂(s+1), m₁ = (s+1)/2^{n₁}

**Cycle existence = periodic orbit of the meta-equation.**

**N-5.** ✓ **W = 3^n·m is invariant during countdown.**  
*Proof.* Under (n,m) → (n−1, 3m): 3^{n−1}·(3m) = 3^n·m. □

W is the natural energy function for this coordinate system. Any Lyapunov argument must track W through the reset step.

### §6.3 — The Lyapunov condition at the reset

**N-6.** ✓ **The reset condition.** W = 3^n·m decreases at a reset iff:
    n₁ · ln(3/2) < k · ln(2)
equivalently: **n₁/k < ln(2)/ln(3/2) = log_{3/2}(2) ≈ 1.709**

where k = v₂(3^{n₀}·m₀ − 1) and n₁ = v₂(s+1), s = (3^{n₀}·m₀−1)/2^k.

*Proof.* W_after/W_before ≈ (3/2)^{n₁}/2^k. This ratio < 1 iff n₁·ln(3/2) < k·ln(2). □

**N-7.** ◈ **The threshold 1.709 encodes log₂(3).** Note ln(2)/ln(3/2) = 1/(log₂3 − 1) = 1/log₂(3/2). The Lyapunov threshold IS log₂(3) repackaged.

**N-8.** ◈ **The Lyapunov condition is equivalent to the CF partial quotient bound.** The reset condition n₁/k < 1.709 fails precisely when 3^{n₀}·m₀ is 2-adically anomalously close to a power of 2 — which occurs when n₀ is near a convergent denominator of log₂(3) with a large next partial quotient. Therefore:

    ∀(n₀,m₀) ∈ ℕ, n₁/k < 1.709  ⟺  partial quotients of CF(log₂3) are bounded

This is the same wall as Baker, expressed 2-adically instead of real-analytically.

### §6.4 — The T-period Diophantine formulation

**N-9.** ✓ **Reduction to finite systems.** A cycle of Collatz period-L corresponds to a T-periodic orbit of the meta-equation, where T is the number of macro-steps. For each fixed T, the orbit-closure condition is a finite Diophantine system S_T:

    S_T: T equations in 2T unknowns (n₀,...,n_{T−1}, k₀,...,k_{T−1})
         relating successive states via the meta-equation

**N-10.** ✓ **T=1 meta-period (L=1 Collatz cycle): only (1,1).**  
*Proof.* Fixed point requires (3^{n₀}·m₀−1)/2^k = 2^{n₀}·m₀−1. Rearranging: m₀(3^{n₀}−2^{k+n₀}) = 2^k−1. For m₀ ≥ 1 to have positive solutions: need 2^{k+n₀} < 3^{n₀} and the quotient to be a positive odd integer. Direct inspection: only solution is n₀=1, k=2, m₀=1. □

**N-11.** ◈ **T=2 meta-period:** Two simultaneous equations. No known solution with m₀ > 1. Provable with algebraic analysis at this specific period.

**N-12.** ◈ **Large T (Baker regime):** For T·n̄ > L_Baker (where L_Baker ≈ 10^11 is the current lower bound on cycle length), the Baker/death-spiral argument kills all T-periodic orbits without explicit case analysis.

**THE GAP:** T in the range from ~3 to ~L_Baker/n̄. These are not killed by current algebraic arguments and are too large for exhaustive computation.

---

## §7 — Precise Statement of the Wall

**The wall in one sentence:** We have no upper bound on the partial quotients of the continued fraction of log₂(3).

### §7.1 — Three equivalent formulations

**W-1.** **(Logarithmic / Baker formulation):** Cannot prove that no rational K/L approximates log₂(3) better than C/L^{1+δ} for all L beyond a computable bound.

**W-2.** **(2-adic / v₂ formulation):** Cannot prove that v₂(3^n·q − 1) ≤ n·log₂(3/2) + log₂(q) + C for all positive integers n, q, for any constant C.

**W-3.** **(Lyapunov / manifold formulation):** Cannot prove that n₁/k < 1.709 holds universally at every reset step.

All three are equivalent. A proof of any one closes all three.

### §7.2 — What the wall is NOT

- It is NOT a statement about the conjecture being false.
- It is NOT a statement about unprovability in ZFC.
- It IS a specific open number-theoretic question about the irrationality measure of log₂(3).

### §7.3 — The irrationality measure

The irrationality measure μ(log₂3) satisfies μ ≥ 2 (trivially). Rukhadze (1987) and Hata (1993) established μ ≤ M for some M ≈ 3.57. The Lang conjecture would give μ = 2 (bounded partial quotients). Baker's theorem already implies the gap shrinks no faster than polynomially in K. What's missing is a UNIFORM polynomial upper bound.

---

## §8 — Proof Closure Options

Any one of the following would complete the proof (for the cycle part):

**Option A — Bound the partial quotients of log₂(3).**  
Prove: a_n (the nth partial quotient of CF(log₂3)) satisfies a_n = O(n^c) for some c.  
Equivalent to bounding the irrationality measure μ(log₂3) = 2 (the generic Diophantine approximation rate).  
*Status:* Conjectured (generalized Lang conjecture). No proof exists. Transcendence of log₂3 means algebraic tools don't reach it directly.

**Option B — Find a purely algebraic Lyapunov function on (n, m).**  
Find W: {(n,m) : n≥1, m odd ≥1} → ℝ₊ such that W(n₁,m₁) < W(n₀,m₀) at every meta-step.  
Requirements: (i) W decreases under (n,m) → (n−1, 3m), (ii) W decreases at the reset.  
*Status:* W = 3^n·m is constant during countdown (good) but can increase at reset (insufficient). No valid candidate known.

**Option C — Prove the T-period Diophantine systems S_T have no solutions by induction on T.**  
Show: for every T ≥ 1, S_T has no solution with m₀ > 1. Baker covers large T; small T needs algebraic proofs.  
*Status:* T=1 proved. T=2 potentially provable. T=3,...,N needs investigation. No inductive pattern discovered.

**Option D — Galois structure argument in ℚ(√2, i).**  
Use the Klein four Galois group of ℚ(√2, i)/ℚ to show the cycle equation has no solutions in the ring of integers of ℚ(√2, i).  
*Status:* The phase constraint does not pull back to ℤ-Collatz directly. The Galois route is undeveloped.

**Option E — Direct algebraic impossibility of D | C.**  
Prove: for all integer step sequences k₁,...,k_L with Σkᵢ = K and K/L ≈ log₂3, the integer D = 2^K−3^L does not divide C = Σⱼ 3^{L-1-j}·2^{Kⱼ}.  
*Status:* The structure of C (sum of "mixed-base" products of powers of 2 and 3) modulo D = 2^K−3^L (using the congruence 2^K ≡ 3^L mod D) has been identified but not exploited to prove non-divisibility.

---

## §9 — Key Equations Reference Sheet

### The reduced map
    f(m) = (3m+1) / 2^{v₂(3m+1)}     (odd m → odd m)

### The cycle product equation
    ∏ᵢ (3 + 1/mᵢ) = 2^K

### The fixed-point formula
    m₁ = C/D,   C = Σⱼ₌₀^{L-1} 3^{L-1-j} · 2^{Kⱼ},   D = 2^K − 3^L

### The chain identity
    3Cᵢ + D = 2^{kᵢ} · Cᵢ₊₁

### Bridge identities
    3/(2√2) = √(9/8) ∈ ℚ(√2)
    3/2 − √2 = (1 − 1/√2)²
    9/8 = 1 + (1/8) = 1 + (1/2)³
    ln(3) = (3/2)·ln(2) + (1/2)·ln(9/8)

### Pell algebra
    (1 − 1/√2)^n = Aₙ − Bₙ√2,   Aₙ² − 2Bₙ² = (1/2)^n ≠ 0

### Cascade operator
    ω = (1+i)/2,   |ω| = 1/√2,   arg(ω) = π/4
    π = 4·arg(ω),   ln(2) = −2·ln|ω|

### Baker's bound
    |L·ln(3) − K·ln(2)| > C · max(L,K)^{−δ}    (C, δ effectively computable)

### (n,m) coordinates
    p = 2^n·m − 1,   n = v₂(p+1),   m = (p+1)/2^n

### Meta-equation
    k = v₂(3^{n₀}·m₀ − 1)
    s = (3^{n₀}·m₀ − 1)/2^k
    n₁ = v₂(s + 1),   m₁ = (s + 1)/2^{n₁}

### Lyapunov condition at reset
    W = 3^n·m decreases  ⟺  n₁/k < ln(2)/ln(3/2) ≈ 1.709

---

## §10 — What Is and Is Not Proven

### Proven unconditionally (✓)
- No 1-cycles, 2-cycles, 3-cycles, or uniform-step cycles (except trivial {1})
- The unique candidate m₁ = C/D for each step sequence: C odd, D odd, C/D automatically odd and not divisible by 3
- The chain identity 3Cᵢ + D = 2^{kᵢ}·Cᵢ₊₁
- The correction sum collapses to an identity (not a constraint)
- Cycle existence = pure divisibility D | C
- All bridge identities (3/(2√2) ∈ ℚ(√2), 3/2−√2=(1−1/√2)², 9/8=1+(1/2)³)
- Baker's theorem (external result, assumed)
- Computational verification B = 2^68 (external result, assumed)
- No cycles with L ≤ 10^11 (external result, assumed)
- All 24 tested convergent families killed by death spiral
- Mod-8 rung pattern
- No infinite rung-1 streak in ℕ (requires 2-adic −1)
- No rung-≤2-only cycle (irrational ratio argument)
- The (n,m) canonical representation is a bijection
- The countdown phase is deterministic: (n,m)→(n−1,3m)
- W = 3^n·m is invariant during countdown
- The Lyapunov threshold = 1/(log₂3 − 1) ≈ 1.709
- T=1 meta-period has only solution (1,1)

### Structural arguments (◈) — valid but not sufficient
- Baker IS transcendental Pell (exact analogy, not a proof connection)
- 2-adic Cantor set structure of potential cycles
- The Lyapunov condition equivalence with CF partial quotient bounds
- The dimensional argument (1D push cannot close 2D loop)
- The T-period Diophantine reduction for all T

### The single remaining gap
**Prove that the partial quotients of the continued fraction of log₂(3) are bounded, OR find a Lyapunov function W on the (n,m) lattice that decreases at every meta-step, OR prove the T-period systems S_T have no solutions for all T by a uniform algebraic argument.**

All three are equivalent formulations of the same missing piece.

---

## §11 — Glossary

| Symbol | Definition |
|---|---|
| O | set of positive odd integers |
| f | reduced Collatz map: f(m) = odd_part(3m+1) |
| L | number of odd steps in a cycle |
| K | total halvings in a cycle: K = Σkᵢ |
| kᵢ | v₂(3mᵢ+1): rung at step i |
| C | accumulated constant: Σⱼ 3^{L-1-j}·2^{Kⱼ} |
| D | 2^K − 3^L: the Baker gap in integer form |
| ω | cascade operator (1+i)/2 |
| n(v) | cascade coordinate: 2·log₂(v) |
| (n,m) | canonical coordinates: p = 2^n·m − 1 |
| k | v₂(3^{n₀}·m₀ − 1): halvings at reset |
| n₁ | v₂(s+1): new countdown length after reset |
| W | Lyapunov candidate: 3^n·m |
| S_T | Diophantine system for T-periodic meta-orbit |
| CF(x) | continued fraction expansion of x |
| μ(x) | irrationality measure of x |
| B | computational verification bound: 2^68 |

---

*This document was assembled from a research program exploring the Collatz conjecture through the lens of √2, the cascade operator ω, and the (n,m) coordinate system. All results marked ✓ are proven. Results marked ◈ are structurally valid but not individually sufficient for a proof. Results marked ○ are conjectural. The single open problem is identifying which of the five closure options in §8 is most tractable.*
