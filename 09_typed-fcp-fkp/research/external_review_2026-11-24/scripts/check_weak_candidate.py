#!/usr/bin/env python3
"""Run: python3 -I scripts/check_weak_candidate.py
Checks the proposed UNtyped weak-2-FCP witness after adding a second
centre marker @ to KY2017 L1. Membership predicates are exact for the
infinite languages; test inputs are bounded. This does NOT test all CFGs
or resolve the fresh-identity/s0-typed version of op:weak-fcp.
"""
import re
from itertools import product

def central(w):
 m=re.fullmatch(r'([ab#]*)(c*)(d*)(e*)([ab]*)',w)
 if not m:return None
 v,c,d,e,z=m.groups()
 first=v.split('#')[0]
 return first.count('a')-first.count('b'),len(c),len(d),len(e)
def marked(w,ch):
 if w.count(ch)!=1:return False
 u,v=w.split(ch)
 return bool(re.fullmatch('[ab#]*',u)) and bool(re.fullmatch('[ab]*',v)) and u.replace('#','')[::-1]==v
def l2(w):
 t=central(w)
 return t is not None and t[0]>=0 and t[1]==t[2]
def l3(w):
 t=central(w)
 return t is not None and t[0]<=0 and t[2]==t[3]
def diagonal(w):
 t=central(w)
 return t is not None and t[1]==t[2]==t[3]
def l45(w):
 if not re.fullmatch(r'[^%]*%f*',w):return False
 base=w.split('%')[0]
 if re.fullmatch(r'[ab#]*\$[ab]*c*',base):return True
 for k in range(len(base)+1):
  if k and not base.endswith('c'*k):continue
  core=base[:-k] if k else base
  t=central(core)
  if t is not None and t[1]==t[2] and t[3]!=k:return True
 return False
def member(w):return marked(w,'$') or marked(w,'@') or l2(w) or l3(w) or l45(w)
def q(w):return bool(re.fullmatch('[ab]*',w)) and w.count('a')==w.count('b')
def f(w):
 return '#' in w and q(w.split('#',1)[0]) and bool(re.fullmatch('[ab#]*',w.split('#',1)[1]))
def u(w):
 m=re.fullmatch('(e*)([ab]*)(c*)',w)
 return bool(m) and len(m[1])!=len(m[3])
preds={
 'S1':lambda w:marked(w,'$') or marked(w,'@') or diagonal(w),
 'S2':lambda w:l2(w) or diagonal(w),
 'S3':lambda w:l3(w) or diagonal(w),
 'Q':q,'F':f,
 'H':lambda w:bool(re.fullmatch('c*d*',w)) and w.count('c')==w.count('d'),
 'E':lambda w:bool(re.fullmatch('e*',w)),
 'C':lambda w:bool(re.fullmatch('c*',w)),
 'J':lambda w:bool(re.fullmatch('d*e*',w)) and w.count('d')==w.count('e'),
 'T':lambda w:bool(re.fullmatch('[ab]*',w)), 'U':u,'S45':l45,
}
contexts={
 'S1':[('a#','a'),('b#','b')],
 'S2':[('',''),('a#','b')], 'S3':[('',''),('b#','a')],
 'Q':[('','#cd'),('a','b#de')], 'F':[('','cd'),('','ade')],
 'H':[('a#c','d')], 'E':[('a#cd','e')], 'C':[('b#c','de')],
 'J':[('b#d','e')], 'T':[('$','a%')], 'U':[('e','c%')], 'S45':[('','f')],
}
words={''.join(t) for n in range(5) for t in product('abcdef#$%@',repeat=n)}
for v in ('','a','b','ab','ba','a#','b#','ab#','ba#','a#b','b#a'):
 for i,j,k in product(range(5),repeat=3):
  for z in ('','a','b','ab'):
   words.add(v+'c'*i+'d'*j+'e'*k+z)
   for tail in range(3): words.add(v+'c'*i+'d'*j+'e'*k+z+'c'*tail+'%f')
for x in words:
 for nt,pred in preds.items():
  assert bool(pred(x))==all(member(a+x+b) for a,b in contexts[nt]), (nt,x)
print('PASS untyped candidate context predicates:',len(words),'words x',len(preds),'nonterminals')
print('Evidence only: equality with closures of nonterminal languages is proved separately.')
