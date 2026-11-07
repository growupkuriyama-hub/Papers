#!/usr/bin/env python3
"""check_claude_verify_astra_cw_2026-11-07.py  (standard library only)

Claude-side check of Astra's report on (CW) (README (196)); no code of the Astra script.
  1. one-edge-per-letter digraphs: brute-force canonical forms of all maps of the 6 endpoints
     (tail a, head a, tail b, head b, tail c, head c) to vertices, up to vertex renaming -> count;
  2. classes by explicit word enumeration (length <= 8): long ab-walk (content ab, length >= 3),
     interior c (a word with a, b and a c not in first/last position);
  3. lattices C_x^M, D_stM from explicit walks up to length L in {8, 11}; (CW1)-(CW3) on the
     17 relevant types, stability in L, and the failing pair outside the 17.
Run: python3 check_claude_verify_astra_cw_2026-11-07.py   (about 1 minute)
"""
import itertools
from collections import Counter

def canon(f):
    m, out = {}, []
    for x in f:
        if x not in m: m[x] = len(m)
        out.append(m[x])
    return tuple(out)

def all_graphs():
    return sorted({canon(f) for f in itertools.product(range(6), repeat=6)})

def words(g, L):
    E = {'a': (g[0], g[1]), 'b': (g[2], g[3]), 'c': (g[4], g[5])}
    layer = [(ch, E[ch][0], E[ch][1]) for ch in 'abc']
    out = list(layer)
    for _ in range(L - 1):
        nxt = [(w + ch, s, E[ch][1]) for w, s, t in layer for ch in 'abc' if E[ch][0] == t]
        out += nxt; layer = nxt
    return out

def parikh(w): return (w.count('a'), w.count('b'), w.count('c'))
def cont(w): return frozenset(w)
def sub(p, q): return tuple(x - y for x, y in zip(p, q))

def echelon(vecs):
    rows = [list(v) for v in vecs if any(v)]; basis = []
    for col in range(3):
        while True:
            idx = [i for i, r in enumerate(rows) if r[col]]
            if len(idx) <= 1: break
            idx.sort(key=lambda i: abs(rows[i][col])); p = rows[idx[0]]
            rows = [r if (i == idx[0] or not r[col]) else [x - (r[col] // p[col]) * y for x, y in zip(r, p)]
                    for i, r in enumerate(rows)]
            rows = [r for r in rows if any(r)]
        idx = [i for i, r in enumerate(rows) if r[col]]
        if idx:
            p = rows.pop(idx[0]); basis.append(p if p[col] > 0 else [-x for x in p])
    return basis

def member(v, B):
    v = list(v)
    for r in B:
        j = next(i for i, x in enumerate(r) if x)
        if v[j] % r[j]: return False
        q = v[j] // r[j]; v = [x - q * y for x, y in zip(v, r)]
    return not any(v)

def subl(A, B): return all(member(a, B) for a in A)
def eq(A, B): return subl(A, B) and subl(B, A)

def lattices(g, L):
    W = words(g, L); V = set(g)
    C = {(x, M): echelon({parikh(w) for w, s, t in W if s == t == x and cont(w) <= M})
         for x in V for M in (frozenset('ab'), frozenset('abc'))}
    D, base = {}, {}
    for s in V:
        for t in V:
            for M in (frozenset('ab'), frozenset('abc')):
                ps = sorted({parikh(w) for w, a, b in W if (a, b) == (s, t) and cont(w) == M})
                if ps: base[s, t, M] = min(ps); D[s, t, M] = echelon({sub(p, min(ps)) for p in ps})
    return C, D, base

def cw(g, L):
    C, D, base = lattices(g, L); AB, ABC = frozenset('ab'), frozenset('abc'); bad = []
    pairs = {(s, t) for s, t, M in D}
    for s, t in pairs:
        for M in (AB, ABC):
            if (s, t, M) in D and not subl(D[s, t, M], C[s, M] + C[t, M]): bad.append((s, t, 'CW1', ''.join(sorted(M))))
        if (s, t, AB) in D and (s, t, ABC) in D:
            CC = C[s, ABC] + C[t, ABC]
            if not any(r[2] for r in CC): bad.append((s, t, 'CW2c'))
            if not member(sub(base[s, t, ABC], base[s, t, AB]), CC): bad.append((s, t, 'CW2'))
            if not any(subl(D[s, t, AB], C[r, AB]) for r in set(g[:4])): bad.append((s, t, 'CW3'))
    return bad, len(pairs), (C, D)

def main():
    G = all_graphs()
    print('graphs:', len(G), ' by #vertices:', sorted(Counter(max(g) + 1 for g in G).items()))
    cls = {}
    for g in G:
        W = words(g, 8)
        longab = any(cont(w) == frozenset('ab') and len(w) >= 3 for w, s, t in W)
        inter = any({'a', 'b'} <= set(w) and 'c' in w[1:-1] for w, s, t in W)
        anyab = any(cont(w) == frozenset('ab') for w, s, t in W)
        cls[g] = (longab, inter, anyab)
    print('classes (longab, interior c, has ab):', sorted(Counter(cls.values()).items()))
    sel = [g for g in G if cls[g][0] and cls[g][1]]
    print('relevant types:', len(sel))
    tot, bad, unstable = 0, 0, 0
    for g in sel:
        b8, n8, L8 = cw(g, 8); b11, n11, L11 = cw(g, 11)
        tot += n11; bad += len(b11)
        C8, D8 = L8; C11, D11 = L11
        if set(D8) != set(D11) or any(not eq(C8[k], C11[k]) for k in C8) or any(not eq(D8[k], D11[k]) for k in D8):
            unstable += 1
    print('endpoint pairs:', tot, ' CW violations:', bad, ' lattices unstable 8->11:', unstable)
    g = canon((0, 1, 1, 2, 1, 1))   # a:0->1, b:1->2, c:1->1
    print('outside example', g, 'class', cls[g], 'CW failures:', cw(g, 11)[0])

if __name__ == '__main__':
    main()
