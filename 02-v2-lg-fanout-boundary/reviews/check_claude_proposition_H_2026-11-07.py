#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prop_H_check.py  —  命題 H（claude_proposition_H_2026-11-07.md）の各段を、
小さな文法で実際に計算して確かめる。標準ライブラリのみ。

計算は証明の代わりにはならない。確かめる範囲は実行の最後に表示する。

使い方:
    python3 prop_H_check.py                 # 既定（seed 1, 試行数 400）
    python3 prop_H_check.py --seed 7 --trials 1000
    python3 prop_H_check.py --quick         # 短い実行

確かめること（記号は報告書に従う）:
  [A]  場合A（{a,b,c}∈𝓜 かつ g_abc−g_ab ∉ H）で、最短の ab 語 W と節点数最小の導出 T、
       全ての印の選び方について
         A1 印を含まない重い節点は全て c-強制
         A2 印を含まない重い節点は互いに比較可能（反鎖の幅 ≤ 1）
         A3 重い部分木の葉は高々3個
         A4 同じラベル・同じ印集合の祖先と子孫の組はない（短絡の補題）
         A5 c-強制の重い節点の最大反鎖 q ≤ 3（依頼の §2 の主張）
         A6 N ≤ 9(r+1)vθ
       {a,b,c}∉𝓜 の場合（A′）は印を含まない重い節点がないこと。
  [B]  ab 語の任意の導出 T について（場合を問わない部分と、場合Bだけの部分）
         B1 恒等式 π(W) = π(p₀) + Σ_z δ_z
         B2 代表の長さ |rep(B,M)| ≤ ℓ_{|M|}（ℓ0=θ, ℓ1=vθ, ℓ2=3vθ）
         B3 |p′_z| ≤ (3v+1)θ、‖δ_z‖∞ ≤ (3v+1)θ、‖p₀‖₁ ≤ 3vθ
         B4 証人 C_z[p], C_z[p′] が L に入り a と b を含む
         B5 （場合B）Φ(δ_z) ∈ H
         B6 格子補題：面 z=0 の象限での最小点 x+y ≤ 2Θ²Θ₀+8Θ²+2（実測の Θ, Θ₀）
         B7 （場合B）その最小点がオイラー路で L の ab 語として実現される
         B8 （完全な文法 L(G)=L のとき）実現した語の長さ ≥ μ_ab = |W|、かつ |W| ≤ 定理の上界
  [L]  格子補題 5.4 の単独の無作為検査（窓 [1,4K]² の中に点があれば x+y ≤ K の点がある）
"""
import argparse
import itertools
import random
import sys
from collections import defaultdict

LET = 'abc'
BIT = {'a': 1, 'b': 2, 'c': 4}
AB, ABC = 3, 7


def cont(w):
    m = 0
    for ch in w:
        m |= BIT[ch]
    return m


def parikh(w):
    return (w.count('a'), w.count('b'), w.count('c'))


def vadd(u, v):
    return tuple(x + y for x, y in zip(u, v))


def vsub(u, v):
    return tuple(x - y for x, y in zip(u, v))


# ---------------------------------------------------------------- 言語 (16)

class Inst:
    """L = {w ∈ Path_D(s,t) ∩ Σ⁺ : cont(w) ∈ 𝓜, φ(w) ∈ g_{cont(w)} + H}。
    A = Z/n, H = dZ/n（d | n）。各文字はちょうど一本の辺。"""

    def __init__(self, rng, want_case):
        self.k = rng.choice([1, 1, 2])
        self.edge = {s: (rng.randrange(self.k), rng.randrange(self.k)) for s in LET}
        self.s = rng.randrange(self.k)
        self.t = rng.randrange(self.k)
        self.n = rng.choice([2, 3, 4, 6])
        self.d = rng.choice([d for d in range(2, self.n + 1) if self.n % d == 0])
        self.phi = {s: rng.randrange(self.n) for s in LET}
        M = {AB}
        for m in range(1, 8):
            if m not in (AB, ABC) and rng.random() < 0.5:
                M.add(m)
        if want_case == 'A' or rng.random() < 0.8:
            M.add(ABC)
        self.M = M
        self.g = {m: rng.randrange(self.n) for m in M}
        if ABC in M:
            if want_case == 'A':
                while (self.g[ABC] - self.g[AB]) % self.d == 0:
                    self.g[ABC] = rng.randrange(self.n)
            else:
                self.g[ABC] = (self.g[AB] + self.d * rng.randrange(self.n // self.d)) % self.n
        self.case = 'A' if (ABC in M and (self.g[ABC] - self.g[AB]) % self.d) else 'B'

    def Phi(self, vec):
        return sum(vec[i] * self.phi[LET[i]] for i in range(3)) % self.n

    def inH(self, val):
        return val % self.d == 0

    def accepting(self, u, m, val):
        return u == self.t and m in self.M and (val - self.g[m]) % self.d == 0

    def member(self, w):
        if not w:
            return False
        cur = self.s
        for ch in w:
            tl, hd = self.edge[ch]
            if tl != cur:
                return False
            cur = hd
        return self.accepting(cur, cont(w), self.Phi(parikh(w)))


# ---------------------------------------------------------------- 文法

class Rule:
    __slots__ = ('lhs', 'kids', 'f', 'tlen', 'tcont', 'tvec')

    def __init__(self, lhs, kids, f):
        self.lhs, self.kids, self.f = lhs, list(kids), f
        ts = ''.join(it[1] for comp in f for it in comp if it[0] == 't')
        self.tlen, self.tcont, self.tvec = len(ts), cont(ts), parikh(ts)


class Grammar:
    """線形・非削除の MCFG。非終端 0 が S（ファンアウト1）。各非終端に型を持たせ、
    型が合う規則だけを作るので L(G) ⊆ L（健全）。"""

    def __init__(self):
        self.types, self.fan, self.rules, self.keys = [], [], [], set()
        self.by_type = defaultdict(list)

    def add_nt(self, tp, fan):
        self.types.append(tp)
        self.fan.append(fan)
        if tp is not None:
            self.by_type[tp].append(len(self.types) - 1)
        return len(self.types) - 1

    def add_rule(self, lhs, kids, f):
        key = (lhs, tuple(kids), repr(f))
        if key in self.keys:
            return False
        self.keys.add(key)
        self.rules.append(Rule(lhs, kids, f))
        return True


def out_type(inst, G, kids, f):
    comps, m, val = [], 0, 0
    for b in kids:
        _, cm, cv = G.types[b]
        m |= cm
        val += cv
    for comp in f:
        cur = start = None
        for it in comp:
            if it[0] == 't':
                se = inst.edge[it[1]]
                m |= BIT[it[1]]
                val += inst.phi[it[1]]
            else:
                se = G.types[kids[it[1]]][0][it[2]]
            if cur is None:
                start = se[0]
            elif cur != se[0]:
                return None
            cur = se[1]
        comps.append((start, cur))
    return (tuple(comps), m, val % inst.n)


def rand_body(rng, G, kids, fan_out, tmin=0, tmax=2):
    items = [('v', j, i) for j, b in enumerate(kids) for i in range(G.fan[b])]
    items += [('t', rng.choice(LET)) for _ in range(rng.randint(tmin, tmax))]
    if not items:
        return None
    rng.shuffle(items)
    if fan_out == 2:
        if len(items) < 2:
            return None
        cut = rng.randint(1, len(items) - 1)
        return [items[:cut], items[cut:]]
    return [items]


def gen_grammar(inst, rng, vmax, rmax, steps, complete):
    G = Grammar()
    G.add_nt(None, 1)  # S
    if complete:
        # 接頭辞の文法：状態 q=(頂点, 内容, 値) ごとに P_q。L(G) = L になる。
        st = {}
        frontier = []
        for ch in LET:
            tl, hd = inst.edge[ch]
            if tl == inst.s:
                q = (hd, BIT[ch], inst.phi[ch] % inst.n)
                if q not in st:
                    st[q] = G.add_nt((((inst.s, hd),), q[1], q[2]), 1)
                    frontier.append(q)
                G.add_rule(st[q], [], [[('t', ch)]])
        while frontier:
            q = frontier.pop()
            u, m, val = q
            for ch in LET:
                tl, hd = inst.edge[ch]
                if tl != u:
                    continue
                q2 = (hd, m | BIT[ch], (val + inst.phi[ch]) % inst.n)
                if q2 not in st:
                    st[q2] = G.add_nt((((inst.s, hd),), q2[1], q2[2]), 1)
                    frontier.append(q2)
                G.add_rule(st[q2], [st[q]], [[('v', 0, 0), ('t', ch)]])
        for q, x in st.items():
            if inst.accepting(*q):
                G.add_rule(0, [x], [[('v', 0, 0)]])
    else:
        for _ in range(3 * vmax):
            fo = rng.choice([1, 2])
            f = rand_body(rng, G, [], fo, 1, 3)
            if f is None:
                continue
            tp = out_type(inst, G, [], f)
            if tp is None:
                continue
            lhs = (rng.choice(G.by_type[tp]) if tp in G.by_type and
                   (rng.random() < 0.6 or len(G.types) >= vmax) else
                   (G.add_nt(tp, fo) if len(G.types) < vmax else None))
            if lhs is not None:
                G.add_rule(lhs, [], f)
    limit = len(G.types) + vmax
    for _ in range(steps):
        if len(G.types) < 2:
            break
        k = rng.randint(1, rmax)
        kids = [rng.randrange(1, len(G.types)) for _ in range(k)]
        fo = rng.choice([1, 2])
        f = rand_body(rng, G, kids, fo)
        if f is None:
            continue
        tp = out_type(inst, G, kids, f)
        if tp is None:
            continue
        if tp in G.by_type and (rng.random() < 0.7 or len(G.types) >= limit):
            lhs = rng.choice(G.by_type[tp])
        elif len(G.types) < limit:
            lhs = G.add_nt(tp, fo)
        else:
            continue
        G.add_rule(lhs, kids, f)
    # S の規則
    for x in range(1, len(G.types)):
        segs, m, val = G.types[x]
        if segs == ((inst.s, inst.t),) and inst.accepting(inst.t, m, val) and rng.random() < 0.7:
            G.add_rule(0, [x], [[('v', 0, 0)]])
    for _ in range(4 * vmax):
        if len(G.types) < 2:
            break
        k = rng.randint(1, rmax)
        kids = [rng.randrange(1, len(G.types)) for _ in range(k)]
        f = rand_body(rng, G, kids, 1)
        if f is None:
            continue
        tp = out_type(inst, G, kids, f)
        if tp and tp[0] == ((inst.s, inst.t),) and inst.accepting(inst.t, tp[1], tp[2]):
            G.add_rule(0, kids, f)
    return reduce_grammar(G)


BAD = 'BAD'


def profile_out(inst, kidprofs, f):
    """子の像（成分ごとの端点・内容・値）から規則の出力の像を計算する。路でなければ BAD。"""
    m, val = 0, 0
    for p in kidprofs:
        if p == BAD:
            return BAD
        m |= p[1]
        val += p[2]
    comps = []
    for comp in f:
        cur = start = None
        for it in comp:
            if it[0] == 't':
                se = inst.edge[it[1]]
                m |= BIT[it[1]]
                val += inst.phi[it[1]]
            else:
                se = kidprofs[it[1]][0][it[2]]
            if cur is None:
                start = se[0]
            elif cur != se[0]:
                return BAD
            cur = se[1]
        comps.append((start, cur))
    return (tuple(comps), m, val % inst.n)


def profiles(inst, G, prof=None):
    """各非終端の生成の像の集合（不動点）。prof を与えればそこから単調に広げる。"""
    prof = {b: set(s) for b, s in prof.items()} if prof else defaultdict(set)
    prof = defaultdict(set, prof)
    ch = True
    while ch:
        ch = False
        for R in G.rules:
            sets = [prof[b] for b in R.kids]
            if any(not s for s in sets):
                continue
            for combo in itertools.product(*sets):
                p = profile_out(inst, combo, R.f)
                if p not in prof[R.lhs]:
                    prof[R.lhs].add(p)
                    ch = True
    return prof


def sound_S(inst, prof):
    return all(p != BAD and p[0] == ((inst.s, inst.t),) and inst.accepting(inst.t, p[1], p[2])
               for p in prof[0])


def gen_mixed(inst, rng, vmax, rmax, steps, complete):
    """非終端が複数の内容・値を混ぜて持てる文法。規則を一本ずつ足し、S の像が全て受理なら残す
    （従って L(G) ⊆ L）。complete なら接頭辞の文法から始める（L(G) = L）。"""
    if complete:
        G = gen_grammar(inst, rng, vmax, rmax, 0, True)
        if G is None:
            return None
        # gen_grammar は型付きの印を付けるが、ここでは使わない
    else:
        G = Grammar()
        G.add_nt(None, 1)
        for _ in range(vmax - 1):
            fo = rng.choice([1, 1, 2])
            b = G.add_nt(None, fo)
            for _ in range(rng.randint(1, 2)):
                f = rand_body(rng, G, [], fo, max(1, fo), 2)
                if f:
                    G.add_rule(b, [], f)
    prof = profiles(inst, G)
    if not sound_S(inst, prof):
        return None
    nts = len(G.types)
    for _ in range(steps):
        lhs = rng.randrange(0, nts) if rng.random() < 0.25 else rng.randrange(1, nts)
        k = rng.randint(1, rmax)
        kids = [rng.randrange(1, nts) for _ in range(k)]
        f = rand_body(rng, G, kids, G.fan[lhs], 0, 2)
        if f is None or len(f) != G.fan[lhs]:
            continue
        if not G.add_rule(lhs, kids, f):
            continue
        new = profiles(inst, G, prof)
        if sound_S(inst, new) and sum(len(s) for s in new.values()) < 400:
            prof = new
        else:
            G.rules.pop()
            G.keys.discard((lhs, tuple(kids), repr(f)))
    return reduce_grammar(G)


def gen_chain(rng):
    """μ_ab が θ より長くなりやすい族：c 入りの短い逃げ道を持つ鎖（ファンアウト1と2）を
    一本か二本作り、S で結ぶ。無作為な規則を少し足す。D は一頂点。
    言語 (16) は後で像から決める（L(G) ⊆ L）。"""
    G = Grammar()
    G.add_nt(None, 1)

    def rw(lo, hi, need_c=False, alpha='ab'):
        w = [rng.choice(alpha) for _ in range(rng.randint(lo, hi))]
        if need_c:
            w[rng.randrange(len(w))] = 'c'
        return w

    def body_from(words):
        return [[('t', ch) for ch in w] for w in words]

    tops, allc = [], []
    for ci in range(rng.choice([1, 2, 2])):
        m = rng.randint(2, 6)
        fo = rng.choice([1, 2])
        alpha = rng.choice(['ab', 'a', 'b'])
        chain = [G.add_nt(None, fo) for _ in range(m + 1)]
        allc += chain
        G.add_rule(chain[0], [], body_from([rw(1, 2, alpha=alpha) for _ in range(fo)]))
        for j in range(1, m + 1):
            if fo == 1:
                items = [('v', 0, 0)] + [('t', ch) for ch in rw(1, 2, alpha=alpha)]
                if rng.random() < 0.5:
                    items = items[1:] + items[:1]
                f = [items]
            else:
                l, r_ = rw(0, 1, alpha=alpha), rw(1, 1, alpha=alpha)
                f = [[('t', ch) for ch in l] + [('v', 0, 0)],
                     [('v', 0, 1)] + [('t', ch) for ch in r_]]
                if rng.random() < 0.3:
                    f = [f[1], f[0]]
            G.add_rule(chain[j], [chain[j - 1]], f)
            if rng.random() < 0.85:  # 逃げ道
                G.add_rule(chain[j], [], body_from([rw(1, 2, need_c=(i == 0)) for i in range(fo)]))
        tops.append(chain[m])
    items = [('t', ch) for ch in rw(0, 1)]
    for j, b in enumerate(tops):
        items += [('v', j, i) for i in range(G.fan[b])]
    rng.shuffle(items)
    G.add_rule(0, tops, [items])
    for _ in range(rng.randint(0, 4)):
        lhs = rng.choice(allc)
        k = rng.randint(1, 2)
        kids = [rng.choice(allc) for _ in range(k)]
        f = rand_body(rng, G, kids, G.fan[lhs], 0, 1)
        if f and len(f) == G.fan[lhs]:
            G.add_rule(lhs, kids, f)
    return reduce_grammar(G)


def inst_from_grammar(rng, G, want=None):
    """一頂点の D と無作為な φ: Σ→Z/n を取り、S の像から 𝓜, g, H（最小）を決める。
    want を与えればその場合になる φ を何度か探す。"""
    for _ in range(30):
        inst = _inst_from_grammar(rng, G)
        if want is None or inst.case == want:
            break
    return inst


def _inst_from_grammar(rng, G):
    from math import gcd
    inst = Inst.__new__(Inst)
    inst.k = 1
    inst.edge = {s: (0, 0) for s in LET}
    inst.s = inst.t = 0
    inst.n = rng.choice([2, 3, 4, 5, 6, 8, 12])
    inst.phi = {s: rng.randrange(inst.n) for s in LET}
    inst.d = inst.n
    inst.M, inst.g = set(), {}
    prof = profiles(inst, G)
    byc = defaultdict(set)
    for p in prof[0]:
        byc[p[1]].add(p[2])
    d = inst.n
    for m, vals in byc.items():
        vals = sorted(vals)
        for x in vals:
            d = gcd(d, (x - vals[0]) % inst.n)
    inst.d = d if d else inst.n
    inst.M = set(byc)
    inst.g = {m: min(vals) for m, vals in byc.items()}
    inst.case = 'A' if (ABC in inst.M and AB in inst.M and
                        (inst.g[ABC] - inst.g[AB]) % inst.d) else 'B'
    return inst


def reduce_grammar(G):
    # 生成的：子が全て生成的な規則を持つ非終端（不動点）
    prod = set()
    ch = True
    while ch:
        ch = False
        for R in G.rules:
            if R.lhs not in prod and all(b in prod for b in R.kids):
                prod.add(R.lhs)
                ch = True
    if 0 not in prod:
        return None
    rules = [R for R in G.rules if R.lhs in prod and all(b in prod for b in R.kids)]
    reach = {0}
    stack = [0]
    while stack:
        a = stack.pop()
        for R in rules:
            if R.lhs == a:
                for b in R.kids:
                    if b not in reach:
                        reach.add(b)
                        stack.append(b)
    keep = sorted(reach)
    ren = {a: i for i, a in enumerate(keep)}
    H = Grammar()
    for a in keep:
        H.add_nt(G.types[a], G.fan[a])
    for R in rules:
        if R.lhs in reach:
            H.add_rule(ren[R.lhs], [ren[b] for b in R.kids], R.f)
    return H


# ---------------------------------------------------------------- 最短の導出（内容ごと）

def dp(G):
    """best[(B,C)] = (長さ, 節点数, 規則番号, 子の内容) を辞書式最小で。C は正確な内容。"""
    best = {}
    have = defaultdict(set)
    changed = True
    while changed:
        changed = False
        for ri, R in enumerate(G.rules):
            opts = [sorted(have[b]) for b in R.kids]
            if any(not o for o in opts):
                continue
            for combo in itertools.product(*opts):
                L, N, C = R.tlen, 1, R.tcont
                for b, cb in zip(R.kids, combo):
                    e = best[(b, cb)]
                    L += e[0]
                    N += e[1]
                    C |= cb
                key = (R.lhs, C)
                if key not in best or (L, N) < best[key][:2]:
                    best[key] = (L, N, ri, combo)
                    have[R.lhs].add(C)
                    changed = True
    return best


class Node:
    __slots__ = ('ri', 'kids')

    def __init__(self, ri, kids):
        self.ri, self.kids = ri, kids


def build(G, best, B, C):
    _, _, ri, combo = best[(B, C)]
    R = G.rules[ri]
    return Node(ri, [build(G, best, b, cb) for b, cb in zip(R.kids, combo)])


def ev(G, nd, subst=None):
    """成分の列。各文字に、それを書いた節点を付ける。subst は {id(節点): 置き換える木}。"""
    if subst and id(nd) in subst:
        nd = subst[id(nd)]
    R = G.rules[nd.ri]
    kv = [ev(G, k, subst) for k in nd.kids]
    out = []
    for comp in R.f:
        s = []
        for it in comp:
            if it[0] == 't':
                s.append((it[1], nd))
            else:
                s.extend(kv[it[1]][it[2]])
        out.append(s)
    return out


def word(G, nd, subst=None):
    return ''.join(ch for ch, _ in ev(G, nd, subst)[0])


def ylen(G, nd):
    return sum(len(c) for c in ev(G, nd))


def yvec(G, nd):
    s = ''.join(ch for c in ev(G, nd) for ch, _ in c)
    return parikh(s)


def walk(nd, parent, out, par):
    out.append(nd)
    par[id(nd)] = parent
    for k in nd.kids:
        walk(k, nd, out, par)


def params(G, best):
    v = len(G.types)
    r = max(len(R.kids) for R in G.rules)
    tau = {}
    for (b, c), e in best.items():
        tau[b] = min(tau.get(b, 10 ** 9), e[0])
    theta = max(R.tlen + sum(tau[b] for b in R.kids) for R in G.rules)
    return v, r, tau, theta


# ---------------------------------------------------------------- 格子

def hnf(vecs):
    """列の順 (z, x, y) の階段形。返り値は (主列, 行) の列。行は (z, x, y) の順。"""
    rows = [[v[2], v[0], v[1]] for v in vecs if any(v)]
    out = []
    for c in range(3):
        while True:
            nz = [i for i, r in enumerate(rows) if r[c] != 0]
            if not nz:
                break
            pi = min(nz, key=lambda i: abs(rows[i][c]))
            piv = rows[pi]
            rest = []
            for i, r in enumerate(rows):
                if i == pi:
                    continue
                if r[c] != 0:
                    q = r[c] // piv[c]
                    r = [r[j] - q * piv[j] for j in range(3)]
                if any(r):
                    rest.append(r)
            if all(r[c] == 0 for r in rest):
                if piv[c] < 0:
                    piv = [-x for x in piv]
                out.append((c, piv))
                rows = rest
                break
            rows = rest + [piv]
    return out


def in_lattice(H, t):
    t = [t[2], t[0], t[1]]
    for c, row in H:
        if t[c] % row[c]:
            return False
        q = t[c] // row[c]
        t = [t[j] - q * row[j] for j in range(3)]
    return not any(t)


def plane_points(gens, p0, W):
    """(p0+Λ) ∩ {z=0} ∩ [1,W]² の点を全て返す。"""
    H = hnf(gens)
    P = [p0[2], p0[0], p0[1]]  # (z,x,y)
    plane = []
    for c, row in H:
        if c == 0:
            if P[0] % row[0]:
                return []
            q = -P[0] // row[0]
            P = [P[j] + q * row[j] for j in range(3)]
        else:
            plane.append((c, row))
    if P[0] != 0:
        return []
    x0, y0 = P[1], P[2]
    pts = []
    xr = [r for c, r in plane if c == 1]
    yr = [r for c, r in plane if c == 2]
    e, f = (xr[0][1], xr[0][2]) if xr else (None, None)
    g = yr[0][2] if yr else None
    if e is None:
        xs = [(0, x0)] if 1 <= x0 <= W else []
    else:
        a_lo = -((x0 - 1) // e)
        a_hi = (W - x0) // e
        xs = [(a, x0 + a * e) for a in range(a_lo, a_hi + 1)]
    for a, x in xs:
        yb = y0 + (a * f if e is not None else 0)
        if g is None:
            if 1 <= yb <= W:
                pts.append((x, yb))
        else:
            b_lo = -((yb - 1) // g)
            for b in range(b_lo, b_lo + W // g + 2):
                y = yb + b * g
                if y > W:
                    break
                if y >= 1:
                    pts.append((x, y))
    return pts


def lemma_K(Th, Th0):
    return 2 * Th * Th * Th0 + 8 * Th * Th + 2


def euler_word(inst, x, y):
    """辺 a を x 本、辺 b を y 本使う s→t の路（Hierholzer）。なければ None。"""
    adj = defaultdict(list)
    for ch, cnt in (('a', x), ('b', y)):
        tl, hd = inst.edge[ch]
        adj[tl].extend([(ch, hd)] * cnt)
    stack, out = [(None, inst.s)], []
    while stack:
        ch, u = stack[-1]
        if adj[u]:
            stack.append(adj[u].pop())
        else:
            stack.pop()
            if ch:
                out.append(ch)
    w = ''.join(reversed(out))
    if len(w) != x + y:
        return None
    cur = inst.s
    for c in w:
        if inst.edge[c][0] != cur:
            return None
        cur = inst.edge[c][1]
    return w if cur == inst.t else None


# ---------------------------------------------------------------- 検査

class Stats:
    def __init__(self):
        self.c = defaultdict(int)
        self.viol = []
        self.mx = defaultdict(float)

    def ok(self, name, cond, info=''):
        self.c[name + ' 検査'] += 1
        if not cond:
            self.viol.append((name, info))

    def note(self, name, x):
        self.mx[name] = max(self.mx[name], x)


def check_A(inst, G, best, T, S, rng):
    v, r, tau, th = params(G, best)
    nodes, par = [], {}
    walk(T, None, nodes, par)
    lab = {id(z): G.rules[z.ri].lhs for z in nodes}
    yl = {id(z): ylen(G, z) for z in nodes}
    heavy = {id(z) for z in nodes if yl[id(z)] > th}
    cfree_min = {}
    for (b, c), e in best.items():
        if not c & 4:
            cfree_min[b] = min(cfree_min.get(b, 10 ** 9), e[0])
    cforced = {b: cfree_min.get(b, 10 ** 9) > th for b in range(len(G.types))}
    Wl = ev(G, T)[0]
    N = len(Wl)

    def anc(z):
        s = []
        while z is not None:
            s.append(id(z))
            z = par[id(z)]
        return s

    ancset = {id(z): set(anc(z)) for z in nodes}
    pa = [i for i, (ch, _) in enumerate(Wl) if ch == 'a']
    pb = [i for i, (ch, _) in enumerate(Wl) if ch == 'b']
    pairs = [(i, j) for i in pa for j in pb]
    if len(pairs) > 40:
        pairs = rng.sample(pairs, 40)
    S.ok('A6 N ≤ 9(r+1)vθ', N <= 9 * (r + 1) * v * th, (N, r, v, th))
    S.note('A6 N/(9(r+1)vθ)', N / (9 * (r + 1) * v * th))
    nontriv = False
    for ia, ib in pairs:
        Ma = set(anc(Wl[ia][1]))
        Mb = set(anc(Wl[ib][1]))
        M = {id(z): (1 if id(z) in Ma else 0) | (2 if id(z) in Mb else 0) for z in nodes}
        mf = [z for z in nodes if id(z) in heavy and M[id(z)] == 0]
        if mf:
            nontriv = True
        S.ok('A1 印なしの重い節点は c-強制', all(cforced[lab[id(z)]] for z in mf))
        if inst.case == 'A':
            comp = all(id(x) in ancset[id(y)] or id(y) in ancset[id(x)]
                       for x, y in itertools.combinations(mf, 2))
            S.ok('A2 印なしの重い節点は比較可能（場合A）', comp)
            hl = [z for z in nodes if id(z) in heavy and not any(id(k) in heavy for k in z.kids)]
            S.ok('A3 重い葉 ≤ 3（場合A）', len(hl) <= 3, len(hl))
            S.note('A3 重い葉の数', len(hl))
            cf = {id(z) for z in nodes if id(z) in heavy and cforced[lab[id(z)]]}

            def ach(z):
                s = sum(ach(k) for k in z.kids)
                return max(s, 1 if id(z) in cf else 0)

            q = ach(T)
            S.ok('A5 q ≤ 3（場合A）', q <= 3, q)
            S.note('A5 q', q)
        if ABC not in inst.M:
            S.ok("A′ {a,b,c}∉𝓜 なら印なしの重い節点なし", not mf)
        bad = False
        for y in nodes:
            for z in nodes:
                if z is not y and id(y) in ancset[id(z)] and lab[id(y)] == lab[id(z)] \
                        and M[id(y)] == M[id(z)]:
                    bad = True
        S.ok('A4 同ラベル・同印集合の祖先子孫なし', not bad)
    if nontriv:
        S.c['A 印なしの重い節点がある例（場合%s）' % inst.case] += 1


def rep_tree(G, best, B, Mbits):
    cands = [(best[(B, C)][:2], C) for C in range(1, 8) if (B, C) in best and C & Mbits == Mbits]
    if not cands:
        return None
    return build(G, best, B, min(cands)[1])


def check_B(inst, G, best, T, S, complete):
    v, r, tau, th = params(G, best)
    nodes, par = [], {}
    walk(T, None, nodes, par)
    Wl = ev(G, T)[0]
    W = ''.join(ch for ch, _ in Wl)
    ia = next(i for i, (ch, _) in enumerate(Wl) if ch == 'a')
    ib = next(i for i, (ch, _) in enumerate(Wl) if ch == 'b')

    def anc(z):
        s = set()
        while z is not None:
            s.add(id(z))
            z = par[id(z)]
        return s

    Ma, Mb = anc(Wl[ia][1]), anc(Wl[ib][1])
    M = {id(z): (1 if id(z) in Ma else 0) | (2 if id(z) in Mb else 0) for z in nodes}
    ell = {0: th, 1: v * th, 2: 3 * v * th}
    reps = {}

    def rep(B, Mb_):
        if (B, Mb_) not in reps:
            reps[(B, Mb_)] = rep_tree(G, best, B, Mb_)
        return reps[(B, Mb_)]

    p0 = rep(0, AB)
    p0v = yvec(G, p0)
    S.ok('B3 ‖p₀‖₁ ≤ 3vθ', sum(p0v) <= 3 * v * th, (sum(p0v), v, th))
    S.ok('B5 Φ(p₀) ∈ g_ab+H（場合B）', inst.case != 'B' or
         (inst.Phi(p0v) - inst.g[AB]) % inst.d == 0)
    tot = p0v
    gens = set()
    Th = 0
    for z in nodes:
        R = G.rules[z.ri]
        Mz = M[id(z)]
        nb = bin(Mz).count('1')
        p = rep(R.lhs, Mz)
        pp = Node(z.ri, [rep(R.kids[j], M[id(k)]) for j, k in enumerate(z.kids)])
        lp, lpp = ylen(G, p), ylen(G, pp)
        S.ok('B2 |rep(B,M)| ≤ ℓ_|M|', lp <= ell[nb], (lp, nb, v, th))
        S.note('B2 |rep|/ℓ', lp / ell[nb])
        S.ok("B3 |p′| ≤ (3v+1)θ", lpp <= (3 * v + 1) * th, (lpp, v, th))
        d = vsub(yvec(G, pp), yvec(G, p))
        Th = max(Th, max(abs(x) for x in d))
        gens.add(d)
        tot = vadd(tot, d)
        w1 = word(G, T, {id(z): p})
        w2 = word(G, T, {id(z): pp})
        S.ok('B4 証人が L に入り a,b を含む',
             inst.member(w1) and inst.member(w2) and cont(w1) & AB == AB and cont(w2) & AB == AB,
             (w1, w2))
        if inst.case == 'B':
            S.ok('B5 Φ(δ_z) ∈ H（場合B）', inst.inH(inst.Phi(d)), d)
        else:
            if not inst.inH(inst.Phi(d)):
                S.c['（参考）場合Aで Φ(δ_z) ∉ H となった節点'] += 1
    S.ok('B1 恒等式 π(W)=π(p₀)+Σδ', tot == parikh(W), (tot, parikh(W)))
    S.ok("B3 ‖δ‖∞ ≤ (3v+1)θ", Th <= (3 * v + 1) * th)
    Th = max(Th, 1)
    Th0 = sum(p0v)
    K = lemma_K(Th, Th0)
    Kthm = lemma_K((3 * v + 1) * th, 3 * v * th)
    gens = list(gens)
    pts = plane_points(gens, p0v, max(len(W), K) + 2)
    S.ok('B6 π(W) は p₀+Λ の面の点', (parikh(W)[0], parikh(W)[1]) in set(pts))
    if not pts:
        return
    xm, ym = min(pts, key=lambda q: q[0] + q[1])
    Hh = hnf(gens)
    S.ok('B6 最小点の所属（別法）', in_lattice(Hh, vsub((xm, ym, 0), p0v)))
    S.ok('B6 最小点 x+y ≤ 2Θ²Θ₀+8Θ²+2（実測）', xm + ym <= K, (xm + ym, Th, Th0))
    S.ok('B6 最小点 x+y ≤ 定理の上界', xm + ym <= Kthm)
    S.note('B6 (x+y)/K（実測）', (xm + ym) / K)
    if inst.case == 'B':
        w = euler_word(inst, xm, ym)
        S.ok('B7 最小点が L の ab 語として実現', w is not None and inst.member(w) and cont(w) == AB,
             (xm, ym, w))
        if complete and w is not None:
            S.ok('B8 実現した語の長さ ≥ μ_ab=|W|', len(w) >= len(W), (len(w), len(W)))
        if complete:
            S.ok('B8 μ_ab ≤ 定理の上界', len(W) <= max(9 * (r + 1) * v * th, Kthm))
            S.note('B8 μ_ab / (226v³θ³)', len(W) / (226 * v ** 3 * th ** 3))
    if complete and inst.case == 'A':
        S.ok('B8 μ_ab ≤ 9(r+1)vθ（場合A）', len(W) <= 9 * (r + 1) * v * th)


def lemma_stress(rng, trials, S):
    for _ in range(trials):
        Th = rng.randint(1, 4)
        Th0 = rng.randint(0, 6)
        ng = rng.randint(1, 4)
        gens = [tuple(rng.randint(-Th, Th) for _ in range(3)) for _ in range(ng)]
        gens = [g for g in gens if any(g)]
        if not gens:
            continue
        Thr = max(max(abs(x) for x in g) for g in gens)
        # ‖p0‖₁ ≤ Th0
        p0 = [0, 0, 0]
        for _ in range(Th0):
            i = rng.randrange(3)
            p0[i] += rng.choice([-1, 1])
        p0 = tuple(p0)
        Th0r = sum(abs(x) for x in p0)
        K = lemma_K(Thr, Th0r)
        pts = plane_points(gens, p0, 4 * K)
        if not pts:
            continue
        S.c['L 窓の中に点がある例'] += 1
        m = min(x + y for x, y in pts)
        S.ok('L 格子補題 5.4（窓 [1,4K]²）', m <= K, (gens, p0, m, K))
        S.note('L 最小 x+y / K', m / K)
        S.note('L 最小 x+y / (Θ²(Θ₀+1))', m / (Thr * Thr * (Th0r + 1)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--trials', type=int, default=400)
    ap.add_argument('--quick', action='store_true')
    a = ap.parse_args()
    rng = random.Random(a.seed)
    trials = 60 if a.quick else a.trials
    S = Stats()
    used = defaultdict(int)
    maxv = maxr = maxth = maxN = 0
    for it in range(trials):
        want = 'A' if it % 2 == 0 else 'B'
        mode = (it // 2) % 6          # 0 型付き健全, 1 混合健全, 2 型付き完全, 3 混合完全, 4-5 鎖
        complete = mode in (2, 3)
        inst = Inst(rng, want)
        if mode >= 4:
            G = gen_chain(rng)
            if G is None:
                continue
            inst = inst_from_grammar(rng, G, want)
        elif mode in (1, 3):
            inst.k = 1 if rng.random() < 0.8 else inst.k
            if inst.k == 1:
                inst.edge = {s: (0, 0) for s in LET}
                inst.s = inst.t = 0
            G = gen_mixed(inst, rng, vmax=rng.randint(3, 7), rmax=rng.randint(1, 2),
                          steps=rng.randint(40, 160), complete=complete)
        else:
            G = gen_grammar(inst, rng, vmax=rng.randint(4, 9), rmax=rng.randint(1, 3),
                            steps=rng.randint(30, 120), complete=complete)
        if G is None:
            continue
        gkind = ['typed', 'mixed', 'typed', 'mixed', 'chain', 'chain'][mode] + \
            ('-complete' if complete else '-sound')
        best = dp(G)
        if (0, AB) not in best:
            continue
        T = build(G, best, 0, AB)
        v, r, _, th = params(G, best)
        maxv, maxr, maxth = max(maxv, v), max(maxr, r), max(maxth, th)
        maxN = max(maxN, best[(0, AB)][0])
        used[(inst.case, gkind)] += 1
        if ylen(G, T) > 60:
            continue
        check_A(inst, G, best, T, S, rng)
        check_B(inst, G, best, T, S, complete)
    lemma_stress(rng, 3000 if not a.quick else 300, S)

    print('== 命題 H の計算機による確認（seed=%d, 試行=%d）==' % (a.seed, trials))
    print('使った実例（場合, 文法の種類）:', dict(used))
    print('範囲: v ≤ %d, r ≤ %d, θ ≤ %d, μ_ab ≤ %d；A = Z/n (n ≤ 12), |V_D| ≤ 2' %
          (maxv, maxr, maxth, maxN))
    for k in sorted(S.c):
        print('  %-48s %d' % (k, S.c[k]))
    print('観測した最大値:')
    for k in sorted(S.mx):
        print('  %-48s %.4f' % (k, S.mx[k]))
    if S.viol:
        print('違反 %d 件。最初の5件:' % len(S.viol))
        for x in S.viol[:5]:
            print('  ', x)
        sys.exit(1)
    print('違反なし。')


if __name__ == '__main__':
    main()
