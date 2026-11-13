#!/usr/bin/env python3
"""Independent exact finite check of the local-pigeonhole Lemma 2(a) counterexample.
The infinite-language premises are verified mathematically in the companion note.
"""
SIGMA = ('p', 'x', 'b', 'y')

def A(n):
    if n == 0:
        return ('x', 'y')
    u, v = A(n - 1)
    return ('p', u + 'b' + v)

def B(n):
    u, v = A(n)
    return ('p' + u + 'p', 'xby' + v + 'xby')

def tp(pair):
    return tuple(frozenset(w) for w in pair)

T = (frozenset('p'), frozenset('xby'))
for n in range(5):
    print(f'n={n}: A={A(n)!r}, B={B(n)!r}, typed_B={tp(B(n))==T}')
assert tp(B(0)) != T and tp(B(1)) == T
assert all(tp(B(n)) != T for n in range(2, 10))

root = B(1)
marks = []
for w in root:
    marks.append({i for a in set(w) for i in (w.index(a), w.rindex(a))})
print('B(1) tuple =', root)
print('first/last positions by component =', [sorted(x) for x in marks])
# First A node: first component is p at position 1; second is xby at 3..5.
A1_pos = ({1}, {3,4,5})
# Inner A node has first x at position 3 in second B component,
# second y at position 5 in that same B component.
A0_pos = (set(), {3,5})
assert all(not (marks[i] & pos) for i,pos in enumerate(A1_pos))
assert all(not (marks[i] & pos) for i,pos in enumerate(A0_pos))
print('Both ancestor and descendant A nodes are free in minimal B_T derivation.')
assert tp(root) == T
assert tp(B(0)) != T
assert root != B(0)
print('Contracting ancestor A to descendant A changes B componentwise content.')
print('Lemma 2(a) is false, even for L=Sigma+ (one-stage Parikh-saturated, universally substitutable).')
