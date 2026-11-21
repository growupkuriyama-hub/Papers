#!/usr/bin/env python3
"""Search for j<j' with equal GLOBAL colour but some Psi(R cap phi_kappa) not a circulation.
Self-contained; standard library; fixed seeds."""
import random, sys
from collections import Counter
sys.setrecursionlimit(10000)
LET = {'a': (0, 1), 'b': (1, 0), 'c': (0, 0), 'e': (1, 1)}
L4 = 'abce'
def T(x): return ('t', x)
def V(i, j): return ('v', i, j)
RULE = {
 'B0': ('B', [], [[T('c')], [T('e')]]),
 'B1': ('B', ['B'], [[T('c'), V(0, 0)], [V(0, 1), T('e')]]),
 'B4': ('B', ['B', 'B'], [[V(0, 0), V(1, 0)], [V(0, 1), V(1, 1)]]),
 'P0': ('P', [], [[T('a')], [T('b')]]),
 'P1': ('P', ['P'], [[T('c'), V(0, 0), T('e')], [V(0, 1)]]),
 'P3': ('P', ['B', 'P'], [[V(0, 0), V(1, 0)], [V(0, 1), V(1, 1)]]),
 'P5': ('P', ['B', 'P'], [[V(0, 0), V(1, 0), V(0, 1)], [V(1, 1)]]),
 'P6': ('P', ['P', 'P'], [[V(0, 0), T('e'), V(0, 1), T('c'), V(1, 0)], [V(1, 1)]]),
}
SHORT = {'B': [['c'], ['e']], 'P': [['a'], ['b']]}
def circ(p):
    bal = Counter()
    for a, n in p.items():
        bal[LET[a][0]] -= n; bal[LET[a][1]] += n
    return all(v == 0 for v in bal.values())
class N: pass
def gen(nt, b, rng, cnt):
    n = N(); n.nt = nt
    if nt == 'B':
        r = 'B0' if b <= 1 else rng.choice(['B1', 'B1', 'B4'])
    else:
        r = 'P0' if b <= 1 else rng.choice(['P1', 'P3', 'P5', 'P6'])
    n.r = r; n.tid = []
    for comp in RULE[r][2]:
        for it in comp:
            if it[0] == 't':
                cnt[0] += 1; n.tid.append(cnt[0])
    ch = RULE[r][1]
    n.ch = [gen(c, max(1, b // len(ch) - 1), rng, cnt) for c in ch]
    for c in n.ch: c.parent = n
    return n
def yld(n, L):
    tpl = RULE[n.r][2]; cy = [yld(c, L) for c in n.ch]; out = []; k = 0
    for comp in tpl:
        cc = []
        for it in comp:
            if it[0] == 't':
                L[n.tid[k]] = it[1]; cc.append(n.tid[k]); k += 1
            else:
                cc += cy[it[1]][it[2]]
        out.append(cc)
    return out
def nodes(n):
    out = [n]
    for c in n.ch: out += nodes(c)
    return out
def run(seed):
    rng = random.Random(seed)
    eta = gen('P', rng.randint(4, 14), rng, [0]); eta.parent = None
    Lt = {}; ey = yld(eta, Lt)
    kap = {p: k for k, comp in enumerate(ey) for p in comp}
    cnt = [0]
    def iv(n):
        n.lo = cnt[0]
        if not n.ch: cnt[0] += 1
        for c in n.ch: iv(c)
        n.hi = cnt[0]
    iv(eta); q = cnt[0]
    allN = nodes(eta)
    pos = {}
    for n in reversed(allN):
        pos[id(n)] = set(n.tid).union(*[pos[id(c)] for c in n.ch]) if n.ch else set(n.tid)
    data = []
    for j in range(q + 1):
        I = [n for n in allN if n.hi <= j and (n is eta or n.parent.hi > j)]
        U = set().union(*[pos[id(n)] for n in I]) if I else set()
        col = [Counter(), Counter()]
        for n in I:
            for m, comp in enumerate(yld(n, {})):
                col[kap[comp[0]]].update(SHORT[n.nt][m])
        data.append((U, col))
    for j in range(q + 1):
        for jp in range(j + 1, q + 1):
            g1 = data[j][1][0] + data[j][1][1]; g2 = data[jp][1][0] + data[jp][1][1]
            if g1 == g2:
                R = data[jp][0] - data[j][0]
                zs = [Counter(Lt[p] for p in R if kap[p] == k) for k in range(2)]
                if not all(circ(z) for z in zs):
                    return dict(seed=seed, j=j, jp=jp, q=q,
                                phi=[''.join(Lt[p] for p in comp) for comp in ey],
                                R_in_phi=[''.join(Lt[p] for p in comp if p in R) for comp in ey],
                                col_j=[dict(c) for c in data[j][1]], col_jp=[dict(c) for c in data[jp][1]])
    return None
found = None
for s in range(20000):
    found = run(s)
    if found: break
print(found)
