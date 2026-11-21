#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_path_ordered_joining_2026-11-14.py   (Python 3, standard library only, fixed seeds)

Executes, on concrete derivation trees of a good fan-out-2 / rank-2 MCFG, the
constructive proof of Theorem P (path languages with an arbitrary Parikh filter)
of the Claude round-3 report, and checks every intermediate claim with asserts:

  * marks: first CM occurrences of each letter in each root component;
  * W2 (frequency gap) in each root component: weak components of the frequent
    graph are strongly connected; rare letters are completely marked;
  * free factors lie in one frequent stretch, hence in one frequent component J;
  * prefix antichains I_j, regions R = U_{j'} \\ U_j, colours refined per
    eta-component (Parikh vector of the substituted material landing in phi_kappa);
  * Lemma P1: z_kappa = Psi(psi^(j)_kappa) - Psi(psi^(j')_kappa) equals Psi(R cap phi_kappa)
    and is a circulation;
  * Lemma Y (y side): a tuple y^pi with the current per-component Parikh vectors,
    same endpoints and contents, keeps the rare skeleton and exposes closed walks t
    at skeleton cuts; y' = y^pi with t replaced by h;
  * Lemma F (F side): W' with Psi(W') = Psi(W_{j'}), same rare skeleton, exposing h
    at the same skeleton cuts; F[t'] = W' in L, F[t] in L, admissible separators;
  * the hole order of F and of F_{E_A} coincide;
  * the final tuple has the endpoints and contents of x and length much smaller.

Target: D has vertices 0,1; a:0->1, b:1->0, c: loop at 0, e: loop at 1.
L = Path_D(0,0) ∩ {w : |w|_c = |w|_e} ∩ Σ^+ .  L(G) ⊆ L by construction; the
proof only uses W_j ∈ L, membership of F[t], F[t'] (walk + Parikh), and
substitutability as a hypothesis (it does hold for this L, see report §2).

Asserts check the bookkeeping of the proof on finite trees; they are not a proof.
"""
import random
from collections import Counter, defaultdict

LET = {'a': (0, 1), 'b': (1, 0), 'c': (0, 0), 'e': (1, 1)}
LETTERS = sorted(LET)
K = len(LETTERS)


def is_walk(w, s=None, t=None):
    if not w:
        return s is None or s == t
    for x, y in zip(w, w[1:]):
        if LET[x][1] != LET[y][0]:
            return False
    if s is not None and LET[w[0]][0] != s:
        return False
    if t is not None and LET[w[-1]][1] != t:
        return False
    return True


def in_L(w):
    return len(w) > 0 and is_walk(w, 0, 0) and w.count('c') == w.count('e')


def parikh(w):
    c = Counter(w)
    return {a: c.get(a, 0) for a in LETTERS}


def padd(p, q, s=1):
    return {a: p[a] + s * q[a] for a in LETTERS}


def is_circulation(p):
    bal = Counter()
    for a, n in p.items():
        u, v = LET[a]
        bal[u] -= n
        bal[v] += n
    return all(x == 0 for x in bal.values())


# --------------------------------------------------------------------------- grammar
# items: ('t', letter) or ('v', child, comp)
def T(x):
    return ('t', x)


def V(i, j):
    return ('v', i, j)


RULES = {
    'B': [
        ('B0', [], [[T('c')], [T('e')]]),
        ('B1', ['B'], [[T('c'), V(0, 0)], [V(0, 1), T('e')]]),
        ('B2', ['B'], [[V(0, 0), T('c')], [T('e'), V(0, 1)]]),
        ('B3', ['B'], [[T('a'), T('e'), T('b'), V(0, 0)], [V(0, 1), T('b'), T('c'), T('a')]]),
        ('B4', ['B', 'B'], [[V(0, 0), V(1, 0)], [V(0, 1), V(1, 1)]]),
        ('B5', ['B', 'B'], [[V(0, 0), V(1, 0)], [V(1, 1), V(0, 1)]]),           # crossing
        ('B6', ['B', 'B'], [[V(0, 0), T('a'), V(0, 1), T('b'), V(1, 0)], [V(1, 1)]]),  # moving
        ('B7', ['B', 'C'], [[V(0, 0), V(1, 0)], [V(0, 1)]]),
        ('B8', ['B', 'P'], [[V(0, 0), V(1, 0), T('e'), V(1, 1), T('c')], [V(0, 1)]]),
    ],
    'P': [                                    # P yields (walk 0->1, walk 1->0)
        ('P0', [], [[T('a')], [T('b')]]),
        ('P1', ['P'], [[T('c'), V(0, 0), T('e')], [V(0, 1)]]),
        ('P2', ['P'], [[V(0, 0)], [T('e'), V(0, 1), T('c')]]),
        ('P3', ['B', 'P'], [[V(0, 0), V(1, 0)], [V(0, 1), V(1, 1)]]),
        ('P5', ['B', 'P'], [[V(0, 0), V(1, 0), V(0, 1)], [V(1, 1)]]),
        ('P6', ['P', 'P'], [[V(0, 0), T('e'), V(0, 1), T('c'), V(1, 0)], [V(1, 1)]]),
    ],
    'C': [
        ('C0', ['B'], [[V(0, 0), T('a'), V(0, 1), T('b')]]),
        ('C1', ['C', 'C'], [[V(0, 0), V(1, 0)]]),
    ],
}
FAN = {'B': 2, 'C': 1, 'P': 2}
SHORT = {'B': [['c'], ['e']], 'C': [['c', 'a', 'e', 'b']], 'P': [['a'], ['b']]}   # u_B, u_C (theta-short yields)
RULE = {r[0]: r for nt in RULES for r in RULES[nt]}


def check_good():
    for nt, rs in RULES.items():
        for name, ch, tpl in rs:
            assert len(tpl) == FAN[nt]
            assert all(len(c) > 0 for c in tpl)                        # eps-free
            occ = [(it[1], it[2]) for comp in tpl for it in comp if it[0] == 'v']
            want = [(i, j) for i, c in enumerate(ch) for j in range(FAN[c])]
            assert sorted(occ) == sorted(want)                         # nondeleting, linear
            for i, c in enumerate(ch):                                 # nonpermuting
                assert [j for (ii, j) in occ if ii == i] == list(range(FAN[c]))
            for comp in tpl:                                           # nonmerging
                for x, y in zip(comp, comp[1:]):
                    assert not (x[0] == 'v' and y[0] == 'v' and x[1] == y[1] and y[2] == x[2] + 1)


class Node:
    __slots__ = ('nt', 'rule', 'ch', 'tid', 'parent', 'lo', 'hi', 'uid')


UID = [0]
POS = [0]


FORCE = []
FORCE_HALF = [False]
P_MODE = [0.0, 1, 0.0]


def gen(nt, budget, rng, rare_p):
    n = Node()
    n.nt = nt
    UID[0] += 1
    n.uid = UID[0]
    rs = RULES[nt]
    if nt == 'B' and FORCE:
        choice = FORCE.pop(0)
    elif nt == 'B' and P_MODE[0] and budget >= 3 and rng.random() < P_MODE[0]:
        choice = 'B8'
    elif nt == 'B':
        if budget <= 1:
            choice = 'B0'
        else:
            x = rng.random()
            if x < rare_p:
                choice = rng.choice(['B3', 'B6', 'B7'])
            elif budget >= 4 and x < 0.55:
                choice = rng.choice(['B4', 'B5'])
            else:
                choice = rng.choice(['B1', 'B2'])
    elif nt == 'P':
        if budget <= 1:
            choice = 'P0'
        elif budget >= 4 and rng.random() < P_MODE[2]:
            choice = rng.choice(['P3', 'P5', 'P6'])
        else:
            choice = rng.choice(['P1', 'P2'])
    elif nt == 'B' and P_MODE[0] and budget >= 3 and rng.random() < P_MODE[0]:
        choice = 'B8'
    else:
        choice = 'C1' if (budget >= 6 and rng.random() < 0.3) else 'C0'
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
        n.ch = [gen(ch[0], budget - 1, rng, rare_p)]
    else:
        if ch[1] == 'P' and nt == 'B':
            b1 = max(1, budget - 1 - rng.randint(1, P_MODE[1]))
        else:
            b1 = rng.randint(1, max(1, budget - 2)) if not FORCE_HALF[0] else budget // 2
        FORCE_HALF[0] = False
        n.ch = [gen(ch[0], b1, rng, rare_p), gen(ch[1], max(1, budget - 1 - b1), rng, rare_p)]
    for c in n.ch:
        c.parent = n
    return n


def yield_of(n, repl, fresh):
    """components as lists of (pos_id, letter); repl: uid -> list of components (letters)."""
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


# --------------------------------------------------------------------------- walk tools
def bfs_path(u, v, edges):
    if u == v:
        return []
    prev = {u: None}
    q = [u]
    while q:
        nq = []
        for x in q:
            for a in edges:
                if LET[a][0] == x and LET[a][1] not in prev:
                    prev[LET[a][1]] = (x, a)
                    nq.append(LET[a][1])
        q = nq
    assert v in prev
    path, x = [], v
    while x != u:
        y, a = prev[x]
        path.append(a)
        x = y
    return path[::-1]


def euler(counts, s, t):
    """Hierholzer: walk s->t using each letter a exactly counts[a] times."""
    tot = sum(counts.values())
    if tot == 0:
        assert s == t
        return []
    adj = defaultdict(list)
    for a in sorted(counts):
        for _ in range(counts[a]):
            adj[LET[a][0]].append(a)
    stack, out = [(s, None)], []
    while stack:
        v, a = stack[-1]
        if adj[v]:
            b = adj[v].pop()
            stack.append((LET[b][1], b))
        else:
            stack.pop()
            if a is not None:
                out.append(a)
    out.reverse()
    assert len(out) == tot, 'not connected'
    assert is_walk(out, s, t)
    assert parikh(out) == {x: counts.get(x, 0) for x in LETTERS}
    return out


def cover_walk(u, J):
    h = []
    for a in sorted(J):
        h += bfs_path(u, LET[a][0], J) + [a] + bfs_path(LET[a][1], u, J)
    assert is_walk(h, u, u) and set(h) == set(J)
    return h


def strongly_connected(edges):
    vs = {LET[a][0] for a in edges} | {LET[a][1] for a in edges}
    if not vs:
        return True
    v0 = min(vs)
    for fw in (True, False):
        seen, st = {v0}, [v0]
        while st:
            x = st.pop()
            for a in edges:
                u, v = LET[a] if fw else LET[a][::-1]
                if u == x and v not in seen:
                    seen.add(v)
                    st.append(v)
        if seen != vs:
            return False
    return True


def weak_components(edges):
    comps = []
    rem = set(edges)
    while rem:
        a = rem.pop()
        comp, vs = {a}, set(LET[a])
        ch = True
        while ch:
            ch = False
            for b in list(rem):
                if set(LET[b]) & vs:
                    rem.discard(b)
                    comp.add(b)
                    vs |= set(LET[b])
                    ch = True
        comps.append(frozenset(comp))
    return comps


# --------------------------------------------------------------------------- the proof
STATS = Counter()
STATS_W = {}


def run_tree(seed, budget, rare_p, CM, force=(), pmode=(0.0, 1, 0.0)):
    rng = random.Random(seed)
    P_MODE[:] = list(pmode)
    FORCE[:] = list(force)
    FORCE_HALF[0] = bool(force)
    UID[0] = 0
    POS[0] = 0
    root = gen('B', budget, rng, rare_p)
    for n in nodes_of(root):
        for c in n.ch:
            c.parent = n
    root.parent = None
    x = yield_of(root, {}, [0])
    ctx = ['a', 'b']                      # E_A = []_1 a []_2 b  (derivational context of B)
    d = 2
    letters_of = {}
    for comp in x:
        for pid, l in comp:
            letters_of[pid] = l
    xw = [[l for _, l in comp] for comp in x]
    w = xw[0] + ['a'] + xw[1] + ['b']
    assert in_L(w)
    ends = [(LET[c[0]][0], LET[c[-1]][1]) for c in xw]
    cont = [set(c) for c in xw]

    # marks: first CM occurrences of each letter in each component
    marks = set()
    for comp in x:
        seen = Counter()
        for pid, l in comp:
            if seen[l] < CM:
                marks.add(pid)
            seen[l] += 1

    # W2 per component with thresholds c_i = K^(i-1)
    thr = [K ** i for i in range(K + 2)]
    freq, J_of, stretches = [], [], []
    for i, comp in enumerate(xw):
        n = Counter(comp)
        g = next(gi for gi in range(K + 1)
                 if not any(thr[gi] <= n[a] < thr[gi + 1] for a in n))
        fr = {a for a in n if n[a] >= thr[g + 1]}
        ra = {a for a in n if n[a] < thr[g]}
        assert fr | ra == set(n)
        Js = weak_components(fr)
        for J in Js:
            assert strongly_connected(J), 'W2 failed'
            STATS['W2 components'] += 1
        # rare letters completely marked?
        if not all(pid in marks for pid, l in x[i] if l in ra):
            return 'rare-unmarked'
        jof = {a: J for J in Js for a in J}
        # stretches: maximal runs of frequent letters
        st, cur = [], None
        for idx, l in enumerate(comp):
            if l in fr:
                if cur is None:
                    cur = [idx, idx + 1, jof[l]]
                else:
                    assert jof[l] == cur[2]
                    cur[1] = idx + 1
            else:
                if cur is not None:
                    st.append(tuple(cur))
                cur = None
        if cur is not None:
            st.append(tuple(cur))
        freq.append(fr)
        J_of.append(jof)
        stretches.append(st)

    # tree bookkeeping
    allnodes = nodes_of(root)
    memo = {}
    for n in allnodes:
        pos_set(n, memo)
    free = {n.uid for n in allnodes if not (memo[n.uid] & marks)}
    maxfree = [n for n in allnodes if n.uid in free and (n.parent is None or n.parent.uid not in free)]
    comp_of = {}
    idx_of = {}
    for i, comp in enumerate(x):
        for t_, (pid, l) in enumerate(comp):
            comp_of[pid] = i
            idx_of[pid] = t_

    m = [parikh(c) for c in xw]           # current per-component Parikh vectors
    total_deleted = 0
    for eta in maxfree:
        q = leaf_intervals(eta)
        sub = nodes_of(eta)
        ey = yield_of(eta, {}, [0])
        # eta components phi_kappa: contiguous factors of root components
        phi = []
        kap_of = {}
        for kap, comp in enumerate(ey):
            ids = [pid for pid, _ in comp]
            i = comp_of[ids[0]]
            js = [idx_of[p] for p in ids]
            assert all(comp_of[p] == i for p in ids) and js == list(range(js[0], js[0] + len(js)))
            letters = {letters_of[p] for p in ids}
            assert letters <= freq[i], 'free factor has a rare letter'
            Js = {J_of[i][l] for l in letters}
            assert len(Js) == 1
            J = Js.pop()
            stx = [s_ for s_ in stretches[i] if s_[0] <= js[0] and js[-1] < s_[1]]
            assert len(stx) == 1                     # inside one stretch
            phi.append((i, js[0], js[-1] + 1, J, set(ids)))
            for p in ids:
                kap_of[p] = kap

        def I_j(j):
            out = []
            for n in sub:
                if n.hi <= j and (n is eta or n.parent.hi > j):
                    out.append(n)
            return out

        def U_and_col(j):
            I = I_j(j)
            U = set()
            col = [Counter() for _ in ey]
            for n in I:
                U |= memo[n.uid]
                ny = yield_of(n, {}, [0])
                for mm, compn in enumerate(ny):
                    kap = kap_of[compn[0][0]]
                    col[kap].update(SHORT[n.nt][mm])
            colkey = tuple(tuple(col[kk][a] for a in LETTERS) for kk in range(len(ey)))
            return I, U, colkey

        data = [U_and_col(j) for j in range(q + 1)]
        # control: GLOBAL colours (sum over kappa) -- is Psi(R cap phi_kappa) still a circulation?
        gcol = [tuple(sum(c[t_] for c in dd[2]) for t_ in range(K)) for dd in data]
        jg = 0
        while jg <= q:
            jpg = max(jj for jj in range(jg, q + 1) if gcol[jj] == gcol[jg])
            if jpg > jg:
                Rg = data[jpg][1] - data[jg][1]
                STATS['control(global colour): steps'] += 1
                bad = [kk for kk, ph in enumerate(phi)
                       if not is_circulation(parikh([letters_of[p_] for p_ in Rg & ph[4]]))]
                if bad:
                    STATS['control(global colour): some z_kappa NOT a circulation'] += 1
                    if 'witness' not in STATS_W:
                        STATS_W['witness'] = (seed, [''.join(sorted(letters_of[p_] for p_ in Rg & phi[kk][4]))
                                                     for kk in range(len(phi))])
            jg = jpg + 1
        for j in range(q):
            assert data[j][1] < data[j + 1][1]
        j = 0
        while j <= q:
            colj = data[j][2]
            jp = max(jj for jj in range(j, q + 1) if data[jj][2] == colj)
            if jp > j:
                step(x, xw, ctx, ends, cont, m, eta, ey, phi, data, j, jp, letters_of,
                     marks, freq, J_of, stretches, comp_of, idx_of)
                total_deleted += len(data[jp][1] - data[j][1])
            j = jp + 1
    # final tuple
    final = []
    for i in range(d):
        yi = euler(m[i], ends[i][0], ends[i][1])
        assert set(yi) == cont[i]
        final.append(yi)
    newlen = sum(len(c) for c in final)
    assert newlen == sum(len(c) for c in xw) - total_deleted
    STATS['trees'] += 1
    return (sum(len(c) for c in xw), newlen)


def step(x, xw, ctx, ends, cont, m, eta, ey, phi, data, j, jp, letters_of,
         marks, freq, J_of, stretches, comp_of, idx_of):
    STATS['steps'] += 1
    R = data[jp][1] - data[j][1]
    assert R and not (R & marks)
    # build W_j, W_jp and the replaced eta-components psi
    root = eta
    while root.parent is not None:
        root = root.parent

    def build(jj):
        repl = {n.uid: SHORT[n.nt] for n in data[jj][0]}
        xr = yield_of(root, repl, [0])
        er = yield_of(eta, repl, [0])
        Wl = [l for _, l in xr[0]] + ['a'] + [l for _, l in xr[1]] + ['b']
        return xr, er, Wl
    xr_j, er_j, Wj = build(j)
    xr_p, er_p, Wp = build(jp)
    assert in_L(Wj) and in_L(Wp)
    z = {}
    for kap, (i, s0, s1, J, ids) in enumerate(phi):
        zk = padd(parikh([l for _, l in er_j[kap]]), parikh([l for _, l in er_p[kap]]), -1)
        assert zk == parikh([letters_of[p] for p in R & ids]), 'P1 identity'
        assert all(v >= 0 for v in zk.values()) and is_circulation(zk), 'P1 circulation'
        if any(zk.values()):
            key = (i, J)
            z[key] = padd(z.get(key, parikh([])), zk)
    assert z
    holes = sorted(z, key=lambda key: (key[0], next(s_[0] for s_ in stretches[key[0]] if s_[2] == key[1])))
    STATS['holes=%d' % len(holes)] += 1
    if len({J for _, J in holes}) > 1:
        STATS['steps with holes in distinct J'] += 1
    if len({i for i, _ in holes}) > 1:
        STATS['steps with holes in distinct components'] += 1
    if len(holes) > len({i for i, _ in holes}):
        STATS['steps with 2 holes in one component (distinct J)'] += 1
    hw, tw = {}, {}
    for key in holes:
        i, J = key
        st0 = next(s_ for s_ in stretches[i] if s_[2] == J)
        u = LET[xw[i][st0[0]]][0]
        h = cover_walk(u, J)
        t = euler(padd(parikh(h), z[key]), u, u)
        assert set(t) == set(h) == set(J)
        hw[key], tw[key] = h, t

    # ---------------- y side
    def rebuild_component(i, material, ins):
        """skeleton of x_i kept; J-stretches re-routed; ins[J] closed walk inserted at first J-stretch."""
        comp = xw[i]
        out, order = [], []
        st = stretches[i]
        byJ = defaultdict(list)
        for s_ in st:
            byJ[s_[2]].append(s_)
        routed = {}
        for J, lst in byJ.items():
            M = {a: material[a] for a in LETTERS if a in J}
            paths = {}
            for s_ in lst[1:]:
                paths[s_] = bfs_path(LET[comp[s_[0]]][0], LET[comp[s_[1] - 1]][1], J)
            N = dict(M)
            for p in paths.values():
                for a in p:
                    N[a] -= 1
            if J in ins:
                for a in ins[J]:
                    N[a] -= 1
            if not all(N[a] >= 1 for a in J):
                return None
            s0 = lst[0]
            main = euler({a: N[a] for a in J}, LET[comp[s0[0]]][0], LET[comp[s0[1] - 1]][1])
            routed[s0] = main
            routed.update(paths)
        k_ = 0
        while k_ < len(comp):
            s_ = next((s for s in st if s[0] == k_), None)
            if s_ is None:
                out.append(comp[k_])            # rare letter (skeleton)
                k_ += 1
            else:
                if s_ == byJ[s_[2]][0] and s_[2] in ins:
                    order.append(((i, s_[2]), len(out)))
                    out.extend(ins[s_[2]])
                out.extend(routed[s_])
                k_ = s_[1]
        return out, order

    ypi, yprime, yorder = [], [], []
    for i in range(len(xw)):
        insJ = {J: tw[(ii, J)] for (ii, J) in holes if ii == i}
        r = rebuild_component(i, m[i], insJ)
        if r is None:
            STATS['skipped: y-side material'] += 1
            return
        yi, ordi = r
        assert is_walk(yi, *ends[i]) and parikh(yi) == m[i] and set(yi) == cont[i]
        mz = dict(m[i])
        for (ii, J) in holes:
            if ii == i:
                mz = padd(mz, z[(ii, J)], -1)
        yp = list(yi)
        # replace exposed t by h at the recorded offsets (process right to left)
        for key, off in sorted(ordi, key=lambda p: -p[1]):
            assert yp[off:off + len(tw[key])] == tw[key]
            yp[off:off + len(tw[key])] = hw[key]
        assert is_walk(yp, *ends[i]) and parikh(yp) == mz and set(yp) == cont[i]
        ypi.append(yi)
        yprime.append(yp)
        yorder.extend(ordi)
    # F_{E_A}: E_A[y^pi] with the t's cut out
    EY = ypi[0] + ['a'] + ypi[1] + ['b']
    offs = []
    base = 0
    for i in range(2):
        for key, off in yorder:
            if key[0] == i:
                offs.append((base + off, key))
        base += len(ypi[i]) + 1
    offs.sort()
    yholes = [key for _, key in offs]
    assert yholes == holes
    for (o1, k1), (o2, k2) in zip(offs, offs[1:]):
        assert o2 > o1 + len(tw[k1]), 'F_E separator empty'
    EYp = yprime[0] + ['a'] + yprime[1] + ['b']
    assert in_L(EY) == in_L(EYp)       # consistent with D(t)=D(t') (here both are in L)

    # ---------------- F side: W_{j'} with eta-components as fixed blocks
    # slot i of W_{j'}: x_i with current eta's components replaced by psi^(j') blocks
    Wparts = []
    forder = []
    for i in range(2):
        comp = x[i]
        items = []          # ('r', l) | ('f', l) | ('psi', kap)
        k_ = 0
        while k_ < len(comp):
            pid, l = comp[k_]
            kap = next((kk for kk, ph in enumerate(phi) if ph[0] == i and ph[1] == k_), None)
            if kap is not None:
                items.append(('psi', kap, k_))
                k_ = phi[kap][2]
            else:
                items.append(('f' if l in freq[i] else 'r', l, k_))
                k_ += 1
        # J-pieces: maximal runs of 'f'
        pieces = []
        cur = None
        for t_, it in enumerate(items):
            if it[0] == 'f':
                if cur is None:
                    cur = [t_, t_ + 1]
                else:
                    cur[1] = t_ + 1
            else:
                if cur is not None:
                    pieces.append(tuple(cur))
                cur = None
        if cur is not None:
            pieces.append(tuple(cur))
        routed = {}
        insert_at = {}
        for (ii, J) in holes:
            if ii != i:
                continue
            st0 = next(s_ for s_ in stretches[i] if s_[2] == J)
            pos0 = next(t_ for t_, it in enumerate(items) if it[2] == st0[0] or
                        (it[0] == 'psi' and phi[it[1]][1] <= st0[0] < phi[it[1]][2]))
            insert_at[pos0] = (ii, J)
            Jp = [p for p in pieces if J_of[i][items[p[0]][1]] == J]
            M = parikh([items[t_][1] for p in Jp for t_ in range(*p)])
            paths = {}
            for p in Jp[1:]:
                paths[p] = bfs_path(LET[items[p[0]][1]][0], LET[items[p[1] - 1][1]][1], J)
            N = dict(M)
            for pa in paths.values():
                for a in pa:
                    N[a] -= 1
            for a in hw[(ii, J)]:
                N[a] -= 1
            if not all(N[a] >= 1 for a in J):
                STATS['skipped: F-side material'] += 1
                return
            p0 = Jp[0]
            routed[p0] = euler({a: N[a] for a in J}, LET[items[p0[0]][1]][0], LET[items[p0[1] - 1][1]][1])
            routed.update(paths)
        out = []
        t_ = 0
        while t_ < len(items):
            if t_ in insert_at:
                forder.append((insert_at[t_], len(Wparts) + len(out)))
                out.append(('HOLE', insert_at[t_]))
            p = next((p for p in routed if p[0] == t_), None)
            if p is not None:
                out.extend(routed[p])
                t_ = p[1]
                continue
            it = items[t_]
            if it[0] == 'psi':
                out.extend(l for _, l in er_p[it[1]])
            else:
                out.append(it[1])
            t_ += 1
        Wparts.extend(out)
        Wparts.append(ctx[i])
    fholes = [key for key, _ in sorted(forder, key=lambda p: p[1])]
    assert fholes == holes, 'hole order differs between F and F_E'

    def fill(Fp, tup):
        res = []
        for it in Fp:
            if isinstance(it, tuple):
                res.extend(tup[it[1]])
            else:
                res.append(it)
        return res
    Wprime = fill(Wparts, hw)
    Ft = fill(Wparts, tw)
    assert is_walk(Wprime, 0, 0) and parikh(Wprime) == parikh(Wp) and in_L(Wprime)
    assert parikh(Ft) == parikh(Wj) and in_L(Ft)
    # admissibility: consecutive holes separated by >= 1 letter
    hp = [t_ for t_, it in enumerate(Wparts) if isinstance(it, tuple)]
    for p1, p2 in zip(hp, hp[1:]):
        assert p2 > p1 + 1, 'F separator empty'
    # commit
    for (i, J) in holes:
        m[i] = padd(m[i], z[(i, J)], -1)
    STATS['steps verified'] += 1


def main():
    check_good()
    results = []
    cfgs = [(1000 + s, 700, 0.004, 64) for s in range(12)] + \
           [(2000 + s, 1200, 0.002, 256) for s in range(6)] + \
           [(3000 + s, 400, 0.02, 16) for s in range(12)]
    cfgs = [c + ((),) for c in cfgs] + \
           [(4000 + s, 900, 0.0, 64, ('B6',)) for s in range(12)] + \
           [(5000 + s, 900, 0.0, 64, ('B4', 'B6')) for s in range(8)]
    cfgs = [c + ((0.0, 1, 0.0),) for c in cfgs] + \
           [(6000 + s, 900, 0.0, 16, (), (0.08, 40, 0.0)) for s in range(20)] + \
           [(7000 + s, 1500, 0.0, 8, (), (0.15, 60, 0.0)) for s in range(20)] + \
           [(8000 + s, 1500, 0.0, 8, (), (0.15, 120, 0.3)) for s in range(30)] + \
           [(9000 + s, 2500, 0.0, 6, (), (0.10, 400, 0.4)) for s in range(30)]
    for seed, budget, rp, CM, force, pm in cfgs:
        r = run_tree(seed, budget, rp, CM, force, pm)
        results.append((seed, CM, r))
    for row in results:
        print(row)
    for k_, v in sorted(STATS.items()):
        print('%-45s %d' % (k_, v))
    print('control witness (seed, letters of R cap phi_kappa per kappa):', STATS_W.get('witness'))
    print('all asserts passed')


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)
    main()
