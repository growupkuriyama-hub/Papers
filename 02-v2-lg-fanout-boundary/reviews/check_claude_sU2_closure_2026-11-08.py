import sys, itertools, random
from collections import defaultdict
def typ(x): return 'b' in x
def close(seed, Lmax, maxw=20000):
    L=set(seed)
    while True:
        D=defaultdict(set)
        for w in L:
            n=len(w)
            for i in range(n):
                for j in range(i+1,n+1): D[w[i:j]].add((w[:i],w[j:]))
        byctx=defaultdict(list)
        for x,cs in D.items():
            for c in cs: byctx[(typ(x),c)].append(x)
        # union-find classes of factors sharing a context
        parent={}
        def f(x):
            while parent.get(x,x)!=x: x=parent[x]
            return x
        for xs in byctx.values():
            r=f(xs[0])
            for y in xs[1:]:
                ry=f(y)
                if ry!=r: parent[ry]=r
        cls=defaultdict(list)
        for x in D: cls[f(x)].append(x)
        new=set()
        for xs in cls.values():
            if len(xs)<2: continue
            ctx=set().union(*(D[x] for x in xs))
            for x in xs:
                for (l,r) in ctx:
                    w=l+x+r
                    if w not in L:
                        if len(w)>Lmax: return L,'overflow'
                        new.add(w)
        if not new: return L,'closed'
        L|=new
        if len(L)>maxw: return L,'toobig'
def doubling(ms,n):
    E=[{'a'}]
    for i in range(1,n+1): E.append({x+y for x in E[-1] for y in E[-1]}|{ms[i-1]})
    return E[n]
if __name__=="__main__":
  random.seed(int(sys.argv[1]))
  bw=[''.join(p) for k in range(1,5) for p in itertools.product('ab',repeat=k) if 'b' in p]
  n=int(sys.argv[2]); N=2**n
  stats=defaultdict(int)
  for trial in range(int(sys.argv[3])):
      ms=[random.choice(bw) for _ in range(n)]
      seed=doubling(ms,n)
      L,st=close(seed,N+int(sys.argv[4]))
      pure=sorted(len(w) for w in L if 'b' not in w)
      key=(st, 'shorter_pure' if pure and pure[0]<N else 'ok')
      stats[key]+=1
      if st=='closed' and key[1]=='ok': print("SURVIVOR",ms,len(L),pure[:3])
  print(dict(stats))
  