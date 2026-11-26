#!/usr/bin/env python3
"""Ideal restriction of frame presentations (Proposition prop:ideal, Remark
rem:ideal-examples).  For the strong 1-FCP presentation of L_n by G_n (initial E_n) and
an ideal I of the observer, check that every typed component C_A^{<|} ∩ F_mu, taken
relative to L' = L_n ∩ s^{-1}(I), equals L(G_n,E_i) ∩ F_mu, and the initial one equals L'.
  (A1) s_U (contains a mark), I = {zeta}: L' = M_n, contexts (⌈^{n-i},⌉^{n-i});  n = 2..4.
  (A2) t(w) = min(#⌈(w), 2) with saturating addition, I = {2}: contexts
       (⌈^{n-i},⌉^{n-i}) for i <= n-2 and (⌊, u_{n-1}⌋) for E_{n-1};  n = 3..4.
In both cases the non-initial contexts force I.
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


def check(n, typ, ideal, ctx):
    E = levels(n)
    Ln = E[n]
    Lp = {w for w in Ln if typ(w) in ideal}
    good = True
    for i in range(n):
        c = ctx[i]
        good &= typ(c[0] + c[1]) in ideal           # forcing (the types here absorb into I)
        good &= fillers(Ln, c) == E[i]              # strong 1-FCP of G_n with this context
        for mu in {typ(x) for x in E[i]}:
            fib = {x for x in E[i] if typ(x) == mu}
            good &= {x for x in fillers(Lp, c) if typ(x) == mu} == fib
    good &= {x for x in fillers(Lp, ('', '')) if typ(x) in ideal} == Lp
    return good, len(Lp)


def main():
    ok = True
    sU = lambda w: 'Z' if ('{' in w or '}' in w) else '1'
    for n in range(2, 5):
        ctx = {i: ('{' * (n - i), '}' * (n - i)) for i in range(n)}
        g, size = check(n, sU, {'Z'}, ctx)
        g &= {w for w in levels(n)[n] if sU(w) == 'Z'} == levels(n)[n] - {wstar(n)}
        print(f'(A1) n={n}: M_n = L_n ∩ s_U^-1(zeta) has the typed strong 1-FCP with the contexts of G_n: {g} (|L\'|={size})')
        ok &= g
    t = lambda w: min(w.count('{'), 2)
    for n in range(3, 5):
        ctx = {i: ('{' * (n - i), '}' * (n - i)) for i in range(n - 1)}
        ctx[n - 1] = ('[', u(n - 1) + ']')
        g, size = check(n, t, {2}, ctx)
        print(f'(A2) n={n}: at least two marks has the typed strong 1-FCP, contexts <= {2 * n + 1}: {g} (|L\'|={size})')
        ok &= g
    print('ALL OK' if ok else 'SOME CHECK FAILED')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
