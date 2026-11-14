#!/usr/bin/env python3
"""Core exact deciders for round-7 hostability (HC), l=2, A={a,c}, B={b,c}.

Everything is decided on the Gamma statistic of Lemma G (round six):
  Gamma(w) = (n, |w|_a, |w|_b, nu_A, nu_B, a0, an, b0, bn)
where w = w_0 c w_1 ... c w_n, alpha_k = |w_k|_a, beta_k = |w_k|_b,
nu_A = #{0<k<n : alpha_k>0}, a0 = [alpha_0>0], an = [alpha_n>0] (similarly B).
For n = 0 the tuple is (0, |w|_a, |w|_b).  Standard library only.
"""
from collections import Counter
from functools import lru_cache
import itertools

SIGMA = "abc"


def proj(w, X):
    return "".join(ch for ch in w if ch in X)


def windows(u):
    return Counter(u[i:i + 2] for i in range(len(u) - 1))


def shat(u):
    """completion of s_{1,1}: short words recorded exactly"""
    return ("short", u) if len(u) < 2 else ("long", u[0], u[-1])


def dat_ov(w):
    pa, pb = proj(w, "ac"), proj(w, "bc")
    return (shat(pa), frozenset(windows(pa).items()),
            shat(pb), frozenset(windows(pb).items()))


def intervals(w):
    gaps = w.split("c")
    return [g.count("a") for g in gaps], [g.count("b") for g in gaps]


def gamma(w):
    al, be = intervals(w)
    n = len(al) - 1
    if n == 0:
        return (0, al[0], be[0])
    return (n, sum(al), sum(be),
            sum(1 for k in range(1, n) if al[k]), sum(1 for k in range(1, n) if be[k]),
            al[0] > 0, al[n] > 0, be[0] > 0, be[n] > 0)


# ---------------------------------------------------------------- feasibility

def feasible_side(n, tot, nu, e0, en, cons):
    """Is there alpha_0..alpha_n >= 0 with sum tot, #{0<k<n: alpha_k>0} = nu,
    [alpha_0>0]=e0, [alpha_n>0]=en, satisfying cons: pos -> ('ex', v) | ('al', v)?"""
    if n == 0:
        c = cons.get(0)
        if c is None:
            return True
        return tot == c[1] if c[0] == "ex" else tot >= c[1]
    forced_nz = forced_z = free = 0
    min_total = 0
    flexible = False
    for p in range(n + 1):
        c = cons.get(p)
        if p in (0, n):
            e = e0 if p == 0 else en
            if c is None:
                if e:
                    min_total += 1; flexible = True
                continue
            kind, v = c
            if kind == "ex":
                if (v > 0) != e:
                    return False
                min_total += v
            else:
                if v > 0 and not e:
                    return False
                if e:
                    min_total += max(v, 1); flexible = True
            continue
        if c is None:
            free += 1
            continue
        kind, v = c
        if kind == "ex":
            if v > 0:
                forced_nz += 1; min_total += v
            else:
                forced_z += 1
        else:
            if v > 0:
                forced_nz += 1; min_total += v; flexible = True
            else:
                free += 1
    extra = nu - forced_nz
    if extra < 0 or extra > free:
        return False
    min_total += extra
    if extra > 0:
        flexible = True
    if tot < min_total:
        return False
    if tot > min_total and not flexible:
        return False
    return True


def split_hole(h):
    parts = h.split("c")
    return [(p.count("a"), p.count("b")) for p in parts]


def _place_constraints(n, holes, starts):
    """Return list of (consA, consB) alternatives (separator branching), or []"""
    consA, consB = {}, {}
    shared = []
    for idx, (h, s) in enumerate(zip(holes, starts)):
        parts = split_hole(h)
        k = len(parts) - 1
        if s + k > n:
            return []
        for m, (ca, cb) in enumerate(parts):
            p = s + m
            kind = "ex" if 0 < m < k else "al"
            for cons, v in ((consA, ca), (consB, cb)):
                if p in cons:
                    ok, ov = cons[p]
                    if ok == "ex" or kind == "ex":
                        return []
                    cons[p] = ("al", ov + v)
                else:
                    cons[p] = (kind, v)
            if m == 0 and idx > 0 and p == prev_end:
                shared.append(p)
        prev_end = s + k
    alts = [(consA, consB)]
    for p in shared:
        new = []
        for cA, cB in alts:
            a2 = dict(cA); a2[p] = ("al", a2[p][1] + 1)
            b2 = dict(cB); b2[p] = ("al", b2[p][1] + 1)
            new.append((a2, cB)); new.append((cA, b2))
        alts = new
    return alts


@lru_cache(maxsize=None)
def hosts(G, holes):
    """G: Gamma tuple; holes: tuple of words (in order, pairwise separated by a
    nonempty word).  Decides whether some word with Gamma G contains them."""
    if G[0] == 0:
        n, ta, tb = G
        if any("c" in h for h in holes):
            return False
        na = sum(h.count("a") for h in holes); nb = sum(h.count("b") for h in holes)
        need = na + nb + (len(holes) - 1)
        if ta < na or tb < nb or ta + tb < need:
            return False
        return True
    n, ta, tb, nuA, nuB, a0, an, b0, bn = G
    ks = [h.count("c") for h in holes]
    def rec(i, lo, starts):
        if i == len(holes):
            for cA, cB in _place_constraints(n, holes, starts):
                if feasible_side(n, ta, nuA, a0, an, cA) and feasible_side(n, tb, nuB, b0, bn, cB):
                    return True
            return False
        for s in range(lo, n + 1 - ks[i]):
            if rec(i + 1, s + ks[i], starts + (s,)):
                return True
        return False
    return rec(0, 0, ())


def literal_hosts(w, holes):
    """brute check: holes occur in w in order, disjoint, nonempty gaps"""
    def rec(i, pos):
        if i == len(holes):
            return True
        h = holes[i]
        start = pos if i == 0 else pos + 1
        j = w.find(h, start)
        while j != -1:
            if rec(i + 1, j + len(h)):
                return True
            j = w.find(h, j + 1)
        return False
    return rec(0, 0)


# ---------------------------------------------------------------- states

def proj_stats(u, letter):
    """for a projection u over {letter, c}: (first, last, Counter windows)"""
    return u[0], u[-1], windows(u)


def state_range(x, Z, cstar):
    """Permissive set of Gamma tuples of possible states T of a root component
    whose original word is x, after deleting this stage's Z=(ZA,ZB) and any
    earlier deletions of unmarked occurrences (Lemma P):
      min(N0(w), cstar) <= N_T(w) <= N0(w) - Z(w),  shat, content fixed."""
    res = set()
    per = []
    for X, l in (("ac", "a"), ("bc", "b")):
        u = proj(x, X)
        ZX = Z[0] if l == "a" else Z[1]
        if len(u) < 2:          # short projection: recorded exactly by shat
            assert not ZX
            nn = u.count("c")
            per.append([(nn, u.count(l), 0, u == l, u == l)])
            continue
        f, la, N0 = u[0], u[-1], windows(u)
        rng = {}
        for w in (l + l, l + "c", "c" + l, "cc"):
            lo = min(N0[w], cstar); hi = N0[w] - ZX.get(w, 0)
            if hi < lo:
                return set()
            rng[w] = (lo, hi)
        opts = []
        if "c" not in u:
            for ll in range(rng[l + l][0], rng[l + l][1] + 1):
                opts.append((0, ll + 1, 0, False, False))
        else:
            for lc in range(rng[l + "c"][0], rng[l + "c"][1] + 1):
                cl = lc + (f == "c") - (la == "c")
                if not (rng["c" + l][0] <= cl <= rng["c" + l][1]):
                    continue
                for cc in range(rng["cc"][0], rng["cc"][1] + 1):
                    n = lc + cc + (f == "c")
                    for ll in range(rng[l + l][0], rng[l + l][1] + 1):
                        tot = ll + cl + (f == l)
                        nu = cl - (la == l)
                        if nu < 0 or nu > n - 1:
                            continue
                        opts.append((n, tot, nu, f == l, la == l))
        per.append(opts)
    for (nA, ta, nuA, a0, an) in per[0]:
        for (nB, tb, nuB, b0, bn) in per[1]:
            if nA != nB:
                continue
            if nA == 0:
                res.add((0, ta, tb))
            else:
                res.add((nA, ta, tb, nuA, nuB, a0, an, b0, bn))
    return res


def marks(x, cstar):
    m = set()
    for X in ("ac", "bc"):
        idx = [i for i, ch in enumerate(x) if ch in X]
        pw = "".join(x[i] for i in idx)
        seen = Counter()
        for i in range(len(pw) - 1):
            key = pw[i:i + 2]; seen[key] += 1
            if seen[key] <= cstar:
                m.update((idx[i], idx[i + 1]))
    return m


def internal_windows(phi):
    return windows(proj(phi, "ac")), windows(proj(phi, "bc"))
