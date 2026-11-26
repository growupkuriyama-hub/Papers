from itertools import product
from functools import cache
@cache
def words(n):
    if not n: return frozenset(['a'])
    p=words(n-1)
    return frozenset(['['+x+y+']' for x,y in product(p,repeat=2)]+['<'+x+'>' for x in p])
@cache
def bare(n): return 'a' if not n else '['+bare(n-1)*2+']'
def typ(w): return '<' in w or '>' in w

def reconstruct(K):
    # Direct quotient of unary rules via union-find; saturation of binary rules.
    ctx={}
    for w in K:
        for i in range(len(w)):
            for j in range(i+1,len(w)+1):
                x=w[i:j]; ctx.setdefault((w[:i],w[j:],typ(x)),set()).add(x)
    fac=set().union(*ctx.values()) if ctx else set()
    parent={x:x for x in fac}
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for X in ctx.values():
        x=min(X)
        for y in X: parent[root(y)]=root(x)
    P={(root(w),root(w[:i]),root(w[i:])) for w in fac for i in range(1,len(w))}
    Y={root(x):set() for x in fac}
    for x in fac:
        if len(x)==1: Y[root(x)].add(x)
    while True:
        change=False
        for z,x,y in P:
            new={a+b for a,b in product(Y[x],Y[y])}-Y[z]
            if new: Y[z].update(new); change=True
        if not change: break
    return set().union(*(Y[root(w)] for w in K)) if K else set()

for n,minlen in [(2,9),(3,16)]:
    M=words(n)-{bare(n)}
    K={w for w in M if len(w)<minlen}
    R=reconstruct(K); assert R<M
    print(f'n={n}, length<{minlen}: data={len(K)}, generated={len(R)}, target={len(M)}')
M=words(3)-{bare(3)}
K={w for w in M if bare(2) not in w}
assert reconstruct(K)==M
# Greedy removal from the largest permissible sample; then repeat with
# deterministic shuffled deletion orders if needed.
import random
rng=random.Random(20261127)
best=K
for trial in range(100):
    curr=set(K); order=sorted(curr); rng.shuffle(order)
    for w in order:
        if reconstruct(curr-{w})==M: curr.remove(w)
    if len(curr)<len(best): best=curr
    if len(best)<=11: break
assert len(best)<=11
# Pad to 11 if necessary, retaining exact reconstruction by monotonicity.
for w in sorted(K-best):
    if len(best)==11: break
    best.add(w)
assert len(best)==11 and all(bare(2) not in w for w in best) and reconstruct(best)==M
print('n=3 independently found 11-word sample:')
print('\n'.join(sorted(best)))
for n,L in [(2,9),(3,16)]:
    M=words(n)-{bare(n)}
    assert reconstruct({w for w in M if len(w)<=L})==M
    print(f'n={n}: length<={L} reconstructs all words exactly')
M=words(3)-{bare(3)}
K3=['{{{a}}}', '{{[aa]}}', '{[{a}{a}]}', '{[{a}[aa]]}', '{[[aa]{a}]}','[{{a}}[{a}{a}]]', '[[{a}{a}]{{a}}]', '[{{a}}[{a}[aa]]]', '[[[aa]{a}]{{a}}]', '[[{a}[aa]]{{a}}]', '[{{a}}[[aa]{a}]]']
K3={w.translate(str.maketrans('{}','<>')) for w in K3}
assert K3<=M and all(bare(2) not in w for w in K3) and reconstruct(K3)==M
print('published 11-word sample: exact reconstruction with both marks detected')
for n in range(2,5):
    M=words(n)-{bare(n)}
    u='<'*n+'a'+'>'*n
    contexts={(w[:i],w[i+len(u):]) for w in M for i in range(len(w)-len(u)+1) if w[i:i+len(u)]==u}
    assert contexts=={('','')} and max(map(len,M))==3*2**n-3
    print(f'n={n}: listing grammar closure and maximal RHS verified')
