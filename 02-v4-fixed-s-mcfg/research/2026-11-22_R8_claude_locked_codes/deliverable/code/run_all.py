#!/usr/bin/env python3
"""R8 (Claude Opus 5.5, 2026-11-22): finite checks for the report
"locked rigid codes and the two-escape stage".

Python 3 standard library only, no network.  Run:  python3 -I run_all.py
All iteration orders are fixed (lists, insertion-ordered dicts, sorted sets), so the
output does not depend on PYTHONHASHSEED.  Exit code 0 iff every check holds.

Sections
  [A] engine self-tests (check_step, two independent exact substitutability checkers)
  [B] counts: |L(G_n)|, |T(2^n)| (the forced arrangements), aligned fills
  [C] token level: SUB closure of the native token words, n = 3, 4, three content typings
  [D] letter level: explicit certificates of Theorem H2 (forcing of misaligned
      arrangements) for six codes, replayed from the finite native set N_H only
  [E] Lemma H3 and the swap of Theorem H4: planted lighter words force shortcuts
  [F] letter level, n = 3: the two-escape stage creates non-token words (recuts)
  [G] classification of every certificate step
"""
import sys
import time
import random
import itertools
from collections import defaultdict, deque, Counter
from functools import lru_cache

sys.setrecursionlimit(1000000)
def fill(E, t):
    if len(t) == 1:
        return E[0] + t[0] + E[1]
    return E[0] + t[0] + E[1] + t[1] + E[2]


def make_typing(cmap):
    """cmap: char -> int bitmask (its content).  Returns the content of a word."""
    def ty(w):
        b = 0
        for ch in set(w):
            b |= cmap[ch]
        return b
    return ty


def letter_cmap(alpha):
    return {ch: 1 << i for i, ch in enumerate(sorted(alpha))}


def check_step(E0, E1, x, y, member, ty):
    """One SUB step, checked independently:
    E0[x], E0[y], E1[x] in L, componentwise equal types, nonempty components,
    nonempty middle  ==>  E1[y] in L.  Returns E1[y]."""
    d = len(x)
    assert d in (1, 2) and len(y) == d and len(E0) == d + 1 and len(E1) == d + 1
    assert all(p != '' for p in x) and all(p != '' for p in y), 'empty component'
    if d == 2:
        assert E0[1] != '' and E1[1] != '', 'empty middle'
    assert tuple(ty(p) for p in x) == tuple(ty(p) for p in y), 'type mismatch'
    for wd in (fill(E0, x), fill(E0, y), fill(E1, x)):
        assert member(wd), 'premise not in L: %r' % (wd,)
    return fill(E1, y)


def replay(steps, seed_member, ty):
    have = set()
    out = None

    def member(u):
        return u in have or seed_member(u)
    for (E0, E1, x, y) in steps:
        out = check_step(E0, E1, x, y, member, ty)
        have.add(out)
    return out, have


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


class Closure:
    """Closure of seeds under SUB_1, SUB_2 (all occurrences) for a typing ty.
    Sound: every produced word lies in every (2,ty)-substitutable language containing
    the seeds.  Stops at max_words (then .truncated) or when stop(w) holds."""

    def __init__(self, seeds, ty, cap=None, stop=None, max_words=10 ** 6):
        self.ty, self.cap, self.stop, self.max_words = ty, cap, stop, max_words
        self.S, self.prov = set(), {}
        self.parent, self.members, self.ctxs = {}, {}, {}
        self.ctx_of = defaultdict(set)
        self.bucket, self.edges = {}, defaultdict(list)
        self.queue = deque()
        self.found, self.truncated, self.processed = None, False, 0
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
        if (self.cap is None or len(w) <= self.cap) and w not in self.S:
            self._add_word(w, (E, x0, y))

    def _add_word(self, w, pv):
        if self.found is not None:
            return
        if len(self.S) >= self.max_words:
            self.truncated = True
            return
        self.S.add(w)
        self.prov[w] = pv
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
        key = (tuple(self.ty(p) for p in t), E)
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
        while self.queue and self.found is None and not self.truncated:
            if max_processed is not None and self.processed >= max_processed:
                self.truncated = True
                break
            w = self.queue.popleft()
            self.processed += 1
            for E, t in occ_full(w):
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


def is_closed_exact(S, cmap):
    """Exact (2,ty)-substitutability test of a finite set S (all occurrences),
    independent of Closure: every arity-1/2 occurrence is listed; substrings are
    interned exactly; tuples are grouped by (component types, context) and each
    group must show a single distribution.  Returns None or a violation
    (E0, E1, x, y) with E0[x], E0[y], E1[x] in S and E1[y] not in S."""
    S = sorted(set(S), key=lambda u: (len(u), u))
    Sset = set(S)
    sid, strs, cb = {}, [], []

    def I(s):
        k = sid.get(s)
        if k is None:
            k = len(strs)
            sid[s] = k
            strs.append(s)
            b = 0
            for ch in set(s):
                b |= cmap[ch]
            cb.append(b)
        return k
    for w in S:
        n = len(w)
        for i in range(n + 1):
            for j in range(i, n + 1):
                I(w[i:j])
    M = len(strs) + 1
    keys = []
    for w in S:
        n = len(w)
        sub = [[sid[w[i:j]] if j >= i else -1 for j in range(n + 1)] for i in range(n + 1)]
        s0 = sub[0]
        for i in range(n):
            si = sub[i]
            pre = s0[i]
            for j in range(i + 1, n + 1):
                keys.append(((si[j] + 1) << 128) | (pre * M + sub[j][n]))
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
    dist_of, dists, inv = {}, {}, []
    cur, buf = None, []

    def flush():
        if cur is not None:
            d = tuple(buf)
            if d not in dists:
                dists[d] = len(inv)
                inv.append(d)
            dist_of[cur] = dists[d]
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
        if t < M + M:
            return (strs[t - 1],)
        r = t - M
        return (strs[r // M - 1], strs[r % M - 1])

    def tbits(t):
        if t < M + M:
            return (cb[t - 1],)
        r = t - M
        return (cb[r // M - 1], cb[r % M - 1])

    def decode_e(e):
        if e >> 127:
            e &= (1 << 127) - 1
            v2 = e % M
            e //= M
            v1 = e % M
            v0 = e // M
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
            D0, D1 = set(inv[h[1]]), set(inv[d])
            if D0 - D1:
                xa, ya, E1 = h[0], t, sorted(D0 - D1)[0]
            else:
                xa, ya, E1 = t, h[0], sorted(D1 - D0)[0]
            v = (decode_e(e), decode_e(E1), decode_t(xa), decode_t(ya))
            assert fill(v[0], v[2]) in Sset and fill(v[0], v[3]) in Sset
            assert fill(v[1], v[2]) in Sset and fill(v[1], v[3]) not in Sset
            return v
    return None


def is_closed_naive(S, cmap):
    """Second exact checker (slow, dictionary based) for cross-validation."""
    ty = make_typing(cmap)
    S = sorted(set(S), key=lambda u: (len(u), u))
    groups, ctx_of = defaultdict(list), defaultdict(set)
    for w in S:
        for E, t in occ_full(w):
            groups[(tuple(ty(p) for p in t), E)].append(t)
            ctx_of[t].add(E)
    for (tyk, E0), ts in groups.items():
        t0 = ts[0]
        for t in ts[1:]:
            if ctx_of[t] != ctx_of[t0]:
                return (E0, t0, t)
    return None


# ------------------------------------------------------------------ spine grammar
def spine_grammar(n, z, esc, left='', right=''):
    """A_0 -> z, A_i -> A_{i-1} A_{i-1} | esc(i); start S -> left A_n right."""
    R = {'A0': [[z]]}
    for i in range(1, n + 1):
        R['A%d' % i] = [['A%d' % (i - 1), 'A%d' % (i - 1)]]
        if esc(i) is not None:
            R['A%d' % i].append([esc(i)])
    rhs = ([left] if left else []) + ['A%d' % n] + ([right] if right else [])
    R['S'] = [rhs]
    return R, 'S'


def member_fn(R, S):
    """Exact membership in L(G) by recursive parsing (CFG)."""
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


def spine_language(n, z, esc, left='', right=''):
    """All words of L(G_n) (antichain escapings of the full binary tree)."""
    @lru_cache(maxsize=None)
    def L(i):
        out = set()
        if i == 0:
            return frozenset([z])
        for u in L(i - 1):
            for v in L(i - 1):
                out.add(u + v)
        if esc(i) is not None:
            out.add(esc(i))
        return frozenset(out)
    return sorted({left + w + right for w in L(n)}, key=lambda u: (len(u), u))


# ------------------------------------------------------------------ token weights
def tokch(i):
    """token character: 'z' for the spine letter (level 0), 'A','B',... for E_1, E_2, ..."""
    return 'z' if i == 0 else chr(ord('A') + i - 1)


def arrangements(N, n):
    """T(N): all token strings over z (weight 1) and E_1..E_n (weight 2^i) of weight N."""
    tok = [('z', 1)] + [(tokch(i), 2 ** i) for i in range(1, n + 1)]

    @lru_cache(maxsize=None)
    def T(k):
        if k == 0:
            return ('',)
        out = []
        for (ch, w) in tok:
            if w <= k:
                for rest in T(k - w):
                    out.append(ch + rest)
        return tuple(out)
    return list(T(N))


def count_T(N):
    f = [1] + [0] * N
    for k in range(1, N + 1):
        j = 0
        while 2 ** j <= k:
            f[k] += f[k - 2 ** j]
            j += 1
    return f[N]


def tweight(toks):
    return sum(1 if t == 0 else 2 ** t for t in toks)


def aligned_fill(n, c):
    """levels of the maximal aligned dyadic intervals covering [c, 2^n) (0 = one leaf)."""
    N = 2 ** n
    out, pos = [], c
    while pos < N:
        d = 0
        while pos % (2 ** (d + 1)) == 0 and pos + 2 ** (d + 1) <= N:
            d += 1
        out.append(d)
        pos += 2 ** d
    return out


# ------------------------------------------------------------------ the weight calculus (Theorem H)
class Spine:
    """Doubling spine u_L A_n u_R, A_0 -> z, A_i -> A_{i-1}A_{i-1} | e_i.
    i0 is the smallest level of the chosen content class K."""

    def __init__(self, n, z, code, left='', right='', i0=1):
        self.n, self.z, self.code, self.left, self.right, self.i0 = n, z, code, left, right, i0
        self.N = 2 ** n

    def h(self, toks):
        return ''.join(self.z if t == 0 else self.code[t] for t in toks)

    def wrap(self, w):
        return self.left + w + self.right

    def natives_H(self, P, c):
        """the finite native set N_H(P, c) used by Theorem H2/H3"""
        z, N, i0, e0, L, R = self.z, self.N, self.i0, self.code[self.i0], self.left, self.right
        p = 2 ** i0
        out = [L + z * N + R,
               L + z * p + e0 + z * (N - 2 * p) + R,
               L + e0 + e0 + z * (N - 2 * p) + R]
        for i in P:
            out.append(L + self.code[i] + z * (N - 2 ** i) + R)
            out.append(L + e0 * (2 ** (i - i0)) + z * (N - 2 ** i) + R)
        out.append(L + e0 + z * (c - p) + self.h(aligned_fill(self.n, c)) + R)
        return sorted(set(out), key=lambda u: (len(u), u))

    def pre_steps(self):
        """slide (2-hole): makes u_L z^{2^i0+1} e z^{N-2^{i0+1}-1} u_R available"""
        z, N, i0, e = self.z, self.N, self.i0, self.code[self.i0]
        p, q = 2 ** i0, N - 2 ** (i0 + 1)
        return [((self.left, z * p, self.right), (self.left, e, self.right),
                 (z * p, z * q), (z * (p + 1), z * (q - 1)), 'slide')]

    def cong_comp(self, i):
        e, e0 = self.code[i], self.code[self.i0]
        return e, e0 * (2 ** (i - self.i0)), (self.left, self.z * (self.N - 2 ** i) + self.right), 'comp'

    def cong_comm(self):
        z, e, p = self.z, self.code[self.i0], 2 ** self.i0
        return z + e, e + z, (self.left + z * p, z * (self.N - 2 * p - 1) + self.right), 'comm'

    def cong_conv(self):
        z, e, p = self.z, self.code[self.i0], 2 ** self.i0
        return e + e + z, z * p + e + z, (self.left, z * (self.N - 2 * p - 1) + self.right), 'conv'


def capply(sp, toks, pos, old, new, cong, forward, steps):
    assert tuple(toks[pos:pos + len(old)]) == tuple(old)
    x, y, E0, kind = cong
    if not forward:
        x, y = y, x
    assert sp.h(old) == x and sp.h(new) == y, (old, new)
    lam = sp.left + sp.h(toks[:pos])
    rho = sp.h(toks[pos + len(old):]) + sp.right
    steps.append((E0, (lam, rho), (x,), (y,), kind))
    return toks[:pos] + list(new) + toks[pos + len(old):]


def normalize(sp, toks, core, steps):
    """reduce the mixed factor toks[0:core] (z and class-K escapes) to z^{w-2^i0} E_i0"""
    i0 = sp.i0
    toks = list(toks)
    k = 0
    while k < core:
        t = toks[k]
        if t not in (0, i0):
            m = 2 ** (t - i0)
            toks = capply(sp, toks, k, [t], [i0] * m, sp.cong_comp(t), True, steps)
            core += m - 1
        k += 1

    def bubble():
        nonlocal toks
        changed = True
        while changed:
            changed = False
            for j in range(core - 1):
                if toks[j] == i0 and toks[j + 1] == 0:
                    toks = capply(sp, toks, j, [i0, 0], [0, i0], sp.cong_comm(), False, steps)
                    changed = True
    bubble()
    while True:
        p = 0
        while toks[p] == 0:
            p += 1
        l = core - p
        assert p >= 1 and all(t == i0 for t in toks[p:core])
        if l <= 1:
            break
        j = p - 1
        for _ in range(l):
            toks = capply(sp, toks, j, [0, i0], [i0, 0], sp.cong_comm(), True, steps)
            j += 1
        toks = capply(sp, toks, core - 3, [i0, i0, 0], [0] * (2 ** i0) + [i0, 0], sp.cong_conv(), True, steps)
        core += 2 ** i0 - 1
        bubble()
    return toks, core


def reverse_steps(steps):
    return [(E0, E1, y, x, kind) for (E0, E1, x, y, kind) in reversed(steps)]


def core_of(order, g):
    core = [0] * g
    for t in order:
        core += [t] + [0] * g
    return core


def forcing_certificate(sp, order, g):
    """Theorem H2: x_pi = h(core_pi Fill_c) from the natives N_H."""
    i0 = sp.i0
    core = core_of(order, g)
    c = tweight(core)
    fl = aligned_fill(sp.n, c)
    target = core + fl
    native = [i0] + [0] * (c - 2 ** i0) + fl
    steps = list(sp.pre_steps())
    s1, s2 = [], []
    nf1, _ = normalize(sp, native, c - 2 ** i0 + 1, s1)
    nf2, _ = normalize(sp, target, len(core), s2)
    assert nf1 == nf2
    steps += s1 + reverse_steps(s2)
    return steps, sp.wrap(sp.h(target)), c


def shortcut_certificate(sp, low_core, c_ref):
    """Lemma H3: from a word h(low_core Fill_{c_ref}) with tweight(low_core) < c_ref,
    derive the shorter spine word u_L z^{N-c_ref+c''} u_R."""
    i0 = sp.i0
    fl = aligned_fill(sp.n, c_ref)
    native = [i0] + [0] * (c_ref - 2 ** i0) + fl
    steps = list(sp.pre_steps())
    s1, s2 = [], []
    normalize(sp, native, c_ref - 2 ** i0 + 1, s1)
    normalize(sp, list(low_core) + fl, len(low_core), s2)
    steps += s1 + s2
    c2 = tweight(low_core)
    z, e = sp.z, sp.code[i0]
    E0 = (sp.left, e + sp.h(fl) + sp.right)
    E1 = (sp.left, z * (sp.N - c_ref + 2 ** i0) + sp.right)
    steps.append((E0, E1, (z * (c_ref - 2 ** i0),), (z * (c2 - 2 ** i0),), 'final'))
    return steps, sp.wrap(z * (sp.N - c_ref + c2))


def replay_k(steps, seed_member, ty):
    have = set()
    out = None

    def member(u):
        return u in have or seed_member(u)
    for st in steps:
        out = check_step(st[0], st[1], st[2], st[3], member, ty)
        have.add(out)
    return out, have


def classify(st, m_letters):
    E0, E1, x, y = st[:4]
    pp = Counter(''.join(x)) == Counter(''.join(y))
    return '%d-hole %s %s' % (len(x), 'Parikh-preserving' if pp else 'Parikh-changing', st[4] if len(st) > 4 else '?')


# ------------------------------------------------------------------ codes
RND = {1: 'cfdfdeddc', 2: 'cefffdedfdc', 3: 'cefdeeefc', 4: 'cfeefedc', 5: 'cddfefffdfc',
       6: 'cedfefddfc', 7: 'cfeedfeefdc', 8: 'cfeffefddfc'}
RIG = {1: 'dcdeeecde', 2: 'cddcceeeddeddc', 3: 'dceddccdc', 4: 'ceecdceee', 5: 'dccdceced',
       6: 'eeedecedd', 7: 'ddcccecceedd', 8: 'ceededced'}
CODES = {
    'sq': lambda s: 'c' + 'a' * s + 'c' + 'b' * (s * s) + 'c',
    'exp': lambda s: 'c' + 'a' * s + 'c' + 'b' * (2 ** s) + 'c',
    'pal': lambda s: 'c' + 'a' * s + 'c' + 'b' * (s * s) + 'c' + 'a' * s + 'c',
    'rnd': lambda s: RND[s],
    'rig': lambda s: RIG[s],
    'alt': lambda s: ('c' + 'd' * s + 'c') if s % 2 else ('e' * s + 'f'),
}
CODE_NAMES = {'sq': 'c a^s c b^(s^2) c (R6/R7)', 'exp': 'c a^s c b^(2^s) c (R7)',
              'pal': 'c a^s c b^(s^2) c a^s c (R7)', 'rnd': 'random, {c,d,e,f} (R7)',
              'rig': 'rigid ternary, {c,d,e} (R7)', 'alt': 'level-varying contents (R8)'}


def content_class(code, n, alpha):
    """largest content class K among levels 1..n-2 (ties: class of the smallest level)"""
    cl = defaultdict(list)
    for i in range(1, n - 1):
        cl[frozenset(code(i))].append(i)
    best = max(cl.values(), key=lambda v: (len(v), -v[0]))
    return best


# =====================================================================================
#                                     the checks
# =====================================================================================
FAILS = []
T0 = time.time()


def check(cond, msg):
    print(('  ok   ' if cond else '  FAIL ') + msg, flush=True)
    if not cond:
        FAILS.append(msg)


def main():
    ALLCERTS = []
    # ============================================================ [A]
    print('[A] engine self-tests')
    cm3 = letter_cmap('abc')
    ty3 = make_typing(cm3)
    F = 'abbabaabbaababba'
    F1 = check_step(('', 'b', 'baababba'), ('', 'baabb', 'abba'), ('abba', 'aab'), ('ab', 'abaab'),
                    lambda u: u == F, ty3)
    check(F1 == 'abbaabbabaababba', 'R6 [A] re-cut F -> F_1 reproduced by check_step')
    bad = 0
    for args in ((('', '', 'x'), ('', 'b', ''), ('a', 'b'), ('a', 'b')),
                 (('', 'b'), ('', 'c'), ('a',), ('b',)),
                 (('', 'b', ''), ('', 'b', ''), ('', 'a'), ('a', 'a'))):
        try:
            check_step(args[0], args[1], args[2], args[3], lambda u: True, ty3)
        except AssertionError:
            bad += 1
    check(bad == 3, 'check_step rejects an empty middle, a type mismatch and an empty component')
    rng = random.Random(20261122)
    agree = 0
    for trial in range(80):
        S = set()
        al = 'ab' if trial % 2 else 'abc'
        for _ in range(rng.randint(1, 4)):
            S.add(''.join(rng.choice(al) for _ in range(rng.randint(1, 7))))
        agree += (is_closed_exact(S, cm3) is None) == (is_closed_naive(S, cm3) is None)
    check(agree == 80, 'is_closed_exact agrees with the independent is_closed_naive on 80 random small sets')
    check(is_closed_exact(['aaabaabbcaabcbcabccaaaccbbcccbbb'], cm3) is None,
          'R6 w32 is a (2,c)-substitutable singleton (exact checker)')
    # closure engine soundness on a small case: every produced word has a replayable certificate
    seeds = ['abab', 'aabb']
    cl = Closure(seeds, ty3, max_words=200).run()
    okc = True
    for w in sorted(cl.S, key=lambda u: (len(u), u))[:40]:
        st = cl.certificate(w)
        have = replay(st, lambda u: u in seeds, ty3)[1] if st else set()
        okc = okc and (w in seeds or w in have)
    check(okc, 'Closure: certificates of the first 40 produced words replay (seeds abab, aabb)')

    # ============================================================ [B]
    print('[B] counts')
    LG = [None, 2]
    for n in range(2, 6):
        LG.append(LG[-1] ** 2 + 1)
    for n in range(1, 6):
        print('     n=%d  |L(G_n)| = %d   |T(2^n)| = %d' % (n, LG[n], count_T(2 ** n)))
    print('     n=6  |T(64)| = %d' % count_T(64))
    check(count_T(32) == 47350056 and len(arrangements(16, 4)) == count_T(16) == 5272,
          '|T(16)| = 5272 (enumerated) and |T(32)| = 47350056: by Theorem H2 the n=5 closure has >= 4.7e7 words')
    def prefix_free(ws):
        return all(not (u != v and v.startswith(u)) for u in ws for v in ws)
    pf = {nm: prefix_free([CODES[nm](i) for i in range(1, 9)]) and all('a' not in CODES[nm](i) for i in range(1, 9))
          for nm in ('rnd', 'rig')}
    check(pf['rnd'] and pf['rig'], 'rnd and rig (levels 1..8) are prefix codes avoiding a, so h is injective on '
          'token strings and |h(T(N))| = |T(N)|')
    okf = True
    for n in range(3, 9):
        for c in range(1, 2 ** n):
            fl = aligned_fill(n, c)
            pos = c
            for d in fl:
                okf = okf and pos % (2 ** d) == 0
                pos += 2 ** d
            okf = okf and pos == 2 ** n and fl.count(0) <= 1 and len(fl) <= n
    check(okf, 'aligned_fill: [c,2^n) is covered by <= n aligned dyadic intervals, at most one leaf (n <= 8)')

    # ============================================================ [C]
    print('[C] token level: closure of the native token words L_tok(G_n)')
    TYP = {'common': lambda i: 2, 'alt': lambda i: 2 if i % 2 else 4, 'distinct': lambda i: 2 << i}
    for n in (3, 4):
        N = 2 ** n
        seeds = spine_language(n, 'z', tokch)
        T = set(arrangements(N, n))
        for name in ('common', 'alt', 'distinct'):
            cmap = {'z': 1}
            cmap.update({tokch(i): TYP[name](i) for i in range(1, n + 1)})
            t1 = time.time()
            cl = Closure(seeds, make_typing(cmap), max_words=10 ** 6).run()
            S = cl.S
            pred = set()
            for tau in T:
                lev = [ord(ch) - 64 for ch in tau if ch != 'z']
                if 'z' in tau and lev and max(lev) <= n - 2 and len({TYP[name](i) for i in lev}) == 1:
                    pred.add(tau)
            zw = sorted(w for w in S if set(w) == {'z'})
            msg = 'n=%d %-8s seeds %4d -> closure %4d (not truncated: %s), closure <= T(N): %s, = T(N): %s, ' \
                  'single-class mixed words of levels <= n-2 forced: %d/%d, z-words %s' % (
                      n, name, len(seeds), len(S), not cl.truncated, S <= T, S == T, len(pred & S), len(pred), zw)
            sys.stderr.write('  [C] n=%d %s %.1fs\n' % (n, name, time.time() - t1))
            ok = (not cl.truncated) and S <= T and pred <= S and zw == ['z' * N]
            if name == 'common':
                ok = ok and S == T
            check(ok, msg)
            ex = is_closed_exact(S, cmap)
            check(ex is None, '   closure is exactly (2,c)-substitutable (fast checker)' + (
                '' if n == 4 else ', naive checker agrees: %s' % (is_closed_naive(S, cmap) is None)))
            ext = is_closed_exact(T, cmap)
            check(ext is None, '   T(%d) itself is exactly (2,c)-substitutable (Prop. 5: weight is additive)' % N)

    # ============================================================ [D]
    print('[D] letter level: Theorem H2 certificates (misaligned arrangements forced from N_H only)')
    DEF = [('sq', 5, '', ''), ('sq', 6, '', ''), ('exp', 6, '', ''), ('pal', 6, '', ''),
           ('rnd', 5, '', ''), ('rnd', 6, '', ''), ('rig', 5, '', ''), ('rig', 6, '', ''),
           ('rig', 6, 'f', 'f'), ('alt', 7, '', '')]
    for (name, n, uL, uR) in DEF:
        code = {i: CODES[name](i) for i in range(1, n + 1)}
        alpha = sorted(set(''.join(code.values())) | {'a'} | set(uL + uR))
        cm = letter_cmap(alpha)
        ty = make_typing(cm)
        R, S = spine_grammar(n, 'a', lambda i: code[i], uL, uR)
        mem = member_fn(R, S)
        P = content_class(CODES[name], n, alpha)
        sp = Spine(n, 'a', code, uL, uR, i0=P[0])
        t1 = time.time()
        ncert, nsteps, okall, tgt_ex = 0, 0, True, None
        natives_ok = True
        for g in (2, 3):
            for order in itertools.permutations(P):
                steps, target, c = forcing_certificate(sp, list(order), g)
                NH = set(sp.natives_H(P, c))
                natives_ok = natives_ok and all(mem(u) for u in NH)
                out, have = replay_k(steps, lambda u: u in NH, ty)
                okall = okall and out == target and not mem(target)
                ncert += 1
                nsteps += len(steps)
                if tgt_ex is None:
                    tgt_ex = (order, g, c, target)
                if g == 2 and order == tuple(P):
                    ALLCERTS.append(('D %s n=%d' % (name, n), steps))
        check(okall and natives_ok,
              '%-4s n=%d margins=%r K-levels P=%s: %d certificates (all orders of P, gaps g=2,3), %d steps; '
              'each replays from N_H (all in L(G_n) by the parser); every target is NOT in L(G_n)'
              % (name, n, uL + '|' + uR, P, ncert, nsteps))
        sys.stderr.write('  [D] %s n=%d %.1fs\n' % (name, n, time.time() - t1))
        if name in ('rig', 'alt') and uL == '':
            o, g, c, tgt = tgt_ex
            print('       e.g. order %s, g=%d, c=%d: %s' % (o, g, c, tgt))
    # arbitrary arrangements of T(N) (common content): random samples, rig, n = 5, 6
    for n, cnt in ((5, 25), (6, 8)):
        code = {i: RIG[i] for i in range(1, n + 1)}
        ty = make_typing(letter_cmap('acde'))
        R, S = spine_grammar(n, 'a', lambda i: code[i])
        mem = member_fn(R, S)
        sp = Spine(n, 'a', code, '', '', 1)
        rs = random.Random(1000 + n)
        ok, mis, nst = True, 0, 0
        for _ in range(cnt):
            while True:
                tau, rem = [], sp.N
                while rem:
                    t = rs.choice([j for j in range(0, n) if 2 ** j <= rem] + [0, 0])
                    tau.append(t)
                    rem -= 2 ** t if t else 1
                if 0 in tau and any(tau):
                    break
            s2 = []
            nf, _ = normalize(sp, tau, len(tau), s2)
            ok = ok and nf == [0] * (sp.N - 2) + [1]
            steps = list(sp.pre_steps()) + reverse_steps(s2)
            out, have = replay_k(steps, mem, ty)
            ok = ok and out == sp.h(tau)
            mis += not mem(out)
            nst += len(steps)
        check(ok, 'rig n=%d: %d random mixed arrangements tau in T(%d) (any order, any levels <= n-1) are forced '
              '(%d steps in all, replayed from L(G_n)); %d of them are not in L(G_n)' % (n, cnt, sp.N, nst, mis))
    # one full certificate printed (rig, n=5, order (3,1,2), g=2)
    n = 5
    code = {i: RIG[i] for i in range(1, n + 1)}
    sp = Spine(n, 'a', code, '', '', 1)
    steps, target, c = forcing_certificate(sp, [3, 1, 2], 2)
    print('     full certificate, rig n=5, order (3,1,2), g=2, c=%d, target %s (%d steps); first 12 and last 3:'
          % (c, target, len(steps)))
    for i, st in enumerate(steps):
        if i < 12 or i >= len(steps) - 3:
            E0, E1, x, y, kind = st
            print('       step %d [%s]: x=%r y=%r E0=%r E1=%r' % (i + 1, kind, x, y, E0, E1))
            print('         E0[x]=%s E0[y]=%s E1[x]=%s => E1[y]=%s' % (fill(E0, x), fill(E0, y), fill(E1, x), fill(E1, y)))

    # ============================================================ [E]
    print('[E] Lemma H3 (lighter cores force shortcuts) and the swap of Theorem H4')
    for (name, n, uL, uR) in (('rig', 6, '', ''), ('rig', 6, 'f', 'f'), ('alt', 7, '', ''), ('sq', 6, '', '')):
        code = {i: CODES[name](i) for i in range(1, n + 1)}
        alpha = sorted(set(''.join(code.values())) | {'a'} | set(uL + uR))
        ty = make_typing(letter_cmap(alpha))
        R, S = spine_grammar(n, 'a', lambda i: code[i], uL, uR)
        mem = member_fn(R, S)
        P = content_class(CODES[name], n, alpha)
        sp = Spine(n, 'a', code, uL, uR, i0=P[0])
        g = 2
        # two orders and one one-component "node": from offset 1 in gap 0 to offset 1 in gap 2
        pi = list(P)
        pi2 = list(P[1:]) + [P[0]] if len(P) > 2 else list(reversed(P))
        core1, core2 = core_of(pi, g), core_of(pi2, g)
        c = tweight(core1)
        # pseudo-token positions: gap k occupies core indices [k(g+1), k(g+1)+g)
        s_idx, t_idx = 1, 2 * (g + 1) + 1          # cut after 1 z of gap 0, after 1 z of gap 2
        inner1, inner2 = core1[s_idx:t_idx], core2[s_idx:t_idx]
        sw_a = core2[:s_idx] + inner1 + core2[t_idx:]       # context of pi2, yield of pi
        sw_b = core1[:s_idx] + inner2 + core1[t_idx:]       # context of pi, yield of pi2
        wa, wb = tweight(sw_a), tweight(sw_b)
        low = sw_a if wa < wb else sw_b
        check(wa != wb and wa + wb == 2 * c and min(wa, wb) < c,
              '%s n=%d %r: swap of a one-component yield between orders %s and %s (equal cut data): '
              'core weights %d and %d around c=%d' % (name, n, uL + '|' + uR, pi, pi2, wa, wb, c))
        planted = sp.wrap(sp.h(low + aligned_fill(n, c)))
        NH = set(sp.natives_H(P, c))
        steps, short = shortcut_certificate(sp, low, c)
        out, have = replay_k(steps, lambda u: u in NH or u == planted, ty)
        check(out == short and len(short) < len(sp.wrap('a' * sp.N)) and not mem(planted) and mem(short) is False,
              '   from N_H + {lighter swap word} (%d letters): %d steps derive %s (length %d < %d), not in L(G_n)'
              % (len(planted), len(steps), short if len(short) < 70 else short[:30] + '...', len(short),
                 len(sp.wrap('a' * sp.N))))
        if name == 'rig' and uL == '':
            ALLCERTS.append(('E %s n=%d' % (name, n), steps))

    # ============================================================ [F]
    print('[F] letter level, n = 3: h(T(8)) is not substitutable (two-escape recuts create non-token words)')
    n = 3
    for name in ('sq', 'exp', 'pal', 'rnd', 'rig', 'alt'):
        code = {i: CODES[name](i) for i in range(1, n + 1)}
        alpha = sorted(set(''.join(code.values())) | {'a'})
        cm = letter_cmap(alpha)
        hT = sorted({''.join(code[ord(ch) - 64] if ch != 'z' else 'a' for ch in tau)
                     for tau in arrangements(8, n)}, key=lambda u: (len(u), u))
        v = is_closed_exact(hT, cm)
        check(v is not None, '%-4s h(T(8)) (%d words) is NOT (2,c)-substitutable; violation x=%r y=%r E0=%r E1=%r'
              % (name, len(hT), v[2] if v else None, v[3] if v else None, v[0] if v else None, v[1] if v else None))
    # an explicit recut certificate for rig from L(G_3)
    code = {i: RIG[i] for i in range(1, 4)}
    cm = letter_cmap('acde')
    ty = make_typing(cm)
    R, S = spine_grammar(3, 'a', lambda i: code[i])
    mem = member_fn(R, S)
    seeds = spine_language(3, 'a', lambda i: code[i])
    hT = {''.join(code[ord(ch) - 64] if ch != 'z' else 'a' for ch in tau) for tau in arrangements(8, 3)}
    cl = Closure(seeds, ty, max_words=3000).run(max_processed=30)
    nt = sorted((w for w in cl.S if w not in hT), key=lambda u: (len(u), u))
    w0 = nt[0]
    st = cl.certificate(w0)
    out, have = replay(st, mem, ty)
    check(w0 in have and not mem(w0) and w0 not in hT,
          'rig n=3: the non-token word %s is forced from L(G_3) (%d-step certificate, replayed)' % (w0, len(st)))
    for i, s in enumerate(st):
        E0, E1, x, y = s
        print('       step %d: x=%r y=%r E0=%r E1=%r  ->  %s' % (i + 1, x, y, E0, E1, fill(E1, y)))
    print('     (budgeted closure: %d words after %d processed; truncated=%s; no claim is made from it)'
          % (len(cl.S), cl.processed, cl.truncated))
    # random delimited codes c u_i c, u_i in {d,e}^{2..6}
    rng = random.Random(8)
    tried, closed = 0, 0
    cm = letter_cmap('acde')
    while tried < 150:
        us = [''.join(rng.choice('de') for _ in range(rng.randint(2, 6))) for _ in range(3)]
        if len(set(us)) < 3:
            continue
        tried += 1
        code = {i + 1: 'c' + us[i] + 'c' for i in range(3)}
        hT = {''.join(code[ord(ch) - 64] if ch != 'z' else 'a' for ch in tau) for tau in arrangements(8, 3)}
        closed += is_closed_exact(hT, cm) is None
    check(closed == 0, 'search: 150 random delimited codes c u_i c (u_i in {d,e}^{2..6}); '
          'h(T(8)) exactly substitutable for %d of them' % closed)

    # ============================================================ [G]
    print('[G] classification of the certificate steps')
    tot = Counter()
    for (label, steps) in ALLCERTS:
        cnt = Counter(classify(s, None) for s in steps)
        print('     %-12s %s' % (label, '; '.join('%s x%d' % kv for kv in sorted(cnt.items()))))
        tot.update(cnt)
    print('     total over the listed certificates:')
    for k, v in sorted(tot.items()):
        print('       %-40s %d' % (k, v))
    print()
    sys.stderr.write('time %.0fs\n' % (time.time() - T0))
    print('FAILED: %d' % len(FAILS))
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
