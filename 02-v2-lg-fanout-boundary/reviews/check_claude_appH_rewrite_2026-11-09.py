#!/usr/bin/env python3
"""Numerical and small-model checks for the rewritten Appendix H (2026-11-09).

Standard library only.  Run:  python3 -I check_claude_appH_rewrite_2026-11-09.py
(about 1-2 minutes).  Nothing here replaces a proof.

(A) constants: mu=(27/4)^(1/3), gamma=ln3/ln mu, eta=1/80, C_eta, final exponents
    and the constant C0 with  tau <= C0 k^22 theta^8.
(B) exact check of the binomial step for 6 <= M <= 3000:
      (27/4)^floor(M/3) <= (M+1) * min_{floor(M/3) <= j <= floor(2M/3)} C(M+1, j)
(C) M*(k,theta) from the counting inequality, comparison with C0 k^22 theta^8,
    effective exponents.
(D) random value sequences along a heavy path: new selection rule
    (superincreasing, sum < Lambda, Lambda <= 3^M (v_top + d), formal values never
    taken, S_t + d <= 3^(t-1)(S_1 + d)) and the greedy filler (q <= 1 first, q <= 3
    later, exact target).
(E) small regular languages in C_{1,s} for typings with an isolated letter a
    (U1 with one letter of type 1 over {a,b,c}; content typing on {a,b};
    a typing with a group on the a-free words): cancellation, the period lemma
    (P0 = p0 N, F(l,r) a residue class, a ~ a^{1+p0}) and the base relations.
"""
import math, random, itertools, sys
from fractions import Fraction

random.seed(20261109)

# ---------------------------------------------------------------- (A)
mu = (27/4) ** (1/3)
gamma = math.log(3) / math.log(mu)
eta = 1/80
g = gamma / (1 - eta)
expK, expT = 2 + 11*g, 1 + 4*g
# C_eta = sup_{M>=0} (M+1)^6 mu^{-eta M}
best = 0.0
for M in range(0, 20000):
    val = 6*math.log(M+1) - eta*M*math.log(mu)
    best = max(best, val)
lnCeta = best
lnC0 = math.log(11) + g*(math.log(15625) + 2*math.log(mu) + lnCeta)
print("(A) mu=%.6f gamma=%.6f gamma/(1-eta)=%.6f" % (mu, gamma, g))
print("    exponents with eta=1/80: k^%.4f theta^%.4f (claimed <= 22, 8)" % (expK, expT))
print("    asymptotic exponents (eta->0): k^%.4f theta^%.4f" % (2+11*gamma, 1+4*gamma))
print("    ln C_eta = %.3f, ln C0 = %.3f (C0 ~ 10^%.1f); with k<=2(|G|+2): C ~ 10^%.1f"
      % (lnCeta, lnC0, lnC0/math.log(10), (lnC0+22*math.log(2))/math.log(10)))
assert expK <= 22 and expT <= 8

# ---------------------------------------------------------------- (B)
bad = 0
for M in range(6, 3001):
    k = M // 3
    lo, hi = M // 3, (2*M) // 3
    # min over the range is attained at an end (unimodality); compute both ends
    mn = min(math.comb(M+1, lo), math.comb(M+1, hi))
    if 27**k > 4**k * (M+1) * mn:
        bad += 1
    # also the intermediate claim C(3k,k) >= (27/4)^k/(3k+1)
    if 27**k > 4**k * (3*k+1) * math.comb(3*k, k):
        bad += 1
print("(B) binomial step, 6<=M<=3000: violations =", bad)
assert bad == 0

# ---------------------------------------------------------------- (C)
def counting_ok(M, k, th):
    ell = 5*k*k*th
    lhs = Fraction(27, 4) ** (M // 3)
    rhs = (M+1)**4 * k * (3*k + M + 4)**2 * ell**4
    return lhs <= rhs

def Mstar(k, th):
    best = 5
    M = 6
    # the inequality fails for all large M; scan until a long run of failures
    fails = 0
    while fails < 60:
        if counting_ok(M, k, th):
            best = M; fails = 0
        else:
            fails += 1
        M += 1
    return best

ratios = []
pts = []
for k in [2, 3, 5, 10, 30, 100, 10**3, 10**4, 10**6]:
    for th in [1, 2, 10, 100, 10**4, 10**6]:
        Ms = Mstar(k, th)
        tau_bound_ln = math.log(11) + Ms*math.log(3) + 2*math.log(k) + math.log(th)
        rhs_ln = lnC0 + 22*math.log(k) + 8*math.log(th)
        ratios.append(tau_bound_ln - rhs_ln)
        pts.append((k, th, Ms, tau_bound_ln))
print("(C) max over grid of ln(11*3^M* k^2 th) - ln(C0 k^22 th^8) = %.2f (must be <= 0)"
      % max(ratios))
assert max(ratios) <= 0
# effective exponents: slopes between large k (theta fixed) and large theta (k fixed)
def lnb(k, th):
    return math.log(11) + Mstar(k, th)*math.log(3) + 2*math.log(k) + math.log(th)
sk = (lnb(10**12, 10) - lnb(10**8, 10)) / math.log(10**4)
st = (lnb(10, 10**16) - lnb(10, 10**10)) / math.log(10**6)
print("    effective exponents of 11*3^M* k^2 th: k ~ %.2f, theta ~ %.2f" % (sk, st))

# ---------------------------------------------------------------- (D)
def random_path():
    d = random.randint(1, 30)
    istar = random.randint(1, 25)
    # pure lengths along the path, bottom-up: n_{istar} > d, n_{i-1} in [n_i, 2 n_i]
    nn = [0]*(istar+1)
    nn[istar] = d + random.randint(1, 3*d+5)
    for i in range(istar, 0, -1):
        nn[i-1] = random.randint(nn[i], 2*nn[i])
    n = nn[0]
    i0 = next(i for i in range(istar+1) if nn[i] < n) if nn[istar] < n else None
    if i0 is None or i0 == 0:
        return None
    v = [n]*(istar+1)
    for i in range(i0, istar+1):
        base = -(-nn[i] // d) * d          # least multiple of d >= n_i
        v[i] = base + d*random.randint(0, (nn[i] + 2*d - base)//d)
        assert nn[i] <= v[i] <= nn[i] + 2*d
    for i in range(istar):
        assert v[i] <= 2*v[i+1] + 2*d
    Vstar = d * random.randint(1, n // d) if n >= d else None
    if Vstar is None:
        return None
    D = random.choice([None, d*random.randint(1, 40)])
    return d, istar, i0, n, v, Vstar, D

viol = 0; trials = 0; maxM = 0
for _ in range(200000):
    P = random_path()
    if P is None:
        continue
    d, istar, i0, n, v, Vstar, D = P
    Lam = Vstar if D is None else min(Vstar, D)
    trials += 1
    sel = []
    S = 0
    if v[istar] < Lam:
        sel = [istar]; S = v[istar]
        S1 = S
        while True:
            j = sel[-1]
            cand = next((i for i in range(j-1, -1, -1) if v[i] > S), None)
            if cand is None:
                viol += 1; break          # should never happen
            if S + v[cand] >= Lam:
                break
            sel.append(cand); S += v[cand]
            if S + d > 3**(len(sel)-1) * (S1 + d):
                viol += 1
    M = len(sel)
    maxM = max(maxM, M)
    vals = [v[i] for i in sel]
    if any(vals[t] <= sum(vals[:t]) for t in range(M)): viol += 1
    if sum(vals) >= Lam: viol += 1
    if any(i < i0 for i in sel): viol += 1
    if Lam > 3**M * (v[istar] + d): viol += 1
    # filler (only meaningful if M >= 1)
    if M >= 1:
        X = Vstar - sum(vals)
        if X <= 0 or X % d: viol += 1
        for i in range(i0, istar+1):
            q = X // v[i]
            if i == i0 and q > 1: viol += 1
            if i > i0 and q > 3: viol += 1
            X -= q*v[i]
        if not (0 <= X < v[istar]) or X % d: viol += 1
print("(D) %d random paths, max M = %d, violations = %d" % (trials, maxM, viol))
assert viol == 0

# ---------------------------------------------------------------- (E)
# typings given as finite semigroups on symbols, with a map letter -> element
def typing_U1():
    # elements: 'one', 'z'; a -> one, b,c -> z
    mul = lambda x, y: 'one' if (x == 'one' and y == 'one') else 'z'
    return ['a', 'b', 'c'], {'a': 'one', 'b': 'z', 'c': 'z'}, mul
def typing_c2():
    mul = lambda x, y: x | y
    return ['a', 'b'], {'a': frozenset('a'), 'b': frozenset('b')}, mul
def make_typing(name):
    if name == 'U1':
        return typing_U1()
    if name == 'c2':
        return typing_c2()
    # 'grp': state = ('A',) a-only, ('F',parity) a-free, ('M',) a-mixed
    def mul(x, y):
        if x[0] == 'A' and y[0] == 'A': return ('A',)
        if x[0] == 'F' and y[0] == 'F': return ('F', x[1] ^ y[1])
        return ('M',)
    return ['a', 'b', 'c'], {'a': ('A',), 'b': ('F', 1), 'c': ('F', 0)}, mul

def random_dfa(sig, nq):
    delta = {(q, x): random.randrange(nq) for q in range(nq) for x in sig}
    acc = frozenset(q for q in range(nq) if random.random() < 0.4)
    return delta, acc

def build(sig, letter_type, mul, delta, acc, nq, cap=260):
    # elements: (transformation tuple, type); words realised; BFS with representative words
    def tr(word):
        return tuple(_run(q, word) for q in range(nq))
    def _run(q, word):
        for x in word: q = delta[(q, x)]
        return q
    elems = {}
    frontier = []
    for x in sig:
        e = (tr(x), letter_type[x])
        if e not in elems:
            elems[e] = x; frontier.append(e)
    while frontier:
        nf = []
        for e in frontier:
            for x in sig:
                t = tuple(delta[(q, x)] for q in e[0])
                f = (t, mul(e[1], letter_type[x]))
                if f not in elems:
                    elems[f] = elems[e] + x; nf.append(f)
                    if len(elems) > cap: return None
        frontier = nf
    return elems

def check_language(sig, letter_type, mul, isolated='a'):
    nq = random.randint(2, 5)
    delta, acc = random_dfa(sig, nq)
    E = build(sig, letter_type, mul, delta, acc, nq)
    if E is None: return None
    trans = sorted({e[0] for e in E})
    ident = tuple(range(nq))
    ctx = [ident] + trans                         # transformations of l and r (incl. empty)
    reach = sorted({l[0] for l in ctx})           # states after a left context
    Rmask = [sum(1 << j for j, r in enumerate(ctx) if r[q] in acc) for q in range(nq)]
    # D(t) is encoded by the vector of right-context masks after each reachable state
    D = {t: tuple(Rmask[t[q]] for q in reach) for t in trans}
    nonempty = lambda v: any(v)
    meet = lambda v, w: any(x & y for x, y in zip(v, w))
    if not any(nonempty(D[t]) for t in trans): return None
    els = list(E)
    for e1, e2 in itertools.combinations(els, 2):
        if e1[1] == e2[1] and meet(D[e1[0]], D[e2[0]]) and D[e1[0]] != D[e2[0]]:
            return None
    return E, D, delta, nq, acc

def run_E(name, ntries):
    sig, lt, mul = make_typing(name)
    a = 'a'
    stats = dict(langs=0, cancel=0, period=0, F=0, base=0, viol=0)
    for _ in range(ntries):
        res = check_language(sig, lt, mul)
        if res is None: continue
        E, D, delta, nq, acc = res
        stats['langs'] += 1
        def tr(word):
            out = []
            for q in range(nq):
                for x in word: q = delta[(q, x)]
                out.append(q)
            return tuple(out)
        def typ(word):
            t = lt[word[0]]
            for x in word[1:]: t = mul(t, lt[x])
            return t
        Dw = lambda w: D[tr(w)]
        nz = lambda v: any(v)
        sim = lambda u, v: Dw(u) == Dw(v)
        nona = [x for x in sig if x != a]
        def rword(maxlen):
            return ''.join(random.choice(sig) for _ in range(random.randint(1, maxlen)))
        # cancellation: same type x,y, zx ~ zy, D(zx) nonempty => x ~ y
        for _ in range(60):
            x, y, z = rword(5), rword(5), rword(3)
            if typ(x) == typ(y) and nz(Dw(z+x)) and sim(z+x, z+y):
                stats['cancel'] += 1
                if not sim(x, y): stats['viol'] += 1
            if typ(x) == typ(y) and nz(Dw(x+z)) and sim(x+z, y+z):
                stats['cancel'] += 1
                if not sim(x, y): stats['viol'] += 1
        # period lemma for a-mixed z0 with nonempty distribution
        for _ in range(30):
            z0 = rword(4)
            if a not in z0 or set(z0) == {a}: continue
            if not nz(Dw(z0)): continue
            P = [p for p in range(0, 40) if sim(a*p + z0, z0)]
            p0 = P[1] if len(P) > 1 else None
            stats['period'] += 1
            if p0 is not None:
                if P != [p for p in range(0, 40) if p % p0 == 0]: stats['viol'] += 1
                if not sim(a, a*(1+p0)): stats['viol'] += 1
            # F(l,r) for a few contexts
            for _ in range(5):
                l, r = rword(3), rword(3)
                Fs = [f for f in range(0, 40) if tr(l + a*f + z0 + r)[0] in acc]
                if not Fs: continue
                stats['F'] += 1
                f0 = Fs[0]
                if p0 is None:
                    if len(Fs) != 1: stats['viol'] += 1
                else:
                    if Fs != [f for f in range(f0, 40) if (f - f0) % p0 == 0]:
                        stats['viol'] += 1
        # base relations: W1,W2,W3 accepted in a common context, x+g0+y >= 1, d > g0
        for _ in range(60):
            om = rword(3)
            if set(om) <= {a}: continue
            x, y = random.randint(0, 4), random.randint(0, 4)
            d = random.randint(1, 6); g0 = random.randint(0, d-1)
            if x + g0 + y == 0: continue
            W1 = a*x + om + a*g0 + om + a*y
            W2 = a*x + om + a*(d+y)
            W3 = a*(x+d) + om + a*y
            common = any(x & y & z for x, y, z in zip(Dw(W1), Dw(W2), Dw(W3)))
            if not common: continue
            # under an isolated letter the three words have one type (they contain a)
            if not (typ(W1) == typ(W2) == typ(W3)): stats['viol'] += 1; continue
            stats['base'] += 1
            if not sim(om + a*d, a*d + om): stats['viol'] += 1
            if g0 >= 1 or a in om:
                z0, c0 = om + a*g0, d
            else:
                z0, c0 = om + a*d, 2*d
            if not nz(Dw(z0)): stats['viol'] += 1
            if not sim(a*d + z0, z0 + a*d): stats['viol'] += 1
            if not sim(z0 + z0, a*c0 + z0): stats['viol'] += 1
    return stats

for name, nt in [('U1', 2500), ('c2', 2500), ('grp', 2500)]:
    st = run_E(name, nt)
    print("(E) typing %-3s: %s" % (name, st))
    assert st['viol'] == 0
print("all checks passed")
