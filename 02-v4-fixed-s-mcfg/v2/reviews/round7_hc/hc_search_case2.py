#!/usr/bin/env python3
"""Bounded search for simultaneous hostability, Case II (round 7).

kappa  : {a,b}-type component, Z = (aa, bb), lives in root component i.
kappa' : other eta component, in the OTHER root component, Z' from a menu of
         all minimal nonzero circulation pairs obeying the c-conservation law.
Model (permissive superset of what real derivations produce):
  x_i, x_o : original root components; marks = first cstar occurrences.
  phi, phi': mark-free factors (phi has internal aa in pi_A and bb in pi_B,
             phi' carries the windows of Z').
  psi, psi': replacements in W_{j'} with |pi_X psi| >= 2 whenever Z_X != 0
             (forced by equal shat-colours, since psi^{(j)} carries Z).
  W_{j'}   = v0 x_1' v1 x_2' v2  (v1 nonempty).
  Y states : every Gamma allowed by Lemma P (state_range).
Decision : exists (h, h') with  T_i hosts h,  T_o hosts h',
           Gamma(W_{j'}) hosts (h_first, h_second) in root order.
Usage: hc_search_case2.py MODE CSTAR SEED N
"""
import itertools, random, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from hc_core import *

MODE = sys.argv[1] if len(sys.argv) > 1 and __name__ == "__main__" else "random"
CSTAR = int(sys.argv[2]) if len(sys.argv) > 2 else 2
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 20261114
NITER = int(sys.argv[4]) if len(sys.argv) > 4 else 2000
rng = random.Random(SEED)

ZMENU = []
for p in (0, 1):
    for pp in (0, 1):
        if p or pp:
            ZMENU.append(({"aa": 1} if p else {}, {"bb": 1} if pp else {}))
for Ap in ({"cc": 1}, {"ac": 1, "ca": 1}):
    for Bp in ({"cc": 1}, {"bc": 1, "cb": 1}):
        for p in (0, 1):
            for pp in (0, 1):
                A = dict(Ap); B = dict(Bp)
                if p: A["aa"] = 1
                if pp: B["bb"] = 1
                ZMENU.append((A, B))


def required(Z):
    A, B = Z
    need = set()
    if A.get("aa", 0) + A.get("ac", 0): need.add("a")
    if B.get("bb", 0) + B.get("bc", 0): need.add("b")
    if A.get("cc", 0) + A.get("ac", 0): need.add("c")
    return need


def supports(phi, Z):
    wa, wb = internal_windows(phi)
    return all(wa[k] >= v for k, v in Z[0].items()) and all(wb[k] >= v for k, v in Z[1].items())


def free_factors(x, cstar, pred):
    mk = marks(x, cstar)
    out = []
    for s in range(len(x)):
        for e in range(s + 2, len(x) + 1):
            if any(i in mk for i in range(s, e)):
                break
            if pred(x[s:e]):
                out.append((s, e))
    return out


def words_upto(L, lo=1):
    for n in range(lo, L + 1):
        for t in itertools.product("abc", repeat=n):
            yield "".join(t)


PSI_AB = [w for w in words_upto(3, 2) if len(proj(w, "ac")) >= 2 and len(proj(w, "bc")) >= 2]


def psi_menu(Z):
    out = []
    for w in words_upto(3, 1):
        if Z[0] and len(proj(w, "ac")) < 2: continue
        if Z[1] and len(proj(w, "bc")) < 2: continue
        out.append(w)
    return out


def cand_ab(nmax):
    c = [w for w in words_upto(4, 2) if "a" in w and "b" in w]
    for k in range(4, nmax + 2):
        c += ["a" + "c" * k + "b", "b" + "c" * k + "a"]
    return c


def cand_req(need, nmax):
    c = [w for w in words_upto(3, 1) if need <= set(w)]
    for k in range(3, nmax + 2):
        if "c" in need:
            c += ["c" * k]
    return c


def yset(T, cands):
    return frozenset(h for h in cands if hosts(T, (h,)))


stats = Counter()
CEX = []


def check(i_ab, x_ab, phi, x_o, phio, Zo, psi, psio, v0, v1, v2):
    s, e = phi; so, eo = phio
    xa2 = x_ab[:s] + psi + x_ab[e:]
    xo2 = x_o[:so] + psio + x_o[eo:]
    W = v0 + (xa2 + v1 + xo2 if i_ab == 1 else xo2 + v1 + xa2) + v2
    GF = gamma(W)
    nmax = max(x_ab.count("c"), x_o.count("c"), W.count("c")) + 1
    CA = cand_ab(nmax); CO = cand_req(required(Zo), nmax)
    TA = state_range(x_ab, ({"aa": 1}, {"bb": 1}), CSTAR)
    TO = state_range(x_o, Zo, CSTAR)
    if not TA or not TO:
        stats["empty-state-range"] += 1
        return
    SA = {yset(T, CA) for T in TA}; SO = {yset(T, CO) for T in TO}
    for ya in SA:
        if not ya:
            CEX.append(("Y-ab empty", x_ab, phi)); return
        for yo in SO:
            if not yo:
                CEX.append(("Y-o empty", x_o, phio, Zo)); return
            ok = False
            for h in ya:
                for ho in yo:
                    pair = (h, ho) if i_ab == 1 else (ho, h)
                    if hosts(GF, pair):
                        ok = True; break
                if ok: break
            stats["tested"] += 1
            if not ok:
                stats["FAIL"] += 1
                if len(CEX) < 20:
                    CEX.append(("NO COMMON PAIR", i_ab, x_ab, phi, x_o, phio, Zo, psi, psio,
                                v0, v1, v2, W, GF, sorted(ya)[:8], sorted(yo)[:8]))


def rand_word(L, weights):
    return "".join(rng.choices("abc", weights=weights, k=L))


def random_mode():
    it = 0
    while it < NITER:
        L = rng.randint(8, 15)
        x_ab = rand_word(L, rng.choice([(4, 4, 2), (3, 3, 3), (5, 5, 1), (3, 3, 4)]))
        ph = free_factors(x_ab, CSTAR, lambda f: internal_windows(f)[0]["aa"] and internal_windows(f)[1]["bb"])
        if not ph:
            continue
        Zo = rng.choice(ZMENU)
        x_o = rand_word(rng.randint(5, 11), rng.choice([(1, 1, 3), (2, 2, 3), (3, 1, 2), (1, 3, 2)]))
        pho = free_factors(x_o, CSTAR, lambda f: supports(f, Zo))
        if not pho:
            continue
        it += 1
        check(rng.choice((1, 2)), x_ab, rng.choice(ph), x_o, rng.choice(pho), Zo,
              rng.choice(PSI_AB), rng.choice(psi_menu(Zo)),
              rng.choice(["", "a", "b", "c", "ac", "bc", "ca"]), rng.choice(["a", "b", "c", "cc", "ab"]),
              rng.choice(["", "a", "b", "c", "ca", "cb"]))


def exhaustive_mode(LAB):
    # all x_ab up to length LAB; x_o from a fixed menu; all psi, all short contexts
    XO = [("ccccc", ({"cc": 1}, {"cc": 1})), ("acacacac", ({"ac": 1, "ca": 1}, {"cc": 1})),
          ("bcbcbcbc", ({"cc": 1}, {"bc": 1, "cb": 1})), ("aaaaa", ({"aa": 1}, {})),
          ("abcabcabcab", ({"ac": 1, "ca": 1}, {"bc": 1, "cb": 1}))]
    CTX = ["", "a", "b", "c"]
    for x_ab in words_upto(LAB, 8):
        ph = free_factors(x_ab, CSTAR, lambda f: internal_windows(f)[0]["aa"] and internal_windows(f)[1]["bb"])
        for phi in ph:
            for x_o, Zo in XO:
                pho = free_factors(x_o, CSTAR, lambda f: supports(f, Zo))
                if not pho:
                    continue
                phio = pho[-1]
                for i_ab in (1, 2):
                    for psi in PSI_AB:
                        for psio in psi_menu(Zo)[:6]:
                            for v0 in CTX:
                                for v2 in CTX:
                                    check(i_ab, x_ab, phi, x_o, phio, Zo, psi, psio, v0, "c" if v0 == "" else "a", v2)
        if x_ab.endswith("c" * len(x_ab)):
            pass


if __name__ == "__main__":
    if MODE == "random":
        random_mode()
    else:
        exhaustive_mode(int(MODE))
    print("MODE", MODE, "CSTAR", CSTAR, "SEED", SEED, dict(stats))
    for c in CEX[:20]:
        print(c)
