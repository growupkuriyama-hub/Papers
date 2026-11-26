#!/usr/bin/env python3
"""Finite check of Proposition 4.2(c) (exemplar upper bound for M_n).

Encoding: a -> 'a', floor brackets -> '[' ']', ceiling brackets -> '{' '}'.
For n = 2..N (default 4) it checks, relative to M_n = L_n minus {w*_n}:
  * {w*_i}^{RL} = L(G_n, E_i)                       (0 <= i < n)
  * {u_i}^{RL}  = L(G_n, E_i) minus {w*_i}           (1 <= i <= n)
  * hence the typed closures equal the yields of H_n (typed strong 1-FKP),
  * the untyped family is a pre-fixed point of H_n and sound,
  * kappa = max(3*2^(n-1)-2, 2n+1), |N| = 2n, rho = 4, and, with the lower bound of
    Theorem thm:deletion, 3*2^n-n-5 <= rho*|N|*kappa <= 8n*kappa.
Usage: python3 -I tools/check_exemplar_upper.py [N]
"""
import sys


def levels(n):
    E = [{'a'}]
    for _ in range(n):
        prev = E[-1]
        E.append({'[' + x + y + ']' for x in prev for y in prev}
                 | {'{' + x + '}' for x in prev})
    return E


def wstar(i):
    w = 'a'
    for _ in range(i):
        w = '[' + w + w + ']'
    return w


def u(i):
    return '{' * i + 'a' + '}' * i


def marked(w):
    return '{' in w


def contexts(lang, x):
    out = set()
    for m in lang:
        k = m.find(x)
        while k != -1:
            out.add((m[:k], m[k + len(x):]))
            k = m.find(x, k + 1)
    return out


def closure(lang, kernel):
    """kernel^{RL} relative to the finite language lang (kernel nonempty)."""
    ctx = set.intersection(*(contexts(lang, x) for x in kernel))
    result = None
    for p, q in ctx:
        fit = {m[len(p):len(m) - len(q)] for m in lang
               if len(m) >= len(p) + len(q) and m.startswith(p) and m.endswith(q)}
        result = fit if result is None else result & fit
    return result


def check(n):
    E = levels(n)
    Mn = E[n] - {wstar(n)}
    ok = True
    X = {}
    for i in range(n):
        c = closure(Mn, {wstar(i)})
        ok &= c == E[i]
        ok &= {x for x in c if not marked(x)} == {wstar(i)}
        X[(i, 1)] = c
    for i in range(1, n + 1):
        c = closure(Mn, {u(i)})
        ok &= c == E[i] - {wstar(i)}
        ok &= all(marked(x) for x in c)
        X[(i, 'z')] = c
    # productions of H_n
    yields = {(i, 1): {wstar(i)} for i in range(n)}
    yields.update({(i, 'z'): E[i] - {wstar(i)} for i in range(1, n + 1)})
    prods = [((0, 1), ['a'])]
    for i in range(1, n):
        prods.append(((i, 1), ['[', (i - 1, 1), (i - 1, 1), ']']))
    for i in range(1, n + 1):
        for x in (1, 'z'):
            if (i - 1, x) not in yields:
                continue
            prods.append(((i, 'z'), ['{', (i - 1, x), '}']))
            for y in (1, 'z'):
                if (x, y) != (1, 1) and (i - 1, y) in yields:
                    prods.append(((i, 'z'), ['[', (i - 1, x), (i - 1, y), ']']))
    for lhs, rhs in prods:
        words = {''}
        for sym in rhs:
            words = {w + t for w in words
                     for t in (X[sym] if isinstance(sym, tuple) else {sym})}
        ok &= words <= X[lhs]
    ok &= X[(n, 'z')] <= Mn
    kappa = max(len(wstar(n - 1)), len(u(n)))
    ok &= kappa == max(3 * 2 ** (n - 1) - 2, 2 * n + 1)
    rho = max(len(r) for _, r in prods)
    N = len(yields)
    ok &= N == 2 * n and rho == 4 and len(prods) == 6 * n - 4
    low = 3 * 2 ** n - n - 5          # Theorem thm:deletion
    ok &= low <= rho * N * kappa <= 8 * n * kappa
    print(f"n={n}: |N|={N} productions={len(prods)} rho={rho} kappa={kappa} "
          f"rho*|N|*kappa={rho * N * kappa} lower bound={low}: "
          f"{'pass' if ok else 'FAIL'}")
    return ok


if __name__ == '__main__':
    top = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    results = [check(n) for n in range(2, top + 1)]
    print('all checks passed' if all(results) else 'SOME CHECK FAILED')
    sys.exit(0 if all(results) else 1)
