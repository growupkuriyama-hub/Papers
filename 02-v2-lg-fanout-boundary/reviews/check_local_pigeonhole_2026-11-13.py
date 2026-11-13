#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_local_pigeonhole_2026-11-13.py   (Python 3, 標準ライブラリのみ、乱数不使用)

報告「段付きパリク言語の多項式上界（局所鳩の巣法）」の検査スクリプト。
無限族についての主張は報告書の中で手で証明してある。ここでの検査は
(T1) 局所移動補題（補題1）の言語側の照合と、三段移動では結論が偽になることの確認
(T2) 定理の証明の手順（印・自由節点・DFS 接頭反鎖・色・貪欲削除）を具体的な
     文法の導出木の上で実行し、各段の主張（領域の狭義単調性、反鎖の大きさ、
     残る段の数 <= 色の数、W_I in L、最終的な組 x'' ≡ x）を確かめる
だけを目的とする。
"""
import itertools
from collections import Counter

# ---------------------------------------------------------------- T1
def ex2(m):
    """Fable の Ex2^0_m。段 a<b<c<d<e（各段一文字）。Parikh ベクトル (a,b,c,d,e)。"""
    def member(v):
        a, b, c, d, e = v
        if min(a, c, e) < 1:
            return False
        if b == 0 and d == 0:
            return a % m == 0 and c % m == 0 and e % m == 0
        if b >= 1 and d >= 1:
            return (a - c) % m == 0 and (c - e) % m == 0
        return False
    return member

def t1():
    print('=' * 72)
    print('T1  局所移動補題（補題1）: Ex2^0_m での照合')
    print('=' * 72)
    for m, B in ((2, 6), (3, 7)):
        mem = ex2(m)
        box = [v for v in itertools.product(range(B + 1), repeat=5) if mem(v)]
        stats = Counter()
        cert = None
        for P in box:
            for P2 in box:
                z = tuple(x - y for x, y in zip(P, P2))
                T = [i for i in range(5) if z[i] != 0]
                if not T or len(T) > 3:
                    continue
                if any(min(P[i], P2[i]) < 2 for i in T):
                    continue
                kind = 'local(<=2段)' if len(T) <= 2 else '3段'
                for beta in box:
                    if all(beta[i] >= max(z[i], 0) + 2 for i in T):
                        tgt = tuple(x - y for x, y in zip(beta, z))
                        ok = mem(tgt)
                        stats[(kind, ok)] += 1
                        if kind == '3段' and not ok and cert is None:
                            cert = (P, P2, beta, tgt)
        print('  m=%d 箱[0,%d]^5: ' % (m, B) +
              ', '.join('%s 結論%s=%d' % (k, '成立' if ok else '不成立', n)
                        for (k, ok), n in sorted(stats.items())))
        assert stats[('local(<=2段)', False)] == 0
        print("    三段移動の反例 (P, P', beta, beta-z):", cert)

# ---------------------------------------------------------------- T2
class Node:
    __slots__ = ('label', 'kids', 'yld', 'lo', 'hi')
    def __init__(self, label, kids):
        self.label, self.kids = label, kids

def build(n, fan, letters_leaf, ids):
    """A_n の完全二分木。葉 A_0 -> letters_leaf（成分ごとに一文字）。"""
    if n == 0:
        nd = Node(0, [])
        comp = []
        for ch in letters_leaf:
            ids.append(ch)
            comp.append([len(ids) - 1])
        nd.yld = tuple(comp)
        return nd
    l = build(n - 1, fan, letters_leaf, ids)
    r = build(n - 1, fan, letters_leaf, ids)
    nd = Node(n, [l, r])
    nd.yld = tuple(l.yld[c] + r.yld[c] for c in range(fan))
    return nd

def number_leaves(root):
    cnt = [0]
    def rec(nd):
        if not nd.kids:
            cnt[0] += 1
            nd.lo = nd.hi = cnt[0]
        else:
            for k in nd.kids:
                rec(k)
            nd.lo, nd.hi = nd.kids[0].lo, nd.kids[-1].hi
    rec(root)
    return cnt[0]

def antichain(root, j):
    """I_j: 葉が全て {1..j} に入る極大な節点の反鎖。"""
    out = []
    def rec(nd):
        if nd.hi <= j:
            out.append(nd)
        elif nd.lo <= j:
            for k in nd.kids:
                rec(k)
    rec(root)
    return out

def evaluate(nd, repl, esc, ids, fan):
    """nd の生成組。repl に入る節点は詰め物 esc[label] に取り替える。"""
    if id(nd) in repl:
        return esc[nd.label]
    if not nd.kids:
        return tuple(''.join(ids[i] for i in comp) for comp in nd.yld)
    parts = [evaluate(k, repl, esc, ids, fan) for k in nd.kids]
    return tuple(''.join(p[c] for p in parts) for c in range(fan))

def run(name, n, fan, leaf, esc, ctx, member, letters, rank=2):
    ids = []
    root = build(n, fan, leaf, ids)
    x = tuple(''.join(ids[i] for i in comp) for comp in root.yld)
    assert member(ctx(x)), 'x 自体が L に入らない'
    theta = max(sum(len(c) for c in e) for e in esc.values())
    marks = set()                      # 各成分・各文字の最初と最後の出現
    for comp in root.yld:
        for ch in set(ids[i] for i in comp):
            occ = [i for i in comp if ids[i] == ch]
            marks.add(occ[0]); marks.add(occ[-1])
    def free(nd):
        return not any(i in marks for comp in nd.yld for i in comp)
    maxfree, skeleton = [], []
    def rec(nd):
        if free(nd):
            maxfree.append(nd)
        else:
            skeleton.append(nd)
            for k in nd.kids:
                rec(k)
    rec(root)
    deleted = set()
    max_colors = max_I = kept_steps = checked = 0
    for eta in maxfree:
        q = number_leaves(eta)
        depth = eta.label + 1
        cuts, sizes = [], []
        for j in range(q + 1):
            I = antichain(eta, j)
            max_I = max(max_I, len(I))
            assert len(I) <= (rank - 1) * depth + 1
            sizes.append(sum(len(comp) for nd in I for comp in nd.yld))
            V = Counter()
            for nd in I:
                for comp in esc[nd.label]:
                    V.update(comp)
            cuts.append(tuple(V[ch] for ch in letters))
        assert all(sizes[j] < sizes[j + 1] for j in range(q))   # 領域の狭義単調性
        colors = set(cuts)
        max_colors = max(max_colors, len(colors))
        last = {}
        for j, col in enumerate(cuts):
            last[col] = j
        j = steps = 0
        while j < q:
            j2 = last[cuts[j]]
            if j2 > j:
                U1 = set(i for nd in antichain(eta, j) for comp in nd.yld for i in comp)
                U2 = set(i for nd in antichain(eta, j2) for comp in nd.yld for i in comp)
                assert U1 < U2
                if checked < 60:       # 照合: W_I, W_J in L
                    for jj in (j, j2):
                        repl = set(id(nd) for nd in antichain(eta, jj))
                        assert member(ctx(evaluate(root, repl, esc, ids, fan))), (name, jj)
                    checked += 1
                deleted |= (U2 - U1)
                j = j2
            if j < q:
                steps += 1             # 段 j -> j+1 は残す
                j += 1
        assert steps <= len(colors)
        kept_steps += steps
    x2 = tuple(''.join(ids[i] for i in comp if i not in deleted) for comp in root.yld)
    assert all(x2) and tuple(set(c) for c in x2) == tuple(set(c) for c in x)   # 型の保存
    bad = 0                            # x'' ≡ x の照合（文脈の Parikh ベクトルを箱で全数）
    for e in itertools.product(range(5), repeat=len(letters)):
        pad = ''.join(ch * k for ch, k in zip(letters, e))
        if member(ctx(x) + pad) != member(ctx(x2) + pad):
            bad += 1
    assert bad == 0
    print("  %-30s |x|=%6d -> |x''|=%4d 骨格=%3d 極大自由木=%3d max|I_j|=%2d 色<=%3d 残した段=%3d theta=%d"
          % (name, sum(map(len, x)), sum(map(len, x2)), len(skeleton), len(maxfree),
             max_I, max_colors, kept_steps, theta))

def t2():
    print('=' * 72)
    print("T2  定理の証明の手順を導出木の上で実行（x'' ≡ x と各段の主張を assert）")
    print('=' * 72)
    # (A) 一頂点（パリク飽和）: L = {w in {a,c}+ : #a + 3#c ≡ 2^n (mod m)}
    #     S->A_n, A_i->A_{i-1}A_{i-1} | u_i, A_0->a。u_i は c を含む短い語。
    for n, m in ((8, 5), (10, 7), (12, 11), (13, 13)):
        esc = {}
        for i in range(n + 1):
            c = 1 + (i % 3)
            esc[i] = ('a' * ((pow(2, i, m) - 3 * c) % m) + 'c' * c,)
        tgt = pow(2, n, m)
        member = lambda w, m=m, tgt=tgt: len(w) > 0 and (w.count('a') + 3 * w.count('c')) % m == tgt
        run('A: 一頂点 n=%d m=%d' % (n, m), n, 1, ('a',), esc, lambda t: t[0], member, 'ac')
    # (B) 段付き・ファンアウト2: 段1={a,p} < 段2={b} < 段3={c,q}
    #     L = ND ∩ {b を含み #a + #c + 2#p + 5#q ≡ 2^{n+1} (mod m)}
    #     S->(xi^1 b xi^2)(A_n), A_i->(xx',yy')(A_{i-1},A_{i-1}) | (a^e p, q^beta), A_0->(a,c)
    stage = {'a': 1, 'p': 1, 'b': 2, 'c': 3, 'q': 3}
    for n, m in ((8, 5), (10, 7), (11, 9), (12, 11)):
        esc = {}
        for i in range(n + 1):
            beta = 1 + (i % 2)
            esc[i] = ('a' * ((pow(2, i + 1, m) - 2 - 5 * beta) % m) + 'p', 'q' * beta)
        tgt = pow(2, n + 1, m)
        def member(w, m=m, tgt=tgt):
            w = ''.join(sorted(w, key=lambda ch: stage[ch]))   # 詰め物は段の順に整列して置く
            if 'b' not in w:
                return False
            return (w.count('a') + w.count('c') + 2 * w.count('p') + 5 * w.count('q')) % m == tgt
        run('B: 段付き f=2 n=%d m=%d' % (n, m), n, 2, ('a', 'c'), esc,
            lambda t: t[0] + 'b' + t[1], member, 'apbcq')

if __name__ == '__main__':
    t1()
    t2()
    print('=' * 72)
    print('全ての assert を通過')
