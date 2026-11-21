#!/usr/bin/env python3
"""R6 (Claude Opus 5.5, 2026-11-22): finite checks for the report.

Python 3 standard library only, no network.  Run:  python3 -I run_all.py
Every iteration that matters is sorted, so the output does not depend on
PYTHONHASHSEED.  Exit code 0 iff every assertion holds.

Sections
  [A] engine self-test: the two Thue-Morse re-cuttings of chatgpt_sl_fanout2 sec.3
  [B] F (Thue-Morse, length 16) forces aaaa and bbbb  (certificates, replay, wrapping)
  [C] binary power forcing: exhaustive DFS (every binary word of length 14 contains
      some u^4 or forces a letter fourth power)
  [D] ternary: a rigid fourth-power-free word of length 32 ({w} is (2,c)-substitutable)
  [E] Theorem C3 / D1 certificates in the Thue-Morse host (no periodic frame)
  [F] T1(b): Thue-Morse doubling with escapes, n=3,4: exact Rect test of L(G_n),
      searched shortcuts with replayed certificates, size/thickness of G_n
  [G] Proposition D3: a code with injective Parikh differences has no shared move
  [H] calibration in the periodic spine A_i -> A_{i-1}A_{i-1} | e_i, z=a, n=4
"""
import sys
import heapq
from collections import defaultdict, deque
from functools import lru_cache

sys.setrecursionlimit(100000)
FAILS = []


def check(cond, msg):
    print(('  ok   ' if cond else '  FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


# ---------------------------------------------------------------- engine
def cont(w):
    return ''.join(sorted(set(w)))


def fill(E, t):
    if len(t) == 1:
        return E[0] + t[0] + E[1]
    return E[0] + t[0] + E[1] + t[1] + E[2]


def ttype(t):
    return tuple(cont(p) for p in t)


def occurrences(w, dmax=2):
    """All admissible arity-1 and arity-2 tuple occurrences (nonempty components,
    nonempty middle for arity 2; outer parts may be empty)."""
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield (w[:i], w[j:]), (w[i:j],)
    if dmax >= 2:
        for i in range(n):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    for l in range(k + 1, n + 1):
                        yield (w[:i], w[j:k], w[l:]), (w[i:j], w[k:l])


def check_step(E0, E1, x, y, member):
    """One SUB step of (2,c)-substitutability, checked independently.
    E0[x], E0[y], E1[x] in L, componentwise equal content  ==>  E1[y] in L."""
    d = len(x)
    assert d in (1, 2) and len(y) == d and len(E0) == d + 1 and len(E1) == d + 1
    assert all(p != '' for p in x) and all(p != '' for p in y), 'empty component'
    if d == 2:
        assert E0[1] != '' and E1[1] != '', 'empty middle'
    assert ttype(x) == ttype(y), 'type mismatch'
    for wd in (fill(E0, x), fill(E0, y), fill(E1, x)):
        assert member(wd), 'premise not in L: %r' % wd
    return fill(E1, y)


class Closure:
    """Forced words: closure of seeds under SUB_1, SUB_2, outputs longer than cap
    discarded (sound: every word produced lies in every (2,c)-substitutable
    language containing the seeds; incomplete because of the cap)."""

    def __init__(self, seeds, cap, dmax=2, stop=None, max_words=10 ** 6, order='bfs'):
        self.cap, self.dmax, self.stop, self.max_words, self.order = cap, dmax, stop, max_words, order
        self.S, self.prov, self.parent, self.members, self.ctxs = set(), {}, {}, {}, {}
        self.ctx_of = defaultdict(set)
        self.bucket, self.edges = {}, defaultdict(list)
        self.queue, self.heap, self.cnt = deque(), [], 0
        self.found, self.truncated = None, False
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
        if E in self.ctx_of[t]:
            return
        self.ctx_of[t].add(E)
        r = self.find(t)
        if E not in self.ctxs[r]:
            self.ctxs[r][E] = None
            for y in self.members[r]:
                self._emit(E, t, y)
        key = (ttype(t), E)
        if key in self.bucket:
            t2 = self.bucket[key]
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

    def run(self):
        while (self.queue or self.heap) and self.found is None and not self.truncated:
            w = heapq.heappop(self.heap)[2] if self.order == 'short' else self.queue.popleft()
            for E, t in occurrences(w, self.dmax):
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


def replay(steps, seed_member, target):
    """Independent replay: every premise is a seed (checked by seed_member, e.g. an
    exact grammar parser) or was produced by an earlier step."""
    have = set()

    def member(u):
        return u in have or seed_member(u)
    for (E0, E1, x, y) in steps:
        have.add(check_step(E0, E1, x, y, member))
    assert target in have or seed_member(target)
    return len(steps)


def is_closed(S, dmax=2):
    """Exact test that the finite set S is (dmax, content)-substitutable.
    Returns None, or a violation (E0, E1, x, y): E0[x],E0[y],E1[x] in S, E1[y] not in S."""
    S = sorted(set(S), key=lambda u: (len(u), u))
    groups, ctx_of = defaultdict(list), defaultdict(set)
    for w in S:
        for E, t in occurrences(w, dmax):
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
        if i < n:                      # B_n would be unreachable (grammar kept reduced)
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


def language(R, S):
    memo = {}

    def L(X):
        if X not in memo:
            out = set()
            for rhs in R[X]:
                part = {''}
                for sym in rhs:
                    part = {p + q for p in part for q in (L(sym) if sym in R else {sym})}
                out |= part
            memo[X] = out
        return memo[X]
    return sorted(L(S), key=lambda u: (len(u), u))


def member_fn(R, S):
    """Exact membership by recursive parsing (independent of enumeration)."""
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


def esc_words(R, S, k):
    """W and the words with exactly one (k=1) or at most two (k=2) escaped nodes."""
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
    """||G|| proxy = sum over rules of (1 + |rhs symbols| + terminal letters);
    theta_G = max over rules of the shortest sentence using the rule (fan-out 1)."""
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


def has_letter4(w):
    return any(w[i] == w[i + 1] == w[i + 2] == w[i + 3] for i in range(len(w) - 3))


def has_u4(w):
    L = len(w)
    for l in range(1, L // 4 + 1):
        for i in range(L - 4 * l + 1):
            if w[i:i + 4 * l] == w[i:i + l] * 4:
                return True
    return False


def ends_with_u4(w):
    L = len(w)
    return any(w[L - 4 * l:] == w[L - l:] * 4 for l in range(1, L // 4 + 1))


# ================================================================ [A]
print('[A] engine self-test: Thue-Morse re-cuttings (chatgpt_sl_fanout2_2026-11-01 sec.3)')
F = 'abbabaabbaababba'
inF = lambda u: u == F
F1 = check_step(('', 'b', 'baababba'), ('', 'baabb', 'abba'), ('abba', 'aab'), ('ab', 'abaab'), inF)
F2 = check_step(('', 'b', 'ababba'), ('', 'bbaa', 'bba'), ('abbabaa', 'ba'), ('ab', 'abaabba'), inF)
check(F1 == 'abbaabbabaababba', '(4): F -> F_1 = %s' % F1)
check(F2 == 'abbbaaabaabbabba' and 'bbb' in F2, '(6): F -> F_2 = %s (contains bbb)' % F2)
check(not has_u4(F) and 'aaa' not in F and 'bbb' not in F, 'F is cube-free and has no fourth power')

# ================================================================ [B]
print('[B] F forces a word with aaaa and a word with bbbb (Proposition P1)')
certs = {}
for pat in ('aaaa', 'bbbb'):
    c = Closure([F], 16, stop=lambda w, p=pat: p in w, max_words=20000).run()
    check(c.found is not None, 'closure of {F} reaches a word containing %s: %s' % (pat, c.found))
    st = c.certificate(c.found)
    k = replay(st, inF, c.found)
    certs[pat] = (st, c.found)
    print('     certificate (%d steps):' % k)
    for (E0, E1, x, y) in st:
        print('       E0=%r E1=%r x=%r y=%r  ->  %s' % (E0, E1, x, y, fill(E1, y)))
# wrapping lemma: certificates lift to P F Q
for (P, Q) in (('c', 'ca'), ('bb', ''), ('', 'acb')):
    for pat, (st, tgt) in certs.items():
        lifted = []
        for (E0, E1, x, y) in st:
            lifted.append(((P + E0[0],) + E0[1:-1] + (E0[-1] + Q,),
                           (P + E1[0],) + E1[1:-1] + (E1[-1] + Q,), x, y))
        replay(lifted, lambda u, P=P, Q=Q: u == P + F + Q, P + tgt + Q)
check(True, 'all certificates lift to P F Q for (P,Q) in {(c,ca),(bb,),(,acb)}')

# ================================================================ [C]
print('[C] binary power forcing: exhaustive DFS over words avoiding u^4 whose closure avoids letter^4')
trunc = [0]
best = ['']
count = [0]


replayed = [0]


def okC(w):
    if ends_with_u4(w):
        return False
    c = Closure([w], len(w), stop=has_letter4, max_words=5000).run()
    if c.truncated:
        trunc[0] += 1
        return True          # unknown: keep exploring (conservative)
    if c.found is not None:  # pruning only on a replayed certificate
        replay(c.certificate(c.found), lambda u, w=w: u == w, c.found)
        replayed[0] += 1
        return False
    return True


def dfsC(w):
    count[0] += 1
    if len(w) > len(best[0]):
        best[0] = w
    for ch in 'ab':
        if ch == 'b' and w == '':
            continue           # symmetry a<->b: words start with a
        u = w + ch
        if okC(u):
            dfsC(u)


dfsC('')
print('     explored %d words, longest %r (length %d), truncated closures %d, pruned by replayed certificates %d'
      % (count[0], best[0], len(best[0]), trunc[0], replayed[0]))
check(len(best[0]) == 13 and trunc[0] == 0,
      'every binary word of length 14 contains some u^4 or forces a word with a letter fourth power')

# ================================================================ [D]
print('[D] ternary: a rigid word without fourth powers (no universal power forcing over 3 letters)')
w32 = 'aaabaabbcaabcbcabccaaaccbbcccbbb'
v = is_closed([w32])
check(len(w32) == 32 and not has_u4(w32), 'w32 has length 32 and contains no u^4')
check(v is None, '{w32} is (2,c)-substitutable (exact test of all arity-1/2 occurrences)')

# ================================================================ [E]
print('[E] Theorem C3 and Theorem D1 in the Thue-Morse host (no periodic frame)')


def tm_certificate(code, n, Ns, Np, Nq, Nl, alpha, beta, gamma, eta, x, y):
    """C2 step then C1 step.  Ns, Np: frames (start,end) of e and e' (common start);
    Nq: frame of the host f (common end with Ns); Nl: a native frame of f'."""
    R, S = tm_grammar(n, lambda i: code[i])
    W = tree_yield(R, S)
    mem = member_fn(R, S)
    (i_s, j_s), (i_p, j_p), (i_q, j_q), (i_l, j_l) = Ns, Np, Nq, Nl
    assert i_s == i_p and j_q == j_s
    have = set()
    m2 = lambda u: u in have or mem(u)
    out1 = check_step((W[:i_s] + alpha, beta, ''), (W[:i_q] + gamma, eta, ''),
                      (x, W[j_s:]), (y, W[j_p:]), m2)
    have.add(out1)
    fprime = gamma + y + eta
    out2 = check_step(('', fprime, ''), ('', W[i_l:j_l], ''),
                      (W[:i_l], W[j_l:]), (W[:i_q], W[j_p:]), m2)
    return W, out1, out2, mem


nd6 = nodes(*tm_grammar(6, lambda i: 'c'))
print('     n=6 nodes used:', [t for t in nd6 if (t[1], t[2]) in ((16, 32), (16, 24), (20, 24), (22, 24))])
code1 = {i: 'c' * i for i in range(1, 7)}
W, o1, o2, mem = tm_certificate(code1, 6, (16, 24), (16, 32), (20, 24), (16, 24), '', 'cc', '', 'c', 'c', 'cc')
check(o1 == W[:20] + 'ccc' + W[32:], 'C3, code c^i: C2 step places c^3 at frame (20,32)')
check(len(o2) == 60 and set(o2) == {'a', 'b'} and not mem(o2),
      'C3, code c^i: C1 step gives a {a,b}-word of length 60 < 64, not in L(G_6)')
code2 = {i: 'c' + 'a' * i for i in range(1, 7)}
W, o1, o2, mem = tm_certificate(code2, 6, (16, 24), (16, 32), (20, 24), (16, 24), 'c', 'aa', 'c', 'a', 'a', 'aa')
check(len(o2) == 60 and set(o2) == {'a', 'b'} and not mem(o2), 'C3, code ca^i: shortcut of length 60')
code3 = {1: 'acba', 2: 'acbba', 3: 'bcbcc', 4: 'bcbbcc', 5: 'cc', 6: 'ccc'}
W, o1, o2, mem = tm_certificate(code3, 6, (16, 24), (16, 32), (22, 24), (20, 24), 'b', 'cc', 'a', 'a', 'cb', 'cbb')
check(len(o2) == 58 and set(o2) == {'a', 'b'} and not mem(o2),
      'D1, pairs (1->2),(3->4) share cb->cbb: shortcut of length 58 (= 64 - (R1+R4-R3-R2))')

# ================================================================ [F]
print('[F] T1(b): Thue-Morse doubling A_i->A_{i-1}B_{i-1}|e_i, B_i->B_{i-1}A_{i-1}|e_i\'')
RA = {1: 'acca', 2: 'bcbc', 3: 'caca', 4: 'bbca'}
RB = {1: 'cbca', 2: 'caac', 3: 'bccb', 4: 'cbbc'}
designs = [
    ('c^i', lambda i: 'c' * i, None),
    ('ca^i / cb^i', lambda i: 'c' + 'a' * i, lambda i: 'c' + 'b' * i),
    ('c bin(i) c', lambda i: 'c' + bin(i)[2:].replace('0', 'a').replace('1', 'b') + 'c', None),
    ('fixed random code', lambda i: RA[i], lambda i: RB[i]),
    ('c TM-prefix(i) c', lambda i: 'c' + 'abbabaab'[:i] + 'c', lambda i: 'c' + 'baababba'[:i] + 'c'),
]
for n in (3, 4):
    for name, ea, eb in designs:
        R, S = tm_grammar(n, ea, eb)
        L = language(R, S)
        W = tree_yield(R, S)
        mem = member_fn(R, S)
        size, theta, nv, npr = size_and_thickness(R, S)
        viol = is_closed(L)
        stop = lambda w, W=W: set(w) <= {'a', 'b'} and len(w) < len(W)
        res = None
        tried = []
        for seedmode in ('single', 'L'):
            seeds = L if seedmode == 'L' else esc_words(R, S, 1)
            c = Closure(seeds, len(W), stop=stop, max_words=40000).run()
            tried.append('%s:%s' % (seedmode, 'found' if c.found else ('budget' if c.truncated else 'closed')))
            if c.found:
                st = c.certificate(c.found)
                k = replay(st, mem, c.found)
                res = (c.found, k, seedmode)
                break
        print('     n=%d %-18s |V|=%d |P|=%d size=%d theta=%d |L(G)|=%d' % (n, name, nv, npr, size, theta, len(L)))
        print('        Rect of L(G_n): %s' % ('holds' if viol is None else
              'VIOLATED  E0=%r E1=%r x=%r y=%r, E1[y]=%r not in L(G_n)' % (viol[0], viol[1], viol[2], viol[3], fill(viol[1], viol[3]))))
        check(viol is not None and not mem(fill(viol[1], viol[3])), 'n=%d %s: exact Rect violation confirmed by parser' % (n, name))
        if res:
            print('        forced shortcut %r (length %d < %d), %d-step certificate replayed (seeds %s)'
                  % (res[0], len(res[0]), len(W), res[1], res[2]))
        else:
            print('        no shortcut found within budget (%s): INCONCLUSIVE' % ', '.join(tried))

# ================================================================ [G]
print('[G] Proposition D3: code e_s = c a^s c b^(s^2) c has no move shared by two upward pairs')


def moves_of(e, f):
    """All moves (x,y), c(x)=c(y), x,y nonempty, with e = alpha x beta, f = alpha y beta."""
    out = set()
    for a in range(min(len(e), len(f)) + 1):
        if e[:a] != f[:a]:
            break
        for b in range(min(len(e), len(f)) - a + 1):
            if b and e[len(e) - b:] != f[len(f) - b:]:
                break
            x, y = e[a:len(e) - b], f[a:len(f) - b]
            if x and y and x != y and set(x) == set(y):
                out.add((x, y))
    return out


T = 7
code = {s: 'c' + 'a' * s + 'c' + 'b' * (s * s) + 'c' for s in range(1, T + 1)}
owner = {}
shared = 0
for p in range(1, T + 1):
    for q in range(p + 1, T + 1):
        for mv in moves_of(code[p], code[q]):
            if mv in owner and owner[mv] != (p, q):
                shared += 1
            owner.setdefault(mv, (p, q))
check(shared == 0, 'T=%d: %d moves realized, none by two distinct upward pairs' % (T, len(owner)))
diffs = [(q - p, q * q - p * p) for p in range(1, T + 1) for q in range(p + 1, T + 1)]
check(len(set(diffs)) == len(diffs), 'Parikh differences of upward pairs are pairwise distinct (the proof)')
# contrast: the code c a^s c b^s c shares a move (B3-type), as the theory predicts
code_lin = {s: 'c' + 'a' * s + 'c' + 'b' * s + 'c' for s in range(1, 5)}
check(bool(moves_of(code_lin[1], code_lin[2]) & moves_of(code_lin[2], code_lin[3])),
      'contrast: c a^s c b^s c realizes a common move for (1,2) and (2,3)')
# superincreasing regions: R_q + R_p' = R_p + R_q' only trivially (D1 arithmetic)
Rg = [2 ** k for k in range(1, 9)]
bad = [(p, pp, q, qq) for p in range(8) for pp in range(8) for q in range(8) for qq in range(8)
       if p < pp and q < qq and (p, pp) != (q, qq) and Rg[q] + Rg[pp] == Rg[p] + Rg[qq]]
check(not bad, 'regions 2^k: R_q + R_p\' = R_p + R_q\' has no nontrivial solution (k<=8)')

# ================================================================ [H]
print('[H] calibration, periodic spine A_0->a, A_i->A_{i-1}A_{i-1}|e_i, n=4, seeds = W + single escapes')
for name, cd in (('b^i (dies by B3 for n>=6)', ['b', 'bb', 'bbb', 'bbbb']),
                 ('cb^(i-1) (dies by B3 for n>=6)', ['c', 'cb', 'cbb', 'cbbb']),
                 ('random code (b,cbb,ccaa,cbcc)', ['b', 'cbb', 'ccaa', 'cbcc'])):
    R, S = spine_grammar(4, 'a', lambda i, cd=cd: cd[i - 1])
    W = tree_yield(R, S)
    mem = member_fn(R, S)
    seeds = esc_words(R, S, 1)
    c = Closure(seeds, 16, stop=lambda w: set(w) == {'a'} and len(w) < 16, max_words=100000).run()
    if c.found:
        st = c.certificate(c.found)
        k = replay(st, mem, c.found)
        print('     %-34s forced shortcut %s (%d steps)' % (name, c.found, k))
    else:
        exact = (not c.truncated) and is_closed(c.S) is None
        print('     %-34s capped closure ends with %d words, no shortcut; exactly substitutable: %s'
              % (name, len(c.S), exact))
        if name.startswith('random'):
            check(exact and min(len(u) for u in c.S if set(u) == {'a'}) == 16,
                  'random code: a finite (2,c)-substitutable language with W=a^16 shortest {a}-word exists')
print()
print('FAILED: %d' % len(FAILS))
sys.exit(1 if FAILS else 0)
