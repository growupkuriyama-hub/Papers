#!/usr/bin/env python3
"""The untyped frame grammar F_n for M_n (Proposition prop:untyped-frames).

Encoding: a -> 'a',  ⌊ -> '[',  ⌋ -> ']',  ⌈ -> '{',  ⌉ -> '}'.
F_n: nonterminals E_0..E_{n-1} with the productions of G_n, initial S, and S -> T_pi
for every path pi in {l,r}^d, 0 <= d <= n-1, where T_d = ⌈E_{n-d-1}⌉ and
T_{j-1} = ⌊T_j E_{n-j}⌋ (pi_j = l) or ⌊E_{n-j} T_j⌋ (pi_j = r).
Checks, for n = 1..N (exact, all languages finite):
  (1) L(F_n, S) = M_n;
  (2) relative to M_n: {(⌈^{n-k}, ⌉^{n-k})}^{<|} = L(G_n, E_k) for k < n, and
      {(λ,λ)}^{<|} = M_n  (strong 1-FCP with contexts of length <= 2n);
  (3) |N| = n+1, number of productions = 2^n + 2n - 2, rho = 3n.
  (4) total lengths (Definition def:presentation, Theorem thm:observer(d)):
      F_n with its frames, H_n with its exemplars {w*_i},{u_i}, and the s_U-typed
      H_n with its frames; printed with the ratios to n*2^n, 2^n and n^2.
Usage: python3 -I check_untyped_frames.py [N]   (default N = 5)
"""
import itertools
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


def fillers(L, c):
    p, q = c
    return {m[len(p):len(m) - len(q)] for m in L
            if len(m) >= len(p) + len(q) and m.startswith(p) and m.endswith(q)}


def root_rhs(n):
    out = []
    for d in range(n):
        for pi in itertools.product('lr', repeat=d):
            T = ['{', ('E', n - d - 1), '}']
            for j in range(d, 0, -1):
                sib = ('E', n - j)
                T = ['['] + (T + [sib] if pi[j - 1] == 'l' else [sib] + T) + [']']
            out.append(T)
    return out


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    ok = True
    for n in range(1, N + 1):
        E = levels(n)
        M = E[n] - {wstar(n)}
        rhs = root_rhs(n)
        LS = set()
        for T in rhs:
            words = {''}
            for sym in T:
                words = {w + x for w in words for x in (E[sym[1]] if isinstance(sym, tuple) else [sym])}
            LS |= words
        frames = all(fillers(M, ('{' * (n - k), '}' * (n - k))) == E[k] for k in range(n)) \
            and fillers(M, ('', '')) == M
        nprod = len(rhs) + 1 + 2 * (n - 1)
        rho = max([len(T) for T in rhs] + ([4] if n > 1 else [1]))
        good = LS == M and frames and nprod == 2 ** n + 2 * n - 2 and rho == 3 * n
        print(f'n={n}: L(F_n)=M_n: {LS == M}, strong 1-FCP: {frames}, |N|={n + 1}, '
              f'productions={nprod} (2^n+2n-2={2 ** n + 2 * n - 2}), rho={rho}, |M_n|={len(M)}')
        # (4) total lengths
        pE = 2 + sum(5 + 4 for _ in range(1, n))
        tot_F = sum(len(T) + 1 for T in rhs) + pE + sum(2 * (n - k) + 1 for k in range(n)) + 1
        pH = 2 + 5 * (n - 1) + 4 + (5 * 3 + 4 * 2) * (n - 1)
        tot_H_ex = pH + sum(len(wstar(i)) + 1 for i in range(n)) + sum(2 * i + 2 for i in range(1, n + 1))
        # contexts: (E_0,1) has length 2n; (E_i,1),(E_i,zeta) for 1<=i<n have 2(n-i);
        # the root (E_n,zeta) has (lambda,lambda); each context costs length+1
        tot_H_fr = pH + (2 * n + 1) + 2 * sum(2 * (n - i) + 1 for i in range(1, n)) + 1
        if n >= 2:
            good &= tot_H_fr == 2 * n * n + 30 * n - 22
        print(f'      total length: F_n frames {tot_F} (/n2^n={tot_F / (n * 2 ** n):.2f}), '
              f'H_n exemplars {tot_H_ex} (/2^n={tot_H_ex / 2 ** n:.2f}), '
              f'typed H_n frames {tot_H_fr} (/n^2={tot_H_fr / n ** 2:.2f})')
        ok &= good
    print('ALL OK' if ok else 'SOME CHECK FAILED')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
