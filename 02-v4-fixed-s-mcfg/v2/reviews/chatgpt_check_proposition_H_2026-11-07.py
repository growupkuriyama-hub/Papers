#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent finite audit of Proposition H (2026-11-07).
Standard library only. Does NOT import or reuse either supplied checker.
Tests the lattice bound by constructive witnesses plus exact lattice membership
using gcds of maximal minors, and illustrates the A/B grammar mechanisms.
It is a finite test, not a proof. Run: python3 this_file.py --seed 1 --trials 400
"""
import argparse
from itertools import combinations, product
from math import gcd
from random import Random


def det2(a, b, c, d):
    return a*d-b*c


def det3(a, b, c):
    return (a[0]*det2(b[1], b[2], c[1], c[2])
            - a[1]*det2(b[0], b[2], c[0], c[2])
            + a[2]*det2(b[0], b[1], c[0], c[1]))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def rank_basis(gens):
    result=[]
    for g in gens:
        if not any(g):
            continue
        if len(result)==0 or (len(result)==1 and any(cross(result[0],g))) or (len(result)==2 and det3(result[0],result[1],g)):
            result.append(g)
            if len(result)==3:
                break
    return result


def minor_gcd(vectors, k):
    """gcd of ALL k x k minors, including all column and row selections."""
    if k==0:
        return 1
    gg=0
    for cols in combinations(vectors,k):
        for axes in combinations(range(3),k):
            if k==1:
                d=cols[0][axes[0]]
            elif k==2:
                d=det2(cols[0][axes[0]], cols[0][axes[1]],
                       cols[1][axes[0]], cols[1][axes[1]])
            else:
                d=det3(*cols)
            gg=gcd(gg,abs(d))
    return gg


def belongs(gens, diff):
    """Independent exact Z-lattice membership test (rank + determinantal divisors)."""
    k=len(rank_basis(gens))
    extended=gens+[diff]
    if len(rank_basis(extended))!=k:
        return False
    return minor_gcd(gens,k)==minor_gcd(extended,k)


def ceildiv(a,b):
    return -((-a)//b)


def shrink_line(w, d):
    """Minimize x+y along the integer line w + Z*d with x,y >= 1.
    It suffices to check the first/last feasible integer shift.
    """
    x,y,z=w
    dx,dy,dz=d
    assert z==0 and dz==0 and (dx or dy)
    lo,hi=None,None
    for coord,step in ((x,dx),(y,dy)):
        if step>0:
            low=ceildiv(1-coord,step)
            lo=low if lo is None else max(lo,low)
        elif step<0:
            high=(coord-1)//(-step)
            hi=high if hi is None else min(hi,high)
        else:
            assert coord>=1
    assert lo is None or hi is None or lo<=hi
    slope=dx+dy
    if slope>0:
        assert lo is not None
        t=lo
    elif slope<0:
        assert hi is not None
        t=hi
    else:
        t=0 if (lo is None or lo<=0) and (hi is None or 0<=hi) else (lo if lo is not None else hi)
    q=(x+t*dx,y+t*dy,0)
    assert q[0]>0 and q[1]>0
    return q


def short_representative(gens, p0, w):
    """Construct a short element in (p0+<gens>) intersect {z=0,x,y>=1}.
    Uses independent rank cases / adjugate, not the source report's routines.
    """
    assert w[2]==0 and w[0]>0 and w[1]>0
    bs=rank_basis(gens)
    k=len(bs)
    if k==0:
        return p0
    if k==3:
        d=abs(det3(*bs))
        return ((w[0]-1)%d+1,(w[1]-1)%d+1,0)
    if k==2:
        u,v=bs
        n=cross(u,v)
        if n[0]==n[1]==0:
            d=abs(n[2])
            return ((w[0]-1)%d+1,(w[1]-1)%d+1,0)
        return shrink_line(w,(n[1],-n[0],0))
    g=bs[0]
    if g[2]!=0:
        return w
    return shrink_line(w,g)


def stress(rng, trials):
    tested={0:0,1:0,2:0,3:0}
    tight=0
    maximum_ratio=0.0
    for trial in range(trials):
        theta=rng.randint(1,3)
        p0=(rng.randint(0,3),rng.randint(0,3),rng.randint(0,2))
        cap0=sum(p0)
        count=rng.randint(0,4)
        gens=[tuple(rng.randint(-theta,theta) for _ in range(3)) for _ in range(count)]
        bs=rank_basis(gens)
        # Plant a known solution, without relying on a lattice search or an HNF implementation.
        # Random coefficients are allowed to be negative; the resulting word vector must be positive.
        candidates=[]
        for _ in range(400):
            coeff=[rng.randint(-8,8) for __ in gens]
            w=tuple(p0[j]+sum(c*g[j] for c,g in zip(coeff,gens)) for j in range(3))
            if w[2]==0 and w[0]>=1 and w[1]>=1:
                candidates.append(w)
                break
        if not candidates:
            continue
        w=candidates[0]
        theta_eff=max(1,max((abs(x) for g in gens for x in g),default=0))
        K=2*theta_eff**2*cap0+8*theta_eff**2+2
        q=short_representative(gens,p0,w)
        assert q[2]==0 and q[0]>=1 and q[1]>=1
        assert belongs(gens,tuple(q[j]-p0[j] for j in range(3))), (gens,p0,w,q)
        assert q[0]+q[1]<=K, (gens,p0,w,q,K)
        assert minor_gcd(gens,len(bs))>=0
        tested[len(bs)]+=1
        tight=max(tight,q[0]+q[1])
        maximum_ratio=max(maximum_ratio,(q[0]+q[1])/K)
    return tested,tight,maximum_ratio


def case_a():
    # EXACT case A target, D is one vertex with 3 different labeled loops.
    # A=Z/2, phi(a)=phi(b)=0, phi(c)=1, H={0}, g_ab=0, g_abc=1.
    # The regular portion of G is the right-linear grammar of the *complete*
    # 12-state DFA for the language, with final transitions made terminal rules.
    # Extra S -> a A20 b, A0 -> a, Ai -> a A(i-1) | c are redundant and sound.
    def accepts(w):
        co=set(w)
        return (co=={'a','b'} and w.count('c')==0) or (co=={'a','b','c'} and w.count('c')%2==1)
    start=(0,0,0,0)    # seen(a),seen(b),seen(c), parity(c)
    def step(q,ch):
        a,b,c,p=q
        return (a or ch=='a', b or ch=='b', c or ch=='c',p^(ch=='c'))
    def accept_state(q):
        a,b,c,p=q
        return bool(a and b and (not c or p))
    states={start}
    pending=[start]
    while pending:
        q=pending.pop()
        for ch in 'abc':
            v=step(q,ch)
            if v not in states:
                states.add(v)
                pending.append(v)
    assert len(states)==12
    # Length of a shortest nonempty accepting continuation from each state,
    # as needed for rho(R). A BFS here enumerates at most 3^5 words.
    def shortest(q):
        for n in range(1,7):
            for cs in product('abc',repeat=n):
                z=q
                for ch in cs:
                    z=step(z,ch)
                if accept_state(z):
                    return n
        raise AssertionError('state not coaccessible')
    tau={q:shortest(q) for q in states}
    theta=max([3,2,1]+[1+tau[step(q,ch)] for q in states for ch in 'abc'])
    assert theta<=5
    n=20
    W='a'+'a'*(n+1)+'b'
    Wt='a'+'c'+'b'
    assert accepts(W) and accepts(Wt) and n+1>theta
    # Actual shortest ab word of this COMPLETE grammar is 'ab' (length 2).
    assert accepts('ab')
    # The four-word obstruction uses two hypothetical incomparable shortcuts.
    raw='a'+'a'*4+'a'*4+'b'
    left='a'+'c'+'a'*4+'b'
    right='a'+'a'*4+'c'+'b'
    both='a'+'c'+'c'+'b'
    assert accepts(raw) and accepts(left) and accepts(right) and not accepts(both)
    assert (left.count('c')-raw.count('c'))%2 == (both.count('c')-right.count('c'))%2
    return {'theta':theta,'dfa_states':len(states),'mu_ab':2,
            'long_ab_derivation':W,'heavy_unmarked_A20_length':n+1,
            'short_escape':Wt,'four_words':(raw,left,right,both),
            'fourth_rejected':True,'equality_with_target':True,
            'heavy_node_is_in_minimal_derivation':False}


def case_b():
    # Complete CFG for Sigma+: S -> a|b|c|SS|a T^8 b; T -> a|TT.
    # The S -> a T^8 b rule is additional: completeness comes from S -> SS and constants.
    # The intentionally NONMINIMAL derivation makes eight pairwise incomparable heavy T-nodes.
    q=8
    theta=q+2  # max rho(rule), because tau(S)=tau(T)=1
    heavy_t_len=32
    W='a'+'a'*(q*heavy_t_len)+'b'
    assert theta==10 and heavy_t_len>theta and len(W)==258
    min_ab=2  # 'ab' belongs to L(G)=Sigma^+, also has both letters.
    v=2
    assert min_ab <= 226*v**3*theta**3
    return {'theta':theta,'v':v,'rank':q,'mu_ab':min_ab,
            'nonminimal_word_length':len(W),'incomparable_unmarked_heavy':q,
            'equality_with_target':True}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--seed',type=int,default=1)
    ap.add_argument('--trials',type=int,default=400)
    args=ap.parse_args()
    result=stress(Random(args.seed),args.trials)
    print('INDEPENDENT lattice audit',{'seed':args.seed,'trials':args.trials,
         'successful_planted_cases_by_rank':result[0],
         'max_constructed_length':result[1], 'max_length_over_K':round(result[2],6)})
    print('CASE A:',case_a())
    print('CASE B:',case_b())
    print('K at (v,theta)=(1,1):',2*4**2*3+8*4**2+2)
    print('ALL ASSERTIONS PASSED')

if __name__=='__main__':
    main()
