#!/usr/bin/env python3
"""Companion search to check_claude_mu_ab_2026-11-05.py (same engine, imported from it).
Concrete doubling A_0 -> ab, A_i -> A_{i-1}A_{i-1} | e_i.  Step 1: all (e_1, e_2) with |e_1| <= 2,
|e_2| <= 3 at depth m = 2, keeping those whose closure is closed (brute force).  Step 2: for those,
all e_3 with |e_3| <= 3 at depth m = 3.  'shortcut' = a shorter ab-word is forced (certificate
replayed); 'closed' = closure is genuinely closed (no shortcut at all from these seeds);
'capped'/'stopped' = observation within the cap / word limit (1500 words or 20 s per run) only.
Windows: py -3 search_m3_escapes.py   (both files in one folder)"""
import os
import time
import importlib.util
from itertools import product
from collections import Counter

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    'chk', os.path.join(here, 'check_claude_mu_ab_2026-11-05.py'))
chk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chk)

cw = lambda n: [''.join(p) for p in product('abc', repeat=n) if 'c' in p]
t0 = time.time()
pairs = [(e1, e2) for e1 in cw(1) + cw(2) for e2 in cw(1) + cw(2) + cw(3)]
ok2 = [p for p in pairs if chk.classify(2, {1: p[0], 2: p[1]}, 1500)[0] == 'closed']
print('m=2: %d pairs, closed: %d (%.0fs)' % (len(pairs), len(ok2), time.time() - t0), flush=True)
st, surv = Counter(), []
for k, (e1, e2) in enumerate(ok2):
    for e3 in cw(1) + cw(2) + cw(3):
        r, tr = chk.classify(3, {1: e1, 2: e2, 3: e3}, 1500, time_limit=20)
        st[r] += 1
        if r != 'shortcut':
            surv.append((e1, e2, e3, r))
            print('  survivor', (e1, e2, e3, r), flush=True)
    if k % 10 == 9:
        print('  progress %d/%d %s (%.0fs)' % (k + 1, len(ok2), dict(st), time.time() - t0), flush=True)
print('m=3 (|e_3| <= 3): %s (%.0fs)' % (dict(sorted(st.items())), time.time() - t0))
print('closed:', [s[:3] for s in surv if s[3] == 'closed'])
print('capped/stopped:', [s for s in surv if s[3] != 'closed'])
