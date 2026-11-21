#!/usr/bin/env python3
"""R7 (Claude Opus 5.5, 2026-11-22): finite checks for the report.

Python 3 standard library only, no network.  Run:  python3 -I run_all.py
Iteration orders are fixed (lists, dicts in insertion order, sorted sets), so the output
does not depend on PYTHONHASHSEED.  Exit code 0 iff every check holds.

Sections
  [A] engine self-tests (check_step, the two exact substitutability checkers)
  [B] the codes: R6-D3 condition, locking, grammar size and thickness
  [C] Lemma P (potential of the end walk), Lemma R (reachability), Lemma B (box)
  [D] shortest certificates by breadth-first search (code c a^s c b^(s^2) c), both hosts
  [E] Theorem E: explicit pigeonhole certificates for two-end-run codes
  [F] transfer calculus with derived pairs, both hosts, 5 codes, n=6,7,8, with/without cap
  [G] generic SUB closures on the locked codes (n=5)
  [H] classification of every certificate step
"""
import sys
import heapq
from collections import defaultdict, deque
from functools import lru_cache

sys.setrecursionlimit(1000000)


def cont(w):
    return ''.join(sorted(set(w)))


def fill(E, t):
    if len(t) == 1:
        return E[0] + t[0] + E[1]
    return E[0] + t[0] + E[1] + t[1] + E[2]


def ttype(t):
    return tuple(cont(p) for p in t)


def occ_full(w):
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield (w[:i], w[j:]), (w[i:j],)
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                for l in range(k + 1, n + 1):
                    yield (w[:i], w[j:k], w[l:]), (w[i:j], w[k:l])


def occ_anchored(w):
    """All arity-1 occurrences; arity-2 occurrences whose first hole starts at 0
    or whose second hole ends at |w| (one outer part empty)."""
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield (w[:i], w[j:]), (w[i:j],)
    for j in range(1, n + 1):
        x1 = w[:j]
        for k in range(j + 1, n + 1):
            mid = w[j:k]
            for l in range(k + 1, n + 1):
                yield ('', mid, w[l:]), (x1, w[k:l])
    for i in range(1, n):          # i>=1 so that i==0 is not listed twice
        pre = w[:i]
        for j in range(i + 1, n + 1):
            x1 = w[i:j]
            for k in range(j + 1, n):
                yield (pre, w[j:k], ''), (x1, w[k:])


POLICIES = {'full': occ_full, 'anchored': occ_anchored}


def check_step(E0, E1, x, y, member):
    """One SUB step, checked independently:
    E0[x], E0[y], E1[x] in L and componentwise equal content  ==>  E1[y] in L."""
    d = len(x)
    assert d in (1, 2) and len(y) == d and len(E0) == d + 1 and len(E1) == d + 1
    assert all(p != '' for p in x) and all(p != '' for p in y), 'empty component'
    if d == 2:
        assert E0[1] != '' and E1[1] != '', 'empty middle'
    assert ttype(x) == ttype(y), 'type mismatch'
    for wd in (fill(E0, x), fill(E0, y), fill(E1, x)):
        assert member(wd), 'premise not in L: %r' % (wd,)
    return fill(E1, y)


def replay(steps, seed_member, target=None):
    have = set()

    def member(u):
        return u in have or seed_member(u)
    for (E0, E1, x, y) in steps:
        have.add(check_step(E0, E1, x, y, member))
    if target is not None:
        assert target in have or seed_member(target)
    return len(steps)


class Closure:
    """Forced words: closure of seeds under SUB_1, SUB_2 restricted to an occurrence
    policy; outputs longer than cap, or rejected by keep(), are discarded.
    Sound (every word produced lies in every (2,c)-substitutable language containing
    the seeds); incomplete because of cap, keep and the policy."""

    def __init__(self, seeds, cap, policy='full', keep=None, stop=None,
                 max_words=10 ** 6, order='bfs'):
        self.cap, self.stop, self.max_words, self.order = cap, stop, max_words, order
        self.keep = keep
        self.occ = POLICIES[policy]
        self.S, self.prov = set(), {}
        self.parent, self.members, self.ctxs = {}, {}, {}
        self.ctx_of = defaultdict(set)
        self.bucket, self.edges = {}, defaultdict(list)
        self.queue, self.heap, self.cnt = deque(), [], 0
        self.found, self.truncated = None, False
        self.processed = 0
        for s in sorted(seeds, key=lambda u: (len(u), u)):
            self._add_word(s, None)

    def find(self, t):
        p = self.parent
        r = t
        while p[r] != r:
            r = p[r]
        while p[t] != r:
            p[t], t = r, p[t]
        return r

    def _emit(self, E, x0, y):
        w = fill(E, y)
        if len(w) <= self.cap and w not in self.S:
            if self.keep is None or self.keep(w):
                self._add_word(w, (E, x0, y))

    def _add_word(self, w, pv):
        if self.found is not None:
            return
        if len(self.S) >= self.max_words:
            self.truncated = True
            return
        self.S.add(w)
        self.prov[w] = pv
        if self.order == 'short':
            self.cnt += 1
            heapq.heappush(self.heap, (len(w), self.cnt, w))
        else:
            self.queue.append(w)
        if self.stop is not None and self.stop(w):
            self.found = w

    def _add_occ(self, E, t):
        if t not in self.parent:
            self.parent[t] = t
            self.members[t] = [t]
            self.ctxs[t] = {}
        co = self.ctx_of[t]
        if E in co:
            return
        co.add(E)
        r = self.find(t)
        if E not in self.ctxs[r]:
            self.ctxs[r][E] = None
            for y in self.members[r]:
                self._emit(E, t, y)
        key = (ttype(t), E)
        t2 = self.bucket.get(key)
        if t2 is not None:
            r2 = self.find(t2)
            if r2 != r:
                self.edges[t].append((t2, E))
                self.edges[t2].append((t, E))
                self._union(r, r2)
        else:
            self.bucket[key] = t

    def _union(self, r1, r2):
        if len(self.members[r1]) + len(self.ctxs[r1]) < len(self.members[r2]) + len(self.ctxs[r2]):
            r1, r2 = r2, r1
        m1, m2, c1, c2 = self.members[r1], self.members[r2], self.ctxs[r1], self.ctxs[r2]
        newc2 = [E for E in c2 if E not in c1]
        newc1 = [E for E in c1 if E not in c2]
        for E in newc1:
            x0 = self._witness(E, m1)
            for y in m2:
                self._emit(E, x0, y)
        for E in newc2:
            x0 = self._witness(E, m2)
            for y in m1:
                self._emit(E, x0, y)
        self.parent[r2] = r1
        m1.extend(m2)
        for E in c2:
            c1[E] = None
        del self.members[r2]
        del self.ctxs[r2]

    def _witness(self, E, mem):
        for t in mem:
            if E in self.ctx_of[t]:
                return t
        raise RuntimeError('no witness')

    def run(self, max_processed=None):
        while (self.queue or self.heap) and self.found is None and not self.truncated:
            if max_processed is not None and self.processed >= max_processed:
                self.truncated = True
                break
            w = heapq.heappop(self.heap)[2] if self.order == 'short' else self.queue.popleft()
            self.processed += 1
            for E, t in self.occ(w):
                self._add_occ(E, t)
                if self.found is not None or self.truncated:
                    break
        return self

    def path(self, a, b):
        if a == b:
            return [a], []
        prev = {a: None}
        dq = deque([a])
        while dq and b not in prev:
            u = dq.popleft()
            for v, C in self.edges[u]:
                if v not in prev:
                    prev[v] = (u, C)
                    dq.append(v)
        nodes, ctxs = [b], []
        while prev[nodes[-1]] is not None:
            u, C = prev[nodes[-1]]
            ctxs.append(C)
            nodes.append(u)
        return nodes[::-1], ctxs[::-1]

    def certificate(self, w):
        steps, done = [], set()

        def need(word):
            if word in done:
                return
            done.add(word)
            pv = self.prov[word]
            if pv is None:
                return
            E, x0, y = pv
            nodes, ctxs = self.path(x0, y)
            need(fill(E, x0))
            for i, C in enumerate(ctxs):
                need(fill(C, nodes[i]))
                need(fill(C, nodes[i + 1]))
                steps.append((C, E, nodes[i], nodes[i + 1]))
                done.add(fill(E, nodes[i + 1]))
        need(w)
        return steps


def is_closed(S, dmax=2):
    """Exact test that the finite set S is (dmax, content)-substitutable (all
    occurrences).  Returns None, or a violation (E0, E1, x, y)."""
    S = sorted(set(S), key=lambda u: (len(u), u))
    groups, ctx_of = defaultdict(list), defaultdict(set)
    for w in S:
        for E, t in occ_full(w):
            if len(t) > dmax:
                continue
            groups[(ttype(t), E)].append(t)
            ctx_of[t].add(E)
    for (ty, E0), ts in groups.items():
        t0 = ts[0]
        for t in ts[1:]:
            if ctx_of[t] != ctx_of[t0]:
                d1 = sorted(ctx_of[t0] - ctx_of[t])
                if d1:
                    return (E0, d1[0], t0, t)
                return (E0, sorted(ctx_of[t] - ctx_of[t0])[0], t, t0)
    return None


# ---------------------------------------------------------------- grammars
def tm_grammar(n, escA, escB=None):
    escB = escB or escA
    R = {'A0': [['a']], 'B0': [['b']]}
    for i in range(1, n + 1):
        R['A%d' % i] = [['A%d' % (i - 1), 'B%d' % (i - 1)]]
        if escA(i) is not None:
            R['A%d' % i].append([escA(i)])
        if i < n:
            R['B%d' % i] = [['B%d' % (i - 1), 'A%d' % (i - 1)]]
            if escB(i) is not None:
                R['B%d' % i].append([escB(i)])
    return R, 'A%d' % n


def spine_grammar(n, z, esc):
    R = {'A0': [[z]]}
    for i in range(1, n + 1):
        R['A%d' % i] = [['A%d' % (i - 1), 'A%d' % (i - 1)]]
        if esc(i) is not None:
            R['A%d' % i].append([esc(i)])
    return R, 'A%d' % n


def member_fn(R, S):
    """Exact membership in L(G) by recursive parsing (CFG, fan-out 1)."""
    @lru_cache(maxsize=None)
    def der(X, w):
        return any(match(tuple(rhs), w) for rhs in R[X])

    @lru_cache(maxsize=None)
    def match(rhs, w):
        if not rhs:
            return w == ''
        sym = rhs[0]
        if sym not in R:
            return w.startswith(sym) and match(rhs[1:], w[len(sym):])
        return any(der(sym, w[:k]) and match(rhs[1:], w[k:]) for k in range(1, len(w) + 1))
    return lambda w: der(S, w)


def tree_yield(R, S):
    def y(X):
        return ''.join(y(s) if s in R else s for s in R[X][0])
    return y(S)


def nodes(R, S):
    out = []

    def go(X, pos):
        p = pos
        for s in R[X][0]:
            p = go(s, p) if s in R else p + len(s)
        out.append((X, pos, p))
        return p
    go(S, 0)
    return out


def esc_words(R, S, k=1):
    W = tree_yield(R, S)
    out, singles = {W}, []
    for (X, s, e) in nodes(R, S):
        for rhs in R[X][1:]:
            singles.append((s, e, rhs[0]))
    for (s, e, r) in singles:
        out.add(W[:s] + r + W[e:])
    if k >= 2:
        for (s, e, r) in singles:
            for (s2, e2, r2) in singles:
                if e <= s2:
                    out.add(W[:s] + r + W[e:s2] + r2 + W[e2:])
    return sorted(out, key=lambda u: (len(u), u))


def size_and_thickness(R, S):
    size = sum(1 + len(rhs) + sum(len(s) for s in rhs if s not in R) for X in R for rhs in R[X])
    INF = float('inf')
    y = {X: INF for X in R}
    changed = True
    while changed:
        changed = False
        for X in R:
            for rhs in R[X]:
                v = sum(y[s] if s in R else len(s) for s in rhs)
                if v < y[X]:
                    y[X], changed = v, True
    o = {X: INF for X in R}
    o[S] = 0
    changed = True
    while changed:
        changed = False
        for X in R:
            if o[X] == INF:
                continue
            for rhs in R[X]:
                tot = sum(y[s] if s in R else len(s) for s in rhs)
                for s in rhs:
                    if s in R and o[X] + tot - y[s] < o[s]:
                        o[s], changed = o[X] + tot - y[s], True
    theta = max(o[X] + sum(y[s] if s in R else len(s) for s in rhs) for X in R for rhs in R[X])
    return size, theta, len(R), sum(len(R[X]) for X in R)


def breakpoints(w, d):
    """Cut positions within distance d of a letter change, plus 0 and |w|.
    A word with no letter change gets every position."""
    n = len(w)
    ch = [i for i in range(1, n) if w[i] != w[i - 1]]
    if not ch:
        return list(range(n + 1))
    P = {0, n}
    for i in ch:
        for k in range(i - d, i + d + 1):
            if 0 <= k <= n:
                P.add(k)
    return sorted(P)


def make_occ_brk(d, full_pure=True):
    def occ(w):
        n = len(w)
        P = breakpoints(w, d)
        for a_ in range(len(P)):
            i = P[a_]
            for b_ in range(a_ + 1, len(P)):
                j = P[b_]
                yield (w[:i], w[j:]), (w[i:j],)
        # arity 2, anchored left (i = 0)
        for b_ in range(1, len(P)):
            j = P[b_]
            x1 = w[:j]
            for c_ in range(b_ + 1, len(P)):
                k = P[c_]
                mid = w[j:k]
                for d_ in range(c_ + 1, len(P)):
                    l = P[d_]
                    yield ('', mid, w[l:]), (x1, w[k:l])
        # arity 2, anchored right (l = n), i >= 1
        for a_ in range(1, len(P)):
            i = P[a_]
            if i >= n:
                break
            pre = w[:i]
            for b_ in range(a_ + 1, len(P)):
                j = P[b_]
                x1 = w[i:j]
                for c_ in range(b_ + 1, len(P)):
                    k = P[c_]
                    if k >= n:
                        break
                    yield (pre, w[j:k], ''), (x1, w[k:])
    return occ


for _d in (1, 2, 3, 4):
    POLICIES['brk%d' % _d] = make_occ_brk(_d)


def is_closed_fast(S):
    """Exact (2,c)-substitutability test of a finite set S, written independently of
    the Closure engine.  Every admissible arity-1/2 occurrence of every word is
    enumerated; substrings are interned exactly.  Two sorts replace dictionaries:
    (1) occurrences sorted by tuple give each tuple its exact distribution (the
    sorted tuple of context ids, interned); (2) occurrences sorted by
    (component types, context) must show one distribution per group.
    Returns None, or a violation (E0, E1, x, y) with E1[y] not in S."""
    S = sorted(set(S), key=lambda u: (len(u), u))
    Sset = set(S)
    sid, strs, cbits = {}, [], []
    def I(s):
        k = sid.get(s)
        if k is None:
            k = len(strs)
            sid[s] = k
            strs.append(s)
            b = 0
            for ch in set(s):
                b |= 1 << (ord(ch) - 97)
            cbits.append(b)
        return k
    for w in S:
        n = len(w)
        for i in range(n + 1):
            for j in range(i, n + 1):
                I(w[i:j])
    M = len(strs) + 1
    keys = []                       # (tuple id) << 64*2 | (context id)
    for w in S:
        n = len(w)
        sub = [[sid[w[i:j]] if j >= i else -1 for j in range(n + 1)] for i in range(n + 1)]
        s0 = sub[0]
        for i in range(n):
            si = sub[i]
            pre = s0[i]
            for j in range(i + 1, n + 1):
                keys.append(((si[j] + 1) << 128) | (pre * M + sub[j][n]))
        base2 = M * M
        for i in range(n):
            si = sub[i]
            pre = s0[i]
            for j in range(i + 1, n + 1):
                x1 = si[j]
                sj = sub[j]
                for k in range(j + 1, n + 1):
                    mid = sj[k]
                    sk = sub[k]
                    for l in range(k + 1, n + 1):
                        tid = M + (x1 + 1) * M + sk[l] + 1
                        keys.append((tid << 128) | (1 << 127) | ((pre * M + mid) * M + sub[l][n]))
    keys.sort()
    MASK = (1 << 128) - 1
    dist_of = {}
    dists = {}
    cur, buf = None, []
    def flush():
        if cur is not None:
            d = tuple(buf)
            dist_of[cur] = dists.setdefault(d, len(dists))
    for k in keys:
        t = k >> 128
        if t != cur:
            flush()
            cur, buf = t, []
        e = k & MASK
        if not buf or buf[-1] != e:
            buf.append(e)
    flush()
    def decode_t(t):
        if t < M + M:      # arity 1: t = sid+1
            return (strs[t - 1],)
        r = t - M
        x1 = r // M - 1
        x2 = r % M - 1
        return (strs[x1], strs[x2])
    def tbits(t):
        if t < M + M:
            return (cbits[t - 1],)
        r = t - M
        return (cbits[r // M - 1], cbits[r % M - 1])
    def decode_e(e):
        if e >> 127:
            e &= (1 << 127) - 1
            v2 = e % M; e //= M
            v1 = e % M; v0 = e // M
            return (strs[v0], strs[v1], strs[v2])
        return (strs[e // M], strs[e % M])
    groups = {}
    for k in keys:
        t, e = k >> 128, k & MASK
        g = (tbits(t), e)
        d = dist_of[t]
        h = groups.get(g)
        if h is None:
            groups[g] = (t, d)
        elif h[1] != d:
            t0 = h[0]
            D0 = set(dists_inv(dists, h[1]))
            D1 = set(dists_inv(dists, d))
            if D0 - D1:
                xa, ya, E1 = t0, t, sorted(D0 - D1)[0]
            else:
                xa, ya, E1 = t, t0, sorted(D1 - D0)[0]
            v = (decode_e(e), decode_e(E1), decode_t(xa), decode_t(ya))
            assert fill(v[0], v[2]) in Sset and fill(v[0], v[3]) in Sset
            assert fill(v[1], v[2]) in Sset and fill(v[1], v[3]) not in Sset
            return v
    return None


def dists_inv(dists, idx):
    for d, i in dists.items():
        if i == idx:
            return d
    raise KeyError(idx)


# ===================== aligned transfers =====================
"""Aligned-transfer walks (C2 end moves, C2* start moves) in a binary doubling host,
with C1 collision detection and explicit certificates (independently replayable)."""


def minimal_moves(e, f, need_beta=True, need_alpha=False):
    """Moves (alpha, x, beta, y) with e = alpha x beta, f = alpha y beta, x,y nonempty,
    x != y, c(x) = c(y); beta nonempty if need_beta, alpha nonempty if need_alpha.
    Only maximal (|alpha|,|beta|) are kept (others give the same outputs)."""
    cands = []
    L = min(len(e), len(f))
    for a in range(0, L + 1):
        if e[:a] != f[:a]:
            break
        if need_alpha and a == 0:
            continue
        for b in range(0, L - a + 1):
            if b and e[len(e) - b:] != f[len(f) - b:]:
                break
            if need_beta and b == 0:
                continue
            x, y = e[a:len(e) - b], f[a:len(f) - b]
            if x and y and x != y and set(x) == set(y):
                cands.append((a, b))
    keep = [(a, b) for (a, b) in cands
            if not any((a2 >= a and b2 >= b and (a2, b2) != (a, b)) for (a2, b2) in cands)]
    return [(e[:a], e[a:len(e) - b], e[len(e) - b:], f[a:len(f) - b]) for (a, b) in sorted(keep)]


def frame_class(W, i, j):
    return (cont(W[:i]), cont(W[j:]))


class Walk:
    def __init__(self, R, S, mirror=True, maxstates=300000, minmargin=1):
        self.R, self.S = R, S
        self.W = W = tree_yield(R, S)
        self.N = N = len(W)
        self.esc = {}
        for (X, s, e) in nodes(R, S):
            if len(R[X]) > 1 and (s, e) != (0, N):
                self.esc[(s, e)] = R[X][1][0]
        self.mirror, self.maxstates = mirror, maxstates
        mv = {}
        self.end_pairs, self.start_pairs = {}, {}
        for (s1, e1), w1 in self.esc.items():
            for (s2, e2), w2 in self.esc.items():
                if (s1, e1) == (s2, e2):
                    continue
                # C2: same start, both right margins nonempty with equal content
                if s1 == s2 and N - max(e1, e2) >= minmargin and cont(W[e1:]) == cont(W[e2:]):
                    key = ('E', w1, w2)
                    if key not in mv:
                        mv[key] = minimal_moves(w1, w2, need_beta=True)
                    for m in mv[key]:
                        self.end_pairs.setdefault(e1, []).append(((s1, e1), (s2, e2), m))
                # C2*: same end, both left margins nonempty with equal content
                if mirror and e1 == e2 and min(s1, s2) >= minmargin and cont(W[:s1]) == cont(W[:s2]):
                    key = ('S', w1, w2)
                    if key not in mv:
                        mv[key] = minimal_moves(w1, w2, need_beta=False, need_alpha=True)
                    for m in mv[key]:
                        self.start_pairs.setdefault(s1, []).append(((s1, e1), (s2, e2), m))

    def run(self):
        W, N = self.W, self.N
        prev, placed = {}, {}
        dq = deque()
        self.found = None
        for (s, e), w in sorted(self.esc.items()):
            st = (s, e, w)
            prev[st] = None
            dq.append(st)
            if self._place(placed, st):
                return self
        while dq and len(prev) < self.maxstates:
            st = dq.popleft()
            I, J, f = st
            outs = []
            for (u, u2, (al, x, be, y)) in self.end_pairs.get(J, []):
                i = f.find(x)
                while i != -1:
                    if i + len(x) < len(f):           # eta nonempty
                        outs.append(((I, u2[1], f[:i] + y + f[i + len(x):]), ('E', u, u2, al, x, be, y, i)))
                    i = f.find(x, i + 1)
            if self.mirror and I >= 1:
                for (u, u2, (al, x, be, y)) in self.start_pairs.get(I, []):
                    i = f.find(x)
                    while i != -1:
                        if i >= 1:                    # gamma nonempty
                            outs.append(((u2[0], J, f[:i] + y + f[i + len(x):]), ('S', u, u2, al, x, be, y, i)))
                        i = f.find(x, i + 1)
            for ns, how in outs:
                if ns[0] < ns[1] and ns not in prev:
                    prev[ns] = (st, how)
                    dq.append(ns)
                    if self._place(placed, ns):
                        self.prev = prev
                        return self
        self.prev, self.placed = prev, placed
        return self

    def _place(self, placed, st):
        I, J, f = st
        key = (f, frame_class(self.W, I, J))
        d = placed.setdefault(key, {})
        R = J - I
        for R2, st2 in d.items():
            if R2 != R:
                self.found = (st2, st)
                return True
        d.setdefault(R, st)
        return False

    def path(self, st):
        out = []
        while self.prev[st] is not None:
            p, how = self.prev[st]
            out.append((p, how, st))
            st = p
        return out[::-1]

    def certificate(self):
        W = self.W
        steps, seen = [], set()
        A, B = self.found
        for st in (A, B):
            for (src, how, dst) in self.path(st):
                if (src, dst) in seen:
                    continue
                seen.add((src, dst))
                I, J, f = src
                kind, u, u2, al, x, be, y, i = how
                gam, eta = f[:i], f[i + len(x):]
                if kind == 'E':
                    E0 = (W[:u[0]] + al, be, '')
                    E1 = (W[:I] + gam, eta, '')
                    steps.append((E0, E1, (x, W[u[1]:]), (y, W[u2[1]:])))
                else:
                    E0 = ('', al, be + W[u[1]:])
                    E1 = ('', gam, eta + W[J:])
                    steps.append((E0, E1, (W[:u[0]], x), (W[:u2[0]], y)))
        steps.append(c1_step(W, A, B))
        return steps


def c1_step(W, A, B):
    """Frame lemma C1 for one filler M at two frames of one class with different
    region lengths: returns the step producing the shorter word."""
    (i1, j1, M), (i2, j2, M2) = A, B
    assert M == M2
    if j1 - i1 > j2 - i2:
        (i1, j1), (i2, j2) = (i2, j2), (i1, j1)
    lam1, rho1, lam2, rho2, g1 = W[:i1], W[j1:], W[:i2], W[j2:], W[i1:j1]
    if lam1 and rho1:
        return (('', M, ''), ('', g1, ''), (lam1, rho1), (lam2, rho2))
    if rho1:            # empty left margins
        return ((M, ''), (g1, ''), (rho1,), (rho2,))
    return (('', M), ('', g1), (lam1,), (lam2,))


def replay_cert(steps, mem):
    have = set()
    m2 = lambda u: u in have or mem(u)
    out = None
    for s in steps:
        out = check_step(*s, m2)
        have.add(out)
    return out


def runs(w):
    out, i = [], 0
    while i < len(w):
        j = i
        while j < len(w) and w[j] == w[i]:
            j += 1
        out.append((w[i], i, j))
        i = j
    return out


class TransferClosure:
    """Closure of placements under aligned transfers whose pairs may be derived.
    mode 'tree': frames are W-frames (I,J); C2 uses pairs with a common start and a
    host ending where the first pair word ends; C2* the mirror.  mode 'periodic'
    (W = z^N): frames are regions R (B0 realigns), plus P4/absorption moves.
    A placement is a state; prov[state] = (kind, data).  Stops at the first filler
    placed in two frames of one class with different region lengths."""

    def __init__(self, R, S, mode='tree', z=None, p4=True, maxstates=20000, rmax=None,
                 mirror=True, native_only_pairs=False, cap=None, inner_p4=False):
        self.cap, self.inner_p4 = cap, inner_p4
        self.Rg, self.S, self.mode = R, S, mode
        self.W = W = tree_yield(R, S)
        self.N = N = len(W)
        self.z, self.p4, self.maxstates, self.mirror = z, p4, maxstates, mirror
        self.native_only_pairs = native_only_pairs
        self.rmax = N - 2 if rmax is None else rmax
        self.native = []
        for (X, s, e) in nodes(R, S):
            if len(R[X]) > 1 and (s, e) != (0, N):
                if mode == 'periodic' and (s < 1 or e > N - 1):
                    continue
                self.native.append(((s, e), R[X][1][0]))
        self.found = None

    # --- state helpers
    def key(self, st):
        if self.mode == 'periodic':
            return st                       # (R, f)
        I, J, f = st
        return (f, frame_class(self.W, I, J))

    def region(self, st):
        return st[0] if self.mode == 'periodic' else st[1] - st[0]

    def run(self):
        W, N = self.W, self.N
        self.prov, self.order = {}, []
        self.byfiller = {}
        self.bystart, self.byend = {}, {}
        self.endmoves, self.startmoves, self.gmoves = {}, {}, []
        self.pending = deque()
        for (fr, w) in self.native:
            st = (fr[1] - fr[0], w) if self.mode == 'periodic' else (fr[0], fr[1], w)
            self._add(st, ('native', fr))
            if self.found:
                return self
        while self.pending and not self.found and len(self.prov) < self.maxstates:
            st = self.pending.popleft()
            self._process(st)
        return self

    def _add(self, st, pv):
        if st in self.prov or self.found:
            return
        if self.mode == 'periodic':
            if not (1 <= st[0] <= self.rmax):
                return
            if self.cap is not None and pv[0] != 'native' and self.N - st[0] + len(st[1]) > self.cap:
                return
        else:
            if not (0 <= st[0] < st[1] <= N_(self)):
                return
            if self.cap is not None and pv[0] != 'native' and self.N - (st[1] - st[0]) + len(st[2]) > self.cap:
                return
        self.prov[st] = pv
        self.order.append(st)
        k = (st[1],) if self.mode == 'periodic' else self.key(st)
        d = self.byfiller.setdefault(k, {})
        Rr = self.region(st)
        for R2, st2 in d.items():
            if R2 != Rr:
                self.found = (st2, st)
                return
        d.setdefault(Rr, st)
        self.pending.append(st)

    def _process(self, st):
        W, N = self.W, self.N
        is_native = self.prov[st][0] == 'native'
        if self.mode == 'periodic':
            Rf, f = st
            # new pairs with every earlier state
            if is_native or not self.native_only_pairs:
                for st2 in list(self.order):
                    if st2 == st or (self.native_only_pairs and self.prov[st2][0] != 'native'):
                        continue
                    for (a, b) in ((st, st2), (st2, st)):
                        for m in minimal_moves(a[1], b[1], need_beta=False):
                            mv = (a, b, m)
                            self.gmoves.append(mv)
                            for host in list(self.order):
                                self._apply_p(host, mv)
                                if self.found:
                                    return
            for mv in list(self.gmoves):
                self._apply_p(st, mv)
                if self.found:
                    return
            if self.p4:
                for (ns, how) in self._p4moves(st):
                    self._add(ns, how)
                    if self.found:
                        return
        else:
            I, J, f = st
            if is_native or not self.native_only_pairs:
                for st2 in list(self.bystart.get(I, [])):
                    if self.native_only_pairs and self.prov[st2][0] != 'native':
                        continue
                    J2 = st2[1]
                    if N - max(J, J2) < 1 or cont(W[J:]) != cont(W[J2:]):
                        continue
                    for (a, b) in ((st, st2), (st2, st)):
                        for m in minimal_moves(a[2], b[2], need_beta=True):
                            mv = (a, b, m)
                            self.endmoves.setdefault(a[1], []).append(mv)
                            for host in list(self.byend.get(a[1], [])):
                                self._apply_e(host, mv)
                                if self.found:
                                    return
                if self.mirror and I >= 1:
                    for st2 in list(self.byend.get(J, [])):
                        if self.native_only_pairs and self.prov[st2][0] != 'native':
                            continue
                        I2 = st2[0]
                        if min(I, I2) < 1 or cont(W[:I]) != cont(W[:I2]):
                            continue
                        for (a, b) in ((st, st2), (st2, st)):
                            for m in minimal_moves(a[2], b[2], need_beta=False, need_alpha=True):
                                mv = (a, b, m)
                                self.startmoves.setdefault(a[0], []).append(mv)
                                for host in list(self.bystart.get(a[0], [])):
                                    self._apply_s(host, mv)
                                    if self.found:
                                        return
            self.bystart.setdefault(I, []).append(st)
            self.byend.setdefault(J, []).append(st)
            for mv in list(self.endmoves.get(J, [])):
                self._apply_e(st, mv)
                if self.found:
                    return
            if self.mirror and I >= 1:
                for mv in list(self.startmoves.get(I, [])):
                    self._apply_s(st, mv)
                    if self.found:
                        return
            if self.inner_p4:
                for (g, a_, b_) in self._inner_p4(f):
                    self._add((I, J, g), ('P4t', st, a_, b_))
                    if self.found:
                        return

    def _apply_e(self, host, mv):
        a, b, (al, x, be, y) = mv
        I, J, f = host
        if host == a:
            return
        i = f.find(x)
        while i != -1:
            if i + len(x) < len(f):
                self._add((I, b[1], f[:i] + y + f[i + len(x):]), ('C2', host, mv, i))
                if self.found:
                    return
            i = f.find(x, i + 1)

    def _apply_s(self, host, mv):
        a, b, (al, x, be, y) = mv
        I, J, f = host
        if host == a:
            return
        i = f.find(x)
        while i != -1:
            if i >= 1:
                self._add((b[0], J, f[:i] + y + f[i + len(x):]), ('C2*', host, mv, i))
                if self.found:
                    return
            i = f.find(x, i + 1)

    def _apply_p(self, host, mv):
        a, b, (al, x, be, y) = mv
        Rf, f = host
        if host == a:
            return
        i = f.find(x)
        while i != -1:
            self._add((Rf + b[0] - a[0], f[:i] + y + f[i + len(x):]), ('C2p', host, mv, i))
            if self.found:
                return
            i = f.find(x, i + 1)

    def _inner_p4(self, f):
        letters4 = self._letters4()
        rs = runs(f)
        out = []
        for a_ in range(len(rs)):
            for b_ in range(len(rs)):
                ch, i1, j1 = rs[a_]
                ch2, i2, j2 = rs[b_]
                if a_ == b_ or ch != ch2 or ch not in letters4 or j2 - i2 < 2 or abs(a_ - b_) < 2:
                    continue
                g = list(f)
                del g[i2]
                g.insert(i1 if i1 < i2 else i1 - 1, ch)
                out.append((''.join(g), a_, b_))
        return out

    def _p4moves(self, st):
        Rf, f = st
        z = self.z
        out = []
        letters4 = self._letters4()
        rs = runs(f)
        for a_ in range(len(rs)):
            for b_ in range(len(rs)):
                ch, i1, j1 = rs[a_]
                ch2, i2, j2 = rs[b_]
                if a_ == b_ or ch != ch2 or ch not in letters4 or j2 - i2 < 2 or abs(a_ - b_) < 2:
                    continue
                g = list(f)
                del g[i2]
                g.insert(i1 if i1 < i2 else i1 - 1, ch)
                out.append(((Rf, ''.join(g)), ('P4', st, a_, b_)))
        if f[0] != z and f[-1] != z:
            for (ch, i1, j1) in rs:
                if ch != z:
                    continue
                if j1 - i1 >= 2:
                    out.append(((Rf - 1, f[:i1] + f[i1 + 1:]), ('ABS-out', st, i1)))
                out.append(((Rf + 1, f[:i1] + z + f[i1:]), ('ABS-in', st, i1)))
        return out

    def _letters4(self):
        if not hasattr(self, '_l4'):
            l4 = {self.z} if self.z else set()
            self._src4 = {}
            cands = [self.W] + [self.W[:fr[0]] + w + self.W[fr[1]:] for (fr, w) in self.native]
            for w in cands:
                for (ch, i, j) in runs(w):
                    if j - i >= 4 and ch not in self._src4:
                        self._src4[ch] = (w[:i], w[i + 4:])
                        l4.add(ch)
            self._l4 = l4
        return self._l4


def N_(tc):
    return tc.N


def tc_certificate(tc):
    """Concrete, independently replayable SUB steps for tc.found."""
    W, N, z = tc.W, tc.N, tc.z
    steps = []
    built = set()
    if tc.mode == 'tree':
        def build(st):
            if st in built:
                return
            built.add(st)
            pv = tc.prov[st]
            if pv[0] == 'native':
                return
            if pv[0] == 'P4t':
                _, src, a_, b_ = pv
                build(src)
                I, J, f0 = src
                w = W[:I] + f0 + W[J:]
                off = I
                rs = runs(f0)
                ch, i1, j1 = rs[a_]
                ch2, i2, j2 = rs[b_]
                y0, z0 = tc._src4[ch]
                if i1 < i2:
                    E1 = (w[:off + j1 - 1], w[off + j1:off + i2], w[off + i2 + 2:])
                    steps.append(((y0, ch, z0), E1, (ch, ch * 2), (ch * 2, ch)))
                else:
                    E1 = (w[:off + j2 - 2], w[off + j2:off + i1], w[off + i1 + 1:])
                    steps.append(((y0, ch, z0), E1, (ch * 2, ch), (ch, ch * 2)))
                return
            kind, host, mv, i = pv
            a, b, (al, x, be, y) = mv
            build(a); build(b); build(host)
            f = host[2]
            gam, eta = f[:i], f[i + len(x):]
            if kind == 'C2':
                steps.append(((W[:a[0]] + al, be, ''), (W[:host[0]] + gam, eta, ''),
                              (x, W[a[1]:]), (y, W[b[1]:])))
            else:
                steps.append((('', al, be + W[a[1]:]), ('', gam, eta + W[host[1]:]),
                              (W[:a[0]], x), (W[:b[0]], y)))
        A, B = tc.found
        build(A); build(B)
        steps.append(c1_step(W, A, B))
        return steps
    # periodic mode
    pos = {}
    native_pos = {}
    for (fr, w) in tc.native:
        native_pos.setdefault((fr[1] - fr[0], w), (fr[0], N - fr[1]))

    def word(st):
        p, q = pos[st]
        return z * p + st[1] + z * q

    def slide(st, pq):
        cur = pos[st]
        if cur == pq:
            return
        R = st[0]
        assert cur[0] + cur[1] == pq[0] + pq[1] == N - R and min(cur + pq) >= 1 and R >= 1
        steps.append((('', z * R, ''), ('', st[1], ''), (z * cur[0], z * cur[1]), (z * pq[0], z * pq[1])))
        pos[st] = pq

    def build(st):
        if st in pos:
            return
        pv = tc.prov[st]
        if pv[0] == 'native':
            pos[st] = native_pos[st]
            return
        kind = pv[0]
        if kind == 'C2p':
            _, host, mv, i = pv
            a, b, (al, x, be, y) = mv
            build(a); build(b); build(host)
            Rf, f = host
            R1, R2 = a[0], b[0]
            h = max(1, Rf - R1 + 1)
            k1, k2 = N - h - R1, N - h - R2
            if k1 < 2 or k2 < 2:
                raise ValueError('no room')
            hf = h + R1 - Rf
            slide(a, (h, k1)); slide(b, (h, k2)); slide(host, (hf, k1))
            gam, eta = f[:i], f[i + len(x):]
            steps.append(((z * h + al, be + z, ''), (z * hf + gam, eta + z, ''),
                          (x, z * (k1 - 1)), (y, z * (k2 - 1))))
            pos[st] = (hf, k2)
            return
        if kind == 'P4':
            _, src, a_, b_ = pv
            build(src)
            w = word(src)
            off = pos[src][0]
            rs = runs(src[1])
            ch, i1, j1 = rs[a_]
            ch2, i2, j2 = rs[b_]
            y0, z0 = tc._src4[ch]
            if i1 < i2:
                E1 = (w[:off + j1 - 1], w[off + j1:off + i2], w[off + i2 + 2:])
                steps.append(((y0, ch, z0), E1, (ch, ch * 2), (ch * 2, ch)))
            else:
                E1 = (w[:off + j2 - 2], w[off + j2:off + i1], w[off + i1 + 1:])
                steps.append(((y0, ch, z0), E1, (ch * 2, ch), (ch, ch * 2)))
            pos[st] = pos[src]
            return
        if kind == 'ABS-out':
            _, src, i1 = pv
            build(src)
            p, q = pos[src]
            w = word(src)
            y0, z0 = tc._src4[z]
            steps.append(((y0, z, z0), (w[:p - 1], w[p:p + i1], w[p + i1 + 2:]), (z, z * 2), (z * 2, z)))
            pos[st] = (p + 1, q)
            return
        if kind == 'ABS-in':
            _, src, i1 = pv
            build(src)
            p, q = pos[src]
            if p < 2:
                if q < 2:
                    raise ValueError('no room')
                slide(src, (2, q - (2 - p)))
                p, q = pos[src]
            w = word(src)
            y0, z0 = tc._src4[z]
            steps.append(((y0, z, z0), (w[:p - 2], w[p:p + i1], w[p + i1 + 1:]), (z * 2, z), (z, z * 2)))
            pos[st] = (p - 1, q)
            return
        raise ValueError(kind)

    A, B = tc.found
    build(A); build(B)
    if A[0] > B[0]:
        A, B = B, A
    (pa, qa), (pb, qb) = pos[A], pos[B]
    steps.append((('', A[1], ''), ('', z * A[0], ''), (z * pa, z * qa), (z * pb, z * qb)))
    return steps


# ===================== Theorem E generator =====================
"""Theorem E (pigeonhole over frame ends) as an explicit certificate generator.

Binary doubling host of height n with leaves of length ell, level-uniform escapes
eps_t = s0 x^{f_t} mu y^{g_t} s2 for 1 <= t <= n-1.  For Jt in [1, 2^(n-2)] the
frame end is J = 2*ell*Jt and the potential is
    V(Jt) = (f_1,g_1) + sum over maximal runs [a,b] of 1-bits of (Jt-1)
                          of ( (f,g)_{b+2} - (f,g)_{a+1} ).
"""


def runs_of_bits(m):
    out, b = [], 0
    while m >> b:
        if (m >> b) & 1:
            a = b
            while (m >> b) & 1:
                b += 1
            out.append((a, b - 1))
        else:
            b += 1
    return out


def V(Jt, fg):
    f, g = fg[1]
    for (a, b) in runs_of_bits(Jt - 1):
        f += fg[b + 2][0] - fg[a + 1][0]
        g += fg[b + 2][1] - fg[a + 1][1]
    return (f, g)


def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def path_from_one(Jt):
    """Edges (K, s, s2) of a path 1 -> ... -> Jt in reduced units; an edge joins
    K+2^s and K+2^s2 (2^s2 | K, s < s2), i.e. real levels s+1 and s2+1 at real
    start 2*ell*K.  Built by reversing the popcount reduction."""
    red = []
    J = Jt
    while J != 1:
        s = v2(J)
        K = J - (1 << s)
        if K == 0:
            red.append((0, 0, s, J, 1))          # J = 2^s -> 1  (reverse edge)
            J = 1
        else:
            c = v2(K)
            red.append((K, s, c, J, K + (1 << c)))   # J=K+2^s -> K+2^c (forward)
            J = K + (1 << c)
    # reverse: sequence of (from, to, K, lo, hi)
    out = []
    for (K, s, c, frm, to) in reversed(red):
        if K == 0 and frm == (1 << c) and to == 1 and s == 0:
            out.append((1, frm, 0, 0, c))
        else:
            out.append((to, frm, K, s, c))
    return out


def skel(s0, x, mu, y, s2, F, G):
    return s0 + x * F + mu + y * G + s2


def move_words(x, mu, y, f, g, f2, g2):
    """(x_part, y_part, p, q) for the move eps(f,g) -> eps(f2,g2)."""
    p = max(1, 1 + f - f2)
    q = max(1, 1 + g - g2)
    return x * p + mu + y * q, x * (p + f2 - f) + mu + y * (q + g2 - g), p, q


def certificate(W, ell, n, parts, fg):
    """Explicit certificate: walks 1 -> J1 and 1 -> J2 for the first collision
    V(J1) = V(J2), then C1.  parts = (s0, x, mu, y, s2)."""
    s0, x, mu, y, s2 = parts
    seen = {}
    J1 = J2 = None
    for Jt in range(1, 2 ** (n - 2) + 1):
        v = V(Jt, fg)
        if v in seen:
            J1, J2 = seen[v], Jt
            break
        seen[v] = Jt
    if J1 is None:
        return None
    steps = []
    for target in (J1, J2):
        cur = 1
        Fh, Gh = fg[1]
        for (frm, to, K, s, c) in path_from_one(target):
            assert frm == cur
            # pair: nodes of real levels s+1 and c+1 starting at real position P
            P = 2 * ell * K
            if to > frm:      # forward: lower level s+1 -> higher level c+1
                lo, hi = s + 1, c + 1
            else:             # reverse: higher -> lower
                lo, hi = c + 1, s + 1
            (f1, g1), (f2, g2) = fg[lo], fg[hi]
            xp, yp, p, q = move_words(x, mu, y, f1, g1, f2, g2)
            e = skel(s0, x, mu, y, s2, f1, g1)
            al = s0 + x * (f1 - p)
            be = y * (g1 - q) + s2
            assert al + xp + be == e and al + yp + be == skel(s0, x, mu, y, s2, f2, g2)
            Jend = 2 * ell * frm
            Jnew = 2 * ell * to
            assert Jend == P + (2 ** lo) * ell and Jnew == P + (2 ** hi) * ell
            host = skel(s0, x, mu, y, s2, Fh, Gh)
            gam = s0 + x * (Fh - p)
            eta = y * (Gh - q) + s2
            assert Fh - p >= 0 and Gh - q >= 0 and gam + xp + eta == host
            E0 = (W[:P] + al, be, '')
            E1 = (gam, eta, '')
            steps.append((E0, E1, (xp, W[Jend:]), (yp, W[Jnew:])))
            Fh, Gh = Fh + f2 - f1, Gh + g2 - g1
            cur = to
            assert (Fh, Gh) == V(cur, fg), 'potential mismatch'
        assert cur == target
    M = skel(s0, x, mu, y, s2, *V(J1, fg))
    A = (0, 2 * ell * J1, M)
    B = (0, 2 * ell * J2, M)
    steps.append(c1_step(W, A, B))
    return J1, J2, steps


# =====================================================================================
#                                     the checks
# =====================================================================================
import random
import time
import re
from collections import Counter

FAILS = []
T0 = time.time()


def check(cond, msg):
    print(('  ok   ' if cond else '  FAIL ') + msg, flush=True)
    if not cond:
        FAILS.append(msg)


def parikh(w, al='abcdef'):
    c = Counter(w)
    return tuple(c[x] for x in al)


RND = {1: 'cfdfdeddc', 2: 'cefffdedfdc', 3: 'cefdeeefc', 4: 'cfeefedc', 5: 'cddfefffdfc',
       6: 'cedfefddfc', 7: 'cfeedfeefdc', 8: 'cfeffefddfc'}
RIG = {1: 'dcdeeecde', 2: 'cddcceeeddeddc', 3: 'dceddccdc', 4: 'ceecdceee', 5: 'dccdceced',
       6: 'eeedecedd', 7: 'ddcccecceedd', 8: 'ceededced'}
CODES = {
    'sq':  lambda s: 'c' + 'a' * s + 'c' + 'b' * (s * s) + 'c',
    'exp': lambda s: 'c' + 'a' * s + 'c' + 'b' * (2 ** s) + 'c',
    'pal': lambda s: 'c' + 'a' * s + 'c' + 'b' * (s * s) + 'c' + 'a' * s + 'c',
    'rnd': lambda s: RND[s],
    'rig': lambda s: RIG[s],
}
CODE_NAMES = {'sq': 'c a^s c b^(s^2) c', 'exp': 'c a^s c b^(2^s) c', 'pal': 'c a^s c b^(s^2) c a^s c',
              'rnd': 'random words over {c,d,e,f}', 'rig': 'rigid ternary words over {c,d,e}'}


def grammar(host, code, n):
    if host == 'spine':
        R, S = spine_grammar(n, 'a', CODES[code])
        return R, S, set('a')
    R, S = tm_grammar(n, CODES[code])
    return R, S, set('ab')


def d3_ok(code, n, al='abcdef'):
    diffs = set()
    for p in range(1, n + 1):
        for q in range(p + 1, n + 1):
            d = tuple(a - b for a, b in zip(parikh(code(q), al), parikh(code(p), al)))
            if d in diffs:
                return False
            diffs.add(d)
    return True


def locked(code, n):
    """every minimal move x of every ordered pair of levels occurs in no other code word"""
    for p in range(1, n + 1):
        for q in range(1, n + 1):
            if p == q:
                continue
            for (al, x, be, y) in minimal_moves(code(p), code(q)):
                for r in range(1, n + 1):
                    if r != p and x in code(r):
                        return False
    return True


# -------------------------------------------------------------- step classification
def classify(step, m):
    """kind of one SUB step, relative to the host word E1[x]: arity, whether the
    tuple keeps its Parikh vector, and where each component lies (M = margin,
    X = escape span = from the first to the last letter outside m, S = spanning)."""
    E0, E1, x, y = step
    host = fill(E1, x)
    bad = [i for i, ch in enumerate(host) if ch not in m]
    pp = parikh(''.join(x)) == parikh(''.join(y))
    pos = []
    off = len(E1[0])
    for k, comp in enumerate(x):
        a, b = off, off + len(comp)
        if not bad:
            pos.append('M')
        else:
            lo, hi = bad[0], bad[-1] + 1
            if b <= lo or a >= hi:
                pos.append('M')
            elif a >= lo and b <= hi:
                pos.append('X')
            else:
                pos.append('S')
        off = b + (len(E1[1]) if k == 0 and len(x) == 2 else 0)
    return '%d-hole %s (%s)' % (len(x), 'Parikh-preserving' if pp else 'Parikh-changing', ','.join(pos))


def summarize(steps, m):
    c = Counter(classify(s, m) for s in steps)
    return '; '.join('%s x%d' % (k, v) for k, v in sorted(c.items()))


ALLCERTS = []      # (label, steps, m)


def print_cert(label, steps):
    """all four words of every step (premises E0[x], E0[y], E1[x]; conclusion E1[y])"""
    print('     certificate %s (%d steps):' % (label, len(steps)))
    for i, (E0, E1, x, y) in enumerate(steps):
        print('       step %d: x=%r y=%r E0=%r E1=%r' % (i + 1, x, y, E0, E1))
        print('         E0[x]=%s\n         E0[y]=%s\n         E1[x]=%s\n         E1[y]=%s'
              % (fill(E0, x), fill(E0, y), fill(E1, x), fill(E1, y)))

# ================================================================ [A]
print('[A] engine self-tests')
F = 'abbabaabbaababba'
inF = lambda u: u == F
F1 = check_step(('', 'b', 'baababba'), ('', 'baabb', 'abba'), ('abba', 'aab'), ('ab', 'abaab'), inF)
check(F1 == 'abbaabbabaababba', 'R6 [A] re-cut F -> F_1 reproduced')
bad = 0
for args in ((('', '', 'x'), ('', 'b', ''), ('a', 'b'), ('a', 'b')),          # empty middle
             (('', 'b'), ('', 'c'), ('a',), ('b',)),                          # type mismatch
             (('', 'b', ''), ('', 'b', ''), ('', 'a'), ('a', 'a'))):          # empty component
    try:
        check_step(*args, lambda u: True)
    except AssertionError:
        bad += 1
check(bad == 3, 'check_step rejects empty middles, type mismatches and empty components')
rnd_ = random.Random(20261122)
agree = 0
for trial in range(60):
    S = set()
    for _ in range(rnd_.randint(1, 4)):
        S.add(''.join(rnd_.choice('ab') for _ in range(rnd_.randint(1, 7))))
    agree += (is_closed(S) is None) == (is_closed_fast(S) is None)
check(agree == 60, 'is_closed_fast agrees with the R6 checker is_closed on 60 random small sets')
check(is_closed_fast(['aaabaabbcaabcbcabccaaaccbbcccbbb']) is None, 'R6 w32 is a (2,c)-substitutable singleton (fast checker)')

# ================================================================ [B]
print('[B] codes: Parikh differences (R6 D3 condition), locking, grammar size and thickness')
for name in ('sq', 'exp', 'pal', 'rnd', 'rig'):
    code = CODES[name]
    for host in ('spine', 'tm'):
        R, S, m = grammar(host, name, 8)
        size, theta, nv, npr = size_and_thickness(R, S)
        print('     %-5s %-34s host=%-5s n=8: |V|=%d rules=%d size=%d theta=%d max|e|=%d'
              % (name, CODE_NAMES[name], host, nv, npr, size, theta, max(len(code(s)) for s in range(1, 9))))
    check(d3_ok(code, 8), '%s: Parikh differences of all level pairs are pairwise distinct (n=8)' % name)
    print('     %-5s locked (no minimal move occurs in another code word): %s' % (name, locked(code, 8)))
check(not locked(CODES['sq'], 8) and locked(CODES['rnd'], 8) and locked(CODES['rig'], 8),
      'sq is transferable; rnd and rig are locked')

# ================================================================ [C]
print('[C] Lemma P (potential of the end walk) and Lemma R (reachability): finite verification')
# formal check: for every edge K+2^s -- K+2^s2 (2^s2 | K, s < s2, K+2^s2 <= 2^h) the formal potential
# Psi(J) = sum_{runs [a,b] of bin(J-1)} (e_{b+1} - e_a) changes by e_s2 - e_s, and [1,2^h] is connected.
def psi(J):
    out = Counter()
    for (a, b) in runs_of_bits(J - 1):
        out[b + 1] += 1
        out[a] -= 1
    return out
okP, okR = True, True
for h in range(1, 12):
    top = 2 ** h
    adj = {J: [] for J in range(1, top + 1)}
    for K in range(0, top):
        for s in range(0, h + 1):
            for s2 in range(s + 1, h + 1):
                if K % (2 ** s2) == 0 and K + 2 ** s2 <= top:
                    J1, J2 = K + 2 ** s, K + 2 ** s2
                    d = psi(J2)
                    d.subtract(psi(J1))
                    d = {k: v for k, v in d.items() if v}
                    if d != {s2: 1, s: -1}:
                        okP = False
                    adj[J1].append(J2)
                    adj[J2].append(J1)
    seen, st = {1}, [1]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                st.append(v)
    okR = okR and len(seen) == top
    for J in range(1, top + 1):          # the explicit path of the proof
        cur = 1
        for (frm, to, K, s, c) in path_from_one(J):
            okR = okR and frm == cur and (K % (2 ** c) == 0) and K + 2 ** c <= top
            cur = to
        okR = okR and cur == J
check(okP, 'Lemma P: Psi(K+2^s2) - Psi(K+2^s) = e_s2 - e_s on every edge (h <= 11)')
check(okR, 'Lemma R: [1,2^h] is connected and the popcount path of the proof is valid (h <= 11)')
# box lemma: for coordinatewise monotone codes V stays between the end values (random codes)
okB = True
for trial in range(300):
    h = rnd_.randint(2, 9)
    seqs = []
    for c_ in range(2):
        v = [rnd_.randint(1, 30) for _ in range(h + 2)]
        v.sort(reverse=rnd_.random() < 0.5)
        seqs.append(v)
    fg = [None] + [(seqs[0][t - 1], seqs[1][t - 1]) for t in range(1, h + 2)]
    for Jt in range(1, 2 ** (h - 1) + 1):
        vv = V(Jt, fg)
        for i in range(2):
            lo, hi = sorted((fg[1][i], fg[h][i]))
            if not lo <= vv[i] <= hi:
                okB = False
check(okB, 'Lemma B: V(J) lies in the box spanned by the end values for coordinatewise monotone codes (300 random)')

# ================================================================ [D]
print('[D] shortest certificates by breadth-first search over aligned transfers (code sq; no periodic frame used)')
for host in ('spine', 'tm'):
    for n in (6, 7, 8):
        R, S, m = grammar(host, 'sq', n)
        wk = Walk(R, S).run()
        mem = member_fn(R, S)
        st = wk.certificate()
        out = replay_cert(st, mem)
        ok = set(out) == m and len(out) < wk.N and not mem(out)
        check(ok, '%s n=%d: %d-step certificate, shortcut of length %d < %d, not in L(G_n) (parser)'
              % (host, n, len(st), len(out), wk.N))
        ALLCERTS.append(('D %s sq n=%d' % (host, n), st, m))
        if n == 6:
            A, B = wk.found
            print('     filler %s placed at frames (%d,%d) and (%d,%d)' % (A[2], A[0], A[1], B[0], B[1]))
            print_cert('%s sq n=6' % host, st)

# ================================================================ [E]
print('[E] Theorem E: explicit pigeonhole construction for two-end-run codes c a^f(s) c b^g(s) c')
FAM = [('sq', lambda s: s, lambda s: s * s), ('lin', lambda s: s, lambda s: s),
       ('tri', lambda s: s, lambda s: s * (s + 1) // 2), ('cub', lambda s: s, lambda s: s ** 3),
       ('half', lambda s: (s + 1) // 2, lambda s: s), ('dec', lambda s: 12 - s, lambda s: s * s),
       ('exp', lambda s: s, lambda s: 2 ** s)]
for host in ('spine', 'tm'):
    for (name, f, g) in FAM:
        for n in (6, 8, 10):
            code = lambda s, f=f, g=g: 'c' + 'a' * f(s) + 'c' + 'b' * g(s) + 'c'
            R, S = spine_grammar(n, 'a', code) if host == 'spine' else tm_grammar(n, code)
            m = set('a') if host == 'spine' else set('ab')
            W = tree_yield(R, S)
            N = len(W)
            seeds = set(esc_words(R, S, 1))
            fg = [None] + [(f(t), g(t)) for t in range(1, n)]
            box = (abs(fg[n - 1][0] - fg[1][0]) + 1) * (abs(fg[n - 1][1] - fg[1][1]) + 1)
            res = certificate(W, 1, n, ('c', 'a', 'c', 'b', 'c'), fg)
            guaranteed = 2 ** (n - 2) > box
            if res is None:
                check(not guaranteed, '%s %-4s n=%-2d no collision among %d ends (box %d, pigeonhole not applicable)'
                      % (host, name, n, 2 ** (n - 2), box))
                continue
            J1, J2, st = res
            out = replay_cert(st, lambda u: u in seeds)
            ok = set(out) == m and len(out) == N - 2 * (J2 - J1)
            if n <= 8:
                ok = ok and not member_fn(R, S)(out)
            check(ok, '%s %-4s n=%-2d collision of V at J~=(%d,%d): %d-step certificate, shortcut %d < %d%s'
                  % (host, name, n, J1, J2, len(st), len(out), N, ' [pigeonhole-guaranteed]' if guaranteed else ''))
            if n == 8:
                ALLCERTS.append(('E %s %s n=%d' % (host, name, n), st, m))

# ================================================================ [F]
print('[F] transfer calculus with derived pairs (C2/C2*; in the periodic spine also B0, power transfer P4 and absorption)')
TF = {}
for host in ('spine', 'tm'):
    for name in ('sq', 'exp', 'pal', 'rnd', 'rig'):
        for n in (6, 7, 8):
            for capped in (False, True):
                R, S, m = grammar(host, name, n)
                N = len(tree_yield(R, S))
                if host == 'tm' and name == 'exp' and n == 8:
                    ms = 1500
                else:
                    ms = 3000
                if host == 'spine':
                    tc = TransferClosure(R, S, mode='periodic', z='a', maxstates=ms, cap=N if capped else None)
                else:
                    tc = TransferClosure(R, S, mode='tree', maxstates=ms, cap=N if capped else None, inner_p4=True)
                tc.run()
                tag = '%s %-3s n=%d %s' % (host, name, n, 'cap |W|' if capped else 'no cap ')
                if tc.found:
                    st = tc_certificate(tc)
                    mem = member_fn(R, S)
                    out = replay_cert(st, mem)
                    maxout = max(len(fill(E1, y)) for (E0, E1, x, y) in st)
                    outs_ok = (maxout <= N) if (capped and host == 'tm') else True
                    ok = set(out) == m and len(out) < N and not mem(out) and outs_ok
                    check(ok, '%s: FOUND, %d steps, shortcut %d < %d, longest output %d%s' % (
                        tag, len(st), len(out), N, maxout,
                        (' <= |W|' if host == 'tm' else ' (states <= |W|; B0 realignment of long seeds may exceed |W|)') if capped else ''))
                    TF[(host, name, n, capped)] = 'found'
                    if n == 6 and not capped and (host, name) in (('spine', 'exp'), ('tm', 'pal')):
                        print_cert('%s %s n=6' % (host, name), st)
                    if n == 8 and not capped:
                        ALLCERTS.append(('F %s %s n=%d' % (host, name, n), st, m))
                else:
                    status = 'exhausted' if not tc.pending else 'budget'
                    print('     %s: none; %d states, %s' % (tag, len(tc.prov), status))
                    TF[(host, name, n, capped)] = status
check(all(TF[(h, 'sq', n, False)] == 'found' for h in ('spine', 'tm') for n in (6, 7, 8)), 'sq dies in both hosts, n=6,7,8')
check(all(TF[('spine', c_, n, False)] == 'found' for c_ in ('exp', 'pal') for n in (6, 7, 8)), 'exp and pal die in the periodic spine (absorption), n=6,7,8')
check(all(TF[('tm', 'pal', n, False)] == 'found' for n in (6, 7, 8)), 'pal dies in the Thue-Morse host (inner power transfer unlocks it), n=6,7,8')
check(all(TF[(h, c_, n, False)] == 'exhausted' for h in ('spine', 'tm') for c_ in ('rnd', 'rig') for n in (6, 7, 8)),
      'Proposition F: for the locked codes rnd, rig the transfer calculus is closed on the native placements')
check(TF[('tm', 'exp', 6, False)] == 'exhausted' and TF[('tm', 'exp', 7, False)] == 'exhausted',
      'exp in the Thue-Morse host: transfer calculus exhausted without collision (n=6,7)')
# exp is additive on the end walk: V_g(J~) = 2 J~ (the b-count of the host equals its region)
check(all(V(Jt, [None] + [(t, 2 ** t) for t in range(1, 12)])[1] == 2 * Jt for Jt in range(1, 2 ** 10 + 1)),
      'exp: V_g(J~) = 2 J~ for J~ <= 2^10, so the end walk is injective (no pigeonhole)')

# ================================================================ [G]
print('[G] generic SUB_1/SUB_2 closures (all occurrences) on the locked codes, spine, n=5')
R, S, m = grammar('spine', 'rnd', 5)
mem = member_fn(R, S)
c = Closure(esc_words(R, S, 1), 32, policy='full', stop=lambda w: 'ffff' in w, order='short').run()
st = c.certificate(c.found)
k = replay(st, mem, c.found)
check(c.found is not None and k == 2, 'rnd is not rigid: the root escape cddfefffdfc is recut to %s (%d steps, Parikh-preserving)' % (c.found, k))
ALLCERTS.append(('G spine rnd n=5 (f^4)', st, set('cdef')))
R, S, m = grammar('spine', 'rig', 5)
seeds = esc_words(R, S, 1)
cap = int(1.5 * max(map(len, seeds)))
t1 = time.time()
c = Closure(seeds, cap, policy='full', stop=lambda w: set(w) <= m and len(w) < 32, order='short').run()
mx = max(map(len, c.S))
v = is_closed_fast(c.S)
check(c.found is None and not c.truncated and mx < cap and v is None,
      'rig, seeds W + single escapes: closure has %d words (max length %d < cap %d), no shortcut, and is exactly (2,c)-substitutable'
      % (len(c.S), mx, cap))
slides = {w for w in c.S if set(w) != {'a'}}
check(all(re.fullmatch('a*([^a]+)a*', w) and re.fullmatch('a*([^a]+)a*', w).group(1) in RIG.values() for w in slides),
      'rig: every closure word other than W is a single code word e_s with a-margins (B0 slides only)')
check(len(c.S) == sum(32 - 2 ** s_ + 1 for s_ in range(1, 5)) + 2,
      'rig: |closure| = sum_{s=1}^{n-1} (2^n - 2^s + 1) + 2 = 104 (all positions of each e_s, plus W and e_5)')
R, S, m = grammar('spine', 'sq', 5)
mem = member_fn(R, S)
c = Closure(esc_words(R, S, 1), 32, policy='anchored', stop=lambda w: set(w) == {'a'} and len(w) < 32, order='short').run()
st = c.certificate(c.found)
k = replay(st, mem, c.found)
check(len(c.found) == 14 and not mem(c.found), 'sq n=5, generic closure (cap |W|): shortcut a^14 with a %d-step certificate (uses the root escape)' % k)
ALLCERTS.append(('G spine sq n=5 generic', st, set('a')))

# ================================================================ [H]
print('[H] which Rect steps did the work (classification of every certificate step)')
tot = Counter()
for (label, st, m) in ALLCERTS:
    print('     %-28s %s' % (label, summarize(st, m)))
    for s in st:
        tot[classify(s, m)] += 1
print('     total:')
for k_, v_ in sorted(tot.items()):
    print('       %-44s %d' % (k_, v_))
print()
sys.stderr.write('time %.0fs\n' % (time.time() - T0))
print('FAILED: %d' % len(FAILS))
sys.exit(1 if FAILS else 0)
