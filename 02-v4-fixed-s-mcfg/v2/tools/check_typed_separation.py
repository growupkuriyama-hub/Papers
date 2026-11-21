# Brute-force check on words up to length N of the separation language
# L = { a^m X b^n Y c^m' Z d^n : m' in {m, m-1}, m'>=0 }, typing s = (#a+#c) mod 2.
import itertools, re
N=11
pat=re.compile(r'^(a*)X(b*)Y(c*)Z(d*)$')
def inL(w):
    m_=pat.match(w)
    if not m_: return False
    A,B,C,D=map(len,m_.groups())
    return B==D and (C==A or C==A-1)
s=lambda w:(w.count('a')+w.count('c'))%2
words=[]
for m in range(0,6):
  for n in range(0,4):
    for mp in (m,m-1):
      if mp<0: continue
      w='a'*m+'X'+'b'*n+'Y'+'c'*mp+'Z'+'d'*n
      if len(w)<=N: words.append(w)
Lset=set(words)
# collect all d-tuple occurrences (d=1,2) with admissible contexts, from words of L up to length N
def occ(w,d):
    n=len(w)
    cuts=range(n+1)
    for cs in itertools.combinations(cuts,2*d):
        ok=all(cs[2*i]<cs[2*i+1] for i in range(d)) and all(cs[2*i+1]<cs[2*i+2] for i in range(d-1))
        if not ok: continue
        x=tuple(w[cs[2*i]:cs[2*i+1]] for i in range(d))
        parts=[w[:cs[0]]]+[w[cs[2*i+1]:cs[2*i+2]] for i in range(d-1)]+[w[cs[-1]:]]
        yield x,tuple(parts)
def fill(E,x):
    r=E[0]
    for i,xi in enumerate(x): r+=xi+E[i+1]
    return r
viol_typed=0; viol_triv=0
for d in (1,2):
    ctx={}
    for w in words:
        for x,E in occ(w,d):
            ctx.setdefault(x,set()).add(E)
    tuples=list(ctx)
    allctx=set().union(*ctx.values())
    # distributions restricted to contexts seen (finite approximation) and membership by inL (exact)
    for x,y in itertools.combinations(tuples,2):
        if ctx[x]&ctx[y]:
            Dx={E for E in allctx if inL(fill(E,x))}
            Dy={E for E in allctx if inL(fill(E,y))}
            if Dx!=Dy:
                same=all(s(a)==s(b) for a,b in zip(x,y))
                if same: viol_typed+=1; print('TYPED VIOLATION',d,x,y)
                else: viol_triv+=1
print('words',len(words),'typed violations',viol_typed,'untyped violations',viol_triv)
