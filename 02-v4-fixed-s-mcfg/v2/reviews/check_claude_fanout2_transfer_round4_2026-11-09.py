#!/usr/bin/env python3
r"""check_claude_fanout2_transfer_round4_2026-11-09.py

Round 4 of the op:fanout-two exploration (paper #2). Standard library only, seed 20261109.
Everything printed is an OBSERVATION (computation).  Substitutability checks on FINITE
languages are exhaustive (all d<=2 occurrences); for infinite languages nothing here is a
membership proof.  A printed violation certificate (x, y, shared context, distinguishing
context) is a genuine disproof of membership, because all words involved are decided exactly.

Sections
 [1] MCFG utilities (goodness, ||G||, exact theta, mu_M, kappa) and exhaustive d<=2 check.
 [2] Lemma T0: every same-word sharing of two 2-tuples is a conjugate shift (random words).
 [3] Doubling family L_n (Prop 7.1) under the content typing: membership n=1,2; first
     violation n=3; explicit move W_3 -> W_3' (power transfer at n=3); self-sharings in W_n.
 [4] Theorem M_beta (block number) on L_n and on random finite grammars.
 [5] Task 3: candidate families, n<=3 exhaustive, n=4 d=1 exhaustive + T1-certificate search.
 [6] Task 4: (Hyp) for B^{<=2}_{2,c}: counterexamples, h(L) vs shortest characteristic sample,
     iterated operator B^infinity.
"""
import itertools, random, time
random.seed(20261109)
INF = float("inf")
T0 = time.time()

# ------------------------------------------------------------------ [1] utilities ----
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

# ------------------------------------------------------------------ [2] Lemma T0 ----
def section2():
    print("[2] Lemma T0: same-word sharings of 2-occurrences are conjugate shifts")
    n_pairs = bad = 0
    for _ in range(300):
        w = "".join(random.choice("abc") for _ in range(random.randint(4, 11)))
        byE = {}
        for x, E in occ(w, 2): byE.setdefault(E, []).append(x)
        for E, xs in byE.items():
            for x, y in itertools.combinations(xs, 2):
                n_pairs += 1
                if len(x[0]) > len(y[0]): x, y = y, x
                pi = len(y[0]) - len(x[0]); t = y[0][len(x[0]):]; s = x[1][:pi]; v = E[1]
                ok = pi > 0 and y[0] == x[0] + t and x[1] == s + y[1] and t + v == v + s
                bad += not ok
    print(f"    random words: sharing pairs={n_pairs}, not of the form (x1 t, x2)/(x1, s x2) with tv=vs: {bad}")

# ------------------------------------------------------------------ [3] doubling family ----
def doubling(n, br=lambda i: ("b", "", "b"), cbr=lambda i: [("c", "c")]):
    fan = {"S": 1, "E0": 1}; rules = [("S", [f"E{n}"], [[(0, 0)]]), ("E0", [], [["a"]])]
    for i in range(1, n + 1):
        fan[f"E{i}"] = 1; l, m, r = br(i)
        rules.append((f"E{i}", [f"E{i-1}"] * 2, [list(l) + [(0, 0)] + list(m) + [(1, 0)] + list(r)]))
        for cl, cr in cbr(i): rules.append((f"E{i}", [f"E{i-1}"], [list(cl) + [(0, 0)] + list(cr)]))
    return MCFG(fan, rules)
def Wn(n): return "a" if n == 0 else "b" + Wn(n - 1) * 2 + "b"
def section3():
    print("[3] Doubling family L_n, content typing c_{a,b,c}")
    for n in (1, 2, 3):
        L = doubling(n).words(100)
        ok, v = in_class(L)
        print(f"    n={n}: |L|={len(L)}  in C_2,c (exhaustive): {ok}" + ("" if ok else f"   first violation found: d={v[0]} {v[1]} ~ {v[2]}"))
    L3 = doubling(3).words(100); W3 = Wn(3)
    d, x, y, E, E2, same = smallest_violation(L3)
    print(f"    smallest violation at n=3: {x} ~ {y}, shared {E} ({'same word' if same else 'two words'}), distinguishing {E2}")
    shared = ("bbbaabbaa", "b", "aabbaabbb"); dist = ("bb", W3[3:19], "b")
    W3p = fill(dist, ("bb", "b"))
    print(f"    explicit: (b,bb),(bb,b) share {shared} -> {fill(shared,('b','bb'))} (=W_3: {fill(shared,('b','bb'))==W3})")
    print(f"    context {dist}: (b,bb) -> W_3 in L_3; (bb,b) -> W_3' = {W3p}; same Parikh vector: {sorted(W3p)==sorted(W3)}; W_3' in L_3: {W3p in L3}")
    for n in (2, 3, 4):
        w = Wn(n); byE = {}; per = {}
        for xx, EE in occ(w, 2): byE.setdefault(EE, []).append(xx)
        for EE, xs in byE.items():
            for a, b in itertools.combinations(xs, 2):
                if ctype(a) == ctype(b):
                    pi = abs(len(a[0]) - len(b[0])); per[pi] = per.get(pi, 0) + 1
        print(f"    W_{n} (|W|={len(w)}): same-type same-word sharings = {sum(per.values())}; by period pi: "
              + ", ".join(f"{k}:{per[k]}" for k in sorted(per)[:8]) + (" ..." if len(per) > 8 else ""))

# ------------------------------------------------------------------ [4] Theorem M_beta ----
def blocks(w, out):
    b = 0; prev = False
    for ch in w:
        cur = ch in out
        if cur and not prev: b += 1
        prev = cur
    return b
def bound_beta(G, M, kappa, beta, th):
    return (2 * len(M) - 1 + min(kappa, 2 * beta)) * len(G.V) * (G.rho_max() + G.rank() * th)
def rand_template(ch_fans, d, sigma):
    seqs = [[(i, j) for j in range(f)] for i, f in enumerate(ch_fans)]; merged = []; idx = [0] * len(seqs)
    while any(idx[i] < len(seqs[i]) for i in range(len(seqs))):
        i = random.choice([i for i in range(len(seqs)) if idx[i] < len(seqs[i])]); merged.append(seqs[i][idx[i]]); idx[i] += 1
    for _ in range(random.randint(0 if merged else 1, 2)): merged.insert(random.randint(0, len(merged)), random.choice(sigma))
    if len(merged) < d: return None
    cuts = sorted(random.sample(range(1, len(merged)), d - 1)) if d > 1 else []
    comps, prev = [], 0
    for c in cuts + [len(merged)]: comps.append(merged[prev:c]); prev = c
    for c in comps:
        for a, b in zip(c, c[1:]):
            if isinstance(a, tuple) and isinstance(b, tuple) and a[0] == b[0] and b[1] == a[1] + 1: return None
    return comps
def section4():
    print("[4] Theorem M_beta: mu_M <= (2|M|-1+min(kappa,2 beta)) |V| (rho_max + r theta_bar)")
    for n in range(1, 5):
        G = doubling(n); L = G.words(200); th = max(1, G.theta())
        kap = max(w.count("c") for w in L); bet = max(blocks(w, "c") for w in L); mu = G.mu("ab")
        print(f"    L_{n}: mu_ab={mu} kappa_c={kap} beta_c={bet} bound={bound_beta(G,'ab',kap,bet,th)} ok={mu<=bound_beta(G,'ab',kap,bet,th)}")
    # random acyclic (finite-language) grammars: exact kappa, beta, mu by enumeration
    tested = viol = 0; maxr = 0
    for _ in range(3000):
        nts = ["S", "A", "B", "C"]; fan = {X: (1 if X == "S" else random.choice([1, 2])) for X in nts}
        rules = []
        for k, l in enumerate(nts):            # acyclic: children have larger index
            for _ in range(random.randint(1, 3)):
                r = random.choice([0, 1, 2]) if k < 3 else 0
                ch = [random.choice(nts[k + 1:]) for _ in range(r)]
                t = rand_template([fan[B] for B in ch], fan[l], "abc")
                if t: rules.append((l, ch, t))
        G = MCFG(fan, rules)
        lam = G.lam(); prod = {A for A in G.V if lam[A] < INF}
        if "S" not in prod: continue
        G = MCFG({A: fan[A] for A in prod}, [r for r in rules if r[0] in prod and all(B in prod for B in r[1])])
        reach = {"S"}; chg = True
        while chg:
            chg = False
            for l, ch, t in G.rules:
                if l in reach and not set(ch) <= reach: reach |= set(ch); chg = True
        G = MCFG({A: fan[A] for A in reach}, [r for r in G.rules if r[0] in reach])
        try: G.check_good()
        except AssertionError: continue
        L = G.words(60); th = max(1, G.theta())
        for k in (1, 2):
            for M in itertools.combinations("abc", k):
                cand = [len(w) for w in L if set(w) == set(M)]
                if not cand: continue
                out = set("abc") - set(M)
                kap = max(sum(w.count(o) for o in out) for w in L); bet = max(blocks(w, out) for w in L)
                tested += 1; b = bound_beta(G, M, kap, bet, th); m = min(cand)
                viol += m > b; maxr = max(maxr, m / b)
    print(f"    random finite good grammars (fan-out<=2, rank<=2): instances={tested} violations={viol} max mu/bound={maxr:.3f}")

# ------------------------------------------------------------------ [5] candidates ----
def pair_family(n, kind):
    fan = {"S": 1}; rules = [("S", [f"A{n}"], [[(0, 0), "a", (0, 1)]]), ("A0", [], [["a"], ["b"]])]
    for i in range(n + 1): fan[f"A{i}"] = 2
    for i in range(1, n + 1):
        p = f"A{i-1}"; A = f"A{i}"
        if kind == "K2": rules += [(A, [p, p], [[(0, 0), (1, 0)], [(1, 1), (0, 1)]]), (A, [p], [["c", (0, 0)], [(0, 1), "c"]])]
        if kind == "K3": rules += [(A, [p, p], [["b", (0, 0), (1, 0)], [(1, 1), (0, 1), "b"]]), (A, [p], [["c", (0, 0)], [(0, 1), "c"]])]
        if kind == "K5": rules += [(A, [p, p], [[(0, 0), "b", (1, 0)], [(1, 1), "b", (0, 1)]]), (A, [p], [["c", (0, 0), "c"], [(0, 1)]]), (A, [p], [[(0, 0)], ["c", (0, 1), "c"]])]
        if kind == "K7": rules += [(A, [p, p], [[(0, 0), (1, 0)], [(1, 1), (0, 1)]]), (A, [p], [[(0, 0), "c", (0, 1)], ["b"]])]
    return MCFG(fan, rules)
def thue(n):
    fan = {"S": 1, "X0": 1, "Y0": 1}; rules = [("S", [f"X{n}"], [[(0, 0)]]), ("X0", [], [["a"]]), ("Y0", [], [["b"]])]
    for i in range(1, n + 1):
        fan[f"X{i}"] = fan[f"Y{i}"] = 1; X, Y = f"X{i-1}", f"Y{i-1}"
        rules += [(f"X{i}", [X, Y], [[(0, 0), (1, 0)]]), (f"X{i}", [X], [["c", (0, 0), "c"]])]
        if i < n: rules += [(f"Y{i}", [Y, X], [[(0, 0), (1, 0)]]), (f"Y{i}", [Y], [["c", (0, 0), "c"]])]
    if n >= 1: fan.pop(f"Y{n}", None)
    return MCFG(fan, rules)
def br5(i): return ("b", "d", "b") if i == 1 else (("d", "a", "d") if i % 2 == 0 else ("b", "a", "b"))
CANDS = [
 ("C0 E->bEEb|cEc (fan-out-1 family)", "ab", lambda n: doubling(n)),
 ("C2 E->bEaEb|cEc", "ab", lambda n: doubling(n, br=lambda i: ("b", "a", "b"))),
 ("C3 E->bE a^i Eb|cEc (level separators)", "ab", lambda n: doubling(n, br=lambda i: ("b", "a" * i, "b"))),
 ("C4 c-branch odd / d-branch even (4 letters)", "ab", lambda n: doubling(n, cbr=lambda i: [("c", "c")] if i % 2 else [("d", "d")])),
 ("C4' E->bEEb|cEd", "ab", lambda n: doubling(n, cbr=lambda i: [("c", "d")])),
 ("C6 Thue-Morse X->XY|cXc, Y->YX|cYc", "ab", thue),
 ("K2 (x1y1,y2x2)|(cx1,x2c)", "ab", lambda n: pair_family(n, "K2")),
 ("K3 (bx1y1,y2x2b)|(cx1,x2c)", "ab", lambda n: pair_family(n, "K3")),
 ("K5 (x1by1,y2bx2)|(cx1c,x2)|(x1,cx2c)", "ab", lambda n: pair_family(n, "K5")),
 ("K7 c between components (x1cx2,b)", "ab", lambda n: pair_family(n, "K7")),
 ("D1 brackets (b,d,b)/(d,b,d), cEc", "abd", lambda n: doubling(n, br=lambda i: ("b", "d", "b") if i % 2 else ("d", "b", "d"))),
 ("D5' letter-square-free M-words, cEc", "abd", lambda n: doubling(n, br=br5)),
 ("D5'' no letter squares at all, c/e branches", "abd", lambda n: doubling(n, br=br5, cbr=lambda i: [("c", "c")] if i % 2 else [("e", "e")])),
]
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
def section5():
    print("[5] Candidate families (Task 3).  n<=3: exhaustive d<=2;  n=4: exhaustive d=1 + T1-certificate search")
    for name, M, mk in CANDS:
        for n in (1, 2, 3, 4):
            G = mk(n); G.check_good(); L = G.words(400); ml = max(map(len, L))
            th = max(1, G.theta()); mu = G.mu(M); sig = set("".join(L)); out = sig - set(M)
            kap = max(sum(w.count(o) for o in out) for w in L); bet = max(blocks(w, out) for w in L)
            head = f"    {name} n={n}: ||G||={G.size()} th={th} mu={mu} kappa={kap} beta={bet} |L|={len(L)} :: "
            if ml <= 34:
                r = smallest_violation(L)
                if r is None: print(head + "PASS (exhaustive d<=2)"); continue
                d, x, y, E, E2, same = r
                print(head + f"FAIL d={d} {x}~{y} shared {E} [{'same word' if same else 'two words'}]")
                break
            v1 = violations(L, 1, limit=1)
            if v1: print(head + f"FAIL d=1 {v1[0][0]}~{v1[0][1]}"); break
            c = t1_certificate(L)
            print(head + ("d=1 PASS; T1-certificate FAIL " + f"{c[0]}~{c[1]} shared {c[2]}" if c else "d=1 PASS; no T1-certificate found"))
            if c: break

# ------------------------------------------------------------------ [6] (Hyp) ----
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
def section6():
    print("[6] Task 4: (Hyp) for B^{<=2}_{2,c}; target L finite, so L(B(K)) <= L is computed exactly")
    W = lambda s, n: {"".join(p) for p in itertools.product(s, repeat=n)}
    L1 = W("ab", 3) - {"aaa", "bbb"}; K1 = {"aab", "aba", "abb"}
    S1 = B_lang(K1, 3)
    print(f"    L={sorted(L1)} in C_2,c: {in_class(L1)[0]};  K={sorted(K1)};  L(B(K))={sorted(S1)}")
    print(f"      L(B(K)) in C_2,c: {in_class(S1)[0]}  (violation {in_class(S1)[1]});  uniform rank: same set: {B_lang(K1,3,rmax=3)==S1}")
    def analyse(name, L):
        Ls = sorted(L); N = max(map(len, L))
        subs = [frozenset(c) for k in range(1, len(Ls)) for c in itertools.combinations(Ls, k)]
        FL = [L - S for S in subs if in_class(S)[0]] + [frozenset(L)]
        h = min(sum(map(len, F)) for k in range(1, len(Ls) + 1) for F in itertools.combinations(Ls, k) if all(set(F) & X for X in FL))
        char = None; hit_not_char = 0; nfail = 0; nfix_fail = 0
        for k in range(1, len(Ls) + 1):
            for F in itertools.combinations(Ls, k):
                LK = B_lang(set(F), N)
                if not in_class(LK)[0]: nfail += 1
                cur = LK                                   # iterate B to a fixpoint
                while True:
                    nxt = B_lang(cur, N)
                    if nxt == cur: break
                    cur = nxt
                nfix_fail += not in_class(cur)[0]
                if LK == set(L):
                    char = min(char or INF, sum(map(len, F)))
                elif all(set(F) & X for X in FL): hit_not_char += 1
        print(f"    {name}: |L|={len(L)} K tested={2**len(L)-1}: L(B(K)) not in class={nfail}; B^inf fixpoint not in class={nfix_fail};"
              f" h(L)={h}; shortest characteristic sample={char}; hitting-but-not-characteristic={hit_not_char}")
    analyse("{a,b}^3\\{aaa,bbb}", L1)
    analyse("{a,b}^3", W("ab", 3))
    analyse("{w in {a,b}^4 : |w|_a=2}", {w for w in W("ab", 4) if w.count("a") == 2})
    L2 = {w for w in W("ab", 4) if w.count("a") == 2}
    print(f"    {{aabb,abab}}: L(B)={sorted(B_lang({'aabb','abab'},4))};  uniform rank 4: {sorted(B_lang({'aabb','abab'},4,rmax=4))}")
    # random finite targets
    nL = nK = nbad = 0; t = time.time()
    while nL < 150 and time.time() - t < 60:
        sig = random.choice(["ab", "abc"]); ln = random.randint(2, 5 if sig == "ab" else 4)
        pool = [w for w in W(sig, ln) | W(sig, ln - 1)]
        L = set(random.sample(pool, min(random.randint(2, 7), len(pool))))
        if not in_class(L)[0]: continue
        nL += 1
        for k in range(1, len(L) + 1):
            for K in itertools.combinations(sorted(L), k):
                nK += 1; nbad += not in_class(B_lang(set(K), max(map(len, L))))[0]
    print(f"    random finite targets in C_2,c: {nL}, subsets K: {nK}, L(B(K)) not in class: {nbad}")

if __name__ == "__main__":
    for sec in (section2, section3, section4, section5, section6):
        sec(); print(f"    ({time.time()-T0:.0f}s)\n", flush=True)
