#!/usr/bin/env python3
"""
Collatz-Cascade Engine
======================
1. Tier builder: backward tree from 1, tracking which odd numbers are "claimed"
2. Baker bound: lower bound on |k*ln3 - K*ln2| for cycle candidates
3. Death spiral test: as tiers grow, do corrections shrink faster than Baker gap?
4. Cycle equation residual: for hypothetical cycles at given parameters
"""

import math
from fractions import Fraction
from collections import defaultdict

# ============================================================
# PART 1: TIER STRUCTURE (backward tree from 1)
# ============================================================

def build_tiers(max_tier=20, max_value=10**6):
    """
    Build the backward Collatz tree from 1.
    
    Forward: odd m -> (3m+1)/2^k (some odd result)
    Backward: odd n can come from:
      - n*2^j for any j>=1 (even predecessors, but we want odd predecessors)
      - For odd predecessors: if n = (3m+1)/2^k, then m = (n*2^k - 1)/3
        m must be a positive odd integer not divisible by 3.
    
    Tier 0: {1}
    Tier t+1: all odd numbers that map to some number in tier t in one Collatz step
    """
    claimed = set()  # all odd numbers known to reach 1
    tiers = {0: {1}}
    claimed.add(1)
    
    tier_sizes = [1]
    tier_min_unclaimed = []
    
    for t in range(1, max_tier + 1):
        new_tier = set()
        # For each n in previous tier, find odd predecessors
        for n in tiers[t-1]:
            # Try different k values (number of halvings)
            # m = (n * 2^k - 1) / 3
            for k in range(1, 40):  # up to 2^40 multiplier
                val = n * (2**k) - 1
                if val % 3 != 0:
                    continue
                m = val // 3
                if m <= 0:
                    continue
                if m % 2 == 0:  # must be odd
                    continue
                if m > max_value:
                    continue
                if m not in claimed:
                    new_tier.add(m)
                    claimed.add(m)
        
        tiers[t] = new_tier
        tier_sizes.append(len(new_tier))
        
        # Find smallest unclaimed odd number (not div by 3)
        # that's NOT in claimed set
        min_unc = None
        for v in range(1, max_value, 2):
            if v not in claimed and v % 3 != 0:
                min_unc = v
                break
        tier_min_unclaimed.append(min_unc)
        
        if len(new_tier) == 0:
            break
    
    return tiers, claimed, tier_sizes, tier_min_unclaimed

# ============================================================
# PART 2: COVERAGE ANALYSIS
# ============================================================

def coverage_analysis(claimed, max_val):
    """What fraction of odd numbers (not div by 3) are claimed?"""
    total_candidates = 0
    covered = 0
    for v in range(1, max_val, 2):
        if v % 3 != 0:
            total_candidates += 1
            if v in claimed:
                covered += 1
    return covered, total_candidates, covered / total_candidates

# ============================================================
# PART 3: BAKER'S BOUND
# ============================================================

def baker_bound(L_max=200):
    """
    Baker's theorem gives: |k*ln(3) - K*ln(2)| > C * max(k,K)^(-delta)
    
    For the specific case of ln(2) and ln(3):
    Laurent (2008) refined: |b1*ln(2) + b2*ln(3)| > exp(-c * (log B)^2)
    where B = max(|b1|, |b2|).
    
    For our purposes: the cycle equation requires k odd steps and K = sum of halvings.
    Average K/k ≈ log2(3) ≈ 1.585.
    
    The "gap" is |k*ln(3) - K*ln(2)|. Since log2(3) is irrational,
    this is never 0 for positive k, K. But how small can it get?
    
    Best rational approximations to log2(3) from continued fraction:
    """
    log2_3 = math.log2(3)
    
    # Continued fraction of log2(3)
    x = log2_3
    cf = []
    for _ in range(30):
        a = int(x)
        cf.append(a)
        frac = x - a
        if frac < 1e-12:
            break
        x = 1.0 / frac
    
    # Convergents give the BEST rational approximations K/k to log2(3)
    # These are the cycle parameters that come closest to satisfying 3^k = 2^K
    convergents = []
    h_prev, h_curr = 0, 1
    k_prev, k_curr = 1, cf[0]
    convergents.append((k_curr, h_curr))
    
    for i in range(1, len(cf)):
        h_next = cf[i] * h_curr + h_prev
        k_next = cf[i] * k_curr + k_prev
        convergents.append((k_next, h_next))
        h_prev, h_curr = h_curr, h_next
        k_prev, k_curr = k_curr, k_next
    
    results = []
    for K, k in convergents:
        if k == 0:
            continue
        gap = abs(k * math.log(3) - K * math.log(2))
        # For a cycle with these parameters, the corrections must bridge this gap
        # Corrections sum ≈ sum of 1/(3*m_i) for i=1..k
        # If all m_i > B, then corrections < k/(3B)
        # Need: k/(3B) >= gap => B <= k/(3*gap)
        max_B = k / (3 * gap) if gap > 0 else float('inf')
        results.append({
            'k': k,  # odd steps
            'K': K,  # total halvings  
            'K_over_k': K/k,
            'gap': gap,
            'gap_log10': math.log10(gap) if gap > 0 else None,
            'max_element_bound': max_B,
        })
    
    return results, cf

# ============================================================
# PART 4: DEATH SPIRAL QUANTIFICATION
# ============================================================

def death_spiral_test(baker_results, computational_bound):
    """
    For each convergent (best cycle candidate):
    - The corrections must bridge the gap
    - All cycle elements must be > computational_bound (from tiers)
    - Maximum possible correction = k/(3*B) where B = min element
    - Is max correction < gap?
    """
    results = []
    for br in baker_results:
        k = br['k']
        gap = br['gap']
        if gap <= 0:
            continue
        
        # Max possible correction if all elements > computational_bound
        max_correction = k / (3.0 * computational_bound)
        
        # Is it enough?
        ratio = max_correction / gap
        killed = ratio < 1.0  # corrections can't bridge the gap
        
        results.append({
            'k': k,
            'K': br['K'],
            'gap': gap,
            'max_correction': max_correction,
            'ratio': ratio,
            'killed': killed,
        })
    
    return results

# ============================================================
# PART 5: PELL DEFECT IN CYCLE EQUATION
# ============================================================

def pell_in_cycle(k_odd, K_halving):
    """
    Express the cycle equation residual in cascade terms.
    
    Cycle requires: prod(3 + 1/m_i) = 2^K
    In log: sum(ln(3 + 1/m_i)) = K*ln(2)
    Expand: k*ln(3) + sum(ln(1 + 1/(3m_i))) = K*ln(2)
    
    The 3/(2√2) bridge: 3 = 2√2 * 3/(2√2) = 2√2 * √(9/8)
    So ln(3) = ln(2) + (1/2)*ln(2) + (1/2)*ln(9/8)
             = (3/2)*ln(2) + (1/2)*ln(9/8)
    
    Wait, let me be more careful:
    ln(3) = ln(2√2 * 3/(2√2)) = ln(2√2) + ln(3/(2√2))
           = ln(2) + (1/2)*ln(2) + ln(√(9/8))
           = (3/2)*ln(2) + (1/2)*ln(9/8)
    
    So: k*ln(3) = k*(3/2)*ln(2) + k*(1/2)*ln(9/8)
    
    Cycle eq: k*(3/2)*ln(2) + k*(1/2)*ln(9/8) + corrections = K*ln(2)
    
    Rearranging: (K - 3k/2)*ln(2) = k*(1/2)*ln(9/8) + corrections
    
    The LHS involves only ln(2) (cascade-native).
    The RHS involves ln(9/8) = ln(1 + 1/8) (Pell-adjacent, since 9/8 = 1 + (1/2)^3).
    """
    # Decomposition
    lhs_coeff = K - 1.5 * k  # coefficient of ln(2)
    rhs_base = k * 0.5 * math.log(9.0/8.0)  # the 3/(2√2) contribution
    
    # The residual that corrections must supply
    residual = lhs_coeff * math.log(2) - rhs_base
    
    # Express 9/8 in Pell terms
    # 9/8 = 1 + 1/8 = 1 + (1/2)^3
    # ln(9/8) = ln(1 + (1/2)^3) ≈ (1/2)^3 - (1/2)^6/2 + ...
    # This is a series in powers of (1/2), deeply cascade-native
    
    pell_depth_3 = (0.5)**3  # = 1/8
    ln_9_8_approx = pell_depth_3 - pell_depth_3**2/2 + pell_depth_3**3/3
    ln_9_8_exact = math.log(9.0/8.0)
    
    return {
        'k': k_odd,
        'K': K_halving,
        'lhs_coeff': lhs_coeff,
        'rhs_base': rhs_base,
        'residual': residual,
        'ln_9_8': ln_9_8_exact,
        'pell_approx_error': abs(ln_9_8_exact - ln_9_8_approx),
    }


# ============================================================
# RUN EVERYTHING
# ============================================================

print("=" * 70)
print("COLLATZ-CASCADE ENGINE — FULL DIAGNOSTIC")
print("=" * 70)

# --- PART 1: Build Tiers ---
print("\n[1] BUILDING TIER STRUCTURE (backward tree from 1)")
print("-" * 50)

MAXVAL = 100000  # keep manageable
tiers, claimed, tier_sizes, tier_min_unc = build_tiers(max_tier=15, max_value=MAXVAL)

for t in range(min(16, len(tier_sizes))):
    unc = tier_min_unc[t-1] if t > 0 and t-1 < len(tier_min_unc) else 'N/A'
    print(f"  Tier {t:2d}: {tier_sizes[t]:6d} new members | min unclaimed: {unc}")

# --- Coverage ---
print("\n[2] COVERAGE ANALYSIS")
print("-" * 50)
covered, total, frac = coverage_analysis(claimed, MAXVAL)
print(f"  Odd non-3-div numbers up to {MAXVAL}: {total}")
print(f"  Claimed by tier structure: {covered}")
print(f"  Coverage: {frac*100:.4f}%")
print(f"  Unclaimed: {total - covered}")

# Find first 20 unclaimed
unclaimed_list = []
for v in range(1, MAXVAL, 2):
    if v % 3 != 0 and v not in claimed:
        unclaimed_list.append(v)
        if len(unclaimed_list) >= 20:
            break
if unclaimed_list:
    print(f"  First unclaimed: {unclaimed_list[:20]}")
else:
    print(f"  ALL odd non-3-div numbers up to {MAXVAL} are claimed!")

# --- Baker bounds ---
print("\n[3] BAKER BOUNDS (best rational approx to log2(3))")
print("-" * 50)
baker_results, cf = baker_bound()
print(f"  CF of log2(3): {cf[:15]}...")
print()
print(f"  {'k':>8s} {'K':>8s} {'K/k':>12s} {'|gap|':>14s} {'log10(gap)':>12s} {'max_elem':>14s}")
for r in baker_results[:12]:
    me = f"{r['max_element_bound']:.1e}" if r['max_element_bound'] < 1e20 else "huge"
    gl = f"{r['gap_log10']:.2f}" if r['gap_log10'] else "N/A"
    print(f"  {r['k']:8d} {r['K']:8d} {r['K_over_k']:12.8f} {r['gap']:14.6e} {gl:>12s} {me:>14s}")

# --- Death spiral ---
print("\n[4] DEATH SPIRAL TEST")
print("-" * 50)
# Test with different computational bounds
for bound_exp in [3, 6, 9, 12, 15, 18, 20]:
    bound = 10**bound_exp
    ds = death_spiral_test(baker_results[:12], bound)
    killed_count = sum(1 for d in ds if d['killed'])
    total_tested = len(ds)
    print(f"  Bound = 10^{bound_exp:2d}: {killed_count}/{total_tested} convergent-families killed")
    # Show the surviving ones
    survivors = [d for d in ds if not d['killed']]
    if survivors and bound_exp <= 9:
        for s in survivors[:3]:
            print(f"    SURVIVES: k={s['k']}, K={s['K']}, ratio={s['ratio']:.4f}")

# --- Pell decomposition of cycle equation ---
print("\n[5] PELL DECOMPOSITION OF CYCLE EQUATION")
print("-" * 50)
print("  Decomposition: k·ln(3) = k·(3/2)·ln(2) + k·(1/2)·ln(9/8)")
print("  Where 9/8 = 1 + (1/2)³ (Pell depth 3)")
print()
for r in baker_results[:8]:
    p = pell_in_cycle(r['k'], r['K'])
    print(f"  k={p['k']:5d}, K={p['K']:5d}: LHS coeff of ln2 = {p['lhs_coeff']:+.1f}, "
          f"RHS base = {p['rhs_base']:.6f}, residual = {p['residual']:+.6e}")

# --- Phase constraint ---
print("\n[6] PHASE CONSTRAINT (K mod 8)")
print("-" * 50)
print("  For cascade phase closure, K must ≡ 0 mod 8")
print()
for r in baker_results[:12]:
    kmod = r['K'] % 8
    closed = "CLOSED" if kmod == 0 else f"OPEN (shift={kmod})"
    print(f"  k={r['k']:8d}, K={r['K']:8d}: K mod 8 = {kmod} → {closed}")

# --- Key identity verification ---
print("\n[7] KEY IDENTITIES VERIFICATION")
print("-" * 50)
sqrt2 = math.sqrt(2)
cascade_disp = 1 - 1/sqrt2
print(f"  3/2 - √2 = {1.5 - sqrt2:.15f}")
print(f"  (1-1/√2)² = {cascade_disp**2:.15f}")
print(f"  Match: {abs(1.5 - sqrt2 - cascade_disp**2) < 1e-15}")
print()
gm = 3/(2*sqrt2)
print(f"  3/(2√2) = {gm:.15f}")
print(f"  √(9/8)  = {math.sqrt(9/8):.15f}")
print(f"  Match: {abs(gm - math.sqrt(9/8)) < 1e-15}")
print()
print(f"  9/8 = 1 + (1/2)³ = {1 + 0.5**3}")
print(f"  ln(9/8) = {math.log(9/8):.15f}")
print(f"  (1/2)³  = {0.5**3}")
print(f"  Pell defect at n=3: A₃²-2B₃² = (1/2)³ = {0.5**3}")

# --- Cascade coordinate of key Collatz numbers ---
print("\n[8] CASCADE COORDINATES OF COLLATZ CONSTANTS")
print("-" * 50)
def n_cascade(v):
    return 2 * math.log2(v)

vals = [
    ("1 (identity)", 1),
    ("√2", sqrt2),
    ("2 (cascade base)", 2),
    ("3 (first off-cascade prime)", 3),
    ("3/2 (Collatz growth)", 1.5),
    ("3/4 (Collatz shrink)", 0.75),
    ("3/(2√2) (geometric mean)", gm),
    ("log₂(3)", math.log2(3)),
]
for name, v in vals:
    nc = n_cascade(v) if v > 0 else 'N/A'
    print(f"  n({name}) = {nc:.6f}")

