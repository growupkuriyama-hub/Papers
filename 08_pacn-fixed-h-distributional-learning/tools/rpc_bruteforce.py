#!/usr/bin/env python3
"""Brute-force rectangular product capacity for small marked finite monoids.

This is a research utility for the PAC_n fixed-h project.  It computes

    rpc_r(M,P)

where P is the subset of monoid elements realized by nonempty words.

The search is exponential and intended only for small examples.
"""

from __future__ import annotations

import argparse
import itertools
import math
from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class MarkedMonoid:
    table: tuple[tuple[int, ...], ...]
    positive: tuple[int, ...]
    name: str = "monoid"

    @property
    def size(self) -> int:
        return len(self.table)

    def mul(self, a: int, b: int) -> int:
        return self.table[a][b]


def cyclic(n: int) -> MarkedMonoid:
    table = tuple(tuple((i + j) % n for j in range(n)) for i in range(n))
    return MarkedMonoid(table, tuple(range(n)), f"C_{n}")


def chain_semilattice(n: int) -> MarkedMonoid:
    table = tuple(tuple(max(i, j) for j in range(n)) for i in range(n))
    return MarkedMonoid(table, tuple(range(n)), f"Chain_{n}")


def boolean_semilattice(atoms: int) -> MarkedMonoid:
    n = 1 << atoms
    table = tuple(tuple(i | j for j in range(n)) for i in range(n))
    return MarkedMonoid(table, tuple(range(n)), f"Boolean_{atoms}_atoms")


def product_value(
    monoid: MarkedMonoid,
    xs: Sequence[int],
    separators: Sequence[int],
) -> int:
    value = xs[0]
    for i, sep in enumerate(separators):
        value = monoid.mul(value, sep)
        value = monoid.mul(value, xs[i + 1])
    return value


def injective_rectangle(
    monoid: MarkedMonoid,
    coordinate_sets: Sequence[Sequence[int]],
    separators: Sequence[int],
) -> bool:
    seen: set[int] = set()
    for xs in itertools.product(*coordinate_sets):
        value = product_value(monoid, xs, separators)
        if value in seen:
            return False
        seen.add(value)
    return True


def rpc(monoid: MarkedMonoid, r: int):
    if r < 1:
        raise ValueError("r must be positive")
    P = monoid.positive
    upper = int(len(P) ** (1.0 / r))
    while (upper + 1) ** r <= len(P):
        upper += 1
    while upper ** r > len(P):
        upper -= 1

    subsets_by_size = {
        m: list(itertools.combinations(P, m)) for m in range(1, upper + 1)
    }

    for m in range(upper, 0, -1):
        subsets = subsets_by_size[m]
        separator_choices: Iterable[tuple[int, ...]]
        if r == 1:
            separator_choices = [()]
        else:
            separator_choices = itertools.product(P, repeat=r - 1)

        # Materialize once because it is reused for every coordinate tuple.
        sep_list = list(separator_choices)
        for coordinate_sets in itertools.product(subsets, repeat=r):
            for separators in sep_list:
                if injective_rectangle(monoid, coordinate_sets, separators):
                    return m, coordinate_sets, separators
    raise RuntimeError("rpc search failed unexpectedly")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--builtin",
        choices=["cyclic", "chain", "boolean"],
        required=True,
        help="small built-in marked monoid",
    )
    parser.add_argument(
        "--size",
        type=int,
        required=True,
        help="order for cyclic/chain; number of atoms for boolean",
    )
    parser.add_argument("--arity", type=int, required=True, help="r in rpc_r")
    args = parser.parse_args()

    if args.builtin == "cyclic":
        monoid = cyclic(args.size)
    elif args.builtin == "chain":
        monoid = chain_semilattice(args.size)
    else:
        monoid = boolean_semilattice(args.size)

    m, coordinate_sets, separators = rpc(monoid, args.arity)
    print(f"{monoid.name}: |P|={len(monoid.positive)}, r={args.arity}")
    print(f"rpc_{args.arity} = {m}")
    print("coordinate sets:")
    for i, A in enumerate(coordinate_sets, start=1):
        print(f"  A_{i} = {A}")
    print(f"separators = {separators}")


if __name__ == "__main__":
    main()
