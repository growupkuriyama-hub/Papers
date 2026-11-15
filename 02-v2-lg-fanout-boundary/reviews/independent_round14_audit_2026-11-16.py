#!/usr/bin/env python3
"""Independent Round 14 auditor: exact finite class check & independent replay of Claude-generated TR data.
The content-typing closure evaluator and replay below are written independently and do not call the submitted checking functions.
"""
from collections import defaultdict
from itertools import combinations,product
from pathlib import Path
import importlib.util

BASE=Path(__file__).resolve().parent
ORIG=BASE/'claude_round14_noncomm_Parikh_checker_2026-11-15.py'

def typ(t):
    return tuple(frozenset(s) for s in t)

def split_occurrences(w):
    n=len(w)
    for i in range(n):
        for j in range(i+1,n+1):
            yield (w[i:j],),(w[:i],w[j:])
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for h in range(k+1,n+1):
                    yield (w[i:j],w[k:h]),(w[:i],w[j:k],w[h:])

def put(ctx, seq):
    if len(seq)==1:return ctx[0]+seq[0]+ctx[1]
    return ctx[0]+seq[0]+ctx[1]+seq[1]+ctx[2]

def exact_class(S):
    distributions=defaultdict(set)
    for word in S:
        for tup,ctx in split_occurrences(word):
            distributions[tup].add(ctx)
    common=defaultdict(list)
    for t,es in distributions.items():
        for e in es:
            common[(len(t),typ(t),e)].append(t)
    checked=0
    for (_,_,e),items in common.items():
        for t in items[1:]:
            checked+=1
            if distributions[t]!=distributions[items[0]]:
                return False,(items[0],t,e),len(distributions),sum(map(len,distributions.values())),checked
    return True,None,len(distributions),sum(map(len,distributions.values())),checked

def shuffles2(N):
    return {'a'*i+'b'+'a'*(j-i-1)+'c'+'a'*(N-j-1) for i in range(N) for j in range(i+1,N)} | {'a'*i+'c'+'a'*(j-i-1)+'b'+'a'*(N-j-1) for i in range(N) for j in range(i+1,N)}

def independent_step_replay(seed,steps):
    known=set(seed)
    for i,entry in enumerate(steps):
        x,y,e,f,w=entry
        if len(x)!=len(y) or not all(x) or not all(y) or typ(x)!=typ(y):
            raise AssertionError(('type',i))
        if len(x)==2 and (not e[1] or not f[1]):raise AssertionError(('sep',i))
        if len(e)!=len(x)+1 or len(f)!=len(x)+1:raise AssertionError(('arity',i))
        prereqs=[put(e,x),put(e,y),put(f,x)]
        if any(p not in known for p in prereqs):raise AssertionError(('missing',i,prereqs))
        if put(f,y)!=w:raise AssertionError(('yield',i))
        known.add(w)
    return known

def skeleton(w):
    out=[]
    for a in w:
        if a!='a':out.append(a)
        elif not out or out[-1]!='A':out.append('A')
    return ''.join(out)

def run():
    # Independent finite counterexample to CA as stated.
    N=10
    S={'a'*N} | shuffles2(N) | {''.join(z) for z in product('bc',repeat=4) if set(z)==set('bc')}
    ok,w,tuples,contexts,comparisons=exact_class(S)
    assert ok and len(S)==105 and 'bccb' in S and 'bccb'+'a'*6 not in S
    assert 'a'+'bc'+'a'*7 in S and 'a'+'cb'+'a'*7 in S
    print('CA COUNTEREXAMPLE: |L|=%d N=10 type=content closed=%s tuples=%d contexts=%d checked_comparisons=%d' %(len(S),ok,tuples,contexts,comparisons))
    print('  units bc,cb: lambda=8 delta=2 for each, seed=bccb (zero outer a); e_2=6 >=3')
    print('  predicts bccb a^6 in L, but that word is ABSENT. CA requires initial host room.')
    # Stronger CA counterexample: an *initially positive-room* connected seed,
    # but with an a-count different from the additive value assumed without proof.
    words48 = '''aaabbcc aaabcbc aaabccb aaacbbc aaacbcb aaaccbb
    aabbcca aabcabc aabcacb aabcbca aabccba aacbabc aacbacb aacbbca aacbcba aaccbba
    abbccaa abcaabc abcaacb abcabca abcacba abcbcaa abccbaa acbaabc acbaacb acbabca acbacba acbbcaa acbcbaa accbbaa
    bbccaaa bcaaabc bcaaacb bcaabca bcaacba bcabcaa bcacbaa bcbcaaa bccbaaa
    cbaaabc cbaaacb cbaabca cbaacba cbabcaa cbacbaa cbbcaaa cbcbaaa ccbbaaa'''.split()
    assert len(words48)==48 and len(set(words48))==48
    singles = {'a'*i + z + 'a'*(8-i) for i in range(9) for z in ('bc','cb')}
    S67={'a'*10} | singles | set(words48)
    ok67, wit67, t67, c67, p67 = exact_class(S67)
    assert len(S67)==67 and ok67 and 'bccbaaa' in S67 and 'bccb'+'a'*6 not in S67
    assert 'abca'+'a'*6 in S67 and 'acba'+'a'*6 in S67
    print('CA STRONGER COUNTEREXAMPLE: |L|=67 N=10 type=content closed=%s tuples=%d contexts=%d comparisons=%d'%(ok67,t67,c67,p67))
    print('  single Rot bc,cb: lambda=8 delta=2; connected seed bccb a^3 IN L (t=3)')
    print('  CA still predicts bccb a^6 IN L (e_2=6), which is ABSENT.')
    print('  Missing hypotheses: initial two-unit seed must have ADDITIVE a-budget (t=6), not merely t>=3.')
    S82={'a'*10} | {'a'*i+'b'+'a'*(j-i-1)+'c'+'a'*(10-j-1) for i in range(10) for j in range(i+1,10)} | {'a'*i+'c'+'a'*(j-i-1)+'b'+'a'*(9-j-1) for i in range(9) for j in range(i+1,9)}
    ok82,w82,t82,c82,p82=exact_class(S82)
    assert ok82 and len(S82)==82
    print('INDEPENDENT B: 82-word finite target closed=%s tuple-keys=%d context-pairs=%d comparisons=%d'%(ok82,t82,c82,p82))
    # Claude code only creates the certificates. Every step is verified by the independent checker above.
    spec=importlib.util.spec_from_file_location('claude_round14_for_certificates_only',str(ORIG))
    source=importlib.util.module_from_spec(spec);spec.loader.exec_module(source)
    ncert=0;nsteps=0;nctrl=0;miss=0
    for n in range(7,41):
        for d1 in range(1,n):
            for d2 in range(1,n):
                if n-d1-d2<3:continue
                if d1==d2:
                    if source.conditions(n,d1,d2):
                        c,w4,w7=source.tr_derivation(n,d1,d2)
                        k=independent_step_replay(c.seed,c.steps)
                        assert w4==w7 and w4 in k
                        nctrl+=1
                    continue
                flip=False
                if source.conditions(n,d1,d2):a,b=d1,d2
                elif source.conditions(n,d2,d1):a,b=d2,d1;flip=True
                else:
                    if n>=4*max(d1,d2)+1:miss+=1
                    continue
                d,w4,w7=source.tr_derivation(n,a,b)
                k=independent_step_replay(d.seed,d.steps)
                assert w4 in k and w7 in k and skeleton(w4)==skeleton(w7)
                assert 1<=w4.count('a')<n and 1<=w7.count('a')<n and w4.count('a')!=w7.count('a')
                ncert+=1;nsteps+=len(d.steps)
    assert miss==0 and ncert==3270 and nctrl==244
    print('INDEPENDENT TR REPLAY: 3270 certificates %d primitive rule steps; 244 controls; gaps=%d; ALL PASS'%(nsteps,miss))
    # Algebraic range test, separate from the submitted conditions() implementation.
    for N in range(7,101):
        for d1 in range(1,N):
            for d2 in range(1,N):
                if N<4*max(d1,d2)+1:continue
                a=max(d1,d2);b=min(d1,d2);D=b-a;t=N-a-b;j=1+a-b
                assert 1<=a<=N-3 and 1<=b<=N-3 and t>=3
                assert N-2*a>=3 and N-2*b>=1 and N-3*a>=1
                assert j<=t-1 and N-3*a-j>=0 and 1<=3*a-D<=N-1
    print('INDEPENDENT TR RANGE: all positive deficits with N<=100 covered by symbolic inequalities')
    print('ALL INDEPENDENT AUDIT CHECKS PASSED')

if __name__=='__main__':run()