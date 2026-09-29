#!/usr/bin/env python3
"""Exact finite audit for the rank-four binary census in OFET v31.

Standard-library only.  It verifies:
  * C(16,5)=4368 minimum-cardinality samples;
  * 2672 unimodular samples and 13 hyperoctahedral affine-shape orbits;
  * 2096 locking / 576 nonlocking unimodular samples under the exact
    nonempty fan-out-two laminar-trace fixed point;
  * 400 exchange-connected locking samples;
  * the row-10 / row-13 dihedral 16:8 coordinate-order split;
  * the native fan-out-two reachable-set sizes 12 (row 9 = K_diamond)
    and 10 (row 12).

The implementation follows Theorem ``Exact laminar-trace characterization``
literally for X_{2,4}.  A trace is a nonempty support on the eight ordered
positions A1 A2 A3 A4 B1 B2 B3 B4 having one or two interval components.
Semantic-unary components are collapsed exactly.  Composition is evaluated
by a finite fixed point over pairwise support-disjoint child traces.

No floating-point arithmetic and no third-party packages are used.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations
from math import comb

R = 4
N = 2 * R
FULL = (1 << N) - 1
CUBE = tuple(range(1 << R))
PERMS = tuple(permutations(range(R)))

PAPER_ROWS = (
    (0x0, 0x1, 0x2, 0x4, 0x8),
    (0x0, 0x1, 0x2, 0x4, 0x9),
    (0x0, 0x1, 0x2, 0x4, 0xB),
    (0x0, 0x1, 0x2, 0x4, 0xF),
    (0x0, 0x1, 0x2, 0x5, 0xA),
    (0x0, 0x1, 0x2, 0x5, 0xB),
    (0x0, 0x1, 0x2, 0x5, 0xE),
    (0x0, 0x1, 0x2, 0x7, 0xB),
    (0x0, 0x1, 0x2, 0x7, 0xC),
    (0x0, 0x1, 0x2, 0x7, 0xD),
    (0x0, 0x1, 0x2, 0x7, 0xF),
    (0x0, 0x1, 0x6, 0xA, 0xF),
    (0x0, 0x1, 0x6, 0xB, 0xE),
)
EXPECTED_ORBIT_SIZES = (16, 192, 192, 64, 192, 384, 384, 96, 192, 384, 192, 192, 192)
EXPECTED_D4 = {
    (0, 1, 2, 3), (1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2),
    (3, 2, 1, 0), (0, 3, 2, 1), (1, 0, 3, 2), (2, 1, 0, 3),
}


def popcount(x: int) -> int:
    return x.bit_count()


def det_bareiss(a):
    """Exact determinant over Z using fraction-free Bareiss elimination."""
    m = [list(map(int, row)) for row in a]
    n = len(m)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if m[i][k] != 0), None)
            if swap is None:
                return 0
            m[k], m[swap] = m[swap], m[k]
            sign *= -1
        pivot = m[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                m[i][j] = (m[i][j] * pivot - m[i][k] * m[k][j]) // prev
        for i in range(k + 1, n):
            m[i][k] = 0
        prev = pivot
    return sign * m[n - 1][n - 1]


def bits4(v: int):
    return tuple((v >> j) & 1 for j in range(R))


def unimodular(sample) -> bool:
    s = sorted(sample)
    base = bits4(s[0])
    cols = []
    for v in s[1:]:
        b = bits4(v)
        cols.append([b[j] - base[j] for j in range(R)])
    # columns -> matrix rows
    mat = [[cols[c][r] for c in range(R)] for r in range(R)]
    return abs(det_bareiss(mat)) == 1


def permute_vec(v: int, perm) -> int:
    # Physical coordinate j receives abstract coordinate perm[j].
    out = 0
    for j in range(R):
        if (v >> perm[j]) & 1:
            out |= 1 << j
    return out


def transform_sample(sample, perm, flip: int = 0):
    return tuple(sorted(permute_vec(v, perm) ^ flip for v in sample))


def bitflip_canonical(sample):
    return min(tuple(sorted(v ^ f for v in sample)) for f in CUBE)


def cube_orbit(sample):
    return {
        transform_sample(sample, p, f)
        for p in PERMS for f in CUBE
    }


def cube_canonical(sample):
    return min(cube_orbit(sample))


def exchange_connected(sample) -> bool:
    s = tuple(sample)
    seen = {s[0]}
    stack = [s[0]]
    S = set(s)
    while stack:
        v = stack.pop()
        for j in range(R):
            w = v ^ (1 << j)
            if w in S and w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == len(s)


def run_intervals(mask: int):
    out = []
    i = 0
    while i < N:
        if (mask >> i) & 1:
            j = i + 1
            while j < N and ((mask >> j) & 1):
                j += 1
            out.append((i, j))
            i = j
        else:
            i += 1
    return tuple(out)


TRACES = tuple(m for m in range(1, 1 << N) if len(run_intervals(m)) <= 2)
SUBTRACES = {
    M: tuple(Nm for Nm in TRACES if Nm != M and (Nm & M) == Nm)
    for M in TRACES
}
CHILD_BY_POINT = {
    (M, p): tuple(Nm for Nm in SUBTRACES[M] if (Nm >> p) & 1)
    for M in TRACES for p in range(N) if (M >> p) & 1
}
# Every derivable tuple preserves slot consistency: if a trace contains both
# Aj and Bj, they carry the same index bit; if it contains only one half, that
# half can never change away from its observed anchor because the other half
# remains in the concrete context.  Thus a trace has at most 2^4 relevant
# fillings, not 2^{|support|}.
CONSISTENT_ASSIGNMENTS = {}
for M in TRACES:
    touched = [j for j in range(R) if M & ((1 << j) | (1 << (R + j)))]
    vals = []
    for code in range(1 << len(touched)):
        a = 0
        for q, j in enumerate(touched):
            if (code >> q) & 1:
                if M & (1 << j):
                    a |= 1 << j
                if M & (1 << (R + j)):
                    a |= 1 << (R + j)
        vals.append(a)
    CONSISTENT_ASSIGNMENTS[M] = tuple(vals)


def expand_vec(v: int) -> int:
    """Duplicate slot bit j at positions Aj and Bj."""
    out = 0
    for j in range(R):
        if (v >> j) & 1:
            out |= (1 << j) | (1 << (R + j))
    return out


def build_unary_components(sample):
    Kexp = tuple(expand_vec(v) for v in sample)
    comp_of = {}
    comps = {}
    for M in TRACES:
        assigns = sorted({u & M for u in Kexp})
        adj = {a: {a} for a in assigns}
        # Shared concrete sentence context means equality outside M.
        for u in Kexp:
            a = u & M
            for v in Kexp:
                if ((u ^ v) & (FULL ^ M)) == 0:
                    b = v & M
                    adj[a].add(b)
                    adj[b].add(a)
        seen = set()
        cid = 0
        for a in assigns:
            if a in seen:
                continue
            cc = set()
            stack = [a]
            while stack:
                x = stack.pop()
                if x in cc:
                    continue
                cc.add(x)
                seen.add(x)
                stack.extend(adj[x] - cc)
            key = (M, cid)
            anchors = {u for u in Kexp if (u & M) in cc}
            comps[key] = (frozenset(cc), tuple(sorted(anchors)))
            for x in cc:
                comp_of[(M, x)] = key
            cid += 1
    return comp_of, comps


def laminar_reach(sample):
    """Exact fan-out-two full-word reachability for X_{2,4}."""
    comp_of, comps = build_unary_components(sample)
    derived = {key: set(assigns) for key, (assigns, _) in comps.items()}

    changed = True
    while changed:
        changed = False
        additions = {key: set() for key in comps}
        for key, (_, anchors) in comps.items():
            M, _ = key
            for anchor_word in anchors:
                anchor = anchor_word & M
                for target in CONSISTENT_ASSIGNMENTS[M]:
                    if target in derived[key]:
                        continue
                    diff = (anchor ^ target) & M
                    if not diff:
                        additions[key].add(target)
                        continue

                    @lru_cache(maxsize=None)
                    def can_cover(rem: int, used: int) -> bool:
                        if rem == 0:
                            return True
                        first = rem & -rem
                        p = first.bit_length() - 1
                        for child in CHILD_BY_POINT[(M, p)]:
                            if child & used:
                                continue
                            child_key = comp_of[(child, anchor_word & child)]
                            if (target & child) not in derived[child_key]:
                                continue
                            if can_cover(rem & ~child, used | child):
                                return True
                        return False

                    if can_cover(diff, 0):
                        additions[key].add(target)

        for key, vals in additions.items():
            new = vals - derived[key]
            if new:
                derived[key].update(new)
                changed = True

    reachable = set()
    for key in comps:
        if key[0] == FULL:
            reachable.update(derived[key])

    vectors = set()
    for a in reachable:
        v = 0
        ok = True
        for j in range(R):
            x = (a >> j) & 1
            y = (a >> (R + j)) & 1
            if x != y:
                ok = False
                break
            if x:
                v |= 1 << j
        if ok:
            vectors.add(v)
    return frozenset(vectors)


def main():
    all_samples = list(combinations(CUBE, 5))
    assert len(all_samples) == comb(16, 5) == 4368

    unims = [s for s in all_samples if unimodular(s)]
    assert len(unims) == 2672

    # Full cube-shape orbits.
    shape_classes = {}
    for s in unims:
        shape_classes.setdefault(cube_canonical(s), 0)
        shape_classes[cube_canonical(s)] += 1
    assert len(shape_classes) == 13

    paper_orbit_sizes = tuple(len(cube_orbit(row)) for row in PAPER_ROWS)
    assert paper_orbit_sizes == EXPECTED_ORBIT_SIZES
    assert sum(paper_orbit_sizes) == 2672
    assert {cube_canonical(row) for row in PAPER_ROWS} == set(shape_classes)

    # Bit flips are genuine learner symmetries; five-point sets have no
    # nontrivial translation stabilizer, so each bit-flip orbit has size 16.
    bf_reps = sorted({bitflip_canonical(s) for s in unims})
    assert len(bf_reps) == 2672 // 16 == 167
    for s in bf_reps:
        assert len({tuple(sorted(v ^ f for v in s)) for f in CUBE}) == 16

    lock_cache = {}
    reach_cache = {}
    for i, s in enumerate(bf_reps, 1):
        reach = laminar_reach(s)
        reach_cache[s] = reach
        lock_cache[s] = len(reach) == 16
        if i % 25 == 0:
            print(f"  evaluated {i:3d}/167 bit-flip classes", flush=True)

    lock_classes = sum(lock_cache.values())
    nonlock_classes = len(bf_reps) - lock_classes
    locking = 16 * lock_classes
    nonlocking = 16 * nonlock_classes
    assert (lock_classes, nonlock_classes) == (131, 36)
    assert (locking, nonlocking) == (2096, 576)

    exchange_classes = sum(exchange_connected(s) for s in bf_reps)
    assert exchange_classes == 25
    assert 16 * exchange_classes == 400

    # The two all-order failures and the mixed dihedral split.
    row9_reach = laminar_reach(PAPER_ROWS[8])
    row12_reach = laminar_reach(PAPER_ROWS[11])
    assert len(row9_reach) == 12
    assert len(row12_reach) == 10

    for row_index in (8, 11):  # paper rows 9 and 12
        assert all(
            not lock_cache[bitflip_canonical(transform_sample(PAPER_ROWS[row_index], p))]
            for p in PERMS
        )

    mixed_nonlocking = []
    for row_index in (9, 12):  # paper rows 10 and 13
        fails = {
            p for p in PERMS
            if not lock_cache[bitflip_canonical(transform_sample(PAPER_ROWS[row_index], p))]
        }
        mixed_nonlocking.append(fails)
        assert fails == EXPECTED_D4

    print("\nOFET rank-four exact audit: PASS")
    print(f"  all five-point samples:       {len(all_samples)}")
    print(f"  unimodular:                   {len(unims)}")
    print(f"  affine-shape orbits:          {len(shape_classes)}")
    print(f"  bit-flip learner classes:     {len(bf_reps)}")
    print(f"  locking / nonlocking:         {locking} / {nonlocking}")
    print(f"  exchange-connected locking:   {16 * exchange_classes}")
    print(f"  row 9 reachable full words:   {len(row9_reach)}")
    print(f"  row 12 reachable full words:  {len(row12_reach)}")
    d4_text = ["".join(map(str, p)) for p in sorted(EXPECTED_D4)]
    print("  mixed nonlocking orders:      " + ",".join(d4_text))
    print("  paper orbit sizes:            " + ",".join(map(str, paper_orbit_sizes)))


if __name__ == "__main__":
    main()
