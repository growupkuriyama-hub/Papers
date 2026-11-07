#!/usr/bin/env python3
"""check_claude_verify_prop73_2026-11-07.py  (standard library only)

Independent check (verifier side) of reviews/claude_prop73_2026-11-07.md.
No code of check_claude_prop73_2026-11-07.py is used; every routine is rewritten.

  python3 -u check_claude_verify_prop73_2026-11-07.py --seed 7   (defaults: --grammars 300 --lmax 14; about 4 minutes)

V1  closedness (p+q-r rule, brute force), rank / determinant, condition (T) written
    directly from Theorem 2.1 of the closure report:
        for q,q' in Q with supp q = supp q', h = q'-q != 0, S = supp h, gamma >= 0:
        h^- + 1_S + gamma in Q  <=>  h^+ + 1_S + gamma in Q
    (exact for finite Q: only gammas making one side a point of Q matter);
    explicit V-memberships quoted in the report; apex sets A(Q) (Lemma 8);
    necessary conditions (N1)-(N5') (Conj. 7.5) by own search; for
    F4, F_{X,Y} (4<=X,Y<=15), S_n (3<=n<=20), Example 4, Y23, X, 5-point example.
V2  Theorem 4: closures of random seeds biased to produce rank 3; whenever the
    closure is finite and of rank <= 2, a strictly positive integer lambda constant on
    it is searched for directly (lambda in [1,K]^3, no normal-vector shortcut).
V3  grammars (with cycles allowed): Parikh vectors enumerated up to a length bound,
    mu_ab, K_c (only when all abc words are known, i.e. the abc part is length-bounded
    below the bound -- otherwise skipped), Lemma 5 (shortest abc <= 5 v theta),
    Lemma 7, Theorem 6 when its hypothesis holds (short abc words on a positive level,
    found by direct search for lambda); weight-homogeneous grammars for Theorem 6.
find_level: search lambda in [1,K]^3; if none, a cross-product candidate is tried and
accepted only after checking lambda >= 1 and lambda . d = 0 for every difference d
(rank-1 sets with a level always have one in the search range here, see output).
A closure touching the box is discarded, never used as evidence.
"""
import argparse
import itertools
import random
from fractions import Fraction


def vadd(p, q): return tuple(a + b for a, b in zip(p, q))
def vsub(p, q): return tuple(a - b for a, b in zip(p, q))
def norm(p): return sum(p)


def det(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def rank(F):
    """rank of the lattice of differences, by Gaussian elimination over Q."""
    F = list(F)
    rows = [[Fraction(x) for x in vsub(q, F[0])] for q in F[1:]]
    r = 0
    for col in range(3):
        piv = next((i for i in range(r, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][col] != 0:
                f = rows[i][col] / rows[r][col]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[r])]
        r += 1
    return r


def closed(F):
    S = set(F)
    for p in F:
        for q in F:
            for r in F:
                x = vsub(vadd(p, q), r)
                if min(x) >= 1 and x not in S:
                    return False
    return True


def supp(v): return frozenset(i for i in range(3) if v[i] != 0)


def cond_T(Q):
    """number of violations of (T), exact for finite Q."""
    Qs = set(Q)
    bad = 0
    for q in Q:
        for q2 in Q:
            if q == q2 or supp(q) != supp(q2):
                continue
            h = vsub(q2, q)
            S = supp(h)
            hp = tuple(max(x, 0) for x in h)
            hm = tuple(max(-x, 0) for x in h)
            one = tuple(1 if i in S else 0 for i in range(3))
            L0, R0 = vadd(hm, one), vadd(hp, one)
            gammas = set()
            for x in Q:
                for base in (L0, R0):
                    g = vsub(x, base)
                    if min(g) >= 0:
                        gammas.add(g)
            for g in gammas:
                if (vadd(L0, g) in Qs) != (vadd(R0, g) in Qs):
                    bad += 1
    return bad


def apexes(Q3, mu):
    sh = [p for p in Q3 if norm(p) < mu]
    out = set()
    for p1 in sh:
        for p2 in sh:
            for p12 in sh:
                x = vsub(vadd(p1, p2), p12)
                if x[2] == 0 and x[0] >= 1 and x[1] >= 1:
                    out.add(x[:2])
    return out


def N_conditions(Q3, P, thmax):
    """least theta <= thmax with (N1)-(N5') of Conj. 7.5, or None.  Own enumeration."""
    P3 = (P[0], P[1], 0)
    mu = P[0] + P[1]
    sh = [p for p in Q3 if norm(p) < mu]
    trip = [(p1, p2) for p1 in sh for p2 in sh
            if vsub(vadd(p1, p2), P3) in set(sh)]                    # (N1),(N2)
    for th in range(1, thmax + 1):
        for p1, p2 in trip:
            Ys = []
            for p in (p1, p2):
                cand = set()
                rc = p[2]
                for ra in range(0, th - rc + 1):
                    for rb in range(0, th - rc - ra + 1):
                        Y = (P[0] - p[0] + ra, P[1] - p[1] + rb)
                        if min(Y) < 0 or Y[0] + Y[1] <= th:             # (N3)
                            continue
                        ok5 = False                                       # (N5')
                        for q in Q3:
                            e = (max(P[0] - q[0], 0), max(P[1] - q[1], 0))
                            if e[0] <= Y[0] and e[1] <= Y[1] and e[0] + e[1] <= th:
                                ok5 = True
                                break
                        if ok5:
                            cand.add(Y)
                Ys.append(cand)
            for Y1 in Ys[0]:
                for Y2 in Ys[1]:
                    if Y1[0] + Y2[0] <= P[0] - 1 and Y1[1] + Y2[1] <= P[1] - 1:   # (N4)
                        return th
    return None


def find_level(F, K=80):
    """strictly positive integer lambda in [1,K]^3 constant on F, or None."""
    F = list(F)
    if len(F) <= 1:
        return (1, 1, 1)
    D = [vsub(q, F[0]) for q in F[1:]]
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            # solve for c from the first difference with nonzero c-entry
            dc = next((d for d in D if d[2] != 0), None)
            if dc is None:
                if all(a * d[0] + b * d[1] == 0 for d in D):
                    return (a, b, 1)
                continue
            num = -(a * dc[0] + b * dc[1])
            if num % dc[2] or num // dc[2] < 1:
                continue
            c = num // dc[2]
            if all(a * d[0] + b * d[1] + c * d[2] == 0 for d in D):
                return (a, b, c)
    # fallback (levels with entries > K): candidate from two differences, verified directly
    for d1, d2 in itertools.combinations(D, 2):
        n = (d1[1] * d2[2] - d1[2] * d2[1], d1[2] * d2[0] - d1[0] * d2[2], d1[0] * d2[1] - d1[1] * d2[0])
        if any(n):
            for lam in (n, tuple(-x for x in n)):
                if min(lam) >= 1 and all(sum(x * y for x, y in zip(lam, d)) == 0 for d in D):
                    return lam
            return None
    return None


def report(name, Q3, P, out, thmax=None):
    Q = [(P[0], P[1], 0)] + list(Q3)
    mu = P[0] + P[1]
    sh = [p for p in Q3 if norm(p) < mu]
    row = dict(closed=closed(list(Q3)), rank=rank(Q3), T_viol=cond_T(Q),
               mu=mu, B_ab=max(p[0] + p[1] for p in Q3), K_c=len({p[2] for p in Q3}),
               P_in_A=tuple(P) in apexes(Q3, mu),
               short_level=find_level(sh) is not None if sh else True)
    if thmax:
        row['N_theta'] = N_conditions(Q3, P, thmax)
    out.append((name, row))
    return row


def V1(out):
    bad = []
    F4 = [(1, 3, 12), (4, 8, 1), (6, 4, 4), (12, 1, 3)]
    out.append(('F4 det', det(vsub(F4[0], F4[1]), vsub(F4[2], F4[1]), vsub(F4[3], F4[1]))))
    out.append(('F4: (4,8,1)+(12,1,3)-(6,4,4)', vsub(vadd(F4[1], F4[3]), F4[2])))
    r = report('F4 + (10,5)', F4, (10, 5), out, thmax=15)
    if not (r['closed'] and r['rank'] == 3 and r['T_viol'] == 0):
        bad.append('F4')
    report('F4 + (14,26)', F4, (14, 26), out, thmax=12)
    nb = 0
    for X in range(4, 16):
        for Y in range(4, 16):
            A, B, M, Z = (1, Y + 1, 1), (X + 1, 1, 1), (2, 2, 2), (1, 1, 4)
            F = [A, B, M, Z]
            tmp = []
            r = report('F', F, (X, Y), tmp, thmax=X + Y)
            d = det(vsub(A, M), vsub(B, M), vsub(Z, M))
            ok = (r['closed'] and r['rank'] == 3 and r['T_viol'] == 0 and r['P_in_A']
                  and not r['short_level'] and r['N_theta'] is None
                  and d == 3 * X + 3 * Y - 2 * X * Y
                  and vsub(vadd(A, B), M) == (X, Y, 0))
            nb += not ok
    out.append(('F_{X,Y} 4<=X,Y<=15: #pairs, #not as claimed', (144, nb)))
    nb = 0
    for n in range(3, 21):
        s = [(2 * k, 2 * (n + 1 - k), k) for k in range(1, n + 1)]
        Z, A = (1, 1, 2 * n), (4 * n, 1, 1)
        F = s + [Z, A]
        P = (4 * n - 3, 3)
        tmp = []
        r = report('S', F, P, tmp)
        comb = tuple(-2 * n * x + y + 2 * z for x, y, z in
                     zip(vsub(s[1], s[0]), vsub(Z, s[0]), vsub(A, s[0])))
        ok = (r['closed'] and r['rank'] == 3 and r['T_viol'] == 0 and not r['P_in_A']
              and r['short_level'] and r['mu'] == 4 * n and r['B_ab'] == 4 * n + 1
              and r['K_c'] == n + 1 and comb == vsub((P[0], P[1], 0), s[0])
              and det(vsub(s[1], s[0]), vsub(Z, s[0]), vsub(A, s[0])) in (2 * n - 1, 1 - 2 * n))
        nb += not ok
    out.append(('S_n 3<=n<=20: #not as claimed', nb))
    report('Example 4', [(1, 4, 6), (3, 9, 3), (9, 3, 1), (1, 27, 1)], (5, 14), out, thmax=19)
    report('Y23', [(1, 2, 5), (1, 26, 1), (11, 10, 2), (24, 3, 1)], (10, 23), out, thmax=33)
    report('X', [(3, 2, 1), (1, 3, 2), (2, 1, 3)], (5, 1), out, thmax=6)
    F5 = [(1, 1, 10), (2, 6, 1), (4, 4, 2), (6, 2, 3), (12, 1, 1)]
    out.append(('5-point example closed, rank', (closed(F5), rank(F5))))
    return bad


def closure(seed, B, cap=120):
    F = set(seed)
    while True:
        L = list(F)
        new = set()
        for p in L:
            for q in L:
                for r in L:
                    x = vsub(vadd(p, q), r)
                    if min(x) >= 1 and x not in F:
                        if max(x) > B:
                            return None
                        new.add(x)
        if not new:
            return F
        F |= new
        if len(F) > cap:
            return None


def V2(rng, trials):
    st = dict(finite=0, rank3=0, rank_le2=0, VIOL_no_level=0)
    for _ in range(trials):
        k = rng.choice([3, 4, 4, 5])
        seed = set()
        while len(seed) < k:
            p = [rng.randint(1, 14) for _ in range(3)]
            p[rng.randrange(3)] = rng.randint(1, 2)
            seed.add(tuple(p))
        F = closure(seed, 40)
        if F is None:
            continue
        st['finite'] += 1
        if rank(F) == 3:
            st['rank3'] += 1
            continue
        st['rank_le2'] += 1
        if find_level(F) is None:
            st['VIOL_no_level'] += 1
    return st


# ---------------------------- grammars ----------------------------------------
E = {'a': (1, 0, 0), 'b': (0, 1, 0), 'c': (0, 0, 1)}


def parikh_upto(G, Lmax):
    """sets of Parikh vectors of length <= Lmax for each nonterminal (fixpoint)."""
    S = {X: set() for X in G}
    ch = True
    while ch:
        ch = False
        for X, rules in G.items():
            for rhs in rules:
                cur = {(0, 0, 0)}
                for s in rhs:
                    if s in E:
                        cur = {vadd(x, E[s]) for x in cur if norm(x) < Lmax}
                    else:
                        cur = {vadd(x, y) for x in cur for y in S[s] if norm(x) + norm(y) <= Lmax}
                    if not cur:
                        break
                for x in cur:
                    if x not in S[X]:
                        S[X].add(x)
                        ch = True
    return S


def reduce(G, start):
    prod, ch = set(), True
    while ch:
        ch = False
        for X, rs in G.items():
            if X not in prod and any(all(s in E or s in prod for s in r) for r in rs):
                prod.add(X); ch = True
    if start not in prod:
        return None
    G = {X: [r for r in rs if all(s in E or s in prod for s in r)] for X, rs in G.items() if X in prod}
    reach, st = {start}, [start]
    while st:
        X = st.pop()
        for r in G[X]:
            for s in r:
                if s not in E and s not in reach:
                    reach.add(s); st.append(s)
    return {X: G[X] for X in reach}


def params(G):
    INF = 10 ** 9
    tau = {X: INF for X in G}
    ch = True
    while ch:
        ch = False
        for X, rs in G.items():
            for r in rs:
                l = sum(1 if s in E else tau[s] for s in r)
                if l < tau[X]:
                    tau[X] = l; ch = True
    theta = max(sum(1 if s in E else tau[s] for s in r) for rs in G.values() for r in rs)
    rr = max(1, max(sum(1 for s in r if s not in E) for rs in G.values() for r in rs))
    return len(G), rr, theta


def rand_grammar(rng, v):
    G = {}
    for X in range(v):
        rules = []
        for _ in range(rng.randint(1, 3)):
            rhs = []
            for _ in range(rng.randint(1, 3)):
                if rng.random() < 0.5:
                    rhs.append(rng.randrange(v))       # cycles allowed
                else:
                    rhs.append(rng.choice('aabbc'))
            if rhs == [X]:
                rhs.append('a')
            rules.append(tuple(rhs))
        G[X] = rules
    return G


def rand_homog(rng, v, lam):
    w = {X: rng.randint(2, 18) for X in range(v)}
    wt = lambda s: lam['abc'.index(s)] if s in E else w[s]
    G = {}
    for X in range(v):
        rules, tries = [], 0
        while len(rules) < 3 and tries < 800:
            tries += 1
            rhs = tuple(rng.choice(list('abc') + list(range(X + 1, v))) for _ in range(rng.randint(1, 4)))
            if sum(wt(s) for s in rhs) == w[X]:
                rules.append(rhs)
        G[X] = rules
    return G


def V3(rng, trials, Lmax):
    st = dict(grammars_with_ab=0, abc_fully_known=0, VIOL_L5=0, VIOL_L7=0,
              T6_hyp_nonvacuous=0, VIOL_T6=0, max_mu_over_vth=0.0,
              homog_with_ab=0, VIOL_T6_homog=0)
    for _ in range(trials):
        G = reduce(rand_grammar(rng, rng.randint(2, 6)), 0)
        if G is None:
            continue
        S = parikh_upto(G, Lmax)[0]
        ab = [p for p in S if p[0] and p[1] and not p[2]]
        if not ab:
            continue
        mu = min(map(norm, ab))
        if mu > Lmax // 2:
            continue
        st['grammars_with_ab'] += 1
        v, r, th = params(G)
        st['max_mu_over_vth'] = max(st['max_mu_over_vth'], round(mu / (v * th), 3))
        abc = [p for p in S if all(p)]
        if abc and min(map(norm, abc)) > 5 * v * th:
            st['VIOL_L5'] += 1
        short = [p for p in abc if norm(p) < mu]
        if short and find_level(short, K=30) is not None:
            st['T6_hyp_nonvacuous'] += 1
            if mu > max(9 * (r + 1) * v * th, 11 * (r + 1) * v * v * th ** 4):
                st['VIOL_T6'] += 1
        # K_c only when the abc part is known exactly: no abc word of length in
        # (Lmax/2, Lmax] (pumping would produce one if the abc part were unbounded)
        if not any(norm(p) > Lmax // 2 for p in abc):
            st['abc_fully_known'] += 1
            Kc = len({p[2] for p in abc})
            if mu > (Kc + 3) * v * th:
                st['VIOL_L7'] += 1
    for _ in range(trials // 3):
        lam = tuple(rng.randint(1, 5) for _ in range(3))
        G = reduce(rand_homog(rng, rng.randint(2, 6), lam), 0)
        if G is None:
            continue
        S = parikh_upto(G, Lmax)[0]
        ab = [p for p in S if p[0] and p[1] and not p[2]]
        if not ab:
            continue
        st['homog_with_ab'] += 1
        mu = min(map(norm, ab))
        v, r, th = params(G)
        if mu > max(9 * (r + 1) * v * th, 11 * (r + 1) * v * v * th ** 4):
            st['VIOL_T6_homog'] += 1
    return st


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--grammars', type=int, default=300)
    ap.add_argument('--lmax', type=int, default=14)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    out = []
    bad = V1(out)
    print('V1 examples')
    for k, v in out:
        print('   ', k, ':', v)
    print('    hard failures:', bad)
    print('V2 Theorem 4 :', V2(rng, 20000))
    print('V3 grammars  :', V3(rng, a.grammars, a.lmax))


if __name__ == '__main__':
    main()
