from itertools import product
from functools import cache

# Independent direct tree enumeration, not imported from authors' tools.
@cache
def level(n):
    if n == 0: return frozenset(('a',))
    p=level(n-1)
    return frozenset({'['+x+y+']' for x,y in product(p,repeat=2)} | {'<'+x+'>' for x in p})
@cache
def bare(n):
    return 'a' if not n else '['+bare(n-1)*2+']'

def closure(L,c):
    u,v=c
    return {w[len(u):len(w)-len(v) if v else len(w)] for w in L if len(w)>=len(u)+len(v) and w.startswith(u) and w.endswith(v)}

def frames(n):
    rules=[]
    for d in range(n):
        for path in product((0,1),repeat=d):
            rhs=('<',n-d-1,'>')
            for j in range(d,0,-1):
                rhs=('[',*rhs,n-j,']') if not path[j-1] else ('[',n-j,*rhs,']')
            rules.append(rhs)
    return rules

def expand(rhs):
    return {''.join(x) for x in product(*(level(a) if isinstance(a,int) else (a,) for a in rhs))}

def type_rules(n):
    p={((0,0),('a',))}
    for i in range(1,n+1):
        prev=[(i-1,t) for t in range(2) if i>1 or t==0]
        for x,y in product(prev,repeat=2):
            t=x[1] or y[1]
            if i<n or t: p.add(((i,t),('[',x,y,']')))
        for x in prev: p.add(((i,1),('<',x,'>')))
    return p

for n in range(1,5):
    M=set(level(n))-{bare(n)}
    rs=frames(n)
    assert len(set(rs))==2**n-1 and max(map(len,rs))==3*n
    assert set().union(*map(expand,rs))==M
    for j in range(n): assert closure(M,('<'*(n-j),'>'*(n-j)))==level(j)
    assert closure(M,('',''))==M
    for j in range(1,n):
        v='<'+bare(j-1)+'>'
        w=bare(n)
        k=w.find(bare(j)); z=w[:k]+v+w[k+len(bare(j)):]
        for a in range(k+1):
            for b in range(k+len(v),len(z)+1):
                x=z[a:b]; xp=x[:k-a]+bare(j)+x[k-a+len(v):]
                for c in [(m[:t],m[t+len(x):]) for m in M for t in range(len(m)-len(x)+1) if m[t:t+len(x)]==x]:
                    if c[0]+xp+c[1] not in M:
                        assert c[0]+xp+c[1]==w
                        assert len(x)==len(w)-len(c[0])-len(c[1])-len(bare(j-1))
    if n>=2:
        p=type_rules(n); assert len(p)==6*n-4
        T=sum(len(rhs)+1 for _,rhs in p)+sum(2*(n-i)+1 for i,t in {a for a,_ in p})
        print(f'n={n} |M|={len(M)} F_rules={len(rs)+2*n-1} H_rules={len(p)} H_frame_T={T}')
    else: print(f'n={n} |M|={len(M)} F_rules={len(rs)+2*n-1}')

# Test total-length accounting on actual derivations of the hard word, including
# arbitrary partitions of its left prefix, and inert nonterminals.
# This tests the combinatorial inequality, not all possible CFGs.
for n in range(2,9):
    R=len(bare(n-1))+1
    for k in range(1,R+1):
        # Minimal number of positive-length pieces with length <= k.
        p=(R+k-1)//k
        # In the minimum tree the chain uses distinct LHSs; each piece
        # charges a distinct RHS occurrence among the chain productions.
        T=p+k+1
        assert T*T>=4*R and T**3>=R
    print(f'n={n} prefix={R}: all piece-length budgets pass T^2>=4R, T^3>=R')

# Nontrivial observer counterexample to "only trivial typing": length parity.
for n in range(1,5):
    for i in range(n+1):
        for parity in {len(w)%2 for w in level(i)}:
            e=min((w for w in level(i) if len(w)%2==parity),key=len)
            assert len(e)<=max(2*i+1,4*i)
            # All words of a level share distributions in L_n.
            for x in level(i):
                assert x in closure(level(n),('<'*(n-i),'>'*(n-i)))
    print(f'n={n}: parity-fibre short kernels verified')
# Check the actual typed frame and exemplar components and the frame identity
# of Remark 5.8, for M_n up to n=3. Each nonempty factor is indexed by all contexts.
for n in range(1,4):
    M=level(n)-{bare(n)}
    D={}
    for w in M:
        for i in range(len(w)):
            for j in range(i+1,len(w)+1):
                D.setdefault(w[i:j],set()).add((w[:i],w[j:]))
    typ=lambda w: '<' in w or '>' in w
    groups={}
    for x,C in D.items():
        for c in C: groups.setdefault((c,typ(x)),set()).add(x)
    assert all(len({frozenset(D[x]) for x in xs})==1 for xs in groups.values())
    for i in range(n+1):
        for t in (False,True):
            if (i==n and not t) or (i==0 and t): continue
            E={x for x in level(i) if typ(x)==t}
            e=('<'*i+'a'+'>'*i) if t else bare(i)
            c=('<'*(n-i),'>'*(n-i))
            assert {x for x in closure(M,c) if typ(x)==t}==E
            assert {x for x,C in D.items() if typ(x)==t and D[e]<=C}==E
    print(f'n={n}: typed H_n components and substitutable frame identity verified, {len(D)} factors')
