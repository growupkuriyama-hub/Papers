#!/usr/bin/env python3
"""Independent finite checks of Appendix H (Python standard library only).
These finite tests are NOT proofs. Run: python3 check_chatgpt_appH_rewrite_2026-11-09.py
"""
from __future__ import annotations
import itertools
import math
import random
import time


def distributions(lang):
    d = {}
    for word in lang:
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                d.setdefault(word[i:j], set()).add((word[:i], word[j:]))
    return d


def u1_type(word):
    return 1 if set(word) == {'a'} else 0


def is_typed_substitutable(lang, typing):
    d = distributions(lang)
    by_context_type = {}
    for x, contexts in d.items():
        for context in contexts:
            by_context_type.setdefault((typing(x), context), []).append(x)
    for xs in by_context_type.values():
        if any(d[x] != d[xs[0]] for x in xs[1:]):
            return False
    return True


def select(values, i0, d, limit):
    # Values are indexed from 0 to i_star, with formal n before i0.
    i_star = len(values) - 1
    if values[i_star] >= limit:
        return [], 0
    chosen = [i_star]
    total = values[i_star]
    while True:
        candidates = [i for i in range(chosen[-1]) if values[i] > total]
        assert candidates, 'v_0=n >= limit guarantees a candidate'
        i = max(candidates)
        if total + values[i] >= limit:
            break
        assert i >= i0
        chosen.append(i)
        total += values[i]
    assert all(values[j] > sum(values[h] for h in chosen[:t])
               for t, j in enumerate(chosen))
    assert total < limit <= 3 ** len(chosen) * (values[i_star] + d)
    return chosen, total


def filler(values, i0, d, x):
    original = x
    counts = {}
    for i in range(i0, len(values)):
        q, x = divmod(x, values[i])
        counts[i] = q
        assert q <= (1 if i == i0 else 3)
    assert sum(counts[i] * values[i] for i in counts) + x == original
    assert x % d == 0 and 0 <= x < values[-1]
    assert sum(counts.values()) <= 3 * (len(values) - i0)
    return counts, x


def test_sequences(rng, trials=20000):
    for _ in range(trials):
        d = rng.randint(1, 9)
        i0 = rng.randint(1, 4)
        i_star = rng.randint(i0, i0 + 10)
        vals = [0] * (i_star + 1)
        vals[-1] = d * rng.randint(2, 12)
        for i in range(i_star - 1, i0 - 1, -1):
            # Monotonicity is not required by the proof but is compatible with ancestry.
            vals[i] = d * rng.randint(vals[i + 1] // d,
                                         2 * vals[i + 1] // d + 2)
        n = d * rng.randint(vals[i0] // d, 2 * vals[i0] // d)
        for i in range(i0):
            vals[i] = n
        assert all(v > d and v % d == 0 for v in vals)
        assert all(vals[i] <= 2 * vals[i+1] + 2*d
                   for i in range(i_star))
        limit = d * rng.randint(1, n // d)
        select(vals, i0, d, limit)
        x = d * rng.randint(1, n // d - 1) if n > d else 0
        if x:
            filler(vals, i0, d, x)
    return trials


def test_binomials():
    for m in range(6, 1001):
        k = m // 3
        j0, j1 = m // 3, 2*m // 3
        assert j1 <= m + 1 - k
        assert math.comb(m + 1, k) >= math.comb(3*k, k)
        assert all(math.comb(m+1, j) >= math.comb(m+1, k)
                   for j in range(j0, j1+1))
        assert math.comb(3*k, k) * (m + 1) * (4 ** k) >= 27 ** k
    return 995


def test_constants():
    mu = (27/4) ** (1/3)
    gamma = math.log(3) / math.log(mu)
    eta = 1/80
    x = 6/(eta*math.log(mu))
    log_ceta = 6*math.log(x) - (x - 1)*eta*math.log(mu)
    a = gamma/(1-eta)
    log_c0 = math.log(11) + a*(math.log(15625)+2*math.log(mu)+log_ceta)
    log_c = 22*math.log(2)+log_c0
    # C' = 12(C + 2); logs evaluated safely.
    log_cp = math.log(12)+log_c+math.log1p(2*math.exp(-log_c))
    assert log_ceta < 34
    assert a < 1.7479
    assert log_c0 < 36*math.log(10)
    assert log_c < 43*math.log(10)
    assert log_cp < 45*math.log(10)
    for m in range(6, 1001):
        assert (27/4) ** (m//3) >= mu ** (m-2) if m < 600 else (
            (m//3)*math.log(27/4) >= (m-2)*math.log(mu)-1e-10)
    return {'mu':mu, 'gamma':gamma, '80gamma/79':a,
            'log10(C_eta)':log_ceta/math.log(10),
            'log10(C0)':log_c0/math.log(10),
            'log10(C)':log_c/math.log(10),
            'log10(Cprime)':log_cp/math.log(10)}


def test_regular_examples():
    # L_{2,2} is finite and (1,U1)-substitutable by direct finite check.
    k, M = 4, 4
    lang = {''.join(x) for x in itertools.product(('a'*k, 'b'), repeat=M)}
    assert len(lang) == 16
    assert is_typed_substitutable(lang, u1_type)
    ds = distributions(lang)
    z0, d = 'b' + 'a'*k, 2*k
    # A small explicit instance of the base relations with g0=0 and mixed omega.
    assert ds.get('a'*d+z0, set()) == ds.get(z0+'a'*d, set())
    assert ds.get(z0+z0, set()) == ds.get('a'*d+z0, set())
    assert ds.get(z0)
    # A finite language cannot admit a positive period for a productive z0.
    assert all(ds.get('a'*p+z0, set()) != ds[z0] for p in range(1, 9))
    # Infinite regular example L_even={w in {a,b}+ : #b(w) even}.
    # Membership depends only on parity of b; all a^p z0 have the same
    # distribution as z0, so p0=1. Test finite contexts explicitly.
    def in_even(word):
        return bool(word) and word.count('b') % 2 == 0
    context_words = [''] + [''.join(t) for length in range(1, 4)
                             for t in itertools.product('ab', repeat=length)]
    for p in range(1, 9):
        for left in context_words:
            for right in context_words:
                assert in_even(left + 'ab' + right) == in_even(left + 'a'*p + 'ab' + right)
    return len(lang)


def main():
    start = time.perf_counter()
    random_checks = test_sequences(random.Random(20261109))
    binomial_checks = test_binomials()
    examples = test_regular_examples()
    stats = test_constants()
    print('PASS: random value sequences:', random_checks)
    print('PASS: binomial inequalities M=6..1000:', binomial_checks)
    print('PASS: typed substitutability/base/aperiodicity for L_2,2:', examples, 'words')
    for key, value in stats.items():
        print('  %s = %.12g' % (key, value))
    print('elapsed_seconds = %.4f' % (time.perf_counter() - start))

if __name__ == '__main__':
    main()
