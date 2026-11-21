#!/usr/bin/env python3
"""check_claude_fanout2_U1_lower_2026-11-09.py

Problem U (op:fanout-two) exploration helper.  Standard library only.

For a fan-out <= 2 MCFG G (given as data) and a U_1 typing (a set of
type-1 letters; every other letter has type zeta) this script computes

  * ||G||   = |V| + sum_rules (1 + r + sum_i |alpha_i|)
  * theta_G = max_R min{|w| : w in L(G), some derivation of w uses R}
              (exact, via min inside / min outside lengths)
  * mu_1    = min{|w| : w in L(G), s(w) = 1}  (exact, via min inside length
              over the rules containing no zeta letter)
  * a bounded-length check of (2,s)-tuple substitutability:
    all words of L of length <= N are enumerated, then for d = 1, 2 every
    pair of same-type d-tuples sharing a d-context is compared on all
    contexts whose filled word has length <= N.  The first violations are
    printed (word, context, tuples).

A bounded check is NOT a membership proof; it can only refute membership.
"""
import sys
from itertools import combinations

# ---------------------------------------------------------------- grammar
# rule = (lhs, [child nonterminals], template)
# template = tuple of components; component = list of items
#   ('t', letter)  or  ('v', j, k)   (component k of child j, 0-based)

class MCFG:
    def __init__(self, fan, rules, start='S'):
        self.fan, self.rules, self.start = fan, rules, start

    def size(self):
        s = len(self.fan)
        for (_, ch, tp) in self.rules:
            s += 1 + len(ch) + sum(len(c) for c in tp)
        return s

    def check_good(self):
        for (A, ch, tp) in self.rules:
            assert len(tp) == self.fan[A], ('fan', A)
            occ = {}
            for ci, comp in enumerate(tp):
                assert comp, ('eps', A)
                prev = None
                for it in comp:
                    if it[0] == 'v':
                        occ.setdefault(it[1], []).append(it[2])
                        if prev and prev[0] == 'v' and prev[1] == it[1] \
                                and prev[2] + 1 == it[2]:
                            raise AssertionError(('merging', A, tp))
                    prev = it
            for j, B in enumerate(ch):
                assert occ.get(j) == list(range(self.fan[B])), \
                    ('deleting/permuting', A, tp)
        return True

    # exact minimum lengths ------------------------------------------
    def _term(self, tp):
        return sum(1 for c in tp for it in c if it[0] == 't')

    def min_inside(self, allowed=None):
        INF = float('inf')
        m = {A: INF for A in self.fan}
        changed = True
        while changed:
            changed = False
            for R in self.rules:
                A, ch, tp = R
                if allowed is not None and not allowed(R):
                    continue
                v = self._term(tp) + sum(m[B] for B in ch)
                if v < m[A]:
                    m[A] = v
                    changed = True
        return m

    def min_outside(self, mi):
        INF = float('inf')
        o = {A: INF for A in self.fan}
        o[self.start] = 0
        changed = True
        while changed:
            changed = False
            for (A, ch, tp) in self.rules:
                base = o[A] + self._term(tp) + sum(mi[B] for B in ch)
                for j, B in enumerate(ch):
                    v = base - mi[B]
                    if v < o[B]:
                        o[B] = v
                        changed = True
        return o

    def theta(self):
        mi = self.min_inside()
        mo = self.min_outside(mi)
        return max(mo[A] + self._term(tp) + sum(mi[B] for B in ch)
                   for (A, ch, tp) in self.rules)

    def mu1(self, one_letters):
        def ok(R):
            return all(it[0] != 't' or it[1] in one_letters
                       for c in R[2] for it in c)
        return self.min_inside(ok)[self.start]

    # bounded enumeration ---------------------------------------------
    def yields(self, N):
        Y = {A: set() for A in self.fan}
        changed = True
        while changed:
            changed = False
            for (A, ch, tp) in self.rules:
                for combo in _product([list(Y[B]) for B in ch]):
                    if sum(sum(len(x) for x in t) for t in combo) \
                            + self._term(tp) > N:
                        continue
                    out = tuple(''.join(it[1] if it[0] == 't'
                                        else combo[it[1]][it[2]]
                                        for it in comp) for comp in tp)
                    if sum(map(len, out)) <= N and out not in Y[A]:
                        Y[A].add(out)
                        changed = True
        return {w[0] for w in Y[self.start]}


def _product(lists):
    if not lists:
        yield ()
        return
    for x in lists[0]:
        for rest in _product(lists[1:]):
            yield (x,) + rest

# ------------------------------------------------- substitutability check
def typ(w, one):
    return 1 if all(ch in one for ch in w) else 'z'


def check_subst(L, N, one, max_viol=3, dmax=2):
    viols = []
    for d in range(1, dmax + 1):
        T2C, C2T = {}, {}
        for w in L:
            n = len(w)
            if d == 1:
                for i in range(n):
                    for j in range(i + 1, n + 1):
                        x, c = (w[i:j],), (w[:i], w[j:])
                        T2C.setdefault(x, set()).add(c)
                        C2T.setdefault(c, set()).add(x)
            else:
                for i in range(n):
                    for j in range(i + 1, n):
                        for k in range(j + 1, n):
                            for l in range(k + 1, n + 1):
                                x = (w[i:j], w[k:l])
                                c = (w[:i], w[j:k], w[l:])
                                T2C.setdefault(x, set()).add(c)
                                C2T.setdefault(c, set()).add(x)

        def fill(c, x):
            if d == 1:
                return c[0] + x[0] + c[1]
            return c[0] + x[0] + c[1] + x[1] + c[2]
        seen = set()
        for c, ts in C2T.items():
            groups = {}
            for x in ts:
                groups.setdefault(tuple(typ(p, one) for p in x), []).append(x)
            for g in groups.values():
                g.sort()
                rep = g[0]
                for y in g[1:]:
                    if (rep, y) in seen:
                        continue
                    seen.add((rep, y))
                    for (p, q) in ((rep, y), (y, rep)):
                        for e in T2C[p]:
                            u = fill(e, q)
                            if len(u) <= N and u not in L:
                                viols.append((d, c, p, q, e, u))
                                break
                        if viols and viols[-1][2] == p and viols[-1][3] == q:
                            break
                    if len(viols) >= max_viol:
                        return viols
    return viols

# ------------------------------------------------------------ candidates
T = lambda a: ('t', a)
V = lambda j, k: ('v', j, k)


def K1_CE(n):
    """Clark-Eyraud doubling family (prop:three-letter-family), fan-out 1."""
    fan = {'S': 1, **{f'E{i}': 1 for i in range(n + 1)}}
    R = [('S', [f'E{n}'], ([V(0, 0)],)), ('E0', [], ([T('a')],))]
    for i in range(1, n + 1):
        E = f'E{i-1}'
        R.append((f'E{i}', [E, E], ([T('b'), V(0, 0), V(1, 0), T('b')],)))
        R.append((f'E{i}', [E], ([T('c'), V(0, 0), T('c')],)))
    return MCFG(fan, R)


def K2_pair_doubling(n):
    """fan-2 doubling A_i -> (x1 y1, y2 x2) | (c x1, x2 c); S -> x1 a x2."""
    fan = {'S': 1, **{f'A{i}': 2 for i in range(n + 1)}}
    R = [('S', [f'A{n}'], ([V(0, 0), T('a'), V(0, 1)],)),
         ('A0', [], ([T('a')], [T('b')]))]
    for i in range(1, n + 1):
        A = f'A{i-1}'
        R.append((f'A{i}', [A, A], ([V(0, 0), V(1, 0)], [V(1, 1), V(0, 1)])))
        R.append((f'A{i}', [A], ([T('c'), V(0, 0)], [V(0, 1), T('c')])))
    return MCFG(fan, R)


def K3_pair_marked(n):
    """CE markers carried in two components:
       A_i -> (b x1 y1, y2 x2 b) | (c x1, x2 c);  A0 -> (a, a); S -> x1 b x2."""
    fan = {'S': 1, **{f'A{i}': 2 for i in range(n + 1)}}
    R = [('S', [f'A{n}'], ([V(0, 0), T('b'), V(0, 1)],)),
         ('A0', [], ([T('a')], [T('a')]))]
    for i in range(1, n + 1):
        A = f'A{i-1}'
        R.append((f'A{i}', [A, A],
                  ([T('b'), V(0, 0), V(1, 0)], [V(1, 1), V(0, 1), T('b')])))
        R.append((f'A{i}', [A], ([T('c'), V(0, 0)], [V(0, 1), T('c')])))
    return MCFG(fan, R)


def K4_single_letter(n):
    """direction (v): only 'a' has type 1.
       A_i -> (x1 y1, y2 x2) | (b x1, x2 c); A0 -> (a, a); S -> x1 a x2."""
    fan = {'S': 1, **{f'A{i}': 2 for i in range(n + 1)}}
    R = [('S', [f'A{n}'], ([V(0, 0), T('a'), V(0, 1)],)),
         ('A0', [], ([T('a')], [T('a')]))]
    for i in range(1, n + 1):
        A = f'A{i-1}'
        R.append((f'A{i}', [A, A], ([V(0, 0), V(1, 0)], [V(1, 1), V(0, 1)])))
        R.append((f'A{i}', [A], ([T('b'), V(0, 0)], [V(0, 1), T('c')])))
    return MCFG(fan, R)


def K5_two_phase(n):
    """direction (i): c always on both sides, in different phases.
       A_i -> (x1 b y1, y2 b x2) | (c x1 c, x2) | (x1, c x2 c);
       A0 -> (a, a); S -> x1 a x2."""
    fan = {'S': 1, **{f'A{i}': 2 for i in range(n + 1)}}
    R = [('S', [f'A{n}'], ([V(0, 0), T('a'), V(0, 1)],)),
         ('A0', [], ([T('a')], [T('a')]))]
    for i in range(1, n + 1):
        A = f'A{i-1}'
        R.append((f'A{i}', [A, A],
                  ([V(0, 0), T('b'), V(1, 0)], [V(1, 1), T('b'), V(0, 1)])))
        R.append((f'A{i}', [A], ([T('c'), V(0, 0), T('c')], [V(0, 1)])))
        R.append((f'A{i}', [A], ([V(0, 0)], [T('c'), V(0, 1), T('c')])))
    return MCFG(fan, R)


def K6_CE_two_c(n):
    """CE with the c-branch replaced by a two-sided one at fan-out 1:
       E_i -> b E E b | c E c E c  (c inside on both sides of a copy)."""
    fan = {'S': 1, **{f'E{i}': 1 for i in range(n + 1)}}
    R = [('S', [f'E{n}'], ([V(0, 0)],)), ('E0', [], ([T('a')],))]
    for i in range(1, n + 1):
        E = f'E{i-1}'
        R.append((f'E{i}', [E, E], ([T('b'), V(0, 0), V(1, 0), T('b')],)))
        R.append((f'E{i}', [E, E],
                  ([T('c'), V(0, 0), T('c'), V(1, 0), T('c')],)))
    return MCFG(fan, R)


# --------------------------------------------- Corollary 3 sanity check
def cor3_random(trials=300, seed=20261109):
    """Random small fan<=2 grammars over {a,b,c} whose rules contain at most
    one 'c' in total along any derivation is hard to force; instead we
    generate random grammars, keep those whose bounded language has <= 1 c
    per word up to length 12 AND whose mu_1 is finite, and test
    mu_1 <= (r+1)*thetabar + rho (rho = max terminals in a rule).
    This is an observation, not a proof (the proof is in the report)."""
    import random
    rnd = random.Random(seed)
    tested = bad = 0
    for _ in range(trials):
        nts = ['S', 'A', 'B']
        fan = {'S': 1, 'A': rnd.choice([1, 2]), 'B': rnd.choice([1, 2])}
        rules = []
        for X in ['A', 'B']:
            comps = tuple([T(rnd.choice('ab'))] for _ in range(fan[X]))
            rules.append((X, [], comps))
        for _ in range(4):
            X = rnd.choice(nts)
            Y = rnd.choice(['A', 'B'])
            comps = [[] for _ in range(fan[X])]
            # put variables of Y in order, spread over components, add letters
            slots = sorted(rnd.randrange(fan[X]) for _ in range(fan[Y]))
            for k, sl in enumerate(slots):
                if rnd.random() < 0.5:
                    comps[sl].append(T(rnd.choice('abc')))
                comps[sl].append(V(0, k))
            for c in comps:
                c.append(T(rnd.choice('abc')))
            rules.append((X, [Y], tuple(comps)))
        rules.append(('S', ['A'], tuple([[V(0, k) for k in range(fan['A'])]
                                         if fan['A'] == 1 else
                                         [V(0, 0), T('a'), V(0, 1)]])))
        G = MCFG(fan, rules)
        try:
            G.check_good()
        except AssertionError:
            continue
        mi = G.min_inside()
        if any(v == float('inf') for v in mi.values()):
            continue
        mo = G.min_outside(mi)
        if any(v == float('inf') for v in mo.values()):
            continue
        mu = G.mu1('ab')
        if mu == float('inf'):
            continue
        L = G.yields(12)
        if any(w.count('c') > 1 for w in L):
            continue
        th = max(1, G.theta())
        rho = max(G._term(tp) for (_, _, tp) in rules)
        tested += 1
        if mu > 2 * th + rho and mu > th:   # r = 1 in these grammars
            bad += 1
    return tested, bad


# ------------------------------------------------------------------ main
def report(name, ctor, ns, Nfor, one='ab'):
    print(f'== {name}  (type-1 letters: {one})')
    for n in ns:
        G = ctor(n)
        G.check_good()
        line = (f'  n={n}: ||G||={G.size()}, thetabar={max(1, G.theta())}, '
                f'mu_1={G.mu1(one)}')
        N = Nfor(n)
        if N:
            L = G.yields(N)
            v = check_subst(L, N, set(one), max_viol=1)
            if v:
                d, c, p, q, e, u = v[0]
                line += (f' | N={N}: VIOLATION d={d}: tuples {p} vs {q} share '
                         f'context {c}; context {e} gives {u!r} not in L')
            else:
                line += f' | N={N}: no violation up to length {N} (|L_N|={len(L)})'
        print(line)


if __name__ == '__main__':
    report('K1 CE doubling (fan-out 1)', K1_CE, range(1, 8),
           lambda n: 13 if n in (2, 3) else 0)
    report('K2 pair doubling, c both components', K2_pair_doubling,
           range(1, 8), lambda n: 11 if n in (1, 2, 3) else 0)
    report('K3 pair doubling with CE markers', K3_pair_marked,
           range(1, 8), lambda n: 12 if n in (1, 2, 3) else 0)
    report('K4 single type-1 letter a', K4_single_letter,
           range(1, 8), lambda n: 11 if n in (1, 2, 3) else 0, one='a')
    report('K5 two-phase c', K5_two_phase, range(1, 8),
           lambda n: 11 if n in (1, 2, 3) else 0)
    report('K6 CE with two-sided c-branch (fan-out 1)', K6_CE_two_c,
           range(1, 8), lambda n: 12 if n in (2, 3) else 0)
    t, b = cor3_random()
    print(f'== Corollary 3 random check: {t} grammars with <=1 c per word '
          f'(up to length 12) and finite mu_1; counterexamples to '
          f'mu_1 <= (r+1)thetabar+rho: {b}')
