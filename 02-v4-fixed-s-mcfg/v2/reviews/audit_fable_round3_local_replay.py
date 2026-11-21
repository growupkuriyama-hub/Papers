#!/usr/bin/env python3
"""Independent symbolic/direct-context checks for Fable Round 3 framed AB.
No data/code imported from Fable; no language closure claim.
"""
from itertools import product

checked={'F':0,'S':0,'X':0,'T1':0,'T1p':0,'C4':0,'T2_paths':0,'T2_steps':0}

def A(k):
    assert k>=0
    return 'a'*k

def E(ctx,tup):
    if len(tup)==1:
        l,r=ctx
        return l+tup[0]+r
    l,m,r=ctx
    assert m, 'empty 2-hole separator'
    assert all(tup), 'empty component'
    return l+tup[0]+m+tup[1]+r

def ts(t): return tuple(frozenset(w) for w in t)

def rectangle(x,y,e0,e1,left,right,common=None):
    assert ts(x)==ts(y), (x,y,ts(x),ts(y))
    v0=E(e0,x); w0=E(e0,y)
    v1=E(e1,x); w1=E(e1,y)
    assert v1==left and w1==right, (x,y,e1,left,right,v1,w1)
    if common is not None: assert v0==common and w0==common,(v0,w0,common)
    return v0,w0

def F(p,q,N,d,d2,prefix,suf,word,outword,sign=1):
    k=p+'bc'+q; kk=p+'cb'+q
    lam=N-d; s=d-d2
    i=1+max(0,-s)
    assert 1<=i<=lam and i+s>=1
    v=(('bc','a'*i),('cb','a'*(i+s)))
    if sign<0: v=v[::-1]
    e0=(A(lam-i)+p,q,'')
    e1=(prefix,suf[0],suf[1])
    assert word==E(e1,v[0]) and outword==E(e1,v[1])
    c0,c1=rectangle(*v,e0,e1,word,outword)
    assert set((c0,c1))==set((A(lam-i)+k+A(i),A(lam-i)+kk+A(i+s)))
    assert (lam-i)+i==lam and (lam-i)+(i+s)==N-d2
    checked['F']+=1

def S(x1,m,y2,e0,e1,accepted0,accepted1,outword,order=1):
    x=(x1,m+y2);y=(x1+m,y2)
    if order<0: x,y=y,x
    v0,w0=rectangle(x,y,e0,e1,accepted1,outword,accepted0)
    checked['S']+=1

def X(N,d,d2,k,kk):
    s=d-d2;lam=N-d; t=N-d-d2;i=1+max(0,-s);j=i
    assert t>=2+abs(s)
    # first left-side replacement a^i k to a^(i+s) kk
    x=(A(i)+k,);y=(A(i+s)+kk,)
    e0=('',A(lam-i))
    e1=('',kk+A(t-i))
    w0=A(i)+k+kk+A(t-i)
    w1=A(i+s)+kk+kk+A(t-i)
    v0,v1=rectangle(x,y,e0,e1,w0,w1)
    assert v0==A(i)+k+A(lam-i) and v1==A(i+s)+kk+A(lam-i)
    # reverse trailing replacement: kk a^(j+s) -> k a^j
    x=(kk+A(j+s),);y=(k+A(j),)
    e0=(A(lam-j),'')
    e1=(A(i+s)+kk,A(t-i-j-s))
    out=A(i+s)+kk+k+A(t-i-s)
    v0,v1=rectangle(x,y,e0,e1,w1,out)
    assert v0==A(lam-j)+kk+A(j+s) and v1==A(lam-j)+k+A(j)
    checked['X']+=1
    return kk+k+A(t)

def T1(N,d,d2):
    M=max(d,d2);s=d-d2
    if N<2*M+1 or N-d-d2<3: return
    k='bbccc';kk='bcbcc';p='b';q='cc';t=N-d-d2;lam2=N-d2;i=1+max(0,-s)
    assert t>=i
    w0=k+kk+A(t)
    w1=k+'cb'+'bcc'+A(t+s)
    F(p,q,N,d,d2,k,('bcc',A(t-i)),w0,w1)
    v0=kk+A(lam2);v1='bccbc'+A(lam2)
    S('c','c','c',('bb','c','bbcc'+A(t+s)),('b','b',A(lam2)),w1,v0,v1)
    w4='bccbc'+A(lam2+s)
    F(p,q,N,d,d2,'bc',('c',A(lam2-i)),v0,w4)
    assert lam2>=1 and lam2+s>=1 and 0<abs(s)<N if s else True
    checked['T1']+=1

def T1p(N,d,d2):
    M=max(d,d2);s=d-d2
    if N<2*M+2 or N-d-d2<3: return
    k='bbbcc';kk='bbcbc';p='bb';q='c';t=N-d-d2;lam2=N-d2;i=1+max(0,-s)
    w0=X(N,d,d2,k,kk)
    w1='bbc'+'cb'+'bbbcc'+A(t+s)
    F(p,q,N,d,d2,'bbc',('bbbcc',A(t-i)),w0,w1)
    v0=kk+A(lam2);v1='bcbbc'+A(lam2)
    S('b','b','b',('bbcc','b','cc'+A(t+s)),('','c','c'+A(lam2)),w1,v0,v1,order=-1)
    w4='bcbbc'+A(lam2+s)
    F(p,q,N,d,d2,'b',('bc',A(lam2-i)),v0,w4)
    checked['T1p']+=1

def C4(N,d,d2):
    M=max(d,d2);s=d-d2
    if N<2*M+2 or N-d-d2<3: return
    k='bbcc';kk='bcbc';p='b';q='c';t=N-d-d2;i=1+max(0,-s)
    w0=k+kk+A(t)
    w1=k+'cb'+'bc'+A(t+s)
    F(p,q,N,d,d2,k,('bc',A(t-i)),w0,w1)
    rev=X(N,d,d2,k,kk)
    w2='bccbbbcc'+A(t)
    S('c','c','bbc',('bb','c',A(t+s)),('b','b','c'+A(t)),w1,rev,w2)
    w3='bccbbbcc'+A(t+s)
    F(p,q,N,d,d2,'bc',('bbcc',A(t-i)),rev,w3)
    checked['C4']+=1

def swap_run(w,first,last):
    """Adjacent bubble-swap path on b/c strings; checks Hamming 2 & inversion step."""
    path=[w]
    w=list(w)
    for i in range(len(first)):
        if w[i]!=first[i]:
            j=next(j for j in range(i+1,len(w)) if w[j]==first[i])
            for k in range(j,i,-1):
                assert w[k]!=w[k-1]
                w[k],w[k-1]=w[k-1],w[k]
                path.append(''.join(w))
    assert ''.join(w)==first
    if first!=last:
        w=list(first)
        for i in range(len(last)):
            if w[i]!=last[i]:
                j=next(j for j in range(i+1,len(w)) if w[j]==last[i])
                for k in range(j,i,-1):
                    assert w[k]!=w[k-1]
                    w[k],w[k-1]=w[k-1],w[k]
                    path.append(''.join(w))
        assert ''.join(w)==last
    return path

def inv(w): return sum(1 for i,a in enumerate(w) if a=='c' for b in w[i+1:] if b=='b')

def T2(N,d,d2,p,q):
    k=p+'bc'+q;kk=p+'cb'+q;n=len(k);s=d-d2;t=N-d-d2
    M=max(d,d2)
    assert n>=4 and N>=(n*n+2*n)*M
    w0=k+kk
    x='b' if k.count('b')>=2 else 'c';y='c' if x=='b' else 'b'
    m=w0.count(x);l=w0.count(y)
    assert m>=4 and l>=2
    V1=x*m+y*l;V2=x+y+x*(m-1)+y*(l-1);V3=x+x+y+x*(m-2)+y*(l-1)
    path=swap_run(w0,V1,V2)
    path.append(V3)
    assert len(path)-1<=n*n+2*n-2,(k,len(path)-1,n*n+2*n-2)
    for pos,(wa,wb) in enumerate(zip(path,path[1:])):
        assert len(wa)==len(wb)
        diffs=[i for i in range(len(wa)) if wa[i]!=wb[i]]
        assert len(diffs)==2 and diffs[1]==diffs[0]+1
        i0=diffs[0]
        assert wa[i0:i0+2] in ('bc','cb') and wb[i0:i0+2]==wa[i0:i0+2][::-1]
        e=t+s*(inv(wa)-inv(w0));en=t+s*(inv(wb)-inv(w0))
        assert en-e==s*(inv(wb)-inv(wa))
        assert e>=2+abs(s)
        if i0+2==len(wa):
            # Q=a, second a-hole must remain positive after reserving a
            gap='a';post=A(e-1)
        else:
            gap=wa[i0+2:];post=A(e)
        prefix=wa[:i0]
        # F picks up a standard sub-run in the final a-run
        ii=1+max(0,-s)
        direction=1 if wa[i0:i0+2]=='bc' else -1
        exp_before=ii if direction==1 else ii+s
        assert len(post)>=exp_before
        suff=(gap,A(len(post)-exp_before))
        F(p,q,N,d,d2,prefix,suff,wa+A(e),wb+A(en),sign=direction)
        checked['T2_steps']+=1
    # verify slide in two-hole with E0 at V1 and E1 at V2
    e1=t+s*(inv(V1)-inv(w0));e2=t+s*(inv(V2)-inv(w0));e3=t+s*(inv(V3)-inv(w0))
    S(x,x,x,('',x,x*(m-4)+y*l+A(e1)),('',y,x*(m-3)+y*(l-1)+A(e2)),V1+A(e1),V2+A(e2),V3+A(e2))
    assert abs(e3-e2)==abs(s)
    checked['T2_paths']+=1

if __name__=='__main__':
    for d in range(1,7):
      for d2 in range(1,7):
        M=max(d,d2)
        for N in range(max(3,2*M+1),2*M+9):
            T1(N,d,d2)
            T1p(N,d,d2)
            C4(N,d,d2)
    bs=['b','c']
    words=[ ''.join(p) for m in range(1,4) for p in product(bs,repeat=m)]
    for p,q in product(words,repeat=2):
        k=p+'bc'+q;n=len(k)
        for d,d2 in product(range(1,4),repeat=2):
            N=max(7,(n*n+2*n)*max(d,d2))
            T2(N,d,d2,p,q)
    print('PASS',checked)
