"""Checks for claude_S1_problemC_2026-11-08.md (standard library only).
Run:  python3 -I check_claude_S1_problemC_2026-11-08.py      (about 1-2 minutes)

(A) Theorem C: min over |I| in (M/3-1, 2M/3] of C(M+1,|I|) >= 3^(M/3-1), M = 6..400.
(B) Corollary D: exponent of theta in N <= 2 theta [..theta^4..]^(3/log2 3).
(C) Lemma R (language level) on finite C1 languages:
    if a^x w a^g w a^y, a^x w a^(g+n+y), a^(x+g+n) w a^y are all in L (w contains b, n>=1),
    then  w a^g w == w a^(g+n)  and  a^(g+n) w == w a^(g+n)  (== : equal distributions).
    Languages: all subsets of Sigma^{<=3} that are in C1, plus finite C1 closures of random seeds.
(D) Task 4: Fibonacci chain with markers alternating between two bases; partial closure.
These are sanity checks of the algebra, not proofs.
"""
import itertools, random, math
from collections import defaultdict

def typ(x): return 'b' in x

def dists(L):
    D = defaultdict(set)
    for w in L:
        for i in range(len(w)):
            for j in range(i+1, len(w)+1):
                D[w[i:j]].add((w[:i], w[j:]))
    return D

def in_C1(L, D=None):
    D = D or dists(L)
    by = defaultdict(list)
    for x, cs in D.items():
        for c in cs: by[(typ(x), c)].append(x)
    for xs in by.values():
        d0 = D[xs[0]]
        if any(D[y] != d0 for y in xs[1:]): return False
    return True

def closure(seed, Lmax, rounds=15):
    """s_{U,2} forcing closure, words longer than Lmax dropped.
    Returns (L, saturated?)."""
    L = set(seed)
    for _ in range(rounds):
        D = dists(L)
        parent = {}
        def f(x):
            while parent.get(x, x) != x: x = parent[x]
            return x
        by = defaultdict(list)
        for x, cs in D.items():
            for c in cs: by[(typ(x), c)].append(x)
        for xs in by.values():
            r = f(xs[0])
            for y in xs[1:]:
                if f(y) != r: parent[f(y)] = r
        cls = defaultdict(list)
        for x in D: cls[f(x)].append(x)
        new, overflow = set(), False
        for xs in cls.values():
            if len(xs) < 2: continue
            ctx = set().union(*(D[x] for x in xs))
            for x in xs:
                for l, r in ctx:
                    w = l + x + r
                    if w not in L:
                        if len(w) <= Lmax: new.add(w)
                        else: overflow = True
        if not new: return L, not overflow
        L |= new
        if len(L) > 1500: return L, False
    return L, False

def antichain_violation(L):
    bw = sorted((w for w in L if 'b' in w), key=len)
    return any(len(y) > len(x) and x in y for i, x in enumerate(bw) for y in bw[i+1:])

def check_lemmaR(L):
    D = dists(L)
    eq = lambda u, v: D.get(u, set()) == D.get(v, set())
    tested = bad = 0
    for W1 in L:
        if W1.count('b') < 2: continue
        # decompose W1 = a^x w a^g w a^y with w starting and ending with b
        for x in range(len(W1)):
            if W1[x] != 'b' or W1[:x].strip('a'): continue
            for e in range(x+1, len(W1)+1):
                w = W1[x:e]
                if w[-1] != 'b': continue
                rest = W1[e:]
                g = len(rest) - len(rest.lstrip('a'))
                if rest[g:g+len(w)] != w: continue
                tail = rest[g+len(w):]
                if tail.strip('a'): continue
                y = len(tail)
                for n in range(1, 8):
                    W2 = 'a'*x + w + 'a'*(g+n+y)
                    W3 = 'a'*(x+g+n) + w + 'a'*y
                    if W2 in L and W3 in L:
                        tested += 1
                        ok = eq(w+'a'*g+w, w+'a'*(g+n)) and eq('a'*(g+n)+w, w+'a'*(g+n))
                        bad += (not ok)
    return tested, bad

if __name__ == '__main__':
    # (A)
    worst = min(min(math.comb(M+1, j) for j in range(1, M+1) if M/3-1 < j <= 2*M/3) / 3**(M/3-1)
                for M in range(6, 401))
    print(flush=True); print('(A) min_M min_j C(M+1,j)/3^(M/3-1) over M=6..400 :', round(worst, 3), '(>=1 required)')
    # (B)
    print('(B) Cor.D theta-exponent: 1 + 4*3/log2(3) = %.3f  (the "(||G|| theta^4)^(1.9+eps)" form gives 7.6+)' % (1 + 12/math.log2(3)))
    # (C)
    words = [''.join(p) for k in range(1, 4) for p in itertools.product('ab', repeat=k)]
    langs = []
    for mask in range(1, 1 << len(words)):
        L = {w for i, w in enumerate(words) if mask >> i & 1}
        if in_C1(L): langs.append(L)
    n_small = len(langs)
    random.seed(7)
    bwords = [''.join(p) for k in range(1, 4) for p in itertools.product('ab', repeat=k) if 'b' in p]
    n_clos = 0
    for t in range(400):
        seed = {random.choice(['a'*random.randint(1, 6)] + bwords) + random.choice(['', 'a', 'aa', 'b', 'ab', 'ba'])
                for _ in range(random.randint(2, 5))}
        L, sat = closure(seed, 8, rounds=8)
        if sat and in_C1(L) and not antichain_violation(L):
            langs.append(L); n_clos += 1
    T = B = 0
    for L in langs:
        t, b = check_lemmaR(L); T += t; B += b
    print('(C) finite C1 languages: %d subsets of Sigma^<=3, %d saturated closures; Lemma R instances %d, failures %d' % (n_small, n_clos, T, B))
    # (D)
    random.seed(11)
    A = ['b', 'bab', 'baab']           # base 1
    Bm = ['bb', 'bbab', 'abb']         # base 2
    for n in (4, 5, 6):
        viol = 0
        for t in range(30):
            ms = [random.choice(A if i % 2 == 0 else Bm) for i in range(n-1)]
            F = [{'a'}, {'aa', ms[0]}]
            for i in range(2, n): F.append({x+y for x in F[-1] for y in F[-2]} | {ms[i-1]})
            N = min(len(w) for w in F[-1] if 'b' not in w)
            L, sat = closure(F[-1], N+4, rounds=12)
            viol += antichain_violation(L)
        print('(D) alternating-base Fibonacci n=%d (N=%d): antichain violation in partial closure %d/30' % (n, N, viol))
