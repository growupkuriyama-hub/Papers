#!/usr/bin/env python3
"""R13 (Claude): finite checks for the WN split-pair round.

Run:  python3 -I run_all.py      (standard library only, no network)
Exit code 0 iff every check passes.  Output is deterministic (no set/dict
iteration order reaches the output unsorted).

Sections
 [A] L_{N,d}: all one- and two-hole Rect conditions under the content typing
     (exhaustive, (d,q)=(4,1),(6,1))                                  CERTIFIED FINITE
 [B] G^nest / G^cross of R15: WN test of every rule, L(G)=L_{N,d} for small
     parameters, exact rule thickness, node-minimal tree of a^N, the nested
     split pair (bb,cc)                                               CERTIFIED FINITE
 [C] the two-hole nested dissolution DIS2-nest, the wrap dissolution WRAP and
     EX2 as congruences of L_{19,4} (exhaustive over all contexts)    CERTIFIED FINITE
 [D] pairing test (PP) for nested two-sided words in L_{N,d}          CERTIFIED FINITE
 [E] random WN derivation trees: no crossing, gap-closed subtrees,
     laminar hulls (structural facts used in T2(b))                   CERTIFIED FINITE
 [F] Theorem LIN: Lemma S by brute force, and the identity
     l_u = w.Psi(omega_u) on the minimal tree of G^nest_{64,4}        CERTIFIED FINITE
 [G] hull-anchor bookkeeping of Theorem D-hull on random WN trees    CERTIFIED FINITE
 [H] Proposition NL: L_f with non-affine f violates a two-hole Rect   CERTIFIED FINITE
"""
import itertools
import random
import sys
from math import comb, log

FAILS = []


def check(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("  FAIL:", msg)
    return cond


def content(s):
    return frozenset(s)


# ---------------------------------------------------------------------------
# L_{N,d}
# ---------------------------------------------------------------------------
def in_LNd(w, N, d):
    if not w:
        return False
    nb = w.count('b')
    nc = w.count('c')
    na = w.count('a')
    if nb + nc + na != len(w):
        return False
    if nb != nc or na + d * nb != N:
        return False
    p = w.replace('a', '')
    return p == 'b' * nb + 'c' * nc


def enum_LNd(N, d):
    out = []
    k = 0
    while d * k <= N:
        na = N - d * k
        length = na + 2 * k
        if na == 0 and k == 0:
            break
        # choose positions of the 2k non-a letters; they read b^k c^k
        for pos in itertools.combinations(range(length), 2 * k):
            w = ['a'] * length
            for i, p in enumerate(pos):
                w[p] = 'b' if i < k else 'c'
            s = ''.join(w)
            if s:
                out.append(s)
        k += 1
    out.sort()
    return out


# ---------------------------------------------------------------------------
# [A] exhaustive Rect check of a finite language under the content typing
# ---------------------------------------------------------------------------
def rect_check(words, label):
    Lset = set(words)
    # one hole
    ctx_of = {}          # tuple -> set of contexts
    tup_of = {}          # context -> list of tuples
    for w in words:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                x = w[i:j]
                E = (w[:i], w[j:])
                ctx_of.setdefault(x, set()).add(E)
                tup_of.setdefault(E, []).append(x)
    bad1 = 0
    for E in sorted(tup_of):
        groups = {}
        for x in tup_of[E]:
            groups.setdefault(content(x), []).append(x)
        for T in groups:
            xs = groups[T]
            D0 = ctx_of[xs[0]]
            for x in xs[1:]:
                if ctx_of[x] != D0:
                    bad1 += 1
    # two holes (middle nonempty, outer may be empty)
    ctx2 = {}
    tup2 = {}
    for w in words:
        n = len(w)
        for i in range(n):
            for i2 in range(i + 1, n):
                for j in range(i2 + 1, n):
                    for j2 in range(j + 1, n + 1):
                        X = (w[i:i2], w[j:j2])
                        E = (w[:i], w[i2:j], w[j2:])
                        ctx2.setdefault(X, set()).add(E)
                        tup2.setdefault(E, []).append(X)
    bad2 = 0
    for E in sorted(tup2):
        groups = {}
        for X in tup2[E]:
            groups.setdefault((content(X[0]), content(X[1])), []).append(X)
        for T in groups:
            xs = groups[T]
            D0 = ctx2[xs[0]]
            for X in xs[1:]:
                if ctx2[X] != D0:
                    bad2 += 1
    print("  %s: |L|=%d, 1-hole tuples=%d, 2-hole tuples=%d, violations 1-hole=%d 2-hole=%d"
          % (label, len(words), len(ctx_of), len(ctx2), bad1, bad2))
    check(bad1 == 0 and bad2 == 0, "Rect violated for " + label)
    _ = Lset


def section_A():
    print("[A] L_{N,d}: exhaustive one- and two-hole Rect (content typing)")
    for d, q in [(4, 1), (6, 1)]:
        N = d * 2 ** q + 3
        words = enum_LNd(N, d)
        check(all(in_LNd(w, N, d) for w in words), "enumeration (A)")
        rect_check(words, "L_{%d,%d}" % (N, d))


# ---------------------------------------------------------------------------
# grammars G^nest_{d,q}, G^cross_{d,q}
# rule = (lhs, children(list of nonterminals), outputs(list of components))
# component item: ('t', ch) or ('v', child_index, comp_index)
# ---------------------------------------------------------------------------
def fanout(X):
    return 2 if X[0] == 'B' else 1


def grammar(d, q, kind):
    N = d * 2 ** q + 3
    R = []
    T = lambda c: ('t', c)
    V = lambda i, j: ('v', i, j)
    R.append((('A', 1), [], [[T('a')]]))
    R.append((('A', d), [], [[T('b'), T('c')]]))
    for n in range(2, N + 1):
        R.append((('A', n), [('A', n - 1)], [[T('a'), V(0, 0)]]))
        R.append((('A', n), [('A', n - 1)], [[V(0, 0), T('a')]]))
    for n in range(d + 1, N + 1):
        R.append((('A', n), [('A', n - d)], [[T('b'), V(0, 0), T('c')]]))
    R.append((('B', 0), [], [[T('a')] * (d // 2), [T('a')] * (d // 2)]))
    R.append((('B', 0), [], [[T('b')], [T('c')]]))
    for i in range(1, q + 1):
        ch = [('B', i - 1), ('B', i - 1)]
        if kind == 'nest':
            out = [[V(0, 0), V(1, 0)], [V(1, 1), V(0, 1)]]
        else:
            out = [[V(0, 0), V(1, 0)], [V(0, 1), V(1, 1)]]
        R.append((('B', i), ch, out))
    R.append((('S',), [('A', N)], [[V(0, 0)]]))
    R.append((('S',), [('B', q)], [[T('a'), V(0, 0), T('a'), V(0, 1), T('a')]]))
    return N, R


def rule_is_wn(rule):
    lhs, ch, out = rule
    seq = [(it[1], it[2]) for comp in out for it in comp if it[0] == 'v']
    pos = {}
    for k, (i, j) in enumerate(seq):
        pos.setdefault(i, {})[j] = k
    kids = sorted(pos)
    for i in kids:
        for i2 in kids:
            if i == i2:
                continue
            for j, k in itertools.combinations(sorted(pos[i]), 2):
                for j2, k2 in itertools.combinations(sorted(pos[i2]), 2):
                    if pos[i][j] < pos[i2][j2] < pos[i][k] < pos[i2][k2]:
                        return False
    return True


def explicit(rule):
    return sum(1 for comp in rule[2] for it in comp if it[0] == 't')


def inside_outside(R):
    nts = sorted({r[0] for r in R}, key=repr)
    INF = float('inf')
    ins = {X: INF for X in nts}
    changed = True
    while changed:
        changed = False
        for r in R:
            v = explicit(r) + sum(ins[c] for c in r[1])
            if v < ins[r[0]]:
                ins[r[0]] = v
                changed = True
    out = {X: INF for X in nts}
    out[('S',)] = 0
    changed = True
    while changed:
        changed = False
        for r in R:
            base = out[r[0]] + explicit(r) + sum(ins[c] for c in r[1])
            for k, c in enumerate(r[1]):
                v = base - ins[c]
                if v < out[c]:
                    out[c] = v
                    changed = True
    return ins, out


def thickness(R):
    ins, out = inside_outside(R)
    return max(out[r[0]] + explicit(r) + sum(ins[c] for c in r[1]) for r in R), ins, out


def gen_language(R, N):
    """All yields (finite here).  Order: A_1..A_N, B_0..B_q, S."""
    Y = {}
    order = sorted({r[0] for r in R}, key=lambda X: (0, X[1]) if X[0] == 'A'
                   else ((1, X[1]) if X[0] == 'B' else (2, 0)))
    byl = {}
    for r in R:
        byl.setdefault(r[0], []).append(r)
    for X in order:
        acc = set()
        for lhs, ch, out in byl[X]:
            pools = [sorted(Y[c]) for c in ch]
            for combo in itertools.product(*pools):
                tup = []
                for comp in out:
                    s = ''.join(it[1] if it[0] == 't' else combo[it[1]][it[2]] for it in comp)
                    tup.append(s)
                acc.add(tuple(tup))
        Y[X] = acc
    return sorted(t[0] for t in Y[('S',)])


def min_tree_nest(d, q):
    """node-minimal derivation of a^N in G^nest via S -> a X1 a X2 a (B_q).
    returns list of nodes: (name, depth, path, intervals list[(start,end)])."""
    N = d * 2 ** q + 3
    counter = [0]
    nodes = []

    def build(i, path):
        # returns tuple of components, each a list of position tokens
        if i == 0:
            c1 = []
            for _ in range(d // 2):
                c1.append(counter[0]); counter[0] += 1
            c2 = []
            for _ in range(d // 2):
                c2.append(counter[0]); counter[0] += 1
            comps = (c1, c2)
        else:
            X = build(i - 1, path + 'X')
            Y = build(i - 1, path + 'Y')
            comps = (X[0] + Y[0], Y[1] + X[1])
        nodes.append([('B', i), path, comps])
        return comps

    s1 = counter[0]; counter[0] += 1
    top = build(q, '')
    s2 = counter[0]; counter[0] += 1
    s3 = counter[0]; counter[0] += 1
    word = [s1] + top[0] + [s2] + top[1] + [s3]
    check(len(word) == N, "min tree length")
    posof = {tok: p for p, tok in enumerate(word)}
    res = []
    for name, path, comps in nodes:
        ivs = []
        for c in comps:
            ps = sorted(posof[t] for t in c)
            check(ps == list(range(ps[0], ps[-1] + 1)), "component contiguous")
            ivs.append((ps[0], ps[-1] + 1))
        res.append((name, path, ivs))
    return N, res, 1 + len(nodes)


def section_B():
    print("[B] G^nest / G^cross (R15): WN, language, thickness, minimal tree")
    for d, q in [(4, 1), (6, 1), (4, 2)]:
        for kind in ('nest', 'cross'):
            N, R = grammar(d, q, kind)
            ill = [r for r in R if not rule_is_wn(r)]
            if kind == 'nest':
                check(not ill, "G^nest has an ill-nested rule")
            else:
                check(len(ill) == q and all(r[0][0] == 'B' and r[0][1] >= 1 for r in ill),
                      "G^cross ill-nested rules are exactly B_i, i>=1")
            Lg = gen_language(R, N)
            Lw = enum_LNd(N, d)
            check(Lg == Lw, "L(G^%s_{%d,%d}) = L_{N,d}" % (kind, d, q))
            th, ins, out = thickness(R)
            check(th == 2 ** (q + 1) + d + 1, "thickness formula")
            print("  (d,q)=(%d,%d) %-5s N=%d |L|=%d ill-nested rules=%d theta=%d (formula %d)"
                  % (d, q, kind, N, len(Lg), len(ill), th, 2 ** (q + 1) + d + 1))
    # large instance of RV1 / prompt
    for d, q in [(64, 4), (16, 3)]:
        N, R = grammar(d, q, 'nest')
        check(all(rule_is_wn(r) for r in R), "WN large")
        th, ins, out = thickness(R)
        check(th == 2 ** (q + 1) + d + 1, "thickness formula large")
        Nn, nodes, nnodes = min_tree_nest(d, q)
        check(nnodes == 2 ** (q + 1) and nnodes < N + 1, "B-route is node-minimal")
        # B_1 siblings under one B_2: X = path p+'X', Y = path p+'Y'
        byp = {path: (name, ivs) for name, path, ivs in nodes}
        pX = 'X' * (q - 1)
        nameX, ivX = byp[pX[:-1] + 'X']
        nameY, ivY = byp[pX[:-1] + 'Y']
        lX = sum(b - a for a, b in ivX)
        lY = sum(b - a for a, b in ivY)
        heavy = lX > th and lY > th
        nonb = all(iv[0][0] >= 1 and iv[-1][1] <= N - 1 for iv in (ivX, ivY))
        gapX = (ivX[0][1], ivX[1][0])
        hullY = (ivY[0][0], ivY[1][1])
        exact_fill = gapX == hullY
        # short yields: shortest tuple of B_1 is (bb, cc)
        check(ins[('B', 1)] == 4, "inside(B_1)=4")
        print("  (d,q)=(%d,%d) nest: N=%d theta=%d nodes(min tree)=%d; B_1 pair X%s Y%s lengths %d,%d "
              "heavy=%s nonboundary=%s Y fills gap of X exactly=%s"
              % (d, q, N, th, nnodes, ivX, ivY, lX, lY, heavy, nonb, exact_fill))
        check(nonb and exact_fill and (heavy == (lX > th)), "nested split pair data")
        if (d, q) == (64, 4):
            check(heavy and lX == 128 and th == 97 and N == 1027, "RV1 instance (64,4)")
        # all incomparable pairs of B-nodes are gap-nested (laminar hulls)
        bad = 0
        for (n1, p1, i1), (n2, p2, i2) in itertools.combinations(nodes, 2):
            if p1.startswith(p2) or p2.startswith(p1):
                continue
            h1 = (i1[0][0], i1[-1][1]); h2 = (i2[0][0], i2[-1][1])
            g1 = (i1[0][1], i1[1][0]); g2 = (i2[0][1], i2[1][0])
            inside12 = g1[0] <= h2[0] and h2[1] <= g1[1]
            inside21 = g2[0] <= h1[0] and h1[1] <= g2[1]
            if not (inside12 or inside21):
                bad += 1
        check(bad == 0, "all incomparable B-node pairs gap-nested")
        print("  (d,q)=(%d,%d) nest: incomparable B-node pairs that are not gap-nested: %d" % (d, q, bad))


# ---------------------------------------------------------------------------
# [C] congruences in L_{19,4}
# ---------------------------------------------------------------------------
def contexts1(words, x):
    D = set()
    for w in words:
        start = w.find(x)
        while start != -1:
            D.add((w[:start], w[start + len(x):]))
            start = w.find(x, start + 1)
    return D


def contexts2(words, X):
    x1, x2 = X
    D = set()
    for w in words:
        i = w.find(x1)
        while i != -1:
            i2 = i + len(x1)
            j = w.find(x2, i2 + 1)
            while j != -1:
                D.add((w[:i], w[i2:j], w[j + len(x2):]))
                j = w.find(x2, j + 1)
            i = w.find(x1, i + 1)
    return D


def section_C():
    print("[C] DIS2-nest, WRAP, EX2 as congruences of L_{19,4} (all contexts)")
    d, q = 4, 2
    N = d * 2 ** q + 3
    words = enum_LNd(N, d)
    nrel = 0
    # DIS2-nest: (w1 a^g u1 a, a u2 a^g' w2) == (w1 a^y1, a^y2 w2), y1+y2 = g+g'+2+l_u
    # level B_0: omega=(b,c), l = d
    for g, g2 in [(1, 1), (1, 2), (2, 1), (2, 2), (1, 3)]:
        X = ('b' + 'a' * g + 'b' + 'a', 'a' + 'c' + 'a' * g2 + 'c')
        DX = contexts2(words, X)
        tot = g + g2 + 2 + d
        for y1 in range(1, tot):
            Y = ('b' + 'a' * y1, 'a' * (tot - y1) + 'c')
            DY = contexts2(words, Y)
            ok = DX == DY and len(DX) > 0
            check(ok, "DIS2-nest g=%d g'=%d y1=%d" % (g, g2, y1))
            check(content(X[0]) == content(Y[0]) and content(X[1]) == content(Y[1]), "DIS2 types")
            nrel += 1
    print("  DIS2-nest: %d instances, all with equal nonempty two-hole distributions" % nrel)
    # one-hole DIS with the split anchor is not even type-correct
    x = 'b' + 'a' + 'bac' + 'a'
    y = 'b' + 'a' * (1 + d + 1 + 1)
    check(content(x) != content(y), "one-hole DIS type mismatch for split anchor")
    print("  one-hole DIS with anchor omega^1_v: types %s vs %s (differ, as expected)"
          % (''.join(sorted(content(x))), ''.join(sorted(content(y)))))
    # WRAP: b a^g1 (b a c) a^g2 c == a^h1 (b a c) a^h2, h1+h2 = g1+g2+d
    nw = 0
    for g1, g2 in [(1, 1), (1, 2), (2, 1), (0, 1), (1, 0), (0, 0)]:
        x = 'b' + 'a' * g1 + 'bac' + 'a' * g2 + 'c'
        Dx = contexts1(words, x)
        tot = g1 + g2 + d
        for h1 in range(0, tot + 1):
            y = 'a' * h1 + 'bac' + 'a' * (tot - h1)
            Dy = contexts1(words, y)
            check(Dx == Dy and len(Dx) > 0 and content(x) == content(y), "WRAP %d %d %d" % (g1, g2, h1))
            nw += 1
    print("  WRAP: %d instances (including g1=0 or g2=0, the exact-fill shape), all congruent" % nw)
    # EX2: (bb a, cc) == (b a^(d+1), c)   [profile ({a,b},{c})], and with a's moved
    ne = 0
    for X, Y in [(('bba', 'cc'), ('b' + 'a' * (d + 1), 'c')),
                 (('abb', 'cc'), ('a' * (d + 1) + 'b', 'c')),
                 (('bba', 'acc'), ('b' + 'a' * (d + 1), 'ac'))]:
        DX = contexts2(words, X)
        DY = contexts2(words, Y)
        check(DX == DY and len(DX) > 0, "EX2 %s %s" % (X, Y))
        ne += 1
    print("  EX2: %d instances congruent" % ne)
    # concatenated (disjoint) kernels never occur
    cnt = sum(1 for w in words if 'c' in w and 'b' in w.split('c', 1)[1])
    check(cnt == 0, "no b after c")
    print("  words of L_{19,4} with a b after a c (concatenated kernels): %d" % cnt)


# ---------------------------------------------------------------------------
# [D] pairing test (PP) in L_{N,d}
# ---------------------------------------------------------------------------
def xi(sig, tau, kval, frame_a, d, N):
    """nested two-sided word: left components omega^1 = b^k, right = c^k.
    left list sig (outer to inner), right list tau (outer to inner).
    a-runs: Z between slots, outer runs adjusted so that the matched reference
    with total sum K0 is in L."""
    Z = 'a' * 3
    left = Z.join('b' * kval[s] for s in sig)
    right = Z.join('c' * kval[t] for t in reversed(tau))
    core = left + 'a' * 5 + right
    na_core = core.count('a')
    rest = frame_a - na_core
    if rest < 2:
        return None
    return 'a' * (rest // 2) + core + 'a' * (rest - rest // 2)


def section_D():
    print("[D] pairing (PP) for nested two-sided words in L_{N,d}")
    for label, d, q, levels in [("ratio 4", 16, 8, [1, 3, 5, 7]),
                                ("ratio 2", 16, 8, [1, 2, 3, 4])]:
        N = d * 2 ** q + 3
        kval = {i: 2 ** i for i in levels}
        M = len(levels)
        K0 = sum(kval.values())
        frame_a = N - d * K0   # a-count of the matched reference
        stats = {"matched": [0, 0], "perm-pairing": [0, 0], "other": [0, 0],
                 "same-sum-diff-multiset": [0, 0]}
        seqs = list(itertools.product(levels, repeat=M))
        for sig in seqs:
            if max(sig.count(x) for x in levels) > 2:
                continue
            for tau in seqs:
                if max(tau.count(x) for x in levels) > 2:
                    continue
                w = xi(sig, tau, kval, frame_a, d, N)
                if w is None:
                    continue
                acc = in_LNd(w, N, d)
                ssig = sum(kval[s] for s in sig)
                stau = sum(kval[t] for t in tau)
                pred = (ssig == stau == K0)
                check(acc == pred, "membership = (sums equal to K0)")
                if sig == tau and sorted(sig) == sorted(levels):
                    key = "matched"
                elif sorted(sig) == sorted(tau) == sorted(levels):
                    key = "perm-pairing"
                elif ssig == stau and sorted(sig) != sorted(tau):
                    key = "same-sum-diff-multiset"
                else:
                    key = "other"
                stats[key][0] += 1
                stats[key][1] += acc
        print("  %s (levels %s, N=%d): " % (label, levels, N) +
              ", ".join("%s %d/%d accepted" % (k, stats[k][1], stats[k][0]) for k in sorted(stats)))
        check(stats["matched"][1] == stats["matched"][0], "matched accepted")
        check(stats["perm-pairing"][1] == stats["perm-pairing"][0], "perm pairings accepted")
        if label == "ratio 4":
            check(stats["same-sum-diff-multiset"][0] == 0, "ratio 4: multiset sums injective")
            check(stats["other"][1] == 0, "ratio 4: only permutations of the family accepted")
        else:
            check(stats["same-sum-diff-multiset"][0] > 0, "ratio 2: collisions exist")


# ---------------------------------------------------------------------------
# [E] random WN derivation trees
# ---------------------------------------------------------------------------
class Node:
    pass


def rand_wn_rule(rng, kid_fans, fan):
    """random flattened variable order that is WN, then split into `fan`
    components with terminals 'a' between all adjacent variables."""
    while True:
        items = []
        for i, f in enumerate(kid_fans):
            for j in range(f):
                items.append((i, j))
        rng.shuffle(items)
        # enforce component order inside each child (order preserving)
        pos = {}
        cnt = {}
        seq = []
        for (i, j) in items:
            jj = cnt.get(i, 0)
            cnt[i] = jj + 1
            seq.append((i, jj))
        ok = True
        for i, i2 in itertools.permutations(range(len(kid_fans)), 2):
            if kid_fans[i] == 2 and kid_fans[i2] == 2:
                p = {x: k for k, x in enumerate(seq)}
                if p[(i, 0)] < p[(i2, 0)] < p[(i, 1)] < p[(i2, 1)]:
                    ok = False
        if ok:
            break
    if fan == 1:
        comps = [seq]
    elif len(seq) < 2:
        comps = [seq, []]
    else:
        cut = rng.randint(1, len(seq) - 1)
        comps = [seq[:cut], seq[cut:]]
    out = []
    for comp in comps:
        c = []
        for k, v in enumerate(comp):
            if k > 0 or rng.random() < 0.3:
                c.append(('t',))
            c.append(('v',) + v)
        if rng.random() < 0.3 or not c:
            c.append(('t',))
        out.append(c)
    return out, fan


def rand_tree(rng, depth, fan):
    n = Node()
    n.fan = fan
    if depth == 0 or rng.random() < 0.15:
        n.kids = []
        n.out = [[('t',)] * rng.randint(1, 3) for _ in range(fan)]
        return n
    k = rng.randint(1, 3)
    n.kids = [rand_tree(rng, depth - 1, rng.choice([1, 2, 2])) for _ in range(k)]
    kf = [c.fan for c in n.kids]
    out, f2 = rand_wn_rule(rng, kf, fan)
    n.out = out
    n.fan = f2
    return n


def realize(root):
    tok = [0]
    allnodes = []

    def go(n, parent):
        n.parent = parent
        n.id = len(allnodes)
        allnodes.append(n)
        kidc = [go(c, n) for c in n.kids]
        comps = []
        for comp in n.out:
            c = []
            for it in comp:
                if it[0] == 't':
                    c.append(tok[0]); tok[0] += 1
                else:
                    c.extend(kidc[it[1]][it[2]])
            comps.append(c)
        n._comps = comps
        return comps

    top = go(root, None)
    word = top[0] if len(top) == 1 else top[0] + [-1] + top[1]
    pos = {t: p for p, t in enumerate(word)}
    for n in allnodes:
        ivs = []
        for c in n._comps:
            ps = sorted(pos[t] for t in c)
            ivs.append((ps[0], ps[-1] + 1))
        n.ivs = ivs
    return allnodes, len(word)


def section_E():
    print("[E] random WN derivation trees: crossing, gap-closed subtrees, laminar hulls")
    rng = random.Random(20261122)
    trees = 0
    pairs = 0
    stats = {"disjoint": 0, "gap-nested": 0}
    for _ in range(150):
        root = rand_tree(rng, 6, 1)
        nodes, n = realize(root)
        trees += 1
        anc = {}
        for x in nodes:
            s = set()
            p = x.parent
            while p is not None:
                s.add(p.id); p = p.parent
            anc[x.id] = s
        for x, y in itertools.combinations(nodes, 2):
            if x.id in anc[y.id] or y.id in anc[x.id]:
                continue
            pairs += 1
            hx = (x.ivs[0][0], x.ivs[-1][1]); hy = (y.ivs[0][0], y.ivs[-1][1])
            if hx[1] <= hy[0] or hy[1] <= hx[0]:
                stats["disjoint"] += 1
                # one of two disjoint hulls is at most half of the word
                check(min(hx[1] - hx[0], hy[1] - hy[0]) <= n / 2, "half")
                continue
            ok = False
            if len(x.ivs) == 2 and x.ivs[0][1] <= hy[0] and hy[1] <= x.ivs[1][0]:
                ok = True
            if len(y.ivs) == 2 and y.ivs[0][1] <= hx[0] and hx[1] <= y.ivs[1][0]:
                ok = True
            if not check(ok, "incomparable WN nodes cross"):
                return
            stats["gap-nested"] += 1
        # gap-closed: every node incomparable to v meeting gap(v) lies inside gap(v)
        for v in nodes:
            if len(v.ivs) < 2:
                continue
            g = (v.ivs[0][1], v.ivs[1][0])
            for z in nodes:
                if z.id == v.id or z.id in anc[v.id] or v.id in anc[z.id]:
                    continue
                meets = any(a < g[1] and g[0] < b for a, b in z.ivs)
                if meets:
                    inside = all(g[0] <= a and b <= g[1] for a, b in z.ivs)
                    check(inside, "gap-closed")
    print("  trees=%d incomparable pairs=%d: disjoint=%d gap-nested=%d crossing=0; "
          "gap-closed property held" % (trees, pairs, stats["disjoint"], stats["gap-nested"]))


# ---------------------------------------------------------------------------
# [F] Theorem LIN
# ---------------------------------------------------------------------------
def lemmaS_bound(k, th):
    H = th ** k
    g = 1
    while 4 ** g <= (4.0 / 3.0) * H:
        g += 1
    return k * g


def section_F():
    print("[F] Theorem LIN: Lemma S (ratio-4 chains of values w.n, |n|_1<=theta') and l_u = w.Psi(omega_u)")
    # brute force: k=1,2; integer weights in [-4,4]; theta' <= 5
    worst = 0
    for k in (1, 2):
        for th in range(1, 6):
            vecs = [v for v in itertools.product(range(th + 1), repeat=k) if 0 < sum(v) <= th]
            best = 0
            for w in itertools.product(range(-4, 5), repeat=k):
                vals = sorted({sum(a * b for a, b in zip(w, v)) for v in vecs})
                vals = [x for x in vals if x >= 1]
                # longest chain with ratio >= 4
                L = {}
                for x in vals:
                    L[x] = 1 + max([L[y] for y in vals if y * 4 <= x and y in L] or [0])
                b = max(L.values()) if L else 0
                best = max(best, b)
            bound = lemmaS_bound(k, th)
            worst = max(worst, best - bound)
            check(best <= bound, "Lemma S k=%d th=%d" % (k, th))
            print("  k=%d theta'=%d: longest ratio-4 chain %d <= bound %d" % (k, th, best, bound))
    # identity on G^nest_{64,4}: mu=(1,d,0): l_u = d*|omega_u|_b + |omega_u|_a
    d, q = 64, 4
    N, R = grammar(d, q, 'nest')
    th, ins, out = thickness(R)
    Nn, nodes, nn = min_tree_nest(d, q)
    ok = True
    for name, path, ivs in nodes:
        i = name[1]
        l = sum(b - a for a, b in ivs)
        omega_b = 2 ** i      # shortest yield (b^{2^i}, c^{2^i})
        ok &= (l == d * omega_b)
    check(ok, "l_u = w.Psi(omega_u)")
    # content-wise version: k = |Sigma|+1 = 4, theta' = theta+1, 2^|Sigma| = 8 contents
    T = 8 * lemmaS_bound(4, th + 1)
    bound = th + 8 * 2 * th * (8 * 2) ** T
    print("  G^nest_{64,4}: every B-node satisfies l_u = d*|omega_u|_b; N=%d, theta=%d, "
          "LIN bound with r=2: log2 = %.1f (polynomial in theta; crude)" % (N, th, log(bound, 2)))
    check(N <= bound, "LIN bound")


# ---------------------------------------------------------------------------
# [G] hull anchor bookkeeping (Theorem D-hull) on random WN trees
# ---------------------------------------------------------------------------
def section_G():
    print("[G] hull anchor: native words {v}+C_gap and {v,w}+C_gap on random WN trees")
    rng = random.Random(1122)
    tested = 0
    for _ in range(200):
        root = rand_tree(rng, 6, 1)
        nodes, n = realize(root)
        anc = {}
        for x in nodes:
            s = set(); p = x.parent
            while p is not None:
                s.add(p.id); p = p.parent
            anc[x.id] = s
        cand = []
        for x, y in itertools.combinations(nodes, 2):
            if x.id in anc[y.id] or y.id in anc[x.id] or x.parent is None or y.parent is None:
                continue
            hx = (x.ivs[0][0], x.ivs[-1][1]); hy = (y.ivs[0][0], y.ivs[-1][1])
            if (hx[1] <= hy[0] or hy[1] <= hx[0]) and len(x.ivs) + len(y.ivs) >= 3:
                cand.append((x, y))
        cand.sort(key=lambda t: (t[0].id, t[1].id))
        for x, y in cand[:6]:
            hx = (x.ivs[0][0], x.ivs[-1][1]); hy = (y.ivs[0][0], y.ivs[-1][1])
            v, w = (x, y) if hx[1] - hx[0] <= hy[1] - hy[0] else (y, x)
            hv = (v.ivs[0][0], v.ivs[-1][1])
            check(hv[1] - hv[0] <= n / 2, "anchor hull <= N/2")
            # C_gap: maximal nodes inside gap(v) (parent not inside gap)
            cgap = []
            if len(v.ivs) == 2:
                g = (v.ivs[0][1], v.ivs[1][0])
                def inside(z):
                    return all(g[0] <= a and b <= g[1] for a, b in z.ivs)
                for z in nodes:
                    if z.id == v.id or v.id in anc[z.id] or z.id in anc[v.id]:
                        continue
                    if inside(z) and (z.parent is None or not inside(z.parent)):
                        if rng.random() < 0.6:
                            cgap.append(z)
            esc_v = [v] + cgap
            esc_vw = [v, w] + cgap
            ids = [z.id for z in esc_vw]
            ok_anti = all(a not in anc[b] and b not in anc[a] for a, b in itertools.combinations(ids, 2))
            check(ok_anti, "{v,w}+C_gap antichain")

            def native(esc):
                lab = ['a'] * n
                for z in esc:
                    for k, (a, b) in enumerate(z.ivs):
                        for p in range(a, b):
                            lab[p] = None
                        lab[a] = 'F%d.%d' % (z.id, k)
                return lab

            def hull_word(lab):
                seg = [t for t in lab[hv[0]:hv[1]] if t is not None]
                out = []
                for t in seg:
                    if t == 'a':
                        if not out or out[-1] != 'a':
                            out.append('a')
                    else:
                        out.append(t)
                return tuple(out)

            l1 = native(esc_v); l2 = native(esc_vw)
            check(hull_word(l1) == hull_word(l2), "compressed hull identical")
            a1 = sum(1 for t in l1 if t == 'a'); a2 = sum(1 for t in l2 if t == 'a')
            lw = sum(b - a for a, b in w.ivs)
            check(a1 - a2 == lw, "(A) accounting")
            # the region between the two hulls and outside is a-only in l2
            hw = (w.ivs[0][0], w.ivs[-1][1])
            outside = [l2[p] for p in range(n) if not (hv[0] <= p < hv[1]) and not (hw[0] <= p < hw[1])]
            check(all(t == 'a' for t in outside if t is not None), "outside a-only")
            tested += 1
    print("  disjoint pairs tested=%d: anchor hull <= N/2, antichain, identical compressed hull, "
          "(A) accounting, a-only outside: all held" % tested)


# ---------------------------------------------------------------------------
# [H] Proposition NL: non-affine accounting breaks a two-hole Rect
# ---------------------------------------------------------------------------
def in_Lf(w, N, f):
    if not w or set(w) - set('abc'):
        return False
    k = w.count('b')
    if w.count('c') != k:
        return False
    p = w.replace('a', '')
    if p != 'b' * k + 'c' * k:
        return False
    return w.count('a') == N - f(k)


def section_H():
    print("[H] Proposition NL: L_f = {pi in b*c*, |b|=|c|=k, |a| = N - f(k)}")
    N = 40
    for name, f, affine in [("f(k)=4k", lambda k: 4 * k, True),
                            ("f(k)=4k+k(k-1)", lambda k: 4 * k + k * (k - 1), False)]:
        # Rect of the proof: x=(a^al b, c), y=(a^al2 bb, cc), E0=(a^A0, a, eps), E1=(a^A1 b, a, c)
        al2 = 1
        al = f(2) - f(1) + al2            # alpha - alpha' = f(2)-f(1)
        A0 = N - f(1) - al - 1
        A1 = N - f(2) - al - 1
        x = ('a' * al + 'b', 'c'); y = ('a' * al2 + 'bb', 'cc')
        E0 = ('a' * A0, 'a', ''); E1 = ('a' * A1 + 'b', 'a', 'c')
        fill = lambda E, X: E[0] + X[0] + E[1] + X[1] + E[2]
        w = [fill(E0, x), fill(E0, y), fill(E1, x), fill(E1, y)]
        acc = [in_Lf(t, N, f) for t in w]
        types_ok = (content(x[0]) == content(y[0]) and content(x[1]) == content(y[1]))
        print("  %-16s types equal=%s  E0[x],E0[y],E1[x],E1[y] in L: %s" % (name, types_ok, acc))
        check(types_ok and acc[0] and acc[1] and acc[2], "NL premises")
        check(acc[3] == affine, "NL conclusion matches affinity")


def main():
    section_A()
    section_B()
    section_C()
    section_D()
    section_E()
    section_F()
    section_G()
    section_H()
    print()
    if FAILS:
        print("FAILED: %d checks" % len(FAILS))
        sys.exit(1)
    print("ALL CHECKS PASSED")
    sys.exit(0)


if __name__ == '__main__':
    main()
