#!/usr/bin/env python3
"""Reproduce a (2,h)-substitutability failure for the CFG doubling family L_3.

Here h=(h_Sigma^{1,1},h_U), h_U maps ceiling brackets to the absorbing
element of the two-element semilattice and all other letters to the identity.
The example does NOT settle fixed windows of width >= 2, or higher-rank
MCFG characteristic-sample lower bounds.

Run: python3 revision/check_fanout2_window1_counterexample.py
"""
from __future__ import annotations


def doubling_languages(max_level: int) -> list[set[str]]:
    levels = [{"a"}]
    for _ in range(max_level):
        old = levels[-1]
        levels.append(
            {"⌊" + p + q + "⌋" for p in old for q in old}
            | {"⌈" + p + "⌉" for p in old}
        )
    return levels


def typing_1(word: str) -> tuple[object, object]:
    # All test tuples have length >=2; the original window morphism
    # records words of length <2 with a separate short-word tag.
    window = ("long", word[0], word[-1]) if len(word) >= 2 else ("short", word)
    semilattice = "zeta" if ("⌈" in word or "⌉" in word) else "one"
    return window, semilattice


def main() -> None:
    levels = doubling_languages(3)
    assert list(map(len, levels)) == [1, 2, 6, 42]
    x = ("⌊⌈a⌉⌈", "⌉⌋")
    y = ("⌊⌈", "⌉⌊aa⌋⌋")

    def E(u: tuple[str, str]) -> str:
        return "⌈" + u[0] + "a" + u[1] + "⌉"

    def F(u: tuple[str, str]) -> str:
        return "⌊" + u[0] + "a⌉⌋⌈⌈a⌉" + u[1]

    assert tuple(map(typing_1, x)) == tuple(map(typing_1, y))
    values = {"E[x]": E(x), "E[y]": E(y), "F[x]": F(x), "F[y]": F(y)}
    expected = {"E[x]": True, "E[y]": True, "F[x]": True, "F[y]": False}
    for key, word in values.items():
        assert (word in levels[3]) is expected[key], (key, word)
        print(f"{key}: {word} | in L3 = {word in levels[3]}")
    assert F(y)[1:-1] not in {u + v for u in levels[2] for v in levels[2]}
    print("PASS: (2, h_window_1 x h_U) substitutability fails for L_3.")


if __name__ == "__main__":
    main()
