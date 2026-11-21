"""One generic SUB_1/SUB_2 closure with cap |W| (sound, incomplete)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sys, time, re, resource
from r7lib import *
from codes import CODES
host, code, n, pol, budget = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5])
R,S=(spine_grammar(n,'a',CODES[code]) if host=='spine' else tm_grammar(n,CODES[code]))
m=set('a') if host=='spine' else set('ab')
W=tree_yield(R,S); N=len(W); mem=member_fn(R,S)
seeds=esc_words(R,S,1)
t=time.time()
c=Closure(seeds,N,policy=pol,stop=lambda w:set(w)<=m and len(w)<N,max_words=budget,order='short').run()
stt='FOUND' if c.found else ('budget' if c.truncated else 'closed-under-cap')
line='%s %s n=%d policy=%s cap=|W|=%d seeds=%d words=%d processed=%d %s %.0fs maxrss=%dMB'%(host,code,n,pol,N,len(seeds),len(c.S),c.processed,stt,time.time()-t,resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//1024)
if c.found:
    st=c.certificate(c.found); k=replay(st,mem,c.found); line+=' shortcut=%d steps=%d replayed'%(len(c.found),k)
print(line, flush=True)
