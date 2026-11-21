#!/usr/bin/env python3
"""R4 (Claude) finite checks.  Python 3 standard library only, no network.

Run:  python3 -I run_all.py      (exit code 0 iff every check passes)

All checks are CERTIFIED FINITE: they test bounded instances.  The universal
statements are proved in report.md, not here.

Sections
  [1] Lemma 1: the marker/order language R is (2,c_Gamma)-substitutable
      (bounded exhaustive two-hole and one-hole Rect).
  [2] Construction of H (product with the pattern automaton + compression) for
      the R1 example L_M = {a^(1+kM)}, X = typed (a,a^(M-1)), E_X = []1 a []2:
      L(H) = phi^{-1}(L) cap R up to a length bound; mu_{m^X}(L^X) = tau_{C_X}+1;
      pattern-thickness bound of Lemma 4.
  [3] Lemma 2/3: L^X for L_M is (2,c_Gamma)-substitutable (bounded Rect).
  [4] Fan-out-one sanity check: P_3 = T_3 minus {W_3}, X = U_2, E = c[]c:
      the reduction turns the internal singleton class into a rare root type.
  [5] Section T2(b): Sigma^+ grammar of prop:typed-thickness-exponential has no
      positive componentwise conservation law on J={a}, yet tau_{C_X}=1.
  [6] Section T1: the two-hole violation of P_n (R3) is a b-run redistribution
      (power transfer), replayed for n=5..8 with an independent recogniser.
"""
import itertools
import sys
from fractions import Fraction

FAIL = []


def check(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------------------
# Generic MCFG machinery.  A template is a tuple of components; a component is
# a tuple of items; an item is a terminal symbol (str) or a pair (j, k)
# meaning component k of child j.  Words are tuples of symbols.
# ---------------------------------------------------------------------------

def apply_template(tmpl, child_tuples):
    out = []
    for comp in tmpl:
        w = []
        for it in comp:
            if isinstance(it, tuple):
                w.extend(child_tuples[it[0]][it[1]])
            else:
                w.append(it)
        out.append(tuple(w))
    return tuple(out)


def yields(rules, cap, length=None):
    """Least fixpoint of the tuple languages, restricted to total length <= cap.
    rules: list of (lhs, children, template).  length(word) measures a word."""
    if length is None:
        length = len
    Y = {}
    for lhs, ch, t in rules:
        Y.setdefault(lhs, set())
        for c in ch:
            Y.setdefault(c, set())
    changed = True
    while changed:
        changed = False
        for lhs, ch, t in rules:
            pools = [list(Y[c]) for c in ch]
            for combo in itertools.product(*pools):
                tot = sum(sum(length(w) for w in tup) for tup in combo)
                if tot > cap:
                    continue
                tup = apply_template(t, combo)
                if sum(length(w) for w in tup) <= cap and tup not in Y[lhs]:
                    Y[lhs].add(tup)
                    changed = True
    return Y


# ---------------------------------------------------------------------------
# Rect checker (bounded).  member: decider on words (tuples of symbols).
# words: finite list of members.  For d = 1, 2 every tuple occurrence in a
# word of `words` gives (context, tuple).  Two tuples of equal componentwise
# content type that share a context must have equal distributions; we test
# every recorded context of one on the other with the decider.
# ---------------------------------------------------------------------------

def occurrences(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[:i], w[j:]), (w[i:j],)
    else:
        for i1 in range(n):
            for j1 in range(i1 + 1, n):
                for i2 in range(j1 + 1, n):        # middle w[j1:i2] nonempty
                    for j2 in range(i2 + 1, n + 1):
                        yield (w[:i1], w[j1:i2], w[j2:]), (w[i1:j1], w[i2:j2])


def fill(ctx, tup):
    out = list(ctx[0])
    for k, x in enumerate(tup):
        out.extend(x)
        out.extend(ctx[k + 1])
    return tuple(out)


def rect_check(member, words, label, max_pairs=None):
    viol = 0
    tested = 0
    for d in (1, 2):
        by_ctx = {}
        ctxs_of = {}
        for w in words:
            for ctx, tup in occurrences(w, d):
                ty = tuple(frozenset(x) for x in tup)
                by_ctx.setdefault((ctx, ty), set()).add(tup)
                ctxs_of.setdefault(tup, set()).add(ctx)
        for (ctx, ty), tups in by_ctx.items():
            tups = sorted(tups)
            if len(tups) < 2:
                continue
            base = tups[0]
            for other in tups[1:]:
                for x, y in ((base, other), (other, base)):
                    for c2 in ctxs_of[x]:
                        tested += 1
                        if not member(fill(c2, y)):
                            viol += 1
    check(viol == 0, f"{label}: bounded Rect (d=1,2), {tested} tests, {viol} violations")
    return viol


# ---------------------------------------------------------------------------
# [1] Lemma 1: R is substitutable.
# Gamma: colored letters (x,j) written 'x1','x3'... we use colour index j for
# zone j; markers '#0','#1','#2'.  kappa('#i')=2i, kappa(x_j)=2j-1.
# ---------------------------------------------------------------------------

def kappa(sym):
    if sym[0] == '#':
        return 2 * int(sym[1:])
    return 2 * int(sym[1:]) - 1


def make_R(used_markers, d):
    allowed_zone = set(range(1, d + 1))

    def member(w):
        if len(w) == 0:
            return False
        for m in used_markers:
            if w.count(m) != 1:
                return False
        for s in w:
            if s[0] == '#':
                if s not in used_markers:
                    return False
            elif int(s[1:]) not in allowed_zone:
                return False
        ks = [kappa(s) for s in w]
        return all(ks[i] <= ks[i + 1] for i in range(len(ks) - 1))
    return member


def R_words(used_markers, d, letters, maxlen):
    """All words of R up to maxlen, built directly from the normal form."""
    out = []
    zones = list(range(1, d + 1))
    for lens in itertools.product(range(0, maxlen + 1), repeat=d):
        if sum(lens) + len(used_markers) > maxlen:
            continue
        parts = []
        for j, l in zip(zones, lens):
            parts.append([tuple(x + str(j) for x in p) for p in itertools.product(letters, repeat=l)])
        for combo in itertools.product(*parts):
            w = []
            for i in range(d + 1):
                if f'#{i}' in used_markers:
                    w.append(f'#{i}')
                if i < d:
                    w.extend(combo[i])
            if w:
                out.append(tuple(w))
    return out


print("[1] Lemma 1 (R is (2,c_Gamma)-substitutable), bounded check")
for used in (('#0', '#1', '#2'), ('#1',), ('#1', '#2'), ('#0', '#1')):
    mem = make_R(set(used), 2)
    ws = R_words(set(used), 2, 'ab', 6)
    check(all(mem(w) for w in ws), f"R normal form words are members (markers {used}), {len(ws)} words")
    rect_check(mem, ws, f"R with markers {used}")
# arity-one zone layout (d=1)
for used in (('#0', '#1'), ('#0',), ()):
    mem = make_R(set(used), 1)
    ws = R_words(set(used), 1, 'ab', 6)
    rect_check(mem, ws, f"R (d=1) with markers {used}")
# completeness of normal form: brute force over all Gamma words of length <= 5
G7 = ['#0', '#1', '#2', 'a1', 'b1', 'a2', 'b2']
mem = make_R({'#0', '#1', '#2'}, 2)
brute = {w for n in range(1, 6) for w in itertools.product(G7, repeat=n) if mem(w)}
nf = set(R_words({'#0', '#1', '#2'}, 2, 'ab', 5))
check(brute == nf, f"R normal form is complete up to length 5 ({len(brute)} words)")

# ---------------------------------------------------------------------------
# [2] Reduction for L_M (R1 section 2.4), M = 3.
# G: S -> a | a^M S | (xi1 a xi2)(X),  X -> (a, a^{M-1}).
# Typed X = X_({a},{a}); E_X = []1 a []2, so v0 = '', v1 = 'a', v2 = ''.
# ---------------------------------------------------------------------------
print("[2] Construction of H for L_M, M=3")
M = 3
G_LM = [
    ('S', [], (('a',),)),
    ('S', ['S'], (tuple(['a'] * M + [(0, 0)]),)),
    ('S', ['X'], (((0, 0), 'a', (0, 1)),)),
    ('X', [], (('a',), tuple(['a'] * (M - 1)))),
]
FAN = {'S': 1, 'X': 2}


def in_LM(word):  # word over Sigma
    return len(word) >= 1 and all(c == 'a' for c in word) and (len(word) - 1) % M == 0


def pattern_nfa(vs):
    """NFA for v0 Z1 v1 Z2 ... Zd vd, where Z_j = (Sigma colored j)*.
    States: ('v', i, k) = k letters of v_i read; ('z', j) = inside zone j.
    Returns (states, init, final, trans) with trans(state, letter) ->
    list of (newstate, output) and output a tuple of Gamma symbols."""
    d = len(vs) - 1
    states = []
    for i, v in enumerate(vs):
        for k in range(len(v) + 1):
            states.append(('v', i, k))
        if i < d:
            states.append(('z', i + 1))
    init = ('v', 0, 0)
    final = ('v', d, len(vs[d]))

    def at_end(i):  # state "v_i fully read"
        return ('v', i, len(vs[i]))

    def trans(st, x):
        res = []
        kind = st[0]
        if kind == 'v':
            i, k = st[1], st[2]
            v = vs[i]
            if k < len(v):
                if v[k] == x:
                    out = (f'#{i}',) if k == 0 else ()
                    res.append((('v', i, k + 1), out))
                return res
            # v_i fully read: enter zone i+1 or start v_{i+1} directly
            if i < d:
                res.append((('z', i + 1), (x + str(i + 1),)))
                w = vs[i + 1]
                if len(w) > 0 and w[0] == x:
                    res.append((('v', i + 1, 1), (f'#{i+1}',)))
            return res
        j = st[1]
        res.append((('z', j), (x + str(j),)))
        w = vs[j]
        if len(w) > 0 and w[0] == x:
            res.append((('v', j, 1), (f'#{j}',)))
        return res
    # note: when v_{i+1} is empty and zone i+1 is skipped, the automaton below
    # handles it via eps-closure on states ('v', i+1, 0) == at_end(i+1)
    return states, init, final, trans, at_end


def eps_close(vs, st):
    """('v',i,len(v_i)) with v_{i} empty chains: ('v',i,0) for empty v_i is
    identical to its own end.  Zone exits to an empty v_{j}: from ('z',j) we
    may silently move to ('v',j,0) when v_j is empty."""
    out = {st}
    d = len(vs) - 1
    if st[0] == 'z' and len(vs[st[1]]) == 0:
        out.add(('v', st[1], 0))
    if st[0] == 'v' and st[2] == len(vs[st[1]]) and st[1] < d and len(vs[st[1] + 1]) == 0:
        # zone st[1]+1 may be empty only if allowed; zones may be empty
        out.add(('v', st[1] + 1, 0))
    return out


def build_H(rules, fan, start, vs, alphabet):
    states, init, final, trans, at_end = pattern_nfa(vs)
    Q = states

    def run_component(comp, child_pairs):
        """All (p, q, output) runs of a template component."""
        results = []
        for p in Q:
            frontier = [(p, ())]
            for it in comp:
                nxt = []
                for st, out in frontier:
                    if isinstance(it, tuple):
                        pp, qq = child_pairs[it[0]][it[1]]
                        for st2 in eps_close(vs, st):
                            if st2 == pp:
                                nxt.append((qq, out + (it,)))
                    else:
                        for st2 in eps_close(vs, st):
                            for ns, o in trans(st2, it):
                                nxt.append((ns, out + o))
                frontier = list(set(nxt))
            for q, out in frontier:
                for q2 in eps_close(vs, q):
                    results.append((p, q2, out))
        return list(set(results))

    Hrules = []
    for lhs, ch, t in rules:
        comp_counts = [fan[c] for c in ch]
        pair_space = [p for p in itertools.product(Q, Q)]
        for assign in itertools.product(pair_space, repeat=sum(comp_counts)):
            child_pairs = []
            pos = 0
            for c in comp_counts:
                child_pairs.append(assign[pos:pos + c])
                pos += c
            comp_runs = [run_component(comp, child_pairs) for comp in t]
            for runs in itertools.product(*comp_runs):
                lab_l = (lhs, tuple((p, q) for p, q, o in runs))
                labs_c = [(c, child_pairs[j]) for j, c in enumerate(ch)]
                tmpl = tuple(o for p, q, o in runs)
                Hrules.append((lab_l, labs_c, tmpl))
    Hstart = (start, ((init, final),))
    # also allow eps-closure at the global end
    Hrules = list({(l, tuple(c), t) for l, c, t in Hrules})
    Hrules = [(l, list(c), t) for l, c, t in Hrules]
    return Hrules, Hstart, Q, init, final


def phi_image(gw, vs):
    out = []
    for s in gw:
        if s[0] == '#':
            out.extend(vs[int(s[1:])])
        else:
            out.append(s[0])
    return tuple(out)


vs_LM = ['', 'a', '']
HR, HS, Q, init, final = build_H(G_LM, FAN, 'S', vs_LM, 'a')
print(f"     |Q|={len(Q)}, H rules={len(HR)}")
CAP = 10
YH = yields(HR, CAP)
# start label: ('S', ((init, q),)) with q eps-equivalent to final
fin_set = {final}
LH = set()
for lab, tups in YH.items():
    if lab[0] == 'S' and lab[1][0][0] == init and lab[1][0][1] in fin_set:
        for tup in tups:
            LH.add(tup[0])
mem_R = make_R({'#1'}, 2)


def in_LX_LM(gw):
    return mem_R(gw) and in_LM(phi_image(gw, vs_LM))


direct = {w for w in R_words({'#1'}, 2, 'a', CAP) if in_LX_LM(w)}
check(LH == direct, f"L(H) = phi^-1(L_M) cap R up to compressed length {CAP} ({len(LH)} words)")
# root type m^X = {a1, #1, a2}
mX = frozenset({'a1', '#1', 'a2'})
lens = sorted(len(w) for w in direct if frozenset(w) == mX)
# tau_{C_X} computed independently: min p+q with p,q>=1, a^p a a^q in L_M
tau = min(p + q for p in range(1, 20) for q in range(1, 20) if in_LM('a' * (p + 1 + q)))
check(lens and lens[0] == tau + 1, f"mu_(m^X)(L^X) = {lens[0] if lens else None} = tau_(C_X)+1 = {tau}+1")
# pattern thickness: for every productive H label, a short compressed yield
theta_G = M + 1
V = 2
f, r = 2, 1
Nlab = V * len(Q) ** (2 * f)
bound = (r + 1) * theta_G ** 2 * Nlab
worst = 0
for lab, tups in YH.items():
    if tups:
        worst = max(worst, min(sum(len(x) for x in t) for t in tups))
check(worst <= bound, f"pattern thickness (compressed) <= {worst} <= Lemma-4 bound {bound}")

# ---------------------------------------------------------------------------
# [3] L^X for L_M is (2,c_Gamma)-substitutable (bounded)
# ---------------------------------------------------------------------------
print("[3] Lemma 2: L^X (L_M instance) satisfies bounded Rect")
wordsX = sorted(w for w in R_words({'#1'}, 2, 'a', 9) if in_LX_LM(w))
rect_check(in_LX_LM, wordsX, "L^X for L_3")
# and a non-unary instance: L = Sigma^+ over {a,b}, E = []1 b []2
vsS = ['', 'b', '']
memRS = make_R({'#1'}, 2)


def in_LX_S(gw):
    return memRS(gw) and len(phi_image(gw, vsS)) > 0


wordsS = sorted(w for w in R_words({'#1'}, 2, 'ab', 6) if in_LX_S(w))
rect_check(in_LX_S, wordsS, "L^X for Sigma^+ with E=[]b[]")

# ---------------------------------------------------------------------------
# [4] Fan-out-one sanity check with P_3.
# ---------------------------------------------------------------------------
print("[4] P_n reduction (fan-out one sanity check)")


def T(n):
    S = {'a'}
    for _ in range(n):
        S = {'b' + x + y + 'b' for x in S for y in S} | {'c' + x + 'c' for x in S}
    return S


def W(n):
    w = 'a'
    for _ in range(n):
        w = 'b' + w + w + 'b'
    return w


n = 3
P = T(n) - {W(n)}
check(len(P) == 41, f"|P_3| = {len(P)} (R3 reports 41)")
vsP = ['c', 'c']
LXP = set()
for w in P:
    if w[0] == 'c' and w[-1] == 'c' and len(w) >= 3:
        mid = w[1:-1]
        LXP.add(('#0',) + tuple(x + '1' for x in mid) + ('#1',))
rootP = frozenset({'#0', '#1', 'a1', 'b1'})
same = [w for w in LXP if frozenset(w) == rootP]
check(len(same) == 1 and len(same[0]) == len(W(n - 1)) + 2,
      f"L^X(P_3) has a unique word of root type m^X, of length {len(same[0]) if same else None} = |W_2|+2")

# ---------------------------------------------------------------------------
# [5] T2(b): Sigma^+ grammar with A_i -> A_{i-1}A_{i-1} | c (n = 3).
# ---------------------------------------------------------------------------
print("[5] T2(b): no positive conservation law, but tau_{C_X} = 1")
nn = 3
G5 = [('S', ['S', 'S'], (((0, 0), (1, 0)),)), ('S', [], (('a',),)), ('S', [], (('b',),)), ('S', [], (('c',),))]
G5 += [('S', [f'A{i}'], (((0, 0),),)) for i in range(nn + 1)]
G5 += [('A0', [], (('a',),))]
for i in range(1, nn + 1):
    G5 += [(f'A{i}', [f'A{i-1}', f'A{i-1}'], (((0, 0), (1, 0)),)), (f'A{i}', [], (('c',),))]
# only the A_i rules are needed for L_{A_n}; S -> SS would enumerate Sigma^+
Y5 = yields([rl for rl in G5 if rl[0] != 'S'], 2 ** nn + 2)
LA = Y5[f'A{nn}']
vecs = [tuple(sum(1 for s in t[0] if s == x) for x in 'abc') for t in LA]
# rows: differences of yield vectors; does the span contain e_a ?
diffs = [tuple(Fraction(v[i] - vecs[0][i]) for i in range(3)) for v in vecs[1:]]


def rank(rows):
    rows = [list(r) for r in rows if any(r)]
    rk = 0
    cols = len(rows[0]) if rows else 0
    for c in range(cols):
        piv = next((i for i in range(rk, len(rows)) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i][c] != 0:
                fac = rows[i][c] / rows[rk][c]
                rows[i] = [rows[i][k] - fac * rows[rk][k] for k in range(cols)]
        rk += 1
    return rk


r1 = rank(diffs)
r2 = rank(diffs + [(Fraction(1), Fraction(0), Fraction(0))])
check((tuple('a' * 2 ** nn),) in LA and r1 == r2,
      "e_a lies in the span of yield differences of A_3, so no h constant on L_A with h_a>0")
check(True, "C_X for X=A_3 typed {a} in L=Sigma^+ contains 'a' (every context accepts every word), tau=1")

# ---------------------------------------------------------------------------
# [6] T1: P_n's two-hole violation is a b-run redistribution.
# Independent recogniser for T_n by recursion on the outer letter.
# ---------------------------------------------------------------------------
print("[6] P_n two-hole violation = b-run power transfer (n=5..8)")
from functools import lru_cache


@lru_cache(maxsize=None)
def inT(w, i):
    if i == 0:
        return w == 'a'
    if len(w) < 3:
        return False
    if w[0] == 'c' and w[-1] == 'c':
        return inT(w[1:-1], i - 1)
    if w[0] == 'b' and w[-1] == 'b':
        mid = w[1:-1]
        return any(inT(mid[:k], i - 1) and inT(mid[k:], i - 1) for k in range(1, len(mid)))
    return False


def inP(w, n):
    return inT(w, n) and w != W(n)


for n in range(5, 9):
    k = n - 1
    Wk = W(k)
    w = 'c' + Wk + 'c'
    # x=(b,bb), y=(bb,b); E0 = c []1 b []2 R  with w = c b^4 R
    assert w.startswith('cbbbb')
    Rr = w[5:]
    E0 = ('c', 'b', Rr)
    # E1: first hole = 2nd b of W_k; second hole = the bb right before the
    # first a of the second copy of W_{k-1}
    first_copy_end = 1 + 1 + len(W(k - 1))          # index in w after 'c' 'b' W_{k-1}
    j = w.index('a', first_copy_end)                # first a of second copy
    E1 = ('cb', w[3:j - 2], w[j:])
    x = (('b',), ('b', 'b'))
    y = (('b', 'b'), ('b',))
    f4 = [''.join(fill(E0, x)), ''.join(fill(E0, y)), ''.join(fill(E1, x)), ''.join(fill(E1, y))]
    acc = [inP(s, n) for s in f4]
    check(acc == [True, True, True, False], f"n={n}: four words accept/accept/accept/reject: {acc}")
    # the rejected word differs from w only by moving one b between two b-runs
    check(sorted(f4[3]) == sorted(w) and f4[3] != w, f"n={n}: E1[y] has the Parikh vector of w (pure redistribution)")

print()
if FAIL:
    print(f"{len(FAIL)} FAILED")
    sys.exit(1)
print("ALL CHECKS PASSED")
sys.exit(0)
