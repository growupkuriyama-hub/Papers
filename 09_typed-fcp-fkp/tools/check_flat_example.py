#!/usr/bin/env python3
"""Example ex:flat: the flat family M^flat_n = L^flat_n minus {a^(2^n)}, with
B_i = {a,b}^(2^i), t_i = #a^i#, L^flat_n = B_n ∪ U_i t_i B_i (0 <= i <= n).
Checks, exhaustively for n = 1..N (default 3):
  (i)   the contexts (t_i,eps) for A_i and (eps,eps) for S give the strong 1-FCP of
        L^flat_n; they force {zeta} for s_flat (b or # occurs); W_n is the only word of
        type 1; relative to M^flat_n the typed components equal the typed yields
        (the presentation of Proposition prop:ideal), and its total length;
  (ii)  Lemma lem:one-word with R = a^(2^n-1), T = b, T° = a, and condition (4.1);
  (iii) the frame argument: for z_i = a^i b a^(2^n-1-i) and every factor x containing
        the b, every context accepting x and rejecting x' (b -> a) completes x' to
        W_n; and the mixed words a^i b a^(2^n-1-i') lie in M^flat_n only for i = i'.
Usage: python3 -I check_flat_example.py [N]
"""
import sys
from itertools import product


def langs(n):
    B = [{''.join(w) for w in product('ab', repeat=2 ** i)} for i in range(n + 1)]
    t = ['#' + 'a' * i + '#' for i in range(n + 1)]
    L = set(B[n]) | {t[i] + x for i in range(n + 1) for x in B[i]}
    return B, t, L


def fillers(L, u, v):
    return {m[len(u):len(m) - len(v)] for m in L
            if len(m) >= len(u) + len(v) and m.startswith(u) and m.endswith(v)}


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    ok = True
    sf = lambda w: 'Z' if ('b' in w or '#' in w) else '1'
    for n in range(1, N + 1):
        B, t, L = langs(n)
        W = 'a' * 2 ** n
        M = L - {W}
        # (i)
        g1 = all(fillers(L, t[i], '') == B[i] for i in range(n + 1))
        g1 &= all(sf(t[i]) == 'Z' for i in range(n + 1))
        g1 &= {w for w in L if sf(w) == '1'} == {W}
        for i in range(n + 1):
            for mu in ('1', 'Z'):
                g1 &= {x for x in fillers(M, t[i], '') if sf(x) == mu} == {x for x in B[i] if sf(x) == mu}
        g1 &= {x for x in fillers(M, '', '') if sf(x) == 'Z'} == M
        # total length of the typed presentation: types of A_i are 1 (a-words) and Z
        prods = 2                                   # (A_0,1)->a, (A_0,Z)->b
        prods_len = 2 * 2
        for i in range(1, n + 1):                   # (A_i,mu)->(A_{i-1},.)(A_{i-1},.): 4 instances
            prods += 4
            prods_len += 4 * 3
        for i in range(n + 1):                      # (S,Z)->t_i(A_i,mu) for both mu, and (S,Z)->(A_n,Z)
            prods += 2
            prods_len += 2 * (len(t[i]) + 2)
        prods += 1
        prods_len += 3
        ctx_len = sum((len(t[i]) + 1) * 2 for i in range(n + 1)) + 1
        total = prods_len + ctx_len
        # (ii)
        R, T, To = 'a' * (2 ** n - 1), 'b', 'a'
        g2 = R + T in L and R + To == W
        g2 &= all(m[:-1] + To in L for m in L if m.endswith(T))
        g2 &= {m[:-1] for m in M if m.endswith(T) and m[:-1] + To not in M} == {R}
        # (iii)
        g3 = True
        cnt = 0
        for i in range(2 ** n):
            z = 'a' * i + 'b' + 'a' * (2 ** n - 1 - i)
            g3 &= z in M
            for lo in range(i + 1):
                for hi in range(i + 1, len(z) + 1):
                    x = z[lo:hi]
                    xp = x[:i - lo] + 'a' + x[i - lo + 1:]
                    for m in M:
                        for k in range(len(m) - len(x) + 1):
                            if m[k:k + len(x)] == x:
                                u, v = m[:k], m[k + len(x):]
                                if u + xp + v not in M:
                                    cnt += 1
                                    g3 &= u + xp + v == W
        g3 &= all((('a' * i + 'b' + 'a' * (2 ** n - 1 - j)) in M) == (i == j)
                  for i in range(2 ** n) for j in range(2 ** n))
        print(f'n={n}: |M|={len(M)} (i) strong 1-FCP, forcing, typed presentation: {g1}, '
              f'total length {total}; (ii) |R|={len(R)}: {g2}; (iii) rejecting contexts {cnt}, mixing: {g3}')
        ok &= g1 and g2 and g3
    print('ALL OK' if ok else 'SOME CHECK FAILED')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
