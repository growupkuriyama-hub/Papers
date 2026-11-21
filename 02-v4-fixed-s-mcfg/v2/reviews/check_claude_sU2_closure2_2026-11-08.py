import sys
import sys,random,itertools
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.argv_saved=sys.argv
import importlib.util as _u
_sp=_u.spec_from_file_location('cl',os.path.join(os.path.dirname(os.path.abspath(__file__)),'check_claude_sU2_closure_2026-11-08.py'))
_m=_u.module_from_spec(_sp); _sp.loader.exec_module(_m); close,doubling=_m.close,_m.doubling
from collections import defaultdict
def antichain_violation(L):
    bw=sorted((w for w in L if 'b' in w), key=len)
    for i,x in enumerate(bw):
        for y in bw[i+1:]:
            if len(y)>len(x) and x in y: return (x,y)
    return None
random.seed(int(sys.argv[1])); n=int(sys.argv[2]); N=2**n
bw=[''.join(p) for k in range(1,5) for p in itertools.product('ab',repeat=k) if 'b' in p]
st=defaultdict(int)
for t in range(int(sys.argv[3])):
    ms=[random.choice(bw) for _ in range(n)]
    L,s=close(doubling(ms,n),N+int(sys.argv[4]))
    v=antichain_violation(L)
    pure=min((len(w) for w in L if 'b' not in w))
    st[(s, 'viol' if v else 'noviol', 'short' if pure<N else 'ok')]+=1
print(dict(st))
