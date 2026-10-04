#!/usr/bin/env python3
"""Exhaustive K4 search for q=6 simultaneous factorizations.

For d=3, an abelian-group direct-factor sharpness witness with q=6 would be
four 6-subsets B_0,...,B_3 of an abelian group G of order 36 such that every
pair gives an exact factorization G=B_i+B_j.  Independent translations let us
normalize every B_i to contain 0.

For normalized A,B of size 6,
    G=A+B is an exact factorization
iff
    (A-A) intersect (B-B) = {0}.
Thus a K4 is exactly four nonzero difference masks that are pairwise disjoint.

The four abelian groups of order 36 are:
    C36, C18 x C2, C12 x C3, C6 x C6.

This script exhaustively enumerates C(35,5)=324632 normalized 6-subsets in
each group, collapses subsets with identical difference masks, and searches
for four pairwise-disjoint nonzero masks.
"""

from __future__ import annotations

import argparse
import itertools
import math
from collections import Counter


GROUPS = {
    "C36": (36,),
    "C18xC2": (18, 2),
    "C12xC3": (12, 3),
    "C6xC6": (6, 6),
}


def make_group(mods: tuple[int, ...]):
    elems = list(itertools.product(*[range(m) for m in mods]))
    index = {x: i for i, x in enumerate(elems)}
    n = len(elems)
    sub = [[0] * n for _ in range(n)]
    for i, a in enumerate(elems):
        for j, b in enumerate(elems):
            c = tuple((x - y) % m for x, y, m in zip(a, b, mods))
            sub[i][j] = index[c]
    return elems, sub


def normalized_difference_masks(mods: tuple[int, ...], q: int = 6):
    elems, sub = make_group(mods)
    n = len(elems)
    if n != q * q:
        raise ValueError(f"group order {n} is not q^2={q*q}")

    first_witness: dict[int, tuple[int, ...]] = {}
    for comb in itertools.combinations(range(1, n), q - 1):
        A = (0,) + comb
        mask = 1  # bit 0
        for a in A:
            for b in A:
                mask |= 1 << sub[a][b]
        first_witness.setdefault(mask, A)
    return first_witness


def find_k_clique_by_disjoint_masks(
    mask_to_subset: dict[int, tuple[int, ...]],
    group_order: int,
    k: int = 4,
):
    # Drop the zero-difference bit.  Exact factorization means disjoint masks.
    items = [(mask >> 1, A) for mask, A in mask_to_subset.items()]
    items.sort(key=lambda x: x[0].bit_count())

    masks = [m for m, _ in items]
    subsets = [A for _, A in items]
    sizes = [m.bit_count() for m in masks]
    min_size = sizes[0]

    def search(chosen: list[int], used: int, start: int):
        depth = len(chosen)
        if depth == k:
            return chosen
        remaining = k - depth
        if used.bit_count() + min_size * remaining > group_order - 1:
            return None

        for i in range(start, len(items)):
            if (
                used.bit_count()
                + sizes[i]
                + min_size * (remaining - 1)
                > group_order - 1
            ):
                break
            if masks[i] & used:
                continue
            out = search(chosen + [i], used | masks[i], i + 1)
            if out is not None:
                return out
        return None

    indices = search([], 0, 0)
    if indices is None:
        return None
    return [subsets[i] for i in indices]


def run_one(name: str, mods: tuple[int, ...]):
    q = 6
    masks = normalized_difference_masks(mods, q=q)
    clique = find_k_clique_by_disjoint_masks(masks, q * q, k=4)
    dist = Counter((mask >> 1).bit_count() for mask in masks)

    print(f"{name}: mods={mods}")
    print(f"  normalized 6-subsets checked = {math.comb(35, 5)}")
    print(f"  distinct difference masks    = {len(masks)}")
    print(f"  minimum nonzero |A-A|        = {min(dist)}")
    print(f"  K4 found                     = {clique is not None}")
    if clique is not None:
        print(f"  witness                      = {clique}")
    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--group",
        choices=["all", *GROUPS],
        default="all",
    )
    args = parser.parse_args()

    if args.group == "all":
        for name, mods in GROUPS.items():
            run_one(name, mods)
    else:
        run_one(args.group, GROUPS[args.group])


if __name__ == "__main__":
    main()
