"""
Build the mod-5 transition graph and the combined mod-40 (= mod 5 × mod 8) graph.

Key insight: the Collatz map on residues mod 5 depends on (m mod 5, k mod 4)
since 2 has multiplicative order 4 mod 5.

Then we'll look at closed orbits — what 'cycle shapes' are even possible 
at each modular resolution.
"""

from collections import defaultdict
from itertools import combinations

# ============================================================
# PART 1: The mod-5 transition graph
# ============================================================

print("=" * 60)
print("MOD-5 TRANSITION GRAPH")
print("=" * 60)
print()
print("From m mod 5, with k mod 4 controlling division:")
print("(transition rule: m → (3m+1)·2^(-k) mod 5)")
print()

# 2 has order 4 mod 5. 2^(-1) mod 5: 2*3=6≡1, so 2^(-1)≡3.
# So 2^(-k) mod 5 cycles: k=0→1, k=1→3, k=2→4, k=3→2.
inv_2k_mod_5 = {0: 1, 1: 3, 2: 4, 3: 2}

transitions_5 = defaultdict(set)
for m_mod_5 in range(5):
    a = (3 * m_mod_5 + 1) % 5
    for k_mod_4 in range(4):
        target = (a * inv_2k_mod_5[k_mod_4]) % 5
        transitions_5[m_mod_5].add((target, k_mod_4))

print(f"{'State':<8} {'Targets (target, k mod 4)':<60}")
for m_mod_5 in range(5):
    targets = sorted(transitions_5[m_mod_5])
    targets_str = ", ".join(f"({t},{k})" for t, k in targets)
    print(f"  {m_mod_5}    →  {targets_str}")

print()
print("Notice the asymmetry:")
print("  - State 3 mod 5: ALWAYS maps to 0 mod 5 (regardless of k mod 4).")
print("  - States 0, 1, 2, 4 mod 5: can reach any state via choice of k.")
print()
print("So m ≡ 3 mod 5 is a 'funnel': every trajectory through 3 immediately exits to 0.")
print()

# ============================================================
# PART 2: Closed orbits in the mod-5 graph
# ============================================================

print("=" * 60)
print("CLOSED ORBITS IN MOD-5 GRAPH (length ≤ 5)")
print("=" * 60)
print()

# State graph: ignore the k details for orbit-finding, just look at reachability
reachable_5 = defaultdict(set)
for src, edges in transitions_5.items():
    for tgt, k in edges:
        reachable_5[src].add(tgt)

print("Reachability:")
for src in sorted(reachable_5.keys()):
    print(f"  {src} → {sorted(reachable_5[src])}")
print()

def find_closed_orbits(reachable, max_length):
    orbits = []
    seen_canon = set()
    
    def dfs(start, path):
        if len(path) > max_length:
            return
        last = path[-1]
        for nxt in reachable.get(last, []):
            if nxt == start and len(path) >= 1:
                cycle = tuple(path)
                rotations = [cycle[i:] + cycle[:i] for i in range(len(cycle))]
                canon = min(rotations)
                if canon not in seen_canon:
                    seen_canon.add(canon)
                    orbits.append(canon)
            elif nxt not in path:
                dfs(start, path + [nxt])
    
    for start in reachable.keys():
        dfs(start, [start])
    return orbits

orbits_5 = find_closed_orbits(reachable_5, max_length=5)
print(f"Total distinct closed orbits in mod-5 graph (length ≤ 5): {len(orbits_5)}")
print()

# Group by length
by_len = defaultdict(list)
for o in orbits_5:
    by_len[len(o)].append(o)

for L in sorted(by_len.keys()):
    print(f"\nLength L = {L}:")
    for o in by_len[L][:15]:
        print(f"  {o}")
    if len(by_len[L]) > 15:
        print(f"  ... +{len(by_len[L])-15} more")

