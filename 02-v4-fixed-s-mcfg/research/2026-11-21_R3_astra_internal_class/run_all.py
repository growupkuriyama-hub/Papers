"""R3 finite checks. Run with python3 -I run_all.py. Standard library only."""

from collections import defaultdict
from functools import lru_cache


def pure_word(level):
    word = "a"
    for _ in range(level):
        word = "b" + word * 2 + "b"
    return word


def next_sets(all_previous, marked_previous):
    unary = {"c" + word + "c" for word in all_previous}
    binary = {"b" + left + right + "b"
              for left in all_previous for right in all_previous}
    flagged_binary = {"b" + left + right + "b"
                      for first, second in ((marked_previous, all_previous),
                                            (all_previous, marked_previous))
                      for left in first for right in second}
    return unary | binary, unary | flagged_binary


def distributions(words):
    result = defaultdict(set)
    for word in words:
        for start in range(len(word)):
            for stop in range(start + 1, len(word) + 1):
                result[word[start:stop]].add((word[:start], word[stop:]))
    return result


def rect_check(dists, typing):
    # Every shared context and type must select exactly one distribution.
    context_rows = {}
    for x, contexts in dists.items():
        for context in contexts:
            row = context_rows.setdefault((typing(x), context), contexts)
            assert row == contexts


def finite_one_hole():
    all_words, marked = {"a"}, set()
    for level in range(1, 4):
        all_words, marked = next_sets(all_words, marked)
        assert marked == all_words - {pure_word(level)}
        assert min(map(len, marked)) == 2 * level + 1
        dists = distributions(marked)
        target = pure_word(level - 1)
        for typing in (lambda x: "c" in x, frozenset):
            rect_check(dists, typing)
            cl = {x for x in dists
                  if typing(x) == typing(target) and dists[x] == dists[target]}
            assert cl == {target}
        print(f"n={level} words={len(marked)} one-hole fillers={len(dists)} "
              f"root shortest={min(map(len, marked))} tau={len(target)} "
              "Rect(U,content)=PASS class=singleton")


def accepts(word, level):
    @lru_cache(None)
    def end(i, pos):
        if pos >= len(word):
            return -1
        ch = word[pos]
        if i == 0:
            return pos + 1 if ch == "a" else -1
        if ch not in "bc":
            return -1
        stop = end(i - 1, pos + 1)
        if stop >= 0 and ch == "b":
            stop = end(i - 1, stop)
        if 0 <= stop < len(word) and word[stop] == ch:
            return stop + 1
        return -1

    return "c" in word and end(level, 0) == len(word)


def finite_two_hole():
    for k in range(4, 10):
        child = pure_word(k - 1)
        sentence = "c" + pure_word(k) + "c"
        left = "cb"
        # Index of the first a in the second copy of W_{k-1}.
        first_a = 2 + len(child) + k - 1
        mid = sentence[3:first_a - 2]
        right = sentence[first_a:]
        common = ("c", "b", sentence[5:])
        test = (left, mid, right)
        x, y = ("b", "bb"), ("bb", "b")

        def fill(context, pair):
            u, v, w = context
            return u + pair[0] + v + pair[1] + w

        words = [fill(ctx, pair) for ctx in (common, test) for pair in (x, y)]
        assert "a" in mid and words[:3] == [sentence] * 3
        assert [accepts(w, k + 1) for w in words] == [True, True, True, False]
        print(f"n={k + 1} two-hole four memberships=1110 |w|={len(sentence)}")


if __name__ == "__main__":
    finite_one_hole()
    finite_two_hole()
    print("All finite checks passed.")
