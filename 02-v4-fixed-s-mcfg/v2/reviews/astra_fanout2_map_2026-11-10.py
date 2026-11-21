#!/usr/bin/env python3
"""Reproducible checks; Python 3 standard library only. Seed: 20261110.
No bounded word test is used as a proof of infinite-language membership.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial, gcd
import random
import time

SEED = 20261110


def indexed_group(elements, mul, identity):
    elements = list(elements)
    idx = {g: i for i, g in enumerate(elements)}
    table = [[idx[mul(g, h)] for h in elements] for g in elements]
    e = idx[identity]
    inv = [next(j for j in range(len(elements))
                if table[i][j] == e and table[j][i] == e)
           for i in range(len(elements))]
    return table, e, inv, idx


def test_groups():
    groups = []
    for n in (2, 3, 4):
        groups.append(("C" + str(n), indexed_group(
            range(n), lambda a, b, n=n: (a+b) % n, 0)))
    groups.append(("C2xC2", indexed_group(
        list(product(range(2), repeat=2)),
        lambda a, b: ((a[0]+b[0]) % 2, (a[1]+b[1]) % 2), (0, 0))))
    groups.append(("S3", indexed_group(
        permutations(range(3)),
        lambda a, b: tuple(a[b[i]] for i in range(3)), (0, 1, 2))))
    groups.append(("D8", indexed_group(
        list(product(range(4), range(2))),
        lambda a, b: ((a[0]+(-1 if a[1] else 1)*b[0]) % 4,
                      (a[1]+b[1]) % 2), (0, 0))))
    return groups


def distribution_masks(tab, e, d):
    n = len(tab)
    tuples = list(product(range(n), repeat=d))
    contexts = list(product(range(n), repeat=d+1))
    rows = []
    for x in tuples:
        masks = [0]*n
        for j, ctx in enumerate(contexts):
            val = ctx[0]
            for i, a in enumerate(x):
                val = tab[tab[val][a]][ctx[i+1]]
            masks[val] |= 1 << j
        rows.append(masks)
    return rows


def overlap_equal(rows, accepted):
    sigs = []
    for masks in rows:
        sig = 0
        for a in accepted:
            sig |= masks[a]
        sigs.append(sig)
    for i, a in enumerate(sigs):
        for b in sigs[i+1:]:
            if a & b and a != b:
                return False
    return True


def predicted(tab, e, inv, accepted):
    n = len(tab)
    if not accepted:
        return True, True
    p = min(accepted)
    normal = {tab[inv[p]][a] for a in accepted}
    if e not in normal:
        return False, False
    if any(tab[a][b] not in normal for a in normal for b in normal):
        return False, False
    if any(tab[tab[g][a]][inv[g]] not in normal
           for g in range(n) for a in normal):
        return False, False
    abelian_quotient = all(
        tab[tab[tab[a][b]][inv[a]]][inv[b]] in normal
        for a in range(n) for b in range(n))
    return True, abelian_quotient


def finite_group_check():
    print("[1] Exact finite-group distribution checks (all accepting subsets)")
    for name, (tab, e, inv, idx) in test_groups():
        n = len(tab)
        rows1 = distribution_masks(tab, e, 1)
        rows2 = distribution_masks(tab, e, 2)
        count1 = count2 = mismatches = 0
        for mask in range(1 << n):
            p = {i for i in range(n) if mask >> i & 1}
            a1 = overlap_equal(rows1, p)
            a2 = overlap_equal(rows2, p)
            b1, b2 = predicted(tab, e, inv, p)
            mismatches += ((a1, a1 and a2) != (b1, b2))
            count1 += a1
            count2 += a1 and a2
        assert mismatches == 0
        print(name, "subsets", 1 << n, "SUB1", count1,
              "SUB1+2", count2, "mismatches", mismatches)


def full_content_reps(tab, e, letters):
    keys = sorted(letters)
    target = (1 << len(keys))-1
    seen = {(e, 0): ""}
    queue = deque([(e, 0)])
    while queue:
        g, mask = queue.popleft()
        for j, a in enumerate(keys):
            nxt = (tab[g][letters[a]], mask | (1 << j))
            if nxt not in seen:
                seen[nxt] = seen[(g, mask)] + a
                queue.append(nxt)
    return {g: seen[(g, target)] for g in range(len(tab))}


def fill(ctx, x):
    out = ctx[0]
    for i, w in enumerate(x):
        out += w + ctx[i+1]
    return out


def s3_certificate():
    name, data = next(x for x in test_groups() if x[0] == "S3")
    tab, e, inv, idx = data
    letters = {"a": idx[(1, 0, 2)], "b": idx[(0, 2, 1)], "c": e}
    reps = full_content_reps(tab, e, letters)
    s, t = letters["a"], letters["b"]
    x = (reps[s], reps[inv[s]])
    y = (reps[e], reps[e])
    E = ("", reps[e], "")
    F = ("", reps[t], reps[inv[t]])

    def val(w):
        v = e
        for a in w:
            v = tab[v][letters[a]]
        return v

    words = [fill(E, x), fill(E, y), fill(F, y), fill(F, x)]
    flags = [val(w) == e for w in words]
    assert flags == [True, True, True, False]
    assert list(map(set, x)) == list(map(set, y))
    print("[2] S3 kernel certificate: X,Y,E,F =", x, y, E, F)
    print("words E[X],E[Y],F[Y],F[X] =", words)
    print("accepted =", flags)


def words_upto(alphabet, cap):
    for n in range(1, cap+1):
        for t in product(alphabet, repeat=n):
            yield "".join(t)


def occurrences(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i+1, n+1):
                yield (w[i:j],), (w[:i], w[j:])
    else:
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for ell in range(k+1, n+1):
                        yield (w[i:j], w[k:ell]), (w[:i], w[j:k], w[ell:])


def word_check(accepted_words, member, d):
    # Every premise sentence is in accepted_words. The conclusion is checked
    # against the actual membership predicate, even if it exceeds the bound.
    dist = defaultdict(set)
    shared = defaultdict(set)
    for w in accepted_words:
        for x, ctx in occurrences(w, d):
            typ = tuple("".join(sorted(set(a))) for a in x)
            dist[x].add(ctx)
            shared[(ctx, typ)].add(x)
    seen_pairs = set()
    for (E, typ), values in sorted(shared.items()):
        for x, y in combinations(sorted(values), 2):
            if (x, y) in seen_pairs:
                continue
            seen_pairs.add((x, y))
            for a, b in ((x, y), (y, x)):
                for H in sorted(dist[a]):
                    result = fill(H, b)
                    if not member(result):
                        return {"X": a, "Y": b, "E": E, "H": H,
                                "premises": [fill(E, a), fill(E, b), fill(H, a)],
                                "missing": result}, len(seen_pairs)
    return None, len(seen_pairs)


def stage(w):
    pos = 0
    while pos < len(w) and w[pos] == "a":
        pos += 1
    return 0 < pos < len(w) and all(a in "bc" for a in w[pos:])


def bounded_checks():
    print("[3] Bounded word checks: all three premise sentences length <= 6")
    universe = list(words_upto("abc", 6))
    predicates = [("stage+Z", lambda w: stage(w) and w.count("a") == w.count("b"))]
    for q in (1, 2, 3, 4):
        predicates.append(("stage+C"+str(q),
                           lambda w, q=q: stage(w) and len(w) % q == 0))
    for name, member in predicates:
        language = [w for w in universe if member(w)]
        counts = []
        for d in (1, 2):
            bad, checked = word_check(language, member, d)
            assert bad is None, (name, d, bad)
            counts.append(checked)
        print(name, "positive words", len(language), "tuple pairs", counts,
              "violations 0 (bounded only)")
    print("[4] Finite-language checks (all positive premises enumerated)")
    for n in (7, 8, 9):
        w = "b" + "a"*(n-1)
        for d in (1, 2):
            bad, _ = word_check([w], lambda x, w=w: x == w, d)
            assert bad is None
        print("singleton", w, "SUB1+2 pass; literal B7 list omits this reversal")
    L = {"".join(w) for w in product("ab", repeat=3)} - {"aaa", "bbb"}
    S = L - {"bba"}
    for d in (1, 2):
        assert word_check(sorted(L), lambda w: w in L, d)[0] is None
    bad, _ = word_check(sorted(S), lambda w: w in S, 1)
    assert bad is not None
    print("B9 target SUB1+2 pass; S violation:", bad)
    Lsmall = {"aba", "cbb", "aaa"}
    for d in (1, 2):
        assert word_check(sorted(Lsmall), lambda w: w in Lsmall, d)[0] is None
    X, Y, E, H = ("a", "a"), ("c", "b"), ("", "b", ""), ("", "a", "")
    assert all(w in Lsmall for w in (fill(E, X), fill(E, Y), fill(H, X)))
    assert fill(H, Y) == "cab" and "cab" not in Lsmall
    print("B1 without equal types: target SUB1+2 pass; aba,cbb,aaa accepted; cab rejected")


def rref(matrix, width):
    a = [[Fraction(x) for x in row] for row in matrix]
    pivots = []
    row = 0
    for col in range(width):
        p = next((i for i in range(row, len(a)) if a[i][col]), None)
        if p is None:
            continue
        a[row], a[p] = a[p], a[row]
        value = a[row][col]
        a[row] = [x/value for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                factor = a[i][col]
                a[i] = [x-factor*y for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def integer_null_vector(matrix, width):
    a, pivots = rref(matrix, width)
    free = next((j for j in range(width) if j not in pivots), None)
    if free is None:
        return None
    v = [Fraction(0)]*width
    v[free] = 1
    for i, p in enumerate(pivots):
        v[p] = -a[i][free]
    denom = 1
    for x in v:
        denom = denom*x.denominator // gcd(denom, x.denominator)
    ints = [int(x*denom) for x in v]
    divisor = 0
    for x in ints:
        divisor = gcd(divisor, abs(x))
    return [x//divisor for x in ints]


def matvec(D, x):
    return [sum(a*b for a, b in zip(row, x)) for row in D]


def orthant_shorten(D, c, coefficients, allowed):
    k, h = len(D), len(coefficients)
    B = max(1, max((abs(a) for row in D for a in row), default=0))
    C = max(1, max(map(abs, c)))
    T = factorial(k)*B**k
    delta = list(coefficients)
    y = [a+b for a, b in zip(c, matvec(D, delta))]
    assert all(a >= 0 for a in y)
    assert all(y[i] == 0 for i in range(k) if i not in allowed)
    before = sum(y)
    steps = 0
    while True:
        large = {i for i in range(k) if y[i] >= T}
        lam = integer_null_vector([D[i] for i in range(k) if i not in large], h)
        if lam is None:
            break
        z = matvec(D, lam)
        assert any(z)
        assert max(map(abs, z)) <= T
        assert all(z[i] == 0 for i in range(k) if i not in large)
        if sum(z) < 0:
            lam, z = [-a for a in lam], [-a for a in z]
        q = min(y[i]//z[i] for i in range(k) if z[i] > 0)
        assert q >= 1
        y = [a-q*b for a, b in zip(y, z)]
        delta = [a-q*b for a, b in zip(delta, lam)]
        assert y == [a+b for a, b in zip(c, matvec(D, delta))]
        assert all(a >= 0 for a in y)
        new_large = {i for i in range(k) if y[i] >= T}
        assert new_large < large
        steps += 1
    bound = k*C+k*k*T*(T+C)
    assert steps <= k and sum(y) <= before and sum(y) <= bound
    assert all(y[i] == 0 for i in range(k) if i not in allowed)
    return steps, before, sum(y), y


def lattice_checks():
    rng = random.Random(SEED)
    tested = deficient = max_steps = 0
    largest_before = 0
    for k in range(1, 5):
        for trial in range(100):
            active = k if trial % 3 else max(1, k-1)
            h = rng.randint(1, active)
            while True:
                D = [[rng.randint(1, 3)] + [rng.randint(-3, 3) for _ in range(h-1)]
                     for _ in range(active)]
                D += [[0]*h for _ in range(k-active)]
                if len(rref(D, h)[1]) == h:
                    break
            c = [rng.randint(-5, 5) for _ in range(active)] + [0]*(k-active)
            coeff = [rng.randint(10**5, 10**6)] + [rng.randint(-1000, 1000)
                                                  for _ in range(h-1)]
            steps, before, after, result = orthant_shorten(D, c, coeff, set(range(active)))
            tested += 1
            deficient += h < k
            max_steps = max(max_steps, steps)
            largest_before = max(largest_before, before)
    print("[5] Constructive orthant lemma tests; seed", SEED)
    print("cases", tested, "rank-deficient", deficient, "max steps", max_steps,
          "largest initial l1", largest_before, "failures 0")
    D = [[1, 0], [1, 0], [0, 1]]
    p, N = 2**80, 2**96
    steps, before, after, y = orthant_shorten(
        D, [0, 0, -2], [p-1, N+1], {0, 1, 2})
    n = [y[i]+1 for i in range(3)]
    assert n == [1, 1, 1]
    print("two-component example (a^p,b^p c^N), p=2^80,N=2^96:",
          "short counts", n, "steps", steps, "representative (a,bc)")
    steps, before, after, y = orthant_shorten(
        [[2, 0], [0, 2]], [0, 0],
        [Fraction(2**80+1, 2), Fraction(2**90+1, 2)], {0, 1})
    assert y == [1, 1]
    print("nonprimitive sublattice basis test:", list(map(int, y)),
          "in H=< (2,0),(0,2),(1,1) >; parity coset preserved")
    assert orthant_shorten([[], []], [3, 0], [], {0})[3] == [3, 0]
    print("rank-zero lattice test passed")


def grammar_checks():
    # S -> a S T | a T; T -> b | c T | T c.
    pS, pT = (1, 1, 0), (0, 1, 0)
    rules = [("S", (1, 0, 0), [pS, pT], 3),
             ("S", (1, 0, 0), [pT], 2),
             ("T", (0, 1, 0), [], 1),
             ("T", (0, 0, 1), [pT], 2),
             ("T", (0, 0, 1), [pT], 2)]
    deltas = []
    size = 2
    for head, term, children, template_length in rules:
        parent = pS if head == "S" else pT
        d = tuple(term[i]+sum(p[i] for p in children)-parent[i] for i in range(3))
        deltas.append(d)
        size += 1+len(children)+template_length
    assert size == 22
    assert set(deltas) == {(0, 0, 0), (1, 1, 0), (0, 0, 1)}
    print("[6] Grammar S_infinity: size", size, "rule deltas", deltas,
          "rank", len(rref(deltas, 3)[1]))
    for n in range(1, 6):
        size = (n+2)+5+2+2+3*(n+1)+2+7*n
        assert size == 11*n+16
    print("Refinement example size=11n+16 checked for n=1..5")
    augmented_size = 22
    augmented_size += 1+(1+1+3)+(1+0+2)+(1+1+4)+(1+1+3)
    assert augmented_size == 42
    print("Fan-out-2 redundant extension: size", augmented_size,
          "thickness 5 by explicit shortest rule witnesses in report")


def main():
    start = time.monotonic()
    finite_group_check()
    s3_certificate()
    bounded_checks()
    lattice_checks()
    grammar_checks()
    print("ALL CHECKS PASSED")
    print("Elapsed seconds (machine dependent):", round(time.monotonic()-start, 3))


if __name__ == "__main__":
    main()
