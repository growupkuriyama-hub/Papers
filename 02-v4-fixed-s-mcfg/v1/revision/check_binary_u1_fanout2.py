#!/usr/bin/env python3
"""Checks for thm:binary-u1-polydata / app:binary-u1 (2026-10-30).

Bounded reproducibility audit for the binary typing a->1, b->zeta onto U_1 at
fan-out two: exact finite (1,s)/(2,s)-substitutability tests (nonempty middle
separator), the (a,ba)/(aa,b) collision of lem:app-u1-deep, (2,s)-closures of
seeds R_e (e=1,2,3) reaching a full Parikh row, a sweep of 1024 finite families
with a^6 (no counterexample to deep insertion => Parikh saturation), and an
enumeration of small fan-out<=2 grammars comparing tau with |V|^2 theta^5.
Origin: script accompanying the ChatGPT report
Binary_U1_Fanout2_Polynomial (2026-10-30), re-run and reviewed by Claude.
No finite computation is used as a proof of a universal statement.
Standard library only.
"""
from collections import defaultdict, deque
from itertools import product, combinations
from math import comb
from hashlib import sha256

ALPHABET = 'ab'
def typ(w):
    assert w
    return 'z' if 'b' in w else '1'

def occ(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i+1, n+1):
                yield (w[i:j],), (w[:i], w[j:])
    elif d == 2:
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):  # nonempty middle word
                    for t in range(k+1,n+1):
                        yield (w[i:j],w[k:t]), (w[:i],w[j:k],w[t:])
    else:
        raise ValueError(d)

def fill(ctx, vals):
    if len(vals)==1:
        return ctx[0]+vals[0]+ctx[1]
    return ctx[0]+vals[0]+ctx[1]+vals[1]+ctx[2]

def check(L, dimensions=(1,2), return_data=False):
    L=set(L)
    contexts={}
    dists={}
    for d in dimensions:
        D=defaultdict(set); C=defaultdict(set)
        for w in sorted(L):
            for x,E in occ(w,d):
                D[x].add(E); C[E].add(x)
        for E,xs in sorted(C.items()):
            classes=defaultdict(list)
            for x in sorted(xs):
                classes[tuple(map(typ,x))].append(x)
            for vs in classes.values():
                first=vs[0]
                for y in vs[1:]:
                    if D[first]!=D[y]:
                        missing=min(D[first]^D[y])
                        item=(d,first,y,E,missing)
                        return (item, (D,C)) if return_data else item
        contexts[d]=C; dists[d]=D
    return (None,(dists,contexts)) if return_data else None

def closure(seed, bound=10, rounds=8):
    """Sound forward consequences only; truncation is by output word length."""
    L=set(seed)
    sizes=[len(L)]
    for _ in range(rounds):
        added=set()
        for d in (1,2):
            D=defaultdict(set); inv=defaultdict(set)
            for w in L:
                for xs,E in occ(w,d):
                    D[xs].add(E); inv[(tuple(map(typ,xs)),E)].add(xs)
            # union-find components for overlapping distributions within each type
            typed=defaultdict(set)
            for xs in D: typed[tuple(map(typ,xs))].add(xs)
            for t,group in typed.items():
                parent={x:x for x in group}
                def root(x):
                    while parent[x]!=x:
                        parent[x]=parent[parent[x]];x=parent[x]
                    return x
                for (ts,E),xs in inv.items():
                    if ts!=t: continue
                    it=iter(xs);a=next(it)
                    for x in it: parent[root(x)]=root(a)
                comp=defaultdict(list)
                for x in group: comp[root(x)].append(x)
                for items in comp.values():
                    all_E=set().union(*(D[x] for x in items))
                    for E in all_E:
                        for xs in items:
                            w=fill(E,xs)
                            if len(w)<=bound: added.add(w)
        newer=added-L
        L|=newer; sizes.append(len(L))
        if not newer: break
    return L,sizes

# A compact acyclic f<=2 MCFG representation. Each rule=(head, children, template).
# Template is tuple of component strings over terminals and symbolic placeholders
# '{0:0}', '{0:1}', '{1:0}', ... . (Not a global string-grammar notation.)
class Rule:
    def __init__(self, head, children, template):
        self.head=head; self.children=tuple(children);self.template=tuple(template)
    def rank(self): return len(self.children)
    def cost(self):
        n=sum(len(z) for z in self.template)
        return 1+self.rank()+n
    def show(self): return f'N{self.head} -> '+repr(self.template)+' ('+','.join('N'+str(x) for x in self.children)+')'

def evaluate(R, args):
    out=[]
    for comp in R.template:
        s=''
        for x in comp:
            if isinstance(x,str): s+=x
            else: s+=args[x[0]][x[1]]
        out.append(s)
    return tuple(out)

def good(R, fan):
    if len(R.template)!=fan[R.head] or any(not c for c in R.template):return False
    got=[]
    for part in R.template:
        got.extend([x for x in part if isinstance(x,tuple)])
        for j in range(len(part)-1):
            a,b=part[j:j+2]
            if isinstance(a,tuple) and isinstance(b,tuple) and a[0]==b[0] and b[1]==a[1]+1:return False
    wanted=[(i,j) for i,v in enumerate(R.children) for j in range(fan[v])]
    return sorted(got)==sorted(wanted) and len(got)==len(set(got)) and all([x[1] for x in got if x[0]==i]==list(range(fan[v])) for i,v in enumerate(R.children))

def options(i,fan):
    ar=fan[i]
    opts=[]
    if ar==1:
        const=['a','b','aa','ab','ba']
        for c in const:opts.append(Rule(i,(),((c,),)))
    else:
        for u,v in [('a','a'),('a','b'),('b','a'),('b','b'),('aa','b'),('a','bb')]:
            opts.append(Rule(i,(),((u,),(v,))))
    if not i: return opts
    for j in range(i):
        f=fan[j]
        if ar==1 and f==1:
            for temp in [((0,0),),('a',(0,0)),((0,0),'a'),('b',(0,0)),((0,0),'b')]:
                opts.append(Rule(i,(j,),(temp,)))
        if ar==1 and f==2:
            for sep in 'ab': opts.append(Rule(i,(j,),(((0,0),sep,(0,1)),)))
        if ar==2 and f==1:
            for z in 'ab':
                opts.append(Rule(i,(j,),(((0,0),),(z,))))
                opts.append(Rule(i,(j,),((z,),((0,0),))))
        if ar==2 and f==2:
            for z in 'ab':
                opts.extend([Rule(i,(j,),(((z,(0,0))),((0,1),))),Rule(i,(j,),(((0,0),),((0,1),z)))])
    if i>=2:
        for j,k in combinations(range(i),2):
            if fan[j]==fan[k]==1:
                if ar==1:
                    for z in ['','a','b']:
                        opts.append(Rule(i,(j,k),(((0,0),z,(1,0)),)))
                else:
                    opts.append(Rule(i,(j,k),((((0,0),)),(((1,0),)))))
    return [R for R in opts if good(R,fan)]

def emit(Rs,fan,cap=100000):
    """Exact finite language if <= cap yields per nonterminal, otherwise raise."""
    G=defaultdict(list)
    for R in Rs:G[R.head].append(R)
    values={}
    for i in range(len(fan)):
        accum=set()
        for R in G[i]:
            for args in product(*(values[j] for j in R.children)):
                accum.add(evaluate(R,args))
                if len(accum)>cap:raise OverflowError('cap')
        values[i]=accum
    return values

def grammar_stats(Rs,fan,values):
    k=len(fan)
    if not values[k-1]:return None
    G=defaultdict(list)
    for R in Rs:G[R.head].append(R)
    reachable={k-1}
    queue=deque([k-1])
    while queue:
        for R in G[queue.popleft()]:
            for j in R.children:
                if j not in reachable:reachable.add(j);queue.append(j)
    if reachable!=set(range(k)) or not all(values[i] for i in range(k)):
        return None
    mins={i:min((sum(map(len,t)),t) for t in values[i])[1] for i in range(k)}
    # Minimal externally fixed material in a *sentential* context of each N_i.
    C={k-1:(('',),)}  # instead use placeholder symbol tuples {component index}
    C={k-1:tuple(((i,),) for i in range(fan[k-1]))}
    # component placeholder i is an int; terminal strings remain str
    # all contexts globally: (prefix,middle,suffix) built by replacing A-hole via rule
    ctx={k-1:('','')}
    mincontext={k-1:0}
    for i in range(k-1,-1,-1):
        if i not in ctx:continue
        for R in G[i]:
            for pos,j in enumerate(R.children):
                args=[]
                for t,cid in enumerate(R.children):
                    args.append(tuple('~'+str(v)+'~' for v in range(fan[cid])) if t==pos else mins[cid])
                filled=evaluate(R,args)
                # use sentinel for the two components of target child
                mid=''.join(ctx[i][a]+filled[a] for a in range(fan[i])) + ctx[i][-1] if fan[i]==1 else None
                # context of arity2 for i could itself be spread into parent, handle using substitution
                # generic: from context segments [v0,...vd], plug parent components with filled strings
                text=ctx[i][0]
                for a,c in enumerate(filled):text+=c+ctx[i][a+1]
                spl=text.split('~0~')
                if fan[j]==1:
                    if len(spl)!=2:raise AssertionError((text,R.show()))
                    result=(spl[0],spl[1])
                else:
                    p=text.index('~0~');q=text.index('~1~')
                    if p>q:raise AssertionError('bad order')
                    result=(text[:p],text[p+3:q],text[q+3:])
                if len(result)==3 and not result[1]:raise AssertionError('middle empty')
                cost=sum(map(len,result))
                if j not in ctx or cost<mincontext[j]:
                    ctx[j]=result;mincontext[j]=cost
    theta=[]
    for R in Rs:
        l=sum(len(x) for comp in R.template for x in comp if isinstance(x,str))
        l+=sum(sum(map(len,mins[j])) for j in R.children)
        theta.append(mincontext[R.head]+l)
    size=k+sum(R.cost() for R in Rs)
    return size,max(1,max(theta)),theta,ctx

def exact_tau(Rs,fan,values,ctx,language):
    indexed={1:defaultdict(lambda:defaultdict(lambda:10**15)),2:defaultdict(lambda:defaultdict(lambda:10**15))}
    for w in language:
        for d in (1,2):
            for xs,E in occ(w,d):
                tt=tuple(map(typ,xs));val=sum(map(len,xs))
                if val<indexed[d][E][tt]:indexed[d][E][tt]=val
    tau=0; by=[]
    for i in range(len(fan)):
        for t in sorted(set(tuple(map(typ,v)) for v in values[i])):
            val=indexed[fan[i]][ctx[i]].get(t,10**15)
            assert val < 10**15,(i,ctx[i],t)
            tau=max(tau,val);by.append((i,''.join(t),val))
    return tau,by

def run_enumeration(limit_grammars=4000):
    tested=valid=correct=over100=0
    per_k=[]
    passed_with_fan2=passed_with_rank2=0
    maxima=[(0,None),(0,None)]; examples=[]; statistics=[]
    # Grid of acyclic grammars. Each N_i has precisely one base constant rule;
    # N_i with i>0 has one extra rule from the FIRST THREE nonconstant options
    # in the fixed 'options' order. No language-size cutoff at 100.
    for k in (2,3,4):
        before=(tested,valid,correct,over100)
        for suffix in product((1,2),repeat=k-1):
            fan=tuple(suffix)+(1,)
            opts=[options(i,fan) for i in range(k)]
            candidates=[]
            for i in range(k):
                bases=[r for r in opts[i] if r.rank()==0][:2]
                extras=[]
                if i:
                    comps=[r for r in opts[i] if r.rank()!=0]
                    for sub in ([r for r in comps if (i-1) in r.children],
                                [r for r in comps if 0 in r.children],
                                [r for r in comps if r.rank()==2], comps):
                        for r in sub:
                            if r not in extras:
                                extras.append(r)
                                break
                        if len(extras)>=3:break
                else:extras=[None]
                candidates.append([(b,) if e is None else (b,e) for b in bases for e in extras])
            for choices in product(*candidates):
                Rs=[r for pair in choices for r in pair]
                tested+=1
                try: values=emit(Rs,fan,cap=50000)
                except OverflowError:continue
                stats=grammar_stats(Rs,fan,values)
                if stats is None:continue
                valid+=1
                size,theta,thetas,ctx=stats
                L={x[0] for x in values[k-1]}
                if len(L)>100:over100+=1
                bad=check(L)
                if bad is not None:continue
                correct+=1
                if 2 in fan:passed_with_fan2+=1
                if any(r.rank()==2 for r in Rs):passed_with_rank2+=1
                tau,by=exact_tau(Rs,fan,values,ctx,L)
                c_s=9*k+81*len(Rs)
                bound=c_s*(1+2*theta+2*tau)+1
                ratio1=tau/(k*k*theta**5);ratio2=tau/theta
                meta=(k,fan,len(Rs),size,theta,len(L),tau,round(bound),by)
                if ratio1>maxima[0][0]:maxima[0]=(ratio1,meta)
                if ratio2>maxima[1][0]:maxima[1]=(ratio2,meta)
                if len(examples)<7 or ratio2>examples[-1][0]:
                    examples.append((ratio2,ratio1,meta))
                    examples.sort(reverse=True,key=lambda e:e[0]);examples=examples[:7]
                if len(statistics)<6:statistics.append((meta,[r.show() for r in Rs]))
                if tested-before[0]>=limit_grammars//3:break
            if tested-before[0]>=limit_grammars//3:break
        per_k.append((k,*(x-y for x,y in zip((tested,valid,correct,over100),before))))
    print('GRAMMAR by k (k,enumerated,reduced,passed,>100)',per_k)
    print('GRAMMAR enumeration tested',tested,'reduced_good',valid,'passed_2s',correct,'languages_gt_100',over100,'passed_with_fan2',passed_with_fan2,'passed_with_rank2',passed_with_rank2)
    print('GRAMMAR maxima tau/(|V|^2 theta^5)',maxima[0]);print('GRAMMAR maxima tau/theta',maxima[1])
    print('GRAMMAR top records ratio2,ratio1, (NT,fan,rules,size,theta,|L|,tau,bound,typed)',*[e for e in examples],sep='\n')
    print('GRAMMAR sample exact rules',*[e for e in statistics],sep='\n')


def parikh_saturated(L):
    P={(w.count('a'),w.count('b')) for w in L}
    for na,nb in P:
        n=na+nb
        if any(w not in L for w in (''.join(z) for z in product('ab',repeat=n) if z.count('a')==na)):
            return False
    return True

def short_R_premise(L):
    if not any('a'*6 in w for w in L):return False
    for w in L:
        for i in range(len(w)):
            if w[i]!='a':continue
            for j in range(i+1,len(w)):
                if w[j]!='b':continue
                t=j
                while t<len(w) and w[t]=='b':t+=1
                u=t
                while u<len(w) and w[u]=='a':u+=1
                if u==t:continue
                left=j-i
                right=u-t
                if left+right>=5 and w[i:j]=='a'*left:return True
    return False

def finite_sweep():
    # ALL 2^10 subsets of a prescribed 10-word universe, with a^6 included.
    # Unlike forward closure, each selected language is tested in its entirety.
    pool=['a'*i+'b'+'a'*(6-i) for i in range(7)]
    pool+=['a'*4+'bb'+'a','a'*3+'bb'+'a'*2,'a'+'bb'+'a'*4]
    premise=pass_count=saturated=bad=0
    for mask in range(1<<len(pool)):
        L={'a'*6}
        for i,w in enumerate(pool):
            if (mask>>i)&1:L.add(w)
        if not short_R_premise(L):continue
        premise+=1
        if check(L) is None:
            pass_count+=1
            if parikh_saturated(L):saturated+=1
            else:bad+=1
    print('FINITE_SWEEP 2^10=1024 families (a^6 plus subsets of 7 one-b length7 and 3 two-b length7): premise',premise,'(2,s)-passing',pass_count,'Parikh-saturated',saturated,'counterexamples',bad)
    assert bad==0

def main():
    examples=[
        ('two_tuple_failure', {'a'*7}|{'a'*i+'bb'+'a'*(5-i) for i in range(6)},False),
        ('one_b_saturation', {'a'*7}|{'a'*i+'b'+'a'*(6-i) for i in range(7)},True),
        ('ab_bba', {'ab','bba'},True),
    ]
    for label,L,ok in examples:
        bad=check(L)
        print('TEST',label,'words',len(L),'pass',bad is None,'expected',ok,'witness',bad)
        assert (bad is None)==ok
    # Check the specific collision requested in the prompt, not merely any pair.
    Lminus=examples[0][1]
    x=('aa','b');y=('a','ba')
    Dx={E for w in Lminus for xs,E in occ(w,2) if xs==x}
    Dy={E for w in Lminus for xs,E in occ(w,2) if xs==y}
    shared=min(Dx & Dy); disting=min(Dx-Dy)
    assert typ(x[0])==typ(y[0]) and typ(x[1])==typ(y[1])
    assert fill(shared,x) in Lminus and fill(shared,y) in Lminus
    assert fill(disting,x) in Lminus and fill(disting,y) not in Lminus
    print('TARGETED COLLISION (aa,b) vs (a,ba): shared',shared,'accepted_words',fill(shared,x),fill(shared,y),'distinguishing',disting,'accepted_x',fill(disting,x),'rejected_y',fill(disting,y))
    print('TEST 2-hole nonempty middle: all occurrences satisfy',all(E[1] for w in {'aabbab','babaaba'} for _,E in occ(w,2)))
    for label,seed in [('R_e2',{'a'*6,'a'*4+'bb'+'a'}),('R_e3',{'a'*6,'a'*2+'bbb'+'a'*3}),('R_e1',{'a'*6,'a'*4+'b'+'a'})]:
        out,sizes=closure(seed,bound=9,rounds=6)
        e={'R_e2':2,'R_e3':3,'R_e1':1}[label]
        rows={w for w in out if w.count('b')==e and w.count('a')==5}
        print('CLOSURE',label,'sizes',sizes,'contains aaba or abaa',any('aaba' in w or 'abaa' in w for w in out),'Parikh row',len(rows),'of',comb(5+e,e))
        assert any('aaba' in w or 'abaa' in w for w in out)
    # A separate positive control: all 2^8 binary words of length 8,
    # generated by a four-nonterminal doubling grammar; no 100-word exclusion.
    fan=(1,1,1,1)
    rules=[Rule(0,(),(('a',),)),Rule(0,(),(('b',),))]
    rules += [Rule(i,(i-1,i-1),(((0,0),(1,0)),)) for i in range(1,4)]
    vals=emit(rules,fan)
    L={x[0] for x in vals[3]}
    stat=grammar_stats(rules,fan,vals)
    assert stat and len(L)==256
    assert check(L) is None
    size,theta,_,ctx=stat
    tau,by=exact_tau(rules,fan,vals,ctx,L)
    c_s=9*len(fan)+81*len(rules)
    print('LARGE positive-control Sigma^8:', 'words',len(L),'size',size,'theta',theta,'tau',tau,'tau/(|V|^2theta^5)',round(tau/(len(fan)**2*theta**5),12),'tau/theta',round(tau/theta,6),'sample_upper_bound',c_s*(1+2*theta+2*tau)+1,'types',by)
    finite_sweep()
    run_enumeration(6000)

if __name__=='__main__':main()
