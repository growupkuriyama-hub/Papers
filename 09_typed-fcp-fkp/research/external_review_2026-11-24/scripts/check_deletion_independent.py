#!/usr/bin/env python3
"""Run: python3 -I scripts/check_deletion_independent.py
Independent checks of all datum-selected contexts and candidate refutations
for n=2,3,4; includes empty yields in the capture check. No learner is
simulated: exact candidate validity tests are isolated from Algorithm 1.
"""
from itertools import product

def levels(n):
 out=[{'a'}]
 for _ in range(n):
  E=out[-1];out.append({'['+x+y+']' for x in E for y in E}|{'{'+x+'}' for x in E})
 return out
def star(n):
 w='a'
 for _ in range(n):w='['+w+w+']'
 return w
def substrings(words):return {w[i:j] for w in words for i in range(len(w)+1) for j in range(i,len(w)+1)}
def quotient(L,c):
 u,v=c
 return {w[len(u):len(w)-len(v)] for w in L if len(w)>=len(u)+len(v) and w.startswith(u) and w.endswith(v)}
def context(d):
 if d[0]=='{':return ('{','}')
 depth=0
 for j in range(1,len(d)-1):
  if d[j] in '[{':depth+=1
  if d[j] in ']}':depth-=1
  if depth==0:
   x,y=d[1:j+1],d[j+1:-1]
   return ('[',y+']') if '{' in y else ('['+x,']')
 raise AssertionError(d)

for n in (2,3,4):
 E=levels(n);M=E[n]-{star(n)};prev=E[n-1];w=star(n-1)
 for d in M:
  c=context(d);assert quotient(M,c)==prev
  assert {x for x in quotient(M,c) if not ('{' in x or '}' in x)}=={w}
 bad={(x,y) for x in prev for y in prev if '['+x+y+']' not in M}
 assert bad=={(w,w)}
 assert all('['+w+y+']' not in prev for y in prev-{w})
 # Validity on the actual factor set of all short data.
 short={d for d in M if w not in d};obs=substrings(short)
 assert all('['+x+y+']' in M for x in prev&obs for y in prev&obs)
 assert not (prev&obs&{w})
 z='['+w+'{'*(n-1)+'a'+'}'*(n-1)+']';r=1+len(w)
 count=0
 for i in range(r+1):
  for j in range(i,r+1):
   p,x,q=z[:i],z[i:j],z[j:]
   suffix='{'*(n-1)+'a'+'}'*(n-1)+']'
   qprime=q[:-len(suffix)]+w+']'
   assert p+x+qprime==star(n)
   for k in quotient(M,(p,q)):
    assert p+k+qprime in E[n]
    assert ((p+k+qprime not in M)==(k==x))
    count+=1
 print('PASS n',n,'all datum contexts',len(M),'capture cases including epsilon',count,
       'short-data count',len(short),'short-data factors',len(obs))
