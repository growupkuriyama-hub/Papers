#!/usr/bin/env python3
"""v80: which type-disjoint unions of cyclic-group filters are in C(2,h_U)?

Setting (exact, finite algebra; no string enumeration needed).
  Sigma = {a, c},  h = h_U (c |-> zeta, a |-> 1),
  phi : Sigma* -> Z_k,  phi(a) = alpha, phi(c) = beta,
  L = { w in Sigma^+ : h(w) = 1 and phi(w) in S1 }
    U { w in Sigma^+ : h(w) = zeta and phi(w) in S2 },   S1, S2 subsets of Z_k.

Membership of E[x] depends only on (OR of types, sum of values), because
the monoid {1,zeta} x Z_k is commutative.  A 2-tuple x is described by
(t1,v1),(t2,v2) realisable by NONEMPTY words; a 2-hole context by
(type, value) realisable by u0 u1 u2 with u1 nonempty.  We test exact
(2,h_U)- and (1,h_U)-tuple substitutability and classify each L as
  * EMPTY-branch / SINGLE filter (S1 = S2 coset of the same subgroup, or one
    branch empty and the other a coset), or
  * NONTRIVIAL union in the class.
Nontrivial members are printed: they are the test cases for Lemma F1.
"""
from __future__ import annotations

import itertools
import sys


def realisable(k, alpha, beta, nonempty=True, maxlen=None):
    """(type, value) pairs of words over {a,c}; type 0 = c-free."""
    maxlen = maxlen or 3 * k + 2
    out = set()
    for i in range(0, maxlen + 1):
        for j in range(0, maxlen + 1):
            if nonempty and i + j == 0:
                continue
            out.add((1 if j else 0, (i * alpha + j * beta) % k))
    return out


def in_L(t, v, S1, S2):
    return v in (S2 if t else S1)


def check(k, alpha, beta, S1, S2):
    W = realisable(k, alpha, beta)              # nonempty words
    C = W                                        # contexts: middle part nonempty
    # (prefix/suffix may be empty; they can only add elements of W or nothing,
    #  and W is closed under addition, so contexts = W)
    for d in (1, 2):
        tuples = list(itertools.product(W, repeat=d))
        sig = {}
        for x in tuples:
            tx = tuple(t for t, _ in x)
            vt = 1 if any(tx) else 0
            vs = sum(v for _, v in x) % k
            acc = frozenset(c for c in C if in_L(c[0] | vt, (c[1] + vs) % k, S1, S2))
            sig[x] = (tx, acc)
        by_type = {}
        for x, (tx, acc) in sig.items():
            by_type.setdefault(tx, []).append(acc)
        for tx, accs in by_type.items():
            for A, B in itertools.combinations(set(accs), 2):
                if A & B and A != B:
                    return False, d
    return True, None


def is_coset(S, k):
    if not S:
        return True
    s0 = next(iter(S))
    H = {(s - s0) % k for s in S}
    return all((x + y) % k in H for x in H for y in H) and \
        all({(s + h) % k for h in H} <= S for s in S)


def main(kmax=6):
    found = []
    stats = {"tested": 0, "in_class": 0, "nontrivial": 0}
    for k in range(2, kmax + 1):
        subsets = [frozenset(s) for r in range(0, k + 1)
                   for s in itertools.combinations(range(k), r)]
        for alpha in range(k):
            for beta in range(k):
                for S1 in subsets:
                    for S2 in subsets:
                        stats["tested"] += 1
                        ok, _ = check(k, alpha, beta, S1, S2)
                        if not ok:
                            continue
                        stats["in_class"] += 1
                        # reduce to what is actually realisable
                        W = realisable(k, alpha, beta)
                        R1 = frozenset(v for (t, v) in W if t == 0 and v in S1)
                        R2 = frozenset(v for (t, v) in W if t == 1 and v in S2)
                        single = (not R1 or not R2) or (R1 == R2)
                        if single and is_coset(R1, k) and is_coset(R2, k):
                            continue
                        stats["nontrivial"] += 1
                        found.append((k, alpha, beta, tuple(sorted(R1)), tuple(sorted(R2))))
    print(stats)
    # classify nontrivial members: is L a semilattice-split union with a
    # COMMON subgroup H (Theorem F1-sl), i.e. are there H <= Z_k and g0,g1
    # with R_b = (g_b + H) intersected with the values realisable in branch b?
    covered = 0
    uncovered = []
    for (k, al, be, R1, R2) in sorted(set(found)):
        W = realisable(k, al, be)
        W0 = {v for (t, v) in W if t == 0}
        W1 = {v for (t, v) in W if t == 1}
        subgroups = {frozenset((d * i) % k for i in range(k)) for d in range(k)}
        ok = False
        for H in subgroups:
            o0 = [g for g in range(k) if {(g + x) % k for x in H} & W0 == set(R1)] \
                if R1 else [None]
            o1 = [g for g in range(k) if {(g + x) % k for x in H} & W1 == set(R2)] \
                if R2 else [None]
            if o0 and o1:
                ok = True
                break
        if ok:
            covered += 1
        else:
            uncovered.append((k, al, be, R1, R2))
    print("nontrivial members covered by F1-sl (common H, branch may be empty):",
          covered, "; not covered:", len(uncovered))
    for e in uncovered[:20]:
        print("  NOT COVERED:", e)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 6)
