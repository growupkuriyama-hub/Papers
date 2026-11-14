#!/usr/bin/env python3
"""Bounded search, Cases I and III (both holes in the same root component).
Case I  : only kappa ({a,b}) deletes; two holes allowed in comp i.
Case III: kappa ({a,b}) and kappa' (Z' from the menu) both in comp i;
          total Z_i split into <= 2 conservation-respecting holes
          (split used in the report: (Z'+aa-part, bb-part) or (Z'+bb-part, aa-part)).
Decision is by exact Gamma feasibility (hc_core.hosts) over candidate holes;
the search does not use the constructive proof.
Usage: hc_search_case13.py CSTAR SEED N
"""
import random, sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hc_core import *
from hc_search_case2 import ZMENU, free_factors, supports, psi_menu, PSI_AB, required

CSTAR = int(sys.argv[1]) if len(sys.argv) > 1 else 3
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 20261114
N = int(sys.argv[3]) if len(sys.argv) > 3 else 300
rng = random.Random(SEED)
stats = Counter(); CEX = []
ZAB = ({"aa": 1}, {"bb": 1})


def addZ(Z1, Z2):
    out = []
    for a, b in zip(Z1, Z2):
        c = Counter(a); c.update(b); out.append(dict(c))
    return tuple(out)


def words(L, lo=1):
    for n in range(lo, L + 1):
        for t in itertools.product("abc", repeat=n):
            yield "".join(t)


def cands(need):
    return [w for w in words(3) if need <= set(w)]


def splits(Zp):
    """hole-part lists for comp i; each part = needed letter set"""
    if Zp is None:
        return [[{"a"}, {"b"}], [{"a", "b"}]]
    rp = required(Zp)
    return [[rp | {"a"}, {"b"}], [rp | {"b"}, {"a"}], [rp | {"a", "b"}]]


def decide(T, GF, parts):
    C = [cands(p) for p in parts]
    for combo in itertools.product(*C):
        for perm in set(itertools.permutations(combo)):
            if hosts(T, perm) and hosts(GF, perm):
                return True
    return False


def rand_word(L, wts):
    return "".join(rng.choices("abc", weights=wts, k=L))


done = 0
while done < N:
    case = rng.choice(("I", "III"))
    Q = "a" * (CSTAR + 1) + "c" * (CSTAR + 1) + "b" * (CSTAR + 1) + "c" + "ac" * (CSTAR + 1) + "bc" * (CSTAR + 1)
    body = rand_word(rng.randint(6, 12), rng.choice([(3, 3, 2), (2, 2, 3), (4, 4, 1)]))
    x = (Q if rng.random() < 0.6 else "") + body
    phs = free_factors(x, CSTAR, lambda f: internal_windows(f)[0]["aa"] and internal_windows(f)[1]["bb"])
    if not phs:
        continue
    s, e = rng.choice(phs)
    Zp = None; pp = None
    if case == "III":
        Zp = rng.choice(ZMENU)
        others = [q for q in free_factors(x, CSTAR, lambda f: supports(f, Zp)) if q[1] <= s or q[0] >= e + 1]
        if not others:
            continue
        pp = rng.choice(others)
    psi = rng.choice(PSI_AB + ["cc", "cac", "cbc"])
    segs = sorted([((s, e), psi)] + ([(pp, rng.choice(psi_menu(Zp)))] if pp else []), reverse=True)
    xw = x
    for (u, v), rep in segs:
        xw = xw[:u] + rep + xw[v:]
    v0 = rng.choice(["", "a", "b", "c"]); v2 = rng.choice(["", "a", "b", "c"])
    other = rand_word(rng.randint(0, 5), (1, 1, 1))
    W = v0 + xw + (("c" + other) if other else "") + v2
    GF = gamma(W)
    Ztot = ZAB if Zp is None else addZ(ZAB, Zp)
    TT = sorted(state_range(x, Ztot, CSTAR))
    if not TT:
        continue
    if len(TT) > 20:
        TT = TT[:6] + TT[-6:] + rng.sample(TT[6:-6], 8)
    done += 1
    for T in TT:
        ok = any(decide(T, GF, parts) for parts in splits(Zp))
        stats[case + (":ok" if ok else ":FAIL")] += 1
        if not ok and len(CEX) < 10:
            CEX.append((case, x, (s, e), Zp, pp, psi, W, T, GF))
print("CSTAR", CSTAR, "SEED", SEED, "configs", done, dict(stats))
for c in CEX:
    print("NO HOLES:", c)
