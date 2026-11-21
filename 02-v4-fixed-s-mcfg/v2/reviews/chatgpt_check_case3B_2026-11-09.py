#!/usr/bin/env python3
"""Independent SUB1/SUB2 proof builder and auditor, Python 3 stdlib only.
No import/execution of Claude's checker. Fixed KL proof DATA transcribed from
chatgpt_case2_branches App.A. Every other construction is implemented here.
Run: python3 -I chatgpt_check_case3B_2026-11-09.py
Optional: --certificates writes the complete seed/step records as JSON to stdout.
Finite tests are not membership proofs for infinite languages.
"""
from dataclasses import dataclass, asdict
from itertools import product, groupby
import argparse
import json

@dataclass(frozen=True)
class Rule:
    witness: tuple
    source: tuple
    target: tuple
    context: tuple

def instantiate(context, components):
    if len(context) != len(components)+1:
        raise ValueError('arity mismatch')
    parts = [context[0]]
    for component, suffix in zip(components, context[1:]):
        parts.extend((component, suffix))
    return ''.join(parts)

def audit(known, rule):
    E, X, Y, H = rule.witness, rule.source, rule.target, rule.context
    n = len(X)
    if n not in (1, 2) or len(Y) != n or not all(X+Y):
        raise ValueError('invalid components')
    if len(E) != n+1 or len(H) != n+1:
        raise ValueError('invalid contexts')
    if n == 2 and (not E[1] or not H[1]):
        raise ValueError('empty separator')
    if [set(x) for x in X] != [set(y) for y in Y]:
        raise ValueError('different component contents')
    for w in (instantiate(E,X), instantiate(E,Y), instantiate(H,X)):
        if w not in known:
            raise ValueError(('missing premise', w))
    return instantiate(H,Y)

class Proof:
    def __init__(self, seeds):
        self.seeds = frozenset(seeds)
        self.words = set(seeds)
        self.steps = []
    def infer(self,E,X,Y,H):
        step = Rule(tuple(E),tuple(X),tuple(Y),tuple(H))
        result = audit(self.words,step)
        self.steps.append((step,result))
        self.words.add(result)
        return result
    def replay(self):
        known = set(self.seeds)
        for step, expected in self.steps:
            result = audit(known,step)
            if result != expected:
                raise ValueError('wrong recorded conclusion')
            known.add(result)
        if known != self.words:
            raise ValueError('unjustified extra word')
    def export(self):
        return {'seeds': sorted(self.seeds), 'steps':[
            dict(asdict(s),conclusion=w) for s,w in self.steps]}

def intervals(word, letter):
    result=[]; pos=0
    for c, chars in groupby(word):
        size=len(list(chars))
        if c == letter:
            result.append((pos,pos+size))
        pos += size
    return result

class Builder:
    def __init__(self, k, seeds):
        self.k=k
        self.proof=Proof(seeds)
    def move(self,word,x,donor,recipient):
        spans=intervals(word,x)
        i,j=sorted((donor,recipient))
        a,b=spans[i]; c,d=spans[j]
        left_to_right = donor == i
        sizes=(2,1) if left_to_right else (1,2)
        assert spans[donor][1]-spans[donor][0]>=2
        X=tuple(x*n for n in sizes); Y=X[::-1]
        H=(word[:b-sizes[0]],word[b:c],word[c+sizes[1]:])
        quad=next(w for w in sorted(self.proof.seeds) if x*4 in w)
        cut=quad.index(x*4)
        E=(quad[:cut],x,quad[cut+4:])
        return self.proof.infer(E,X,Y,H)
    def allocate(self,w,x,wanted):
        while True:
            have=[b-a for a,b in intervals(w,x)]
            assert len(have)==len(wanted) and sum(have)==sum(wanted) and min(wanted)>0
            if have==list(wanted): return w
            donor=next(i for i in range(len(have)) if have[i]>wanted[i])
            recipient=next(i for i in range(len(have)) if have[i]<wanted[i])
            w=self.move(w,x,donor,recipient)
    def delete_run(self,w,x,remove,keep):
        # Normalize all runs, put every spare copy at the survivor.
        n=len(intervals(w,x)); assert n>=2 and remove!=keep and w.count(x)>n
        sizes=[1]*n; sizes[keep]+=w.count(x)-n
        w=self.allocate(w,x,sizes)
        spans=intervals(w,x)
        if keep<remove:
            _,end=spans[keep]; start,_=spans[remove]
            U,u,V=w[:end-2],w[end:start],w[start+1:]
            self.move(w,x,keep,remove)
            return self.proof.infer((U,x+V),(x+u+x,),(x+x+u,),(U+x,V))
        start,_=spans[remove]; begin,_=spans[keep]
        U,u,V=w[:start],w[start+1:begin],w[begin+2:]
        self.move(w,x,keep,remove)
        return self.proof.infer((U+x,V),(x+u+x,),(u+x+x,),(U,x+V))
    def sb(self,w,left):
        assert len(intervals(w,'a'))==2
        return self.allocate(w,'a',(left,w.count('a')-left))
    def force_c(self,w):
        # Keep a b-run outside the c-span, then erase every other b-run.
        assert w.count('b')>len(intervals(w,'b'))
        while 'cccc' not in w:
            spans=intervals(w,'b'); first=w.index('c'); last=w.rindex('c')
            keep=next(i for i,(s,e) in enumerate(spans) if e<=first or s>last)
            remove=next(i for i in range(len(spans)) if i!=keep)
            w=self.delete_run(w,'b',remove,keep)
        return w

class Branch(Builder):
    def __init__(self,k,P,dP,Q,dQ):
        self.P=P; self.Q=Q; self.dP=dP; self.dQ=dQ
        self.root='a'+P+'a'+Q+'a'*(k-dP-dQ-2)
        super().__init__(k,{'a'*k,'bbbb',self.root,
            'a'+P+'a'*(k-dP-1),'a'+Q+'a'*(k-dQ-1)})
        self.blocks={(P,dP):'a'+P+'a'*(k-dP-1),(Q,dQ):'a'+Q+'a'*(k-dQ-1)}
    def exchange(self,w,index,old,new):
        F,d=old; C,e=new; need=1+max(0,e-d)
        counts=[b-a for a,b in intervals(w,'a')]
        target=[1]*3; target[index]=sum(counts)-2
        w=self.allocate(w,'a',target)
        assert target[index]>=need
        oldpart='a'*need+F
        newpart='a'*(1+max(0,d-e))+C
        E=('', 'a'*(self.k-max(d,e)-1))
        self.sb(self.blocks[old],need)
        self.sb(self.blocks[new],1+max(0,d-e))
        spans=intervals(w,'a'); start=spans[index][1]; end=spans[index+1][0]
        assert w[start:end]==F
        return self.proof.infer(E,(oldpart,),(newpart,),(w[:start-need],w[end:]))
    def separate(self,A,B):
        assert A[1]+B[1]<=self.k-3
        jobs=[(0,(self.P,self.dP),A),(1,(self.Q,self.dQ),B)]
        # Repair: a-increasing replacements precede a-decreasing ones.
        jobs.sort(key=lambda job: job[2][1]-job[1][1])
        w=self.root
        for pos,old,new in jobs:
            w=self.exchange(w,pos,old,new)
        return w
    def concatenate(self,A,B):
        key=(A[0]+B[0],A[1]+B[1])
        if key not in self.blocks:
            assert key[1]<=self.k-4
            w=self.separate(A,B)
            w=self.delete_run(w,'a',1,0)
            self.blocks[key]=self.sb(w,1)
        return key
    def power(self,A,n):
        result=A
        for _ in range(n-1): result=self.concatenate(result,A)
        return result

# Fixed proof data, not prover code, from the specified prior report App.A.
KL={
'bcb':[
(('', 'a'),('aaabcba',),('abcbaabcb',),('a','')),
(('', 'b','a'),('aabcb','cba'),('abc','aabcb'),('','bcbb','')),
(('', 'b','a'),('aabc','bcba'),('aabcb','cba'),('','bbcb','')),
(('', 'aabcb'),('aabcb',),('abcbcbb',),('','bbcbcba'))],
'bcc':[
(('', 'c','a'),('aabc','bcca'),('abccb','cbcca'),('','cbcc','')),
(('', 'aa'),('aaabcc',),('abccbccbcc',),('','bcca')),
(('abccb','cbcca'),('cbcc',),('ccbc',),('abccbcbcc','a'))],
'bbc':[
(('', 'aa'),('aaabbc',),('abbcbbcbbc',),('','bbca')),
(('', 'b','a'),('aabbc','bca'),('abbcb','cbbca'),('','bbcb','')),
(('abbc','bcbbca'),('bbcb',),('bbbc',),('abbcb','cbbca'))],
'xpxxq':[
(('', 'aaa'),('axpxxqa',),('axpxxqxpxxq',),('aaxpxxq','')),
(('', 'x','a'),('aaxp','xqxpxxqa'),('aaxpx','qaxpxxq'),('','xxqxpx','')),
(('', 'x','a'),('aaxpx','qxpxxqa'),('aaxp','xqaxpxxq'),('','xqxpxx','')),
(('aaxp','xpxxq'),('xxqaxpxxq',),('xxxqxpxqa',),('aaxpxqxpx',''))],
'pxxqx':[
(('', 'aa'),('aaapxxqx',),('apxxqxapxxqx',),('','pxxqxa')),
(('', 'x','a'),('aapxxqxpx','qxa'),('apxxqxap','xqxa'),('','xqxpxx','')),
(('', 'x','a'),('aapxxqxp','xqxa'),('apxxqxpx','qxaa'),('','xxqxpx','')),
(('apxxqx','qxa'),('apxxqxpxx',),('apxqxpxxx',),('','xqxpxqxaa'))]}

def kl_seeds(F,k=6,d=1):
    seeds={'a'*k}
    for j in (1,2,3):
        for s in range(1,k-j*d): seeds.add('a'*s+F*j+'a'*(k-j*d-s))
    for s in range(1,k-2*d):
        for t in range(1,k-2*d-s):
            seeds.add('a'*s+F+'a'*t+F+'a'*(k-2*d-s-t))
    return seeds

def lifted(B,A,template,mapping):
    F,d=A; k=B.k; assert k>=6*d
    for n in (1,2,3):
        key=B.power(A,n)
        for s in range(1,k-n*d): B.sb(B.blocks[key],s)
    separated=B.separate(A,A)
    for s in range(1,k-2*d):
        for t in range(1,k-2*d-s):
            B.allocate(separated,'a',(s,t,k-2*d-s-t))
    h=lambda w: ''.join(mapping[c] if c!='a' else 'a'*d for c in w)
    def ctx(E): return ('a'*(k-6*d)+h(E[0]),)+tuple(h(x) for x in E[1:])
    for E,X,Y,H in KL[template]:
        result=B.proof.infer(ctx(E),tuple(map(h,X)),tuple(map(h,Y)),ctx(H))
    assert 'cccc' in result
    return result

def route(F):
    if F[0]==F[-1]=='c': return 'bcb',{'b':'c','c':F[1:-1]}
    if F.startswith('cc'): return 'bbc',{'b':'c','c':F[2:]}
    if F.endswith('cc'): return 'bcc',{'b':F[:-2],'c':'c'}
    if 'cc' in F and F[0]!=F[-1]:
        i=F.index('cc')
        if F[0]=='c':
            p,q=F[1:i],F[i+2:]; assert p and q
            return 'xpxxq',{'x':'c','p':p,'q':q}
        p,q=F[:i],F[i+2:-1]; assert p and q
        return 'pxxqx',{'x':'c','p':p,'q':q}
    return None

def reject(B,A):
    choice=route(A[0])
    if choice: return lifted(B,A,*choice)
    F=A[0]
    if all(x!=y for x,y in zip(F,F[1:])) and F[0]!=F[-1]:
        return None
    key=B.power(A,4)
    return B.force_c(B.blocks[key])

def finish(label,B,w,records):
    B.proof.replay()
    records[label]=B.proof.export()
    print(label,'steps',len(B.proof.steps),'forced',w)


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--certificates',action='store_true')
    args=parser.parse_args(); records={}
    for template,steps in KL.items():
        pr=Proof(kl_seeds(template))
        for E,X,Y,H in steps: w=pr.infer(E,X,Y,H)
        pr.replay()
        assert any(x*4 in w for x in set(template))
    print('KL base certificates: 5 passed')
    B=Builder(7,{'aaaaaaa','bbbb','abcccbbcccbaaaa'})
    w=B.force_c('abcccbbcccbaaaa'); finish('[2] bcccb',B,w,records)
    for F in ('bcb','cbb','cbcc'):
        B=Branch(12,F,1,'bc',1); w=reject(B,(F,1)); finish('[3] '+F,B,w,records)
    for mode in ('fusion','KL'):
        B=Branch(14,'bc',1,'cb',1)
        A=B.concatenate(('bc',1),('cb',1)) if mode=='fusion' else B.concatenate(('cb',1),('bc',1))
        if mode=='fusion':
            A=B.power(A,2); w=B.force_c(B.blocks[A])
        else: w=lifted(B,A,'bcb',{'b':'c','c':'bb'})
        finish('[4] '+mode,B,w,records)
    B=Branch(12,'bc',1,'bcbc',3)
    A=B.power(('bc',1),2)
    wlo=B.sb(B.blocks[('bcbc',3)],1); whi=B.sb(B.blocks[A],1)
    delta=whi.count('a')-wlo.count('a'); assert delta==1
    E=(wlo[:-1],''); H=('a'*(12-delta-1),'')
    w=B.proof.infer(E,('a'*(1+delta),),('a',),H)
    assert w=='a'*11; finish('[5] linear loss',B,w,records)
    seeds={'a'*5,'bbbb'}
    for F,d in [('cbbc',1),('cbbccbbc',2)]:
        for s in range(1,5-d): seeds.add('a'*s+F+'a'*(5-d-s))
    B=Builder(5,seeds)
    B.proof.infer(('', 'b',''),('b','bb'),('bb','b'),('ac','bcc','caa'))
    B.proof.infer(('', 'b',''),('bb','b'),('b','bb'),('aac','cc','bca'))
    w=B.proof.infer(('', 'bcaa'),('aacb',),('acbbbcc',),('','ccbbbca'))
    finish('[8] cbbc',B,w,records)
    # Independent finite classification search: no Claude routines or logs read.
    total=0; failures=[]; survivors=[]; steps=0
    for k,d in ((8,1),(12,1),(16,2)):
        for n in range(2,8):
            for letters in product('bc',repeat=n):
                F=''.join(letters)
                if set(F)!=set('bc') or 'cccc' in F: continue
                B=Branch(k,F,d,'bc',1)
                w=reject(B,(F,d)); B.proof.replay(); steps+=len(B.proof.steps)
                total+=1
                expected=F in {'bc'*(n//2),'cb'*(n//2)} and n%2==0
                if w is None:
                    survivors.append((k,d,F))
                    if not expected: failures.append((k,d,F))
                elif 'cccc' not in w: failures.append((k,d,F))
    print('Finite block search:',total,'instances;',steps,'SUB steps;',len(survivors),'alternating survivors;',len(failures),'unexcluded nonalternating candidates')
    assert not failures
    # Regression for the general chain lemma's replacement-order defect.
    k,p,q,e,f=1200,3,3,1196,1
    assert p<=k/(50*2**3) and q<=k/(50*2**3) and e+f==k-3
    assert k-p-q-2 < 1+e-p
    assert k-p-f-2 >= 1+e-p
    print('Budget regression: original P-first order fails; Q-first order has sufficient a')
    checked=0
    for k in range(7,31):
        for p in range(1,k-3):
            for q in range(1,k-p-2):
                for e in range(1,k-3):
                    for f in range(1,k-e-2):
                        current=k-p-q
                        for change in sorted((e-p,f-q)):
                            assert current-2>=1+max(0,change)
                            current-=change
                        assert current==k-e-f>=3
                        checked+=1
    print('Replacement budgets:',checked,'integer cases passed')
    # b-run count at all joins, independently from the proof classifier.
    count=0
    for n in range(2,10):
        for letters in product('bc',repeat=n):
            F=''.join(letters)
            if set(F)!=set('bc'): continue
            rho=len(intervals(F,'b')); join=int(F[0]==F[-1]=='b')
            assert len(intervals(F*4,'b'))==4*rho-3*join
            count+=1
    print('F^4 b-run identity:',count,'words passed')
    # Deliberately malformed inference must not pass.
    try:
        audit({'bbbb'},Rule(('', '', ''),('b','bbb'),('bb','bb'),('', 'b','')))
    except ValueError: pass
    else: raise AssertionError('empty middle accepted')
    print('ALL INDEPENDENT CHECKS PASSED')
    if args.certificates: print(json.dumps(records,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
