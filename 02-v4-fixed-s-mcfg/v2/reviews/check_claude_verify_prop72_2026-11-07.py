"""check_claude_verify_prop72_2026-11-07.py -- independent checks (Claude, verifying thread) for claude_prop72_2026-11-07.md:
condition (T) of Thm 2.1 implemented directly from its statement (not via moves),
for Y23 (finite, exact) and E_N (infinite, on a box), plus F_L(Y23) by enumeration."""
import itertools
def supp(v): return frozenset(i for i in range(3) if v[i])
def T_violations(inQ, pts, box):
    """pts: the points of Q inside the box; checks (T) for gamma with both sides in box."""
    bad = 0
    P = list(pts)
    for q in P:
        for q2 in P:
            if q == q2 or supp(q) != supp(q2): continue
            h = tuple(b - a for a, b in zip(q, q2)); S = supp(h)
            hm = tuple(max(-x, 0) for x in h); hp = tuple(max(x, 0) for x in h)
            one = tuple(1 if i in S else 0 for i in range(3))
            lo = tuple(m + o for m, o in zip(hm, one)); hi = tuple(m + o for m, o in zip(hp, one))
            for g in itertools.product(range(box + 1), repeat=3):
                A = tuple(x + y for x, y in zip(lo, g)); B = tuple(x + y for x, y in zip(hi, g))
                if max(A) > box or max(B) > box: continue
                if inQ(A) != inQ(B): bad += 1
    return bad
# Y23 (finite): box 60 >= 2*26+8, so a violation with one side in Q and the other outside
# the box cannot be missed (|h| <= 26 componentwise)
Y = {(10,23,0),(1,2,5),(1,26,1),(11,10,2),(24,3,1)}
print('Y23 (T) violations (box 60):', T_violations(lambda p: p in Y, Y, 60))
# F_L(Y23): admissible K2 = Z(M,-M) with (10+M,23-M),(10-M,23+M) not in Pi2 ; H30 = Z(1,-1)
adm = [M for M in range(1, 200) if not (10+M >= 1 and 23-M >= 1) and not (10-M >= 1 and 23+M >= 1)]
print('F_L(Y23) = min admissible M =', min(adm))
# E_N on a box
for N in (2, 3, 4, 5):
    def inQ(p, N=N):
        a, b, c = p
        if c == 0: return (a, b) == (N, N)
        return ((a, b) == (1, 2) and c % 2 == 1) or ((a, b) == (2, 1) and c % 2 == 0 and c >= 2)
    box = N + 5
    pts = [p for p in itertools.product(range(box + 1), repeat=3) if any(p) and inQ(p)]
    print('E_%d (T) violations on box %d:' % (N, box), T_violations(inQ, pts, box))
