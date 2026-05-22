"""
Inverse construction at (K, L) = (8, 5).
D = 2^8 - 3^5 = 256 - 243 = 13.

Enumerate ALL 35 ordered partitions of 8 into 5 positive parts.
For each, compute N_L and check if D | N_L.

If we find ZERO tuples where D | N_L, no cycle exists at this convergent.
"""

from itertools import combinations

K_total = 8
L = 5
D = 2**K_total - 3**L
print(f"K = {K_total}, L = {L}, D = 2^K - 3^L = {D}")
print()

# Generate ordered partitions of K_total into L positive parts.
# Equivalent: choose L-1 dividers among K_total-1 spaces.
# Equivalent: pick increasing sequence 0 < s_1 < s_2 < ... < s_{L-1} < K_total
# where s_i = k_1 + ... + k_i.

partitions = []
for divider_set in combinations(range(1, K_total), L - 1):
    # divider_set is (s_1, s_2, s_3, s_4); s_0 = 0, s_5 = K_total
    s = (0,) + divider_set + (K_total,)
    ks = tuple(s[i+1] - s[i] for i in range(L))
    partitions.append((ks, divider_set))

print(f"Total ordered partitions of {K_total} into {L} positive parts: {len(partitions)}")
print()

# For each partition, compute N_L = sum_{i=1..L} 3^(L-i) * 2^(s_{i-1})
# where s_0 = 0, s_1 = k_1, ..., s_{L-1} = k_1+...+k_{L-1}

print(f"{'k-tuple':<25} {'N_L':<15} {'N_L mod D':<10}")
print("-" * 50)

zero_tuples = []
all_residues = []
for ks, _ in partitions:
    s = [0]
    for k in ks[:-1]:
        s.append(s[-1] + k)
    # s = (s_0, s_1, ..., s_{L-1})
    N_L = sum(3**(L - 1 - i) * 2**s[i] for i in range(L))
    residue = N_L % D
    all_residues.append(residue)
    if residue == 0:
        zero_tuples.append((ks, N_L, N_L // D))

# Print all
for (ks, _), residue in zip(partitions, all_residues):
    flag = "  *** ZERO!" if residue == 0 else ""
    # Recompute N_L for display
    s_disp = [0]
    for k in ks[:-1]:
        s_disp.append(s_disp[-1] + k)
    N_L_disp = sum(3**(L - 1 - i) * 2**s_disp[i] for i in range(L))
    print(f"{str(ks):<25} {N_L_disp:<15} {residue:<10}{flag}")

print()
print("=" * 60)
print(f"RESULT: {len(zero_tuples)} tuple(s) give N_L ≡ 0 (mod {D})")
print("=" * 60)

if zero_tuples:
    print("Tuples giving integer m candidates:")
    for ks, N_L, m_candidate in zero_tuples:
        print(f"  k-tuple {ks}: N_L = {N_L}, candidate m = N_L/D = {m_candidate}")
else:
    print(f"NO k-tuple yields N_L ≡ 0 mod {D}.")
    print(f"Conclusion: No cycle of length L={L}, total halvings K={K_total} exists.")
print()

# Distribution of residues
from collections import Counter
residue_dist = Counter(all_residues)
print("Distribution of N_L mod D values:")
for r in sorted(residue_dist.keys()):
    print(f"  residue {r}: {residue_dist[r]} times")
