"""Independent spot checks for chatgpt_outer_c_2026-11-06 (Claude)."""
import itertools
# D_n = (138) example 5.1: S -> A_n b | aaaa | bbbb | cccc ; A_0 -> a|c ; A_i -> A_{i-1}A_{i-1} | c
def gen(n):
    A = {'a', 'c'}
    for _ in range(n): A = {'c'} | {u+v for u in A for v in A}
    return {x+'b' for x in A} | {'aaaa','bbbb','cccc'}
for n in (1, 2, 3):
    L = gen(n)
    mu = min(len(w) for w in L if set(w) == {'a','b'})
    assert mu == 2**n + 1
    # SUB1 certificate: E0=(eps,b) accepts c, cc ; E1=(ccc,eps): ccc+c in L, ccc+cc not
    assert {'cb','ccb','cccc'} <= L and 'ccccc' not in L
    # S1 / S2: c-counts among full-content words
    Kc = {w.count('c') for w in L if set(w) == {'a','b','c'}}
    assert set(range(1, 2**n)) <= Kc, (n, sorted(Kc))
    print(f'n={n}: |L|={len(L)}, mu_ab={mu}, full-content c-counts={sorted(Kc)}  OK')
# S1 argument sanity on n=3: replace the j unmarked level-1 blocks after the first by c
n, i = 3, 1; L = gen(n); q = 2**(n-i); blk = 'a'*2**i
for k in range(1, q):
    w = blk + 'c'*k + blk*(q-1-k) + 'b'
    assert w in L and w.count('c') == k
print('S1 cube words in L for n=3, level 1: OK')
