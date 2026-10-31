#!/usr/bin/env python3
"""Independent check for prop:linear-factor-all-fanout (f=2), 2026-10-30.
Four-corner criterion: every subset of L is (2,triv)-substitutable iff
E[x],E[y],F[x] in L implies F[y] in {E[x],E[y],F[x]} (d<=2, nonempty middle).
Checks L^{(2)}_{q,k} for q<=3, k<=2, and a 3-marker negative control.
Usage: python3 check_linear_factor_fanout.py 3
"""
import sys
from collections import defaultdict
def fam(q,k):
    M=2**k
    return ['a'*i+'A'+'b'*i+'B'+'c'*i+'C'+'d'*i+'D'+'z'*(4*(q-i)+M) for i in range(q+1)]
def occ(w):
    n=len(w)
    for i in range(n):
        for j in range(i+1,n+1):
            yield (w[i:j],),(w[:i],w[j:])
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for t in range(k+1,n+1):
                    yield (w[i:j],w[k:t]),(w[:i],w[j:k],w[t:])
def fill(E,x):
    s=E[0]
    for xi,e in zip(x,E[1:]): s+=xi+e
    return s
def check(L):
    Ls=set(L); D=defaultdict(dict); byctx=defaultdict(set)
    for w in L:
        for x,E in occ(w):
            D[x][E]=w; byctx[E].add(x)
    viol=0
    for E,xs in byctx.items():
        xs=list(xs)
        for x in xs:
            for y in xs:
                if x==y or len(x)!=len(y): continue
                u,v=D[x][E],D[y][E]
                for F,w in D[x].items():
                    fy=fill(F,y)
                    if fy not in (u,v,w):
                        return (x,y,E,F,fy)
    return None
for q in range(1,int(sys.argv[1])+1):
    for k in (1,2):
        if k>q: continue
        r=check(fam(q,k)); print('q',q,'k',k,'violation',r)
# negative control: 3-marker reduction from report 8.1(c)
print('control', check(['ABC'+'z'*11,'aAbBcC'+'z'*8]))
