#!/usr/bin/env python3
"""Independent finite-model and arithmetic checks for the 2026-11-09 T' note.
Python standard library only.  These tests are not a proof of the theorem.
Run: python3 check_chatgpt_S1_proofnote_2026-11-09.py
"""
from itertools import product
from collections import defaultdict, deque
from math import comb
from time import perf_counter

START=perf_counter()


def compose(t, u):
    # transformation for the concatenation of a word with action t,
    # followed by a word with action u
    return tuple(u[q] for q in t)


def analyze_dfa(a, b, final):
    n=len(a)
    ident=tuple(range(n))
    action={'a':a,'b':b}
    # Distinct transformation + content pairs (every nonempty word).
    seen={(ident,0)}
    todo=deque([(ident,0)])
    while todo:
        t,mask=todo.popleft()
        for letter, bit in [('a',1),('b',2)]:
            p=(compose(t,action[letter]),mask|bit)
            if p not in seen:
                seen.add(p); todo.append(p)
    trans={t for t,mask in seen}
    reachable={0}
    todo=deque([0])
    while todo:
        q=todo.popleft()
        for x in (a,b):
            if x[q] not in reachable:
                reachable.add(x[q]); todo.append(x[q])
    # A syntactic signature is the *full two-sided* distribution,
    # encoded over every reachable prefix-state and suffix action.
    slots=[(q,h) for q in sorted(reachable) for h in sorted(trans)]
    bits={}
    for t in trans:
        acc=0
        for i,(q,h) in enumerate(slots):
            if h[t[q]] in final:
                acc |= 1<<i
        bits[t]=acc
    for typ in (1,2,3):
        classes=[bits[t] for t,m in seen if m==typ]
        for i,vi in enumerate(classes):
            for vj in classes[i+1:]:
                if (vi & vj) and vi!=vj:
                    return None

    def word(w):
        t=ident
        for ch in w:
            t=compose(t,action[ch])
        return t
    def eq(x,y):
        return bits[word(x)]==bits[word(y)]
    def productive(x):
        return bits[word(x)]!=0
    def is_infinite():
        # useful accepting SCC test: a reachable state on a cycle that can
        # reach acceptance implies infinitely many accepted words.
        co=set(final)
        changed=True
        while changed:
            changed=False
            for q in range(n):
                if q not in co and (a[q] in co or b[q] in co):
                    co.add(q); changed=True
        for q in reachable & co:
            todo=[(q,0)]; visited={(q,0)}
            while todo:
                s,length=todo.pop()
                for x in (a,b):
                    nxt=x[s]
                    if nxt==q and length+1>0:
                        return True
                    if (nxt,1) not in visited:
                        visited.add((nxt,1));todo.append((nxt,1))
        return False
    return word, eq, productive, is_infinite()


def check_dfas():
    n=3
    count=0; infin=0; checks_43=0; checks_21=0; checks_p=0
    witnesses=[]
    for xs in product(range(n), repeat=2*n):
        a=tuple(xs[:n]); b=tuple(xs[n:])
        for fm in range(1,1<<n):
            final={q for q in range(n) if fm & (1<<q)}
            z=analyze_dfa(a,b,final)
            if z is None:continue
            word,eq,productive,inf=z
            count+=1;infin+=int(inf)
            if len(witnesses)<3 and inf: witnesses.append((a,b,tuple(sorted(final))))
            for z0 in ('ab','ba','aab','abb','bba','bab','aba'):
                if not productive(z0):continue
                p0=next((p for p in range(1,32) if eq('a'*p+z0,z0)),None)
                if p0 is not None:
                    checks_43+=1
                    assert eq('a','a'*(1+p0)),(a,b,final,z0,p0)
                    for p in range(p0,32):
                        if eq('a'*p+z0,z0):
                            assert p%p0==0,(a,b,final,z0,p,p0)
                            checks_p+=1
            # Lemma 2.1 with W1,W2,W3 congruent, as ensured by C_1
            # in the actual derivation. Exhaust small numerical configurations.
            for d in range(1,5):
                for nY in range(1,d+1):
                    g=d-nY
                    for omega in ('b','bb','ab','ba','aba'):
                        if 'b' not in omega:continue
                        for x,y in product(range(3),repeat=2):
                            if g==0 and set(omega)=={'b'} and x+y==0:continue
                            w1='a'*x+omega+'a'*g+omega+'a'*y
                            w2='a'*x+omega+'a'*(d+y)
                            w3='a'*(x+d)+omega+'a'*y
                            if not (set(w1)==set(w2)==set(w3)=={'a','b'}):continue
                            if not (productive(w1) and eq(w1,w2) and eq(w2,w3)):continue
                            if g==0 and set(omega)=={'b'}:
                                z0=omega+'a'*d;c=2*d
                            else:
                                z0=omega+'a'*g;c=d
                            checks_21+=1
                            assert productive(z0),('z0-unproductive',a,b,final,w1,z0)
                            assert eq('a'*d+z0,z0+'a'*d),(a,b,final,d,z0)
                            assert eq(z0+z0,'a'*c+z0),(a,b,final,d,z0,c)
    return dict(C_1_c_dfas=count,infinite=infin,tests_lemma_4_3=checks_43,
                tests_period=checks_p,tests_lemma_2_1=checks_21,
                sample_infinite_dfas=witnesses)


def numerical_skeleton(N=12):
    # The unbinarized grammar S -> SS|a|b|A0|..|AN,
    # A0 -> a, Ai -> A(i-1)A(i-1)|b has theta=2 and
    # K=N+2 (S,A0,...,AN). The examined nonterminal is A_N.
    # A2 nodes are exactly the seeds (yield length 4>theta); their
    # values are distinct from the actual shortest yield |omega_Ai|=1.
    K=N+2;theta=2;n=2**N;d=4;g0=0;c=8
    # A_j has 2^(j-2) seed occurrences when j>=2.
    eligible=[j for j in range(2,N+1) if 2**(j-2)>=K+1]
    if not eligible:return {'skipped':'K+1 seeds not met'}
    j=min(eligible)
    # heavy path A_N,A_(N-1),...,A_j, so i*=N-j
    i_star=N-j;i0=1
    v={0:n}
    for i in range(i0,i_star+1):
        # left-spine Xi=A_(N-i), first seed is A2. For omega=b and
        # p_i=0, right padding s_i=4, left s'_i=0.
        v[i]=2**(N-i)+d
    for i in range(i_star):
        assert v[i]<=2*v[i+1]+2*d
        assert v[i]>=2**(N-i)
    assert v[i_star]>d
    assert 2**j<=2*K*(K+2)*theta
    # Note: L=Sigma+ in this example has p0=1 and D=4, so the
    # actual S selection has M=0. D=infinity below is purely a
    # numerical stress test of the inequalities (not a model of L).
    vals=[v[i] for i in range(i_star,i0-1,-1)]
    Vstar=n
    selected=[]
    if vals[0]<=Vstar/2:
        selected=[vals[0]]
        for item in vals[1:]:
            if item>2*selected[-1]:
                if item>Vstar/2:break
                selected.append(item)
    sigma=sum(selected)
    assert sigma<Vstar and (not selected or sigma<2*selected[-1])
    X=Vstar-sigma
    quantities=[]
    for i in range(i0,i_star+1):
        vi=v[i];q,X=divmod(X,vi);quantities.append(q)
        assert q<2+4*K*K
    assert X<v[i_star] and X%d==0
    assert sigma+sum(q*v[i] for q,i in zip(quantities,range(i0,i_star+1)))+X==Vstar
    lam=5*K*K*theta; B1=14*K*K*theta
    assert sum(quantities)*lam+X<=(5*K**3+3)*lam
    return dict(K=K,theta=theta,n=n,seed_label='A2',seed_count=2**(N-2),
                d=d,z0='baaaa',c=c,omega_Ai='b',p_i=0,s_prime_i=0,s_i=4,
                e_i=[v[i]-c for i in range(i0,i_star+1)],
                i0=i0,i_star=i_star,selected_values=selected,
                formal_values=[v[i] for i in range(i0,i_star+1)],
                greedy_quantities=quantities,remainder=X,
                note='D=infinity arithmetic is synthetic; actual Sigma+ has D=4')


def check_binomial():
    tested=0
    for M in range(6,501):
        for j in range(M+1):
            if M/3-1<j<=2*M/3:
                assert comb(M+1,j)>=3**(M/3-1)
                tested+=1
    return tested

if __name__=='__main__':
    print('DFA exact syntactic-profile checks:', check_dfas())
    print('CFG / superincrease / greedy skeleton N=12:', numerical_skeleton(12))
    r=numerical_skeleton(20)
    print('Synthetic D=infinity arithmetic stress N=20:',
          {k:r[k] for k in ('K','n','i_star','selected_values','remainder')},
          'M=',len(r['selected_values']))
    print('Binomial inequalities checked:', check_binomial())
    print('Runtime_sec:',round(perf_counter()-START,3))
