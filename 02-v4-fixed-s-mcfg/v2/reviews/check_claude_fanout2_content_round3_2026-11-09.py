#!/usr/bin/env python3
r"""check_claude_fanout2_content_round3_2026-11-09.py

Round 3 of the op:fanout-two exploration (paper #2).  Standard library only.
Everything printed here is an OBSERVATION (bounded computation); nothing here
is a proof of class membership, except that the substitutability check on a
FINITE language is exhaustive (all occurrences of all tuples are enumerated).

Sections
  [1] MCFG utilities: goodness, ||G||, exact theta, lambda_M, mu_M (exact DP over
      (nonterminal, content)), kappa_{M-bar} (with infinity detection).
  [2] Claim M on the three-letter doubling family L_n (Prop. 7.1).
  [3] Claim M on random reduced good MCFGs (fan-out <= 2, rank <= 2), with
      exact mu_M and a brute-force cross-check by enumeration.
  [4] Theorem W (subword witness x content) on random grammars: brute-force
      min{|w| : w in L, u subword of w, c(w) subset M} vs. the bound.
  [5] Fan-out-two reordering under pump-down (why the factor (k+1)^(f-1)).
  [6] Exhaustive substitutability checks (content typing, d <= 2) on finite
      languages: {ab, b a^n} > {ab};  {aab, baa} > {aab};  Sigma^n \ {w}.
Seed fixed: 20261109.
"""
import itertools
import random
from math import comb

random.seed(20261109)
INF = float("inf")

# ---------------------------------------------------------------- [1] MCFG ----
# A rule: (lhs, children(list of nonterminals), template(tuple of components)).
# A component is a list of symbols; a terminal is a 1-char str, a variable is
# (i, j): component j of child i (0-based).


class MCFG:
    def __init__(self, fan, rules, start="S"):
        self.fan = dict(fan)
        self.rules = [(l, list(ch), tuple(tuple(c) for c in t)) for l, ch, t in rules]
        self.S = start
        self.V = sorted(self.fan)

    # ---- properties
    def check_good(self):
        for l, ch, t in self.rules:
            assert len(t) == self.fan[l], ("fan-out", l, t)
            assert all(len(c) > 0 for c in t), ("eps-free", l, t)
            occ = [s for c in t for s in c if isinstance(s, tuple)]
            need = [(i, j) for i, B in enumerate(ch) for j in range(self.fan[B])]
            assert sorted(occ) == sorted(need), ("nondeleting", l, t)
            for i, B in enumerate(ch):  # nonpermuting
                order = [s[1] for s in occ if s[0] == i]
                assert order == sorted(order), ("nonpermuting", l, t)
            for c in t:  # nonmerging
                for s1, s2 in zip(c, c[1:]):
                    if isinstance(s1, tuple) and isinstance(s2, tuple):
                        assert not (s1[0] == s2[0] and s2[1] == s1[1] + 1), ("nonmerging", l, t)
        return True

    def size(self):
        return len(self.V) + sum(1 + len(ch) + sum(len(c) for c in t) for l, ch, t in self.rules)

    def rank(self):
        return max(len(ch) for _, ch, _ in self.rules)

    def rho_max(self):
        return max(sum(1 for c in t for s in c if isinstance(s, str)) for _, _, t in self.rules)

    @staticmethod
    def terms(t):
        return [s for c in t for s in c if isinstance(s, str)]

    # ---- min-plus inside value restricted to rules whose terminals lie in M
    def lam(self, M=None):
        val = {A: INF for A in self.V}
        changed = True
        while changed:
            changed = False
            for l, ch, t in self.rules:
                tm = self.terms(t)
                if M is not None and any(a not in M for a in tm):
                    continue
                v = len(tm) + sum(val[B] for B in ch)
                if v < val[l]:
                    val[l] = v
                    changed = True
        return val

    def outside(self, lam):
        out = {A: INF for A in self.V}
        out[self.S] = 0
        changed = True
        while changed:
            changed = False
            for l, ch, t in self.rules:
                if out[l] == INF:
                    continue
                base = out[l] + len(self.terms(t)) + sum(lam[B] for B in ch)
                for i, B in enumerate(ch):
                    v = base - lam[B]
                    if v < out[B]:
                        out[B] = v
                        changed = True
        return out

    def theta(self):
        lam = self.lam()
        out = self.outside(lam)
        th = [out[l] + len(self.terms(t)) + sum(lam[B] for B in ch) for l, ch, t in self.rules]
        return max(th)

    def reduce(self):
        lam = self.lam()
        prod = {A for A in self.V if lam[A] < INF}
        rules = [r for r in self.rules if r[0] in prod and all(B in prod for B in r[1])]
        if self.S not in prod:
            return None
        reach = {self.S}
        changed = True
        while changed:
            changed = False
            for l, ch, t in rules:
                if l in reach:
                    for B in ch:
                        if B not in reach:
                            reach.add(B)
                            changed = True
        rules = [r for r in rules if r[0] in reach]
        fan = {A: self.fan[A] for A in reach}
        return MCFG(fan, rules, self.S)

    # ---- exact mu over contents: I[A][C] = least total length of a tuple of A with content C
    def content_table(self, sigma):
        subsets = [frozenset(c) for k in range(1, len(sigma) + 1) for c in itertools.combinations(sigma, k)]
        I = {A: {} for A in self.V}
        changed = True
        while changed:
            changed = False
            for l, ch, t in self.rules:
                base_c = frozenset(self.terms(t))
                base_l = len(self.terms(t))
                # combine children
                combos = [(base_c, base_l)]
                for B in ch:
                    new = {}
                    for c0, l0 in combos:
                        for c1, l1 in I[B].items():
                            c2 = c0 | c1
                            if l0 + l1 < new.get(c2, INF):
                                new[c2] = l0 + l1
                    combos = list(new.items())
                for c, ln in combos:
                    if ln < I[l].get(c, INF):
                        I[l][c] = ln
                        changed = True
        return I

    # ---- capacity of letters outside M: sup #outside over In(A), with infinity detection
    def cap(self, M):
        lam = self.lam()
        val = {A: (-INF if lam[A] == INF else 0) for A in self.V}
        nV = len(self.V)
        for rnd in range(2 * nV + 3):
            changed = set()
            for l, ch, t in self.rules:
                v = sum(1 for a in self.terms(t) if a not in M) + sum(val[B] for B in ch)
                if v > val[l]:
                    val[l] = v
                    changed.add(l)
            if not changed:
                return val
            if rnd >= nV + 1:
                for A in changed:
                    val[A] = INF
        # propagate infinity to fixpoint
        changed = True
        while changed:
            changed = False
            for l, ch, t in self.rules:
                if val[l] != INF and any(val[B] == INF for B in ch):
                    val[l] = INF
                    changed = True
        return val

    # ---- enumeration of all words of length <= N
    def words(self, N, cap_per_nt=20000):
        tup = {A: set() for A in self.V}
        changed = True
        while changed:
            changed = False
            for l, ch, t in self.rules:
                pools = [list(tup[B]) for B in ch]
                if any(len(p) == 0 for p in pools):
                    continue
                nt = len(self.terms(t))
                for combo in itertools.product(*pools):
                    if nt + sum(sum(len(c) for c in y) for y in combo) > N:
                        continue
                    res = tuple("".join(s if isinstance(s, str) else combo[s[0]][s[1]] for s in c) for c in t)
                    if res not in tup[l] and len(tup[l]) < cap_per_nt:
                        tup[l].add(res)
                        changed = True
        return {y[0] for y in tup[self.S]}


def content(w):
    return frozenset(w)


def claimM_bound(G, M, kappa, theta_bar):
    k = len(M)
    return (2 * k - 1 + kappa) * len(G.V) * (G.rho_max() + G.rank() * theta_bar)


def thmW_bound(G, k, kappa, theta_bar, f):
    return ((2 * k - 1) * comb(k + f - 1, f - 1) + kappa) * len(G.V) * (G.rho_max() + G.rank() * theta_bar)


# ---------------------------------------------------- [2] doubling family L_n ----
def doubling_family(n):
    fan = {"S": 1}
    rules = [("S", [f"E{n}"], [[(0, 0)]]), ("E0", [], [["a"]])]
    fan["E0"] = 1
    for i in range(1, n + 1):
        fan[f"E{i}"] = 1
        rules.append((f"E{i}", [f"E{i-1}", f"E{i-1}"], [["b", (0, 0), (1, 0), "b"]]))
        rules.append((f"E{i}", [f"E{i-1}"], [["c", (0, 0), "c"]]))
    return MCFG(fan, rules)


def section2():
    print("[2] Claim M on the three-letter doubling family L_n (Prop. 7.1), M = {a,b}")
    print("    n  ||G||  theta_bar  mu_ab        kappa_c     bound(ClaimM)  ok")
    for n in range(1, 9):
        G = doubling_family(n)
        G.check_good()
        th = max(1, G.theta())
        I = G.content_table("abc")
        mu = I["S"].get(frozenset("ab"), INF)
        kap = G.cap(set("ab"))["S"]
        bd = claimM_bound(G, "ab", kap, th)
        print(f"   {n:2d}  {G.size():5d}  {th:9d}  {mu:10}  {kap:10}  {bd:13}  {mu <= bd}")
    print("    (mu_ab = 3*2^n-2, kappa_c = 2^n: exponential kappa, as Claim M requires)")
    print("[2b] Claim M on L_{m,n} of Prop. 7.8 (two letters), M = {a}")
    print("    m n  ||G||  theta_bar  mu_a     kappa_b  bound   mu_a/theta_bar^2")
    for m, n in ((1, 1), (2, 2), (3, 3), (4, 4), (2, 5), (5, 2)):
        fan = {f"C{j}": 1 for j in range(m + 1)}
        fan.update({f"A{i}": 1 for i in range(n + 1)})
        rules = [("C0", [], [["a"]]), ("A0", [f"C{m}"], [[(0, 0)]]), ("A0", [], [["b"]])]
        rules += [(f"C{j}", [f"C{j-1}"] * 2, [[(0, 0), (1, 0)]]) for j in range(1, m + 1)]
        rules += [(f"A{i}", [f"A{i-1}"] * 2, [[(0, 0), (1, 0)]]) for i in range(1, n + 1)]
        G = MCFG(fan, rules, start=f"A{n}")
        G.check_good()
        th = max(1, G.theta())
        mu = G.content_table("ab")[f"A{n}"].get(frozenset("a"), INF)
        kap = G.cap({"a"})[f"A{n}"]
        bd = claimM_bound(G, "a", kap, th)
        print(f"    {m} {n}  {G.size():5d}  {th:9d}  {mu:7}  {kap:7}  {bd:7}  {mu/th**2:.3f}   ok={mu <= bd}")
    print("    (mu_a = 2^(m+n), kappa_b = 2^n, theta_bar = 2^m+2^n-1: quadratic mu through linear kappa)")


# ------------------------------------------------------- random grammars ----
def random_template(ch_fans, d, sigma, max_terms=2):
    seqs = [[(i, j) for j in range(f)] for i, f in enumerate(ch_fans)]
    merged = []
    idx = [0] * len(seqs)
    while any(idx[i] < len(seqs[i]) for i in range(len(seqs))):
        i = random.choice([i for i in range(len(seqs)) if idx[i] < len(seqs[i])])
        merged.append(seqs[i][idx[i]])
        idx[i] += 1
    for _ in range(random.randint(0 if merged else 1, max_terms)):
        merged.insert(random.randint(0, len(merged)), random.choice(sigma))
    if len(merged) < d:
        return None
    cuts = sorted(random.sample(range(1, len(merged)), d - 1)) if d > 1 else []
    comps, prev = [], 0
    for c in cuts + [len(merged)]:
        comps.append(merged[prev:c])
        prev = c
    for c in comps:
        for s1, s2 in zip(c, c[1:]):
            if isinstance(s1, tuple) and isinstance(s2, tuple) and s1[0] == s2[0] and s2[1] == s1[1] + 1:
                return None
    return comps


def random_grammar(sigma="abc", nts=("S", "A", "B", "C"), nrules=8):
    fan = {X: (1 if X == "S" else random.choice([1, 2])) for X in nts}
    rules = []
    tries = 0
    while len(rules) < nrules and tries < 500:
        tries += 1
        l = random.choice(nts)
        r = random.choice([0, 1, 1, 2])
        ch = [random.choice(nts[1:]) for _ in range(r)]
        t = random_template([fan[B] for B in ch], fan[l], sigma)
        if t is not None:
            rules.append((l, ch, t))
    G = MCFG(fan, rules).reduce()
    if G is None:
        return None
    G.check_good()
    return G


def is_subword(u, w):
    it = iter(w)
    return all(ch in it for ch in u)


def section3_4():
    print("[3] Claim M on random reduced good MCFGs (fan-out<=2, rank<=2, Sigma={a,b,c})")
    print("[4] Theorem W (subword witness u, content M) on the same grammars")
    sigma = "abc"
    n_g = n_tests = n_fin = n_viol = 0
    n_cross = n_cross_bad = 0
    maxratio = 0.0
    nW = nW_viol = 0
    maxratioW = 0.0
    N = 9
    for trial in range(1500):
        G = random_grammar()
        if G is None:
            continue
        n_g += 1
        th = max(1, G.theta())
        I = G.content_table(sigma)
        W = None
        if trial % 3 == 0:
            W = G.words(N)
        f = max(G.fan.values())
        for k in range(1, 4):
            for M in itertools.combinations(sigma, k):
                Ms = set(M)
                mu = I["S"].get(frozenset(M), INF)
                if mu == INF:
                    continue
                n_tests += 1
                kap = G.cap(Ms)["S"]
                if W is not None:
                    bf = min((len(w) for w in W if content(w) == frozenset(M)), default=INF)
                    if mu <= N or bf <= N:
                        n_cross += 1
                        if bf != mu:
                            n_cross_bad += 1
                if kap == INF:
                    continue
                n_fin += 1
                bd = claimM_bound(G, M, kap, th)
                if mu > bd:
                    n_viol += 1
                    print("   VIOLATION", G.rules, M, mu, bd)
                maxratio = max(maxratio, mu / bd)
                # Theorem W: witnesses u over M of length <= 3
                if W is not None:
                    for ku in range(1, 4):
                        for u in itertools.product(M, repeat=ku):
                            u = "".join(u)
                            cand = [len(w) for w in W if set(w) <= Ms and is_subword(u, w)]
                            if not cand:
                                continue
                            nW += 1
                            bw = thmW_bound(G, ku, kap, th, f)
                            m = min(cand)
                            if m > bw:
                                nW_viol += 1
                                print("   VIOLATION W", G.rules, u, M, m, bw)
                            maxratioW = max(maxratioW, m / bw)
    print(f"    grammars={n_g}  (grammar,M) pairs with mu_M finite={n_tests}  with kappa finite={n_fin}")
    print(f"    Claim M violations={n_viol}   max mu_M/bound={maxratio:.3f}")
    print(f"    exact DP vs enumeration (len<={N}): compared={n_cross}  mismatches={n_cross_bad}")
    print(f"    Theorem W: instances (found within len<={N})={nW}  violations={nW_viol}  max ratio={maxratioW:.3f}")


# ------------------------------------------- [5] reordering at fan-out two ----
def section5():
    print("[5] Pump-down at fan-out two can reorder marks (rule A(x1 c x2, d) <- A(x1,x2))")
    fan = {"S": 1, "A": 2}
    rules = [("S", ["A"], [[(0, 0), "e", (0, 1)]]),
             ("A", ["A"], [[(0, 0), "c", (0, 1)], ["d"]]),
             ("A", [], [["a"], ["b"]])]
    G = MCFG(fan, rules)
    G.check_good()
    big = "acb" + "e" + "d"      # S <- A <- A <- base : (a c b, d) then S: a c b e d
    small = "a" + "e" + "b"      # pump the upper A down to the lower A
    print(f"    word with two A-nodes: {big};  after replacing upper A-subtree by lower one: {small}")
    print(f"    in big: b before e ({big.index('b') < big.index('e')});  in small: b before e "
          f"({small.index('b') < small.index('e')})  -> order of marks b,e changed")
    print(f"    the lower A-yield (a,b): b sits in component 1 of the upper A but component 2 of the lower A")
    W = G.words(8)
    assert big in W and small in W


# -------------------------------------- [6] exhaustive substitutability ----
def occurrences(w, d):
    n = len(w)
    for cuts in itertools.combinations(range(n + 1), 2 * d):
        ok = all(cuts[2 * i] < cuts[2 * i + 1] for i in range(d))
        ok = ok and all(cuts[2 * i + 1] < cuts[2 * i + 2] for i in range(d - 1))  # v1..v_{d-1} nonempty
        if not ok:
            continue
        x = tuple(w[cuts[2 * i]:cuts[2 * i + 1]] for i in range(d))
        E = (w[:cuts[0]],) + tuple(w[cuts[2 * i + 1]:cuts[2 * i + 2]] for i in range(d - 1)) + (w[cuts[-1]:],)
        yield x, E


def substitutable(L, f=2):
    """exhaustive for finite L: content typing, all d <= f. Returns (True,None) or (False,witness)."""
    for d in range(1, f + 1):
        D = {}
        for w in L:
            for x, E in occurrences(w, d):
                D.setdefault(x, set()).add(E)
        bytype = {}
        for x in D:
            bytype.setdefault(tuple(frozenset(c) for c in x), []).append(x)
        for ty, xs in bytype.items():
            for x, y in itertools.combinations(xs, 2):
                if D[x] & D[y] and D[x] != D[y]:
                    E = next(iter(D[x] ^ D[y]))
                    return False, (d, x, y, E)
    return True, None


def section6():
    print("[6] Exhaustive content-typing substitutability (d<=2) on finite languages")
    for n in range(2, 7):
        L = {"ab", "b" + "a" * n}
        print(f"    n={n}: {{ab, ba^n}} in C_2,c: {substitutable(L)[0]};  {{ab}}: {substitutable({'ab'})[0]}"
              f";  min|L\\L'|={n+1};  mu_ab(L)=2")
    print(f"    {{aab,baa}}: {substitutable({'aab','baa'})[0]};  {{aab}}: {substitutable({'aab'})[0]}")
    for sig, n in (("ab", 3), ("ab", 4), ("abc", 3)):
        L = {"".join(p) for p in itertools.product(sig, repeat=n)}
        okL = substitutable(L)[0]
        dele = [w for w in sorted(L) if substitutable(L - {w})[0]]
        print(f"    Sigma={sig}, n={n}: Sigma^n in class: {okL};  w with Sigma^n\\{{w}} in class: {dele}")
    # an inclusion-chain check for the counting question: content-class deletions
    L = {"".join(p) for p in itertools.product("abc", repeat=3)}
    for M in ("ab", "abc"):
        X = {w for w in L if set(w) == set(M)}
        print(f"    Sigma=abc, n=3: Sigma^3 minus all words of content {{{','.join(M)}}} "
              f"({len(X)} words) in class: {substitutable(L - X)[0]}")


if __name__ == "__main__":
    section2()
    print()
    section3_4()
    print()
    section5()
    print()
    section6()
