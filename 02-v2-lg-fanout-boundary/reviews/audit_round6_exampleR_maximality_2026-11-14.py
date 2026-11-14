#!/usr/bin/env python3
"""Independent boundary check: correct non-maximal eta in Claude round-six example R.

Run alongside claude_fanout2_round6_sync_test_2026-11-14.py. Standard library only.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

SRC = Path(__file__).with_name('claude_fanout2_round6_sync_test_2026-11-14.py')
spec = spec_from_file_location('round6_original', SRC)
r6 = module_from_spec(spec)
spec.loader.exec_module(r6)

M, k, L0, C = 8, 6, 64, 50  # eta=B_6; its parent B_7 does have protected positions
N = 2 ** M
x = 'ab' * N + 'ab' + 'ac' * N

def marks_on_projected_windows(word, block, width=2, protect=C):
    indices = [i for i, ch in enumerate(word) if ch in block]
    projected = ''.join(word[i] for i in indices)
    counts = Counter()
    marks = set()
    for j in range(len(projected) - width + 1):
        edge = projected[j:j+width]
        counts[edge] += 1
        if counts[edge] <= protect:
            marks.update(indices[j:j+width])
    return marks

marks = marks_on_projected_windows(x, 'ace') | marks_on_projected_windows(x, 'bc')
component_offsets = (0, 2*N + 2)
parent_leaf_count = 2 ** (k+1)
parent_leaf_start = L0 // parent_leaf_count * parent_leaf_count
for offset in component_offsets:
    eta = set(range(offset + 2*L0, offset + 2*(L0 + 2**k)))
    parent = set(range(offset + 2*parent_leaf_start,
                       offset + 2*(parent_leaf_start + parent_leaf_count)))
    assert not (marks & eta), 'eta must be mark-free'
    assert marks & parent, 'parent must contain a mark (maximality)'

# Same algebraic counterexample, now on a genuinely maximal free eta.
r6.section6(M=M, cstar=C, k=k, L0=L0)
print('INDEPENDENT CHECK: eta=B_6 is mark-free, both parent components hit marks;')
print('the old same-rank bundling still needs incompatible holes,')
print('and the kappa-indexed Y/F example still passes. ALL CHECKS PASSED')
