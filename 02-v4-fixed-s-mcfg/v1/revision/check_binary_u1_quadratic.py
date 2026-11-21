#!/usr/bin/env python3
"""Check for prop:binary-u1-quadratic (2026-10-30): exact |G| and theta-bar of the
compressed block-code grammar C0->a, Cj->C(j-1)C(j-1), A0->Cm|b, Ai->A(i-1)A(i-1),
ratios N/(|G| theta), N/(|G|^2 theta), N/theta^2, and exact (1,s)-substitutability
of {a^k,b}^(2^n) for small k,n. Run from this folder.
"""
import random, itertools
from collections import defaultdict
def dist(L):
    D=defaultdict(set)
    for w in L:
        for i in range(len(w)):
            for j in range(i+1,len(w)+1):
                D[w[i:j]].add((w[:i],w[j:]))
    return D
def subst(L,only_mixed=False):
    D=dist(L); by=defaultdict(list)
    for x,cs in D.items():
        for c in cs: by[(c,'b' in x)].append(x)
    for (c,t),xs in by.items():
        if only_mixed and not t: continue
        for x in xs:
            if D[x]!=D[xs[0]]: return False,(xs[0],x,c)
    return True,None
def cond(L):
    if sum(1 for w in L if 'b' not in w)>1: return False
    return subst(L,only_mixed=True)[0]
def grammar(m,n):
    R=[('C0',['a'])]+[(f'C{j}',[f'C{j-1}',f'C{j-1}']) for j in range(1,m+1)]
    R+=[('A0',[f'C{m}']),('A0',['b'])]+[(f'A{i}',[f'A{i-1}',f'A{i-1}']) for i in range(1,n+1)]
    return R, f'A{n}'
def metrics(R,S):
    V=sorted({l for l,_ in R}); NT=set(V)
    d={}
    for _ in range(len(R)+2):
        for l,rhs in R:
            if all(x not in NT or x in d for x in rhs):
                v=sum(d[x] if x in NT else len(x) for x in rhs)
                d[l]=min(d.get(l,10**18),v)
    o={S:0}
    for _ in range(len(R)+2):
        for l,rhs in R:
            if l not in o: continue
            for i,x in enumerate(rhs):
                if x in NT:
                    v=o[l]+sum(d[y] if y in NT else len(y) for j,y in enumerate(rhs) if j!=i)
                    o[x]=min(o.get(x,10**18),v)
    theta=max(o[l]+sum(d[x] if x in NT else len(x) for x in rhs) for l,rhs in R)
    size=len(V)+sum(1+sum(x in NT for x in rhs)+sum(1 if x in NT else len(x) for x in rhs) for l,rhs in R)
    return size,theta
for m,n in [(1,1),(2,2),(3,3),(5,5),(8,8),(10,10),(20,20)]:
    R,S0=grammar(m,n); g,th=metrics(R,S0); N=2**(m+n)
    print(f'm={m} n={n} |G|={g} (6m+6n+9={6*m+6*n+9}) theta={th} (2^n+2^m-1={2**n+2**m-1}) N=tau={N} N/(|G|theta)={N/(g*th):.3f} N/(|G|^2 theta)={N/(g*g*th):.4f} N/theta^2={N/th**2:.3f}')
for k,n in [(4,2),(2,3),(8,1),(4,3)]:
    L={''.join(p) for p in itertools.product(['a'*k,'b'],repeat=2**n)}
    print('subst check k',k,'n',n,'|L|',len(L),subst(L)[0])
