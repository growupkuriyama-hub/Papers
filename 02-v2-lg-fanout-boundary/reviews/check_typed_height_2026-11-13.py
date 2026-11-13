#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_typed_height_2026-11-13.py  (Python 3, standard library only, fixed seeds)

Finite check of Lemma A (typed shortcut) of the Opus 5.5 round-2 report:
in a node-minimal derivation of a typed nonterminal X = A_T (content typing),
no root-to-leaf path repeats a typed label (B, content of each component),
hence height <= #typed labels <= v (2^k - 1)^f.

(1) The independent-review counterexample grammar: base label A repeats on a path
    of the minimal B_T derivation, but typed labels do not.
(2) Random reduced good MCFGs (fan-out <= 2, rank <= 2) whose templates freely move
    child components into other parent components.

This is a sanity check of the bookkeeping; the lemma itself is proved in the report.
"""
import random
from itertools import product

# A template component is a list of items: ('t', letter) or ('v', child, comp).

def good_template(tmpl, fans):
    """eps-free, nondeleting, nonpermuting, nonmerging."""
    if any(len(c) == 0 for c in tmpl):
        return False
    seq = [it for c in tmpl for it in c]
    for j, d in enumerate(fans):
        occ = [(it[2]) for it in seq if it[0] == 'v' and it[1] == j]
        if occ != list(range(d)):
            return False
    for c in tmpl:
        for x, y in zip(c, c[1:]):
            if x[0] == 'v' and y[0] == 'v' and x[1] == y[1] and y[2] == x[2] + 1:
                return False
    return True

def out_content(tmpl, child_types):
    res = []
    for c in tmpl:
        s = set()
        for it in c:
            if it[0] == 't':
                s.add(it[1])
            else:
                s |= child_types[it[1]][it[2]]
        res.append(frozenset(s))
    return tuple(res)

def minimal_typed(rules, fan):
    """Least node count for every realizable typed label (B, U); Bellman-Ford style."""
    best = {}      # (B,U) -> (count, rule index, child labels)
    changed = True
    while changed:
        changed = False
        for ri, (lhs, tmpl, kids) in enumerate(rules):
            pools = []
            for B in kids:
                pools.append([lab for lab in best if lab[0] == B])
            for combo in product(*pools):
                U = out_content(tmpl, [lab[1] for lab in combo])
                cnt = 1 + sum(best[lab][0] for lab in combo)
                lab = (lhs, U)
                if lab not in best or cnt < best[lab][0]:
                    best[lab] = (cnt, ri, combo)
                    changed = True
    return best

def paths_ok(best, root):
    """Rebuild the minimal tree of root; return (max height, repeated base?, repeated typed?)."""
    rep_base = rep_typed = False
    maxh = 0
    stack = [(root, (root,))]
    while stack:
        lab, path = stack.pop()
        _, _, combo = best[lab]
        if not combo:
            maxh = max(maxh, len(path))
            bases = [p[0] for p in path]
            rep_base |= len(set(bases)) < len(bases)
            rep_typed |= len(set(path)) < len(path)
        for ch in combo:
            stack.append((ch, path + (ch,)))
    return maxh, rep_base, rep_typed

def counterexample():
    T = lambda s: [('t', ch) for ch in s]
    V = lambda j, c: ('v', j, c)
    rules = [
        ('A', (T('x'), T('y')), ()),
        ('A', (T('p'), [V(0, 0)] + T('b') + [V(0, 1)]), ('A',)),
        ('B', (T('p') + [V(0, 0)] + T('p'), T('xby') + [V(0, 1)] + T('xby')), ('A',)),
    ]
    for r in rules:
        assert good_template(r[1], [2] * len(r[2]))
    best = minimal_typed(rules, {'A': 2, 'B': 2})
    root = ('B', (frozenset('p'), frozenset('xby')))
    h, rb, rt = paths_ok(best, root)
    print('  counterexample: minimal B_T nodes=%d height=%d base label repeats=%s typed label repeats=%s'
          % (best[root][0], h, rb, rt))
    assert rb and not rt

def random_grammar(rng, letters, nts, fan):
    rules = []
    for A in nts:
        d = fan[A]
        # constant rules
        for _ in range(rng.randint(1, 2)):
            rules.append((A, tuple([('t', rng.choice(letters)) for _ in range(rng.randint(1, 2))]
                                   for _ in range(d)), ()))
        # rank 1/2 rules with random good templates (components may move)
        tries = 0
        made = 0
        while made < rng.randint(2, 4) and tries < 400:
            tries += 1
            r = rng.randint(1, 2)
            kids = tuple(rng.choice(nts) for _ in range(r))
            items = []
            for j, B in enumerate(kids):
                items += [('v', j, c) for c in range(fan[B])]
            # random interleaving preserving each child's order
            seqs = [[it for it in items if it[1] == j] for j in range(r)]
            merged = []
            while any(seqs):
                j = rng.choice([j for j in range(r) if seqs[j]])
                merged.append(seqs[j].pop(0))
            # sprinkle terminals, then cut into d components
            full = []
            for it in merged:
                if rng.random() < 0.5:
                    full.append(('t', rng.choice(letters)))
                full.append(it)
            if rng.random() < 0.5:
                full.append(('t', rng.choice(letters)))
            if len(full) < d:
                continue
            cuts = sorted(rng.sample(range(1, len(full)), d - 1)) if d > 1 else []
            comps, prev = [], 0
            for c in cuts + [len(full)]:
                comps.append(full[prev:c]); prev = c
            tmpl = tuple(comps)
            if good_template(tmpl, [fan[B] for B in kids]):
                rules.append((A, tmpl, kids)); made += 1
    return rules

def random_tests(n_grammars=150, seed=20261113):
    rng = random.Random(seed)
    stats = {'grammars': 0, 'labels': 0, 'base_repeat': 0, 'max_ratio': 0.0}
    for g in range(n_grammars):
        k = rng.randint(2, 3)
        letters = 'abcd'[:k]
        nts = ['A', 'B', 'C'][:rng.randint(2, 3)]
        fan = {A: rng.randint(1, 2) for A in nts}
        rules = random_grammar(rng, letters, nts, fan)
        best = minimal_typed(rules, fan)
        H = sum((2 ** k - 1) ** fan[A] for A in nts)
        for lab in best:
            h, rb, rt = paths_ok(best, lab)
            assert not rt, (rules, lab)
            assert h <= H
            stats['labels'] += 1
            stats['base_repeat'] += rb
            stats['max_ratio'] = max(stats['max_ratio'], h / H)
        stats['grammars'] += 1
    print('  random good MCFGs: %(grammars)d grammars, %(labels)d typed labels checked; '
          'minimal trees with a repeated BASE label on a path: %(base_repeat)d; '
          'typed labels never repeat; max height/H = %(max_ratio).2f' % stats)

if __name__ == '__main__':
    print('=' * 72)
    print('Lemma A (typed shortcut) -- finite checks')
    print('=' * 72)
    counterexample()
    random_tests()
    print('all asserts passed')
