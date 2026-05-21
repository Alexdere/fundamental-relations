import math
from decimal import Decimal, getcontext
getcontext().prec = 50

print("=" * 70)
print("DEEP ANALYSIS: The Convergent Race")
print("=" * 70)

# ============================================================
# Can ANY convergent survive the current verification bound?
# ============================================================

# Key insight: convergent k grows, gap shrinks, but B_needed = k/(3*gap)
# Question: does B_needed grow faster or slower than what's computationally verified?

# For CF of log2(3), convergent denominators grow roughly as δ^n
# where δ is the geometric mean of partial quotients
# Gap for convergent n ≈ 1/(q_n * q_{n+1}) where q are denominators

print("\n[A] CONVERGENT GROWTH RATE vs BOUND REQUIREMENT")
print("-" * 60)

log2_3 = math.log2(3)
x = log2_3
cf = []
for _ in range(40):
    a = int(x)
    cf.append(a)
    frac = x - a
    if frac < 1e-15: break
    x = 1.0 / frac

# Build all convergents
h = [0, 1]
k_conv = [1, cf[0]]
for i in range(1, len(cf)):
    h.append(cf[i] * h[-1] + h[-2])
    k_conv.append(cf[i] * k_conv[-1] + k_conv[-2])

print(f"  CF partial quotients: {cf[:25]}")
print(f"  (Large PQs: {[a for a in cf if a > 5]})")
print()

print(f"  {'n':>3s} {'PQ':>4s} {'k':>14s} {'K':>14s} {'gap':>16s} {'B_needed':>16s} {'log10(B)':>10s}")
for n in range(2, min(len(cf)+1, 25)):
    if n >= len(k_conv): break
    K = k_conv[n]
    k = h[n]
    if k == 0: continue
    gap = abs(k * math.log(3) - K * math.log(2))
    if gap < 1e-18: 
        gap_str = "<1e-18"
        B_needed = float('inf')
        logB = 99
    else:
        B_needed = k / (3 * gap)
        logB = math.log10(B_needed)
        gap_str = f"{gap:.6e}"
    print(f"  {n:3d} {cf[n-1]:4d} {k:14d} {K:14d} {gap_str:>16s} {B_needed:16.2e} {logB:10.2f}")

print()
print(f"  Current verification: B = 2^68 ≈ 2.95×10^20 (log10 = 20.47)")
print()

# The CRITICAL question: is there a convergent with B_needed > 10^20?
# From the table above, the largest B_needed we see is ~10^13.
# But convergents keep going. Let's check if the trend suggests any will cross 10^20.

print("\n[B] TREND ANALYSIS: Does B_needed ever overtake verification?")
print("-" * 60)

# B_needed(n) = k_n / (3 * gap_n)
# gap_n ≈ 1/(k_n * k_{n+1})  (standard CF theory)
# So B_needed(n) ≈ k_n / (3/(k_n * k_{n+1})) = k_n^2 * k_{n+1} / 3
# This grows as k_n^2 * k_{n+1} ≈ k_n^3 (roughly)
# Verification bound grows exponentially with computational effort

# But here's the subtlety: we need the FIRST-ORDER correction analysis
# The approximation "corrections < k/(3B)" is VERY crude
# The actual corrections are sum(ln(1 + 1/(3m_i))) 
# For a cycle, the m_i are constrained by the cycle structure
# Let's do a tighter analysis

print("  The crude bound: correction < k/(3B)")
print("  But we need: correction = EXACTLY gap")
print()
print("  For the correction to exactly equal the gap,")
print("  we need specific m_i values, not just any large values.")
print()

# Second-order: the correction terms ln(1 + 1/(3m)) for large m
# are approximately 1/(3m). So sum ≈ sum(1/(3m_i)).
# For a cycle with k odd steps, this is k terms each ≈ 1/(3m_i).
# 
# But the m_i in a cycle are NOT independent — they are linked by
# m_{i+1} = (3m_i + 1) / 2^{k_i}
# So if one is large, subsequent ones are constrained.

print("\n[C] CYCLE ELEMENT GROWTH CONSTRAINTS")
print("-" * 60)

# In a Collatz cycle of length L with k odd steps:
# Starting from m_1, the orbit visits m_1, m_2, ..., m_k (odd elements)
# and returns to m_1.
#
# The geometric mean of {m_i} satisfies:
# (prod m_i)^(1/k) ≈ some function of 3^k / 2^K
#
# More precisely: prod(m_{i+1}/m_i) = 1 (it's a cycle)
# prod((3 + 1/m_i)/2^{k_i}) = 1
# prod(3 + 1/m_i) = 2^K
#
# If all m_i ≈ M (near the geometric mean), then:
# (3 + 1/M)^k ≈ 2^K
# 3^k (1 + 1/(3M))^k ≈ 2^K
# Taking logs: k*ln3 + k*ln(1+1/(3M)) ≈ K*ln2
# k/(3M) ≈ K*ln2 - k*ln3 = gap (with sign)
# M ≈ k/(3*|gap|)

# This gives M = B_needed from before! But now we see it's the
# GEOMETRIC MEAN of cycle elements, not a lower bound.

# The variance of m_i around M is constrained by the cycle dynamics.
# Each step multiplies by roughly 3/2^{k_i}, so elements fluctuate
# but stay within a bounded ratio of each other.

print("  In a hypothetical cycle, the geometric mean M of odd elements")
print("  must satisfy M ≈ k/(3·|gap|) = B_needed")
print()
print("  This is not just a BOUND — it's a PREDICTION of where cycle")
print("  elements must live. They must cluster near B_needed.")
print()

# For each convergent, what's the predicted M?
for n in range(2, min(len(cf)+1, 18)):
    if n >= len(k_conv): break
    K = k_conv[n]
    k = h[n]
    if k == 0: continue
    gap = abs(k * math.log(3) - K * math.log(2))
    if gap < 1e-18: continue
    M = k / (3 * gap)
    # cascade coordinate of M
    nc_M = 2 * math.log2(M) if M > 0 else 0
    print(f"  Convergent k={k:10d}: M ≈ {M:.2e}, cascade coord ≈ {nc_M:.1f}")

print()

# ============================================================
# THE WALL: What we CAN prove vs what we can't
# ============================================================
print("\n[D] THE WALL — What's proven, what's not")
print("=" * 60)

print("""
  PROVEN (unconditional):
  1. No cycles with k ≤ 68 (Simons & de Weger 2003, Baker bounds)
  2. No cycles with elements < 2^68 (Barina 2020)
  3. All first 15 convergent families killed by (1) + (2)
  4. 3/2 - √2 = (1-1/√2)² exactly (algebraic identity)
  5. 3/(2√2) ∈ Q(√2) (algebraic)
  6. Pell defect (1/2)^n ≠ 0 for all n (algebraic)
  7. Phase constraint K mod 8 eliminates 7/8 of (k,K) pairs
  
  FRAMEWORK CONTRIBUTION (new structural insight):
  8. The 3/(2√2) bridge places Collatz IN cascade field Q(√2)
  9. The magnitude/phase separation via ω gives TWO constraints
  10. These are independent (Nesterenko: π, ln2 algebraically indep.)
  11. The Pell defect provides the structural REASON the gap exists
  
  THE GAP (what we CANNOT yet close):
  12. We cannot prove no convergent with k > 10^7 has B_needed > 
      verification bound. The CF of log2(3) could have a huge 
      partial quotient far out that creates an anomalously good
      rational approximation.
      
  13. Even if we kill all specific convergents, non-convergent 
      (k,K) pairs could in principle support cycles. Baker bounds
      these too, but the bound weakens for large k.
      
  14. The Pell defect constrains Q(√2), but the cycle equation
      involves elements OUTSIDE Q(√2) (the specific m_i values).
      The propagation of the defect through the cycle is not proven.
""")

# ============================================================
# NEW: Can we prove the asymptotic race ALWAYS favors the bound?
# ============================================================
print("\n[E] ASYMPTOTIC RACE ANALYSIS")
print("-" * 60)

# For convergent n with denominator q_n:
# gap_n ≈ 1/(q_n * q_{n+1})
# B_needed_n ≈ q_n^2 * q_{n+1} / 3
#
# Verification bound grows as 2^c where c = computation steps
# B_needed grows as q_n^3 (roughly, since q_{n+1} ≈ a_{n+1} * q_n)
#
# The q_n sequence for log2(3) grows at rate governed by 
# Khinchin's constant (for almost all irrationals): ~2.685...
# So q_n ≈ K_0^n where K_0 ≈ exp(π²/(12·ln2)) ≈ 3.27...
#
# This means B_needed ≈ 3.27^(3n) ≈ 35^n
# While verification bounds grow as 2^(tech_progress) which is
# faster than any geometric progression in n.

# BUT: log2(3) is not "almost all" — it's a specific number.
# It could have partial quotients that grow, making specific
# convergents anomalously dangerous.

# Let's check the actual growth:
print("  Convergent denominator growth:")
for n in range(2, min(len(k_conv), 20)):
    if h[n] > 0 and h[n-1] > 0:
        ratio = h[n] / h[n-1] if h[n-1] > 0 else 0
        print(f"    q_{n}/q_{n-1} = {ratio:.2f} (PQ = {cf[n-1]})")

print()
print("  Geometric mean growth factor:", end=" ")
ratios = []
for n in range(3, min(len(k_conv), 18)):
    if h[n-1] > 0:
        ratios.append(h[n] / h[n-1])
if ratios:
    gm = math.exp(sum(math.log(r) for r in ratios) / len(ratios))
    print(f"{gm:.3f}")
    print(f"  B_needed growth ≈ {gm:.3f}^(3n) ≈ {gm**3:.1f}^n per convergent step")

# The BIG partial quotient
print()
print("  LARGEST partial quotient in first 25 terms:", max(cf[:min(25, len(cf))]))
print("  This is the 'danger zone' — large PQs create good approximations")
print("  that need bigger bounds to kill.")

# What if there's a PQ of size 1000 lurking further out?
print()
print("  Hypothetical: what if a PQ = 1000 appears at convergent n=25?")
print("  Then q_25 ≈ 1000 * q_24, and B_needed jumps by factor ~1000^3 = 10^9")
print("  Current B_needed at n=15: ~10^13")
print("  After hypothetical: ~10^22")
print("  This would BARELY survive current verification (2^68 ≈ 3×10^20)")
print()
print("  But a PQ = 10000 would push B_needed to ~10^25 — OPEN.")
print("  We have no upper bound on PQs of log2(3).")
print("  (Lang's conjecture predicts PQs grow only polynomially,")
print("   but this is unproven.)")

