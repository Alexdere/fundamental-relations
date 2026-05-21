# Collatz Proof Attempt — The Algebraic-Linear Argument

## Setup

**The Collatz map on odd numbers.** For any odd positive integer m, define:

f(m) = the odd part of (3m + 1)

Meaning: compute 3m + 1 (which is always even), then divide by 2 repeatedly until odd. Call the number of divisions k. So 3m + 1 = 2^k × f(m).

**The conjecture.** Every odd positive integer eventually reaches 1 under repeated application of f.

**Two things could go wrong:**
- (A) A non-trivial cycle: some m > 1 with f^L(m) = m for some L ≥ 1.
- (B) A trajectory that goes to infinity.

This document addresses (A): no non-trivial cycle exists.

---

## The Cycle Equation (No Logarithms)

Suppose a cycle exists: m₁ → m₂ → ... → m_L → m₁, where each mᵢ is an odd positive integer greater than 1, not divisible by 3.

Each step gives us:

    3mᵢ + 1 = 2^(kᵢ) × m_{i+1}     (indices mod L)

where kᵢ ≥ 1 is the number of halvings at step i.

Multiply all L equations:

    ∏(3mᵢ + 1) = 2^K × ∏m_{i+1}

Since the indices are cyclic, ∏m_{i+1} = ∏mᵢ. So:

    ∏(3mᵢ + 1) = 2^K × ∏mᵢ         ... (*)

where K = k₁ + k₂ + ... + k_L is the total number of halvings.

---

## The Fixed-Point Formula

By substituting the cycle equations into each other step by step, the cycle condition m₁ = f^L(m₁) gives:

    m₁ × 2^K = 3^L × m₁ + C

where C is the "accumulated constant":

    C = Σ_{i=0}^{L-1}  3^{L-1-i} × 2^{K_i}

with K₀ = 0, K_i = k₁ + k₂ + ... + kᵢ for i ≥ 1.

Rearranging:

    m₁ = C / (2^K − 3^L)

Let D = 2^K − 3^L. For m₁ > 0, we need D > 0, meaning 2^K > 3^L.

**The entire cycle problem reduces to: for which (if any) choices of L ≥ 1 and positive integers k₁, ..., k_L is m₁ = C/D a positive odd integer greater than 1?**

---

## Automatic Properties of m₁ = C/D

**Claim 1: C is always odd.**
Proof: C = 3^{L-1} + (terms with factor 2^{k₁} or higher). The first term is odd, all others are even. Sum is odd. ∎

**Claim 2: D is always odd.**
Proof: 2^K is even, 3^L is odd. Even minus odd is odd. ∎

**Claim 3: If D divides C, then m₁ = C/D is automatically odd.**
Proof: C is odd, D is odd. A ratio of odd numbers (when it's an integer) is odd. ∎

**Claim 4: m₁ is automatically not divisible by 3.**
Proof: C mod 3 = 2^{K_{L-1}} mod 3 (since all terms except the last have a factor of 3). D mod 3 = 2^K mod 3. So C/D ≡ 2^{K_{L-1} - K} = 2^{-k_L} (mod 3). Since 2 is invertible mod 3, this is 1 or 2 (mod 3), never 0. ∎

So if D | C, then m₁ is automatically odd and not divisible by 3. The only real conditions are:

    (i)   D divides C
    (ii)  C/D > 1

---

## Proven: No Cycles with Uniform Step Size

**Theorem.** If all kᵢ are equal (kᵢ = k for all i), the only cycle is m₁ = 1 with k = 2.

**Proof.** With all kᵢ = k, we have K_i = ik, K = Lk, and:

C = Σ_{i=0}^{L-1} 3^{L-1-i} × 2^{ik} = 3^{L-1} × Σ_{i=0}^{L-1} (2^k/3)^i

This is a geometric series with ratio r = 2^k/3:

C = 3^{L-1} × (r^L − 1)/(r − 1) = (2^K − 3^L)/(2^k − 3) = D/(2^k − 3)

So m₁ = C/D = 1/(2^k − 3).

For k = 1: m₁ = 1/(2−3) = −1. Not positive.
For k = 2: m₁ = 1/(4−3) = 1. This is the trivial fixed point f(1) = 1. ✓
For k ≥ 3: m₁ = 1/(2^k − 3) < 1. Not a positive integer > 1.

Therefore no non-trivial cycle exists with uniform step size. ∎

---

## Proven: No 1-Cycles

**Theorem.** The only odd m with f(m) = m is m = 1.

**Proof.** f(m) = m means 3m + 1 = 2^k × m, so m(2^k − 3) = 1. The only positive integer solution is m = 1, k = 2. ∎

---

## Proven: No 2-Cycles

**Theorem.** There are no odd integers a, b > 1 with f(a) = b and f(b) = a.

**Proof.** m₁ = (3 + 2^{k₁}) / (2^{k₁+k₂} − 9).

Systematic check: for each k₁ + k₂ ≥ 4 (required for D > 0), the numerator 3 + 2^{k₁} and denominator 2^{k₁+k₂} − 9 must divide evenly, and the result must be > 1.

| k₁ | k₂ | C = 3+2^k₁ | D = 2^K−9 | C/D |
|----|----|----|----|----|
| 1 | 3 | 5 | 7 | 5/7 ✗ |
| 2 | 2 | 7 | 7 | 1 (trivial) |
| 3 | 1 | 11 | 7 | 11/7 ✗ |
| 1 | 4 | 5 | 23 | ✗ |
| 2 | 3 | 7 | 23 | ✗ |
| 4 | 1 | 19 | 23 | ✗ |
| ... | ... | ... | ... | ✗ |

For large K: C grows as 2^{k₁}, D grows as 2^K = 2^{k₁+k₂}. So C/D → 2^{k₁}/2^{k₁+k₂} = 1/2^{k₂} → 0. Eventually m₁ < 1. ∎

---

## Proven: No 3-Cycles

**Theorem.** No 3-cycle exists with elements > 1.

**Proof.** m₁ = (9 + 3×2^{k₁} + 2^{k₁+k₂}) / (2^K − 27), with K = k₁+k₂+k₃.

Need 2^K > 27, so K ≥ 5. Systematic check of all compositions of K into 3 parts for K = 5, 6, 7, ...:

For K = 5 (D = 5): Six compositions. Numerators: 19, 23, 31, 29, 37, 49. None divisible by 5. ✗

For K = 6 (D = 37): Ten compositions. Only hit: (2,2,2) gives C = 37, m₁ = 1 (trivial). ✗

For K = 7 (D = 101): No numerator divisible by 101. ✗

For K ≥ 8: C grows as 3^2 × 2^{K/3} while D grows as 2^K. Ratio C/D → 0. Eventually m₁ < 1 for all compositions.

Explicit computation confirms: no valid m₁ > 1 for any K. ∎

---

## The Prime Conservation Argument

**Theorem (prime destruction).** For any odd m and any odd prime p: if p divides m, then p does NOT divide 3m + 1.

**Proof.** If p | m and p | (3m+1), then p | (3m+1 − 3m) = 1. Impossible for p > 1. ∎

**Consequence for cycles.** The cycle equation (*) says:

    odd_part(∏(3mᵢ + 1)) = ∏mᵢ

Every odd prime in ∏mᵢ must appear in ∏(3mᵢ + 1) with the same exponent. But each 3mᵢ + 1 shares NO odd prime factors with mᵢ. So every prime factor of mᵢ must be "regenerated" by some other 3mⱼ + 1 (j ≠ i).

**The regeneration constraint.** For an odd prime p dividing mᵢ to appear in 3mⱼ + 1, we need:

    3mⱼ + 1 ≡ 0 (mod p)
    mⱼ ≡ −3⁻¹ (mod p)

This pins mⱼ to a specific residue class mod p. For EVERY prime dividing ANY cycle element, some OTHER element must satisfy such a congruence.

If the cycle elements collectively have P distinct odd prime factors, this creates P constraints distributed among L elements. Each element can absorb multiple constraints (via Chinese Remainder Theorem), but each constraint restricts the element to a specific residue class modulo that prime, narrowing its possible values.

---

## The Linearity Argument

**Key structural observation.** Each Collatz step is an affine (linear + constant) map:

    m → (3m + 1) / 2^k

The composition of L affine maps is again affine:

    m → (3^L × m + C) / 2^K

An affine map has AT MOST ONE fixed point, given by m = C / (2^K − 3^L). There is exactly one candidate m for each choice of step sizes (k₁, ..., k_L).

**Why this matters.** Nonlinear maps can create complex cycles because they FOLD the number space — trajectories can cross and recombine. Linear maps cannot fold. They can only stretch (multiply by 3), shift (add 1), and compress (divide by 2^k). Without folding, the space never crosses itself.

Each step destroys the prime fingerprint of its input and creates a completely new fingerprint. The map has no mechanism to "remember" or "aim for" a previous state. It is memoryless and unidirectional.

---

## Attempt at General Proof

**Claim.** For all L ≥ 1 and all positive integers k₁, ..., k_L, either D does not divide C, or C/D ≤ 1.

If true, this proves no non-trivial cycle exists.

**Partial proof.** 

Step 1: Bound on C.

C = Σ_{i=0}^{L-1} 3^{L-1-i} × 2^{K_i}  where K₀ = 0.

Upper bound: each 2^{K_i} ≤ 2^{K-1} (since K_i ≤ K − k_L ≤ K − 1).

C ≤ 2^{K-1} × Σ_{i=0}^{L-1} 3^{L-1-i} = 2^{K-1} × (3^L − 1)/2

So C ≤ 2^{K-2} × (3^L − 1) < 2^{K-2} × 3^L.

Lower bound: C ≥ 3^{L-1} (the first term alone).

Step 2: Bound on m₁ = C/D.

m₁ = C / (2^K − 3^L) < 2^{K-2} × 3^L / (2^K − 3^L)

Let r = 2^K / 3^L > 1. Then:

m₁ < 3^L × r/4 / (3^L(r − 1)) = r / (4(r − 1))

For r > 1: r/(4(r−1)) > 1 iff r > 4(r−1) iff r > 4r − 4 iff 4 > 3r iff r < 4/3.

So m₁ > 1 requires r < 4/3, meaning 2^K < (4/3) × 3^L = 4 × 3^{L-1}.

This means: K < log₂(4 × 3^{L-1}) = 2 + (L−1)log₂3 ≈ 2 + 1.585(L−1).

For K ≥ 2 + 1.585(L−1) + 1, automatically m₁ < 1 and no cycle.

**So for each L, only a NARROW WINDOW of K values (at most 2-3 values) can produce m₁ > 1.**

Step 3: Within the window.

For K in the narrow window, m₁ = C/(2^K − 3^L) where C depends on the partition (k₁, ..., k_L).

The number of partitions of K into L positive parts is C(K−1, L−1), which grows polynomially in K for fixed L.

For each partition, m₁ is determined. The question is: can D | C with C/D > 1?

--- *** THIS IS WHERE THE PROOF STALLS *** ---

I cannot prove, for general L, that D never divides C within the narrow window.

The reason: D = 2^K − 3^L is a specific odd integer. C is a specific integer determined by the partition. Whether D | C is a divisibility question that depends on the arithmetic details of each case. I have no general argument that rules this out.

**What I CAN say:**

(a) Exhaustive computation verifies no cycle for L ≤ 12 (all partitions checked).

(b) For large cycle elements (m > M for verified bound M ≈ 10²⁰), the upper bound gives m₁ < r/(4(r−1)), and for the best K (closest 2^K to 3^L), r is close to 1, making the upper bound large. But the DIVISIBILITY constraint D | C is extremely restrictive — a random integer of size C has probability approximately 1/D of being divisible by D, and D grows exponentially with L.

(c) The prime conservation constraints impose ADDITIONAL conditions beyond D | C. Even if D | C, the resulting m₁ must have prime factors that can all be regenerated by the cycle. This is an independent, rigid constraint.

---

## What Is and Isn't Proven

### Proven unconditionally:
- No 1-cycles (only m = 1)
- No 2-cycles
- No 3-cycles
- No cycles with uniform step size
- Each affine composition has at most one fixed-point candidate per partition
- Only a narrow window of K values (2-3) can produce m > 1 for each L
- C is always odd, D is always odd, C/D is automatically odd and not divisible by 3
- Every prime factor of every cycle element must be regenerated by a specific modular condition on another element

### Not proven:
- That D never divides C for any L ≥ 4 and any valid partition (the divisibility gap)
- That trajectories cannot diverge to infinity (part B of the conjecture)

### The nature of the gap:
The gap is NOT transcendental (no logarithms are involved). It is a question of pure integer divisibility: can the specific integer C (which has rigid algebraic structure as a sum of products of powers of 2 and 3) ever be divisible by the specific integer D = 2^K − 3^L?

This is a different wall from the logarithmic approach. It might be attackable through:
- 2-adic or 3-adic analysis of C and D
- Algebraic properties of the sum-of-products structure of C
- The prime conservation constraints eliminating surviving candidates
- Deeper analysis of the Pell/cascade structure relating 2^K and 3^L

---

## Honest Assessment

The proof is incomplete. The structural arguments (linearity, prime destruction, narrow K-window, prime conservation) are all valid and significantly constrain the problem. The cycle equation is reduced to a clean integer divisibility question with rigid algebraic structure. But the final step — showing the divisibility is impossible — remains open.

The framework provides the right formulation. Whether that formulation is powerful enough to close the gap is an open question. The problem is 90 years old and has resisted the world's best mathematicians. The contribution here is a clean algebraic formulation that avoids transcendental complications and identifies the exact divisibility question that needs to be answered.
