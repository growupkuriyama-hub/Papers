from itertools import combinations
from collections import defaultdict
from functools import lru_cache

ALPH='abc'
def content(s): return frozenset(s)
def fill(context, parts):
    assert len(context)==len(parts)+1
    return ''.join(context[i]+parts[i] for i in range(len(parts)))+context[-1]
def occurrences(w,d):
    n=len(w)
    if d==1:
        for i in range(n):
            for j in range(i+1,n+1):
                yield (w[i:j],),(w[:i],w[j:])
    if d==2:
        for i in range(n):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    for l in range(k+1,n+1):
                        yield (w[i:j],w[k:l]),(w[:i],w[j:k],w[l:])
def implications(words,ds=(1,2)):
    known=set(words); dists=defaultdict(set); shared=defaultdict(set)
    for w in sorted(known):
        for d in ds:
            for x,e in occurrences(w,d):
                dists[x].add(e)
                shared[(d,tuple(content(t) for t in x),e)].add(x)
    res={}
    for (d,t,e), xs in sorted(shared.items(), key=lambda kv:str(kv[0])):
        if len(xs)<2:continue
        for x in sorted(xs):
            for y in sorted(xs):
                if x==y:continue
                for f in sorted(dists[x]):
                    z=fill(f,y)
                    if z not in known:
                        res.setdefault(z,(e,x,y,f))
    return res

def goodstep(s,e,x,y,f):
    assert len(x)==len(y)==len(e)-1==len(f)-1
    assert 1<=len(x)<=2
    assert all(xi and yi and content(xi)==content(yi) for xi,yi in zip(x,y))
    assert len(x)==1 or (e[1] and f[1])
    assert fill(e,x) in s,(e,x,y,f,'E[x]')
    assert fill(e,y) in s,(e,x,y,f,'E[y]')
    assert fill(f,x) in s,(e,x,y,f,'F[x]')
    return fill(f,y)

def language(es):
    x={'ab'}
    for e in es:
        x={u+v for u in x for v in x}|{e}
    return x

# Independently check user/provided archive statements about finite K and a new 2-step example.
K={'abab','abc','cab','cc','ac'}
rK=implications(K)
print('K size',len(K),'C2 implications',len(rK),'min-ab',min(len(x) for x in K if content(x)=={'a','b'}))

Sdeg=language(('c','cc','c'))
extra_deg=implications(Sdeg,(1,2))
assert extra_deg
print('degenerate m3 seeds',len(Sdeg),'missing one-step consequences',len(extra_deg),
      'first',sorted(extra_deg)[0])

# New parametric two-step case, and exhaustive *one-step* C_{2,c} check for k<=8.
for k in range(1,9):
    w='a'*k+'ba'; seeds={w,'c'+'a'*k+'b','c'+'a'*(2*k)+'b'}
    direct=implications(seeds,(1,2))
    assert not any(content(z)=={'a','b'} and len(z)<len(w) for z in direct)
    state=set(seeds)
    steps=[(('c',''),('a'*k+'b',),('a'*(2*k)+'b',),('','a')),
           (('a'*k,''),(w,),('ba',),('',''))]
    for step in steps:state.add(goodstep(state,*step))
    assert 'ba' in state
    print('S_k k',k,'N',len(w),'one-step-consequences',len(direct),'direct-shortcuts',0,
          'two-step-result','ba','ratio',f'2/{len(w)}')
    if k==2:
        for z,st in sorted(direct.items()):print('  direct-candidate',z,'step=',st)

# Two-hole slot transport (general result instantiated by the n=2 doubling grammar).
seeds=language(('abc','aacb'))
e=('','ab','');x=('ab','abab');y=('abab','ab');f=('','c','')
assert fill(e,x)==fill(e,y)=='abababab'
out=goodstep(seeds,e,x,y,f)
assert out=='ababcab' and out not in seeds
print('L2 slot transfer E[x]=E[y]=',fill(e,x),'F[x]=',fill(f,x),'F[y]=',out,'absent=',out not in seeds)

# Exact lifted symbolic two-step certificate, n=3,...,8.
for n in range(3,9):
    es=['abc' if i==1 else 'a'*i+'cb' for i in range(1,n+1)]
    u='ab'*(2**(n-1)-2); z='abab';beta='a'*(n-1)+'cb'; e='abc';s='a'
    seeds={beta+beta,beta+u+e,u+z+u+z,u+z+u+e,s+beta}
    # verify only explicitly required seeds using grammar exact membership with recursion, no exponential enumeration
    @lru_cache(None)
    def member(i,w):
        if i==0:return w=='ab'
        if w==es[i-1]:return True
        for t in range(1,len(w)):
            if member(i-1,w[:t]) and member(i-1,w[t:]):return True
        return False
    assert all(member(n,w) for w in seeds)
    steps=[((beta,''),(beta,),(u+e,),(s,'')),(('',e),(u+z+u,),(s+u,),('',z))]
    known=set(seeds)
    for ee,xx,yy,ff in steps:known.add(goodstep(known,ee,xx,yy,ff))
    target=s+u+z
    assert target in known
    print('L_n n',n,'N',2**(n+1),'result',len(target),'ratio',str(len(target))+'/'+str(2**(n+1)))

from itertools import product
alpha='ab'
seen=0;hits=[];both=0
for N in (4,5):
    for Wt in map(''.join,product(alpha,repeat=N)):
        if content(Wt)!={'a','b'}:continue
        for i in range(N):
            for j in range(i+1,N+1):
                orig=Wt[i:j];ty=content(orig)
                if ty!={'a','b'}:continue
                for m in (len(orig)+1,len(orig)+2):
                    for ytuple in product(alpha,repeat=m):
                        longer=''.join(ytuple)
                        if content(longer)!=ty:continue
                        for p,q in (('c',''),('','c'),('ca',''),('','ac'),('bc',''),('','cb'),('c','a'),('b','c')):
                            seeds={Wt,p+orig+q,p+longer+q}
                            if len(seeds)<3:continue
                            seen+=1
                            s1=implications(seeds,(1,))
                            if any(content(z)=={'a','b'} and len(z)<N for z in s1):continue
                            # all one-step consequences with length <=N+5
                            mids={z for z in s1 if len(z)<=N+5}
                            S2=seeds|mids
                            s2=implications(S2,(1,))
                            for z,cert in s2.items():
                                if content(z)=={'a','b'} and len(z)<N and 'c' not in ''.join(cert[0]):
                                    hits.append((Wt,orig,longer,p,q,z,cert,len(s1)))
                                    print('FOUND',hits[-1]);break
                            if hits:break
                        if hits:break
                    if hits:break
                if hits:break
            if hits:break
        if hits:break
    if hits:break
print('EXP search checked=',seen,'hits=',len(hits))

# Replay ten concrete archived certificates, without importing their previous solver.
# Each entry is (case name, (e1,e2,e3), explicit E/x/y/F steps).
CASES = [
 ('c^i',('c','cc','ccc'), [
  (('','cc'),('cc',),('c',),('abababab','')),
  (('','abababc'),('ababab',),('ab',),('','ababababab'))]),
 ('a^(i-1)c',('c','ac','aac'), [
  (('','c'),('abababababab',),('ababababa',),('','abab'))]),
 ('ca^(i-1)',('c','ca','caa'), [
  (('c',''),('abababababab',),('aabababab',),('','abab'))]),
 ('cb^(i-1)',('c','cb','cbb'), [
  (('c',''),('abababababab',),('babababab',),('','abab'))]),
 ('b^(i-1)c',('c','bc','bbc'), [
  (('','bc'),('abababababa',),('abababab',),('','babab'))]),
 ('c(ab)^(i-1)',('c','cab','cabab'), [
  (('ababababc',''),('abab',),('ab',),('','abababababab'))]),
 ('ac^ib',('acb','accb','acccb'), [
  (('ac',''),('cbabababab',),('bababababacb',),('ababa','')),
  (('','abababababacb'),('abab',),('ab',),('','abababababab'))]),
 ('priority ac,cc,c',('ac','cc','c'), [
  (('',''),('c',),('cccc',),('ababa','abababab')),
  (('',''),('ccabababab',),('ababacacac',),('ababacc','')),
  (('','c'),('ababababaca',),('ababacc',),('','bab')),
  (('',''),('c',),('cccc',),('ababa','acac')),
  (('',''),('ababaccc',),('ababaccbab',),('','cacac')),
  (('ababacc','cacac'),('ababa',),('bab',),('','bababababab'))]),
 ('priority ca,bbc,abc',('ca','bbc','abc'), [
  (('',''),('abc',),('ababababbbc',),('bbcab','a')),
  (('',''),('abc',),('caababbbc',),('bbcab','a')),
  (('','ababbbca'),('bbcababab',),('bbcabca',),('','ab')),
  (('',''),('abc',),('bbcabababab',),('bbc','aab')),
  (('','c'),('ab',),('ababababbb',),('bbcca','ab')),
  (('','abab'),('caabababab',),('bbcabab',),('bbc','bbab')),
  (('bbcbbc','ab'),('ababababa',),('ababbb',),('','bababab'))]),
 ('priority cc,ac,c',('cc','ac','c'), [
  (('abab',''),('ababababcc',),('ababac',),('','cc')),
  (('',''),('c',),('cccccccc',),('abab','cac')),
  (('',''),('ababcccccc',),('ababababac',),('','cccac')),
  (('',''),('ababaccc',),('ababababac',),('abab','cac')),
  (('','ccac'),('ababababababa',),('abab',),('','bab'))]),
]
for name,es,steps in CASES:
    known=language(es)
    for i,step in enumerate(steps,1):
        z=goodstep(known,*step)
        known.add(z)
    assert content(z)=={'a','b'} and len(z)<16
    finale=steps[-1]
    e_has_c=('c' in ''.join(finale[0]))
    print('ARCHIVED',name,'steps',len(steps),'result',z,'length',len(z),'saved',16-len(z),
          'last-E-has-c',e_has_c)
