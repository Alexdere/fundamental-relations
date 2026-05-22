"""
For closed orbits in mod-5 graph, derive the forced k mod 4 sequences,
and check whether they're consistent with the (K, L) for actual cycles.

The triangle cycles live in {1, 2, 4} mod 5.
The smallest triangle cycle: (1) self-loop, requires k ≡ 2 mod 4 every step.
Other triangle cycles need specific k mod 4 patterns.
"""

# inv_2k_mod_5: which k mod 4 gives 2^(-k) ≡ value mod 5
# k=0: 1, k=1: 3, k=2: 4, k=3: 2

# Edges with (target, k_mod_4):
edges = {
    0: [(1,0), (2,3), (3,1), (4,2)],
    1: [(1,2), (2,1), (3,3), (4,0)],
    2: [(1,1), (2,0), (3,2), (4,3)],
    3: [(0,0), (0,1), (0,2), (0,3)],   # always to 0
    4: [(1,3), (2,2), (3,0), (4,1)],
}

print("="*60)
print("DERIVING FORCED k mod 4 SEQUENCES FOR CLOSED ORBITS")
print("="*60)
print()

# For a closed orbit (r_1, r_2, ..., r_L, r_1), the k-mod-4 at step i is
# the unique k_mod_4 such that r_i has an edge (r_{i+1}, k_mod_4).

# (Unique because for each (source, target) pair in mod-5, exactly one k mod 4 works.)

def transition_k(src, tgt):
    """Return k mod 4 for the transition src → tgt in mod-5 graph, or None if impossible."""
    for t, k in edges[src]:
        if t == tgt:
            return k
    return None

# Triangle cycles
triangle_orbits = [
    (1,),           # self-loop at 1
    (2,),           # self-loop at 2
    (4,),           # self-loop at 4
    (1, 2),
    (1, 4),
    (2, 4),
    (1, 2, 4),
    (1, 4, 2),
]

# Funnel cycles  
funnel_orbits = [
    (0, 3),
    (0, 1, 3),
    (0, 2, 3),
    (0, 4, 3),
]

def derive_k_sequence(orbit):
    L = len(orbit)
    ks = []
    for i in range(L):
        src = orbit[i]
        tgt = orbit[(i+1) % L]
        k = transition_k(src, tgt)
        ks.append(k)
    return tuple(ks)

print("TRIANGLE CYCLES (lives in {1, 2, 4} mod 5):")
print(f"{'orbit':<15} {'k mod 4 sequence':<20} {'K mod 4':<10}")
print("-" * 50)
for o in triangle_orbits:
    ks = derive_k_sequence(o)
    K_mod_4 = sum(ks) % 4
    print(f"{str(o):<15} {str(ks):<20} {K_mod_4}")

print()
print("FUNNEL CYCLES (passes through 3 → 0):")
print(f"{'orbit':<15} {'k mod 4 sequence':<20} {'K mod 4':<10}")
print("-" * 50)
for o in funnel_orbits:
    ks = derive_k_sequence(o)
    K_mod_4 = sum(ks) % 4
    print(f"{str(o):<15} {str(ks):<20} {K_mod_4}")

print()
print("="*60)
print("WHAT THIS TELLS US")
print("="*60)
print("""
For each closed orbit shape, the k mod 4 sequence is FORCED.
This determines K mod 4 for any cycle realizing this orbit.

A cycle of length L has K ≈ L · log₂(3) ≈ 1.585 L.
So K mod 4 should approximately equal int(1.585 L) mod 4
= L (mod some pattern).

If the forced K mod 4 disagrees with what an integer cycle needs,
the orbit can't be realized.
""")

# Check: for triangle cycle (1,2,4) with k=(1,3,2), K=6, K mod 4 = 2.
# An integer cycle of length 3 needs K close to 3·1.585 = 4.76, so K ∈ {4, 5}.
# K=4 mod 4 = 0, K=5 mod 4 = 1. Neither matches K_forced mod 4 = 2.
# So this orbit doesn't correspond to an integer cycle with K=4 or K=5.

# But wait - K doesn't have to be near 1.585*L; that's just for cycle closure (m positive).
# Actually for m to be ≥ 3, we need 2^K - 3^L > 0 (positive D),  
# AND m = N_L/D large enough.

# But the k-values in our derivation are k MOD 4, not actual k.
# The actual k can be any value ≡ k_mod_4 (mod 4).
# E.g., k=1 means k ∈ {1, 5, 9, ...}; k=2 means k ∈ {2, 6, 10, ...}.

# Constraint from mod-8 valuation lemma:
# k = 1 ⟺ m ≡ 3 or 7 mod 8
# k = 2 ⟺ m ≡ 1 mod 8  (exact)
# k ≥ 3 ⟺ m ≡ 5 mod 8

# So k mod 4 = 1 means k ∈ {1, 5, 9, ...}.
# k = 1 needs m ≡ 3 or 7 mod 8.
# k = 5 needs m ≡ 5 mod 8 with extra constraints.
# So different ACTUAL k values are accessible from different mod-8 residues.

# Combining mod-5 and mod-8 gives a sharper transition graph (mod 40).

