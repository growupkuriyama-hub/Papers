#!/usr/bin/env python3
"""Exhaustive audit of the cyclic-interval sharpness construction.

This checks the *arbitrary sublanguage* issue in the proof of
Corollary cor:all-q-sharp.  For fixed d,q we build the full rigid codebook

  c_i0 x_1,i1 s_i0,1 ... s_i0,d-1 x_d,id r_i0

over the universal interval frame in (Z/qZ)^(d-1).  For every arity
1 <= e <= d we enumerate every legal e-hole decomposition: holes are
nonempty contiguous intervals, successive holes have a nonempty literal
gap, and the two outer contexts may be empty.

For a tuple x write D_full(x) for its contexts in the full codebook.
If distinct same-type tuples x,y share a context E, then an arbitrary
sublanguage S may contain E[x] and E[y].  Universal substitutability for
*every* S is equivalent, for every further context F, to the two membership
bits for F[x],F[y] being forced equal once E[x],E[y] are forced present.
The finite test below checks exactly this condition.

The script is an audit/counterexample search, not a proof of the theorem.
"""

from __future__ import annotations

import argparse
import itertools
from collections import defaultdict


def interval_vectors(d: int, q: int):
    m = d - 1
    vecs = []
    for k in range(m):
        v = [0] * m
        v[k] = 1
        vecs.append(tuple(v))
    vecs.append((1,) * m)
    b = tuple(1 if ((r + 1) % 2) == (m % 2) else 0 for r in range(m))
    vecs.append(b)
    assert len(vecs) == d + 1
    return vecs


def build_word(d: int, indices: tuple[int, ...]):
    i0 = indices[0]
    word = [("C", i0), ("X1", indices[1])]
    for t in range(1, d):
        word.append((f"S{t}", i0))
        word.append((f"X{t + 1}", indices[t + 1]))
    word.append(("R", i0))
    return tuple(word)


def legal_intervals(n: int, e: int):
    """All ordered e-tuples of nonempty intervals with nonempty inner gaps."""
    out = []

    def rec(min_left: int, k: int, acc):
        if k == e:
            out.append(tuple(acc))
            return
        remaining = e - k - 1
        # After the current interval, reserve one literal gap and one
        # symbol for each remaining hole: 2*remaining positions.
        max_right = n - 2 * remaining
        for left in range(min_left, n):
            for right in range(left + 1, max_right + 1):
                rec(right + 1, k + 1, acc + [(left, right)])

    rec(0, 0, [])
    return out


def add_vec(a, b, q: int):
    return tuple((x + y) % q for x, y in zip(a, b))


def symbol_type(symbol, d: int, q: int, vecs):
    role, value = symbol
    if role in {"C", "R"}:
        v = vecs[0]
    elif role.startswith("S"):
        return (0,) * (d - 1)
    else:
        v = vecs[int(role[1:])]
    return tuple((value * x) % q for x in v)


def substring_type(substring, d: int, q: int, vecs):
    total = (0,) * (d - 1)
    for symbol in substring:
        total = add_vec(total, symbol_type(symbol, d, q, vecs), q)
    return total


def split_occurrence(word, intervals):
    gaps = []
    components = []
    previous = 0
    for left, right in intervals:
        gaps.append(word[previous:left])
        components.append(word[left:right])
        previous = right
    gaps.append(word[previous:])
    return tuple(gaps), tuple(components)


def audit_case(d: int, q: int):
    if d < 2 or q < 2:
        raise ValueError("audit expects d>=2 and q>=2")

    vecs = interval_vectors(d, q)
    codewords = {
        build_word(d, indices): indices
        for indices in itertools.product(range(q), repeat=d + 1)
    }

    report = []
    for e in range(1, d + 1):
        distributions = defaultdict(dict)
        by_type_context = defaultdict(dict)
        occurrence_count = 0

        for word in codewords:
            for intervals in legal_intervals(len(word), e):
                context, tup = split_occurrence(word, intervals)
                typ = tuple(
                    substring_type(component, d, q, vecs)
                    for component in tup
                )
                distributions[tup][context] = word
                by_type_context[(typ, context)][tup] = word
                occurrence_count += 1

        shared_type_contexts = 0
        same_type_pairs = 0
        witness = None

        for (typ, common_context), tuple_to_word in by_type_context.items():
            items = list(tuple_to_word.items())
            if len(items) > 1:
                shared_type_contexts += 1

            for left in range(len(items)):
                x, forced_x = items[left]
                for right in range(left + 1, len(items)):
                    y, forced_y = items[right]
                    same_type_pairs += 1
                    forced = {forced_x, forced_y}

                    for context in set(distributions[x]) | set(distributions[y]):
                        wx = distributions[x].get(context)
                        wy = distributions[y].get(context)

                        # If exactly one filling is a codeword, choose S to
                        # include that codeword as well as the two forced
                        # common-context words.  The two distributions differ.
                        if (wx is None) != (wy is None):
                            witness = (
                                typ, common_context, x, y,
                                forced_x, forced_y, context, wx, wy,
                            )
                            break

                        if wx is None:  # both absent
                            continue

                        # If both are codewords, their membership bits are
                        # equal for every S containing the two forced words
                        # iff they are the same word, or both are already
                        # among the forced common-context words.
                        if wx != wy and not (wx in forced and wy in forced):
                            witness = (
                                typ, common_context, x, y,
                                forced_x, forced_y, context, wx, wy,
                            )
                            break

                    if witness is not None:
                        break
                if witness is not None:
                    break
            if witness is not None:
                break

        report.append(
            {
                "arity": e,
                "codewords": len(codewords),
                "tuple_objects": len(distributions),
                "type_context_cells": len(by_type_context),
                "occurrences": occurrence_count,
                "shared_type_contexts": shared_type_contexts,
                "same_type_pairs_tested": same_type_pairs,
                "pass": witness is None,
                "witness": witness,
            }
        )
        if witness is not None:
            break

    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("d", type=int)
    parser.add_argument("q", type=int)
    args = parser.parse_args()

    rows = audit_case(args.d, args.q)
    print(f"cyclic-interval sharpness audit: d={args.d}, q={args.q}")
    for row in rows:
        print(
            "  e={arity}: codewords={codewords}, tuple_objects={tuple_objects}, "
            "type_context_cells={type_context_cells}, occurrences={occurrences}, "
            "shared_type_contexts={shared_type_contexts}, "
            "same_type_pairs_tested={same_type_pairs_tested}, {status}".format(
                status="PASS" if row["pass"] else "FAIL", **row
            )
        )
        if not row["pass"]:
            print("  witness =", row["witness"])
            raise SystemExit(1)


if __name__ == "__main__":
    main()
