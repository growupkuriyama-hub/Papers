#!/usr/bin/env python3
"""Constructive checker for the round-7 Case II proof (Theorem HC_II).

For a configuration (x_i, phi, psi) of an {a,b}-type component and
(x_o, phi', psi', Z') of the other root component, it runs exactly the
construction of the proof:
  * Lemma AB  (comp i): hole H and a dat-preserving operation on W_{j'}
    confined to the x_i' region;
  * Lemma OT  (comp o): hole H' and a dat-preserving operation confined to
    the x_o' region (all Z' types of the menu, {a,b} type via Lemma AB);
and asserts: dat_ov(W*) = dat_ov(W), the region of the other component is
untouched, H and H' occur literally in their regions in root order with a
nonempty gap, every state T of Lemma P hosts the chosen hole, and the
H*-expansion of the holes changes the data of W* by exactly Z + Z'.
"""
from hc_core import *

SWAP = {"a": "b", "b": "a"}


def interval_bounds(w):
    """list of (start, end) half-open index ranges of the c-separated intervals"""
    out, st = [], 0
    for i, ch in enumerate(w):
        if ch == "c":
            out.append((st, i)); st = i + 1
    out.append((st, len(w)))
    return out


def interval_of(w, pos):
    for k, (s, e) in enumerate(interval_bounds(w)):
        if s <= pos <= e:
            return k, s, e
    raise ValueError


def marked_occurrences(x, X, cstar):
    idx = [i for i, ch in enumerate(x) if ch in X]
    pw = "".join(x[i] for i in idx)
    seen = Counter(); out = []
    for i in range(len(pw) - 1):
        key = pw[i:i + 2]; seen[key] += 1
        if seen[key] <= cstar:
            out.append((key, idx[i], idx[i + 1]))
    return out


# ------------------------------------------------------------------ Lemma AB

def lemma_AB(W, off, x, s, e, psi, T, cstar):
    """comp-i construction.  Returns (W*, H, pos) with pos absolute in W*."""
    P = x[:s]; R = x[e:]
    reg_end = off + len(P) + len(psi) + len(R)
    pb = interval_bounds(P)
    # step 1: a P-interval containing both letters -> literal ab / ba
    for k, (a0, a1) in enumerate(pb):
        seg = P[a0:a1]
        for j in range(len(seg) - 1):
            if {seg[j], seg[j + 1]} == {"a", "b"}:
                return W, seg[j:j + 2], off + a0 + j, "literal-both"
    typ = []
    for (a0, a1) in pb:
        seg = P[a0:a1]
        typ.append("a" if "a" in seg else ("b" if "b" in seg else "E"))
    best = None
    for m1 in range(len(typ)):
        for m2 in range(m1 + 1, len(typ)):
            if typ[m1] != "E" and typ[m2] != "E" and typ[m1] != typ[m2]:
                if best is None or m2 - m1 < best[1] - best[0]:
                    best = (m1, m2)
    assert best is not None, "FO lemma violated: P lacks a or b"
    m1, m2 = best
    X, Y = typ[m1], typ[m2]
    k = m2 - m1
    assert all(typ[m] == "E" for m in range(m1 + 1, m2))
    n0 = x.count("c"); t = P.count("c")
    first_last = (m1 == 0 and m2 == n0)
    nT = T[0]
    kstar = nT if first_last else 1
    # J = W-interval containing P-interval m2
    jpos = off + pb[m2][0]
    Jk, J0, J1 = interval_of(W, jpos)
    regionJ = [p for p in range(J0, J1) if off <= p < reg_end]
    if any(W[p] == X for p in regionJ):
        # reorder region letters of J to create Y X adjacency
        ys = [p for p in regionJ if W[p] == Y]; xs = [p for p in regionJ if W[p] == X]
        assert ys and xs
        letters = [W[p] for p in regionJ]
        rest = [ch for ch in letters]
        rest.remove(Y); rest.remove(X)
        new = [Y, X] + rest
        Wl = list(W)
        for p, ch in zip(regionJ, new):
            Wl[p] = ch
        return "".join(Wl), Y + X, regionJ[0], "reorder-J"
    if k == kstar:
        pos = off + pb[m1][1] - 1
        return W, X + "c" * k + Y, pos, "literal-run"
    # swap: move Y-letters of J into empty P-interval m1+kstar
    assert J1 <= reg_end and J0 >= off, "J must be closed inside the region"
    assert all(W[p] in (Y,) for p in range(J0, J1)), "J must contain only Y letters"
    E0, E1 = pb[m1 + kstar]
    assert E0 == E1, "target interval must be empty"
    nY = J1 - J0
    Wn = W[:off + E0] + Y * nY + W[off + E0:J0] + W[J1:]
    # recompute: removing J letters shifts nothing before E; J letters removed
    assert len(Wn) == len(W)
    pos = off + pb[m1][1] - 1
    return Wn, X + "c" * kstar + Y, pos, "swap-run"


# ------------------------------------------------------------------ Lemma OT

def required(Z):
    A, B = Z
    need = set()
    if A.get("aa", 0) + A.get("ac", 0): need.add("a")
    if B.get("bb", 0) + B.get("bc", 0): need.add("b")
    if A.get("cc", 0) + A.get("ac", 0): need.add("c")
    return need


def lemma_OT(W, off, x, s, e, psi, Z, T, cstar):
    need = required(Z)
    P = x[:s]
    if need == {"a", "b"}:
        return lemma_AB(W, off, x, s, e, psi, T, cstar)
    if len(need) == 1:
        (l,) = need
        p = P.index(l)
        return W, l, off + p, "single"
    if need in ({"a", "c"}, {"b", "c"}):
        l = "a" if "a" in need else "b"
        Xp = l + "c"; other = SWAP[l]
        wA = internal_windows(x[s:e])[0 if l == "a" else 1]
        typ = l + "c" if wA[l + "c"] else "c" + l
        assert wA[typ], "transition window must be internal to phi'"
        occ = [(i, j) for (ty, i, j) in marked_occurrences(x, Xp, cstar) if ty == typ and j < s]
        i, j = occ[0]
        Wl = list(W)
        seg = W[off + i:off + j + 1]
        if typ == l + "c":     # l other^* c -> other^* l c
            new = seg[1:-1] + l + "c"
            Wl[off + i:off + j + 1] = list(new)
            return "".join(Wl), l + "c", off + j - 1, "reorder-" + typ
        else:                  # c other^* l -> c l other^*
            new = "c" + l + seg[1:-1]
            Wl[off + i:off + j + 1] = list(new)
            return "".join(Wl), "c" + l, off + i, "reorder-" + typ
    # need == {a,b,c}: find interval fully inside P with both letters, else swap
    pb = interval_bounds(P)
    inside = list(range(1, len(pb) - 1))
    both = [k for k in inside if "a" in P[pb[k][0]:pb[k][1]] and "b" in P[pb[k][0]:pb[k][1]]]
    Wl = list(W)
    if both:
        k = both[0]
    else:
        ka = [k for k in inside if "a" in P[pb[k][0]:pb[k][1]]]
        kb = [k for k in inside if "b" in P[pb[k][0]:pb[k][1]]]
        assert ka and kb, "fully-inside a- and b-intervals needed"
        k, kk = ka[0], kb[0]
        sa, ea = pb[k]; sb, eb = pb[kk]
        # beta swap: interval k gets the b's of kk; kk keeps nothing (alpha=0)
        nb = eb - sb
        segk = P[sa:ea] + "b" * nb
        segkk = ""
        newP = []
        for q, (u0, u1) in enumerate(pb):
            if q == k: newP.append(segk)
            elif q == kk: newP.append(segkk)
            else: newP.append(P[u0:u1])
        P2 = "c".join(newP)
        Wl[off:off + len(P)] = list(P2)
        W2 = "".join(Wl)
        pb = interval_bounds(P2); P = P2; Wl = list(W2)
    s0, e0 = pb[k]
    seg = P[s0:e0]
    rest = list(seg); rest.remove("a"); rest.remove("b")
    new = "ab" + "".join(rest)
    Wl[off + s0:off + e0] = list(new)
    return "".join(Wl), "cab", off + s0 - 1, "both-inside"


# ------------------------------------------------------------------ expand (H*)

def expand(h, Z):
    A, B = Z
    p = A.get("aa", 0); pp = B.get("bb", 0)
    r = A.get("ac", 0); rp = B.get("bc", 0)
    m = A.get("cc", 0) + r
    assert m == B.get("cc", 0) + rp
    out = []; da = db = dc = False
    for ch in h:
        if ch == "a" and not da:
            out.append("a" * (1 + p)); da = True
        elif ch == "b" and not db:
            out.append("b" * (1 + pp)); db = True
        elif ch == "c" and not dc:
            out.append("c" + "".join(("a" if j < r else "") + ("b" if j < rp else "") + "c" for j in range(m))); dc = True
        else:
            out.append(ch)
    return "".join(out)


def zdiff(w1, w0):
    d = []
    for X in ("ac", "bc"):
        n1, n0 = windows(proj(w1, X)), windows(proj(w0, X))
        d.append({k: n1[k] - n0[k] for k in set(n1) | set(n0) if n1[k] != n0[k]})
    return tuple(d)


def addZ(Z1, Z2):
    out = []
    for a, b in zip(Z1, Z2):
        c = Counter(a); c.update(b); out.append({k: v for k, v in c.items() if v})
    return tuple(out)
