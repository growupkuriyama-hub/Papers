#!/usr/bin/env python3
"""Finite sanity checks for Section 5 of Minimal Observation Is Not Enough.

This script is NOT a proof. It exhaustively enumerates the finite Clark--Wurm
and positive sentence-context factorizations of several small X_{k,r} targets.
It checks:
  (1) the emptiness observer is Clark--Wurm safe in the tested arities;
  (2) the trivial observer is positive-interface safe in the tested arities;
  (3) the trivial observer fails Clark--Wurm safety at arity two.
"""
from collections import defaultdict
from itertools import product


def weak_compositions(n, p):
    if p == 1:
        yield (n,)
        return
    for first in range(n + 1):
        for rest in weak_compositions(n - first, p - 1):
            yield (first,) + rest


def x_words(k, r):
    ans = []
    for inds in product(range(k), repeat=r):
        w = tuple(
            [f"a{j}_{i}" for j, i in enumerate(inds, 1)]
            + [f"b{j}_{i}" for j, i in enumerate(inds, 1)]
        )
        ans.append(w)
    return ans


def segments(w, lengths):
    out, pos = [], 0
    for ell in lengths:
        out.append(w[pos:pos + ell])
        pos += ell
    assert pos == len(w)
    return tuple(out)


def distributions(k, r, d, positive=False):
    tuple_to_contexts = defaultdict(set)
    context_to_tuples = defaultdict(set)
    for w in x_words(k, r):
        for lens in weak_compositions(len(w), 2 * d + 1):
            if positive:
                # Holes are nonempty; internal fixed separators are nonempty.
                if any(lens[i] == 0 for i in range(1, 2 * d, 2)):
                    continue
                if any(lens[i] == 0 for i in range(2, 2 * d, 2)):
                    continue
            seg = segments(w, lens)
            context = tuple(seg[0::2])
            tup = tuple(seg[1::2])
            context_to_tuples[context].add(tup)
            tuple_to_contexts[tup].add(context)
    return tuple_to_contexts, context_to_tuples


def emptiness_type(tup):
    return tuple(bool(x) for x in tup)


def check_safety(k, r, d, positive=False, typed=True):
    t2c, c2t = distributions(k, r, d, positive=positive)
    for context, tuples in c2t.items():
        buckets = defaultdict(list)
        for tup in tuples:
            key = emptiness_type(tup) if typed else None
            buckets[key].append(tup)
        for bucket in buckets.values():
            if len(bucket) < 2:
                continue
            base = t2c[bucket[0]]
            for tup in bucket[1:]:
                if t2c[tup] != base:
                    return False, (context, bucket[0], tup)
    return True, None


def run_case(k, r):
    # Empty components can make CW arity exceed the word length, so test a few
    # arities beyond 2r as well.
    for d in range(1, 2 * r + 4):
        ok, witness = check_safety(k, r, d, positive=False, typed=True)
        assert ok, ("emptiness observer CW failure", k, r, d, witness)

    # Testing beyond feasible positive arity also checks vacuous safety.
    for d in range(1, 2 * r + 2):
        ok, witness = check_safety(k, r, d, positive=True, typed=False)
        assert ok, ("trivial positive-interface failure", k, r, d, witness)

    ok, witness = check_safety(k, r, 2, positive=False, typed=False)
    assert not ok, ("trivial observer unexpectedly CW-safe at arity two", k, r)

    print(
        f"PASS k={k}, r={r}: CW emptiness safety; "
        "positive trivial safety; CW arity-2 lower bound"
    )


if __name__ == "__main__":
    for case in [(2, 2), (2, 3), (3, 2)]:
        run_case(*case)
    print(
        "All finite sanity checks passed. "
        "These checks supplement, but do not replace, the proof."
    )
