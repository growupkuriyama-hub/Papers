#!/usr/bin/env python3
"""Theorem S is not contained in the ell-local counting class (round-4 report, Prop. N1).
L_S = { w in {a,b,c}^+ : no b occurs before an a, |w|_a = |w|_b }.
For every ell<=8 and n>=ell:  w1 = a c^n a c^n b c^n b  in L_S,  w2 = a c^n b c^n a c^n b  not in L_S,
yet s_{ell-1,ell-1}(w1) = s_{ell-1,ell-1}(w2) and N_ell(w1) = N_ell(w2).  Standard library only."""
from collections import Counter
def N(w, l): return Counter(w[i:i+l] for i in range(len(w)-l+1))
def st(w, l):
    return ('S', w) if len(w) < 2*(l-1) else ('P', w[:l-1], w[len(w)-l+1:])
def inLS(w):
    return w.count('a') == w.count('b') and 'b' not in w[:w.rfind('a')+1] if 'a' in w else w.count('b') == 0
for l in range(1, 9):
    for n in range(l, l+4):
        c = 'c'*n
        w1, w2 = 'a'+c+'a'+c+'b'+c+'b', 'a'+c+'b'+c+'a'+c+'b'
        assert inLS(w1) and not inLS(w2)
        assert N(w1, l) == N(w2, l) and st(w1, l) == st(w2, l)
print('ok: for ell=1..8, n=ell..ell+3, w1 in L_S, w2 not in L_S, same (s_ell, N_ell)')

# Prop. N2: L_natural = { w in ND_P : |w|_a = |w|_d },  P: a<c, b<c, b<d  (dependence graph a-c-b-d connected)
def inND(w):
    for x, y in (('a', 'c'), ('b', 'c'), ('b', 'd')):
        if y in w and x in w and w.find(y) < w.rfind(x):
            return False
    return True
def inLnat(w): return inND(w) and w.count('a') == w.count('d')
for l in range(1, 9):
    for n in range(l, l+4):
        dd = 'd'*n
        v1 = 'a'*(3*n-1) + dd + 'a' + dd + 'c' + dd + 'c'
        v2 = 'a'*(3*n-1) + dd + 'c' + dd + 'a' + dd + 'c'
        assert inLnat(v1) and not inLnat(v2)
        assert N(v1, l) == N(v2, l) and st(v1, l) == st(v2, l)
print('ok: N2 for ell=1..8 -- L_natural is not ell-local counting (single block forced)')

# Prop. D2: E_ev = { w in {a,b}^+ : every maximal a-run has even length } is not ell-local counting.
import re
def inEev(w): return all(len(r) % 2 == 0 for r in re.findall('a+', w))
for l in range(1, 9):
    for n in range(l, l+4):
        u1 = 'b' + 'a'*(2*n) + 'b' + 'a'*(2*n) + 'b'
        u2 = 'b' + 'a'*(2*n+1) + 'b' + 'a'*(2*n-1) + 'b'
        assert inEev(u1) and not inEev(u2)
        assert N(u1, l) == N(u2, l) and st(u1, l) == st(u2, l)
print('ok: D2 for ell=1..8 -- even-runs language is not ell-local counting')
