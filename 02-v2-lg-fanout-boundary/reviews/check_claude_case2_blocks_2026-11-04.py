#!/usr/bin/env python3
"""Claude's experiments on case II blocks (README (130)/(131)).  Python 3 standard library only.

Windows: py -3 check_claude_case2_blocks_2026-11-04.py

Part 1  Weight-level languages over {b,c}-blocks:
          L = { words whose maximal a-free factors are concatenations of blocks
                from a set C, with |w|_a + sum of block weights = K }.
        Exact (1,c),(2,c)-substitutability test of these FINITE languages.
        Single root u: only u = bc passes for every weight tried.
Part 2  Forced closure (sound rules only): seeds = a^k, the single-block words
        a^s u^j a^t (j = 1, 2, 3, loss j*d) and the separated pairs
        a^p u a^q u a^r.  Every added word is forced in every L in C_(2,c)
        containing the seeds.  A word containing b^4 or c^4 is therefore a
        certificate that no case-II language contains the seeds.  A fixpoint
        proves nothing about infinite languages.  Generated words are limited to
        length <= k+4, so "no x^4 found" is an observation, not a proof.
"""
from collections import defaultdict


def occurrences(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[i:j],), (w[:i], w[j:])
    else:
        for i in range(n):
            for j in range(i + 1, n):
                for p in range(j + 1, n):          # nonempty middle
                    for q in range(p + 1, n + 1):
                        yield (w[i:j], w[p:q]), (w[:i], w[j:p], w[q:])


def substitutable(L):
    for d in (1, 2):
        D = defaultdict(set)
        for w in L:
            for t, c in occurrences(w, d):
                D[t].add(c)
        seen = {}
        for t, cs in D.items():
            ty = tuple(frozenset(x) for x in t)
            for c in cs:
                o = seen.setdefault((ty, c), t)
                if o != t and D[o] != D[t]:
                    return False
    return True


def weight_level(blocks, K):
    out = set()

    def rec(w, weight):
        if weight == K:
            if w:
                out.add(w)
            return
        if weight + 1 <= K:
            rec(w + 'a', weight + 1)
        for u, wt in blocks.items():
            if weight + wt <= K:
                rec(w + u, weight + wt)
    rec('', 0)
    return out


def part1():
    for u in ('bc', 'bcc', 'bbc', 'bbcc', 'bcbb'):
        row = []
        for wt in (1, 2):
            row.append(substitutable(weight_level({u: wt}, 9)))
        print('Part 1: root %-5s weights 1,2, K=9: substitutable %s' % (u, row))
        if u == 'bc':
            assert all(row)
        else:
            assert not any(row)


def fill(c, t):
    return ''.join(x + y for x, y in zip(c, t)) + c[-1]


def closure(S, maxlen, rounds):
    S = set(S)
    for _ in range(rounds):
        new = set()
        for d in (1, 2):
            D = defaultdict(set)
            for w in S:
                for t, c in occurrences(w, d):
                    D[t].add(c)
            parent = {}

            def find(x):
                while parent.get(x, x) != x:
                    x = parent[x]
                return x
            byc = defaultdict(list)
            for t, cs in D.items():
                ty = tuple(frozenset(x) for x in t)
                for c in cs:
                    byc[(ty, c)].append(t)
            for ts in byc.values():
                for t in ts[1:]:
                    a, b = find(ts[0]), find(t)
                    if a != b:
                        parent[b] = a
            groups = defaultdict(list)
            for t in D:
                groups[find(t)].append(t)
            for g in groups.values():
                if len(g) < 2:
                    continue
                allc = set().union(*(D[t] for t in g))
                for t in g:
                    for c in allc - D[t]:
                        w = fill(c, t)
                        if len(w) <= maxlen and w not in S:
                            new.add(w)
        if not new:
            return S, 'fixpoint'
        S |= new
        if any('bbbb' in w or 'cccc' in w for w in S):
            return S, 'x^4 forced'
    return S, 'round limit'


def seeds(k, u, d):
    S = {'a' * k}
    for j in (1, 2, 3):
        S |= {'a' * s + u * j + 'a' * (k - j * d - s) for s in range(1, k - j * d)}
    S |= {'a' * p + u + 'a' * q + u + 'a' * (k - 2 * d - p - q)
          for p in range(1, k - 2 * d) for q in range(1, k - 2 * d - p)}
    return S


def part2(k=9, d=2):
    for u in ('bc', 'bcbc', 'bcc', 'bbc', 'bcb'):
        S, status = closure(seeds(k, u, d), k + 4, rounds=4)
        short = [w for w in S if set(w) == {'a'} and len(w) < k]
        bad = sorted((w for w in S if 'bbbb' in w or 'cccc' in w), key=len)
        print('Part 2: block %-4s k=%d d=%d: %s, %d words, short pure a-words %d, x^4 example %s'
              % (u, k, d, status, len(S), len(short), bad[0] if bad else '-'))
        assert not short
        if u in ('bc', 'bcbc'):
            assert status == 'fixpoint' and not bad
        else:
            assert bad


if __name__ == '__main__':
    part1()
    part2()
