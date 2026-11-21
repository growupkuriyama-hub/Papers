#!/usr/bin/env python3
"""Claude (README (149)): the candidate family of reviews/chatgpt_negative_design_2026-11-04.md,
    A_0 -> ab,  A_1 -> A_0 A_0 | abc,  A_i -> A_{i-1} A_{i-1} | a^i c b  (2 <= i <= n),  S -> A_n,
cannot be repaired by adding words: for n >= 3, EVERY (1,c)-substitutable language containing L_n
also contains the ab-word a(ab)^(2^(n-1)), of length 2^n + 1 < 2^(n+1) = |(ab)^(2^n)|.
Two steps of the sound arity-1 rule SUB_1 (E[x], E[y], F[x] in L and equal contents => F[y] in L),
with i = n-1, y_i = (ab)^(2^i - 2) abc:
  step 1: x = a^i c b (escape of A_i), y = y_i, E = (_, R) with R = abc (ab)^(2^i - 2) (an A_i yield
          containing c), F = (a, _).  E[x], E[y] are A_n -> A_i A_i words of L_n and
          F[x] = a^(i+1) c b = a^n c b is the escape of A_n; forces a y_i.
  step 2: x = (ab)^(2^(i+1) - 2), y = a (ab)^(2^i - 2), E = (_, abc), F = (_, abab);
          E[x] = (ab)^(2^(i+1)-2) abc in L_n, E[y] = a y_i (step 1), F[x] = (ab)^(2^(i+1)) in L_n;
          forces a (ab)^(2^i - 2) abab = a (ab)^(2^i).
Membership in L_n is decided exactly by the grammar (code from the report, section 5).
Windows: py -3 check_claude_negative_shortcut_2026-11-04.py"""
from functools import lru_cache


def escape(i):
    return "abc" if i == 1 else "a" * i + "cb"


def exact_member(n, word):
    @lru_cache(None)
    def inside(i, w):
        if i == 0:
            return w == "ab"
        if w == escape(i):
            return True
        return any(inside(i - 1, w[:k]) and inside(i - 1, w[k:]) for k in range(1, len(w)))
    return inside(n, word)


def fill(E, x):
    return E[0] + x + E[1]


def content(w):
    return frozenset(w)


def step(L, E, x, y, F):
    assert content(x) == content(y)
    for w in (fill(E, x), fill(E, y), fill(F, x)):
        assert w in L, w
    return fill(F, y)


def main():
    for n in range(3, 8):
        i = n - 1
        member = lambda w: exact_member(n, w)
        known = set()

        class Acc:
            def __contains__(self, w):
                return w in known or member(w)
        L = Acc()
        yi = "ab" * (2 ** i - 2) + "abc"           # an A_i yield containing c
        right = "abc" + "ab" * (2 ** i - 2)          # another A_i yield containing c
        assert member(escape(i) + right) and member(yi + right) and member("a" + escape(i))
        w1 = step(L, ("", right), escape(i), yi, ("a", ""))
        assert w1 == "a" + yi and not member(w1)
        known.add(w1)
        x2 = "ab" * (2 ** (i + 1) - 2)
        y2 = "a" + "ab" * (2 ** i - 2)
        w2 = step(L, ("", "abc"), x2, y2, ("", "abab"))
        assert w2 == "a" + "ab" * (2 ** i) and set(w2) == {"a", "b"}
        W = "ab" * (2 ** n)
        print("n=%d forced a(ab)^%d: length %d < |W_n| = %d; in L_n: %s"
              % (n, 2 ** i, len(w2), len(W), member(w2)))
        assert len(w2) < len(W)
    print("SHORTER ab-WORD FORCED FOR n = 3..7 (arity 1 only)")


if __name__ == "__main__":
    main()
