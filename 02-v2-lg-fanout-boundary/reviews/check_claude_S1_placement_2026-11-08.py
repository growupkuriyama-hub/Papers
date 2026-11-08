"""Checks for astra_S1_placement_2026-11-08.md (standard library only).
(1) Doubling chain: all solutions of the placement equations (E1)(E2) with P_n={(0,0)},
    every P_j on its diagonal, written as x-sets X_j.  Claim (Sec.1.3): X_j = X_1 ∩ [0,N-2^j]
    and X_1 is 2-periodic, so X_1 ∈ {evens, all} (if the lowest b-level is k: multiples of 2^k ...).
(2) Fibonacci chain F_k -> F_{k-1}F_{k-2} | m_k with random short codes: partial s_{U,2}
    closure (a subset of every C1 superset) already shows a factor relation between b-words.
"""
import sys, itertools, random
from collections import defaultdict

def is_prog(xs, top):
    # Theorem 1 (Astra) on the diagonal: gapless progression, first < d, top - last < d
    if len(xs) <= 1: return True
    d = xs[1]-xs[0]
    return all(b-a == d for a, b in zip(xs, xs[1:])) and xs[0] < d and top-xs[-1] < d

def solutions(n, k=1):
    N = 2**n
    M = lambda j: N - 2**j
    sols = []
    rng = list(range(0, M(k)+1))
    for mask in range(1 << len(rng)):
        X = {k: {x for i, x in enumerate(rng) if mask >> i & 1}}
        for j in range(k+1, n+1):
            X[j] = {x for x in X[j-1] if x <= M(j)}          # (E1)
        ok = X[n] == {0}
        for j in range(k+1, n+1):                            # (E2)
            h = 2**(j-1)
            if {x for x in X[j-1] if h <= x <= M(j-1)} != {x+h for x in X[j]}: ok = False
        if ok and is_prog(sorted(X[k]), M(k)): sols.append(sorted(X[k]))
    return sols

def substitutable_closure_violation(seed, Lmax):
    def typ(x): return 'b' in x
    L = set(seed)
    for _ in range(12):
        D = defaultdict(set)
        for w in L:
            for i in range(len(w)):
                for j in range(i+1, len(w)+1): D[w[i:j]].add((w[:i], w[j:]))
        parent = {}
        def f(x):
            while parent.get(x, x) != x: x = parent[x]
            return x
        by = defaultdict(list)
        for x, cs in D.items():
            for c in cs: by[(typ(x), c)].append(x)
        for xs in by.values():
            r = f(xs[0])
            for y in xs[1:]:
                if f(y) != r: parent[f(y)] = r
        cls = defaultdict(list)
        for x in D: cls[f(x)].append(x)
        new = set()
        for xs in cls.values():
            if len(xs) < 2: continue
            ctx = set().union(*(D[x] for x in xs))
            for x in xs:
                for l, r in ctx:
                    w = l+x+r
                    if w not in L and len(w) <= Lmax: new.add(w)
        L |= new
        bw = sorted((w for w in L if 'b' in w), key=len)
        for i, x in enumerate(bw):
            for y in bw[i+1:]:
                if len(y) > len(x) and x in y: return True
        if not new or len(L) > 20000: return False
    return False

if __name__ == '__main__':
    for n, k in [(3, 1), (4, 1), (4, 2), (5, 4)]:
        S = solutions(n, k); print('doubling n=%d, lowest b-level k=%d: steps of all solutions X_k:' % (n, k), sorted({(x[1]-x[0]) if len(x) > 1 else None for x in S}), len(S))
    random.seed(1)
    bw = [''.join(p) for L_ in range(1, 4) for p in itertools.product('ab', repeat=L_) if 'b' in p]
    for n in (4, 5, 6):
        viol = 0
        for t in range(30):
            ms = [random.choice(bw) for _ in range(n-1)]
            F = [{'a'}, {'aa', ms[0]}]
            for i in range(2, n): F.append({x+y for x in F[-1] for y in F[-2]} | {ms[i-1]})
            N = min(len(w) for w in F[-1] if 'b' not in w)
            viol += substitutable_closure_violation(F[-1], N+4)
        print('fibonacci chain n=%d (N=%d): antichain violation in partial closure %d/30' % (n, N, viol))
