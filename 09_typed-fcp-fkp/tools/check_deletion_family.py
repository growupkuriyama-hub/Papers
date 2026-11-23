#!/usr/bin/env python3
"""Finite checks for the bracketed doubling family L_n (from #1, Sec. 6) and
its one-word deletion M_n = L_n \\ {w*_n}.

Encoding of the alphabet Gamma_br = {a, floor-open, floor-close, ceil-open, ceil-close}:
    a -> 'a',  ⌊ -> '[',  ⌋ -> ']',  ⌈ -> '{',  ⌉ -> '}'.
The U1 typing s_U sends a,[,] to 1 and {,} to zeta: type(w) = 'Z' iff w contains '{'.

Checks (all exact, the languages are finite):
  (A) L_n: {u_i}^{|><|} = L(E_i) and {(⌈^{n-i},⌉^{n-i})}^{<|} = L(E_i)
      (strong 1-FKP and strong 1-FCP of G_n with short witnesses).
  (B) M_n: the s_U-typed grammar with nonterminals (E_i,1), (E_i,Z) has the typed
      strong 1-FCP with contexts (⌈^{n-i},⌉^{n-i}) and (λ,λ).
  (C) Kernel-capture lemma for M_n: for z = ⌊ w*_{n-1} u_{n-1} ⌋, every occurrence x
      inside R = ⌊ w*_{n-1} with context (p,q), and every k with p k q in M_n:
      p k q' in M_n  <=>  k != x,   where q' = q with u_{n-1} replaced by w*_{n-1}.
  (D) Refutation lemma: for the level-(n-1) context c taken from a datum, the typed set
      c^{<|} ∩ F_1 is the singleton {w*_{n-1}}.
Usage: python3 -I check_deletion_family.py [nmax]
"""
import sys


def levels(n):
    E = [{'a'}]
    for i in range(1, n + 1):
        prev = E[-1]
        E.append({'[' + x + y + ']' for x in prev for y in prev} | {'{' + x + '}' for x in prev})
    return E


def wstar(i):
    w = 'a'
    for _ in range(i):
        w = '[' + w + w + ']'
    return w


def u(i):
    return '{' * i + 'a' + '}' * i


def typ(w):
    if w == '':
        return 'e'
    return 'Z' if '{' in w else '1'


def ctx_closure(L, contexts):
    """C^{<|} restricted to factors (exact for nonempty C over a finite L)."""
    res = None
    for (p, q) in contexts:
        S = {m[len(p):len(m) - len(q)] for m in L
             if len(m) >= len(p) + len(q) and m.startswith(p) and m.endswith(q)}
        res = S if res is None else (res & S)
    return res


def dist(L, x):
    out = set()
    for m in L:
        start = m.find(x)
        while start != -1:
            out.add((m[:start], m[start + len(x):]))
            start = m.find(x, start + 1)
    if x == '':
        for m in L:
            for i in range(len(m) + 1):
                out.add((m[:i], m[i:]))
    return out


def check(n):
    E = levels(n)
    Ln = E[n]
    ws = wstar(n)
    assert ws in Ln
    Mn = Ln - {ws}
    ok = True
    # (A)
    for i in range(0, n + 1):
        K = u(i)
        D = dist(Ln, K)
        cl = ctx_closure(Ln, D)
        if cl != E[i]:
            print(f'  (A) kernel FAIL n={n} i={i}'); ok = False
        c = ('{' * (n - i), '}' * (n - i))
        if ctx_closure(Ln, [c]) != E[i]:
            print(f'  (A) context FAIL n={n} i={i}'); ok = False
    # (B)
    for i in range(0, n):
        c = ('{' * (n - i), '}' * (n - i))
        cl = ctx_closure(Mn, [c])
        one = {x for x in cl if typ(x) == '1'}
        zet = {x for x in cl if typ(x) == 'Z'}
        if one != {wstar(i)} or zet != E[i] - {wstar(i)}:
            print(f'  (B) FAIL n={n} i={i}'); ok = False
    top = ctx_closure(Mn, [('', '')])
    if {x for x in top if typ(x) == 'Z'} != Mn or any(typ(x) == '1' for x in top):
        print('  (B) top FAIL'); ok = False
    # (C)
    z = '[' + wstar(n - 1) + u(n - 1) + ']'
    assert z in Mn
    r = 1 + len(wstar(n - 1))
    tested = 0
    for a_ in range(0, r):
        for b_ in range(a_ + 1, r + 1):
            p, x, q = z[:a_], z[a_:b_], z[b_:]
            q2 = q[:len(q) - len(u(n - 1)) - 1] + wstar(n - 1) + ']'
            assert p + x + q2 == ws
            for m in Mn:
                if len(m) >= len(p) + len(q) and m.startswith(p) and m.endswith(q):
                    k = m[len(p):len(m) - len(q)]
                    tested += 1
                    if ((p + k + q2) in Mn) != (k != x):
                        print(f'  (C) FAIL n={n} x={x} k={k}'); ok = False
    # (D)
    for c in [('{', '}'), ('[', u(n - 1) + ']'), ('[' + u(n - 1), ']')]:
        cl = ctx_closure(Mn, [c])
        one = {x for x in cl if typ(x) == '1'}
        if one != {wstar(n - 1)}:
            print(f'  (D) FAIL n={n} c={c}'); ok = False
    print(f'n={n}: |L_n|={len(Ln)}, |w*|={len(ws)}, capture pairs tested={tested}, '
          f'{"all checks passed" if ok else "FAILURES"}')
    return ok


if __name__ == '__main__':
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    allok = all(check(n) for n in range(2, nmax + 1))
    sys.exit(0 if allok else 1)
