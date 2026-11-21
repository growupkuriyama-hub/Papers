#!/usr/bin/env python3
"""R8 long run (not part of run_all.py): budgeted letter-level SUB closures of L(G_3)
(all native words, i.e. with the two-escape words) for the six codes, all occurrences,
stopping at a shortcut (a word of content {a} shorter than 8) or at the word budget.
Run from this directory:  python3 -I closure_n3.py > closure_n3.log
A budgeted 'no shortcut' shows nothing (R8 report, mandatory checks)."""
import importlib.util
import os
import sys
import time

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r8', os.path.join(here, '..', 'run_all.py'))
r8 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r8)

BUDGET = int(sys.argv[1]) if len(sys.argv) > 1 else 60000
for name in ('sq', 'exp', 'pal', 'rnd', 'rig', 'alt'):
    code = {i: r8.CODES[name](i) for i in range(1, 4)}
    alpha = sorted(set(''.join(code.values())) | {'a'})
    ty = r8.make_typing(r8.letter_cmap(alpha))
    seeds = r8.spine_language(3, 'a', lambda i: code[i])
    hT = {''.join(code[ord(ch) - 64] if ch != 'z' else 'a' for ch in tau) for tau in r8.arrangements(8, 3)}
    t = time.time()
    cl = r8.Closure(seeds, ty, stop=lambda w: set(w) == {'a'} and len(w) < 8, max_words=BUDGET).run()
    print('%-4s n=3 seeds=%d words=%d processed=%d truncated=%s shortcut=%s h(T(8))<=closure=%s non-token=%d  %.0fs'
          % (name, len(seeds), len(cl.S), cl.processed, cl.truncated, cl.found, hT <= cl.S,
             len(cl.S - hT), time.time() - t), flush=True)
    if cl.found:
        R, S = r8.spine_grammar(3, 'a', lambda i: code[i])
        mem = r8.member_fn(R, S)
        st = cl.certificate(cl.found)
        out, have = r8.replay(st, mem, ty)
        print('     shortcut certificate: %d steps, replayed from L(G_3) by check_step: %s' % (len(st), cl.found in have))
        for k, (E0, E1, x, y) in enumerate(st):
            print('       step %d: x=%r y=%r E0=%r E1=%r -> %s' % (k + 1, x, y, E0, E1, r8.fill(E1, y)))
