#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fable_three_stages_2026-11-11.py
報告 fable_three_stages_2026-11-11.md の検査スクリプト（Python 3、標準ライブラリのみ）。

規約
- 乱数の種は固定（20261111）。
- 無限の言語についての主張は報告書の中で手で証明する。有界な検査は反例探しと照合のためだけに使う。
- 「違反」として出力する語の四つ組は、必ず真の所属述語 member() で判定し直す。
- StageLang、criterion などの部品は前回のスクリプト（2026-11-10）と同じもの。

節
 S1  隣接する段の対による被覆（補題 M* の組合せ部分）
 S2  系 M*（有限指数）：SUB_d なら、d 個の隣接対で覆える S の上で面の格子が一致する
 S3  Ex2 の族 Ex2^0_m：所属、文法、厚さ、tau、定理 B の上界
 S4  定理 B の対比：段が一文字の H(n) と、同じ段に二文字ある G1(n)
"""
import itertools
import math
import random
import time

random.seed(20261111)


# ----------------------------------------------------------------------------
# 0. 言語の記述と定理1 の判定条件（前回と同じ）
# ----------------------------------------------------------------------------
class StageLang:
    """クラス K の言語。cond(M) は内容 M の条件のリスト [(重み, 法, 剰余)]。
    法 0 は等式を表す。cond(M) が None なら M は受理されない内容。"""

    def __init__(self, name, letters, stage, cond):
        self.name = name
        self.letters = letters
        self.k = len(letters)
        self.stage = stage
        self.idx = {a: i for i, a in enumerate(letters)}
        self.faces = {}
        for r in range(1, self.k + 1):
            for M in itertools.combinations(letters, r):
                c = cond(frozenset(M))
                if c is not None:
                    self.faces[frozenset(M)] = c

    def accept(self, m):
        M = frozenset(a for a, x in zip(self.letters, m) if x > 0)
        c = self.faces.get(M)
        if c is None:
            return False
        for w, mod, res in c:
            v = sum(w.get(a, 0) * x for a, x in zip(self.letters, m))
            if mod == 0:
                if v != res:
                    return False
            elif (v - res) % mod:
                return False
        return True

    def in_lattice(self, M, h):
        for w, mod, _res in self.faces[M]:
            v = sum(w.get(a, 0) * x for a, x in zip(self.letters, h))
            if mod == 0:
                if v != 0:
                    return False
            elif v % mod:
                return False
        return True

    def nd(self, w):
        s = [self.stage[c] for c in w]
        return all(s[i] <= s[i + 1] for i in range(len(s) - 1))

    def parikh(self, w):
        return tuple(w.count(a) for a in self.letters)

    def member(self, w):
        return len(w) > 0 and self.nd(w) and self.accept(self.parikh(w))


def nd_words(lang, L):
    res, frontier = [], ['']
    for _ in range(L):
        new = []
        for w in frontier:
            last = lang.stage[w[-1]] if w else -1
            for a in lang.letters:
                if lang.stage[a] >= last:
                    new.append(w + a)
        res += new
        frontier = new
    return res


def factorizations(w, d):
    """w = v0 x1 v1 ... xd vd。x_i は空でなく、内側の v_i も空でない。"""
    n = len(w)

    def rec(i, start, xs, vs):
        if i == d:
            yield tuple(xs), tuple(vs + [w[start:]])
            return
        lo = start if i == 0 else start + 1
        for p in range(lo, n):
            for q in range(p + 1, n + 1):
                yield from rec(i + 1, q, xs + [w[p:q]], vs + [w[start:p]])

    yield from rec(0, 0, [], [])


def fill(ctx, x):
    s = ctx[0]
    for xi, v in zip(x, ctx[1:]):
        s += xi + v
    return s


def typ(x):
    return tuple(frozenset(c) for c in x)


def brute_sub(lang, d, L):
    """長さ L 以下の文から SUB_d の違反 (E, F, x, y) を探す。
    E[x], E[y], F[x] は L に入り、F[y] は入らない（全て member で判定）。"""
    words = [w for w in nd_words(lang, L) if lang.member(w)]
    D, byctx = {}, {}
    for w in words:
        for x, E in factorizations(w, d):
            D.setdefault(x, set()).add(E)
            byctx.setdefault((E, typ(x)), []).append(x)
    for (E, _T), xs in byctx.items():
        x0 = xs[0]
        for y in xs[1:]:
            for F in D[x0]:
                if not lang.member(fill(F, y)):
                    return (E, F, x0, y)
            for F in D[y]:
                if not lang.member(fill(F, x0)):
                    return (E, F, y, x0)
    return None


def check_certificate(lang, cert):
    E, F, x, y = cert
    return (lang.member(fill(E, x)) and lang.member(fill(E, y))
            and lang.member(fill(F, x)) and not lang.member(fill(F, y)))


# ----------------------------------------------------------------------------
# 1. 定理1 の判定条件（全ての法が正の場合の厳密な形）
# ----------------------------------------------------------------------------
def type_info(lang, T):
    los = [min(lang.stage[a] for a in M) for M in T]
    his = [max(lang.stage[a] for a in M) for M in T]
    d = len(T)
    for i in range(d - 1):
        if his[i] > los[i + 1]:
            return None
    J = frozenset().union(*T)
    b = tuple(sum(1 for M in T if a in M) for a in lang.letters)
    pos = {}
    for a in lang.letters:
        s = lang.stage[a]
        P = []
        if s <= los[0]:
            P.append(0)
        for i in range(1, d):
            if his[i - 1] <= s <= los[i]:
                P.append(i)
        if s >= his[d - 1]:
            P.append(d)
        pos[a] = P
    return J, b, pos


def place_inner(lang, e, pos, d):
    """内側の区切り 1..d-1 に文字を一つずつ置けるか。置ければ残りと配置を返す。"""
    rem = list(e)
    slots = [[] for _ in range(d + 1)]

    def rec(i):
        if i == d:
            return True
        for j, a in enumerate(lang.letters):
            if rem[j] > 0 and i in pos[a]:
                rem[j] -= 1
                slots[i].append(a)
                if rec(i + 1):
                    return True
                slots[i].pop()
                rem[j] += 1
        return False

    if not rec(1):
        return None
    return rem, slots


def build_ctx(lang, e, pos, d):
    rem, slots = place_inner(lang, e, pos, d)
    for j, a in enumerate(lang.letters):
        if rem[j] > 0:
            slots[pos[a][0]] += [a] * rem[j]
    key = lambda a: (lang.stage[a], a)
    return tuple(''.join(sorted(s, key=key)) for s in slots)


def build_tuple(lang, T, n):
    rem = list(n)
    comps = [[] for _ in T]
    for i, M in enumerate(T):
        for a in M:
            comps[i].append(a)
            rem[lang.idx[a]] -= 1
    for j, a in enumerate(lang.letters):
        if rem[j] > 0:
            i = next(i for i, M in enumerate(T) if a in M)
            comps[i] += [a] * rem[j]
    assert min(rem) >= 0
    key = lambda a: (lang.stage[a], a)
    return tuple(''.join(sorted(c, key=key)) for c in comps)


def criterion(lang, d, Lcm):
    """定理1（有限指数の形）：全ての型 T（arity d）、n、M, M' in Acc_T(n) について
    N_M ∩ Z^J = N_M' ∩ Z^J。破れていれば証人を返す。"""
    letters, k = lang.letters, lang.k
    contents = [frozenset(c) for r in range(1, k + 1)
                for c in itertools.combinations(letters, r)]
    top = Lcm if d <= 2 else 2 * Lcm
    for T in itertools.product(contents, repeat=d):
        info = type_info(lang, T)
        if info is None:
            continue
        J, b, pos = info
        faces = [M for M in lang.faces if J <= M]
        if len(faces) < 2:
            continue
        Jidx = [i for i, a in enumerate(letters) if a in J]
        ranges = [range(0, top + 1) if pos[a] else range(0, 1) for a in letters]
        es = []
        for e in itertools.product(*ranges):
            if d > 1 and place_inner(lang, e, pos, d) is None:
                continue
            M = J | frozenset(a for a, x in zip(letters, e) if x > 0)
            if M in lang.faces:
                es.append((e, M))
        if not es:
            continue
        latt = {}
        for M in faces:
            S = set()
            for hJ in itertools.product(range(Lcm), repeat=len(Jidx)):
                h = [0] * k
                for i, v in zip(Jidx, hJ):
                    h[i] = v
                if lang.in_lattice(M, h):
                    S.add(tuple(h))
            latt[M] = S
        for nJ in itertools.product(range(Lcm), repeat=len(Jidx)):
            n = list(b)
            for i, v in zip(Jidx, nJ):
                n[i] += v
            acc = {}
            for e, M in es:
                if M not in acc and lang.accept(tuple(x + y for x, y in zip(e, n))):
                    acc[M] = e
            Ms = list(acc)
            for M1 in Ms:
                for M2 in Ms:
                    diff = latt[M1] - latt[M2]
                    if diff:
                        return dict(T=T, n=tuple(n), M1=M1, M2=M2, h=min(diff),
                                    e1=acc[M1], e2=acc[M2], pos=pos)
    return None


def witness_to_certificate(lang, wit):
    T, n, h, pos = wit['T'], wit['n'], wit['h'], wit['pos']
    d = len(T)
    x = build_tuple(lang, T, n)
    y = build_tuple(lang, T, tuple(a + c for a, c in zip(n, h)))
    E = build_ctx(lang, wit['e1'], pos, d)
    F = build_ctx(lang, wit['e2'], pos, d)
    return (E, F, x, y)


def show(M):
    return ''.join(sorted(M))


# ----------------------------------------------------------------------------
# S1. 隣接する段の対による被覆
# ----------------------------------------------------------------------------
def pairs_needed(stages):
    """段の集合を {u,u+1} の形の対で覆うのに必要な対の最小数（貪欲で最適）。"""
    st = sorted(set(stages))
    cnt, i = 0, 0
    while i < len(st):
        if i + 1 < len(st) and st[i + 1] == st[i] + 1:
            i += 2
        else:
            i += 1
        cnt += 1
    return cnt


def section1():
    print('=' * 78)
    print('S1  隣接する段の対による被覆（補題 M*）')
    print('=' * 78)
    for t in range(1, 8):
        row = []
        for d in (1, 2, 3):
            bad = [S for r in range(1, t + 1)
                   for S in itertools.combinations(range(1, t + 1), r)
                   if pairs_needed(S) > d]
            minimal = [S for S in bad
                       if not any(set(B) < set(S) for B in bad)]
            row.append((d, len(bad), minimal[:4]))
        print('  t=%d:' % t, ' / '.join(
            'd=%d 覆えない集合 %d 個%s' % (d, n, ('（極小: %s）' % mn) if n else '')
            for d, n, mn in row))
    print('  （t ≤ 2d なら覆えない集合は 0 個。d=2 では t=5 の {1,3,5} が最初の例）')


# ----------------------------------------------------------------------------
# S2. 系 M*：SUB_d なら d 対で覆える S の上で格子が一致
# ----------------------------------------------------------------------------
def rank_stage(stage):
    vals = sorted(set(stage.values()))
    return {a: vals.index(s) + 1 for a, s in stage.items()}


def agree(lang, M1, M2, S, Lcm):
    idx = [lang.idx[a] for a in S]
    for hs in itertools.product(range(Lcm), repeat=len(idx)):
        h = [0] * lang.k
        for i, v in zip(idx, hs):
            h[i] = v
        if lang.in_lattice(M1, h) != lang.in_lattice(M2, h):
            return False
    return True


def lattice_table(lang, Lcm, dmax=2):
    """SUB_1..SUB_dmax の判定と、面の対・部分集合 S ごとの一致の表。"""
    rk = rank_stage(lang.stage)
    ok = {}
    prev = True
    for d in range(1, dmax + 1):
        prev = prev and criterion(lang, d, Lcm) is None
        ok[d] = prev
    rows = []
    for M1, M2 in itertools.combinations(list(lang.faces), 2):
        I = sorted(M1 & M2)
        for r in range(1, len(I) + 1):
            for S in itertools.combinations(I, r):
                rows.append((M1, M2, S, pairs_needed([rk[a] for a in S]),
                             agree(lang, M1, M2, S, Lcm)))
    return ok, rows


def ex2_family(m, res):
    """段 a<b<c<d<e。面 ace: i≡j≡l≡res (m)。面 abcde: i≡j≡l (m)。"""
    def cond(M):
        if M == frozenset('ace'):
            return [({'a': 1}, m, res), ({'c': 1}, m, res), ({'e': 1}, m, res)]
        if M == frozenset('abcde'):
            return [({'a': 1, 'c': -1}, m, 0), ({'c': 1, 'e': -1}, m, 0)]
        return None
    return StageLang('Ex2^%d_%d' % (res, m), 'abcde',
                     {c: i + 1 for i, c in enumerate('abcde')}, cond)


def section2():
    print('=' * 78)
    print('S2  系 M*（有限指数）の検査')
    print('=' * 78)

    def cond1(M):
        if M == frozenset('ac'):
            return [({'a': 1, 'c': 1}, 2, 0)]
        if M == frozenset('abc'):
            return [({'a': 1}, 2, 1), ({'c': 1}, 2, 1)]
        return None
    ex1 = StageLang('Ex1', 'abc', {'a': 1, 'b': 2, 'c': 3}, cond1)
    named = [(ex1, 2), (ex2_family(2, 1), 2), (ex2_family(2, 0), 2), (ex2_family(3, 0), 3)]
    for lang, Lcm in named:
        ok, rows = lattice_table(lang, Lcm)
        dis = [(show(M1), show(M2), ''.join(S), p) for M1, M2, S, p, ag in rows if not ag]
        print('  %-8s SUB_1=%s SUB_1&2=%s  格子が一致しない (面,面,S,必要な対の数): %s'
              % (lang.name, ok[1], ok[2], dis))
        for d in (1, 2):
            if ok[d]:
                assert all(ag for _, _, _, p, ag in rows if p <= d)
    # 語の段階の照合（Ex2^0_2）
    e20 = ex2_family(2, 0)
    print('  Ex2^0_2 語の段階（長さ≤11）: arity1 違反 %s / arity2 違反 %s'
          % (brute_sub(e20, 1, 11), brute_sub(e20, 2, 11)))
    cert = (('', 'b', 'd', ''), ('a', 'c', 'e', ''), ('a', 'c', 'e'), ('aa', 'cc', 'ee'))
    print('  Ex2^0_2 arity3 の証明書 E=□b□d□, F=a□c□e□, x=(a,c,e), y=(aa,cc,ee):',
          check_certificate(e20, cert))

    # ランダムな例
    letters = 'abcde'
    contents = [frozenset(c) for r in range(2, 6) for c in itertools.combinations(letters, r)]
    stats = {}
    brute = {'checked': 0, 'viol': 0}
    N = 0
    t0 = time.time()
    while N < 4000:
        t = random.choice((2, 3, 4, 5))
        cuts = sorted(random.sample(range(1, 5), t - 1))
        stage, s = {}, 1
        for i, a in enumerate(letters):
            if i in cuts:
                s += 1
            stage[a] = s
        mod = random.choice((2, 2, 3))
        table = {}
        base = random.choice(contents)
        fs = [base]
        for _ in range(random.randint(1, 2)):
            if random.random() < 0.5:
                extra = [a for a in letters if a not in base]
                if extra:
                    fs.append(base | frozenset(random.sample(extra, random.randint(1, len(extra)))))
                    continue
            fs.append(random.choice(contents))
        for M in fs:
            cs = []
            for _ in range(random.randint(0, 3)):
                w = {a: random.randint(0, mod - 1) for a in sorted(M)}
                cs.append((w, mod, random.randint(0, mod - 1)))
            table[M] = cs
        lang = StageLang('rnd', letters, stage, lambda M: table.get(M))
        for M in list(lang.faces):
            if not any(lang.accept(m) for m in itertools.product(range(mod + 2), repeat=5)
                       if frozenset(a for a, x in zip(letters, m) if x > 0) == M):
                del lang.faces[M]
        if len(lang.faces) < 2:
            continue
        N += 1
        ok, rows = lattice_table(lang, mod)
        for d in (1, 2):
            if not ok[d]:
                continue
            for _, _, S, p, ag in rows:
                key = (t, d, 'covered' if p <= d else 'not covered', 'agree' if ag else 'DISAGREE')
                stats[key] = stats.get(key, 0) + 1
        if ok[2] and rows and brute['checked'] < 25:
            brute['checked'] += 1
            if brute_sub(lang, 1, 6) is not None or brute_sub(lang, 2, 6) is not None:
                brute['viol'] += 1
    print('  ランダムな例 %d 個（k=5、t=2..5、法 2 か 3）。(t, d, 被覆, 一致) ごとの (面の対, S) の数:' % N)
    for key in sorted(stats):
        print('   ', key, stats[key])
    bad = sum(v for k, v in stats.items() if k[2] == 'covered' and k[3] == 'DISAGREE')
    print('  「覆えるのに一致しない」の数 = %d（系 M* が正しければ 0）' % bad)
    print('  判定条件で SUB_1・SUB_2 が成り立つ例のうち最初の %d 個を語の段階（長さ≤6、arity 1,2）で検査: 違反 %d'
          % (brute['checked'], brute['viol']))
    print('  （%.1f 秒）' % (time.time() - t0))


# ----------------------------------------------------------------------------
# S3. Ex2 の族：文法、厚さ、tau
# ----------------------------------------------------------------------------
def build_dfa(m):
    """Ex2^0_m の決定性オートマトン（到達可能かつ受理に届く状態だけ、最小化済み）。"""
    letters = 'abcde'
    st = {c: i for i, c in enumerate(letters)}
    start = ('s', 0, 0, 0, 0, 0)

    def step(q, x):
        ph, i, j, l, hb, hd = q
        if ph != 's' and st[x] < st[ph]:
            return None
        if x == 'a':
            return ('a', (i + 1) % m, j, l, hb, hd)
        if x == 'b':
            return ('b', i, j, l, 1, hd)
        if x == 'c':
            return ('c', i, (j + 1) % m, l, hb, hd)
        if x == 'd':
            return ('d', i, j, l, hb, 1)
        return ('e', i, j, (l + 1) % m, hb, hd)

    def acc(q):
        ph, i, j, l, hb, hd = q
        if ph != 'e':
            return False
        if hb and hd:
            return i == j == l
        if not hb and not hd:
            return i == j == l == 0
        return False

    # 文字 a, c, e を全て含むことは ph の進み方では保証されないので、個数 0 を区別する
    def step2(q, x):
        base, seen = q
        nb = step(base, x)
        if nb is None:
            return None
        return (nb, seen | {x})

    def acc2(q):
        base, seen = q
        return acc(base) and {'a', 'c', 'e'} <= seen and \
            (seen == {'a', 'c', 'e'} or seen == set(letters))

    start2 = (start, frozenset())
    reach, frontier = {start2}, [start2]
    trans = {}
    while frontier:
        q = frontier.pop()
        for x in letters:
            n = step2(q, x)
            if n is None:
                continue
            n = (n[0], frozenset(n[1]))
            trans[(q, x)] = n
            if n not in reach:
                reach.add(n)
                frontier.append(n)
    # 受理に届く状態
    good = {q for q in reach if acc2(q)}
    changed = True
    while changed:
        changed = False
        for (q, x), n in trans.items():
            if n in good and q not in good:
                good.add(q)
                changed = True
    states = sorted(good, key=repr)
    # Moore の最小化
    part = {q: (1 if acc2(q) else 0) for q in states}
    while True:
        sig = {q: (part[q], tuple(part.get(trans.get((q, x))) if trans.get((q, x)) in good else None
                                  for x in letters)) for q in states}
        ids = {}
        new = {q: ids.setdefault(sig[q], len(ids)) for q in states}
        if len(ids) == len(set(part.values())):
            part = new
            break
        part = new
    nst = len(set(part.values()))
    delta, final = {}, set()
    for q in states:
        if acc2(q):
            final.add(part[q])
        for x in letters:
            n = trans.get((q, x))
            if n in good:
                delta[(part[q], x)] = part[n]
    return part[start2], nst, delta, final


def dfa_accepts(dfa, w):
    q0, _n, delta, final = dfa
    q = q0
    for c in w:
        q = delta.get((q, c))
        if q is None:
            return False
    return q in final


def section3():
    print('=' * 78)
    print('S3  Ex2 の族 Ex2^0_m：L = {a^i c^j e^l : i≡j≡l≡0 (m)} ∪ {a^i b^+ c^j d^+ e^l : i≡j≡l (m)}')
    print('=' * 78)
    letters = 'abcde'
    k, f, r = 5, 1, 1
    print('  右線形文法（最小 DFA から。非終端 = 状態、規則 q -> x q\' と q -> x）。f=1, r=1。')
    print('  %3s %5s %6s %7s %9s %10s %12s %14s' %
          ('m', 'v', '規則', 'thick', 'mu_ace', 'max tau', '定理Bの上界', 'SUB_1&2(判定)'))
    for m in (2, 3, 4, 5, 6, 8):
        lang = ex2_family(m, 0)
        dfa = build_dfa(m)
        q0, nst, delta, final = dfa
        # L(G) = L の有界な照合（長さ ≤ Lb。先頭 4 文字は任意、その後は段非減少に伸ばした語）
        Lb = 9 if m <= 3 else 8
        mism = 0
        frontier = ['']
        for _ in range(Lb):
            frontier = [w + c for w in frontier for c in letters
                        if (not w) or lang.stage[c] >= lang.stage[w[-1]] or len(w) < 4]
            for w in frontier:
                if dfa_accepts(dfa, w) != lang.member(w):
                    mism += 1
        # 長い語の照合（ND な語を乱数で）
        for _ in range(3000):
            cnt = [random.randint(0, 3 * m) for _ in letters]
            w = ''.join(c * n for c, n in zip(letters, cnt))
            if w and dfa_accepts(dfa, w) != lang.member(w):
                mism += 1
        # 距離
        INF = 10 ** 9
        dist = {q0: 0}
        frontier = [q0]
        while frontier:
            nf = []
            for q in frontier:
                for x in letters:
                    n = delta.get((q, x))
                    if n is not None and n not in dist:
                        dist[n] = dist[q] + 1
                        nf.append(n)
            frontier = nf
        togo = {q: 0 for q in final}
        changed = True
        while changed:
            changed = False
            for (q, x), n in delta.items():
                if n in togo and togo[n] + 1 < togo.get(q, INF):
                    togo[q] = togo[n] + 1
                    changed = True
        nrules, thick = 0, 0
        for (q, x), n in delta.items():
            nrules += 1                      # q -> x n
            thick = max(thick, dist[q] + 1 + togo[n])
            if n in final:
                nrules += 1                  # q -> x
                thick = max(thick, dist[q] + 1)
        # tau: 型付き非終端 (q, M) ごとに、q から受理される内容ちょうど M の最短の語
        # （決定性なので、文脈 u□（u は q に届く語）を共有する語の全体が q の言語。
        #   SUB_1 の下で、これが同値類になる）
        best = {}
        start_items = [(q, frozenset()) for q in range(nst)]
        seen = set(start_items)
        layer = [(q, q, frozenset()) for q in range(nst)]
        length = 0
        while layer:
            length += 1
            nl = []
            for src, q, M in layer:
                for x in letters:
                    n = delta.get((q, x))
                    if n is None:
                        continue
                    M2 = M | {x}
                    if (src, n, M2) in seen:
                        continue
                    seen.add((src, n, M2))
                    if n in final and (src, M2) not in best:
                        best[(src, M2)] = length
                    nl.append((src, n, M2))
            layer = nl
        tau = max(best.values())
        mu_ace = best[(q0, frozenset('ace'))]
        theta = max(1, thick)
        D = nst * (2 ** k - 1) ** f
        boundB = 2 * f * k * D * (1 + r) * theta
        if m <= 3:
            s12 = criterion(lang, 1, m) is None and criterion(lang, 2, m) is None
        else:
            s12 = '(手の証明)'
        assert mism == 0
        assert tau <= boundB
        print('  %3d %5d %6d %7d %9d %10d %12d %14s' %
              (m, nst, nrules, thick, mu_ace, tau, boundB, s12))
    print('  L(G) = L の照合：長さ ≤ 8〜9 の語（先頭 4 文字は任意、その後は ND）と、乱数の長い ND な語 3000 個で不一致 0。')
    print('  tau は m について一次、文法の大きさは m の二次。超多項式ではない。')


# ----------------------------------------------------------------------------
# S4. 定理 B の対比
# ----------------------------------------------------------------------------
def shortest_typed(rules, letters):
    """CFG（ファンアウト 1）。rules: {A: [右辺のリスト]}、右辺は記号の列。
    best[(A, M)] = A から導出される、内容がちょうど M の最短の語の長さ。"""
    best = {}
    changed = True
    while changed:
        changed = False
        for A, rhss in rules.items():
            for rhs in rhss:
                opts = [{(frozenset(), 0)}]
                cur = {frozenset(): 0}
                for X in rhs:
                    nxt = {}
                    if X in rules:
                        items = [(M, l) for (B, M), l in best.items() if B == X]
                    else:
                        items = [(frozenset(X), 1)]
                    for M0, l0 in cur.items():
                        for M1, l1 in items:
                            M2 = M0 | M1
                            if l0 + l1 < nxt.get(M2, 10 ** 18):
                                nxt[M2] = l0 + l1
                    cur = nxt
                for M, l in cur.items():
                    if l < best.get((A, M), 10 ** 18):
                        best[(A, M)] = l
                        changed = True
    return best


def cfg_thickness(rules, start):
    inside = {}
    changed = True
    while changed:
        changed = False
        for A, rhss in rules.items():
            for rhs in rhss:
                if all((X not in rules) or X in inside for X in rhs):
                    l = sum(inside[X] if X in rules else 1 for X in rhs)
                    if l < inside.get(A, 10 ** 18):
                        inside[A] = l
                        changed = True
    outside = {start: 0}
    changed = True
    while changed:
        changed = False
        for A, rhss in rules.items():
            if A not in outside:
                continue
            for rhs in rhss:
                tot = sum(inside[X] if X in rules else 1 for X in rhs)
                for X in rhs:
                    if X in rules:
                        o = outside[A] + tot - inside[X]
                        if o < outside.get(X, 10 ** 18):
                            outside[X] = o
                            changed = True
    th = 0
    for A, rhss in rules.items():
        for rhs in rhss:
            th = max(th, outside[A] + sum(inside[X] if X in rules else 1 for X in rhs))
    return th


def section4():
    print('=' * 78)
    print('S4  定理 B の対比：型付き非終端 (A_n, {a}) の最短の生成語')
    print('=' * 78)
    print('  H(n)  : S -> A_n c,  A_i -> A_{i-1} A_{i-1} | a,  A_0 -> aa   （段 a<c、各段一文字）')
    print('  G1(n) : S -> b A_n,  A_i -> A_{i-1} A_{i-1} | c,  A_0 -> aa   （段 b<{a,c}、a と c が同じ段）')
    print('  %3s | %5s %6s %14s %12s | %5s %6s %14s' %
          ('n', 'v', 'thick', '最短(A_n,{a})', '定理Bの上界', 'v', 'thick', '最短(A_n,{a})'))
    for n in range(1, 9):
        out = []
        for kind in ('H', 'G1'):
            rules = {'A0': [['a', 'a']]}
            for i in range(1, n + 1):
                rules['A%d' % i] = [['A%d' % (i - 1), 'A%d' % (i - 1)], ['a' if kind == 'H' else 'c']]
            rules['S'] = [['A%d' % n, 'c']] if kind == 'H' else [['b', 'A%d' % n]]
            best = shortest_typed(rules, 'abc')
            th = cfg_thickness(rules, 'S')
            out.append((len(rules), th, best[('A%d' % n, frozenset('a'))]))
        (v1, th1, s1), (v2, th2, s2) = out
        k, f, r = 2, 1, 2
        boundB = 2 * f * k * (v1 * (2 ** k - 1) ** f) * (1 + r) * max(1, th1)
        assert s1 <= boundB
        print('  %3d | %5d %6d %14d %12d | %5d %6d %14d' % (n, v1, th1, s1, boundB, v2, th2, s2))
    print('  H(n) では最短の生成語が定数、G1(n) では 2^(n+1)。定理 B は「各段一文字」を本当に使う。')
    print('  （G1(n) でも代表は aa で tau = 2。これは前回の報告の S3 の結果）')


if __name__ == '__main__':
    t0 = time.time()
    section1()
    section2()
    section3()
    section4()
    print('=' * 78)
    print('完了（%.1f 秒）' % (time.time() - t0))
