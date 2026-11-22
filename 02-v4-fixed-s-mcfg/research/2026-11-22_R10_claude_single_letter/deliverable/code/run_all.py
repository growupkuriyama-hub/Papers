#!/usr/bin/env python3
"""R10 (Claude Opus 5.5, 2026-11-22): finite checks for the report
"the single-letter root type m={a}: class elimination and interleaved configurations".

Python 3 standard library only, no network.  Run:   python3 -I run_all.py
All iteration orders are fixed (lists, sorted containers, seeded random.Random), so the
standard output does not depend on PYTHONHASHSEED.  Elapsed times go to standard error only.
Exit code 0 iff every check holds.

Sections
  [A] engine self-tests (SUB step checker, closure engine vs. naive checker)
  [B] Lemma 1 (chain / side branch) and the class-elimination dichotomy of Theorem A on
      random derivation trees; classification of same-class pairs (Lemma D / residual types)
  [C] Theorem H-Xi* with the new dissolvers of Lemma D2 (fan-out-2 v*, one component,
      inside the gap or right of the hull) and the two-frame prototype (Lemma Phi2):
      forcing certificates replayed from native words only, planted swaps -> shortcut
  [D] nested-only chain class: (D1) token-level closure of a spine whose c-class lies on
      one chain; (D2) a letter-level finite language with nested escapes only
  [E] R15 order-invariant language L_{N,d}: exact substitutability (small N), the
      interleaved configuration in the node-minimal tree, no concatenated pair placement
  [F] the two-sided normal form NF2 on a synthetic crossing pair (certificates replayed
      from native words), and the numerical comparison of the bounds of Theorem A and
      R9's H-gamma-1
"""
import sys
import time
import random
import itertools
from collections import defaultdict, deque, Counter
from math import log2

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
        STEP_CLASSES['%d-hole, componentwise Parikh %s' % (d, 'kept' if keep else 'changed')] += 1


# ==================================================================================
# closure engine (adapted from the R9 engine; re-validated in [A] against the naive
# pairwise checker) and the exact substitutability checker
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

    def __init__(self, seeds, ty, max_words=10 ** 6, stop=None):
        self.ty, self.max_words, self.stop = ty, max_words, stop
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
        if len(self.S) >= self.max_words:
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
    """Exact check that the finite set S is (2,ty)-substitutable: all one- and two-hole
    occurrences, componentwise types, nonempty components and nonempty middle."""
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
    L = {'aaaa', 'acaa', 'aaca'}
    mem = lambda u: u in L
    rejected = 0
    tests = [
        (('a', 'a'), ('', 'aa'), ('', ''), ('',)),
        (('', '', ''), ('', 'a', ''), ('a', 'a'), ('a', 'a')),
        (('a', 'a'), ('a', 'a'), ('c',), ('a',)),
        (('', ''), ('', ''), ('cc',), ('cc',)),
    ]
    for (E0, E1, x, y) in tests:
        try:
            check_step(E0, E1, x, y, mem)
        except AssertionError:
            rejected += 1
    check(rejected == 4, 'check_step rejects the four malformed steps')
    ok = check_step(('a', 'a'), ('a', 'a'), ('ca',), ('ac',), mem)
    check(ok == 'aaca', 'check_step accepts a legal step')
    rng = random.Random(1)
    agree = 0
    for _ in range(60):
        S = set()
        for _ in range(rng.randint(2, 5)):
            S.add(''.join(rng.choice('ab') for _ in range(rng.randint(1, 5))))
        e1, e2 = is_closed_exact(S, content), is_closed_naive(S, content)
        agree += (e1 == e2)
        if e1:
            C = Closure(S, content).run()
            check(C.S == S, 'closure of a closed set is itself')
    check(agree == 60, 'exact == naive on 60 random sets')
    C = Closure({'aaaa', 'acaa'}, content).run()
    check(is_closed_exact(C.S, content), 'closure output is closed')
    say('  check_step rejects %d/4 malformed steps; exact==naive on %d/60 random sets; '
        'closure of {aaaa, acaa} has %d words and is closed' % (rejected, agree, len(C.S)))
    tlog('A')


# ==================================================================================
# synthetic derivation trees (positions only; every node yields a^{len})
# ==================================================================================
class TNode:
    __slots__ = ('id', 'fan', 'comps', 'children', 'ivals', 'parent', 'esc', 'tag')

    def __init__(self, fan, comps, children, tag=''):
        self.fan, self.comps, self.children = fan, comps, children
        self.ivals = None
        self.parent = None
        self.esc = None
        self.id = None
        self.tag = tag


def tn_comp_len(node, j):
    tot = 0
    for it in node.comps[j]:
        tot += it[1] if it[0] == 'a' else tn_comp_len(node.children[it[1]], it[2])
    return tot


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
    # sanity: good-grammar shape (nonmerging: the components of a fan-out-2 node are separated)
    for v in nodes:
        if v.fan == 2:
            assert v.ivals[0][1] < v.ivals[1][0], 'merging components'
        for ch in v.children:
            for (l, h) in ch.ivals:
                assert any(L <= l and h <= H for (L, H) in v.ivals)
    return nodes


def nlen(v):
    return sum(h - l for (l, h) in v.ivals)


def hull(v):
    return (v.ivals[0][0], v.ivals[-1][1])


def npos(v):
    s = set()
    for (l, h) in v.ivals:
        s |= set(range(l, h))
    return s


def is_anc(u, v):
    p = v.parent
    while p is not None:
        if p is u:
            return True
        p = p.parent
    return False


def comparable(u, v):
    return u is v or is_anc(u, v) or is_anc(v, u)


def native(N, nodes, antichain):
    """W[A <- omega]: replace every component interval of every node of the antichain by
    the corresponding component of its escape."""
    reps = []
    for v in antichain:
        for j, (lo, hi) in enumerate(v.ivals):
            reps.append((lo, hi, v.esc[j]))
    reps.sort()
    out, i = [], 0
    for lo, hi, w in reps:
        assert lo >= i, 'antichain overlaps'
        out.append('a' * (lo - i))
        out.append(w)
        i = hi
    out.append('a' * (N - i))
    return ''.join(out)


def build_filler(rng, depth, allow_fan2=True):
    """Random doubling-type subtree; fan-out-2 nodes appear inside 'W' gadgets."""
    if depth <= 0:
        return TNode(1, [[('a', 1)]], [])
    kinds = ['D', 'D', 'T'] + (['W', 'X'] if allow_fan2 else [])
    kind = rng.choice(kinds)
    if kind == 'D':
        c1, c2 = build_filler(rng, depth - 1, allow_fan2), build_filler(rng, depth - 1, allow_fan2)
        return TNode(1, [[('c', 0, 0), ('c', 1, 0)]], [c1, c2])
    if kind == 'T':
        c1, c2 = build_filler(rng, depth - 1, allow_fan2), build_filler(rng, depth - 2, allow_fan2)
        return TNode(1, [[('c', 0, 0), ('a', 1), ('c', 1, 0)]], [c1, c2])
    if kind == 'X':
        # two crossing fan-out-2 nodes:  q1.0 q2.0 q1.1 q2.1  (as in R15's G^cross)
        qs = []
        for _ in range(2):
            z1 = build_filler(rng, depth - 2, allow_fan2)
            z2 = build_filler(rng, depth - 2, allow_fan2)
            qs.append(TNode(2, [[('c', 0, 0)], [('c', 1, 0)]], [z1, z2]))
        return TNode(1, [[('c', 0, 0), ('c', 1, 0), ('c', 0, 1), ('c', 1, 1)]], qs)
    z1, z2 = build_filler(rng, depth - 1, allow_fan2), build_filler(rng, depth - 2, allow_fan2)
    y = build_filler(rng, depth - 1, allow_fan2)
    q = TNode(2, [[('c', 0, 0)], [('c', 1, 0)]], [z1, z2])
    return TNode(1, [[('c', 0, 0), ('c', 1, 0), ('c', 0, 1)]], [q, y])


def subtree_len(node):
    return sum(tn_comp_len(node, j) for j in range(node.fan))


# ==================================================================================
# [B] Lemma 1 and the class-elimination dichotomy on random trees
# ==================================================================================
def chain_next(w, theta):
    """R5 B5 / R9 (F4): descend along the longest child until the first node of length
    <= len(w)/4.  Returns (next, path) with path = nodes from w to the parent of next."""
    path = [w]
    cur = w
    while True:
        if not cur.children:
            return None, path
        ch = max(cur.children, key=lambda c: (nlen(c), -c.id))
        if 4 * nlen(ch) <= nlen(w):
            return ch, path
        path.append(ch)
        cur = ch


def side_branches(path, nxt):
    on = set(id(p) for p in path)
    out = []
    for p in path:
        for c in p.children:
            if id(c) not in on and c is not nxt:
                out.append(c)
    return out


def explicit_a(v):
    return sum(it[1] for comp in v.comps for it in comp if it[0] == 'a')


def eff_component(v):
    """effective component: the unique component whose escape contains a non-'a' letter,
    or None if both do (genuinely fan-out 2)."""
    if v.fan == 1:
        return 0
    nona = [j for j in range(2) if set(v.esc[j]) - {'a'}]
    return nona[0] if len(nona) == 1 else None


def pair_type(x, y):
    """Configuration of two incomparable nodes, following Lemma D / Corollary C.
    Returns one of 'D1' (disjoint, one effectively fan-out 1), 'D2' (both genuine,
    disjoint hulls), 'N' (one inside the gap of the other), 'C' (crossing)."""
    def eint(v):
        j = eff_component(v)
        return [v.ivals[j]] if j is not None else list(v.ivals)
    ix, iy = eint(x), eint(y)
    hx = (ix[0][0], ix[-1][1])
    hy = (iy[0][0], iy[-1][1])
    if hx[1] <= hy[0] or hy[1] <= hx[0]:
        return 'D1' if (len(ix) == 1 or len(iy) == 1) else 'D2'
    if len(ix) == 2 and ix[0][1] <= hy[0] and hy[1] <= ix[1][0]:
        return 'N'
    if len(iy) == 2 and iy[0][1] <= hx[0] and hx[1] <= iy[1][0]:
        return 'N'
    return 'C'


def section_B():
    say('[B] Lemma 1 and the class-elimination dichotomy (Theorem A) on random trees')
    theta = 3
    stats = Counter()
    ptypes = Counter()
    trees = 0
    for seed in range(40):
        rng = random.Random(1000 + seed)
        allow2 = (seed % 2 == 1)
        root = build_filler(rng, 9, allow_fan2=allow2)
        nodes = tn_layout(root)
        N = root.ivals[0][1]
        h = 0
        for v in nodes:
            d, p = 1, v.parent
            while p is not None:
                d, p = d + 1, p.parent
            h = max(h, d)
        r = max(len(v.children) for v in nodes)
        th = max(theta, max(explicit_a(v) for v in nodes))
        # classes: inherited along the longest child with probability 0.7 (to create
        # nested-only classes), random otherwise; 4 classes
        cls = {}
        for v in sorted(nodes, key=lambda v: -nlen(v)):
            if nlen(v) <= th:
                continue
            p = v.parent
            if p is not None and id(p) in cls and max(p.children, key=lambda c: (nlen(c), -c.id)) is v \
                    and rng.random() < 0.7:
                cls[id(v)] = cls[id(p)]
            else:
                cls[id(v)] = rng.randrange(4)
        # escapes (for the pair classification): random components over {c, d}, some pure
        for v in nodes:
            if v.children:
                v.esc = tuple(rng.choice(['c', 'cd', 'd', 'aa']) if (v.fan == 2 and j == 1) else
                              rng.choice(['c', 'cd', 'dc']) for j in range(v.fan))
        heavy = [v for v in nodes if nlen(v) > th and v is not root]
        for u in heavy:
            nxt, path = chain_next(u, th)
            if nxt is None:
                continue
            # Lemma 1 (i): ratio bounds
            check(4 * nlen(nxt) <= nlen(u), 'next <= len/4')
            if nlen(u) >= 8 * th:
                check(nlen(nxt) * 8 * r >= nlen(u) or nlen(nxt) >= (nlen(u) / 4 - th) / r,
                      'next >= (len/4 - theta)/r')
            check(len(path) <= h, 'path length <= height')
            sb = side_branches(path, nxt)
            tot = sum(nlen(c) for c in sb) + sum(explicit_a(p) for p in path)
            check(tot + nlen(nxt) == nlen(u), 'yield = side branches + explicit + next')
            check(len(sb) <= h * r, 'number of side branches <= h r')
            if sb:
                z = max(sb, key=lambda c: (nlen(c), -c.id))
                check(nlen(z) * len(sb) >= nlen(u) - nlen(nxt) - th * len(path),
                      'largest side branch >= average')
                # every node of subtree(z) is incomparable with next
                stack = [z]
                while stack:
                    a = stack.pop()
                    check(not comparable(a, nxt), 'side subtree incomparable with next')
                    stack.extend(a.children)
                # class-elimination dichotomy: K = class of some chain node below u
                sub = []
                stack = [u]
                while stack:
                    a = stack.pop()
                    if id(a) in cls:
                        sub.append(a)
                    stack.extend(a.children)
                chainK = set()
                w_ = nxt
                while w_ is not None and nlen(w_) > th:
                    if id(w_) in cls:
                        chainK.add(cls[id(w_)])
                    w_, _ = chain_next(w_, th)
                for K in sorted(chainK):
                    KV = [a for a in sub if cls[id(a)] == K]
                    has_pair = any(not comparable(a, b) for a, b in itertools.combinations(KV, 2))
                    zK = False
                    stack = [z]
                    while stack:
                        a = stack.pop()
                        if id(a) in cls and cls[id(a)] == K:
                            zK = True
                        stack.extend(a.children)
                    if not has_pair:
                        check(not zK, 'nested-only class avoids the side subtree')
                        stats['nested-only (case B)'] += 1
                    else:
                        stats['incomparable pair (case A)'] += 1
                    for a, b in itertools.combinations(KV, 2):
                        if not comparable(a, b):
                            ptypes[pair_type(a, b)] += 1
        trees += 1
    say('  %d random trees (half with fan-out-2 gadgets): dichotomy cases %s' % (
        trees, dict(sorted(stats.items()))))
    say('  same-class incomparable pairs by configuration (D1 disjoint with an effectively '
        'fan-out-1 member, D2 disjoint genuine, N nested, C crossing): %s' % dict(sorted(ptypes.items())))
    check(stats['nested-only (case B)'] > 0 and stats['incomparable pair (case A)'] > 0,
          'both cases of the dichotomy occur')
    check(ptypes['C'] > 0 and ptypes['N'] > 0, 'crossing and nested pairs occur in random trees')
    tlog('B')


# ==================================================================================
# [C] Theorem H-Xi* with the dissolvers of Lemma D2 and the two-frame prototype
# ==================================================================================
class RunBook:
    """Words a^{r0} B1 a^{r1} ... Bk a^{rk} over a-free blocks B_i on the host W = a^N.
    `natives[blocks] = runs` registers native words; `get(blocks, runs)` derives the word
    with the same blocks and the same number of a's by slides (Lemma P1'), each slide one
    two-hole SUB step from W, appended to self.steps."""

    def __init__(self, N):
        self.N = N
        self.W = 'a' * N
        self.natives = {}
        self.native_words = set([self.W])
        self.steps = []
        self.known = set()

    @staticmethod
    def word(blocks, runs):
        out = ['a' * runs[0]]
        for b, r in zip(blocks, runs[1:]):
            out.append(b)
            out.append('a' * r)
        return ''.join(out)

    def register(self, blocks, runs, w=None):
        blocks, runs = tuple(blocks), tuple(runs)
        wd = self.word(blocks, runs)
        if w is not None:
            assert wd == w, 'native word bookkeeping'
        lst = self.natives.setdefault(blocks, [])
        if runs not in lst:
            lst.append(runs)
        self.native_words.add(wd)
        return wd

    def _slide(self, blocks, runs, i, j, d):
        """move d a's from run i to run j (i != j); both runs stay >= 1."""
        N = self.N
        lo, hi = min(i, j), max(i, j)
        assert runs[i] - d >= 1 and runs[j] >= 1 and runs[i] + runs[j] <= N - 1
        assert hi > lo
        pre = ['a' * runs[0]]
        for b, r in zip(blocks[:lo], runs[1:lo + 1]):
            pre.append(b)
            pre.append('a' * r)
        U = ''.join(pre)[:sum(len(b) for b in blocks[:lo]) + sum(runs[:lo])]
        mid = []
        for k in range(lo, hi):
            mid.append(blocks[k])
            if k + 1 < hi:
                mid.append('a' * runs[k + 1])
        M = ''.join(mid)
        post = []
        for k in range(hi, len(blocks)):
            post.append(blocks[k])
            post.append('a' * runs[k + 1])
        V = ''.join(post)
        assert M != ''
        new = list(runs)
        new[i] -= d
        new[j] += d
        p1, q1 = runs[lo], runs[hi]
        p2, q2 = new[lo], new[hi]
        E0 = ('', 'a' * (N - p1 - q1), '')
        E1 = (U, M, V)
        x, y = ('a' * p1, 'a' * q1), ('a' * p2, 'a' * q2)
        assert fill(E1, x) == self.word(blocks, runs)
        out = fill(E1, y)
        assert out == self.word(blocks, new)
        self.steps.append((E0, E1, x, y))
        self.known.add(out)
        return tuple(new)

    def get(self, blocks, runs):
        blocks, runs = tuple(blocks), tuple(runs)
        target = self.word(blocks, runs)
        if target in self.known or target in self.native_words:
            return target
        cands = [c for c in self.natives[blocks] if sum(c) == sum(runs)
                 and all((c[k] == 0) == (runs[k] == 0) for k in range(len(runs)))]
        assert cands, 'no native word with these blocks and this a-budget'
        cur = cands[0]
        for k in range(len(runs)):
            assert (cur[k] == 0) == (runs[k] == 0), 'cannot create or delete a run'
        cur = list(cur)
        while tuple(cur) != runs:
            i = [k for k in range(len(cur)) if cur[k] > runs[k]][0]
            j = [k for k in range(len(cur)) if cur[k] < runs[k]][0]
            d = min(cur[i] - runs[i], runs[j] - cur[j])
            cur = list(self._slide(blocks, tuple(cur), i, j, d))
        out = self.word(blocks, tuple(cur))
        assert out == target
        return out


class Inst:
    """A synthetic node-minimal-tree instance: positions, escapes, weights."""

    def __init__(self, root):
        self.root = root
        self.nodes = tn_layout(root)
        self.N = root.ivals[0][1]
        self.book = RunBook(self.N)

    def comps(self, v):
        return tuple(v.esc)

    def p(self, v):
        """weight of the contiguous escape e_v (components joined by one 'a')."""
        return nlen(v) + (v.fan - 1)

    def e(self, v):
        return 'a'.join(v.esc)

    def iso_blocks(self, v):
        return self.comps(v)

    def register_native(self, antichain):
        w = native(self.N, self.nodes, antichain)
        reps = sorted((v.ivals[j][0], v.ivals[j][1], v.esc[j]) for v in antichain for j in range(v.fan))
        blocks, runs, i = [], [], 0
        for lo, hi, wd in reps:
            runs.append(lo - i)
            blocks.append(wd)
            i = hi
        runs.append(self.N - i)
        return self.book.register(blocks, runs, w), tuple(blocks), tuple(runs)

    # isolated placement of the contiguous escape: a^s e_v a^{R-s}
    def iso(self, v, s):
        R = self.N - self.p(v)
        runs = (s,) + (1,) * (v.fan - 1) + (R - s,)
        return self.book.get(self.comps(v), runs)

    def rel_COM(self, v):
        R = self.N - self.p(v)
        assert R >= 3
        E0 = ('a', 'a' * (R - 2))
        x, y = ('a' + self.e(v),), (self.e(v) + 'a',)
        assert fill(E0, x) == self.iso(v, 2) and fill(E0, y) == self.iso(v, 1)
        return E0, x, y

    def rel_EX(self, v, v2):
        N, pv, pv2 = self.N, self.p(v), self.p(v2)
        assert pv + pv2 <= N - 2
        E0 = ('a', 'a' * (N - pv - pv2 - 1))
        x = (self.e(v) + 'a' * pv2,)
        y = ('a' * pv + self.e(v2),)
        assert fill(E0, x) == self.iso(v, 1) and fill(E0, y) == self.iso(v2, 1 + pv)
        return E0, x, y


class Dissolver:
    """Lemma D2: pi0 = a component of a fan-out-2 node v*, w* placed natively
      mode 'gap'  : inside the gap of v*, block right after omega^1 (pi0 = omega^1),
      mode 'right': right of the hull of v*, block right after omega^2 (pi0 = omega^2).
    The relation   pi0 a^g e_w a  ==  pi0 a^{g+p_w+1}   (one hole), 1 <= g <= gmax."""

    def __init__(self, inst, vs, ws, mode):
        self.I, self.vs, self.ws, self.mode = inst, vs, ws, mode
        self.pi0 = vs.esc[0] if mode == 'gap' else vs.esc[1]
        assert vs.fan == 2
        self.lv = nlen(vs)
        self.pw = inst.p(ws)

    def gmax(self):
        return self.I.N - self.lv - self.pw - 4

    def rel(self, g):
        I, vs, ws = self.I, self.vs, self.ws
        N, lv, pw = I.N, self.lv, self.pw
        assert 1 <= g <= self.gmax()
        w1, w2 = vs.esc
        wc = I.comps(ws)
        x = (self.pi0 + 'a' * g + I.e(ws) + 'a',)
        y = (self.pi0 + 'a' * (g + pw + 1),)
        r = N - lv - pw - g - 3
        if self.mode == 'gap':
            E0 = ('a', 'a' * r + w2 + 'a')
            blocks_x = (w1,) + wc + (w2,)
            runs_x = (1, g) + (1,) * (len(wc) - 1) + (1 + r, 1)
            blocks_y = (w1, w2)
            runs_y = (1, g + pw + 1 + r, 1)
        else:
            E0 = ('a' + w1 + 'a', 'a' * r)
            blocks_x = (w1, w2) + wc
            runs_x = (1, 1, g) + (1,) * (len(wc) - 1) + (1 + r,)
            blocks_y = (w1, w2)
            runs_y = (1, 1, g + pw + 1 + r)
        assert fill(E0, x) == I.book.get(blocks_x, runs_x)
        assert fill(E0, y) == I.book.get(blocks_y, runs_y)
        return E0, x, y


def apply_rel(cur, pos, rel):
    E0, x, y = rel
    assert cur[pos:pos + len(x[0])] == x[0], 'factor mismatch'
    E1 = (cur[:pos], cur[pos + len(x[0]):])
    return (E0, E1, x, y), fill(E1, y)


def reverse_chain(chain):
    return [(E0, E1, y, x) for (E0, E1, x, y) in reversed(chain)]


class KBlock:
    """Theorem NF* on a K-block led by pi0:
       family word = PhiL pi0 a^g e_w (a^g e_y)_{slots} a^{g_last} PhiR."""

    def __init__(self, inst, dis, PhiL, PhiR, g, q0):
        self.I, self.D = inst, dis
        self.PhiL, self.PhiR, self.g, self.q0 = PhiL, PhiR, g, q0
        self.proto = PhiL + dis.pi0 + 'a' * q0 + PhiR

    def g_last(self, slots):
        I = self.I
        return self.q0 - (len(slots) + 1) * self.g - self.D.pw - sum(I.p(y) for y in slots)

    def word(self, slots, g_last):
        I, g = self.I, self.g
        assert g_last >= 1
        X = self.D.pi0 + 'a' * g + I.e(self.D.ws)
        for y in slots:
            X += 'a' * g + I.e(y)
        X += 'a' * g_last
        return self.PhiL + X + self.PhiR

    def nf_chain(self, word, slots, g_last):
        I, D, g = self.I, self.D, self.g
        pw = D.pw
        pos0 = len(self.PhiL)
        chain = []
        cur = word
        rights = [g] * len(slots) + [g_last]
        st, cur = apply_rel(cur, pos0, D.rel(g))
        chain.append(st)
        H = g + pw + 1 + (rights[0] - 1)
        for idx, y in enumerate(slots):
            ey = I.e(y)
            h = rights[idx + 1]
            p_ey = pos0 + len(D.pi0) + H
            assert cur[p_ey:p_ey + len(ey)] == ey
            for _ in range(max(0, pw + 1 - h)):
                st, cur = apply_rel(cur, p_ey - 1, I.rel_COM(y))
                chain.append(st)
                p_ey -= 1
                H -= 1
            hh = max(h, pw + 1)
            st, cur = apply_rel(cur, p_ey, I.rel_EX(y, D.ws))
            chain.append(st)
            H2 = H + I.p(y)
            st, cur = apply_rel(cur, pos0, D.rel(H2))
            chain.append(st)
            H = H2 + pw + 1 + (hh - pw - 1)
        return chain, cur, H

    def rigidity_step(self, q_small, q_big):
        """Lemma P7 with left context PhiL pi0: two words differing in one a-run => shortcut."""
        N = self.I.N
        E0 = (self.PhiL + self.D.pi0, self.PhiR)
        E1 = ('', 'a' * (N - q_big))
        return (E0, E1, ('a' * q_big,), ('a' * q_small,))


def prototype_phi2(inst, vs, side_after_comp, qmin, slack=30):
    """Lemma Phi2 (two-frame version of R9's Phi-gamma): E = frame(v*) u {beta}, beta the
    position right after component `side_after_comp` of v*; pieces = maximal nodes disjoint
    from E; greedy: keep pieces pure while the budget lasts, split the first overflowing
    piece, escape the rest; then slide every a-run into the run at beta (each other run
    keeps one letter).  Returns (PhiL, PhiR, q0, |C|, slides)."""
    N, nodes = inst.N, inst.nodes
    beta = vs.ivals[side_after_comp][1]
    Epts = npos(vs) | {beta}
    budget = qmin + slack
    for _attempt in range(12):
        pieces = []

        def collect(nd):
            if nd is vs:
                return
            P = npos(nd)
            if not (P & Epts):
                pieces.append(nd)
                return
            for ch in nd.children:
                collect(ch)
        collect(inst.root)
        pieces.sort(key=lambda nd: nd.ivals[0][0])
        covered = set()
        for pc in pieces:
            covered |= npos(pc)
        fixed_a = N - len(npos(vs)) - len(covered)       # crossing explicit letters, beta
        remaining = budget - fixed_a
        queue_ = list(pieces)
        esc_nodes = []
        while queue_:
            P = queue_.pop(0)
            if not P.children:
                remaining -= nlen(P)
                continue
            if remaining <= 0:
                esc_nodes.append(P)
                continue
            if nlen(P) <= remaining:
                remaining -= nlen(P)
                continue
            remaining -= explicit_a(P)
            queue_ = sorted(P.children, key=lambda nd: nd.ivals[0][0]) + queue_
        anti = [vs] + esc_nodes
        w, blocks, runs = inst.register_native(anti)
        # index of the block pi0 = component side_after_comp of v*
        reps = sorted((v.ivals[j][0], v is vs and j == side_after_comp) for v in anti for j in range(v.fan))
        k0 = [k for k, (_, flag) in enumerate(reps) if flag][0]
        tgt = k0 + 1
        assert runs[tgt] >= 1
        new = list(runs)
        total_movable = 0
        for k in range(len(new)):
            if k != tgt and new[k] >= 1:
                total_movable += new[k] - 1
                new[k] = 1
        new[tgt] += total_movable
        q0 = new[tgt]
        if q0 < qmin:
            budget += qmin - q0 + 5
            continue
        before = len(inst.book.steps)
        word = inst.book.get(blocks, tuple(new))
        PhiL = RunBook.word(blocks[:k0], tuple(new[:k0 + 1]))
        PhiR = RunBook.word(blocks[tgt:], (0,) + tuple(new[tgt + 1:]))
        assert PhiL + blocks[k0] + 'a' * q0 + PhiR == word
        return PhiL, PhiR, q0, len(esc_nodes), len(inst.book.steps) - before
    raise AssertionError('prototype budget did not converge')


def family_chain(rng, m, base_depth):
    """Nested chain F_1 > F_2 > ... > F_m of fan-out-1 nodes, ratio >= 4 (Lemma 1 shape):
    F_j -> F_{j+1} filler_j with |filler_j| >= 3 |F_{j+1}|."""
    inner = build_filler(rng, base_depth, allow_fan2=False)
    inner.tag = 'F%d' % m
    chain = [inner]
    cur = inner
    for j in range(m - 1, 0, -1):
        L = subtree_len(cur)
        d = 1
        while True:
            f = build_filler(rng, d, allow_fan2=True)
            if subtree_len(f) >= 3 * L:
                break
            d += 1
        node = TNode(1, [[('c', 0, 0), ('c', 1, 0)]], [cur, f], tag='F%d' % j)
        chain.insert(0, node)
        cur = node
    return chain


def assign_filler_escapes(rng, nodes):
    for v in nodes:
        if v.children and v.esc is None:
            v.esc = tuple(''.join(rng.choice('de') for _ in range(rng.randint(1, 2)))
                          for _ in range(v.fan))


def run_hxi_star(inst, dis, fam, label, prng):
    """Build the prototype, force random family words, plant swaps."""
    I = inst
    g = 3
    Mf = len(fam)
    qmin = dis.pw + (Mf + 1) * g + sum(I.p(y) for y in fam) + 1
    side = 0 if dis.mode == 'gap' else 1
    PhiL, PhiR, q0, nC, nsl = prototype_phi2(I, dis.vs, side, qmin)
    check(q0 >= qmin and q0 <= qmin + 80, '%s: prototype run in range' % label)
    check(q0 + I.p(dis.ws) <= dis.gmax() + dis.pw, '%s: dissolver range covers the block' % label)
    kb = KBlock(I, dis, PhiL, PhiR, g, q0)
    proto = kb.proto
    natives = I.book.native_words
    seed_member = lambda u: u in natives
    forced = 0
    nsteps = []
    for _ in range(6):
        slots = prng.sample(fam, Mf)
        gl = kb.g_last(slots)
        w = kb.word(slots, gl)
        chain, end, H = kb.nf_chain(w, slots, gl)
        check(end == proto, '%s: NF* ends at the prototype' % label)
        cert = list(I.book.steps) + reverse_chain(chain)
        o, _ = replay(cert, seed_member)
        check(o == w, '%s: forcing certificate replays from native words' % label)
        classify(reverse_chain(chain))
        nsteps.append(len(chain))
        forced += 1
    swaps = 0
    for _ in range(40):
        a = prng.randint(0, Mf - 1)
        b = prng.randint(a + 1, Mf)
        p1 = prng.sample(fam, Mf)
        p2 = prng.sample(fam, Mf)
        mix = p2[:a] + p1[a:b] + p2[b:]
        if sum(I.p(x) for x in p1[a:b]) == sum(I.p(x) for x in p2[a:b]):
            continue
        gl = kb.g_last(p2)
        xp = kb.word(mix, gl)
        chain, end, H = kb.nf_chain(xp, mix, gl)
        if H == q0 or max(H, q0) > I.N:
            continue
        rig = kb.rigidity_step(min(H, q0), max(H, q0))
        cert = list(I.book.steps) + chain + [rig]
        o, _ = replay(cert, lambda u, xp=xp: u == xp or u in natives)
        check(o == 'a' * (I.N - abs(H - q0)), '%s: planted swap forces a shortcut' % label)
        classify(chain + [rig])
        swaps += 1
        if swaps >= 4:
            break
    check(swaps >= 2, '%s: some planted swaps' % label)
    classify(I.book.steps)
    return dict(q0=q0, qmin=qmin, nC=nC, phi=len(PhiL) + len(PhiR), forced=forced,
                swaps=swaps, steps=nsteps)


def build_gadget_instance(seed, mode, w_fan):
    """root = [left filler | G | F_1 | right filler] with the gadget G containing v*
    (fan-out 2) and w* (class {a,c}) either inside the gap of v* ('gap') or right of its
    hull ('right'); F_1 > ... > F_m is the nested family chain of class {a,c}."""
    rng = random.Random(seed)
    m = 5
    fam = family_chain(rng, m, 1)
    X1, X2 = build_filler(rng, 5), build_filler(rng, 5)
    vs = TNode(2, [[('c', 0, 0)], [('c', 1, 0)]], [X1, X2], tag='v*')
    if w_fan == 1:
        ws = build_filler(rng, 4, allow_fan2=False)
        ws.tag = 'w*'
    else:
        Y1, Y2 = build_filler(rng, 3), build_filler(rng, 3)
        ws = TNode(2, [[('c', 0, 0)], [('c', 1, 0)]], [Y1, Y2], tag='w*')
    Y = build_filler(rng, 5)
    after = build_filler(rng, 5)
    if mode == 'gap':
        if w_fan == 1:
            comps = [[('c', 0, 0), ('a', 1), ('c', 1, 0), ('a', 1), ('c', 2, 0), ('c', 0, 1),
                      ('c', 3, 0)]]
        else:
            comps = [[('c', 0, 0), ('a', 1), ('c', 1, 0), ('c', 2, 0), ('c', 1, 1), ('a', 1),
                      ('c', 0, 1), ('c', 3, 0)]]
        G = TNode(1, comps, [vs, ws, Y, after], tag='G')
    else:
        if w_fan == 1:
            comps = [[('c', 0, 0), ('c', 2, 0), ('c', 0, 1), ('a', 1), ('c', 1, 0), ('a', 1),
                      ('c', 3, 0)]]
        else:
            comps = [[('c', 0, 0), ('c', 2, 0), ('c', 0, 1), ('a', 1), ('c', 1, 0), ('c', 3, 0),
                      ('c', 1, 1), ('a', 1)]]
        G = TNode(1, comps, [vs, ws, Y, after], tag='G')
    Lf, Rf = build_filler(rng, 12), build_filler(rng, 12)
    root = TNode(1, [[('c', 0, 0), ('c', 1, 0), ('c', 2, 0), ('c', 3, 0)]], [Lf, G, fam[0], Rf],
                 tag='root')
    inst = Inst(root)
    # escapes: family and w*: only 'c'; v*: component carrying c on the used side
    for k, f in enumerate(fam):
        f.esc = ('c' * (1 + k),)          # distinct escape words (R5 B1: one word, one weight)
    ws.esc = ('c' * 7,) if w_fan == 1 else ('cc', 'c')
    if mode == 'gap':
        vs.esc = ('cd', 'e')       # cl_1 = {a,c,d} contains {a,c}; cl_2 = {a,e} does not
    else:
        vs.esc = ('c', 'c')        # a genuine fan-out-2 node of class {a,c}
    assign_filler_escapes(rng, inst.nodes)
    for v in inst.nodes:
        if v.children:
            assert 'a' not in ''.join(v.esc)
    return inst, vs, ws, fam


def section_C():
    say('[C] Theorem H-Xi* with the dissolvers of Lemma D2 (fan-out-2 v*) and Lemma Phi2')
    prng = random.Random(77)
    rows = []
    for (seed, mode, w_fan) in ((11, 'gap', 1), (16, 'gap', 2), (13, 'right', 1), (14, 'right', 2)):
        I, vs, ws, fam = build_gadget_instance(seed, mode, w_fan)
        N = I.N
        # natives: W, isolated words of v*, w*, family; the native pair word {v*, w*}
        for v in [vs, ws] + fam:
            I.register_native([v])
        I.register_native([vs, ws])
        check(not comparable(vs, ws), 'pair incomparable')
        hv, hw = hull(vs), hull(ws)
        if mode == 'gap':
            check(vs.ivals[0][1] <= hw[0] and hw[1] <= vs.ivals[1][0], 'w* inside the gap of v*')
        else:
            check(hv[1] <= hw[0], 'w* right of the hull of v*')
        nested = sum(1 for a, b in itertools.combinations(fam, 2) if comparable(a, b))
        check(nested == len(fam) * (len(fam) - 1) // 2, 'family is a nested chain')
        check(all(4 * nlen(fam[k + 1]) <= nlen(fam[k]) for k in range(len(fam) - 1)),
              'family ratio >= 4 (superincreasing weights)')
        check(16 * (nlen(vs) + I.p(ws) + sum(I.p(y) for y in fam)) <= 3 * N, 'margins')
        # the family members must not be comparable with v* or w*? -- not needed (Lemma NF*)
        dis = Dissolver(I, vs, ws, mode)
        res = run_hxi_star(I, dis, fam, '%s/w-fan%d' % (mode, w_fan), prng)
        rows.append((seed, mode, w_fan, N, [I.p(y) for y in fam], I.p(ws), nlen(vs), vs.esc, res))
    for (seed, mode, w_fan, N, wts, pw, lv, vesc, res) in rows:
        say('  seed %d, w* %s, fan-out(w*)=%d: N=%d, |v*|=%d, esc(v*)=%s, p(w*)=%d, family '
            'weights (nested chain) %s' % (seed, 'inside the gap of v*' if mode == 'gap' else
                                         'right of the hull of v*', w_fan, N, lv, vesc, pw, wts))
        say('    prototype (Lemma Phi2): |C|=%d escaped pieces, |PhiL|+|PhiR|=%d, run after pi0 = '
            '%d (needed >= %d); forced %d/6 random family words (NF* chains of %s steps, '
            'replayed with all slide/COM/EX/DIS premises from native words); planted swaps -> '
            'shortcut: %d' % (res['nC'], res['phi'], res['q0'], res['qmin'], res['forced'],
                              sorted(set(res['steps'])), res['swaps']))
    # print one dissolver step in full (the four words)
    I, vs, ws, fam = build_gadget_instance(11, 'gap', 1)
    for v in [vs, ws] + fam:
        I.register_native([v])
    I.register_native([vs, ws])
    dis = Dissolver(I, vs, ws, 'gap')
    E0, x, y = dis.rel(3)
    say('  one D2 (gap) dissolution in full, g=3 (one hole; types %s = %s):' % (
        ''.join(sorted(content(x[0]))), ''.join(sorted(content(y[0])))))
    say('    x = %s   y = %s' % (x[0], y[0]))
    say('    E0 = (%s, %s)' % (E0[0], E0[1][:20] + '...%d letters...' % len(E0[1]) + E0[1][-3:]))
    say('    E0[x] = native pair word {v*, w*} after slides;  E0[y] = native word {v*} after slides')
    tlog('C')


# ==================================================================================
# [D] nested-only chain class
# ==================================================================================
def nested_spine_tokens(n):
    """Token-level native words of  S -> a A_n a,  A_t -> A_{t-1} D_{t-1} | C_t,
    D_t -> D_{t-1} D_{t-1} | E_t,  A_0 = D_0 = a.   C_t: uppercase (class c), E_t: digit
    (class d).  The class c occurs only on the chain A_n > A_{n-1} > ... (nested only)."""
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def D(t):
        if t == 0:
            return ('a',)
        res = set(x + y for x in D(t - 1) for y in D(t - 1))
        res.add(str(t))
        return tuple(sorted(res))

    @lru_cache(maxsize=None)
    def A(t):
        if t == 0:
            return ('a',)
        res = set(x + y for x in A(t - 1) for y in D(t - 1))
        res.add(chr(ord('A') + t))
        return tuple(sorted(res))
    return set('a' + x + 'a' for x in A(n))


def ty_nest(w):
    return frozenset(('c' if ch.isupper() else 'd' if ch.isdigit() else ch) for ch in w)


def tok_weight(w):
    tot = 0
    for ch in w:
        if ch == 'a':
            tot += 1
        elif ch.isdigit():
            tot += 1 << int(ch)
        else:
            tot += 1 << (ord(ch) - ord('A'))
    return tot


def section_D():
    say('[D] nested-only chain class')
    for n in (3,):
        seeds = nested_spine_tokens(n)
        N = (1 << n) + 2
        C = Closure(seeds, ty_nest, max_words=400000,
                    stop=lambda w: set(w) == {'a'} and len(w) != N).run()
        ex = is_closed_exact(C.S, ty_nest) if (not C.truncated and n == 3) else None
        twoC = [w for w in C.S if sum(1 for ch in w if ch.isupper()) >= 2]
        twoE = [w for w in C.S if sum(1 for ch in w if ch.isdigit()) >= 2 and not any(ch.isupper() for ch in w)]
        nat_twoE = [w for w in seeds if sum(1 for ch in w if ch.isdigit()) >= 2 and not any(ch.isupper() for ch in w)]
        wts = Counter(tok_weight(w) for w in C.S)
        say('  (D1) n=%d (W=a^%d): %d native token words -> closure %d words%s, exactly '
            'substitutable: %s, shortcut: %s, weights %s' % (
                n, N, len(seeds), len(C.S), ' (TRUNCATED: nothing claimed)' if C.truncated else '',
                ex, C.found, dict(sorted(wts.items()))))
        say('       words with >= 2 c-class escapes: %d;  words with >= 2 d-class escapes and no '
            'c-escape: %d native -> %d in the closure' % (len(twoC), len(nat_twoE), len(twoE)))
        if n == 3:
            check(not C.truncated and ex and C.found is None, 'nested spine n=3: exact closure, no shortcut')
            check(len(twoC) == 0, 'nested spine n=3: no word with two c-escapes is forced')
            check(len(twoE) > len(nat_twoE), 'nested spine n=3: the d-class gains non-native arrangements')
        else:
            if not C.truncated:
                check(C.found is None and len(twoC) == 0, 'nested spine n=4: no two c-escapes')
    # (D2) letter level: closure of {a^N} u {a^s e_i a^t : s,t >= 1, s+t = N - p_i}
    def nblocks(w):
        return sum(1 for k in range(len(w)) if w[k] != 'a' and (k == 0 or w[k - 1] == 'a'))
    for (N, esc, pv, expect_ok) in ((16, ('cd', 'dcc', 'ddc'), (3, 6, 12), True),
                                     (16, ('ccd', 'cdc', 'cdd'), (2, 5, 11), True),
                                     (13, ('bcb', 'bccb'), (3, 5), False)):
        L = set(['a' * N])
        for e, p in zip(esc, pv):
            for s_ in range(1, N - p):
                L.add('a' * s_ + e + 'a' * (N - p - s_))
        C = Closure(L, content, max_words=5000, stop=lambda w, N=N: set(w) == {'a'} and len(w) < N).run()
        ex = is_closed_exact(C.S, content) if not C.truncated else None
        two = [w for w in C.S if nblocks(w) >= 2]
        new = sorted(C.S - L, key=lambda w: (len(w), w))
        kls = sorted(set(''.join(sorted(set(e) | {'a'})) for e in esc))
        say('  (D2) N=%d, escapes %s (class %s), weights %s: seeds %d -> closure %d '
            '(exact: %s), shortcut: %s, words with two escape blocks: %d, new words e.g. %s' % (
                N, esc, '/'.join(kls), pv, len(L), len(C.S), ex, C.found, len(two), new[:3]))
        if expect_ok:
            check(not C.truncated and ex and C.found is None and not two,
                  'letter-level nested escapes: closed, no shortcut, no two-escape word')
        else:
            check(C.found is None and len(two) == 0, 'calibration case')
    tlog('D')


# ==================================================================================
# [E] the R15 order-invariant language L_{N,d}
# ==================================================================================
def in_Lnd(w, N, d):
    pi = ''.join(ch for ch in w if ch != 'a')
    if set(w) - set('abc'):
        return False
    k = pi.find('c')
    if k >= 0 and 'b' in pi[k:]:
        return False
    nb, nc = w.count('b'), w.count('c')
    return nb == nc and w.count('a') + d * nb == N and len(w) > 0


def enum_Lnd(N, d):
    out = set()
    for k in range(0, N // d + 1):
        na = N - d * k
        if na < 0:
            continue
        L = na + 2 * k
        for pos in itertools.combinations(range(L), 2 * k):
            w = ['a'] * L
            for idx, p in enumerate(pos):
                w[p] = 'b' if idx < k else 'c'
            out.add(''.join(w))
    return out


def gcross_tree(d, q):
    """Node-minimal a^N derivation of G^{cross}_{d,q} (R15 Sect. 5.1):
    S -> a X1 a X2 a (B_q),  B_i -> (X1 Y1, X2 Y2)(B_{i-1}, B_{i-1}),  B_0 -> (a^{d/2}, a^{d/2})."""
    def B(i):
        if i == 0:
            return TNode(2, [[('a', d // 2)], [('a', d // 2)]], [], tag='B0')
        x, y = B(i - 1), B(i - 1)
        return TNode(2, [[('c', 0, 0), ('c', 1, 0)], [('c', 0, 1), ('c', 1, 1)]], [x, y], tag='B%d' % i)
    top = B(q)
    root = TNode(1, [[('a', 1), ('c', 0, 0), ('a', 1), ('c', 0, 1), ('a', 1)]], [top], tag='S')
    return root


def section_E():
    say('[E] the R15 order-invariant language L_{N,d} (two-letter split class)')
    for (d, q) in ((4, 1), (6, 1)):
        N = d * (1 << q) + 3
        L = enum_Lnd(N, d)
        ok = is_closed_exact(L, content)
        check(ok, 'L_{N,d} exactly (2,c)-substitutable')
        check(all(in_Lnd(w, N, d) for w in L), 'predicate')
        say('  d=%d q=%d N=%d: |L|=%d, exactly (2,c)-substitutable (all one- and two-hole '
            'occurrences): %s' % (d, q, N, len(L), ok))
    # original thickness of G^cross_{d,q} by inside/outside shortest lengths (R15 Sect. 5.1, 5.3)
    def theta_gcross(d, q):
        N = d * (1 << q) + 3
        rules = []        # (lhs, explicit letters, children)
        rules.append(('A1', 1, []))
        rules.append(('A%d' % d, 2, []))
        for n in range(2, N + 1):
            rules.append(('A%d' % n, 1, ['A%d' % (n - 1)]))
            rules.append(('A%d' % n, 1, ['A%d' % (n - 1)]))
            if n >= d + 1:
                rules.append(('A%d' % n, 2, ['A%d' % (n - d)]))
        rules.append(('B0', d, []))
        rules.append(('B0', 2, []))
        for i in range(1, q + 1):
            rules.append(('B%d' % i, 0, ['B%d' % (i - 1), 'B%d' % (i - 1)]))
        rules.append(('S', 0, ['A%d' % N]))
        rules.append(('S', 3, ['B%d' % q]))
        INF = 10 ** 9
        nts = sorted(set(r[0] for r in rules))
        inn = {X: INF for X in nts}
        changed = True
        while changed:
            changed = False
            for (X, e, ch) in rules:
                v = e + sum(inn[c] for c in ch)
                if v < inn[X]:
                    inn[X], changed = v, True
        out = {X: INF for X in nts}
        out['S'] = 0
        changed = True
        while changed:
            changed = False
            for (X, e, ch) in rules:
                if out[X] >= INF:
                    continue
                for k, c in enumerate(ch):
                    v = out[X] + e + sum(inn[cc] for kk, cc in enumerate(ch) if kk != k)
                    if v < out[c]:
                        out[c], changed = v, True
        th = max(out[X] + e + sum(inn[c] for c in ch) for (X, e, ch) in rules)
        return N, th, inn
    Nc, thc, innc = theta_gcross(6, 3)
    check(thc == (1 << 4) + 6 + 1, 'theta_bar(G^cross_{6,3}) = 2^{q+1}+d+1 = 23')
    check(innc['B2'] == 8, 'shortest yield of B_2 has length 8 = |(b^4, c^4)|')
    say('  original thickness of G^cross_{6,3} by inside/outside shortest lengths: theta_bar = %d '
        '(R15: 2^{q+1}+d+1 = 23); shortest yield of B_2: %d letters' % (thc, innc['B2']))
    # the interleaved configuration in the node-minimal tree, d=6, q=3 (N=51, theta=23)
    d, q = 6, 3
    N = d * (1 << q) + 3
    theta = (1 << (q + 1)) + d + 1
    root = gcross_tree(d, q)
    nodes = tn_layout(root)
    check(root.ivals[0][1] == N, 'G^cross tree yields a^N')
    heavy = [v for v in nodes if nlen(v) > theta and v is not root]
    for v in nodes:
        if v.tag.startswith('B'):
            i = int(v.tag[1:])
            v.esc = ('b' * (1 << i), 'c' * (1 << i))      # the shortest yield of B_i
    hv = [v for v in heavy if v.tag == 'B%d' % (q - 1)]
    check(len(hv) == 2, 'two heavy B_{q-1} nodes')
    x, y = hv
    check(not comparable(x, y), 'incomparable')
    check(pair_type(x, y) == 'C', 'crossing pair')
    # forced: every yield of B_{q-1} shorter than its own uses b,c (all pure yields have length d 2^{q-1})
    check(nlen(x) == d * (1 << (q - 1)), 'pure yields of B_{q-1} have one length')
    iso_x = native(N, nodes, [x])
    pair = native(N, nodes, [x, y])
    check(in_Lnd(iso_x, N, d) and in_Lnd(pair, N, d), 'isolated and crossing pair words in L')
    ex = 'b' * 4 + 'a' + 'c' * 4
    # concatenated placements of the two kernels (block transposition): never in L
    conc = 0
    tot = N - 2 * (d * 4)
    for s in range(1, tot):
        for gq in range(1, tot - s):
            t = tot - s - gq
            if t < 1:
                continue
            w = 'a' * s + ex + 'a' * gq + ex + 'a' * t
            conc += in_Lnd(w, N, d)
    check(conc == 0, 'no concatenated pair placement')
    # crossing-order and mismatched two-sided words
    left = lambda ms: 'a'.join('b' * m for m in ms)
    right = lambda ms: 'a'.join('c' * m for m in ms)
    def twos(ml, mr):
        core_b, core_c = left(ml), right(mr)
        na = N - d * sum(ml) - (len(ml) - 1) - (len(mr) - 1)
        return 'a' + core_b + 'a' * (na - 2) + core_c + 'a'
    wm = twos([4, 2], [4, 2])
    wr = twos([4, 2], [2, 4])
    wx = twos([4, 4], [4, 2])
    check(in_Lnd(wm, N, d) and in_Lnd(wr, N, d) and not in_Lnd(wx, N, d), 'two-sided words')
    say('  node-minimal tree of G^cross_{6,3}: N=%d, theta_bar=%d (R15 Sect. 5.3); the two '
        'heavy B_2 nodes are incomparable, forced, of class {a,b,c} with component classes '
        '({a,b},{a,c}), and crossing (hulls %s, %s)' % (N, theta, hull(x), hull(y)))
    say('    isolated placement and crossing pair word lie in L; concatenated placements '
        'a^s (b^4 a c^4) a^g (b^4 a c^4) a^t in L: %d (all splits); two-sided words: matched '
        '%s, right parts permuted %s, mismatched (left 4+4, right 4+2) %s' % (
            conc, in_Lnd(wm, N, d), in_Lnd(wr, N, d), in_Lnd(wx, N, d)))
    tlog('E')


# ==================================================================================
# [F] the two-sided normal form NF2 on a synthetic crossing pair; numbers
# ==================================================================================
def section_F():
    say('[F] two-sided normal form NF2 (crossing pair) and the numerical comparison of bounds')
    rng = random.Random(31)
    # gadget: v* = (X1, X2), w* = (Y1, Y2) crossing: v1 w1 v2 w2; family of genuinely
    # fan-out-2 nodes y_j = (P_j, Q_j) placed far away (disjoint), componentwise classes ({a,c},{a,e})
    X1, X2, Y1, Y2 = (build_filler(rng, 5) for _ in range(4))
    vs = TNode(2, [[('c', 0, 0)], [('c', 1, 0)]], [X1, X2], tag='v*')
    ws = TNode(2, [[('c', 0, 0)], [('c', 1, 0)]], [Y1, Y2], tag='w*')
    G1, G2, G3 = (build_filler(rng, 5) for _ in range(3))
    gad = TNode(1, [[('c', 0, 0), ('c', 2, 0), ('c', 1, 0), ('c', 3, 0), ('c', 0, 1), ('c', 4, 0),
                     ('c', 1, 1), ('a', 1)]], [vs, ws, G1, G2, G3], tag='G')
    fam = []
    holders = []
    for j in range(4):
        P, Q, M = build_filler(rng, 3 + j), build_filler(rng, 3 + j), build_filler(rng, 2)
        yj = TNode(2, [[('c', 0, 0)], [('c', 1, 0)]], [P, Q], tag='y%d' % j)
        fam.append(yj)
        holders.append(TNode(1, [[('c', 0, 0), ('c', 1, 0), ('c', 0, 1)]], [yj, M]))
    Lf = build_filler(rng, 9)
    root = TNode(1, [[('c', 0, 0), ('c', 1, 0)] + [('c', 2 + j, 0) for j in range(4)]
                     + [('c', 6, 0)]], [Lf, gad] + holders + [build_filler(rng, 9)], tag='root')
    I = Inst(root)
    vs.esc = ('cd', 'ce')
    ws.esc = ('c', 'e')
    for j, yj in enumerate(fam):
        yj.esc = ('c' * (1 + j % 2), 'e' * (1 + (j + 1) % 2))
    assign_filler_escapes(rng, I.nodes)
    N = I.N
    check(pair_type(vs, ws) == 'C', 'crossing gadget')
    for v in [vs, ws] + fam:
        I.register_native([v])
    I.register_native([vs, ws])
    bk = I.book
    lv, lw = nlen(vs), nlen(ws)
    Rv = N - lv                                   # a's in an isolated v*-word

    # two-hole relations as (E0, x, y)
    def rel_DIS2(g, g2, y1):
        """(w1v a^g w1w a, w2v a^g2 w2w a) ==_2 (w1v a^{y1}, w2v a^{y2}),
        y1 + y2 = g + g2 + lw + 2; from the crossing native pair word and isolated v*."""
        y2 = g + g2 + lw + 2 - y1
        assert y1 >= 1 and y2 >= 1
        c = 1
        t = Rv - lw - 1 - g - c - g2 - 1 - 1
        assert t >= 1
        E0 = ('a', 'a' * c, 'a' * t)
        x = (vs.esc[0] + 'a' * g + ws.esc[0] + 'a', vs.esc[1] + 'a' * g2 + ws.esc[1] + 'a')
        y = (vs.esc[0] + 'a' * y1, vs.esc[1] + 'a' * y2)
        bx = bk.get((vs.esc[0], ws.esc[0], vs.esc[1], ws.esc[1]), (1, g, 1 + c, g2, 1 + t))
        by = bk.get((vs.esc[0], vs.esc[1]), (1, y1 + c, y2 + t))
        assert fill(E0, x) == bx and fill(E0, y) == by
        return E0, x, y

    def rel_EX2(yj):
        """(a^{1+delta} w1y a, a w2y a) ==_2 (a w1w a, a w2w a), delta = l_w - l_y >= 0
        (for delta < 0 the |delta| extra a's stand before w1w); premises: the isolated
        words of y_j and of w*."""
        ly = nlen(yj)
        G = 5
        delta = lw - ly
        dx, dy = max(0, delta), max(0, -delta)
        t = N - ly - G - 3 - dx
        assert t >= 1
        E0 = ('a', 'a' * (G - 2), 'a' * t)
        x = ('a' * (1 + dx) + yj.esc[0] + 'a', 'a' + yj.esc[1] + 'a')
        y = ('a' * (1 + dy) + ws.esc[0] + 'a', 'a' + ws.esc[1] + 'a')
        bx = bk.get(I.comps(yj), (2 + dx, G, 1 + t))
        by = bk.get(I.comps(ws), (2 + dy, G, 1 + t))
        assert fill(E0, x) == bx and fill(E0, y) == by
        return E0, x, y

    # a two-sided family word (crossing order on both sides) and the NF2 reduction
    g = 3
    def twoside(order, H1, H2):
        Lb = vs.esc[0] + 'a' * g + ws.esc[0]
        Rb = vs.esc[1] + 'a' * g + ws.esc[1]
        for yj in order:
            Lb += 'a' * g + yj.esc[0]
            Rb += 'a' * g + yj.esc[1]
        return 'a' + Lb + 'a' * H1 + Rb + 'a' * H2

    total_a = Rv - lw - sum(nlen(y) for y in fam)   # a's of the two-sided word (weights add)
    certs = 0
    for trial in range(5):
        order = rng.sample(fam, len(fam))
        nblk = len(fam) + 1
        H1 = 4
        H2 = total_a - 1 - 2 * g * nblk - H1
        w = twoside(order, H1, H2)
        cur = w
        chain = []
        # dissolve w*, then each family member in order: EX2 then DIS2
        def locate(cur):
            p1 = cur.index(vs.esc[0])
            p2 = cur.index(vs.esc[1], p1 + len(vs.esc[0]))
            return p1, p2

        def apply2(cur, rel, p1, p2):
            E0, x, y = rel
            assert cur[p1:p1 + len(x[0])] == x[0] and cur[p2:p2 + len(x[1])] == x[1]
            E1 = (cur[:p1], cur[p1 + len(x[0]):p2], cur[p2 + len(x[1]):])
            return (E0, E1, x, y), fill(E1, y)
        def runs_after(cur):
            p1, p2 = locate(cur)
            k1 = p1 + len(vs.esc[0])
            r1 = len(cur[k1:]) - len(cur[k1:].lstrip('a'))
            k2 = p2 + len(vs.esc[1])
            r2 = len(cur[k2:]) - len(cur[k2:].lstrip('a'))
            return p1, p2, k1, r1, k2, r2
        p1, p2 = locate(cur)
        # dissolve w*; all dissolved weight to the left run (the right run keeps 1)
        st, cur = apply2(cur, rel_DIS2(g, g, 2 * g + lw + 1), p1, p2)
        chain.append(st)
        for yj in order:
            p1, p2, k1, r1, k2, r2 = runs_after(cur)
            assert cur[k1 + r1:k1 + r1 + len(yj.esc[0])] == yj.esc[0]
            assert cur[k2 + r2:k2 + r2 + len(yj.esc[1])] == yj.esc[1]
            dx = max(0, lw - nlen(yj))
            assert r1 >= 1 + dx and r2 >= 1
            st, cur = apply2(cur, rel_EX2(yj), k1 + r1 - 1 - dx, k2 + r2 - 1)
            chain.append(st)
            p1, p2, k1, r1, k2, r2 = runs_after(cur)
            st, cur = apply2(cur, rel_DIS2(r1, r2, r1 + r2 + lw + 1), p1, p2)
            chain.append(st)
        # the end word has the form a w1v a^{Q1} w2v a^{Q2}
        p1, p2 = locate(cur)
        endQ1 = p2 - p1 - len(vs.esc[0])
        endQ2 = len(cur) - p2 - len(vs.esc[1])
        check(cur == 'a' + vs.esc[0] + 'a' * endQ1 + vs.esc[1] + 'a' * endQ2, 'NF2 end form')
        check(1 + endQ1 + endQ2 == Rv, 'NF2 end word is an isolated v*-word (weights add)')
        target = bk.get((vs.esc[0], vs.esc[1]), (1, endQ1, endQ2))
        cert = list(bk.steps) + reverse_chain(chain)
        o, _ = replay(cert, lambda u: u in bk.native_words)
        check(o == w, 'NF2 forcing certificate replays from native words')
        classify(reverse_chain(chain))
        certs += 1
    say('  crossing pair v*=(cd,ce), w*=(c,e) (positions v1 < w1 < v2 < w2), N=%d; family of %d '
        'genuinely fan-out-2 nodes with component classes ({a,c},{a,e}); forced %d/5 random '
        'crossing-order two-sided family words from native words only (two-hole DIS2, EX2, '
        'slides)' % (N, len(fam), certs))
    # numbers: M0 and the exponents of Theorem A versus R9's H-gamma-1
    say('  bounds (log2 of the bounds on Lambda; q = number of classes; the ratio to log2(v theta) is the exponent):')
    for (v, th, r, qq) in ((100, 100, 2, 3), (10 ** 3, 10 ** 3, 2, 3), (10 ** 4, 10 ** 4, 3, 7),
                           (10 ** 6, 10 ** 6, 3, 7), (10 ** 9, 10 ** 9, 3, 7), (10 ** 12, 10 ** 12, 3, 7)):
        h = 2 * v
        lam = 6 * h * (r + 1) * (th + 4)
        M = 12 * r + 6
        while 2 ** (M / (3 * r)) <= 2 * v * ((2 * M + 6) * (M + 1) * lam + 1) ** 4:
            M += 1
        T0 = qq * (M - 1) + 1
        lnA = qq * log2(2 * h * r) + log2(8 * h * th) + T0 * log2(8 * r) + log2(4 * h * r * 64 * r * r)
        # R9 H-gamma-1: chain length t <= 3 + j (q M + 1), j = ceil(log_4(16 h r)); Lambda <= 4hr L1 (8r)^{t+1}
        j = 1
        while 4 ** j < 16 * h * r:
            j += 1
        t = 3 + j * (qq * M + 1)
        lnH = log2(4 * h * r) + log2(8 * h * (r + 1) * th) + (t + 1) * log2(8 * r)
        say('    v=%g theta=%g r=%d q=%d: M0=%d, log2(bound) Theorem A = %.0f (= %.1f log2(v theta)),'
            ' R9 H-gamma-1 = %.0f (= %.1f log2(v theta))' % (
                v, th, r, qq, M, lnA, lnA / log2(v * th), lnH, lnH / log2(v * th)))
        check(lnA < lnH, 'Theorem A improves H-gamma-1')
    tlog('F')


# ==================================================================================
def main():
    say('R10 finite checks (Claude Opus 5.5, 2026-11-22)')
    section_A()
    section_B()
    section_C()
    section_D()
    section_E()
    section_F()
    say('[G] classification of the replayed certificate steps: %s' % dict(sorted(STEP_CLASSES.items())))
    if FAILS:
        say('FAILED checks: %d' % len(FAILS))
        for f in FAILS[:30]:
            say('  ', f)
        sys.exit(1)
    say('ALL CHECKS PASSED')
    tlog('total')
    sys.exit(0)


if __name__ == '__main__':
    main()
