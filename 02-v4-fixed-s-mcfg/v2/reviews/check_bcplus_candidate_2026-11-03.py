# Candidate: A_0 -> a | D, A_i -> A_{i-1} A_{i-1} | D, D -> bc | bc D   (start A_n)
# Bounded substitutability test with an exact membership oracle (observation; any violation is a certificate).
import itertools, re, sys
from functools import lru_cache
n=int(sys.argv[1]); MAXLEN=int(sys.argv[2])
DRE=re.compile(r'(bc)+\Z')
@lru_cache(None)
def gen(i,w):
    if DRE.match(w): return True
    if i==0: return w=='a'
    return any(gen(i-1,w[:j]) and gen(i-1,w[j:]) for j in range(1,len(w)))
def mem(w): return len(w)>0 and gen(n,w)
words=[ ''.join(t) for L in range(1,MAXLEN+1) for t in itertools.product('abc',repeat=L) if mem(''.join(t))]
print('words',len(words),'pure a',[w for w in words if set(w)=={'a'}])
def occ(w,d):
    m=len(w)
    if d==1:
        for i in range(m):
            for j in range(i+1,m+1): yield (w[i:j],),(w[:i],w[j:])
    else:
        for i in range(m):
            for j in range(i+1,m):
                for k in range(j+1,m):
                    for h in range(k+1,m+1): yield (w[i:j],w[k:h]),(w[:i],w[j:k],w[h:])
def fill(c,x): return ''.join(c[i]+x[i] for i in range(len(x)))+c[-1]
for d in (1,2):
    D={}; ctxs=set()
    for w in words:
        for x,c in occ(w,d): D.setdefault(x,set()).add(c); ctxs.add(c)
    by={}
    for x,cs in D.items():
        typ=tuple(frozenset(s) for s in x)
        for c in cs: by.setdefault((typ,c),[]).append(x)
    found=None
    for (typ,c),xs in by.items():
        for x,y in itertools.combinations(xs,2):
            for c2 in D[x]-D[y]:
                if not mem(fill(c2,y)): found=(d,x,y,c,c2,fill(c2,x),fill(c2,y)); break
            if found: break
        if found: break
    print('arity',d,'violation' if found else 'none found (bounded)',found)
