#!/usr/bin/env python3
"""Independent check (Claude, 2026-11-07) of Example 2.8 of claude_algebraic_closure_2026-11-07.md.

T_n = all words whose Parikh vector lies in
  Q(T_n) = {(1+3n,1,0), (1,1+3n,0), (3,2,1), (1,3,2), (2,1,3)}.
Checks, at the word level and exhaustively (T_n is finite), that T_n has no
one-step SUB_1 or SUB_2 violation under content typing (inner separator of SUB_2
nonempty), and that (3n-2,4,0) is not in Q(T_n), which is the vector a (16)-form
presentation would force.  Standard library only; independent of the report's code.
Run: python3 check_claude_verify_algebraic_closure_Tn_2026-11-07.py
"""
import itertools
from collections import defaultdict


def plug(ctx, parts):
    out = ctx[0]
    for p, c in zip(parts, ctx[1:]):
        out += p + c
    return out


def violations(L):
    L = set(L)
    by_ctx, ctxs = defaultdict(set), defaultdict(set)
    for w in L:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                E, x = (w[:i], w[j:]), (w[i:j],)
                by_ctx[E].add(x); ctxs[x].add(E)
                for k in range(j + 1, n):
                    for l in range(k + 1, n + 1):
                        E, x = (w[:i], w[j:k], w[l:]), (w[i:j], w[k:l])
                        by_ctx[E].add(x); ctxs[x].add(E)
    for E, xs in by_ctx.items():
        groups = defaultdict(list)
        for x in xs:
            groups[tuple(frozenset(t) for t in x)].append(x)
        for grp in groups.values():
            for x in grp:
                for y in grp:
                    if x != y:
                        for F in ctxs[x]:
                            if plug(F, y) not in L:
                                return (E, x, y, F, plug(F, y))
    return None


def words(p):
    s = 'a' * p[0] + 'b' * p[1] + 'c' * p[2]
    return {''.join(w) for w in set(itertools.permutations(s))}


if __name__ == '__main__':
    for n in (2, 3):
        Q = [(1 + 3 * n, 1, 0), (1, 1 + 3 * n, 0), (3, 2, 1), (1, 3, 2), (2, 1, 3)]
        L = set().union(*(words(q) for q in Q))
        v = violations(L)
        print('T_%d: |L|=%d, SUB1/SUB2 violation: %s, (3n-2,4,0) in Q: %s'
              % (n, len(L), v, (3 * n - 2, 4, 0) in Q))
        assert v is None and (3 * n - 2, 4, 0) not in Q
    print('ALL PASS')
