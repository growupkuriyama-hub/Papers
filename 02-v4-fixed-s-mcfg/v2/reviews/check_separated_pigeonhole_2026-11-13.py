#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_separated_pigeonhole_2026-11-13.py  (Python 3, standard library only, fixed seeds)

Executes, on concrete derivation trees, the constructive proof of
Theorem S (local pigeonhole for I-separated, I-closed targets) of the Opus 5.5
round-2 report, and checks every intermediate claim with asserts:

  * marks: first 2f and last 2f occurrences of each letter in each root component;
  * Lemma B3_I: the letters of every free factor are pairwise independent;
  * prefix antichains I_j, regions U_{j'} \\ U_j, colors = (Parikh sum, orientation(W_j));
  * W_j = E_A[x_{I_j}] is in L (here L(G) is a subset of L by construction);
  * Step lemma, y side: the mark copies moved next to the free factor only pass
    independent letters; the hole factor is 1^_k z^_k followed by a separator g_k;
  * Step lemma, F side: the same moves inside W_{j'}; F[t'] = W' in L and F[t] in L,
    holes separated by nonempty words;
  * final tuple x'' has the same component contents, E_A[x''] in L, and
    x'' and x agree on every admissible context with short fixed parts.

Targets (both in C_{f,c} for every f, see report):
  P: an N-shaped stage poset  (1<3, 2<3, 2<4)  -- not a staged-Parikh (ND) language;
  N: a chain of stages                         -- the staged-Parikh class N_st.
L = ND_P  intersected with  {w : weight(w) = 0 mod 7}.
Grammars use rules that move a child component into a different parent component,
and crossing templates (the case the original T2 test did not cover).

Asserts check the bookkeeping of the proof on finite trees; they are not a proof.
"""
import itertools
import random
from collections import Counter

# --------------------------------------------------------------------------- languages
class Target:
    def __init__(self, name, stage, less, weight, mod=7):
        self.name, self.stage, self.less, self.weight, self.mod = name, stage, less, weight, mod
        self.letters = sorted(stage)

    def dep(self, x, y):
        s, t = self.stage[x], self.stage[y]
        return x != y and ((s, t) in self.less or (t, s) in self.less)

    def indep(self, x, y):
        return not self.dep(x, y)

    def ndp(self, w):
        seen = set()
        for ch in w:
            t = self.stage[ch]
            if any((t, s) in self.less for s in seen):
                return False
            seen.add(t)
        return True

    def member(self, w):
        return len(w) > 0 and self.ndp(w) and sum(self.weight[ch] for ch in w) % self.mod == 0

    def orientation(self, w):
        first, last = {}, {}
        for i, ch in enumerate(w):
            first.setdefault(ch, i); last[ch] = i
        o = []
        for x, y in itertools.combinations(sorted(first), 2):
            if self.dep(x, y):
                assert last[x] < first[y] or last[y] < first[x], 'word not separated'
                o.append((x, y) if last[x] < first[y] else (y, x))
        return tuple(o)

def closure(rel):
    rel = set(rel)
    while True:
        new = {(a, d) for (a, b) in rel for (c, d) in rel if b == c} - rel
        if not new:
            return rel
        rel |= new

TARGET_P = Target('P (N-poset)', {'a': 1, 'e': 1, 'b': 2, 'c': 3, 'd': 4},
                  closure({(1, 3), (2, 3), (2, 4)}),
                  {'a': 1, 'e': 3, 'b': 2, 'c': 5, 'd': 6})
TARGET_N = Target('N (chain)', {'a': 1, 'e': 1, 'b': 2, 'c': 3, 'd': 4},
                  closure({(1, 2), (2, 3), (3, 4)}),
                  {'a': 1, 'e': 3, 'b': 2, 'c': 5, 'd': 6})

# --------------------------------------------------------------------------- grammars
def T(s):
    return [('t', ch) for ch in s]

def V(j, c):
    return ('v', j, c)

def pad(tmpl, weight, mod):
    """Prefix 'a'*r to the first component so that explicit terminals weigh 0 mod 7."""
    w = sum(weight[it[1]] for c in tmpl for it in c if it[0] == 't')
    r = (-w) % mod
    return (T('a' * r) + list(tmpl[0]),) + tuple(tmpl[1:])

def grammar_P(weight):
    R = []
    add = lambda lhs, tmpl, kids: R.append((lhs, pad(tmpl, weight, 7) if lhs != 'S' else tmpl, kids))
    R.append(('S', ([V(0, 0)] + T('e') + [V(0, 1)] + T('cd'),), ('A',)))   # e+c+d = 14
    for u, v in (('b', 'd'), ('ea', 'da'), ('ab', 'ad'), ('e', 'aed')):
        add('A', (T(u), T(v)), ())
    add('A', ([V(0, 0), V(1, 0)], [V(0, 1), V(1, 1)]), ('A', 'A'))
    add('A', ([V(0, 0), V(1, 0)], [V(1, 1), V(0, 1)]), ('A', 'A'))          # crossing
    add('A', ([V(0, 0)] + T('b') + [V(1, 0)], [V(1, 1)] + T('d') + [V(0, 1)]), ('A', 'C'))
    add('A', (T('b'), [V(0, 0)] + T('d') + [V(0, 1)]), ('C',))              # moves C.1 into A.2
    add('C', (T('a'), T('e')), ())
    add('C', (T('e'), T('ae')), ())
    add('C', (T('e'), [V(0, 0)] + T('a') + [V(0, 1)]), ('C',))              # moves C.1 into C.2
    add('C', ([V(0, 0), V(1, 0)], [V(1, 1), V(0, 1)]), ('C', 'C'))
    fan = {'S': 1, 'A': 2, 'C': 2}
    return R, fan, ('', 'e', 'cd')

def grammar_N(weight):
    R = []
    add = lambda lhs, tmpl, kids: R.append((lhs, pad(tmpl, weight, 7) if lhs != 'S' else tmpl, kids))
    R.append(('S', ([V(0, 0)] + T('b') + [V(0, 1)] + T('dd'),), ('A',)))   # b+d+d = 14
    for u, v in (('a', 'c'), ('ea', 'cc'), ('ae', 'c')):
        add('A', (T(u), T(v)), ())
    add('A', ([V(0, 0), V(1, 0)], [V(0, 1), V(1, 1)]), ('A', 'A'))
    add('A', ([V(0, 0), V(1, 0)], [V(1, 1), V(0, 1)]), ('A', 'A'))
    add('A', ([V(0, 0)] + T('e') + [V(0, 1)], T('c')), ('C',))              # moves C.2 into A.1
    add('A', ([V(0, 0)] + T('a') + [V(1, 0), V(0, 1)], [V(1, 1)] + T('c')), ('C', 'A'))
    add('C', (T('a'), T('e')), ())
    add('C', (T('e'), [V(0, 0)] + T('a') + [V(0, 1)]), ('C',))
    add('C', ([V(0, 0), V(1, 0)], [V(1, 1), V(0, 1)]), ('C', 'C'))
    fan = {'S': 1, 'A': 2, 'C': 2}
    return R, fan, ('', 'b', 'dd')

def check_good(rules, fan):
    for lhs, tmpl, kids in rules:
        assert all(len(c) > 0 for c in tmpl) and len(tmpl) == fan[lhs]
        seq = [it for c in tmpl for it in c]
        for j, B in enumerate(kids):
            assert [it[2] for it in seq if it[0] == 'v' and it[1] == j] == list(range(fan[B]))
        for c in tmpl:
            for x, y in zip(c, c[1:]):
                assert not (x[0] == y[0] == 'v' and x[1] == y[1] and y[2] == x[2] + 1)

# --------------------------------------------------------------------------- trees
class Node:
    __slots__ = ('B', 'tmpl', 'kids', 'comps', 'own', 'lo', 'hi')

def build(rules, B, depth, rng):
    cand = [r for r in rules if r[0] == B and (len(r[2]) > 0) == (depth > 0)]
    if depth > 0:
        two = [r for r in cand if len(r[2]) == 2]
        if two and rng.random() < 0.8:
            cand = two
    _, tmpl, kids = rng.choice(cand)
    nd = Node()
    nd.B, nd.tmpl = B, tmpl
    nd.kids = [build(rules, K, max(0, depth - 1 - (rng.random() < 0.2)), rng) for K in kids]
    return nd

def evaluate(nd, letter):
    for k in nd.kids:
        evaluate(k, letter)
    out, own = [], []
    for c in nd.tmpl:
        ids = []
        for it in c:
            if it[0] == 't':
                letter.append(it[1]); own.append(len(letter) - 1); ids.append(len(letter) - 1)
            else:
                ids.extend(nd.kids[it[1]].comps[it[2]])
        out.append(ids)
    nd.comps, nd.own = tuple(out), own

def eval_rep(nd, repl, short, eta):
    """Tokens (letter, x-id or None, eta-component tag); nodes in repl replaced by short[B]."""
    if id(nd) in repl:
        out = [[(ch, None, None) for ch in comp] for comp in short[nd.B]]
    else:
        kid_out = [eval_rep(k, repl, short, eta) for k in nd.kids]
        own = iter(nd.own)
        out = []
        for c in nd.tmpl:
            toks = []
            for it in c:
                if it[0] == 't':
                    toks.append((it[1], next(own), None))
                else:
                    toks.extend(kid_out[it[1]][it[2]])
            out.append(toks)
    if nd is eta:
        out = [[(ch, i, kappa) for (ch, i, _) in comp] for kappa, comp in enumerate(out)]
    return out

def number(nd):
    cnt = [0]
    def rec(v):
        if not v.kids:
            cnt[0] += 1; v.lo = v.hi = cnt[0]
        else:
            for k in v.kids:
                rec(k)
            v.lo, v.hi = v.kids[0].lo, v.kids[-1].hi
    rec(nd)
    return cnt[0]

def antichain(eta, j):
    out = []
    def rec(v):
        if v.hi <= j:
            out.append(v)
        elif v.lo <= j:
            for k in v.kids:
                rec(k)
    rec(eta)
    return out

def shortest_tuples(rules, fan):
    short = {}
    changed = True
    while changed:
        changed = False
        for lhs, tmpl, kids in rules:
            if any(K not in short for K in kids):
                continue
            tup = tuple(''.join(it[1] if it[0] == 't' else short[kids[it[1]]][it[2]] for it in c)
                        for c in tmpl)
            if lhs not in short or sum(map(len, tup)) < sum(map(len, short[lhs])):
                short[lhs] = tup; changed = True
    return short

def with_ctx(ctx, comps):
    w = ctx[0]
    for c, v in zip(comps, ctx[1:]):
        w += c + v
    return w

def tok_ctx(ctx, comps):
    toks = [(ch, 'E', None) for ch in ctx[0]]
    for c, v in zip(comps, ctx[1:]):
        toks += list(c) + [(ch, 'E', None) for ch in v]
    return toks

# --------------------------------------------------------------------------- the proof, executed
def run(tg, gfun, depth, seed, f=2):
    rules, fan, ctx = gfun(tg.weight)
    check_good(rules, fan)
    rng = random.Random(seed)
    root = build(rules, 'A', depth, rng)
    letter = []
    evaluate(root, letter)
    L = lambda ids: ''.join(letter[i] for i in ids)
    x = [list(c) for c in root.comps]
    assert tg.member(with_ctx(ctx, [L(c) for c in x])), 'E_A[x] not in L'
    compof = {i: ci for ci, c in enumerate(x) for i in c}
    MF = 2 * f
    marks, firstmarks = set(), {}
    for ci, c in enumerate(x):
        occ = {}
        for i in c:
            occ.setdefault(letter[i], []).append(i)
        for a, lst in occ.items():
            marks.update(lst[:MF]); marks.update(lst[-MF:])
            firstmarks[(ci, a)] = lst[:MF]
    def free(nd):
        return not any(i in marks for c in nd.comps for i in c)
    maxfree, skeleton = [], []
    def walk(nd):
        if free(nd):
            maxfree.append(nd)
        else:
            skeleton.append(nd)
            for k in nd.kids:
                walk(k)
    walk(root)
    # Lemma B3_I: letters of a free factor pairwise independent
    for eta in maxfree:
        for c in eta.comps:
            al = set(letter[i] for i in c)
            assert all(tg.indep(p, q) for p in al for q in al), 'B3 violated'
    short = shortest_tuples(rules, fan)
    regions = []
    stats = Counter()
    for eta in maxfree:
        q = number(eta)
        U, col = [], []
        for j in range(q + 1):
            I = antichain(eta, j)
            stats['max_I'] = max(stats['max_I'], len(I))
            U.append(set(i for nd in I for c in nd.comps for i in c))
            Wj = tok_ctx(ctx, eval_rep(root, set(id(nd) for nd in I), short, eta))
            wj = ''.join(t[0] for t in Wj)
            assert tg.member(wj), 'W_j not in L'
            ps = Counter()
            for nd in I:
                for comp in short[nd.B]:
                    ps.update(comp)
            col.append((tuple(ps[a] for a in tg.letters), tg.orientation(wj)))
        assert all(U[j] < U[j + 1] for j in range(q))
        last = {c: j for j, c in enumerate(col)}
        stats['max_colors'] = max(stats['max_colors'], len(last))
        j = 0
        while j < q:
            j2 = last[col[j]]
            if j2 > j:
                regions.append((eta, j, j2, U[j2] - U[j]))
                j = j2
            if j < q:
                stats['kept_steps'] += 1
                j += 1
    # ---------------------------------------------------------------- step lemma, region by region
    y = [list(c) for c in x]
    for (eta, j, j2, R) in regions:
        assert not (R & marks)
        holes = []                                   # (component, start index, kappa, Rids, phi ids)
        for kappa, comp in enumerate(eta.comps):
            ci = compof[comp[0]]
            S = set(comp)
            idx = [p for p, i in enumerate(y[ci]) if i in S]
            assert idx == list(range(idx[0], idx[0] + len(idx))), 'free factor not contiguous'
            Rk = [i for i in y[ci][idx[0]:idx[-1] + 1] if i in R]
            if Rk:
                holes.append((ci, idx[0], kappa, Rk, y[ci][idx[0]:idx[-1] + 1]))
        holes.sort()
        e = len(holes)
        assert 1 <= e <= f
        stats['steps'] += 1
        stats['two_hole_steps'] += (e == 2)
        # -------- y side
        used = set()
        plan = []                                    # per hole: (copies for 1^, copy g)
        for (ci, st, kappa, Rk, phi) in holes:
            Tk = sorted(set(letter[i] for i in Rk))
            if len(set(tg.stage[a] for a in Tk)) > 1:      # hole spans incomparable stages
                stats['holes_multi_stage'] += 1
            copies = []
            for a in Tk + [Tk[0]]:
                c = next(i for i in firstmarks[(ci, a)] if i not in used)
                used.add(c)
                p = y[ci].index(c)
                assert p < st
                assert all(letter[b] == a or tg.indep(a, letter[b]) for b in y[ci][p + 1:st]), 'illegal move'
                copies.append(c)
            plan.append(copies)
        ypi = []
        for ci, comp in enumerate(y):
            moved = set(c for copies in plan for c in copies)
            hs = {h[1]: (h, plan[n]) for n, h in enumerate(holes) if h[0] == ci}
            new, p = [], 0
            while p < len(comp):
                if p in hs:
                    (ci_, st, kappa, Rk, phi), copies = hs[p]
                    new += copies[:-1] + Rk + [copies[-1]] + [i for i in phi if i not in set(Rk)]
                    p += len(phi)
                    continue
                if comp[p] not in moved:
                    new.append(comp[p])
                p += 1
            ypi.append(new)
        assert tg.member(with_ctx(ctx, [L(c) for c in ypi]))
        t = [L(plan[n][:-1] + h[3]) for n, h in enumerate(holes)]
        tp = [L(plan[n][:-1]) for n, h in enumerate(holes)]
        assert all(set(a) == set(b) for a, b in zip(t, tp))
        # -------- F side, inside W_{j'}
        I2 = antichain(eta, j2)
        Wt = tok_ctx(ctx, eval_rep(root, set(id(nd) for nd in I2), short, eta))
        Wj1 = tok_ctx(ctx, eval_rep(root, set(id(nd) for nd in antichain(eta, j)), short, eta))
        z = Counter(letter[i] for i in R)
        assert Counter(tk[0] for tk in Wj1) == Counter(tk[0] for tk in Wt) + z
        used_w, insert = set(), {}
        for n, (ci, st, kappa, Rk, phi) in enumerate(holes):
            pstart = next(p for p, tk in enumerate(Wt) if tk[2] == kappa)
            Tk = sorted(set(letter[i] for i in Rk))
            chosen = []
            for a in Tk + [Tk[0]]:
                c = next(i for i in firstmarks[(ci, a)] if i not in used_w)
                used_w.add(c)
                p = next(p for p, tk in enumerate(Wt) if tk[1] == c)
                assert p < pstart
                assert any(tk[0] == a for tk in Wt[pstart:]), 'no later copy of a in W'
                assert all(tk[0] == a or tg.indep(a, tk[0]) for tk in Wt[p + 1:pstart]), 'illegal move in W'
                chosen.append(c)
            insert[pstart] = (n, chosen)
        moved = used_w
        segs, cur, holes_in_order = [], [], []
        for p, tk in enumerate(Wt):
            if p in insert:
                n, chosen = insert[p]
                segs.append(cur); cur = []
                holes_in_order.append(n)
                cur = [letter[chosen[-1]]]              # separator g_k right after the hole
            if tk[1] not in moved:
                cur.append(tk[0])
        segs.append(cur)
        assert holes_in_order == list(range(e))
        assert all(len(s) > 0 for s in segs[1:-1]), 'empty separator between holes'
        Fw = lambda tup: ''.join(segs[0]) + ''.join(tt + ''.join(sg) for tt, sg in zip(tup, segs[1:]))
        assert tg.member(Fw(tp)), "F[t'] not in L"
        assert tg.member(Fw(t)), 'F[t] not in L'
        # -------- apply: y <- y with R deleted
        y = [[i for i in c if i not in R] for c in y]
        assert tg.member(with_ctx(ctx, [L(c) for c in y]))
    x2 = y
    assert all(set(L(a)) == set(L(b)) for a, b in zip(x, x2))
    # x'' agrees with x on all admissible contexts with short fixed parts
    bad = tested = 0
    X1, X2 = [L(c) for c in x], [L(c) for c in x2]
    for n in range(1, 4):
        for fixed in itertools.product(tg.letters, repeat=n):
            fixed = ''.join(fixed)
            for c1 in range(n + 1):
                for c2 in range(c1 + 1, n + 1):
                    E = (fixed[:c1], fixed[c1:c2], fixed[c2:])
                    tested += 1
                    bad += tg.member(with_ctx(E, X1)) != tg.member(with_ctx(E, X2))
    assert bad == 0
    # negative control: deleting one free letter of nonzero weight is detected by some context
    fx = next(i for nd in maxfree for c in nd.comps for i in c if tg.weight[letter[i]] % tg.mod)
    X3 = [L([i for i in c if i != fx]) for c in x]
    assert any(tg.member(with_ctx(E, X1)) != tg.member(with_ctx(E, X3))
               for E in (ctx, ('', ctx[1] + 'a', ctx[2]), ('a', ctx[1], ctx[2])))
    print("  %-14s depth=%2d seed=%d |x|=%5d -> |x''|=%4d skeleton=%3d max-free-subtrees=%3d "
          "max|I_j|=%2d max#colors=%3d regions=%3d (2-hole %3d) contexts=%d"
          % (tg.name, depth, seed, sum(map(len, x)), sum(map(len, x2)), len(skeleton), len(maxfree),
             stats['max_I'], stats['max_colors'], stats['steps'], stats['two_hole_steps'], tested))
    return stats

def main():
    print('=' * 100)
    print('Theorem S: local pigeonhole for I-separated, I-closed targets -- executed proof with asserts')
    print('=' * 100)
    tot = Counter()
    for tg, gf in ((TARGET_P, grammar_P), (TARGET_N, grammar_N)):
        for depth, seed in ((7, 1), (8, 2), (9, 3), (10, 4), (10, 5), (11, 6)):
            tot += run(tg, gf, depth, seed)
    print('  holes whose letters span two incomparable stages (e.g. a and d in P):', tot['holes_multi_stage'])
    print('all asserts passed')

if __name__ == '__main__':
    main()
