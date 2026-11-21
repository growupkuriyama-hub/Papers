#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finite checks for the outer-c research note (standard library only).

This is NOT a decision procedure for arbitrary MCFGs or infinite languages.
It checks all arity-1/2 contexts of explicitly enumerated FINITE languages,
and constructs checkable derivation-tree witnesses for a failed doubled family.
"""

from __future__ import annotations
from collections import defaultdict
from itertools import combinations, product
import argparse

ALPHABET = 'abc'


def supp(s: str) -> frozenset[str]:
    return frozenset(s)


def c_signature(tup: tuple[str, ...]) -> tuple[frozenset[str], ...]:
    return tuple(supp(x) for x in tup)


def fill(context: tuple[str, ...], holes: tuple[str, ...]) -> str:
    assert len(context) == len(holes) + 1
    return ''.join(context[i] + holes[i] for i in range(len(holes))) + context[-1]


def distributions(language: set[str], d: int):
    """Complete d-hole distributions over positive tuple occurrences in L.

    Each recorded context is admissible: d=2 has a nonempty internal gap.
    There is no arbitrary length truncation (language itself is finite).
    """
    assert d in (1, 2)
    distributions_by_tuple = defaultdict(set)
    for w in language:
        n = len(w)
        if d == 1:
            for i in range(n):
                for j in range(i + 1, n + 1):
                    x = (w[i:j],)
                    context = (w[:i], w[j:])
                    assert fill(context, x) == w
                    distributions_by_tuple[x].add(context)
        else:
            for i in range(n):
                for j in range(i + 1, n + 1):
                    for k in range(j + 1, n):  # nonempty fixed middle
                        for l in range(k + 1, n + 1):
                            x = (w[i:j], w[k:l])
                            context = (w[:i], w[j:k], w[l:])
                            assert context[1]
                            assert fill(context, x) == w
                            distributions_by_tuple[x].add(context)
    return dict(distributions_by_tuple)


def find_failure(language: set[str], d: int):
    """Return a complete C_d failure certificate, or None if C_d holds."""
    ds = distributions(language, d)
    by_type = defaultdict(list)
    for tup in ds:
        by_type[c_signature(tup)].append(tup)
    for signature, tuples in by_type.items():
        for x, y in combinations(sorted(tuples), 2):
            common = ds[x] & ds[y]
            if common and ds[x] != ds[y]:
                if ds[x] - ds[y]:
                    witness_x, witness_y = x, y
                    distinguish = sorted(ds[x] - ds[y])[0]
                else:
                    witness_x, witness_y = y, x
                    distinguish = sorted(ds[y] - ds[x])[0]
                shared = sorted(common)[0]
                assert fill(shared, witness_x) in language
                assert fill(shared, witness_y) in language
                assert fill(distinguish, witness_x) in language
                assert fill(distinguish, witness_y) not in language
                return {
                    'arity': d,
                    'type': signature,
                    'x': witness_x,
                    'y': witness_y,
                    'shared': shared,
                    'distinguishing': distinguish,
                    'shared_x': fill(shared, witness_x),
                    'shared_y': fill(shared, witness_y),
                    'yes': fill(distinguish, witness_x),
                    'no': fill(distinguish, witness_y),
                }
    return None


def fixed_content_layer(m: int) -> set[str]:
    """All length-m words of full abc support, plus the two ab words.

    This is C_d for every arity d by the equal-(support,length)-layer proof.
    Enumeration is intended only for small m (tested m=3,4).
    """
    assert m >= 3
    return {'ab', 'ba'} | {
        ''.join(t) for t in product(ALPHABET, repeat=m)
        if supp(''.join(t)) == supp('abc')
    }


def doubled_A(n: int) -> set[str]:
    """Exact finite A_n language for n<=3 (size rises doubly exponentially)."""
    assert 0 <= n <= 3
    lang = {'a', 'c'}
    for _ in range(1, n + 1):
        lang = {'c'} | {u + v for u in lang for v in lang}
    return lang


def doubled_L(n: int) -> set[str]:
    """Example (138) from 2026-11-04, enumerated exactly."""
    return {'aaaa', 'bbbb', 'cccc'} | {x + 'b' for x in doubled_A(n)}


def theta_doubled(n: int) -> int:
    """Rule-successful shortest lengths, minimized analytically per rule.

    S -> A_n b: 2. S -> zzzz: 4.
    A_i -> c: shortest outside path costs 1+(n-i), plus 1.
    A_i -> A_(i-1) A_(i-1): shortest outside costs 1+(n-i), plus 2.
    A_0 -> a|c: shortest outside cost 1+n, plus 1.
    """
    assert n >= 1
    costs = [2, 4]
    costs += [1 + (n - i) + 1 for i in range(n + 1)]
    costs += [1 + (n - i) + 2 for i in range(1, n + 1)]
    costs += [1 + n + 1]
    assert max(costs) == max(4, n + 2)
    return max(costs)


def best_antichain_level(n: int):
    """Choose a level A_i with heavy yield 2^i>theta and maximal width."""
    theta = theta_doubled(n)
    choices = [i for i in range(n) if 2 ** i > theta]
    if not choices:
        return None
    i = min(choices)
    q = 2 ** (n - i)
    ell = 2 ** i
    n_word = 2 ** n + 1
    min_c_free_outer = n_word - ell
    return (i, q, ell, theta, min_c_free_outer)


def cube_words(n: int, i: int) -> list[str]:
    """Explicit legal simultaneous A_i->c substitutions in a^2^n b.

    The FIRST A_i block is never touched, keeping an a-witness outside.
    At least one c is introduced; b always remains at the last position.
    """
    assert 0 <= i < n
    q = 2 ** (n - i)
    block = 'a' * (2 ** i)
    result = []
    for k in range(1, q):
        blocks = [block] + ['c'] * k + [block] * (q - 1 - k)
        w = ''.join(blocks) + 'b'
        assert supp(w) == supp('abc')
        assert w.count('c') == k
        result.append(w)
    return result


def run_checks():
    print('== exact finite C_1,C_2 tester ==')
    good = {'ab', 'cb'}
    for d in (1, 2):
        fail = find_failure(good, d)
        assert fail is None
        print(f'L={{ab, cb}} arity {d}: PASS; enumerated tuples={len(distributions(good, d))}')
    assert 'ab' in good and 'ba' not in good

    for m in (3, 4):
        finite = fixed_content_layer(m)
        assert find_failure(finite, 1) is None
        assert find_failure(finite, 2) is None
        assert min(len(w) for w in finite if supp(w) == supp('ab')) == 2
        k_c = len({w.count('c') for w in finite if supp(w) == supp('abc')})
        assert k_c == m - 2
        print(f'finite layer m={m}: C1,C2 PASS, mu_ab=2, K_c={k_c}, |L|={len(finite)}')

    for n in (1, 2):
        L = doubled_L(n)
        expected_mu = 2 ** n + 1
        min_ab = min(len(w) for w in L if supp(w) == supp('ab'))
        assert min_ab == expected_mu
        assert theta_doubled(n) == max(4, n + 2)
        certificate = find_failure(L, 1)
        assert certificate is not None
        print(f'bad family n={n}: |L|={len(L)}, theta={theta_doubled(n)}, '
              f'mu_ab={min_ab}, C1 fails')
        print('  witness:', certificate)
        # A fixed certificate valid for every n>=1 from (138):
        assert {'cb', 'ccb', 'cccc'} <= L
        assert 'ccccc' not in L

    print('== spectrum and antichain stress tests ==')
    for n in (6, 8, 10, 12):
        info = best_antichain_level(n)
        assert info is not None
        i, q, ell, theta, outer = info
        assert ell > theta
        assert outer > theta
        assert q <= 2 ** n
        # Short contexts of A_i MUST contain c, because a c-free
        # context costs at least outer > theta.
        # In this grammar all A_i also derive the one-letter word c.
        print(f'n={n}: v={n+2}, theta={theta}, mu_ab={2**n+1}, '
              f'level={i}, ell={ell}, q={q}, min-c-free-outer={outer}, '
              f'lower-bound K_abc >= {q-1}')
        # q-1 is sharper than the general q-2 because b is always outside.
        if n <= 8:
            samples = cube_words(n, i)
            assert len({w.count('c') for w in samples}) == q - 1
            assert all(w.endswith('b') for w in samples)
            print('  c-switch counts:', [w.count('c') for w in samples])
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='run exhaustive finite checks')
    args = parser.parse_args()
    run_checks()
