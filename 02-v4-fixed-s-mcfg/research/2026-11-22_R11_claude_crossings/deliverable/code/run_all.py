#!/usr/bin/env python3
"""R11 (Claude, 2026-11-22): crossings and exact fills for the root type m={a}.

All checks are finite.  Nothing here proves a universal statement; the
certificates replay instances of the proofs in report.md step by step.

  [A] Rect engine self-test (illegal steps are rejected).
  [B] Lemma SD (single-letter dissolution) on random configurations
      D / N / C (crossing) / F (exact fill): from the native words only,
      derive both words of the one-hole Rect of (Xi2*) and replay every step.
  [C] Projection criterion for classes with two or more non-a letters
      (PNF): exact fills and nested pairs succeed; crossings succeed exactly
      when the projection condition holds; in R15's L_{11,4} the obstruction
      is the content of the compared factors.
  [D] HXi* family forcing with the new dissolving pair for a crossing
      single-letter pair: all M! family words from the prototype, and a
      planted wrong-weight word yields a shorter a-power (P7).
  [E] Exhaustive finite substitutability checks (one- and two-hole,
      content typing): the Parikh-linear model languages, a run-pattern
      candidate (fails, as SLC predicts), and R15's L_{11,4}.
  [F] Independent closure engine: the least substitutable superset of the
      four native words of small single-letter crossings / exact fills
      contains every pair placement; R15's two-letter crossing does not.

Usage:  python3 -I run_all.py > run_all.log      (stdout is deterministic)
Standard library only, no network.  Exit code 0 iff all checks pass.
"""
import sys
import time
import random
import itertools

T_START = time.time()
FAIL = []
MERGED = [0]        # merged blocks that had to be split into witnessed blocks


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("  FAIL:", msg)
    return cond


def content(w):
    return frozenset(w)


def cstr(s):
    return "{" + ",".join(sorted(s)) + "}"


# ---------------------------------------------------------------------------
# [A] Rect engine
# ---------------------------------------------------------------------------
class IllegalStep(Exception):
    pass


class Cert:
    """Known words of L, closed under legal Rect steps only.

    A step (x, y, E0, E1) is legal if: d in {1,2}; all components of x, y are
    nonempty; for d=2 the middles of E0 and E1 are nonempty; componentwise
    contents of x and y agree; E0[x], E0[y], E1[x] are known.  Then E1[y] is
    added.  Nothing else ever adds a word except the axioms.
    """

    def __init__(self, axioms, N):
        self.N = N
        self.known = set(axioms)
        self.axioms = set(axioms)
        self.steps = 0

    @staticmethod
    def fill(E, t):
        if len(t) == 1:
            return E[0] + t[0] + E[1]
        return E[0] + t[0] + E[1] + t[1] + E[2]

    def step(self, x, y, E0, E1):
        d = len(x)
        if d not in (1, 2) or len(y) != d or len(E0) != d + 1 or len(E1) != d + 1:
            raise IllegalStep("arity")
        if any(len(z) == 0 for z in x + y):
            raise IllegalStep("empty component")
        if d == 2 and (len(E0[1]) == 0 or len(E1[1]) == 0):
            raise IllegalStep("empty middle")
        for i in range(d):
            if content(x[i]) != content(y[i]):
                raise IllegalStep("type mismatch %r %r" % (x[i], y[i]))
        a0, b0, a1 = self.fill(E0, x), self.fill(E0, y), self.fill(E1, x)
        for z in (a0, b0, a1):
            if z not in self.known:
                raise IllegalStep("premise not known: %r" % z)
        out = self.fill(E1, y)
        self.known.add(out)
        self.steps += 1
        return out


def runs_of(w):
    """Maximal a-runs as (start, length) and the skeleton of non-a blocks."""
    runs, blocks, i, n = [], [], 0, len(w)
    while i < n:
        j = i
        if w[i] == 'a':
            while j < n and w[j] == 'a':
                j += 1
            runs.append((i, j - i))
        else:
            while j < n and w[j] != 'a':
                j += 1
            blocks.append(w[i:j])
        i = j
    return runs, blocks


def p1_move(C, w, r1, r2, n1, n2):
    """P1' (two-hole slide from W=a^N): a-runs r1 < r2 of w get lengths n1, n2."""
    (s1, l1), (s2, l2) = r1, r2
    assert s1 + l1 <= s2 and n1 + n2 == l1 + l2 and n1 >= 1 and n2 >= 1
    N = C.N
    if l1 + l2 > N - 1:
        raise IllegalStep("P1' room")
    x = ('a' * l1, 'a' * l2)
    y = ('a' * n1, 'a' * n2)
    E0 = ('', 'a' * (N - l1 - l2), '')
    E1 = (w[:s1], w[s1 + l1:s2], w[s2 + l2:])
    return C.step(x, y, E0, E1)


def redistribute(C, w, target):
    """w known; target has the same skeleton and a-count, all runs >= 1."""
    rw, bw = runs_of(w)
    rt, bt = runs_of(target)
    if bw != bt or len(rw) != len(rt) or w[0] != target[0] or w[-1] != target[-1]:
        raise IllegalStep("skeleton mismatch")
    if sum(l for _, l in rw) != sum(l for _, l in rt):
        raise IllegalStep("a-count mismatch")
    k = len(rw)
    if k == 1:
        if w != target:
            raise IllegalStep("single run differs")
        return w
    cur = w
    for r in range(k - 1):            # bank everything in the last run
        runs, _ = runs_of(cur)
        if runs[r][1] > 1:
            cur = p1_move(C, cur, runs[r], runs[-1], 1, runs[r][1] + runs[-1][1] - 1)
    tl = [l for _, l in rt]
    for r in range(k - 1):            # pay out the target lengths
        runs, _ = runs_of(cur)
        if tl[r] > 1:
            cur = p1_move(C, cur, runs[r], runs[-1], tl[r], runs[r][1] + runs[-1][1] - tl[r])
    if cur != target:
        raise IllegalStep("redistribute failed")
    return cur


def selftest_engine():
    print("[A] Rect engine self-test")
    N = 12
    C = Cert({'a' * N, 'aaxaaaaa', 'axaaaaaa', 'aaaaaxaa'}, N)
    bad = 0
    tests = [
        (('ax',), ('x',), ('a', 'aaaaa'), ('a', 'aaaaa')),          # type mismatch
        (('a', ''), ('a', 'a'), ('', 'a', ''), ('', 'a', '')),      # empty comp
        (('a', 'a'), ('a', 'a'), ('a', '', 'a'), ('a', '', 'a')),   # empty middle
        (('ax',), ('xa',), ('a', 'aaaa'), ('zz', 'q')),             # premise unknown
    ]
    for t in tests:
        try:
            C.step(*t)
        except IllegalStep:
            bad += 1
    check(bad == len(tests), "engine rejects all illegal steps")
    out = C.step(('ax',), ('xa',), ('a', 'aaaaa'), ('aaaa', 'aa'))
    check(out == 'aaaaxaaa' and out in C.known, "legal step adds E1[y]")
    print("  illegal steps rejected: %d/%d; legal step ok" % (bad, len(tests)))


# ---------------------------------------------------------------------------
# Block commutation (Lemma RC / PNF) and normal forms
# ---------------------------------------------------------------------------
class Blocks:
    """Witnessed commutations a.beta == beta.a for blocks beta in B."""

    def __init__(self, C):
        self.C = C
        self.wit = {}

    def add_from(self, w):
        """Every maximal non-a block of the known word w that is flanked by a's."""
        runs, blocks = runs_of(w)
        # positions of blocks
        i, n = 0, len(w)
        while i < n:
            if w[i] == 'a':
                i += 1
                continue
            j = i
            while j < n and w[j] != 'a':
                j += 1
            beta = w[i:j]
            if i > 0 and j < n and beta not in self.wit:
                self._witness(w, i, j)
            i = j

    def _witness(self, w, i, j):
        C = self.C
        beta = w[i:j]
        runs, _ = runs_of(w)
        left = [r for r in runs if r[0] + r[1] == i][0]
        right = [r for r in runs if r[0] == j][0]
        cur = w
        if left[1] < 2:   # borrow one a from another run of length >= 2 (P1')
            donor = [r for r in runs if r[1] >= 2 and r != left]
            if not donor:
                return
            dn = donor[0]
            if dn[0] < left[0]:
                cur = p1_move(C, cur, dn, left, dn[1] - 1, left[1] + 1)
            else:
                cur = p1_move(C, cur, left, dn, left[1] + 1, dn[1] - 1)
        runs, _ = runs_of(cur)
        pos = self._locate(cur, w, i)        # same block, same skeleton index
        i2, j2 = pos, pos + len(beta)
        L_run = [r for r in runs if r[0] + r[1] == i2][0]
        R_run = [r for r in runs if r[0] == j2][0]
        cur2 = p1_move(C, cur, L_run, R_run, L_run[1] - 1, R_run[1] + 1)
        P, Q = cur[:i2 - 1], cur[j2:]
        E0 = (P, Q)
        # E0[a beta] = cur, E0[beta a] = cur2
        assert P + 'a' + beta + Q == cur and P + beta + 'a' + Q == cur2
        self.wit[beta] = E0

    @staticmethod
    def _locate(cur, w, i):
        """Start of the block of w at index i, inside cur (same skeleton)."""
        bi = len(runs_of(w[:i])[1])          # number of blocks before i in w
        cnt, p, n = 0, 0, len(cur)
        while p < n:
            if cur[p] == 'a':
                p += 1
                continue
            if cnt == bi:
                return p
            while p < n and cur[p] != 'a':
                p += 1
            cnt += 1
        raise IllegalStep("block not found")

    def parse(self, block):
        """Split a merged block into witnessed blocks (DP); None if impossible."""
        n = len(block)
        best = [None] * (n + 1)
        best[0] = []
        for i in range(n):
            if best[i] is None:
                continue
            for beta in sorted(self.wit):
                if block.startswith(beta, i) and best[i + len(beta)] is None:
                    best[i + len(beta)] = best[i] + [beta]
        return best[n]

    def commute(self, u, i, beta, rev=False):
        """u[i]=='a' followed by beta; one Rect step a.beta -> beta.a
        (rev=True: beta.a at i -> a.beta)."""
        E0 = self.wit[beta]
        if not rev:
            assert u[i] == 'a' and u.startswith(beta, i + 1)
            E1 = (u[:i], u[i + 1 + len(beta):])
            return self.C.step(('a' + beta,), (beta + 'a',), E0, E1)
        assert u.startswith(beta, i) and u[i + len(beta)] == 'a'
        E1 = (u[:i], u[i + len(beta) + 1:])
        return self.C.step((beta + 'a',), ('a' + beta,), E0, E1)


def nf_path(B, u):
    """Forward normalization of the factor from the first to the last non-a
    letter: every inner a is moved right past the blocks.  Returns the list of
    moves (i, beta) and the normal word.  Does not touch the Cert."""
    lo = next(i for i, ch in enumerate(u) if ch != 'a')
    hi = max(i for i, ch in enumerate(u) if ch != 'a') + 1
    moves, cur = [], u
    while True:
        i = None
        for p in range(lo, hi - 1):
            if cur[p] == 'a' and cur[p + 1] != 'a':
                i = p
                break
        if i is None:
            break
        j = i + 1
        while j < len(cur) and cur[j] != 'a':
            j += 1
        parts = B.parse(cur[i + 1:j])
        if parts is None:
            return None, None
        if len(parts) > 1:
            MERGED[0] += 1
        p = i
        for beta in parts:
            moves.append((p, beta))
            cur = cur[:p] + beta + 'a' + cur[p + 1 + len(beta):]
            p += len(beta)
    return moves, cur


def derive_by_normal_form(C, B, src, tgt):
    """src known.  Derive tgt using only block commutations and P1'.
    Returns True on success (tgt known), False if the normal forms differ."""
    m1, n1 = nf_path(B, src)
    m2, n2 = nf_path(B, tgt)
    if m1 is None or m2 is None:
        return False
    cur = src
    for (i, beta) in m1:
        cur = B.commute(cur, i, beta)
    assert cur == n1
    # normal forms a^alpha PI a^rest: same PI and same a-count?
    if runs_of(n1)[1] != runs_of(n2)[1] or n1.count('a') != n2.count('a'):
        return False
    cur = redistribute(C, n1, n2)
    for (i, beta) in reversed(m2):
        cur = B.commute(cur, i, beta, rev=True)
    return cur == tgt and tgt in C.known


# ---------------------------------------------------------------------------
# Synthetic configurations of two incomparable heavy nodes v, w in W=a^N
# ---------------------------------------------------------------------------
def rand_comp(rng, letters, maxlen=4):
    while True:
        n = rng.randint(1, maxlen)
        w = ''.join(rng.choice('a' + letters) for _ in range(n))
        if any(ch != 'a' for ch in w):
            return w


def ylen(comp, lam):
    """a-yield length of a component so that the Parikh-linear model holds."""
    return comp.count('a') + lam * (len(comp) - comp.count('a'))


def layout(N, pieces):
    """pieces: list of ('a', k) or (node, j, comp, length).  Returns words."""
    pos, out = 0, []
    for p in pieces:
        if p[0] == 'a':
            pos += p[1]
        else:
            out.append((p[0], p[1], pos, p[3], p[2]))
            pos += p[3]
    assert pos == N, (pos, N)
    return out


def native(N, intervals, escaped):
    w = ['a'] * N
    repl = sorted([iv for iv in intervals if iv[0] in escaped], key=lambda t: -t[2])
    s = ''.join(w)
    for (node, j, st, ln, comp) in repl:
        s = s[:st] + comp + s[st + ln:]
    return s


def make_config(rng, kind, letters, lam, fan_w, fan_v=2):
    v = (rand_comp(rng, letters), rand_comp(rng, letters)) if fan_v == 2 else (rand_comp(rng, letters),)
    w = (rand_comp(rng, letters),) if fan_w == 1 else (rand_comp(rng, letters), rand_comp(rng, letters))
    lv = [ylen(c, lam) for c in v]
    lw = [ylen(c, lam) for c in w]
    R = lambda lo, hi: rng.randint(lo, hi)
    pad1, pad2 = R(3, 6), R(20, 30)
    P = []
    if kind == 'D' and fan_v == 1:
        P = [('a', pad1), ('v', 0, v[0], lv[0]), ('a', R(0, 3))]
        P += [('w', 0, w[0], lw[0])]
        if fan_w == 2:
            P += [('a', R(1, 3)), ('w', 1, w[1], lw[1])]
        P += [('a', pad2)]
    elif kind == 'D':
        P = [('a', pad1), ('v', 0, v[0], lv[0]), ('a', R(1, 3)), ('v', 1, v[1], lv[1]), ('a', R(0, 3))]
        P += [('w', 0, w[0], lw[0])]
        if fan_w == 2:
            P += [('a', R(1, 3)), ('w', 1, w[1], lw[1])]
        P += [('a', pad2)]
    elif kind == 'N':
        g1, g2 = R(0, 3), R(0, 3)
        if g1 + g2 == 0:
            g1 = 1
        P = [('a', pad1), ('v', 0, v[0], lv[0]), ('a', g1), ('w', 0, w[0], lw[0])]
        if fan_w == 2:
            P += [('a', R(1, 3)), ('w', 1, w[1], lw[1])]
        P += [('a', g2), ('v', 1, v[1], lv[1]), ('a', pad2)]
    elif kind == 'F':      # exact fill: no a between v's components and w's hull
        P = [('a', pad1), ('v', 0, v[0], lv[0]), ('w', 0, w[0], lw[0])]
        if fan_w == 2:
            P += [('a', R(1, 3)), ('w', 1, w[1], lw[1])]
        P += [('v', 1, v[1], lv[1]), ('a', pad2)]
    elif kind == 'C':      # crossing: I1v < I1w < I2v < I2w
        assert fan_w == 2
        P = [('a', pad1), ('v', 0, v[0], lv[0]), ('a', R(0, 3)), ('w', 0, w[0], lw[0]),
             ('a', R(0, 3)), ('v', 1, v[1], lv[1]), ('a', R(0, 3)), ('w', 1, w[1], lw[1]), ('a', pad2)]
    N = sum(p[1] if p[0] == 'a' else p[3] for p in P)
    ivs = layout(N, P)
    return v, w, lv, lw, N, ivs


def iso_placement(N, comps, ylens):
    """a e a^{N-p-1} with e = w1 a w2 (or w1); weight p = l + d - 1."""
    d = len(comps)
    e = comps[0] if d == 1 else comps[0] + 'a' + comps[1]
    p = sum(ylens) + d - 1
    return e, p, 'a' + e + 'a' * (N - p - 1)


def sd_instance(C, B, v, lv, w, lw, i, g, Nvw):
    """Both words of the (Xi2*) Rect for pi0 = v[i]: return (E0, x, y) or None."""
    N = C.N
    ev, pv, _ = iso_placement(N, v, lv)
    ew, pw, _ = iso_placement(N, w, lw)
    ellv = sum(lv)
    rho = N - ellv - pw - g - 3
    if rho < 1:
        return None
    if len(v) == 1:
        rho1 = N - ellv - pw - g - 2
        if rho1 < 1:
            return None
        E0 = ('a', 'a' * rho1)
        x = (v[0] + 'a' * g + ew + 'a',)
        y = (v[0] + 'a' * (g + pw + 1),)
    elif i == 0:
        E0 = ('a', 'a' * rho + v[1] + 'a')
        x = (v[0] + 'a' * g + ew + 'a',)
        y = (v[0] + 'a' * (g + pw + 1),)
    else:
        E0 = ('a' + v[0] + 'a' * rho, 'a')
        x = (v[1] + 'a' * g + ew + 'a',)
        y = (v[1] + 'a' * (g + pw + 1),)
    Ey = C.fill(E0, y)       # v's isolated placement, runs (1, g+pw+1+rho, 1)
    Ex = C.fill(E0, x)       # to be derived from the native word with v, w
    return E0, x, y, Ex, Ey


# ---------------------------------------------------------------------------
# [B] Lemma SD on random single-letter configurations
# ---------------------------------------------------------------------------
def model_ok(w, N, lam, letters):
    return all(ch in 'a' + letters for ch in w) and \
        w.count('a') + lam * (len(w) - w.count('a')) == N


def run_sd_config(rng, kind, fan_w, letters, lam, stats, fan_v=2):
    v, w, lv, lw, N, ivs = make_config(rng, kind, letters, lam, fan_w, fan_v)
    W = 'a' * N
    Nv = native(N, ivs, {'v'})
    Nw = native(N, ivs, {'w'})
    Nvw = native(N, ivs, {'v', 'w'})
    C = Cert({W, Nv, Nw, Nvw}, N)
    # isolated placements (P1' from the native words)
    ev, pv, Iv = iso_placement(N, v, lv)
    ew, pw, Iw = iso_placement(N, w, lw)
    redistribute(C, Nv, Iv)
    redistribute(C, Nw, Iw)
    B = Blocks(C)
    B.add_from(Iv)
    B.add_from(Iw)
    ok_all = True
    ellv = sum(lv)
    Gstar = N - ellv - pw - 4
    gs = sorted(set([1, max(1, Gstar // 2), Gstar]))
    for i in range(len(v)):
        if not any(ch != 'a' for ch in v[i]):
            continue
        if not (content(ew) <= content(v[i]) | {'a'}):
            stats['content_fail'] += 1
            continue
        for g in gs:
            inst = sd_instance(C, B, v, lv, w, lw, i, g, Nvw)
            if inst is None:
                continue
            E0, x, y, Ex, Ey = inst
            # E0[y] from v's isolated placement
            redistribute(C, Iv, Ey)
            okx = derive_by_normal_form(C, B, Nvw, Ex)
            stats['instances'] += 1
            if okx:
                stats['derived'] += 1
                # the congruence x == y is witnessed: both E0[x], E0[y] known
                check(Ex in C.known and Ey in C.known, "SD witness known")
            else:
                stats['nf_mismatch'] += 1
                ok_all = False
    for z in C.known:
        if not model_ok(z, N, lam, letters):
            check(False, "derived word outside the model: %r" % z)
            ok_all = False
    stats['steps'] += C.steps
    stats['words'] += len(C.known)
    return ok_all, (v, w, N)


def part_B():
    print("[B] Lemma SD (single-letter class K={a,x}) on random configurations")
    rng = random.Random(20261122)
    lam = 3
    total_ok = True
    for kind, fan_v, fan_w, reps in [('D', 1, 1, 30), ('D', 1, 2, 30), ('D', 2, 1, 40), ('D', 2, 2, 40),
                                     ('N', 2, 1, 40), ('N', 2, 2, 40),
                                     ('F', 2, 1, 40), ('F', 2, 2, 40), ('C', 2, 2, 80)]:
        stats = dict(instances=0, derived=0, nf_mismatch=0, content_fail=0, steps=0, words=0)
        ok = True
        m0 = MERGED[0]
        for _ in range(reps):
            o, _ = run_sd_config(rng, kind, fan_w, 'x', lam, stats, fan_v)
            ok = ok and o
        total_ok = total_ok and ok and stats['nf_mismatch'] == 0
        print("  config %s, fan-out(v)=%d, fan-out(w)=%d: %3d configs, %4d Rect instances, %4d derived, "
              "%d mismatches, %d content skips, %6d Rect steps, %d merged runs split" %
              (kind, fan_v, fan_w, reps, stats['instances'], stats['derived'], stats['nf_mismatch'],
               stats['content_fail'], stats['steps'], MERGED[0] - m0))
        check(stats['nf_mismatch'] == 0 and stats['content_fail'] == 0 and stats['derived'] == stats['instances'],
              "SD derivable in every %s instance" % kind)
    # one fully printed crossing certificate (small)
    rng2 = random.Random(7)
    v, w, lv, lw, N, ivs = make_config(rng2, 'C', 'x', 2, 2)
    print("  example crossing: N=%d, v=(%s,%s), w=(%s,%s)" % (N, v[0], v[1], w[0], w[1]))
    Nvw = native(N, ivs, {'v', 'w'})
    print("    native {v,w}: %s" % Nvw)
    ew, pw, _ = iso_placement(N, w, lw)
    g = 1
    rho = N - sum(lv) - pw - g - 3
    print("    Rect (Xi2*), g=1: x=(%s), y=(%s), types {a,x}/{a,x}" %
          (v[0] + 'a' * g + ew + 'a', v[0] + 'a' * (g + pw + 1)))
    print("      E0=(a, a^%d %s a);  E0[x]=%s" % (rho, v[1], 'a' + v[0] + 'a' * g + ew + 'a' * (1 + rho) + v[1] + 'a'))
    print("      E0[y]=%s" % ('a' + v[0] + 'a' * (g + pw + 1 + rho) + v[1] + 'a'))
    return total_ok


# ---------------------------------------------------------------------------
# [C] Classes with two or more non-a letters: the projection criterion
# ---------------------------------------------------------------------------
def proj(w):
    return ''.join(ch for ch in w if ch != 'a')


def part_C():
    print("[C] Projection criterion (PNF) for classes with >=2 non-a letters")
    rng = random.Random(4242)
    lam = 3
    res = {}
    for kind, fan_w, reps in [('N', 1, 40), ('F', 1, 40), ('F', 2, 30), ('C', 2, 200)]:
        pred_yes = pred_no = got_yes = got_no = agree = 0
        gap_unequal = 0
        for _ in range(reps):
            v, w, lv, lw, N, ivs = make_config(rng, kind, 'bc', lam, fan_w)
            W = 'a' * N
            Nv, Nw, Nvw = native(N, ivs, {'v'}), native(N, ivs, {'w'}), native(N, ivs, {'v', 'w'})
            C = Cert({W, Nv, Nw, Nvw}, N)
            ev, pv, Iv = iso_placement(N, v, lv)
            ew, pw, Iw = iso_placement(N, w, lw)
            redistribute(C, Nv, Iv)
            redistribute(C, Nw, Iw)
            B = Blocks(C)
            B.add_from(Iv)
            B.add_from(Iw)
            for i in (0, 1):
                if not (content(ew) <= content(v[i]) | {'a'}):
                    continue
                # predicted: projection of target equals projection of the native word
                tgt_proj = proj(v[0]) + proj(ew) + proj(v[1]) if i == 0 else proj(v[0]) + proj(v[1]) + proj(ew)
                pred = (tgt_proj == proj(Nvw))
                inst = sd_instance(C, B, v, lv, w, lw, i, 1, Nvw)
                if inst is None:
                    continue
                E0, x, y, Ex, Ey = inst
                redistribute(C, Iv, Ey)
                got = derive_by_normal_form(C, B, Nvw, Ex)
                pred_yes += pred
                pred_no += (not pred)
                if i == 0 and not pred:
                    gap_unequal += 1
                got_yes += got
                got_no += (not got)
                agree += (pred == got)
            for z in C.known:
                if not model_ok(z, N, lam, 'bc'):
                    check(False, "PNF derived word outside the model")
        res[kind] = (pred_yes, pred_no, got_yes, got_no, agree)
        print("  config %s, fan-out(w)=%d: projection equal %d / unequal %d; derived %d / not %d; "
              "agreement %d/%d; gap placement (i=1) unequal %d" %
              (kind, fan_w, pred_yes, pred_no, got_yes, got_no, agree, pred_yes + pred_no, gap_unequal))
        check(agree == pred_yes + pred_no, "PNF derivation iff projection condition (%s)" % kind)
        if kind in ('N', 'F'):
            check(gap_unequal == 0, "nested/exact fill: gap placement projection always equal (%s)" % kind)
    check(res['C'][1] > 0, "crossings with unequal projections occur in the sample")
    # R15's L_{11,4}: the crossing B0-pair is blocked by content, not by projection
    N, d = 11, 4
    cross = 'a' + 'b' + 'a' + 'b' + 'a' + 'c' + 'a' + 'c' + 'a'
    print("  L_{11,4} (R15): crossing native word %s, components v=(b,c), w=(b,c)" % cross)
    xt = 'b' + 'a' + 'bac' + 'a'
    yt = 'b' + 'a' * 6
    print("    D2-gap comparison x=(%s) content %s vs y=(%s) content %s -> not a legal Rect"
          % (xt, cstr(content(xt)), yt, cstr(content(yt))))
    check(content(xt) != content(yt), "R15 blocked by content")
    return True


# ---------------------------------------------------------------------------
# [D] HXi* family forcing with a crossing single-letter dissolving pair
# ---------------------------------------------------------------------------
class NF:
    """Forward NF* rewriting of a family word to the prototype form.  Each move
    is a one-hole congruence with a witness E0 whose two words are known."""

    def __init__(self, C, B, v, lv, w, lw, Nvw, fam):
        self.C, self.B = C, B
        self.v, self.lv, self.w, self.lw, self.Nvw = v, lv, w, lw, Nvw
        self.fam = fam               # list of (e, p, isolated word)
        self.ew, self.pw, self.Iw = iso_placement(C.N, w, lw)
        self.ev, self.pv, self.Iv = iso_placement(C.N, v, lv)
        self.cache = {}

    def dis_witness(self, g):
        if g in self.cache:
            return self.cache[g]
        inst = sd_instance(self.C, self.B, self.v, self.lv, self.w, self.lw, 0, g, self.Nvw)
        if inst is None:
            raise IllegalStep("DIS out of range g=%d" % g)
        E0, x, y, Ex, Ey = inst
        redistribute(self.C, self.Iv, Ey)
        if not derive_by_normal_form(self.C, self.B, self.Nvw, Ex):
            raise IllegalStep("SD failed")
        self.cache[g] = (E0, x, y)
        return self.cache[g]

    def ex_witness(self, e, p):
        """e a^{pw} == a^{p} e_w from isolated placements (R9 P4)."""
        N = self.C.N
        E0 = ('a', 'a' * (N - p - self.pw - 1))
        x = (e + 'a' * self.pw,)
        y = ('a' * p + self.ew,)
        iso_e = 'a' + e + 'a' * (N - p - 1)
        tgt = 'a' + 'a' * p + self.ew + 'a' * (N - p - self.pw - 1)
        redistribute(self.C, self.Iw, tgt)
        assert self.C.fill(E0, x) == iso_e and self.C.fill(E0, y) == tgt
        return E0, x, y

    def com_witness(self, e, p):
        """a e == e a (R9 P3)."""
        N = self.C.N
        E0 = ('a', 'a' * (N - p - 2))
        iso1 = 'a' + e + 'a' * (N - p - 1)
        iso2 = 'aa' + e + 'a' * (N - p - 2)
        redistribute(self.C, iso1, iso2)
        return E0, ('a' + e,), (e + 'a',)

    def forward(self, word, start, slots):
        """word = PhiL + v0 + a^g + e_w + a^g + e_1 a^g ... e_M + a^gl + PhiR;
        start = index of v0.  Returns list of moves (E0, x, y, E1) and final."""
        moves = []
        cur = word
        v0 = self.v[0]
        p0 = start + len(v0)       # position after pi0

        def apply(E0, x, y, i):
            nonlocal cur
            assert cur.startswith(x[0], i)
            E1 = (cur[:i], cur[i + len(x[0]):])
            moves.append((E0, x, y, E1))
            cur = E1[0] + y[0] + E1[1]

        # DIS of e_w directly after the first run
        H = 0
        while cur[p0 + H] == 'a':
            H += 1
        assert cur.startswith(self.ew, p0 + H)
        E0, x, y = self.dis_witness(H)
        apply(E0, x, y, start)
        for (e, p) in slots:
            H = 0
            while cur[p0 + H] == 'a':
                H += 1
            assert cur.startswith(e, p0 + H), (cur, e)
            q = p0 + H + len(e)
            h = 0
            while cur[q + h] == 'a':
                h += 1
            need = max(0, self.pw + 1 - h)
            for _ in range(need):       # COM: move a from left to right of e
                E0c, xc, yc = self.com_witness(e, p)
                i = p0 + H - 1
                apply(E0c, xc, yc, i)
                H -= 1
            E0e, xe, ye = self.ex_witness(e, p)
            apply(E0e, xe, ye, p0 + H)
            H2 = H + p
            E0, x, y = self.dis_witness(H2)
            apply(E0, x, y, start)
        return moves, cur

    def backward(self, moves, final):
        cur = final
        assert cur in self.C.known
        for (E0, x, y, E1) in reversed(moves):
            assert E1[0] + y[0] + E1[1] == cur
            cur = self.C.step(y, x, E0, E1)
        return cur

    def replay_forward(self, moves, word):
        cur = word
        for (E0, x, y, E1) in moves:
            assert E1[0] + x[0] + E1[1] == cur
            cur = self.C.step(x, y, E0, E1)
        return cur


def part_D():
    print("[D] HXi* family forcing with a crossing single-letter dissolving pair")
    lam = 2
    v = ('xax', 'xx')       # crossing pair, single-letter class {a,x}
    w = ('xx', 'x')
    lv = [ylen(c, lam) for c in v]
    lw = [ylen(c, lam) for c in w]
    # family escapes with superincreasing weights p = |e|_a + lam*|e|_x
    fam_comps = [('x',), ('xx',), ('xxxx',)]
    M = len(fam_comps)
    g = 2
    Npad = 70
    # crossing layout
    P = [('a', 4), ('v', 0, v[0], lv[0]), ('a', 1), ('w', 0, w[0], lw[0]), ('a', 2),
         ('v', 1, v[1], lv[1]), ('a', 0), ('w', 1, w[1], lw[1]), ('a', Npad)]
    N = sum(p[1] if p[0] == 'a' else p[3] for p in P)
    ivs = layout(N, P)
    W = 'a' * N
    Nv, Nw, Nvw = native(N, ivs, {'v'}), native(N, ivs, {'w'}), native(N, ivs, {'v', 'w'})
    fam = []
    axioms = {W, Nv, Nw, Nvw}
    for comps in fam_comps:
        ly = [ylen(c, lam) for c in comps]
        e, p, I = iso_placement(N, comps, ly)
        fam.append((e, p, I))
        axioms.add('a' * 5 + e + 'a' * (N - p - 5))   # a native-like isolated placement
    C = Cert(axioms, N)
    for (e, p, I) in fam:
        redistribute(C, 'a' * 5 + e + 'a' * (N - p - 5), I)
    ev, pv, Iv = iso_placement(N, v, lv)
    ew, pw, Iw = iso_placement(N, w, lw)
    redistribute(C, Nv, Iv)
    redistribute(C, Nw, Iw)
    B = Blocks(C)
    for z in [Iv, Iw] + [I for (_, _, I) in fam]:
        B.add_from(z)
    nf = NF(C, B, v, lv, w, lw, Nvw, fam)
    weights = [p for (_, p, _) in fam]
    print("  N=%d; v=(%s,%s) w=(%s,%s) cross (native %s...)" % (N, v[0], v[1], w[0], w[1], Nvw[:30]))
    print("  family escapes %s with weights %s (distinct subset sums: %s)" %
          ([e for (e, _, _) in fam], weights,
           len(set(sum(s) for k in range(M + 1) for s in itertools.combinations(weights, k))) == 2 ** M))
    # family word for permutation pi
    total = pw + sum(weights) + (M + 1) * g
    gl = 3
    q0 = total + gl            # K-block after pi0 has weight pv' = q0 a's in prototype
    rho = N - sum(lv) - q0 - 3
    check(rho >= 1, "room for the prototype")
    proto = 'a' + v[0] + 'a' * (q0 + 1 + rho) + v[1] + 'a'
    # prototype from v's isolated placement (P1')
    redistribute(C, Iv, proto)
    forced = 0
    for perm in itertools.permutations(range(M)):
        body = 'a' * g + ew + ''.join('a' * g + fam[k][0] for k in perm) + 'a' * gl
        xw = 'a' + v[0] + body + 'a' * (1 + rho) + v[1] + 'a'
        slots = [(fam[k][0], fam[k][1]) for k in perm]
        moves, fin = nf.forward(xw, 1, slots)
        if fin != proto:
            check(False, "family word normal form != prototype for %s" % (perm,))
            continue
        got = nf.backward(moves, fin)
        if check(got == xw and xw in C.known, "family word forced for %s" % (perm,)):
            forced += 1
        check(model_ok(xw, N, lam, 'x'), "family word in model")
    print("  family words forced from the prototype: %d/%d (Rect steps so far %d)" %
          (forced, len(list(itertools.permutations(range(M)))), C.steps))
    # planted swap word: slot content replaced by an escape of another weight
    planted_e = ('xxx',)
    lp = [ylen(c, lam) for c in planted_e]
    e_p, p_p, I_p = iso_placement(N, planted_e, lp)
    C.known.add('a' * 5 + e_p + 'a' * (N - p_p - 5))          # axiom: native-like
    redistribute(C, 'a' * 5 + e_p + 'a' * (N - p_p - 5), I_p)
    B.add_from(I_p)
    perm = (0, 1, 2)
    body = 'a' * g + ew + 'a' * g + fam[0][0] + 'a' * g + e_p + 'a' * g + fam[2][0] + 'a' * gl
    xp = 'a' + v[0] + body + 'a' * (1 + rho) + v[1] + 'a'
    C.known.add(xp)                                           # hypothesis: x' in L
    slots = [(fam[0][0], fam[0][1]), (e_p, p_p), (fam[2][0], fam[2][1])]
    moves, fin = nf.forward(xp, 1, slots)
    fin2 = nf.replay_forward(moves, xp)
    assert fin2 == fin
    # fin = a v0 a^{q'} v1 a versus prototype a v0 a^{q} v1 a: P7
    q_fin = len(fin) - len(v[0]) - len(v[1]) - 2
    q_pro = q0 + 1 + rho
    k = abs(q_pro - q_fin)
    hi, lo = max(q_pro, q_fin), min(q_pro, q_fin)
    E0 = ('a' + v[0], v[1] + 'a')
    E1 = ('', 'a' * (N - hi))
    short = C.step(('a' * hi,), ('a' * lo,), E0, E1)
    print("  planted word with slot %s (weight %d instead of %d): normal form a %s a^%d %s a; "
          "prototype a^%d; P7 gives a^%d (shorter than a^%d)" %
          (e_p, p_p, fam[1][1], v[0], q_fin, v[1], q_pro, len(short), N))
    check(short == 'a' * (N - k) and k > 0, "planted wrong-weight word yields a shorter a-power")
    check(not model_ok(xp, N, lam, 'x'), "planted word is outside the model (consistent)")
    print("  total Rect steps in [D]: %d" % C.steps)
    return True


# ---------------------------------------------------------------------------
# [E] Exhaustive substitutability checks for finite languages
# ---------------------------------------------------------------------------
def exhaustive(L, name, show=True):
    """One- and two-hole content-typed tuple-substitutability of a finite L.
    Returns (ok, counts, witness)."""
    L = sorted(L)
    Lset = set(L)
    res = {}
    for d in (1, 2):
        dist = {}
        for w in L:
            n = len(w)
            if d == 1:
                for i in range(n):
                    for j in range(i + 1, n + 1):
                        t = (w[i:j],)
                        dist.setdefault(t, set()).add((w[:i], w[j:]))
            else:
                for i in range(n):
                    for j in range(i + 1, n):
                        for k in range(j + 1, n):
                            for l in range(k + 1, n + 1):
                                t = (w[i:j], w[k:l])
                                dist.setdefault(t, set()).add((w[:i], w[j:k], w[l:]))
        bytype = {}
        for t in dist:
            ty = tuple(frozenset(z) for z in t)
            bytype.setdefault(ty, []).append(t)
        pairs = 0
        for ty in sorted(bytype, key=lambda z: tuple(sorted(''.join(sorted(s)) for s in z))):
            ts = sorted(bytype[ty])
            ctx_to = {}
            for t in ts:
                for e in dist[t]:
                    ctx_to.setdefault(e, []).append(t)
            parent = {t: t for t in ts}

            def find(t):
                while parent[t] != t:
                    parent[t] = parent[parent[t]]
                    t = parent[t]
                return t
            for e in sorted(ctx_to):
                lst = ctx_to[e]
                for t in lst[1:]:
                    a, b = find(lst[0]), find(t)
                    if a != b:
                        parent[max(a, b)] = min(a, b)
                        pairs += 1
            groups = {}
            for t in ts:
                groups.setdefault(find(t), []).append(t)
            for r in sorted(groups):
                g = groups[r]
                base = dist[g[0]]
                for t in g[1:]:
                    if dist[t] != base:
                        # find shared and distinguishing contexts
                        shared = None
                        for e in sorted(ctx_to):
                            if g[0] in ctx_to[e] and t in ctx_to[e]:
                                shared = e
                                break
                        diff = sorted(base ^ dist[t])[0]
                        return False, res, (d, g[0], t, shared, diff)
        res[d] = (len(dist), pairs)
    return True, res, None


def part_E():
    print("[E] Exhaustive finite substitutability checks (content typing, arity 1 and 2)")
    # (1) Parikh-linear model languages used as soundness models in [B], [D]
    for (N, lam, letters) in [(9, 2, 'x'), (10, 3, 'x'), (9, 2, 'bc')]:
        L = set()
        alph = 'a' + letters
        for n in range(1, N + 1):
            for t in itertools.product(alph, repeat=n):
                w = ''.join(t)
                if model_ok(w, N, lam, letters):
                    L.add(w)
        ok, res, wit = exhaustive(L, "model")
        print("  model |u|_a+%d|u|_{%s}=%d: %d words, substitutable=%s (tuples d1=%d d2=%d)" %
              (lam, letters, N, len(L), ok, res.get(1, (0,))[0], res.get(2, (0,))[0]))
        check(ok, "model language substitutable")
    # (2) a run-pattern candidate for a single-letter analogue of L_{N,d}
    #     words a..a, x-runs of length 1 or 2, run lengths non-decreasing,
    #     #runs of length 1 = #runs of length 2, |w|_a + 3 #runs = N
    N = 14
    L = set()
    for n in range(1, N + 1):
        for t in itertools.product('ax', repeat=n):
            w = ''.join(t)
            if w[0] != 'a' or w[-1] != 'a':
                continue
            rl = [len(r) for r in w.split('a') if r]
            if any(r > 2 for r in rl) or rl != sorted(rl):
                continue
            if rl.count(1) != rl.count(2):
                continue
            if w.count('a') + 3 * len(rl) != N:
                continue
            L.add(w)
    ok, res, wit = exhaustive(L, "runs")
    print("  run-pattern candidate (N=%d): %d words, substitutable=%s" % (N, len(L), ok))
    if wit:
        d, t1, t2, shared, diff = wit
        print("    violation (arity %d): %r vs %r share %r, differ at %r" % (d, t1, t2, shared, diff))
    check(not ok, "run-pattern candidate is NOT substitutable (as Lemma RC predicts)")
    check(wit is not None, "violation witness reported")
    # (3) R15's L_{11,4}
    N, d = 11, 4
    L = set()
    for n in range(1, N + 1):
        for t in itertools.product('abc', repeat=n):
            w = ''.join(t)
            pw = proj(w)
            if pw != ''.join(sorted(pw)):
                continue
            if w.count('b') != w.count('c') or w.count('a') + d * w.count('b') != N:
                continue
            L.add(w)
    ok, res, wit = exhaustive(L, "L114")
    print("  L_{11,4}: %d words, substitutable=%s (tuples d1=%d d2=%d)" %
          (len(L), ok, res.get(1, (0,))[0], res.get(2, (0,))[0]))
    check(len(L) == 72 and ok, "L_{11,4} has 72 words and is substitutable")
    conc = [w for w in L if 'cab' in w or 'cb' in w]
    check(not conc, "no concatenated pair placement in L_{11,4}")
    return True


# ---------------------------------------------------------------------------
# [F] Independent check: full substitution closure of native words
# ---------------------------------------------------------------------------
def occ_all(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[i:j],), (w[:i], w[j:])
    else:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n + 1):
                        yield (w[i:j], w[k:l]), (w[:i], w[j:k], w[l:])


def sub_closure(seeds, cap=20000):
    """Least (2,c)-substitutable superset (content typing) of a finite set:
    iterate 'shared context => equal distributions' on all one- and two-hole
    occurrences until nothing new appears.  Independent of the Rect engine."""
    S = set(seeds)
    it = 0
    while True:
        it += 1
        new = set()
        for d in (1, 2):
            dist = {}
            for w in sorted(S):
                for t, e in occ_all(w, d):
                    dist.setdefault(t, set()).add(e)
            bytype = {}
            for t in dist:
                bytype.setdefault(tuple(frozenset(z) for z in t), []).append(t)
            for ty in bytype:
                ts = sorted(bytype[ty])
                ctx = {}
                for t in ts:
                    for e in dist[t]:
                        ctx.setdefault(e, []).append(t)
                par = {t: t for t in ts}

                def f(t):
                    while par[t] != t:
                        par[t] = par[par[t]]
                        t = par[t]
                    return t
                for e in ctx:
                    lst = ctx[e]
                    for t in lst[1:]:
                        a, b = f(lst[0]), f(t)
                        if a != b:
                            par[max(a, b)] = min(a, b)
                grp = {}
                for t in ts:
                    grp.setdefault(f(t), []).append(t)
                for g in grp.values():
                    if len(g) < 2:
                        continue
                    U = set().union(*[dist[t] for t in g])
                    for t in g:
                        for e in U - dist[t]:
                            new.add(Cert.fill(e, t))
        new -= S
        if not new:
            return S, it
        S |= new
        if len(S) > cap:
            return None, it


def lay_words(N, parts, comps, esc):
    s = ''
    for k, l in parts:
        if k == 'a':
            s += 'a' * l
        else:
            node, j = k[0], int(k[1])
            s += comps[node][j] if node in esc else 'a' * l
    assert len(s) == N or len(s) < N
    return s


def part_F():
    print("[F] Independent closure check: least substitutable superset of the native words")
    cases = [
        ("single-letter crossing", 15, 2, 'x',
         {'v': ('x', 'xx'), 'w': ('x', 'x')},
         [('a', 1), ('v0', 2), ('a', 1), ('w0', 2), ('a', 0), ('v1', 4), ('a', 1), ('w1', 2), ('a', 2)]),
        ("single-letter crossing", 15, 2, 'x',
         {'v': ('xa', 'x'), 'w': ('x', 'ax')},
         [('a', 1), ('v0', 3), ('a', 0), ('w0', 2), ('a', 1), ('v1', 2), ('a', 0), ('w1', 3), ('a', 3)]),
        ("single-letter exact fill", 14, 2, 'x',
         {'v': ('x', 'x'), 'w': ('xx',)},
         [('a', 2), ('v0', 2), ('w0', 4), ('v1', 2), ('a', 4)]),
    ]
    for (name, N, lam, letters, comps, parts) in cases:
        W = 'a' * N
        seeds = {W, lay_words(N, parts, comps, {'v'}), lay_words(N, parts, comps, {'w'}),
                 lay_words(N, parts, comps, {'v', 'w'})}
        S, it = sub_closure(seeds)
        check(S is not None, "closure finite")
        model = [z for z in S if model_ok(z, N, lam, letters)]
        ev = comps['v'][0] + ('a' + comps['v'][1] if len(comps['v']) == 2 else '')
        ew = comps['w'][0] + ('a' + comps['w'][1] if len(comps['w']) == 2 else '')
        pv = sum(ylen(c, lam) for c in comps['v']) + len(comps['v']) - 1
        pw = sum(ylen(c, lam) for c in comps['w']) + len(comps['w']) - 1
        tot = N - pv - pw
        pairs = [('a' * s1) + ev + ('a' * g) + ew + ('a' * (tot - s1 - g))
                 for s1 in range(1, tot) for g in range(1, tot - s1)]
        pairs += [('a' * s1) + ew + ('a' * g) + ev + ('a' * (tot - s1 - g))
                  for s1 in range(1, tot) for g in range(1, tot - s1)]
        inS = sum(1 for z in pairs if z in S)
        print("  %s (N=%d, v=%s, w=%s): 4 seeds -> closure %d words in %d rounds; "
              "all in the model: %s; pair placements in closure %d/%d" %
              (name, N, comps['v'], comps['w'], len(S), it, len(model) == len(S), inS, len(pairs)))
        check(len(model) == len(S), "closure inside the Parikh-linear model")
        check(pairs and inS == len(pairs), "every pair placement is forced (%s)" % name)
    # contrast: R15's crossing B0-pair in L_{11,4}
    N = 11
    parts = [('a', 1), ('v0', 2), ('w0', 2), ('a', 1), ('v1', 2), ('w1', 2), ('a', 1)]
    comps = {'v': ('b', 'c'), 'w': ('b', 'c')}
    seeds = {'a' * N, lay_words(N, parts, comps, {'v'}), lay_words(N, parts, comps, {'w'}),
             lay_words(N, parts, comps, {'v', 'w'})}
    S, it = sub_closure(seeds)
    conc = [z for z in S if proj(z) not in ('', 'bc', 'bbcc')]
    inL = all(proj(z) == ''.join(sorted(proj(z))) and z.count('b') == z.count('c') and
              z.count('a') + 4 * z.count('b') == N for z in S)
    print("  contrast, R15 crossing B0-pair in L_{11,4}: seeds %s -> closure %d words in %d rounds; "
          "inside L_{11,4}: %s; words with a concatenated pair (projection bcbc): %d" %
          (sorted(seeds), len(S), it, inL, len(conc)))
    check(inL and not conc, "two-letter split crossing: no concatenation is forced")
    return True


def main():
    selftest_engine()
    part_B()
    part_C()
    part_D()
    part_E()
    part_F()
    print()
    if FAIL:
        print("RESULT: %d FAILURES" % len(FAIL))
        for f in FAIL:
            print("  -", f)
    else:
        print("RESULT: all checks passed")
    sys.stderr.write("elapsed %.1f s\n" % (time.time() - T_START))
    return 1 if FAIL else 0


if __name__ == '__main__':
    sys.exit(main())
