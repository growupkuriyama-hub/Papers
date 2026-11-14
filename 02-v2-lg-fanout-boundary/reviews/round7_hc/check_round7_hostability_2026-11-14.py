#!/usr/bin/env python3
"""Round-7 hostability (HC) checks, l=2, A={a,c}, B={b,c}, f=2.  Fixed seeds,
standard library only.  Needs hc_core.py, hc_construct.py, hc_search_case2.py,
hc_check_case2.py, hc_search_case13.py in the same directory.

[1] exact Gamma decider `hosts` versus brute force over all words (Lemma G + decider)
[2] Lemma FL: the (first,last)-rigid configuration never occurs with a mark-free phi
[3] Case II constructive proof (Lemmas AB, OT) on random/structured/saturated configs
[4] Case II existence search (exact, does not use the proof)
[5] Cases I and III existence search
Finite checks are not proofs.  Every assert separates true from false.
"""
import itertools, subprocess, sys, os, time
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from hc_core import *
from hc_construct import interval_bounds

t0 = time.time()
print("== [1] decider vs brute force (all words of length <= 7)")
groups = defaultdict(list)
for n in range(1, 8):
    for t in itertools.product("abc", repeat=n):
        w = "".join(t); groups[gamma(w)].append(w)
for G, ws in groups.items():
    assert len({dat_ov(w) for w in ws}) == 1, "Lemma G"
HS = ["".join(t) for k in (1, 2, 3) for t in itertools.product("abc", repeat=k)]
HL = [(h,) for h in HS] + [(h1, h2) for h1 in HS for h2 in HS if len(h1) + len(h2) <= 4]
tests = 0
for G, ws in groups.items():
    for H in HL:
        tests += 1
        assert any(literal_hosts(w, H) for w in ws) == hosts(G, H), (G, H)
print("   classes", len(groups), "tests", tests, "mismatches 0")

print("== [2] Lemma FL: no (first,last) minimal pair in P, all x of length <= 12, cstar=2")
CS = 2; nx = nphi = nrigid = 0
for L in range(8, 13):
    for t in itertools.product("abc", repeat=L):
        x = "".join(t)
        if x.count("a") < CS + 2 or x.count("b") < CS + 2:
            continue
        mk = marks(x, CS); nx += 1
        for s in range(L):
            if s in mk:
                continue
            for e in range(s + 2, L + 1):
                if (e - 1) in mk:
                    break
                f = x[s:e]
                wa, wb = internal_windows(f)
                if not (wa["aa"] and wb["bb"]):
                    continue
                nphi += 1
                P = x[:s]; pb = interval_bounds(P)
                typ = ["ab" if ("a" in P[u:v] and "b" in P[u:v]) else ("a" if "a" in P[u:v] else ("b" if "b" in P[u:v] else "E")) for u, v in pb]
                if "ab" in typ:
                    continue
                best = None
                for m1 in range(len(typ)):
                    for m2 in range(m1 + 1, len(typ)):
                        if "E" not in (typ[m1], typ[m2]) and typ[m1] != typ[m2]:
                            if best is None or m2 - m1 < best[1] - best[0]:
                                best = (m1, m2)
                assert best is not None, ("FO lemma", x, s, e)
                if best[0] == 0 and best[1] == x.count("c"):
                    nrigid += 1
                    print("   RIGID", x, s, e)
assert nrigid == 0
print("   words", nx, "mark-free phi", nphi, "rigid 0")

def run(args):
    out = subprocess.run([sys.executable, "-I"] + args, cwd=HERE, capture_output=True, text=True, timeout=1500)
    assert out.returncode == 0, out.stderr[-2000:]
    return out.stdout.strip().splitlines()

print("== [3] Case II construction")
for cs, seed, n in ((3, 3, 300), (3, 5, 300), (4, 11, 200), (5, 12, 150)):
    line = run(["hc_check_case2.py", str(cs), str(seed), str(n)])[-1]
    print("  ", line)
    assert "'ok'" in line
print("== [4] Case II existence search")
for cs, seed, n in ((2, 11, 800), (3, 21, 800)):
    lines = run(["hc_search_case2.py", "random", str(cs), str(seed), str(n)])
    print("  ", lines[0])
    assert "FAIL" not in lines[0] and len(lines) == 1
print("== [5] Cases I/III existence search")
for cs, seed, n in ((3, 7, 400), (3, 8, 400), (4, 9, 300)):
    lines = run(["hc_search_case13.py", str(cs), str(seed), str(n)])
    print("  ", lines[0])
    assert "FAIL" not in lines[0]
print("ALL CHECKS PASSED  (%.0f s)" % (time.time() - t0))
