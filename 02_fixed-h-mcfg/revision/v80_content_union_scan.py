#!/usr/bin/env python3
"""v80: Boolean combinations of a cyclic filter under a CONTENT typing.

Setting (exact; commutative, so 2-tuples reduce to sums).
  Sigma = {a, c, d};  markers c, d;  h = content typing
      h(w) = set of markers occurring in w  (a semilattice, not in LG);
  phi: Sigma* -> Z_k, letter values (va, vc, vd);
  L = { w in Sigma^+ : (h(w), phi(w)) in R }   for an arbitrary relation
      R subset of P({c,d}) x Z_k.
A tuple of arity d<=2 is described by its componentwise (content, value);
a context by (content, value) of its fixed material (middle part nonempty).

For every R we decide exactly whether L is (2,h)-tuple-substitutable, and
if so whether L is a TWISTED COMMON-SUBGROUP FILTER:
    there are H <= Z_k and offsets g_S (S a realisable content) such that
    for every realisable content S, R_S (restricted to realisable values)
    is either empty or equal to (g_S + H) restricted to realisable values.
This is the shape of Conjecture F1-tw.  Members of the class that are NOT
of this shape would be candidates for new phenomena; the script prints them.
A finite scan proves nothing in general.

Run:  python3 revision/v80_content_union_scan.py [kmax]
"""
from __future__ import annotations

import itertools
import sys

CONTENTS = [frozenset(), frozenset("c"), frozenset("d"), frozenset("cd")]


def realisable(k, va, vc, vd, maxrep=None):
    maxrep = maxrep or k + 1
    out = set()
    for i in range(maxrep + 1):
        for j in range(maxrep + 1):
            for l in range(maxrep + 1):
                if i + j + l == 0:
                    continue
                S = frozenset(("c" if j else "") + ("d" if l else ""))
                out.add((S, (i * va + j * vc + l * vd) % k))
    return out


def check(k, W, R):
    """exact (2,h)-substitutability; W = realisable (content,value) of
    nonempty words (also = realisable contexts, closed under +)."""
    def acc(S, v):
        return (S, v) in R
    for d in (1, 2):
        sig = {}
        for x in itertools.product(W, repeat=d):
            types = tuple(S for S, _ in x)
            Sx = frozenset().union(*types)
            vx = sum(v for _, v in x) % k
            A = frozenset(c for c in W if acc(c[0] | Sx, (c[1] + vx) % k))
            sig.setdefault(types, set()).add(A)
        for accs in sig.values():
            for A, B in itertools.combinations(accs, 2):
                if A & B:
                    return False
    return True


def twisted_shape(k, W, R):
    by_S = {}
    for S, v in W:
        by_S.setdefault(S, set()).add(v)
    subgroups = {frozenset((dd * i) % k for i in range(k)) for dd in range(k)}
    for H in subgroups:
        ok = True
        for S, vals in by_S.items():
            RS = {v for v in vals if (S, v) in R}
            if not RS:
                continue
            if not any({(g + x) % k for x in H} & vals == RS for g in range(k)):
                ok = False
                break
        if ok:
            return True
    return False


def branchwise_shape(k, W, R):
    """each branch R_S is (g_S + H_S) restricted to realisable values,
    with its OWN subgroup H_S (the shape of Conjecture F1-gen)."""
    by_S = {}
    for S, v in W:
        by_S.setdefault(S, set()).add(v)
    subgroups = {frozenset((dd * i) % k for i in range(k)) for dd in range(k)}
    for S, vals in by_S.items():
        RS = {v for v in vals if (S, v) in R}
        if RS and not any({(g + x) % k for x in H} & vals == RS
                          for H in subgroups for g in range(k)):
            return False
    return True


def main(kmax=3):
    stats = {"tested": 0, "in_class": 0, "twisted": 0, "other": 0,
             "other_branchwise": 0}
    others = []
    for k in range(2, kmax + 1):
        for va, vc, vd in itertools.product(range(k), repeat=3):
            W = realisable(k, va, vc, vd)
            Wl = sorted(W, key=lambda t: (sorted(t[0]), t[1]))
            n = len(Wl)
            for mask in range(1 << n):
                R = {Wl[i] for i in range(n) if mask >> i & 1}
                stats["tested"] += 1
                if not check(k, W, R):
                    continue
                stats["in_class"] += 1
                if twisted_shape(k, W, R):
                    stats["twisted"] += 1
                else:
                    stats["other"] += 1
                    if branchwise_shape(k, W, R):
                        stats["other_branchwise"] += 1
                    others.append((k, (va, vc, vd),
                                   sorted((sorted(S), v) for S, v in R)))
        print(f"k={k}: {stats}", flush=True)
    for o in others[:30]:
        print("  NOT TWISTED-COMMON-H:", o)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
