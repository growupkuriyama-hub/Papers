#!/usr/bin/env python3
"""check_claude_fanout2_U1_kzeta_2026-11-09.py

Problem K (paper #2, op:fanout-two, round 2).  Standard library only.

What it does
  * MCFG as data; goodness assert; ||G||; exact theta_G; exact mu_1 (= lambda(S));
    exact cmax(A) = max #zeta-letters over In(A) (with infinity detection).
  * Builds the Knuth-order minimal type-1 derivation tree T and checks the
    proof of Theorem 1 step by step:
      #minimal big nodes <= cmax(S),  #big nodes <= cmax(S)*|V|,
      mu_1 <= max(theta_bar, cmax(S)*|V|*(rho_max + r*theta_bar)).
  * Family B_n (baseline for variant K'), CE family K1 (for comparison).
  * Bounded-length (d=1,2) substitutability check (NOT a membership proof).
  * Random test of Theorem 1 (seed fixed).
Everything printed is computation only ([観察]); proofs are in the report.
"""
import itertools
import random
import sys

INF = float("inf")


class G:
    """rules: list of (lhs, children(list), template(tuple of comps)),
    a comp is a list of items: str (terminal) or (j, i) = i-th comp of child j."""

    def __init__(self, fan, rules, start="S", sigma1=frozenset("ab")):
        self.fan, self.rules, self.S, self.sigma1 = fan, rules, start, sigma1
        self.V = list(fan)
        self.check_good()

    # ---------- basic data ----------
    def size(self):
        return len(self.V) + sum(1 + len(ch) + sum(len(c) for c in t)
                                 for _, ch, t in self.rules)

    def terms(self, t):
        return [x for c in t for x in c if isinstance(x, str)]

    def rho_max(self):
        return max(len(self.terms(t)) for _, _, t in self.rules)

    def rank(self):
        return max(len(ch) for _, ch, _ in self.rules)

    def check_good(self):
        for lhs, ch, t in self.rules:
            assert len(t) == self.fan[lhs], (lhs, t)
            assert all(len(c) > 0 for c in t), "epsilon"
            seq = [x for c in t for x in c if not isinstance(x, str)]
            for j, B in enumerate(ch):  # nondeleting + nonpermuting
                assert [x for x in seq if x[0] == j] == [(j, i) for i in range(self.fan[B])], (lhs, t)
            for c in t:  # nonmerging: x_{j,i} x_{j,i+1} never adjacent
                for u, v in zip(c, c[1:]):
                    assert not (isinstance(u, tuple) and isinstance(v, tuple)
                                and u[0] == v[0] and v[1] == u[1] + 1), (lhs, t)

    # ---------- exact quantities ----------
    def min_in(self, rule_ok=lambda r: True):
        m = {A: INF for A in self.V}
        ch = True
        while ch:
            ch = False
            for r in self.rules:
                if not rule_ok(r):
                    continue
                lhs, kids, t = r
                v = len(self.terms(t)) + sum(m[B] for B in kids)
                if v < m[lhs]:
                    m[lhs], ch = v, True
        return m

    def min_out(self, mi):
        mo = {A: INF for A in self.V}
        mo[self.S] = 0
        ch = True
        while ch:
            ch = False
            for lhs, kids, t in self.rules:
                base = mo[lhs] + len(self.terms(t)) + sum(mi[B] for B in kids)
                for j, B in enumerate(kids):
                    v = base - mi[B]
                    if v < mo[B]:
                        mo[B], ch = v, True
        return mo

    def theta(self):
        mi = self.min_in()
        mo = self.min_out(mi)
        return max(mo[l] + len(self.terms(t)) + sum(mi[B] for B in k)
                   for l, k, t in self.rules)

    def pure_rule(self, r):
        return all(x in self.sigma1 for x in self.terms(r[2]))

    def lam(self):
        return self.min_in(self.pure_rule)

    def cmax(self):
        """max #zeta letters in In(A); INF if unbounded."""
        zc = lambda t: sum(1 for x in self.terms(t) if x not in self.sigma1)
        NEG = -1
        cm = {A: NEG for A in self.V}
        nV = len(self.V)

        def rnd(cm):
            new = dict(cm)
            for lhs, kids, t in self.rules:
                if all(cm[B] != NEG for B in kids):
                    v = zc(t) + sum(cm[B] for B in kids)
                    if v > new[lhs]:
                        new[lhs] = v
            return new
        for _ in range(nV + 1):
            cm = rnd(cm)
        snap = dict(cm)
        for _ in range(nV + 1):
            cm = rnd(cm)
        res = {A: (INF if cm[A] != snap[A] else cm[A]) for A in self.V}
        for _ in range(nV + 1):  # propagate infinity
            for lhs, kids, t in self.rules:
                if any(res[B] == INF for B in kids):
                    res[lhs] = INF
        return res

    def lambda_tree(self):
        """Knuth-order argmin tree for lambda; returns list of (label, parent_idx)."""
        lam = {A: INF for A in self.V}
        arg, done = {}, set()
        while True:
            best = None
            for r in self.rules:
                lhs, kids, t = r
                if lhs in done or not self.pure_rule(r) or any(B not in done for B in kids):
                    continue
                v = len(self.terms(t)) + sum(lam[B] for B in kids)
                if best is None or v < best[0]:
                    best = (v, lhs, r)
            if best is None:
                break
            v, A, r = best
            lam[A], arg[A] = v, r
            done.add(A)
        if self.S not in done:
            return lam, None
        nodes = []

        def build(A, par, depth_labels):
            assert A not in depth_labels  # labels on a path are distinct
            idx = len(nodes)
            nodes.append((A, par))
            for B in arg[A][1]:
                build(B, idx, depth_labels | {A})
        build(self.S, -1, frozenset())
        return lam, nodes

    # ---------- bounded enumeration ----------
    def inside_sets(self, N):
        I = {A: set() for A in self.V}
        ch = True
        while ch:
            ch = False
            for lhs, kids, t in self.rules:
                for combo in itertools.product(*[sorted(I[B]) for B in kids]):
                    if sum(len("".join(y)) for y in combo) + len(self.terms(t)) > N:
                        continue
                    tup = tuple("".join(x if isinstance(x, str) else combo[x[0]][x[1]] for x in c)
                                for c in t)
                    if tup not in I[lhs]:
                        I[lhs].add(tup)
                        ch = True
        return I

    def lang(self, N):
        return {y[0] for y in self.inside_sets(N)[self.S]}


def C(s):  # template comp parser: "a0b" -> ['a',(0,0),'b'];  "0.1" style via tuples given directly
    return list(s)


# ---------------- families ----------------
def fam_B(n):
    """Baseline for K': S -> A_n | c A_i (i<n);  A_i -> A_{i-1}A_{i-1} | c;  A_0 -> a."""
    fan = {"S": 1, **{f"A{i}": 1 for i in range(n + 1)}}
    R = [("S", [f"A{n}"], ([(0, 0)],))]
    R += [("S", [f"A{i}"], (["c", (0, 0)],)) for i in range(n)]
    for i in range(1, n + 1):
        R.append((f"A{i}", [f"A{i-1}", f"A{i-1}"], ([(0, 0), (1, 0)],)))
        R.append((f"A{i}", [], (["c"],)))
    R.append(("A0", [], (["a"],)))
    return G(fan, R)


def fam_CE(n):
    """K1 of round 1: E_i -> b E E b | c E c, E_0 -> a, S -> E_n."""
    fan = {"S": 1, **{f"E{i}": 1 for i in range(n + 1)}}
    R = [("S", [f"E{n}"], ([(0, 0)],)), ("E0", [], (["a"],))]
    for i in range(1, n + 1):
        e = f"E{i-1}"
        R.append((f"E{i}", [e, e], (["b", (0, 0), (1, 0), "b"],)))
        R.append((f"E{i}", [e], (["c", (0, 0), "c"],)))
    return G(fan, R)


# ---------------- theorem check ----------------
def thm_check(g):
    tb = max(1, g.theta())
    lam, nodes = g.lambda_tree()
    mu = lam[g.S]
    cm = g.cmax()[g.S]
    if nodes is None:
        return dict(mu=INF)
    big = [i for i, (A, p) in enumerate(nodes) if lam[A] > tb]
    has_big_child = {p for i, (A, p) in enumerate(nodes) if i in set(big) and p >= 0}
    minimal = [i for i in big if i not in has_big_child]
    bound = max(tb, (cm * len(g.V) * (g.rho_max() + g.rank() * tb)) if cm != INF else INF)
    return dict(size=g.size(), tb=tb, mu=mu, cm=cm, nbig=len(big), nmin=len(minimal),
                V=len(g.V), bound=bound,
                ok=(mu <= bound and len(minimal) <= max(cm, 0 if mu <= tb else cm)
                    and (mu <= tb or len(big) <= cm * len(g.V))))


# ---------------- bounded substitutability ----------------
def tuple_type(g, x):
    return tuple(1 if all(ch in g.sigma1 for ch in comp) else "z" for comp in x)


def bounded_subst(g, N):
    L = g.lang(N)
    D = {}
    for w in L:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                D.setdefault((w[i:j],), set()).add((w[:i], w[j:]))
        for i, j, k, l in itertools.combinations(range(n + 1), 4):
            if i < j < k < l:
                D.setdefault((w[i:j], w[k:l]), set()).add((w[:i], w[j:k], w[l:]))
    fill = lambda E, x: "".join(itertools.chain.from_iterable(
        itertools.zip_longest(E, x, fillvalue="")))
    byctx = {}
    for x, Es in D.items():
        for E in Es:
            byctx.setdefault((len(x), E), []).append(x)
    for (d, E), xs in byctx.items():
        groups = {}
        for x in xs:
            groups.setdefault(tuple_type(g, x), []).append(x)
        for ty, grp in groups.items():
            x0 = grp[0]
            for x1 in grp[1:]:
                for a, b in ((x0, x1), (x1, x0)):
                    for E2 in D[a]:
                        w2 = fill(E2, b)
                        if len(w2) <= N and w2 not in L:
                            return dict(x=a, y=b, shared=E, ctx=E2, bad=w2)
    return None


def random_grammar(rng, nV, acyclic):
    V = ["S"] + [f"N{i}" for i in range(1, nV)]
    fan = {A: (1 if A == "S" else rng.choice([1, 2])) for A in V}
    R = []
    for idx, A in enumerate(V):
        for _ in range(rng.randint(1, 3)):
            pool = V[idx + 1:] if acyclic else V
            r = 0 if not pool else rng.choice([0, 1, 2, 2])
            kids = [rng.choice(pool) for _ in range(r)]
            seq, ptr = [], [0] * r
            while any(ptr[j] < fan[kids[j]] for j in range(r)):
                j = rng.choice([j for j in range(r) if ptr[j] < fan[kids[j]]])
                seq.append((j, ptr[j])); ptr[j] += 1
            d = fan[A]
            cuts = sorted(rng.sample(range(len(seq) + 1), d - 1)) if len(seq) + 1 >= d - 1 else []
            if len(cuts) != d - 1:
                cuts = [len(seq)] * (d - 1)
            parts, prev = [], 0
            for c in cuts + [len(seq)]:
                parts.append(seq[prev:c]); prev = c
            comps = []
            for p in parts:
                comp = []
                for x in p:
                    if comp and isinstance(comp[-1], tuple) and comp[-1][0] == x[0]:
                        comp.append(rng.choice("abc"))
                    if rng.random() < 0.3:
                        comp.append(rng.choice("abc"))
                    comp.append(x)
                if not comp or rng.random() < 0.3:
                    comp.append(rng.choice("abc"))
                comps.append(comp)
            R.append((A, kids, tuple(comps)))
    try:
        g = G(fan, R)
    except AssertionError:
        return None
    # reduce: require every rule usable (theta finite)
    if g.theta() == INF:
        return None
    return g


def main():
    print("== Family B_n (baseline for K'; no substitutability) ==")
    for n in range(1, 8):
        g = fam_B(n)
        r = thm_check(g)
        print(f"n={n}: ||G||={r['size']}, theta_bar={r['tb']}, mu1={r['mu']}, "
              f"cmax(S)={r['cm']}, #big={r['nbig']}, #minimal big={r['nmin']}, thm ok={r['ok']}")
    v = bounded_subst(fam_B(2), 8)
    print("B_2 bounded (d<=2, N=8) substitutability violation:", v)

    print("\n== CE family K1 (round 1) ==")
    for n in range(1, 6):
        r = thm_check(fam_CE(n))
        print(f"n={n}: ||G||={r['size']}, theta_bar={r['tb']}, mu1={r['mu']}, cmax(S)={r['cm']}, "
              f"#minimal big={r['nmin']}, thm ok={r['ok']}")

    print("\n== Random test of Theorem 1 (seed 20261109) ==")
    rng = random.Random(20261109)
    stats = dict(tested=0, finite_cm=0, mu_gt_theta=0, fail=0, enum_ok=0)
    for trial in range(4000):
        g = random_grammar(rng, rng.randint(2, 6), acyclic=(trial % 2 == 0))
        if g is None:
            continue
        r = thm_check(g)
        if r["mu"] == INF:
            continue
        stats["tested"] += 1
        if r["cm"] != INF:
            stats["finite_cm"] += 1
        if r["mu"] > r["tb"]:
            stats["mu_gt_theta"] += 1
        if not r["ok"]:
            stats["fail"] += 1
            print("FAIL", g.rules, r)
        # cross-check mu1 and cmax by enumeration on small cases
        if r["mu"] <= 9 and trial % 7 == 0:
            Lw = g.lang(9)
            m = min((len(w) for w in Lw if all(ch in "ab" for ch in w)), default=INF)
            cz = max((sum(ch == "c" for ch in w) for w in Lw), default=0)
            assert m == r["mu"], (m, r)
            assert cz <= r["cm"], (cz, r)
            stats["enum_ok"] += 1
    print(stats)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
