#!/usr/bin/env python3
"""check_claude_problemQ_round6_2026-11-09.py  (Python 3 standard library only)

Companion to reviews/claude_problemQ_round6_2026-11-09.md.
Problem Q, case III (b^4 occurs, c^4 must not), branch (B).

Every inference is an instance of one of the two rules
  SUB_1, SUB_2 :  E[X], E[Y], H[X] in L,  c(X_i) = c(Y_i) for all i,
                  all components nonempty, and (arity 2) the middle fixed
                  parts of E and H nonempty   ==>   H[Y] in L.
The PROVER below follows the proofs of the report literally
(Lemma 2.1 moves, Lemma F'/F'^R fusion, Lemma E swaps, chain lemma,
lifted (KL) certificates, Theorem S) and records each step.
The independent REPLAY function re-checks every recorded step from the
seed set only.  A forced word containing cccc is a certificate that NO
L in C_{2,c} containing the seeds avoids c^4 (i.e. the seed situation is
impossible in case III).  Failure to force is only an observation.

Parts
  [1] replay of the (KL) base certificates (bcc, bbc, bcb, xpxxq, pxxqx);
      step data copied from reviews/chatgpt_case2_branches_2026-11-04.md App. A,
      replayed by the verifier of this file.
  [2] (O2) literal: seeds a^k, bbbb, ONE word a F F a^t; F = bcccb, bccb, bcbcb.
  [3] branch (B*) from generic seeds: every block F over {b,c} with both
      letters, |F| <= 7, not containing c^4: a c^4-certificate unless F is
      (bc)^j or (cb)^j.  Seeds: a^k, bbbb, SB(F,d), SB(G,dG), one two-block
      word a F a G a^* with a-count k-d-dG (G = bc).
  [4] mixed roots (bc)^i, (cb)^j: two independent certificates
      (chain PQ by b-fusion; chain QP by lifted bcb with z = c).
  [5] Theorem S on a common root: SB(bc,1), SB(bcbc,3) force a^{k-1}.
  [6] b-cap lemma demo (Section 7 of the report).
  [7] (d=2) repetitions of [3] for some blocks with unequal losses.
  [8] (O2) literal for blocks with both ends c (not covered by b-fusion):
      bounded closure search (method of check_claude_case3_bfusion_2026-11-04.py)
      with seeds a^5, bbbb, SB(F,1), SB(F^2,2) only.  A hit is replayed as a
      certificate; a miss is an observation only.
Windows: py -3 check_claude_problemQ_round6_2026-11-09.py
"""
import itertools
import sys
import time

FOUR_C = 'cccc'


# ---------------------------------------------------------------- basics
def fill(ctx, xs):
    assert len(ctx) == len(xs) + 1
    return ''.join(ctx[i] + xs[i] for i in range(len(xs))) + ctx[-1]


def cont(w):
    return frozenset(w)


def runs(w, x):
    out, i, n = [], 0, len(w)
    while i < n:
        if w[i] == x:
            j = i
            while j < n and w[j] == x:
                j += 1
            out.append((i, j))
            i = j
        else:
            i += 1
    return out


def check_step(known, step):
    """Independent check of one SUB_t step; returns the forced word."""
    t, E, X, Y, H = step
    assert t in (1, 2)
    assert len(X) == len(Y) == t and len(E) == len(H) == t + 1
    assert all(X) and all(Y), 'empty component'
    assert all(cont(u) == cont(v) for u, v in zip(X, Y)), 'content mismatch'
    if t == 2:
        assert E[1] != '' and H[1] != '', 'empty middle fixed part'
    for w in (fill(E, X), fill(E, Y), fill(H, X)):
        assert w in known, ('premise not available', w)
    return fill(H, Y)


def replay(seeds, steps):
    known = set(seeds)
    for st in steps:
        known.add(check_step(known, st))
    return known


# ---------------------------------------------------------------- prover
class Prover:
    def __init__(self, k, seeds, quad):
        self.k = k
        self.seeds = set(seeds)
        self.known = set(seeds)
        self.steps = []
        self.quad = quad          # letter -> (p, q) with p x^4 q a seed
        self.hit = None

    def sub(self, t, E, X, Y, H):
        w = check_step(self.known, (t, E, X, Y, H))
        if w not in self.known:
            self.known.add(w)
            self.steps.append((t, E, X, Y, H))
            if FOUR_C in w and self.hit is None:
                self.hit = w
        return w

    # Lemma 2.1 (SUB_2): move one x from run src (len>=2) to run dst
    def move(self, w, x, src, dst):
        R = runs(w, x)
        (ss, se), (ds, de) = R[src], R[dst]
        assert se - ss >= 2
        p, q = self.quad[x]
        E = (p, x, q)
        if de <= ss:                       # dst left of src
            U, Z, V = w[:de - 1], w[de:ss], w[ss + 2:]
            assert U + x + Z + x + x + V == w
            return self.sub(2, E, (x, x + x), (x + x, x), (U, Z, V))
        U, Z, V = w[:se - 2], w[se:ds], w[ds + 1:]
        assert U + x + x + Z + x + V == w
        return self.sub(2, E, (x + x, x), (x, x + x), (U, Z, V))

    def redistribute(self, w, x, target):
        while True:
            cur = [e - s for s, e in runs(w, x)]
            assert len(cur) == len(target) and sum(cur) == sum(target)
            assert min(target) >= 1
            if cur == list(target):
                return w
            i = next(i for i in range(len(cur)) if cur[i] > target[i])
            j = next(j for j in range(len(cur)) if cur[j] < target[j])
            w = self.move(w, x, i, j)

    # Lemma F' (S left of R) / F'^R (S right of R): delete run R of x
    def fuse(self, w, x, S, Rr):
        R = runs(w, x)
        n, tot = len(R), w.count(x)
        assert tot >= n + 1, 'no spare letter: count < runs + 1'
        tgt = [1] * n
        tgt[S] = tot - (n - 1)
        w = self.redistribute(w, x, tgt)
        R = runs(w, x)
        (ss, se), (rs, re) = R[S], R[Rr]
        assert se - ss >= 2 and re - rs == 1
        if S < Rr:
            u = w[se:rs]
            w1 = self.move(w, x, S, Rr)
            E0 = (w[:se - 2], x + w[re:])
            H = (w[:se - 1], w[re:])
            assert fill(E0, (x + u + x,)) == w1
            return self.sub(1, E0, (x + u + x,), (x + x + u,), H)
        u = w[re:ss]
        w1 = self.move(w, x, S, Rr)
        E0 = (w[:rs] + x, w[ss + 2:])
        H = (w[:rs], w[ss + 1:])
        assert fill(E0, (x + u + x,)) == w1
        return self.sub(1, E0, (x + u + x,), (u + x + x,), H)

    # SB family of block C with loss d, from one word a^s C a^t
    def sb_family(self, w):
        n = w.count('a')
        assert len(runs(w, 'a')) == 2
        w = self.redistribute(w, 'a', [1, n - 1])
        for s in range(2, n):
            w = self.move(w, 'a', 1, 0)
        return n

    # Lemma E swap: in w, the block P starting at pos (preceded by a's)
    # is replaced by C (with the a-adjustment)
    def swap(self, w, pos, P, dP, C, dC):
        k = self.k
        assert w[pos:pos + len(P)] == P
        if dC >= dP:
            e = dC - dP
            X, Y = 'a' * (1 + e) + P, 'a' + C
            E0 = ('', 'a' * (k - dC - 1))
            H = (w[:pos - 1 - e], w[pos + len(P):])
            assert w[pos - 1 - e:pos] == 'a' * (1 + e)
        else:
            e = dP - dC
            X, Y = 'a' + P, 'a' * (1 + e) + C
            E0 = ('', 'a' * (k - dP - 1))
            H = (w[:pos - 1], w[pos + len(P):])
            assert w[pos - 1] == 'a'
        return self.sub(1, E0, (X,), (Y,), H)


class BranchB:
    """Seeds of branch (B*): a^k, bbbb, SB(P,dP), SB(Q,dQ), one two-block
    word a P a Q a^{k-dP-dQ-2}.  Derives chains and separated pairs."""

    def __init__(self, k, P, dP, Q, dQ):
        self.k = k
        seeds = {'a' * k, 'bbbb'}
        for (B, d) in ((P, dP), (Q, dQ)):
            seeds |= {'a' * s + B + 'a' * (k - d - s) for s in range(1, k - d)}
        self.W0 = 'a' + P + 'a' + Q + 'a' * (k - dP - dQ - 2)
        seeds.add(self.W0)
        self.pr = Prover(k, seeds, {'a': ('a' * (k - 4), ''), 'b': ('', '')})
        self.P, self.dP, self.Q, self.dQ = P, dP, Q, dQ
        self.loss = {P: dP, Q: dQ}

    def separated(self, C, Cp, family=False):
        """a^x C a^y Cp a^z with a-count k - dC - dCp (Claim 1)."""
        pr, k = self.pr, self.k
        dC, dCp = self.loss[C], self.loss[Cp]
        tot = k - self.dP - self.dQ
        w = pr.redistribute(self.W0, 'a', [tot - 2, 1, 1])
        w = pr.swap(w, tot - 2, self.P, self.dP, C, dC)
        tot1 = k - dC - self.dQ
        w = pr.redistribute(w, 'a', [1, tot1 - 2, 1])
        w = pr.swap(w, 1 + len(C) + tot1 - 2, self.Q, self.dQ, Cp, dCp)
        tot2 = k - dC - dCp
        assert w.count('a') == tot2
        if family:
            for p in range(1, tot2 - 1):
                for q in range(1, tot2 - p):
                    pr.redistribute(w, 'a', [p, q, tot2 - p - q])
        return w

    def chain(self, C, Cp):
        """SB(C Cp, dC + dCp) (Claim 2: separation + a-fusion)."""
        pr, k = self.pr, self.k
        w = self.separated(C, Cp)
        tot2 = w.count('a')
        assert tot2 >= 4
        w = pr.redistribute(w, 'a', [tot2 - 2, 1, 1])
        w = pr.fuse(w, 'a', 0, 1)
        CC = C + Cp
        self.loss[CC] = self.loss[C] + self.loss[Cp]
        pr.sb_family(w)
        return CC

    def power(self, F, m):
        cur = F
        for _ in range(m - 1):
            cur = self.chain(cur, F)
        return cur


# ---------------------------------------------------------------- [1] KL base
CERT = {
    'xpxxq': [
        (1, ('', 'aaa'), ('axpxxqa',), ('axpxxqxpxxq',), ('aaxpxxq', '')),
        (2, ('', 'x', 'a'), ('aaxp', 'xqxpxxqa'), ('aaxpx', 'qaxpxxq'), ('', 'xxqxpx', '')),
        (2, ('', 'x', 'a'), ('aaxpx', 'qxpxxqa'), ('aaxp', 'xqaxpxxq'), ('', 'xqxpxx', '')),
        (1, ('aaxp', 'xpxxq'), ('xxqaxpxxq',), ('xxxqxpxqa',), ('aaxpxqxpx', ''))],
    'pxxqx': [
        (1, ('', 'aa'), ('aaapxxqx',), ('apxxqxapxxqx',), ('', 'pxxqxa')),
        (2, ('', 'x', 'a'), ('aapxxqxpx', 'qxa'), ('apxxqxap', 'xqxa'), ('', 'xqxpxx', '')),
        (2, ('', 'x', 'a'), ('aapxxqxp', 'xqxa'), ('apxxqxpx', 'qxaa'), ('', 'xxqxpx', '')),
        (1, ('apxxqx', 'qxa'), ('apxxqxpxx',), ('apxqxpxxx',), ('', 'xqxpxqxaa'))],
    'bcc': [
        (2, ('', 'c', 'a'), ('aabc', 'bcca'), ('abccb', 'cbcca'), ('', 'cbcc', '')),
        (1, ('', 'aa'), ('aaabcc',), ('abccbccbcc',), ('', 'bcca')),
        (1, ('abccb', 'cbcca'), ('cbcc',), ('ccbc',), ('abccbcbcc', 'a'))],
    'bbc': [
        (1, ('', 'aa'), ('aaabbc',), ('abbcbbcbbc',), ('', 'bbca')),
        (2, ('', 'b', 'a'), ('aabbc', 'bca'), ('abbcb', 'cbbca'), ('', 'bbcb', '')),
        (1, ('abbc', 'bcbbca'), ('bbcb',), ('bbbc',), ('abbcb', 'cbbca'))],
    'bcb': [
        (1, ('', 'a'), ('aaabcba',), ('abcbaabcb',), ('a', '')),
        (2, ('', 'b', 'a'), ('aabcb', 'cba'), ('abc', 'aabcb'), ('', 'bcbb', '')),
        (2, ('', 'b', 'a'), ('aabc', 'bcba'), ('aabcb', 'cba'), ('', 'bbcb', '')),
        (1, ('', 'aabcb'), ('aabcb',), ('abcbcbb',), ('', 'bbcbcba'))],
}
TERM = {'bcc': 'cccc', 'bbc': 'bbbb', 'bcb': 'bbbb', 'xpxxq': 'xxxx', 'pxxqx': 'xxxx'}


def kl_initial(k, F, d):
    words = {'a' * k}
    for j in (1, 2, 3):
        for s in range(1, k - j * d):
            words.add('a' * s + F * j + 'a' * (k - j * d - s))
    for i in range(1, k - 2 * d):
        for j in range(1, k - 2 * d - i):
            words.add('a' * i + F + 'a' * j + F + 'a' * (k - 2 * d - i - j))
    return words


def lift(steps, h, pad):
    m = lambda w: ''.join(h[ch] for ch in w)
    out = []
    for (t, E, X, Y, H) in steps:
        out.append((t, (pad + m(E[0]),) + tuple(m(e) for e in E[1:]),
                    tuple(m(x) for x in X), tuple(m(y) for y in Y),
                    (pad + m(H[0]),) + tuple(m(e) for e in H[1:])))
    return out


def part1():
    print('[1] replay of the (KL) base certificates')
    for tm, st in CERT.items():
        known = replay(kl_initial(6, tm, 1), st)
        last = fill(st[-1][4], st[-1][3])
        assert TERM[tm] in last
        print('   ', tm, 'steps', len(st), 'terminal', last, 'contains', TERM[tm])


def kl_template(F):
    """(template, homomorphism) of (KL) giving c^4 for F (one end c with cc,
    or both ends c).  Returns None if (KL) gives no c^4."""
    if F[0] == 'c' and F[-1] == 'c':
        return 'bcb', {'b': 'c', 'c': F[1:-1]}
    if F.startswith('cc'):
        return 'bbc', {'b': 'c', 'c': F[2:]}
    if F.endswith('cc'):
        return 'bcc', {'b': F[:-2], 'c': 'c'}
    if 'cc' in F and F[0] == 'c':          # F = c P cc Q, ends with b
        i = F.index('cc', 1)
        return 'xpxxq', {'x': 'c', 'p': F[1:i], 'q': F[i + 2:]}
    if 'cc' in F and F[-1] == 'c':          # F = P cc Q c, starts with b
        i = F.rindex('cc', 0, len(F) - 1)
        return 'pxxqx', {'x': 'c', 'p': F[:i], 'q': F[i + 2:-1]}
    return None


def run_kl(bb, F):
    """F has SB in branch bb; derive (KL) seeds for F and run the lifted cert."""
    pr, k = bb.pr, bb.k
    d = bb.loss[F]
    assert k >= 6 * d
    F2 = bb.chain(F, F)
    bb.chain(F2, F)
    bb.separated(F, F, family=True)
    tm, hom = kl_template(F)
    hom = dict(hom)
    hom['a'] = 'a' * d
    for z in 'abcpqx':
        hom.setdefault(z, z)
    need = kl_initial(k, F, d)
    missing = need - pr.known
    assert not missing, ('KL seeds not derived', sorted(missing)[:3])
    for st in lift(CERT[tm], hom, 'a' * (k - 6 * d)):
        pr.sub(*st)
    return tm


def run_bfusion(bb, block):
    """b-fusion on a word a^s block a^t: delete every b-run lying between
    the first and the last c (survivor outside the c-span)."""
    pr = bb.pr
    w = next(x for x in sorted(pr.known) if x.startswith('a' + block + 'a'))
    while pr.hit is None:
        R = runs(w, 'b')
        fc, lc = w.index('c'), w.rindex('c')
        inner = [i for i, (s, e) in enumerate(R) if fc < s and e <= lc]
        if not inner:
            break
        if R[0][1] <= fc:
            w = pr.fuse(w, 'b', 0, inner[0])
        else:
            assert R[-1][0] > lc
            w = pr.fuse(w, 'b', len(R) - 1, inner[-1])
    return w


def classify(F):
    alt = all(F[i] != F[i + 1] for i in range(len(F) - 1))
    if alt and F[0] != F[-1]:
        return 'root'
    if F[0] == 'b' and F[-1] == 'b':
        return 'bfusion'
    if (F[0] == 'b' or F[-1] == 'b') and 'bb' in F:
        return 'bfusion'
    return 'KL'


def instance(F, d, k, G='bc', dG=1, show=False):
    bb = BranchB(k, F, d, G, dG)
    route = classify(F)
    if route == 'root':
        return route, None, bb
    if route == 'bfusion':
        F4 = bb.power(F, 4)
        run_bfusion(bb, F4)
    else:
        route = route + ':' + run_kl(bb, F)
    assert bb.pr.hit is not None, ('no c^4 for', F)
    known = replay(bb.pr.seeds, bb.pr.steps)
    assert bb.pr.hit in known
    return route, bb.pr.hit, bb


def print_cert(pr, limit=None):
    for i, (t, E, X, Y, H) in enumerate(pr.steps, 1):
        if limit is None or i > len(pr.steps) - limit:
            print('      %4d SUB_%d E=%s X=%s Y=%s H=%s => %s' %
                  (i, t, E, X, Y, H, fill(H, Y)))


# ---------------------------------------------------------------- [2]
def part2():
    print('[2] (O2) literal: seeds a^k, bbbb, one word a F F a^t (k=7, loss 2d=2)')
    k = 7
    for F in ('bcccb', 'bccb', 'bcbcb', 'bbcbc', 'cbcbb'):
        w0 = 'a' + F + F + 'a' * (k - 2 - 1)
        seeds = {'a' * k, 'bbbb', w0}
        pr = Prover(k, seeds, {'a': ('a' * (k - 4), ''), 'b': ('', '')})
        w = w0
        while pr.hit is None and FOUR_C not in w:
            R = runs(w, 'b')
            fc, lc = w.index('c'), w.rindex('c')
            inner = [i for i, (s, e) in enumerate(R) if fc < s and e <= lc]
            if R[0][1] <= fc:
                w = pr.fuse(w, 'b', 0, inner[0])
            else:
                w = pr.fuse(w, 'b', len(R) - 1, inner[-1])
        replay(seeds, pr.steps)
        print('    F=%-6s seed %-16s steps %2d forced %s' % (F, w0, len(pr.steps), pr.hit))
        if F == 'bcccb':
            print_cert(pr)


# ---------------------------------------------------------------- [3]
def part3(maxlen=9, k=12, d=1):
    print('[3] branch (B*): all blocks F over {b,c}, 2<=|F|<=%d, k=%d, d=%d' % (maxlen, k, d))
    stats, roots, total_steps = {}, [], 0
    for n in range(2, maxlen + 1):
        for t in itertools.product('bc', repeat=n):
            F = ''.join(t)
            if set(F) != {'b', 'c'} or FOUR_C in F:
                continue
            route, hit, bb = instance(F, d, k)
            if route == 'root':
                roots.append(F)
                continue
            stats[route] = stats.get(route, 0) + 1
            total_steps += len(bb.pr.steps)
    print('    certificates by route:', dict(sorted(stats.items())),
          'total steps', total_steps)
    print('    no certificate attempted (alternating, one end b one end c):', roots)
    exp = [F for F in roots]
    assert all(F in ('bc' * j, 'cb' * j) for F in exp for j in [len(F) // 2]), exp
    for F, show in (('bcccb', 12), ('bcb', 12), ('cbb', 8), ('cbcc', 6)):
        route, hit, bb = instance(F, d, k)
        print('    example F=%s route=%s steps=%d forced=%s (last %d steps shown)'
              % (F, route, len(bb.pr.steps), hit, show))
        print_cert(bb.pr, show)


# ---------------------------------------------------------------- [4]
def part4():
    print('[4] mixed roots P=(bc)^i, Q=(cb)^j')
    for (i, j, dP, dQ, k) in ((1, 1, 1, 1, 14), (1, 2, 1, 2, 20), (2, 1, 2, 1, 20)):
        P, Q = 'bc' * i, 'cb' * j
        bb = BranchB(k, P, dP, Q, dQ)
        PQ = bb.chain(P, Q)
        PQ2 = bb.chain(PQ, PQ)
        run_bfusion(bb, PQ2)
        replay(bb.pr.seeds, bb.pr.steps)
        print('    PQ=%s (both ends b) b-fusion on (PQ)^2: steps %d forced %s'
              % (PQ, len(bb.pr.steps), bb.pr.hit))
        bb2 = BranchB(k, P, dP, Q, dQ)
        QP = bb2.chain(Q, P)
        tm = run_kl(bb2, QP)
        replay(bb2.pr.seeds, bb2.pr.steps)
        print('    QP=%s (both ends c) lifted %s: steps %d forced %s'
              % (QP, tm, len(bb2.pr.steps), bb2.pr.hit))


# ---------------------------------------------------------------- [5]
def part5():
    print('[5] Theorem S on a common root u=bc: SB(bc,1), SB(bcbc,3), k=12')
    k = 12
    bb = BranchB(k, 'bc', 1, 'bcbc', 3)
    pr = bb.pr
    C2 = bb.chain('bc', 'bc')                    # SB(bcbc, 2) by the chain lemma
    w2 = 'a' + C2 + 'a' * (k - 2 - 1)            # a-count 10
    w3 = 'a' + 'bcbc' + 'a' * (k - 3 - 1)        # a-count 9 (seed)
    assert w2 in pr.known and w3 in pr.known
    delta = w2.count('a') - w3.count('a')
    E = ('a' + 'bcbc' + 'a' * (w3.count('a') - 2), '')
    assert fill(E, ('a',)) == w3 and fill(E, ('a' * (1 + delta),)) == w2
    H = ('a' * (k - 1 - delta), '')
    out = pr.sub(1, E, ('a' * (1 + delta),), ('a',), H)
    replay(pr.seeds, pr.steps)
    print('    forced', out, '(a-word shorter than k: contradiction with mu_a = k);',
          'steps', len(pr.steps))
    print_cert(pr, 2)


# ---------------------------------------------------------------- [6]
def part6():
    print('[6] b-cap lemma: a b-spare word with >=4 c after the first b-run')
    k = 6
    for N in ('cbbcbcbcbc', 'bcbcbbcbcb', 'ccbcbcbcbcbb'):
        w0 = 'a' + N + 'a' * (k - 1 - 1)
        seeds = {'a' * k, 'bbbb', w0}
        pr = Prover(k, seeds, {'a': ('a' * (k - 4), ''), 'b': ('', '')})
        w = w0
        while pr.hit is None:
            R = runs(w, 'b')
            if len(R) == 1:
                break
            w = pr.fuse(w, 'b', 0, 1)
        replay(seeds, pr.steps)
        print('    N=%s steps %d forced %s' % (N, len(pr.steps), pr.hit))
        assert pr.hit


# ---------------------------------------------------------------- [7]
def part7():
    print('[7] d=2, dG=1, k=24 (unequal losses)')
    for F in ('bcccb', 'bcb', 'cbb', 'cbcc', 'ccbc', 'bcbcc', 'cbbc'):
        route, hit, bb = instance(F, 2, 24, G='bc', dG=1)
        print('    F=%-6s route=%-10s steps=%4d forced=%s' % (F, route, len(bb.pr.steps), hit))


# ---------------------------------------------------------------- [8]
def occurrences(w, t):
    n = len(w)
    if t == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[i:j],), (w[:i], w[j:])
    else:
        for i in range(n):
            for j in range(i + 1, n):
                for p in range(j + 1, n):
                    for q in range(p + 1, n + 1):
                        yield (w[i:j], w[p:q]), (w[:i], w[j:p], w[q:])


def closure_search(seeds, maxlen, rounds):
    from collections import defaultdict
    known, prov = set(seeds), {}
    for _ in range(rounds):
        added = {}
        for t in (1, 2):
            D, byctx = defaultdict(set), defaultdict(set)
            for w in sorted(known):
                for xs, E in occurrences(w, t):
                    if t == 2 and not E[1]:
                        continue
                    D[xs].add(E)
                    byctx[(tuple(frozenset(x) for x in xs), E)].add(xs)
            for (_, E), xset in sorted(byctx.items(), key=lambda z: str(z[0])):
                xl = sorted(xset)
                for X in xl:
                    for Y in xl:
                        if X == Y:
                            continue
                        for H in sorted(D[X] - D[Y]):
                            w = fill(H, Y)
                            if len(w) > maxlen or w in known or w in added:
                                continue
                            added[w] = (t, E, X, Y, H)
                            if FOUR_C in w:
                                prov.update(added)
                                return w, prov
        if not added:
            return None, prov
        known.update(added)
        prov.update(added)
    return None, prov


def extract(goal, seeds, prov):
    order, done = [], set()

    def visit(w):
        if w in seeds or w in done:
            return
        t, E, X, Y, H = prov[w]
        for v in (fill(E, X), fill(E, Y), fill(H, X)):
            visit(v)
        done.add(w)
        order.append((t, E, X, Y, H))
    visit(goal)
    return order


def part8():
    print('[8] (O2) literal, both ends c: seeds a^5, bbbb, SB(F,1), SB(F^2,2)')
    k = 5
    for F, maxlen, rounds in (('cbbc', 14, 3), ('cbbbc', 14, 3)):
        S = {'a' * k, 'bbbb'}
        for j in (1, 2):
            S |= {'a' * s + F * j + 'a' * (k - j - s) for s in range(1, k - j)}
        goal, prov = closure_search(S, maxlen, rounds)
        if goal is None:
            print('    F=%s: no c^4 within maxlen %d, %d rounds (observation only)'
                  % (F, maxlen, rounds))
            continue
        cert = extract(goal, S, prov)
        replay(S, cert)
        print('    F=%s: certificate, %d steps, forced %s' % (F, len(cert), goal))
        for i, (t, E, X, Y, H) in enumerate(cert, 1):
            print('      %d SUB_%d E=%s X=%s Y=%s H=%s => %s' % (i, t, E, X, Y, H, fill(H, Y)))


def main():
    t0 = time.time()
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    part7()
    part8()
    print('ALL CHECKS PASSED  (%.1f s)' % (time.time() - t0))


if __name__ == '__main__':
    main()
