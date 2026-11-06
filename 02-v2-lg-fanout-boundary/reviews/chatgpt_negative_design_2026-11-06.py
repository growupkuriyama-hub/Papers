#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replayable counterexample-design audit (standard library only).

This script provides genuine non-membership checks by exhaustive generation
of the finite MCFG candidate (a), not by bounded-length overapproximation.
Candidate (b) is infinite and uses an exact modular membership predicate.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from dataclasses import dataclass
from typing import Tuple

P = 'ab'


def cont(w: str) -> frozenset:
    return frozenset(w)


def fill(ctx: Tuple[str, ...], values: Tuple[str, ...]) -> str:
    assert len(ctx) == len(values) + 1
    return ''.join(ctx[k] + values[k] for k in range(len(values))) + ctx[-1]


def goodstep(L, E, x, y, F):
    """Check the manuscript's typed SUB_d premises, including middle gaps."""
    d = len(x)
    assert d in (1, 2) and len(y) == d
    assert len(E) == len(F) == d + 1
    assert all(z for z in x + y)
    assert all(E[k] and F[k] for k in range(1, d))
    assert all(cont(a) == cont(b) for a, b in zip(x, y))
    p1, p2, p3, conclusion = (fill(E, x), fill(E, y), fill(F, x), fill(F, y))
    assert p1 in L and p2 in L and p3 in L, (p1, p2, p3)
    assert conclusion not in L, conclusion
    return dict(d=d, E=E, x=x, y=y, F=F,
                premises=(p1, p2, p3), absent=conclusion)


@dataclass(frozen=True)
class Rule:
    name: str
    head: str
    children: Tuple[str, ...]
    fixed: int
    variables: int

    @property
    def size(self):
        return 1 + len(self.children) + self.fixed + self.variables


def rules_a(n: int):
    assert n >= 2
    out = [Rule('D0/p', 'D0', (), 2, 0)]
    for i in range(1, n + 1):
        out.extend((
            Rule(f'D{i}/double', f'D{i}', (f'D{i-1}', f'D{i-1}'), 0, 2),
            Rule(f'D{i}/escape', f'D{i}', (), i + 2, 0),
        ))
    out.append(Rule('A1/base', 'A1', (), 4, 0))
    for i in range(2, n + 1):
        out.extend((
            Rule(f'A{i}/left', f'A{i}', (f'D{i-1}', f'A{i-1}'), 0, 3),
            Rule(f'A{i}/right', f'A{i}', (f'A{i-1}', f'D{i-1}'), 0, 3),
            Rule(f'A{i}/middle', f'A{i}', (f'D{i-1}', f'D{i-1}'), 0, 2),
        ))
    out.extend((
        Rule('S/pure', 'S', (f'D{n}',), 2, 1),
        Rule('S/slot', 'S', (f'A{n}',), 1, 2),
    ))
    return out


def metrics_a(n: int):
    rs = rules_a(n)
    nts = [f'D{i}' for i in range(n+1)] + [f'A{i}' for i in range(1,n+1)] + ['S']
    size = len(nts) + sum(r.size for r in rs)
    assert size == n*(n+1)//2 + 27*n + 3
    byhead = defaultdict(list)
    for r in rs:
        byhead[r.head].append(r)
    least = {}
    for h in nts:
        least[h] = min(r.fixed + sum(least[c] for c in r.children)
                       for r in byhead[h])
    # Exact shortest *successful sentence* which uses a designated rule.
    thickness_per_rule = {}
    INF = 10**90
    for target in rs:
        with_target = {}
        for h in nts:
            best = INF
            for r in byhead[h]:
                base = r.fixed + sum(least[c] for c in r.children)
                if r == target:
                    best = min(best, base)
                for c in r.children:
                    best = min(best, base - least[c] + with_target[c])
            with_target[h] = best
        assert with_target['S'] < INF, target.name
        thickness_per_rule[target.name] = with_target['S']
    return size, max(thickness_per_rule.values()), thickness_per_rule


def language_a(n: int):
    """Exact finite L(G_n) by evaluation of all (acyclic) MCFG rules."""
    assert n >= 2
    D = [{'ab'}]
    for i in range(1, n+1):
        old = D[-1]
        D.append({x+y for x in old for y in old} | {'a'*i + 'cb'})
    A = [None, {('ab', 'ab')}]
    for i in range(2, n+1):
        old, block = A[-1], D[i-1]
        A.append({(v+x,y) for (x,y) in old for v in block} |
                 {(x,y+v) for (x,y) in old for v in block} |
                 {(v,w) for v in block for w in block})
    L = {u+'ab' for u in D[n]} | {x+'c'+y for (x,y) in A[n]}
    return L, D, A


def cert_a(n: int, L):
    u = 'a'*(n-1) + 'cb'
    x = (u,)
    y = (u[1:] + u,)
    E = ('a', 'ab')
    F = ('', u+'ab')
    return goodstep(L, E, x, y, F)


def cert_a_scissors(n: int, L):
    """Universal 2-hole shortening certificate, valid for all n>=2."""
    M = 2**n
    x = ('a', 'b' + 'ab'*(M-1))
    y = ('a'*n, 'b'+'ab')
    E = ('', 'c', '')
    F = ('', 'ba', '')
    return goodstep(L, E, x, y, F)


def check_a(n: int):
    L, D, A = language_a(n)
    sz, theta, which = metrics_a(n)
    M = 2**n
    pure = {w for w in L if 'c' not in w}
    assert pure == {'ab'*(M+1)}
    assert min(len(w) for w in L if cont(w) == {'a','b'}) == 2*(M+1)
    # Complete insertion-slot coverage, at every nontrivial position.
    for h in range(1,M):
        assert ('ab'*h)+'c'+('ab'*(M-h)) in L
    # N3: exponentially many disjoint c-runs in a sentence.
    witness_runs = 'acb' * (2**(n-1)) + 'ab'
    assert witness_runs in L and witness_runs.count('c') == 2**(n-1)
    assert 'cc' not in witness_runs
    cert = cert_a(n,L)
    scissors = cert_a_scissors(n,L)
    assert len(scissors['absent']) == n+5 < 2*(M+1)
    assert theta <= (n+3)**2
    return {'n':n,'size':sz,'theta':theta,'mu_ab':2*(M+1),
            'language_size':len(L),'slot_count':M-1,
            'scissors':scissors,
            'c_runs':2**(n-1),'certificate':cert,
            'theta_worst_rules':sorted(which.items(),key=lambda kv:-kv[1])[:3]}


def in_b(w: str, n: int) -> bool:
    M = 2**n
    return bool(w) and len(set(w) - set('abc')) == 0 and w.count('a')%M == 0 and w.count('b')%M == 0


def metrics_b(n: int):
    M = 2**n
    # |V|=M^2; 3M^2 right-linear rules of size 4; 3 terminal rules of size 2.
    size = 13*M*M + 6
    # Any successful derivation with the terminal rule Q_(M-1,0)->a
    # must contain at least M a's.  Every rule has a witness of length
    # <=2M+1 by a shortest residue-prefix and residue-completing suffix.
    return size, M, 2*M+1, 2*M


def check_b(n: int):
    M=2**n
    assert in_b('a'*M+'b'*M,n)
    assert not in_b('a'*(M-1)+'b'*M,n)
    assert in_b('c',n)
    assert in_b('a'*M,n) and in_b('b'*M,n)
    sz,lo,hi,mu = metrics_b(n)
    return {'n':n, 'size':sz, 'theta_lower':lo,
            'theta_upper':hi, 'mu_ab':mu}


def scan_one_step(L, d):
    """Optional exact first-violation search over a FINITE language only."""
    occ = defaultdict(set)
    f_by_x = defaultdict(set)
    for word in sorted(L, key=lambda w:(len(w),w)):
        m=len(word)
        if d == 1:
            ranges=((i,j) for i in range(m) for j in range(i+1,m+1))
            for i,j in ranges:
                E=(word[:i],word[j:]); x=(word[i:j],)
                occ[(E,tuple(map(cont,x)))].add(x)
                f_by_x[x].add(E)
        else:
            for i in range(m):
                for j in range(i+1,m):
                    for k in range(j+1,m):
                        for t in range(k+1,m+1):
                            E=(word[:i],word[j:k],word[t:])
                            x=(word[i:j],word[k:t])
                            occ[(E,tuple(map(cont,x)))].add(x)
                            f_by_x[x].add(E)
    for (E,_),poss in sorted(occ.items(),key=lambda z:sum(map(len,z[0][0]))):
        if len(poss)<2: continue
        for x in sorted(poss):
            for y in sorted(poss):
                if x==y: continue
                for F in sorted(f_by_x[x]):
                    if fill(F,y) not in L:
                        return goodstep(L,E,x,y,F)
    return None


def main():
    arg=argparse.ArgumentParser()
    arg.add_argument('--max-n',type=int,default=4)
    arg.add_argument('--scan',action='store_true',
                     help='run one-step SUB1 and SUB2 search for candidate a, n=2')
    opts=arg.parse_args()
    for n in range(2,opts.max_n+1):
        if n>4: raise ValueError('exact finite enumeration capped at n=4; general certificate is symbolic')
        z=check_a(n)
        print('A n=%d size=%d theta=%d mu_ab=%d |L|=%d slots=%d c_runs=%d' %
              (z['n'],z['size'],z['theta'],z['mu_ab'],z['language_size'],z['slot_count'],z['c_runs']))
        c=z['certificate']
        print('   SUB1 E=%r x=%r y=%r F=%r' % (c['E'],c['x'],c['y'],c['F']))
        print('   SUB1 E[x]=%s E[y]=%s F[x]=%s F[y] (absent)=%s' %
              (*c['premises'],c['absent']))
        c=z['scissors']
        print('   SUB2 E=%r x=%r y=%r F=%r' % (c['E'],c['x'],c['y'],c['F']))
        print('   SUB2 E[x]=%s E[y]=%s F[x]=%s F[y] (absent, SHORT)=%s' %
              (*c['premises'],c['absent']))
    for n in (2,3,4):
        z=check_b(n)
        print('B n=%d size=%d theta in [%d,%d] mu_ab=%d' %
              (z['n'],z['size'],z['theta_lower'],z['theta_upper'],z['mu_ab']))
    if opts.scan:
        L,_,_=language_a(2)
        for d in (1,2):
            print('A n=2 exact SUB_%d scan:'%d,scan_one_step(L,d))

if __name__=='__main__':
    main()
