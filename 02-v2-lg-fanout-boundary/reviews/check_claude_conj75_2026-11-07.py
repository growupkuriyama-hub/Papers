#!/usr/bin/env python3
"""check_claude_conj75_2026-11-07.py  (Claude, 2026-11-07; standard library only)

Computations for the report claude_conj75_2026-11-07.md (Conjecture 7.5 / Proposition 7.4).

  python3 check_claude_conj75_2026-11-07.py --seed 1            # full  (box 10, about 6-8 min)
  python3 check_claude_conj75_2026-11-07.py --seed 1 --quick    # quick (box 8,  about 1-2 min)
  options: --box N  --search-secs S  --only-search (C6 only)

Sections
  C1  enumerator of closed sets validated against brute force (box 3 / 4)
  C2  exhaustive enumeration of all closed F in [1,N]^3 with |F| <= 5 (closedness = all p+q-r);
      rank-3 sets up to coordinate permutation; apexes; exact least theta of (N1),(N3),(N4),(N5');
      exact strict-positive-level test of Q3^{<|P|}; exact (T) for {P} u F;
      structure: largest positive-level subset; satellite length vs |P|
  C3  the 4-point counterexample E* to Conjecture 7.5
  C4  the family F_n (line + two satellites): theta = 7 fixed, mu = 10n+1
  C5  Lemma C on random acyclic CFGs (mu <= 3v theta + 3rv(theta + Delta(theta)))
  C6  structured random search (seeded): (N)-configurations with small theta, finite closures,
      all one/two-satellite extensions; ratio mu/theta, one-satellite structure, deficit Delta
All tests on finite sets are exact.  Closures computed in a box are discarded when they touch the box.
"""
import sys, time, random, itertools
from collections import Counter

# ----------------------------------------------------------------------------- vectors

def sub(p, q): return tuple(a - b for a, b in zip(p, q))
def add(p, q): return tuple(a + b for a, b in zip(p, q))
def cross(u, v): return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
def det3(a, b, c): return sum(x*y for x, y in zip(a, cross(b, c)))

def rank_aff(F):
    F = list(F)
    if len(F) <= 1: return 0
    D = [sub(q, F[0]) for q in F[1:]]
    for a, b, c in itertools.combinations(D, 3):
        if det3(a, b, c): return 3
    for a, b in itertools.combinations(D, 2):
        if any(cross(a, b)): return 2
    return 1 if any(any(d) for d in D) else 0

def positive_level(F):
    """exact: is there lambda in R^3 with all three coordinates > 0, constant on F ?"""
    F = list(F)
    r = rank_aff(F)
    if r == 0: return True
    if r == 3: return False
    D = [sub(q, F[0]) for q in F[1:]]
    if r == 1:
        d = next(d for d in D if any(d))
        return any(x > 0 for x in d) and any(x < 0 for x in d)
    for a, b in itertools.combinations(D, 2):
        n = cross(a, b)
        if any(n):
            return all(x > 0 for x in n) or all(x < 0 for x in n)

def closed3(F):
    S = set(F)
    for p in F:
        for q in F:
            for r in F:
                if q == r or p == r: continue
                x = (p[0]+q[0]-r[0], p[1]+q[1]-r[1], p[2]+q[2]-r[2])
                if min(x) >= 1 and x not in S: return False
    return True

def supp(v): return frozenset(i for i, x in enumerate(v) if x)

def T_holds(Q):
    """(T) of the closure report, Thm 2.1, for a finite Q: for same-support q,q' in Q, h = q'-q,
    S = supp h, every alpha with alpha_s >= 1, alpha_s + h_s >= 1 (s in S): alpha in Q <=> alpha+h in Q.
    For finite Q it suffices to start the move from points of Q (both signs of h are in D)."""
    Qs = set(Q); groups = {}
    for q in Q: groups.setdefault(supp(q), []).append(q)
    D = {sub(b, a) for g in groups.values() for a in g for b in g if a != b}
    for h in D:
        S = supp(h)
        for al in Q:
            be = add(al, h)
            if min(be) < 0: continue
            if all(al[i] >= 1 and be[i] >= 1 for i in S) and be not in Qs:
                return False
    return True

# ----------------------------------------------------------------------------- (N1)-(N5')

def apexes(F):
    out = []
    for p1, p2 in itertools.combinations_with_replacement(sorted(F), 2):
        for p12 in F:
            P = sub(add(p1, p2), p12)
            if P[2] == 0 and P[0] >= 1 and P[1] >= 1:
                out.append((P, p1, p2, p12))
    return out

def N_thetas(F, P, p1, p2, first_only=False, cap=None):
    """all theta with (N1),(N3),(N4),(N5') (p12 = p1+p2-P).  (N2) and |p12| < |P| follow from (N1),(N3).
    r_i = (e_a, e_b, (p_i)_c), Y_i = (P - p_i)_{ab} + e >= 0, |r_i| <= theta < |Y_i|,
    Y_1 + Y_2 <= P - (1,1), and some q in F with (P - q)^+_{ab} <= Y_i and |(P - q)^+_{ab}| <= theta."""
    nP = P[0] + P[1]
    defs = [(max(0, P[0]-q[0]), max(0, P[1]-q[1])) for q in F]
    lo = max(p[2] + max(0, p[0]-P[0]) + max(0, p[1]-P[1]) for p in (p1, p2))
    lo = max(lo, min(e[0] + e[1] for e in defs), 1)
    hi = nP if cap is None else min(nP, cap)
    res = []
    for th in range(lo, hi + 1):
        Ysets = []
        for p in (p1, p2):
            la, lb = max(0, p[0]-P[0]), max(0, p[1]-P[1])
            ys = []
            for ea in range(la, th + 1):
                for eb in range(lb, th + 1 - ea):
                    if ea + eb + p[2] > th: break
                    Y = (P[0]-p[0]+ea, P[1]-p[1]+eb)
                    if Y[0] < 0 or Y[1] < 0 or Y[0] + Y[1] <= th: continue
                    if any(e[0]+e[1] <= th and e[0] <= Y[0] and e[1] <= Y[1] for e in defs):
                        ys.append(Y)
            if not ys: break
            Ysets.append(ys)
        if len(Ysets) < 2: continue
        if any(Y1[0]+Y2[0] <= P[0]-1 and Y1[1]+Y2[1] <= P[1]-1 for Y1 in Ysets[0] for Y2 in Ysets[1]):
            res.append(th)
            if first_only: break
    return res

def analyse(F, first_only=False, cap=None):
    out = []
    for P, p1, p2, p12 in apexes(F):
        nP = P[0] + P[1]
        if max(sum(p1), sum(p2), sum(p12)) >= nP: continue
        ths = N_thetas(F, P[:2], p1, p2, first_only, cap)
        if not ths: continue
        short = [p for p in F if sum(p) < nP]
        out.append(dict(P=P[:2], p1=p1, p2=p2, p12=p12, thetas=ths, short=short,
                        short_pos=positive_level(short), T=T_holds([P] + list(F))))
    return out

def Delta(F, P, th):
    """Delta_Q(theta) = max(0, max{|P| - |f|_ab : f in Q3, f_c <= theta})  (Lemma C)."""
    return max([0] + [P[0]+P[1]-f[0]-f[1] for f in F if f[2] <= th])

def nsat(F):
    """least number of points to delete so that the rest lies on a strictly positive level (<= 3 tested)."""
    F = list(F)
    for k in range(0, 3):
        for X in itertools.combinations(F, k):
            if positive_level([p for p in F if p not in X]): return k
    return 3

PERMS = list(itertools.permutations(range(3)))
def canon(F): return min(tuple(sorted(tuple(p[i] for i in pi) for p in F)) for pi in PERMS)
def c_variants(F):
    """the three choices of the c-coordinate (a <-> b is a symmetry of all conditions)."""
    return [tuple(sorted(tuple(p[i] for i in [j for j in range(3) if j != ci] + [ci]) for p in F))
            for ci in range(3)]

# ----------------------------------------------------------------------------- exhaustive enumerator

def enum_closed(N, nmax):
    """all closed F subset [1,N]^3 with 2 <= |F| <= nmax.  Points are added in lexicographic order;
    a point p+q-r in Pi_3 forced by the current set must be in the set or be added later (so it must be
    in the box and later in the order); bitset filters prune candidates, exceptions re-admit candidates
    whose forced point already lies in the set."""
    pts = [(a, b, c) for a in range(1, N+1) for b in range(1, N+1) for c in range(1, N+1)]
    idx = {p: i for i, p in enumerate(pts)}; n = len(pts)
    def kind(y):
        if y[0] < 1 or y[1] < 1 or y[2] < 1: return 0
        if y[0] > N or y[1] > N or y[2] > N: return 2
        return 1
    def okx(y, j):
        k = kind(y)
        return k == 0 or (k == 1 and idx[y] > j)
    C = []
    for p in pts:
        bits = 0
        for j, x in enumerate(pts):
            if x != p and okx((2*p[0]-x[0], 2*p[1]-x[1], 2*p[2]-x[2]), j) \
                    and okx((2*x[0]-p[0], 2*x[1]-p[1], 2*x[2]-p[2]), j):
                bits |= 1 << j
        C.append(bits)
    mG, mK = {}, {}
    def Gd(d):
        if d not in mG:
            bits = 0
            for j, x in enumerate(pts):
                if okx((x[0]-d[0], x[1]-d[1], x[2]-d[2]), j) and okx((x[0]+d[0], x[1]+d[1], x[2]+d[2]), j):
                    bits |= 1 << j
            mG[d] = bits
        return mG[d]
    def Ks(s):
        if s not in mK:
            bits = 0
            for j, x in enumerate(pts):
                if okx((s[0]-x[0], s[1]-x[1], s[2]-x[2]), j): bits |= 1 << j
            mK[s] = bits
        return mK[s]
    out = []
    def required(S, x):
        T = S + [x]; Ts = set(T); req = set()
        for p in T:
            for q in T:
                for r in T:
                    if q == r or p == r or x not in (p, q, r): continue
                    y = (p[0]+q[0]-r[0], p[1]+q[1]-r[1], p[2]+q[2]-r[2])
                    k = kind(y)
                    if k == 2: return None
                    if k == 1 and y not in Ts: req.add(y)
        return req
    def rec(S, last, R, cand):
        if not R and len(S) >= 2: out.append(tuple(S))
        if len(S) >= nmax or len(S) + len(R) > nmax: return
        hi = min(idx[y] for y in R) if R else n - 1
        ex = 0
        for p in S:
            for q in S:
                for r in S:
                    y = (p[0]+q[0]-r[0], p[1]+q[1]-r[1], p[2]+q[2]-r[2])
                    if y in idx: ex |= 1 << idx[y]
                y = (2*p[0]-q[0], 2*p[1]-q[1], 2*p[2]-q[2])
                if y in idx: ex |= 1 << idx[y]
                if all((p[i]+q[i]) % 2 == 0 for i in range(3)):
                    y = tuple((p[i]+q[i])//2 for i in range(3))
                    if y in idx: ex |= 1 << idx[y]
        m = (cand | ex) & ~((1 << (last + 1)) - 1) & ((1 << (hi + 1)) - 1)
        while m:
            low = m & -m; j = low.bit_length() - 1; m ^= low
            x = pts[j]
            req = required(S, x)
            if req is None: continue
            newR = (R - {x}) | req
            if all(idx[y] > j for y in newR) and len(S) + 1 + len(newR) <= nmax:
                nc = cand & C[j]
                for p in S:
                    nc &= Gd((x[0]-p[0], x[1]-p[1], x[2]-p[2])) & Ks((x[0]+p[0], x[1]+p[1], x[2]+p[2]))
                rec(S + [x], j, newR, nc)
    for i in range(n):
        rec([pts[i]], i, set(), C[i])
    return out

# ----------------------------------------------------------------------------- C1

def C1(quick):
    res = {}
    for N, k in ((3, 5), (4, 4)) if not quick else ((3, 5), (4, 3)):
        pts = [(a, b, c) for a in range(1, N+1) for b in range(1, N+1) for c in range(1, N+1)]
        bf = {frozenset(F) for m in range(2, k+1) for F in itertools.combinations(pts, m) if closed3(F)}
        en = {frozenset(F) for F in enum_closed(N, k)}
        res[(N, k)] = (len(bf), len(en), bf == en)
    return res

# ----------------------------------------------------------------------------- C2

def C2(N):
    t = time.time()
    allF = enum_closed(N, 5)
    te = time.time() - t
    r3 = {}
    for F in allF:
        if len(F) >= 4 and rank_aff(F) == 3: r3.setdefault(canon(F), None)
    st = Counter(); best_ratio = (0,); best_metric = (0,); smallest = None
    sat_short = Counter(); structure = Counter()
    for F in r3:
        structure[(len(F), nsat(F))] += 1
        for G in c_variants(F):
            for rr in analyse(G):
                st['admissible_apexes'] += 1
                if rr['short_pos']: continue
                st['COUNTEREX_closed_only'] += 1
                if not rr['T']: continue
                st['COUNTEREX_with_T'] += 1
                mu = sum(rr['P']); th = rr['thetas'][0]
                Kc = len({f[2] for f in G})
                if mu / th > best_ratio[0]: best_ratio = (round(mu/th, 3), mu, th, rr['P'], G)
                for th2 in rr['thetas']:
                    m = min(Kc, Delta(G, rr['P'], th2) / th2, mu / th2)
                    if m > best_metric[0]: best_metric = (round(m, 3), th2, Kc, mu, rr['P'], G)
                # points x of F with F - {x} on a positive level; is one of them in the apex triple?
                off = [x for x in G if positive_level([p for p in G if p != x])]
                sat_short[('apex_uses_off_level_point', any(x in (rr['p1'], rr['p2'], rr['p12']) for x in off))] += 1
                key = (mu, G)
                if smallest is None or key < smallest[0]: smallest = (key, rr)
    return dict(enum_secs=round(te, 1), closed_by_size=dict(Counter(len(F) for F in allF)),
                rank3_up_to_S3=dict(Counter(len(F) for F in r3)), stats=dict(st),
                structure_nsat=dict(structure), apex_vs_off_level_point=dict(sat_short),
                best_ratio=best_ratio, best_metric=best_metric, smallest=smallest)

# ----------------------------------------------------------------------------- C3

def C3():
    F = [(1, 1, 4), (2, 8, 1), (4, 4, 2), (8, 2, 1)]; P = (6, 6, 0)
    diffs = [sub(F[i], F[0]) for i in (1, 2, 3)]
    combos = {(p, q, r): add(sub(p, r), q) for p in F for q in F for r in F if r not in (p, q)}
    in_pi3 = [k for k, y in combos.items() if min(y) >= 1]
    return dict(closed=closed3(F), nontrivial_combos=len(combos), combos_in_Pi3=len(in_pi3),
                det=det3(*diffs), T=T_holds([P] + F), thetas=N_thetas(F, (6, 6), (2, 8, 1), (8, 2, 1)),
                lengths=[sum(p) for p in F], mu=12, short_part_positive=positive_level(F),
                positive_triples=[positive_level(T) for T in itertools.combinations(F, 3)],
                Delta4=Delta(F, (6, 6), 4), Kc=len({p[2] for p in F}))

# ----------------------------------------------------------------------------- C4

def family(n):
    line = [(3*n + 2*k, 1 + 5*k, 2*(n - k)) for k in range(n)]
    return line + [(1, 10*n - 8, 1), (10*n - 4, 1, 1)], (5*n, 5*n + 1)

def C4(nmax):
    bad = []; rows = []
    for n in range(3, nmax + 1):
        F, P = family(n); Fs = sorted(F)
        p = F[n-1]; p12 = F[n-2]
        ths = N_thetas(Fs, P, p, p)
        ok = (closed3(Fs) and rank_aff(Fs) == 3 and T_holds([P + (0,)] + Fs)
              and sub(add(p, p), p12) == P + (0,) and ths[0] == 7 and max(ths) == 5*n - 2
              and all(sum(f) < sum(P) for f in Fs) and not positive_level(Fs)
              and det3(sub(F[1], F[0]), sub(F[n], F[0]), sub(F[n+1], F[0])) == 29 - 50*n
              and len({f[2] for f in Fs}) == n + 1
              and all(Delta(Fs, P, t) == max(8, 7 * (min(t, 2*n) // 2)) for t in range(1, 3*n)))
        rows.append((n, sum(P), ths[0], max(ths), len({f[2] for f in Fs}), Delta(Fs, P, 7)))
        if not ok: bad.append(n)
    return dict(checked=(3, nmax), not_as_claimed=bad, sample=rows[:3] + rows[-1:])

# ----------------------------------------------------------------------------- C5 (grammars)

def parikh_sets(G, start, cap=4000):
    order, seen = [], set()
    def visit(X, stack):
        if X in seen: return True
        if X in stack: return False
        stack.add(X)
        for rhs in G[X]:
            for s in rhs:
                if not isinstance(s, str) and not visit(s, stack): return False
        stack.discard(X); seen.add(X); order.append(X); return True
    if not visit(start, set()): return None
    E = {'a': (1, 0, 0), 'b': (0, 1, 0), 'c': (0, 0, 1)}; Pm = {}
    for X in order:
        S = set()
        for rhs in G[X]:
            cur = {(0, 0, 0)}
            for s in rhs:
                cur = {add(x, E[s]) for x in cur} if isinstance(s, str) else {add(x, y) for x in cur for y in Pm[s]}
                if len(cur) > cap: return None
            S |= cur
        Pm[X] = S
    return Pm

def gstats(G):
    INF = float('inf'); tau = {X: INF for X in G}; ch = True
    while ch:
        ch = False
        for X, rules in G.items():
            for rhs in rules:
                l = sum(1 if isinstance(s, str) else tau[s] for s in rhs)
                if l < tau[X]: tau[X] = l; ch = True
    theta = max(sum(1 if isinstance(s, str) else tau[s] for s in rhs) for rs in G.values() for rhs in rs)
    r = max(max(sum(1 for s in rhs if not isinstance(s, str)) for rhs in rs) for rs in G.values())
    return len(G), max(r, 1), theta

def reduce_grammar(G, start):
    prod = set(); ch = True
    while ch:
        ch = False
        for X, rules in G.items():
            if X not in prod and any(all(isinstance(s, str) or s in prod for s in rhs) for rhs in rules):
                prod.add(X); ch = True
    if start not in prod: return None
    G = {X: [rhs for rhs in rs if all(isinstance(s, str) or s in prod for s in rhs)] for X, rs in G.items() if X in prod}
    reach, st = {start}, [start]
    while st:
        X = st.pop()
        for rhs in G[X]:
            for s in rhs:
                if not isinstance(s, str) and s not in reach: reach.add(s); st.append(s)
    return {X: G[X] for X in reach}

def random_acyclic(rng, v, letters):
    G = {}
    for X in range(v):
        rules = []
        for _ in range(rng.randint(1, 3)):
            rhs = []
            for _ in range(rng.randint(1, 3)):
                if X < v - 1 and rng.random() < 0.6: rhs.append(rng.randint(X + 1, v - 1))
                else: rhs.append(rng.choice(letters))
            rules.append(tuple(rhs))
        G[X] = rules
    return G

def C5(rng, quick):
    st = Counter(); worst = 0.0
    T = 4000 if quick else 20000
    for i in range(T):
        letters = 'aabbc' if i % 2 else 'aaabbbc'
        G = reduce_grammar(random_acyclic(rng, rng.randint(2, 8), letters), 0)
        if G is None: continue
        Pm = parikh_sets(G, 0)
        if Pm is None: continue
        L = Pm[0]
        ab = [p for p in L if p[0] and p[1] and not p[2]]
        if not ab: continue
        st['grammars_with_ab'] += 1
        mu = min(sum(p) for p in ab)
        abc = [p for p in L if p[0] and p[1] and p[2]]
        v, r, th = gstats(G)
        D = min(max([0] + [sum(P) - f[0] - f[1] for f in abc if f[2] <= th]) for P in ab if sum(P) == mu)
        bound = 3*v*th + 3*r*v*(th + D)
        if mu > bound: st['VIOLATION_LemmaC'] += 1
        if not [f for f in abc if f[2] <= th]: st['no_low_c_abc_word'] += 1
        worst = max(worst, mu / bound)
    st['max mu/bound'] = round(worst, 3)
    return dict(st)

# ----------------------------------------------------------------------------- C6 (structured search)

def closure(seed, B, maxpts=40):
    F = set(seed)
    while True:
        L = list(F); new = set()
        for p in L:
            for q in L:
                for r in L:
                    if r == p or r == q: continue
                    y = (p[0]+q[0]-r[0], p[1]+q[1]-r[1], p[2]+q[2]-r[2])
                    if min(y) >= 1 and y not in F:
                        if max(y) > B: return None          # touches the box: not used
                        new.add(y)
        if not new: return F
        F |= new
        if len(F) > maxpts: return None

def sample(rng, th, X, Yb):
    P = (X, Yb, 0); rs = []; Ys = []
    for _ in range(2):
        c = rng.randint(1, max(1, th - 1)); ea = rng.randint(0, th - c); eb = rng.randint(0, th - c - ea)
        rs.append((ea, eb, c))
    for _ in range(2):
        tot = rng.randint(th + 1, 3*th + 2); ya = rng.randint(0, tot); Ys.append((ya, tot - ya))
    if Ys[0][0] + Ys[1][0] > X - 1 or Ys[0][1] + Ys[1][1] > Yb - 1: return None
    p = [(X - Ys[i][0] + rs[i][0], Yb - Ys[i][1] + rs[i][1], rs[i][2]) for i in range(2)]
    if min(p[0]) < 1 or min(p[1]) < 1: return None
    p12 = sub(add(p[0], p[1]), P)
    if min(p12) < 1: return None
    return P, p[0], p[1], p12

def ext_closed(Fs, s):
    if s in Fs: return False
    S = Fs | {s}
    def bad(y): return y[0] >= 1 and y[1] >= 1 and y[2] >= 1 and y not in S
    for p in Fs:
        if bad((2*s[0]-p[0], 2*s[1]-p[1], 2*s[2]-p[2])) or bad((2*p[0]-s[0], 2*p[1]-s[1], 2*p[2]-s[2])):
            return False
        for q in Fs:
            if p != q and (bad((s[0]+p[0]-q[0], s[1]+p[1]-q[1], s[2]+p[2]-q[2])) or
                           bad((p[0]+q[0]-s[0], p[1]+q[1]-s[1], p[2]+q[2]-s[2]))):
                return False
    return True

def sat_cands(R, small=4):
    out = set()
    for x in range(1, small + 1):
        for y in range(1, small + 1):
            for z in range(1, R + 1):
                out |= {(x, y, z), (x, z, y), (z, x, y)}
    return sorted(out)

def C6(rng, secs):
    t0 = time.time(); st = Counter(); best = {}; structure = Counter()
    while time.time() - t0 < secs:
        th = rng.randint(2, 5); X = rng.randint(2*th + 2, 45); Yb = rng.randint(2*th + 2, 45)
        s = sample(rng, th, X, Yb)
        if s is None: continue
        P, p1, p2, p12 = s; nP = X + Yb
        F = closure([p1, p2, p12], 3*nP)
        if F is None: continue
        st['finite_base_closures'] += 1
        C1s = [c for c in sat_cands(2*nP) if ext_closed(F, c)]
        exts = [F | {c} for c in C1s]
        for i in range(len(C1s)):
            G = F | {C1s[i]}
            for j in range(i + 1, len(C1s)):
                if ext_closed(G, C1s[j]): exts.append(G | {C1s[j]})
        for G in exts:
            if rank_aff(G) < 3: continue
            st['rank3_closed_sets'] += 1
            if len(st) and st['rank3_closed_sets'] % 7 == 0:
                structure[(min(len(G), 9), nsat(G))] += 1
            Gl = sorted(G)
            ths = N_thetas(Gl, P[:2], p1, p2, cap=3*th)
            if not ths: continue
            st['admissible'] += 1
            short = [q for q in Gl if sum(q) < nP]
            if positive_level(short): continue
            st['CE_closed_only'] += 1
            if not T_holds([P] + Gl): continue
            st['CE_with_T'] += 1
            Kc = len({f[2] for f in Gl})
            r = nP / ths[0]
            if r > best.get('ratio', (0,))[0]: best['ratio'] = (round(r, 2), nP, ths[0], P[:2], p1, p2, p12, Gl)
            for t in ths:
                m = min(Kc, Delta(Gl, P[:2], t) / t, nP / t)
                if m > best.get('metric', (0,))[0]: best['metric'] = (round(m, 2), t, Kc, nP, P[:2], Gl)
                if t <= 6:
                    D = Delta(Gl, P[:2], t)
                    if D > best.get('Delta_theta<=6', (0,))[0]: best['Delta_theta<=6'] = (D, t, nP, P[:2], Gl)
    return dict(stats=dict(st), structure_sample=dict(structure), best=best)

# ----------------------------------------------------------------------------- main

def main():
    a = sys.argv[1:]
    seed = int(a[a.index('--seed') + 1]) if '--seed' in a else 1
    quick = '--quick' in a
    N = int(a[a.index('--box') + 1]) if '--box' in a else (8 if quick else 10)
    secs = float(a[a.index('--search-secs') + 1]) if '--search-secs' in a else (30 if quick else 150)
    rng = random.Random(seed); T0 = time.time()
    print('seed', seed, 'quick', quick, 'box', N)
    if '--only-search' in a:
        r = C6(rng, secs)
        print('C6 structured search (%ss):' % secs)
        for k, v in r.items(): print('   ', k, ':', v)
        print('total seconds', round(time.time() - T0, 1)); return
    print('C1 enumerator vs brute force {(N, max size): (#bf, #enum, equal)}:', C1(quick))
    r = C2(N)
    print('C2 exhaustive box', N)
    for k, v in r.items(): print('   ', k, ':', v)
    print('C3 counterexample E*:', C3())
    print('C4 family F_n:', C4(12 if quick else 30))
    print('C5 Lemma C on random CFGs:', C5(rng, quick))
    r = C6(rng, secs)
    print('C6 structured search (%ss):' % secs)
    for k, v in r.items(): print('   ', k, ':', v)
    print('total seconds', round(time.time() - T0, 1))

if __name__ == '__main__':
    main()
