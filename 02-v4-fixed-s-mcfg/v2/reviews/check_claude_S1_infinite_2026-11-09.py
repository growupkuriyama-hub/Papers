#!/usr/bin/env python3
"""check_claude_S1_infinite_2026-11-09.py  (standard library only)

Auxiliary checks for claude_S1_infinite_2026-11-09.md.  Computation is NOT a proof.

 (A) exponent arithmetic of Theorem P (final bound K^76 theta^21).
 (B) random straight-line trees (labels never repeat on a root path, same label =>
     same yield): the purely combinatorial steps P1(d)(e), (P1)-(P5) of Theorem P,
     incl. the variant with a modulus D (infinite case, Theorem P-infinity).
 (C) random regular languages in C1 (typing s_{U,2}), via the syntactic monoid:
     (C-i)  P0(z) = {p : a^p z == z} is p0*N  (closed under differences),
     (C-ii) for every b-word z and context (l, r): {f : l a^f z r in L} = f_min + P0(z),
     (C-iii) Lemma S: if a^D z == z == z a^D (D>=1) and a^x z a^y in L,
             then x and y are not in (D, N]  (N = shortest pure word).
     (C-iv) Lemma R at monoid level.
Run:  python3 -I check_claude_S1_infinite_2026-11-09.py      (about 1-2 minutes)
"""
import math, random, sys
from itertools import product

random.seed(20261109)

# ---------------------------------------------------------------- (A)
def part_A():
    e = 3 * math.log(6) / math.log(3)
    # bracket 3K(M+1)(m+1)^2(M lam+1)^2 with m ~ 25 K^5 theta, lam = 5K^2 theta
    kexp = (1 + 2 * 5 + 2 * 2) * e + 2      # times B1 = 14 K^2 theta
    texp = (2 + 2) * e + 1
    print(f"(A) 3 log_3 6 = {e:.4f};  K-exponent {kexp:.3f} (claimed 76),"
          f"  theta-exponent {texp:.3f} (claimed 21)")
    assert kexp < 76 and texp < 21

# ---------------------------------------------------------------- (B)
def random_slp(K):
    """rules: X_0 -> a ; X_j -> X_i X_k (i,k < j), X_{K-1} root"""
    rules = [None]
    ln = [1]
    for j in range(1, K):
        i = random.randrange(j); k = random.randrange(j)
        if random.random() < 0.6:            # bias to long chains
            i = j - 1 if random.random() < .5 else i
            k = j - 1 if random.random() < .5 else k
        rules.append((i, k)); ln.append(ln[i] + ln[k])
    return rules, ln

def part_B(trials=60000):
    viol = 0; tested = 0; Mtested = 0; Mmax = 0
    for _ in range(trials):
        K = random.randint(3, 9); th = random.randint(1, 4)
        rules, ln = random_slp(K)
        N = ln[-1]
        heavy = lambda X: ln[X] > th
        def isseed(X):
            if not heavy(X) or rules[X] is None: return False
            i, k = rules[X]; return not heavy(i) and not heavy(k)
        # seeds of the tree, left to right (positions); expand only heavy parts
        seeds = []
        def walk(X, pos):
            if not heavy(X): return
            if isseed(X): seeds.append((pos, X)); return
            i, k = rules[X]; walk(i, pos); walk(k, pos + ln[i])
        if N > 10**7: continue
        walk(K - 1, 0)
        s = len(seeds)
        if s <= K:
            if N > K * (K + 2) * th: viol += 1; print("P1(d) viol", rules, th)
            continue
        tested += 1
        for (p1, X1), (p2, X2) in zip(seeds, seeds[1:]):
            if not (ln[X1] <= 2 * th and p2 - p1 <= 2 * K * th):
                viol += 1; print("P1(c)(e) viol")
        # heavy path
        path = [K - 1]; offs = [0]
        def nseeds(X):
            if not heavy(X): return 0
            if isseed(X): return 1
            i, k = rules[X]; return nseeds(i) + nseeds(k)
        while not isseed(path[-1]):
            i, k = rules[path[-1]]
            if ln[i] >= ln[k]: path.append(i); offs.append(offs[-1])
            else: path.append(k); offs.append(offs[-1] + ln[i])
        istar = max(t for t in range(len(path)) if nseeds(path[t]) >= K + 1)
        B0 = ln[path[istar]]
        if B0 > 2 * K * (K + 2) * th: viol += 1; print("B0 viol")
        lo = offs[istar]; hi = lo + B0
        sub = [(p, X) for (p, X) in seeds if lo <= p < hi]
        found = None
        for a_ in range(len(sub)):
            for b_ in range(a_ + 1, min(len(sub), a_ + K + 1)):
                if sub[a_][1] == sub[b_][1]:
                    dd = sub[b_][0] - sub[a_][0]
                    if found is None or dd < found[0]:
                        found = (dd, sub[a_], sub[b_])
            # pigeonhole guarantees some pair within K steps
        if found is None: viol += 1; print("pigeonhole viol"); continue
        d, (x1, Y), (x2, _) = found
        if d > 2 * K * K * th: viol += 1; print("d viol")
        nY = ln[Y]; g0 = d - nY
        if g0 < 0: viol += 1; print("g0<0")
        # values v_i
        vals = []
        for t in range(istar + 1):
            X = path[t]; Li = x1 - offs[t]; Ri = ln[X] - Li - nY
            sp = (-Li) % d; si = (g0 - Ri) % d
            kap = (Ri + si - g0)
            assert kap >= 0 and kap % d == 0
            ei = Li + sp + kap
            v = ei + d
            assert v == ln[X] + si + sp and ei % d == 0
            vals.append(v)
        for t in range(istar):
            if vals[t] > 2 * vals[t + 1] + 2 * d: viol += 1; print("(*) viol")
        y1 = N - x1 - nY
        q, rho = divmod(y1 - g0, d)
        estar = ((x1 + q * d) // d) * d; rhop = x1 + q * d - estar
        Vs = estar + d
        assert Vs == N - rho - rhop
        B1 = 14 * K * K * th; lam = 5 * K * K * th
        for Dmod in (None, random.randint(d, 3 * N + 3)):
            Lam = Vs if Dmod is None else min(Vs, Dmod)
            # (P4)
            chosen = []; t = istar
            if vals[t] > B1: viol += 1; print("start viol")
            if vals[t] <= Lam / 2:
                chosen.append(t); cur = vals[t]
                while True:
                    nxt = next((u for u in range(chosen[-1] - 1, -1, -1)
                                if vals[u] > 2 * cur), None)
                    if nxt is None: break
                    if vals[nxt] > 6 * cur: viol += 1; print("6x viol")
                    if vals[nxt] > Lam / 2: break
                    chosen.append(nxt); cur = vals[nxt]
            M = len(chosen); Mmax = max(Mmax, M)
            if M:
                last = vals[chosen[-1]]
                if not last > Lam / 12: viol += 1; print("last viol")
                sums = set()
                for mask in range(1 << min(M, 14)):
                    sm = sum(vals[chosen[j]] for j in range(min(M, 14)) if mask >> j & 1)
                    key = sm if Dmod is None else sm % Dmod
                    if key in sums: viol += 1; print("subset sums viol"); break
                    sums.add(key)
            if Lam >= 15 * B1 and Lam >= 10 * d and M < 1 + math.log(Lam / (15 * B1), 6) - 1e-9:
                viol += 1; print("M bound viol")
            Mtested += 1
            # (P5) greedy filler with exact target Vs
            X = Vs - sum(vals[c] for c in chosen)
            assert X >= 0 and X % d == 0
            qs = []
            for t in range(istar + 1):
                qt = X // vals[t]; X -= qt * vals[t]; qs.append(qt)
            if qs[0] > 1 or any(qs[t] > 2 + 4 * K * K for t in range(1, len(qs))):
                viol += 1; print("q viol")
            Qlen = sum(qs) * lam + X
            if Qlen > 5 * K ** 3 * lam + 3 * lam: viol += 1; print("|Q| viol")
            if X >= vals[istar] or X % d: viol += 1; print("rest viol")
    print(f"(B) trees with >K seeds: {tested}, selections checked: {Mtested}, max M: {Mmax}, violations: {viol}")
    return viol

# ---------------------------------------------------------------- (C)
def minimize(nq, delta, F, q0):
    reach = {q0}; st = [q0]
    while st:
        q = st.pop()
        for c in (0, 1):
            r = delta[q][c]
            if r not in reach: reach.add(r); st.append(r)
    reach = sorted(reach)
    cls = {q: (q in F) for q in reach}
    while True:
        sig = {q: (cls[q], cls[delta[q][0]], cls[delta[q][1]]) for q in reach}
        ids = {}; new = {}
        for q in reach: new[q] = ids.setdefault(sig[q], len(ids))
        if len(ids) == len(set(cls.values())): cls = new; break
        cls = new
    n = len(set(cls.values()))
    d2 = [[0, 0] for _ in range(n)]
    for q in reach: d2[cls[q]] = [cls[delta[q][0]], cls[delta[q][1]]]
    F2 = {cls[q] for q in reach if q in F}
    return n, d2, F2, cls[q0]

def analyse(n, dl, F, q0, B=40):
    A = tuple(dl[q][0] for q in range(n)); Bt = tuple(dl[q][1] for q in range(n))
    comp = lambda f, g: tuple(g[f[q]] for q in range(n))   # first f then g
    idt = tuple(range(n))
    # semigroup elements with type
    elems = {(A, 0): 'a', (Bt, 1): 'b'}; frontier = list(elems)
    while frontier:
        nf = []
        for (f, t) in frontier:
            for (g, u, ch) in ((A, 0, 'a'), (Bt, 1, 'b')):
                key = (comp(f, g), t | u)
                if key not in elems: elems[key] = elems[(f, t)] + ch; nf.append(key)
        frontier = nf
        if len(elems) > 3000: return None
    # pairs J
    J = {(p, q) for p in F for q in F}; st = list(J)
    pre = [[[] for _ in range(n)] for _ in range(2)]
    for q in range(n):
        for c in (0, 1): pre[c][dl[q][c]].append(q)
    while st:
        p, q = st.pop()
        for c in (0, 1):
            for p2 in pre[c][p]:
                for q2 in pre[c][q]:
                    if (p2, q2) not in J: J.add((p2, q2)); st.append((p2, q2))
    reach = range(n)   # minimal DFA: all reachable
    keys = list(elems)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            (f, t), (g, u) = keys[i], keys[j]
            if t != u or f == g: continue
            if any((f[s], g[s]) in J for s in reach): return None   # not C1
    inL = lambda s: s in F
    pure = [k for k in range(1, 4 * B) if inL(tuple_pow_apply(A, k, q0))]
    if not pure: return None
    N = pure[0]
    return dict(A=A, Bt=Bt, comp=comp, idt=idt, elems=elems, J=J, N=N)

def tuple_pow_apply(f, k, q):
    for _ in range(k): q = f[q]
    return q

def part_C(trials=30000, B=40):
    stats = dict(C1=0, periodic=0, ctx=0, S=0, R=0, Snontriv=0); viol = 0
    for _ in range(trials):
        nq = random.randint(2, 6)
        delta = [[random.randrange(nq), random.randrange(nq)] for _ in range(nq)]
        F = {q for q in range(nq) if random.random() < .4}
        if not F: continue
        n, dl, F2, q0 = minimize(nq, delta, F, 0)
        if n < 2: continue
        res = analyse(n, dl, F2, q0, B)
        if res is None: continue
        stats['C1'] += 1
        A, comp, N = res['A'], res['comp'], res['N']
        J = res['J']
        apow = [res['idt']]
        for k in range(1, 3 * B): apow.append(comp(apow[-1], A))
        coreach = {p for (p, q) in J if p == q}
        nonempty = lambda f: any(f[s] in coreach for s in range(n))
        for (z, t) in res['elems']:
            if t != 1 or not nonempty(z): continue
            # (C-i)
            P0 = [p for p in range(B) if comp(apow[p], z) == z]
            p0 = P0[1] if len(P0) > 1 else None
            if p0:
                stats['periodic'] += 1
                if P0 != list(range(0, B, p0)): viol += 1; print("P0 not p0N", P0)
            # (C-ii): contexts l = state s, r = any element (incl. identity)
            for s in range(n):
                for (r, _) in list(res['elems'])[:60] + [(res['idt'], 0)]:
                    Fs = [f for f in range(B) if r[z[apow[f][s]]] in F2]
                    if not Fs: continue
                    stats['ctx'] += 1
                    f0 = Fs[0]
                    exp = [f0] if p0 is None else list(range(f0, B, p0))
                    if Fs != exp: viol += 1; print("ctx viol", Fs, exp)
            # (C-iii) Lemma S
            for Dd in range(1, B // 2):
                if comp(apow[Dd], z) == z and comp(z, apow[Dd]) == z:
                    for x in range(0, B):
                        for y in range(0, B):
                            if apow[y][z[apow[x][q0]]] in F2:
                                stats['S'] += 1
                                if Dd < N: stats['Snontriv'] += 1
                                if Dd < x <= N or Dd < y <= N:
                                    viol += 1; print("Lemma S viol", x, y, Dd, N)
                    break
            # (C-iv) Lemma R at monoid level: a^x z a^g z a^y, a^x z a^{d+y}, a^{x+d} z a^y in L
            for g in range(4):
                zz = comp(comp(z, apow[g]), z)
                for nn in range(1, 4):
                    dd = g + nn
                    for x in range(4):
                        for y in range(4):
                            w1 = comp(comp(apow[x], zz), apow[y])[q0] in F2
                            w2 = comp(comp(apow[x], z), apow[dd + y])[q0] in F2
                            w3 = comp(comp(apow[x + dd], z), apow[y])[q0] in F2
                            if w1 and w2 and w3:
                                stats['R'] += 1
                                z0 = comp(z, apow[g])
                                ok = (comp(apow[dd], z0) == comp(z0, apow[dd]) ==
                                      comp(z0, z0))
                                if not ok: viol += 1; print("Lemma R viol")
    print(f"(C) C1 languages {stats['C1']}, periodic b-classes {stats['periodic']},"
          f" contexts {stats['ctx']}, Lemma-S instances {stats['S']},"
          f" Lemma-R instances {stats['R']}, violations {viol}")
    print(f"    Lemma-S instances with D < N (non-vacuous): {stats['Snontriv']}")
    return viol

if __name__ == "__main__":
    part_A()
    v = part_B()
    v += part_C()
    print("TOTAL violations:", v)
