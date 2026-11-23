#!/usr/bin/env python3
"""Randomized exact check (finite languages) of the kernel-reduction identity

   (w0 cl_t1(K1) w1 ... cl_tn(Kn) wn)^|>  =  (w0 K1 w1 ... Kn wn)^|>,   cl_t(K) = K^{|><|} ∩ F_t,

and of its consequence: for a type-consistent rule A -> w0 A1 w1 ... An wn and
type-homogeneous kernels K_i ⊆ F_{t_i},
   cl_t0(K0) ⊇ w0 cl(K1) w1 ... cl(Kn) wn   <=>   K0^{|><|} ⊇ w0 K1^{|><|} w1 ... Kn^{|><|} wn.

Typings tested: content, first letter, |w|_a mod 2, U1 indicator of 'c', trivial.
Kernels are restricted to sets with a nonempty common context, so that all closures
are finite subsets of Sub(L).  This is CHECKED-FINITE evidence; the identity is
proved in general in the manuscript (Lemma lem:star).
Usage: python3 -I check_reduction_identity.py [trials] [seed]
"""
import random
import sys
from itertools import product

SIGMA = 'abc'
TYPINGS = {
    'content': lambda w: frozenset(w),
    'first': lambda w: w[0],
    'amod2': lambda w: w.count('a') % 2,
    'U1c': lambda w: 'c' in w,
    'trivial': lambda w: 0,
}


def T(name, w):
    return ('EMPTY',) if w == '' else ('T', TYPINGS[name](w))


def dist(L, x):
    out = set()
    for m in L:
        for i in range(len(m) - len(x) + 1):
            if m[i:i + len(x)] == x:
                out.add((m[:i], m[i + len(x):]))
    return frozenset(out)


def subs(L):
    return {m[i:j] for m in L for i in range(len(m) + 1) for j in range(i, len(m) + 1)}


def tri(L, X, DC):
    """X^|> for a finite set X of strings."""
    res = None
    for x in X:
        d = DC[x] if x in DC else dist(L, x)
        res = d if res is None else (res & d)
        if not res:
            break
    return res if res is not None else None  # None = all contexts (X empty)


def closure(L, K, SUB, DC):
    C = tri(L, K, DC)
    assert C, 'kernel must have a nonempty common context'
    return {x for x in SUB if C <= DC[x]}


def concat(parts):
    out = {''}
    for P in parts:
        out = {a + b for a in out for b in P}
    return out


def trial(rng, L, tname):
    SUB = subs(L)
    DC = {x: dist(L, x) for x in SUB}
    pos = [x for x in SUB if x and DC[x]]
    by_type = {}
    for x in pos:
        by_type.setdefault(T(tname, x), []).append(x)
    nnt = rng.choice([1, 2])
    Ks, ts = [], []
    for _ in range(nnt):
        t = rng.choice(list(by_type))
        cands = by_type[t]
        for _ in range(20):
            K = set(rng.sample(cands, min(len(cands), rng.choice([1, 2]))))
            if tri(L, K, DC):
                break
        else:
            return None
        Ks.append(K); ts.append(t)
    ws = [''.join(rng.choice(SIGMA) for _ in range(rng.choice([0, 0, 1, 2]))) for _ in range(nnt + 1)]
    P0, P1, P2 = [{ws[0]}], [{ws[0]}], [{ws[0]}]
    for K, t, w in zip(Ks, ts, ws[1:]):
        clK = closure(L, K, SUB, DC)
        clt = {x for x in clK if T(tname, x) == t}
        P0 += [K, {w}]; P1 += [clt, {w}]; P2 += [clK, {w}]
    S0, S1, S2 = concat(P0), concat(P1), concat(P2)
    D = lambda S: frozenset.intersection(*[dist(L, x) for x in S]) if S else None
    d0, d1, d2 = D(S0), D(S1), D(S2)
    ident = (d0 == d1 == d2)
    # rule-level equivalence for a random homogeneous K0 of the rule's type
    rtype = T(tname, next(iter(S0)))
    if any(T(tname, x) != rtype for x in S0):
        return ident, None
    cands = by_type.get(rtype)
    if not cands:
        return ident, None
    K0 = set(rng.sample(cands, min(len(cands), rng.choice([1, 2]))))
    if not tri(L, K0, DC):
        return ident, None
    cl0 = closure(L, K0, SUB, DC)
    cl0t = {x for x in cl0 if T(tname, x) == rtype}
    typed = S1 <= cl0t
    ordinary = S2 <= cl0
    return ident, (typed == ordinary)


def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20261123
    rng = random.Random(seed)
    stats = {'ident_ok': 0, 'ident_bad': 0, 'rule_ok': 0, 'rule_bad': 0, 'skipped': 0}
    for _ in range(trials):
        L = {''.join(rng.choice(SIGMA) for _ in range(rng.randint(1, 6))) for _ in range(rng.randint(3, 9))}
        tname = rng.choice(list(TYPINGS))
        res = trial(rng, L, tname)
        if res is None:
            stats['skipped'] += 1; continue
        ident, rule = res
        stats['ident_ok' if ident else 'ident_bad'] += 1
        if rule is not None:
            stats['rule_ok' if rule else 'rule_bad'] += 1
        if not ident or rule is False:
            print('COUNTEREXAMPLE', sorted(L), tname)
            return 1
    print(stats)
    return 0


if __name__ == '__main__':
    sys.exit(main())
