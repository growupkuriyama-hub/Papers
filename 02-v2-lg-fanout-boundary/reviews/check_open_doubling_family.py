# Family: E_0 -> a ; E_i -> l E_{i-1} E_{i-1} | c E_{i-1} r   (no closing bracket on the l-branch)
import sys, itertools
def lang(n):
    L=[{'a'}]
    for i in range(1,n+1):
        P=L[-1]; L.append({'l'+x+y for x in P for y in P}|{'c'+x+'r' for x in P})
    return L
def check_cesub(Ln):
    # Clark-Eyraud substitutability: x,y nonempty sharing a context => same distribution
    dist={}
    for w in Ln:
        n=len(w)
        for i in range(n):
            for j in range(i+1,n+1):
                dist.setdefault(w[i:j],set()).add((w[:i],w[j:]))
    byctx={}
    for x,D in dist.items():
        for c in D: byctx.setdefault(c,[]).append(x)
    for c,xs in byctx.items():
        d0=dist[xs[0]]
        for y in xs[1:]:
            if dist[y]!=d0: return False,(xs[0],y,c)
    return True,None
for n in range(1,5):
    L=lang(n); Ln=L[n]
    ok,wit=check_cesub(Ln)
    mua=min(len(w) for w in Ln if w[-1]=='a')
    print(n,len(Ln),'maxlen',max(map(len,Ln)),'CE-substitutable',ok,wit,'mu_a',mua,'n(n+1)+1=',n*(n+1)+1)
