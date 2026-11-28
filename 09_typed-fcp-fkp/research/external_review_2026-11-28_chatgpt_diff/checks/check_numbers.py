from pathlib import Path
from itertools import product
import re

# abstract.txt is a transcription of the pinned main.tex abstract (l.73–94).
s = Path(__file__).with_name('abstract.txt').read_text()
print('Abstract whitespace tokens:', len(s.split()))
print('Abstract prose tokens (whitespace, excluding math):', len(re.sub(r'\$[^$]*\$', '', s).split()))
print('Abstract formula occurrences:', len(re.findall(r'\$[^$]*\$', s)))
assert len(s.split()) == 248

def w(i):
    return 'a' if i == 0 else '['+w(i-1)*2+']'

def u(i):
    return '('*i+'a'+')'*i

def spine(n):
    return 'a' if n == 0 else '['+spine(n-1)+u(n-1)+']'

print('n | F_n rules | H_n rules | ell | 4|P_H| | 2^(n-2) | |w_(n-1)| | normalized witness length')
for n in range(2,17):
    # enumerate RHS templates by path; represent binary direction as a bit
    f_rules = 1 + 2*(n-1) + sum(len(list(product((0,1), repeat=d))) for d in range(n))
    # typed child pairs, available nonterminals, exclude (1,1) for marked binary rule
    h_rules = n
    for i in range(1,n+1):
        children = (1,) if i == 1 else (1,2)
        h_rules += len(children) + sum(a != 1 or b != 1 for a,b in product(children, repeat=2))
    ell = len(w(n))-len(w(1))
    rhs = 4*h_rules
    bound = 2**(n-2)
    assert f_rules == 2**n+2*n-2
    assert h_rules == 6*n-4
    assert ell == 3*2**n-6
    assert len(w(n-1)) == 3*2**(n-1)-2
    assert len(spine(n)) == (n+1)**2
    assert len(u(n)) == 2*n+1
    assert len(w(n))-(n+3) == 3*2**n-n-5
    if n >= 10:
        assert rhs < bound
    print(n, f_rules, h_rules, ell, rhs, bound, len(w(n-1)), len(spine(n)), sep=' | ')
# n=10 is the first n>=2 satisfying this strict inequality.
assert all(4*(6*n-4) >= 2**(n-2) for n in range(2,10))
# Inductive step for all n >=10: left +24 < double left, right doubles.
assert 4*(6*10-4) > 24
# Operation count for Q intersect ((complement empty) marker (complement empty)).
print('Operation count:', 1 + 2 + 1 + 2 + 2)
assert 1 + 2 + 1 + 2 + 2 == 8
