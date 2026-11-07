#!/usr/bin/env python3
"""check_claude_prop72_2026-11-07.py  (standard library only)

Checks for reviews/claude_prop72_2026-11-07.md (Proposition 7.2: Parikh-saturated
substitutable languages with infinite Q_3 and no (P+)).

  S1  condition (T) (= Lemma 2.3 moves) on boxes for the named examples, with the
      lattice data H_2, H_3^0, V and the index F_L computed exactly
  S2  random move closures in a box: the structural lemmas B1/B3 (sign pattern of
      the nonnegative differences) and the case frequencies
  S3  exhaustive small (beta-III) families: (T) on a box, then Theorem S
      ("V meets Q_2  =>  F_L = 1") and the F_L values when V misses Q_2
  S4  Lemma W on random weight-homogeneous CFGs: mu_ab <= 7(r+1) v^2 theta^2
  S5  finite Q_3: exact finite SUB_1 closures; V, F_L, B_ab, positive level
  S6  closures of seeds of the shape forced by case (ii) (x, x+d1, x+d2, x+d1+d2)
  S7  finite Q_3 alone; F_L for every compatible single point of V (Conjecture 7.3)

Finite computations only detect violations or find structure; the statements about
infinite languages are proved in the report.  Run:  python3 check_claude_prop72_2026-11-07.py [--seed 1] [--quick]
"""
import argparse
import itertools
import random
import sys
import time
from math import gcd

A, B, C = 0, 1, 2


# ---------------------------------------------------------------------------
# vectors and moves
# ---------------------------------------------------------------------------
def vadd(u, v):
    return tuple(x + y for x, y in zip(u, v))


def vsub(u, v):
    return tuple(x - y for x, y in zip(u, v))


def vneg(u):
    return tuple(-x for x in u)


def supp(v):
    return frozenset(i for i, x in enumerate(v) if x)


def valid(alpha, h):
    """Lemma 2.3: the h-move is valid at alpha."""
    for i, x in enumerate(h):
        if x and (alpha[i] < 1 or alpha[i] + x < 1):
            return False
    return True


def diffs_same_support(Q):
    groups = {}
    for q in Q:
        groups.setdefault(supp(q), []).append(q)
    D = set()
    for pts in groups.values():
        for p in pts:
            for q in pts:
                if p != q:
                    D.add(vsub(q, p))
    return D


# ---------------------------------------------------------------------------
# integer lattices (echelon / Hermite-like form)
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
    # reduce entries above pivots (not needed for membership)
    return basis


def pivot(row):
    for i, x in enumerate(row):
        if x:
            return i
    return None


def in_lattice(v, basis):
    v = list(v)
    for row in basis:
        j = pivot(row)
        if v[j] % row[j] != 0:
            return False
        q = v[j] // row[j]
        v = [v[k] - q * row[k] for k in range(len(v))]
    return not any(v)


def plane_part(basis3):
    """{h in H : h_c = 0} for a lattice H in Z^3 (coordinates a,b,c)."""
    perm = [(r[C], r[A], r[B]) for r in basis3]
    e = echelon(perm, 3)
    out = []
    for r in e:
        if r[0] == 0:
            out.append((r[1], r[2]))
    return echelon(out, 2)


def lattice2(vecs):
    return echelon([tuple(v[:2]) for v in vecs], 2)


# ---------------------------------------------------------------------------
# F_L for finite Q_2  (closure report, Theorem 3.7)
# ---------------------------------------------------------------------------
def in_Pi2(p):
    return p[0] >= 1 and p[1] >= 1


def admissible_rank1(k, q2, Q2set):
    """(q2 + Zk) cap Pi_2 == Q2 for finite Q2."""
    if (k[0] >= 0 and k[1] >= 0) or (k[0] <= 0 and k[1] <= 0):
        return False  # a ray inside Pi_2 (k != 0)
    pts = set()
    for sgn in (1, -1):
        j = 0
        while True:
            p = (q2[0] + sgn * j * k[0], q2[1] + sgn * j * k[1])
            if not in_Pi2(p):
                break
            pts.add(p)
            j += 1
    return pts == Q2set


def F_L_finite(Q2set, H30, jmax=400):
    """Exact F_L when Q_2 is finite: returns an int, or None for infinity
    (or > jmax, never reached in the examples)."""
    if not H30:
        return 1
    q2 = min(Q2set)
    H2 = lattice2([vsub(p, q2) for p in Q2set])
    if len(H30) == 2:
        return None  # every finite-index K has rank 2, hence a positive vector
    g = H30[0]
    best = None
    for j in range(1, jmax + 1):
        K = echelon(list(H2) + [(j * g[0], j * g[1])], 2)
        if len(K) == 2:
            continue
        k = K[0]
        if not admissible_rank1(k, q2, Q2set):
            continue
        # index [Zg : Zk cap Zg]
        g0 = gcd(abs(g[0]), abs(g[1]))
        k0 = gcd(abs(k[0]), abs(k[1]))
        prim = (g[0] // g0, g[1] // g0)
        if (k[0] // k0, k[1] // k0) not in (prim, (-prim[0], -prim[1])):
            continue
        lcm = g0 * k0 // gcd(g0, k0)
        idx = lcm // g0
        if best is None or idx < best:
            best = idx
    if best is None and not H2 and len(Q2set) == 1:
        return None
    return best


# ---------------------------------------------------------------------------
# condition (T) on a box for a membership predicate
# ---------------------------------------------------------------------------
def box_points(Bx, dim=3):
    return [p for p in itertools.product(range(Bx + 1), repeat=dim) if any(p)]


def check_T_box(inQ, Bx):
    """Violations of Lemma 2.3 (equivalently (T)) with alpha, alpha+h in the box."""
    pts = [p for p in box_points(Bx) if inQ(p)]
    Qs = set(pts)
    D = diffs_same_support(pts)
    viol = 0
    inbox = lambda p: all(0 <= x <= Bx for x in p)
    for h in D:
        for al in pts:
            be = vadd(al, h)
            if inbox(be) and valid(al, h) and be not in Qs:
                viol += 1
            ga = vsub(al, h)
            if inbox(ga) and valid(ga, h) and ga not in Qs:
                viol += 1
    return viol, len(pts), len(D)


def check_T_finite(Q):
    """Exact (T) for a finite Q (no box): every valid move from a point of Q lands in Q."""
    Qs = set(Q)
    D = diffs_same_support(Q)
    viol = 0
    for h in D:
        for al in Q:
            be = vadd(al, h)
            if valid(al, h) and be not in Qs:
                viol += 1
            ga = vsub(al, h)
            if min(ga) >= 0 and valid(ga, h) and ga not in Qs:
                viol += 1
    return viol


def lattice_data(Q2, Q3):
    """H_2 (2D), H_3 (3D), H_3^0 (2D), q3."""
    H2 = lattice2([vsub(p, Q2[0]) for p in Q2]) if Q2 else []
    H3 = echelon([vsub(p, Q3[0]) for p in Q3], 3) if Q3 else []
    H30 = plane_part(H3) if Q3 else []
    return H2, H3, H30


def V_meets_Q2(Q2, Q3, H3):
    """Is (q,0) in q3 + H_3 for some q in Q_2 ?"""
    q3 = Q3[0]
    return any(in_lattice(vsub((q[0], q[1], 0), q3), H3) for q in Q2)


def Pplus(Q2):
    return any(q[0] > p[0] and q[1] > p[1] for p in Q2 for q in Q2)


# ---------------------------------------------------------------------------
# S1: named examples
# ---------------------------------------------------------------------------
def S1(quick):
    out = []
    # E_N : (beta-III), V misses Q_2, F_L ~ N/2
    Ns = range(2, 6) if quick else range(2, 9)
    rows = []
    for N in Ns:
        def inQ(p, N=N):
            a, b, c = p
            if c == 0:
                return (a, b) == (N, N)
            return (a, b) == (1, 2) and c % 2 == 1 or (a, b) == (2, 1) and c % 2 == 0
        Bx = N + 4
        viol, npts, nd = check_T_box(inQ, Bx)
        Q2 = [(N, N)]
        Q3 = [p for p in box_points(Bx) if p[2] > 0 and inQ(p)]
        H2, H3, H30 = lattice_data(Q2, Q3)
        rows.append((N, viol, tuple(H30), V_meets_Q2(Q2, Q3, H3), F_L_finite(set(Q2), H30), 2 * N))
    out.append(('E_N (N, T-viol, H30, V meets Q2, F_L, mu_ab)', rows))

    # L^(t) : (beta-III), V meets Q_2, F_L = 1
    rows = []
    for t in (range(1, 4) if quick else range(1, 6)):
        def inQ(p, t=t):
            a, b, c = p
            if c == 0:
                return (a, b) == (1, 2 * t + 1)
            return a >= 1 and b >= 1 and t * a + b == 3 * t + 1 and (c - (a - 1)) % 3 == 0
        Bx = 2 * t + 4
        viol, npts, nd = check_T_box(inQ, Bx)
        Q2 = [(1, 2 * t + 1)]
        Q3 = [p for p in box_points(Bx) if p[2] > 0 and inQ(p)]
        H2, H3, H30 = lattice_data(Q2, Q3)
        rows.append((t, viol, tuple(H30), V_meets_Q2(Q2, Q3, H3), F_L_finite(set(Q2), H30), 2 * t + 2))
    out.append(('L^(t) (t, T-viol, H30, V meets Q2, F_L, mu_ab)', rows))

    # S_M : (beta-III) with |Q_2| >= 2 and V meeting Q_2  (line a+b=M, parity heights)
    rows = []
    for M in (range(4, 8) if quick else range(4, 11)):
        def inQ(p, M=M):
            a, b, c = p
            if a < 1 or b < 1 or a + b != M:
                return False
            if c == 0:
                return a % 2 == 1
            return (c - (a - 1)) % 2 == 0
        Bx = M + 2
        viol, npts, nd = check_T_box(inQ, Bx)
        Q2 = sorted({(p[0], p[1]) for p in box_points(Bx) if p[2] == 0 and inQ(p)})
        Q3 = [p for p in box_points(Bx) if p[2] > 0 and inQ(p)]
        H2, H3, H30 = lattice_data(Q2, Q3)
        rows.append((M, viol, len(Q2), tuple(H2), tuple(H30), V_meets_Q2(Q2, Q3, H3), F_L_finite(set(Q2), H30)))
    out.append(('S_M (M, T-viol, |Q2|, H2, H30, V meets Q2, F_L)', rows))

    # other cases: (alpha), (beta-I), (beta-II)
    rows = []
    N = 5

    def inQ_alpha(p):  # x+y=2z ; Q2 = x+y=N
        a, b, c = p
        if a < 1 or b < 1:
            return False
        return a + b == N if c == 0 else a + b == 2 * c

    def inQ_b1(p):  # Q3 = a^x b c^z ; Q2 = b-count N
        a, b, c = p
        if a < 1 or b < 1:
            return False
        return b == N if c == 0 else b == 1

    def inQ_b2(p):  # Q2 = {(x,N): x odd}; fibers (b,c)=(1,2): x odd, (2,1): x even
        a, b, c = p
        if a < 1 or b < 1:
            return False
        if c == 0:
            return b == N and a % 2 == 1
        return (b, c) == (1, 2) and a % 2 == 1 or (b, c) == (2, 1) and a % 2 == 0

    for name, inQ in (('alpha', inQ_alpha), ('beta-I', inQ_b1), ('beta-II', inQ_b2)):
        viol, npts, nd = check_T_box(inQ, 9)
        pts = [p for p in box_points(9) if inQ(p)]
        Q2 = [(p[0], p[1]) for p in pts if p[2] == 0]
        Q3 = [p for p in pts if p[2] > 0]
        H2, H3, H30 = lattice_data(Q2, Q3)
        sub = all(in_lattice(h, H2) for h in H30)
        rows.append((name, viol, tuple(H2), tuple(H30), 'H30 in H2' if sub else 'H30 not in H2', Pplus(Q2)))
    out.append(('other cases (name, T-viol on box 9, H2, H30, inclusion, (P+))', rows))

    # finite Q_3: X = {(5,1,0)} + triangle ; T_n
    rows = []
    tri = [(3, 2, 1), (1, 3, 2), (2, 1, 3)]
    X = [(5, 1, 0)] + tri
    H2, H3, H30 = lattice_data([(5, 1)], tri)
    rows.append(('X={(5,1,0)}+tri', check_T_finite(X), tuple(H30), V_meets_Q2([(5, 1)], tri, H3),
                 F_L_finite({(5, 1)}, H30)))
    # Y_23: finite Q_3 on the level a+b+6c=33, Q_2 = {(10,23)} on V, F_L = 23
    Y3 = [(1, 2, 5), (1, 26, 1), (11, 10, 2), (24, 3, 1)]
    Y = [(10, 23, 0)] + Y3
    H2, H3, H30 = lattice_data([(10, 23)], Y3)
    rows.append(('Y23={(10,23,0)}+4pts', check_T_finite(Y), tuple(H30), V_meets_Q2([(10, 23)], Y3, H3),
                 F_L_finite({(10, 23)}, H30)))
    for n in range(1, 5 if quick else 7):
        Q2 = [(1 + 3 * n, 1), (1, 1 + 3 * n)]
        Qn = [(q[0], q[1], 0) for q in Q2] + tri
        H2, H3, H30 = lattice_data(Q2, tri)
        rows.append(('T_%d' % n, check_T_finite(Qn), tuple(H30), V_meets_Q2(Q2, tri, H3),
                     F_L_finite(set(Q2), H30)))
    out.append(('finite Q3 (name, exact T-viol, H30, V meets Q2, F_L)', rows))
    return out


# ---------------------------------------------------------------------------
# S2: random move closures in a box
# ---------------------------------------------------------------------------
def closure_box(seed_pts, Bx, max_pts=900):
    """Least set containing the seeds and closed under valid moves inside the box
    (every added point is forced, so the result is contained in the true least
    SUB_1 superset)."""
    Q = set(seed_pts)
    inbox = lambda p: all(0 <= x <= Bx for x in p)
    groups = {}
    for q in Q:
        groups.setdefault(supp(q), set()).add(q)
    D = diffs_same_support(Q)
    new_pts = set(Q)
    new_D = set(D)
    while new_pts or new_D:
        if len(Q) > max_pts:
            return Q, False
        added = set()
        # new diffs on all points, old diffs on new points
        for h in new_D:
            for al in Q:
                for be, ok in ((vadd(al, h), valid(al, h)), (vsub(al, h), None)):
                    if ok is None:
                        ok = inbox(be) and min(be) >= 0 and valid(be, h)
                    if ok and inbox(be) and be not in Q:
                        added.add(be)
        old_D = D - new_D
        for h in old_D:
            for al in new_pts:
                be = vadd(al, h)
                if inbox(be) and valid(al, h) and be not in Q:
                    added.add(be)
                ga = vsub(al, h)
                if inbox(ga) and min(ga) >= 0 and valid(ga, h) and ga not in Q:
                    added.add(ga)
        # differences created by the added points
        nd = set()
        for p in added:
            s = supp(p)
            for q in groups.get(s, ()):
                nd.add(vsub(q, p))
                nd.add(vsub(p, q))
            for q in added:
                if q != p and supp(q) == s:
                    nd.add(vsub(q, p))
        for p in added:
            Q.add(p)
            groups.setdefault(supp(p), set()).add(p)
        nd -= D
        D |= nd
        new_pts, new_D = added, nd
    return Q, True


def classify_box(Q, Bx):
    """Case of a box closure (only meaningful inside the box)."""
    Q2 = [(p[0], p[1]) for p in Q if p[2] == 0 and p[0] > 0 and p[1] > 0]
    Q3 = [p for p in Q if min(p) > 0]
    if Pplus(Q2):
        return 'P+'
    if not Q3 or max(max(p) for p in Q3) < Bx:
        return 'Q3_bounded'
    P = [vsub(q, p) for p in Q3 for q in Q3 if p != q and min(vsub(q, p)) >= 0]
    if any(min(d) > 0 for d in P):
        return 'alpha'
    hasA = any(d[A] > 0 for d in P)
    hasB = any(d[B] > 0 for d in P)
    if hasA and hasB:
        return 'flag_B1'
    lv = B if not hasB else A
    if len({p[lv] for p in Q3}) == 1:
        return 'beta_one_level'
    other = A if lv == B else B
    mixed = any(d[other] > 0 and d[C] > 0 for d in P)
    pure_o = any(d[other] > 0 and d[C] == 0 for d in P)
    pure_c = any(d[other] == 0 and d[C] > 0 for d in P)
    if mixed or (pure_o and pure_c):
        return 'flag_B3'
    return 'beta_a_periods' if pure_o else 'beta_c_periods'


def S2(rng, trials, Bx, Bbig=13):
    """A flag (B1/B3 pattern seen in the box) is re-tested in the larger box Bbig:
    the proofs of B1/B3 say that the sum of the two nonnegative differences is a
    strictly positive difference or gives (P+), and that sum may leave the small box.
    VIOLATION = still flagged in the larger box."""
    stats = {'closures': 0, 'too_big': 0}
    for _ in range(trials):
        seeds = set()
        for _ in range(rng.randint(1, 2)):
            seeds.add((rng.randint(1, Bx - 1), rng.randint(1, Bx - 1), 0))
        for _ in range(rng.randint(2, 3)):
            seeds.add((rng.randint(1, Bx - 2), rng.randint(1, Bx - 2), rng.randint(1, Bx - 2)))
        Q, ok = closure_box(seeds, Bx)
        stats['closures'] += 1
        if not ok:
            stats['too_big'] += 1
            continue
        c = classify_box(Q, Bx)
        if c.startswith('flag'):
            Q2_, ok2 = closure_box(seeds, Bbig, max_pts=8000)
            c2 = classify_box(Q2_, Bbig) if ok2 else 'too_big'
            if c2.startswith('flag'):
                c = 'VIOLATION_' + c[5:]
            else:
                c = c + '->' + c2 + '_in_box%d' % Bbig
        stats[c] = stats.get(c, 0) + 1
    return dict(sorted(stats.items()))


# ---------------------------------------------------------------------------
# S3: exhaustive small (beta-III) families
# ---------------------------------------------------------------------------
def Q2_compatible(Q2c, Q3set, in3, D30):
    """Exact (T) for Q = Q2c x {0}  +  Q_3, given that Q_3 alone satisfies (T):
    the only remaining moves are (i) differences of Q_2 acting anywhere and
    (ii) same-height differences of Q_3 acting on Pi_2 (moves keep the support,
    and a move with c in its support is never valid at a point with c = 0).
    The a,b-coordinates are not truncated, and c is unchanged by these moves."""
    Q2p = {(x, y, 0) for (x, y) in Q2c}

    def inQ(p):
        return (p[0], p[1]) in Q2c if p[2] == 0 else in3(p)
    for h in D30:
        for al in Q2p:
            be = vadd(al, h)
            if valid(al, h) and be not in Q2p:
                return False
            ga = vsub(al, h)
            if min(ga) >= 0 and valid(ga, h) and ga not in Q2p:
                return False
    D2 = {vsub(q, p) for p in Q2p for q in Q2p if p != q}
    for h in D2:
        for al in list(Q2p) + list(Q3set):
            be = vadd(al, h)
            if valid(al, h) and not inQ(be):
                return False
            ga = vsub(al, h)
            if min(ga) >= 0 and valid(ga, h) and not inQ(ga):
                return False
    return True


def S3(quick):
    res = {'Q3_families': 0, 'Q3_T_violations': 0, 'Q2_candidates': 0, 'SUB1_pass': 0,
           'V_meets_Q2': 0, 'VIOLATION_TheoremS': 0, 'V_misses_Q2': 0,
           'F_L_values_when_V_misses': {}, 'F_L_infinite_when_V_misses': 0}
    st_range = [(1, 1), (1, 2), (2, 1)] if quick else [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 3)]
    for s, t in st_range:
        for a0 in range(1, s + 1):
            for m in range(1, 4 if quick else 5):
                b0 = 1 + m * t  # last fibre has b = 1
                F = [(a0 + i * s, b0 - i * t) for i in range(m + 1)]
                for gp in range(1, 4 if quick else 5):
                    for de in range(gp):
                        for z0 in range(gp):
                            res['Q3_families'] += 1
                            fib = {f: (z0 + i * de) % gp for i, f in enumerate(F)}

                            def in3(p, fib=fib, gp=gp):
                                f = (p[0], p[1])
                                return p[2] >= 1 and f in fib and (p[2] - fib[f]) % gp == 0
                            Bx = max(max(f) for f in F) + 3
                            # Q_2 candidates: single points in a window, and
                            # segments (q + Z je) cap Pi_2 for q in F
                            cands = set()
                            for x in range(1, Bx):
                                for y in range(1, Bx):
                                    cands.add(frozenset([(x, y)]))
                            for i0 in range(m + 1):
                                for j in range(1, m + 1):
                                    seg = frozenset(f for k, f in enumerate(F) if (k - i0) % j == 0)
                                    if len(seg) >= 2:
                                        cands.add(seg)
                            Q3pts = [p for p in box_points(Bx) if p[2] > 0 and in3(p)]
                            H3 = echelon([vsub(p, Q3pts[0]) for p in Q3pts], 3)
                            H30 = plane_part(H3)
                            v0, _, _ = check_T_box(in3, Bx)
                            if v0:
                                res['Q3_T_violations'] += 1
                                continue
                            Q3set = set(Q3pts)
                            # realized same-height differences of Q_3 (they act on Pi_2)
                            D30 = {vsub(q, p) for p in Q3pts for q in Q3pts
                                   if p != q and p[2] == q[2]}
                            for Q2c in cands:
                                res['Q2_candidates'] += 1
                                if not Q2_compatible(Q2c, Q3set, in3, D30):
                                    continue
                                res['SUB1_pass'] += 1
                                Q2 = sorted(Q2c)
                                FL = F_L_finite(set(Q2), H30)
                                if V_meets_Q2(Q2, Q3pts, H3):
                                    res['V_meets_Q2'] += 1
                                    if FL != 1:
                                        res['VIOLATION_TheoremS'] += 1
                                else:
                                    res['V_misses_Q2'] += 1
                                    if FL is None:
                                        res['F_L_infinite_when_V_misses'] += 1
                                    else:
                                        d = res['F_L_values_when_V_misses']
                                        d[FL] = d.get(FL, 0) + 1
    res['F_L_values_when_V_misses'] = dict(sorted(res['F_L_values_when_V_misses'].items()))
    return res


# ---------------------------------------------------------------------------
# S4: Lemma W on weight-homogeneous CFGs
# ---------------------------------------------------------------------------
CONTENTS = [frozenset(s) for s in ([], ['a'], ['b'], ['c'], ['a', 'b'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c'])]


def grammar_stats(G, start):
    """G: dict X -> list of rhs tuples (symbols are 'a','b','c' or nonterminal ints).
    Returns (v, r, theta_loc, mu_ab) for the reduced grammar, or None."""
    # productive
    prod = set()
    changed = True
    while changed:
        changed = False
        for X, rules in G.items():
            if X in prod:
                continue
            for rhs in rules:
                if all(isinstance(s, str) or s in prod for s in rhs):
                    prod.add(X)
                    changed = True
                    break
    if start not in prod:
        return None
    G = {X: [rhs for rhs in rules if all(isinstance(s, str) or s in prod for s in rhs)]
         for X, rules in G.items() if X in prod}
    reach = {start}
    stack = [start]
    while stack:
        X = stack.pop()
        for rhs in G[X]:
            for s in rhs:
                if not isinstance(s, str) and s not in reach:
                    reach.add(s)
                    stack.append(s)
    G = {X: G[X] for X in reach}
    # tau
    INF = float('inf')
    tau = {X: INF for X in G}
    changed = True
    while changed:
        changed = False
        for X, rules in G.items():
            for rhs in rules:
                l = sum(1 if isinstance(s, str) else tau[s] for s in rhs)
                if l < tau[X]:
                    tau[X] = l
                    changed = True
    theta = max(sum(1 if isinstance(s, str) else tau[s] for s in rhs) for rules in G.values() for rhs in rules)
    r = max(sum(1 for s in rhs if not isinstance(s, str)) for rules in G.values() for rhs in rules)
    # best[X][content]
    best = {X: {} for X in G}
    changed = True
    while changed:
        changed = False
        for X, rules in G.items():
            for rhs in rules:
                opts = []
                for s in rhs:
                    if isinstance(s, str):
                        opts.append([(frozenset([s]), 1)])
                    else:
                        opts.append(list(best[s].items()))
                for combo in itertools.product(*opts):
                    cont = frozenset().union(*[c for c, _ in combo])
                    l = sum(x for _, x in combo)
                    if l < best[X].get(cont, INF):
                        best[X][cont] = l
                        changed = True
    mu = best[start].get(frozenset(['a', 'b']))
    return len(G), r, theta, mu


def random_weighted_grammar(rng, v, wa, wb, Wmax):
    """Every rule of X has total weight w_X (lambda(a)=wa, lambda(b)=wb, lambda(c)=0),
    so every generation of X has weight w_X and L(G) lies in one level."""
    w = {X: rng.randint(0, Wmax) for X in range(v)}
    w[0] = rng.randint(max(wa, wb) + 1, Wmax + max(wa, wb))
    G = {X: [] for X in range(v)}
    syms = ['a', 'b', 'c'] + list(range(v))
    wt = lambda s: wa if s == 'a' else wb if s == 'b' else 0 if s == 'c' else w[s]
    for X in range(v):
        tries = 0
        while len(G[X]) < 3 and tries < 400:
            tries += 1
            k = rng.randint(1, 3)
            rhs = tuple(rng.choice(syms) for _ in range(k))
            if sum(wt(s) for s in rhs) != w[X]:
                continue
            if rhs == (X,):
                continue
            G[X].append(rhs)
    return G


def S4(rng, trials):
    st = {'grammars': 0, 'with_ab_word': 0, 'VIOLATION_LemmaW': 0, 'max_mu/((r+1)v^2theta^2)': 0.0,
          'max_mu': 0, 'max_kappa_used': 0, 'theta>=kappa_cases': 0}
    for _ in range(trials):
        v = rng.randint(2, 6)
        wa, wb = rng.randint(1, 7), rng.randint(1, 7)
        G = random_weighted_grammar(rng, v, wa, wb, 14)
        res = grammar_stats(G, 0)
        st['grammars'] += 1
        if res is None or res[3] is None:
            continue
        vv, r, th, mu = res
        r = max(r, 1)
        st['with_ab_word'] += 1
        bound = 7 * (r + 1) * vv * vv * th * th
        if mu > bound:
            st['VIOLATION_LemmaW'] += 1
        ratio = mu / ((r + 1) * vv * vv * th * th)
        st['max_mu/((r+1)v^2theta^2)'] = max(st['max_mu/((r+1)v^2theta^2)'], round(ratio, 4))
        st['max_mu'] = max(st['max_mu'], mu)
        kap = max(wa, wb) / min(wa, wb)
        st['max_kappa_used'] = max(st['max_kappa_used'], round(kap, 3))
        if th >= kap:
            st['theta>=kappa_cases'] += 1
    return st


def lemmaW_family(tmax):
    """Thin attempt at L^(t): X_t -> b^t | a c (the obvious thin-looking grammar) ;
    lemma W predicts theta >= t once a heavy b-pure unmarked node appears."""
    rows = []
    for t in range(2, tmax + 1):
        # S -> a Y Y ;  Y -> X B ; X -> b^t | a c ; B -> b   (weights: a=t, b=1, c=0)
        # here the rule X -> b^t has rho = t
        G = {0: [('a', 1, 1, 'b')], 1: [(2,)], 2: [tuple('b' * t), ('a', 'c')]}
        vv, r, th, mu = grammar_stats(G, 0)
        rows.append((t, vv, th, mu))
    return rows


# ---------------------------------------------------------------------------
# S5: finite Q_3
# ---------------------------------------------------------------------------
def positive_level(H3):
    """Does span(H3) contain no nonzero nonnegative vector?  (Stiemke)"""
    if not H3:
        return True
    if len(H3) == 3:
        return False
    if len(H3) == 1:
        u = H3[0]
        return any(x > 0 for x in u) and any(x < 0 for x in u)
    u, w = H3
    n = (u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0])
    return all(x > 0 for x in n) or all(x < 0 for x in n)


def S5(rng, trials, Bx):
    st = {'trials': 0, 'finite_exact_SUB1': 0, 'with_Q2_and_Q3_noPplus': 0,
          'Q3_on_positive_level': 0, 'Q3_NOT_on_positive_level': 0,
          'V_meets_Q2': 0, 'V_misses_Q2': 0, 'F_L_when_V_meets': {}, 'F_L_when_V_misses': {},
          'max_B_ab': 0, 'examples_V_meets_FL>1': []}
    for _ in range(trials):
        st['trials'] += 1
        S = rng.randint(4, Bx + 1)
        seeds = set()
        for _ in range(rng.randint(2, 3)):
            a = rng.randint(1, S - 2)
            b = rng.randint(1, S - 1 - a)
            seeds.add((a, b, S - a - b))  # antichain on a+b+c=S
        for _ in range(rng.randint(1, 2)):
            seeds.add((rng.randint(1, Bx - 1), rng.randint(1, Bx - 1), 0))
        Q, ok = closure_box(seeds, Bx + 2, max_pts=400)
        if not ok or max(max(p) for p in Q) >= Bx + 2:
            continue
        Ql = sorted(Q)
        if check_T_finite(Ql):
            continue
        st['finite_exact_SUB1'] += 1
        Q2 = [(p[0], p[1]) for p in Ql if p[2] == 0 and p[0] > 0 and p[1] > 0]
        Q3 = [p for p in Ql if min(p) > 0]
        if not Q2 or not Q3 or Pplus(Q2):
            continue
        st['with_Q2_and_Q3_noPplus'] += 1
        H2, H3, H30 = lattice_data(Q2, Q3)
        if positive_level(H3):
            st['Q3_on_positive_level'] += 1
        else:
            st['Q3_NOT_on_positive_level'] += 1
        FL = F_L_finite(set(Q2), H30)
        key = 'inf' if FL is None else FL
        st['max_B_ab'] = max(st['max_B_ab'], max(p[0] + p[1] for p in Q3))
        if V_meets_Q2(Q2, Q3, H3):
            st['V_meets_Q2'] += 1
            d = st['F_L_when_V_meets']
            d[key] = d.get(key, 0) + 1
            if FL != 1 and len(st['examples_V_meets_FL>1']) < 3:
                st['examples_V_meets_FL>1'].append((tuple(Q2), tuple(Q3), key))
        else:
            st['V_misses_Q2'] += 1
            d = st['F_L_when_V_misses']
            d[key] = d.get(key, 0) + 1
    return st


# ---------------------------------------------------------------------------
# S6: seeds of the shape forced by case (ii): x, x+d1, x+d2, x+d1+d2
# ---------------------------------------------------------------------------
def S6(rng, trials, Bx):
    """d_i = omega_i - y_i with y_1, y_2 disjoint unmarked ab-blocks of W (|y_i| > |omega_i|)
    and omega_i short and containing c.  Closure in a box; classify the outcome."""
    st = {'trials': 0, 'too_big_or_boundary': 0, 'P+': 0, 'finite_exact_SUB1_noP+': 0,
          'finite_F_L': {}, 'finite_max_mu_over_Bab': 0.0, 'finite_examples_FL>1': []}
    for _ in range(trials):
        st['trials'] += 1
        xa, xb = rng.randint(3, Bx - 2), rng.randint(3, Bx - 2)
        # disjoint blocks, marks outside: y1 + y2 <= x - (1,1)
        y1a = rng.randint(0, xa - 1); y2a = rng.randint(0, xa - 1 - y1a)
        y1b = rng.randint(0, xb - 1); y2b = rng.randint(0, xb - 1 - y1b)
        y1, y2 = (y1a, y1b), (y2a, y2b)
        if y1a + y1b < 2 or y2a + y2b < 2:
            continue
        om = []
        for y in (y1, y2):
            L = rng.randint(1, max(1, y[0] + y[1] - 1))
            oc = rng.randint(1, L)
            oa = rng.randint(0, L - oc)
            om.append((oa, L - oc - oa, oc))
        d1 = (om[0][0] - y1[0], om[0][1] - y1[1], om[0][2])
        d2 = (om[1][0] - y2[0], om[1][1] - y2[1], om[1][2])
        x = (xa, xb, 0)
        seeds = {x, vadd(x, d1), vadd(x, d2), vadd(vadd(x, d1), d2)}
        if any(min(p[:2]) < 1 for p in seeds):
            continue
        Q, ok = closure_box(seeds, Bx, max_pts=500)
        Q2 = [(p[0], p[1]) for p in Q if p[2] == 0 and min(p[:2]) > 0]
        if Pplus(Q2):
            st['P+'] += 1
            continue
        if not ok or max(max(p) for p in Q) >= Bx:
            st['too_big_or_boundary'] += 1
            continue
        Ql = sorted(Q)
        if check_T_finite(Ql):
            st['too_big_or_boundary'] += 1
            continue
        st['finite_exact_SUB1_noP+'] += 1
        Q3 = [p for p in Ql if min(p) > 0]
        H2, H3, H30 = lattice_data(Q2, Q3)
        FL = F_L_finite(set(Q2), H30)
        key = 'inf' if FL is None else FL
        st['finite_F_L'][key] = st['finite_F_L'].get(key, 0) + 1
        mu = min(a + b for a, b in Q2)
        Bab = max(p[0] + p[1] for p in Q3)
        st['finite_max_mu_over_Bab'] = max(st['finite_max_mu_over_Bab'], round(mu / Bab, 3))
        if FL != 1 and len(st['finite_examples_FL>1']) < 4:
            st['finite_examples_FL>1'].append((tuple(sorted(Q2)), tuple(Q3), key))
    return st


# ---------------------------------------------------------------------------
# S7: finite Q_3 alone, then every single point x of V cap Pi_2 that is
#     compatible as Q_2 = {x}: the value of F_L  (Conjecture 7.3: F_L <= 2)
# ---------------------------------------------------------------------------
def S7(rng, trials, Bx):
    st = {'finite_closed_Q3': 0, 'with_H30_nonzero': 0, 'F_L_hist(single-point Q2 on V)': {},
          'examples_F_L>=3_or_inf': []}
    for _ in range(trials):
        K = rng.randint(1, 4)
        S = rng.randint(K + 3, Bx + 2 * K)
        seeds = set()
        for _ in range(rng.randint(2, 4)):
            c = rng.randint(1, max(1, (S - 2) // K))
            r = S - K * c
            if r < 2:
                continue
            a = rng.randint(1, r - 1)
            seeds.add((a, r - a, c))  # antichain on a+b+Kc=S
        if len(seeds) < 2:
            continue
        Q, ok = closure_box(seeds, Bx, max_pts=300)
        if not ok or max(max(p) for p in Q) >= Bx:
            continue
        Q3 = sorted(Q)
        if check_T_finite(Q3):
            continue
        st['finite_closed_Q3'] += 1
        H3 = echelon([vsub(p, Q3[0]) for p in Q3], 3)
        H30 = plane_part(H3)
        if not H30:
            continue
        st['with_H30_nonzero'] += 1
        D30 = {vsub(q, p) for p in Q3 for q in Q3 if p != q and p[2] == q[2]}
        for x in range(1, 3 * Bx):
            for y in range(1, 3 * Bx):
                X = (x, y, 0)
                if not in_lattice(vsub(X, Q3[0]), H3):
                    continue
                # Q = {X} + Q3 satisfies (T) iff no realized same-height move is valid at X
                if any(valid(X, h) for h in D30):
                    continue
                FL = F_L_finite({(x, y)}, H30)
                key = 'inf' if FL is None else FL
                d = st['F_L_hist(single-point Q2 on V)']
                d[key] = d.get(key, 0) + 1
                if (FL is None or FL >= 3) and len(st['examples_F_L>=3_or_inf']) < 3:
                    st['examples_F_L>=3_or_inf'].append(((x, y), tuple(Q3), key))
    st['F_L_hist(single-point Q2 on V)'] = dict(sorted(st['F_L_hist(single-point Q2 on V)'].items(), key=str))
    return st


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--quick', action='store_true')
    args = ap.parse_args()
    rng = random.Random(args.seed)
    q = args.quick

    t0 = time.time()
    for name, rows in S1(q):
        print('S1', name, ':', rows)
    print('   [%.1fs]' % (time.time() - t0)); sys.stdout.flush()

    t0 = time.time()
    print('S2 random closures (box 7):', S2(rng, 60 if q else 250, 7))
    print('   [%.1fs]' % (time.time() - t0)); sys.stdout.flush()

    t0 = time.time()
    print('S3 (beta-III) families:', S3(q))
    print('   [%.1fs]' % (time.time() - t0)); sys.stdout.flush()

    t0 = time.time()
    print('S4 Lemma W random grammars:', S4(rng, 300 if q else 2000))
    print('S4 Lemma W family X->b^t|ac (t, v, theta, mu_ab):', lemmaW_family(8))
    print('   [%.1fs]' % (time.time() - t0)); sys.stdout.flush()

    t0 = time.time()
    print('S5 finite Q3:', S5(rng, 150 if q else 600, 6))
    print('   [%.1fs]' % (time.time() - t0)); sys.stdout.flush()

    t0 = time.time()
    print('S6 case-(ii) seeds (box 11):', S6(rng, 150 if q else 600, 11))
    print('   [%.1fs]' % (time.time() - t0)); sys.stdout.flush()

    t0 = time.time()
    print('S7 finite Q3, single-point Q2 on V (box 13):', S7(rng, 300 if q else 3000, 13))
    print('   [%.1fs]' % (time.time() - t0))


if __name__ == '__main__':
    main()
