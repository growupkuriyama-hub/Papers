#!/usr/bin/env python3
"""v79: exhaustive search over small "doubling + shortcut" schemas.

A schema fixes, for every level i>=1, two rules
    X_i -> tau(X_{i-1}, X_{i-1})      (doubling, terminals from {a,b})
    X_i -> sigma(X_{i-1})  or  X_i -> const   (shortcut, contains c)
with a base constant X_0 -> beta over {a,b}, fan-out d in {1,2}
(d=2: start S -> (x^1 t x^2), t in {a,b}).  Every grammar is good and
reduced, has size O(n) and ordinary thickness O(n); the unique c-free word
is the pure doubling yield, of length Theta(2^n).  Typing: h_U with
c |-> zeta (optionally times the (1,1)-window).

The question tested: is any such L_n (2,h)-tuple-substitutable for
n=1,2,3?  Exact finite check (see v79_lib).  Survivors would be
candidates for op:fanout-two and are printed.  This is a FINITE search; a
survivor at n<=3 proves nothing in general, and the absence of survivors
only rules out this schema space.

Run:  python3 revision/v79_schema_search.py [--window] [--d 1|2|both]
"""
from __future__ import annotations

import argparse
import itertools
import sys
from multiprocessing import Pool
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v79_lib import (MCFG, check_substitutable, content_typing,  # noqa: E402
                     product_typing, window_typing)

LET = ["a", "b"]


def insert_letters(items, max_letters, alphabet, require=None):
    """Insert up to max_letters single letters into the gaps of `items`
    (a list of components, each a list of variable tuples)."""
    slots = []
    for ci, comp in enumerate(items):
        for p in range(len(comp) + 1):
            slots.append((ci, p))
    out = set()
    for k in range(0, max_letters + 1):
        for chosen in itertools.combinations_with_replacement(range(len(slots)), k):
            for letters in itertools.product(alphabet, repeat=k):
                if require and require not in letters:
                    continue
                comps = [list(c) for c in items]
                # insert from the back so indices stay valid
                ins = sorted(zip(chosen, letters), key=lambda t: (slots[t[0]][0], -slots[t[0]][1]))
                adds = {}
                for s, l in zip(chosen, letters):
                    adds.setdefault(slots[s], []).append(l)
                newc = []
                for ci, comp in enumerate(comps):
                    nc = []
                    for p in range(len(comp) + 1):
                        if (ci, p) in adds:
                            nc.append("".join(adds[(ci, p)]))
                        if p < len(comp):
                            nc.append(comp[p])
                    newc.append(tuple(nc))
                out.add(tuple(newc))
    return sorted(out, key=str)


def good_template(tpl, nchild, fan_child):
    g = MCFG({"A": len(tpl), **{f"B{j}": fan_child for j in range(nchild)}},
             [("A", [f"B{j}" for j in range(nchild)], tuple(list(c) for c in tpl))], "A")
    return not g.check_good()


def doubling_templates(d):
    vs = [(0, k) for k in range(d)] + [(1, k) for k in range(d)]
    res = set()
    for perm in itertools.permutations(vs):
        # nonpermuting order per child
        if [v for v in perm if v[0] == 0] != [(0, k) for k in range(d)]:
            continue
        if [v for v in perm if v[0] == 1] != [(1, k) for k in range(d)]:
            continue
        if d == 1:
            splits = [[list(perm)]]
        else:
            splits = [[list(perm[:s]), list(perm[s:])] for s in range(1, len(perm))]
        for comps in splits:
            for t in insert_letters(comps, 1, LET):
                if good_template(t, 2, d):
                    res.add(t)
    return sorted(res, key=str)


def shortcut_templates(d):
    res = set()
    comps = [[(0, k)] for k in range(d)]
    for t in insert_letters(comps, 2, ["a", "b", "c"], require="c"):
        if good_template(t, 1, d):
            res.add(("R1", t))
    consts = ["c", "ca", "ac", "cb", "bc", "cc"] if d == 1 else None
    if d == 1:
        for c in consts:
            res.add(("R0", ((c,),)))
    else:
        for c1 in ["c", "a", "b"]:
            for c2 in ["c", "a", "b"]:
                if "c" in c1 + c2:
                    res.add(("R0", ((c1,), (c2,))))
    return sorted(res, key=str)


def bases(d):
    if d == 1:
        return [(("a",),), (("b",),)][:1]
    return [(("a",), ("a",)), (("a",), ("b",))]


def build(d, base, dbl, sc, start_t, n):
    fan = {f"X{i}": d for i in range(n + 1)}
    rules = [("X0", [], tuple(list(c) for c in base))]
    for i in range(1, n + 1):
        p = f"X{i-1}"
        rules.append((f"X{i}", [p, p], tuple(list(c) for c in dbl)))
        kind, t = sc
        if kind == "R1":
            rules.append((f"X{i}", [p], tuple(list(c) for c in t)))
        else:
            rules.append((f"X{i}", [], tuple(list(c) for c in t)))
    if d == 1:
        return MCFG(fan, rules, f"X{n}")
    fan["S"] = 1
    rules.append(("S", [f"X{n}"], ([(0, 0), start_t, (0, 1)],)))
    return MCFG(fan, rules, "S")


H_U = content_typing("c", "hU")
H_WU = product_typing(window_typing(1, 1), H_U)


def test(args):
    d, base, dbl, sc, st, use_window, nmax = args
    h = H_WU if use_window else H_U
    for n in range(1, nmax + 1):
        G = build(d, base, dbl, sc, st, n)
        L = G.language()
        ok, v, _ = check_substitutable(L, h, 2, find_min=False)
        if not ok:
            return (args, n, v)
    return (args, None, None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--window", action="store_true")
    ap.add_argument("--d", default="both")
    ap.add_argument("--nmax", type=int, default=3)
    a = ap.parse_args()
    ds = [1, 2] if a.d == "both" else [int(a.d)]
    jobs = []
    for d in ds:
        for base in bases(d):
            for dbl in doubling_templates(d):
                for sc in shortcut_templates(d):
                    for st in (["a", "b"] if d == 2 else [None]):
                        jobs.append((d, base, dbl, sc, st, a.window, a.nmax))
    print(f"schemas: {len(jobs)}  (window={a.window})", flush=True)
    fail_at = {}
    survivors = []
    with Pool(2) as pool:
        for i, (args, n, v) in enumerate(pool.imap_unordered(test, jobs, chunksize=8)):
            if n is None:
                survivors.append(args)
            else:
                fail_at[n] = fail_at.get(n, 0) + 1
            if (i + 1) % 500 == 0:
                print(f"  {i+1} done; fails by n={fail_at}; survivors={len(survivors)}", flush=True)
    print("failures by first failing n:", dict(sorted(fail_at.items())))
    print("survivors through n =", a.nmax, ":", len(survivors))
    for s in survivors[:50]:
        print("  SURVIVOR", s)


if __name__ == "__main__":
    main()
