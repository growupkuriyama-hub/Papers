#!/usr/bin/env python3
"""Finite check for Appendix `app:singleton` of main.tex (Theorem thm:app-singleton).

Python 3 standard library only.  Run from this folder:  python3 tools/check_singleton.py
It reads Table `tab:singleton-certificates` from main.tex and checks:
  1. every row is a violation for arity 2 (E[x]=E[y]=F[x]=W != F[y], nonempty
     holes, nonempty middle separators);
  2. the rows cover, up to exchange of letters and reversal, exactly the words of
     length 7 outside the five shapes, and an exhaustive search confirms that the
     other 10 words admit no violation for arity 2;
  3. the transitions between consecutive length-7 factors listed in the proof.
"""
import re, itertools
from collections import defaultdict

def plug(E, x):
    return ''.join(E[i] + x[i] for i in range(len(x))) + E[-1]

def violation(w, d=2):
    ctx = defaultdict(set); dist = defaultdict(set)
    for cuts in itertools.combinations(range(len(w) + 1), 2 * d):
        E = (w[:cuts[0]],) + tuple(w[cuts[2*i+1]:cuts[2*i+2]] for i in range(d - 1)) + (w[cuts[-1]:],)
        x = tuple(w[cuts[2*i]:cuts[2*i+1]] for i in range(d))
        ctx[E].add(x); dist[x].add(E)
    for E, xs in ctx.items():
        xs = sorted(xs)
        for y in xs[1:]:
            if dist[y] != dist[xs[0]]:
                return True
    return False

def orbit(w):
    s = w.translate(str.maketrans('ab', 'ba'))
    return {w, w[::-1], s, s[::-1]}

def shapes(n):
    out = set()
    for x, y in (('a', 'b'), ('b', 'a')):
        out |= {x * n, x * (n - 1) + y, y + x * (n - 1), y + x * (n - 2) + y,
                ''.join(x if i % 2 == 0 else y for i in range(n))}
    return out

tex = open('main.tex', encoding='utf-8').read()
tab = tex[tex.index(r'\label{tab:singleton-certificates}'):]
tab = tab[:tab.index(r'\end{tabular}')]
def word(s):
    s = s.strip()
    if s == r'\eps': return ''
    m = re.fullmatch(r'\\mathtt\{([ab]*)\}', s)
    assert m, s
    return m.group(1)
def tup(cell):
    inner = cell.strip().strip('$').strip()
    assert inner[0] == '(' and inner[-1] == ')'
    return tuple(word(p) for p in inner[1:-1].split(','))
rows = []
for line in tab.splitlines():
    if line.startswith(r'$\mathtt{') and '&' in line:
        c = [z.strip() for z in line.rstrip('\\').split('&')]
        rows.append((word(c[0].strip('$')), tup(c[1]), tup(c[2]), tup(c[3]), tup(c[4]), word(c[5].strip('$'))))
assert len(rows) == 32, len(rows)
covered = set()
for W, E, x, y, F, Fy in rows:
    assert len(W) == 7 and all(x) and all(y) and E[1] and F[1]
    assert plug(E, x) == plug(E, y) == plug(F, x) == W
    assert plug(F, y) == Fy != W
    covered |= orbit(W)
allw = {''.join(t) for t in itertools.product('ab', repeat=7)}
good = shapes(7)
assert len(good) == 10 and covered == allw - good
assert all(not violation(w) for w in good) and all(violation(w) for w in allw - good)
trans = {v: sorted(z for z in 'ab' if v[1:] + z in good) for v in good}
expected = {'aaaaaaa': ['a', 'b'], 'baaaaaa': ['a', 'b'], 'aaaaaab': [], 'baaaaab': [],
            'abababa': ['b'], 'bbbbbbb': ['a', 'b'], 'abbbbbb': ['a', 'b'], 'bbbbbba': [],
            'abbbbba': [], 'bababab': ['a']}
assert trans == expected, trans
print('OK: 32 rows checked; they cover the 118 words of length 7 outside the 10 shapes;',
      'the 10 shapes pass for arity 2; transitions as stated.')
