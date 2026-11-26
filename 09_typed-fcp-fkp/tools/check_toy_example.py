#!/usr/bin/env python3
"""Example 1.1 (toy fragment with agreement): exact check of the frame and
exemplar identities stated in the introduction of main.tex.
Usage: python3 -I check_toy_example.py
"""
from itertools import product
NPs=[('the','dog'),('John',)]; NPp=[('the','dogs'),]
NP=NPs+NPp
L=set()
for x in NPs: L.add(x+('barks',))
for x in NPp: L.add(x+('bark',))
for x,y in product(NP,NP): L.add(x+('saw',)+y)
L=frozenset(L)
subs={m[i:j] for m in L for i in range(len(m)) for j in range(i+1,len(m)+1)}
def D(x):
    return {(m[:i],m[i+len(x):]) for m in L for i in range(len(m)-len(x)+1) if m[i:i+len(x)]==x}
def ctxcl(C): return {x for x in subs if all(u+x+v in L for (u,v) in C)}
def kercl(K):
    C=set.intersection(*[D(k) for k in K]); return {x for x in subs if C<=D(x)}
S=lambda *w: tuple(w)
print('frame (_,barks):', sorted(ctxcl({((),('barks',))})))
print('kernel {John}:', sorted(kercl([('John',)])))
print('frame (John saw,_):', sorted(ctxcl({(('John','saw'),())})))
print('kernel {the dog,the dogs}:', sorted(kercl([('the','dog'),('the','dogs')])))
print('kernel {the dogs}:', sorted(kercl([('the','dogs')])), ' frame (_,bark):', sorted(ctxcl({((),('bark',))})))
print('S: kernel {John barks}:', kercl([('John','barks')])==set(L), ' frame (.,.):', ctxcl({((),())})==set(L))
pl=lambda x: any(w in ('dogs','bark') for w in x)
print('typed: (John saw,_) cap sg-fibre:', sorted(x for x in ctxcl({(('John','saw'),())}) if not pl(x)))
print('kernel {John} closure contains a plural word?', any(pl(x) for x in kercl([('John',)])))
print('any single NP word with closure = NP?', [k for k in NP if kercl([k])==set(NP)])

# assertions (exit code 1 on any mismatch)
import sys
sg = {('the', 'dog'), ('John',)}
npall = sg | {('the', 'dogs')}
checks = [
    ctxcl({((), ('barks',))}) == sg,
    kercl([('John',)]) == sg,
    ctxcl({(('John', 'saw'), ())}) == npall,
    kercl([('the', 'dog'), ('the', 'dogs')]) == npall,
    kercl([('the', 'dogs')]) == {('the', 'dogs')} == ctxcl({((), ('bark',))}),
    kercl([('John', 'barks')]) == set(L) == ctxcl({((), ())}),
    not any(pl(x) for x in kercl([('John',)])),
    [k for k in NP if kercl([k]) == set(NP)] == [],
]
print('ALL OK' if all(checks) else 'SOME CHECK FAILED')
sys.exit(0 if all(checks) else 1)
