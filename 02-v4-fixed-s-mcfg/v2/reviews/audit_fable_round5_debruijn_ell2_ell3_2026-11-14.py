#!/usr/bin/env python3
"""Independent stress test of *noncommutative* frozen-block Euler Y/F machinery.
Nontrivial full binary de Bruijn strongly connected edge systems for ell=2,3;
actual overlapping factors, frozen text, designated hole, and arbitrary circulation.
Finite testing is not an infinite theorem proof. Python standard library only.
"""
from collections import Counter,deque,defaultdict
from itertools import product
import random

def all_edges(A,ell):return [''.join(t) for t in product(A,repeat=ell)]
def sf(e):return e[:-1]
def tf(e):return e[1:]
def N(word,ell):return Counter(word[i:i+ell] for i in range(len(word)-ell+1))
def bfs(u,v,edges):
    if u==v:return []
    Q=deque([u]); prev={u:None}
    while Q:
        x=Q.popleft()
        for e in edges:
            if sf(e)==x and tf(e) not in prev:
                prev[tf(e)]=(x,e);Q.append(tf(e))
    assert v in prev,(u,v)
    out=[];cur=v
    while cur!=u:
        cur0,e=prev[cur];out.append(e);cur=cur0
    return out[::-1]

def euler(M,u,v):
    adj=defaultdict(list)
    for e,c in sorted(M.items()): adj[sf(e)]+=[e]*c
    S=[(u,None)]; out=[]
    while S:
        curr,_=S[-1]
        if adj[curr]:
            e=adj[curr].pop();S.append((tf(e),e))
        else:
            _,e=S.pop()
            if e is not None:out.append(e)
    out.reverse()
    assert len(out)==sum(M.values()) and Counter(out)==+Counter(M)
    assert out[0] and sf(out[0])==u and tf(out[-1])==v
    assert all(tf(a)==sf(b) for a,b in zip(out,out[1:]))
    return out

def closed_cover(u,edges):
    h=[]
    for e in edges:h+=bfs(u,sf(e),edges)+[e]+bfs(tf(e),u,edges)
    assert sf(h[0])==u and tf(h[-1])==u and set(h)==set(edges)
    return h

def letters(E):return ''.join(e[-1] for e in E)
def sample(ell,seed,rng):
    A='ab';edges=all_edges(A,ell);u='a'*(ell-1)
    word=u+''.join(rng.choice(A) for _ in range(10000))
    E=[word[i:i+ell] for i in range(len(word)-ell+1)]
    lo=3000+rng.randrange(100);hi=lo+100
    flexible=[not(i<hi and i+ell>lo) for i in range(len(E))]
    seg=[];i=0
    while i<len(E):
        if not flexible[i]:i+=1;continue
        j=i
        while j<len(E) and flexible[j]:j+=1
        seg.append((i,j));i=j
    assert len(seg)==2
    M=Counter(e for a,b in seg for e in E[a:b])
    p=[sf(E[a]) for a,b in seg];q=[tf(E[b-1]) for a,b in seg]
    hc=closed_cover(u,edges)
    H0=hc*(ell-1) if ell>1 else hc
    h=H0+H0 if ell>1 else hc
    z=Counter(hc) # an arbitrary nonzero J-supported circulation
    lead=bfs(p[0],u,edges);sec=bfs(p[1],q[1],edges)
    rem=M-Counter(lead)-Counter(h)-Counter(sec)
    assert all(rem[e]>0 for e in edges)
    P=euler(rem,u,q[0]);R0=lead+h+P;R1=sec
    assert Counter(R0+R1)==M
    replacement={seg[0][0]:(seg[0][1],R0),seg[1][0]:(seg[1][1],R1)}
    arr=[];i=0;hole_idx=None
    while i<len(E):
        if i in replacement:
            j,r=replacement[i]
            if i==seg[0][0]:hole_idx=len(arr)+len(lead)
            arr+=r;i=j
        else:arr.append(E[i]);i+=1
    assert all(tf(e)==sf(f) for e,f in zip(arr,arr[1:]))
    reconstructed=u+letters(arr)
    assert N(reconstructed,ell)==N(word,ell)
    assert reconstructed[:ell-1]==word[:ell-1] and reconstructed[-(ell-1):]==word[-(ell-1):]
    # conversion from edge index to string index: edge j corresponds to letter at j+ell-1
    hole_at=hole_idx+ell-1
    hs=letters(h)
    assert reconstructed[hole_at:hole_at+len(hs)]==hs
    if ell==1:t=euler(Counter(h)+z,u,u)
    else:t=H0+euler(Counter(H0)+z,u,u)
    ts=letters(t)
    assert len(ts)>0 and len(hs)>0
    if ell>1:
        assert hs[:ell-1]==ts[:ell-1] and hs[-(ell-1):]==ts[-(ell-1):]
    assert N(ts,ell)-N(hs,ell)==z
    longer=reconstructed[:hole_at]+ts+reconstructed[hole_at+len(hs):]
    assert N(longer,ell)-N(reconstructed,ell)==z
    return True

def main():
    rng=random.Random(20261114)
    for ell in [2,3]:
        for seed in range(120):sample(ell,seed,rng)
        print(f'ell={ell} complete noncommuting de Bruijn graph: 120 frozen-block Euler/hole checks passed')
    print('all independent assertions passed')
if __name__=='__main__':main()
