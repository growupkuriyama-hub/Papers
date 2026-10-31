#!/usr/bin/env python3
"""Port checker for 02-v2 (run from this folder: python3 tools/check_port.py).

1. Every \\label of v1 (../02_fixed-h-mcfg/main.tex) is either in v2 main.tex or
   listed in PARKED (and then present in parked/parked_from_v1.tex).
2. Labels new in v2 are listed in NEW.
3. For every theorem-like environment carrying a ported label, the body in v2 is
   compared with v1 (whitespace-normalized); differences are reported so that
   intended edits can be reviewed (they are not errors by themselves).
"""
import re, sys
V1='../02_fixed-h-mcfg/main.tex'; V2='main.tex'; PKS=['parked/parked_from_v1.tex','parked/parked_u1_typing_level.tex']
PARKED={'subsec:rank-one', 'prop:unary-cyclic-linear', 'prop:linear-factor-sharp', 'app:three-letter-family', 'thm:rankone-polydata', 'subsec:necessity', 'sec:further', 'lem:flag-separation', 'prop:app-tl-congruence', 'prop:three-letter-family', 'app:binary-u1-quadratic', 'lem:app-lf-descent', 'lem:app-tl-recognition', 'prop:lg-needed-target', 'prop:nonabelian-needed-target', 'cor:typing-level-obstruction', 'lem:app-tl-reachable', 'subsec:baseline', 'prop:binary-u1-quadratic'}
NEW={'thm:A','thm:B','thm:C','cor:trivial-exact','op:S1',
     'sec:upper','sec:linear','sec:fanout-one','sec:fanout-two'}
def labels(s): return re.findall(r'\\label\{([^}]*)\}',s)
v1=open(V1,encoding='utf-8').read(); v2=open(V2,encoding='utf-8').read(); pk='\n'.join(open(x,encoding='utf-8').read() for x in PKS)
L1,L2,LP=set(labels(v1)),set(labels(v2)),set(labels(pk))
ok=True
missing=sorted(L1-L2-PARKED)
if missing: ok=False; print('v1 labels missing in v2 and not parked:',missing)
lost=sorted((L1&PARKED)-LP)
if lost: ok=False; print('parked labels not found in parked file:',lost)
extra=sorted(L2-L1-NEW)
if extra: ok=False; print('v2 labels neither from v1 nor in NEW:',extra)
dup=[l for l in set(labels(v2)) if labels(v2).count(l)>1]
if dup: ok=False; print('duplicate labels in v2:',dup)
env=r'\\begin\{(theorem|lemma|proposition|corollary|definition|remark|openproblem)\}(\[[^\]]*\])?\s*\\label\{([^}]*)\}(.*?)\\end\{\1\}'
def bodies(s): return {m.group(3):' '.join(m.group(4).split()) for m in re.finditer(env,s,re.S)}
B1,B2=bodies(v1),bodies(v2)
changed=[l for l in B2 if l in B1 and B1[l]!=B2[l]]
print(f'labels: v1={len(L1)} v2={len(L2)} parked={len(L1&PARKED)} new={len(L2-L1)}')
print('ported statements changed relative to v1 (review these):',changed if changed else 'none')
sys.exit(0 if ok else 1)
