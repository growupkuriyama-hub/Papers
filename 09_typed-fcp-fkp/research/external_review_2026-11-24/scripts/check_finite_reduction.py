#!/usr/bin/env python3
"""Run: python3 -I scripts/check_finite_reduction.py
Exact finite-language checks, including empty kernels, epsilon, empty L,
and closures equal to the infinite universe. None represents an infinite
set; products of nonempty infinite fibres are unbounded in length.
All non-epsilon fibres of the three tested typings are infinite.
This is computational evidence, not a proof of the general theorem.
"""
from itertools import product, combinations
from collections import Counter

U = ['', 'a', 'b', 'aa', 'ab', 'ba', 'bb']
TYPES = {
 'trivial': lambda w: 'e' if not w else 'p',
 'indicator_b': lambda w: 'e' if not w else ('z' if 'b' in w else 'p'),
 'a_parity': lambda w: 'e' if not w else str(w.count('a') % 2),
}

def dist(L, w):
 return frozenset((z[:i], z[i+len(w):]) for z in L
                  for i in range(len(z)-len(w)+1) if z[i:i+len(w)] == w)

def contexts(L, K):
 if K is None: return frozenset()  # any unbounded set, finite target
 if not K: return None  # all contexts
 return frozenset.intersection(*(dist(L,w) for w in K))

def closure(L, K):
 C = contexts(L,K)
 if C is None: return frozenset()  # bottom for a finite L over {a,b}
 if not C: return None  # Sigma*
 return frozenset(x for x in U if C <= dist(L,x))

def mul(parts):
 if any(p == frozenset() for p in parts): return frozenset()
 if any(p is None for p in parts): return None
 out = {''}
 for p in parts: out = {x+y for x in out for y in p}
 return frozenset(out)

def subset(a,b):
 if b is None: return True
 if a is None: return False
 return a <= b

stats=Counter()
for bits in range(1 << len(U)):
 L=frozenset(w for i,w in enumerate(U) if bits & (1<<i))
 for name,typ in TYPES.items():
  sorts=sorted({typ(x) for x in U})
  entries=[]
  for t in sorts:
   pool=[x for x in U if typ(x)==t]
   for k in range(3):
    for tup in combinations(pool,k):
     K=frozenset(tup); un=closure(L,K)
     typed=(frozenset({''}) if t=='e' else None) if un is None else frozenset(x for x in un if typ(x)==t)
     entries.append((K,t,un,typed))
     # Initial soundness equivalence, no pre-fixed assumption needed.
     assert subset(typed,L)==subset(un,L)==(K <= L)
     stats['initial_conditions']+=1
  bysort={t:[e for e in entries if e[1]==t] for t in sorts}
  for rank in range(3):
   for children in product(entries,repeat=rank):
    for ws in product(['','a','b'],repeat=rank+1):
     # The type of a representative, even when a kernel is empty.
     reps=[next(x for x in U if typ(x)==e[1]) for e in children]
     representative=ws[0]+''.join(x+w for x,w in zip(reps,ws[1:]))
     headtype=typ(representative)
     vals=[]
     for field in (0,3,2):
      parts=[frozenset({ws[0]})]
      for e,w in zip(children,ws[1:]): parts.extend([e[field],frozenset({w})])
      vals.append(mul(parts))
     ctx=[contexts(L,v) for v in vals]
     assert ctx[0]==ctx[1]==ctx[2], (L,name,children,ws,ctx)
     stats['star_instances']+=1
     for K,t,un,typed in bysort[headtype]:
      assert subset(vals[1],typed)==subset(vals[2],un), (L,name,K,children,ws)
      stats['rule_equivalences']+=1
 print('languages_completed',bits+1,dict(stats)) if bits in (31,63,95,127) else None
print('PASS',dict(stats))
