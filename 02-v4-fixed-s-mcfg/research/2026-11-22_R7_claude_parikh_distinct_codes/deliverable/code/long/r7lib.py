"""R7 development library: closure engine, replay, grammars (standard library only)."""
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


def is_closed_exact(S, passes=1, report=False):
    """Exact (2,c)-substitutability test of a finite set S, memory-light version.
    All arity-1 and arity-2 admissible occurrences are enumerated.  Substrings are
    interned (exact, no hashing of contents beyond Python dict equality), and the
    test is run separately for each of `passes` classes of component types.
    Returns None or a violation (E0, E1, x, y) with E0[x], E0[y], E1[x] in S and
    E1[y] not in S."""
    S = sorted(set(S), key=lambda u: (len(u), u))
    Sset = set(S)
    sid, strs, cid = {}, [], {}
    def I(s):
        k = sid.get(s)
        if k is None:
            k = len(strs)
            sid[s] = k
            strs.append(s)
        return k
    def occs(w):
        n = len(w)
        sub = [[I(w[i:j]) for j in range(n + 1)] for i in range(n + 1)]
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (sub[0][i], sub[j][n]), (sub[i][j],)
        for i in range(n):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    for l in range(k + 1, n + 1):
                        yield (sub[0][i], sub[j][k], sub[l][n]), (sub[i][j], sub[k][l])
    def tkey(t):
        return tuple(cont(strs[p]) for p in t)
    types = set()
    for w in S:
        for E, t in occs(w):
            types.add(tkey(t))
    types = sorted(types)
    tpass = {ty: i % passes for i, ty in enumerate(types)}
    for ps in range(passes):
        ctx_of = defaultdict(list)
        for w in S:
            for E, t in occs(w):
                if tpass[tkey(t)] == ps:
                    ctx_of[t].append(E)
        dist = {}
        for t, lst in ctx_of.items():
            dist[t] = frozenset(lst)
        first = {}
        for t, D in dist.items():
            ty = tkey(t)
            for E in D:
                k = (ty, E)
                t0 = first.get(k)
                if t0 is None:
                    first[k] = t
                elif dist[t0] != D:
                    a, b = (t0, t) if dist[t0] - D else (t, t0)
                    E1 = sorted(dist[a] - dist[b])[0]
                    E0s = tuple(strs[p] for p in E)
                    E1s = tuple(strs[p] for p in E1)
                    xs = tuple(strs[p] for p in a)
                    ys = tuple(strs[p] for p in b)
                    assert fill(E1s, ys) not in Sset
                    return (E0s, E1s, xs, ys)
        del ctx_of, dist, first
    return None


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
