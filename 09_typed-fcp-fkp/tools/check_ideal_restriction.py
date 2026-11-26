#!/usr/bin/env python3
"""Ideal restriction of frame presentations (Proposition prop:ideal, Remark
rem:ideal-examples).  For the strong 1-FCP presentation of L_n by G_n (initial E_n) and
an ideal I of the observer, check that every typed component C_A^{<|} ∩ F_mu, taken
relative to L' = L_n ∩ s^{-1}(I), equals L(G_n,E_i) ∩ F_mu, and the initial one equals L'.
  (A1) s_U (contains a mark), I = {zeta}: L' = M_n, contexts (⌈^{n-i},⌉^{n-i});  n = 2..4.
  (A2) t(w) = min(#⌈(w), 2) with saturating addition, I = {2}: contexts
       (⌈^{n-i},⌉^{n-i}) for i <= n-2 and (⌊, u_{n-1}⌋) for E_{n-1};  n = 3..4.
In both cases the non-initial contexts force I; forcing is tested against every
type mu of S^# (s(u) mu s(v) in I), not only against s(uv).
  (R) Regression test for the deletion in Proposition prop:ideal: for S -> a | b with
      the context (eps,eps) and the indicator of b, keeping the excluded copy (S,1)
      of the old initial breaks the pre-fixed point; deleting it, as the proposition
      now requires, gives a typed strong presentation.  The same generic check of the
      whole refined grammar G' is run for (A1) n = 2, 3 and (A2) n = 3.
Encoding: a, ⌊ -> '[', ⌋ -> ']', ⌈ -> '{', ⌉ -> '}'.
Usage: python3 -I check_ideal_restriction.py
"""
import sys


def levels(n):
    E = [{'a'}]
    for _ in range(n):
        p = E[-1]
        E.append({'[' + x + y + ']' for x in p for y in p} | {'{' + x + '}' for x in p})
    return E


def wstar(i):
    w = 'a'
    for _ in range(i):
        w = '[' + w + w + ']'
    return w


def u(i):
    return '{' * i + 'a' + '}' * i


def fillers(L, c):
    p, q = c
    return {m[len(p):len(m) - len(q)] for m in L
            if len(m) >= len(p) + len(q) and m.startswith(p) and m.endswith(q)}


def check(n, typ, ideal, ctx, op=None, types=()):
    E = levels(n)
    Ln = E[n]
    Lp = {w for w in Ln if typ(w) in ideal}
    good = True
    for i in range(n):
        c = ctx[i]
        tp, tq = typ(c[0]) if c[0] else 'e', typ(c[1]) if c[1] else 'e'
        mul = lambda x, y: x if y == 'e' else (y if x == 'e' else op(x, y))
        good &= all(mul(mul(tp, m), tq) in ideal for m in list(types) + ['e'])   # forcing
        good &= fillers(Ln, c) == E[i]              # strong 1-FCP of G_n with this context
        for mu in {typ(x) for x in E[i]}:
            fib = {x for x in E[i] if typ(x) == mu}
            good &= {x for x in fillers(Lp, c) if typ(x) == mu} == fib
    good &= {x for x in fillers(Lp, ('', '')) if typ(x) in ideal} == Lp
    return good, len(Lp)


# ---------- generic check of the refined grammar G' of Proposition prop:ideal ----------
from itertools import product as _prod

def word_type(w, typ):
    return 'e' if w == '' else typ(w)

def lang_of(G, A, memo):
    if A in memo:
        return memo[A]
    out = set()
    for rhs in G[A]:
        parts = [lang_of(G, x, memo) if x in G else {x} for x in rhs]
        out |= {''.join(c) for c in _prod(*parts)}
    memo[A] = out
    return out

def refined_ok(G, init, ctx, typ, op, S_types, ideal, delete=True):
    memo = {}
    L = set().union(*(lang_of(G, S, memo) for S in init))
    Lp = {w for w in L if word_type(w, typ) in ideal}
    def tmul(*ts):
        r = 'e'
        for x in ts:
            r = x if r == 'e' else (r if x == 'e' else op(r, x))
        return r
    # refined productions (A, mu) -> rhs with typed nonterminals
    prods = []
    for A in G:
        for rhs in G[A]:
            choices = []
            for x in rhs:
                if x in G:
                    choices.append([(x, m) for m in {word_type(y, typ) for y in lang_of(G, x, memo)}])
                else:
                    choices.append([x])
            for ch in _prod(*choices):
                mu = tmul(*[c[1] if isinstance(c, tuple) else word_type(c, typ) for c in ch])
                prods.append(((A, mu), ch))
    if delete:
        prods = [pr for pr in prods if not (pr[0][0] in init and pr[0][1] not in ideal)]
    N = {pr[0] for pr in prods}
    def comp(Am):
        A, mu = Am
        cand = {m[i:j] for m in Lp for i in range(len(m) + 1) for j in range(i, len(m) + 1)}
        return {x for x in cand if word_type(x, typ) == mu
                and all(u + x + v in Lp for (u, v) in ctx[A])}
    X = {Am: comp(Am) for Am in N}
    ok = True
    for lhs, ch in prods:
        parts = [X[c] if isinstance(c, tuple) else {c} for c in ch]
        ok &= all(''.join(c) in X[lhs] for c in _prod(*parts))
    ok &= all(X[(S, m)] <= Lp for (S, m) in N if S in init)
    # the generated language is L'
    gen = {}
    def lang2(Am):
        if Am in gen:
            return gen[Am]
        out = set()
        for lhs, ch in prods:
            if lhs == Am:
                parts = [lang2(c) if isinstance(c, tuple) else {c} for c in ch]
                out |= {''.join(c) for c in _prod(*parts)}
        gen[Am] = out
        return out
    ok &= set().union(*(lang2((S, m)) for (S, m) in N if S in init and m in ideal)) == Lp
    return ok

def Gn(n):
    G = {'E0': [('a',)]}
    for i in range(1, n + 1):
        G[f'E{i}'] = [('[', f'E{i-1}', f'E{i-1}', ']'), ('{', f'E{i-1}', '}')]
    return G

def regression():
    ok = True
    ind_b = lambda w: 'Z' if 'b' in w else '1'
    orU = lambda x, y: 'Z' if 'Z' in (x, y) else '1'
    G = {'S': [('a',), ('b',)]}
    ctx = {'S': [('', '')]}
    kept = refined_ok(G, {'S'}, ctx, ind_b, orU, ['1', 'Z'], {'Z'}, delete=False)
    fixed = refined_ok(G, {'S'}, ctx, ind_b, orU, ['1', 'Z'], {'Z'}, delete=True)
    print(f'(R) S->a|b: SPP with the excluded copy kept: {kept} (must be False); after deletion: {fixed}')
    ok &= (not kept) and fixed
    sU = lambda w: 'Z' if ('{' in w or '}' in w) else '1'
    for n in (2, 3):
        ctx = {f'E{i}': [('{' * (n - i), '}' * (n - i))] for i in range(n)}
        ctx[f'E{n}'] = [('', '')]
        g = refined_ok(Gn(n), {f'E{n}'}, ctx, sU, orU, ['1', 'Z'], {'Z'})
        print(f'(R) A1 n={n}: the whole refined grammar G\' is a typed SPP generating M_n: {g}')
        ok &= g
    t = lambda w: min(w.count('{'), 2)
    sat = lambda x, y: min(x + y, 2)
    n = 3
    ctx = {f'E{i}': [('{' * (n - i), '}' * (n - i))] for i in range(n - 1)}
    ctx[f'E{n-1}'] = [('[', u(n - 1) + ']')]
    ctx[f'E{n}'] = [('', '')]
    g = refined_ok(Gn(n), {f'E{n}'}, ctx, t, sat, [0, 1, 2], {2})
    print(f'(R) A2 n=3: the whole refined grammar G\' is a typed SPP: {g}')
    ok &= g
    return ok


def main():
    ok = True
    sU = lambda w: 'Z' if ('{' in w or '}' in w) else '1'
    for n in range(2, 5):
        ctx = {i: ('{' * (n - i), '}' * (n - i)) for i in range(n)}
        g, size = check(n, sU, {'Z'}, ctx, lambda x, y: 'Z' if 'Z' in (x, y) else '1', ['1', 'Z'])
        g &= {w for w in levels(n)[n] if sU(w) == 'Z'} == levels(n)[n] - {wstar(n)}
        print(f'(A1) n={n}: M_n = L_n ∩ s_U^-1(zeta) has the typed strong 1-FCP with the contexts of G_n: {g} (|L\'|={size})')
        ok &= g
    t = lambda w: min(w.count('{'), 2)
    for n in range(3, 5):
        ctx = {i: ('{' * (n - i), '}' * (n - i)) for i in range(n - 1)}
        ctx[n - 1] = ('[', u(n - 1) + ']')
        g, size = check(n, t, {2}, ctx, lambda x, y: min(x + y, 2), [0, 1, 2])
        print(f'(A2) n={n}: at least two marks has the typed strong 1-FCP, contexts <= {2 * n + 1}: {g} (|L\'|={size})')
        ok &= g
    ok &= regression()
    print('ALL OK' if ok else 'SOME CHECK FAILED')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
