#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_debruijn_local_counting_2026-11-14.py  (Python 3, standard library only, fixed seeds)

Runs, on concrete derivation trees of a good fan-out-2 / rank-2 MCFG, the constructive
proof of Theorem L (round-4 report): ell-local counting languages, i.e. languages whose
membership depends only on (s_{ell-1,ell-1}(w), N_ell(w)), with N_ell the vector of
ell-factor counts.  Every intermediate claim is checked by asserts:

  * marks = all positions of the first CM occurrences of each ell-window in each root
    component; W2 (frequency gap) on de Bruijn edges; rare windows completely marked;
  * internal windows of a free factor are frequent and lie in one interval (one J);
  * Lemma P1^ell: with colour (s_ell(psi_kappa), Imp_kappa) per eta-component kappa,
      N_ell(psi^(j)_kappa) - N_ell(psi^(j')_kappa) = Z_kappa
        (= windows of phi_kappa missing U_j and meeting U_j'), Z_kappa >= 0,
      Z_kappa is a circulation of D_ell, and N_ell(W_j) - N_ell(W_j') = sum_kappa Z_kappa;
  * control: round-3 colour (letter Parikh of replaced material per kappa) -- counts how
    often the identity N(W_j)-N(W_j') = sum Z_kappa or circularity fails;
  * Lemma Y: y^pi realises the current edge counts N_i with the same window type,
    content, rare skeleton, exposing t at u_J; y' = y^pi with t -> h has N_i - Z;
  * Lemma F: W' (flexible runs of W_j' Euler-rewired) has N_ell(W') = N_ell(W_j'),
    F[h] = W' in L, F[t] in L with N_ell(F[t]) = N_ell(W_j), separators nonempty,
    hole order equal to that of F_{E_A};
  * t and h have equal (content, s_ell) type;
  * final tuple: same window types and contents as x; random admissible contexts E
    are checked to satisfy E[x] in L  <=>  E[y_final] in L (end-to-end equivalence on
    samples; uses the explicit L, not the proof).

Target (ell = 2 or 3): Sigma = {a,b},
   L = { w : w starts and ends with a, b^ell is not a factor, |w|_a = 2|w|_b }.
L is SL_ell intersected with an abelian coset, hence (f, c x s_ell)-substitutable
(main.tex prop:abelian-coset-filter + SL argument in the report) and a CFL.
Asserts check the bookkeeping on finite trees; they are not a proof.

usage: python3 check_debruijn_local_counting_2026-11-14.py ELL
"""
import random
import sys
from collections import Counter, defaultdict

ELL = int(sys.argv[1]) if len(sys.argv) > 1 else 3
assert ELL in (2, 3)
SIG = ('a', 'b')
FORB = tuple('b' * ELL)


def all_tuples(n):
    out = [()]
    for _ in range(n):
        out = [t + (c,) for t in out for c in SIG]
    return out


EDGES = [e for e in all_tuples(ELL) if e != FORB]
K = len(EDGES)


def tl(e):
    return e[:-1]


def hd(e):
    return e[1:]


def windows(word):
    return [tuple(word[t - ELL + 1:t + 1]) for t in range(ELL - 1, len(word))]


def Nl(word):
    return Counter(windows(word))


def stype(word):
    m0 = 2 * (ELL - 1)
    if len(word) < m0:
        return ('S', tuple(word))
    return ('P', tuple(word[:ELL - 1]), tuple(word[len(word) - ELL + 1:]))


def in_L(w):
    return (len(w) > 0 and w[0] == 'a' and w[-1] == 'a'
            and FORB not in set(windows(w)) and w.count('a') == 2 * w.count('b'))


def csub(p, q):
    r = Counter(p)
    r.subtract(q)
    return {e: v for e, v in r.items() if v != 0}


def cadd(p, q):
    r = Counter(p)
    r.update(q)
    return r


def is_circ(z):
    bal = Counter()
    for e, n in z.items():
        bal[tl(e)] -= n
        bal[hd(e)] += n
    return all(v == 0 for v in bal.values())


def word_of_walk(start, edges):
    return list(start) + [e[-1] for e in edges]


# --------------------------------------------------------------------------- grammar
def T(x):
    return ('t', x)


def V(i, j):
    return ('v', i, j)


RULES = {
    'B': [
        ('B0', [], [[T('a')], [T('a')]]),
        ('B1', ['B'], [[V(0, 0), T('b'), T('a'), T('a')], [V(0, 1)]]),
        ('B2', ['B'], [[T('a'), T('a'), T('b'), V(0, 0)], [V(0, 1)]]),
        ('B2p', ['B'], [[V(0, 0)], [T('a'), T('b'), T('a'), V(0, 1)]]),
        ('B3', ['B'], [[V(0, 0), T('b'), T('b'), T('a'), T('a'), T('a'), T('a')], [V(0, 1)]]),
        ('B4', ['B', 'B'], [[V(0, 0), T('b'), V(1, 0)], [V(0, 1), V(1, 1)]]),
        ('B5', ['B', 'B'], [[V(0, 0), T('b'), V(1, 0)], [V(1, 1), V(0, 1)]]),            # crossing
        ('B6', ['B', 'B'], [[V(0, 0), T('b'), V(0, 1), T('a'), T('a'), T('b'), V(1, 0)], [V(1, 1)]]),  # moving
        ('B7', ['B', 'C'], [[V(0, 0), T('b'), V(1, 0)], [V(0, 1)]]),
        ('B9', ['B'], [[V(0, 0), T('b'), T('a'), T('b'), T('a')], [V(0, 1), T('a'), T('a')]]),
        ('B10', ['B'], [[V(0, 0), T('a'), T('a')], [V(0, 1), T('b'), T('a'), T('b'), T('a')]]),
    ],
    'C': [
        ('C0', [], [[T('a'), T('a'), T('b'), T('a'), T('a')]]),
        ('C1', ['C', 'C'], [[V(0, 0), T('b'), V(1, 0)]]),
        ('C2', ['B'], [[V(0, 0), T('a'), T('b'), T('a'), V(0, 1)]]),
    ],
}
if ELL == 2:
    RULES['B'] = [r for r in RULES['B'] if r[0] != 'B3']
FAN = {'B': 2, 'C': 1}
SHORT = {'B': [['a'], ['a']], 'C': [['a', 'a', 'b', 'a', 'a']]}
RULE = {r[0]: r for nt in RULES for r in RULES[nt]}
UNARY = ['B1', 'B2', 'B2p', 'B9', 'B10', 'B9', 'B10']


def check_good():
    for nt, rs in RULES.items():
        for name, ch, tpl in rs:
            assert len(tpl) == FAN[nt]
            assert all(len(c) > 0 for c in tpl)
            occ = [(it[1], it[2]) for comp in tpl for it in comp if it[0] == 'v']
            want = [(i, j) for i, c in enumerate(ch) for j in range(FAN[c])]
            assert sorted(occ) == sorted(want)
            for i, c in enumerate(ch):
                assert [j for (ii, j) in occ if ii == i] == list(range(FAN[c]))
            for comp in tpl:
                for x, y in zip(comp, comp[1:]):
                    assert not (x[0] == 'v' and y[0] == 'v' and x[1] == y[1] and y[2] == x[2] + 1)


class Node:
    __slots__ = ('nt', 'rule', 'ch', 'tid', 'parent', 'lo', 'hi', 'uid')


UID = [0]
POS = [0]
P2 = [0.03]
P6 = [0.0]
CH2 = [['B4', 'B4', 'B5', 'B6', 'B7']]


def gen(nt, budget, rng, mode, rare_p):
    n = Node()
    n.nt = nt
    UID[0] += 1
    n.uid = UID[0]
    if nt == 'B':
        if budget <= 1:
            choice = 'B0'
        elif budget >= 6 and rng.random() < P6[0]:
            choice = 'B6'
        else:
            x = rng.random()
            if x < rare_p:
                choice = rng.choice([r for r in ('B3', 'B6', 'B7', 'B5') if r in RULE])
            elif budget >= 6 and x < rare_p + P2[0]:
                choice = rng.choice(CH2[0])
            elif x < 0.85:
                choice = mode
            else:
                choice = rng.choice(UNARY)
    else:
        if budget <= 1:
            choice = 'C0'
        else:
            x = rng.random()
            choice = 'C2' if x < 0.6 else ('C1' if budget >= 6 and x < 0.7 else 'C0')
    name, ch, tpl = RULE[choice]
    n.rule = name
    n.tid = []
    for comp in tpl:
        for it in comp:
            if it[0] == 't':
                POS[0] += 1
                n.tid.append(POS[0])
    if len(ch) == 0:
        n.ch = []
    elif len(ch) == 1:
        n.ch = [gen(ch[0], budget - 1, rng, mode, rare_p)]
    else:
        b1 = rng.randint(1, max(1, budget - 2))
        m1 = rng.choice(UNARY) if rng.random() < 0.5 else mode
        m2 = rng.choice(UNARY)
        n.ch = [gen(ch[0], b1, rng, m1, rare_p), gen(ch[1], max(1, budget - 1 - b1), rng, m2, rare_p)]
    for c in n.ch:
        c.parent = n
    return n


def mk(rule, rng, kids):
    """build a node with a fixed rule; kids are thunks producing the children"""
    n = Node()
    name, ch, tpl = RULE[rule]
    n.nt = 'B' if rule.startswith('B') else 'C'
    UID[0] += 1
    n.uid = UID[0]
    n.rule = name
    n.tid = []
    for comp in tpl:
        for it in comp:
            if it[0] == 't':
                POS[0] += 1
                n.tid.append(POS[0])
    n.ch = [k() for k in kids]
    for c in n.ch:
        c.parent = n
    return n


def gen_p2(by, rng):
    """eta-candidate built only from B9 (cycle aba/bab in comp 0, loop aaa in comp 1), B4, B5, B0"""
    if by <= 1:
        return mk('B0', rng, [])
    if by >= 6 and rng.random() < 0.15:
        b1 = rng.randint(2, by - 3)
        return mk(rng.choice(['B4', 'B5']), rng, [lambda: gen_p2(b1, rng), lambda: gen_p2(by - 1 - b1, rng)])
    return mk('B9', rng, [lambda: gen_p2(by - 1, rng)])


def chain(rules, rng):
    if not rules:
        return mk('B0', rng, [])
    return mk(rules[0], rng, [lambda: chain(rules[1:], rng)])


def targeted_root(rng, bx, by):
    # root = B4( x , B6( eta-candidate , B0 ) ),  x = B10^m B9^n B0 (two cycle blocks, rare transitions)
    m = bx // 2 + rng.randint(0, 20)
    n = bx // 2 + rng.randint(0, 20)
    return mk('B4', rng, [lambda: chain(['B10'] * m + ['B9'] * n, rng),
                         lambda: mk('B6', rng, [lambda: gen_p2(by, rng),
                                                lambda: gen('B', 1, rng, 'B1', 0.0)])])


def yield_of(n, repl, fresh):
    if n.uid in repl:
        out = []
        for comp in repl[n.uid]:
            cc = []
            for x in comp:
                fresh[0] -= 1
                cc.append((fresh[0], x))
            out.append(cc)
        return out
    name, ch, tpl = RULE[n.rule]
    cy = [yield_of(c, repl, fresh) for c in n.ch]
    out, k = [], 0
    for comp in tpl:
        cc = []
        for it in comp:
            if it[0] == 't':
                cc.append((n.tid[k], it[1]))
                k += 1
            else:
                cc.extend(cy[it[1]][it[2]])
        out.append(cc)
    return out


def nodes_of(n):
    st, out = [n], []
    while st:
        x = st.pop()
        out.append(x)
        st.extend(reversed(x.ch))
    return out


def pos_set(n, memo):
    if n.uid in memo:
        return memo[n.uid]
    s = set(n.tid)
    for c in n.ch:
        s |= pos_set(c, memo)
    memo[n.uid] = s
    return s


def leaf_intervals(eta):
    cnt = [0]

    def rec(n):
        n.lo = cnt[0]
        if not n.ch:
            cnt[0] += 1
        for c in n.ch:
            rec(c)
        n.hi = cnt[0]
    rec(eta)
    return cnt[0]


# --------------------------------------------------------------------------- graph tools
def bfs_path(u, v, J):
    if u == v:
        return []
    prev = {u: None}
    q = [u]
    while q:
        nq = []
        for x in q:
            for e in sorted(J):
                if tl(e) == x and hd(e) not in prev:
                    prev[hd(e)] = (x, e)
                    nq.append(hd(e))
        q = nq
    assert v in prev
    path, x = [], v
    while x != u:
        y, e = prev[x]
        path.append(e)
        x = y
    return path[::-1]


def euler(counts, s, t):
    tot = sum(counts.values())
    assert all(v >= 0 for v in counts.values())
    if tot == 0:
        assert s == t
        return []
    adj = defaultdict(list)
    for e in sorted(counts):
        for _ in range(counts[e]):
            adj[tl(e)].append(e)
    stack, out = [(s, None)], []
    while stack:
        v, e = stack[-1]
        if adj[v]:
            f = adj[v].pop()
            stack.append((hd(f), f))
        else:
            stack.pop()
            if e is not None:
                out.append(e)
    out.reverse()
    assert len(out) == tot, 'not connected'
    for e1, e2 in zip(out, out[1:]):
        assert hd(e1) == tl(e2)
    assert out[0][:-1] == s and hd(out[-1]) == t
    assert Counter(out) == Counter({e: c for e, c in counts.items() if c})
    return out


def cover_walk(u, J):
    h = []
    for e in sorted(J):
        h += bfs_path(u, tl(e), J) + [e] + bfs_path(hd(e), u, J)
    assert set(h) == set(J)
    return h


def verts(J):
    return {tl(e) for e in J} | {hd(e) for e in J}


def strongly_connected(J):
    vs = verts(J)
    if not vs:
        return True
    v0 = min(vs)
    for fw in (True, False):
        seen, st = {v0}, [v0]
        while st:
            x = st.pop()
            for e in J:
                a, b = (tl(e), hd(e)) if fw else (hd(e), tl(e))
                if a == x and b not in seen:
                    seen.add(b)
                    st.append(b)
        if seen != vs:
            return False
    return True


def weak_components(edges):
    comps, rem = [], set(edges)
    while rem:
        e = rem.pop()
        comp, vs = {e}, {tl(e), hd(e)}
        ch = True
        while ch:
            ch = False
            for f in list(rem):
                if {tl(f), hd(f)} & vs:
                    rem.discard(f)
                    comp.add(f)
                    vs |= {tl(f), hd(f)}
                    ch = True
        comps.append(frozenset(comp))
    return comps


# --------------------------------------------------------------------------- proof
STATS = Counter()
WIT = {}


class Skip(Exception):
    pass


def realise(i, N, ctx, hole=None):
    """Lemma Y: rebuild component i (skeleton of x_i) with edge counts N; optionally expose
    closed walk tword (edge list) for hole=(J, anchor_interval_index, tedges)."""
    xw, win, ivs, rare_idx, Jof_i = ctx['xw'][i], ctx['win'][i], ctx['ivs'][i], ctx['rare'][i], ctx['Jof'][i]
    if len(xw) < 2 * (ELL - 1) or not win:
        assert hole is None or not hole
        return list(xw), {}
    byJ = defaultdict(list)
    for iv in ivs:
        byJ[iv[2]].append(iv)
    routed, offs_local = {}, {}
    hole = hole or {}
    for J, lst in byJ.items():
        M = {e: N.get(e, 0) for e in J}
        if J in hole:
            anchor, tedges = hole[J]
            main = lst[anchor]
        else:
            main, tedges = lst[0], None
        paths = {}
        for iv in lst:
            if iv is not main:
                p, q = tl(win[iv[0]][1]), hd(win[iv[1] - 1][1])
                paths[iv] = bfs_path(p, q, J)
        R = dict(M)
        for pa in paths.values():
            for e in pa:
                R[e] -= 1
        p, q = tl(win[main[0]][1]), hd(win[main[1] - 1][1])
        pre = []
        if tedges is not None:
            uJ = min(verts(J))
            pre = bfs_path(p, uJ, J)
            for e in pre + tedges:
                R[e] -= 1
            if not all(R[e] >= 1 for e in J):
                raise Skip('Y-material')
            routed[main] = (pre, tedges, euler(R, uJ, q))
        else:
            if not all(R[e] >= 1 for e in J):
                raise Skip('Y-material0')
            routed[main] = ([], [], euler(R, p, q))
        for iv, pa in paths.items():
            routed[iv] = ([], [], pa)
    edges, k, holepos = [], 0, {}
    starts = {iv[0]: iv for iv in ivs}
    while k < len(win):
        if k in starts:
            iv = starts[k]
            pre, te, rest = routed[iv]
            edges += pre
            if te:
                holepos[iv[2]] = len(edges)
            edges += te + rest
            k = iv[1]
        else:
            assert k in rare_idx
            edges.append(win[k][1])
            k += 1
    for e1, e2 in zip(edges, edges[1:]):
        assert hd(e1) == tl(e2)
    word = word_of_walk(tuple(xw[:ELL - 1]), edges)
    # offsets in the word: edge index m <-> letter index m + ELL - 1
    offs = {J: holepos[J] + ELL - 1 for J in holepos}
    return word, offs


def run_tree(seed, budget, CM, rare_p, p2=0.03, p6=0.0, targeted=False):
    rng = random.Random(seed)
    P2[0] = p2
    P6[0] = p6
    UID[0] = 0
    POS[0] = 0
    if targeted:
        CH2[0] = ['B4', 'B5']
        root = targeted_root(rng, budget, budget // 3)
        CH2[0] = ['B4', 'B4', 'B5', 'B6', 'B7']
    else:
        root = gen('B', budget, rng, rng.choice(UNARY), rare_p)
    root.parent = None
    x = yield_of(root, {}, [0])
    xw = [[l for _, l in c] for c in x]
    w = xw[0] + ['b'] + xw[1]
    assert in_L(w)
    d = 2
    letters_of, comp_of, idx_of = {}, {}, {}
    for i, comp in enumerate(x):
        for t_, (pid, l) in enumerate(comp):
            letters_of[pid] = l
            comp_of[pid] = i
            idx_of[pid] = t_
    styp = [stype(c) for c in xw]
    cont = [set(c) for c in xw]
    win = [[(t, tuple(xw[i][t - ELL + 1:t + 1]), tuple(p for p, _ in x[i][t - ELL + 1:t + 1]))
            for t in range(ELL - 1, len(xw[i]))] for i in range(d)]
    marks = set()
    for i in range(d):
        seen = Counter()
        for t, e, ps in win[i]:
            if seen[e] < CM:
                marks |= set(ps)
            seen[e] += 1
    thr = [K ** g for g in range(K + 2)]
    ivs, rare, Jof, freq = [], [], [], []
    for i in range(d):
        n = Counter(e for _, e, _ in win[i])
        if not n:
            ivs.append([])
            rare.append(set())
            Jof.append({})
            freq.append(set())
            continue
        g = next(gi for gi in range(K + 1) if not any(thr[gi] <= n[e] < thr[gi + 1] for e in n))
        fr = {e for e in n if n[e] >= thr[g + 1]}
        ra = {e for e in n if n[e] < thr[g]}
        assert fr | ra == set(n)
        Js = weak_components(fr)
        for J in Js:
            assert strongly_connected(J), 'W2 failed'
            STATS['W2 frequent components'] += 1
        for t, e, ps in win[i]:
            if e in ra and not set(ps) <= marks:
                return 'rare-unmarked'
        jof = {e: J for J in Js for e in J}
        iv, cur = [], None
        for k_, (t, e, ps) in enumerate(win[i]):
            if e in fr:
                if cur is None:
                    cur = [k_, k_ + 1, jof[e]]
                else:
                    assert jof[e] == cur[2], 'interval meets two J'
                    cur[1] = k_ + 1
            else:
                if cur is not None:
                    iv.append(tuple(cur))
                cur = None
        if cur is not None:
            iv.append(tuple(cur))
        ivs.append(iv)
        rare.append({k_ for k_, (t, e, ps) in enumerate(win[i]) if e in ra})
        Jof.append(jof)
        freq.append(fr)
    ctx = {'xw': xw, 'win': win, 'ivs': ivs, 'rare': rare, 'Jof': Jof}

    allnodes = nodes_of(root)
    memo = {}
    for n_ in allnodes:
        pos_set(n_, memo)
    free = {n_.uid for n_ in allnodes if not (memo[n_.uid] & marks)}
    maxfree = [n_ for n_ in allnodes if n_.uid in free and (n_.parent is None or n_.parent.uid not in free)]

    Nst = [Counter(e for _, e, _ in win[i]) for i in range(d)]
    deleted_edges = 0
    for eta in maxfree:
        q = leaf_intervals(eta)
        sub = nodes_of(eta)
        ey = yield_of(eta, {}, [0])
        eta_pos = memo[eta.uid]
        phi = []
        kap_of = {}
        for kap, comp in enumerate(ey):
            ids = [pid for pid, _ in comp]
            i = comp_of[ids[0]]
            js = [idx_of[p] for p in ids]
            assert all(comp_of[p] == i for p in ids) and js == list(range(js[0], js[0] + len(js)))
            inner = [k_ for k_, (t, e, ps) in enumerate(win[i]) if set(ps) <= set(ids)]
            J = None
            if inner:
                es = {win[i][k_][1] for k_ in inner}
                assert es <= freq[i], 'free factor has a rare window'
                Js = {Jof[i][e] for e in es}
                assert len(Js) == 1
                J = Js.pop()
                assert sum(1 for iv in ivs[i] if iv[0] <= inner[0] and inner[-1] < iv[1]) == 1
                STATS['free factors with inner windows'] += 1
            phi.append((i, js[0], js[-1] + 1, J, set(ids)))
            for p in ids:
                kap_of[p] = kap

        def I_j(j):
            return [n_ for n_ in sub if n_.hi <= j and (n_ is eta or n_.parent.hi > j)]

        def info(j):
            I = I_j(j)
            U = set()
            for n_ in I:
                U |= memo[n_.uid]
            repl = {n_.uid: SHORT[n_.nt] for n_ in I}
            er = yield_of(eta, repl, [0])
            col, colctl = [], []
            for kap, comp in enumerate(er):
                wd = [l for _, l in comp]
                imp = Counter(tuple(wd[t - ELL + 1:t + 1]) for t in range(ELL - 1, len(wd))
                              if any(p < 0 for p, _ in comp[t - ELL + 1:t + 1]))
                col.append((stype(wd), tuple(sorted(imp.items()))))
                colctl.append(tuple(sorted(Counter(l for p, l in comp if p < 0).items())))
            return I, U, tuple(col), tuple(colctl)

        data = [info(j) for j in range(q + 1)]
        for j in range(q):
            assert data[j][1] < data[j + 1][1]

        def build(jj):
            repl = {n_.uid: SHORT[n_.nt] for n_ in data[jj][0]}
            rt = eta
            while rt.parent is not None:
                rt = rt.parent
            xr = yield_of(rt, repl, [0])
            er = yield_of(eta, repl, [0])
            W = xr[0] + [('ctx', 'b')] + xr[1]
            return xr, er, W

        def zk(j, jp):
            out = []
            for (i, s0, s1, J, ids) in phi:
                out.append(Counter(e for t, e, ps in win[i]
                                   if set(ps) <= ids and not (set(ps) & data[j][1]) and (set(ps) & data[jp][1])))
            return out

        # ---- control: round-3 colour (letter Parikh of replaced material per kappa)
        j = 0
        while j <= q:
            jp = max(jj for jj in range(j, q + 1) if data[jj][3] == data[j][3])
            if jp > j:
                STATS['control(letter colour) steps'] += 1
                _, er_j, Wj = build(j)
                _, er_p, Wp = build(jp)
                Z = zk(j, jp)
                Wjw, Wpw = [l for _, l in Wj], [l for _, l in Wp]
                ok_tot = csub(Nl(Wjw), Nl(Wpw)) == csub(sum(Z, Counter()), Counter())
                ok_c = all(is_circ(csub(Nl([l for _, l in er_j[kk]]), Nl([l for _, l in er_p[kk]])))
                           for kk in range(len(phi)))
                ok_id = all(csub(Nl([l for _, l in er_j[kk]]), Nl([l for _, l in er_p[kk]])) ==
                            csub(Z[kk], Counter()) for kk in range(len(phi)))
                if not ok_c:
                    STATS['control(letter colour) some kappa-difference NOT a circulation'] += 1
                    if 'control_circ' not in WIT:
                        WIT['control_circ'] = (seed, j, jp, [''.join(l for _, l in er_j[kk]) for kk in range(len(phi))],
                                               [''.join(l for _, l in er_p[kk]) for kk in range(len(phi))])
                if not ok_tot:
                    STATS['control(letter colour) N(W_j)-N(W_jp) != sum Z'] += 1
                if not (ok_tot and ok_c and ok_id):
                    STATS['control(letter colour) P1^ell identity/circulation FAILS'] += 1
                    if 'control' not in WIT:
                        WIT['control'] = (seed, j, jp, [''.join(l for _, l in er_j[kk]) for kk in range(len(phi))],
                                          [''.join(l for _, l in er_p[kk]) for kk in range(len(phi))])
            j = jp + 1

        j = 0
        while j <= q:
            jp = max(jj for jj in range(j, q + 1) if data[jj][2] == data[j][2])
            if jp > j:
                try:
                    deleted_edges += step(seed, x, xw, win, ivs, Jof, ctx, Nst, eta_pos, phi, data, j, jp,
                                          build, zk, marks, comp_of, idx_of, styp, cont)
                except Skip as s_:
                    STATS['skipped: ' + str(s_)] += 1
                    return 'skip'
            j = jp + 1

    final = []
    for i in range(d):
        yi, _ = realise(i, Nst[i], ctx)
        assert stype(yi) == styp[i] and set(yi) == cont[i] and Nl(yi) == +Nst[i]
        final.append(yi)
    old, new = sum(map(len, xw)), sum(map(len, final))
    assert old - new == deleted_edges
    # end-to-end: random admissible contexts
    crng = random.Random(seed + 77)
    pool0 = ['', 'a', 'aa', 'aab', 'ab', 'b', 'aba', 'ba']
    pool1 = ['b', 'a', 'ab', 'ba', 'aba', 'bab', 'abba', 'bb', 'aab', 'baab']
    agree = acc = 0
    for _ in range(300):
        v0, v1, v2 = crng.choice(pool0), crng.choice(pool1), crng.choice(pool0)
        om = lambda s: s.count('a') - 2 * s.count('b')
        r = om(''.join(xw[0])) + om(''.join(xw[1])) + om(v0 + v1 + v2)
        if crng.random() < 0.85:
            v2 = v2 + ('ba' * r if r > 0 else 'a' * (-r))
        Ex = list(v0) + xw[0] + list(v1) + xw[1] + list(v2)
        Ey = list(v0) + final[0] + list(v1) + final[1] + list(v2)
        assert in_L(Ex) == in_L(Ey), ('end-to-end mismatch', seed, v0, v1, v2)
        agree += 1
        acc += in_L(Ex)
    STATS['end-to-end contexts checked'] += agree
    STATS['end-to-end contexts accepting'] += acc
    STATS['trees'] += 1
    return (old, new)


def step(seed, x, xw, win, ivs, Jof, ctx, Nst, eta_pos, phi, data, j, jp, build, zk, marks,
         comp_of, idx_of, styp, cont):
    STATS['steps'] += 1
    R = data[jp][1] - data[j][1]
    assert R and not (R & marks)
    xr_j, er_j, Wj = build(j)
    xr_p, er_p, Wp = build(jp)
    Wjw, Wpw = [l for _, l in Wj], [l for _, l in Wp]
    assert in_L(Wjw) and in_L(Wpw)
    Z = zk(j, jp)
    for kap in range(len(phi)):
        diff = csub(Nl([l for _, l in er_j[kap]]), Nl([l for _, l in er_p[kap]]))
        assert diff == csub(Z[kap], Counter()), 'P1^ell identity'
        assert is_circ(Z[kap]), 'P1^ell circulation'
        if Z[kap]:
            assert set(Z[kap]) <= phi[kap][3]
    assert csub(Nl(Wjw), Nl(Wpw)) == csub(sum(Z, Counter()), Counter()), 'P1^ell total'
    assert stype(Wjw) == stype(Wpw)
    z = {}
    for kap, Zk in enumerate(Z):
        if Zk:
            key = (phi[kap][0], phi[kap][3])
            z[key] = cadd(z.get(key, Counter()), Zk)
    if not z:
        STATS['steps with all Z_kappa = 0 (no-op)'] += 1
        return 0
    # ---- flexible windows / runs of W_j'
    flex = {}            # W-index t -> (i, original window list index)
    for t in range(ELL - 1, len(Wp)):
        ps = [p for p, _ in Wp[t - ELL + 1:t + 1]]
        if not all(isinstance(p, int) and p > 0 for p in ps):
            continue
        if any(p in eta_pos for p in ps):
            continue
        i = comp_of[ps[0]]
        if any(comp_of[p] != i for p in ps):
            continue
        ix = [idx_of[p] for p in ps]
        if ix != list(range(ix[0], ix[0] + ELL)):
            continue
        flex[t] = (i, ix[-1] - (ELL - 1))
    runs = []
    for t in sorted(flex):
        if runs and runs[-1][-1] == t - 1:
            runs[-1].append(t)
        else:
            runs.append([t])
    run_info = []
    for r_ in runs:
        i = flex[r_[0]][0]
        ks = [flex[t][1] for t in r_]
        assert ks == list(range(ks[0], ks[0] + len(ks)))
        e0 = win[i][ks[0]][1]
        J = Jof[i].get(e0)
        if J is None:                                  # a rare window: frozen, not flexible
            # split: rare windows are frozen; keep only frequent ones
            pass
        run_info.append((i, r_, ks))
    # split runs at rare windows (rare edges are frozen)
    R2 = []
    for i, r_, ks in run_info:
        cur = None
        for t, k_ in zip(r_, ks):
            e = win[i][k_][1]
            if e in Jof[i]:
                if cur is None:
                    cur = [i, [t], [k_]]
                else:
                    cur[1].append(t)
                    cur[2].append(k_)
            else:
                if cur is not None:
                    R2.append(tuple(cur))
                cur = None
        if cur is not None:
            R2.append(tuple(cur))
    finfo = []
    for i, ts, ks in R2:
        Js = {Jof[i][win[i][k_][1]] for k_ in ks}
        assert len(Js) == 1
        J = Js.pop()
        ivx = [n_ for n_, iv in enumerate(ivs[i]) if iv[0] <= ks[0] and ks[-1] < iv[1]]
        assert len(ivx) == 1, 'flexible run in two intervals'
        finfo.append((i, ts, ks, J, ivx[0]))
    # anchors: first J-interval (index among J-intervals of comp i) containing a flexible window
    holes = []
    anchor = {}
    for key in z:
        i, J = key
        Jivs = [n_ for n_, iv in enumerate(ivs[i]) if iv[2] == J]
        cand = [ivn for (ii, ts, ks, JJ, ivn) in finfo if ii == i and JJ == J]
        if not cand:
            raise Skip('no flexible J window')
        a_iv = min(cand)
        anchor[key] = (Jivs.index(a_iv), a_iv)
        holes.append(key)
    holes.sort(key=lambda key: (key[0], ivs[key[0]][anchor[key][1]][0]))
    STATS['holes=%d' % len(holes)] += 1
    if len(holes) > len({i for i, _ in holes}):
        STATS['steps with 2 holes in one component'] += 1
    if len({i for i, _ in holes}) > 1:
        STATS['steps with holes in both components'] += 1
    # ---- h, t
    hw, tw = {}, {}
    for key in holes:
        i, J = key
        uJ = min(verts(J))
        hJ = cover_walk(uJ, J)
        r = -(-(ELL - 1) // len(hJ))
        H0 = hJ * r
        h = H0 + H0
        t = H0 + euler(cadd(Counter(H0), z[key]), uJ, uJ)
        assert Counter(t) == cadd(Counter(h), z[key])
        hword = [e[-1] for e in h]
        tword = [e[-1] for e in t]
        assert stype(hword) == stype(tword) and set(hword) == set(tword), 'type of t != type of h'
        hw[key], tw[key] = (h, hword), (t, tword)
    # ---- y side
    ypi, yprime, yoffs = [], [], []
    for i in range(2):
        hole = {J: (anchor[(ii, J)][0], tw[(ii, J)][0]) for (ii, J) in holes if ii == i}
        yi, offs = realise(i, Nst[i], ctx, hole)
        assert stype(yi) == styp[i] and set(yi) == cont[i] and Nl(yi) == +Nst[i], 'Y'
        yp = list(yi)
        for J, off in sorted(offs.items(), key=lambda p: -p[1]):
            tword = tw[(i, J)][1]
            assert yp[off:off + len(tword)] == tword
            yp[off:off + len(tword)] = hw[(i, J)][1]
        newN = Counter(Nst[i])
        for (ii, J) in holes:
            if ii == i:
                newN.subtract(z[(ii, J)])
        assert stype(yp) == styp[i] and set(yp) == cont[i] and Nl(yp) == +newN, "y'"
        ypi.append(yi)
        yprime.append(yp)
        yoffs.append(offs)
    EY = ypi[0] + ['b'] + ypi[1]
    yo = sorted([(off, (0, J)) for J, off in yoffs[0].items()] +
                [(len(ypi[0]) + 1 + off, (1, J)) for J, off in yoffs[1].items()])
    assert [k_ for _, k_ in yo] == holes, 'y-side hole order'
    for (o1, k1), (o2, k2) in zip(yo, yo[1:]):
        assert o2 >= o1 + len(tw[k1][1]) + 1, 'F_E separator empty'
    # ---- F side: Euler-rewire flexible runs of W_j'
    newruns = {}
    for i in range(2):
        for J in {ff[3] for ff in finfo if ff[0] == i and (i, ff[3]) in z}:
            lst = [ff for ff in finfo if ff[0] == i and ff[3] == J]
            lst.sort(key=lambda ff: ff[1][0])
            M = Counter()
            for ff in lst:
                M.update(win[i][k_][1] for k_ in ff[2])
            key = (i, J)
            if key in z:
                main = next(ff for ff in lst if ff[4] == anchor[key][1])
            else:
                main = lst[0]
            Rm = Counter(M)
            for ff in lst:
                if ff is main:
                    continue
                p, q = tl(win[i][ff[2][0]][1]), hd(win[i][ff[2][-1]][1])
                pa = bfs_path(p, q, J)
                Rm.subtract(pa)
                newruns[ff[1][0]] = (ff[1], [], None, pa)
            p, q = tl(win[i][main[2][0]][1]), hd(win[i][main[2][-1]][1])
            if key in z:
                uJ = min(verts(J))
                pre = bfs_path(p, uJ, J)
                Rm.subtract(pre)
                Rm.subtract(hw[key][0])
                if not all(Rm[e] >= 1 for e in J):
                    raise Skip('F-material')
                newruns[main[1][0]] = (main[1], pre, key, euler(+Rm, uJ, q))
            else:
                if not all(Rm[e] >= 1 for e in J if M[e] > 0):
                    raise Skip('F-material0')
                newruns[main[1][0]] = (main[1], [], None, euler(+Rm, p, q))
    out, foffs, t = [], {}, 0
    while t < len(Wp):
        if t in newruns:
            ts, pre, key, rest = newruns[t]
            out += [e[-1] for e in pre]
            if key is not None:
                foffs[key] = len(out)
                out += hw[key][1]
            out += [e[-1] for e in rest]
            t = ts[-1] + 1
        else:
            out.append(Wp[t][1])
            t += 1
    Wprime = out
    assert in_L(Wprime) and Nl(Wprime) == Nl(Wpw) and stype(Wprime) == stype(Wpw), 'W prime'
    fo = sorted((off, key) for key, off in foffs.items())
    assert [k_ for _, k_ in fo] == holes, 'hole order differs between F and F_E'
    for (o1, k1), (o2, k2) in zip(fo, fo[1:]):
        assert o2 >= o1 + len(hw[k1][1]) + 1, 'F separator empty'
    Ft = list(Wprime)
    for off, key in sorted(fo, key=lambda p: -p[0]):
        assert Ft[off:off + len(hw[key][1])] == hw[key][1]
        Ft[off:off + len(hw[key][1])] = tw[key][1]
    assert Nl(Ft) == Nl(Wjw) and stype(Ft) == stype(Wjw) and in_L(Ft), 'F[t]'
    # E_A[y'] vs E_A[y^pi] (both in L by D(t)=D(h); here checked directly)
    assert in_L(EY) == in_L(yprime[0] + ['b'] + yprime[1])
    for (i, J) in holes:
        Nst[i].subtract(z[(i, J)])
    STATS['steps verified'] += 1
    return sum(sum(v.values()) for v in z.values())


def main():
    check_good()
    sys.setrecursionlimit(100000)
    cfgs = []
    for s in range(40):
        cfgs.append((ELL * 100000 + 1000 + s, 300, 16, 0.01, 0.03))
    for s in range(40):
        cfgs.append((ELL * 100000 + 2000 + s, 700, 32, 0.006, 0.02))
    for s in range(40):
        cfgs.append((ELL * 100000 + 3000 + s, 400, 8, 0.0, 0.08))
    for s in range(40):
        cfgs.append((ELL * 100000 + 4000 + s, 900, 12, 0.0, 0.05))
    for s in range(30):
        cfgs.append((ELL * 100000 + 5000 + s, 1500, 24, 0.002, 0.04))
    for s in range(60):
        cfgs.append((ELL * 100000 + 6000 + s, 2000, 64, 0.0, 0.06))
    for s in range(60):
        cfgs.append((ELL * 100000 + 7000 + s, 1200, 40, 0.0, 0.10))
    cfgs = [c + (0.0, False) for c in cfgs]
    for s in range(80):
        cfgs.append((ELL * 100000 + 8000 + s, 1500, 32, 0.0, 0.05, 0.02, False))
    for s in range(60):
        cfgs.append((ELL * 100000 + 9000 + s, 600, 16, 0.0, 0.0, 0.0, True))
    rows = []
    for seed, budget, CM, rp, p2, p6, tg in cfgs:
        r = run_tree(seed, budget, CM, rp, p2, p6, tg)
        rows.append((seed, CM, r))
        STATS['result: ' + (r if isinstance(r, str) else 'ok')] += 1
    for r in rows:
        print(r)
    print('ELL =', ELL, ' K(de Bruijn edges) =', K)
    for k_, v in sorted(STATS.items()):
        print('%-55s %d' % (k_, v))
    print('control witness (seed, j, jp, psi_j per kappa, psi_jp per kappa):', WIT.get('control'))
    print('control circulation witness:', WIT.get('control_circ'))
    print('all asserts passed')


if __name__ == '__main__':
    main()
