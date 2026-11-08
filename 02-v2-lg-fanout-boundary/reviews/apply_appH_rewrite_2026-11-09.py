#!/usr/bin/env python3
"""Apply appH_rewrite_2026-11-09.tex to main.tex.
Usage: python3 -I apply_appH_rewrite_2026-11-09.py main.tex appH_rewrite_2026-11-09.tex out.tex
"""
import sys, re
main, rew, dst = sys.argv[1:4]
R = open(rew).read()
def between(a, b):
    i = R.index(a); i = R.index('\n', i) + 1
    # skip the comment banner that follows the marker
    while R[i:].startswith('%'):
        i = R.index('\n', i) + 1
    return R[i:R.index(b)]
A = between('%%%% PART (a):', '%%%% END PART (a)')
B = between('%%%% PART (b):', '%%%% END PART (b)')
C = R[R.index('%% PART (c):'):R.index('%%%% END PART (c)')]
pairs = []
for blk in re.split(r'^%% ---- ', C, flags=re.M)[1:]:
    old_part, new_part = blk.split('%% NEW:\n')
    old_lines = old_part.split('%% OLD:\n')[1].rstrip('\n').split('\n')
    old = '\n'.join(l[3:] if l.startswith('%% ') else l[2:] for l in old_lines) + '\n'
    new = new_part.rstrip('\n') + '\n'
    pairs.append((old, new))
L = open(main).read().split('\n')
def find(pref):
    idx = [i for i, l in enumerate(L) if l.startswith(pref)]
    assert len(idx) == 1, (pref, idx); return idx[0]
a1 = find('\\paragraph{Individual typings onto'); a2 = find('Table~\\ref{tab:scope} collects')
b1 = find('\\section{Two Letters at Fan-Out One}'); b2 = find('\\section{Typings onto \\texorpdfstring')
L = L[:a1] + A.rstrip('\n').split('\n') + [''] + L[a2:b1] + B.rstrip('\n').split('\n') + [''] + L[b2:]
s = '\n'.join(L)
for old, new in pairs:
    n = s.count(old); assert n == 1, (old[:60], n)
    s = s.replace(old, new)
open(dst, 'w').write(s)
print('applied: parts (a), (b) and %d replacement pairs' % len(pairs))
