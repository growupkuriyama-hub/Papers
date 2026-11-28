from itertools import product
from functools import lru_cache

# ASCII: floor [ ], ceiling ( ), terminal a.
@lru_cache(None)
def A(j):
    if j == 0: return frozenset({'a'})
    prev=A(j-1)
    return frozenset({'('+x+')' for x in prev} | {'['+x+y+']' for x,y in product(prev,repeat=2)})
def w(j):
    return 'a' if j==0 else '['+w(j-1)*2+']'
def u(j): return '('*j+'a'+')'*j

def root_children(t):
    if t[0]=='(': return (t[1:-1],)
    depth=0
    for j,c in enumerate(t[1:-1],1):
        depth += (c in '[(')-(c in '])')
        if depth==0: return (t[1:j+1],t[j+1:-1])
    raise AssertionError(t)

def quotient(M,c):
    p,q=c
    return frozenset(t[len(p):len(t)-len(q)] for t in M if len(t)>=len(p)+len(q) and t.startswith(p) and t.endswith(q))

def contexts_of_factor(M,x):
    out=set()
    for t in M:
        start=0
        while (j:=t.find(x,start))>=0:
            out.add((t[:j],t[j+len(x):])); start=j+1
    return out

def key(c,order):
    return tuple((len(x),tuple(order.index(a) for a in x)) for x in c)

def main():
    for n in range(2,5):
        M=A(n)-{w(n)}; prev=A(n-1); C=set()
        for t in M:
            ch=root_children(t)
            if len(ch)==1: c=('(',')')
            elif '(' in ch[1]: c=('[',ch[1]+']')
            else:
                assert '(' in ch[0]; c=('['+ch[0],']')
            assert t.startswith(c[0]) and t.endswith(c[1]); C.add(c)
        assert all(quotient(M,c)==prev for c in C)
        bad={(x,y) for x,y in product(prev,repeat=2) if '['+x+y+']' not in M}
        assert bad=={(w(n-1),w(n-1))}
        # SPP for the exact grammar, checking even the overapproximation at state 1.
        X={(j,0):quotient(M,('('*(n-j),')'*(n-j))) for j in range(n)}
        X.update({(j,1):frozenset(x for x in quotient(M,('('*(n-j),')'*(n-j))) if '(' in x) for j in range(1,n)})
        X[n,1]=M; assert 'a' in X[0,0]
        rules=1
        for (j,flag),v in X.items():
            if j==0: continue
            for a,b in product(range(2),repeat=2):
                if (j-1,a) in X and (j-1,b) in X and flag==(a|b):
                    assert all('['+x+y+']' in v for x,y in product(X[j-1,a],X[j-1,b])); rules+=1
            if flag:
                for a in range(2):
                    if (j-1,a) in X:
                        assert all('('+x+')' in v for x in X[j-1,a]); rules+=1
        assert rules==6*n-4
        # Exhaust all contexts accepting w_j. Any representative of A_j is among these.
        for order in ('a[]()','a()[]'):
            canonical=[]
            for j in range(n):
                candidates=sorted(contexts_of_factor(M,w(j)),key=lambda c:key(c,order))
                actual=next(c for c in candidates if quotient(M,c)==A(j))
                expected=('('*(n-j),')'*(n-j)) if order.index('(')<order.index('[') else ('['*(n-j),''.join(u(h)+']' for h in range(j,n)))
                assert actual==expected; canonical.append(actual)
            sample=canonical[0][0]+'a'+canonical[0][1]
            assert sample in M
            assert all(sample.startswith(p) and sample.endswith(q) and len(sample)>=len(p)+len(q) for p,q in canonical)
            print(f'n={n} order={order} canonical singleton data length={len(sample)}')
        print(f'n={n} |M|={len(M)} root context classes checked={len(C)} bad pairs={len(bad)} SPP rules={rules}: PASS')
if __name__=='__main__': main()
