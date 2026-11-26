#!/usr/bin/env python3
"""Length-parity typing on L_n (Remark rem:Ln-sU).

p(w) = |w| mod 2 is a typing onto the group of order two.  Check, relative to L_n, that
for every level i and parity t with a nonempty fibre, the typed closure of the single
kernel word (u_i for odd, ⌊u_{i-1}u_{i-1}⌋ for even) is exactly L(G_n,E_i) ∩ F_t, i.e. the
parity refinement of G_n has the typed strong 1-FKP with kernels of length <= 4n.
Encoding: a, ⌊ -> '[', ⌋ -> ']', ⌈ -> '{', ⌉ -> '}'.
Usage: python3 -I check_parity_typing.py [N]   (default N = 4)
"""
import sys


def levels(n):
    E = [{'a'}]
    for _ in range(n):
        p = E[-1]
        E.append({'[' + x + y + ']' for x in p for y in p} | {'{' + x + '}' for x in p})
    return E


def u(i):
    return '{' * i + 'a' + '}' * i


def contexts(L):
    D = {}
    for m in L:
        for i in range(len(m)):
            for j in range(i + 1, len(m) + 1):
                D.setdefault(m[i:j], set()).add((m[:i], m[j:]))
    return D


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    ok = True
    for n in range(1, N + 1):
        E = levels(n)
        D = contexts(E[n])
        res = []
        for i in range(n + 1):
            for t in (1, 0):
                fibre = {w for w in E[i] if len(w) % 2 == t}
                if not fibre:
                    continue
                rep = u(i) if t == 1 else '[' + u(i - 1) + u(i - 1) + ']'
                C = D[rep]
                closure = {x for x, Cx in D.items() if C <= Cx and len(x) % 2 == t}
                good = rep in fibre and closure == fibre and len(rep) <= 4 * n
                res.append(good)
        print(f'n={n}: parity-typed strong 1-FKP with short kernels: {all(res)} ({len(res)} typed nonterminals)')
        ok &= all(res)
    print('ALL OK' if ok else 'SOME CHECK FAILED')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
