#!/usr/bin/env python3
"""Finite checks for the report. Standard library only; no membership inference.

Checks explicit lattice reductions, weighted CFG recognition and thickness,
and sound SUB consequences using exact predicates for infinite languages.
"""
from itertools import product
from random import Random
from collections import defaultdict
from heapq import heappop, heappush


def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])


def dot(u, v):
    return sum(a*b for a, b in zip(u, v))


def rank_basis(ds):
    bs = []
    for u in ds:
        if not any(u):
            continue
        if not bs or (len(bs) == 1 and any(cross(bs[0], u))) or (
                len(bs) == 2 and dot(cross(*bs), u)):
            bs.append(u)
        if len(bs) == 3:
            break
    return bs


def line_reduce(p, z):
    """Subtract a same-sign direction maximally, keeping a,b positive."""
    z = tuple(z)
    if z[0]*z[1] < 0:
        return tuple(p)
    if min(z[:2]) < 0:
        z = tuple(-x for x in z)
    if not any(z[:2]):
        return tuple(p)
    k = min((p[i]-1)//z[i] for i in (0, 1) if z[i] > 0)
    return tuple(p[i]-k*z[i] for i in range(3))


def reduce_face(p0, ds, p, theta):
    """Input includes an actual p in p0+span_Z(ds), p=(a,b,0)>0.
    The proof ensures the output is in that coset; checks below also verify
    each explicit shift in the selected sublattice without Smith forms.
    """
    bs = rank_basis(ds)
    k = len(bs)
    if k == 0:
        out = tuple(p)
        assert out == tuple(p0)
    elif k == 1:
        u = bs[0]
        out = tuple(p) if u[2] else line_reduce(p, u)
        change = tuple(out[i]-p[i] for i in range(3))
        j = next(i for i in range(3) if u[i])
        assert change[j] % u[j] == 0
        assert change == tuple((change[j]//u[j])*x for x in u)
    elif k == 2:
        u, v = bs
        n = cross(u, v)
        if n[0] == n[1] == 0:
            d = abs(n[2])
            out = ((p[0]-1) % d+1, (p[1]-1) % d+1, 0)
            change = tuple(out[i]-p[i] for i in range(3))
            det = n[2]
            assert (change[0]*v[1]-change[1]*v[0]) % det == 0
            assert (u[0]*change[1]-u[1]*change[0]) % det == 0
        else:
            z = (n[1], -n[0], 0)
            out = line_reduce(p, z)
            change = tuple(out[i]-p[i] for i in range(3))
            j = next(i for i in (0, 1) if z[i])
            assert change[j] % z[j] == 0
            assert change == tuple((change[j]//z[j])*x for x in z)
        assert dot(n, out) == dot(n, p0)
    else:
        u, v, w = bs
        d = abs(dot(cross(u, v), w))
        out = ((p[0]-1) % d+1, (p[1]-1) % d+1, 0)
        change = tuple(out[i]-p[i] for i in range(3))
        assert dot(change, cross(v, w)) % d == 0
        assert dot(u, cross(change, w)) % d == 0
        assert dot(u, cross(v, change)) % d == 0
    assert out[0] >= 1 and out[1] >= 1 and out[2] == 0
    assert sum(out) <= 12*theta**3, (p0, ds, p, out, theta)
    return out, k


def lattice_checks():
    rng = Random(20261107)
    counts = [0]*4
    # Exhaustive rank-one boxes: theta=1,2; p0 L1<=theta; coefficients -12..12.
    for t in (1, 2):
        for p0 in product(range(t+1), repeat=3):
            if sum(p0) > t:
                continue
            for u in product(range(-t, t+1), repeat=3):
                for z in range(-12, 13):
                    p = tuple(p0[i]+z*u[i] for i in range(3))
                    if p[0] > 0 and p[1] > 0 and p[2] == 0:
                        _, k = reduce_face(p0, [u], p, t)
                        counts[k] += 1
    # Deterministic random higher-rank inputs; only witnessed feasible faces tested.
    for trial in range(120000):
        t = rng.randint(1, 12)
        p0 = [rng.randint(0, t), 0, 0]
        p0[1] = rng.randint(0, t-p0[0])
        p0[2] = rng.randint(0, t-p0[0]-p0[1])
        ds = [tuple(rng.randint(-t, t) for _ in range(3))
              for _ in range(rng.randint(1, 4))]
        if trial % 3 == 0:
            ds = [(u[0], u[1], 0) for u in ds]
            p0[2] = 0
        coeff = [rng.randint(-50, 50) for _ in ds]
        p = tuple(p0[i]+sum(z*u[i] for z, u in zip(coeff, ds))
                  for i in range(3))
        if p[0] > 0 and p[1] > 0 and p[2] == 0:
            _, k = reduce_face(p0, ds, p, t)
            counts[k] += 1
    # Explicit rank-two tilted planes, both direction-sign cases, large witnesses.
    for t in range(2, 16):
        for u, v, p0, coeff in [
            ((t, 0, 1), (0, t, -1), (1, 1, 0), (10**6, 10**6)),
            ((t, 0, 0), (0, 0, 1), (0, 1, 0), (10**6, 0)),
            ((1, -1, 0), (0, 0, 1), (t, 0, 0), (-1, 0)),
        ]:
            p = tuple(p0[i]+coeff[0]*u[i]+coeff[1]*v[i] for i in range(3))
            _, k = reduce_face(p0, [u, v], p, t)
            counts[k] += 1
    print('LATTICE checked by rank', counts, 'total', sum(counts))


def grammar(m):
    rules = [(k, (i, j), '') for k in range(-m, m+1)
             for i in range(-m, m+1) for j in range(-m, m+1) if i+j == k]
    rules += [(1, (), 'a'), (-1, (), 'b'), (m, (), 'c')]
    return rules


def metrics(m):
    rules = grammar(m)
    inf = 10**9
    dist = {i: inf for i in range(-m, m+1)}
    while True:
        changed = False
        for k, children, term in rules:
            cost = len(term)+sum(dist[i] for i in children)
            if cost < dist[k]:
                dist[k], changed = cost, True
        if not changed:
            break
    outside = {i: inf for i in dist}
    outside[m] = 0
    while True:
        changed = False
        for k, children, term in rules:
            for at, child in enumerate(children):
                cost = outside[k]+len(term)+sum(dist[x] for j, x in enumerate(children) if j != at)
                if cost < outside[child]:
                    outside[child], changed = cost, True
        if not changed:
            break
    assert all(dist[i] < inf and outside[i] < inf for i in dist)
    theta = max(outside[k]+len(term)+sum(dist[i] for i in children)
                for k, children, term in rules)
    size = 2*m+1+sum(1+len(ch)+len(term)+len(ch) for k, ch, term in rules)
    assert theta <= 3*m+1
    return size, theta


def parses(word, m):
    n = len(word)
    chart = {}
    weights = {'a': 1, 'b': -1, 'c': m}
    for i, letter in enumerate(word):
        chart[i, i+1] = {weights[letter]}
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i+length
            chart[i, j] = {x+y for k in range(i+1, j)
                           for x in chart[i, k] for y in chart[k, j]
                           if -m <= x+y <= m}
    return m in chart[0, n]


def cfg_checks():
    count = 0
    for m in range(2, 7):
        for n in range(1, 8):
            for w in map(''.join, product('abc', repeat=n)):
                expected = w.count('a')-w.count('b')+m*w.count('c') == m
                assert parses(w, m) == expected, (m, w)
                count += 1
        size, theta = metrics(m)
        print('CFG m', m, 'v', 2*m+1, 'size', size, 'theta', theta, 'mu_ab', m+2)
    print('CFG recognition words checked', count)


def growing_antichain_checks():
    for k in range(6, 13):
        m = k*k-1
        inf = 10**9
        dist = [inf]*m
        heap = []
        for state, cost in ((1, 2), ((-k) % m, 1)):
            dist[state] = min(dist[state], cost)
            heappush(heap, (cost, state))
        while heap:
            cost, state = heappop(heap)
            if cost != dist[state]:
                continue
            for step, extra in ((1, 2), (-k, 1)):
                nxt = (state+step) % m
                if cost+extra < dist[nxt]:
                    dist[nxt] = cost+extra
                    heappush(heap, (dist[nxt], nxt))
        outside = [0 if g == 0 else dist[(-g) % m] for g in range(m)]
        theta = max(outside[(i+j) % m]+dist[i]+dist[j]
                    for i in range(m) for j in range(m))
        theta = max(theta, outside[1]+2, outside[(-k) % m]+1)
        h = 5*k
        assert h < m and 2*h > theta and theta <= 9*k
        assert dist[h] <= theta  # all short alternatives contain c
        print('ANTICHAIN k', k, 'M', m, 'theta', theta,
              'mu_ab', 2*m, 'proved width >=', m//h)


def occurrences(w, d):
    n = len(w)
    for i in range(n):
        for j in range(i+1, n+1):
            if d == 1:
                yield (w[:i], w[j:]), (w[i:j],)
            else:
                for k in range(j+1, n):
                    for ell in range(k+1, n+1):
                        yield (w[:i], w[j:k], w[ell:]), (w[i:j], w[k:ell])


def fill(e, x):
    return ''.join(e[i]+x[i] for i in range(len(x)))+e[-1]


def path_predicate(w, m):
    state, balance = 0, 0
    for c in w:
        if c == 'a' and state == 0:
            state, balance = 1, balance+1
        elif c == 'b' and state == 1:
            state = 0
        elif c == 'c' and state == 0:
            balance -= 1
        else:
            return False
    return bool(w) and state == 0 and balance % m == 0


def sub_checks(name, pred, cap=6):
    # Premises are bounded; conclusions use the EXACT infinite-language predicate.
    # Absence of violations is not used as a membership proof.
    words = {w for n in range(1, cap+1)
             for w in map(''.join, product('abc', repeat=n)) if pred(w)}
    totals = []
    for d in (1, 2):
        by_e = defaultdict(set)
        by_x = defaultdict(set)
        for w in words:
            for e, x in occurrences(w, d):
                sig = tuple(frozenset(t) for t in x)
                by_e[e, sig].add(x)
                by_x[x].add(e)
        ncheck = 0
        for (e, sig), xs in by_e.items():
            for x in xs:
                for y in xs:
                    for f in by_x[x]:
                        out = fill(f, y)
                        assert pred(out), (name, d, e, x, y, f, out)
                        ncheck += 1
        totals.append(ncheck)
    print('SUB', name, 'premise length <=', cap, 'accepted seeds', len(words), 'checks', totals)


def main():
    lattice_checks()
    cfg_checks()
    growing_antichain_checks()
    for m in (2, 3, 4):
        sub_checks('integer-fibre-'+str(m),
                   lambda w, m=m: w.count('a')-w.count('b')+m*w.count('c') == m)
        sub_checks('edge-path-mod-'+str(m), lambda w, m=m: path_predicate(w, m), 8)
    sub_checks('support-dependent-parity',
               lambda w: len(w) % 2 == (1 if set(w) == {'a', 'b'} else 0))
    print('ALL CHECKS PASSED. Finite tests do not establish C1/C2 membership.')


if __name__ == '__main__':
    main()
