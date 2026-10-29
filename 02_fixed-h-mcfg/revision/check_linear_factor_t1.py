"""Check for Proposition prop:linear-factor-sharp (main.tex, 2026-10-29).

Written from the definitions of main.tex, independently of the ChatGPT report
that proposed the family.

- Contexts: v0 [] v1 [] ... [] vd with inner v_i nonempty (Def. tuple occurrence).
- (f,s)-substitutability with trivial typing and window typing s_{1,1}.
- Grammar G_{q,k}: language, size formula, all rules used.
"""
from itertools import combinations
from collections import defaultdict
import sys


def words(q, M):
    return ['a' * i + 'd' + 'a' * (q - i) + 'c' * M + 'a' * (q - i) + 'd' + 'a' * i
            for i in range(q + 1)]


def occ(w, d):
    n = len(w)
    for cuts in combinations(range(n + 1), 2 * d):
        if any(cuts[2 * j] == cuts[2 * j + 1] for j in range(d)):
            continue  # components nonempty
        if any(cuts[2 * j + 1] == cuts[2 * j + 2] for j in range(d - 1)):
            continue  # inner separators nonempty
        x = tuple(w[cuts[2 * j]:cuts[2 * j + 1]] for j in range(d))
        E = (w[:cuts[0]],) + tuple(w[cuts[2 * j + 1]:cuts[2 * j + 2]] for j in range(d - 1)) + (w[cuts[-1]:],)
        yield x, E


def typ(v, kind):
    if kind == 'triv':
        return 0
    if kind == 'win11':
        return v if len(v) <= 1 else (v[0], v[-1])
    raise ValueError


def substitutable(J, d, kind='triv'):
    D = defaultdict(set)
    C = defaultdict(set)
    for w in J:
        for x, E in occ(w, d):
            D[x].add(E)
            C[E].add(x)
    for E, X in C.items():
        groups = defaultdict(list)
        for x in X:
            groups[tuple(typ(v, kind) for v in x)].append(x)
        for g in groups.values():
            for x in g[1:]:
                if D[x] != D[g[0]]:
                    return False, (E, g[0], x)
    return True, None


def grammar(q, k):
    # rules: (lhs, rhs list of symbols); nonterminals are tuples
    R = []
    for j in range(q + 1):
        R.append((('A', j), ['d', ('H', j), 'd']))
    for j in range(1, q + 1):
        R.append((('A', j), ['a', ('A', j - 1), 'a']))
    R.append((('H', 0), [('C', k)]))
    for j in range(1, q + 1):
        R.append((('H', j), ['a', ('H', j - 1), 'a']))
    R.append((('C', 0), ['c']))
    for t in range(1, k + 1):
        R.append((('C', t), [('C', t - 1), ('C', t - 1)]))
    V = {r[0] for r in R}
    size = len(V) + sum(1 + sum(isinstance(s, tuple) for s in rhs) + len(rhs) for _, rhs in R)
    return R, V, size


def lang(R, V):
    L = {A: set() for A in V}
    changed = True
    while changed:
        changed = False
        for A, rhs in R:
            parts = [{''}]
            for s in rhs:
                parts.append(L[s] if isinstance(s, tuple) else {s})
            cur = {''}
            for P in parts:
                cur = {u + v for u in cur for v in P}
            if not cur <= L[A]:
                L[A] |= cur
                changed = True
    return L


if __name__ == '__main__':
    print('== f=1, all subsets, trivial typing (implies every typing) ==')
    for q in range(1, 7):
        for M in (1, 2, 3, 4, 8):
            L = words(q, M)
            ok = all(substitutable([w for i, w in enumerate(L) if m >> i & 1], 1)[0]
                     for m in range(1 << len(L)))
            print(f'q={q} M={M} subsets={1 << len(L)} all_1-substitutable={ok}')
            if not ok:
                sys.exit('FAIL')
    print('== grammar G_{q,k} ==')
    for q in range(1, 7):
        for k in range(1, q + 1):
            R, V, size = grammar(q, k)
            L = lang(R, V)
            M = 2 ** k
            assert L[('A', q)] == set(words(q, M)), (q, k)
            assert size == 17 * q + 6 * k + 13, (q, k, size)
            W = M + 2 * q + 2
            Fplus = (q + 1) * (W + 1)
            assert 23 * Fplus >= size * W
    print('language, size 17q+6k+13 and ||F||_+ >= ||G||W/23 verified for 1<=k<=q<=6')
    print('== f=2: the counterexample stated after the proposition (L_{2,1}) ==')
    L21 = set(words(2, 2))
    x, y = ('d', 'ac'), ('da', 'c')
    shared = lambda t: t[0] + 'a' + t[1] + 'caad'
    dist = lambda t: t[0] + 'ac' + t[1] + 'aad'
    assert shared(x) in L21 and shared(y) in L21
    assert dist(y) in L21 and dist(x) not in L21
    print('[]a[]caad accepts both; []ac[]aad accepts only (da,c): verified')
    print('== f=2, other parameters (window typing s_{1,1} keeps the short-word tag) ==')
    for q, M in ((2, 1), (3, 1), (3, 2), (4, 4)):
        L = words(q, M)
        for kind in ('triv', 'win11'):
            print(f'q={q} M={M} d=2 {kind}:', substitutable(L, 2, kind)[0])
    print('singleton {aadcdaa} d=2 triv:', substitutable(['aadcdaa'], 2)[0])
