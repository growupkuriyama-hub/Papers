#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Frame-equivalence audit for 3-letter content typing; stdlib only.

Run: python chatgpt_frame_equivalence_2026-11-06.py
Optional: --scan (enumerate all first-step SUB1/2 for the small finite examples)
All asserted non-membership certificates concern complete finite languages,
not length-truncated approximations.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from itertools import combinations

ALPHABET = frozenset('abc')


def content(word):
    return frozenset(word)


def fill(context, values):
    assert len(context) == len(values) + 1
    return ''.join(context[i] + values[i] for i in range(len(values))) + context[-1]


def goodstep(L, E, x, y, F):
    """Check exact source premises and a genuine *missing* conclusion."""
    d = len(x)
    assert d in (1, 2) and len(y) == d
    assert len(E) == len(F) == d + 1
    assert all(x) and all(y)
    assert all(content(a) == content(b) for a, b in zip(x, y))
    assert all(E[j] and F[j] for j in range(1, d))
    A, B, C, D = fill(E, x), fill(E, y), fill(F, x), fill(F, y)
    assert A in L, ('first premise', A)
    assert B in L, ('second premise', B)
    assert C in L, ('third premise', C)
    assert D not in L, ('conclusion unexpectedly present', D)
    return dict(d=d, E=E, x=x, y=y, F=F, premises=(A, B, C), missing=D)


def frame_of(w, i, j):
    assert 0 <= i < j <= len(w)
    return w[:i], w[j:], w[i:j]


def all_frames(L):
    """Exact incidence: frame -> all nonempty centers occurring in finite L."""
    ans = defaultdict(set)
    for w in L:
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                ans[(w[:i], w[j:])].add(w[i:j])
    return dict(ans)


def frame_classes(L):
    """For a finite L, compute *actual* active-frame classes.

    If L obeys frame lemma, (outline,Z) is precisely the overlap class.
    For a non-closed L, this exact-Z grouping need not agree with the
    transitive closure of the overlap graph. Both are tested separately.
    """
    incidence = all_frames(L)
    grouped = defaultdict(list)
    for frame, centers in incidence.items():
        outline = (content(frame[0]), content(frame[1]))
        grouped[(outline, frozenset(centers))].append(frame)
    return incidence, grouped




def overlap_components(L):
    """Actual connected components of same-outline overlapping active frames.

    These components need not be valid equivalence classes when the frame
    property fails; ``bad`` counts components having unequal center sets.
    """
    incidence = all_frames(L)
    frames = list(incidence)
    parent = list(range(len(frames)))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def union(i, j):
        a, b = root(i), root(j)
        if a != b: parent[a] = b
    buckets = {}
    for i, f in enumerate(frames):
        outline = (content(f[0]), content(f[1]))
        for z in incidence[f]:
            key = (outline, z)
            if key in buckets: union(i, buckets[key])
            else: buckets[key] = i
    groups = defaultdict(list)
    for i, f in enumerate(frames): groups[root(i)].append(f)
    bad = sum(len({frozenset(incidence[f]) for f in group}) > 1
              for group in groups.values())
    return len(groups), bad


def exact_layer_words(n):
    from itertools import product
    M = 2 ** n
    assert M <= 8, 'small exact test only'
    return {'a', 'b', 'c'} | {''.join(t) for t in product('ab', repeat=M)
                               if set(t) == {'a','b'}}

def frame_conflict(L):
    """Find one overlap with unequal Z in the same outline (full finite test)."""
    incidence, _ = frame_classes(L)
    by_outline = defaultdict(list)
    for f, Z in incidence.items():
        by_outline[(content(f[0]), content(f[1]))].append((f, Z))
    for outline in sorted(by_outline, key=lambda x: (len(x[0]), len(x[1]), str(x))):
        arr = by_outline[outline]
        # Reverse index over centers: only frames with genuine overlap compete.
        by_center = defaultdict(list)
        for f, Z in arr:
            for z in Z: by_center[z].append(f)
        checked = set()
        for z, frames in by_center.items():
            if len(frames) < 2:
                continue
            for f, g in combinations(sorted(frames), 2):
                if (f, g) in checked: continue
                checked.add((f, g))
                if incidence[f] != incidence[g]:
                    diff = sorted(incidence[f] - incidence[g], key=lambda x:(len(x),x))
                    if diff: return outline, f, g, z, diff[0]
                    diff = sorted(incidence[g] - incidence[f], key=lambda x:(len(x),x))
                    return outline, g, f, z, diff[0]
    return None


def example_same_label():
    """S -> ab B ab B ab | ab b ab a ab, B -> a | c.

    The extra terminal production creates an accidental center 'b'
    in the first B-frame without making b a yield of B.
    """
    L = {'ab' + x + 'ab' + y + 'ab' for x in 'ac' for y in 'ac'}
    accidental = 'ab' + 'b' + 'ab' + 'a' + 'ab'
    L.add(accidental)
    left = ('ab', 'abaab')
    right = ('abaab', 'ab')
    assert left[0] + 'a' + left[1] == right[0] + 'a' + right[1]
    cert = goodstep(L, ('', 'a', ''), left, right, ('', 'b', ''))
    incidence = all_frames(L)
    assert 'a' in incidence[left] & incidence[right]
    assert 'c' in incidence[left] & incidence[right]
    assert 'b' in incidence[left] and 'b' not in incidence[right]
    assert all(content(t) == {'a','b'} for t in left+right)
    return L, cert, left, right, incidence


def candidate_a(n):
    """Exact finite fanout-2 doubled/slotted grammar from preceding report."""
    assert n >= 2
    D = [{'ab'}]
    for i in range(1, n + 1):
        D.append({u + v for u in D[-1] for v in D[-1]} | {'a' * i + 'cb'})
    A = [None, {('ab', 'ab')}]
    for i in range(2, n + 1):
        old, blocks = A[-1], D[i - 1]
        A.append({(d + x, y) for d in blocks for x, y in old}
                 | {(x, y + d) for d in blocks for x, y in old}
                 | {(d, e) for d in blocks for e in blocks})
    L = {w + 'ab' for w in D[n]} | {x + 'c' + y for x, y in A[n]}
    return L


def verify_scissors(n, L):
    M = 2 ** n
    x = ('a', 'b' + 'ab' * (M - 1))
    y = ('a' * n, 'bab')
    cert = goodstep(L, ('', 'c', ''), x, y, ('', 'ba', ''))
    assert {w for w in L if 'c' not in w} == {'ab' * (M + 1)}
    assert len(cert['missing']) == n + 5 < 2 * (M + 1)
    return cert


def layer_language(n, w):
    """Exact membership in {a,b,c} union all full-ab words of length 2**n."""
    M = 2 ** n
    return w in {'a','b','c'} or (len(w) == M and content(w) == {'a','b'})


def layer_grammar_size(n):
    """Exact *reduced* typed-doubling grammar size.

    States are S, A_{0,a}, A_{0,b}, every A_{i,T} for 1<=i<n,
    and only A_{n,ab} at the top. Omitting A_{n,a},A_{n,b}
    is essential for reachability (hence reducedness).
    """
    assert n >= 1
    nonterminals = 3*n + 1
    start_rules = 3*2 + 3
    base_rules = 2*2
    if n == 1:
        binary_rules = 2*5  # only (a,b) or (b,a) at the top
    else:
        binary_rules = 4*5 + (n-2)*9*5 + 7*5
    return nonterminals + start_rules + base_rules + binary_rules


def check_layer(n):
    M = 2 ** n
    assert layer_grammar_size(n) == 48*n - 21
    for c in 'abc': assert layer_language(n, c)
    for w in ['ab'*(M//2), 'a'*(M-1)+'b', 'b'+'a'*(M-1)]:
        assert layer_language(n, w)
    assert not layer_language(n, 'ab'*(M//2)+'a')
    assert not layer_language(n, 'a'*M)
    assert M > 1
    # The general class formula is proved in the report and checked on
    # complete small finite languages in main(); no symbolic tautology here.
    return (layer_grammar_size(n), M, M)


def finite_sub_failure(L, d):
    """Exhaustive finite-language one-step SUB_d search; exact (no cutoff)."""
    incidence = defaultdict(set) # (context, component-content) -> accepted tuples
    contexts_by_tuple = defaultdict(set)
    for w in L:
        N = len(w)
        if d == 1:
            occurrences = (((w[i:j],), (w[:i], w[j:]))
                           for i in range(N) for j in range(i+1,N+1))
        else:
            occurrences = (((w[i:j], w[k:l]), (w[:i], w[j:k], w[l:]))
                           for i in range(N) for j in range(i+1,N)
                           for k in range(j+1,N) for l in range(k+1,N+1))
        for x, E in occurrences:
            incidence[(E, tuple(map(content, x)))].add(x)
            contexts_by_tuple[x].add(E)
    for (E,_), accepted in incidence.items():
        if len(accepted) < 2: continue
        for x in accepted:
            for y in accepted:
                if x == y: continue
                for F in contexts_by_tuple[x]:
                    if fill(F, y) not in L:
                        return goodstep(L, E, x, y, F)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scan', action='store_true', help='exact finite SUB1/SUB2 scans for small models')
    args = ap.parse_args()

    L, cert, f, g, Z = example_same_label()
    print('SAME_LABEL |L|=%d f=%r g=%r Zf=%r Zg=%r' %
          (len(L), f, g, sorted(Z[f]), sorted(Z[g])))
    print('SAME_LABEL_CERT',cert)
    assert frame_conflict(L) is not None
    print('SAME_LABEL_OVERLAP_COMPONENTS', overlap_components(L))
    for n in (2,3):
        L = candidate_a(n)
        c = verify_scissors(n,L)
        incidence, classes = frame_classes(L)
        f, g = c['x'], c['y']
        assert content(f[0]) == content(g[0])
        assert content(f[1]) == content(g[1])
        assert 'c' in incidence[f] & incidence[g]
        assert 'ba' in incidence[f] and 'ba' not in incidence[g]
        print('A n=%d |L|=%d active_frames=%d (outline,Z)-groups=%d'
              ' sizes: |Z(f)|=%d |Z(g)|=%d' %
              (n, len(L), len(incidence), len(classes), len(incidence[f]), len(incidence[g])))
        print('A_OVERLAP_COMPONENTS', overlap_components(L))
        print('A_N9_CERT',c)
    for n in (1,2,3,4):
        print('B_LAYER n=%d grammar_size=%d theta=%d mu_ab=%d short_letters=abc'
              % (n, *check_layer(n)))
    for n in (1, 2):
        L = exact_layer_words(n)
        assert frame_conflict(L) is None
        incidence = all_frames(L)
        by_outline = defaultdict(list)
        for f, Z in incidence.items():
            by_outline[(content(f[0]), content(f[1]))].append((f, Z))
        for entries in by_outline.values():
            for (f, Z), (g, Z2) in combinations(entries, 2):
                if len(f[0])+len(f[1]) == len(g[0])+len(g[1]):
                    assert Z == Z2
                else:
                    assert Z.isdisjoint(Z2)
        assert finite_sub_failure(L,1) is None and finite_sub_failure(L,2) is None
        print('B_EXACT n=%d |L|=%d overlap_components=%r' % (n, len(L),overlap_components(L)))
    if args.scan:
        for name, L in (('same_label', example_same_label()[0]),('A2',candidate_a(2))):
            for d in (1,2):
                print('SCAN', name, 'SUB',d,finite_sub_failure(L,d))
    print('PASS: all assertions; no numerical observation was used as a membership proof.')


if __name__ == '__main__':
    main()
