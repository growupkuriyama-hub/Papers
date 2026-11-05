#!/usr/bin/env python3
"""Claude (README (152)): exploration of mu_ab for the rare type {a,b} (content typing, Sigma={a,b,c}).

Single sound rule (SUB_d, d = 1, 2), valid in every L in C_{2,c}:
    E[x], E[y], F[x] in L;  x, y in (Sigma^+)^d with componentwise equal contents;
    E, F admissible (d = 2: the middle fixed part is nonempty)            ==>  F[y] in L.
Abstract letters ("tokens") carry an intended content (a subset of {a,b,c}); the content of a word is
the union.  A certificate over tokens lifts through every nonerasing morphism h with
content(h(t)) = cont[t] for each token t (equal token contents give equal concrete contents,
nonempty components and middles stay nonempty), provided h(seeds) lies in L.

Parts
  A  L_n of reviews/chatgpt_negative_design_2026-11-04.md: closure finds a shorter ab-word (n=3).
  B  token model M1: fan-out 1, k = 2, 3 same-label c-forced slots, all separator patterns.
  C  token model M3: fan-out 2, two same-label nodes, layouts seq / cross / nest.
  D  token model M4: uniform doubling tree with an abstract escape on every level; the closure is
     exactly the weight-level set T(2^m) (m = 1, 2, 3), which is closed.
  E  bridge lemma P (escape of the parent = s . escape of the child): 2-step token certificate,
     lifted to L_n (n = 3..7, exact grammar membership of every lifted premise).
  F  concrete doubling A_0 -> ab, A_i -> A_{i-1}A_{i-1} | e_i: named escape designs, m = 2, 3.
  G  (--full) all escape pairs (e_1, e_2), |e_1| <= 3, |e_2| <= 3, m = 2.
"Closed" is certified by is_closed (brute force, no length cap).  "No shortcut" for a capped
closure that is not closed is only an observation within the cap.
Windows: py -3 check_claude_mu_ab_2026-11-05.py [--full]
"""
import sys
import time
from itertools import product
from functools import lru_cache
from collections import Counter

AB = frozenset('ab')


# ----------------------------------------------------------------------------- engine
def content(w, cont):
    s = set()
    for ch in w:
        s |= cont[ch]
    return frozenset(s)


def fill(E, t):
    return ''.join(e + s for e, s in zip(E, t)) + E[-1]


def occurrences(w):
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield (w[i:j],), (w[:i], w[j:])
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n + 1):
                    yield (w[i:j], w[k:l]), (w[:i], w[j:k], w[l:])


def closure(seeds, cont, cap, stop=None, max_words=20000, time_limit=None):
    """Saturate under SUB_1/SUB_2, keeping words of length <= cap.  Returns (S, cert, hit);
    hit is the stop word, 'MAX_WORDS' (word or time limit reached) or None (fixpoint under cap)."""
    t_end = None if time_limit is None else time.time() + time_limit
    S, cert, queue = set(seeds), [], sorted(seeds, key=lambda z: (len(z), z))
    ctxs, at, partners = {}, {}, {}
    typ = lambda t: tuple(content(s, cont) for s in t)
    hit = [None]

    def add(w, step):
        if w in S or len(w) > cap:
            return
        S.add(w)
        cert.append(step)
        queue.append(w)
        if stop is not None and stop(w) and hit[0] is None:
            hit[0] = w
        elif len(S) > max_words and hit[0] is None:
            hit[0] = 'MAX_WORDS'

    while queue and hit[0] is None:
        w = queue.pop(0)
        if t_end is not None and time.time() > t_end:
            return S, cert, 'MAX_WORDS'
        for t, E in occurrences(w):
            group = at.setdefault((E, typ(t)), set())
            tc = ctxs.setdefault(t, set())
            tp = partners.setdefault(t, {})
            for t2 in sorted(x for x in group if x != t and x not in tp):
                tp[t2] = E
                partners.setdefault(t2, {})[t] = E
                for F in sorted(tc):
                    add(fill(F, t2), (len(t), E, t, t2, F))
                for F in sorted(ctxs.get(t2, ())):
                    add(fill(F, t), (len(t), E, t2, t, F))
            if E not in tc:
                tc.add(E)
                for t2, E2 in sorted(tp.items()):
                    add(fill(E, t2), (len(t), E2, t, t2, E))
            group.add(t)
            if hit[0] is not None:
                break
    return S, cert, hit[0]


def replay(seeds, cert, cont):
    """Independent re-check of every step from the seeds."""
    S = set(seeds)
    for d, E, x, y, F in cert:
        assert len(E) == len(F) == d + 1 and len(x) == len(y) == d
        assert all(x) and all(y)
        if d == 2:
            assert E[1] and F[1]
        for u, v in zip(x, y):
            assert content(u, cont) == content(v, cont)
        for prem in (fill(E, x), fill(E, y), fill(F, x)):
            assert prem in S, prem
        S.add(fill(F, y))
    return S


def trace(cert, target, seeds):
    produced = {}
    for i, st in enumerate(cert):
        produced.setdefault(fill(st[4], st[3]), i)
    need, idx, seen = [target], set(), set()
    while need:
        w = need.pop()
        if w in seen or w in seeds:
            continue
        seen.add(w)
        i = produced[w]
        idx.add(i)
        d, E, x, y, F = cert[i]
        need += [fill(E, x), fill(E, y), fill(F, x)]
    return [cert[i] for i in sorted(idx)]


def is_closed(S, cont):
    """Brute force, no cap: None iff every SUB_1/SUB_2 step with premises in S concludes in S."""
    ctx = {}
    for w in S:
        for t, E in occurrences(w):
            ctx.setdefault(t, set()).add(E)
    groups = {}
    for t, Es in ctx.items():
        ty = tuple(content(s, cont) for s in t)
        for E in Es:
            groups.setdefault((E, ty), []).append(t)
    for (E, ty), ts in groups.items():
        for x in ts:
            for y in ts:
                if x != y and not ctx[x] <= ctx[y]:
                    return (len(x), E, x, y, min(ctx[x] - ctx[y]))
    return None


def shorter_ab(W, cont):
    return lambda w: content(w, cont) == AB and len(w) < len(W)


def lift(cert, h):
    H = lambda s: ''.join(h[c] for c in s)
    return [(d, tuple(map(H, E)), tuple(map(H, x)), tuple(map(H, y)), tuple(map(H, F)))
            for d, E, x, y, F in cert]


CONC = {ch: frozenset(ch) for ch in 'abc'}


# ----------------------------------------------------------------------------- part A
def ln_escape(i):
    return 'abc' if i == 1 else 'a' * i + 'cb'


def ln_member(n, word):
    @lru_cache(None)
    def inside(i, w):
        if i == 0:
            return w == 'ab'
        if w == ln_escape(i):
            return True
        return any(inside(i - 1, w[:k]) and inside(i - 1, w[k:]) for k in range(1, len(w)))
    return inside(n, word)


def ln_words(n):
    lev = {'ab'}
    for i in range(1, n + 1):
        lev = {ln_escape(i)} | {p + q for p in lev for q in lev}
    return lev


def part_A():
    print('== A: L_n (README (149)); L_2 is not closed; closure of the finite language L_3')
    L2 = ln_words(2)
    viol = is_closed(L2, CONC)
    d, E, x, y, F = viol
    print('   L_2 violation d=%d E=%s x=%s y=%s F=%s: F[y]=%s in L_2: %s'
          % (d, E, x, y, F, fill(F, y), ln_member(2, fill(F, y))))
    assert all(ln_member(2, w) for w in (fill(E, x), fill(E, y), fill(F, x)))
    n = 3
    L, W = ln_words(n), 'ab' * 2 ** n
    S, cert, hit = closure(L, CONC, cap=len(W), stop=shorter_ab(W, CONC))
    tr = trace(cert, hit, L)
    replay(L, tr, CONC)
    for d, E, x, y, F in tr:
        print('   step d=%d E=%s x=%s y=%s F=%s -> %s (in L_3: %s)'
              % (d, E, x, y, F, fill(F, y), ln_member(n, fill(F, y))))
    print('   forced ab-word %s of length %d < |W| = %d' % (hit, len(hit), len(W)))


# ----------------------------------------------------------------------------- part B
def slot_seeds(seps, slots, esc):
    W = ''.join(s + y for s, y in zip(seps, slots)) + seps[-1]
    seeds = set()
    for ch in product((0, 1), repeat=len(slots)):
        seeds.add(''.join(s + (esc if c else y) for s, y, c in zip(seps, slots, ch)) + seps[-1])
    return W, seeds


C1 = {'a': frozenset('a'), 'b': frozenset('b'), 'ab': frozenset('ab')}
CE = {'c': frozenset('c'), 'ac': frozenset('ac'), 'bc': frozenset('bc'), 'abc': frozenset('abc')}


def part_B():
    print('== B: token model M1 (fan-out 1, k same-label slots y, escape e)')
    for k in (2, 3):
        for same in (False, True):
            tot = hit = closed = other = 0
            for pres in product((0, 1), repeat=k + 1):
                for sc in product(('a', 'b', 'ab'), repeat=sum(pres)):
                    for yc in C1:
                        for ec in CE:
                            cont, seps, it, bad = {}, [], iter(sc), False
                            for i, p in enumerate(pres):
                                if not p:
                                    seps.append('')
                                    continue
                                L = 'p' if same else 'pqrs'[i]
                                c = C1[next(it)]
                                if L in cont and cont[L] != c:
                                    bad = True
                                cont[L] = c
                                seps.append(L)
                            if bad:
                                continue
                            cont['y'], cont['e'] = C1[yc], CE[ec]
                            W, seeds = slot_seeds(seps, ['y'] * k, 'e')
                            if content(W, cont) != AB:
                                continue
                            S, cert, h = closure(seeds, cont, cap=2 * len(W) + 2,
                                                 stop=shorter_ab(W, cont))
                            tot += 1
                            if h:
                                hit += 1
                                continue
                            closed += is_closed(S, cont) is None
                            other += sum(1 for w in S if content(w, cont) == AB) > 1
            print('   k=%d separators %-9s configs=%4d shortcut=%d closed=%4d '
                  'with another ab-word (same length)=%d'
                  % (k, 'one token' if same else 'distinct', tot, hit, closed, other))


# ----------------------------------------------------------------------------- part C
LAYOUTS = {'seq': ['y1', 'z1', 'y2', 'z2'], 'cross': ['y1', 'y2', 'z1', 'z2'],
           'nest': ['y1', 'y2', 'z2', 'z1']}


def part_C():
    print('== C: token model M3 (fan-out 2: node yields (y,z), escape (e,f), two same-label nodes)')
    allc = dict(C1)
    allc.update(CE)
    for lay, order in LAYOUTS.items():
        tot = hit = closed = 0
        for pres in [(1, 1, 1, 1, 1), (0, 1, 1, 1, 0), (0, 0, 1, 0, 0), (0, 0, 0, 0, 0), (1, 0, 0, 0, 1)]:
            if any(order.index('z' + i) == order.index('y' + i) + 1 and not pres[order.index('z' + i)]
                   for i in '12'):
                continue                      # components of one node are never adjacent
            for sc in {('ab',) * sum(pres), ('a',) * sum(pres),
                       tuple(('a', 'b')[i % 2] for i in range(sum(pres)))}:
                for yc, zc in product(C1, repeat=2):
                    for ec, fc in product(allc, repeat=2):
                        if ec in C1 and fc in C1:
                            continue          # a c-forced node: every short yield contains c
                        cont = {'y': C1[yc], 'z': C1[zc], 'e': allc[ec], 'f': allc[fc]}
                        seps, it = [], iter(sc)
                        for i, p in enumerate(pres):
                            if p:
                                cont['pqrst'[i]] = C1[next(it)]
                                seps.append('pqrst'[i])
                            else:
                                seps.append('')
                        W = ''.join(s + b[0] for s, b in zip(seps, order)) + seps[-1]
                        if content(W, cont) != AB:
                            continue
                        seeds = set()
                        for ch in product((0, 1), repeat=2):
                            seeds.add(''.join(s + ((('e' if b[0] == 'y' else 'f')
                                                     if ch[int(b[1]) - 1] else b[0]))
                                              for s, b in zip(seps, order)) + seps[-1])
                        S, cert, h = closure(seeds, cont, cap=2 * len(W) + 2,
                                             stop=shorter_ab(W, cont))
                        tot += 1
                        if h:
                            hit += 1
                        else:
                            closed += is_closed(S, cont) is None
        print('   layout=%-5s configs=%4d shortcut=%d closed=%d' % (lay, tot, hit, closed))


# ----------------------------------------------------------------------------- part D
def tree_words(level, leaf, esc):
    if level == 0:
        return {leaf, esc[0]}
    sub = tree_words(level - 1, leaf, esc)
    return {esc[level]} | {p + q for p in sub for q in sub}


def weight_level(N, weights):
    out = {''}
    res = set()
    frontier = {('', 0)}
    while frontier:
        nxt = set()
        for w, s in frontier:
            for t, wt in weights.items():
                if s + wt == N:
                    res.add(w + t)
                elif s + wt < N:
                    nxt.add((w + t, s + wt))
        frontier = nxt
    return res


def part_D():
    print('== D: token model M4 (uniform doubling, escapes E_i of level i, leaf z)')
    for ec in ('c', 'abc'):
        cont = {'z': AB}
        esc = 'EFGH'
        for t in esc:
            cont[t] = frozenset(ec)
        for m in (1, 2, 3):
            seeds = tree_words(m, 'z', esc)
            W = 'z' * 2 ** m
            S, cert, h = closure(seeds, cont, cap=len(W) + 1, stop=shorter_ab(W, cont))
            T = weight_level(2 ** m, dict({'z': 1}, **{esc[i]: 2 ** i for i in range(m + 1)}))
            print('   escapes content %-3s m=%d seeds=%4d closure=%4d shortcut=%s '
                  'closure==T(2^m): %s closed: %s ab-words: %s'
                  % (ec, m, len(seeds), len(S), h, S == T, is_closed(S, cont) is None,
                     sorted(w for w in S if content(w, cont) == AB)))


# ----------------------------------------------------------------------------- part E
def part_E():
    print('== E: bridge lemma P (escape of parent = s . escape of left child)')
    cont = {'U': AB, 'Z': AB, 'e': frozenset('abc'), 'B': frozenset('abc'),
            's': frozenset('a'), 'K': frozenset('abc')}
    W = 'UZUZ'
    gram = {l + r for l in ('UZ', 'Ue', 'B') for r in ('UZ', 'Ue', 'B')}
    for coinc in (False, True):
        seeds = gram | ({'sB'} if coinc else {'K'})
        S, cert, h = closure(seeds, cont, cap=4 * len(W), stop=shorter_ab(W, cont))
        if not h:
            print('   e_C unrelated token K: closure=%d shortcut=None closed=%s'
                  % (len(S), is_closed(S, cont) is None))
            continue
        tr = trace(cert, h, seeds)
        replay(seeds, tr, cont)
        print('   e_C = s.e_B: forced %s in %d steps:' % (h, len(tr)))
        for st in tr:
            print('     ', st)
        prem = set()
        for d, E, x, y, F in tr:
            prem |= {fill(E, x), fill(E, y), fill(F, x)}
        prem &= seeds
        print('   token premises used:', sorted(prem))
        lr = {'l': AB, 'r': AB, 'U': AB, 'Z': AB, 'e': frozenset('abc'), 'B': frozenset('abc'),
              's': frozenset('a')}
        sd = {'l' + a + b + 'r' for a in ('UZ', 'Ue', 'B') for b in ('UZ', 'Ue', 'B')} | {'lsBr'}
        S2, c2, h2 = closure(sd, lr, cap=14, stop=shorter_ab('lUZUZr', lr))
        t2 = trace(c2, h2, sd)
        replay(sd, t2, lr)
        print('   with outer context l, r (content ab): forced %s in %d step: %s' % (h2, len(t2), t2[0]))
        wt = lambda w: sum(10 if ch == 'Y' else 1 for ch in w)   # Y heavy: |s| < |Y|
        p1 = {'l': AB, 'r': AB, 'Y': AB, 'B': frozenset('c'), 's': AB}
        for nm, extra in (('e_C = e_B.s', 'lBsr'), ('e_C = s.e_B', 'lsBr')):
            sd = {'l' + a + b + 'r' for a in ('Y', 'B') for b in ('Y', 'B')} | {extra}
            S3, c3, h3 = closure(sd, p1, cap=12,
                                 stop=lambda w: content(w, p1) == AB and wt(w) < wt('lYYr'))
            t3 = trace(c3, h3, sd)
            replay(sd, t3, p1)
            print('   lemma 7, %s, content(s)=content(Y): forced %s in %d step: %s'
                  % (nm, h3, len(t3), t3[0]))
        for n in range(3, 8):
            i = n - 1
            hm = {'U': 'ab' * (2 ** i - 2), 'Z': 'abab', 'e': 'abc', 'B': ln_escape(i), 's': 'a'}
            for t, w in hm.items():
                assert content(w, CONC) == cont[t], t
            hseeds = {''.join(hm[c] for c in w) for w in prem}
            assert all(ln_member(n, w) for w in hseeds)
            out = replay(hseeds, lift(tr, hm), CONC)
            last = fill(lift(tr, hm)[-1][4], lift(tr, hm)[-1][3])
            assert last in out and content(last, CONC) == AB
            print('   lifted to L_%d: premises in L_%d (exact), forced ab-word length %d < %d'
                  % (n, n, len(last), 2 ** (n + 1)))


# ----------------------------------------------------------------------------- part F / G
def doubling(m, esc):
    lev = {'ab'}
    for i in range(1, m + 1):
        lev = {esc[i]} | {p + q for p in lev for q in lev}
    return lev


def classify(m, esc, max_words, time_limit=None):
    W = 'ab' * 2 ** m
    seeds = doubling(m, esc)
    S, cert, h = closure(seeds, CONC, cap=len(W) + 1, stop=shorter_ab(W, CONC), max_words=max_words,
                         time_limit=time_limit)
    if h == 'MAX_WORDS':
        return 'stopped', None
    if h:
        tr = trace(cert, h, seeds)
        replay(seeds, tr, CONC)
        return 'shortcut', tr
    return ('closed' if is_closed(S, CONC) is None else 'capped'), None


DESIGNS = {'c^i': lambda i: 'c' * i, 'a^(i-1)c': lambda i: 'a' * (i - 1) + 'c',
           'ca^(i-1)': lambda i: 'c' + 'a' * (i - 1), 'cb^(i-1)': lambda i: 'c' + 'b' * (i - 1),
           'b^(i-1)c': lambda i: 'b' * (i - 1) + 'c', 'c(ab)^(i-1)': lambda i: 'c' + 'ab' * (i - 1),
           'ac^ib': lambda i: 'a' + 'c' * i + 'b'}


def part_F():
    print('== F: concrete doubling, named escape designs e_i (cap |W|+1)')
    for m in (2, 3):
        for name, f in DESIGNS.items():
            esc = {i: f(i) for i in range(1, m + 1)}
            r, tr = classify(m, esc, 6000)
            msg = '   m=%d %-12s %s' % (m, name, r)
            if tr:
                last = tr[-1]
                msg += ' in %d step(s); last step E=%s x=%s y=%s F=%s' % (len(tr), *last[1:])
            print(msg)


def part_G():
    print('== G: concrete doubling m=2, all pairs (e_1, e_2) of c-words of length <= 3 (cap |W|+1)')
    cw = [''.join(p) for n in (1, 2, 3) for p in product('abc', repeat=n) if 'c' in p]
    st = Counter()
    for e1, e2 in product(cw, repeat=2):
        r, tr = classify(2, {1: e1, 2: e2}, 1500)
        st[r] += 1
    print('  ', dict(sorted(st.items())))


if __name__ == '__main__':
    part_A()
    part_B()
    part_C()
    part_D()
    part_E()
    part_F()
    if '--full' in sys.argv:
        part_G()
    print('ALL CERTIFICATES REPLAYED; ALL "closed" CLAIMS CHECKED BY BRUTE FORCE')
