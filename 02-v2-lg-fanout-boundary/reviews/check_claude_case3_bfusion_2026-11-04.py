#!/usr/bin/env python3
"""Claude (README (144)): case III (b^4 occurs, c^4 must not).  With the extra seed bbbb,
the blocks bcccb, bccb, bcbcb force a word containing cccc -- a contradiction in case III.
bcccb is the 'b...cc...b' control left open in reviews/chatgpt_case2_branches_2026-11-04.md sec. 8.
Closure and certificate code copied from reviews/chatgpt_alternating_2026-11-04.md (section 5)
(via check_claude_mixed_roots_2026-11-04.py); the stop test is cccc only (bbbb is allowed).
Sound rule only; seeds a^k, bbbb, a^s F^j a^t (j<=2, s,t>=1, s+t=k-j), k=5, loss 1;
no separated pairs are used.  Observation for concrete blocks, not a general lemma.
Windows: py -3 check_claude_case3_bfusion_2026-11-04.py"""
from collections import defaultdict


def occ(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[i:j],), (w[:i], w[j:])
    else:
        for i in range(n):
            for j in range(i + 1, n):
                for p in range(j + 1, n):
                    for q in range(p + 1, n + 1):
                        yield (w[i:j], w[p:q]), (w[:i], w[j:p], w[q:])


def fill(E, xs):
    return ''.join(u + x for u, x in zip(E, xs)) + E[-1]


def ty(xs):
    return tuple(''.join(sorted(set(x))) for x in xs)


def seeds(k, u, loss):
    words = {'a' * k}
    for j in (1, 2, 3):
        words.update('a' * s + u * j + 'a' * (k - j * loss - s)
                     for s in range(1, k - j * loss))
    words.update('a' * p + u + 'a' * q + u +
                 'a' * (k - 2 * loss - p - q)
                 for p in range(1, k - 2 * loss)
                 for q in range(1, k - 2 * loss - p))
    return words


def closure(seed, maxlen=13, rounds=3):
    known = set(seed)
    provenance = {}
    for rnd in range(1, rounds + 1):
        added = {}
        for d in (1, 2):
            D = defaultdict(set)
            by_context = defaultdict(set)
            for w in sorted(known):
                for xs, E in occ(w, d):
                    D[xs].add(E)
                    by_context[(ty(xs), E)].add(xs)
            for (_, E), xs_set in sorted(by_context.items()):
                xs_list = sorted(xs_set)
                for x in xs_list:
                    for y in xs_list:
                        if x == y:
                            continue
                        for F in sorted(D[x] - D[y]):
                            w = fill(F, y)
                            if len(w) > maxlen or w in known or w in added:
                                continue
                            assert ty(x) == ty(y)
                            assert fill(E, x) in known
                            assert fill(E, y) in known
                            assert fill(F, x) in known
                            assert len(E) == d + 1 and len(F) == d + 1
                            if d == 2:
                                assert E[1] and F[1]
                            added[w] = (d, E, x, y, F)
                            if 'cccc' in w:
                                provenance.update(added)
                                known.update(added)
                                print('block: forced at round', rnd,
                                      'seeds', len(seed), 'word', w)
                                return known, provenance, w
        if not added:
            print('block: fixpoint', len(known), 'words')
            return known, provenance, None
        known.update(added)
        provenance.update(added)
        print('block: round', rnd, 'added', len(added), 'total', len(known))
    print('block: round limit', len(known))
    return known, provenance, None


def verify_certificate(goal, seed, provenance):
    ordered, used = [], set()

    def visit(w):
        if w in seed:
            return
        if w in used:
            return
        d, E, x, y, F = provenance[w]
        for v in (fill(E, x), fill(E, y), fill(F, x)):
            visit(v)
        used.add(w)
        ordered.append((w, d, E, x, y, F))

    visit(goal)
    certified = set(seed)
    for i, (w, d, E, x, y, F) in enumerate(ordered, 1):
        assert ty(x) == ty(y)
        assert len(E) == len(F) == d + 1
        assert d == 1 or (E[1] and F[1])
        assert all(fill(C, t) in certified
                   for C, t in ((E, x), (E, y), (F, x)))
        assert fill(F, y) == w
        certified.add(w)
        print('CERT', i, 'd=', d, 'E=', E, 'x=', x,
              'y=', y, 'F=', F, '=>', w)
    print('certificate steps:', len(ordered))


def seeds3(k, F):
    S = {'a' * k, 'bbbb'}
    for j in (1, 2):
        S |= {'a' * s + F * j + 'a' * (k - j - s) for s in range(1, k - j)}
    return S


def main():
    for F in ('bcccb', 'bccb', 'bcbcb'):
        print('\nBLOCK', F)
        seed = seeds3(5, F)
        words, provenance, forced = closure(seed)
        assert forced is not None and 'cccc' in forced
        verify_certificate(forced, seed, provenance)
    print('\nALL THREE BLOCKS FORCE cccc')


if __name__ == '__main__':
    main()
