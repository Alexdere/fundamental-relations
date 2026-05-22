"""
Build the mod-8 transition graph and enumerate closed orbits.
Rewrite with cleaner logic.
"""
from collections import defaultdict

def collatz_step(m):
    val = 3 * m + 1
    k = 0
    while val % 2 == 0:
        val //= 2
        k += 1
    return val, k

def build_transition_graph(n):
    """Returns dict: residue -> set of (next_residue, k)."""
    modulus = 2**n
    transitions = defaultdict(set)
    sample_limit = 2**(n + 10)
    for m in range(3, sample_limit, 2):  # odd m, skip m=1 (boundary)
        residue = m % modulus
        next_m, k = collatz_step(m)
        next_residue = next_m % modulus
        transitions[residue].add((next_residue, k))
    return dict(transitions)

def all_closed_orbits(transitions, max_length):
    """Find ALL closed orbits (cycles in the residue graph) up to max_length."""
    orbits_found = []
    seen_canonical = set()
    
    def dfs(start, current_path, current_ks):
        if len(current_path) > max_length:
            return
        last = current_path[-1]
        if last not in transitions:
            return
        for (next_r, k) in transitions[last]:
            new_path = current_path + [next_r]
            new_ks = current_ks + [k]
            if next_r == start:
                # Closed orbit: path = (start, ..., last) with last edge back to start
                # The cycle consists of current_path, with one full traversal of new_ks edges
                cycle = tuple(current_path)
                ks = tuple(new_ks)
                # Canonical form: lex-min rotation
                rotations = [cycle[i:] + cycle[:i] for i in range(len(cycle))]
                canon_idx = min(range(len(cycle)), key=lambda i: rotations[i])
                canon = tuple(rotations[canon_idx])
                # Rotate ks accordingly
                ks_rot = tuple(ks[canon_idx:] + ks[:canon_idx])
                signature = (canon, ks_rot)
                if signature not in seen_canonical:
                    seen_canonical.add(signature)
                    orbits_found.append((canon, ks_rot))
            elif next_r not in current_path:
                dfs(start, new_path, new_ks)
    
    for start in transitions.keys():
        dfs(start, [start], [])
    
    return orbits_found

print("="*60)
print("MOD-8 TRANSITION GRAPH (odd residues)")
print("="*60)
trans_8 = build_transition_graph(3)
for r in sorted(trans_8.keys()):
    targets = sorted(trans_8[r])
    print(f"  {r} mod 8 → {targets}")

print()
print("="*60)
print("CLOSED ORBITS IN MOD-8 GRAPH (length ≤ 5)")
print("="*60)
orbits = all_closed_orbits(trans_8, max_length=5)
print(f"Total distinct closed orbits: {len(orbits)}\n")

# Group by length
from collections import defaultdict
by_len = defaultdict(list)
for cycle, ks in orbits:
    by_len[len(cycle)].append((cycle, ks))

for L in sorted(by_len.keys()):
    print(f"\n--- Length L = {L} ---")
    for cycle, ks in sorted(by_len[L]):
        K = sum(ks)
        print(f"  Residues {cycle} → k-values {ks} | K={K}, K mod 8 = {K%8}")
