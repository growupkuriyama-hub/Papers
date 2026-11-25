"""Finite checks for Proposition 6.5 (weak FCP is not monotone).

1. Every context (u,v), |u|,|v| <= 2 over the 10-letter alphabet, that accepts
   all sampled nonempty words of L_2 (resp. L_3), including the witnesses
   #cde^ta (resp. #cd^2e^2a), has u in {a,b,#}*, v in {a,b}* and accepts the
   empty word.
2. For all words x of length <= 5, x is accepted by {(e,e),(a#,b)} (resp.
   {(e,e),(b#,a)}) relative to L^+ iff x in L_2 u J_0 (resp. L_3 u J_0).
3. For all words x of length <= 5 and every row of the table in the proof of
   Proposition 6.5, x is accepted by the listed contexts relative to L^+ iff x
   lies in the listed set.
Run: python3 -I tools/check_weak_fcp_s0.py
"""
import re
from itertools import product
def mir(x,s):
    if x.count(s)!=1: return False
    v,z=x.split(s)
    return re.fullmatch(r'[ab#]*',v) is not None and z==v.replace('#','')[::-1]
def ord23(x,which):
    m=re.fullmatch(r'([ab#]*)(c*)(d*)(e*)([ab]*)',x)
    if not m: return False
    p,c,d,e,z=m.groups()
    if '#' in p: w=p.split('#')[0]; free=False
    elif not(c or d or e): w='';free=True
    else: w=p; free=False
    da=w.count('a')-w.count('b')
    if which==2: return len(c)==len(d) and da>=0
    return len(d)==len(e) and da<=0
def l4(x): return re.fullmatch(r'[ab#]*\$[ab]*c*%f*',x) is not None
def l5(x):
    m=re.fullmatch(r'([^%]*)%f*',x)
    if not m: return False
    left=m[1]; tc=len(left)-len(left.rstrip('c'))
    for k in range(tc+1):
        r=left[:len(left)-k]
        mm=re.fullmatch(r'([ab#]*)(c*)(d*)(e*)([ab]*)',r)
        if mm and len(mm[2])==len(mm[3]) and len(mm[4])!=k: return True
    return False
def Lp(x): return mir(x,'$') or mir(x,'@') or ord23(x,2) or ord23(x,3) or l4(x) or l5(x)
A='abcdef#$%@'
def words(al,n):
    for l in range(n+1):
        for t in product(al,repeat=l): yield ''.join(t)
if __name__=="__main__":
  pass
def _main():
    samp={2:[w for w in words('ab#cde',6) if w and ord23(w,2)]+['#cd'+'e'*t+'a' for t in range(6)],
          3:[w for w in words('ab#cde',6) if w and ord23(w,3)]+['#cdde'+'e'+'a']}
    ctx=list(words(A,2)); n=0
    for which,S in samp.items():
        for u in ctx:
            for v in ctx:
                if all(Lp(u+w+v) for w in S):
                    assert re.fullmatch(r'[ab#]*',u) and re.fullmatch(r'[ab]*',v) and Lp(u+v),(which,u,v)
                    n+=1
    print('accepting contexts found',n,'of',2*len(ctx)**2)
    # closures of the S2/S3 diagnostic sets relative to L+ (words up to length 5)
    J0=lambda x: (lambda m: bool(m) and len(m[2])==len(m[3])==len(m[4]))(re.fullmatch(r'([ab#]*)(c*)(d*)(e*)([ab]*)',x))
    cnt=0
    for x in words(A,5):
        assert (Lp(x) and Lp('a#'+x+'b'))==(ord23(x,2) or J0(x)),x
        assert (Lp(x) and Lp('b#'+x+'a'))==(ord23(x,3) or J0(x)),x
        cnt+=1
    print('closure checks',cnt)
def _table():
    bal=lambda w: w.count('a')==w.count('b')
    full=lambda p,x: re.fullmatch(p,x) is not None
    def J0(x):
        m=re.fullmatch(r'([ab#]*)(c*)(d*)(e*)([ab]*)',x); return bool(m) and len(m[2])==len(m[3])==len(m[4])
    def mir(x,sep):
        if x.count(sep)!=1: return False
        v,z=x.split(sep); return full(r'[ab#]*',v) and z==v.replace('#','')[::-1]
    def L45(x):
        if full(r'[ab#]*\$[ab]*c*%f*',x): return True
        m=re.fullmatch(r'([^%]*)%f*',x)
        if not m: return False
        left=m[1]; tc=len(left)-len(left.rstrip('c'))
        for k in range(tc+1):
            mm=re.fullmatch(r'([ab#]*)(c*)(d*)(e*)([ab]*)',left[:len(left)-k])
            if mm and len(mm[2])==len(mm[3]) and len(mm[4])!=k: return True
        return False
    def U(x):
        m=re.fullmatch(r'(e*)([ab]*)(c*)',x); return bool(m) and len(m[1])!=len(m[3])
    rows={'Q':([('','#cd'),('a','b#de')], lambda x: full('[ab]*',x) and bal(x)),
     'F':([('','cd'),('','ade')], lambda x: full(r'[ab]*#[ab#]*',x) and bal(x.split('#')[0])),
     'H':([('a#c','d')], lambda x: full('c*d*',x) and x.count('c')==x.count('d')),
     'E':([('a#cd','e')], lambda x: full('e*',x)),
     'C':([('b#c','de')], lambda x: full('c*',x)),
     'J':([('b#d','e')], lambda x: full('d*e*',x) and x.count('d')==x.count('e')),
     'T':([('$','a%')], lambda x: full('[ab]*',x)),
     'U':([('e','c%')], U),
     'S45':([('','f')], L45),
     'S2':([('',''),('a#','b')], lambda x: ord23(x,2) or J0(x)),
     'S3':([('',''),('b#','a')], lambda x: ord23(x,3) or J0(x)),
     'S1':([('a#','a'),('b#','b')], lambda x: mir(x,'$') or mir(x,'@') or J0(x))}
    n=0
    for x in words('abcdef#$%@',5):
        for A,(C,f) in rows.items():
            assert all(Lp(u+x+v) for u,v in C)==f(x),(A,x)
            n+=1
    print('table checks',n)
if __name__=="__main__":
    _main()
    _table()
