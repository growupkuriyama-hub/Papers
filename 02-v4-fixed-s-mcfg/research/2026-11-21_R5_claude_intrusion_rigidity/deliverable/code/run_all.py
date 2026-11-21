#!/usr/bin/env python3
"""R5 finite checks (Python 3, standard library only, no network).

Run:  python3 -I run_all.py      (exit code 0 iff every check passes)

[T0]  Theorem 0.1 / 0.2 / Lemma 0.3 on random reduced good MCFGs (fan-out <= 2,
      rank <= 2, 3 and 4 letters) and on two structured families.  These statements
      use no substitutability, so they can be tested on arbitrary grammars.
      CERTIFIED FINITE only: no universal claim is proved by this code.
[T1]  Explicit SUB-certificates (Theorems B0, B1, B3) for ten escape designs of
      the doubling backbone A_0 -> ab, A_i -> A_{i-1}A_{i-1} | e_i, S -> A_m,
      for m = 6, 7.  Every premise is decided by an exact membership test in
      the grammar; every step is replayed by an independent checker (nonempty
      fillers, nonempty middle of two-hole contexts, componentwise content).
[B4]  Brute-force sanity check of the lacunary-chain bound for affine values.
"""
import itertools
import math
import random
import sys
from functools import lru_cache

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print('FAIL:', msg)
    return cond


# ---------------------------------------------------------------------------
# MCFG representation.  A rule is (A, children, comps); comps is a tuple of
# components; a component is a tuple of symbols; a symbol is a terminal (str of
# length 1) or a variable (j, k): component k of child j (0-based).
# ---------------------------------------------------------------------------

def is_good(fan, rules):
    for (A, ch, comps) in rules:
        if len(comps) != fan[A]:
            return False
        if any(len(c) == 0 for c in comps):          # eps-free
            return False
        seq = [s for c in comps for s in c]
        vars_ = [s for s in seq if not isinstance(s, str)]
        need = [(j, k) for j, B in enumerate(ch) for k in range(fan[B])]
        if sorted(vars_) != sorted(need) or len(vars_) != len(set(vars_)):
            return False                             # nondeleting, linear
        for j, B in enumerate(ch):                   # nonpermuting
            order = [s[1] for s in seq if not isinstance(s, str) and s[0] == j]
            if order != sorted(order):
                return False
        for c in comps:                              # nonmerging
            for s, t in zip(c, c[1:]):
                if (not isinstance(s, str) and not isinstance(t, str)
                        and s[0] == t[0] and t[1] == s[1] + 1):
                    return False
    return True


def reduce_grammar(fan, rules, start='S'):
    prod = set()
    changed = True
    while changed:
        changed = False
        for (A, ch, comps) in rules:
            if A not in prod and all(B in prod for B in ch):
                prod.add(A)
                changed = True
    if start not in prod:
        return None
    rules = [r for r in rules if r[0] in prod and all(B in prod for B in r[1])]
    reach = {start}
    changed = True
    while changed:
        changed = False
        for (A, ch, comps) in rules:
            if A in reach:
                for B in ch:
                    if B not in reach:
                        reach.add(B)
                        changed = True
    rules = [r for r in rules if r[0] in reach]
    fan2 = {A: fan[A] for A in reach}
    return fan2, rules


def letter_bits(sigma):
    return {x: 1 << i for i, x in enumerate(sigma)}


def typed_dp(fan, rules, sigma):
    """best[(A, ct)] = (length, nodes, rule_index, child_states); lexicographic
    minimum over derivations from A whose componentwise content tuple is ct."""
    bit = letter_bits(sigma)
    best = {}
    changed = True
    while changed:
        changed = False
        by_nt = {}
        for (A, ct), val in best.items():
            by_nt.setdefault(A, []).append((ct, val[0], val[1]))
        for ri, (A, ch, comps) in enumerate(rules):
            lists = [by_nt.get(B, []) for B in ch]
            if any(len(l) == 0 for l in lists):
                continue
            for combo in itertools.product(*lists):
                length = 0
                nodes = 1
                for (_, l, n) in combo:
                    length += l
                    nodes += n
                ct = []
                for c in comps:
                    mask = 0
                    for s in c:
                        if isinstance(s, str):
                            mask |= bit[s]
                            length += 1
                        else:
                            mask |= combo[s[0]][0][s[1]]
                    ct.append(mask)
                key = (A, tuple(ct))
                cand = (length, nodes, ri, tuple((ch[j], combo[j][0]) for j in range(len(ch))))
                old = best.get(key)
                if old is None or (cand[0], cand[1]) < (old[0], old[1]):
                    best[key] = cand
                    changed = True
    return best


def build_tree(best, rules, state):
    length, nodes, ri, kids = best[state]
    A, ch, comps = rules[ri]
    children = [build_tree(best, rules, k) for k in kids]
    yield_ = []
    for c in comps:
        out = []
        for s in c:
            if isinstance(s, str):
                out.append(s)
            else:
                out.append(children[s[0]]['yield'][s[1]])
        yield_.append(''.join(out))
    node = {'nt': A, 'ct': state[1], 'yield': tuple(yield_),
            'len': sum(len(y) for y in yield_), 'children': children,
            'rule_terms': sum(1 for c in comps for s in c if isinstance(s, str))}
    return node


def inside_outside_theta(fan, rules):
    INF = float('inf')
    ins = {A: INF for A in fan}
    changed = True
    while changed:
        changed = False
        for (A, ch, comps) in rules:
            t = sum(1 for c in comps for s in c if isinstance(s, str))
            v = t + sum(ins[B] for B in ch)
            if v < ins[A]:
                ins[A] = v
                changed = True
    out = {A: INF for A in fan}
    out['S'] = 0
    changed = True
    while changed:
        changed = False
        for (A, ch, comps) in rules:
            if out[A] == INF:
                continue
            t = sum(1 for c in comps for s in c if isinstance(s, str))
            tot = t + sum(ins[B] for B in ch)
            for j, B in enumerate(ch):
                v = out[A] + tot - ins[B]
                if v < out[B]:
                    out[B] = v
                    changed = True
    theta = 0
    for (A, ch, comps) in rules:
        t = sum(1 for c in comps for s in c if isinstance(s, str))
        theta = max(theta, out[A] + t + sum(ins[B] for B in ch))
    return ins, out, max(1, theta)


def all_nodes(root):
    stack = [root]
    res = []
    while stack:
        u = stack.pop()
        res.append(u)
        stack.extend(u['children'])
    return res


def max_antichain(root, pred):
    def f(u):
        s = sum(f(c) for c in u['children'])
        return max(1 if pred(u) else 0, s)
    return f(root)


def height(root):
    if not root['children']:
        return 1
    return 1 + max(height(c) for c in root['children'])


def t0_check_instance(fan, rules, sigma, label, stats):
    """Check Theorem 0.1, 0.2 and Lemma 0.3 for every realized root type m."""
    bit = letter_bits(sigma)
    full = (1 << len(sigma)) - 1
    best = typed_dp(fan, rules, sigma)
    ins, out, theta = inside_outside_theta(fan, rules)
    v = len(fan)
    r = max(1, max(len(ch) for (_, ch, _) in rules))
    roots = [st for st in best if st[0] == 'S']
    for st in roots:
        m = st[1][0]
        msize = bin(m).count('1')
        T = build_tree(best, rules, st)
        W = T['yield'][0]
        mu = len(W)
        cnt_W = {x: W.count(x) for x in sigma}

        def minlen_m(B):
            vals = [val[0] for (A2, ct), val in best.items()
                    if A2 == B and all((c & ~m) == 0 for c in ct)]
            return min(vals) if vals else float('inf')

        cache = {}
        nodes = all_nodes(T)
        for u in nodes:
            ys = ''.join(u['yield'])
            u['hold'] = tuple(ys.count(x) == cnt_W[x] and cnt_W[x] > 0
                              for x in sigma if bit[x] & m)
            u['holder'] = any(u['hold'])
            B = u['nt']
            if B not in cache:
                cache[B] = minlen_m(B)
            u['minm'] = cache[B]
            u['heavy'] = u['len'] > theta
            u['forced'] = u['heavy'] and u['minm'] >= u['len']
            u['intr'] = u['heavy'] and u['minm'] > theta
        # Lemma 0.1(i): heavy => forced or holder
        for u in nodes:
            if u['heavy'] and not (u['forced'] or u['holder']):
                check(False, '%s: heavy node neither forced nor holder' % label)
        if m == full:
            check(not any(u['forced'] for u in nodes), '%s: forced node for m=Sigma' % label)
        # holders lie on chains: each x-holder set is ancestor-closed and a chain
        def holder_paths_ok(u, idx):
            hs = [c for c in u['children'] if c['hold'][idx]]
            if len(hs) > 1:
                return False
            return all(holder_paths_ok(c, idx) for c in u['children'])
        for idx in range(msize):
            check(holder_paths_ok(T, idx), '%s: holders not a chain' % label)
        # path length bound (|m|+1) v
        check(height(T) <= (msize + 1) * v, '%s: height %d > (|m|+1)v' % (label, height(T)))
        # Lemma 0.3: below a non-holder, every heavy node is forced; no repeated
        # nonterminal on a path inside a non-holder subtree
        def below_nonholder(u, inside, seen):
            ok = True
            if inside and u['heavy'] and not u['forced']:
                ok = False
            if inside:
                if u['nt'] in seen:
                    ok = False
                seen = seen | {u['nt']}
            inside2 = inside or not u['holder']
            if inside2 and not inside:
                seen = {u['nt']}
            for c in u['children']:
                ok = below_nonholder(c, inside2, seen) and ok
            return ok
        check(below_nonholder(T, False, frozenset()), '%s: Lemma 0.3 failed' % label)
        q = max_antichain(T, lambda u: u['forced'])
        qi = max_antichain(T, lambda u: u['intr'])
        lam = max([theta] + [u['len'] for u in nodes if u['forced']])
        b1 = (r + 1) * (msize + 1) * v * theta * (q + msize)
        b1i = (r + 1) * (msize + 1) * v * theta * (qi + msize)
        b2 = msize * (msize + 1) * v * (theta + r * lam)
        check(mu <= b1, '%s: mu=%d > Thm0.1 bound %d' % (label, mu, b1))
        check(mu <= b1i, '%s: mu=%d > Thm0.1 (intrusion) bound %d' % (label, mu, b1i))
        check(mu <= b2, '%s: mu=%d > Thm0.2 bound %d' % (label, mu, b2))
        check(q * (theta + 1) <= mu and qi * (theta + 1) <= mu, '%s: width converse' % label)
        check(qi >= q, '%s: intrusion width < forced width' % label)
        stats['types'] += 1
        stats['maxmu'] = max(stats['maxmu'], mu)
        stats['maxq'] = max(stats['maxq'], q)
        if any(u['forced'] for u in nodes):
            stats['with_forced'] += 1
        if any(u['forced'] and len(u['yield']) == 2 for u in nodes):
            stats['fo2_forced'] += 1
        stats['ratio1'] = max(stats['ratio1'], mu / b1)
        stats['ratio2'] = max(stats['ratio2'], mu / b2)
    return len(roots)


def random_template(rng, d0, child_fans, sigma):
    seqs = [[(j, k) for k in range(f)] for j, f in enumerate(child_fans)]
    merged = []
    ptr = [0] * len(seqs)
    total = sum(len(s) for s in seqs)
    while len(merged) < total:
        j = rng.choice([i for i in range(len(seqs)) if ptr[i] < len(seqs[i])])
        merged.append(seqs[j][ptr[j]])
        ptr[j] += 1
    nterm = rng.randint(0, 2)
    if len(merged) + nterm < d0:
        nterm = d0 - len(merged)
    for _ in range(nterm):
        pos = rng.randint(0, len(merged))
        merged.insert(pos, rng.choice(sigma))
    if len(merged) < d0:
        return None
    cuts = sorted(rng.sample(range(1, len(merged)), d0 - 1)) if d0 > 1 else []
    comps = []
    prev = 0
    for c in cuts + [len(merged)]:
        comps.append(tuple(merged[prev:c]))
        prev = c
    return tuple(comps)


def random_grammar(rng, sigma, nnt, fan2p):
    nts = ['S'] + ['N%d' % i for i in range(nnt)]
    fan = {'S': 1}
    for A in nts[1:]:
        fan[A] = 2 if rng.random() < fan2p else 1
    rules = []
    for A in nts:
        for _ in range(rng.randint(1, 3)):
            k = rng.choice([0, 1, 2, 2])
            ch = [rng.choice(nts[1:]) for _ in range(k)]
            for _try in range(20):
                t = random_template(rng, fan[A], [fan[B] for B in ch], sigma)
                if t is not None and is_good(fan, [(A, ch, t)]):
                    rules.append((A, ch, t))
                    break
        # a constant rule so that A is productive
        word = ''.join(rng.choice(sigma) for _ in range(fan[A] + rng.randint(0, 1)))
        cuts = sorted(rng.sample(range(1, len(word)), fan[A] - 1)) if fan[A] > 1 else []
        comps, prev = [], 0
        for c in cuts + [len(word)]:
            comps.append(tuple(word[prev:c]))
            prev = c
        rules.append((A, [], tuple(comps)))
    red = reduce_grammar(fan, rules)
    if red is None:
        return None
    fan, rules = red
    assert is_good(fan, rules)
    return fan, rules


def random_layered(rng, sigma, depth):
    """Random layered doubling grammars with short escapes: levels 0..depth, each
    level has 1-2 'pure' rules over m-letters and 1-2 escape rules that write a
    forbidden letter.  Fan-out of each level is 1 or 2 at random."""
    mletters = sigma[:2]
    forb = sigma[2:]
    fan = {'S': 1}
    rules = []
    for i in range(depth + 1):
        A = 'L%d' % i
        fan[A] = 1 if (i == depth or rng.random() < 0.6) else 2
    for i in range(depth + 1):
        A = 'L%d' % i
        d = fan[A]
        if i == 0:
            for _ in range(rng.randint(1, 2)):
                w = ''.join(rng.choice(mletters) for _ in range(d + rng.randint(0, 2)))
                cuts = sorted(rng.sample(range(1, len(w)), d - 1)) if d > 1 else []
                comps, prev = [], 0
                for c in cuts + [len(w)]:
                    comps.append(tuple(w[prev:c]))
                    prev = c
                rules.append((A, [], tuple(comps)))
        else:
            B = 'L%d' % (i - 1)
            npure = 0
            for _try in range(40):
                k = rng.choice([2, 2, 3])
                ch = [B] * k
                t = random_template(rng, d, [fan[B]] * k, mletters)
                if t is not None and is_good(fan, [(A, ch, t)]):
                    rules.append((A, ch, t))
                    npure += 1
                    if npure >= rng.randint(1, 2):
                        break
            for _ in range(rng.randint(1, 2)):
                if rng.random() < 0.5:
                    w = ''.join(rng.choice(sigma) for _ in range(d + rng.randint(0, 2)))
                    if not any(x in w for x in forb):
                        w = w[:-1] + rng.choice(forb)
                    cuts = sorted(rng.sample(range(1, len(w)), d - 1)) if d > 1 else []
                    comps, prev = [], 0
                    for c in cuts + [len(w)]:
                        comps.append(tuple(w[prev:c]))
                        prev = c
                    rules.append((A, [], tuple(comps)))
                else:
                    for _try in range(20):
                        t = random_template(rng, d, [fan[B]], list(forb))
                        if t is not None and is_good(fan, [(A, [B], t)]) and \
                                any(isinstance(s, str) for c in t for s in c):
                            rules.append((A, [B], t))
                            break
    top = 'L%d' % depth
    rules.append(('S', [top], (((0, 0), mletters[0]),)))
    rules.append(('S', [], (tuple(mletters[0] * 2),)))
    red = reduce_grammar(fan, rules)
    if red is None:
        return None
    fan, rules = red
    if not is_good(fan, rules):
        return None
    return fan, rules


def family_intrusion_fanout1(n):
    """Example 5.1 of chatgpt_intrusion_2026-11-04 (outside C_{2,c}; T0 needs no
    substitutability)."""
    fan = {'S': 1}
    rules = [('S', ['A%d' % n], (((0, 0), 'b'),)), ('S', [], (tuple('aaaa'),)),
             ('S', [], (tuple('bbbb'),)), ('S', [], (tuple('cccc'),)),
             ('A0', [], (('a',),)), ('A0', [], (('c',),))]
    fan['A0'] = 1
    for i in range(1, n + 1):
        fan['A%d' % i] = 1
        rules.append(('A%d' % i, ['A%d' % (i - 1), 'A%d' % (i - 1)], (((0, 0), (1, 0)),)))
        rules.append(('A%d' % i, [], (('c',),)))
    return fan, rules


def family_slot_fanout2(n):
    """Candidate (a) of chatgpt_negative_design_2026-11-06 (fan-out 2)."""
    fan = {'S': 1, 'D0': 1}
    rules = [('D0', [], (tuple('ab'),))]
    for i in range(1, n + 1):
        fan['D%d' % i] = 1
        rules.append(('D%d' % i, ['D%d' % (i - 1), 'D%d' % (i - 1)], (((0, 0), (1, 0)),)))
        rules.append(('D%d' % i, [], (tuple('a' * i + 'cb'),)))
    fan['A1'] = 2
    rules.append(('A1', [], (tuple('ab'), tuple('ab'))))
    for i in range(2, n + 1):
        fan['A%d' % i] = 2
        D, A = 'D%d' % (i - 1), 'A%d' % (i - 1)
        rules.append(('A%d' % i, [D, A], (((0, 0), (1, 0)), ((1, 1),))))
        rules.append(('A%d' % i, [A, D], (((0, 0),), ((0, 1), (1, 0)))))
        rules.append(('A%d' % i, [D, D], (((0, 0),), ((1, 0),))))
    rules.append(('S', ['D%d' % n], (((0, 0), 'a', 'b'),)))
    rules.append(('S', ['A%d' % n], (((0, 0), 'c', (0, 1)),)))
    assert is_good(fan, rules)
    return fan, rules


def run_t0():
    print('=== [T0] reduction to intrusion: random and structured grammars ===')
    stats = {'grammars': 0, 'types': 0, 'maxmu': 0, 'maxq': 0, 'with_forced': 0,
             'fo2_forced': 0, 'ratio1': 0.0, 'ratio2': 0.0}
    rng = random.Random(20261121)
    tried = 0
    for sigma in ('abc', 'abcd'):
        count = 0
        while count < (220 if sigma == 'abc' else 80):
            tried += 1
            g = random_grammar(rng, sigma, rng.randint(2, 4), 0.35)
            if g is None:
                continue
            fan, rules = g
            if len(rules) > 18:
                continue
            t0_check_instance(fan, rules, sigma, 'random#%d' % tried, stats)
            stats['grammars'] += 1
            count += 1
    layered = 0
    while layered < 160:
        sigma = 'abc' if layered % 2 == 0 else 'abcd'
        g = random_layered(rng, sigma, rng.randint(2, 5))
        if g is None:
            continue
        fan, rules = g
        t0_check_instance(fan, rules, sigma, 'layered#%d' % layered, stats)
        stats['grammars'] += 1
        layered += 1
    for n in range(2, 9):
        fan, rules = family_intrusion_fanout1(n)
        t0_check_instance(fan, rules, 'abc', 'intrusion-fo1 n=%d' % n, stats)
        stats['grammars'] += 1
    for n in range(2, 5):
        fan, rules = family_slot_fanout2(n)
        t0_check_instance(fan, rules, 'abc', 'slot-fo2 n=%d' % n, stats)
        stats['grammars'] += 1
    print('grammars=%d  realized root types=%d  types with a forced node=%d  '
          'max mu=%d  max forced width q=%d' % (stats['grammars'], stats['types'],
                                                stats['with_forced'], stats['maxmu'], stats['maxq']))
    print('  types with a forced fan-out-2 node=%d; max mu/bound: Thm0.1 %.4f, Thm0.2 %.4f'
          % (stats['fo2_forced'], stats['ratio1'], stats['ratio2']))
    # one explicit line for the structured families
    for n in (4, 8):
        fan, rules = family_intrusion_fanout1(n)
        best = typed_dp(fan, rules, 'abc')
        _, _, theta = inside_outside_theta(fan, rules)
        T = build_tree(best, rules, ('S', (0b011,)))
        print('  intrusion-fo1 n=%d: theta=%d mu_ab=%d' % (n, theta, T['len']))
    for n in (3, 4):
        fan, rules = family_slot_fanout2(n)
        best = typed_dp(fan, rules, 'abc')
        _, _, theta = inside_outside_theta(fan, rules)
        T = build_tree(best, rules, ('S', (0b011,)))
        print('  slot-fo2 n=%d: theta=%d mu_ab=%d' % (n, theta, T['len']))


# ---------------------------------------------------------------------------
# [T1] certificates
# ---------------------------------------------------------------------------

def cont(w):
    return frozenset(w)


def put(E, x):
    return ''.join(E[i] + x[i] for i in range(len(x))) + E[-1]


def replay(seeds, steps):
    known = set(seeds)
    for (E, x, y, F) in steps:
        d = len(x)
        assert d in (1, 2) and len(y) == d and len(E) == d + 1 and len(F) == d + 1
        assert all(len(t) > 0 for t in x) and all(len(t) > 0 for t in y)
        if d == 2:
            assert len(E[1]) > 0 and len(F[1]) > 0, 'empty middle'
        assert all(cont(x[i]) == cont(y[i]) for i in range(d)), 'content mismatch'
        for w in (put(E, x), put(E, y), put(F, x)):
            assert w in known, 'missing premise'
        known.add(put(F, y))
    return known


def make_member(esc):
    m = len(esc)

    @lru_cache(maxsize=None)
    def mem(i, w):
        if i == 0:
            return w == 'ab'
        if w == esc[i - 1]:
            return True
        return any(mem(i - 1, w[:k]) and mem(i - 1, w[k:]) for k in range(1, len(w)))
    return lambda w: mem(m, w)


def find_move(e, f, x0, y0):
    for p in range(len(e) - len(x0) + 1):
        if e[p:p + len(x0)] == x0 and e[:p] + y0 + e[p + len(x0):] == f:
            return e[:p], e[p + len(x0):]
    return None


def slot_step(K, Delta, e, a0, b0, a, b):
    """Theorem B0: z^{a0} e z^{b0} => z^a e z^b (a+b = a0+b0, all >= 1)."""
    z = 'ab'
    E0 = ('', z * Delta, '')
    return (E0, (z * a0, z * b0), (z * a, z * b), ('', e, ''))


def certificate_move(esc, s, sp, x0, y0, K, member):
    """Theorem B3 instance: move x0 -> y0 turns e_s into e_{s+1}; transported
    into the host e_{sp}; compared with the genuine e_{sp+1} by Theorem B1."""
    z = 'ab'
    W = z * K
    D = {i: 2 ** i for i in range(1, len(esc) + 1)}
    e = {i: esc[i - 1] for i in range(1, len(esc) + 1)}
    mv1 = find_move(e[s], e[s + 1], x0, y0)
    mv2 = find_move(e[sp], e[sp + 1], x0, y0)
    assert mv1 is not None and mv2 is not None
    seeds = set()
    steps = []

    def aligned(i):
        p = 2 ** i                      # block position of an interior level-i node
        w = z * p + e[i] + z * (K - p - 2 ** i)
        assert member(w), 'aligned seed not generated'
        seeds.add(w)
        return p, K - p - 2 ** i

    seeds.add(W)
    assert member(W)
    # orientation: forward (x0->y0) if D[s+1] >= D[s], else reverse (y0->x0)
    if D[s + 1] >= D[s]:
        (al_i, be_i), (al_l, be_l) = mv1, mv2
        ei, ej, el = e[s], e[s + 1], e[sp]
        Di, Dj, Dl = D[s], D[s + 1], D[sp]
        xf, yf = x0, y0
        target, Dtarget = e[sp + 1], D[sp + 1]
    else:
        (al_i, be_i), (al_l, be_l) = mv1, mv2
        ei, ej, el = e[s + 1], e[s], e[sp + 1]
        Di, Dj, Dl = D[s + 1], D[s], D[sp + 1]
        xf, yf = y0, x0
        target, Dtarget = e[sp], D[sp]
    k = max(1, 1 + Dj - Di)
    kp = k + Di - Dj
    h = K - Di - k - 1
    hpp = K - Dl - k - 1
    assert min(k, kp, h, hpp) >= 1, 'room condition violated'
    for (word, Dw, a, b) in ((ei, Di, h, k + 1), (ej, Dj, h, kp + 1), (el, Dl, hpp, k + 1)):
        idx = [i for i in e if e[i] == word][0]
        a0, b0 = aligned(idx)
        if (a0, b0) != (a, b):
            steps.append(slot_step(K, Dw, word, a0, b0, a, b))
    E = (z * h + al_i, be_i + z, '')
    F = (z * hpp + al_l, be_l + z, '')
    x = (xf, z * k)
    y = (yf, z * kp)
    assert put(E, x) == z * h + ei + z * (k + 1)
    assert put(E, y) == z * h + ej + z * (kp + 1)
    assert put(F, x) == z * hpp + el + z * (k + 1)
    derived = put(F, y)
    assert derived == z * hpp + target + z * (kp + 1)
    Dstar = K - hpp - (kp + 1)
    assert Dstar == Dl + Dj - Di and Dstar >= 1
    steps.append((E, x, y, F))
    # Theorem B1: two placements of `target`, deficits Dstar and Dtarget
    idx = [i for i in e if e[i] == target][0]
    a1, b1 = aligned(idx)
    plA, plB = (hpp, kp + 1, Dstar), (a1, b1, Dtarget)
    if plA[2] > plB[2]:
        plA, plB = plB, plA
    assert plA[2] != plB[2], 'no inconsistency (deficits agree)'
    E1 = ('', target, '')
    F1 = ('', z * plA[2], '')
    x1 = (z * plA[0], z * plA[1])
    y1 = (z * plB[0], z * plB[1])
    assert put(F1, x1) == W
    steps.append((E1, x1, y1, F1))
    short = put(F1, y1)
    known = replay(seeds, steps)
    assert short in known
    return short, len(steps), Dstar, Dtarget


DESIGNS = [
    ('c^i', lambda i, m: 'c' * i, 'c', 'cc'),
    ('a^(i-1)c', lambda i, m: 'a' * (i - 1) + 'c', 'a', 'aa'),
    ('ca^(i-1)', lambda i, m: 'c' + 'a' * (i - 1), 'a', 'aa'),
    ('cb^(i-1)', lambda i, m: 'c' + 'b' * (i - 1), 'b', 'bb'),
    ('b^(i-1)c', lambda i, m: 'b' * (i - 1) + 'c', 'b', 'bb'),
    ('c(ab)^(i-1)', lambda i, m: 'c' + 'ab' * (i - 1), 'ab', 'abab'),
    ('ac^ib', lambda i, m: 'a' + 'c' * i + 'b', 'c', 'cc'),
    ('a^icb', lambda i, m: 'a' * i + 'cb', 'a', 'aa'),
    ('cd^ic', lambda i, m: 'c' + 'd' * i + 'c', 'd', 'dd'),
    ('one-hot c0^(L-i)10^(i-1)c', lambda i, m: 'c' + '0' * (m + 1 - i) + '1' + '0' * (i - 1) + 'c', '01', '10'),
]


def run_t1():
    print('=== [T1] Theorems B0/B1/B3: replayed shortcut certificates ===')
    for m in (6, 7):
        K = 2 ** m
        for (name, f, x0, y0) in DESIGNS:
            esc = [f(i, m) for i in range(1, m + 1)]
            member = make_member(esc)
            try:
                short, nsteps, Ds, Dt = certificate_move(esc, 2, 3, x0, y0, K, member)
            except AssertionError as ex:
                check(False, 'design %s m=%d: %s' % (name, m, ex))
                continue
            ok = (set(short) == {'a', 'b'} and len(short) < 2 * K and not member(short))
            check(ok, 'design %s m=%d: shortcut word not as expected' % (name, m))
            print('m=%d |W|=%3d  %-28s move %-4s->%-4s  steps=%d  derived deficit %2d vs genuine %2d'
                  '  forced ab-word length %3d  (not in L(G))' %
                  (m, 2 * K, name, x0, y0, nsteps, Ds, Dt, len(short)))
    # Theorem B1 on its own: the word 'c' as escape at two levels (design c(ab)^(i-1))
    m, K = 6, 64
    z = 'ab'
    esc = ['c' + z * (i - 1) for i in range(1, m + 1)]
    member = make_member(esc)
    V2 = z * 4 + esc[1] + z * (K - 4 - 4)       # level-2 escape: word 'c', flanks (4, 61)
    V3 = z * 8 + esc[2] + z * (K - 8 - 8)       # level-3 escape: word 'c', flanks (8, 58)
    assert member(V2) and member(V3) and member(z * K)
    a2, b2 = 4, K - 8 + 1
    a3, b3 = 8, K - 16 + 2
    assert z * a2 + 'c' + z * b2 == V2 and z * a3 + 'c' + z * b3 == V3
    D2, D3 = K - a2 - b2, K - a3 - b3
    step = (('', 'c', ''), (z * a2, z * b2), (z * a3, z * b3), ('', z * D2, ''))
    known = replay({z * K, V2, V3}, [step])
    short = put(step[3], step[2])
    check(short in known and len(short) < 2 * K and set(short) == {'a', 'b'}, 'B1 direct')
    print('B1 direct (word c, deficits %d and %d): forced (ab)^%d, length %d < %d' %
          (D2, D3, len(short) // 2, len(short), 2 * K))
    # Remark: the counterexample of chatgpt_virtual_length 5.3 violates the margin
    # hypothesis of B1 (left flank 0), so no shortcut is claimed there.
    S = {'abab', 'ccab', 'ccababab'}
    print('virtual-length 5.3 example: placements of cc have left flank 0 -> B1 not applicable;'
          ' consistent with H mod 4 having no shortcut')


# ---------------------------------------------------------------------------
# [B4] lacunary chains in affine value sets
# ---------------------------------------------------------------------------

def b4_bound(k, th):
    M = math.floor((math.sqrt(k) * th) ** k)
    G = int(math.floor(math.log2(M))) + 2 if M >= 1 else 2
    return 1 + k * G


def longest_lacunary(vals):
    vals = sorted(set(v for v in vals if v >= 1))
    best = {}
    out = 0
    for v in vals:
        b = 1
        for u in vals:
            if 2 * u > v:
                break
            b = max(b, best[u] + 1)
        best[v] = b
        out = max(out, b)
    return out


def run_b4():
    print('=== [B4] lacunary chains in {A + w.n : n >= 0, |n|_1 <= theta} ===')
    worst = {}
    for k in (1, 2):
        for th in range(2, 7):
            vecs = [n for n in itertools.product(range(th + 1), repeat=k) if sum(n) <= th]
            mx = 0
            rng_w = range(-9, 10) if k == 1 else range(-6, 7)
            for w in itertools.product(rng_w, repeat=k):
                for A in range(-6, 7):
                    vals = [A + sum(wi * ni for wi, ni in zip(w, n)) for n in vecs]
                    mx = max(mx, longest_lacunary(vals))
            bd = b4_bound(k, th)
            check(mx <= bd, 'B4 bound violated k=%d th=%d' % (k, th))
            worst[(k, th)] = (mx, bd)
            print('k=%d theta=%d: longest lacunary chain found %d <= bound %d' % (k, th, mx, bd))


def main():
    run_t0()
    run_t1()
    run_b4()
    if FAIL:
        print('NUMBER OF FAILURES:', len(FAIL))
        sys.exit(1)
    print('ALL CHECKS PASSED (certified finite; no universal claim is proved by this script)')
    sys.exit(0)


if __name__ == '__main__':
    main()
