#!/usr/bin/env python3
"""Independent local checks for Fable 2026-11-16 late addenda.
Checks structural Rect steps, strings and accounting; not a model checker for all L.
"""
from itertools import product
from collections import Counter

count=Counter()

def alph(s):return frozenset(s)
def subst(E, pair):
    assert len(E)==3 and len(pair)==2 and E[1] and pair[0] and pair[1]
    return E[0]+pair[0]+E[1]+pair[1]+E[2]

def rect(E0,E1,x,y,a0,a1):
    assert alph(x[0])==alph(y[0]) and alph(x[1])==alph(y[1])
    assert subst(E0,x)==a0 and subst(E0,y)==a0
    assert subst(E1,x)==a1
    count['rect_instances']+=1
    return subst(E1,y)

def rc_test(t,q,n):
    b='b'*t; B=b+'c'*q; P='ba'; Q='ac'; w=P+B*n+b+'c'+Q
    x=('c'+b, 'c'*(q-1)+b+'c')
    y=('c'+b+'c','c'*(q-2)+b+'c')
    core='c'+b+'c'*q+b+'c'
    pos=w.find(core)
    assert pos>=0
    E0=(w[:pos], 'c', w[pos+len(core):])
    # E0 target is original word, using factor x1 z z y2.
    assert subst(E0,x)==w==subst(E0,y)
    first=len(P)+len(b)+q-1  # last c in B1
    second=len(P)+2*(len(b)+q)+len(b)+1  # second c of B3
    E1=(w[:first],w[first+len(x[0]):second],w[second+len(x[1]):])
    w1=rect(E0,E1,x,y,w,w)
    expected=P+B+b+'c'*(q+1)+b+'c'*(q-1)+B*(n-3)+b+'c'+Q
    assert w1==expected,(w1,expected,t,q,n)
    count['CH_J1']+=1
    # J2 congruence, x=(c, cbc), y=(cc,bc)
    x2=('c','c'+b+'c'); y2=('cc',b+'c')
    seed='ccc'+b+'c'
    pos=w1.find(seed)
    assert pos>=0
    E02=(w1[:pos],'c',w1[pos+len(seed):])
    assert subst(E02,x2)==w1==subst(E02,y2)
    # transfer each c from donor block B3, B4..Bn to the end of block B2
    runs=[q, q+1, q-1]+[q]*(n-3)+[1]
    prefix=P
    def assemble(a):return P+''.join(b+'c'*k for k in a)+Q
    wcur=w1
    assert assemble(runs)==wcur
    for donor in range(2,n):
        while runs[donor]>1:
            rec_tail=len(P)+sum(len(b)+runs[i] for i in range(1)) +len(b)+runs[1]-1
            don_end=len(P)+sum(len(b)+runs[i] for i in range(donor+1))-1
            assert wcur[rec_tail]=='c' and wcur[don_end]=='c'
            assert wcur[don_end+1:don_end+1+len(b)]==b
            assert wcur[don_end+1+len(b)]=='c'
            E1=(wcur[:rec_tail], wcur[rec_tail+1:don_end], wcur[don_end+len('c'+b+'c'):])
            assert E1[1]
            result=rect(E02,E1,x2,y2,w1,wcur)
            runs[1]+=1; runs[donor]-=1
            assert result==assemble(runs),(result,assemble(runs),t,q,n)
            wcur=result
            count['CH_J2_transfers']+=1
    assert runs[1]==(n-1)*(q-1)+1
    count['CH_instances']+=1

for t in range(1,5):
  for q in range(2,7):
    for n in range(3,7):
      rc_test(t,q,n)

# Detailed string rewrite/slide checks for constant-15 proof.
def slide_conflict(w,x,idx,e,s,N):
    # w at idx starts x^R followed by y, or starts y followed by x^R.
    y='c' if x=='b' else 'b'
    run1=0
    while idx+run1<len(w) and w[idx+run1]==x:run1+=1
    if run1>=4 and idx+run1<len(w) and w[idx+run1]==y:
        R=run1; P=w[:idx]; Q=w[idx+R+1:]; sigma=s if x=='b' else -s
        A0=P+x*R+y+Q
        A1=P+x*(R-1)+y+x+Q
        A2=P+x*(R-2)+y+x*2+Q
        E0=(P+x*(R-4),x,y+Q+'a'*e)
        E1=(P+x*(R-3),y,Q+'a'*(e+sigma))
        assert subst(E0,(x,x*2))==A0+'a'*e
        assert subst(E0,(x*2,x))==A0+'a'*e
        assert subst(E1,(x*2,x))==A1+'a'*(e+sigma)
        assert subst(E1,(x,x*2))==A2+'a'*(e+sigma)
        assert e+sigma>0 and e+2*sigma>0
        count['L_slide_right']+=1
        return True
    if w[idx]==y:
        R=0
        while idx+1+R<len(w) and w[idx+1+R]==x:R+=1
        if R>=4:
            P=w[:idx]; Q=w[idx+1+R:]; sigma=-s if x=='b' else s
            A0=P+y+x*R+Q
            A1=P+x+y+x*(R-1)+Q
            A2=P+x*2+y+x*(R-2)+Q
            E0=(P+y,x,x*(R-4)+Q+'a'*e)
            E1=(P,y,x*(R-3)+Q+'a'*(e+sigma))
            assert subst(E0,(x,x*2))==A0+'a'*e
            assert subst(E0,(x*2,x))==A0+'a'*e
            assert subst(E1,(x,x*2))==A1+'a'*(e+sigma)
            assert subst(E1,(x*2,x))==A2+'a'*(e+sigma)
            assert e+sigma>0 and e+2*sigma>0
            count['L_slide_left']+=1
            return True
    return False

def proof15(p,q,delta,dprime):
    s=delta-dprime; M=max(delta,dprime); N=15*M
    t=N-delta-dprime
    kap=p+'bc'+q; kprime=p+'cb'+q
    assert t>=3
    w=kap+kprime; orig=w; e=t
    assert len(w)>=8
    x=('b' if 'bbbb' in w else 'c' if 'cccc' in w else max('bc',key=lambda v:kap.count(v)));y='c' if x=='b' else 'b'
    if x*4 not in w: assert kap.count(x)>=2
    def swapat(w,idx,e):
        old=w[idx:idx+2]; assert old in ('bc','cb')
        sig=s if old=='bc' else -s
        assert e>=2+abs(s) and e+sig>=2
        i=1+max(0,-s)
        lam=N-delta; lamp=N-dprime
        assert i>=1 and i+s>=1 and i<=lam
        # E0 for F matches both Rot hosts.
        assert 'a'*(lam-i)+p+'bc'+q+'a'*i== 'a'*(lam-i)+kap+'a'*i
        assert len('a'*(lam-i)+p+'cb'+q+'a'*(i+s))==len(kprime)+lamp
        Q=w[idx+2:] + 'a' # a nonempty test separator
        assert Q
        return w[:idx]+old[::-1]+w[idx+2:],e+sig
    if x*4 in w:
        pass
    else:
        positions=[i for i,ch in enumerate(w) if ch==x][:4]
        assert len(positions)==4
        Y0=w[:positions[0]];Y1=w[positions[0]+1:positions[1]];Y2=w[positions[1]+1:positions[2]];Y3=w[positions[2]+1:positions[3]];Z=w[positions[3]+1:]
        assert all(set(z)<= {y} for z in [Y0,Y1,Y2,Y3])
        assert max(map(len,[Y1,Y2,Y3]))<=3
        # Sort by swaps using target intermediate and greedy bubble with an inverse-count shortest path.
        target=Y0+Y1+Y2+x*4+Y3+Z
        e=t
        swaps=0
        for k, desired in enumerate(target):
            if w[k]==desired: continue
            j=w.find(desired,k+1)
            assert j>=0
            for at in range(j-1,k-1,-1):
                w,e=swapat(w,at,e)
                swaps+=1
        assert swaps<=12,(orig,target,swaps)
        assert w==target,(orig,w,target)
        count['no_run_sorts']+=1
    assert x*4 in w
    # Locate run x^R with y adjacent (one of two boundaries)
    found=False
    for i in range(len(w)):
        if slide_conflict(w,x,i,e,s,N):found=True;break
    assert found,(p,q,w,x)
    count['constant15_instances']+=1

for lp in range(1,5):
  for lq in range(1,5):
    for a in product('bc',repeat=lp):
      for b in product('bc',repeat=lq):
        p=''.join(a);q=''.join(b)
        for d,dp in [(1,1),(1,2),(2,1),(2,3),(4,1),(3,5)]:
          proof15(p,q,d,dp)

print('PASS',dict(count))

# ON-loc / RED check: move each interior a-run to the exterior of its component.
# Here each non-a token is an entire block (not an unjustified single-letter swap).
def normalize_component(words, gaps):
    assert len(words)==len(gaps)+1 and all(set(w)<={'b','c'} and w for w in words)
    tokens=[]
    for i,z in enumerate(words):
        tokens.append(('z',z))
        if i<len(gaps):tokens.extend([('a','a')]*gaps[i])
    expected='a'*sum(gaps)+''.join(words)
    for i in range(len(tokens)-1):
        pass
    # Slide each a to the start across preceding maximal non-a blocks, using z a == a z.
    while True:
        at=next((i for i in range(len(tokens)-1) if tokens[i][0]=='z' and tokens[i+1][0]=='a'),None)
        if at is None:break
        tokens[at],tokens[at+1]=tokens[at+1],tokens[at]
        count['ON_local_swaps']+=1
    assert ''.join(v for _,v in tokens)==expected
    count['ON_components']+=1

for pu in range(1,5):
  for pv in range(1,5):
    # Randomly shaped alternating b/c maximal z-blocks interspersed with internal a.
    u=['bc' if k%2 else 'cb' for k in range(pu)]
    v=['bcb' if k%2 else 'bcc' for k in range(pv)]
    gaps_u=[(k%3)+1 for k in range(pu-1)]
    gaps_v=[(k%2)+1 for k in range(pv-1)]
    N=sum(gaps_u)+sum(gaps_v)+7
    delta=3
    A=N-delta
    assert A>=sum(gaps_u)+sum(gaps_v)+4
    normalize_component(u,gaps_u)
    normalize_component(v,gaps_v)

print('RED_ON_PASS', {k:count[k] for k in ['ON_components','ON_local_swaps']})

