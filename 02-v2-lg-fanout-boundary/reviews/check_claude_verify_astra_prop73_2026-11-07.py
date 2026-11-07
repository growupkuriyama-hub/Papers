#!/usr/bin/env python3
"""check_claude_verify_astra_prop73_2026-11-07.py (standard library only)

Claude-side check of the new example in Astra's report (S6, README (194)):
Q3 = F_{5,4}, Q2 = {(1,15),(6,11),(11,7),(16,3)}.  Q satisfies (T) (Theorem 2.1 of the
closure report, gamma brute-forced in [0,24]^3, enough since all coordinates of Q are <= 16),
but {P} u Q3 with the shortest P = (1,15) does not; P - A = 2(B-A) - 10(M-A) + 3(Z-A).
No code of the Astra script is used.  Run: python3 check_claude_verify_astra_prop73_2026-11-07.py
"""
import itertools
def add(p,q): return tuple(a+b for a,b in zip(p,q))
def sub(p,q): return tuple(a-b for a,b in zip(p,q))
def supp(v): return frozenset(i for i in range(3) if v[i])
def T(Q):
    Qs=set(Q); bad=[]
    for q in Q:
        for q2 in Q:
            if q==q2 or supp(q)!=supp(q2): continue
            h=sub(q2,q); S=supp(h)
            one=tuple(1 if i in S else 0 for i in range(3))
            L0=add(tuple(max(-x,0) for x in h),one); R0=add(tuple(max(x,0) for x in h),one)
            # brute gamma box
            for g in itertools.product(range(0,25),repeat=3):
                if (add(L0,g) in Qs)!=(add(R0,g) in Qs): bad.append((h,g)); break
            if bad: return bad
    return bad
Q3=[(1,5,1),(6,1,1),(2,2,2),(1,1,4)]
Q2=[(1,15,0),(6,11,0),(11,7,0),(16,3,0)]
print('full Q (T) violations:',T(Q3+Q2))
print('{P} u Q3 violations:',T(Q3+[(1,15,0)])[:1])
A,B,M,Z=Q3; P=(1,15,0)
comb=tuple(2*x-10*y+3*z for x,y,z in zip(sub(B,A),sub(M,A),sub(Z,A)))
print('2(B-A)-10(M-A)+3(Z-A)=',comb,' P-A=',sub(P,A))
print('lengths Q2:',[sum(p) for p in Q2],' Q3:',[sum(p) for p in Q3])
# closedness of Q3
S=set(Q3); print('Q3 closed:',all(min(sub(add(p,q),r))<1 or sub(add(p,q),r) in S for p in Q3 for q in Q3 for r in Q3))
