#!/usr/bin/env python3
"""check_claude_prop73_2026-11-07.py  (standard library only)

Companion script of reviews/claude_prop73_2026-11-07.md.

  python3 check_claude_prop73_2026-11-07.py --seed 1          (about 4-6 minutes)
  python3 check_claude_prop73_2026-11-07.py --seed 1 --quick  (about 1 minute)

Sections (numbering = section E of the report):
  E1  Theorem 1 (planar lemma): every finite closed set of rank <= 2 lies on a strictly
      positive level  [random closures + exhaustive 3-point seeds in [1,4]^3]
  E2  Example 1 (F4, rank 3) and the families F_{X,Y}, S_n (segment + satellites), the
      5-point example: exact closedness, rank, exact condition (T) with Q_2 = {P},
      V cap Q_2, F_L, B_ab, K_c, apex / admissibility of case (ii)
  E3  random 4-point rank-3 closed sets: apexes and admissibility (Lemma 1', Lemma D')
  E4  positive-level bases + one satellite: rank-3 sets with an admissible apex;
      is the short part Q_3^{<mu} on a positive level?
  E5  Y23 and X: apexes (Lemma 1')
  E6  random acyclic CFGs: Lemma K  (mu_ab <= (K_c+3) v theta) and Theorem L'
      (mu_ab <= max{9(r+1)v theta, 11(r+1)v^2 theta^4}) when its hypothesis holds;
      weight-homogeneous CFGs with lambda(c) > 0 for Theorem L'.

Everything on finite sets is exact.  A closure is computed in a box; if it touches the
box it is reported as 'unbounded in the box' and never used as evidence.
"""
import argparse
import itertools
import random
import sys
import time
from math import gcd

# ---------------------------------------------------------------------------
# vectors
# ---------------------------------------------------------------------------


def add(p, q):
    return tuple(x + y for x, y in zip(p, q))


def sub(p, q):
    return tuple(x - y for x, y in zip(p, q))


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def det3(a, b, c):
    return dot(a, cross(b, c))


def rank_of(F):
    F = list(F)
    if len(F) <= 1:
        return 0
    p0 = F[0]
    D = [sub(q, p0) for q in F[1:]]
    for a, b, c in itertools.combinations(D, 3):
        if det3(a, b, c) != 0:
            return 3
    for a, b in itertools.combinations(D, 2):
        if any(cross(a, b)):
            return 2
    return 1 if any(any(d) for d in D) else 0


def positive_level(F):
    """Is there lambda > 0 (all three coordinates) constant on F ?"""
    F = list(F)
    r = rank_of(F)
    if r == 0:
        return True
    if r == 3:
        return False
    p0 = F[0]
    D = [sub(q, p0) for q in F[1:]]
    if r == 1:
        d = next(d for d in D if any(d))
        return any(x > 0 for x in d) and any(x < 0 for x in d)
    for a, b in itertools.combinations(D, 2):
        n = cross(a, b)
        if any(n):
            return all(x > 0 for x in n) or all(x < 0 for x in n)


# ---------------------------------------------------------------------------
# closedness of a finite subset of Pi_3 under its own differences (Q_3 alone)
# ---------------------------------------------------------------------------


def closed3(F):
    S = set(F)
    for p in F:
        for q in F:
            for r in F:
                if q == r:
                    continue
                x = (p[0] + q[0] - r[0], p[1] + q[1] - r[1], p[2] + q[2] - r[2])
                if min(x) >= 1 and x not in S:
                    return False
    return True


def closure(seed, B, maxpts=300):
    """closure of seed under its own differences inside Pi_3; None if it leaves [1,B]^3
    or grows beyond maxpts (then it is not used as evidence)."""
    F = set(seed)
    while True:
        Fl = list(F)
        D = {sub(q, p) for p in Fl for q in Fl if p != q}
        new = set()
        for x in Fl:
            for d in D:
                y = (x[0] + d[0], x[1] + d[1], x[2] + d[2])
                if min(y) >= 1 and y not in F:
                    if max(y) > B:
                        return None
                    new.add(y)
        if not new:
            return F
        F |= new
        if len(F) > maxpts:
            return None


# ---------------------------------------------------------------------------
# exact condition (T) for a finite Q (one vertex): every valid move stays in Q
# ---------------------------------------------------------------------------


def supp(v):
    return frozenset(i for i, x in enumerate(v) if x)


def check_T_finite(Q):
    Qs = set(Q)
    groups = {}
    for q in Q:
        groups.setdefault(supp(q), []).append(q)
    D = {sub(q, p) for pts in groups.values() for p in pts for q in pts if p != q}
    viol = 0
    for h in D:
        S = supp(h)
        for al in Q:
            for be, other in ((add(al, h), None), (sub(al, h), None)):
                # the move from al by +h (resp. -h) is valid iff on supp h both ends >= 1
                if min(be) < 0:
                    continue
                if all(al[i] >= 1 and be[i] >= 1 for i in S) and be not in Qs:
                    viol += 1
    return viol


# ---------------------------------------------------------------------------
# lattices: echelon form, membership, plane part, F_L for a single-point Q_2
# ---------------------------------------------------------------------------


def echelon(vecs, n):
    rows = [list(v) for v in vecs if any(v)]
    basis = []
    for col in range(n):
        while True:
            idx = [i for i, r in enumerate(rows) if r[col] != 0]
            if len(idx) <= 1:
                break
            idx.sort(key=lambda i: abs(rows[i][col]))
            p = rows[idx[0]]
            new = [p]
            for i, r in enumerate(rows):
                if i == idx[0]:
                    continue
                if r[col] != 0:
                    q = r[col] // p[col]
                    r = [r[k] - q * p[k] for k in range(n)]
                if any(r):
                    new.append(r)
            rows = new
        idx = [i for i, r in enumerate(rows) if r[col] != 0]
        if idx:
            p = rows[idx[0]]
            if p[col] < 0:
                p = [-x for x in p]
            basis.append(tuple(p))
            rows = [r for i, r in enumerate(rows) if i != idx[0]]
    return basis


def in_lattice(v, basis):
    v = list(v)
    for row in basis:
        j = next(i for i, x in enumerate(row) if x)
        if v[j] % row[j] != 0:
            return False
        q = v[j] // row[j]
        v = [v[k] - q * row[k] for k in range(len(v))]
    return not any(v)


def plane_part(H3):
    perm = [(r[2], r[0], r[1]) for r in H3]
    e = echelon(perm, 3)
    return echelon([(r[1], r[2]) for r in e if r[0] == 0], 2)


def F_L_single(P, H30):
    """F_L for Q_2 = {P} (closure report, Thm 3.7).  None = infinity."""
    if not H30:
        return 1
    if len(H30) == 2:
        return None          # admissible K_2 has rank <= 1, H_3^0 has rank 2
    g = H30[0]
    g0 = gcd(abs(g[0]), abs(g[1]))
    prim = (g[0] // g0, g[1] // g0)
    if prim[0] * prim[1] >= 0:
        return None          # direction inside the quadrant: no rank-1 admissible K_2 along it
    # K_2 = Z(m*prim) admissible iff P + m*prim and P - m*prim leave Pi_2
    m = 1
    while True:
        a = (P[0] + m * prim[0], P[1] + m * prim[1])
        b = (P[0] - m * prim[0], P[1] - m * prim[1])
        if min(a) < 1 and min(b) < 1:
            break
        m += 1
    best = None
    for mm in range(m, m + g0 + 1):
        idx = (mm * g0 // gcd(mm, g0)) // g0     # [Z g : Z g cap Z (mm prim)]
        best = idx if best is None else min(best, idx)
    return best


def V_contains(P, Q3):
    H3 = echelon([sub(p, Q3[0]) for p in Q3], 3)
    return in_lattice(sub((P[0], P[1], 0), Q3[0]), H3), H3


# ---------------------------------------------------------------------------
# case (ii): apexes (Lemma 1') and the necessary conditions (N2)-(N5') of Lemma D'
# ---------------------------------------------------------------------------


def apex_list(F):
    """P = p1 + p2 - p12 in Pi_2 (p's in F), with Q_2 = {P} compatible with (T)."""
    planed = [sub(w, u) for u in F for w in F if u != w and u[2] == w[2]]
    out = []
    for p1, p2 in itertools.combinations_with_replacement(F, 2):
        for p12 in F:
            P = sub(add(p1, p2), p12)
            if P[2] != 0 or P[0] < 1 or P[1] < 1:
                continue
            if any(min(P[0] + d[0], P[1] + d[1]) >= 1 for d in planed):
                continue
            out.append((P, p1, p2, p12))
    return out


def theta_min(F, P, p1, p2):
    """least theta for which (N2)-(N5') hold with W_t = p1, W_t' = p2, pi(W) = P:
       (N2) |p_i| < |P| ; omega_i = r_i with r_ic = p_ic, r_i,ab >= (p_i - P)^+ , |r_i| <= theta ;
       Y_i = pi(y(t_i)) = P - p_i + r_i (c-free), |Y_i| > theta (t_i heavy) ;
       marks: Y_1 + Y_2 <= P - (1,1) ;
       (N5') some q in F with e := (P - q)^+_ab <= M <= Y_i, |M| <= theta."""
    nP = P[0] + P[1]
    if sum(p1) >= nP or sum(p2) >= nP:
        return None
    defs = [(max(0, P[0] - q[0]), max(0, P[1] - q[1])) for q in F]
    for th in range(1, nP + 1):
        opts = []
        for p in (p1, p2):
            base = p[2] + max(0, p[0] - P[0]) + max(0, p[1] - P[1])
            if base > th:
                opts = None
                break
            slack = th - base
            Ym = (max(0, P[0] - p[0]), max(0, P[1] - p[1]))
            o = []
            for ea in range(slack + 1):
                for eb in range(slack + 1 - ea):
                    Y = (Ym[0] + ea, Ym[1] + eb)
                    if Y[0] + Y[1] <= th:
                        continue
                    if any(e[0] + e[1] <= th and e[0] <= Y[0] and e[1] <= Y[1] for e in defs):
                        o.append(Y)
            if not o:
                opts = None
                break
            opts.append(o)
        if opts is None:
            continue
        for Y1 in opts[0]:
            for Y2 in opts[1]:
                if Y1[0] + Y2[0] <= P[0] - 1 and Y1[1] + Y2[1] <= P[1] - 1:
                    return th
    return None


def admissible_apexes(F, P=None):
    res = []
    for PP, p1, p2, p12 in apex_list(F):
        if P is not None and PP[:2] != tuple(P):
            continue
        if max(sum(p1), sum(p2), sum(p12)) >= PP[0] + PP[1]:
            continue
        t = theta_min(F, PP, p1, p2)
        if t is not None:
            res.append((PP, (p1, p2, p12), t))
    return res


# ---------------------------------------------------------------------------
# E1
# ---------------------------------------------------------------------------


def E1(rng, quick):
    st = {'random_finite_closures': 0, 'rank<=2': 0, 'rank3': 0, 'VIOLATION_rank<=2_not_positive': 0,
          'exhaustive_3pt_seeds': 0, 'exhaustive_finite': 0}
    trials = 1500 if quick else 6000
    for _ in range(trials):
        k = rng.randint(3, 5)
        n = rng.randint(4, 9)
        seed = set()
        while len(seed) < k:
            p = [rng.randint(1, n) for _ in range(3)]
            p[rng.randrange(3)] = rng.randint(1, 3)
            seed.add(tuple(p))
        F = closure(seed, 4 * n + 4, maxpts=200)
        if F is None:
            continue
        st['random_finite_closures'] += 1
        r = rank_of(F)
        if r <= 2:
            st['rank<=2'] += 1
            if not positive_level(F):
                st['VIOLATION_rank<=2_not_positive'] += 1
        else:
            st['rank3'] += 1
    pts = [p for p in itertools.product(range(1, 5), repeat=3)]
    combos = list(itertools.combinations(pts, 3))
    if quick:
        combos = rng.sample(combos, 6000)
    for seed in combos:
        st['exhaustive_3pt_seeds'] += 1
        F = closure(seed, 20, maxpts=150)
        if F is None:
            continue
        st['exhaustive_finite'] += 1
        if rank_of(F) <= 2 and not positive_level(F):
            st['VIOLATION_rank<=2_not_positive'] += 1
    return st


# ---------------------------------------------------------------------------
# E2
# ---------------------------------------------------------------------------


def lang_report(Q3, P):
    Q = [(P[0], P[1], 0)] + list(Q3)
    T = check_T_finite(Q)
    Vok, H3 = V_contains(P, list(Q3))
    H30 = plane_part(H3)
    FL = F_L_single(P, H30)
    Bab = max(p[0] + p[1] for p in Q3)
    Kc = len({p[2] for p in Q3})
    ap = admissible_apexes(list(Q3), P)
    is_apex = any(PP[:2] == tuple(P) and max(sum(p1), sum(p2), sum(p12)) < sum(P)
                  for PP, p1, p2, p12 in apex_list(list(Q3)))
    short = [q for q in Q3 if sum(q) < sum(P)]
    return {'T_viol': T, 'closed3': closed3(list(Q3)), 'rank': rank_of(Q3), 'V_meets_Q2': Vok,
            'F_L': 'inf' if FL is None else FL, 'mu': sum(P), 'B_ab': Bab, 'K_c': Kc,
            'apex_of_shorter': is_apex, 'admissible_caseii': [a[2] for a in ap],
            'short_part_positive_level': positive_level(short) if short else True}


def seg(d, base):
    out, k = [], 0
    while True:
        x = tuple(base[i] + k * d[i] for i in range(3))
        if min(x) < 1:
            return out
        out.append(x)
        k += 1


def E2(quick):
    rows = {}
    F4 = [(1, 3, 12), (4, 8, 1), (6, 4, 4), (12, 1, 3)]
    rows['F4: closed, rank, det'] = (closed3(F4), rank_of(F4),
                                     det3(sub(F4[0], F4[1]), sub(F4[2], F4[1]), sub(F4[3], F4[1])))
    rows['F4 + P=(10,5)'] = lang_report(F4, (10, 5))
    # pick a far point of V for F4
    far = None
    for s in range(40, 120):
        for a in range(1, s):
            if V_contains((a, s - a), F4)[0]:
                far = (a, s - a)
                break
        if far:
            break
    rows['F4 + far P in V'] = (far, lang_report(F4, far))
    fam = []
    rng_xy = [(4, 4), (5, 4), (6, 9), (10, 10), (30, 5), (25, 40)] if quick else \
        [(x, y) for x in range(4, 13) for y in range(4, 13)] + [(30, 5), (25, 40), (60, 7)]
    bad = 0
    for X, Y in rng_xy:
        F = [(1, Y + 1, 1), (X + 1, 1, 1), (2, 2, 2), (1, 1, 4)]
        rep = lang_report(F, (X, Y))
        ok = (rep['T_viol'] == 0 and rep['closed3'] and rep['rank'] == 3 and rep['V_meets_Q2']
              and rep['F_L'] == 'inf' and rep['apex_of_shorter'] and rep['admissible_caseii'] == []
              and 2 * rep['B_ab'] - 2 >= rep['mu'] and not rep['short_part_positive_level'])
        if not ok:
            bad += 1
            fam.append(((X, Y), rep))
    rows['F_{X,Y}: #params, #not as claimed'] = (len(rng_xy), bad, fam[:3])
    rows['F_{30,5} report'] = lang_report([(1, 6, 1), (31, 1, 1), (2, 2, 2), (1, 1, 4)], (30, 5))
    # family S_n (Example 3 of the report): segment s_k=(2k,2(n+1-k),k), Z=(1,1,2n), A=(4n,1,1), P=(4n-3,3)
    segrows, bad = [], 0
    for n in range(3, 10 if quick else 16):
        F = seg((2, -2, 1), (2, 2 * n, 1)) + [(1, 1, 2 * n), (4 * n, 1, 1)]
        P = (4 * n - 3, 3)
        rep = lang_report(F, P)
        short = [q for q in F if sum(q) < sum(P)]
        ok = (rep['closed3'] and rep['T_viol'] == 0 and rep['rank'] == 3 and rep['F_L'] == 'inf'
              and rep['V_meets_Q2'] and rep['mu'] == 4 * n and rep['B_ab'] == 4 * n + 1
              and rep['K_c'] == n + 1 and not rep['apex_of_shorter'] and rep['short_part_positive_level']
              and rank_of(short) == 2)
        if not ok:
            bad += 1
        segrows.append((n, rep['mu'], rep['B_ab'], rep['K_c']))
    rows['S_n (n, mu, B_ab, K_c); #not as claimed'] = (segrows, bad)
    F5 = [(1, 1, 10), (2, 6, 1), (4, 4, 2), (6, 2, 3), (12, 1, 1)]
    rows['5-point rank-3 example'] = (closed3(F5), rank_of(F5), len(admissible_apexes(F5)))
    E4ex = [(1, 4, 6), (3, 9, 3), (9, 3, 1), (1, 27, 1)]
    rows['Example 4: S + satellite (1,27,1), P=(5,14)'] = lang_report(E4ex, (5, 14))
    return rows


# ---------------------------------------------------------------------------
# E3 / E4
# ---------------------------------------------------------------------------


def E3(rng, quick):
    st = {'rank3_4pt_sets': 0, 'apexes': 0, 'apexes_of_shorter_points': 0, 'admissible': 0}
    T = 200000 if quick else 1200000
    n = 20
    for _ in range(T):
        F = []
        for i in range(4):
            p = [rng.randint(1, n) for _ in range(3)]
            p[i % 3] = rng.randint(1, 2)
            F.append(tuple(p))
        if len(set(F)) < 4 or not closed3(F) or rank_of(F) != 3:
            continue
        st['rank3_4pt_sets'] += 1
        for P, p1, p2, p12 in apex_list(F):
            st['apexes'] += 1
            if max(sum(p1), sum(p2), sum(p12)) < P[0] + P[1]:
                st['apexes_of_shorter_points'] += 1
                if theta_min(F, P, p1, p2) is not None:
                    st['admissible'] += 1
    return st


def E4(rng, quick):
    st = {'positive_level_bases_with_admissible_apex': 0, 'rank3_after_one_satellite': 0,
          'admissible_after_satellite': 0, 'VIOLATION_short_part_not_positive': 0,
          'satellite_shorter_than_P': 0}
    T = 1500 if quick else 5000
    bases = []
    for _ in range(T):
        k = rng.randint(3, 5)
        seed = set()
        while len(seed) < k:
            p = [rng.randint(1, 10) for _ in range(3)]
            p[rng.randrange(3)] = rng.randint(1, 3)
            seed.add(tuple(p))
        F = closure(seed, 30, maxpts=150)
        if F is None:
            continue
        F = sorted(F)
        if admissible_apexes(F):
            bases.append(F)
    bases.append([(1, 4, 6), (3, 9, 3), (9, 3, 1)])   # base of Example 4 (report section 5)
    st['positive_level_bases_with_admissible_apex'] = len(bases)
    for F in bases:
        M = max(max(p) for p in F)
        cand = {(x, y, z) for x in range(1, 4 * M) for y in range(1, 4 * M) for z in range(1, 4 * M)
                if sorted((x, y, z))[1] <= 3}
        for s in cand:
            if s in F:
                continue
            G = F + [s]
            if not (closed3(G) and rank_of(G) == 3):
                continue
            st['rank3_after_one_satellite'] += 1
            for PP, tri, t in admissible_apexes(G):
                st['admissible_after_satellite'] += 1
                short = [q for q in G if sum(q) < PP[0] + PP[1]]
                if s in short:
                    st['satellite_shorter_than_P'] += 1
                if not positive_level(short):
                    st['VIOLATION_short_part_not_positive'] += 1
    return st


# ---------------------------------------------------------------------------
# E5
# ---------------------------------------------------------------------------


def E5():
    Y23 = [(1, 2, 5), (1, 26, 1), (11, 10, 2), (24, 3, 1)]
    X = [(3, 2, 1), (1, 3, 2), (2, 1, 3)]
    out = {}
    for name, F, P in (('Y23', Y23, (10, 23)), ('X', X, (5, 1))):
        rep = lang_report(F, P)
        allap = [(PP[:2], tuple(map(sum, (p1, p2, p12)))) for PP, p1, p2, p12 in apex_list(F)]
        out[name] = {'positive_level': positive_level(F), 'F_L': rep['F_L'], 'T_viol': rep['T_viol'],
                     'V_meets_Q2': rep['V_meets_Q2'], 'apexes(P, lengths of p1,p2,p12)': allap,
                     'P is apex of shorter points': rep['apex_of_shorter']}
    return out


# ---------------------------------------------------------------------------
# E6: grammars
# ---------------------------------------------------------------------------


def parikh_sets(G, start, cap=4000):
    """exact Parikh sets of an acyclic CFG (dict X -> list of rhs tuples)."""
    order = []
    seen = set()

    def visit(X, stack):
        if X in seen:
            return True
        if X in stack:
            return False
        stack.add(X)
        for rhs in G[X]:
            for s in rhs:
                if not isinstance(s, str) and not visit(s, stack):
                    return False
        stack.discard(X)
        seen.add(X)
        order.append(X)
        return True
    if not visit(start, set()):
        return None
    P = {}
    for X in order:
        S = set()
        for rhs in G[X]:
            cur = {(0, 0, 0)}
            for s in rhs:
                if isinstance(s, str):
                    e = {'a': (1, 0, 0), 'b': (0, 1, 0), 'c': (0, 0, 1)}[s]
                    cur = {add(x, e) for x in cur}
                else:
                    cur = {add(x, y) for x in cur for y in P[s]}
                if len(cur) > cap:
                    return None
            S |= cur
        P[X] = S
    return P


def gstats(G, start):
    """v, r, theta_loc for the reduced grammar (all nonterminals assumed useful)."""
    INF = float('inf')
    tau = {X: INF for X in G}
    ch = True
    while ch:
        ch = False
        for X, rules in G.items():
            for rhs in rules:
                l = sum(1 if isinstance(s, str) else tau[s] for s in rhs)
                if l < tau[X]:
                    tau[X] = l
                    ch = True
    theta = max(sum(1 if isinstance(s, str) else tau[s] for s in rhs) for rs in G.values() for rhs in rs)
    r = max(max(sum(1 for s in rhs if not isinstance(s, str)) for rhs in rs) for rs in G.values())
    return len(G), max(r, 1), theta


def reduce_grammar(G, start):
    prod = set()
    ch = True
    while ch:
        ch = False
        for X, rules in G.items():
            if X not in prod and any(all(isinstance(s, str) or s in prod for s in rhs) for rhs in rules):
                prod.add(X)
                ch = True
    if start not in prod:
        return None
    G = {X: [rhs for rhs in rs if all(isinstance(s, str) or s in prod for s in rhs)]
         for X, rs in G.items() if X in prod}
    reach, st = {start}, [start]
    while st:
        X = st.pop()
        for rhs in G[X]:
            for s in rhs:
                if not isinstance(s, str) and s not in reach:
                    reach.add(s)
                    st.append(s)
    return {X: G[X] for X in reach}


def random_acyclic(rng, v):
    G = {}
    for X in range(v):
        rules = []
        for _ in range(rng.randint(1, 3)):
            k = rng.randint(1, 3)
            rhs = []
            for _ in range(k):
                if X < v - 1 and rng.random() < 0.55:
                    rhs.append(rng.randint(X + 1, v - 1))
                else:
                    rhs.append(rng.choice('aabbc'))
            rules.append(tuple(rhs))
        G[X] = rules
    return G


def random_weighted(rng, v, lam, Wmax):
    """every rule of X has weight w_X (lambda(c) > 0): every word of L(G) lies on one level."""
    w = {X: rng.randint(1, Wmax) for X in range(v)}
    G = {X: [] for X in range(v)}
    wt = lambda s: lam[0] if s == 'a' else lam[1] if s == 'b' else lam[2] if s == 'c' else w[s]
    for X in range(v):
        tries = 0
        while len(G[X]) < 3 and tries < 600:
            tries += 1
            k = rng.randint(1, 3)
            rhs = tuple(rng.choice(['a', 'b', 'c'] + [Y for Y in range(X + 1, v)]) for _ in range(k))
            if sum(wt(s) for s in rhs) == w[X]:
                G[X].append(rhs)
    return G


def E6(rng, quick):
    st = {'acyclic_grammars_with_ab': 0, 'VIOLATION_LemmaK': 0, 'max mu/((Kc+3)v theta)': 0.0,
          'L_prime_hypothesis_holds': 0, 'VIOLATION_TheoremLprime': 0,
          'weighted_grammars_with_ab': 0, 'VIOLATION_TheoremLprime_weighted': 0,
          'max mu/(v theta) weighted': 0.0}
    T = 3000 if quick else 15000
    for _ in range(T):
        G = reduce_grammar(random_acyclic(rng, rng.randint(2, 7)), 0)
        if G is None:
            continue
        P = parikh_sets(G, 0)
        if P is None:
            continue
        L = P[0]
        ab = [p for p in L if p[0] and p[1] and not p[2]]
        if not ab:
            continue
        st['acyclic_grammars_with_ab'] += 1
        mu = min(sum(p) for p in ab)
        abc = [p for p in L if p[0] and p[1] and p[2]]
        Kc = len({p[2] for p in abc})
        v, r, th = gstats(G, 0)
        if mu > (Kc + 3) * v * th:
            st['VIOLATION_LemmaK'] += 1
        st['max mu/((Kc+3)v theta)'] = max(st['max mu/((Kc+3)v theta)'], round(mu / ((Kc + 3) * v * th), 3))
        short = [p for p in abc if sum(p) < mu]
        if positive_level(short) if short else True:
            st['L_prime_hypothesis_holds'] += 1
            if mu > max(9 * (r + 1) * v * th, 11 * (r + 1) * v * v * th ** 4):
                st['VIOLATION_TheoremLprime'] += 1
    for _ in range(T // 3):
        lam = (rng.randint(1, 6), rng.randint(1, 6), rng.randint(1, 6))
        G = reduce_grammar(random_weighted(rng, rng.randint(2, 6), lam, 16), 0)
        if G is None:
            continue
        P = parikh_sets(G, 0)
        if P is None:
            continue
        ab = [p for p in P[0] if p[0] and p[1] and not p[2]]
        if not ab:
            continue
        st['weighted_grammars_with_ab'] += 1
        mu = min(sum(p) for p in ab)
        v, r, th = gstats(G, 0)
        if mu > max(9 * (r + 1) * v * th, 11 * (r + 1) * v * v * th ** 4):
            st['VIOLATION_TheoremLprime_weighted'] += 1
        st['max mu/(v theta) weighted'] = max(st['max mu/(v theta) weighted'], round(mu / (v * th), 3))
    return st


# ---------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--quick', action='store_true')
    a = ap.parse_args()
    rng = random.Random(a.seed)
    for name, fn in (('E1 planar lemma', lambda: E1(rng, a.quick)),
                     ('E2 examples', lambda: E2(a.quick)),
                     ('E3 random rank-3 4-point sets', lambda: E3(rng, a.quick)),
                     ('E4 positive-level bases + satellite', lambda: E4(rng, a.quick)),
                     ('E5 Y23, X', E5),
                     ('E6 grammars', lambda: E6(rng, a.quick))):
        t0 = time.time()
        res = fn()
        if isinstance(res, dict) and name.startswith('E2'):
            print(name)
            for k, v in res.items():
                print('   ', k, ':', v)
            print('    [%.1fs]' % (time.time() - t0))
        else:
            print(name, ':', res, '[%.1fs]' % (time.time() - t0))
        sys.stdout.flush()


if __name__ == '__main__':
    main()
