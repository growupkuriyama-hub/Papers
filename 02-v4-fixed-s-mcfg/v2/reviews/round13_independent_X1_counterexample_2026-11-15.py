#!/usr/bin/env python3
"""Independent finite counterexample to Round13 Lemma L5-X1, as stated.
No imports from Claude's checker; exact enumeration of arity 1/2 contexts.
"""
from collections import defaultdict
S = set('''aaabc aabac aabca abaac abaca abcaa baaac baaca bacaa bcaaa
aaaaac aaaaca aaaacb aaacaa aaacab aaacba aacaaa aacaab aacaba aacbaa
acaaaa acaaab acaaba acabaa acbaaa caaaaa caaaab caaaba caabaa cabaaa
cbaaaa aaaaaab aaaaaba aaaabaa aaabaaa aabaaaa abaaaaa baaaaaa
aaaaaaaa'''.split())
assert len(S)==39
L=S|{'bc'}

def T(x):return tuple(frozenset(z) for z in x)
def fill(E,x):
    return E[0]+x[0]+E[1] if len(x)==1 else E[0]+x[0]+E[1]+x[1]+E[2]
D=defaultdict(set)
for w in L:
    n=len(w)
    for i in range(n):
        for j in range(i+1,n+1):
            D[(w[i:j],)].add((w[:i],w[j:]))
    for i in range(n):
        for j in range(i+1,n+1):
            for k in range(j+1,n):  # separator w[j:k] must be nonempty
                for z in range(k+1,n+1):
                    D[(w[i:j],w[k:z])].add((w[:i],w[j:k],w[z:]))
K=defaultdict(list)
for x,contexts in D.items():
    for E in contexts:K[(len(x),T(x),E)].append(x)
checks=0
for (d,t,E),xs in K.items():
    for x in xs[1:]:
        checks+=1
        assert D[x]==D[xs[0]],(xs[0],x,D[x]^D[xs[0]])
assert all(w and not (set(w)=={'a'} and len(w)<8) for w in L)
assert 'a'*8 in L
# Standalone words and their outer-a totals:
N=8; kap='bc'; kap2='acb'; lam=3; lam2=3
w='a'+kap+'aa'; w2='aa'+kap2+'a'
assert w=='abcaa' and w2=='aaacba'
assert w in L and w2 in L
assert 3<=lam<=N-1 and 3<=lam2<=N-1
assert set('a'+kap)==set('a'+kap2)=={'a','b','c'}
i=max(0,lam-lam2); ip=max(0,lam2-lam)
assert i==ip==0
assert 'bc' in L and 'acb' not in L
print('S size',len(S),'L size',len(L),'tuple count',len(D),'accepting contexts',sum(map(len,D.values())),'tuple-pair comparisons',checks)
print('C_2,content closed (d=1,2): YES, verified over ALL finite contexts')
print('a^N min N=8: YES')
print('X1 standalone witnesses:',w,w2)
print('s(aκ)=s(aκ\u2032)={a,b,c}: YES; λ=λ\u2032=3')
print('predicted by X1: κ=bc in L iff κ\u2032=acb in L')
print('observed: bc in L, acb not in L; X1 FALSE')
print('Note: s(κ)={b,c} while s(κ\u2032)={a,b,c}, so typed 1-hole substitutability cannot apply')
print('ALL COUNTEREXAMPLE CONDITIONS VERIFIED')
