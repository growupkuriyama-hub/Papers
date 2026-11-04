#!/usr/bin/env python3
"""Claude (README (139)): the key lemma (KL) of case II for blocks with an internal xx.

Two base certificates over the abstract alphabet {a,p,x,q} (content typing on four letters),
k=6, loss d=1, seeds: a^6, a^s F^j a^t (j=1,2,3), a^p F a^q F a^r (all positive splits),
for F = xpxxq and F = pxxqx.  Each forces x^4 in 4 steps of the single sound rule
    E[X], E[Y], H[X] in L, componentwise contents of X and Y equal  =>  H[Y] in L
(two-hole contexts have a nonempty middle).  The certificates were found with the closure
code of reviews/chatgpt_alternating_2026-11-04.md and are stored here as data.
The nonerasing morphism h(a)=a^d, h(x)=x, h(p)=P, h(q)=Q (P, Q in {b,c}+), with left padding
a^(k-6d), maps every step to a valid step (Lemma 2.2 of reviews/chatgpt_key_lemma_2026-11-04.md;
only "equal contents stay equal" is used, so the source alphabet may have four letters).
The script replays the base certificates from the seeds and the lifted ones on concrete blocks.
Windows: py -3 check_claude_kl_internal_2026-11-04.py
"""
BASE = {'xpxxq': [(1, ('', 'aaa'), ('axpxxqa',), ('axpxxqxpxxq',), ('aaxpxxq', '')), (2, ('', 'x', 'a'), ('aaxp', 'xqxpxxqa'), ('aaxpx', 'qaxpxxq'), ('', 'xxqxpx', '')), (2, ('', 'x', 'a'), ('aaxpx', 'qxpxxqa'), ('aaxp', 'xqaxpxxq'), ('', 'xqxpxx', '')), (1, ('aaxp', 'xpxxq'), ('xxqaxpxxq',), ('xxxqxpxqa',), ('aaxpxqxpx', ''))], 'pxxqx': [(1, ('', 'aa'), ('aaapxxqx',), ('apxxqxapxxqx',), ('', 'pxxqxa')), (2, ('', 'x', 'a'), ('aapxxqxpx', 'qxa'), ('apxxqxap', 'xqxa'), ('', 'xqxpxx', '')), (2, ('', 'x', 'a'), ('aapxxqxp', 'xqxa'), ('apxxqxpx', 'qxaa'), ('', 'xxqxpx', '')), (1, ('apxxqx', 'qxa'), ('apxxqxpxx',), ('apxqxpxxx',), ('', 'xqxpxqxaa'))]}


def fill(E, t):
    return ''.join(e + s for e, s in zip(E, t)) + E[-1]


def seeds(k, F, d):
    S = {'a' * k}
    for j in (1, 2, 3):
        S |= {'a' * s + F * j + 'a' * (k - j * d - s) for s in range(1, k - j * d)}
    S |= {'a' * p + F + 'a' * q + F + 'a' * (k - 2 * d - p - q)
          for p in range(1, k - 2 * d) for q in range(1, k - 2 * d - p)}
    return S


def replay(steps, S, target, h=None, pad=''):
    S = set(S)
    H = (lambda s: ''.join(h[c] for c in s)) if h else (lambda s: s)
    last = None
    for d, E, X, Y, F in steps:
        E2 = (pad + H(E[0]),) + tuple(H(e) for e in E[1:])
        F2 = (pad + H(F[0]),) + tuple(H(e) for e in F[1:])
        X2 = tuple(H(t) for t in X)
        Y2 = tuple(H(t) for t in Y)
        assert len(X2) == len(Y2) == d and all(X2) and all(Y2)
        assert all(set(u) == set(v) for u, v in zip(X2, Y2))
        if d == 2:
            assert E2[1] and F2[1]
        for prem in (fill(E2, X2), fill(E2, Y2), fill(F2, X2)):
            assert prem in S, prem
        last = fill(F2, Y2)
        S.add(last)
    assert target in last, last
    return last


def main():
    for B, st in BASE.items():
        print('base %s: %d steps -> %s' % (B, len(st), replay(st, seeds(6, B, 1), 'xxxx')))
    tests = [('xpxxq', 'c', 'b', 'b'), ('xpxxq', 'c', 'bcb', 'bbcb'), ('xpxxq', 'b', 'cbc', 'c'),
             ('pxxqx', 'c', 'b', 'b'), ('pxxqx', 'b', 'cbc', 'ccbc'), ('pxxqx', 'c', 'bbcb', 'bcbb')]
    for B, x, P, Q in tests:
        for d, k in ((1, 6), (2, 12), (3, 21), (2, 15)):
            h = {'a': 'a' * d, 'x': x, 'p': P, 'q': Q}
            F = ''.join(h[c] for c in B)
            last = replay(BASE[B], seeds(k, F, d), x * 4, h, 'a' * (k - 6 * d))
            print('F=%-12s k=%2d d=%d: %s^4 forced in %s' % (F, k, d, x, last))
    print('ALL LIFTED CERTIFICATES VERIFIED')


if __name__ == '__main__':
    main()
