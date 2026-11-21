"""Checks for reviews/claude_compression_review_2026-11-02.md (Python 3, standard library only).

Part J: the 11 minimal two-hole violations over {a,b} and the run-length case split
        (every word of length 7..MAXLEN outside the shapes contains the predicted word).
Part B: Clark-Eyraud substitutability of h(L_n) for h: a->ab, b->aab, c->abb, n <= 3
        (observation only; no claim for general n).
Run:  py -3 check_claude_compression_2026-11-02.py
"""
import itertools

MAXLEN = 14

def violation(W):
    """Return (E, x, y, F) with E[x]=E[y]=F[x]=W != F[y] for arity 2, or None."""
    n = len(W); byE = {}; ctx = {}
    for i1 in range(n):
        for j1 in range(i1 + 1, n):
            for i2 in range(j1 + 1, n):
                for j2 in range(i2 + 1, n + 1):
                    E = (W[:i1], W[j1:i2], W[j2:]); x = (W[i1:j1], W[i2:j2])
                    byE.setdefault(E, []).append(x); ctx.setdefault(x, []).append(E)
    for E, xs in byE.items():
        for x in xs:
            for y in xs:
                if x != y:
                    for F in ctx[x]:
                        if F[0] + y[0] + F[1] + y[1] + F[2] != W:
                            return (E, x, y, F)
    return None

MIN = ['aaabb', 'aabba', 'aaaaba', 'aaabaa', 'aaabab', 'aababa', 'aababb',
       'abaaab', 'ababba', 'aabaaba', 'abbabba']

def orbit(w):
    sw = w.translate(str.maketrans('ab', 'ba'))
    return {w, w[::-1], sw, sw[::-1]}

def runs(W):
    return [len(list(g)) for _, g in itertools.groupby(W)]

def shape(W):
    r = runs(W); n = len(W)
    return (len(r) == 1 or r in ([n - 1, 1], [1, n - 1])
            or (len(r) == 3 and r[0] == 1 == r[2]) or all(l == 1 for l in r))

def case(W):
    L = runs(W); longs = [i for i, l in enumerate(L) if l >= 2]
    if any(L[i] >= 2 and L[i + 1] >= 2 for i in range(len(L) - 1)):
        return 'C1'
    if len(longs) >= 2:
        k = min(j - i for i, j in zip(longs, longs[1:])) - 1
        return 'C2k=%d' % min(k, 3)
    return 'C3m=%d' % min(L[longs[0]], 4)

PRED = {'C1': ['aaabb', 'aabba'], 'C2k=1': ['aaabaa', 'aabaaba', 'abbabba'],
        'C2k=2': ['aababb'], 'C2k=3': ['aababa'], 'C3m=4': ['aaaaba'],
        'C3m=3': ['aaabab', 'abaaab'], 'C3m=2': ['aababa', 'ababba']}

def part_J():
    for W in MIN:
        v = violation(W)
        assert v is not None, W
        # minimality: every proper factor passes
        for i in range(len(W)):
            for j in range(i + 1, len(W) + 1):
                if (i, j) != (0, len(W)):
                    assert violation(W[i:j]) is None, (W, W[i:j])
        print('violation', W, v)
    misses = 0
    for n in range(7, MAXLEN + 1):
        for t in itertools.product('ab', repeat=n):
            W = ''.join(t)
            if shape(W):
                continue
            if not any(o in W for m in PRED[case(W)] for o in orbit(m)):
                misses += 1
    print('case split: lengths 7..%d, misses = %d' % (MAXLEN, misses))

def Ln(n):
    L = {'a'}
    for _ in range(n):
        L = {'b' + x + y + 'b' for x in L for y in L} | {'c' + x + 'c' for x in L}
    return L

def clark_eyraud(L):
    D = {}
    for w in L:
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                D.setdefault(w[i:j], set()).add((w[:i], w[j:]))
    by_ctx = {}
    for x, cs in D.items():
        for c in cs:
            by_ctx.setdefault(c, []).append(x)
    for c, xs in by_ctx.items():
        for x in xs[1:]:
            if D[x] != D[xs[0]]:
                return (xs[0], x, c)
    return None

def part_B():
    h = {'a': 'ab', 'b': 'aab', 'c': 'abb'}
    for n in (1, 2, 3):
        H = {''.join(h[ch] for ch in w) for w in Ln(n)}
        typ_e = [w for w in H if 'bb' not in w]
        print('n=%d |H|=%d substitutable=%s words without bb: %d (length %d)'
              % (n, len(H), clark_eyraud(H) is None, len(typ_e), len(typ_e[0])))

if __name__ == '__main__':
    part_J()
    part_B()
