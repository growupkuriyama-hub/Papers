#!/usr/bin/env python3
"""Characteristic samples of M_n = L_n \\ {w*_n} for Rec_{s_U} (Remark rem:rec-data),
and the listing presentation of M_n (paragraph after Theorem thm:deletion).

Encoding: a -> 'a',  ⌊ -> '[',  ⌋ -> ']',  ⌈ -> '{',  ⌉ -> '}'.
s_U(w) = 'Z' iff w contains '{', else '1'.

Rec_s(K) (#1, Sec. 4.1; Section 5 of this paper): a nonterminal [[x]] for every nonempty
factor x of K, and productions
  (B) [[xy]] -> [[x]][[y]],   (U) [[x]] -> [[y]] for s(x)=s(y) and D_K(x) ∩ D_K(y) ≠ ∅,
  (L) [[a]] -> a,             (S) start -> [[w]] for w in K.
The language is computed exactly as a least fixpoint (all languages are finite).

Checks:
  (1) n=3: the 11-word sample K3 below satisfies L(Rec(K3)) = M_3 (no missing and no
      extra words), and no word of K3 contains the factor w*_2.
  (2) n=2,3: the least L such that {w in M_n : |w| <= L} is characteristic
      (9 and 16).  Rec is monotone in the sample, so every characteristic sample
      contains a word of length at least this L.
  (3) n=2: the only characteristic sample is M_2 itself.
  (4) n=2..4: the listing grammar S -> w (w in M_n) with kernel {u_n} has the strong
      1-FKP ({u_n}^{|><|} = M_n), and its longest right-hand side is 3*2^n - 3.
Usage: python3 -I check_rec_samples.py
"""
import itertools


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


def sU(w):
    return 'Z' if '{' in w else '1'


def contexts(K):
    ctx = {}
    for w in K:
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                ctx.setdefault(w[i:j], set()).add((w[:i], w[j:]))
    return ctx


def rec_language(K, maxlen):
    ctx = contexts(K)
    F = list(ctx)
    unit = {x: [y for y in F if y != x and sU(y) == sU(x) and ctx[x] & ctx[y]] for x in F}
    split = {x: [(x[:k], x[k:]) for k in range(1, len(x))] for x in F}
    Y = {x: ({x} if len(x) == 1 else set()) for x in F}
    changed = True
    while changed:
        changed = False
        for x in F:
            new = set(Y[x])
            for p, q in split[x]:
                for a in Y[p]:
                    for b in Y[q]:
                        if len(a) + len(b) <= maxlen:
                            new.add(a + b)
            for y in unit[x]:
                new |= Y[y]
            if new != Y[x]:
                Y[x] = new
                changed = True
    return set().union(*[Y[w] for w in K])


def kernel_closure(L, K):
    ctx = contexts(L)
    C = set.intersection(*[ctx[k] for k in K])
    return {m[len(p):len(m) - len(q)] for m in L for (p, q) in C
            if len(m) >= len(p) + len(q) and m.startswith(p) and m.endswith(q)
            and all(p2 + m[len(p):len(m) - len(q)] + q2 in L for (p2, q2) in C)}


K3 = ['{{{a}}}', '{{[aa]}}', '{[{a}{a}]}', '{[{a}[aa]]}', '{[[aa]{a}]}',
      '[{{a}}[{a}{a}]]', '[[{a}{a}]{{a}}]', '[{{a}}[{a}[aa]]]', '[[[aa]{a}]{{a}}]',
      '[[{a}[aa]]{{a}}]', '[{{a}}[[aa]{a}]]']


def main():
    ok = True
    M = {n: levels(n)[n] - {wstar(n)} for n in (2, 3, 4)}
    maxlen = {n: len(wstar(n)) for n in (2, 3, 4)}

    assert set(K3) <= M[3]
    L3 = rec_language(set(K3), maxlen[3])
    r1 = (L3 == M[3]) and not any(wstar(2) in w for w in K3)
    print(f'(1) n=3: |K3|={len(K3)}, ||K3||={sum(len(w) + 1 for w in K3)}, '
          f'L(Rec(K3)) = M_3: {L3 == M[3]}, factor w*_2 avoided: {r1}')
    ok &= r1

    for n, expected in ((2, 9), (3, 16)):
        least = next(Lm for Lm in sorted({len(w) for w in M[n]})
                     if rec_language({w for w in M[n] if len(w) <= Lm}, maxlen[n]) == M[n])
        print(f'(2) n={n}: least L with all words of length <= L characteristic: {least}')
        ok &= least == expected

    M2 = sorted(M[2])
    chars = [S for r in range(1, len(M2) + 1) for S in itertools.combinations(M2, r)
             if rec_language(set(S), maxlen[2]) == set(M2)]
    print(f'(3) n=2: characteristic samples: {len(chars)}, only M_2 itself: {chars == [tuple(M2)]}')
    ok &= chars == [tuple(M2)]

    for n in (2, 3, 4):
        strong = kernel_closure(M[n], [u(n)]) == M[n]
        rho = max(len(w) for w in M[n])
        print(f'(4) n={n}: listing grammar strong 1-FKP with kernel {{u_n}}: {strong}, '
              f'rho={rho} (3*2^n-3={3 * 2 ** n - 3}), |P|={len(M[n])}')
        ok &= strong and rho == 3 * 2 ** n - 3

    print('ALL OK' if ok else 'SOME CHECK FAILED')


if __name__ == '__main__':
    main()
