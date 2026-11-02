"""Checks for reviews/claude_compression_review2_2026-11-02.md (Python 3, standard library only).

Part 1: at fan-out one, every subset of {a^i d a^i d a^(2(q-i)+2^k) : 0<=i<=q} is
        Clark-Eyraud substitutable (exhaustive for small q, k).  Observation; the proof is in the report.
Part 2: at fan-out two, merging the letters a_h (or the markers d_h) of the family of
        prop:linear-factor-all-fanout breaks arity-2 substitutability (explicit violations).
Run:  py -3 check_claude_review2_2026-11-02.py
"""
import itertools

def occ(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[i:j],), (w[:i], w[j:])
    else:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for h in range(k + 1, n + 1):
                        yield (w[i:j], w[k:h]), (w[:i], w[j:k], w[h:])

def violation(L, f):
    """Trivial typing; returns (arity, x, y, shared context) or None."""
    for d in range(1, f + 1):
        D = {}
        for w in L:
            for x, c in occ(w, d):
                D.setdefault(x, set()).add(c)
        by_ctx = {}
        for x, cs in D.items():
            for c in cs:
                by_ctx.setdefault(c, []).append(x)
        for c, xs in by_ctx.items():
            for x in xs[1:]:
                if D[x] != D[xs[0]]:
                    return (d, xs[0], x, c)
    return None

def all_subsets_ok(L, f):
    for r in range(1, len(L) + 1):
        for J in itertools.combinations(L, r):
            v = violation(set(J), f)
            if v:
                return v
    return None

def two_letter_family(q, k):
    return ['a' * i + 'd' + 'a' * i + 'd' + 'a' * (2 * (q - i) + 2 ** k) for i in range(q + 1)]

def family(f, q, k, A, D, Z):
    t = 2 * f
    return [''.join(A[h] * i + D[h] for h in range(t)) + Z * (2 * f * (q - i) + 2 ** k)
            for i in range(q + 1)]

if __name__ == '__main__':
    print('Part 1: fan-out one, two letters')
    for q, k in [(3, 1), (4, 2), (5, 2), (6, 3)]:
        v = all_subsets_ok(two_letter_family(q, k), 1)
        print('  q=%d k=%d: %s' % (q, k, 'all subsets substitutable' if v is None else v))
    print('Part 2: fan-out two, merged letters (q=2, k=1)')
    A = ['p', 'q', 'r', 's']; D = ['A', 'B', 'C', 'D']
    print('  original 9 letters :', all_subsets_ok(family(2, 2, 1, A, D, 'z'), 2) or 'ok')
    print('  one letter a        :', all_subsets_ok(family(2, 2, 1, ['a'] * 4, D, 'z'), 2))
    print('  one marker D        :', all_subsets_ok(family(2, 2, 1, A, ['D'] * 4, 'z'), 2))
