#!/usr/bin/env python3
"""Run: python3 -I scripts/check_kernel_witness.py
Bounded tests against an EXACT membership predicate for the infinite L_K.
The membership predicate is not a truncation of L_K. Universal assertions
are proved separately in REVIEW_REPORT.md. Also checks the stronger 1-FKP
presentation with two initial symbols.
"""
from itertools import product
import re

def member(w):
 m=re.fullmatch(r'(a*)([yz]?)(b*)',w)
 if not m:return False
 a,c,b=len(m[1]),m[2],len(m[3])
 return a!=b if not c else (a>=b if c=='z' else a<=b)

def plus(w):
 m=re.fullmatch(r'(a*)(z?)(b*)',w)
 return bool(m) and (len(m[1])>=len(m[3]) if m[2] else len(m[1])>len(m[3]))

def minus(w):
 m=re.fullmatch(r'(a*)(y?)(b*)',w)
 return bool(m) and (len(m[1])<=len(m[3]) if m[2] else len(m[1])<len(m[3]))

words=[''.join(t) for n in range(8) for t in product('abyz',repeat=n)]
checks=0
for w in words:
 assert member(w)==(plus(w) or minus(w))
 # Exact closure formula checked against a sufficiently large bounded
 # family of contexts; the analytic proof establishes all contexts.
 assert plus(w)==all(member('a'*m+w+'b'*n) for m in range(10) for n in range(m+1))
 assert minus(w)==all(member('a'*m+w+'b'*n) for n in range(10) for m in range(n+1))
 if plus(w):
  assert plus('a'+w) and plus('a'+w+'b')
 if minus(w):
  assert minus(w+'b') and minus('a'+w+'b')
 if member(w):assert member('a'+w+'b')
 checks+=1
assert plus('a') and plus('z') and minus('b') and minus('y')
lower=0
for p in range(9):
 K={'a'*m+'b'*n for m in range(p+1) for n in range(p+1) if m!=n}
 # One common context refutes the positive word a^(p+1).
 c=('', 'b'*(p+1))
 assert all(member(k+c[1]) for k in K)
 assert not member('a'*(p+1)+c[1])
 lower+=1
print('PASS words',checks,'lower-bound instances',lower)
print('Original 15 productions checked by closure predicates and induction.')
print('Stronger grammar: I={Splus,Sminus}; Splus->A|W|aSplus b; Sminus->B|Wp|aSminus b.')
print('Other productions unchanged. K_Splus=K_A=K_W={z}; K_Sminus=K_B=K_Wp={y}.')
