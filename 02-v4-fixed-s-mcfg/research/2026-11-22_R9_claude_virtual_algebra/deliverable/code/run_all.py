#!/usr/bin/env python3
"""R9 (Claude Opus 5.5, 2026-11-22): finite checks for the report
"the algebra of virtual productions".

Python 3 standard library only, no network.  Run:   python3 -I run_all.py
All iteration orders are fixed (lists, sorted sets, seeded random.Random), so the standard
output does not depend on PYTHONHASHSEED.  Elapsed times go to standard error only.
Exit code 0 iff every check holds.

Sections
  [A] engine self-tests (check_step, closure engine vs. naive checker, dyadic blocks)
  [B] Theorem H-alpha (periodic spine, node-dependent escapes): pigeonhole selection and
      forcing certificates (Theorem NF + prototype), replayed from native words only
  [C] Lemma W mechanism: planted swapped words of a different weight force a shortcut
  [D] Lemma S on random fan-out<=2 derivation trees; the binomial estimate of step 6
  [E] token level: periodic spine closure = T(N) (n=3,4); Thue--Morse host, n=3
  [F] Theorem H-Xi on a synthetic periodic derivation tree with fan-out-2 nodes and a
      nested family (forcing certificates and a planted swap)
  [G] classification of every certificate step
"""
import sys
import time
import random
import itertools
from collections import defaultdict, deque, Counter
from functools import lru_cache
from math import comb, log2

sys.setrecursionlimit(100000)
T_START = time.time()
FAILS = []


def say(*a):
    print(*a)
    sys.stdout.flush()


def check(cond, msg):
    if not cond:
        FAILS.append(msg)
        say('  FAIL:', msg)


def tlog(tag):
    sys.stderr.write('[%s] %.1fs\n' % (tag, time.time() - T_START))


# ==================================================================================
# Rect / SUB steps
# ==================================================================================
def fill(E, t):
    if len(t) == 1:
        return E[0] + t[0] + E[1]
    return E[0] + t[0] + E[1] + t[1] + E[2]


def content(w):
    return frozenset(w)


def check_step(E0, E1, x, y, member, ty=content):
    """One SUB step: E0[x], E0[y], E1[x] in L, componentwise equal types, nonempty
    components, nonempty middle (arity 2)  ==>  E1[y] in L.  Returns E1[y]."""
    d = len(x)
    assert d in (1, 2) and len(y) == d and len(E0) == d + 1 and len(E1) == d + 1
    assert all(p != '' for p in x) and all(p != '' for p in y), 'empty component'
    if d == 2:
        assert E0[1] != '' and E1[1] != '', 'empty middle'
    assert tuple(ty(p) for p in x) == tuple(ty(p) for p in y), 'type mismatch'
    for wd in (fill(E0, x), fill(E0, y), fill(E1, x)):
        assert member(wd), 'premise not in L: %r' % (wd[:60],)
    return fill(E1, y)


def replay(steps, seed_member, ty=content):
    have = set()

    def member(u):
        return u in have or seed_member(u)
    out = None
    for (E0, E1, x, y) in steps:
        out = check_step(E0, E1, x, y, member, ty)
        have.add(out)
    return out, have


STEP_CLASSES = Counter()


def classify(steps):
    for (E0, E1, x, y) in steps:
        d = len(x)
        keep = all(sorted(x[i]) == sorted(y[i]) for i in range(d))
        STEP_CLASSES['%d-hole, %s' % (d, 'Parikh kept' if keep else 'Parikh changed')] += 1


# ==================================================================================
# Periodic host W = uL a^N uR: placements and the relations of Lemmas P1--P6
# ==================================================================================
class PeriodicBook:
    """nat_single[v] = (s0, t0): the word uL a^s0 e_v a^t0 uR is native (or already
    derived and recorded in `known`); weight p_v = N - s0 - t0.
    nat_pair[(v,w)] = (s0, g0, t0): uL a^s0 e_v a^g0 e_w a^t0 uR likewise."""

    def __init__(self, N, uL, uR, esc, weight, nat_single, nat_pair):
        self.N, self.uL, self.uR = N, uL, uR
        self.esc, self.p = esc, weight
        self.nat_single, self.nat_pair = nat_single, nat_pair
        self.W = uL + 'a' * N + uR
        self.steps = []
        self.known = set()

    def slide(self, U, p1, M, q1, V, p2, q2):
        """Lemma P1': U a^p1 M a^q1 V -> U a^p2 M a^q2 V (one two-hole step from W)."""
        N = self.N
        assert p1 >= 1 and q1 >= 1 and p2 >= 1 and q2 >= 1 and p1 + q1 == p2 + q2 <= N - 1
        assert M != ''
        E0 = (self.uL, 'a' * (N - p1 - q1), self.uR)
        x, y = ('a' * p1, 'a' * q1), ('a' * p2, 'a' * q2)
        E1 = (U, M, V)
        out = fill(E1, y)
        self.steps.append((E0, E1, x, y))
        self.known.add(out)
        return out

    def placement(self, v, s):
        N, p = self.N, self.p[v]
        t = N - p - s
        assert s >= 1 and t >= 1
        w = self.uL + 'a' * s + self.esc[v] + 'a' * t + self.uR
        if w in self.known:
            return w
        s0, t0 = self.nat_single[v]
        assert s0 >= 1 and t0 >= 1 and s0 + t0 == N - p
        if (s0, t0) == (s, t):
            self.known.add(w)
            return w
        base = self.uL + 'a' * s0 + self.esc[v] + 'a' * t0 + self.uR
        self.known.add(base)
        out = self.slide(self.uL, s0, self.esc[v], t0, self.uR, s, t)
        assert out == w
        return w

    def pair_placement(self, v, w_, s, g, t):
        N = self.N
        S = N - self.p[v] - self.p[w_]
        assert s >= 1 and g >= 1 and t >= 1 and s + g + t == S
        ev, ew = self.esc[v], self.esc[w_]

        def word(c):
            return self.uL + 'a' * c[0] + ev + 'a' * c[1] + ew + 'a' * c[2] + self.uR
        target = word((s, g, t))
        if target in self.known:
            return target
        cur = self.nat_pair[(v, w_)]
        self.known.add(word(cur))
        while cur[0] != s:
            r1, r2, r3 = cur
            if s < r1:
                new = (s, r2 + r1 - s, r3)
                out = self.slide(self.uL, r1, ev, r2, ew + 'a' * r3 + self.uR, new[0], new[1])
            elif r2 > 1:
                take = min(s - r1, r2 - 1)
                new = (r1 + take, r2 - take, r3)
                out = self.slide(self.uL, r1, ev, r2, ew + 'a' * r3 + self.uR, new[0], new[1])
            else:
                take = min(s - r1, r3 - 1)
                new = (r1 + take, r2, r3 - take)
                out = self.slide(self.uL, r1, ev + 'a' * r2 + ew, r3, self.uR, new[0], new[2])
            assert out == word(new)
            cur = new
        if cur[1] != g:
            r1, r2, r3 = cur
            new = (r1, g, r2 + r3 - g)
            out = self.slide(self.uL + 'a' * r1 + ev, r2, ew, r3, self.uR, new[1], new[2])
            assert out == word(new)
            cur = new
        assert word(cur) == target
        return target

    # Lemma P3 (COM): a e_v == e_v a
    def rel_COM(self, v):
        N, p = self.N, self.p[v]
        assert N - p >= 3
        E0 = (self.uL + 'a', 'a' * (N - p - 2) + self.uR)
        x, y = ('a' + self.esc[v],), (self.esc[v] + 'a',)
        assert fill(E0, x) == self.placement(v, 2)
        assert fill(E0, y) == self.placement(v, 1)
        return E0, x, y

    # Lemma P4 (EX): e_v a^{p_v'} == a^{p_v} e_v'
    def rel_EX(self, v, v2):
        N, pv, pv2 = self.N, self.p[v], self.p[v2]
        assert pv + pv2 <= N - 2
        E0 = (self.uL + 'a', 'a' * (N - pv - pv2 - 1) + self.uR)
        x = (self.esc[v] + 'a' * pv2,)
        y = ('a' * pv + self.esc[v2],)
        assert fill(E0, x) == self.placement(v, 1)
        assert fill(E0, y) == self.placement(v2, 1 + pv)
        return E0, x, y

    # Lemma P6 (DIS): e_v a^g e_w a == e_v a^{g+p_w+1}
    def rel_DIS(self, v, w_, g):
        N, pv, pw = self.N, self.p[v], self.p[w_]
        assert 1 <= g <= N - pv - pw - 2
        E0 = (self.uL + 'a', 'a' * (N - pv - pw - g - 2) + self.uR)
        x = (self.esc[v] + 'a' * g + self.esc[w_] + 'a',)
        y = (self.esc[v] + 'a' * (g + pw + 1),)
        assert fill(E0, x) == self.pair_placement(v, w_, 1, g, N - pv - pw - g - 1)
        assert fill(E0, y) == self.placement(v, 1)
        return E0, x, y


def apply_rel(cur, pos, rel):
    E0, x, y = rel
    assert cur[pos:pos + len(x[0])] == x[0], 'factor mismatch'
    E1 = (cur[:pos], cur[pos + len(x[0]):])
    return (E0, E1, x, y), fill(E1, y)


def reverse_chain(chain):
    return [(E0, E1, y, x) for (E0, E1, x, y) in reversed(chain)]


class KBlockMachine:
    """Theorem NF on a K-block with the fixed dissolution pair (v*, w*) at its start.

    family word  =  PhiL  e_v* a^g e_w* (a^g e_y)_{slots}  a^{g_last}  PhiR
    nf_chain returns the forward chain to  PhiL e_v* a^H PhiR  (H = block weight - p_v*)."""

    def __init__(self, book, vs, ws, PhiL, PhiR, g, q0):
        self.bk, self.vs, self.ws = book, vs, ws
        self.PhiL, self.PhiR, self.g, self.q0 = PhiL, PhiR, g, q0
        self.proto = PhiL + book.esc[vs] + 'a' * q0 + PhiR

    def g_last(self, slots):
        p, g = self.bk.p, self.g
        return self.q0 - (len(slots) + 1) * g - p[self.ws] - sum(p[y] for y in slots)

    def word(self, slots, g_last=None):
        esc, g = self.bk.esc, self.g
        if g_last is None:
            g_last = self.g_last(slots)
        assert g_last >= 1
        X = esc[self.vs] + 'a' * g + esc[self.ws]
        for y in slots:
            X += 'a' * g + esc[y]
        X += 'a' * g_last
        return self.PhiL + X + self.PhiR

    def block_weight(self, slots, g_last):
        p, g = self.bk.p, self.g
        return p[self.vs] + p[self.ws] + (len(slots) + 1) * g + g_last + sum(p[y] for y in slots)

    def nf_chain(self, word, slots, g_last):
        bk, esc, g = self.bk, self.bk.esc, self.g
        vs, ws = self.vs, self.ws
        pw = bk.p[ws]
        pos0 = len(self.PhiL)
        chain = []
        cur = word
        rights = [g] * len(slots) + [g_last]       # run after e_w*, then after each slot
        st, cur = apply_rel(cur, pos0, bk.rel_DIS(vs, ws, g))
        chain.append(st)
        H = g + pw + 1 + (rights[0] - 1)
        for idx, y in enumerate(slots):
            ey = esc[y]
            h = rights[idx + 1]
            p_ey = pos0 + len(esc[vs]) + H
            assert cur[p_ey:p_ey + len(ey)] == ey
            for _ in range(max(0, pw + 1 - h)):
                st, cur = apply_rel(cur, p_ey - 1, bk.rel_COM(y))
                chain.append(st)
                p_ey -= 1
                H -= 1
            hh = max(h, pw + 1)
            st, cur = apply_rel(cur, p_ey, bk.rel_EX(y, ws))
            chain.append(st)
            H2 = H + bk.p[y]
            st, cur = apply_rel(cur, pos0, bk.rel_DIS(vs, ws, H2))
            chain.append(st)
            H = H2 + pw + 1 + (hh - pw - 1)
        return chain, cur, H

    def rigidity_step(self, q_small, q_big, N, uL, uR):
        """Lemma P7: PhiL e a^{q_big} PhiR, PhiL e a^{q_small} PhiR in L  ==>  shortcut."""
        ev = self.bk.esc[self.vs]
        E0 = (self.PhiL + ev, self.PhiR)
        E1 = (uL, 'a' * (N - q_big) + uR)
        return (E0, E1, ('a' * q_big,), ('a' * q_small,))


def dyadic_blocks(lo, hi):
    out = []
    i = lo
    while i < hi:
        t = 0
        while i % (1 << (t + 1)) == 0 and i + (1 << (t + 1)) <= hi:
            t += 1
        out.append((t, i >> t))
        i += 1 << t
    return out


# ==================================================================================
# closure engine (token level) and exact substitutability checker
# ==================================================================================
def occ_all(w):
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield (w[:i], w[j:]), (w[i:j],)
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                for l in range(k + 1, n + 1):
                    yield (w[:i], w[j:k], w[l:]), (w[i:j], w[k:l])


class Closure:
    """Least superset of the seeds closed under SUB_1 and SUB_2 (all occurrences).
    Sound: each produced word lies in every (2,ty)-substitutable language containing the
    seeds.  If max_words is hit, .truncated is set and nothing is claimed."""

    def __init__(self, seeds, ty, max_words=10 ** 6, stop=None, max_len=None):
        self.ty, self.max_words, self.stop, self.max_len = ty, max_words, stop, max_len
        self.S = set()
        self.queue = deque()
        self.parent, self.members, self.ctxs = {}, {}, {}
        self.ctx_of = defaultdict(set)
        self.bucket = {}
        self.truncated, self.found = False, None
        for s in sorted(seeds, key=lambda u: (len(u), u)):
            self._add(s)

    def _add(self, w):
        if w in self.S or self.found is not None:
            return
        if len(self.S) >= self.max_words or (self.max_len is not None and len(w) > self.max_len):
            self.truncated = True
            return
        self.S.add(w)
        self.queue.append(w)
        if self.stop is not None and self.stop(w):
            self.found = w

    def find(self, t):
        p = self.parent
        while p[t] != t:
            p[t] = p[p[t]]
            t = p[t]
        return t

    def _occ(self, E, t):
        if t not in self.parent:
            self.parent[t] = t
            self.members[t] = [t]
            self.ctxs[t] = set()
        if E in self.ctx_of[t]:
            return
        self.ctx_of[t].add(E)
        r = self.find(t)
        if E not in self.ctxs[r]:
            self.ctxs[r].add(E)
            for y in self.members[r]:
                self._add(fill(E, y))
        key = (tuple(self.ty(p) for p in t), E)
        t2 = self.bucket.get(key)
        if t2 is None:
            self.bucket[key] = t
        else:
            r2 = self.find(t2)
            if r2 != r:
                self._union(r, r2)

    def _union(self, r1, r2):
        if len(self.members[r1]) + len(self.ctxs[r1]) < len(self.members[r2]) + len(self.ctxs[r2]):
            r1, r2 = r2, r1
        c1, c2 = self.ctxs[r1], self.ctxs[r2]
        m1, m2 = self.members[r1], self.members[r2]
        for E in sorted((E for E in c1 if E not in c2), key=repr):
            for y in m2:
                self._add(fill(E, y))
        for E in sorted((E for E in c2 if E not in c1), key=repr):
            for y in m1:
                self._add(fill(E, y))
        self.parent[r2] = r1
        m1.extend(m2)
        c1 |= c2
        del self.members[r2]
        del self.ctxs[r2]

    def run(self):
        while self.queue and not self.truncated and self.found is None:
            w = self.queue.popleft()
            for E, t in occ_all(w):
                self._occ(E, t)
                if self.truncated or self.found is not None:
                    break
        return self


def is_closed_exact(S, ty):
    ctx = defaultdict(set)
    for w in sorted(S):
        for E, t in occ_all(w):
            ctx[t].add(E)
    keys = sorted(ctx, key=repr)
    parent = {t: t for t in keys}

    def find(t):
        while parent[t] != t:
            parent[t] = parent[parent[t]]
            t = parent[t]
        return t
    bucket = {}
    for t in keys:
        tt = tuple(ty(p) for p in t)
        for E in sorted(ctx[t], key=repr):
            key = (tt, E)
            if key in bucket:
                a, b = find(t), find(bucket[key])
                if a != b:
                    parent[a] = b
            else:
                bucket[key] = t
    rep = {}
    for t in keys:
        r = find(t)
        if r in rep:
            if ctx[t] != ctx[rep[r]]:
                return False
        else:
            rep[r] = t
    return True


def is_closed_naive(S, ty):
    """Pairwise definition, for tiny sets only."""
    occ = defaultdict(set)
    for w in S:
        for E, t in occ_all(w):
            occ[t].add(E)
    ts = sorted(occ, key=repr)
    for i, x in enumerate(ts):
        for y in ts[i + 1:]:
            if len(x) != len(y):
                continue
            if tuple(ty(p) for p in x) != tuple(ty(p) for p in y):
                continue
            if occ[x] & occ[y] and occ[x] != occ[y]:
                return False
    return True


# ==================================================================================
# [A] engine self-tests
# ==================================================================================
def section_A():
    say('[A] engine self-tests')
    L = {'aab', 'abb'}

    def mem(u):
        return u in L
    bad = 0
    for args in [((('', ''), ('', ''), ('a',), ('',))),
                 ((('', ''), ('', ''), ('a',), ('b',))),
                 ((('a', '', 'b'), ('', 'x', ''), ('a', 'b'), ('a', 'b')))]:
        try:
            check_step(args[0], args[1], args[2], args[3], mem)
        except AssertionError:
            bad += 1
    check(bad == 3, 'check_step must reject empty components, type mismatch, empty middle')
    try:
        check_step(('', 'b'), ('', 'bb'), ('a',), ('aa',), mem)
        ok = False
    except AssertionError:
        ok = True
    check(ok, 'check_step must reject an unknown premise')
    out = check_step(('', 'b'), ('', 'bb'), ('aa',), ('a',), lambda u: u in {'aab', 'ab', 'aabb'})
    check(out == 'abb', 'check_step output')
    # dyadic blocks
    rng = random.Random(1)
    for _ in range(200):
        lo = rng.randint(0, 200)
        hi = lo + rng.randint(1, 200)
        bl = dyadic_blocks(lo, hi)
        cov = []
        for (t, k) in bl:
            cov.extend(range(k << t, (k + 1) << t))
        check(cov == list(range(lo, hi)), 'dyadic blocks partition')
        check(len(bl) <= 2 * (hi - lo).bit_length() + 2, 'dyadic block count')
    # closure: exact checker vs naive checker on random small sets, and closure is closed
    agree = 0
    for trial in range(60):
        S = set()
        for _ in range(rng.randint(2, 5)):
            S.add(''.join(rng.choice('abc') for _ in range(rng.randint(2, 5))))
        a = is_closed_exact(S, content)
        b = is_closed_naive(S, content)
        check(a == b, 'exact vs naive checker')
        agree += (a == b)
        C = Closure(S, content, max_words=80, max_len=9).run()
        if not C.truncated:
            check(is_closed_exact(C.S, content), 'closure is closed')
    say('  check_step rejects 4/4 bad steps; dyadic partitions OK; exact==naive on %d random sets' % agree)
    tlog('A')


# ==================================================================================
# [B] Theorem H-alpha: periodic spine, node-dependent escapes
# ==================================================================================
def spine_member_fn(n, uL, uR, esc):
    def member(w):
        if len(w) < len(uL) + len(uR) or not w.startswith(uL) or not w.endswith(uR):
            return False
        mid = w[len(uL):len(w) - len(uR)]

        @lru_cache(maxsize=None)
        def ends(t, k, i):
            res = set()
            if t == 0:
                if i < len(mid) and mid[i] == 'a':
                    res.add(i + 1)
                return frozenset(res)
            e = esc.get((t, k))
            if e is not None and mid.startswith(e, i):
                res.add(i + len(e))
            for j in sorted(ends(t - 1, 2 * k, i)):
                res |= ends(t - 1, 2 * k + 1, j)
            return frozenset(res)
        return len(mid) in ends(n, 0, 0)
    return member


def spine_native(n, uL, uR, esc, antichain):
    N = 1 << n
    out, i = [], 0
    for (t, k) in sorted(antichain, key=lambda v: v[1] << v[0]):
        lo = k << t
        assert lo >= i
        out.append('a' * (lo - i))
        out.append(esc[(t, k)])
        i = lo + (1 << t)
    out.append('a' * (N - i))
    return uL + ''.join(out) + uR


def rand_escapes(n, rng, letters, lo=2, hi=4, a_prob=0.0):
    esc = {}
    for t in range(1, n + 1):
        for k in range(1 << (n - t)):
            L = rng.randint(lo, hi)
            w = [rng.choice(letters) for _ in range(L)]
            for i in range(1, L - 1):
                if rng.random() < a_prob:
                    w[i] = 'a'
            esc[(t, k)] = ''.join(w)
    return esc


def cls(e):
    return frozenset(e) | {'a'}


def clsname(K):
    return '{' + ','.join(sorted(K)) + '}'


def spine_select(n, esc):
    """Pigeonhole selection of Corollary H5-alpha."""
    def nb(t, k):
        return 1 <= k <= (1 << (n - t)) - 2
    classes = sorted({cls(e) for e in esc.values()}, key=lambda c: ''.join(sorted(c)))
    best = None
    pair_levels_any = set()
    for K in classes:
        pair = None
        for i in range(1, n - 3):
            ks = [k for k in range(1 << (n - i)) if nb(i, k) and cls(esc[(i, k)]) == K]
            pk = None
            for k1 in ks:
                k2s = [k2 for k2 in ks if k2 >= k1 + 2]
                if k2s:
                    pk = ((i, k1), (i, k2s[0]))
                    break
            if pk is not None:
                pair_levels_any.add(i)
                if pair is None:
                    pair = pk
        if pair is None:
            continue
        fam = []
        for l in range(1, n - 2):
            ks = [k for k in range(1 << (n - l)) if nb(l, k) and cls(esc[(l, k)]) == K]
            if ks:
                fam.append((l, ks[0]))
        key = (len(fam), -pair[0][0])
        if best is None or key > best[0]:
            best = (key, K, pair, fam)
    q = len(classes)
    return best[1], best[2], best[3], q, len(pair_levels_any)


class SpineInstance:
    def __init__(self, n, uL, uR, esc, g):
        self.n, self.uL, self.uR, self.esc, self.g = n, uL, uR, esc, g
        N = 1 << n
        self.N = N
        self.member = spine_member_fn(n, uL, uR, esc)
        self.K, (self.vs, self.ws), self.F, self.q, self.npl = spine_select(n, esc)
        weight = {v: 1 << v[0] for v in esc}
        nat_single = {}
        for (t, k) in esc:
            if 1 <= k <= (1 << (n - t)) - 2:
                nat_single[(t, k)] = (k << t, N - (k << t) - (1 << t))
        vs, ws = self.vs, self.ws
        s0 = vs[1] << vs[0]
        g0 = (ws[1] << ws[0]) - s0 - (1 << vs[0])
        t0 = N - (ws[1] << ws[0]) - (1 << ws[0])
        assert g0 >= 1
        self.book = PeriodicBook(N, uL, uR, esc, weight, nat_single, {(vs, ws): (s0, g0, t0)})
        self.natives_used = {spine_native(n, uL, uR, esc, [v]) for v in nat_single}
        self.natives_used.add(spine_native(n, uL, uR, esc, [vs, ws]))
        self.natives_used.add(self.book.W)
        self._prototype()

    def _prototype(self):
        n, N, esc, uL, uR, g = self.n, self.N, self.esc, self.uL, self.uR, self.g
        vs = self.vs
        pv = 1 << vs[0]
        lo_v, hi_v = vs[1] << vs[0], (vs[1] << vs[0]) + pv
        pw = 1 << self.ws[0]
        sigma = sum(1 << l for (l, k) in self.F)
        M = len(self.F)
        q0 = pw + (M + 2) * g + sigma           # g_last = g for the native order of slots
        beta = hi_v
        left_len, right_len = lo_v, N - hi_v - 1
        right = right_len >= left_len
        if right:
            assert q0 <= right_len - 1, 'room'
            I = (N - q0, N)
        else:
            assert q0 <= left_len - 1, 'room'
            I = (0, q0)
        excluded = set(range(lo_v, hi_v)) | set(range(*I)) | {beta}
        anti = [vs]
        i = 0
        while i < N:
            if i in excluded:
                i += 1
                continue
            j = i
            while j < N and j not in excluded:
                j += 1
            for (t, k) in dyadic_blocks(i, j):
                if t >= 1:
                    anti.append((t, k))
            i = j
        nat = spine_native(n, uL, uR, esc, anti)
        assert self.member(nat)
        self.natives_used.add(nat)
        self.cover_size = len(anti) - 1
        bk = self.book
        bk.known.add(nat)
        ev = esc[vs]
        off = len(uL)
        # position of e_v* in the native word: length of the image of host positions [0, lo_v)
        L_left = self._prefix_len(anti, lo_v)
        pos_v = off + L_left
        assert nat[pos_v:pos_v + len(ev)] == ev and nat[pos_v + len(ev)] == 'a'
        if right:
            U = nat[:pos_v + len(ev)]
            body = nat[pos_v + len(ev):len(nat) - len(uR)]
            assert body.endswith('a' * q0)
            Mid = body[1:len(body) - q0]
            assert Mid != ''
            out = bk.slide(U, 1, Mid, q0, uR, q0, 1)
            self.PhiL = nat[:pos_v]
            self.PhiR = Mid + 'a' + uR
        else:
            pre = nat[:off]
            Mid = nat[off + q0:pos_v]
            assert nat[off:off + q0] == 'a' * q0 and Mid != ''
            restR = nat[pos_v + len(ev) + 1:]
            out = bk.slide(pre, q0, Mid + ev, 1, restR, 1, q0)
            self.PhiL = pre + 'a' + Mid
            self.PhiR = restR
        self.q0 = q0
        self.mach = KBlockMachine(bk, vs, self.ws, self.PhiL, self.PhiR, g, q0)
        assert out == self.mach.proto
        self.proto_steps = list(bk.steps)

    def _prefix_len(self, anti, lo_v):
        L = 0
        i = 0
        for (t, k) in sorted(anti, key=lambda v: v[1] << v[0]):
            a0 = k << t
            if a0 >= lo_v:
                break
            L += (a0 - i) + len(self.esc[(t, k)])
            i = a0 + (1 << t)
        return L + (lo_v - i)

    def slots(self, levels):
        node = {l: (l, k) for (l, k) in self.F}
        return [node[l] for l in levels]


def section_B():
    say('[B] Theorem H-alpha: periodic spine with node-dependent escapes')
    configs = [
        (7, '', '', 'cd', 11, 2, 0.0),
        (8, '', '', 'cd', 12, 2, 0.0),
        (8, 'f', 'f', 'cd', 13, 3, 0.25),
        (8, 'fe', 'ef', 'cde', 14, 2, 0.25),
        (9, '', 'f', 'cd', 15, 2, 0.0),
    ]
    printed = False
    total_certs = 0
    for (n, uL, uR, letters, seed, g, ap) in configs:
        rng = random.Random(seed)
        esc = rand_escapes(n, rng, letters, 2, 4, ap)
        inst = SpineInstance(n, uL, uR, esc, g)
        M = len(inst.F)
        say('  n=%d N=%d margins=(%r,%r) letters=%s: q=%d classes; K=%s; pair (v*,w*)=%s,%s; '
            'family levels %s (M=%d); cover escapes %d' % (
                n, inst.N, uL, uR, letters, inst.q, clsname(inst.K), inst.vs, inst.ws,
                [l for (l, k) in inst.F], M, inst.cover_size))
        bound = inst.npl / inst.q
        check(M >= bound, 'pigeonhole: M >= (#pair levels)/q')
        say('    pigeonhole: levels <= n-4 carrying a same-class non-adjacent pair = %d; '
            'M=%d >= %d/%d' % (inst.npl, M, inst.npl, inst.q))
        levels = [l for (l, k) in inst.F]
        perms = list(itertools.permutations(levels))
        if len(perms) > 40:
            prng = random.Random(seed + 1000)
            perms = [tuple(prng.sample(levels, len(levels))) for _ in range(40)]
        nforced = 0
        for perm in perms:
            slots = inst.slots(perm)
            gl = inst.mach.g_last(slots)
            w = inst.mach.word(slots, gl)
            chain, end, H = inst.mach.nf_chain(w, slots, gl)
            check(end == inst.mach.proto, 'NF ends at the prototype')
            cert = list(inst.book.steps) + reverse_chain(chain)
            out, _ = replay(cert, inst.member)
            check(out == w, 'certificate derives the family word')
            check(not inst.member(w), 'family word is not native')
            nforced += 1
            total_certs += 1
            if not printed:
                printed = True
                classify(cert)
                say('    example certificate: pi=%s, family word length %d, %d steps '
                    '(%d slides, then %d reversed NF steps).  Every step in full '
                    '(E0, E1, x, y; the four words are E0[x], E0[y], E1[x] and E1[y]):' % (
                        list(perm), len(w), len(cert), len(inst.book.steps), len(chain)))
                for si, (E0, E1, x, y) in enumerate(cert):
                    say('      step %2d: E0=%r E1=%r x=%r y=%r' % (si + 1, E0, E1, x, y))
                    say('               E0[x]=%s  E0[y]=%s' % (fill(E0, x), fill(E0, y)))
                    say('               E1[x]=%s  E1[y]=%s' % (fill(E1, x), fill(E1, y)))
            else:
                classify(reverse_chain(chain))
        classify(inst.book.steps)
        say('    forcing certificates replayed from native words only: %d/%d '
            '(each family word is outside L(G_n))' % (nforced, len(perms)))
    say('  total forcing certificates: %d' % total_certs)
    tlog('B')
    return total_certs


# ==================================================================================
# [C] the swap of Lemma W: planted swapped words force a shortcut
# ==================================================================================
def section_C():
    say('[C] Lemma W mechanism: a swapped word of different weight forces a shortcut')
    count = 0
    for (n, uL, uR, letters, seed, g, ap) in [(8, '', '', 'cd', 12, 2, 0.0),
                                                (8, 'f', 'f', 'cd', 13, 3, 0.25),
                                                (9, '', 'f', 'cd', 15, 2, 0.0)]:
        rng = random.Random(seed)
        esc = rand_escapes(n, rng, letters, 2, 4, ap)
        inst = SpineInstance(n, uL, uR, esc, g)
        levels = [l for (l, k) in inst.F]
        M = len(levels)
        prng = random.Random(seed + 7)
        done = 0
        tries = 0
        while done < 6 and tries < 200:
            tries += 1
            pi = prng.sample(levels, M)
            pi2 = prng.sample(levels, M)
            a = prng.randint(0, M - 1)
            b = prng.randint(a + 1, M)
            mix = pi2[:a] + pi[a:b] + pi2[b:]
            if sum(1 << l for l in pi[a:b]) == sum(1 << l for l in pi2[a:b]):
                continue
            slots = inst.slots(mix)
            gl = inst.g                      # inner and outer gaps are those of pi and pi2
            xprime = inst.mach.word(slots, gl)
            H_expected = inst.mach.block_weight(slots, gl) - (1 << inst.vs[0])
            seed_set = {xprime}
            chain, end, H = inst.mach.nf_chain(xprime, slots, gl)
            check(H == H_expected, 'NF weight bookkeeping')
            q0 = inst.q0
            if H == q0:
                continue
            qs, qb = min(H, q0), max(H, q0)
            rig = inst.mach.rigidity_step(qs, qb, inst.N, uL, uR)
            cert = list(inst.book.steps) + chain + [rig]
            out, _ = replay(cert, lambda u: u in seed_set or inst.member(u))
            short = uL + 'a' * (inst.N - (qb - qs)) + uR
            check(out == short, 'rigidity output is the shortcut')
            classify(chain + [rig])
            if done == 0:
                say('  n=%d: pi=%s pi\'=%s inner slots [%d,%d): swapped levels %s, '
                    'weight %+d  ->  shortcut a^%d (|W| core %d), %d steps' % (
                        n, pi, pi2, a, b, mix, H - q0, inst.N - (qb - qs), inst.N, len(cert)))
            done += 1
            count += 1
        check(done >= 3, 'enough planted swaps')
    say('  planted swaps with a weight change, each forcing a shortcut: %d' % count)
    tlog('C')


# ==================================================================================
# [D] Lemma S on random derivation trees; binomial estimate
# ==================================================================================
def random_tree(rng, ivals, theta, r):
    """A random 'derivation' of fan-out<=2, rank<=r over the given intervals.  Each node
    writes at most theta explicit letters in total (fragments); its children's components
    are pieces of its components, in order (nonpermuting); two pieces of one child are never
    adjacent (nonmerging); every child is strictly shorter than its parent, and a node
    without children has total length <= theta.  Returns (ivals, children)."""
    tot = sum(h - l for (l, h) in ivals)
    if tot <= theta:
        return (ivals, [])
    for _attempt in range(40):
        budget = rng.randint(0, theta)
        segs = []
        for ci, (l, h) in enumerate(ivals):
            npieces = rng.randint(1, 3)
            cuts = sorted(rng.sample(range(l + 1, h), min(npieces - 1, h - l - 1))) if h - l > 1 else []
            bounds = [l] + cuts + [h]
            for s_, e_ in zip(bounds, bounds[1:]):
                f = 0
                if budget > 0 and rng.random() < 0.5 and e_ - s_ > 1:
                    f = min(budget, rng.randint(1, max(1, (e_ - s_) // 3)))
                    budget -= f
                if f:
                    segs.append(('F', s_, s_ + f, ci))
                if e_ > s_ + f:
                    segs.append(('C', s_ + f, e_, ci))
        pieces = [i for i, sg in enumerate(segs) if sg[0] == 'C']
        groups = []
        order = pieces[:]
        while order:
            take = 2 if (len(order) >= 2 and rng.random() < 0.4) else 1
            groups.append(order[:take])
            order = order[take:]
        if not groups or len(groups) > r:
            continue
        if any(len(gp) == 2 and segs[gp[0]][3] == segs[gp[1]][3] and segs[gp[0]][2] == segs[gp[1]][1]
               for gp in groups):
            continue
        if any(sum(segs[i][2] - segs[i][1] for i in gp) >= tot for gp in groups):
            continue
        kids = [random_tree(rng, [(segs[i][1], segs[i][2]) for i in gp], theta, r) for gp in groups]
        return (ivals, kids)
    # deterministic valid fallback
    if len(ivals) == 2 and r >= 2:
        return (ivals, [random_tree(rng, [ivals[0]], theta, r), random_tree(rng, [ivals[1]], theta, r)])
    if len(ivals) == 2:                      # r = 1: one child keeps both pieces, minus a fragment
        (l1, h1), (l2, h2) = ivals
        if h2 - l2 > 1:
            return (ivals, [random_tree(rng, [(l1, h1), (l2, h2 - 1)], theta, r)])
        return (ivals, [random_tree(rng, [(l1, h1 - 1), (l2, h2)], theta, r)] if h1 - l1 > 1 else [])
    (l, h) = ivals[0]
    if r >= 2:
        m = (l + h) // 2
        return (ivals, [random_tree(rng, [(l, m)], theta, r), random_tree(rng, [(m, h)], theta, r)])
    return (ivals, [random_tree(rng, [(l, h - 1)], theta, r)])


def tree_nodes(tr):
    out = [tr]
    for ch in tr[1]:
        out.extend(tree_nodes(ch))
    return out


def section_D():
    say('[D] Lemma S (separator node) on random derivation trees; binomial estimate')
    rng = random.Random(2026)
    trials = 0
    worst_uncovered = 0
    for trial in range(300):
        r = rng.randint(1, 3)
        theta = rng.randint(1, 4)
        g = theta + 1
        M = 12 * r + 6 + rng.randint(0, 10)
        lam = rng.randint(1, 4)
        # word layout: PhiL | (Z E)^M Z | PhiR ; escapes of length lam
        L0 = rng.randint(0, 6)
        esc_iv = []
        pos = L0
        for j in range(M):
            pos += g
            esc_iv.append((pos, pos + lam))
            pos += lam
        pos += g + rng.randint(0, 6)
        total = pos
        tr = random_tree(rng, [(0, total)], theta, r)

        def cnt(node):
            iv = node[0]
            return sum(1 for (a, b) in esc_iv if any(l <= a and b <= h for (l, h) in iv))
        nodes = tree_nodes(tr)
        found = any(M / (3 * r) <= cnt(u) <= 2 * M / 3 for u in nodes)
        check(found, 'Lemma S separator exists (trial %d)' % trial)
        for v in nodes:
            if cnt(v) > 2 * M / 3 and all(cnt(c) <= 2 * M / 3 for c in v[1]):
                unc = cnt(v) - sum(cnt(c) for c in v[1])
                worst_uncovered = max(worst_uncovered, unc - (4 * r + 2))
                check(unc <= 4 * r + 2, 'uncovered escapes <= 4r+2')
        trials += 1
    say('  %d random trees (r<=3, theta<=4, M in [12r+6, 12r+16]): separator found in all; '
        'max(uncovered - (4r+2)) = %d <= 0' % (trials, worst_uncovered))
    okb = True
    for r in range(1, 6):
        for M in range(12 * r + 6, 241):
            k0 = -(-M // (3 * r))
            mn = min(comb(M, k) for k in range(k0, (2 * M) // 3 + 1))
            if mn < 2 ** (M / (3 * r)):
                okb = False
    check(okb, 'binomial estimate')
    say('  min_{M/(3r)<=k<=2M/3} C(M,k) >= 2^{M/(3r)} for r<=5, 12r+6<=M<=240: %s' % okb)
    tlog('D')


# ==================================================================================
# [E] token level
# ==================================================================================
def spine_tokens(n):
    def rec(t):
        if t == 0:
            return ['a']
        res = [x + y for x in rec(t - 1) for y in rec(t - 1)]
        res.append(chr(ord('0') + t))
        return res
    return set(rec(n))


def tm_tokens(n, split):
    def rec(t, typ):
        if t == 0:
            return ['a' if typ == 0 else 'b']
        l = rec(t - 1, typ)
        r = rec(t - 1, 1 - typ)
        res = [x + y for x in l for y in r]
        res.append(chr(ord('0') + t) if (typ == 0 or not split) else chr(ord('A') + t))
        return res
    return set(rec(n, 0))


def ty_tok(w):
    return frozenset('e' if (ch.isdigit() or ch.isupper()) else ch for ch in w)


def T_count(N):
    @lru_cache(maxsize=None)
    def f(m):
        if m == 0:
            return 1
        tot = 0
        for t in range(0, N.bit_length()):
            if (1 << t) <= m:
                tot += f(m - (1 << t))
        return tot
    return f(N)


def section_E():
    say('[E] token level (common content for all escape tokens)')
    for n in (3, 4):
        seeds = spine_tokens(n)
        C = Closure(seeds, ty_tok).run()
        ex = is_closed_exact(C.S, ty_tok)
        N = 1 << n
        check(not C.truncated and ex and len(C.S) == T_count(N), 'spine token closure = T(N)')
        say('  periodic spine n=%d: %d native token words -> closure %d words = |T(%d)| = %d, '
            'exactly substitutable: %s' % (n, len(seeds), len(C.S), N, T_count(N), ex))
    n = 3
    N = 8
    for split in (False, True):
        seeds = tm_tokens(n, split)
        C = Closure(seeds, ty_tok, stop=lambda w: set(w) <= {'a', 'b'} and len(w) < N).run()
        ex = is_closed_exact(C.S, ty_tok) if not C.truncated else None
        pure = sorted(w for w in C.S if set(w) <= {'a', 'b'})
        wts = Counter(sum((1 << int(ch)) if ch.isdigit() else ((1 << (ord(ch) - 65)) if ch.isupper() else 1)
                          for ch in w) for w in C.S)
        say('  Thue-Morse host n=3, escapes %s: %d native -> closure %d (exact: %s), shortcut: %s, '
            'pure host words: %d, weights: %s' % (
                'per type A/B' if split else 'one per level', len(seeds), len(C.S), ex,
                C.found, len(pure), dict(sorted(wts.items()))))
        if not split:
            allperm = sorted(set(''.join(p) for p in itertools.permutations('aaaabbbb')))
            check(pure == allperm and len(C.S) == 380 and ex, 'TM level-uniform: all Parikh-(4,4) words')
        else:
            check(len(C.S) == len(seeds) and ex, 'TM type-split: native set already closed')
    tlog('E')


# ==================================================================================
# [F] Theorem H-Xi on a synthetic periodic derivation tree (general forced subtree)
# ==================================================================================
class TNode:
    __slots__ = ('id', 'fan', 'comps', 'children', 'ivals', 'parent', 'esc')

    def __init__(self, fan, comps, children):
        self.fan, self.comps, self.children = fan, comps, children
        self.ivals = None
        self.parent = None
        self.esc = None
        self.id = None


def tn_comp_len(node, j):
    tot = 0
    for it in node.comps[j]:
        tot += it[1] if it[0] == 'a' else tn_comp_len(node.children[it[1]], it[2])
    return tot


def build_gamma(rng, depth):
    if depth <= 0:
        return TNode(1, [[('a', 1)]], [])
    kind = rng.choice(['D', 'D', 'T', 'W'])
    if kind == 'D':
        c1, c2 = build_gamma(rng, depth - 1), build_gamma(rng, depth - 1)
        return TNode(1, [[('c', 0, 0), ('c', 1, 0)]], [c1, c2])
    if kind == 'T':
        c1, c2 = build_gamma(rng, depth - 1), build_gamma(rng, depth - 2)
        return TNode(1, [[('c', 0, 0), ('a', 1), ('c', 1, 0)]], [c1, c2])
    z1, z2, y = build_gamma(rng, depth - 1), build_gamma(rng, depth - 2), build_gamma(rng, depth - 1)
    q = TNode(2, [[('c', 0, 0)], [('c', 1, 0)]], [z1, z2])
    return TNode(1, [[('c', 0, 0), ('c', 1, 0), ('c', 0, 1)]], [q, y])


def tn_layout(root):
    nodes = []

    def place(node, starts):
        node.ivals = []
        kid_starts = defaultdict(dict)
        for j, comp in enumerate(node.comps):
            pos = starts[j]
            begin = pos
            for it in comp:
                if it[0] == 'a':
                    pos += it[1]
                else:
                    kid_starts[it[1]][it[2]] = pos
                    pos += tn_comp_len(node.children[it[1]], it[2])
            node.ivals.append((begin, pos))
        for ci, ch in enumerate(node.children):
            ch.parent = node
            place(ch, [kid_starts[ci][j] for j in range(ch.fan)])
        node.id = len(nodes)
        nodes.append(node)
    place(root, [0])
    return nodes


def tn_is_anc(nodes, u, v):
    p = nodes[v].parent
    while p is not None:
        if p.id == u:
            return True
        p = p.parent
    return False


def gamma_native(N, nodes, antichain):
    reps = []
    for v in antichain:
        for j, (lo, hi) in enumerate(nodes[v].ivals):
            reps.append((lo, hi, nodes[v].esc[j]))
    reps.sort()
    out, i = [], 0
    for lo, hi, w in reps:
        assert lo >= i
        out.append('a' * (lo - i))
        out.append(w)
        i = hi
    out.append('a' * (N - i))
    return ''.join(out)


def section_F():
    say('[F] Theorem H-Xi on synthetic periodic derivation trees (fan-out-2 nodes, nested family)')
    reports = 0
    nested_total = [0]
    for seed in (5, 8, 21):
        rng = random.Random(seed)
        root = build_gamma(rng, 9)
        nodes = tn_layout(root)
        N = root.ivals[0][1]
        for v in nodes:
            if v.children:
                v.esc = tuple(''.join(rng.choice('cd') for _ in range(rng.randint(2, 3)))
                              for _ in range(v.fan))
        uL = uR = ''

        def hull(v):
            return (nodes[v].ivals[0][0], nodes[v].ivals[-1][1])
        cand = [v.id for v in nodes if v.children and hull(v.id)[0] >= 1 and hull(v.id)[1] <= N - 1
                and v.id != root.id]
        # shrunk escape words and weights (fan-out 2: omega1 a omega2)
        ew, wt = {}, {}
        for v in cand:
            nd = nodes[v]
            if nd.fan == 1:
                ew[v] = nd.esc[0]
                wt[v] = nd.ivals[0][1] - nd.ivals[0][0]
            else:
                ew[v] = nd.esc[0] + 'a' + nd.esc[1]
                wt[v] = (nd.ivals[0][1] - nd.ivals[0][0]) + (nd.ivals[1][1] - nd.ivals[1][0]) + 1

        natives = set()
        book = PeriodicBook(N, uL, uR, ew, wt, {}, {})
        natives.add(book.W)
        for v in cand:
            nd = nodes[v]
            nat = gamma_native(N, nodes, [v])
            natives.add(nat)
            lo, hi = hull(v)
            if nd.fan == 1:
                book.nat_single[v] = (lo, N - hi)
            else:
                gap = nd.ivals[1][0] - nd.ivals[0][1]
                U = 'a' * lo + nd.esc[0]
                out = book.slide(U, gap, nd.esc[1], N - hi, '', 1, gap + N - hi - 1)
                assert out == 'a' * lo + ew[v] + 'a' * (gap + N - hi - 1)
                book.nat_single[v] = (lo, gap + N - hi - 1)
        classes = sorted({cls(ew[v]) for v in cand}, key=lambda c: ''.join(sorted(c)))
        best = None
        for K in classes:
            KV = [v for v in cand if cls(ew[v]) == K]
            pair = None
            for v in sorted(KV, key=lambda v: wt[v]):
                if nodes[v].fan != 1:
                    continue
                for w in sorted(KV, key=lambda w: wt[w]):
                    if w == v or tn_is_anc(nodes, v, w) or tn_is_anc(nodes, w, v):
                        continue
                    if hull(w)[0] >= hull(v)[1] + 1 and wt[v] + wt[w] <= N // 16:
                        pair = (v, w)
                        break
                if pair:
                    break
            if pair is None:
                continue
            # superincreasing family (ratio >= 2), allowed to be nested, total <= N/4
            fam = []
            pool = sorted((v for v in KV if wt[v] <= N // 8), key=lambda v: (-wt[v], v))
            while True:
                lim = wt[fam[-1]] // 2 if fam else N // 8
                ok = [v for v in pool if wt[v] <= lim and v not in fam
                      and sum(wt[x] for x in fam) + wt[v] <= N // 4]
                if not ok:
                    break
                desc = [v for v in ok if fam and tn_is_anc(nodes, fam[-1], v)]
                fam.append((desc or ok)[0])
            if best is None or len(fam) > len(best[2]):
                best = (K, pair, fam)
        if best is None or len(best[2]) < 3:
            say('  seed %d: N=%d, no usable configuration (skipped)' % (seed, N))
            continue
        K, (vs, ws), fam = best
        nested = sum(1 for a in fam for b in fam if a != b and tn_is_anc(nodes, a, b))
        fan2 = sum(1 for a in fam if nodes[a].fan == 2)
        # pair native word, shrunk
        nat_pair = gamma_native(N, nodes, [vs, ws])
        natives.add(nat_pair)
        lo_v, hi_v = hull(vs)
        lo_w, hi_w = hull(ws)
        if nodes[ws].fan == 1:
            book.nat_pair[(vs, ws)] = (lo_v, lo_w - hi_v, N - hi_w)
        else:
            nd = nodes[ws]
            gap = nd.ivals[1][0] - nd.ivals[0][1]
            U = 'a' * lo_v + ew[vs] + 'a' * (lo_w - hi_v) + nd.esc[0]
            out = book.slide(U, gap, nd.esc[1], N - hi_w, '', 1, gap + N - hi_w - 1)
            book.nat_pair[(vs, ws)] = (lo_v, lo_w - hi_v, gap + N - hi_w - 1)
        # prototype (Lemma Phi-gamma): pure antichain U chosen greedily, cover C escaped
        g = 3
        Mf = len(fam)
        qmin = wt[ws] + (Mf + 1) * g + sum(wt[x] for x in fam) + 1
        beta = hi_v
        Epts = set(range(lo_v, hi_v)) | {beta}

        def npos(nd):
            out_ = set()
            for (l, h) in nd.ivals:
                out_ |= set(range(l, h))
            return out_

        def explicit(nd):
            return sum(it[1] for comp in nd.comps for it in comp if it[0] == 'a')

        def init_pieces(nd, acc):
            if not (npos(nd) & Epts):
                acc.append(nd)
                return
            for ch in nd.children:
                if ch.id != vs:
                    init_pieces(ch, acc)
        pieces = []
        init_pieces(root, pieces)
        n_cross_expl = N - len(npos(nodes[vs])) - sum(len(npos(p)) for p in pieces)
        base = n_cross_expl + sum(1 for p in pieces if not p.children)
        target = qmin + 40
        remaining = target - base
        queue_ = [p for p in pieces if p.children]
        pure_nodes, esc_nodes = [], []
        while queue_:
            P = queue_.pop(0)
            if remaining <= 0:
                esc_nodes.append(P)
                continue
            if len(npos(P)) <= remaining:
                pure_nodes.append(P)
                remaining -= len(npos(P))
                continue
            remaining -= explicit(P)
            kids = []
            for ch in P.children:
                if ch.children:
                    kids.append(ch)
                else:
                    remaining -= 1
            queue_ = kids + queue_
        anti = [vs] + [p.id for p in esc_nodes]
        protonat = gamma_native(N, nodes, anti)
        natives.add(protonat)
        book.known.add(protonat)
        assert 'a' not in ''.join(''.join(nodes[x].esc) for x in anti)
        ev = ew[vs]
        # locate e_v* (escapes contain no 'a'): by host position bookkeeping
        reps = sorted((nodes[x].ivals[j][0], nodes[x].ivals[j][1], nodes[x].esc[j], x)
                      for x in anti for j in range(nodes[x].fan))
        pos_v, i = 0, 0
        for (lo, hi, wd, x) in reps:
            if x == vs:
                pos_v += lo - i
                break
            pos_v += (lo - i) + len(wd)
            i = hi
        assert protonat[pos_v:pos_v + len(ev)] == ev and protonat[pos_v + len(ev)] == 'a'
        cur = protonat
        vstart = pos_v

        def runs(wd):
            out_, k = [], 0
            while k < len(wd):
                if wd[k] == 'a':
                    l0 = k
                    while k < len(wd) and wd[k] == 'a':
                        k += 1
                    out_.append((l0, k))
                else:
                    k += 1
            return out_
        while True:
            vend = vstart + len(ev)
            rs = runs(cur)
            rv = [r_ for r_ in rs if r_[0] == vend][0]
            others = [r_ for r_ in rs if r_ != rv and r_[1] - r_[0] >= 2]
            if not others:
                break
            (l0, h0) = others[0]
            L_ = h0 - l0
            qv = rv[1] - rv[0]
            if h0 <= vstart:
                out = book.slide(cur[:l0], L_, cur[h0:rv[0]], qv, cur[rv[1]:], 1, L_ + qv - 1)
                vstart -= L_ - 1
            else:
                out = book.slide(cur[:rv[0]], qv, cur[rv[1]:l0], L_, cur[h0:], qv + L_ - 1, 1)
            cur = out
        vend = vstart + len(ev)
        rv = [r_ for r_ in runs(cur) if r_[0] == vend][0]
        q0 = rv[1] - rv[0]
        PhiL, PhiR = cur[:vstart], cur[rv[1]:]
        check(q0 >= qmin, 'gamma prototype run is long enough')
        out = cur
        mach = KBlockMachine(book, vs, ws, PhiL, PhiR, g, q0)
        check(out == mach.proto, 'gamma prototype')
        seed_member = lambda u: u in natives
        prng = random.Random(seed + 99)
        forced = 0
        for _ in range(8):
            slots = prng.sample(fam, Mf)
            gl = mach.g_last(slots)
            w = mach.word(slots, gl)
            chain, end, H = mach.nf_chain(w, slots, gl)
            check(end == mach.proto, 'gamma NF end')
            cert = list(book.steps) + reverse_chain(chain)
            o, _ = replay(cert, seed_member)
            check(o == w, 'gamma forcing certificate')
            classify(reverse_chain(chain))
            forced += 1
        # planted swap with repetition
        swaps = 0
        for _ in range(30):
            a = prng.randint(0, Mf - 1)
            b = prng.randint(a + 1, Mf)
            p1 = prng.sample(fam, Mf)
            p2 = prng.sample(fam, Mf)
            mix = p2[:a] + p1[a:b] + p2[b:]
            if sum(wt[x] for x in p1[a:b]) == sum(wt[x] for x in p2[a:b]):
                continue
            gl = mach.g_last(p2)
            xp = mach.word(mix, gl)
            chain, end, H = mach.nf_chain(xp, mix, gl)
            if H == q0 or max(H, q0) > N:
                continue
            rig = mach.rigidity_step(min(H, q0), max(H, q0), N, uL, uR)
            cert = list(book.steps) + chain + [rig]
            o, _ = replay(cert, lambda u, xp=xp: u == xp or u in natives)
            check(o == 'a' * (N - abs(H - q0)), 'gamma shortcut')
            classify(chain + [rig])
            swaps += 1
            if swaps >= 4:
                break
        classify(book.steps)
        say('  seed %d: N=%d, %d tree nodes (%d of fan-out 2); K=%s; pair %d,%d (weights %d,%d); '
            'family weights %s (nested pairs %d, fan-out-2 members %d); cover %d nodes; '
            'forced %d/8; swaps->shortcut %d' % (
                seed, N, len(nodes), sum(1 for v in nodes if v.fan == 2), clsname(K), vs, ws,
                wt[vs], wt[ws], [wt[x] for x in fam], nested, fan2, len(anti) - 1, forced, swaps))
        say('    prototype: pure antichain of %d nodes, |PhiL|+|PhiR| = %d, run after e_v* = %d '
            '(needed >= %d)' % (len(pure_nodes), len(PhiL) + len(PhiR), q0, qmin))
        reports += 1
        nested_total[0] += nested
    check(reports >= 2, 'at least two gamma instances')
    check(nested_total[0] >= 1, 'some family contains comparable (nested) members')
    tlog('F')


# ==================================================================================
def main():
    say('R9 finite checks (Claude Opus 5.5, 2026-11-22)')
    section_A()
    section_B()
    section_C()
    section_D()
    section_E()
    section_F()
    say('[G] classification of all certificate steps')
    for k in sorted(STEP_CLASSES):
        say('  %-28s %d' % (k, STEP_CLASSES[k]))
    if FAILS:
        say('FAILED checks: %d' % len(FAILS))
        sys.exit(1)
    say('ALL CHECKS PASSED')
    tlog('end')


if __name__ == '__main__':
    main()
