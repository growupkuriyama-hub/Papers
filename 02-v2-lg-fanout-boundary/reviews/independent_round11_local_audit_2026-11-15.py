#!/usr/bin/env python3
"""Independent exhaustive check of Round Eleven origin-marker lemmas V/M.
No imports from Claude's round 9/10/11 modules.
"""
from itertools import product
from collections import Counter
A=set('ac'); B=set('bc'); CS=3

def windows(w, alph):
    pos=[i for i,c in enumerate(w) if c in alph]
    return [(pos[k],pos[k+1],w[pos[k]]+w[pos[k+1]]) for k in range(len(pos)-1)]

def marks(w):
    mark=set(); count=Counter()
    for alph in (A,B):
        for i,j,e in windows(w,alph):
            count[(frozenset(alph),e)]+=1
            if count[(frozenset(alph),e)]<=CS: mark.update((i,j))
    return mark

def nu(w,letter):return sum(letter in block for block in w.split('c')[1:-1])

def check(w):
    mark=marks(w); cp=[i for i,c in enumerate(w) if c=='c']; n=len(cp)
    blocks=w.split('c')
    # M1--M7 provenance positions
    for l in 'ab':
        occupied=[s for s in range(1,n) if l in blocks[s]]
        if occupied:
            s0=occupied[0]
            start=cp[s0-1]+1
            fst=start+blocks[s0].index(l)
            assert {cp[s0-1],fst} <=mark,('M1',w,l,s0,mark)
        occ_ac=[s for s in range(n) if l in blocks[s]]
        for s in occ_ac[:min(2,len(occ_ac))]:
            last=(0 if s==0 else cp[s-1]+1)+blocks[s].rindex(l)
            assert {last,cp[s]}<=mark,('M2',w,l,s,mark)
        if n and nu(w,l)==0:
            if l in blocks[0]:
                last=blocks[0].rindex(l)
                assert {last,cp[0]}<=mark,('M3',w,l,mark)
            if l in blocks[-1]:
                fst=cp[-1]+1+blocks[-1].index(l)
                assert {cp[-1],fst}<=mark,('M3tail',w,l,mark)
        if l in w and len(''.join(c for c in w if c in (set(l)|{'c'})))>=2:
            assert w.index(l) in mark,('M4',w,l,mark)
    for l in 'ab':
        for i,j,e in windows(w,set(l+'c')):
            if e==l+l:
                assert {i,j}<=mark,('M5',w,l,mark)
                break
    if n>=2: assert cp[0] in mark,('M6',w,mark)
    for l in 'ab':
        if n>=2 and w.index(l)<cp[0] if l in w else False:
            assert cp[1] in mark,('M7-left',w,l,mark)
        if n>=3 and l in blocks[1]:
            assert cp[2] in mark,('M7-inner',w,l,mark)
    # V: every unmarked contiguous original interval in non-rich block
    if n:
        for l in 'ab':
            if nu(w,l)==0:
                for i in range(len(w)):
                    if i in mark:continue
                    for j in range(i+1,len(w)+1):
                        if j-1 in mark: break
                        s=w[i:j]
                        assert not(l in s and 'c' in s),('V',w,l,i,j,s,mark)
    return len(mark)

N=0
for n in range(1,11):
    for seq in product('abc',repeat=n):
        w=''.join(seq)
        try:check(w)
        except AssertionError as e:
            print('FAIL',e);raise
        N+=1
print('ALL INDEPENDENT LOCAL CHECKS PASSED, words=',N)
