#!/usr/bin/env python3
r"""check_claude_fanout2_rigid_round5_2026-11-09.py

Round 5 of the op:fanout-two exploration (paper #2): conjecture R (rigid targets at fan-out 2).
Standard library only; seed 20261109; a few minutes.  Everything printed is an OBSERVATION.
Substitutability checks on FINITE languages are exhaustive (all d<=2 occurrences); for the
infinite families nothing here is a membership proof.  A printed violation (x, y, shared context,
distinguishing context) is a genuine disproof of membership (all words decided exactly).
The utilities of section [1] are copied from the round-4 script.

Sections
 [1] MCFG utilities, exhaustive d<=2 check, T1-certificate search, operator B (round 4).
 [2] Word combinatorics behind Lemma E (equal copies) and Lemma Q (square-gap commutation).
 [3] Lemma Q on the doubling family: the factor yy s yy w yy with y=a, s=bb; explicit move W_3 -> W'.
 [4] Task 3, hand-made candidates (periodic (i), content-disjoint ends (ii)), n<=3.
 [5] Task 3, random doubling-type families (M={a,b} and M={a}); survivors of n<=2 rechecked at n=3.
 [6] Task 4 (light): fixpoints of K -> L(B(K)) on random finite targets.
"""
import itertools, random, time, sys, os
if os.environ.get("PYTHONHASHSEED") != "0":          # set iteration order fixed, so the output is reproducible
    os.environ["PYTHONHASHSEED"] = "0"; os.execv(sys.executable, [sys.executable] + sys.argv)
random.seed(20261109)
INF = float("inf")
T0 = time.time()

# ------------------------------------------------------------------ [1] utilities (round 4) ----
class MCFG:
    """rule = (lhs, children, template); template = tuple of components; a component is a
    list of symbols: terminal = 1-char str, variable = (child index, component index)."""
    def __init__(self, fan, rules, start="S"):
        self.fan = dict(fan); self.S = start; self.V = sorted(self.fan)
        self.rules = [(l, list(ch), tuple(tuple(c) for c in t)) for l, ch, t in rules]
    def check_good(self):
        for l, ch, t in self.rules:
            assert len(t) == self.fan[l] and all(len(c) > 0 for c in t)
            occ = [s for c in t for s in c if isinstance(s, tuple)]
            assert sorted(occ) == sorted((i, j) for i, B in enumerate(ch) for j in range(self.fan[B]))
            for i in range(len(ch)):
                o = [s[1] for s in occ if s[0] == i]; assert o == sorted(o)
            for c in t:
                for a, b in zip(c, c[1:]):
                    assert not (isinstance(a, tuple) and isinstance(b, tuple) and a[0] == b[0] and b[1] == a[1] + 1)
        return True
    @staticmethod
    def terms(t): return [s for c in t for s in c if isinstance(s, str)]
    def size(self): return len(self.V) + sum(1 + len(ch) + sum(len(c) for c in t) for _, ch, t in self.rules)
    def rank(self): return max(len(ch) for _, ch, _ in self.rules)
    def rho_max(self): return max(len(self.terms(t)) for _, _, t in self.rules)
    def lam(self, M=None):
        val = {A: INF for A in self.V}; ch_ = True
        while ch_:
            ch_ = False
            for l, ch, t in self.rules:
                tm = self.terms(t)
                if M is not None and any(a not in M for a in tm): continue
                v = len(tm) + sum(val[B] for B in ch)
                if v < val[l]: val[l] = v; ch_ = True
        return val
    def theta(self):
        lam = self.lam(); out = {A: INF for A in self.V}; out[self.S] = 0; ch_ = True
        while ch_:
            ch_ = False
            for l, ch, t in self.rules:
                if out[l] == INF: continue
                base = out[l] + len(self.terms(t)) + sum(lam[B] for B in ch)
                for B in ch:
                    if base - lam[B] < out[B]: out[B] = base - lam[B]; ch_ = True
        return max(out[l] + len(self.terms(t)) + sum(lam[B] for B in ch) for l, ch, t in self.rules)
    def mu(self, M):
        """least length of a word with content exactly M (DP over (nonterminal, content))."""
        I = {A: {} for A in self.V}; ch_ = True
        while ch_:
            ch_ = False
            for l, ch, t in self.rules:
                combos = {frozenset(self.terms(t)): len(self.terms(t))}
                for B in ch:
                    new = {}
                    for c0, l0 in combos.items():
                        for c1, l1 in I[B].items():
                            if l0 + l1 < new.get(c0 | c1, INF): new[c0 | c1] = l0 + l1
                    combos = new
                for c, ln in combos.items():
                    if ln < I[l].get(c, INF): I[l][c] = ln; ch_ = True
        return I[self.S].get(frozenset(M), INF)
    def words(self, N):
        tup = {A: set() for A in self.V}; ch_ = True
        while ch_:
            ch_ = False
            for l, ch, t in self.rules:
                pools = [list(tup[B]) for B in ch]
                if any(not p for p in pools): continue
                nt = len(self.terms(t))
                for combo in itertools.product(*pools):
                    if nt + sum(sum(map(len, y)) for y in combo) > N: continue
                    res = tuple("".join(s if isinstance(s, str) else combo[s[0]][s[1]] for s in c) for c in t)
                    if res not in tup[l]: tup[l].add(res); ch_ = True
        return {y[0] for y in tup[self.S]}

def occ(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1): yield (w[i:j],), (w[:i], w[j:])
    else:
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for e in range(c + 1, n + 1):
                        yield (w[a:b], w[c:e]), (w[:a], w[b:c], w[e:])
def fill(E, x):
    s = E[0]
    for xi, ei in zip(x, E[1:]): s += xi + ei
    return s
def ctype(x): return tuple(frozenset(c) for c in x)
def violations(L, d, limit=None):
    """exhaustive for finite L, content typing. returns list of (x, y, shared E, distinguishing E')"""
    D = {}
    for w in L:
        for x, E in occ(w, d): D.setdefault(x, set()).add(E)
    by = {}
    for x in D: by.setdefault(ctype(x), []).append(x)
    out = []
    for xs in by.values():
        ctx = {}
        for x in xs:
            for E in D[x]: ctx.setdefault(E, []).append(x)
        for E, ys in ctx.items():
            for y in ys[1:]:
                if D[ys[0]] != D[y]:
                    out.append((ys[0], y, E, next(iter(D[ys[0]] ^ D[y]))))
                    if limit and len(out) >= limit: return out
    return out
def in_class(L, f=2):
    for d in range(1, f + 1):
        v = violations(L, d, limit=1)
        if v: return False, (d,) + v[0]
    return True, None
def smallest_violation(L):
    for d in (1, 2):
        v = violations(L, d)
        if v:
            v.sort(key=lambda r: sum(map(len, r[0])) + sum(map(len, r[1])))
            x, y, E, E2 = v[0]
            return d, x, y, E, E2, fill(E, x) == fill(E, y)
    return None


def blocks(w, out):
    b = 0; prev = False
    for ch in w:
        cur = ch in out
        if cur and not prev: b += 1
        prev = cur
    return b

def t1_certificate(L, maxpi=4):
    """search T1 instances (x1, r, x2) with r = sigma z sigma, minimal x1,x2, in words of L and test the
    induced transfer in every word of L; return a violation certificate or None."""
    seen = set()
    for w in L:
        n = len(w)
        for pi in range(1, maxpi + 1):
            for st in range(1, n - pi - 1):
                if w[st] != w[st + pi]: continue
                t, v, s = w[st:st + pi], w[st + pi], w[st + 1:st + pi + 1]; need = set(t)
                x1 = next((w[a:st] for a in range(st - 1, -1, -1) if need <= set(w[a:st])), None)
                x2 = next((w[st + pi + 1:b] for b in range(st + pi + 2, n + 1) if need <= set(w[st + pi + 1:b])), None)
                if x1 is None or x2 is None or (x1, t, x2) in seen: continue
                seen.add((x1, t, x2)); X, Y = (x1 + t, x2), (x1, s + x2)
                E0 = (w[:st - len(x1)], v, w[st + pi + 1 + len(x2):])
                for P, Q in ((X, Y), (Y, X)):
                    for u in L:
                        i = u.find(P[0])
                        while i != -1:
                            j = u.find(P[1], i + len(P[0]) + 1)
                            while j != -1:
                                E = (u[:i], u[i + len(P[0]):j], u[j + len(P[1]):])
                                if fill(E, Q) not in L: return P, Q, E0, E
                                j = u.find(P[1], j + 1)
                            i = u.find(P[0], i + 1)
    return None

def obs_ctx(K):
    D = {}
    for w in K:
        for d in (1, 2):
            for x, E in occ(w, d): D.setdefault(x, set()).add(E)
    return D
def witnesses(z, rmax=2, f=2):
    """composition witnesses z = rho(u_1..u_r) with rho good, children in first-appearance order."""
    res = []
    def segs(s):
        n = len(s)
        for mask in range(1 << (n - 1)):
            p, st = [], 0
            for i in range(1, n):
                if mask >> (i - 1) & 1: p.append(s[st:i]); st = i
            p.append(s[st:]); yield p
    for choice in itertools.product(*[list(segs(c)) for c in z]):
        pieces = [(ci, p) for ci, ps in enumerate(choice) for p in ps]
        for r in range(1, rmax + 1):
            for lab in itertools.product(range(-1, r), repeat=len(pieces)):
                if any(j not in lab for j in range(r)): continue
                cnt = [0] * r; sym = []
                for (ci, p), l in zip(pieces, lab):
                    if l == -1: sym.append((ci, p, None))
                    else: sym.append((ci, p, (l, cnt[l]))); cnt[l] += 1
                if max(cnt) > f: continue
                bad = False
                for a, b in zip(sym, sym[1:]):
                    if a[0] != b[0]: continue
                    if a[2] is None and b[2] is None: bad = True
                    if a[2] and b[2] and a[2][0] == b[2][0] and b[2][1] == a[2][1] + 1: bad = True
                firsts = [next(i for i, s in enumerate(sym) if s[2] and s[2][0] == j) for j in range(r)]
                if bad or firsts != sorted(firsts): continue
                ch = [tuple(s[1] for s in sym if s[2] and s[2][0] == j) for j in range(r)]
                tm = [[] for _ in z]
                for ci, p, v in sym: tm[ci].extend(list(p) if v is None else [v])
                res.append((ch, tm))
    return res
def B_lang(K, N, rmax=2):
    """L(B^{<=rmax}_{2,c}(K)) restricted to length <= N (exact when K is inside a finite target of max length N)."""
    D = obs_ctx(K); O = set(D); rules = []
    for z in O:
        for ch, tm in witnesses(z, rmax):
            if all(c in O for c in ch): rules.append((z, ch, tm))
    by = {}
    for x in O: by.setdefault(ctype(x), []).append(x)
    link = {x: [y for y in xs if y != x and D[x] & D[y]] for xs in by.values() for x in xs}
    gen = {x: {x} for x in O}; chg = True
    while chg:
        chg = False
        for z, ch, tm in rules:
            for combo in itertools.product(*[gen[c] for c in ch]):
                y = tuple("".join(s if isinstance(s, str) else combo[s[0]][s[1]] for s in c) for c in tm)
                if sum(map(len, y)) <= N and y not in gen[z]: gen[z].add(y); chg = True
        for x, ys in link.items():
            for y in ys:
                if not gen[y] <= gen[x]: gen[x] |= gen[y]; chg = True
    return {y[0] for w in K for y in gen[(w,)]}

# ------------------------------------------------------------------ [2] combinatorics ----
def words_upto(alph, n, start=0):
    for k in range(start, n + 1):
        for p in itertools.product(alph, repeat=k): yield "".join(p)
def section2():
    print("[2] Lemma Q step: y s w = w s y and y s w y = w y s y imply y s = s y  (exhaustive, {a,b})")
    both = bad = 0
    for y in words_upto("ab", 3, 1):
        for s in words_upto("ab", 3):
            for w in words_upto("ab", 4, 1):
                if y + s + w == w + s + y and y + s + w + y == w + y + s + y:
                    both += 1; bad += (y + s != s + y)
    print(f"    triples with both equations: {both}; with ys != sy: {bad}")
    # Lemma E, fan-out 2: swap equation W=o[x,x']=o[x',x]; equal first-component lengths force x=x'
    pats = {"S": (0, 0, 1, 1), "C": (0, 1, 0, 1), "N": (0, 1, 1, 0)}
    print("    Lemma E (fan-out 2): solutions of o[x,x'] = o[x',x] with x != x', |x|=|x'|<=4, gaps in {'',c}")
    for name, pat in pats.items():
        same_len = shifted = 0; ex = None
        tup = [(u, v) for u in words_upto("ab", 3, 1) for v in words_upto("ab", 3, 1) if len(u + v) <= 4]
        for x in tup:
            for xp in tup:
                if x == xp or len(x[0] + x[1]) != len(xp[0] + xp[1]): continue
                for gaps in itertools.product(["", "c"], repeat=3):
                    def fillp(A, B):
                        it = {0: iter(A), 1: iter(B)}; out = ""
                        for k, who in enumerate(pat):
                            out += next(it[who]) + (gaps[k] if k < 3 else "")
                        return out
                    if fillp(x, xp) == fillp(xp, x):
                        if len(x[0]) == len(xp[0]): same_len += 1
                        else:
                            shifted += 1
                            if ex is None or (sorted(x[0]+x[1]) != sorted(xp[0]+xp[1]) and sorted(ex[0][0]+ex[0][1]) == sorted(ex[1][0]+ex[1][1])): ex = (x, xp, gaps)
        print(f"      pattern {name}: equal first lengths: {same_len} (Lemma E(b) says 0); shifted solutions: {shifted}; e.g. {ex}")

# ------------------------------------------------------------------ [3] Lemma Q on doubling ----
def doubling(n, br=("b", "", "b"), cbr=(("c", "c"),)):
    fan = {"S": 1, "E0": 1}; rules = [("S", [f"E{n}"], [[(0, 0)]]), ("E0", [], [["a"]])]
    for i in range(1, n + 1):
        fan[f"E{i}"] = 1; l, m, r = br
        rules.append((f"E{i}", [f"E{i-1}"] * 2, [list(l) + [(0, 0)] + list(m) + [(1, 0)] + list(r)]))
        for cl, cr in cbr: rules.append((f"E{i}", [f"E{i-1}"], [list(cl) + [(0, 0)] + list(cr)]))
    return MCFG(fan, rules)
def Wn(n): return "a" if n == 0 else "b" + Wn(n - 1) * 2 + "b"
def lemmaQ_sites(W, y, maxs=6):
    """factorisations W = wL . yy s . w . yy . wR with w != '', s != '', c(s) <= c(y), yy s yy a factor of W."""
    out = []; n = len(W); ly = len(y)
    for i in range(n):
        if W[i:i + 2 * ly] != y + y: continue
        for ls in range(1, maxs + 1):
            s = W[i + 2 * ly:i + 2 * ly + ls]
            if len(s) < ls or not set(s) <= set(y): break
            if (y + y + s + y + y) not in W: continue
            st = i + 2 * ly + ls
            for j in range(st + 1, n - 2 * ly + 1):
                if W[j:j + 2 * ly] == y + y: out.append((i, s, j)); break
    return out
def section3():
    print("[3] Lemma Q on the doubling family (content typing): sites yy s yy ... w ... yy with c(s) <= c(y), sy != ys")
    for n in range(1, 7):
        W = Wn(n); msg = []
        for k in (0, 1, 2):
            y = Wn(k); sites = [(i, s, j) for i, s, j in lemmaQ_sites(W, y, maxs=8) if s + y != y + s]
            msg.append(f"y=W_{k}: {len(sites)}")
        print(f"    n={n}: |W_n|={len(W)}  " + "; ".join(msg))
    n = 4; L4 = doubling(n).words(100); W = Wn(n); y = Wn(1)
    i, s, j = [z for z in lemmaQ_sites(W, y, maxs=8) if z[1] + y != y + z[1]][0]
    wL = W[:i]; w = W[i + 2 * len(y) + len(s):j]; wR = W[j + len(y):]
    assert wL + y + y + s + w + y + wR == W
    Wp = wL + y + w + s + y + y + wR          # T1 with x1=y, t=ys, v=y, s'=sy, x2=y
    print(f"    n=4, y=W_1={y}, s={s}: origin yy s yy is a factor of W_4: {(y+y+s+y+y) in W}; |w|={len(w)}")
    print(f"    W'={Wp}\n      same Parikh as W_4: {sorted(Wp)==sorted(W)}; W'==W_4: {Wp==W}; W' in L_4: {Wp in L4}  (|L_4|={len(L4)})")
    X, Y = (y + y + s, y), (y, s + y + y); Ec = (wL, w, wR)
    print(f"    certificate: X=(yys,y), Y=(y,syy) share the context (W[:i], y, rest) in W_4; context (wL,w,wR) accepts X: {fill(Ec,X) in L4}, Y: {fill(Ec,Y) in L4}")

# ------------------------------------------------------------------ [4] hand-made candidates ----
def gfam(n, base, dbl, wraps):
    fan = {"S": 1, "E0": 1}; rules = [("S", [f"E{n}"], [[(0, 0)]]), ("E0", [], [list(base)])]
    for i in range(1, n + 1):
        fan[f"E{i}"] = 1; p = f"E{i-1}"; l, m, r = dbl
        rules.append((f"E{i}", [p, p], [list(l) + [(0, 0)] + list(m) + [(1, 0)] + list(r)]))
        for cl, cr in wraps: rules.append((f"E{i}", [p], [list(cl) + [(0, 0)] + list(cr)]))
    return MCFG(fan, rules)
X1, X2, Y1, Y2 = (0, 0), (0, 1), (1, 0), (1, 1)
def pairfam(n, comb, short, base=("ab", "ab"), top=((X1, "a", "b", X2),)):
    fan = {"S": 1}; rules = [("S", [f"P{n}"], [list(c) for c in top]), ("P0", [], [list(base[0]), list(base[1])])]
    for k in range(n + 1): fan[f"P{k}"] = 2
    for k in range(1, n + 1):
        p = f"P{k-1}"
        for c in comb: rules.append((f"P{k}", [p, p], c))
        for s in short: rules.append((f"P{k}", [p] if any(isinstance(z, tuple) for comp in s for z in comp) else [], s))
    return MCFG(fan, rules)
FOUR = [[[X1, Y1], [Y2, X2]], [[X1, Y1], [X2, Y2]], [[X1, Y1, X2], [Y2]], [[X1], [Y1, X2, Y2]]]
def fam149(n):
    fan = {"S": 1, "E0": 1}; rules = [("S", [f"E{n}"], [[(0, 0)]]), ("E0", [], [["a", "b"]])]
    for i in range(1, n + 1):
        fan[f"E{i}"] = 1; p = f"E{i-1}"
        rules += [(f"E{i}", [p, p], [[(0, 0), (1, 0)]]), (f"E{i}", [], [["a"] * i + ["c", "b"]])]
    return MCFG(fan, rules)
HAND = [
 ("Z   E->EE|a^i cb, E0=ab (reconstruction of README (149) type, (i))", "ab", fam149),
 ("C0  E->bEEb|cEc, E0=a (doubling)", "ab", lambda n: doubling(n)),
 ("P1  E->EE|cEc, E0=ab (i)", "ab", lambda n: gfam(n, "ab", ("", "", ""), [("c", "c")])),
 ("P3  E->EE|cEc|dEd, E0=ab (i)", "ab", lambda n: gfam(n, "ab", ("", "", ""), [("c", "c"), ("d", "d")])),
 ("Q1  E->abEEab|cEc, E0=ab (i)", "ab", lambda n: gfam(n, "ab", ("ab", "", "ab"), [("c", "c")])),
 ("Q4  E->abEabEab|cEc (i)", "ab", lambda n: gfam(n, "ab", ("ab", "ab", "ab"), [("c", "c")])),
 ("Q7  E->aEEb|cEc, E0=ab", "ab", lambda n: gfam(n, "ab", ("a", "", "b"), [("c", "c")])),
 ("V1  P->(x1y1,y2x2)|(c,c), S->x1 ab x2 (i)", "ab", lambda n: pairfam(n, FOUR[:1], [[["c"], ["c"]]])),
 ("V8  P->4 combos|(c,c), S->x1 ab x2 (i, slide-closed)", "ab", lambda n: pairfam(n, FOUR, [[["c"], ["c"]]])),
 ("V9  P->4 combos|(cx1,x2c) (i)", "ab", lambda n: pairfam(n, FOUR, [[["c", X1], [X2, "c"]]])),
 ("A1  P->(x1y1,y2x2)|(cx1,x2c), P0=(a,b), S->x1 a x2 (ii)", "ab", lambda n: pairfam(n, FOUR[:1], [[["c", X1], [X2, "c"]]], ("a", "b"), ((X1, "a", X2),))),
 ("A2  P->(x1y1,y2x2)|(c,c), P0=(a,b) (ii)", "ab", lambda n: pairfam(n, FOUR[:1], [[["c"], ["c"]]], ("a", "b"), ((X1, "a", X2),))),
 ("A5  P->(ax1y1,y2x2b)|(cx1,x2c), P0=(a,b) (ii)", "ab", lambda n: pairfam(n, [[["a", X1, Y1], [Y2, X2, "b"]]], [[["c", X1], [X2, "c"]]], ("a", "b"), ((X1, "b", X2),))),
 ("A7  P->(x1y1,y2x2)|(cx1,x2c), P0=(ab,ab) (i)", "ab", lambda n: pairfam(n, FOUR[:1], [[["c", X1], [X2, "c"]]])),
]
def section4():
    print("[4] Task 3, hand-made candidates: n<=3, exhaustive d<=2 (skipped if a word is longer than 34)")
    for name, M, mk in HAND:
        for n in (1, 2, 3):
            G = mk(n); G.check_good(); L = G.words(80); ml = max(map(len, L))
            if ml > 34: print(f"    {name} n={n}: skipped (max length {ml})"); break
            cf = [w for w in L if set(w) <= set(M)]; th = max(1, G.theta()); mu = G.mu(M)
            out = set("".join(L)) - set(M); kap = max(sum(w.count(o) for o in out) for w in L); bet = max(blocks(w, out) for w in L)
            r = smallest_violation(L)
            head = f"    {name} n={n}: ||G||={G.size()} th={th} mu={mu} kappa={kap} beta={bet} rigid={len(set(len(w) for w in cf))==len(cf)} :: "
            if r is None: print(head + "PASS"); continue
            d, x, y, E, E2, same = r
            print(head + f"FAIL d={d} {x}~{y} shared {E} [{'same word' if same else 'two words'}] dist {E2}"); break

# ------------------------------------------------------------------ [5] random families ----
def tmpl(ch_fans, d, terms):
    seqs = [[(i, j) for j in range(f)] for i, f in enumerate(ch_fans)]; merged = []; idx = [0] * len(seqs)
    while any(idx[i] < len(seqs[i]) for i in range(len(seqs))):
        i = random.choice([i for i in range(len(seqs)) if idx[i] < len(seqs[i])]); merged.append(seqs[i][idx[i]]); idx[i] += 1
    for t in terms: merged.insert(random.randint(0, len(merged)), t)
    if len(merged) < d: return None
    cuts = sorted(random.sample(range(1, len(merged)), d - 1)) if d > 1 else []
    comps, prev = [], 0
    for c in cuts + [len(merged)]: comps.append(merged[prev:c]); prev = c
    for c in comps:
        for a, b in zip(c, c[1:]):
            if isinstance(a, tuple) and isinstance(b, tuple) and a[0] == b[0] and b[1] == a[1] + 1: return None
    return comps
def spec(M, OUT):
    f = random.choice([1, 2])
    base = ["".join(random.choice(M) for _ in range(random.randint(1, 2))) for _ in range(f)]
    if len(M) > 1 and set("".join(base)) != set(M) and random.random() < 0.5: base[0] = M
    d = tmpl([f, f], f, [random.choice(M) for _ in range(random.randint(0, 2))])
    sh = []
    for _ in range(random.randint(1, 2)):
        if random.random() < 0.75: t = tmpl([f], f, [random.choice(OUT) for _ in range(random.randint(1, 2))] + [random.choice(M) for _ in range(random.randint(0, 1))])
        else: t = tmpl([], f, [random.choice(OUT) for _ in range(f)])
        if t: sh.append(t)
    top = tmpl([f], 1, [random.choice(M) for _ in range(1 if f == 2 else random.randint(0, 1))])
    if not d or not sh or not top: return None
    return f, base, [d], sh, top
def build(sp, n):
    f, base, dbl, sh, top = sp
    fan = {"S": 1}; rules = [("S", [f"E{n}"], top), ("E0", [], [list(b) for b in base])]
    for i in range(n + 1): fan[f"E{i}"] = f
    for i in range(1, n + 1):
        p = f"E{i-1}"
        for t in dbl: rules.append((f"E{i}", [p, p], t))
        for t in sh: rules.append((f"E{i}", [p] if any(isinstance(z, tuple) for c in t for z in c) else [], t))
    return MCFG(fan, rules)
def show(sp):
    f, base, dbl, sh, top = sp
    T = lambda t: "(" + ",".join("".join(z if isinstance(z, str) else "xy"[z[0]] + str(z[1] + 1) for z in c) for c in t) + ")"
    return f"f={f} E0={tuple(base)} dbl={[T(t) for t in dbl]} short={[T(t) for t in sh]} S={T(top)}"
def classify(L):
    r = smallest_violation(L)
    if r is None: return "PASS"
    return f"d={r[0]}" + ("" if r[0] == 1 else (" same-word" if r[5] else " two-word"))
def section5(M, OUT, nspec):
    print(f"[5] Task 3, random doubling-type families, M={{{','.join(M)}}}, outside letters {set(OUT)}: {nspec} random specifications")
    print("    filter: good; n=2 language has max length <= 24; exactly one M-word of each length at n=2 (rigid);"
          " mu_M(n=2) >= 1.6 mu_M(n=1)")
    stats = {}; surv = {}; kept = 0
    for _ in range(nspec):
        sp = spec(M, OUT)
        if not sp: continue
        try:
            G1 = build(sp, 1); G1.check_good(); G2 = build(sp, 2); G2.check_good()
        except AssertionError: continue
        L1 = G1.words(60); L2 = G2.words(60)
        if not L2 or max(map(len, L2)) > 24: continue
        cf = [w for w in L2 if set(w) <= set(M)]; m1 = G1.mu(M); m2 = G2.mu(M)
        if len(set(map(len, cf))) != len(cf) or m1 == INF or m2 < 1.6 * m1: continue
        kept += 1; k1 = classify(L1)
        key = f"f={sp[0]} " + ("n=1 " + k1 if k1 != "PASS" else "n=2 " + classify(L2))
        stats[key] = stats.get(key, 0) + 1
        if key.endswith("n=2 PASS"): surv[show(sp)] = sp
    print(f"    kept {kept}; first failure: " + ", ".join(f"{k}: {v}" for k, v in sorted(stats.items())))
    st3 = {}; ex = {}
    for k, sp in surv.items():
        G3 = build(sp, 3); L3 = G3.words(200); ml = max(map(len, L3))
        if ml <= 30: k3 = classify(L3)
        else:
            v = violations(L3, 1, limit=1); c = None if v else t1_certificate(L3)
            k3 = "d=1" if v else ("T1-certificate" if c else "NO FAILURE FOUND")
        st3[k3] = st3.get(k3, 0) + 1; ex.setdefault(k3, k)
    print(f"    distinct n=2 survivors: {len(surv)}; at n=3: " + ", ".join(f"{k}: {v}" for k, v in sorted(st3.items())))
    for k3, k in sorted(ex.items()): print(f"      e.g. [{k3}] {k}")

# ------------------------------------------------------------------ [6] (Hyp^inf) light ----
def section6(ntargets=1500):
    print(f"[6] Task 4 (light): fixpoint K^inf of K -> L(B^(<=2)_(2,c)(K)) on random finite targets in C_2,c ({ntargets} targets)")
    W = lambda s, n: {"".join(p) for p in itertools.product(s, repeat=n)}
    nL = nK = nfail = nfix = 0; t = time.time()
    while nL < ntargets:
        sig = random.choice(["ab", "abc"]); ln = random.randint(2, 4 if sig == "ab" else 3)
        pool = sorted(W(sig, ln) | W(sig, ln - 1))
        L = set(random.sample(pool, min(random.randint(3, 7), len(pool))))
        if not in_class(L)[0]: continue
        nL += 1; N = max(map(len, L))
        for k in range(1, len(L)):
            for K in itertools.combinations(sorted(L), k):
                nK += 1; cur = B_lang(set(K), N); nfail += not in_class(cur)[0]
                while True:
                    nxt = B_lang(cur, N)
                    if nxt == cur: break
                    cur = nxt
                nfix += not in_class(cur)[0]
    print(f"    targets {nL}, samples K {nK}: L(B(K)) not in class {nfail}; fixpoint not in class {nfix}")

if __name__ == "__main__":
    for sec in (section2, section3, section4, lambda: section5("ab", "c", 30000), lambda: section5("a", "bc", 10000), section6):
        sec(); print(f"    ({time.time()-T0:.0f}s)\n", flush=True)
