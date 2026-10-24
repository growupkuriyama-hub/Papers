#!/usr/bin/env python3
"""v79: executable check of the explicit witnesses in
  * Lemma (power-transfer)   and
  * Theorem (no finite typing rescues the bracketed doubling family at
    fan-out two),
see revision/v79_fanout2_lower_bound_research.md, Sections 4.2-4.3.

For a finite typing h let g=h(floor) and let (i0,p) be the index and
period of g on POSITIVE powers: g^i = g^(i+p) for all i >= i0 >= 1.
Witness (s=r=i0, d=p, n=2*i0+p+2 or larger):
    x=(F^s, F^(d+r) a),  y=(F^(s+d), F^r a),
    E=(F, F, rest-after-first-a)      shared:  E[x]=E[y]=W_n,
    F-context: x1 kept at positions 1..s, x2 moved to the second half.
The script draws random transformation monoids (random DFAs) and checks
(i) componentwise equality of h-types, (ii) E[x]=E[y]=Fc[x]=W_n,
(iii) Fc[y] is ceiling-free and != W_n, hence not in L_n.
The proof is symbolic; this only tests the formula implementation.
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v79_lib import transformation_typing  # noqa: E402

FL, FC, CL, CC = "⌊", "⌋", "⌈", "⌉"
ALPH = ["a", FL, FC, CL, CC]


def wstar(n: int) -> str:
    w = "a"
    for _ in range(n):
        w = FL + w + w + FC
    return w


def index_period(h, letter: str, bound: int = 400):
    vals = {}
    for i in range(1, bound):
        v = h(letter * i)
        if v in vals:
            i0 = vals[v]
            return i0, i - i0
        vals[v] = i
    raise RuntimeError("no period found")


def witness(n: int, s: int, d: int, r: int):
    assert n == s + d + r + 2
    W = wstar(n)
    first_a = W.index("a")
    assert first_a == n
    x = (FL * s, FL * (d + r) + "a")
    y = (FL * (s + d), FL * r + "a")
    E = (FL, FL, W[first_a + 1:])
    # second half W_{n-1} starts right after FL + W_{n-1}
    half = wstar(n - 1)
    start2 = 1 + len(half)
    assert W[start2:start2 + n] == FL * (n - 1) + "a"
    end_x2 = start2 + (n - 1) + 1          # position after the a
    beg_x2 = end_x2 - len(x[1])
    Fc = (FL, W[1 + s:beg_x2], W[end_x2:])
    return W, x, y, E, Fc


def fill(E, z):
    return E[0] + z[0] + E[1] + z[1] + E[2]


def check_typing(h, extra: int = 0) -> int:
    i0, p = index_period(h, FL)
    s = r = i0
    d = p
    n = s + d + r + 2 + extra
    r += extra
    W, x, y, E, Fc = witness(n, s, d, r)
    assert all(x) and all(y) and E[1] and Fc[1]
    assert tuple(h(c) for c in x) == tuple(h(c) for c in y), "types differ"
    assert fill(E, x) == W and fill(E, y) == W and fill(Fc, x) == W
    Fy = fill(Fc, y)
    assert Fy != W and CL not in Fy and CC not in Fy
    assert Fy.index("a") == n + d          # first floor-run lengthened by d
    return n


def main(trials: int = 3000, seed: int = 79) -> None:
    rnd = random.Random(seed)
    worst = 0
    for t in range(trials):
        k = rnd.randint(1, 5)
        maps = {c: tuple(rnd.randrange(k) for _ in range(k)) for c in ALPH}
        h = transformation_typing(k, maps, f"rand{t}")
        msize_bound = k ** k
        for extra in (0, 1, 3):
            n = check_typing(h, extra)
            worst = max(worst, n - extra)
            assert n - extra <= 2 * msize_bound + 3
    print(f"PASS: {trials} random typings (DFAs with <=5 states), "
          f"3 offsets each; largest threshold n used = {worst}.")


if __name__ == "__main__":
    main()
