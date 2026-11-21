#!/usr/bin/env python3
"""Independent audit certificates for two exact issues in theorem L.
This script does not establish the general upper-bound theorem.
"""
from collections import Counter
from itertools import product


def s_type(w, ell):
    d = ell - 1
    if len(w) < max(1, 2*d):
        return ('short', w)
    return ('long', w[:d], w[-d:] if d else '')


def counts(w, ell):
    return Counter(w[i:i+ell] for i in range(len(w)-ell+1))


def gap_counterexample():
    k, ell, f = 2, 2, 2
    K = k**ell
    lam = K*(2*k**(ell-1)-1)
    lamprime = 2*(ell-1)*lam
    c = [1]
    for _ in range(K+1):
        c.append(K*c[-1]+f+lamprime+2)
    w = 'aa' + 'ba'*40 + 'b'*201
    n = counts(w, ell)
    assert n == Counter({'aa':1, 'ab':41, 'ba':40, 'bb':200})
    occupied = [sorted([edge for edge,m in n.items() if c[g] <= m < c[g+1]])
                for g in range(k+1)]
    assert all(occupied), occupied
    assert c[:4] == [1, 32, 156, 652]
    # The K+1-interval formulation has an empty interval for any K positive counts.
    all_gaps = [g for g in range(K+1)
                if not any(c[g] <= m < c[g+1] for m in n.values())]
    assert all_gaps, 'K+1 gaps needed for pigeonhole guarantee'
    print('FALSE k+1-interval formulation:')
    print('  word = aa(ba)^40 b^201; factor counts:', dict(n))
    print('  first 3 intervals:', list(zip(c[:3],c[1:4])), 'occupied:', occupied)
    print('  valid K+1-interval choice (0-indexed):', all_gaps)


def ell_one_nonempty_repair():
    ell=1
    J='abc'  # each letter is a loop at the one vertex of D_1
    Z=Counter('abbccc')
    H0=J*(ell-1)
    reported_h=H0+H0
    assert reported_h == ''  # FAIL: input of substitutability must be nonempty
    corrected_h=J
    corrected_t=''.join(a*(Counter(corrected_h)[a]+Z[a]) for a in sorted(set(J)))
    assert corrected_h and corrected_t
    assert set(corrected_h) == set(corrected_t)
    assert counts(corrected_t,1) - counts(corrected_h,1) == Z
    assert s_type(corrected_h,1) == s_type(corrected_t,1)
    print('ell=1: source h is empty; repaired h=',corrected_h,
          't=',corrected_t)


def finite_p0_sanity():
    # Compare a few nonequivalent same-(type,internal window counts) tuples
    # against all admissible contexts of limited length for a LOCAL-COUNT language.
    ell=3
    alphabet='ab'
    words=[''.join(t) for n in range(1,7) for t in product(alphabet,repeat=n)]
    def in_L(w):
        return bool(w) and w[0]=='a' and w[-1]=='a' and 'bbb' not in w and w.count('a')==2*w.count('b')
    groups={}
    for u in words:
        key=(s_type(u,ell),frozenset(u),tuple(sorted(counts(u,ell).items())))
        groups.setdefault(key,[]).append(u)
    ctx=[''.join(t) for n in range(3) for t in product(alphabet,repeat=n)]
    pairs=0
    for g in groups.values():
        for u in g:
            for v in g:
                for p in ctx:
                    for q in ctx:
                        assert in_L(p+u+q)==in_L(p+v+q), (p,u,v,q)
                pairs+=1
    print('P0^ell finite sanity test OK:',pairs,'same-invariant word pairs')


if __name__=='__main__':
    gap_counterexample()
    ell_one_nonempty_repair()
    finite_p0_sanity()
    print('all asserts passed')
