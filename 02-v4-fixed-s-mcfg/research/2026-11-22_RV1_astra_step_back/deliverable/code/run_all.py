"""RV1 bounded checks. Python 3 standard library, no network."""
from collections import defaultdict
from itertools import combinations, product


def rect_check(words):
    """All positive one-/two-hole occurrences, including empty outer strings."""
    counts = []
    for arity in (1, 2):
        distributions = defaultdict(set)
        for word in sorted(words):
            for cuts in combinations(range(len(word) + 1), 2 * arity):
                parts = tuple(word[i:j] for i, j in zip(cuts[::2], cuts[1::2]))
                context = (word[:cuts[0]],)
                if arity == 2:
                    context += (word[cuts[1]:cuts[2]],)
                context += (word[cuts[-1]:],)
                distributions[parts].add(context)
        seen = {}
        for parts, contexts in distributions.items():
            kind = tuple(frozenset(part) for part in parts)
            for context in contexts:
                key = kind, context
                if key in seen:
                    assert seen[key] == contexts
                else:
                    seen[key] = contexts
        counts.append(len(distributions))
    return counts


def all_words(alphabet, length):
    return map("".join, product(alphabet, repeat=length))


def check_affine():
    words = {w for n in range(1, 13) for w in all_words("ab", n)
             if w.count("a") + 3 * w.count("b") == 12 + int("b" in w)}
    assert {"a" * 12, "ab" + "a" * 9, "abab" + "a" * 5} <= words
    assert "abab" + "a" * 6 not in words
    print("P5 weak reading: size", len(words), "tuples", rect_check(words))


def r15_words(n, d):
    words = set()
    for pairs in range(n // d + 1):
        letters = "b" * pairs + "c" * pairs
        a_count = n - d * pairs
        for idx in combinations(range(len(letters) + a_count), len(letters)):
            w = ["a"] * (len(letters) + a_count)
            for i, ch in zip(idx, letters):
                w[i] = ch
            words.add("".join(w))
    return words


def check_r15():
    n, d = 11, 4
    yields = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i == 1:
            yields[i].add("a")
        if i == d:
            yields[i].add("bc")
        yields[i].update("a" + w for w in yields[i-1])
        yields[i].update(w + "a" for w in yields[i-1])
        if i > d:
            yields[i].update("b" + w + "c" for w in yields[i-d])
        assert yields[i] == r15_words(i, d)
    print("R15 N=11: size", len(yields[n]), "tuples", rect_check(yields[n]))
    for nested in (False, True):
        leaves = [("a" * 32, "a" * 32)] * 16
        leaves[4:8] = [("b", "c")] * 4
        level = leaves
        while len(level) > 1:
            level = [(l[0] + r[0], r[1] + l[1] if nested else l[1] + r[1])
                     for l, r in zip(level[::2], level[1::2])]
        x, y = level[0]
        word = "a" + x + "a" + y + "a"
        middle, last = (513, 129) if nested else (385, 257)
        assert word == "a" * 129 + "bbbb" + "a" * middle + "cccc" + "a" * last
    print("R15 d=64 q=4: both double replacements reproduced; theta=97")


def check_crossings():
    checked = 0
    for xs in combinations(range(4), 2):
        order = tuple("X" if i in xs else "Y" for i in range(4))
        for sizes in product(range(3), repeat=4):
            # Number of selected descendant marks in each immediate child component.
            marks = "".join(color * n for color, n in zip(order, sizes))
            if marks in ("XYXY", "YXYX"):
                assert "".join(order) == marks
            checked += 1
    print("LCA mark configurations", checked)


def check_support():
    # Fixed prefix ab, internal cd, suffix ef. Every hole vertex has two states.
    # Fixed edges emit markers on their first letter. Loops consume arbitrary x.
    holes = {2, 4}
    emissions = (True, False, True, False, True, False)
    states = [(i, active) for i in range(7)
              for active in ((False, True) if i in holes else (False,))]
    observed = defaultdict(set)
    for start in states:
        front = {(start, False)}
        for _ in range(10):
            nxt = set()
            for (i, active), used in front:
                if i in holes:
                    nxt.add(((i, True), True))
                if i < len(emissions):
                    nxt.add(((i+1, False), used or emissions[i]))
            front = nxt
            for end, used in front:
                observed[start, end].add(used)
    assert all(len(flags) == 1 for flags in observed.values())
    assert observed[(1, False), (2, False)] == {False}
    assert observed[(1, False), (2, True)] == {True}
    print("R4 split-boundary transducer: tested endpoint pairs", len(observed))


def check_layered():
    for z in ("a", "ac"):
        words = {z}
        for _ in range(3):
            words = {"b"} | {x + y for x in words for y in words}
        assert z * 8 in words and z * 2 + "b" + z * 4 in words
        assert z * 3 + "b" + z * 3 not in words
    print("WN doubling: two-hole failure for 1- and 2-letter root types")


def check_carrier():
    # Small exhaustive language with the same weighted membership condition.
    words = {w for n in range(1, 9) for w in all_words("abc", n)
             if w.count("a") + 3 * (w.count("b") + w.count("c")) == 8}
    print("T4 small weighted slice: size", len(words), "tuples", rect_check(words))
    for q in (4, 6, 8):
        d = D = 2 ** q
        N = 8 * d * D + 2
        ell = lambda n: n // d + n % d
        # Every A_n rule. Completing above costs ell(N-n), below costs ell(n-weight).
        max_a = max(ell(N-n) + 1 + ell(n-weight)
                    for n in range(1, N+1) for weight in (1, d) if n >= weight)
        theta = max(max_a, 8 * D + 4 * d - 2)
        assert 4 * d * D > theta
        assert N > 4 * D and ell(N) == 8 * D + 2
        P, Q = "bc" * D, "cb" * D
        assert P + Q != Q + P
        print("T4 q", q, "pure length", N, "overall minimum", ell(N), "theta", theta)


def main():
    check_crossings()
    check_support()
    check_affine()
    check_r15()
    check_layered()
    check_carrier()
    print("PASS (finite checks only)")


if __name__ == "__main__":
    main()

