#!/usr/bin/env python3
"""Finite sanity checks for the X_{k,r} results.

This script is NOT a proof. It exhaustively enumerates the finite Clark--Wurm
and positive sentence-context factorizations of several small X_{k,r} targets,
and it independently implements the companion CFG constructor R1--R5 under the
trivial observer.

It checks:
  (1) the emptiness observer is Clark--Wurm safe in the tested arities;
  (2) the trivial observer is positive-interface safe in the tested arities;
  (3) the trivial observer fails Clark--Wurm safety at arity two;
  (4) for every K subset of X_{k,r} in the tested cases,
      L(B_triv(K)) = K.
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



def cfg_observed_nonterminals(K):
    """Observed triples [x:u,v] from the CFG constructor."""
    nts = set()
    for w in K:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                nts.add((w[i:j], w[:i], w[j:]))
    return nts


def cfg_trivial_language(K):
    """Exact finite fixed-point language of R1--R5 under the trivial observer."""
    K = set(K)
    if not K:
        return set()

    nts = cfg_observed_nonterminals(K)
    by_factor = defaultdict(list)
    by_context = defaultdict(list)
    for nt in nts:
        x, u, v = nt
        by_factor[x].append(nt)
        by_context[(u, v)].append(nt)

    rules = defaultdict(list)
    for nt in nts:
        x, u, v = nt

        # R1.
        for cut in range(1, len(x)):
            x1, x2 = x[:cut], x[cut:]
            c1 = (x1, u, x2 + v)
            c2 = (x2, u + x1, v)
            if c1 in nts and c2 in nts:
                rules[nt].append(("bin", c1, c2))

        # R2: same factor, observed in another context.
        for child in by_factor[x]:
            rules[nt].append(("unit", child))

        # R3 under the trivial observer: any observed factor in the same context.
        for child in by_context[(u, v)]:
            rules[nt].append(("unit", child))

        # R4.
        if len(x) == 1:
            rules[nt].append(("term", x))

    yields = {nt: set() for nt in nts}
    changed = True
    while changed:
        changed = False
        for nt, nt_rules in rules.items():
            for rule in nt_rules:
                if rule[0] == "term":
                    new = {rule[1]}
                elif rule[0] == "unit":
                    new = yields[rule[1]]
                else:
                    new = {
                        left + right
                        for left in yields[rule[1]]
                        for right in yields[rule[2]]
                    }
                before = len(yields[nt])
                yields[nt].update(new)
                changed |= len(yields[nt]) != before

    out = set()
    for w in K:
        out.update(yields[(w, (), ())])
    return out


def check_cfg_no_generalization(k, r):
    """Exhaust all subsets for the small test cases."""
    words = x_words(k, r)
    n = len(words)
    for mask in range(1 << n):
        K = {words[i] for i in range(n) if (mask >> i) & 1}
        got = cfg_trivial_language(K)
        assert got == K, (
            "CFG trivial-observer generalization mismatch",
            k,
            r,
            mask,
            len(K),
            len(got),
            got - K,
        )
    print(
        f"PASS k={k}, r={r}: all {1 << n} samples satisfy "
        "L(B_triv(K)) = K"
    )


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
        check_cfg_no_generalization(*case)
    print(
        "All finite sanity checks passed. "
        "These checks supplement, but do not replace, the proofs."
    )
