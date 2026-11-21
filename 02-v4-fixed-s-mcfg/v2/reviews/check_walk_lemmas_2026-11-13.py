#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_walk_lemmas_2026-11-13.py  (Python 3, standard library only, fixed seeds)

Finite checks for the path-language (Route 1) part of the Opus 5.5 round-2 report.
Letters are edges of a digraph D (one edge per letter); words are walks.

 W1  In a walk w, every letter whose edge joins two different strongly connected
     components of the support graph S(w) occurs exactly once; hence a factor that
     avoids the first/last occurrence of every letter lies inside one SCC block.
 W2  (frequency gap) Let c_1 = c0 and c_{i+1} = k*c_i + 1.  Some interval
     [c_i, c_{i+1}) contains no letter frequency of w.  With threshold c_{i+1},
     every weakly connected component of the subgraph of frequent letters is
     strongly connected.
 G   Gap count: with alternating crossing fan-out-2 templates, a DFS-prefix region
     of one free subtree occupies up to floor(n/2)+1 separate pieces of a single
     component (n = depth); so a pigeonhole region is not confined to <= f gaps.

All three are proved (W1, W2) or only computed (G) in the report; this file is a sanity check.
"""
import random
from collections import Counter, defaultdict

def sccs(vertices, edges):
    """Tarjan-free simple SCC: mutual reachability."""
    adj = defaultdict(set)
    for (u, v) in edges:
        adj[u].add(v)
    reach = {}
    for s in vertices:
        seen, st = {s}, [s]
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); st.append(v)
        reach[s] = seen
    comp = {}
    for v in vertices:
        comp[v] = frozenset(u for u in vertices if u in reach[v] and v in reach[u])
    return comp

def random_walk(rng, D, start, length):
    out = defaultdict(list)
    for a, (u, v) in D.items():
        out[u].append(a)
    w, cur = [], start
    for _ in range(length):
        if not out[cur]:
            break
        a = rng.choice(out[cur]); w.append(a); cur = D[a][1]
    return w

def check_w1_w2(trials=400, seed=11):
    rng = random.Random(seed)
    n_w1 = n_w2 = 0
    for _ in range(trials):
        nv = rng.randint(2, 4)
        k = rng.randint(3, 7)
        D = {}
        for i in range(k):
            D['l%d' % i] = (rng.randrange(nv), rng.randrange(nv))
        w = random_walk(rng, D, rng.randrange(nv), rng.randint(5, 400))
        if not w:
            continue
        S = set(w)
        V = set(x for a in S for x in D[a])
        comp = sccs(V, [D[a] for a in S])
        cnt = Counter(w)
        # W1
        for a in S:
            u, v = D[a]
            if comp[u] != comp[v]:
                assert cnt[a] == 1
        marks = set()
        for a in S:
            idx = [i for i, b in enumerate(w) if b == a]
            marks.add(idx[0]); marks.add(idx[-1])
        for i in range(len(w)):
            for j in range(i + 1, min(len(w), i + 40) + 1):
                if not any(p in marks for p in range(i, j)):
                    blocks = set(comp[D[a][0]] for a in w[i:j]) | set(comp[D[a][1]] for a in w[i:j])
                    assert len(blocks) == 1
        n_w1 += 1
        # W2
        c = [3]
        for _ in range(k + 1):
            c.append(k * c[-1] + 1)
        freqs = set(cnt.values())
        gap = next(i for i in range(k + 1) if not any(c[i] <= x < c[i + 1] for x in freqs))
        thr = c[gap + 1]
        Fr = [a for a in S if cnt[a] >= thr]
        if Fr:
            VF = set(x for a in Fr for x in D[a])
            comp2 = sccs(VF, [D[a] for a in Fr])
            for a in Fr:
                assert comp2[D[a][0]] == comp2[D[a][1]], 'frequent edge not on a frequent cycle'
            n_w2 += 1
    print('  W1 checked on %d walks; W2 checked on %d walks with frequent letters' % (n_w1, n_w2))

def check_gap_count(nmax=12):
    def orders(n):
        if n == 0:
            return [0], [0]
        l1, l2 = orders(n - 1)
        m = 2 ** (n - 1)
        r1, r2 = [x + m for x in l1], [x + m for x in l2]
        return l1 + r1, (r2 + l2) if n % 2 == 1 else (l2 + r2)
    def pieces(order, S):
        cnt, prev = 0, False
        for leaf in order:
            cur = leaf in S
            cnt += cur and not prev
            prev = cur
        return cnt
    row = []
    for n in range(1, nmax + 1):
        o1, o2 = orders(n)
        best = max(pieces(o2, set(range(j))) for j in range(2 ** n + 1))
        assert max(pieces(o1, set(range(j))) for j in range(2 ** n + 1)) == 1
        assert best == n // 2 + 1
        row.append(best)
    print('  G: max #pieces of a DFS-prefix region in component 2, depth 1..%d: %s' % (nmax, row))

if __name__ == '__main__':
    print('=' * 72)
    print('Route 1 (walk languages) and gap-count checks')
    print('=' * 72)
    check_w1_w2()
    check_gap_count()
    print('all asserts passed')
