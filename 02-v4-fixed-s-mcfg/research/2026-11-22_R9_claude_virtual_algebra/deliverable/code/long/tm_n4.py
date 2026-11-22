#!/usr/bin/env python3
"""R9 long run: token-level closure of the Thue--Morse host, n = 4 (budgeted).
A budgeted closure shows nothing (it is neither a proof of closedness nor of the absence of
a shortcut); the run only records how fast the closure grows.  Usage:
    python3 -I tm_n4.py 100000 > tm_n4.log
"""
import sys, time, importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('ra', os.path.join(here, '..', 'run_all.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
budget = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
n, N = 4, 16
for split in (False, True):
    seeds = m.tm_tokens(n, split)
    t0 = time.time()
    C = m.Closure(seeds, m.ty_tok, max_words=budget,
                  stop=lambda w: set(w) <= {'a', 'b'} and len(w) < N).run()
    pure = sum(1 for w in C.S if set(w) <= {'a', 'b'})
    a4 = sum(1 for w in C.S if 'aaaa' in w)
    print('TM n=4 escapes %s: %d native -> %d words (budget %d, truncated=%s), shortcut=%r, '
          'pure host words %d, words containing aaaa %d' % (
              'per type A/B' if split else 'one per level', len(seeds), len(C.S), budget,
              C.truncated, C.found, pure, a4))
    sys.stderr.write('%.1fs\n' % (time.time() - t0))
