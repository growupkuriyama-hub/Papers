"""Finite structural sanity checks for Fable Round-2 MS/Rc/CC proof.
Not a proof of tuple substitutability or of the quantified theorem.
"""
from itertools import product

def fill(E,x):
    assert len(E)==len(x)+1
    if len(x)==2:
        assert E[1] and all(x)
    if len(x)==1:
        assert x[0]
    return ''.join(E[i]+x[i] for i in range(len(x)))+E[-1]

def alph(w): return frozenset(w)

def check_rect_shapes(E0,E1,x,y):
    assert len(x)==len(y)==2
    assert all(x) and all(y) and E0[1] and E1[1]
    assert tuple(map(alph,x))==tuple(map(alph,y))
    return tuple(fill(e,z) for e,z in [(E0,x),(E0,y),(E1,x),(E1,y)])

count=0
for N in range(7,55):
  for db in range(1,N-3):
    for dc in range(1,N-3):
      i=N-db-dc
      if i<2: continue
      # The smaller original seed can be held fixed when transporting arbitrary short J.
      dsmall=min(db,dc)
      for dj in range(1,(N-1)//2+1):
        assert N-dsmall-dj>=2
      for dj in [1,(N-1)//2]:
        ip=N-db-dj
        if ip<2: continue # a nonminimal fixed seed is not an authorized transport
        uB,vB='bc','bbcc'
        uC,vC='bbcc','bc'
        uJ,vJ='bc','bc'
        x=(uC,vC+'a'*i); y=(uJ,vJ+'a'*ip)
        E0=('a'*(db-1),'a',''); E1=(uB,vB,'')
        z=check_rect_shapes(E0,E1,x,y)
        assert z[2]==uB+uC+vB+vC+'a'*i
        assert z[3]==uB+uJ+vB+vJ+'a'*ip
        assert z[0].count('a')==N-dc
        assert z[1].count('a')==N-dj
        xn=(uC,vC+'a'*(i-1));yn=(uJ,vJ+'a'*(ip-1))
        E0n=('a'*db,'a',''); E1n=(uB,'a',vB)
        z=check_rect_shapes(E0n,E1n,xn,yn)
        assert z[2]==uB+uC+'a'+vC+'a'*(i-1)+vB
        assert z[3]==uB+uJ+'a'+vJ+'a'*(ip-1)+vB
        assert z[0].count('a')==N-dc
        assert z[1].count('a')==N-dj
        count+=1
print('MS CROSS/NESTED TWO-HOLE TEMPLATES:',count,'PASS')

count=0
for chi in range(2,13):
  m=2*chi+1
  for alpha,beta,t in product(range(1,chi+1),range(1,chi+1),range(1,6)):
    if alpha+beta>=3:
      h=alpha+beta-1
      assert m>=alpha+beta+1
      P='ab';Q='ca';b='b'*t
      w1=P+'c'*h+b+'c'+Q
      w2=P+'c'*(h-1)+b+'cc'+Q
      E0=(P+'c'*(h-1),'c'+Q)
      assert fill(E0,('c'+b,))==w1
      assert fill(E0,(b+'c',))==w2
      assert alph('c'+b)==alph(b+'c')
      count+=1
  assert m>=chi+2 # enough for borrowing from an external c^gamma (gamma <= chi)
print('RR/CC ONE-HOLE WITNESS SHAPES:',count,'PASS')

# Disproof of an unqualified in-component-a extension of MS accounting.
u='ab';v='bc';N=15;d=3
external_a=N-d-(u+v).count('a')
assert external_a != N-d
print('GENERALIZATION CAUTION: internal-a changes exterior deficit accounting, PASS')
