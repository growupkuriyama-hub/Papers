#!/usr/bin/env python3
"""Run the Case II construction on random and structured configurations.
Usage: hc_check_case2.py CSTAR SEED N
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hc_core import *
from hc_construct import *
from hc_search_case2 import ZMENU, free_factors, supports, psi_menu, PSI_AB

CSTAR = int(sys.argv[1]) if len(sys.argv) > 1 else 3
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 20261114
N = int(sys.argv[3]) if len(sys.argv) > 3 else 500
rng = random.Random(SEED)
stats = Counter()
ZAB = ({"aa": 1}, {"bb": 1})


def run(i_ab, x_ab, phi, x_o, phio, Zo, psi, psio, v0, v1, v2):
    s, e = phi; so, eo = phio
    xa2 = x_ab[:s] + psi + x_ab[e:]
    xo2 = x_o[:so] + psio + x_o[eo:]
    if i_ab == 1:
        W = v0 + xa2 + v1 + xo2 + v2; offA = len(v0); offO = len(v0) + len(xa2) + len(v1)
    else:
        W = v0 + xo2 + v1 + xa2 + v2; offO = len(v0); offA = len(v0) + len(xo2) + len(v1)
    regA = (offA, offA + len(xa2)); regO = (offO, offO + len(xo2))
    TA = state_range(x_ab, ZAB, CSTAR); TO = state_range(x_o, Zo, CSTAR)
    TA = sorted(TA); TO = sorted(TO)
    if len(TA) > 24:
        TA = TA[:8] + TA[-8:] + rng.sample(TA[8:-8], 8)
    if len(TO) > 12:
        TO = TO[:4] + TO[-4:] + rng.sample(TO[4:-4], 4)
    for Ti in TA:
        W1, H, pH, howA = lemma_AB(W, offA, x_ab, s, e, psi, Ti, CSTAR)
        assert W1[:regA[0]] == W[:regA[0]] and W1[regA[1]:] == W[regA[1]:], "AB not confined"
        assert hosts(Ti, (H,)), ("Y_i does not host", x_ab, phi, Ti, H, howA)
        for To in TO:
            W2, H2, pH2, howO = lemma_OT(W1, offO, x_o, so, eo, psio, Zo, To, CSTAR)
            assert W2[:regO[0]] == W1[:regO[0]] and W2[regO[1]:] == W1[regO[1]:], "OT not confined"
            assert hosts(To, (H2,)), ("Y_o does not host", x_o, phio, Zo, To, H2, howO)
            assert dat_ov(W2) == dat_ov(W), ("data changed", W, W2, howA, howO)
            assert W2[pH:pH + len(H)] == H and regA[0] <= pH and pH + len(H) <= regA[1], ("H not literal", howA)
            assert W2[pH2:pH2 + len(H2)] == H2 and regO[0] <= pH2 and pH2 + len(H2) <= regO[1], ("H' not literal", howO)
            holes = sorted([(pH, H, ZAB), (pH2, H2, Zo)])
            assert holes[0][0] + len(holes[0][1]) < holes[1][0], "gap"
            # H*: expand both holes
            Wt = W2
            for (p, h, Z) in reversed(holes):
                Wt = Wt[:p] + expand(h, Z) + Wt[p + len(h):]
            d = zdiff(Wt, W2)
            want = addZ(ZAB, Zo)
            assert d == tuple({k: v for k, v in z.items()} for z in want), ("H* diff", d, want)
            stats["ok"] += 1; stats["AB:" + howA] += 1; stats["OT:" + howO] += 1


def rand_word(L, weights):
    return "".join(rng.choices("abc", weights=weights, k=L))


def structured_ab():
    """adversarial shapes: a-block, long c-run, b-block, phi near the end"""
    m = rng.randint(CSTAR + 1, CSTAR + 3); K = rng.randint(1, 2 * CSTAR + 4)
    X, Y = rng.choice([("a", "b"), ("b", "a")])
    pre = X * m + "c" * K + Y * m
    mid = rng.choice(["", "c", "cc", "c" + X, Y + "c"])
    ph = rng.choice(["aabb", "abab", "aacbb", "bbaa", "aabbc", "caabb"])
    tail = rng.choice(["", "c", "a", "b", "cc", "ca", "cb"])
    return pre + mid + ph + tail


def saturated_ab():
    """prefix Q saturates every window type (all later letters unmarked) and has
    no interval containing both a and b; then a designed part D and phi."""
    c = CSTAR
    if rng.random() < 0.3:
        Q = "a" * (c + 1) + "c" * (c + 1) + "b" * (c + 1) + "c" + "ac" * (c + 1) + "bc" * (c + 1)
    else:   # no adjacent a-/b-intervals: minimal distance >= 2 inside Q
        Q = "a" * (c + 1) + "c" * (c + 1) + "b" * (c + 1) + "cc" + "acc" * (c + 1) + "bcc" * (c + 1)
    parts = []
    for _ in range(rng.randint(1, 4)):
        parts.append(rng.choice(["a" * rng.randint(1, 3), "b" * rng.randint(1, 3), ""]))
    D = "c".join(parts)
    ph = rng.choice(["aabb", "abab", "aacbb", "bbaa", "bbcaa", "acabb", "aabbc", "caabb", "babaa"])
    tail = rng.choice(["", "c", "a", "b", "cc", "ca", "cb", "cab"])
    if rng.random() < 0.4:   # P ends with a one-letter-type interval adjacent to phi
        D = D + "c" + rng.choice(["a", "b"]) * rng.randint(1, 2)
        return Q + D + ph + tail
    return Q + D + rng.choice(["", "c", "cc"]) + ph + tail


done = 0
while done < N:
    u = rng.random()
    if u < 0.5:
        x_ab = saturated_ab()
    elif u < 0.7:
        x_ab = structured_ab()
    else:
        x_ab = rand_word(rng.randint(10, 18), rng.choice([(4, 4, 2), (3, 3, 3), (5, 5, 1), (3, 3, 4)]))
    ph = free_factors(x_ab, CSTAR, lambda f: internal_windows(f)[0]["aa"] and internal_windows(f)[1]["bb"])
    if not ph:
        continue
    ph = [q for q in ph if q[0] >= (len(x_ab) - 14 if len(x_ab) > 30 else 0)] or ph
    Zo = rng.choice(ZMENU)
    if rng.random() < 0.5:
        unit = rng.choice(["abc", "acbc", "aabbc", "bac", "abcc", "acb", "cab"])
        x_o = unit * rng.randint(CSTAR + 2, CSTAR + 4) + rng.choice(["", "a", "b", "c"])
    else:
        x_o = rand_word(rng.randint(8, 16), rng.choice([(1, 1, 3), (2, 2, 3), (3, 1, 2), (1, 3, 2), (2, 2, 1)]))
    pho = free_factors(x_o, CSTAR, lambda f: supports(f, Zo))
    if not pho:
        continue
    done += 1
    run(rng.choice((1, 2)), x_ab, ph[0] if rng.random() < 0.6 else rng.choice(ph), x_o,
        pho[0] if rng.random() < 0.5 else rng.choice(pho), Zo,
        rng.choice(PSI_AB + ["cc", "ccc", "cac", "cbc", "bbcaa", "aacbb", "acb", "bca"]), rng.choice(psi_menu(Zo)),
        rng.choice(["", "a", "b", "c", "ac", "bc", "ca", "aa"]), rng.choice(["a", "b", "c", "cc", "ab"]),
        rng.choice(["", "a", "b", "c", "ca", "cb"]))
print("CSTAR", CSTAR, "SEED", SEED, "configs", done, dict(sorted(stats.items())))
