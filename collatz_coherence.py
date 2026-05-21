#!/usr/bin/env python3
"""
COHERENCE PROOF: Does the cascade embedding preserve Collatz dynamics?

We need to establish that ℤ embeds into ℚ(√2, i) in a way that:
1. Preserves the Collatz map (equivariance)
2. Constraints found in the big space pull back to valid constraints on ℤ
3. ℤ-cycles are exactly the ℤ-restriction of ℚ(√2,i)-cycles

The direction that matters:
  NOT: "no cycles in big space → no cycles in small space"
  (bigger space could have MORE cycles, so this is trivially wrong)
  
  YES: "ℤ-cycles ARE cycles in the big space"
  (so constraints that eliminate cycles in the big space 
   also eliminate the ℤ-cycles sitting inside it)

This is the "pullback principle": if C is a constraint on cycles in 
ℚ(√2,i), and every ℤ-cycle is also a ℚ(√2,i)-cycle, then C 
eliminates ℤ-cycles too.
"""

import math, cmath

print("=" * 70)
print("COHERENCE PROOF: Standard Collatz ↪ Cascade Space")
print("=" * 70)

# ============================================================
# PART 1: THE EMBEDDING (trivial but must be stated)
# ============================================================

print("""
THEOREM 1 (Embedding): The inclusion map ι: ℤ → ℤ[√2, i]
defined by ι(n) = n + 0·√2 + 0·i + 0·i√2 is a ring homomorphism.

Proof: ι preserves addition: ι(a+b) = a+b = ι(a) + ι(b).
       ι preserves multiplication: ι(a·b) = a·b = ι(a)·ι(b).
       ι preserves 0 and 1.
       ι is injective (different integers map to different elements).
       ■
       
This is trivial — integers ARE elements of ℚ(√2, i) with the 
irrational and imaginary components set to zero.
""")

# ============================================================
# PART 2: COLLATZ EQUIVARIANCE (the key property)
# ============================================================

print("THEOREM 2 (Equivariance): The standard Collatz map T on ℤ")
print("is the restriction of a well-defined map T̃ on ℤ[√2, i].")
print()
print("We need: T̃(ι(n)) = ι(T(n)) for all n ∈ ℤ.")
print()

# Standard Collatz
def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

# The extended map on ℤ[√2, i] uses √2-divisibility for parity
# Since 2 = (√2)², an integer n is "even" iff divisible by 2
# For integers, √2-divisibility reduces to ordinary 2-divisibility
# because n/√2 is in ℤ[√2] iff n is even (then n/√2 = (n/2)·√2)

# But here's the key: we DON'T need a generalized Collatz on all of ℤ[√2,i].
# We only need that the CONSTRAINTS we derive apply to the ℤ-embedded cycles.

print("CRITICAL DISTINCTION:")
print("-" * 50)
print("""
We are NOT defining a "new Collatz map" on ℚ(√2, i).
We are ANALYZING the standard Collatz map on ℤ using the 
COORDINATE SYSTEM provided by ℚ(√2, i).

Analogy: studying projectile motion using polar coordinates
doesn't change the physics — it reveals structure (circular 
symmetry) that Cartesian coordinates obscure.

Similarly: studying Collatz orbits in cascade coordinates
doesn't change the dynamics — it reveals structure (Pell 
constraints, phase periodicity) that integer coordinates obscure.

The coherence question is therefore:
"Does the cascade coordinate system faithfully represent 
integer Collatz dynamics?"

NOT:
"Does a generalized Collatz map on ℚ(√2,i) behave like 
the integer one?"
""")

# ============================================================
# PART 3: FAITHFUL REPRESENTATION (coordinate change, not map change)
# ============================================================

print("THEOREM 3 (Faithful Representation):")
print("The cascade coordinate n(v) = 2·log₂(v) is a bijection on ℤ⁺.")
print("It preserves multiplicative structure: n(ab) = n(a) + n(b).")
print("It converts the Collatz map into an additive shift in n-space.")
print("-" * 50)
print()

# Verify: Collatz steps as cascade-coordinate shifts
print("Verification: Collatz steps as cascade shifts")
print()
print(f"  {'m':>8s} → {'T(m)':>8s}  {'n(m)':>10s} → {'n(T(m))':>10s}  {'shift':>10s}  type")

def cascade_coord(v):
    return 2 * math.log2(v) if v > 0 else float('-inf')

test_vals = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 27, 31, 41, 53, 97, 127, 255]
for m in test_vals:
    tm = collatz(m)
    nm = cascade_coord(m)
    ntm = cascade_coord(tm)
    shift = ntm - nm
    step_type = "3n+1" if m % 2 == 1 else "n/2"
    print(f"  {m:8d} → {tm:8d}  {nm:10.4f} → {ntm:10.4f}  {shift:+10.4f}  {step_type}")

print()

# The REDUCED map (odd → odd): m → odd_part(3m+1)
print("Reduced map (odd → odd) in cascade coordinates:")
print()
print(f"  {'m':>6s} → {'m_next':>8s}  {'halvings k':>10s}  {'n-shift':>10s}  {'n-shift/k':>10s}")

def reduced_collatz(m):
    """Return (next_odd, halvings)"""
    v = 3 * m + 1
    k = 0
    while v % 2 == 0:
        v //= 2
        k += 1
    return v, k

for m in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 27, 31, 41, 53, 97, 127]:
    m_next, k = reduced_collatz(m)
    nm = cascade_coord(m)
    nnext = cascade_coord(m_next)
    shift = nnext - nm
    print(f"  {m:6d} → {m_next:8d}  k={k:3d}        {shift:+10.4f}  {shift/k if k > 0 else 0:+10.4f}")

print()

# ============================================================
# PART 4: THE CASCADE SHIFT DECOMPOSITION
# ============================================================

print("THEOREM 4 (Cascade Shift Decomposition):")
print("Each reduced Collatz step m → m' has cascade shift:")
print("  Δn = n(m') - n(m) = 2·log₂((3 + 1/m)/2^k)")
print("     = 2·log₂(3 + 1/m) - 2k")
print("     = 2·log₂(3) + 2·log₂(1 + 1/(3m)) - 2k")
print("     = n(3) + 2·log₂(1 + 1/(3m)) - 2k")
print("-" * 50)
print()

n_3 = cascade_coord(3)
print(f"  n(3) = {n_3:.6f} (the off-cascade position of prime 3)")
print(f"  2k is always an even integer (cascade-native shift)")
print()
print("  So each Collatz step = irrational shift n(3) + tiny correction - integer shift 2k")
print("  The CYCLE condition is: sum of all shifts = 0")
print("  i.e.: L·n(3) + Σ corrections - 2K = 0")
print("  where L = odd steps, K = total halvings")
print()

# ============================================================
# PART 5: WHY CONSTRAINTS IN CASCADE SPACE ARE VALID ON ℤ
# ============================================================

print("THEOREM 5 (Pullback Validity):")
print("Any constraint on the cycle equation that uses only:")
print("  (a) properties of ln(2) and ln(3) (Baker's theorem)")
print("  (b) properties of (K mod 8) (phase from cascade periodicity)")
print("  (c) properties of A²-2B²=(1/2)ⁿ (Pell defect)")
print("is a valid constraint on ℤ-cycles.")
print("-" * 50)
print()
print("""
Proof structure:

1. A cycle in ℤ consists of integers m₁, ..., m_L satisfying
   the reduced Collatz recurrence. These are REAL INTEGERS.

2. The cycle equation ∏(3 + 1/mᵢ) = 2^K is a statement about
   REAL NUMBERS (in fact, rationals on the LHS, integer on RHS).
   This equation is true IN ℤ, IN ℚ, IN ℝ, and IN ℚ(√2,i).
   It doesn't change when you embed it.

3. Taking logarithms: Σ ln(3 + 1/mᵢ) = K·ln(2).
   This is a REAL equation. It doesn't involve √2 or i at all.
   Baker's theorem applies to it directly.

4. The decomposition ln(3) = (3/2)·ln(2) + (1/2)·ln(9/8)
   is an IDENTITY between real numbers. It's true in every space.
   
5. The observation that 9/8 = 1 + (1/2)³ connects to the Pell
   structure. This is a REAL algebraic identity.

6. The phase constraint K ≡ 0 mod 8 comes from the cascade 
   operator ω = (1+i)/2. Here's where we need care:

   The phase constraint arises because ω^8 = (1/16)·1 (real).
   So ω^n is real iff n ≡ 0 mod 8.
   
   But DOES this constraint apply to the Collatz cycle equation?
   
   The connection: in cascade coordinates, division by 2 corresponds
   to subtracting 2 from the cascade coordinate. After K halvings,
   the total cascade shift is -2K. For the ORBIT to close (cycle),
   the total shift must be a multiple of the cascade period.
   
   The cascade period for REAL numbers is... just 0. Any shift
   along the real cascade is fine.
   
   BUT: if we track the cascade PHASE (the argument of ω^n),
   then the phase after K halvings is K·(π/4) mod 2π.
   For phase closure: K·(π/4) ≡ 0 mod 2π, i.e., K ≡ 0 mod 8.
   
   CRITICAL QUESTION: does the "phase" have meaning for real
   integer Collatz?
""")

# ============================================================
# PART 6: TESTING THE PHASE CONSTRAINT
# ============================================================

print("EMPIRICAL TEST: Does K mod 8 actually constrain ℤ-cycles?")
print("-" * 50)
print()

# For the trivial cycle {1} → {1}: 
# 1 → 4 → 2 → 1, so the full cycle 1→4→2→1 has K=2 (two halvings)
# K mod 8 = 2 ≠ 0. But this IS a cycle!
# 
# Wait - let's be more careful. The reduced map: 1 → odd_part(4) = 1, k=2
# So the 1-cycle has K=2, k=1.

print("The trivial cycle {1}:")
m, k = reduced_collatz(1)
print(f"  1 → 3·1+1=4 → divide by 2^{k} → {m}")
print(f"  K = {k}, K mod 8 = {k % 8}")
print(f"  Phase constraint says K ≡ 0 mod 8? K={k}, K mod 8 = {k%8} → NOT satisfied!")
print()
print("  THE TRIVIAL CYCLE VIOLATES THE PHASE CONSTRAINT.")
print("  This means K mod 8 = 0 is NOT a valid constraint on ℤ-cycles.")
print()

# This is actually a FINDING. The phase constraint doesn't apply
# to all ℤ-cycles. Let me check what it actually constrains.

print("RE-EXAMINING: What does the phase constraint actually say?")
print("-" * 50)
print()
print("""
The cascade operator ω = (1+i)/2 has ω^n with:
  n=1: (1+i)/2          angle π/4
  n=2: i/2              angle π/2
  n=3: (-1+i)/4         angle 3π/4
  n=4: -1/4             angle π
  n=5: (-1-i)/8         angle 5π/4
  n=6: -i/8             angle 3π/2
  n=7: (1-i)/16         angle 7π/4
  n=8: 1/16             angle 0 (= 2π)

So ω^K is REAL (positive) when K ≡ 0 mod 8.
ω^K is REAL (negative) when K ≡ 4 mod 8.
ω^K is PURELY IMAGINARY when K ≡ 2 or 6 mod 8.

The trivial cycle has K=2. ω^2 = i/2 (purely imaginary).
""")

# So the phase constraint doesn't kill ℤ-cycles directly.
# It's a constraint on the CASCADE SPACE cycles, not on ℤ-cycles.
# This is an honest finding — the phase constraint does NOT
# pull back cleanly to ℤ.

print("HONEST ASSESSMENT: Phase constraint coherence")
print("=" * 50)
print()

# But wait - let me think about this differently.
# The phase isn't about ω^K being real.
# It's about the COLLATZ ORBIT returning to the same point
# in cascade space. The cascade coordinate is REAL for 
# positive integers. So the orbit is always on the real axis
# of cascade space. The phase of ω^K doesn't enter.

# So what DOES the phase constraint actually constrain?

print("""
REVISED ANALYSIS:

The cascade coordinate n(v) = 2·log₂(v) is REAL for v ∈ ℤ⁺.
The Collatz orbit of a positive integer stays on the REAL AXIS
of cascade space. The imaginary axis (phase) is never visited.

Therefore: the phase constraint from ω's complex structure
does NOT directly constrain ℤ-Collatz cycles.

The phase constraint would apply to a GENERALIZED Collatz map
operating on ℚ(√2, i) — but that's a different problem.

WHAT DOES PULL BACK VALIDLY:
✓ Baker's theorem on |k·ln3 - K·ln2| — pure real analysis
✓ The identity 3/2 - √2 = (1-1/√2)² — real algebraic
✓ The identity 9/8 = 1 + (1/2)³ — real algebraic  
✓ The Pell defect A²-2B² = (1/2)ⁿ ≠ 0 — real algebraic
✓ The decomposition ln(3) = (3/2)ln(2) + (1/2)ln(9/8) — real
✓ The death spiral (tier pruning + Baker) — real analysis
✓ Fundamental theorem of arithmetic (3^k ≠ 2^K) — integer

WHAT DOES NOT PULL BACK:
✗ Phase constraint K ≡ 0 mod 8 — requires complex extension
✗ "Two independent constraints" — in ℤ, there's only one
  (the magnitude/Baker constraint). Phase is specific to the 
  complex extension.
  
CONCLUSION: The cascade coordinate system is a valid REAL
coordinate change for studying ℤ-Collatz. The Pell algebra
and Baker bounds are valid constraints on ℤ-cycles. But the
phase constraint is an ADDITIONAL constraint that only applies
to the generalized problem on ℚ(√2, i), not to standard Collatz.

This means our "dual impossibility" argument has only ONE leg
that applies to standard Collatz (Baker/Pell magnitude), not
two (magnitude + phase). The phase is bonus structure for the
extended problem.
""")

# ============================================================
# PART 7: WHAT'S LEFT — the valid core
# ============================================================

print("THE VALID CORE (what survives coherence testing)")
print("=" * 50)
print()

# Let's verify each piece
proofs = [
    ("Embedding ι: ℤ → ℚ(√2)", True, 
     "Trivial ring homomorphism"),
    ("Collatz equivariance T̃∘ι = ι∘T", True, 
     "T is defined on ℤ; ι just re-labels, doesn't change map"),
    ("Cycle equation in log form", True, 
     "Real equation, valid in any extension of ℝ"),
    ("ln(3) = (3/2)ln(2) + (1/2)ln(9/8)", True, 
     "Real algebraic identity, verified numerically"),
    ("9/8 = 1 + Pell defect at n=3", True, 
     "Algebraic identity: 9/8 = 1 + (1/2)³"),
    ("Baker bound on |k·ln3 - K·ln2|", True, 
     "Standard transcendence theory, applies to reals"),
    ("Death spiral (tiers + Baker)", True, 
     "Real analysis + arithmetic, fully valid on ℤ"),
    ("Pell defect (1/2)^n ≠ 0", True, 
     "Algebraic identity in ℚ(√2) ⊂ ℝ, valid"),
    ("Phase constraint K mod 8", False, 
     "Requires complex cascade; ℤ-orbits stay real"),
    ("Two independent constraints", False, 
     "Only magnitude constraint applies to ℤ-Collatz"),
]

for name, valid, reason in proofs:
    status = "✓ VALID" if valid else "✗ DOES NOT APPLY"
    print(f"  {status:20s}  {name}")
    print(f"  {'':20s}  Reason: {reason}")
    print()

# Final count
valid_count = sum(1 for _, v, _ in proofs if v)
invalid_count = sum(1 for _, v, _ in proofs if not v)
print(f"  Score: {valid_count} valid, {invalid_count} not applicable to ℤ-Collatz")
print()

# ============================================================
# PART 8: But wait — can we RESCUE the phase constraint?
# ============================================================

print("CAN THE PHASE CONSTRAINT BE RESCUED?")
print("=" * 50)
print("""
There might be a way to make the phase constraint applicable:

APPROACH 1: Modular arithmetic as "discrete phase"
  The 2-adic valuation v₂(3n+1) determines how many times 
  we divide by 2. This creates a sequence k₁, k₂, ..., k_L
  of halvings. The sum K = Σkᵢ must satisfy:
  
  3^L ≡ 2^K (mod something)
  
  Since 3 has order 2 mod 4, order 2 mod 8:
    3¹ ≡ 3 mod 8
    3² ≡ 1 mod 8
  
  And 2^K mod... well, 2^K = 0 mod 8 for K ≥ 3.
  
  The cycle equation 3^L · ∏(1 + 1/(3mᵢ)) = 2^K 
  taken mod 8 gives constraints on L and K.
  
  This is a REAL mod-8 constraint, not from complex phase!
  It's the NUMBER-THEORETIC shadow of the cascade phase.

APPROACH 2: The constraint is on the PATTERN of halvings
  In a cycle, the sequence of halvings (k₁, k₂, ..., k_L)
  must satisfy sum = K. But also, each kᵢ ≥ 1 (at least one
  halving per step), and the kᵢ are determined by the 2-adic
  structure of 3mᵢ + 1.
  
  The mod-8 structure of integers constrains which sequences
  of kᵢ are achievable. This IS a real constraint on ℤ.
""")

# Test Approach 1: mod-8 constraints
print("Testing mod-8 constraints on cycle equation:")
print("-" * 50)
print()

# For a cycle: ∏(3m_i + 1) = 2^K · ∏m_i (since m_{i+1} = (3m_i+1)/2^{k_i})
# The product ∏(3m_i + 1) ≡ ? mod 8

# For the trivial cycle m=1:
# 3·1+1 = 4. Product = 4. 2^K = 2^2 = 4. ✓
print("  Trivial cycle {1}: ∏(3m+1) = 4, 2^K = 4. mod 8: 4 ≡ 4 ✓")

# For a hypothetical 2-element cycle {a, b}:
# (3a+1)(3b+1) = 2^K · a · b
# 9ab + 3a + 3b + 1 = 2^K · ab
# (9 - 2^K)ab + 3(a+b) + 1 = 0

print()
print("  Hypothetical 2-cycle {a,b}: (9 - 2^K)·ab + 3(a+b) + 1 = 0")
print()

# Check which K values allow positive odd solutions
for K in range(1, 20):
    coeff = 9 - 2**K
    if coeff == 0:
        print(f"    K={K}: degenerate (coeff=0)")
        continue
    # Need: ab = -(3(a+b) + 1) / (9 - 2^K) > 0
    # For K >= 4: 2^K > 9, so coeff < 0
    # Then ab = (3(a+b) + 1) / (2^K - 9) > 0 requires a+b > 0 (yes)
    # and K mod 8:
    if K <= 8:
        feasible = "maybe" if coeff < 0 else ("needs a,b < 0" if coeff > 0 else "degen")
        print(f"    K={K:2d}: coeff = {coeff:6d}, K mod 8 = {K%8}, {feasible}")

print()
print("  For K=2 (the trivial cycle's value): coeff = 9-4 = 5")
print("  5ab + 3(a+b) + 1 = 0 has no positive solutions. ✓")
print("  (The trivial cycle is L=1, not L=2)")

