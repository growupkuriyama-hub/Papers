"""Checks for prop:three-letter-family / app:three-letter-family (2026-10-30).

Part 1: the parser of App. G (letters a,x,P = a,b,c of the paper; markers R_i,Q_i
= hat-b_i, hat-c_i): reachable stacks = normal form, size (5*3^n-1)/2, each letter
injective on reachable stacks, complete words consume one E_i (n<=5, n<=4).
Part 2: all ten type-preserving mergings of the five-letter bracketed family,
exact (1,s)-substitutability for n<=4 (the 2+1 merge a|lr, cd is K_n).
Standard library only.
"""
from itertools import product, combinations
from collections import defaultdict

def step(st, c):
    if not st: return None
    t, rest = st[0], st[1:]
    if t[0]=='E':
        i=t[1]
        if i==0: return rest if c=='a' else None
        if c=='x': return (('E',i-1),('E',i-1),('R',i))+rest
        if c=='P': return (('E',i-1),('Q',i))+rest
        return None
    if t[0]=='R': return rest if c=='x' else None
    if t[0]=='Q': return rest if c=='P' else None
def K(i):
    S={'a'}
    for _ in range(i): S={'x'+u+v+'x' for u in S for v in S}|{'P'+u+'P' for u in S}
    return S
def NF(n):
    out={()}
    frames=lambda i:[(('E',i-1),('R',i)),(('R',i),),(('Q',i),)]
    for j in range(0,n+1):
        for Fs in product(*[frames(i) for i in range(j+1,n+1)]):
            suf=sum(Fs,())
            out.add((('E',j),)+suf)
            if j>=1: out.add((('R',j),)+suf); out.add((('Q',j),)+suf)
    return out
for n in range(1,6):
    # reachable states: BFS from E_n over all letters
    start=(('E',n),); seen={start}; todo=[start]
    while todo:
        st=todo.pop()
        for c in 'axP':
            t=step(st,c)
            if t is not None and t not in seen: seen.add(t); todo.append(t)
    nf=NF(n)
    assert seen==nf, n
    assert len(seen)==(5*3**n-1)//2
    # injectivity of each letter on reachable states
    for c in 'axP':
        img={}
        for st in seen:
            t=step(st,c)
            if t is None: continue
            assert t not in img, (n,c,st,img.get(t)); img[t]=st
    # acceptance = K_n, and Lemma 3 (macro-return) for all reachable X and all w in K_i, i<=min(n,3)
    if n<=4:
        Kn=K(n)
        for w in Kn:
            st=start
            for c in w: st=step(st,c)
            assert st==()
        for i in range(0,min(n,3)+1):
            for w in K(i):
                for X in seen:
                    st=X; ok=True
                    for c in w:
                        st=step(st,c)
                        if st is None: ok=False; break
                    if ok: assert X==(('E',i),)+st, (n,i,w,X)
    print(f'n={n}: reachable={len(seen)} == NF == (5*3^n-1)/2; letters injective on reachable; checks passed')

def occ1(w):
    for i in range(len(w)):
        for j in range(i + 1, len(w) + 1):
            yield w[i:j], (w[:i], w[j:])

def subst1(L, zeta):
    typ = lambda v: any(c in zeta for c in v)
    D, C = defaultdict(set), defaultdict(set)
    for w in L:
        for x, E in occ1(w):
            D[x].add(E); C[E].add(x)
    for E, X in C.items():
        g = defaultdict(list)
        for x in X:
            g[typ(x)].append(x)
        for xs in g.values():
            for x in xs[1:]:
                if D[x] != D[xs[0]]:
                    return False
    return True

def fam(n, m):
    E = {m['a']}
    for _ in range(n):
        E = {m['l'] + x + y + m['r'] for x in E for y in E} | {m['c'] + x + m['d'] for x in E}
    return E

def partitions(items):
    if not items:
        yield []; return
    first, rest = items[0], items[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p

for pn in partitions(['a', 'l', 'r']):
    for pz in partitions(['c', 'd']):
        m = {}
        for i, blk in enumerate(pn):
            for s in blk: m[s] = 'xyz'[i]
        for i, blk in enumerate(pz):
            for s in blk: m[s] = 'PQ'[i]
        res = []
        for n in range(1, 5):
            ok = subst1(fam(n, m), 'PQ'); res.append(ok)
            if not ok: break
        print('neutral', '|'.join(''.join(b) for b in pn), ' zeta', '|'.join(''.join(b) for b in pz), res, flush=True)
