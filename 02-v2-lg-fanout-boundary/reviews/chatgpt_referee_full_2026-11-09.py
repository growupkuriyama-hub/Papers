#!/usr/bin/env python3
"""Independent finite checks for referee report, MCFG #2 (2026-11-09).
No external network, no author-side review records. Exhaustive tests are NOT proofs.
"""
from collections import defaultdict
from itertools import combinations
from math import comb, exp, log, log10


def doubling(n):
    words = {'a'}
    for _ in range(n):
        words = {'b' + x + y + 'b' for x in words for y in words} | {'c' + x + 'c' for x in words}
    return words


def pure_doubling(n):
    w = 'a'
    for _ in range(n):
        w = 'b' + w + w + 'b'
    return w


def distributions(lang, fanout):
    dist = defaultdict(set)
    contexts = defaultdict(set)
    for word in lang:
        cuts = range(len(word) + 1)
        for d in range(1, fanout + 1):
            for pos in combinations(cuts, 2 * d):
                factors = tuple(word[pos[2*k]:pos[2*k+1]] for k in range(d))
                sep = [word[:pos[0]]]
                sep += [word[pos[2*k-1]:pos[2*k]] for k in range(1, d)]
                sep += [word[pos[-1]:]]
                ctx = tuple(sep)
                dist[factors].add(ctx)
                contexts[ctx].add(factors)
    return dist, contexts


def subset_substitutable(lang, fanout, get_type):
    dist, by_context = distributions(lang, fanout)
    for ctx, factors in by_context.items():
        by_type = defaultdict(list)
        for x in factors:
            by_type[tuple(get_type(t) for t in x)].append(x)
        for vs in by_type.values():
            if len(vs) > 1:
                d = dist[vs[0]]
                for y in vs[1:]:
                    if dist[y] != d:
                        return False, ctx, vs[0], y
    return True, None, None, None


def marker_words(f, q, n):
    return [''.join(chr(96+j)*i + chr(64+j) for j in range(1, 2*f+1)) + 'z'*(2*f*(q-i)+2**n) for i in range(q+1)]


def alternate_marker_words(q,n):
    return ['a'*i + 'd' + 'a'*i + 'd' + 'a'*(2*(q-i)+2**n) for i in range(q+1)]


def check_laminar(max_points=4):
    for n in range(1,max_points+1):
        sets = [frozenset(i for i in range(n) if mask>>i&1) for mask in range(1,1<<n)]
        best = 0
        for mask in range(1<<len(sets)):
            chosen = [s for j,s in enumerate(sets) if mask>>j&1]
            if len(chosen) <= best: continue
            if all(a<=b or b<=a or a.isdisjoint(b) for a,b in combinations(chosen,2)):
                best = len(chosen)
        assert best == 2*n-1,(n,best)
        print(f'laminar n={n}: exhaustive max={best} <= 2n-1={2*n-1}')


def h_constants():
    mu = (27/4)**(1/3)
    gamma = log(3)/log(mu)
    eta = 1/80
    x = 6/(eta*log(mu))
    log_ce = 6*log(x) - (x-1)*eta*log(mu)
    exponent = gamma/(1-eta)
    log_c0 = log10(11) + exponent*(log10(15625)+2*log10(mu)+log_ce/log(10))
    log_c = log_c0 + 22*log10(2)
    assert gamma<1.7260 and exponent<1.7479
    assert log_ce < 34 and log_c0 < 36 and log_c < 43
    print(f'H mu={mu:.12f}, gamma={gamma:.12f}, gamma/(1-eta)={exponent:.12f}')
    print(f'H log(C_eta) upper={log_ce:.12f}, log10(C0) upper={log_c0:.12f}, log10(C) upper={log_c:.12f}')
    for M in range(6,81):
        k=M//3
        assert comb(M+1,k)>=comb(3*k,k)
        assert comb(3*k,k) >= (27/4)**k/(M+1)
        # Verify the approximate exponential inequality the proof uses.
        assert mu**(M-2) <= (27/4)**k*(1+1.e-12)
    print('H binomial/subexponential inequalities: M=6..80 PASS')


def check_doubling():
    for n in (1,2,3):
        L = doubling(n)
        W = pure_doubling(n)
        assert [w for w in L if 'c' not in w] == [W]
        assert len(W) == 3*2**n - 2
        assert 13*n+7 == (n+2)+3+2+12*n
        assert 4*n == max(2*n+2*i for i in range(1,n+1))
        assert 3*2**n - 1 >= 2**((13*n+7+4*n)/17)
        good = subset_substitutable(L,1,lambda w:1)
        assert good[0],(n,good)
        print(f'doubling n={n}: |L|={len(L)}, unique pure len={len(W)}, |G|={13*n+7}, theta={4*n}; f=1 substitutable PASS')


def check_marker():
    for f,q,n in ((1,2,1),(2,1,1),(2,2,1)):
        L = marker_words(f,q,n)
        W=2*f*q+2**n+2*f
        assert all(len(w)==W for w in L)
        for mask in range(1<<(q+1)):
            J = [w for i,w in enumerate(L) if mask>>i&1]
            ok = subset_substitutable(J,f,lambda w:1)
            assert ok[0],(f,q,n,mask,ok)
        gram=(7*f+11)*q + 6*n+3*f+10
        assert gram <= (7*f+17)*(q+1)
        print(f'marker f={f} q={q} n={n}: {1<<(q+1)} subsets, untyped f-substitutability PASS; W={W}, |G|={gram}')
    for q in (1,2,3):
        L=alternate_marker_words(q,1)
        for mask in range(1<<(q+1)):
            J=[w for i,w in enumerate(L) if mask>>i&1]
            assert subset_substitutable(J,1,lambda w:1)[0]
        print(f'marker binary CFG f=1 q={q}: all {1<<(q+1)} subsets PASS')


def check_power_transfer():
    n=6
    W=pure_doubling(n)
    # For U1, |S|=2, threshold n>=6; i0=p=1, i=1, delta=1, j=n-3.
    i=1; delta=1; j=n-i-delta-1
    prev=pure_doubling(n-1)
    second_start=1+len(prev)
    second_block_start=second_start + (n-1) - (delta+j)
    wl=W[:1]
    wm=W[1+i:second_block_start]
    wr=W[second_block_start+(delta+j):]
    assert W==wl+'b'*i+wm+'b'*(delta+j)+wr
    assert wm and 'a' in wm and j>=1
    transported=wl+'b'*(i+delta)+wm+'b'*j+wr
    assert transported!=W and len(transported)==len(W)
    assert sorted(transported)==sorted(W)
    assert transported.startswith('b'*(n+delta)+'a')
    print(f'power transfer n={n}: original={len(W)}, transported same length/Parikh, distinct, initial b-run={n+delta} PASS')


def check_capacity_on_doubling():
    for n in (1,2,3):
        L=doubling(n)
        kappa=max(w.count('c') for w in L)
        assert kappa==2**n
        M={'a','b'}
        mu = min(len(w) for w in L if set(w)==M)
        size=13*n+7; thick=4*n; r=2
        bnd=(2*len(M)-1+kappa)*size*(size+r*thick)
        assert mu <= bnd
        print(f'zeta-capacity witness n={n}: M={{a,b}}, kappa={kappa}, mu_M={mu}, predicted bound={bnd} PASS')

if __name__=='__main__':
    print('Referee independent finite checks; exhaustive only for indicated finite instances')
    check_doubling()
    check_marker()
    check_laminar()
    h_constants()
    check_power_transfer()
    check_capacity_on_doubling()
    print('ALL FINITE CHECKS PASS (not a proof of theorems)')
