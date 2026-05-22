"""
Run the inverse construction for multiple small (K, L) convergent pairs.
Restrict to cases where enumeration is feasible.
"""

from itertools import combinations
from math import comb

def run_inverse(K_total, L, limit=200000):
    D = 2**K_total - 3**L
    if D <= 0:
        return None, "D ≤ 0"
    n_partitions = comb(K_total - 1, L - 1)
    if n_partitions > limit:
        return (n_partitions, None, None, D), f"too many partitions ({n_partitions:,})"
    
    zero_tuples = []
    for dividers in combinations(range(1, K_total), L - 1):
        s = (0,) + dividers + (K_total,)
        ks = tuple(s[i+1] - s[i] for i in range(L))
        N_L = sum(3**(L - 1 - i) * 2**s[i] for i in range(L))
        if N_L % D == 0:
            m = N_L // D
            zero_tuples.append((ks, m))
    return (n_partitions, len(zero_tuples), zero_tuples, D), None

test_pairs = [
    (2, 1), (3, 2), (5, 3), (8, 5), (11, 7), (13, 8),
    (16, 10), (19, 12), (24, 15), (27, 17), (32, 20),
]

print(f"{'(K, L)':<10} {'K%8':<4} {'D':<10} {'#part.':<10} {'D|N_L?':<10} {'m≥3 odd':<10}")
print("-" * 65)

for K, L in test_pairs:
    result, err = run_inverse(K, L)
    if err and "too many" in err:
        n_part, _, _, D = result
        print(f"({K:>2},{L:>2})   {K%8:<4} {D:<10} {n_part:<10,} skipped: too many")
        continue
    if err:
        print(f"({K},{L}) -- {err}")
        continue
    n_part, n_zero, tuples, D = result
    valid = [(ks, m) for ks, m in (tuples or []) if m >= 3 and m % 2 == 1]
    flag = ""
    if D < 0:
        flag = "(D<0, no positive m)"
    print(f"({K:>2},{L:>2})   {K%8:<4} {D:<10} {n_part:<10} {n_zero or 0:<10} {len(valid):<10} {flag}")
    if valid:
        print(f"        Candidates: {valid[:5]}")

