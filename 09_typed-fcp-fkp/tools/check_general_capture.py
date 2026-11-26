#!/usr/bin/env python3
"""General kernel capture for one-word deletions (Lemmas lem:capture, lem:one-word;
Theorems thm:general-lower, thm:deletion) on M_n = L_n \\ {w*_n}.

T° = ⌊aa⌋⌋^{n-1} (the last E_1-node of w*_n and the closing brackets after it),
T  = ⌈a⌉⌋^{n-1}, w*_n = R T°, z = R T, |R| = 3*2^n - n - 5.
Checks, exhaustively for n = 2..N:
  (1) condition (eq:capture): {R' : R'T in M_n, R'T° not in M_n} = {R};
  (2) the left-context inheritance of Lemma lem:one-word: yT in L_n => yT° in L_n;
  (3) capture: for every occurrence x inside R (including empty ones) with context
      (p,q), and every e with p e q in M_n:  p e q' in M_n  <=>  e != x,
      where q' is q with the suffix T replaced by T°.
Encoding: a, ⌊ -> '[', ⌋ -> ']', ⌈ -> '{', ⌉ -> '}'.
Usage: python3 -I check_general_capture.py [N]   (default N = 4)
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


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    ok = True
    for n in range(2, N + 1):
        Ln = levels(n)[n]
        Mn = Ln - {wstar(n)}
        W = wstar(n)
        To = '[aa]' + ']' * (n - 1)
        T = '{a}' + ']' * (n - 1)
        R = W[:len(W) - len(To)]
        z = R + T
        good = W.endswith(To) and z in Mn and len(R) == 3 * 2 ** n - n - 5
        cond = {m[:len(m) - len(T)] for m in Mn
                if m.endswith(T) and m[:len(m) - len(T)] + To not in Mn} == {R}
        inherit = all(m[:len(m) - len(T)] + To in Ln for m in Ln if m.endswith(T))
        cap, cnt = True, 0
        for i in range(len(R) + 1):
            for j in range(i, len(R) + 1):
                p, x, q = z[:i], z[i:j], z[j:]
                qp = q[:len(q) - len(T)] + To
                for m in Mn:
                    if len(m) >= len(p) + len(q) and m.startswith(p) and m.endswith(q):
                        e = m[len(p):len(m) - len(q)]
                        cnt += 1
                        cap &= ((p + e + qp) in Mn) == (e != x)
        print(f'n={n}: |R|={len(R)} (3*2^n-n-5={3 * 2 ** n - n - 5}), condition (eq:capture): {cond}, '
              f'inheritance: {inherit}, capture over {cnt} triples: {cap}')
        ok &= good and cond and inherit and cap
    print('ALL OK' if ok else 'SOME CHECK FAILED')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
