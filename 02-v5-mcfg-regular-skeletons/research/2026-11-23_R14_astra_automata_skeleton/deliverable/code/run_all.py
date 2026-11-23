"""Finite regression checks for R14, separate from its universal proofs."""
from collections import Counter
from functools import lru_cache
from itertools import permutations, product


def words(alphabet, limit, minimum=0):
    for length in range(minimum, limit + 1):
        for letters in product(alphabet, repeat=length):
            yield "".join(letters)


def windows(word, ell):
    return Counter(word[i:i + ell] for i in range(len(word) - ell + 1))


def boundary(word, ell):
    q = ell - 1
    if len(word) < max(1, 2 * q):
        return ("short", word)
    return ("long", word[:q], word[-q:] if q else word[:0])


def audit_local():
    count = windows("aa" + "ba" * 40 + "b" * 201, 2)
    assert count == {"aa": 1, "ab": 41, "ba": 40, "bb": 200}
    c = [1]
    for _ in range(5):
        c.append(4 * c[-1] + 28)
    used = [any(lo <= n < hi for n in count.values())
            for lo, hi in zip(c, c[1:])]
    assert used == [True, True, True, False, False]
    h, t = "abc", "aabbbcccc"
    assert set(t) == set(h) and boundary(h, 1) == boundary(t, 1)
    assert windows(t, 1) - windows(h, 1) == Counter("abbccc")
    cases = 0
    # Replace two disjoint original components, including adjacent intervals.
    for w in words("ab", 6, 2):
        for i, j, l, m in product(range(len(w) + 1), repeat=4):
            if not i < j <= l < m:
                continue
            for ell in (1, 2, 3):
                tagged = [(ch, False) for ch in w[:i]]
                tagged += [(ch, True) for ch in "bb"]
                tagged += [(ch, False) for ch in w[j:l]]
                tagged += [("a", True)]
                tagged += [(ch, False) for ch in w[m:]]
                pure = Counter()
                for start in range(len(tagged) - ell + 1):
                    block = tagged[start:start + ell]
                    if not any(tag for _, tag in block):
                        pure["".join(ch for ch, _ in block)] += 1
                expected = windows(w[:i], ell) + windows(w[j:l], ell) + windows(w[m:], ell)
                assert pure == expected
                cases += 1
    print("T1: E1 frequencies 1,41,40,200; E2 positive; pure-window cases", cases)


# Group multiplication in reading order. Tuples encode maps on {0,1,2}.
S3 = tuple(permutations(range(3)))
ONE = (0, 1, 2)
A = (1, 0, 2)
B = (1, 2, 0)


def mul(g, h):
    return tuple(h[g[i]] for i in range(3))


def inv(g):
    return tuple(g.index(i) for i in range(3))


def generated(generators):
    found, todo = {ONE}, [ONE]
    while todo:
        g = todo.pop()
        for h in generators:
            k = mul(g, h)
            if k not in found:
                found.add(k)
                todo.append(k)
    return found


def derived(group):
    return generated({mul(mul(g, h), mul(inv(g), inv(h)))
                      for g in group for h in group})


def power(g, n):
    value = ONE
    for _ in range(n):
        value = mul(value, g)
    return value


def check_group():
    pairs = 0
    for a, b in product(S3, repeat=2):
        subgroup = generated([a, b])
        comm = derived(subgroup)
        values = {(0, 0): {ONE}}
        for i, j in product(range(32), repeat=2):
            if not (i or j):
                continue
            seen = set()
            if i:
                seen.update(mul(g, a) for g in values[i - 1, j])
            if j:
                seen.update(mul(g, b) for g in values[i, j - 1])
            values[i, j] = seen
            if i and j:
                coset = {mul(mul(power(a, i), power(b, j)), h) for h in comm}
                assert seen <= coset
                if min(i, j) >= max(1, len(subgroup) * (len(subgroup) - 1)):
                    assert seen == coset
                pairs += 1
    print("G(ii): fixed-count S3 letter pairs and positive counts tested", pairs)

    # J in D_2, with edges aa, ab, ba. Start at a, end at a or b.
    # Prefix state gauge b_a=1, b_b=B; fundamental loop values A and BA.
    generators = [A, mul(B, A)]
    comm = derived(generated(generators))
    assert len(comm) == 3
    edge_labels = [A, B, A]
    endpoints = [(0, 0), (0, 1), (1, 0)]

    @lru_cache(maxsize=None)
    def euler_values(v, counts):
        if not any(counts):
            return frozenset([ONE])
        found = set()
        for e, (src, dst) in enumerate(endpoints):
            if src != v or not counts[e]:
                continue
            remaining = list(counts)
            remaining[e] -= 1
            found.update(mul(edge_labels[e], g) for g in euler_values(dst, tuple(remaining)))
        return frozenset(found)

    threshold = 6 * (2 * 6 - 1) + 1
    for m, t, final_b in product([1, 2, threshold], [1, 3, threshold], [0, 1]):
        counts = (m, t + final_b, t)
        seen = euler_values(0, counts)
        base = mul(power(A, m), power(mul(B, A), t))
        coset = {mul(mul(g, base), power(B, final_b)) for g in comm}
        assert seen and seen <= coset
        if min(counts) >= threshold:
            assert seen == coset
    print("G(iii): D2 path, open and closed cases, including threshold", threshold)

    for n in [2, 8, 72]:
        frozen = {mul(mul(power(A, i), B), power(A, n - i)) for i in range(n + 1)}
        assert frozen == {B, inv(B)}
        u, v = sorted(frozen)
        assert power(mul(inv(u), v), 2) != ONE
    print("Frozen external edge: two values, quotient has order 3")

    # Two slots in a full S3 pool. Each split of the edge counts is allowed.
    # The recurrent table enumerates individual words by their last letter.
    counts = (37, 38)
    table = {(0, 0): {ONE}}
    for i, j in product(range(counts[0] + 1), range(counts[1] + 1)):
        if i or j:
            table[i, j] = ({mul(x, A) for x in table[i - 1, j]} if i else set())
            if j:
                table[i, j].update(mul(x, B) for x in table[i, j - 1])
    actual = set()
    for (i, j), possible in table.items():
        for left, right in product(possible, table[counts[0] - i, counts[1] - j]):
            actual.add(mul(mul(left, A), right))
    abelian_coset = table[counts]
    predicted = {mul(mul(x, A), y) for x, y in product(S3, repeat=2)
                 if mul(x, y) in abelian_coset}
    assert len(abelian_coset) == 3 and actual == predicted
    # Pure 2-cycle in D2. Proper based subgroup, nontrivial endpoint gauge.
    for a, b in product(S3, repeat=2):
        h = mul(b, a)
        for repetitions in (67, 68):
            closed = power(h, repetitions)
            val = ONE
            for label in (b, a) * repetitions + (b,):
                val = mul(val, label)
            assert val == mul(closed, b)
            assert derived(generated([h])) == {ONE}
    print("Frozen-slot formula at (37,38); proper cyclic loop groups with endpoint gauge")


def act(w, start):
    state = start
    for ch in w:
        if ch == "a":
            state ^= 1
        elif state:
            return -1
    return state


def sigma(w):
    return act(w, 0), act(w, 1)


def compose_partial(a, b):
    return tuple(b[t] if t >= 0 else -1 for t in a)


def decorate(w, start=0):
    tagged = []
    for ch in w:
        tagged.append((start, ch))
        start ^= int(ch == "a")
    return tuple(tagged)


def recover(tagged):
    entrance = tagged[0][0]
    last, ch = tagged[-1]
    shift = entrance ^ last ^ int(ch == "a")
    b_states = {p for p, z in tagged if z == "b"}
    return tuple((i ^ shift) if all((entrance ^ i ^ t) == 0 for t in b_states)
                 else -1 for i in range(2))


def accepted(w):
    return all(len(run) % 2 == 0 for run in w.split("b"))


def check_runs():
    sample = list(words("ab", 9, 1))
    semigroup = {sigma(w) for w in sample}
    assert len(semigroup) == 7
    assert all(compose_partial(u, v) in semigroup for u, v in product(semigroup, repeat=2))
    assert sum(compose_partial(v, v) == v for v in semigroup) == 4
    b = sigma("b")
    assert {compose_partial(compose_partial(b, v), b) for v in semigroup} == {b, (-1, -1)}
    for w in sample:
        assert (sigma(w)[0] == 0) == accepted(w)
        for i in [0, 1]:
            assert recover(decorate(w, i)) == sigma(w)
    for ell in range(1, 9):
        n = ell
        w = "b" + "a" * (2 * n) + "b" + "a" * (2 * n) + "b"
        v = "b" + "a" * (2 * n + 1) + "b" + "a" * (2 * n - 1) + "b"
        assert accepted(w) and not accepted(v)
        assert boundary(w, ell) == boundary(v, ell) and windows(w, ell) == windows(v, ell)
    print("Even runs: 7 maps, 4 idempotents, 2 local elements; decoration tests", 2 * len(sample))

    # Test transport of equal decorated types across different entry parities.
    pools = {}
    for w in words("ab", 5, 1):
        for start in [0, 1]:
            x = decorate(w, start)
            pools.setdefault((frozenset(x), boundary(x, 2)), []).append(w)
    contexts = list(words("ab", 2))
    tests = 0
    for items in pools.values():
        x = items[0]
        for y in items:
            for left, middle, right in product(contexts, contexts[1:], contexts):
                for other in ("a", "ba", "bab"):
                    assert accepted(left + x + middle + other + right) == accepted(
                        left + y + middle + other + right)
                    assert accepted(left + other + middle + x + right) == accepted(
                        left + other + middle + y + right)
                    tests += 2
    print("Two-hole component tests for E, with nonempty central separator", tests)


if __name__ == "__main__":
    audit_local()
    check_group()
    check_runs()
    print("CERTIFIED FINITE: all checks passed")
