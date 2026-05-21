import math

def pell_in_cycle(k_odd, K_halving):
    lhs_coeff = K_halving - 1.5 * k_odd
    rhs_base = k_odd * 0.5 * math.log(9.0/8.0)
    residual = lhs_coeff * math.log(2) - rhs_base
    return {
        'k': k_odd, 'K': K_halving,
        'lhs_coeff': lhs_coeff,
        'rhs_base': rhs_base,
        'residual': residual,
    }

# Convergents from CF of log2(3)
log2_3 = math.log2(3)
x = log2_3
cf = []
for _ in range(30):
    a = int(x)
    cf.append(a)
    frac = x - a
    if frac < 1e-12: break
    x = 1.0 / frac

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

baker_results = []
for K, k in convergents:
    if k == 0: continue
    gap = abs(k * math.log(3) - K * math.log(2))
    baker_results.append({'k': k, 'K': K, 'gap': gap})

print("[5] PELL DECOMPOSITION OF CYCLE EQUATION")
print("-" * 50)
print("  Decomposition: k·ln(3) = k·(3/2)·ln(2) + k·(1/2)·ln(9/8)")
print("  Where 9/8 = 1 + (1/2)³ (Pell depth 3)")
print()
for r in baker_results[:8]:
    p = pell_in_cycle(r['k'], r['K'])
    print(f"  k={p['k']:5d}, K={p['K']:5d}: LHS coeff of ln2 = {p['lhs_coeff']:+.1f}, "
          f"RHS base = {p['rhs_base']:.6f}, residual = {p['residual']:+.6e}")

print("\n[6] PHASE CONSTRAINT (K mod 8)")
print("-" * 50)
for r in baker_results[:12]:
    kmod = r['K'] % 8
    closed = "CLOSED" if kmod == 0 else f"OPEN (shift={kmod})"
    print(f"  k={r['k']:8d}, K={r['K']:8d}: K mod 8 = {kmod} → {closed}")

# Key identity verification
print("\n[7] KEY IDENTITIES")
print("-" * 50)
sqrt2 = math.sqrt(2)
cd = 1 - 1/sqrt2
print(f"  3/2 - √2 = (1-1/√2)² : {abs(1.5-sqrt2 - cd**2) < 1e-15} (exact)")
print(f"  3/(2√2) = √(9/8)     : {abs(3/(2*sqrt2) - math.sqrt(9/8)) < 1e-15} (exact)")
print(f"  9/8 = 1 + (1/2)³     : True (algebraic)")
print(f"  ln(9/8)               = {math.log(9/8):.15f}")

# Cascade coords
print("\n[8] CASCADE COORDINATES")
print("-" * 50)
def nc(v): return 2*math.log2(v)
for name, v in [("1", 1), ("√2", sqrt2), ("2", 2), ("3", 3),
                ("3/2", 1.5), ("3/4", 0.75), ("3/(2√2)", 3/(2*sqrt2)),
                ("log₂(3)", math.log2(3))]:
    print(f"  n({name:12s}) = {nc(v):+.6f}")

# ============================================================
# PART 9: THE CRITICAL TEST — Does tier growth outpace Baker?
# ============================================================
print("\n[9] CRITICAL: TIER GROWTH vs BAKER BOUND RACE")
print("-" * 50)
print("  Key question: as computational bound B grows,")
print("  which convergent families survive?")
print()

# Collatz has been verified up to about 2^68 ≈ 3×10^20
# That means ALL numbers below this are in some tier
verified_bounds = [
    ("Terras 1976", 1e6),
    ("Oliveira+ 1999", 1e15),
    ("Barina 2020", 2**68),  # ≈ 2.95e20
]

for name, bound in verified_bounds:
    print(f"  {name} (B = {bound:.2e}):")
    for r in baker_results[:15]:
        k, K, gap = r['k'], r['K'], r['gap']
        max_corr = k / (3.0 * bound)
        ratio = max_corr / gap
        status = "KILLED" if ratio < 1 else f"SURVIVES (ratio={ratio:.2e})"
        if ratio >= 1 or (ratio < 1 and ratio > 0.01):
            print(f"    k={k:8d}, K={K:8d}: correction/gap = {ratio:.2e} → {status}")
    print()

# Which convergent is the HARDEST to kill?
print("\n[10] HARDEST CONVERGENT TO KILL")
print("-" * 50)
# For each convergent, what bound is needed?
for r in baker_results[:15]:
    k, K, gap = r['k'], r['K'], r['gap']
    # Need k/(3B) < gap => B > k/(3*gap)
    B_needed = k / (3 * gap)
    print(f"  k={k:8d}: need B > {B_needed:.2e} "
          f"({'ALREADY KILLED by Barina' if B_needed < 2**68 else 'OPEN'})")

