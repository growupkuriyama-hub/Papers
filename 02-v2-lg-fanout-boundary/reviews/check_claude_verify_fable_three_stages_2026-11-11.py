"""check_claude_verify_fable_three_stages_2026-11-11.py -- independent checks (Claude Opus,
verifying thread) for fable_three_stages_2026-11-11.md.  Standard library only; Fable's code not reused.

  python3 check_claude_verify_fable_three_stages_2026-11-11.py

V1  Lemma M* by brute force: small finite-index K-languages (k = 3 or 4, several stage patterns)
    that are word-level SUB_1 (premises <= 6 letters); for every z with pi(supp z) = 1 (support in
    one stage or in two ADJACENT stages) and all q, q - z, alpha in a box with the depth condition,
    alpha - z must lie in Q.  Moves spanning two adjacent stages are the new case.
V2  Cor M* with an own implementation of the finite-index criterion (Theorem 1 / Cor 1b of (258)),
    k = 4, t = 3 or 4, modulus 2: if the criterion gives SUB_1 (resp. SUB_1 and SUB_2), the face
    lattices agree on every S with pi(S) <= 1 (resp. <= 2).
V3  Theorem B on random CFGs whose rules respect stage intervals (so L(G) is a subset of a*b*c*,
    one letter per stage): every typed nonterminal (A, M) has a generation of length
    <= 2 f k D (1 + r) theta, D = v (2^k - 1)^f, f = 1.  Exact shortest typed generations by a
    fixed point; thickness = max over rules of the shortest sentence through the rule.
V4  Ex2^0_m (m = 2, 3) at the word level: SUB_1, SUB_2 on premises <= 9 letters; the SUB_3
    certificate of the report; mu_ace = 3m.
"""
import itertools, random
from collections import defaultdict

rng = random.Random(20261112)

def occ(w, d):
    n = len(w)
    for c in itertools.combinations(range(n + 1), 2 * d):
        if any(c[2*i] == c[2*i+1] for i in range(d)): continue
        if any(c[2*i+1] == c[2*i+2] for i in range(d - 1)): continue
        yield (tuple(w[c[2*i]:c[2*i+1]] for i in range(d)),
               (w[:c[0]],) + tuple(w[c[2*i+1]:c[2*i+2]] for i in range(d - 1)) + (w[c[-1]:],))

def fill(ctx, x):
    s = ctx[0]
    for i, xi in enumerate(x): s += xi + ctx[i + 1]
    return s

def sub_violation(pos, member, d):
    by_ctx = defaultdict(set); ctxs = defaultdict(set)
    for w in pos:
        for x, ctx in occ(w, d):
            by_ctx[ctx].add(x); ctxs[x].add(ctx)
    seen = set()
    for ctx, xs in by_ctx.items():
        g = defaultdict(list)
        for x in xs: g[tuple(frozenset(c) for c in x)].append(x)
        for grp in g.values():
            for x, y in itertools.permutations(grp, 2):
                if (x, y) in seen: continue
                seen.add((x, y))
                for F in ctxs[x]:
                    if not member(fill(F, y)): return (ctx, F, x, y)
    return None

def nd_words(letters, stage, L):
    out = []
    def rec(w, last):
        if w: out.append(w)
        if len(w) == L: return
        for a in letters:
            if stage[a] >= last: rec(w + a, stage[a])
    rec('', -1)
    return out

def make_lang(letters, stage, table):
    """table: content -> list of (weights, mod, residue); finite index (all mods > 0)."""
    def inQ(m):
        M = frozenset(a for a, x in zip(letters, m) if x)
        if M not in table: return False
        return all((sum(w.get(a, 0) * x for a, x in zip(letters, m)) - r) % mod == 0 for w, mod, r in table[M])
    def member(w):
        if not w or any(stage[w[i]] > stage[w[i + 1]] for i in range(len(w) - 1)): return False
        return inQ(tuple(w.count(a) for a in letters))
    return inQ, member

def pi_cover(stages):
    st = sorted(set(stages)); cnt = i = 0
    while i < len(st):
        i += 2 if i + 1 < len(st) and st[i + 1] == st[i] + 1 else 1
        cnt += 1
    return cnt

def random_table(letters, mods=(2, 3), p=0.6):
    contents = [frozenset(c) for r in range(1, len(letters) + 1) for c in itertools.combinations(letters, r)]
    table = {}
    for M in contents:
        if rng.random() < p:
            table[M] = [({a: rng.randrange(mod) for a in M}, mod, rng.randrange(mod))
                        for mod in [rng.choice(mods) for _ in range(rng.randint(0, 2))]]
    return table

# ------------------------------------------------------------------ V1
def V1(trials=250):
    print('V1 Lemma M* (arity 1, moves inside one stage or two adjacent stages)')
    patterns = [('abc', (1, 2, 3)), ('abc', (1, 1, 2)), ('abcd', (1, 2, 3, 4)), ('abcd', (1, 1, 2, 3))]
    inst = viol = langs = adj_inst = 0
    for _ in range(trials):
        letters, st = rng.choice(patterns); stage = dict(zip(letters, st)); k = len(letters)
        table = random_table(letters)
        inQ, member = make_lang(letters, stage, table)
        pos = [w for w in nd_words(letters, stage, 6) if member(w)]
        if len({frozenset(w) for w in pos}) < 2 or sub_violation(pos, member, 1): continue
        langs += 1
        box = range(0, 6) if k == 3 else range(0, 5)
        pts = [m for m in itertools.product(box, repeat=k) if inQ(m)]
        for z in itertools.product(range(-2, 3), repeat=k):
            S = [i for i in range(k) if z[i]]
            if not S or pi_cover([st[i] for i in S]) != 1: continue
            adj = len({st[i] for i in S}) == 2
            need = [max(z[i], 0) + (2 if z[i] else 0) for i in range(k)]
            if not any(all(q[i] >= need[i] for i in range(k)) and inQ(tuple(q[i] - z[i] for i in range(k))) for q in pts):
                continue
            for al in pts:
                if all(al[i] >= need[i] for i in range(k)):
                    inst += 1; adj_inst += adj
                    if not inQ(tuple(al[i] - z[i] for i in range(k))): viol += 1
    print('    SUB_1 languages %d, instances %d (two adjacent stages: %d), violations %d' % (langs, inst, adj_inst, viol))

# ------------------------------------------------------------------ V2
def criterion_ok(letters, stage, table, d, P):
    """own finite-index criterion (Cor 1b): True iff (*) holds at arity d."""
    k = len(letters)
    contents = [frozenset(c) for r in range(1, k + 1) for c in itertools.combinations(letters, r)]
    def acc(tot):
        M = frozenset(a for a in letters if tot[a])
        if M not in table: return None
        ok = all((sum(w.get(a, 0) * tot[a] for a in letters) - r) % mod == 0 for w, mod, r in table[M])
        return M if ok else None
    def latt(M, J):
        return frozenset(h for h in itertools.product(range(P), repeat=len(J))
                         if all(sum(w.get(a, 0) * x for a, x in zip(J, h)) % mod == 0 for w, mod, r in table[M]))
    cache = {}
    for T in itertools.product(contents, repeat=d):
        lo = [min(stage[a] for a in M) for M in T]; hi = [max(stage[a] for a in M) for M in T]
        if any(hi[i] > lo[i + 1] for i in range(d - 1)): continue
        J = sorted(set().union(*T)); b = {a: sum(a in M for M in T) for a in letters}
        win = [[a for a in letters if (hi[i - 1] if i else 0) <= stage[a] <= (lo[i] if i < d else 99)] for i in range(d + 1)]
        for nres in itertools.product(range(P), repeat=len(J)):
            n = dict.fromkeys(letters, 0); n.update({a: b[a] + v for a, v in zip(J, nres)})
            Ms = set()
            for e in itertools.product(range(P + 1), repeat=k):
                ev = dict(zip(letters, e))
                if any(not any(ev[a] for a in win[i]) for i in range(1, d)): continue
                if any(ev[a] and not any(a in win[i] for i in range(d + 1)) for a in letters): continue
                M = acc({a: ev[a] + n[a] for a in letters})
                if M: Ms.add(M)
            Ms = list(Ms)
            for M1, M2 in itertools.combinations(Ms, 2):
                key = (M1, M2, tuple(J))
                if key not in cache: cache[key] = latt(M1, J) == latt(M2, J)
                if not cache[key]: return False
    return True

def V2(samples=400):
    print('V2 Cor M* with own criterion (k = 4, modulus 2)')
    letters = 'abcd'; stats = defaultdict(int); tried = 0; bad = []
    while tried < samples:
        st = rng.choice([(1, 2, 3, 4), (1, 1, 2, 3), (1, 2, 2, 3), (1, 2, 3, 3)])
        stage = dict(zip(letters, st))
        table = random_table(letters, mods=(2,), p=0.5)
        # keep only nonempty faces (the set M* of the report): Q_M has a point in {1,2}^M
        table = {M: c for M, c in table.items()
                 if any(all((sum(w.get(a, 0) * x for a, x in zip(letters, pt)) - r) % mod == 0 for w, mod, r in c)
                        for pt in itertools.product(*[(1, 2) if a in M else (0,) for a in letters]))}
        if len(table) < 2: continue
        tried += 1
        ok1 = criterion_ok(letters, stage, table, 1, 2)
        ok2 = ok1 and criterion_ok(letters, stage, table, 2, 2)
        for M1, M2 in itertools.combinations(table, 2):
            I = sorted(M1 & M2)
            for r in range(1, len(I) + 1):
                for S in itertools.combinations(I, r):
                    p = pi_cover([stage[a] for a in S])
                    agree = all((all(sum(w.get(a, 0) * x for a, x in zip(S, h)) % 2 == 0 for w, _, _ in table[M1]) ==
                                 all(sum(w.get(a, 0) * x for a, x in zip(S, h)) % 2 == 0 for w, _, _ in table[M2]))
                                for h in itertools.product(range(2), repeat=len(S)))
                    for d, ok in ((1, ok1), (2, ok2)):
                        if ok and p <= d:
                            stats[('SUB<=%d' % d, 'agree' if agree else 'DISAGREE')] += 1
                            if not agree and len(bad) < 3: bad.append((stage, {''.join(sorted(K)): c for K, c in table.items()}, ''.join(sorted(M1)), ''.join(sorted(M2)), S, d))
    print('    samples', tried, dict(stats))
    for x in bad: print('    disagreement:', x)

# ------------------------------------------------------------------ V3
def V3(trials=3000):
    print('V3 Theorem B on random stage-respecting CFGs (one letter per stage, f = 1)')
    letters = 'abc'; stage = {'a': 1, 'b': 2, 'c': 3}
    worst = 0.0; count = viol = 0
    for _ in range(trials):
        v = rng.randint(2, 6)
        iv = {}
        for X in range(v):
            lo = rng.randint(1, 3); iv[X] = (lo, rng.randint(lo, 3))
        iv[0] = (1, 3)
        G = {}
        for X in range(v):
            lo, hi = iv[X]; rules = []
            for _ in range(rng.randint(1, 3)):
                cur = lo; rhs = []
                for _ in range(rng.randint(1, 4)):
                    cands = [s for s in letters if cur <= stage[s] <= hi] + \
                            [Y for Y in range(v) if Y != X and cur <= iv[Y][0] and iv[Y][1] <= hi]
                    if not cands: break
                    s = rng.choice(cands); rhs.append(s)
                    cur = stage[s] if isinstance(s, str) else iv[s][1]
                if rhs: rules.append(tuple(rhs))
            G[X] = rules
        # recursion allowed (Y != X only forbids immediate self-loops); exact typed shortest via fixed point
        best = {}
        ch = True
        while ch:
            ch = False
            for X, rs in G.items():
                for rhs in rs:
                    cur = {frozenset(): 0}
                    for s in rhs:
                        items = [(frozenset(s), 1)] if isinstance(s, str) else [(M, l) for (Y, M), l in best.items() if Y == s]
                        nxt = {}
                        for M0, l0 in cur.items():
                            for M1, l1 in items:
                                M2 = M0 | M1
                                if l0 + l1 < nxt.get(M2, 10**9): nxt[M2] = l0 + l1
                        cur = nxt
                    for M, l in cur.items():
                        if M and l < best.get((X, M), 10**9): best[(X, M)] = l; ch = True
        prod = {X for (X, M) in best}
        if 0 not in prod: continue
        # reduce: reachable productive part
        reach = {0}; stack = [0]
        while stack:
            X = stack.pop()
            for rhs in G[X]:
                if all(isinstance(s, str) or s in prod for s in rhs):
                    for s in rhs:
                        if not isinstance(s, str) and s not in reach: reach.add(s); stack.append(s)
        Gr = {X: [r for r in G[X] if all(isinstance(s, str) or s in prod for s in r)] for X in reach}
        inside = {X: min(l for (Y, M), l in best.items() if Y == X) for X in reach}
        outside = {0: 0}; ch = True
        while ch:
            ch = False
            for X, rs in Gr.items():
                if X not in outside: continue
                for rhs in rs:
                    tot = sum(1 if isinstance(s, str) else inside[s] for s in rhs)
                    for s in rhs:
                        if not isinstance(s, str):
                            o = outside[X] + tot - inside[s]
                            if o < outside.get(s, 10**9): outside[s] = o; ch = True
        theta = max(1, max(outside[X] + sum(1 if isinstance(s, str) else inside[s] for s in r) for X, rs in Gr.items() for r in rs))
        r = max(1, max(sum(not isinstance(s, str) for s in rr) for rs in Gr.values() for rr in rs))
        vv = len(Gr); k = 3; f = 1
        bound = 2 * f * k * vv * (2 ** k - 1) ** f * (1 + r) * theta
        count += 1
        for (X, M), l in best.items():
            if X in Gr:
                worst = max(worst, l / bound)
                if l > bound: viol += 1
    print('    grammars %d, violations %d, max (shortest typed generation)/bound = %.4f' % (count, viol, worst))

# ------------------------------------------------------------------ V4
def V4():
    print('V4 Ex2^0_m at the word level')
    letters = 'abcde'; stage = dict(zip(letters, range(1, 6)))
    for m in (2, 3):
        table = {frozenset('ace'): [({'a': 1}, m, 0), ({'c': 1}, m, 0), ({'e': 1}, m, 0)],
                 frozenset('abcde'): [({'a': 1, 'c': -1}, m, 0), ({'c': 1, 'e': -1}, m, 0)]}
        inQ, member = make_lang(letters, stage, table)
        pos = [w for w in nd_words(letters, stage, 9) if member(w)]
        r = [sub_violation(pos, member, d) for d in (1, 2)]
        E, F, x, y = ('', 'b', 'd', ''), ('a' * (m - 1), 'c' * (m - 1), 'e' * (m - 1), ''), ('a', 'c', 'e'), ('aa', 'cc', 'ee')
        cert = [member(fill(E, x)), member(fill(E, y)), member(fill(F, x)), member(fill(F, y))]
        mu = min(len(w) for w in pos if set(w) == set('ace')) if any(set(w) == set('ace') for w in pos) else None
        print('    m=%d: SUB_1 viol %s, SUB_2 viol %s, SUB_3 certificate %s (expect T,T,T,F), mu_ace (<=9) %s'
              % (m, r[0], r[1], cert, mu))

if __name__ == '__main__':
    V1(); V2(); V3(); V4()
