# Round-eight HC_III: exact plaintext Python and log archive (2026-11-14)

> Research archive only; the model output and verification source are not proofs of the general P1/B6/DFS claims.

All embedded file bodies below preserve the original UTF-8 content including trailing newline. Copy them out using the extraction script or use the uploaded original ZIP for Claude files.

## Extraction

Save this Markdown as `ROUND8_SOURCE_BUNDLE_2026-11-14.md` and run:

```bash
python - <<'PYEXTRACT'
from pathlib import Path
import re
doc=Path('ROUND8_SOURCE_BUNDLE_2026-11-14.md').read_text(encoding='utf-8')
for name, body in re.findall(r'### `([^`]+)`\n\n```(?:python|text)\n(.*?)\n```', doc, flags=re.S):
    Path(name).write_text(body+'\n',encoding='utf-8')
    print(name)
PYEXTRACT
```

## SHA-256 manifest

| File | SHA-256 |
|---|---|
| `check_round8_HCIII_2026-11-14.py` | `4d265cfc8d1f81adf63a7ec71245f1ee5b209f91c51d1ddd38c433a0b5f1d8b1` |
| `hc3_construct.py` | `f5e669b4a1ecebe7464a2568f0de3053183dfc0c9280810816f1ac4ea3c13353` |
| `hc3_search.py` | `fa6eda1fb98c857ede667e0cd977b740a1c9befb137118ee5c2daf4f3da15e79` |
| `hc_core.py` | `d4664b740b76b29633b076c78a7d129d0a173889f5e27aac7c996c58b305093b` |
| `hc_construct.py` | `470904c7c205d2bbca377889e55f9080f1ee99ba3ee6dbbcbcc4e319d0ed210f` |
| `hc_search_case2.py` | `f2e7e80d312f39a9e60c4ac3664143bbec04583e20b304e22e415303ff8e1507` |
| `out_check_round8_HCIII_2026-11-14.txt` | `a11f075c24720330d2465bff7df508efbd7560b41cb9659ddcc1b6b771f599e2` |
| `out_hc3_search_2026-11-14.txt` | `5df38566b277aef37cfd33d491a98e8f6dc365a775dc704d1a109803f0388b7d` |
| `audit_round8_hcIII_independent_2026-11-14.py` | `9de77bb50a7cbb329e3147058c90844a72d54fc2fd3e025d597e0c638f9d562d` |
| `out_audit_round8_hcIII_independent_2026-11-14.txt` | `7df63d256225a2fe407f1257dd9c251d327afd31469c20f3dc3386bc34a32fcb` |

## Sources

### `check_round8_HCIII_2026-11-14.py`

```python
#!/usr/bin/env python3
"""Round 8 checker for HC_III (Case III: both deleting eta-components in the
same root component), A={a,c}, B={b,c}, l=2, f=2, s=c_Sigma.

Sections
 [1] realize() vs hosts(): exhaustive over all Gamma of words of length <= L1 (default 7) and
     all ordered 1-2 hole tuples of total length <= 4; every witness is checked
     (Gamma equal, holes literal, in order, gaps >= 1).
 [2] Case III construction of Theorems III-A/III-B, random + adversarial
     configurations, ALL Lemma-P states (no subsampling unless > 64).
     Asserted per (configuration, state):
       - the intermediate facts of the proof (in hc3_construct.hc3_holes);
       - holes nonempty, <= 2, each part conserving, sum of parts = Z+Z';
         c_Sigma(h) = c_Sigma(t), t = expand(h, part)   (Lemma H*);
       - Y: explicit y' with Gamma(y') = T hosting the holes in order with gaps,
            y^pi = y'[h->t] has N_2 difference = Z+Z' and the same shat;
       - F: explicit W* with dat_ov(W*) = dat_ov(W_{j'}) hosting the same holes
            in the same order with gaps (III-A: W* = W literally);
            F[t] has N_2 difference = Z+Z' from W*, same shat;
       - rich branch: T hosts every word of S6.
 [3] coverage of the proof's branches (each must be hit), and an independent
     existence cross-check with hc3_search's decision on every state.
Any failure prints the full configuration and stops.  Standard library only;
fixed seeds.  Usage: check_round8_HCIII_2026-11-14.py [N_RANDOM] [N_ADV] [L1]
"""
import sys, os, random, itertools, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hc_core import *
from hc_search_case2 import ZMENU, free_factors, supports, psi_menu, PSI_AB, required
from hc3_construct import *

N_RANDOM = int(sys.argv[1]) if len(sys.argv) > 1 else 600
N_ADV = int(sys.argv[2]) if len(sys.argv) > 2 else 600
L1 = int(sys.argv[3]) if len(sys.argv) > 3 else 7
t0 = time.time()


def fail(msg, **kw):
    print("FAILURE:", msg)
    for k, v in kw.items():
        print("   ", k, "=", v)
    sys.exit(1)


# ---------------------------------------------------------------- [1]
print("== [1] realize() vs hosts() (all words <= %d, holes total length <= 4)" % L1, flush=True)
G_of = {}
for L in range(1, L1 + 1):
    for t in itertools.product("abc", repeat=L):
        G_of.setdefault(gamma("".join(t)), "".join(t))
HW = [''.join(t) for n in range(1, 4) for t in itertools.product("abc", repeat=n)]
tuples = [(h,) for h in HW] + [(h1, h2) for h1 in HW for h2 in HW if len(h1) + len(h2) <= 4]
cnt = Counter()
for G in G_of:
    for H in tuples:
        d = hosts(G, H)
        r = realize(G, H)
        if (r is not None) != d:
            fail("realize/hosts mismatch", G=G, H=H, decided=d, realized=r)
        if r:
            w, pos = r
            if gamma(w) != G:
                fail("witness Gamma", G=G, H=H, w=w)
            for i, (h, q) in enumerate(zip(H, pos)):
                if w[q:q + len(h)] != h or (i and q < pos[i - 1] + len(H[i - 1]) + 1):
                    fail("witness placement", G=G, H=H, w=w, pos=pos)
            cnt["witness"] += 1
        cnt["tests"] += 1
print("   Gamma classes", len(G_of), dict(cnt), "(%.0f s)" % (time.time() - t0), flush=True)


# ---------------------------------------------------------------- [2]
def build_cfg(rng, x, cstar, adversarial=False):
    phs = free_factors(x, cstar, lambda f: internal_windows(f)[0]["aa"] and internal_windows(f)[1]["bb"])
    if not phs:
        return None
    s, e = rng.choice(phs)
    Zp = rng.choice(ZMENU)
    others = [q for q in free_factors(x, cstar, lambda f: supports(f, Zp)) if q[1] <= s or q[0] >= e]
    if not others:
        return None
    s2, e2 = rng.choice(others)
    psi = rng.choice(PSI_AB + ["cc", "cac", "cbc", "acb", "bca", "aabb"])
    psip = rng.choice(psi_menu(Zp))
    segs = [((s, e), psi), ((s2, e2), psip)]
    xw = x
    for (u, v), rep in sorted(segs, reverse=True):
        xw = xw[:u] + rep + xw[v:]
    mp = pos_map(x, segs)
    v0 = rng.choice(["", "a", "b", "c", "ac", "bc", "cc"])
    v2 = rng.choice(["", "a", "b", "c", "ca", "cb", "cc"])
    other = "".join(rng.choices("abc", k=rng.randint(0, 5)))
    first = rng.random() < 0.5            # x is the first or the second root component
    if other:
        sep = rng.choice(["c", "a", "b"])
        W = v0 + (xw + sep + other if first else other + sep + xw) + v2
        off = len(v0) if first else len(v0) + len(other) + 1
    else:
        W = v0 + xw + v2; off = len(v0)
    assert W[off:off + len(xw)] == xw
    return dict(x=x, phi=(s, e), phip=(s2, e2), Zp=Zp, psi=psi, psip=psip, W=W, off=off, mp=mp)


def run_cfg(cfg, cstar, stats):
    x = cfg["x"]
    ZK = ({"aa": 1}, {"bb": 1})
    Ztot = zadd(ZK, cfg["Zp"])
    TT = sorted(state_range(x, Ztot, cstar))
    if len(TT) > 64:                       # keep the 16 extreme ones + 48 random
        TT = TT[:8] + TT[-8:] + random.Random(len(TT)).sample(TT[8:-8], 48)
        stats["states-subsampled-configs"] += 1
    if not TT:
        stats["empty-state-range"] += 1
        return
    W = cfg["W"]; GF = gamma(W); DW = dat_ov(W)
    for T in TT:
        cfg["T"] = T
        try:
            branch, holes, parts, flit = hc3_holes(cfg, cstar)
        except AssertionError as ex:
            fail("proof step failed: " + str(ex), cfg=cfg)
        stats[branch] += 1
        # parts
        if not (1 <= len(holes) <= 2) or any(not h for h in holes):
            fail("hole count/emptiness", cfg=cfg, holes=holes)
        if norm(zadd(*parts)) != norm(Ztot) or not all(conserving(P) for P in parts):
            fail("parts", cfg=cfg, parts=parts)
        ts = [expand(h, P) for h, P in zip(holes, parts)]
        for h, t, P in zip(holes, ts, parts):
            if not required(P) <= set(h) or set(t) != set(h):
                fail("required letters / content type", cfg=cfg, h=h, t=t)
        # Y side
        ry = realize(T, holes)
        if ry is None:
            fail("Y side: state does not host the holes", cfg=cfg, holes=holes)
        y1, py = ry
        ypi = fill(y1, py, holes, ts)
        if gamma(y1) != T or norm(zdiff(ypi, y1)) != norm(Ztot) or shat_pair(ypi) != shat_pair(y1):
            fail("Y side data", cfg=cfg, y1=y1, ypi=ypi)
        if branch == "B-rich":
            for h in S6:
                if not hosts(T, (h,)):
                    fail("rich lemma: T misses an S6 word", cfg=cfg, h=h)
        # F side
        if flit is not None:
            Ws, pf = W, flit
            for h, q in zip(holes, pf):
                if Ws[q:q + len(h)] != h:
                    fail("F literal placement", cfg=cfg, holes=holes, pos=pf)
            if len(pf) == 2 and pf[1] < pf[0] + len(holes[0]) + 1:
                fail("F literal gap", cfg=cfg, pos=pf)
            stats["F-literal(W*=W)"] += 1
        else:
            rf = realize(GF, holes)
            if rf is None:
                fail("F side: Gamma(W) does not host the holes", cfg=cfg, holes=holes)
            Ws, pf = rf
        if dat_ov(Ws) != DW:
            fail("F side: dat changed", cfg=cfg, Ws=Ws)
        Ft = fill(Ws, pf, holes, ts)
        if norm(zdiff(Ft, Ws)) != norm(Ztot) or shat_pair(Ft) != shat_pair(Ws):
            fail("F side H* difference", cfg=cfg, Ws=Ws, Ft=Ft)
        stats["ok"] += 1


def rand_x(rng, cstar):
    Qp = "a" * (cstar + 1) + "c" * (cstar + 1) + "b" * (cstar + 1) + "c" + "ac" * (cstar + 1) + "bc" * (cstar + 1)
    if rng.random() < 0.5:
        body = "".join(rng.choices("abc", weights=rng.choice([(3, 3, 2), (2, 2, 3), (4, 4, 1), (1, 1, 1)]), k=rng.randint(6, 16)))
    else:
        body = "".join(ch * rng.randint(1, cstar + 3) for ch in rng.choices("abc", k=rng.randint(3, 9)))
    pre = Qp if rng.random() < 0.5 else ""
    return pre + body if rng.random() < 0.5 else body + pre


def adv_x(rng, cstar):
    """shapes with nu_A = 0 or nu_B = 0 (a's or b's only in end intervals)"""
    X, Y = rng.choice([("a", "b"), ("b", "a")])
    def endblock():
        k = rng.randint(0, 3)
        return "".join(rng.choice([X * rng.randint(1, cstar + 3), Y * rng.randint(1, cstar + 3)]) for _ in range(k))
    inner = []
    for _ in range(rng.randint(cstar + 2, cstar + 8)):
        inner.append(rng.choice(["", "", Y * rng.randint(1, 3)]) if rng.random() < 0.6 else "")
    u0, un = endblock(), endblock()
    if rng.random() < 0.5:
        un += X * (cstar + 2) + Y * (cstar + 2) + X * 2 + Y * 2
    else:
        u0 = X * (cstar + 2) + Y * (cstar + 2) + X * 2 + Y * 2 + u0
    if rng.random() < 0.5:
        return u0 + "c" + "c".join(inner) + "c" + un
    # targeted templates (then mirrored a<->b at random)
    k = cstar
    t = rng.choice(("first", "last-sep", "last-both"))
    if t == "first":
        w = "a" * (k + 3) + "b" * (k + 3) + "aabb" + "c" * (k + rng.randint(4, 7)) + rng.choice(["", "b", "bb", "a"])
    elif t == "last-sep":
        inner = "c".join("b" * rng.randint(2, 3) for _ in range(k + rng.randint(1, 3)))
        w = rng.choice(["", "a", "aa"]) + "c" + inner + "c" * (k + rng.randint(4, 7)) + "a" * (k + rng.randint(1, 3)) + "aabb"
    else:
        w = rng.choice(["", "a", "b"]) + "c" * (k + rng.randint(4, 7)) + "b" * (k + 2) + "a" * (k + 2) + "aabb"
    if rng.random() < 0.5:
        w = w.translate(str.maketrans("ab", "ba"))
    return w


print("== [2] Case III construction (Theorems III-A, III-B)")
grand = Counter()
for cstar, seed, nr, na in ((3, 801, N_RANDOM, N_ADV), (4, 802, N_RANDOM // 2, N_ADV // 2), (5, 803, N_RANDOM // 3, N_ADV // 3)):
    rng = random.Random(seed)
    stats = Counter(); done = Counter(); tries = 0
    while (done["rand"] < nr or done["adv"] < na) and tries < 400 * (nr + na):
        tries += 1
        kind = "rand" if done["rand"] < nr else "adv"
        if done["rand"] < nr and done["adv"] < na:
            kind = rng.choice(("rand", "adv"))
        x = rand_x(rng, cstar) if kind == "rand" else adv_x(rng, cstar)
        cfg = build_cfg(rng, x, cstar)
        if cfg is None:
            continue
        done[kind] += 1
        run_cfg(cfg, cstar, stats)
    print("   CSTAR", cstar, "SEED", seed, "configs", dict(done), dict(sorted(stats.items())), "(%.0f s)" % (time.time() - t0), flush=True)
    grand.update(stats)

# ---------------------------------------------------------------- [3]
print("== [3] branch coverage")
need = ["A", "B-rich", "B-a0-first", "B-a0-last-both", "B-a0-last-sep",
        "B-b0-first", "B-b0-last-both", "B-b0-last-sep"]
for b in need:
    print("   %-18s %d" % (b, grand[b]))
missing = [b for b in need if grand[b] == 0]
if missing:
    print("   UNCOVERED BRANCHES:", missing, "(not a failure of the proof, a gap of the test)")
# ---------------------------------------------------------------- [4]
print("== [4] negative controls (must detect failures; not part of the proof)")
rng = random.Random(804); ctl = Counter(); seen = 0
while seen < 150:
    x = adv_x(rng, 3)
    cfg = build_cfg(rng, x, 3)
    if cfg is None:
        continue
    seen += 1
    Ztot = zadd(({"aa": 1}, {"bb": 1}), cfg["Zp"])
    if sum(zvec(cfg["Zp"])[1:3]) == 0:
        continue
    GF = gamma(cfg["W"])
    for T in sorted(state_range(x, Ztot, 3))[:16]:
        for h in S6:   # fixed hole, ignoring the proof's choice
            ctl["fixed-%s:%s" % (h, "ok" if hosts(T, (h,)) and hosts(GF, (h,)) else "FAILS")] += 1
    # c* = 2: the rich-case bound n_T >= 3 is allowed to fail
    cfg2 = build_cfg(random.Random(seen), x, 2)
    if cfg2:
        for T in sorted(state_range(x, zadd(({"aa": 1}, {"bb": 1}), cfg2["Zp"]), 2))[:16]:
            cfg2["T"] = T
            try:
                hc3_holes(cfg2, 2); ctl["cstar2:ok"] += 1
            except AssertionError as ex:
                ctl["cstar2:assert(%s)" % str(ex)[:30]] += 1
for k in sorted(ctl):
    print("   ", k, ctl[k])
if not any("FAILS" in k for k in ctl):
    fail("negative control detected nothing")

print("ALL ASSERTIONS PASSED  ok=%d  (%.0f s)" % (grand["ok"], time.time() - t0))
```

### `hc3_construct.py`

```python
#!/usr/bin/env python3
"""Round 8: constructive realiser and the Case-III construction of
Theorems III-A / III-B (claude_fanout2_round8_HCIII_report_2026-11-14.md).

New relative to round 7 (round7_hc/hc_core.py, hc_construct.py are reused
unchanged):
  * realize(G, holes): builds an explicit word with Gamma G containing the
    holes in order, pairwise disjoint, with nonempty gaps (or returns None).
    Checked against the decider hosts() in check_round8 [1].
  * hc3_holes(cfg): the hole choice of the proof, branch by branch, with the
    intermediate facts of the proof asserted on the configuration.
Standard library only.
"""
import itertools
from hc_core import *
from hc_core import _place_constraints
from hc_construct import expand, zdiff, marked_occurrences, interval_bounds

S6 = ("abc", "bac", "cab", "cba", "acb", "bca")


# ------------------------------------------------------------ realiser

def _side_vector(n, tot, nu, e0, en, cons):
    """constructive feasible_side: return alpha_0..alpha_n or None"""
    al = [0] * (n + 1)
    flex = []
    free = []
    for p in range(n + 1):
        c = cons.get(p)
        if p in (0, n):
            e = e0 if p == 0 else en
            if c is None:
                if e:
                    al[p] = 1; flex.append(p)
                continue
            kind, v = c
            if kind == "ex":
                if (v > 0) != e:
                    return None
                al[p] = v
            else:
                if v > 0 and not e:
                    return None
                if e:
                    al[p] = max(v, 1); flex.append(p)
            continue
        if c is None:
            free.append(p); continue
        kind, v = c
        if kind == "ex":
            al[p] = v
        elif v > 0:
            al[p] = v; flex.append(p)
        else:
            free.append(p)
    forced = sum(1 for p in range(1, n) if al[p] > 0)
    extra = nu - forced
    if extra < 0 or extra > len(free):
        return None
    for p in free[:extra]:
        al[p] = 1; flex.append(p)
    rest = tot - sum(al)
    if rest < 0 or (rest > 0 and not flex):
        return None
    if rest:
        al[flex[0]] += rest
    return al


def realize(G, holes):
    """explicit witness: (word, [start positions]) or None"""
    holes = tuple(holes)
    if G[0] == 0:
        n, ta, tb = G
        if any("c" in h for h in holes):
            return None
        ra = ta - sum(h.count("a") for h in holes); rb = tb - sum(h.count("b") for h in holes)
        if ra < 0 or rb < 0 or ra + rb < len(holes) - 1:
            return None
        out, pos, pool = "", [], ["a"] * ra + ["b"] * rb
        for i, h in enumerate(holes):
            if i:
                out += pool.pop()
            pos.append(len(out)); out += h
        out += "".join(pool)
        return out, pos
    n, ta, tb, nuA, nuB, a0, an, b0, bn = G
    ks = [h.count("c") for h in holes]
    for starts in _starts(n, ks):
        for cA, cB in _place_constraints(n, holes, starts):
            va = _side_vector(n, ta, nuA, a0, an, cA)
            vb = _side_vector(n, tb, nuB, b0, bn, cB)
            if va is None or vb is None:
                continue
            w = _build(n, va, vb, holes, starts)
            if w is not None:
                return w
    return None


def _starts(n, ks):
    def rec(i, lo, acc):
        if i == len(ks):
            yield acc; return
        for s in range(lo, n + 1 - ks[i]):
            yield from rec(i + 1, s + ks[i], acc + (s,))
    yield from rec(0, 0, ())


def _build(n, va, vb, holes, starts):
    # items per interval: (hole index, part index, part string, kind)
    items = {p: [] for p in range(n + 1)}
    for i, (h, s) in enumerate(zip(holes, starts)):
        parts = h.split("c"); k = len(parts) - 1
        for m, part in enumerate(parts):
            kind = "whole" if k == 0 else ("suffix" if m == 0 else ("prefix" if m == k else "exact"))
            items[s + m].append((i, m, part, kind))
    segs = []
    holepos = {}
    for p in range(n + 1):
        its = items[p]
        need_a = sum(x[2].count("a") for x in its); need_b = sum(x[2].count("b") for x in its)
        ea, eb = va[p] - need_a, vb[p] - need_b
        if ea < 0 or eb < 0:
            return None
        pool = ["a"] * ea + ["b"] * eb
        if any(x[3] == "exact" for x in its):
            if pool or len(its) != 1:
                return None
            segs.append([("H", its[0])]); continue
        # slots: before item0, between items, after last
        seq = []
        nslots = len(its) + 1
        allowed = [True] * nslots
        for j, it in enumerate(its):
            if it[3] == "prefix":
                allowed[j] = False if j == 0 else allowed[j]
                if j != 0:
                    return None          # prefix part must open the interval
            if it[3] == "suffix":
                allowed[j + 1] = False
                if j != len(its) - 1:
                    return None          # suffix part must close the interval
        gapfill = [0] * nslots
        for j in range(1, len(its)):     # gaps between different holes
            if not pool:
                return None
            gapfill[j] += 1
        free_slots = [j for j in range(nslots) if allowed[j]]
        if len(pool) - sum(gapfill) < 0:
            return None
        if len(pool) > sum(gapfill) and not free_slots:
            return None
        rest = len(pool) - sum(gapfill)
        if rest:
            gapfill[free_slots[0]] += rest
        q = list(pool)
        for j in range(nslots):
            seq.append(("X", "".join(q.pop() for _ in range(gapfill[j]))))
            if j < len(its):
                seq.append(("H", its[j]))
        segs.append(seq)
    # assemble and record hole start positions
    out = ""
    for p, seq in enumerate(segs):
        if p:
            out += "c"
        for typ, val in seq:
            if typ == "X":
                out += val
            else:
                i, m, part, kind = val
                if m == 0:
                    holepos[i] = len(out)
                out += part
    pos = [holepos[i] for i in range(len(holes))]
    for h, q in zip(holes, pos):
        if out[q:q + len(h)] != h:
            return None
    for i in range(1, len(holes)):
        if pos[i] < pos[i - 1] + len(holes[i - 1]) + 1:
            return None
    return out, pos


# ------------------------------------------------------------ Z utilities

def zvec(Z):
    A, B = Z
    return (A.get("aa", 0), A.get("cc", 0), A.get("ac", 0), B.get("bb", 0), B.get("cc", 0), B.get("bc", 0))


def zunvec(v):
    p, q, r, pp, qq, rr = v
    A = {k: x for k, x in (("aa", p), ("cc", q), ("ac", r), ("ca", r)) if x}
    B = {k: x for k, x in (("bb", pp), ("cc", qq), ("bc", rr), ("cb", rr)) if x}
    return (A, B)


def zadd(*Zs):
    return zunvec(tuple(sum(t) for t in zip(*[zvec(Z) for Z in Zs])))


def conserving(Z):
    p, q, r, pp, qq, rr = zvec(Z)
    return q + r == qq + rr


def norm(Z):
    return tuple({k: v for k, v in d.items() if v} for d in Z)


def fill(w, pos, holes, ts):
    out, last = "", 0
    for q, h, t in zip(pos, holes, ts):
        out += w[last:q] + t; last = q + len(h)
    return out + w[last:]


def shat_pair(w):
    return shat(proj(w, "ac")), shat(proj(w, "bc"))


# ------------------------------------------------------------ the proof's choice

def pos_map(x, segs):
    """segs: list of ((u,v), rep) disjoint replaced spans of x; returns map of
    untouched x-positions to positions in x'"""
    segs = sorted(segs)
    mp, shift, j = {}, 0, 0
    for i in range(len(x)):
        while j < len(segs) and i >= segs[j][0][1]:
            (u, v), rep = segs[j]; shift += len(rep) - (v - u); j += 1
        if j < len(segs) and segs[j][0][0] <= i < segs[j][0][1]:
            continue
        mp[i] = i + shift
    return mp


def hc3_holes(cfg, cstar):
    """returns (branch, holes, parts, F_literal_positions or None)"""
    x, (s, e), (s2, e2), Zp, W, off, mp, T = (cfg[k] for k in ("x", "phi", "phip", "Zp", "W", "off", "mp", "T"))
    p, qc, r, pp_, qcp, rp = zvec(Zp)
    q, qp = Zp[0].get("aa", 0), Zp[1].get("bb", 0)
    mprime = qc + r
    assert mprime == qcp + rp
    ZK = ({"aa": 1}, {"bb": 1})
    Ztot = zadd(ZK, Zp)
    if mprime == 0:
        # Theorem III-A: holes a and b at marked letters of W
        ua = [(i, j) for (k, i, j) in marked_occurrences(x, "ac", cstar) if k == "aa"][0]
        vb = [(i, j) for (k, i, j) in marked_occurrences(x, "bc", cstar) if k == "bb"][0]
        assert all(t < s for t in ua + vb), "FO: marked aa/bb letters precede phi"
        cand = [(abs(mp[i] - mp[j]), i, j) for i in ua for j in vb]
        good = [(i, j) for (d, i, j) in cand if d >= 2]
        assert good, "III-A: some marked (a,b) pair at distance >= 2"
        i, j = good[0]
        Pa = zunvec((1 + q, 0, 0, 0, 0, 0)); Pb = zunvec((0, 0, 0, 1 + qp, 0, 0))
        if mp[i] < mp[j]:
            return "A", ("a", "b"), (Pa, Pb), [off + mp[i], off + mp[j]]
        return "A", ("b", "a"), (Pb, Pa), [off + mp[j], off + mp[i]]
    # Theorem III-B: one hole from S6
    n, ta, tb, nuA, nuB = T[:5]
    if nuA >= 1 and nuB >= 1:
        assert n >= 3, "rich case: n_T >= 3 (needs cstar >= 3)"
        for h in S6:
            if hosts(gamma(W), (h,)):
                return "B-rich", (h,), (Ztot,), None
        raise AssertionError("F hosts no S6 word (rigid W)")
    X = "a" if nuA == 0 else "b"; Y = "b" if X == "a" else "a"
    rX = r if X == "a" else rp
    qX = qc if X == "a" else qcp
    assert rX == 0 and qX >= 1, "nu_X=0 forces r_X=0, q_c^X>=1"
    phi = x[s:e]
    assert "c" not in phi, "nu_X=0: phi has no c"
    ib = interval_bounds(x)
    n0 = len(ib) - 1
    k_phi = [k for k, (u, v) in enumerate(ib) if u <= s and e <= v]
    assert k_phi and k_phi[0] in (0, n0), "phi lies in the first or last interval"
    if k_phi[0] == 0:
        return "B-" + X + "0-first", (X + Y + "c",), (Ztot,), None
    lastc = ib[n0][0] - 1
    Lam = x[lastc + 1:s]
    assert X in Lam, "unique cX window is marked: first X of u_n precedes phi"
    if Y in Lam:
        return "B-" + X + "0-last-both", ("c" + X + Y,), (Ztot,), None
    nuY_x = sum(1 for k in range(1, n0) if Y in x[ib[k][0]:ib[k][1]])
    assert nuY_x >= 1, "nu_Y(x) >= 1 when Lambda has no Y"
    return "B-" + X + "0-last-sep", (Y + "c" + X,), (Ztot,), None
```

### `hc3_search.py`

```python
#!/usr/bin/env python3
"""Round 8: bounded search for Case III (both deleting eta-components kappa, kappa'
in the SAME root component), in the Gamma-only formulation of Lemma R:

  (Y) the next state T (Lemma P range) hosts (h_1[,h_2]) in order, disjoint,
      nonempty gap;
  (F) Gamma(W_{j'}) hosts the same ordered holes (no locality requirement:
      Lemma R only needs a sentence with the data of W_{j'}).

Hole options: one hole for Z_kappa+Z_kappa', or ANY split D_1+D_2 into two
nonzero circulation pairs with per-hole c-conservation (all splits enumerated),
each hole a word containing the required letters R(D_i).
Model is the permissive superset of round 7 (hc_search_case13): psi only has
|pi_X psi| >= 2 where needed; states are the whole Lemma-P range.
Usage: hc3_search.py CSTAR SEED N [MAXLEN]
"""
import itertools, random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hc_core import *
from hc_search_case2 import ZMENU, free_factors, supports, psi_menu, PSI_AB, required

CSTAR = int(sys.argv[1]) if len(sys.argv) > 1 else 3
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 1
N = int(sys.argv[3]) if len(sys.argv) > 3 else 200
MAXLEN = int(sys.argv[4]) if len(sys.argv) > 4 else 3
rng = random.Random(SEED)

ZAB = ({"aa": 1}, {"bb": 1})


def vec(Z):
    A, B = Z
    return (A.get("aa", 0), A.get("cc", 0), A.get("ac", 0), B.get("bb", 0), B.get("cc", 0), B.get("bc", 0))


def unvec(v):
    p, q, r, pp, qq, rr = v
    A = {k: x for k, x in (("aa", p), ("cc", q), ("ac", r), ("ca", r)) if x}
    B = {k: x for k, x in (("bb", pp), ("cc", qq), ("bc", rr), ("cb", rr)) if x}
    return (A, B)


def valid(v):
    p, q, r, pp, qq, rr = v
    return q + r == qq + rr


def splits(Ztot):
    """yield lists of parts (each a Z) : one hole, or two nonzero conserving parts"""
    v = vec(Ztot)
    yield [Ztot]
    for d1 in itertools.product(*[range(x + 1) for x in v]):
        d2 = tuple(a - b for a, b in zip(v, d1))
        if not any(d1) or not any(d2):
            continue
        if valid(d1) and valid(d2) and d1 <= d2:
            yield [unvec(d1), unvec(d2)]


WORDS = [''.join(t) for n in range(1, MAXLEN + 1) for t in itertools.product("abc", repeat=n)]


def cands(need, nmax):
    c = [w for w in WORDS if need <= set(w)]
    for k in range(MAXLEN, nmax + 2):
        for X in ("a", "b", ""):
            for Y in ("a", "b", ""):
                w = X + "c" * k + Y
                if need <= set(w) and w not in c:
                    c.append(w)
    return c


def addZ(Z1, Z2):
    return unvec(tuple(a + b for a, b in zip(vec(Z1), vec(Z2))))


def decide(T, GF, Ztot, nmax, record):
    for parts in splits(Ztot):
        C = [cands(required(P), nmax) for P in parts]
        for combo in itertools.product(*C):
            for perm in set(itertools.permutations(combo)):
                if hosts(T, perm) and hosts(GF, perm):
                    record.append((len(parts), perm))
                    return True
    return False


def rand_word(L, wts):
    return "".join(rng.choices("abc", weights=wts, k=L))


stats = Counter(); CEX = []
done = 0
tries = 0
while done < N and tries < 200 * N:
    tries += 1
    Qp = "a" * (CSTAR + 1) + "c" * (CSTAR + 1) + "b" * (CSTAR + 1) + "c" + "ac" * (CSTAR + 1) + "bc" * (CSTAR + 1)
    if rng.random() < 0.5:
        body = rand_word(rng.randint(6, 16), rng.choice([(3, 3, 2), (2, 2, 3), (4, 4, 1), (1, 1, 1)]))
    else:
        body = "".join(ch * rng.randint(1, CSTAR + 3) for ch in rng.choices("abc", k=rng.randint(3, 9)))
    pre = Qp if rng.random() < 0.5 else ""
    x = pre + body if rng.random() < 0.5 else body + pre
    phs = free_factors(x, CSTAR, lambda f: internal_windows(f)[0]["aa"] and internal_windows(f)[1]["bb"])
    if not phs:
        continue
    s, e = rng.choice(phs)
    Zp = rng.choice(ZMENU)
    others = [q for q in free_factors(x, CSTAR, lambda f: supports(f, Zp)) if q[1] <= s or q[0] >= e]
    if not others:
        continue
    pp = rng.choice(others)
    psi = rng.choice(PSI_AB + ["cc", "cac", "cbc", "acb", "bca"])
    psip = rng.choice(psi_menu(Zp))
    segs = sorted([((s, e), psi), (pp, psip)], reverse=True)
    xw = x
    for (u, v), rep in segs:
        xw = xw[:u] + rep + xw[v:]
    v0 = rng.choice(["", "a", "b", "c", "ac", "bc"]); v2 = rng.choice(["", "a", "b", "c", "ca", "cb"])
    other = rand_word(rng.randint(0, 5), (1, 1, 1))
    W = v0 + xw + (("c" + other) if (other and rng.random() < 0.5) else other) + v2
    GF = gamma(W)
    Ztot = addZ(ZAB, Zp)
    TT = sorted(state_range(x, Ztot, CSTAR))
    if not TT:
        stats["empty-range"] += 1
        continue
    if len(TT) > 16:
        TT = TT[:4] + TT[-4:] + rng.sample(TT[4:-4], 8)
    done += 1
    nmax = max(W.count("c"), x.count("c"))
    for T in TT:
        rec = []
        ok = decide(T, GF, Ztot, nmax, rec)
        key = "ok" if ok else "NOT-FOUND-WITHIN-BOUND"
        stats[key] += 1
        if ok:
            stats["holes=%d" % rec[0][0]] += 1
        elif len(CEX) < 10:
            CEX.append(dict(x=x, phi=(s, e), phip=pp, Zp=Zp, psi=psi, psip=psip, W=W, T=T, GF=GF))
print("CSTAR", CSTAR, "SEED", SEED, "configs", done, dict(stats))
for c in CEX:
    print("NOT FOUND WITHIN BOUND:", c)
```

### `hc_core.py`

```python
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
```

### `hc_construct.py`

```python
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
```

### `hc_search_case2.py`

```python
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
```

### `out_check_round8_HCIII_2026-11-14.txt`

```text
== [1] realize() vs hosts() (all words <= 7, holes total length <= 4)
   Gamma classes 841 {'witness': 47108, 'tests': 290145} (11 s)
== [2] Case III construction (Theorems III-A, III-B)
   CSTAR 3 SEED 801 configs {'rand': 600, 'adv': 600} {'A': 31509, 'B-a0-first': 1656, 'B-a0-last-both': 4513, 'B-a0-last-sep': 3136, 'B-b0-first': 1216, 'B-b0-last-both': 1536, 'B-b0-last-sep': 4476, 'B-rich': 26194, 'F-literal(W*=W)': 31509, 'ok': 74236, 'states-subsampled-configs': 1089} (47 s)
   CSTAR 4 SEED 802 configs {'adv': 300, 'rand': 300} {'A': 16447, 'B-a0-first': 386, 'B-a0-last-both': 2434, 'B-a0-last-sep': 2226, 'B-b0-first': 448, 'B-b0-last-both': 512, 'B-b0-last-sep': 1728, 'B-rich': 12709, 'F-literal(W*=W)': 16447, 'ok': 36890, 'states-subsampled-configs': 536} (70 s)
   CSTAR 5 SEED 803 configs {'rand': 200, 'adv': 200} {'A': 12027, 'B-a0-first': 703, 'B-a0-last-both': 1433, 'B-a0-last-sep': 1088, 'B-b0-first': 192, 'B-b0-last-both': 319, 'B-b0-last-sep': 960, 'B-rich': 8320, 'F-literal(W*=W)': 12027, 'ok': 25042, 'states-subsampled-configs': 376} (86 s)
== [3] branch coverage
   A                  59983
   B-rich             47223
   B-a0-first         2745
   B-a0-last-both     8380
   B-a0-last-sep      6450
   B-b0-first         1856
   B-b0-last-both     2367
   B-b0-last-sep      7164
== [4] negative controls (must detect failures; not part of the proof)
    cstar2:ok 144
    fixed-abc:FAILS 960
    fixed-abc:ok 304
    fixed-acb:FAILS 464
    fixed-acb:ok 800
    fixed-bac:FAILS 960
    fixed-bac:ok 304
    fixed-bca:FAILS 608
    fixed-bca:ok 656
    fixed-cab:FAILS 128
    fixed-cab:ok 1136
    fixed-cba:FAILS 128
    fixed-cba:ok 1136
ALL ASSERTIONS PASSED  ok=136168  (87 s)
```

### `out_hc3_search_2026-11-14.txt`

```text
CSTAR 3 SEED 1 configs 400 {'ok': 6400, 'holes=1': 6400}
CSTAR 3 SEED 2 configs 400 {'ok': 6388, 'holes=1': 6388}
CSTAR 2 SEED 11 configs 500 {'ok': 7996, 'holes=1': 7996}
CSTAR 2 SEED 12 configs 500 {'ok': 7992, 'holes=1': 7992}
CSTAR 4 SEED 5 configs 300 {'ok': 4800, 'holes=1': 4800}
CSTAR 5 SEED 6 configs 200 {'ok': 3200, 'holes=1': 3200}
```

### `audit_round8_hcIII_independent_2026-11-14.py`

```python
#!/usr/bin/env python3
"""Independent bounded checks for the round-8 HC_III proof's pure word lemmas.

No imports from the original Claude scripts. These finite tests do not audit P1,
B6, or arbitrary good MCFG derivation trees. Python standard library only.
"""
from collections import Counter, defaultdict
from itertools import product

ALPHA = 'abc'
S6 = ('abc','bac','cab','cba','acb','bca')

def proj(w, subset):
    return ''.join(x for x in w if x in subset)

def stat(w, subset):
    u = proj(w, subset)
    tag = ('short',u) if len(u)<2 else ('long',u[0],u[-1])
    return tag, Counter(u[i:i+2] for i in range(len(u)-1))

def dat(w):
    a,b=stat(w,'ac'),stat(w,'bc')
    return (a[0],tuple(sorted(a[1].items())),b[0],tuple(sorted(b[1].items())))

def gamma(w):
    pp=w.split('c'); n=len(pp)-1
    a=[t.count('a') for t in pp]; b=[t.count('b') for t in pp]
    if n==0: return (0,a[0],b[0])
    return (n,sum(a),sum(b),sum(x>0 for x in a[1:-1]),sum(x>0 for x in b[1:-1]),
            bool(a[0]),bool(a[-1]),bool(b[0]),bool(b[-1]))

def allwords(maxn):
    for n in range(1,maxn+1):
        for t in product(ALPHA,repeat=n): yield ''.join(t)

def expand(h,p,pp,q,qp,r,rp):
    assert q+r==qp+rp
    out=[]; seen=set(); m=q+r
    for c in h:
        if c in seen:
            out.append(c); continue
        seen.add(c)
        if c=='a': out.append('a'*(1+p))
        elif c=='b': out.append('b'*(1+pp))
        else: out.append('c'+''.join(('a' if j<r else '')+('b' if j<rp else '')+'c' for j in range(m)))
    return ''.join(out)

def required(p,pp,q,qp,r,rp):
    out=set()
    if p+r: out.add('a')
    if pp+rp: out.add('b')
    if q+r: out.add('c')
    return out

def delta(u,v):
    return {k: stat(v,'ac')[1][k]-stat(u,'ac')[1][k] for k in ('aa','ac','ca','cc')}, {k: stat(v,'bc')[1][k]-stat(u,'bc')[1][k] for k in ('bb','bc','cb','cc')}

G2D={};D2G={}; G2words=defaultdict(list)
for w in allwords(8):
    G=gamma(w); D=dat(w)
    if G in G2D: assert G2D[G]==D,(w,G)
    if D in D2G: assert D2G[D]==G,(w,D)
    G2D[G]=D;D2G[D]=G;G2words[G].append(w)
print('GAMMA_BIJECTION: words=%d gamma_classes=%d dat_classes=%d'%(sum(map(len,G2words.values())),len(G2D),len(D2G)))
# F6-style immediate combinatorics: provided both letters occur, determine S6-hosted cases.
# The rigid configurations (a^+ c^n b^+, or reverse, n>=2) are the only Gamma values
# that do not host any S6 word in the class, for lengths <=8.
checked=rigid=0
for G,ww in G2words.items():
    if G[0]==0 or not any('a' in w and 'b' in w for w in ww):continue
    hits=[h for h in S6 if any(h in w for w in ww)]
    if not hits:
        rigid+=1
        n=G[0]
        na,nb=G[1:3]
        assert n>=2 and na>0 and nb>0
        expected=(n,na,nb,0,0,True,False,False,True)
        rev=(n,na,nb,0,0,False,True,True,False)
        assert G in (expected,rev),(G,ww[:2])
    checked+=1
print('S6_NO_HOST_CLASSIFICATION: gamma_with_a_b_c=%d rigid=%d'%(checked,rigid))
# Y6-style: when n>=3 and both nu>=1, every S6 candidate is hostable.
y6count=0
for G,ww in G2words.items():
    if len(G)!=9:continue
    n,_,_,nuA,nuB,*_=G
    if n>=3 and nuA>0 and nuB>0:
        for h in S6: assert any(h in w for w in ww),(G,h)
        y6count+=1
print('Y6_ALL_S6: classes=%d all_6_hostable=True'%y6count)
# H* context-independent window-count difference and typed boundary preservation
# under the explicit long-projection precondition; exact small parameters.
ctx=[''] + list(allwords(2))
tested=0;short_tag_exclusions=0
for p in range(3):
 for pp in range(3):
  for m in range(3):
   for r in range(m+1):
    for rp in range(m+1):
     q=m-r;qp=m-rp
     R=required(p,pp,q,qp,r,rp)
     for h in ('a','b','c','ab','ba')+S6:
      if not R.issubset(set(h)):continue
      t=expand(h,p,pp,q,qp,r,rp)
      assert set(t)==set(h)
      expectA={'aa':p,'ac':r,'ca':r,'cc':q}
      expectB={'bb':pp,'bc':rp,'cb':rp,'cc':qp}
      for u in ctx:
       for v in ctx:
        w=u+h+v; w2=u+t+v
        if len(proj(w,'ac'))<2 or len(proj(w,'bc'))<2:
            short_tag_exclusions+=1;continue
        da,db=delta(w,w2)
        assert da==expectA and db==expectB,(u,h,v,t,da,db,expectA,expectB)
        assert stat(w,'ac')[0]==stat(w2,'ac')[0]
        assert stat(w,'bc')[0]==stat(w2,'bc')[0]
        tested+=1
print('H_STAR_CONTEXT_TEST: cases=%d short_projection_excluded=%d'%(tested,short_tag_exclusions))
print('ALL_INDEPENDENT_CHECKS_PASSED')
```

### `out_audit_round8_hcIII_independent_2026-11-14.txt`

```text
GAMMA_BIJECTION: words=9840 gamma_classes=1558 dat_classes=1558
S6_NO_HOST_CLASSIFICATION: gamma_with_a_b_c=1170 rigid=70
Y6_ALL_S6: classes=162 all_6_hostable=True
H_STAR_CONTEXT_TEST: cases=131664 short_projection_excluded=663
ALL_INDEPENDENT_CHECKS_PASSED
```

