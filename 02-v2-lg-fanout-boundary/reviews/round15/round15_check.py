#!/usr/bin/env python3
"""Round 15 independent checks; Python standard library only.
No previous checker imports. No closure search, caps, or random sampling.
"""
from collections import defaultdict
from itertools import combinations
from math import inf
import json

def fill(e,x):
    return ''.join(e[i]+x[i] for i in range(len(x)))+e[-1]

def exact_distributions(L):
    D=defaultdict(set)
    for w in sorted(L):
        n=len(w)
        for i,j in combinations(range(n+1),2):
            D[(w[i:j],)].add((w[:i],w[j:]))
        for i,j,k,l in combinations(range(n+1),4):
            D[(w[i:j],w[k:l])].add((w[:i],w[j:k],w[l:]))
    groups=defaultdict(list)
    for x,es in D.items():
        for e in es: groups[(tuple(frozenset(t) for t in x),e)].append(x)
    checks=0
    for xs in groups.values():
        for x in xs[1:]:
            checks+=1
            assert D[x]==D[xs[0]],('distribution',xs[0],x)
    return len(D),sum(map(len,D.values())),checks

def exact_rectangles(L):
    # Independent occurrence enumeration using component lengths, then
    # rectangularity of each same-type context/tuple incidence relation.
    C=defaultdict(set); T=defaultdict(set)
    for w in sorted(L):
        n=len(w)
        for size in range(1,n+1):
            for left in range(n-size+1):
                x=(w[left:left+size],); e=(w[:left],w[left+size:])
                typ=tuple(''.join(sorted(set(z))) for z in x)
                C[(typ,e)].add(x); T[(typ,x)].add(e)
        for size1 in range(1,n):
            for size2 in range(1,n-size1):
                for gap in range(1,n-size1-size2+1):
                    for left in range(n-size1-size2-gap+1):
                        end1=left+size1; start2=end1+gap; end2=start2+size2
                        x=(w[left:end1],w[start2:end2]); e=(w[:left],w[end1:start2],w[end2:])
                        typ=tuple(''.join(sorted(set(z))) for z in x)
                        C[(typ,e)].add(x); T[(typ,x)].add(e)
    checked=0
    for (typ,e),xs in C.items():
        if len(xs)<2: continue
        for x in xs:
            for f in T[(typ,x)]:
                for y in xs:
                    assert fill(f,y) in L,('rectangle',e,f,x,y)
                    checked+=1
    return checked

def stage_language(N,d):
    out=set()
    for m in range(N//d+1):
        na=N-d*m; n=na+2*m
        for slots in combinations(range(n),2*m):
            w=['a']*n
            for t,p in enumerate(slots): w[p]='b' if t<m else 'c'
            out.add(''.join(w))
    return out

def member(w,N,d):
    p=w.replace('a','')
    return bool(w) and set(w)<=set('abc') and 'cb' not in p and w.count('b')==w.count('c') and w.count('a')+d*w.count('b')==N

# Each variable is (child number, component number), terminals are characters.
def grammar(d,q,nested=False):
    assert d>=4 and d%2==0 and q>=1
    N=d*2**q+3; arity={'S':1}; rules=[]
    def add(A,children,outputs): rules.append((A,tuple(children),tuple(tuple(z) for z in outputs)))
    for n in range(1,N+1): arity['A'+str(n)]=1
    for i in range(q+1): arity['B'+str(i)]=2
    add('A1',[],['a']); add('A'+str(d),[],['bc'])
    for n in range(2,N+1):
        add('A'+str(n),['A'+str(n-1)],[['a',(0,0)]])
        add('A'+str(n),['A'+str(n-1)],[[ (0,0),'a']])
    for n in range(d+1,N+1): add('A'+str(n),['A'+str(n-d)],[['b',(0,0),'c']])
    add('B0',[],['a'*(d//2),'a'*(d//2)]); add('B0',[],['b','c'])
    for i in range(1,q+1):
        second=[(1,1),(0,1)] if nested else [(0,1),(1,1)]
        add('B'+str(i),['B'+str(i-1)]*2,[[(0,0),(1,0)],second])
    add('S',['A'+str(N)],[[(0,0)]])
    add('S',['B'+str(q)],[['a',(0,0),'a',(0,1),'a']])
    return N,arity,rules

def grammar_audit(d,q,nested=False):
    N,arity,rules=grammar(d,q,nested); by=defaultdict(list)
    for R in rules:
        A,ch,outs=R; by[A].append(R)
        assert len(outs)==arity[A] and all(outs) and len(ch)<=2
        flat=[v for z in outs for v in z if isinstance(v,tuple)]
        assert sorted(flat)==[(j,k) for j,B in enumerate(ch) for k in range(arity[B])]
        for j,B in enumerate(ch): assert [k for z,k in flat if z==j]==list(range(arity[B]))
        for z in outs:
            for x,y in zip(z,z[1:]):
                assert not (isinstance(x,tuple) and isinstance(y,tuple) and x[0]==y[0] and y[1]==x[1]+1)
    reached={'S'}; stack=['S']
    while stack:
        for _,ch,_ in by[stack.pop()]:
            for B in ch:
                if B not in reached: reached.add(B); stack.append(B)
    assert reached==set(arity)
    order=['A'+str(n) for n in range(1,N+1)]+['B'+str(i) for i in range(q+1)]+['S']
    lengths={}; pure_nodes={}
    def nt(R): return sum(isinstance(x,str) for z in R[2] for x in z)
    def rlen(R): return nt(R)+sum(lengths[B] for B in R[1])
    for A in order:
        lengths[A]=min(rlen(R) for R in by[A])
        pure_nodes[A]=min((1+sum(pure_nodes[B] for B in R[1]) for R in by[A]
                           if all(x=='a' for z in R[2] for x in z if isinstance(x,str))),default=inf)
    ctx={A:inf for A in arity}; ctx['S']=0
    for A in reversed(order):
        for R in by[A]:
            for B in R[1]:ctx[B]=min(ctx[B],ctx[A]+rlen(R)-lengths[B])
    th=max(ctx[A]+rlen(R) for R in rules for A in [R[0]])
    assert th==2**(q+1)+d+1
    assert pure_nodes['S']==2**(q+1)
    size=len(arity)+sum(1+len(ch)+sum(map(len,outs)) for A,ch,outs in rules)
    return {'d':d,'q':q,'nested':nested,'N':N,'nonterminals':len(arity),'rules':len(rules),'size':size,'theta':th,'min_a_tree_nodes':pure_nodes['S']}

def small_grammar_language(d,q,nested=False):
    N,arity,rules=grammar(d,q,nested); by=defaultdict(list)
    for R in rules:by[R[0]].append(R)
    order=['A'+str(n) for n in range(1,N+1)]+['B'+str(i) for i in range(q+1)]+['S']
    from itertools import product
    lang={}
    for A in order:
        result=set()
        for _,ch,outs in by[A]:
            for vals in product(*(lang[B] for B in ch)):
                result.add(tuple(''.join(x if isinstance(x,str) else vals[x[0]][x[1]] for x in z) for z in outs))
        lang[A]=result
    assert {w[0] for w in lang['S']}==stage_language(N,d)
    return len(lang['S'])

L40=set('''aaabc aabac aabca abaac abaca abcaa baaac baaca bacaa bcaaa
aaaaac aaaaca aaaacb aaacaa aaacab aaacba aacaaa aacaab aacaba aacbaa
acaaaa acaaab acaaba acabaa acbaaa caaaaa caaaab caaaba caabaa cabaaa
cbaaaa aaaaaab aaaaaba aaaabaa aaabaaa aabaaaa abaaaaa baaaaaa aaaaaaaa bc'''.split())
W48=set('''aaabbcc aaabcbc aaabccb aaacbbc aaacbcb aaaccbb
aabbcca aabcabc aabcacb aabcbca aabccba aacbabc aacbacb aacbbca aacbcba aaccbba
abbccaa abcaabc abcaacb abcabca abcacba abcbcaa abccbaa acbaabc acbaacb acbabca acbacba acbbcaa acbcbaa accbbaa
bbccaaa bcaaabc bcaaacb bcaabca bcaacba bcabcaa bcacbaa bcbcaaa bccbaaa
cbaaabc cbaaacb cbaabca cbaacba cbabcaa cbacbaa cbbcaaa cbcbaaa ccbbaaa'''.split())
L67={'a'*10}|{'a'*i+z+'a'*(8-i) for i in range(9) for z in ('bc','cb')}|W48

def evaluate_marked_tree(d,q,selected,nested=False):
    def rec(i,index):
        if i==1 and index in selected:return ('bb','cc')
        if i==0:return ('a'*(d//2),'a'*(d//2))
        x=rec(i-1,2*index);y=rec(i-1,2*index+1)
        return (x[0]+y[0],y[1]+x[1] if nested else x[1]+y[1])
    x=rec(q,0)
    return 'a'+x[0]+'a'+x[1]+'a'

def run():
    for label,L in [('X1_40',L40),('CA_67',L67)]+[(f'stage_N{N}_d4',stage_language(N,4)) for N in range(8,12)]:
        counts=exact_distributions(L); rectangles=exact_rectangles(L)
        print(label,'words',len(L),'tuples/contexts/comparisons',counts,'rectangles',rectangles,'EXACT PASS')
    assert len(L40)==40 and 'bc' in L40 and 'acb' not in L40
    assert len(L67)==67 and 'bccbaaa' in L67 and 'bccb'+'a'*6 not in L67
    for mode in [False,True]:
        print('SMALL GRAMMAR EXACT LANGUAGE',mode,small_grammar_language(4,1,mode))
        print('CONCRETE GRAMMAR',json.dumps(grammar_audit(64,4,mode),sort_keys=True))
    N=1027; d=64; delta=128; kap='bbacc'; h=129; lam=898; budget=769
    for p,g,r in [(129,449,321),(193,449,257),(129,641,129),(193,513,193)]:
        w='a'*p+'bb'+'a'*g+'cc'+'a'*r
        assert member(w,N,d) and w.count('a')==N-delta and p+r>=3
    for w in ['a'*129+'bbbb'+'a'*385+'cccc'+'a'*257,
              'a'*129+'bbbb'+'a'*513+'cccc'+'a'*129]:
        assert member(w,N,d) and w.count('a')==N-2*delta
    assert evaluate_marked_tree(d,4,set())=='a'*N
    for mode,triples in [(False,[(129,449,321),(193,449,257)]),(True,[(129,641,129),(193,513,193)])]:
        for idx,(p,g,r) in zip((2,3),triples):
            assert evaluate_marked_tree(d,4,{idx},mode)=='a'*p+'bb'+'a'*g+'cc'+'a'*r
        expected='a'*129+'bbbb'+'a'*(513 if mode else 385)+'cccc'+'a'*(129 if mode else 257)
        assert evaluate_marked_tree(d,4,{2,3},mode)==expected
    print('ACTUAL MARKED DERIVATION TREES: 4 single + 2 double substitutions PASS')
    assert member('a'+kap+'a'*(lam-1),N,d)
    target='a'+kap+'a'+kap+'a'*(budget-2)
    assert target.count('a')==N-2*delta and not member(target,N,d)
    assert N>=4*delta+1 and budget==N-2*h and 128>97
    print('IH WITNESSES PASS: delta=128 h=129 lambda=898 outer_budget=769 total_a=771')
    for q in range(3,8):
        d=2**(q+2);N=d*2**q+3;theta=d+2**(q+1)+1
        assert 2*d>theta and N-2*(2*d+1)>=3
        print('ROOM FAMILY',q,d,N,theta,'N/delta',N/(2*d))
    print('No closure search. No cap/truncation. Full finite checks above; general claims use hand proofs.')
    print('ALL CHECKS PASSED')



# Generated once from archived Round14 code, not generated by this checker.
TR_CERT = {'seed': ['aaaaaaaaaaaaa', 'abcaaaaaaaaa', 'abcacbaaaaaa', 'acbaaaaaaaaaa'], 'steps': [(('a', 'aaaaaaaaa'), ('aa', 'aaaaaaaa'), ('', 'a', 'aa'), ('', 'bc', ''), 'aabcaaaaaaaa'), (('a', 'aaaaaaaaaa'), ('aa', 'aaaaaaaaa'), ('', 'a', 'a'), ('', 'cb', ''), 'aacbaaaaaaaaa'), (('abc',), ('bca',), ('a', 'aaaaaaaa'), ('', 'acbaaaaaa'), 'bcaacbaaaaaa'), (('acb',), ('cba',), ('a', 'aaaaaaaaa'), ('bca', 'aaaaaa'), 'bcacbaaaaaaa'), (('acb',), ('cba',), ('a', 'aaaaaaaaa'), ('bc', 'aaaaaaa'), 'bccbaaaaaaaa'), (('bca',), ('abc',), ('a', 'aaaaaaaa'), ('', 'cbaaaaaaa'), 'abccbaaaaaaa'), (('a', 'aaaaaaa'), ('aa', 'aaaaaa'), ('', 'a', 'aaaa'), ('', 'bccb', ''), 'aabccbaaaaaa'), (('abc',), ('bca',), ('a', 'aaaaaaaa'), ('', 'aaaaaaaaa'), 'bcaaaaaaaaaa'), (('acb',), ('cba',), ('a', 'aaaaaaaaa'), ('', 'aaaaaaaaaa'), 'cbaaaaaaaaaaa'), (('cbaa',), ('bca',), ('', 'aaaaaaaaa'), ('bc', 'aaaaaa'), 'bcbcaaaaaaa'), (('bc', 'aaaaaaaa'), ('cb', 'aaaaaaaaa'), ('', 'a', 'a'), ('', 'cb', ''), 'cbcbaaaaaaaaa'), (('cbaa',), ('bca',), ('', 'aaaaaaaaa'), ('cb', 'aaaaaaa'), 'cbbcaaaaaaaa'), (('bca',), ('abc',), ('a', 'aaaaaaaa'), ('bc', 'aaaaaa'), 'bcabcaaaaaa'), (('bca',), ('abc',), ('a', 'aaaaaaaa'), ('', 'bcaaaaaa'), 'abcbcaaaaaa'), (('a', 'aaaaaa'), ('aa', 'aaaaa'), ('', 'a', 'aaaaa'), ('', 'bcbc', ''), 'aabcbcaaaaa'), (('cb', 'aaaaaaa'), ('bc', 'aaaaaa'), ('', 'a', 'aaa'), ('b', 'c', ''), 'bbccaaaaaa'), (('bc', 'aaaaaa'), ('bccb', 'aaaa'), ('', 'a', 'aaa'), ('b', 'c', ''), 'bbccbcaaaa'), (('bcaaaa',), ('bcbca',), ('', 'aaaaaa'), ('bc', 'aaa'), 'bcbcbcaaaa'), (('bca',), ('abc',), ('a', 'aaaaaaaa'), ('cb', 'aaaaaaa'), 'cbabcaaaaaaa'), (('cb', 'bc'), ('bc', 'cb'), ('', 'a', 'aaaaaaa'), ('b', 'c', 'aaaa'), 'bbcccbaaaa'), (('bc', 'cbaa'), ('bc', 'bca'), ('', 'a', 'aaaaa'), ('b', 'c', 'aa'), 'bbccbcaaa')], 'w4': 'bbccbcaaaa', 'w7': 'bbccbcaaa'}

def replay_lift(u,v):
    mapping={'a':'a','b':u,'c':v}
    def mu(w):return ''.join(mapping[z] for z in w)
    K={mu(w) for w in TR_CERT['seed']}
    steps=list(TR_CERT['steps'])
    # Append explicit unary contradiction, which works even when u,v contain a.
    steps.append((('aaaa',),('aaa',),('bbccbc',''),('a'*9,''),'a'*12))
    for x,y,e,f,w in steps:
        x=tuple(map(mu,x));y=tuple(map(mu,y));e=tuple(map(mu,e));f=tuple(map(mu,f));w=mu(w)
        assert len(x)==len(y) in (1,2) and all(x) and all(y)
        assert tuple(map(set,x))==tuple(map(set,y))
        assert len(e)==len(f)==len(x)+1
        if len(x)==2:assert e[1] and f[1]
        assert fill(e,x) in K and fill(e,y) in K and fill(f,x) in K
        assert fill(f,y)==w
        K.add(w)
    assert 'a'*12 in K
    return len(steps)

def check_normalization():
    cases=0
    import re
    for L,N in [(L40,8),(L67,10)]+[(stage_language(n,4),n) for n in range(8,12)]:
        for w in L:
            if not w.startswith('a') or not w.endswith('a') or set(w)=={'a'}:continue
            left=len(w)-len(w.lstrip('a'));right=len(w)-len(w.rstrip('a'))
            if not 3<=left+right<N or not 0<w.count('a')<N:continue
            k=w[left:len(w)-right];norm=re.sub('a+','a',k)
            lam=w.count('a')-norm.count('a')
            assert 'a'+norm+'a'*(lam-1) in L
            cases+=1
    print('NORMALIZATION exact finite consequences',cases,'PASS')

if __name__=='__main__':
    run()
    total=0
    pairs=[('b','cc'),('bc','c'),('bb','cc'),('b','bc'),('b','b'),
           ('bac','c'),('baaaac','c'),('b','cac'),('a','b'),('bbacc','cabb')]
    for u,v in pairs:total+=replay_lift(u,v)
    print('LIFTED PRIMITIVE CERTIFICATES',len(pairs),'steps including unary contradiction',total,'PASS')
    check_normalization()
    print('FINAL EXIT: success (0)')
