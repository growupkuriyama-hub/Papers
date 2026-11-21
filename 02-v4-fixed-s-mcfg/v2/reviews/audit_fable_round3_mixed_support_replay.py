#!/usr/bin/env python3
"""Independent literal Rect-step replay for Fable Round 3 mixed-support minimal obstruction.
Checks the proof *as a conditional derivation* from MS-provided words and
content-typed arity 1/2 rectangular closure; no grammar membership or
universal tuple-substitutability is inferred from finite tests.
"""
from collections import Counter

J, K = 'bc', 'bbcc'

def alph(w): return frozenset(w)
def apply(E, tup):
    assert len(E) == len(tup) + 1
    assert all(tup) and (len(tup) == 1 or E[1] != '')
    return ''.join(z for pair in zip(E, tup + ('',)) for z in pair)

def check_rect(L, x, y, E0, E1, name, *, both=False):
    assert len(x)==len(y) in (1,2), (name,x,y)
    assert all(alph(a)==alph(b) for a,b in zip(x,y)), (name,'type mismatch')
    w0x,w0y,w1x,w1y=[apply(E,t) for E,t in ((E0,x),(E0,y),(E1,x),(E1,y))]
    assert w0x in L and w0y in L and w1x in L, (name, w0x in L,w0y in L,w1x in L)
    L.add(w1y)
    if both:
        assert w0x == w0y, (name, 'not same host')
    return w1y

def run(N, d, D):
    assert 2 * max(d,D)<=N-4 and d>0 and D>0
    M=N-d-D
    k=max(1,1+D-d)
    assert k-(D-d)>=1 and N-2*d-k>=0
    # All 5 words are MS outputs; do not infer them from unproved finite closure.
    WJ=J*2+'a'*(N-d)
    WK=K*2+'a'*(N-D)
    WJJ=J*4+'a'*(N-2*d)
    WJK=(J+K)*2+'a'*M
    WKK=K*4+'a'*(N-2*D)
    L={WJ,WK,WJJ,WJK,WKK,'a'*N}
    def do(x,y,E0,E1,name,both=False):
        return check_rect(L,x,y,E0,E1,name,both=both)
    # A: J->K with compensating a offset in the second half of WJJ.
    w_A=do((J*2+'a'*k,), (K*2+'a'*(k-(D-d)),),
           ('','a'*(N-d-k)),(J*2,'a'*(N-2*d-k)),'A')
    assert w_A == J*2+K*2+'a'*M
    # C: two-hole cost-free conversion, common WJK and A host.
    x,y=(K,'c'),('bcb','cc')
    e0=(J,'b',K+'a'*M)
    assert apply(e0,x)==WJK and apply(e0,y)==w_A
    # N: max b,c run <=2 is untenable.
    w_N=do(x,y,e0,('','bbc','a'*(N-D)),'N')
    assert w_N == 'bcbbbccc'+'a'*(N-D)
    # R1 and R2: c^4 acceptance from WKK.
    v1=do(x,y,e0,(K*2,'bbc','a'*(N-2*D)),'R1')
    assert v1 == K*2+J+'bbbccc'+'a'*(N-2*D)
    v2=do(x,y,e0,(K,'bcbbb','cc'+'a'*(N-2*D)),'R2')
    assert v2=='bbccbcbbcbbbcccc'+'a'*(N-2*D)
    # Rc: 4 consecutive c's contain two cuts with same word as host.
    e0c=('bbccbcbbcbbb','c','a'*(N-2*D))
    assert apply(e0c,('cc','c'))==v2
    w2=do(('cc','c'),('c','cc'),e0c,('bcbb','b',K+'a'*M),'Rc',both=True)
    assert w2=='bcbbcbccbbcc'+'a'*M
    # From WJK and w2 obtain the universal one-hole congruence cb~bc.
    e0c1=('bcbbc','c'+K+'a'*M)
    assert apply(e0c1,('cb',))==WJK
    assert apply(e0c1,('bc',))==w2
    # Bubble sorting needs only one valid common host for cb<->bc.
    for base,e in ((J*4,N-2*d),(K*2,N-D)):
        w=base+'a'*e
        while 'cb' in w:
            ix=w.find('cb')
            w=do(('cb',),('bc',),e0c1,(w[:ix],w[ix+2:]),'Sort')
        assert w=='bbbbcccc'+'a'*e
    p,q=N-2*d,N-D
    if p!=q:
        big,small=max(p,q),min(p,q)
        # Same non-a word, two accepted a-suffixes. One-hole substitution
        # in a^N produces an a-only word shorter than N.
        short=do(('a'*big,),('a'*small,),('bbbbcccc',''),('','a'*(N-big)),'Ushift')
        assert short=='a'*(N-(big-small))
        assert 0 < len(short) < N
    return dict(N=N,d=d,D=D,conclusion='contradiction' if d*2!=D else 'consistent')

if __name__=='__main__':
    checked=0;contrad=0;equal=0
    for d in range(1,15):
        for D in range(1,15):
            for N in range(max(7,2*max(d,D)+4), min(65,2*max(d,D)+13)):
                s=run(N,d,D)
                checked+=1
                contrad+=(s['conclusion']=='contradiction')
                equal+=(s['conclusion']=='consistent')
    print('Rect proof-path replay: PASS',checked,'parameter triples,',contrad,'contradictions,',equal,'equal-deficit controls')
    print('Original manuscript theorem is conditional on MS seeds; tests do not verify MS itself.')
