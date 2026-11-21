#!/usr/bin/env python3
"""Independent audit; standard library only. No imports from supplied scripts.
Run: python3 astra_check_prop73_2026-11-07.py --seed 731107
All vector/rank/level/condition checks use exact integers.
"""
import itertools as it, random, json, argparse, collections
Z=(0,0,0)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def mask(a): return sum((x>0)<<i for i,x in enumerate(a))
def pos(a): return min(a)>0
def rank_level(F):
    F=list(F)
    if len(F)<2:return 0,True
    D=[sub(p,F[0]) for p in F[1:] if p!=F[0]]
    if not D:return 0,True
    d=D[0]; normal=next((cross(d,e) for e in D if cross(d,e)!=Z),None)
    if normal is None:return 1,min(d)<0<max(d)
    if any(dot(normal,e) for e in D):return 3,False
    return 2,min(normal)>0 or max(normal)<0

def closed(F):
    F=set(F)
    return all(not pos(x) or x in F for p,q,r in it.product(F,repeat=3) for x in [sub(add(p,q),r)])
def closure(seed,B=24,cap=160):
    F=set(seed)
    if any(max(p)>=B for p in F):return None,'boundary'
    while True:
        extra=set()
        for p,q,r in it.product(tuple(F),repeat=3):
            x=sub(add(p,q),r)
            if pos(x) and x not in F:
                if max(x)>=B:return None,'boundary'
                extra.add(x)
                if len(F)+len(extra)>cap:return None,'cap'
        if not extra:return F,'complete'
        F.update(extra)

def Tcheck(Q):
    Q=set(Q)
    for q,q1 in it.product(Q,repeat=2):
        if q==q1 or mask(q)!=mask(q1):continue
        h=sub(q1,q)
        lo=tuple(max(-x,0)+(x!=0) for x in h)
        hi=tuple(max(x,0)+(x!=0) for x in h)
        # If either side belongs to Q, gamma is exactly p-lo or p-hi.
        gs={sub(p,b) for p in Q for b in [lo,hi] if min(sub(p,b))>=0}
        for g in gs:
            a,b=add(lo,g),add(hi,g)
            if (a in Q)!=(b in Q):return {'h':h,'gamma':g,'ends':[a,b]}
    return None

def apexes(F,P=None):
    if P is not None:F=[q for q in F if sum(q)<sum(P)]
    return [(p,q,r,sub(add(p,q),r)) for p,q,r in it.product(F,repeat=3)
            if sub(add(p,q),r)[2]==0 and min(sub(add(p,q),r)[:2])>0]

def Nwitness(F,P,theta):
    # Enumerate all p1,p2,p12, r1,r2; eliminate M exactly via minimal deficit.
    opts={}
    for p in F:
        if sum(p)>=sum(P):continue
        o=[]
        for a in range(max(0,theta-p[2]+1)):
            for b in range(theta-p[2]-a+1):
                r=(a,b,p[2]); Y=(P[0]-p[0]+a,P[1]-p[1]+b)
                if min(Y)<0 or sum(Y)<=theta:continue
                for q in F:
                    D=(max(P[0]-q[0],0),max(P[1]-q[1],0))
                    if sum(D)<=theta and all(x<=y for x,y in zip(D,Y)):
                        o.append((r,Y,q,D));break
        opts[p]=o
    for p,q,r,p0 in apexes(F,P):
        if p0!=P:continue
        for u,v in it.product(opts.get(p,[]),opts.get(q,[])):
            if all(u[1][i]+v[1][i]<=P[i]-1 for i in range(2)):
                return {'p1':p,'p2':q,'p12':r,'r1':u[0],'Y1':u[1],'q1':u[2],'M1':u[3],
                        'r2':v[0],'Y2':v[1],'q2':v[2],'M2':v[3]}
    return None

def examples():
    out={}; F=[(1,3,12),(4,8,1),(6,4,4),(12,1,3)];P=(10,5,0)
    cases=[(p,q,r,sub(add(p,q),r)) for p,q,r in it.product(F,repeat=3) if q!=r]
    nontr=[x for p,q,r,x in cases if p!=r]
    assert closed(F) and Tcheck(F+[P]) is None
    assert sub(add(F[1],F[3]),F[2])==P
    out['F4']={'q_ne_r':len(cases),'nontrivial_ordered':len(nontr),
      'nontrivial_positive':sum(pos(x) for x in nontr),
      'det':det(sub(F[0],F[1]),sub(F[2],F[1]),sub(F[3],F[1])),
      'nontrivial_unique_expressions':24}
    rows=[]
    for X,Y in it.chain(it.product(range(4,21),repeat=2),[(30,5),(25,40),(60,7)]):
        A,B,M,C=(1,Y+1,1),(X+1,1,1),(2,2,2),(1,1,4);F=[A,B,M,C];P=(X,Y,0)
        assert closed(F) and Tcheck(F+[P]) is None
        assert det(sub(A,M),sub(B,M),sub(C,M))==3*X+3*Y-2*X*Y
        assert sub(add(A,B),M)==P and rank_level(F)==(3,False)
        assert all(sum(p)<sum(P) for p in F)
        assert Nwitness(F,P,min(X,Y)-2) is None
        rows.append((X,Y))
    out['FXY']={'parameter_count':len(rows),'range':'4..20 squared plus (30,5),(25,40),(60,7)'}
    rows=[]
    for n in range(3,31):
        s=[(2*k,2*(n+1-k),k) for k in range(1,n+1)]; C=(1,1,2*n);A=(4*n,1,1);F=s+[C,A];P=(4*n-3,3,0)
        d=sub(s[1],s[0]);h=sub(C,s[0]);j=sub(A,s[0])
        assert closed(F) and Tcheck(F+[P]) is None
        assert det(d,h,j)==2*n-1
        assert add(tuple(-2*n*x for x in d),add(h,tuple(2*x for x in j)))==sub(P,s[0])
        lam=(2*n-1,4*n-1,4*n)
        short=[q for q in F if sum(q)<sum(P)]
        assert set(short)==set(s+[C]) and {dot(lam,q) for q in short}=={8*n*n+6*n-2}
        assert not any(x[3]==P for x in apexes(F,P))
        assert len({q[2] for q in F})==n+1
        rows.append(n)
    out['Sn']={'range':[3,30],'count':len(rows)}
    F=[(1,4,6),(3,9,3),(9,3,1),(1,27,1)];P=(5,14,0)
    assert closed(F) and Tcheck(F+[P]) is None and rank_level(F)==(3,False)
    assert sub(tuple(2*x for x in F[1]),F[0])==P
    assert {dot((2,1,3),p) for p in F[:3]}=={24}
    ws={t:Nwitness(F,P,t) for t in range(1,8)}
    assert all(ws[t] is None for t in range(1,7)) and ws[7] is not None
    out['example4']={'theta1to7':ws,'det':det(*[sub(p,F[0]) for p in F[1:]])}
    for name,F,P in [('X',[(3,2,1),(1,3,2),(2,1,3)],(5,1,0)),
          ('Y23',[(1,2,5),(1,26,1),(11,10,2),(24,3,1)],(10,23,0))]:
        assert Tcheck(F+[P]) is None
        assert not any(t[3]==P for t in apexes(F,P))
        out[name]={'apexes':sorted({t[3] for t in apexes(F)}),'short_apexes':sorted({t[3] for t in apexes(F,P)})}
    F=[(1,5,1),(6,1,1),(2,2,2),(1,1,4)];P=(1,5,0);P1=(6,1,0)
    assert Tcheck(F+[P,P1]) is None and Tcheck(F+[P]) is not None
    out['singleton_deletion']={'Q3':F,'Q2':[P,P1],'failure':Tcheck(F+[P])}
    P=(1,15,0);Q2=[(1,15,0),(6,11,0),(11,7,0),(16,3,0)]
    assert Tcheck(F+Q2) is None and Tcheck(F+[P]) is not None
    ds=[sub(p,F[0]) for p in F[1:]]
    assert add(add(tuple(2*x for x in ds[0]),tuple(-10*x for x in ds[1])),tuple(3*x for x in ds[2]))==sub(P,F[0])
    out['singleton_deletion_in_V']={'Q3':F,'Q2':Q2,'P_in_V_coefficients':[2,-10,3],'failure':Tcheck(F+[P])}
    return out

def seed_search(rng):
    out={}
    for mode in ['exhaustive3','uniform','biased']:
        stats=collections.Counter();witness=[]
        if mode=='exhaustive3': seeds=it.combinations(list(it.product(range(1,4),repeat=3)),3)
        else:
            seeds=[]
            for _ in range(3000):
                F=set()
                while len(F)<3+_%3:
                    p=[rng.randint(1,8) for i in range(3)]
                    if mode=='biased':p[rng.randrange(3)]=rng.randint(1,2)
                    F.add(tuple(p))
                seeds.append(F)
        for seed in seeds:
            stats['seeds']+=1;F,status=closure(seed)
            stats[status]+=1
            if F is not None:
                r,level=rank_level(F);stats['rank'+str(r)]+=1
                if r<=2 and not level:witness.append(sorted(F))
        out[mode]={'counts':dict(stats),'violations':witness}
    return out

# Rules: (lhs, terminal Parikh vector, ordered tuple of child labels).
# These are ordinary CFGs, a subclass of the stipulated linear nondeleting grammars.
def accessible(rules):
    seen={0}
    while True:
        s=seen|{b for a,t,ch in rules if a in seen for b in ch}
        if s==seen:return sorted(seen)
        seen=s

def minimums(rules,v):
    inf=10**30;m=[[inf]*8 for _ in range(v)]
    while True:
        change=False
        for a,t,ch in rules:
            for ms in it.product(*[[i for i in range(8) if m[b][i]<inf] for b in ch]):
                s=mask(t);cost=sum(t)
                for b,k in zip(ch,ms):s|=k;cost+=m[b][k]
                if cost<m[a][s]:m[a][s]=cost;change=True
        if not change:return m,inf

def yields(rules,v,limit=None,cap=20000):
    sets=[set() for _ in range(v)]
    while True:
        change=False
        for a,t,ch in rules:
            for ps in it.product(*[tuple(sets[b]) for b in ch]):
                q=t
                for p in ps:q=add(q,p)
                if limit is not None and sum(q)>=limit:continue
                if q not in sets[a]:sets[a].add(q);change=True
                if len(sets[a])>cap:return None
        if not change:return sets

def assess_grammar(rules,v,stats,finite=True):
    keep=accessible(rules); mp={x:i for i,x in enumerate(keep)}
    rules=[(mp[a],t,tuple(mp[b] for b in ch)) for a,t,ch in rules if a in mp];v=len(keep)
    m,inf=minimums(rules,v)
    if any(min(row)>=inf for row in m):stats['unproductive_skipped']+=1;return
    mu=m[0][3]
    if mu>=inf:stats['no_ab']+=1;return
    tau=[min(row) for row in m];theta=max(sum(t)+sum(tau[b] for b in ch) for a,t,ch in rules)
    r=max(1,max(len(ch) for a,t,ch in rules))
    stats['with_ab']+=1
    if finite:
        sets=yields(rules,v)
        if sets is None:stats['set_cap_skipped']+=1;return
        Q=sets[0];K=len({p[2] for p in Q if mask(p)==7})
        stats['lemma7_tested']+=1
        assert mu<=(K+3)*v*theta,(rules,mu,K,v,theta)
        stats['max_lemma7_ratio']=max(stats['max_lemma7_ratio'],mu/((K+3)*v*theta))
        short=[p for p in Q if mask(p)==7 and sum(p)<mu]
    else:
        sets=yields(rules,v,mu)
        if sets is None:stats['set_cap_skipped']+=1;return
        short=[p for p in sets[0] if mask(p)==7]
        stats['lemma7_not_certified']+=1
    lev=rank_level(short)[1]
    stats['vacuous' if not short else 'nonvacuous_level' if lev else 'hypothesis_false']+=1
    if lev:
        bound=max(9*(r+1)*v*theta,11*(r+1)*v*v*theta**4)
        assert mu<=bound,(rules,mu,v,theta)
        stats['theorem6_tested']+=1
        stats['max_theorem6_ratio']=max(stats['max_theorem6_ratio'],mu/bound)

def grammar_search(rng):
    out={}
    terminals=list(it.product(range(3),repeat=3));terminals=[p for p in terminals if 1<=sum(p)<=3]
    for mode in ['acyclic','identity_cycles','growing_cycles','homogeneous']:
        stats=collections.Counter()
        for trial in range(1000):
            v=rng.randint(1,4);rules=[]
            if mode=='homogeneous':
                lam=(rng.randint(1,3),rng.randint(1,3),rng.randint(2,5))
                energies=[rng.randint(4,12) for _ in range(v)];energies[0]=max(energies)
                ts=[p for p in it.product(range(13),repeat=3) if sum(p)>0 and dot(lam,p)<=12]
                for a in range(v):
                    allowed=[p for p in ts if dot(lam,p)==energies[a]]
                    if not allowed:break
                    for t in rng.sample(allowed,min(4,len(allowed))):rules.append((a,t,()))
                    choices=[(t,ch) for k in [1,2] for ch in it.product(range(v),repeat=k)
                             for t in [Z]+ts if dot(lam,t)+sum(energies[b] for b in ch)==energies[a]]
                    for t,ch in rng.sample(choices,min(4,len(choices))):rules.append((a,t,ch))
                else:
                    assess_grammar(rules,v,stats);continue
                stats['unrepresentable_energy']+=1;continue
            for a in range(v):
                for _ in range(rng.randint(1,3)):rules.append((a,rng.choice(terminals),()))
                for _ in range(rng.randint(1,3)):
                    children=list(range(a+1,v))
                    if children:
                        ch=tuple(rng.choice(children) for _ in range(rng.randint(1,2)))
                        rules.append((a,rng.choice([Z]+terminals),ch))
                if mode=='identity_cycles':rules.append((a,Z,(a,)))
                if mode=='growing_cycles':rules.append((a,rng.choice(terminals),(rng.randrange(v),)))
            assess_grammar(rules,v,stats,finite=mode!='growing_cycles')
        out[mode]=dict(stats)
    # Explicit homogeneous, nonvacuous, productive cyclic example.
    rules=[(0,Z,(1,)),(1,Z,(0,)),(0,(2,2,0),()),(1,(1,1,1),())]
    st=collections.Counter();assess_grammar(rules,2,st);out['explicit_homogeneous_cycle']=dict(st)
    return out

def conjecture_search(rng):
    # Complete enumeration within a stated biased pool, not the whole cube.
    pool=[p for p in it.product(range(1,9),repeat=3) if sum(x==1 for x in p)>=2] + [(2,2,2),(2,2,3),(2,3,2),(3,2,2)]
    stats=collections.Counter();viol=[]
    for k in [4,5]:
        for F in it.combinations(pool,k):
            stats['seeds'+str(k)]+=1
            if rank_level(F)[0]!=3 or not closed(F):continue
            stats['closed_rank3']+=1
            Ps={t[3] for t in apexes(F)}
            for P in Ps:
                if Tcheck(list(F)+[P]) is not None:continue
                for theta in range(1,max(1,(sum(P)-2)//2)):
                    w=Nwitness(F,P,theta)
                    if w:
                        stats['admissible']+=1
                        if not rank_level([p for p in F if sum(p)<sum(P)])[1]:viol.append([F,P,theta,w])
                        break
    # Complement with biased random points in [1,8]^3.
    for _ in range(10000):
        F=set()
        while len(F)<4+_%2:
            p=[rng.randint(1,8) for i in range(3)];p[rng.randrange(3)]=1
            F.add(tuple(p))
        stats['random_seeds']+=1
        if rank_level(F)[0]!=3 or not closed(F):continue
        stats['random_closed_rank3']+=1
        for P in {x[3] for x in apexes(F)}:
            if Tcheck(list(F)+[P]) is not None:continue
            for theta in range(1,max(1,(sum(P)-2)//2)):
                w=Nwitness(F,P,theta)
                if w:
                    stats['random_admissible']+=1
                    if not rank_level([p for p in F if sum(p)<sum(P)])[1]:viol.append([sorted(F),P,theta,w])
                    break
    return {'pool':pool,'counts':dict(stats),'violations':viol}

def main():
    p=argparse.ArgumentParser();p.add_argument('--seed',type=int,default=731107);p.add_argument('--part',default='all');args=p.parse_args()
    rng=random.Random(args.seed)
    funcs={'examples':lambda:examples(),'closures':lambda:seed_search(random.Random(args.seed)),'grammars':lambda:grammar_search(random.Random(args.seed)),'conjecture':lambda:conjecture_search(random.Random(args.seed))}
    for name,f in funcs.items():
        if args.part in ['all',name]:print(json.dumps({'part':name,'seed':args.seed,'result':f()},ensure_ascii=False),flush=True)
if __name__=='__main__':main()
