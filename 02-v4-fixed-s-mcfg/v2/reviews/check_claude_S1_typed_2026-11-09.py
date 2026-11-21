#!/usr/bin/env python3
"""check_claude_S1_typed_2026-11-09.py  (standard library only)

Auxiliary checks for claude_S1_typed_2026-11-09.md.  Computation is not proof.

  (A) Counterexample to Conjecture T: the grammar G_n of the paper's
      prop:typed-thickness-exponential with the letter c renamed b.
      Computes ||G_n||, theta (shortest successful use of every rule),
      L(G_n) = Sigma^+ up to length 7, and the shortest pure-a yield of A_n
      (= 2^n), i.e. t_typ(G_n, c) >= 2^n while tau(G_n, c) = 1.
  (B) Random regular languages in C_{1,c} (content typing on {a,b}), via the
      transition monoid of the minimal DFA (= syntactic monoid):
      (B1) Lemma S'-core: z with nonempty distribution, p >= 1,
           a^p z == z  (or z a^p == z)  ==>  a == a^{1+p}.
      (B2) Lemma R^c in the "shared context" form used for an inner
           nonterminal X (W1, W2, W3 share one context, not necessarily in L):
           normal case z0 = w a^g, c = d; bad case (g = 0, w in b+) z0 = w a^d,
           c = 2d.  Also counts how often the naive  ww == w a^d  fails.
      (B3) Lemma C.0^c  (a w == a Omega  from a shared context a^{p-1}..).
      (B4) Consequence used in Theorem T': if a == a^{1+p0}, every pure-a word
           with nonempty distribution is == to some a^m with m <= p0.

Run:  python3 -I check_claude_S1_typed_2026-11-09.py   (about 30 s)
"""
import random, itertools, sys, time

# ---------------------------------------------------------------- (A)
def part_A(nmax=12):
    print("(A) G_n: S->SS|a|b|A_0|..|A_n, A_0->a, A_i->A_{i-1}A_{i-1}|b")
    for n in range(1, nmax + 1):
        rules = [("S", ("S", "S")), ("S", ("a",)), ("S", ("b",))]
        rules += [("S", ("A%d" % i,)) for i in range(n + 1)]
        rules += [("A0", ("a",))]
        for i in range(1, n + 1):
            rules += [("A%d" % i, ("A%d" % (i - 1), "A%d" % (i - 1))), ("A%d" % i, ("b",))]
        V = {l for l, _ in rules}
        size = len(V) + sum(1 + len(r) for _, r in rules)
        # shortest yield of each nonterminal
        INF = 10 ** 18
        sh = {X: INF for X in V}
        ch = True
        while ch:
            ch = False
            for l, r in rules:
                v = sum(1 if s not in V else sh[s] for s in r)
                if v < sh[l]:
                    sh[l] = v; ch = True
        # shortest pure-a yield
        pa = {X: INF for X in V}
        ch = True
        while ch:
            ch = False
            for l, r in rules:
                if any(s == "b" for s in r):
                    continue
                v = sum(1 if s not in V else pa[s] for s in r)
                if v < pa[l]:
                    pa[l] = v; ch = True
        # shortest context length of each nonterminal (outside size)
        ctx = {X: INF for X in V}; ctx["S"] = 0
        ch = True
        while ch:
            ch = False
            for l, r in rules:
                if ctx[l] >= INF:
                    continue
                tot = sum(1 if s not in V else sh[s] for s in r)
                for k, s in enumerate(r):
                    if s in V:
                        own = sh[s]
                        v = ctx[l] + tot - own
                        if v < ctx[s]:
                            ctx[s] = v; ch = True
        theta = max(ctx[l] + sum(1 if s not in V else sh[s] for s in r) for l, r in rules)
        # L(G_n) up to length 7 equals Sigma^+ (trivially, via S->SS|a|b); check A_n yields
        ok = all(ctx[X] < INF for X in V)
        print("  n=%2d  ||G||=%3d  theta=%d  reduced=%s  min pure-a yield of A_n = %d (2^n=%d)"
              % (n, size, theta, ok, pa["A%d" % n], 2 ** n))
    print("  L(G_n) = {a,b}^+ (S->SS|a|b), so a == a^{2^n} and tau(G_n,c) = 1.")

# ---------------------------------------------------------------- monoid tools
def minimize(nq, delta, q0, F):
    # reachable
    reach = {q0}; st = [q0]
    while st:
        q = st.pop()
        for x in (0, 1):
            r = delta[q][x]
            if r not in reach:
                reach.add(r); st.append(r)
    reach = sorted(reach)
    part = {q: (q in F) for q in reach}
    while True:
        sig = {q: (part[q], part[delta[q][0]], part[delta[q][1]]) for q in reach}
        ids = {}
        newp = {q: ids.setdefault(sig[q], len(ids)) for q in reach}
        if len(ids) == len(set(part.values())):
            part = newp; break
        part = newp
    m = len(set(part.values()))
    d2 = [[None, None] for _ in range(m)]
    for q in reach:
        for x in (0, 1):
            d2[part[q]][x] = part[delta[q][x]]
    F2 = {part[q] for q in reach if q in F}
    return m, d2, part[q0], F2

class Mon:
    def __init__(self, m, d, q0, F, cap):
        self.m, self.d, self.q0, self.F = m, d, q0, F
        self.gen = [tuple(d[q][0] for q in range(m)), tuple(d[q][1] for q in range(m))]
        self.id = tuple(range(m))
        # realized (element, content); content bits: 1=a, 2=b
        seen = {(self.id, 0)}; fr = [(self.id, 0)]
        while fr:
            nf = []
            for e, c in fr:
                for x in (0, 1):
                    f = self.mul(e, self.gen[x]); cc = c | (1 << x)
                    if (f, cc) not in seen:
                        seen.add((f, cc)); nf.append((f, cc))
                        if len(seen) > cap:
                            raise OverflowError
            fr = nf
        self.real = seen
        # co-accepting tuples of states
        self.co1 = self._coacc(1); self.co2 = self._coacc(2); self.co3 = self._coacc(3)
    def mul(self, e, f):            # word e then word f
        return tuple(f[e[q]] for q in range(self.m))
    def word(self, w):
        e = self.id
        for ch in w:
            e = self.mul(e, self.gen[0 if ch == "a" else 1])
        return e
    def _coacc(self, k):
        good = set()
        allt = list(itertools.product(range(self.m), repeat=k))
        for t in allt:
            if all(q in self.F for q in t):
                good.add(t)
        ch = True
        while ch:
            ch = False
            for t in allt:
                if t in good:
                    continue
                for x in (0, 1):
                    if tuple(self.d[q][x] for q in t) in good:
                        good.add(t); ch = True; break
        return good
    def nonempty(self, e):          # some context accepts
        return any((e[s],) in self.co1 for s in range(self.m))
    def share(self, *es):           # all share one context
        k = len(es); co = {1: self.co1, 2: self.co2, 3: self.co3}[k]
        return any(tuple(e[s] for e in es) in co for s in range(self.m))
    def is_C1c(self):
        by = {}
        for e, c in self.real:
            if c:
                by.setdefault(c, set()).add(e)
        for c, es in by.items():
            es = list(es)
            for i in range(len(es)):
                for j in range(i + 1, len(es)):
                    if self.share(es[i], es[j]):
                        return False
        return True

def content(w):
    return ("a" in w) | (("b" in w) << 1)

# ---------------------------------------------------------------- (B)
def part_B(nlang=6000, seed=20261109):
    rnd = random.Random(seed)
    stats = dict(lang=0, withpure=0, B1=0, B2n=0, B2b=0, naive_fail=0, B3=0, B4=0)
    viol = dict(B1=0, B2=0, B3=0, B4=0)
    omegas_b = ["b", "bb", "bbb"]
    omegas_m = ["ab", "ba", "bab", "aba"]
    t0 = time.time()
    tries = 0
    while stats["lang"] < nlang and tries < 40 * nlang:
        tries += 1
        n = rnd.randint(2, 6)
        delta = [[rnd.randrange(n), rnd.randrange(n)] for _ in range(n)]
        F = {q for q in range(n) if rnd.random() < 0.4}
        if not F:
            continue
        m, d, q0, F2 = minimize(n, delta, 0, F)
        try:
            M = Mon(m, d, q0, F2, cap=600)
        except OverflowError:
            continue
        if not M.is_C1c():
            continue
        stats["lang"] += 1
        A = [M.word("a" * k) for k in range(0, 40)]
        Ea = M.word("a")
        # (B1): for every realized element z with nonempty distribution
        P = range(1, 25)
        zs = {e for e, c in M.real if c and M.nonempty(e)}
        for z in zs:
            for p in P:
                if M.mul(A[p], z) == z or M.mul(z, A[p]) == z:
                    stats["B1"] += 1
                    if A[1 + p] != Ea:
                        viol["B1"] += 1
        # (B2): Lemma R^c, shared-context hypothesis
        for w in omegas_b + omegas_m:
            W = M.word(w); wb = content(w) == 2
            for g in range(0, 4):
                for nn in range(1, 5):
                    dd = g + nn
                    for x in range(0, 4):
                        for y in range(0, 4):
                            if wb and g == 0 and x == 0 and y == 0:
                                continue          # excluded (W1 would be b+)
                            W1 = M.word("a" * x + w + "a" * g + w + "a" * y)
                            W2 = M.word("a" * x + w + "a" * (dd + y))
                            W3 = M.word("a" * (x + dd) + w + "a" * y)
                            if not M.share(W1, W2, W3):
                                continue
                            ad = A[dd]
                            if wb and g == 0:
                                stats["B2b"] += 1
                                z0 = M.mul(W, ad); c = A[2 * dd]
                                ok = (M.mul(ad, z0) == M.mul(z0, ad)
                                      and M.mul(z0, z0) == M.mul(c, z0) == M.mul(z0, c))
                                if M.mul(W, W) != M.mul(W, ad):
                                    stats["naive_fail"] += 1
                            else:
                                stats["B2n"] += 1
                                z0 = M.mul(W, A[g])
                                ok = (M.mul(ad, z0) == M.mul(z0, ad) == M.mul(z0, z0))
                            if not ok:
                                viol["B2"] += 1
        # (B3): Lemma C.0^c : w in b+, Omega mixed, a^p w a^q and a^p Om a^q share a context, p>=1
        for w in omegas_b:
            for Om in ["ab", "ba", "abb", "bab", "aab"]:
                for p in range(1, 3):
                    for q in range(0, 3):
                        X1 = M.word("a" * p + w + "a" * q); X2 = M.word("a" * p + Om + "a" * q)
                        if M.share(X1, X2):
                            stats["B3"] += 1
                            if M.word("a" + w) != M.word("a" + Om):
                                viol["B3"] += 1
        # (B4)
        p0 = None
        for p in range(1, 39):
            if A[1 + p] == Ea:
                p0 = p; break
        if p0 is not None:
            for k in range(1, 40):
                if M.nonempty(A[k]):
                    stats["B4"] += 1
                    if not any(A[mm] == A[k] for mm in range(1, p0 + 1)):
                        viol["B4"] += 1
    print("(B) random regular C_{1,c} languages: %d (tries %d, %.1fs)"
          % (stats["lang"], tries, time.time() - t0))
    print("  (B1) a^p z == z => a == a^{1+p}: %d instances, violations %d" % (stats["B1"], viol["B1"]))
    print("  (B2) Lemma R^c (shared context): normal %d, bad %d, violations %d; naive ww==wa^d false in %d bad instances"
          % (stats["B2n"], stats["B2b"], viol["B2"], stats["naive_fail"]))
    print("  (B3) Lemma C.0^c: %d instances, violations %d" % (stats["B3"], viol["B3"]))
    print("  (B4) a==a^{1+p0} => pure classes have reps <= p0: %d instances, violations %d"
          % (stats["B4"], viol["B4"]))
    return sum(viol.values())

if __name__ == "__main__":
    part_A()
    v = part_B(int(sys.argv[1]) if len(sys.argv) > 1 else 3000)
    print("TOTAL violations:", v)
