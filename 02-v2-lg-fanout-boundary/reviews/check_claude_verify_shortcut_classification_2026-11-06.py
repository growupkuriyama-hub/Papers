"""Independent re-check of chatgpt_shortcut_classification_2026-11-06 (Claude).
Own implementation of content-typed SUB_1 / SUB_2 one-step consequences.
Convention flag: interior_nonempty (manuscript convention per report) or allow empty interior."""
import sys
from collections import defaultdict

def cont(s): return ''.join(sorted(set(s)))

def occ(w, d, interior_nonempty=True):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[:i], w[j:]), (w[i:j],)
    else:
        lo = 1 if interior_nonempty else 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                for k in range(j + lo, n):
                    for l in range(k + 1, n + 1):
                        yield (w[:i], w[j:k], w[l:]), (w[i:j], w[k:l])

def plug(ctx, parts):
    out = ctx[0]
    for p, c in zip(parts, ctx[1:]):
        out += p + c
    return out

def one_step(S, ds=(1, 2), interior_nonempty=True):
    """All F[y] not in S with E[x],E[y],F[x] in S, cont(x_j)=cont(y_j)."""
    S = set(S)
    by_ctx = defaultdict(set)      # E -> {x}
    ctxs_of = defaultdict(set)     # x -> {F}
    for w in S:
        for d in ds:
            for E, x in occ(w, d, interior_nonempty):
                by_ctx[E].add(x)
                ctxs_of[x].add(E)
    # x ~ y iff they share a context and have the same componentwise content
    rel = defaultdict(set)
    for E, xs in by_ctx.items():
        groups = defaultdict(list)
        for x in xs:
            groups[tuple(cont(t) for t in x)].append(x)
        for g in groups.values():
            for x in g:
                for y in g:
                    if x != y:
                        rel[x].add(y)
    new = {}
    for x, ys in rel.items():
        for F in ctxs_of[x]:
            for y in ys:
                z = plug(F, y)
                if z not in S and z not in new:
                    new[z] = (x, y, F)
    return new

def check_step(S, E, x, y, F, interior_nonempty=True):
    assert len(E) == len(F) == len(x) + 1 == len(y) + 1 and len(x) in (1, 2)
    assert all(a and b and cont(a) == cont(b) for a, b in zip(x, y))
    if len(x) == 2 and interior_nonempty:
        assert E[1] and F[1]
    for w in (plug(E, x), plug(E, y), plug(F, x)):
        assert w in S, w
    return plug(F, y)

def doubling(es):
    A = {'ab'}
    for e in es:
        A = {u + v for u in A for v in A} | {e}
    return A

def member_doubling(es, n, w, memo=None):
    if memo is None: memo = {}
    key = (n, w)
    if key in memo: return memo[key]
    if n == 0: r = (w == 'ab')
    elif w == es[n - 1]: r = True
    else:
        r = any(member_doubling(es, n - 1, w[:t], memo) and member_doubling(es, n - 1, w[t:], memo)
                for t in range(1, len(w)))
    memo[key] = r
    return r

ok = True
def report(name, cond, extra=''):
    global ok
    ok &= bool(cond)
    print(('PASS ' if cond else 'FAIL ') + name + (('  ' + extra) if extra else ''))

# 1. K is closed (C_1 ∩ C_2), both conventions
K = {'abab', 'abc', 'cab', 'cc', 'ac'}
for ine in (True, False):
    r = one_step(K, (1, 2), ine)
    report(f'K closed, interior_nonempty={ine}', not r, f'new={sorted(r)[:5]}')

# 2. S_k: no one-step short ab word (all arities), 2-step certificate gives 'ba'
for ine in (True, False):
    bad = []
    for k in range(1, 16):
        W = 'a' * k + 'ba'; S = {W, 'c' + 'a' * k + 'b', 'c' + 'a' * (2 * k) + 'b'}
        r = one_step(S, (1, 2), ine)
        if any(set(z) == {'a', 'b'} and len(z) < len(W) for z in r):
            bad.append((k, [z for z in r if set(z) == {'a', 'b'} and len(z) < len(W)][:3]))
    report(f'S_k one-step no shortcut k=1..15, interior_nonempty={ine}', not bad, str(bad[:3]))
for k in range(1, 16):
    W = 'a' * k + 'ba'; S = {W, 'c' + 'a' * k + 'b', 'c' + 'a' * (2 * k) + 'b'}
    T = check_step(S, ('c', ''), ('a' * k + 'b',), ('a' * (2 * k) + 'b',), ('', 'a')); S.add(T)
    z = check_step(S, ('a' * k, ''), (W,), ('ba',), ('', ''))
    assert z == 'ba'
report('S_k two-step certificate -> ba, k=1..15', True)

# 3. Slot transport, generic instances + the A_2 instance
import itertools, random
random.seed(1)
cnt = 0
for p in ['ab', 'a', 'abc', 'ba', 'aab']:
    for beta in ['c', 'cb', 'a', 'acb']:
        for i in range(1, 4):
            for j in range(1, 4):
                n = i + j; M = n + 1
                S = {p * M, p * i + beta + p * j}
                for h in range(1, n):
                    z = check_step(S, ('', p * (M - n), ''), (p * i, p * j), (p * h, p * (n - h)), ('', beta, ''))
                    assert z == p * h + beta + p * (n - h); cnt += 1
report('slot transport lemma 4.1 (instances)', True, f'{cnt} instances')
L2 = doubling(('abc', 'aacb'))
z = check_step(L2, ('', 'ab', ''), ('ab', 'abab'), ('abab', 'ab'), ('', 'c', ''))
report('A_2 not in C_2 (ababcab forced, absent)', z == 'ababcab' and z not in L2)

# 4. Replay the 10 archived m=3 certificates with own checker
CASES = {
 ('c','cc','ccc'): [(('','cc'),('cc',),('c',),('abababab','')),(('','abababc'),('ababab',),('ab',),('','ababababab'))],
 ('c','ac','aac'): [(('','c'),('abababababab',),('ababababa',),('','abab'))],
 ('c','ca','caa'): [(('c',''),('abababababab',),('aabababab',),('','abab'))],
 ('c','cb','cbb'): [(('c',''),('abababababab',),('babababab',),('','abab'))],
 ('c','bc','bbc'): [(('','bc'),('abababababa',),('abababab',),('','babab'))],
 ('c','cab','cabab'): [(('ababababc',''),('abab',),('ab',),('','abababababab'))],
 ('acb','accb','acccb'): [(('ac',''),('cbabababab',),('bababababacb',),('ababa','')),(('','abababababacb'),('abab',),('ab',),('','abababababab'))],
 ('ac','cc','c'): [(('',''),('c',),('cccc',),('ababa','abababab')),(('',''),('ccabababab',),('ababacacac',),('ababacc','')),(('','c'),('ababababaca',),('ababacc',),('','bab')),(('',''),('c',),('cccc',),('ababa','acac')),(('',''),('ababaccc',),('ababaccbab',),('','cacac')),(('ababacc','cacac'),('ababa',),('bab',),('','bababababab'))],
 ('ca','bbc','abc'): [(('',''),('abc',),('ababababbbc',),('bbcab','a')),(('',''),('abc',),('caababbbc',),('bbcab','a')),(('','ababbbca'),('bbcababab',),('bbcabca',),('','ab')),(('',''),('abc',),('bbcabababab',),('bbc','aab')),(('','c'),('ab',),('ababababbb',),('bbcca','ab')),(('','abab'),('caabababab',),('bbcabab',),('bbc','bbab')),(('bbcbbc','ab'),('ababababa',),('ababbb',),('','bababab'))],
 ('cc','ac','c'): [(('abab',''),('ababababcc',),('ababac',),('','cc')),(('',''),('c',),('cccccccc',),('abab','cac')),(('',''),('ababcccccc',),('ababababac',),('','cccac')),(('',''),('ababaccc',),('ababababac',),('abab','cac')),(('','ccac'),('ababababababa',),('abab',),('','bab'))],
}
res = []
for es, steps in CASES.items():
    S = doubling(es)
    for st in steps:
        z = check_step(S, *st); S.add(z)
    res.append((es, len(steps), z, len(z)))
    assert set(z) == {'a', 'b'} and len(z) < 16
report('10 archived certificates replay', True, '; '.join(f'{e}:{l}' for _, _, _, l in res for e in [None])[:0] + str([(r[0], r[1], r[3]) for r in res]))

# 5. L_n two-step certificate, membership by own parser, n=3..9
for n in range(3, 10):
    es = ['abc'] + ['a' * i + 'cb' for i in range(2, n + 1)]
    i = n - 1
    U = 'ab' * (2 ** i - 2); Z = 'abab'; e = 'abc'; beta = 'a' * i + 'cb'; s = 'a'
    memo = {}
    seeds = [beta + beta, beta + U + e, U + Z + U + Z, U + Z + U + e, s + beta]
    assert all(member_doubling(es, n, w, memo) for w in seeds), n
    S = set(seeds)
    z1 = check_step(S, (beta, ''), (beta,), (U + e,), (s, '')); S.add(z1)
    z2 = check_step(S, ('', e), (U + Z + U,), (s + U,), ('', Z))
    assert z2 == 'a' + 'ab' * (2 ** (n - 1)) and len(z2) == 2 ** n + 1
report('L_n two-step shortcut n=3..9 (own membership parser)', True)

# 6. degenerate (c,cc,c) seed set is not closed in one step
r = one_step(doubling(('c', 'cc', 'c')), (1, 2), True)
report('(c,cc,c) m=3 seed set not closed', len(r) > 0, f'{len(r)} new one-step words, e.g. {sorted(r)[0]}')

print('ALL PASS' if ok else 'SOME FAIL')
