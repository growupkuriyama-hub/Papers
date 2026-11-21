"""check_claude_verify_fable_content_values_2026-11-11.py -- independent checks (Claude, verifying
thread) for fable_content_values_2026-11-10.md.  Standard library only; Fable's code is not reused.

  python3 check_claude_verify_fable_content_values_2026-11-11.py

W1  Ex1 and Ex2 at the word level: content-typed SUB_d (admissible contexts: inner separators
    nonempty) on all premise sentences up to a length bound, conclusions by the true predicate;
    the hand certificates of the report.
W2  Theorem 1 / Cor 1b against the word level on random finite-index K-languages with t = 2
    (letters a,b,c, stage pattern random, mod-2/mod-3 conditions per content).  Own
    implementation of the criterion: for every type T of arity d, the contents reachable through
    Comp(T) with every total n, and equality of N_M cap Z^{J_T} (computed as the set of
    J-supported vectors in a period box that lie in N_M).
W3  Lemma M (moving lemma) by brute force: for small K-languages that are SUB_m, every
    instance q, q - z, alpha in Q (q, alpha >= z^+ + 2*1_S) gives alpha - z in Q.
W4  Section 4.2 table: T for F4+P, E1+P, F_n+P (n = 3,4,5), index of <Q3-Q3>, a (WS)-breaking
    pair, and the shortest ab-point of p_S + <Q - Q> below |P| (own lattice code).
"""
import itertools, random
from collections import defaultdict
from math import gcd

rng = random.Random(1111)

# ------------------------------------------------------------------ word level
def occ(w, d):
    n = len(w)
    for c in itertools.combinations(range(n + 1), 2 * d):
        if any(c[2*i] == c[2*i+1] for i in range(d)): continue
        if any(c[2*i+1] == c[2*i+2] for i in range(d - 1)): continue
        x = tuple(w[c[2*i]:c[2*i+1]] for i in range(d))
        ctx = (w[:c[0]],) + tuple(w[c[2*i+1]:c[2*i+2]] for i in range(d - 1)) + (w[c[-1]:],)
        yield x, ctx

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

class KLang:
    def __init__(self, letters, stage, cond):
        self.letters, self.stage, self.cond = letters, stage, cond
    def nd(self, w):
        return all(self.stage[w[i]] <= self.stage[w[i+1]] for i in range(len(w) - 1))
    def member(self, w):
        if not w or not self.nd(w): return False
        m = tuple(w.count(a) for a in self.letters)
        M = frozenset(a for a, x in zip(self.letters, m) if x)
        return self.cond(M, dict(zip(self.letters, m)))

def W1():
    print('W1 Ex1, Ex2 at word level')
    ex1 = KLang('abc', {'a': 1, 'b': 2, 'c': 3},
                lambda M, m: (M == frozenset('ac') and (m['a'] - m['c']) % 2 == 0) or
                             (M == frozenset('abc') and m['a'] % 2 == 1 and m['c'] % 2 == 1))
    pos = [w for w in nd_words('abc', ex1.stage, 9) if ex1.member(w)]
    for d in (1, 2):
        print('   Ex1 arity', d, 'violation:', sub_violation(pos, ex1.member, d))
    E, F, x, y = ('', 'ac', ''), ('', 'b', ''), ('a', 'c'), ('aa', 'cc')
    print('   Ex1 hand certificate:', [ex1.member(fill(E, x)), ex1.member(fill(E, y)), ex1.member(fill(F, x)), ex1.member(fill(F, y))], '(expect T,T,T,F)')
    ex2 = KLang('abcde', {c: i for i, c in enumerate('abcde')},
                lambda M, m: (M == frozenset('ace') and all(m[c] % 2 for c in 'ace')) or
                             (M == frozenset('abcde') and m['a'] % 2 == m['c'] % 2 == m['e'] % 2))
    pos = [w for w in nd_words('abcde', ex2.stage, 9) if ex2.member(w)]
    for d in (1, 2, 3):
        print('   Ex2 arity', d, '(premises <= 9 letters) violation:', sub_violation(pos, ex2.member, d))
    E, F, x, y = ('', 'b', 'd', ''), ('', 'aa', 'cc', ''), ('a', 'c', 'e'), ('aa', 'cc', 'ee')
    print('   Ex2 hand certificate:', [ex2.member(fill(E, x)), ex2.member(fill(E, y)), ex2.member(fill(F, x)), ex2.member(fill(F, y))], '(expect T,T,T,F)')

# ------------------------------------------------------------------ W2
def W2(samples=40, LMAX=7):
    print('W2 Theorem 1 (finite-index form) vs word level, t = 2, random')
    contents = [frozenset(c) for r in (1, 2, 3) for c in itertools.combinations('abc', r)]
    agree = disagree = 0; bad = []
    tried = 0
    while tried < samples:
        stage = dict(zip('abc', rng.choice([(1, 1, 2), (1, 2, 2), (1, 2, 1), (2, 1, 1), (1, 2, 3)])))
        table = {}
        for M in contents:
            if rng.random() < 0.55:
                conds = []
                for _ in range(rng.randint(0, 2)):
                    mod = rng.choice((2, 3))
                    conds.append(({a: rng.randrange(mod) for a in M}, mod, rng.randrange(mod)))
                table[M] = conds
        def acc(M, m, table=table):
            if M not in table: return False
            return all((sum(w[a] * m[a] for a in w) - r) % mod == 0 for w, mod, r in table[M])
        lang = KLang('abc', stage, acc)
        pos = [w for w in nd_words('abc', stage, LMAX) if lang.member(w)]
        if len({frozenset(w) for w in pos}) < 2: continue
        tried += 1
        P = 6  # lcm of moduli
        def latt(M, J):   # N_M cap Z^J restricted to the period box, as residues
            S = set()
            for h in itertools.product(range(P), repeat=len(J)):
                hv = dict.fromkeys('abc', 0); hv.update(zip(J, h))
                if all((sum(w[a] * hv[a] for a in w)) % mod == 0 for w, mod, r in table[M]): S.add(h)
            return S
        for d in (1, 2):
            pred = True
            for T in itertools.product(contents, repeat=d):
                lo = [min(stage[a] for a in M) for M in T]; hi = [max(stage[a] for a in M) for M in T]
                if any(hi[i] > lo[i + 1] for i in range(d - 1)): continue
                J = sorted(set().union(*T))
                allowed = []  # stage windows of v_0..v_d
                for i in range(d + 1):
                    lo_s = hi[i - 1] if i > 0 else 0
                    hi_s = lo[i] if i < d else 99
                    allowed.append([a for a in 'abc' if lo_s <= stage[a] <= hi_s])
                # reachable contents with a total n (residues mod P), context letter counts in {0,1..P} (residues, support)
                reach = defaultdict(set)
                b = {a: sum(a in M for M in T) for a in 'abc'}
                for nres in itertools.product(range(P), repeat=len(J)):
                    n = dict.fromkeys('abc', 0); n.update({a: b[a] + v for a, v in zip(J, nres)})
                    for e in itertools.product(range(P + 1), repeat=3):
                        ev = dict(zip('abc', e))
                        # inner separators need a letter from their window
                        if d == 2 and not any(ev[a] > 0 for a in allowed[1]): continue
                        if any(ev[a] > 0 and not any(a in allowed[i] for i in range(d + 1)) for a in 'abc'): continue
                        tot = {a: ev[a] + n[a] for a in 'abc'}
                        M = frozenset(a for a in 'abc' if tot[a])
                        if acc(M, tot): reach[nres].add(M)
                for nres, Ms in reach.items():
                    Ms = list(Ms)
                    for M1, M2 in itertools.combinations(Ms, 2):
                        if latt(M1, J) != latt(M2, J): pred = False
            real = sub_violation(pos, lang.member, d) is None
            if pred == real: agree += 1
            else:
                disagree += 1; bad.append((stage, table, d, pred, real))
    print('    samples', tried, 'x arity 1,2: agree', agree, 'disagree', disagree)
    for x in bad[:3]: print('    disagreement:', x)

# ------------------------------------------------------------------ W3
def W3(trials=300):
    print('W3 Lemma M by brute force on small K-languages (box 7)')
    count = viol = 0
    for _ in range(trials):
        stage = dict(zip('abc', rng.choice([(1, 1, 1), (1, 1, 2), (1, 2, 2), (1, 2, 3)])))
        table = {}
        for M in [frozenset(c) for r in (2, 3) for c in itertools.combinations('abc', r)]:
            if rng.random() < 0.7:
                mod = rng.choice((2, 3)); table[M] = ({a: rng.randrange(mod) for a in M}, mod, rng.randrange(mod))
        def inQ(m, table=table):
            M = frozenset(a for a, x in zip('abc', m) if x)
            if M not in table: return False
            w, mod, r = table[M]
            return (sum(w.get(a, 0) * x for a, x in zip('abc', m)) - r) % mod == 0
        lang = KLang('abc', stage, lambda M, m: inQ(tuple(m[a] for a in 'abc')))
        stages_used = len(set(stage.values()))
        pos = [w for w in nd_words('abc', stage, 6) if lang.member(w)]
        if any(sub_violation(pos, lang.member, d) for d in range(1, stages_used + 1)): continue
        box = range(0, 7)
        pts = [m for m in itertools.product(box, repeat=3) if inQ(m)]
        for z in itertools.product(range(-2, 3), repeat=3):
            if not any(z): continue
            S = [i for i in range(3) if z[i]]
            need = [max(z[i], 0) + (2 if z[i] else 0) for i in range(3)]
            qs = [q for q in pts if all(q[i] >= need[i] for i in range(3)) and inQ(tuple(q[i] - z[i] for i in range(3)))]
            if not qs: continue
            for al in pts:
                if all(al[i] >= need[i] for i in range(3)):
                    count += 1
                    if not inQ(tuple(al[i] - z[i] for i in range(3))): viol += 1
    print('    instances', count, 'violations', viol)

# ------------------------------------------------------------------ W4
def hnf(vecs):
    rows = [list(v) for v in vecs if any(v)]; basis = []
    for col in range(3):
        while True:
            nz = [r for r in rows if r[col]]
            if len(nz) <= 1: break
            nz.sort(key=lambda r: abs(r[col])); p = nz[0]
            for r in nz[1:]:
                q = r[col] // p[col]
                for i in range(3): r[i] -= q * p[i]
            rows = [r for r in rows if any(r)]
        nz = [r for r in rows if r[col]]
        if nz:
            p = nz[0]; basis.append(p if p[col] > 0 else [-x for x in p]); rows = [r for r in rows if r is not p]
    return basis
def inlat(v, B):
    v = list(v)
    for p in B:
        c = next(i for i in range(3) if p[i])
        if any(v[i] for i in range(c)) or v[c] % p[c]: return False
        q = v[c] // p[c]; v = [a - q * b for a, b in zip(v, p)]
    return not any(v)
def T_ok(Q):
    Q = set(Q)
    for q in Q:
        for q2 in Q:
            if q == q2 or tuple(x > 0 for x in q) != tuple(x > 0 for x in q2): continue
            h = tuple(b - a for a, b in zip(q, q2))
            lo = tuple(max(-x, 0) + (x != 0) for x in h); hi = tuple(max(x, 0) + (x != 0) for x in h)
            for x in Q:
                for A, Bv in ((lo, hi), (hi, lo)):
                    g = tuple(a - b for a, b in zip(x, A))
                    if min(g) >= 0 and tuple(b + c for b, c in zip(Bv, g)) not in Q: return False
    return True
def W4():
    print('W4 Section 4.2 table (own code)')
    ex = [('F4+(14,26)', [(1,3,12),(4,8,1),(6,4,4),(12,1,3)], (14,26,0)),
          ('E1+(6,5)', [(1,8,1),(2,3,4),(4,4,2),(8,1,1)], (6,5,0))]
    for n in (3, 4, 5):
        ex.append(('F_%d+P' % n, [(3*n+2*k, 1+5*k, 2*(n-k)) for k in range(n)] + [(1,10*n-8,1),(10*n-4,1,1)], (5*n, 5*n+1, 0)))
    for name, Q3, P in ex:
        B3 = hnf([tuple(a - b for a, b in zip(q, Q3[0])) for q in Q3[1:]])
        idx = abs(B3[0][0] * B3[1][1] * B3[2][2]) if len(B3) == 3 else None
        Ball = hnf([tuple(a - b for a, b in zip(q, Q3[0])) for q in Q3[1:] + [P]])
        # smallest (by l1) lattice vectors of <Q3-Q3>
        small = sorted((z for z in itertools.product(range(-5, 6), repeat=3) if any(z) and inlat(z, B3)), key=lambda z: (sum(map(abs, z)), z))
        ws = None
        for q in sorted(Q3):
            for z in small[:12]:
                if all(q[i] >= abs(z[i]) + 2 for i in range(3) if z[i]):
                    qz = tuple(q[i] - z[i] for i in range(3))
                    if qz not in Q3: ws = (q, z, qz); break
            if ws: break
        shortab = sorted(((i, j) for i in range(1, sum(P)) for j in range(1, sum(P) - i) if inlat((i - P[0], j - P[1], 0), Ball)), key=lambda p: (sum(p), p))
        print('   %-12s (T)=%s index<Q3-Q3>=%s WS-break=%s  #short ab in p_S+<Q-Q> =%d, shortest %s'
              % (name, T_ok(set(Q3) | {P}), idx, ws, len(shortab), shortab[:1]))

if __name__ == '__main__':
    W1(); W2(); W3(); W4()
