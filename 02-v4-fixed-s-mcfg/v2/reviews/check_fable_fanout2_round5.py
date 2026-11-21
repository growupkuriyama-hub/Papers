#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_fable_fanout2_round5.py  (2026-11-14, Claude Fable)

fan-out 2 第五段: ブロック分割版 L^tensor の「穴数」問題の再現スクリプト。
Python 3 標準ライブラリのみ。乱数シードは固定 (SEED)。

実行:   python3 check_fable_fanout2_round5.py
所要:   数十秒程度。全 assert が通れば最後に "ALL CHECKS PASSED" を表示する。

内容
  例A  (実定数)   言語 L7、文法 G_14、型付き非終端 (B_14)_T (arity 2)。
                  第四段 §5 の手順どおりに一段の削除を作ると e=4>f=2 になること、
                  穴の真部分集合の置換がすべて L の外に出ること、
                  束ね (bundling) で 2 穴の合法な文脈になることを検査する。
                  ell=1 と ell=2 の両方。
  例B  (縮小定数) 根が arity 1。同じ根成分に 4 つの (1,b,J) が現れる変種 (5文字)。
                  c_* は理論値でなく検査用の小さい値 (明示的に縮小)。
  G1   P0^tensor: 射影ごとの (s_ell, N_ell) が文脈挿入で保たれることの乱数検査。
  G2   穴語 h,t の構成 (de Bruijn 閉歩道) の乱数検査。
  G3   束ね組立て関数の乱数検査。

注意: 有限検査は定理の証明ではない。証明は報告書の本文にある。
"""
import random
import sys
from collections import Counter
from itertools import combinations, product

SEED = 20261114
sys.setrecursionlimit(10000)

# ----------------------------------------------------------------------------
# 基本: 射影, 窓型 s_ell, 因子計数 N_ell
# ----------------------------------------------------------------------------

def proj(w, block):
    return ''.join(ch for ch in w if ch in block)


def s_ell(u, ell):
    """s_ell = s_{ell-1,ell-1} の完備化。空語は単位元として区別する。"""
    m = ell - 1
    if u == '':
        return ('eps',)
    if len(u) < 2 * m:
        return ('short', u)
    return ('long', u[:m], u[len(u) - m:] if m else '')


def N_ell(u, ell):
    return Counter(u[i:i + ell] for i in range(len(u) - ell + 1))


def data(w, blocks, ell):
    """所属を決めるデータ ((s_ell, N_ell)(pi_b w))_b"""
    out = []
    for B in blocks:
        p = proj(w, B)
        out.append((s_ell(p, ell), frozenset(N_ell(p, ell).items())))
    return tuple(out)


def is_circulation(Z):
    bal = Counter()
    for e, c in Z.items():
        bal[e[:-1]] -= c
        bal[e[1:]] += c
    return all(v == 0 for v in bal.values())


def c_sequence(k_b, ell, f):
    K = k_b ** ell
    V = k_b ** (ell - 1)
    lam = K * (2 * V - 1)
    lamp = max(2 * (ell - 1) * lam, K)      # ell=1 では |h_J|<=K を使う
    c = [None, 1]
    for _ in range(K + 2):
        c.append(K * c[-1] + f * ell + lamp + 2)
    return K, lamp, c                         # c[g] = c_g,  c_* = c[K+2]


# ----------------------------------------------------------------------------
# 文法
# ----------------------------------------------------------------------------

class Grammar:
    def __init__(self, start):
        self.fan = {}
        self.rules = []       # (lhs, template, children)  template: list[list[sym]]
        self.start = start

    def add(self, lhs, template, children=()):
        self.rules.append((lhs, [list(c) for c in template], tuple(children)))
        return len(self.rules) - 1


def V(j, k):
    return (j, k)             # 変数 xi_{j+1}^{k+1} (0-based)


def check_good_reduced(G):
    for (lhs, tpl, ch) in G.rules:
        assert len(tpl) == G.fan[lhs]
        seq = [s for comp in tpl for s in comp]
        vars_ = [s for s in seq if isinstance(s, tuple)]
        # eps-free
        assert all(len(comp) >= 1 for comp in tpl), 'eps-free'
        # linear + nondeleting
        want = [(j, k) for j, B in enumerate(ch) for k in range(G.fan[B])]
        assert sorted(vars_) == sorted(want), 'linear/nondeleting'
        # nonpermuting
        for j in range(len(ch)):
            ks = [k for (jj, k) in vars_ if jj == j]
            assert ks == sorted(ks), 'nonpermuting'
        # nonmerging
        for comp in tpl:
            for s1, s2 in zip(comp, comp[1:]):
                if isinstance(s1, tuple) and isinstance(s2, tuple):
                    assert not (s1[0] == s2[0] and s2[1] == s1[1] + 1), 'nonmerging'
    # reduced
    prod = set()
    changed = True
    while changed:
        changed = False
        for (lhs, tpl, ch) in G.rules:
            if lhs not in prod and all(c in prod for c in ch):
                prod.add(lhs); changed = True
    reach = {G.start}
    changed = True
    while changed:
        changed = False
        for (lhs, tpl, ch) in G.rules:
            if lhs in reach:
                for c in ch:
                    if c not in reach:
                        reach.add(c); changed = True
    assert prod == set(G.fan) == reach, 'reduced'
    fanout = max(G.fan.values())
    rank = max(len(ch) for (_, _, ch) in G.rules)
    return fanout, rank


def typed_min_table(G):
    """(非終端, 内容型ベクトル) ごとの導出木の最小節点数と、その最小木の本数。"""
    best = {A: {} for A in G.fan}
    changed = True
    while changed:
        changed = False
        for (lhs, tpl, ch) in G.rules:
            tables = [list(best[c].items()) for c in ch]
            for combo in product(*tables):
                cost = 1 + sum(c for (_, c) in combo)
                typ = tuple(
                    frozenset().union(*[
                        (frozenset([s]) if isinstance(s, str) else combo[s[0]][0][s[1]])
                        for s in comp]) for comp in tpl)
                if cost < best[lhs].get(typ, 10 ** 18):
                    best[lhs][typ] = cost; changed = True
    ways = {A: {} for A in G.fan}
    entries = sorted(((c, A, t) for A in best for t, c in best[A].items()),
                     key=lambda z: z[0])
    for (c0, A, t) in entries:
        w = 0
        for (lhs, tpl, ch) in G.rules:
            if lhs != A:
                continue
            tables = [list(best[c].items()) for c in ch]
            for combo in product(*tables):
                if 1 + sum(c for (_, c) in combo) != c0:
                    continue
                typ = tuple(
                    frozenset().union(*[
                        (frozenset([s]) if isinstance(s, str) else combo[s[0]][0][s[1]])
                        for s in comp]) for comp in tpl)
                if typ == t:
                    ww = 1
                    for j, (tj, cj) in enumerate(combo):
                        ww *= ways[ch[j]][tj]
                    w += ww
        ways[A][t] = w
    return best, ways


# ----------------------------------------------------------------------------
# 導出木
# ----------------------------------------------------------------------------

class Node:
    __slots__ = ('rule', 'kids', 'lens', 'spans', 'lo', 'hi', 'parent', 'nt', 'val')

    def __init__(self, rule, kids=()):
        self.rule = rule
        self.kids = list(kids)
        self.parent = None
        for k in self.kids:
            k.parent = self


def evaluate(G, node):
    lhs, tpl, ch = G.rules[node.rule]
    node.nt = lhs
    for k in node.kids:
        evaluate(G, k)
    vals = []
    for comp in tpl:
        vals.append(''.join(s if isinstance(s, str) else node.kids[s[0]].val[s[1]]
                            for s in comp))
    node.val = tuple(vals)
    node.lens = tuple(len(v) for v in vals)


def assign_spans(G, node, spans):
    """spans[kappa] = (根成分 i, start, end)。good 規則なので各成分は連続因子。"""
    node.spans = spans
    lhs, tpl, ch = G.rules[node.rule]
    kid_spans = [[None] * len(k.lens) for k in node.kids]
    for kappa, comp in enumerate(tpl):
        i, pos, end = spans[kappa]
        for s in comp:
            if isinstance(s, str):
                pos += 1
            else:
                ln = node.kids[s[0]].lens[s[1]]
                kid_spans[s[0]][s[1]] = (i, pos, pos + ln)
                pos += ln
        assert pos == end
    for k, sp in zip(node.kids, kid_spans):
        assign_spans(G, k, sp)


def count_nodes(node):
    return 1 + sum(count_nodes(k) for k in node.kids)


def number_leaves(node, start=0):
    node.lo = start
    if not node.kids:
        node.hi = start + 1
    else:
        cur = start
        for k in node.kids:
            cur = number_leaves(k, cur)
        node.hi = cur
    return node.hi


def eval_tagged(G, node, cut, short):
    """cut に入る節点を短い無型生成組 short[nt] に置換して評価する。
    返り値: 成分ごとの [(文字, 置換文字か)] のリスト。"""
    if id(node) in cut:
        return [[(ch, True) for ch in comp] for comp in short[node.nt]]
    lhs, tpl, ch = G.rules[node.rule]
    kv = [eval_tagged(G, k, cut, short) for k in node.kids]
    out = []
    for comp in tpl:
        acc = []
        for s in comp:
            if isinstance(s, str):
                acc.append((s, False))
            else:
                acc.extend(kv[s[0]][s[1]])
        out.append(acc)
    return out


# ----------------------------------------------------------------------------
# 印, 自由節点, 頻度の隙間 (W2)
# ----------------------------------------------------------------------------

def block_positions(word, block):
    return [p for p, ch in enumerate(word) if ch in block]


def mark_component(word, blocks, ell, cstar_per_block):
    marked = bytearray(len(word))
    for B, cstar in zip(blocks, cstar_per_block):
        pos = block_positions(word, B)
        seen = Counter()
        for q in range(len(pos) - ell + 1):
            win = ''.join(word[p] for p in pos[q:q + ell])
            seen[win] += 1
            if seen[win] <= cstar:
                for p in pos[q:q + ell]:
                    marked[p] = 1
    return marked


def prefix_sums(arr):
    ps = [0]
    for v in arr:
        ps.append(ps[-1] + v)
    return ps


def maximal_free_nodes(root, mark_ps):
    out = []

    def is_free(n):
        return all(mark_ps[i][e] - mark_ps[i][s] == 0 for (i, s, e) in n.spans)

    def rec(n):
        if is_free(n):
            out.append(n)
        else:
            for k in n.kids:
                rec(k)
    rec(root)
    return out


def w2_structure(pword, k_b, ell, cseq):
    """頻度の隙間 g, 頻出辺, その弱連結成分 (強連結であることを assert)。"""
    K = k_b ** ell
    cnt = N_ell(pword, ell)
    g = None
    for gg in range(1, K + 2):                 # K+1 個の区間 (監査Lの修正 E1)
        if not any(cseq[gg] <= c < cseq[gg + 1] for c in cnt.values()):
            g = gg; break
    assert g is not None
    freq = {e for e, c in cnt.items() if c >= cseq[g + 1]}
    rare_occ = sum(c for e, c in cnt.items() if e not in freq)
    assert rare_occ <= (K - 1) * (cseq[g] - 1)
    # 弱連結成分
    par = {}

    def find(a):
        while par.setdefault(a, a) != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    for e in freq:
        par[find(e[:-1])] = find(e[1:])
    comps = {}
    for e in freq:
        comps.setdefault(find(e[:-1]), set()).add(e)
    comps = [frozenset(c) for c in comps.values()]
    for J in comps:                            # 強連結性
        verts = {e[:-1] for e in J} | {e[1:] for e in J}
        for v0 in verts:
            seen = {v0}; stack = [v0]
            while stack:
                u = stack.pop()
                for e in J:
                    if e[:-1] == u and e[1:] not in seen:
                        seen.add(e[1:]); stack.append(e[1:])
            assert seen == verts, 'frequent component not strongly connected'
    return g, freq, comps


# ----------------------------------------------------------------------------
# 穴語 h, t (de Bruijn 閉歩道)
# ----------------------------------------------------------------------------

def euler_closed(counts, start):
    """辺個数 counts (釣り合い・start を含む連結) の閉 Euler 歩道のラベル語。"""
    adj = {}
    for e, c in counts.items():
        if c:
            adj.setdefault(e[:-1], []).extend([e] * c)
    stack = [(start, None)]
    out = []
    while stack:
        v, e_in = stack[-1]
        if adj.get(v):
            e = adj[v].pop()
            stack.append((e[1:], e))
        else:
            stack.pop()
            if e_in is not None:
                out.append(e_in)
    out.reverse()
    assert sum(counts.values()) == len(out), 'Euler: not connected'
    # 連続性の確認
    v = start
    for e in out:
        assert e[:-1] == v
        v = e[1:]
    assert v == start
    return ''.join(e[-1] for e in out)


def covering_closed_walk(J, u):
    """u を基点に J の全辺を通る閉歩道 h_J の辺個数 (各辺>=1, 釣り合い)。"""
    verts = sorted({e[:-1] for e in J} | {e[1:] for e in J})

    def path(a, b):
        prev = {a: None}; queue = [a]
        while queue:
            x = queue.pop(0)
            if x == b:
                break
            for e in sorted(J):
                if e[:-1] == x and e[1:] not in prev:
                    prev[e[1:]] = e; queue.append(e[1:])
        res = []
        x = b
        while prev[x] is not None:
            res.append(prev[x]); x = prev[x][:-1]
        return res[::-1]
    cnt = Counter()
    for e in sorted(J):
        for ee in path(u, e[:-1]) + [e] + path(e[1:], u):
            cnt[ee] += 1
    return cnt


def make_hole(J, u, Z, ell):
    """(h, t): 頂点 u に居るときに挿入するラベル語。N(t)-N(h)=Z, 型一致。"""
    hJ = covering_closed_walk(J, u)
    if ell == 1:
        h = euler_closed(hJ, u)
        t = euler_closed(hJ + Z, u)
        return h, t
    H0cnt = Counter({e: c * (ell - 1) for e, c in hJ.items()})
    H0 = euler_closed(hJ, u) * (ell - 1)
    h = H0 + H0
    t = H0 + euler_closed(H0cnt + Z, u)
    return h, t


# ----------------------------------------------------------------------------
# 束ね (bundling) の組立て
# ----------------------------------------------------------------------------

def assemble(block_pieces):
    """
    一つの根成分 (または F 側の語全体) について、ブロックごとの分解
        block_pieces[b] = (u0, [(hole_1, u_1), ..., (hole_n, u_n)])
    を受け取り、順位 m の穴を全ブロックにわたって連結した語を作る。
    返り値: (pre, [(bundled_hole_m, sep_m)]) 。sep_m は穴 m の直後の片。
    前提: 各 u_m (m>=1) は非空 (Euler 残差)。
    """
    pre = ''.join(u0 for (u0, _) in block_pieces)
    nmax = max((len(hs) for (_, hs) in block_pieces), default=0)
    out = []
    for m in range(nmax):
        hole = ''.join(hs[m][0] for (_, hs) in block_pieces if len(hs) > m)
        sep = ''.join(hs[m][1] for (_, hs) in block_pieces if len(hs) > m)
        assert hole != '' and sep != ''
        out.append((hole, sep))
    return pre, out


def fill(pre, bundles):
    return pre + ''.join(h + s for (h, s) in bundles)


# ----------------------------------------------------------------------------
# 例の文法
# ----------------------------------------------------------------------------

WT = {'a': 1, 'c': 1, 'b': -1, 'd': -1, 'e': 0}


def in_L(w):
    return len(w) > 0 and sum(WT[ch] for ch in w) == 0


def build_grammar(M, variant):
    """variant 'A': 4文字, 脱出組 (ab,ab)。 'B': 5文字, 脱出組 (e,e), C を追加。"""
    G = Grammar('S')
    G.fan['S'] = 1
    for m in range(M + 1):
        G.fan['B%d' % m] = 2
    R = {}
    for x in 'ac':
        for y in 'bd':
            G.add('S', [[x, y]]); G.add('S', [[y, x]])
            G.add('S', [[x, V(0, 0), y]], ['S']); G.add('S', [[y, V(0, 0), x]], ['S'])
    R['Sab'] = 0                                      # S -> ab は最初の規則
    assert G.rules[0][1] == [['a', 'b']]
    G.add('S', [[V(0, 0), V(1, 0)]], ['S', 'S'])
    esc = ('ab', 'ab') if variant == 'A' else ('e', 'e')
    for m in range(M + 1):
        R['esc%d' % m] = G.add('B%d' % m, [list(esc[0]), list(esc[1])])
    R['B0'] = G.add('B0', [list('acccc'), list('bbddd')])
    for m in range(1, M + 1):
        R['B%d' % m] = G.add('B%d' % m, [[V(0, 0), V(1, 0)], [V(0, 1), V(1, 1)]],
                             ['B%d' % (m - 1)] * 2)
    if variant == 'A':
        R['SBS'] = G.add('S', [[V(0, 0), V(1, 0), V(0, 1)]], ['B%d' % M, 'S'])
    else:
        G.fan['C'] = 1
        G.add('S', [['e']]); G.add('S', [['e', V(0, 0)]], ['S']); G.add('S', [[V(0, 0), 'e']], ['S'])
        R['C'] = G.add('C', [[V(0, 0), V(1, 0), V(0, 1)]], ['B%d' % M, 'S'])
        G.add('S', [[V(0, 0)]], ['C'])
    return G, R, esc


def full_B_tree(R, m):
    if m == 0:
        return Node(R['B0'])
    return Node(R['B%d' % m], [full_B_tree(R, m - 1), full_B_tree(R, m - 1)])


# ----------------------------------------------------------------------------
# 一段の削除の解析 (第四段 §5 の手順どおり)
# ----------------------------------------------------------------------------

def analyse_step(G, root, x, blocks, ell, cstars, cseqs, esc, j, jp, label):
    d = len(x)
    # 印と自由節点
    marks = [mark_component(x[i], blocks, ell, cstars) for i in range(d)]
    mps = [prefix_sums(m) for m in marks]
    frees = [n for n in maximal_free_nodes(root, mps) if len(n.lens) == 2]
    assert frees, 'no free fan-2 node'
    eta = max(frees, key=lambda n: sum(n.lens))
    # 極大性: 親は印を含む
    par = eta.parent
    assert par is not None
    assert any(mps[i][e] - mps[i][s] > 0 for (i, s, e) in par.spans)
    nleaves = number_leaves(eta, 0)
    assert nleaves >= jp
    # W2: 各 (i,b) の頻出成分
    w2 = {}
    for i in range(d):
        for b, B in enumerate(blocks):
            p = proj(x[i], B)
            if len(p) >= ell:
                w2[(i, b)] = w2_structure(p, len(B), ell, cseqs[b])

    def cut_nodes(jj):
        res = []

        def rec(n):
            if n.hi <= jj:
                res.append(n)
            elif n.lo < jj:
                for k in n.kids:
                    rec(k)
        rec(eta)
        return res

    short = {nt: esc for nt in G.fan if nt.startswith('B')}
    info = {}
    for jj in (j, jp):
        I = cut_nodes(jj)
        U = [bytearray(len(x[i])) for i in range(d)]
        for n in I:
            for (i, s, e) in n.spans:
                for p in range(s, e):
                    U[i][p] = 1
        ups = [prefix_sums(u) for u in U]
        psi = eval_tagged(G, eta, {id(n) for n in I}, short)
        col = []
        Npsi = {}
        for kappa in range(2):
            (i, s, e) = eta.spans[kappa]
            chars = psi[kappa]
            assert len(chars) >= 1
            rps = prefix_sums([1 if r else 0 for (_, r) in chars])
            for b, B in enumerate(blocks):
                pos = [q for q, (ch, _) in enumerate(chars) if ch in B]
                pw = ''.join(chars[q][0] for q in pos)
                imp = Counter(); pure = Counter()
                for q in range(len(pos) - ell + 1):
                    win = pw[q:q + ell]
                    if rps[pos[q + ell - 1] + 1] - rps[pos[q]] > 0:
                        imp[win] += 1
                    else:
                        pure[win] += 1
                # 純窓 <-> phi の窓で span が U_j と交わらないもの (P1 の恒等式)
                ppos = [p for p in range(s, e) if x[i][p] in B]
                pure2 = Counter()
                for q in range(len(ppos) - ell + 1):
                    if ups[i][ppos[q + ell - 1] + 1] - ups[i][ppos[q]] == 0:
                        pure2[''.join(x[i][p] for p in ppos[q:q + ell])] += 1
                assert pure == pure2, 'P1 identity (pure windows)'
                col.append((s_ell(pw, ell), frozenset(imp.items())))
                Npsi[(kappa, b)] = pure + imp
        psi_words = [''.join(ch for (ch, _) in comp) for comp in psi]
        info[jj] = dict(I=I, ups=ups, col=tuple(col), Npsi=Npsi, psi=psi_words)
    assert info[j]['col'] == info[jp]['col'], 'colours differ'
    # Z_{kappa,b} と (i,b,J)
    Z = {}
    triples = {}
    for kappa in range(2):
        (i, s, e) = eta.spans[kappa]
        for b, B in enumerate(blocks):
            ppos = [p for p in range(s, e) if x[i][p] in B]
            z = Counter()
            for q in range(len(ppos) - ell + 1):
                a0, a1 = ppos[q], ppos[q + ell - 1] + 1
                if info[j]['ups'][i][a1] - info[j]['ups'][i][a0] == 0 and \
                   info[jp]['ups'][i][a1] - info[jp]['ups'][i][a0] > 0:
                    z[''.join(x[i][p] for p in ppos[q:q + ell])] += 1
            diff = Counter(info[j]['Npsi'][(kappa, b)])
            diff.subtract(info[jp]['Npsi'][(kappa, b)])
            assert +diff == z and all(v >= 0 for v in diff.values()), 'P1: N(psi_j)-N(psi_j\')=Z'
            assert is_circulation(z)
            if z:
                g, freq, comps = w2[(i, b)]
                Js = [J for J in comps if set(z) <= J]
                assert len(Js) == 1, 'Z not inside one frequent component'
                triples.setdefault((i, b, Js[0]), Counter()).update(z)
            Z[(kappa, b)] = z
    print('  [%s] ell=%d  eta: leaves=%d spans=%s' % (label, ell, nleaves, eta.spans))
    for (i, b, J), z in sorted(triples.items(), key=lambda t: (t[0][0], t[0][1], sorted(t[0][2]))):
        print('     hole (i=%d, block=%d, J=%s): Z=%s' % (i + 1, b + 1, sorted(J), dict(z)))
    return eta, info, triples, marks


def realizes(tup, x, state, blocks, ell):
    """tup が状態 (s_ell(pi_b x_i), alph(x_i), N_{i,b}) を実現するか。"""
    for i in range(len(x)):
        if set(tup[i]) != set(x[i]):
            return False
        for b, B in enumerate(blocks):
            p = proj(tup[i], B)
            if s_ell(p, ell) != s_ell(proj(x[i], B), ell):
                return False
            if N_ell(p, ell) != state[(i, b)]:
                return False
    return True


# ----------------------------------------------------------------------------
# 例A
# ----------------------------------------------------------------------------

def example_A(ell, M=14, f=2):
    print('例A  ell=%d  M=%d' % (ell, M))
    blocks = ('ab', 'cd')
    G, R, esc = build_grammar(M, 'A')
    fanout, rank = check_good_reduced(G)
    assert (fanout, rank) == (2, 2)
    best, ways = typed_min_table(G)
    T = (frozenset('ac'), frozenset('bd'))
    root = full_B_tree(R, M)
    evaluate(G, root)
    x = root.val
    N = 2 ** M
    assert x == ('acccc' * N, 'bbddd' * N)
    assert count_nodes(root) == 2 ** (M + 1) - 1 == best['B%d' % M][T]
    assert ways['B%d' % M][T] == 1, 'typed minimal tree must be unique'
    assign_spans(G, root, [(0, 0, len(x[0])), (1, 0, len(x[1]))])
    # E_A = [] ab []   (S -> xi1^1 xi2^1 xi1^2 (B_M, S),  S -> ab)
    def EA(t):
        return t[0] + 'ab' + t[1]
    assert in_L(EA(x))
    cs = [c_sequence(len(B), ell, f) for B in blocks]
    cstars = [c[2][c[0] + 2] for c in cs]
    cseqs = [c[2] for c in cs]
    print('  定数 c_* (ブロック別) =', cstars, ' N =', N)
    assert N > max(cstars) + 1
    j, jp = 1, 2
    eta, info, triples, marks = analyse_step(G, root, x, blocks, ell, cstars, cseqs, esc, j, jp, 'A')
    e = len(triples)
    assert e == 4 and e > f
    print('  e = %d > f = %d   (書かれたとおりの手順では代入可能性を適用できない)' % (e, f))

    # W_j, W_j'
    def W(jj):
        psi = info[jj]['psi']
        (i1, s1, e1), (i2, s2, e2) = eta.spans
        assert (i1, i2) == (0, 1)
        return EA((x[0][:s1] + psi[0] + x[0][e1:], x[1][:s2] + psi[1] + x[1][e2:]))
    Wj, Wjp = W(j), W(jp)
    assert in_L(Wj) and in_L(Wjp)
    dj, djp = data(Wj, blocks, ell), data(Wjp, blocks, ell)
    for b in range(2):                         # P1 の大域版: 型が等しく差は sum Z
        assert dj[b][0] == djp[b][0]
        diff = Counter(dict(dj[b][1])); diff.subtract(Counter(dict(djp[b][1])))
        tot = Counter()
        for (i, bb, J), z in triples.items():
            if bb == b:
                tot.update(z)
        assert +diff == tot

    # 穴語
    hole = {}
    for (i, b, J), z in triples.items():
        letter = sorted(J)[0][-1]
        u = letter * (ell - 1)
        h, t = make_hole(J, u, z, ell)
        assert h and t and set(h) == set(t) and s_ell(h, ell) == s_ell(t, ell)
        dd = N_ell(u + t, ell); dd.subtract(N_ell(u + h, ell))
        assert +dd == z
        hole[(i, b)] = (letter, h, t)

    # --- (1) 束ねない 4 穴の文脈。真部分集合の置換はすべて L の外 ---
    order = [(0, 0), (0, 1), (1, 0), (1, 1)]
    # W_j' の x_1 領域・x_2 領域 (置換片 'ab' を含む)。可換言語なので文字数だけ使う。
    (i1, s1, e1), (i2, s2, e2) = eta.spans
    Wjp_parts = (x[0][:s1] + info[jp]['psi'][0] + x[0][e1:],
                 x[1][:s2] + info[jp]['psi'][1] + x[1][e2:])

    # 置換片 (ab,ab) の文字は別に末尾へ回す (所属は文字数だけで決まる)
    extra = ''.join(ch for i in range(2) for ch in Wjp_parts[i]
                    if ch not in ('ac' if i == 0 else 'bd'))

    def W4b(choice):
        out = ''
        for (i, b), ch in zip(order, choice):
            letter, h, t = hole[(i, b)]
            n = Wjp_parts[i].count(letter)
            out += letter + (t if ch else h) + letter * (n - 1 - len(h))
            if (i, b) == (0, 1):
                out += 'ab'
        return out + extra
    allh = W4b((False,) * 4)
    assert Counter(allh) == Counter(Wjp) and in_L(allh)
    assert Counter(W4b((True,) * 4)) == Counter(Wj) and in_L(W4b((True,) * 4))
    bad = 0
    for r in range(1, 4):
        for sub in combinations(range(4), r):
            ch = tuple(q in sub for q in range(4))
            assert not in_L(W4b(ch))
            bad += 1
    print('  4穴版: 全 h, 全 t は L に入る。真部分集合 %d 通りの置換はすべて L の外。' % bad)

    # --- (2) 束ね: 根成分ごとに順位の同じ穴を連結して 2 穴にする ---
    state = {(i, b): N_ell(proj(x[i], B), ell) for i in range(2) for b, B in enumerate(blocks)}
    new_state = {k: Counter(v) for k, v in state.items()}
    for (i, b, J), z in triples.items():
        new_state[(i, b)].subtract(z)
        new_state[(i, b)] = +new_state[(i, b)]
    ypi, yprime, G_ctx = [], [], []
    for i in range(2):
        bp_t, bp_h = [], []
        for b, B in enumerate(blocks):
            letter, h, t = hole[(i, b)]
            n = x[i].count(letter)
            u0 = letter * max(ell - 1, 0)       # 頂点 u_J に着くまで
            rest = letter * (n - len(u0) - len(t))
            assert rest != ''
            bp_t.append((u0, [(t, rest)])); bp_h.append((u0, [(h, rest)]))
        pre, bt = assemble(bp_t); pre2, bh = assemble(bp_h)
        assert pre == pre2 and [s for _, s in bt] == [s for _, s in bh]
        ypi.append(fill(pre, bt)); yprime.append(fill(pre, bh))
        G_ctx.append((pre, [s for _, s in bt], [hh for hh, _ in bt], [hh for hh, _ in bh]))
    ypi, yprime = tuple(ypi), tuple(yprime)
    assert realizes(ypi, x, state, blocks, ell), 'y^pi realizes the current state'
    assert realizes(yprime, x, new_state, blocks, ell), "y' realizes state - Z"
    eprime = sum(len(g[1]) for g in G_ctx)
    assert eprime == 2 <= f
    tb = [hh for g in G_ctx for hh in g[2]]; hb = [hh for g in G_ctx for hh in g[3]]
    assert all(set(a) == set(b_) for a, b_ in zip(tb, hb)), 'bundled holes: equal content type'
    # F 側: W_j' をブロックごとに「穴 + 残り」に分解して束ねる
    bp_h, bp_t = [], []
    for b, B in enumerate(blocks):
        wb = proj(Wjp, B)
        l1, h1, t1 = hole[(0, b)]; l2, h2, t2 = hole[(1, b)]
        u0 = l1 * max(ell - 1, 0)
        assert wb.startswith(u0 + h1)
        k2 = wb.index(l2 * (ell - 1) + h2, len(proj(Wjp_parts[0], B)))   # x_2 領域の中
        k2 += ell - 1
        u1 = wb[len(u0) + len(h1):k2]; u2 = wb[k2 + len(h2):]
        assert u0 + h1 + u1 + h2 + u2 == wb and u1 and u2
        bp_h.append((u0, [(h1, u1), (h2, u2)])); bp_t.append((u0, [(t1, u1), (t2, u2)]))
    preF, bF_h = assemble(bp_h); preF2, bF_t = assemble(bp_t)
    assert [hh for hh, _ in bF_h] == hb and [hh for hh, _ in bF_t] == tb, 'same tuples on both sides'
    Fh, Ft = fill(preF, bF_h), fill(preF, bF_t)
    assert data(Fh, blocks, ell) == djp and in_L(Fh), 'F[h] has the data of W_j\''
    assert data(Ft, blocks, ell) == dj and in_L(Ft), 'F[t] has the data of W_j'
    assert all(s for _, s in bF_h)             # 区切り非空 => F in E_2
    # 文脈での同値の有限検査 (可換言語なので自明だが、機械的に確認)
    rng = random.Random(SEED + ell)
    for _ in range(200):
        v = [''.join(rng.choice('abcd') for _ in range(rng.randint(0, 6))) for _ in range(3)]
        if not v[1]:
            v[1] = rng.choice('abcd')
        vals = [in_L(v[0] + tt[0] + v[1] + tt[1] + v[2]) for tt in (x, ypi, yprime)]
        assert vals[0] == vals[1] == vals[2]
    print("  束ね後: e' = %d <= f。F[h], F[t] in L。y^pi は現在の状態、y' は状態-Z を実現。" % eprime)
    print('     束ねた穴 (h -> t):', list(zip(hb, tb)))
    return True


# ----------------------------------------------------------------------------
# 例B (縮小定数): 根が arity 1, 同じ根成分に 4 つの (1,b,J)
# ----------------------------------------------------------------------------

def example_B(ell=2, M=8, f=2, cstar_test=50):
    print('例B  ell=%d  M=%d  (c_* を検査用に %d へ縮小。理論値ではない)' % (ell, M, cstar_test))
    blocks = ('abe', 'cd')
    G, R, esc = build_grammar(M, 'B')
    fanout, rank = check_good_reduced(G)
    assert (fanout, rank) == (2, 2)
    best, ways = typed_min_table(G)
    Tfull = (frozenset('abcd'),)
    TB = (frozenset('ac'), frozenset('bd'))
    btree = full_B_tree(R, M)
    root = Node(R['C'], [btree, Node(R['Sab'])])
    evaluate(G, root)
    x = root.val
    N = 2 ** M
    assert x == ('acccc' * N + 'ab' + 'bbddd' * N,)
    assert count_nodes(root) == best['C'][Tfull] == 2 ** (M + 1) + 1
    assert ways['B%d' % M][TB] == 1
    # C_T の最小木はどれも B_M を完全二分木で使う (e を含む型は T を壊す)
    assert all('e' in (t[0] | t[1]) for t in best['B%d' % M] if t != TB)
    assign_spans(G, root, [(0, 0, len(x[0]))])
    assert in_L(x[0])                          # E_C = []  (S -> C)
    # 縮小定数: c_g の列も縮小して W2 の検査に使う
    cseq = [None, 1, 3, cstar_test, cstar_test, cstar_test, cstar_test,
            cstar_test, cstar_test, cstar_test, cstar_test, cstar_test, cstar_test]
    cseqs = [cseq, cseq]

    # W2 は縮小定数では一般に保証されないので、ここでは頻出成分を直接与える
    global w2_structure
    orig = w2_structure

    def w2_override(pword, k_b, ell_, cs):
        cnt = N_ell(pword, ell_)
        freq = {e_ for e_, c in cnt.items() if c >= cstar_test}
        assert all(c == 1 for e_, c in cnt.items() if e_ not in freq)   # 稀辺は 1 回だけ
        comps = [frozenset([e_]) for e_ in freq]                       # すべて自己ループ
        assert all(e_[0] == e_[1] for e_ in freq)
        return 2, freq, comps
    w2_structure = w2_override
    try:
        eta, info, triples, marks = analyse_step(G, root, x, blocks, ell,
                                                 [cstar_test, cstar_test], cseqs, esc, 1, 2, 'B')
    finally:
        w2_structure = orig
    assert len(triples) == 4 and {i for (i, b, J) in triples} == {0}
    print('  e = 4 > f = 2、しかも 4 つとも根成分 i=1 の中 (ブロックごとに J が 2 つ)。')
    # 束ね: ブロック b の穴を錨区間の順 (a の連 -> b の連 / c の連 -> d の連) に並べる
    hole = {}
    for (i, b, J), z in triples.items():
        letter = sorted(J)[0][-1]
        h, t = make_hole(J, letter * (ell - 1), z, ell)
        hole[letter] = (h, t)
    w = x[0]
    bp_t, bp_h = [], []
    for b, (l1, l2) in enumerate((('a', 'b'), ('c', 'd'))):
        pw = proj(w, blocks[b])
        n1, n2 = pw.count(l1), pw.count(l2)
        assert pw == l1 * n1 + l2 * n2
        (h1, t1), (h2, t2) = hole[l1], hole[l2]
        u0 = l1
        u1 = l1 * (n1 - 1 - len(t1)) + l2      # Euler 残差 + 稀辺 l1->l2 (頂点 l2 に着く)
        u2 = l2 * (n2 - 1 - len(t2))
        assert u1 and u2
        bp_t.append((u0, [(t1, u1), (t2, u2)])); bp_h.append((u0, [(h1, u1), (h2, u2)]))
    pre, bt = assemble(bp_t); _, bh = assemble(bp_h)
    ypi, yprime = fill(pre, bt), fill(pre, bh)
    state = {(0, b): N_ell(proj(w, B), ell) for b, B in enumerate(blocks)}
    new_state = {k: Counter(v) for k, v in state.items()}
    for (i, b, J), z in triples.items():
        new_state[(i, b)].subtract(z); new_state[(i, b)] = +new_state[(i, b)]
    assert realizes((ypi,), x, state, blocks, ell)
    assert realizes((yprime,), x, new_state, blocks, ell)
    assert len(bt) == 2 <= f and all(s for _, s in bt[:-1])
    assert in_L(ypi) and in_L(yprime)
    print("  束ね後: e' = 2。束ねた穴 (h -> t):", [(a, b_) for (a, _), (b_, _) in zip(bh, bt)])
    return True


# ----------------------------------------------------------------------------
# G1: P0^tensor の乱数検査
# ----------------------------------------------------------------------------

def euler_rearrange(u, ell, rng):
    """同じ s_ell, 同じ N_ell を持つ語をランダムに作る (長い語のみ変更)。"""
    m = ell - 1
    if len(u) < max(2 * m, ell) or ell == 1 and len(u) < 1:
        return u
    if ell == 1:
        lst = list(u); rng.shuffle(lst); return ''.join(lst)
    start = u[:m]
    adj = {}
    for i in range(len(u) - ell + 1):
        e = u[i:i + ell]
        adj.setdefault(e[:-1], []).append(e)
    for v in adj:
        rng.shuffle(adj[v])
    stack = [(start, None)]; out = []
    while stack:
        v, e_in = stack[-1]
        if adj.get(v):
            e = adj[v].pop(); stack.append((e[1:], e))
        else:
            stack.pop()
            if e_in is not None:
                out.append(e_in)
    out.reverse()
    res = start + ''.join(e[-1] for e in out)
    assert len(res) == len(u)
    return res


def interleave(words, rng):
    idx = [0] * len(words)
    out = []
    remaining = sum(len(w) for w in words)
    while remaining:
        choices = [b for b in range(len(words)) if idx[b] < len(words[b])]
        weights = [len(words[b]) - idx[b] for b in choices]
        b = rng.choices(choices, weights)[0]
        out.append(words[b][idx[b]]); idx[b] += 1; remaining -= 1
    return ''.join(out)


def test_G1(trials=3000):
    rng = random.Random(SEED)
    done = 0
    for _ in range(trials):
        ell = rng.choice([1, 2, 3])
        blocks = rng.choice([('ab', 'cd'), ('ab', 'c'), ('abc', 'de'), ('a', 'b', 'cd')])
        sigma = ''.join(blocks)
        d = rng.choice([1, 2, 3])
        y = [''.join(rng.choice(sigma) for _ in range(rng.randint(1, 14))) for _ in range(d)]
        yp = []
        for comp in y:
            ws = [euler_rearrange(proj(comp, B), ell, rng) for B in blocks]
            yp.append(interleave(ws, rng))
        for comp, comp2 in zip(y, yp):
            assert set(comp) == set(comp2)
            for B in blocks:
                assert s_ell(proj(comp, B), ell) == s_ell(proj(comp2, B), ell)
                assert N_ell(proj(comp, B), ell) == N_ell(proj(comp2, B), ell)
        for _ in range(5):
            v = [''.join(rng.choice(sigma) for _ in range(rng.randint(0, 4))) for _ in range(d + 1)]
            for q in range(1, d):
                if not v[q]:
                    v[q] = rng.choice(sigma)
            w1 = v[0] + ''.join(y[i] + v[i + 1] for i in range(d))
            w2 = v[0] + ''.join(yp[i] + v[i + 1] for i in range(d))
            assert data(w1, blocks, ell) == data(w2, blocks, ell)
            done += 1
    print('G1  P0^tensor: %d 個の (組, 文脈) で射影データが一致。' % done)


# ----------------------------------------------------------------------------
# G2: 穴語 h,t の乱数検査
# ----------------------------------------------------------------------------

def random_closed_walk(J, u, rng, maxlen=40):
    out = []
    v = u
    for _ in range(maxlen):
        nxt = [e for e in J if e[:-1] == v]
        e = rng.choice(nxt); out.append(e); v = e[1:]
        if v == u and rng.random() < 0.3:
            return out
    # u に戻るまで最短路で帰る
    while v != u:
        prev = {v: None}; queue = [v]
        while queue:
            a = queue.pop(0)
            for e in J:
                if e[:-1] == a and e[1:] not in prev:
                    prev[e[1:]] = e; queue.append(e[1:])
        path = []; a = u
        while prev[a] is not None:
            path.append(prev[a]); a = prev[a][:-1]
        for e in path[::-1]:
            out.append(e); v = e[1:]
    return out


def test_G2(trials=1500):
    rng = random.Random(SEED + 1)
    for _ in range(trials):
        ell = rng.choice([1, 2, 3])
        B = rng.choice(['ab', 'abc'])
        m = ell - 1
        u = ''.join(rng.choice(B) for _ in range(m))
        # ランダムな閉歩道から強連結な J を作る
        v = u; edges = []
        for _ in range(rng.randint(1, 12)):
            ch = rng.choice(B); e = v + ch; edges.append(e); v = e[1:]
        while v != u:                           # u の文字を順に読めば u に戻る
            for ch in u:
                e = v + ch; edges.append(e); v = e[1:]
        if not edges:
            edges = [u + rng.choice(B)] if ell == 1 else edges
        if not edges:
            continue
        J = frozenset(edges)
        # Z: J 内のいくつかの閉歩道の和 (基点は任意の頂点)
        Z = Counter()
        verts = sorted({e[:-1] for e in J})
        for _ in range(rng.randint(1, 3)):
            Z.update(random_closed_walk(J, rng.choice(verts), rng))
        assert is_circulation(Z)
        h, t = make_hole(J, u, Z, ell)
        assert h != '' and t != ''
        assert s_ell(h, ell) == s_ell(t, ell) and set(h) == set(t)
        dd = N_ell(u + t, ell); dd.subtract(N_ell(u + h, ell))
        assert +dd == Z and all(x_ >= 0 for x_ in dd.values())
        assert (u + h).endswith(u) and (u + t).endswith(u)   # 同じ頂点に戻る
    print('G2  穴語 h,t: %d 例で 非空・型一致・内容一致・N(t)-N(h)=Z。' % trials)


# ----------------------------------------------------------------------------
# G3: 束ね組立ての乱数検査
# ----------------------------------------------------------------------------

def test_G3(trials=3000):
    rng = random.Random(SEED + 2)
    for _ in range(trials):
        blocks = rng.choice([('ab', 'cd'), ('ab', 'cd', 'ef'), ('abc', 'de')])
        f = rng.choice([2, 3])
        d = rng.randint(1, f)
        # g_i: eta の成分のうち根成分 i に入る数。合計 <= f
        g = [0] * d
        for _ in range(rng.randint(1, f)):
            g[rng.randrange(d)] += 1
        total = 0
        for i in range(d):
            bp_t, bp_h = [], []
            for B in blocks:
                n = rng.randint(0, g[i])
                u0 = ''.join(rng.choice(B) for _ in range(rng.randint(0, 3)))
                hs_t, hs_h = [], []
                for _ in range(n):
                    alph = rng.sample(B, rng.randint(1, len(B)))
                    h = ''.join(alph) + ''.join(rng.choice(alph) for _ in range(rng.randint(0, 3)))
                    t = ''.join(alph) + ''.join(rng.choice(alph) for _ in range(rng.randint(0, 5)))
                    sep = ''.join(rng.choice(B) for _ in range(rng.randint(1, 3)))
                    hs_t.append((t, sep)); hs_h.append((h, sep))
                bp_t.append((u0, hs_t)); bp_h.append((u0, hs_h))
            pre, bt = assemble(bp_t); pre2, bh = assemble(bp_h)
            yt, yh = fill(pre, bt), fill(pre, bh)
            assert pre == pre2 and len(bt) == len(bh) <= g[i]
            for B, (u0, hs_t), (_, hs_h) in zip(blocks, bp_t, bp_h):
                assert proj(yt, B) == u0 + ''.join(a + s for a, s in hs_t)
                assert proj(yh, B) == u0 + ''.join(a + s for a, s in hs_h)
            for (a, s), (b_, s2) in zip(bt, bh):
                assert s == s2 != '' and set(a) == set(b_) and a and b_
            total += len(bt)
        assert total <= sum(g) <= f
    print("G3  束ね組立て: %d 例で 射影保存・区切り非空・内容一致・e' <= fan(eta) <= f。" % trials)


if __name__ == '__main__':
    example_A(ell=2)
    example_A(ell=1)
    example_B()
    test_G1()
    test_G2()
    test_G3()
    print('ALL CHECKS PASSED')
