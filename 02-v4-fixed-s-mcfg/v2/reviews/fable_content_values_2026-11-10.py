#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fable_content_values_2026-11-10.py
報告 fable_content_values_2026-11-10.md の検査スクリプト（Python 3、標準ライブラリのみ）。

規約
- 乱数の種は固定（20261110）。
- 無限の言語の所属は報告書の中で手で証明する。ここでの有界な検査は反例を探すためだけに使う。
- 「違反」として出力する語の四つ組は、必ず真の所属述語 member() で判定し直す。
- 有限の集合（T_n、F_4、E_1、F_n）は全数で検査する。

節
 S1  定理1（所属の判定条件）と語の段階の有界な検査の照合、例 Ex1・Ex2・T_n
 S2  補題 O'（しきい値つきの象限内短縮）の数値検査
 S3  定理 A の上界と、小さな文法での分布代表
 S4  課題3：F_4、E_1、F_n での格子と飽和の欠け
"""
import itertools
import math
import random
from fractions import Fraction

random.seed(20261110)


# ----------------------------------------------------------------------------
# 0. 言語の記述
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


class FiniteParikhLang:
    """一頂点（t=1）のパリク飽和な言語 π^{-1}(Q)、Q は有限集合。"""

    def __init__(self, name, letters, Q):
        self.name = name
        self.letters = letters
        self.k = len(letters)
        self.stage = {a: 1 for a in letters}
        self.Q = set(Q)

    def parikh(self, w):
        return tuple(w.count(a) for a in self.letters)

    def member(self, w):
        return len(w) > 0 and self.parikh(w) in self.Q


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


def section1():
    print('=' * 78)
    print('S1  定理1 の判定条件と語の段階の検査')
    print('=' * 78)

    # --- 例 Ex1：段 a<b<c。SUB_1 は成り立ち SUB_2 は破れる ---
    def cond1(M):
        if M == frozenset('ac'):
            return [({'a': 1, 'c': 1}, 2, 0)]
        if M == frozenset('abc'):
            return [({'a': 1}, 2, 1), ({'c': 1}, 2, 1)]
        return None
    ex1 = StageLang('Ex1', 'abc', {'a': 1, 'b': 2, 'c': 3}, cond1)
    c1, c2 = criterion(ex1, 1, 2), criterion(ex1, 2, 2)
    print('Ex1  L = {a^i c^l : i≡l (2)} ∪ {a^i b^j c^l : i, l 奇数}（段 a<b<c）')
    print('  判定条件 arity1:', 'OK' if c1 is None else '破れ',
          '/ arity2:', 'OK' if c2 is None else '破れ')
    cert = witness_to_certificate(ex1, c2)
    print('  arity2 の証人: 型', [show(M) for M in c2['T']], 'n', c2['n'], 'h', c2['h'],
          '面', show(c2['M1']), show(c2['M2']))
    print('  四つ組 (E,F,x,y) =', cert, ' 真の述語で確認:', check_certificate(ex1, cert))
    hand = (('', 'ac', ''), ('', 'b', ''), ('a', 'c'), ('aa', 'cc'))
    print('  手の証明書 E=□ac□, F=□b□, x=(a,c), y=(aa,cc):', check_certificate(ex1, hand))
    print('  語の段階（長さ≤9）arity1 の違反:', brute_sub(ex1, 1, 9))
    b2 = brute_sub(ex1, 2, 9)
    print('  語の段階（長さ≤9）arity2 の違反:', b2, '確認:', check_certificate(ex1, b2))

    # --- 例 Ex2：段 a<b<c<d<e。SUB_1, SUB_2 は成り立ち SUB_3 は破れる ---
    def cond2(M):
        if M == frozenset('ace'):
            return [({'a': 1}, 2, 1), ({'c': 1}, 2, 1), ({'e': 1}, 2, 1)]
        if M == frozenset('abcde'):
            return [({'a': 1, 'c': 1}, 2, 0), ({'c': 1, 'e': 1}, 2, 0)]
        return None
    ex2 = StageLang('Ex2', 'abcde', {c: i for i, c in enumerate('abcde')}, cond2)
    c1, c2 = criterion(ex2, 1, 2), criterion(ex2, 2, 2)
    print('Ex2  L = {a^i c^j e^l : 全て奇数} ∪ {a^i b^+ c^j d^+ e^l : i≡j≡l (2)}（段 a<b<c<d<e）')
    print('  判定条件 arity1:', 'OK' if c1 is None else '破れ',
          '/ arity2:', 'OK' if c2 is None else '破れ')
    hand3 = (('', 'b', 'd', ''), ('', 'aa', 'cc', ''), ('a', 'c', 'e'), ('aa', 'cc', 'ee'))
    print('  arity3 の手の証明書 E=□b□d□, F=□aa□cc□, x=(a,c,e), y=(aa,cc,ee):',
          check_certificate(ex2, hand3))
    print('  語の段階（長さ≤11）arity1 の違反:', brute_sub(ex2, 1, 11))
    print('  語の段階（長さ≤11）arity2 の違反:', brute_sub(ex2, 2, 11))
    b3 = brute_sub(ex2, 3, 11)
    print('  語の段階（長さ≤11）arity3 の違反:', b3, '確認:',
          None if b3 is None else check_certificate(ex2, b3))

    # --- T_n は K に入る（剰余類の形）ことの全数検査と、SUB の語の段階の検査 ---
    print('T_n（閉包報告の例2.8）: Q_M = Π_M ∩ (q + <Q_M - Q_M>) の全数検査')
    for n in (1, 2, 3):
        Q2 = [(1 + 3 * n, 1, 0), (1, 1 + 3 * n, 0)]
        Q3 = [(3, 2, 1), (1, 3, 2), (2, 1, 3)]
        ok = True
        for Qm, supp in ((Q2, (1, 1, 0)), (Q3, (1, 1, 1))):
            basis = echelon([tuple(a - b for a, b in zip(q, Qm[0])) for q in Qm[1:]])
            box = 3 * n + 8
            sat = set()
            for m in itertools.product(range(box), repeat=3):
                if tuple(1 if x > 0 else 0 for x in m) != supp:
                    continue
                if in_lat(tuple(a - b for a, b in zip(m, Qm[0])), basis):
                    sat.add(m)
            ok = ok and sat == set(Qm)
        lang = FiniteParikhLang('T%d' % n, 'abc', Q2 + Q3)
        L = 3 * n + 2
        v1 = brute_sub(lang, 1, L) if n <= 2 else 'skip'
        v2 = brute_sub(lang, 2, L) if n <= 1 else 'skip'
        print('  n=%d: 剰余類の形（箱 %d）=%s, (T)=%s, 語の段階 arity1 違反=%s, arity2 違反=%s'
              % (n, box, ok, check_T(set(Q2 + Q3)), v1, v2))

    # --- ランダムな K の例で、判定条件と語の段階の検査を照合 ---
    print('ランダムな例（k=3、段はランダム、法は 2,3）: 判定条件 vs 語の段階（長さ≤7）')
    stats = {'crit_fail_cert_ok': 0, 'crit_fail_cert_bad': 0,
             'crit_ok_brute_none': 0, 'crit_ok_brute_viol': 0}
    samples = 0
    letters = 'abc'
    stage_choices = [{'a': 1, 'b': 1, 'c': 1}, {'a': 1, 'b': 1, 'c': 2},
                     {'a': 1, 'b': 2, 'c': 2}, {'a': 1, 'b': 2, 'c': 3},
                     {'a': 1, 'b': 2, 'c': 1}]
    contents = [frozenset(c) for r in range(1, 4) for c in itertools.combinations(letters, r)]
    while samples < 60:
        stage = random.choice(stage_choices)
        table = {}
        mods = set()
        for M in contents:
            if random.random() < 0.6:
                cs = []
                for _ in range(random.randint(0, 2)):
                    mod = random.choice((2, 3))
                    w = {a: random.randint(0, mod - 1) for a in M}
                    cs.append((w, mod, random.randint(0, mod - 1)))
                    mods.add(mod)
                table[M] = cs
        lang = StageLang('rnd', letters, stage, lambda M: table.get(M))
        # 空の面を除く
        for M in list(lang.faces):
            if not any(lang.accept(m) for m in itertools.product(range(8), repeat=3)
                       if frozenset(a for a, x in zip(letters, m) if x > 0) == M):
                del lang.faces[M]
        if len(lang.faces) < 2:
            continue
        samples += 1
        Lcm = 1
        for m in mods:
            Lcm = Lcm * m // math.gcd(Lcm, m)
        for d in (1, 2):
            wit = criterion(lang, d, Lcm)
            if wit is not None:
                cert = witness_to_certificate(lang, wit)
                if check_certificate(lang, cert):
                    stats['crit_fail_cert_ok'] += 1
                else:
                    stats['crit_fail_cert_bad'] += 1
            else:
                viol = brute_sub(lang, d, 7)
                if viol is None:
                    stats['crit_ok_brute_none'] += 1
                else:
                    stats['crit_ok_brute_viol'] += 1
    print('  例の数 %d（各 arity 1,2）:' % samples, stats)
    print('  （crit_fail_cert_bad と crit_ok_brute_viol が 0 なら定理1 と整合）')


# ----------------------------------------------------------------------------
# 整数格子の道具
# ----------------------------------------------------------------------------
def echelon(gens):
    gens = [list(g) for g in gens if any(g)]
    if not gens:
        return []
    ncol = len(gens[0])
    rows, basis = gens, []
    for col in range(ncol):
        while True:
            nz = [r for r in rows if r[col] != 0]
            if len(nz) <= 1:
                break
            nz.sort(key=lambda r: abs(r[col]))
            p = nz[0]
            for r in nz[1:]:
                q = r[col] // p[col]
                for i in range(ncol):
                    r[i] -= q * p[i]
        nz = [r for r in rows if r[col] != 0]
        if nz:
            basis.append(nz[0])
            rows = [r for r in rows if r is not nz[0]]
        rows = [r for r in rows if any(r)]
    return basis


def in_lat(v, basis):
    v = list(v)
    for p in basis:
        c = next(i for i, x in enumerate(p) if x)
        if any(v[i] for i in range(c)):
            return False
        if v[c] % p[c]:
            return False
        q = v[c] // p[c]
        v = [a - q * b for a, b in zip(v, p)]
    return not any(v)


def rank(rows):
    rows = [[Fraction(x) for x in r] for r in rows]
    rk = 0
    ncol = len(rows[0]) if rows else 0
    for col in range(ncol):
        piv = next((i for i in range(rk, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i][col] != 0:
                f = rows[i][col] / rows[rk][col]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[rk])]
        rk += 1
    return rk


def check_T(Q):
    """有限の Q について条件 (T) を全数で検査する（厳密）。"""
    Q = set(Q)
    for q in Q:
        for q2 in Q:
            if q == q2:
                continue
            if tuple(x > 0 for x in q) != tuple(x > 0 for x in q2):
                continue
            h = tuple(b - a for a, b in zip(q, q2))
            lo = tuple(max(-x, 0) + (1 if x else 0) for x in h)   # h^- + 1_S
            hi = tuple(max(x, 0) + (1 if x else 0) for x in h)    # h^+ + 1_S
            for al in Q:
                if all(a >= l for a, l in zip(al, lo)):
                    if tuple(a + x for a, x in zip(al, h)) not in Q:
                        return False
                if all(a >= l for a, l in zip(al, hi)):
                    if tuple(a - x for a, x in zip(al, h)) not in Q:
                        return False
    return True


# ----------------------------------------------------------------------------
# 2. 補題 O'
# ----------------------------------------------------------------------------
def find_z(D, I, k, h, B):
    R = math.factorial(max(h - 1, 0)) * B ** max(h - 1, 0)
    for lam in itertools.product(range(-R, R + 1), repeat=h):
        if not any(lam):
            continue
        z = [sum(lam[j] * D[j][i] for j in range(h)) for i in range(k)]
        if any(z) and all(z[i] == 0 for i in range(k) if i not in I):
            return z
    return None


def section2():
    print('=' * 78)
    print('S2  補題 O\'（しきい値 T1 つき）の数値検査')
    print('=' * 78)
    k, done, worst, maxsteps = 3, 0, 0.0, 0
    while done < 400:
        B = random.randint(1, 3)
        h = random.randint(1, 2)
        D = [[random.randint(-B, B) for _ in range(k)] for _ in range(h)]
        if rank(D) < h:
            continue
        c = [random.randint(-3, 3) for _ in range(k)]
        C = max(1, max(abs(x) for x in c))
        y = None
        for _ in range(60):
            lam = [random.randint(-300, 300) for _ in range(h)]
            cand = [c[i] + sum(lam[j] * D[j][i] for j in range(h)) for i in range(k)]
            if min(cand) >= 0:
                y = cand
                break
        if y is None:
            continue
        T0 = math.factorial(k) * B ** k
        T1 = T0 + random.randint(0, 6) + 2
        steps = 0
        while True:
            I = [i for i in range(k) if y[i] >= T1]
            z = find_z(D, I, k, h, B)
            if z is None:
                break
            assert max(abs(t) for t in z) <= T0
            if sum(z) < 0 or all(t <= 0 for t in z):
                z = [-t for t in z]
            q = min((y[i] - 1) // z[i] for i in range(k) if z[i] > 0)
            assert q >= 1
            y = [a - q * b for a, b in zip(y, z)]
            assert min(y) >= 0
            steps += 1
            assert steps <= k
        I = [i for i in range(k) if y[i] >= T1]
        rest = [[row[i] for i in range(k) if i not in I] for row in D]
        assert (rank(rest) if rest and rest[0] else 0) == h
        bound = k * C + k * k * T0 * (T1 + C)
        assert sum(y) <= bound
        worst = max(worst, sum(y) / bound)
        maxsteps = max(maxsteps, steps)
        done += 1
    print('  試行 %d 回（k=3、生成元 1〜2 本、B≤3）: 全て上界 kC + k^2 T0 (T1+C) 以下。' % done)
    print('  最大の比 = %.4f、移動の回数の最大 = %d（≤ k）' % (worst, maxsteps))


# ----------------------------------------------------------------------------
# 3. 定理 A の上界と小さな文法
# ----------------------------------------------------------------------------
def tau_bound(k, f, r, theta, v):
    """定理 A の漸化式。tau_{-1} = 0、j = 0..k。"""
    B = (r + 2) * theta
    T0 = math.factorial(k) * B ** k
    Dp = v * (2 ** k - 1) ** f
    tau = 0
    for j in range(0, k + 1):
        K = (j + k) * Dp + 1
        C = theta + f + K * B + j * (tau + theta)
        T1 = T0 + j * tau + 2
        tau = k * f + k * C + k * k * T0 * (T1 + C)
    return tau


def V(j, kappa):
    return (j, kappa)


def enum_grammar(rules, arity, caps):
    lang = {A: set() for A in arity}
    changed = True
    while changed:
        changed = False
        for (A, comps, kids) in rules:
            for choice in itertools.product(*[sorted(lang[B]) for B in kids]):
                tup = tuple(''.join(it if isinstance(it, str) else choice[it[0]][it[1]]
                                    for it in comp) for comp in comps)
                if sum(map(len, tup)) <= caps[A] and tup not in lang[A]:
                    lang[A].add(tup)
                    changed = True
    return lang


def thickness(rules, arity):
    INF = 10 ** 9
    mn = {A: INF for A in arity}
    tl = lambda comps: sum(len(it) for comp in comps for it in comp if isinstance(it, str))
    ch = True
    while ch:
        ch = False
        for A, comps, kids in rules:
            val = tl(comps) + sum(mn[B] for B in kids)
            if val < mn[A]:
                mn[A] = val
                ch = True
    out = {A: INF for A in arity}
    out['S'] = 0
    ch = True
    while ch:
        ch = False
        for A, comps, kids in rules:
            for j, B in enumerate(kids):
                val = out[A] + tl(comps) + sum(mn[C] for i, C in enumerate(kids) if i != j)
                if val < out[B]:
                    out[B] = val
                    ch = True
    return max(out[A] + tl(comps) + sum(mn[B] for B in kids) for A, comps, kids in rules)


def all_words(letters, L):
    res, frontier = [''], ['']
    for _ in range(L):
        frontier = [w + a for w in frontier for a in letters]
        res += frontier
    return res


def all_contexts(letters, d, Lc):
    ws = all_words(letters, Lc)
    out = []

    def rec(i, cur, used):
        if i == d + 1:
            out.append(tuple(cur))
            return
        for w in ws:
            if used + len(w) > Lc:
                continue
            if 0 < i < d and not w:
                continue
            rec(i + 1, cur + [w], used + len(w))

    rec(0, [], 0)
    out.sort(key=lambda E: sum(map(len, E)))
    return out


def representative(lang, x, ctxs):
    T = typ(x)
    n = tuple(sum(c) for c in zip(*[lang.parikh(xi) for xi in x]))
    E0 = next(E for E in ctxs if lang.member(fill(E, x)))
    M0 = frozenset(fill(E0, x))
    b = tuple(sum(1 for M in T if a in M) for a in lang.letters)
    J = frozenset().union(*T)
    Jidx = [i for i, a in enumerate(lang.letters) if a in J]
    total = sum(n)
    for norm in range(sum(b), total + 1):
        extra = norm - sum(b)
        for add in itertools.product(range(extra + 1), repeat=len(Jidx)):
            if sum(add) != extra:
                continue
            n2 = list(b)
            for i, v in zip(Jidx, add):
                n2[i] += v
            if lang.in_lattice(M0, tuple(p - q for p, q in zip(n2, n))):
                x2 = build_tuple(lang, T, tuple(n2))
                agree = all(lang.member(fill(F, x)) == lang.member(fill(F, x2)) for F in ctxs)
                npos = sum(1 for F in ctxs if lang.member(fill(F, x)))
                return x2, E0, agree, npos
    raise AssertionError


def run_grammar(name, lang, rules, arity, caps, Lcheck, Lc1, Lc2, f, r, note=''):
    print('-' * 78)
    print(name, note)
    k, v = lang.k, len(arity)
    gl = enum_grammar(rules, arity, caps)
    gen = {w[0] for w in gl['S'] if len(w[0]) <= Lcheck}
    true = {w for w in nd_words(lang, Lcheck) if lang.member(w)}
    theta = max(1, thickness(rules, arity))
    bound = tau_bound(k, f, r, theta, v)
    print('  k=%d, v=%d, r=%d, f=%d, 厚さ θ=%d, L(G) と L の一致（長さ≤%d、%d 語）: %s'
          % (k, v, r, f, theta, Lcheck, len(true), gen == true))
    print('  定理 A の上界 τ_k ≈ 10^%.1f' % math.log10(bound))
    ctxs = {1: all_contexts(lang.letters, 1, Lc1), 2: all_contexts(lang.letters, 2, Lc2)}
    worst = 0
    rows = []
    for A in sorted(arity):
        bytype = {}
        for tup in gl[A]:
            bytype.setdefault(typ(tup), []).append(tup)
        for T, tups in sorted(bytype.items(), key=lambda p: [show(M) for M in p[0]]):
            x = min(tups, key=lambda t: (sum(map(len, t)), t))
            x2, E0, agree, npos = representative(lang, x, ctxs[len(x)])
            tau = sum(map(len, x2))
            worst = max(worst, tau)
            rows.append((A, '(' + ','.join(show(M) for M in T) + ')', sum(map(len, x)),
                         x2, tau, agree, npos))
    print('  %-4s %-12s %-8s %-18s %-4s %-6s %s'
          % ('非終', '型', '最短生成', '代表', 'τ_X', '同値', '（受理する文脈の数）'))
    for A, T, g, x2, tau, agree, npos in rows:
        print('  %-4s %-12s %-8d %-18s %-4d %-6s %d' % (A, T, g, x2, tau, agree, npos))
    print('  max τ_X = %d、上界との比 ≈ 10^%.1f' % (worst, math.log10(worst) - math.log10(bound)))
    return worst


def section3():
    print('=' * 78)
    print('S3  定理 A の上界と、小さな文法での分布代表')
    print('=' * 78)
    print('上界 τ_k の例: (k,f,r,θ,v)=(3,2,2,4,4) → 10^%.1f、(3,2,2,8,4) → 10^%.1f、'
          '(3,2,2,8,40) → 10^%.1f'
          % tuple(math.log10(tau_bound(3, 2, 2, t, v)) for t, v in ((4, 4), (8, 4), (8, 40))))
    print('  （θ を 2 倍にしたときの増え方から読む次数: %.2f、v を 10 倍: %.2f）'
          % (math.log2(tau_bound(3, 2, 2, 2 ** 21, 4) / tau_bound(3, 2, 2, 2 ** 20, 4)),
             math.log10(tau_bound(3, 2, 2, 8, 10 ** 9) / tau_bound(3, 2, 2, 8, 10 ** 8))))

    # ---- G1(n)：段 {b} < {a,c}。L = b・{w in {a,c}+ : |w|_a 偶数}。型付きの生成が長い ----
    def condG1(M):
        if 'b' not in M or M == frozenset('b'):
            return None
        return [({'b': 1}, 0, 1), ({'a': 1}, 2, 0)]
    for n in (1, 2, 3):
        lang = StageLang('G1', 'abc', {'b': 1, 'a': 2, 'c': 2}, condG1)
        rules = [('S', (('b', V(0, 0)),), ('W',)),
                 ('W', ((V(0, 0), V(1, 0)),), ('W', 'W')),
                 ('W', (('c',),), ()),
                 ('W', (('aa',),), ()),
                 ('W', (('a', V(0, 0), 'a'),), ('W',)),
                 ('W', ((V(0, 0),),), ('A%d' % n,)),
                 ('A0', (('aa',),), ())]
        arity = {'S': 1, 'W': 1, 'A0': 1}
        caps = {'S': 7, 'W': 6, 'A0': 99}
        for i in range(1, n + 1):
            rules.append(('A%d' % i, ((V(0, 0), V(1, 0)),), ('A%d' % (i - 1), 'A%d' % (i - 1))))
            rules.append(('A%d' % i, (('c',),), ()))
            arity['A%d' % i] = 1
            caps['A%d' % i] = 99
        run_grammar('G1(n=%d)' % n, lang, rules, arity, caps, 7, 4, 3, 1, 2,
                    '  S→bW, W→WW|c|aa|aWa|A_n, A_i→A_{i-1}A_{i-1}|c, A_0→aa')

    # ---- G2：段 {b,e} < {a,c}。内容（e の有無）で値が変わる ----
    def condG2(M):
        if 'b' not in M or not (M & frozenset('ac')):
            return None
        return [({'b': 1}, 0, 1), ({'a': 1}, 2, 1 if 'e' in M else 0)]
    lang = StageLang('G2', 'abce', {'b': 1, 'e': 1, 'a': 2, 'c': 2}, condG2)
    rules = [('S', (('b', V(0, 0)),), ('W',)),
             ('S', ((V(0, 0), V(1, 0)),), ('P', 'X')),
             ('P', (('eb',),), ()), ('P', (('be',),), ()),
             ('P', (('e', V(0, 0)),), ('P',)), ('P', ((V(0, 0), 'e'),), ('P',)),
             ('W', ((V(0, 0), V(1, 0)),), ('W', 'W')),
             ('W', (('c',),), ()), ('W', (('aa',),), ()),
             ('W', (('a', V(0, 0), 'a'),), ('W',)),
             ('X', (('a',),), ()),
             ('X', ((V(0, 0), V(1, 0)),), ('X', 'W')),
             ('X', ((V(0, 0), V(1, 0)),), ('W', 'X'))]
    arity = {'S': 1, 'P': 1, 'W': 1, 'X': 1}
    caps = {'S': 6, 'P': 5, 'W': 5, 'X': 5}
    run_grammar('G2', lang, rules, arity, caps, 6, 3, 3, 1, 2,
                '  L = {p w : p∈{b,e}+ に b が一つ, w∈{a,c}+, |w|_a ≡ [e∈p] (2)}')

    # ---- G3：ファンアウト 2、段 {a} < {b,c}、無限群。内容（c の有無）で値が変わる ----
    def condG3(M):
        if M == frozenset('ab'):
            return [({'b': 1, 'a': -1}, 0, 1)]
        if M == frozenset('abc'):
            return [({'b': 1, 'a': -1}, 0, 0)]
        return None
    lang = StageLang('G3', 'abc', {'a': 1, 'b': 2, 'c': 2}, condG3)
    grow = lambda X: [(X, ((V(0, 0),), (V(0, 1), 'c')), (X,)),
                      (X, ((V(0, 0),), ('c', V(0, 1))), (X,)),
                      (X, (('a', V(0, 0)), (V(0, 1), 'b')), (X,)),
                      (X, (('a', V(0, 0)), ('b', V(0, 1))), (X,))]
    rules = [('S', ((V(0, 0), 'c', V(0, 1)),), ('R',)),
             ('S', ((V(0, 0), 'b', V(0, 1)),), ('Q',)),
             ('S', ((V(0, 0), 'b', V(0, 1)),), ('Z',)),
             ('R', (('a',), ('b',)), ()),
             ('Q', (('a',), ('c',)), ()),
             ('Q', (('a', V(0, 0)), (V(0, 1), 'c')), ('R',)),
             ('Q', (('a', V(0, 0)), ('c', V(0, 1))), ('R',)),
             ('Z', (('a',), ('b',)), ()),
             ('Z', (('a', V(0, 0)), (V(0, 1), 'b')), ('Z',))] + grow('R') + grow('Q')
    arity = {'S': 1, 'R': 2, 'Q': 2, 'Z': 2}
    caps = {'S': 8, 'R': 7, 'Q': 7, 'Z': 7}
    run_grammar('G3', lang, rules, arity, caps, 8, 4, 3, 2, 1,
                '  L = {a^p u : c∈u, |u|_b = p} ∪ {a^p b^{p+1}}（ファンアウト 2、値群 Z）')

    # ---- G3+：G3 に倍増の非終端 D1 を加える（v=6、参考）----
    rules2 = rules + [('Z', ((V(0, 0),), (V(0, 1),)), ('D1',)),
                      ('R', ((V(0, 0),), (V(0, 1),)), ('D1',)),
                      ('D1', ((V(0, 0), V(1, 0)), (V(0, 1), V(1, 1))), ('D0', 'D0')),
                      ('D0', (('a',), ('b',)), ())]
    # D1 は (aa,bb) だけを生成する。Z と R の両方から呼ばれる。
    arity2 = dict(arity, D1=2, D0=2)
    caps2 = dict(caps, D1=7, D0=7)
    run_grammar('G3+', lang, rules2, arity2, caps2, 8, 4, 3, 2, 2,
                '  G3 に D1→(ξ1ξ1\',ξ2ξ2\')(D0,D0), D0→(a,b), Z→D1, R→D1 を追加（v=6、参考）')


# ----------------------------------------------------------------------------
# 4. 課題3：F_4, E_1, F_n
# ----------------------------------------------------------------------------
def section4():
    print('=' * 78)
    print('S4  課題3：命題7.4 の例での格子と飽和の欠け')
    print('=' * 78)
    examples = [('F4 ∪ {(14,26)}', [(1, 3, 12), (4, 8, 1), (6, 4, 4), (12, 1, 3)], (14, 26, 0)),
                ('E1 ∪ {(6,5)}', [(1, 8, 1), (2, 3, 4), (4, 4, 2), (8, 1, 1)], (6, 5, 0))]
    for n in (3, 4, 5):
        Fn = [(3 * n + 2 * j, 1 + 5 * j, 2 * (n - j)) for j in range(n)]
        Fn += [(1, 10 * n - 8, 1), (10 * n - 4, 1, 1)]
        examples.append(('F_%d ∪ {P}' % n, Fn, (5 * n, 5 * n + 1, 0)))
    for name, Q3, P in examples:
        Q = set(Q3) | {P}
        N3 = echelon([tuple(a - b for a, b in zip(q, Q3[0])) for q in Q3[1:]])
        idx = abs(N3[0][0] * N3[1][1] * N3[2][2]) if len(N3) == 3 else None
        Hall = echelon([tuple(a - b for a, b in zip(q, Q3[0])) for q in Q3[1:]]
                       + [tuple(a - b for a, b in zip(P, Q3[0]))])
        idx_all = abs(Hall[0][0] * Hall[1][1] * Hall[2][2]) if len(Hall) == 3 else None
        box = max(max(q) for q in Q3) + 1
        sat = [m for m in itertools.product(range(1, box), repeat=3)
               if in_lat(tuple(a - b for a, b in zip(m, Q3[0])), N3)]
        missing = sorted(set(sat) - set(Q3), key=lambda m: (sum(m), m))
        normP = sum(P)
        short_ab = sorted(((i, j) for i in range(1, normP) for j in range(1, normP - i)
                           if in_lat((i - P[0], j - P[1], 0), Hall)),
                          key=lambda p: (sum(p), p))
        plane = sorted(((x, y) for x in range(-60, 61) for y in range(-60, 61)
                        if (x, y) != (0, 0) and in_lat((x, y, 0), N3)),
                       key=lambda p: (abs(p[0]) + abs(p[1]), p))
        print(name)
        print('  (T)（全数）: %s、|Q3|=%d、<Q3-Q3> の指数=%s、<Q-Q> の指数=%s'
              % (check_T(Q), len(Q3), idx, idx_all))
        print('  Π3 ∩ (q + <Q3-Q3>) の箱 [1,%d]^3 の点 %d 個のうち Q3 に入らないもの %d 個。最短: %s'
              % (box - 1, len(sat), len(missing), missing[:3]))
        print('  P=%s（長さ %d）。p_S + <Q-Q> の中の、P より短い ab の点: %d 個。最短: %s'
              % (P[:2], normP, len(short_ab), short_ab[:3]))
        print('  <Q3-Q3> の中の最短の平面ベクトル: %s。P に足した点は Q2 に入るか: %s'
              % (plane[:2], [((P[0] + x, P[1] + y, 0) in Q) for x, y in plane[:2]]))
        # (WS) を破る組：q in Q3、z は格子の小さな元、q >= |z| + 2（z の支持の上）、q - z は Q3 の外
        ws = None
        for q in sorted(Q3):
            for x, y in plane[:6]:
                z = (x, y, 0)
                if all(a >= abs(c) + 2 for a, c in zip(q, z) if c):
                    qz = tuple(a - c for a, c in zip(q, z))
                    if qz not in Q:
                        ws = (q, z, qz)
                        break
            if ws:
                break
        print('  (WS) を破る組 (q, z, q-z): %s' % (ws,))


if __name__ == '__main__':
    section1()
    section2()
    section3()
    section4()
    print('=' * 78)
    print('完了')
