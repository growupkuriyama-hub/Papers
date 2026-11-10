"""check_claude_verify_astra_map_2026-11-10.py -- independent checks (Claude, verifying thread)
for astra_fanout2_map_2026-11-10 (Astra's report).  Standard library only; Astra's code not reused.

V1  Theorem G1 at the WORD level: Gamma in {C2, C3, C4, C2xC2, S3}, letters a,b (onto Gamma),
    every nonempty accepting set P.  Content-typed SUB_1 / SUB_2 are tested on all premise
    sentences of length <= LMAX (conclusions by the true membership predicate), and compared
    with G1's prediction "P = pN, N normal, Gamma/N abelian" (SUB_1 alone: "P = pN").
    Bounded premises can only refute, so: predicted-true must give 0 violations;
    predicted-false should give a violation (reported if not found within the bound).
V2  finite languages, all premises enumerated, arities 1-3:
    {aba, cbb, aaa} (B1 without equal types) and {b a^(N-1)}, N = 7, 8, 9 (B7 reversal).
V3  Lemma S1 at the word level (bounded premises) on ordered-stage x abelian-value languages
    different from Astra's: a^+{b,c}^+ with |w|_b = |w|_a (L_inf), a^+b^+c^+ with
    |w|_a = |w|_c, {a,b}^+c^+ with |w|_a - |w|_b = 0 mod 3, and a non-example
    (a+c)^+ b (a+c)^+ type order that is NOT of the form (sanity: violation expected).
V4  thickness and size of the grammar S -> aST | aT, T -> b | cT | Tc (reported 22, 4).
"""
import itertools, sys
from collections import defaultdict

LMAX = 7

def words(alpha, lo, hi):
    for n in range(lo, hi + 1):
        for t in itertools.product(alpha, repeat=n):
            yield ''.join(t)

def occ(w, d):
    n = len(w)
    cuts = itertools.combinations(range(n + 1), 2 * d)
    for c in cuts:
        # components w[c0:c1], w[c2:c3], ...; components nonempty; inner separators nonempty
        if any(c[2*i] == c[2*i+1] for i in range(d)): continue
        if any(c[2*i+1] == c[2*i+2] for i in range(d - 1)): continue
        x = tuple(w[c[2*i]:c[2*i+1]] for i in range(d))
        ctx = (w[:c[0]],) + tuple(w[c[2*i+1]:c[2*i+2]] for i in range(d - 1)) + (w[c[-1]:],)
        yield x, ctx

def fill(ctx, x):
    s = ctx[0]
    for i, xi in enumerate(x): s += xi + ctx[i + 1]
    return s

def sub_violation(pos_words, member, d):
    """content-typed SUB_d: x,y same componentwise content, E[x],E[y],F[x] in L => F[y] in L."""
    by_ctx = defaultdict(set); ctxs = defaultdict(set)
    for w in pos_words:
        for x, ctx in occ(w, d):
            by_ctx[ctx].add(x); ctxs[x].add(ctx)
    done = set()
    for ctx, xs in by_ctx.items():
        groups = defaultdict(list)
        for x in xs: groups[tuple(frozenset(c) for c in x)].append(x)
        for g in groups.values():
            for x, y in itertools.permutations(g, 2):
                if (x, y) in done: continue
                done.add((x, y))
                for F in ctxs[x]:
                    if not member(fill(F, y)):
                        return (x, y, ctx, F)
    return None

# ---------------------------------------------------------------- groups
def perm_mul(p, q): return tuple(p[q[i]] for i in range(len(q)))   # p after q
def make_groups():
    G = []
    for n in (2, 3, 4):
        G.append(('C%d' % n, list(range(n)), lambda x, y, n=n: (x + y) % n, 0, {'a': 1, 'b': 1 % n if n > 2 else 0}))
    G.append(('C2xC2', [(i, j) for i in range(2) for j in range(2)],
              lambda x, y: ((x[0]+y[0]) % 2, (x[1]+y[1]) % 2), (0, 0), {'a': (1, 0), 'b': (0, 1)}))
    S3 = list(itertools.permutations(range(3)))
    G.append(('S3', S3, perm_mul, (0, 1, 2), {'a': (1, 0, 2), 'b': (1, 2, 0)}))
    return G

def g1_prediction(els, mul, e, P):
    inv = {g: next(h for h in els if mul(g, h) == e) for g in els}
    p = next(iter(P))
    N = {mul(inv[p], q) for q in P}
    is_sub = e in N and all(mul(x, y) in N for x in N for y in N)
    normal = is_sub and all(mul(mul(g, n), inv[g]) in N for g in els for n in N)
    coset = normal and {mul(p, n) for n in N} == set(P)
    if not coset: return False, False
    ab = all(mul(mul(mul(x, y), inv[x]), inv[y]) in N for x in els for y in els)
    return True, ab

def V1():
    print('V1 Theorem G1 at word level (premises <= %d letters)' % LMAX)
    for name, els, mul, e, gen in make_groups():
        def val(w):
            v = e
            for ch in w: v = mul(v, gen[ch])
            return v
        allw = list(words('ab', 1, LMAX))
        vals = {w: val(w) for w in allw}
        stats = dict(P=0, agree=0, pred_true_viol=0, pred_false_not_found=0)
        for k in range(1, len(els) + 1):
            for P in itertools.combinations(els, k):
                P = set(P); stats['P'] += 1
                member = lambda w, P=P: len(w) > 0 and val(w) in P
                pos = [w for w in allw if vals[w] in P]
                s1 = sub_violation(pos, member, 1) is None
                s2 = s1 and sub_violation(pos, member, 2) is None
                p1, p12 = g1_prediction(els, mul, e, P)
                if (p1 and not s1) or (p12 and not s2): stats['pred_true_viol'] += 1
                if (not p1 and s1) or (p1 and not p12 and s2): stats['pred_false_not_found'] += 1
                if (s1, s2) == (p1, p12): stats['agree'] += 1
        print('   ', name, stats)

def V2():
    print('V2 finite languages, all premises, arities 1-3')
    for name, L in [('{aba,cbb,aaa}', {'aba', 'cbb', 'aaa'})] + \
                   [('{b a^%d}' % (N - 1), {'b' + 'a' * (N - 1)}) for N in (7, 8, 9)]:
        res = [sub_violation(sorted(L), lambda w: w in L, d) for d in (1, 2, 3)]
        print('   ', name, 'violations by arity:', [r is not None for r in res])
    L = {'aba', 'cbb', 'aaa'}
    print('    untyped scissors: E=_b_ accepts (a,a),(c,b); H=_a_ accepts (a,a); H[(c,b)] =', 'c'+'a'+'b', 'in L:', 'cab' in L)

def stage_ok(w, stages):
    st = [next(i for i, S in enumerate(stages) if ch in S) for ch in w]
    return all(st[i] <= st[i + 1] for i in range(len(st) - 1)) and set(st) == set(range(len(stages)))

def V3():
    print('V3 Lemma S1, bounded premises (<= %d letters)' % LMAX)
    langs = [
        ('a+{b,c}+, #b=#a', lambda w: stage_ok(w, ['a', 'bc']) and w.count('b') == w.count('a')),
        ('a+b+c+, #a=#c', lambda w: stage_ok(w, ['a', 'b', 'c']) and w.count('a') == w.count('c')),
        ('{a,b}+c+, #a-#b=0 mod 3', lambda w: stage_ok(w, ['ab', 'c']) and (w.count('a') - w.count('b')) % 3 == 0),
        ('NOT of the form: #a=#c and b only between', lambda w: w.count('b') == 1 and w.count('a') == w.count('c') > 0
            and w.index('b') not in (0, len(w) - 1) and set(w) == {'a', 'b', 'c'}),
    ]
    allw = list(words('abc', 1, LMAX))
    for name, mem in langs:
        pos = [w for w in allw if mem(w)]
        r = [sub_violation(pos, mem, d) for d in (1, 2)]
        print('   ', name, '| positive words', len(pos), '| violation found (arity 1, 2):', [x is not None for x in r],
              '| e.g.', r[0] or r[1])

def V4():
    # S -> a S T | a T ; T -> b | c T | T c   (fan-out one, so size = sum (1 + #children + |rhs template|) + #nonterminals)
    rules = [('S', 'aST'), ('S', 'aT'), ('T', 'b'), ('T', 'cT'), ('T', 'Tc')]
    size = 2 + sum(1 + sum(ch in 'ST' for ch in r) + len(r) for _, r in rules)
    tau = {'T': 1, 'S': 2}                       # shortest yields: T -> b, S -> a T -> ab
    ctxlen = {'S': 0, 'T': 1}                    # shortest context of T: a_ (S -> aT)
    thick = max(ctxlen[A] + sum(tau[ch] if ch in 'ST' else 1 for ch in r) for A, r in rules)
    print('V4 grammar S_inf: size', size, 'thickness (shortest sentence through each rule, max)', thick)

if __name__ == '__main__':
    V1(); V2(); V3(); V4()
