# Verification script from the Astra report LG_Quadratic_Bound_2026-10-30 (h_ab typing:
# exact typed shortest yields, rule thickness, catalogue search, buffered-block tests).
# Supports lem:lg-buffered-owners / lem:local-group-shortest; the proofs are in main.tex.
# Reproduced 2026-10-30: ALL CHECKS PASSED.
#!/usr/bin/env python3
"""Exact h_ab MCFG lengths and buffered block tests. Standard library only."""
from dataclasses import dataclass
from itertools import product, permutations
from functools import lru_cache
from fractions import Fraction
from math import inf
import hashlib
import json
import random
import sys
from pathlib import Path


def hab(w):
    if not w:
        return (0, '', '', 0)
    return (min(2, len(w)), w[0], w[-1],
            sum(w[i:i+2] == 'ab' for i in range(len(w)-1)) % 2)


HT = sorted({hab(''.join(w)) for n in range(5)
             for w in product('ab', repeat=n)})
HI = {t: i for i, t in enumerate(HT)}
EPS = HI[hab('')]


def hmul(x, y):
    if x[0] == 0:
        return y
    if y[0] == 0:
        return x
    return (min(2, x[0]+y[0]), x[1], y[2],
            x[3] ^ y[3] ^ int(x[2] == 'a' and y[1] == 'b'))


HM = [[HI[hmul(x, y)] for y in HT] for x in HT]


@dataclass(frozen=True)
class Rule:
    lhs: int
    children: tuple
    template: tuple

    @property
    def terminals(self):
        return sum(isinstance(t, str) for row in self.template for t in row)


def const(a, words):
    return Rule(a, (), tuple(tuple(w) for w in words))


@lru_cache(maxsize=None)
def output_type(template, childtypes):
    out = []
    for row in template:
        z = EPS
        for tok in row:
            q = HI[hab(tok)] if isinstance(tok, str) else childtypes[tok[0]][tok[1]]
            z = HM[z][q]
        out.append(z)
    return tuple(out)


def validate(fans, rules, start):
    assert fans[start] == 1
    for r in rules:
        assert len(r.template) == fans[r.lhs] and all(r.template)
        vs = [t for row in r.template for t in row if not isinstance(t, str)]
        expected = [(j, k) for j, b in enumerate(r.children) for k in range(fans[b])]
        assert sorted(vs) == sorted(expected)  # linear and nondeleting
        for j, b in enumerate(r.children):
            assert [k for p, k in vs if p == j] == list(range(fans[b]))
        for row in r.template:
            assert all(not (isinstance(x, tuple) and isinstance(y, tuple)
                           and y == (x[0], x[1]+1)) for x, y in zip(row, row[1:]))
    seen = {start}
    while True:
        new = seen | {b for r in rules if r.lhs in seen for b in r.children}
        if new == seen:
            break
        seen = new
    assert len(seen) == len(fans)


def typed_shortest(fans, rules):
    """Least-cost fixed point; no length/depth cutoff, cycles allowed."""
    dist = [{} for _ in fans]
    while True:
        changed = False
        for r in rules:
            tables = [list(dist[b].items()) for b in r.children]
            for cs in product(*tables):
                typ = output_type(r.template, tuple(x[0] for x in cs))
                val = r.terminals + sum(x[1] for x in cs)
                if val < dist[r.lhs].get(typ, inf):
                    dist[r.lhs][typ] = val
                    changed = True
        if not changed:
            assert all(dist)
            return dist


def thickness(fans, rules, start):
    """Inside/outside exact minimum for a distinguished occurrence of EACH rule."""
    inside = [inf] * len(fans)
    while True:
        changed = False
        for r in rules:
            v = r.terminals + sum(inside[b] for b in r.children)
            if v < inside[r.lhs]:
                inside[r.lhs] = v
                changed = True
        if not changed:
            break
    assert all(x < inf for x in inside)
    outside = [inf] * len(fans)
    outside[start] = 0
    while True:
        changed = False
        for r in rules:
            for j, b in enumerate(r.children):
                v = outside[r.lhs] + r.terminals + sum(
                    inside[c] for i, c in enumerate(r.children) if i != j)
                if v < outside[b]:
                    outside[b] = v
                    changed = True
        if not changed:
            break
    vals = [outside[r.lhs]+r.terminals+sum(inside[b] for b in r.children)
            for r in rules]
    assert all(x < inf for x in vals)
    return max([1]+vals), vals


def flag_oracle(fans, rules, start, target):
    """Independent two-state grammar: whether the selected rule has been used."""
    d = [[inf, inf] for _ in fans]
    while True:
        changed = False
        for i, r in enumerate(rules):
            for flags in product((0, 1), repeat=len(r.children)):
                flag = int(i == target or any(flags))
                v = r.terminals + sum(d[b][p] for b, p in zip(r.children, flags))
                if v < d[r.lhs][flag]:
                    d[r.lhs][flag] = v
                    changed = True
        if not changed:
            return d[start][1]


def size(fans, rules):
    return len(fans) + sum(1+len(r.children)+sum(map(len, r.template)) for r in rules)


def finite_word_oracle(fans, rules):
    """Enumerate ALL tuples of an acyclic grammar; used only for n=4 tests."""
    done={}
    while len(done)<len(fans):
        progress=False
        for a in range(len(fans)):
            rs=[r for r in rules if r.lhs==a]
            if a in done or any(b not in done for r in rs for b in r.children):
                continue
            words=set()
            for r in rs:
                for cs in product(*(done[b] for b in r.children)):
                    words.add(tuple(''.join(tok if isinstance(tok,str) else cs[tok[0]][tok[1]]
                                            for tok in row) for row in r.template))
            done[a]=words
            progress=True
        assert progress
    ans=[]
    for a in range(len(fans)):
        d={}
        for ws in done[a]:
            ty=tuple(HI[hab(w)] for w in ws)
            d[ty]=min(d.get(ty,inf),sum(map(len,ws)))
        ans.append(d)
    return ans


def stats(fans, rules, start, oracle=False):
    validate(fans, rules, start)
    ds = typed_shortest(fans, rules)
    t = max(v for d in ds for v in d.values())
    theta, per_rule = thickness(fans, rules, start)
    if oracle:
        assert per_rule == [flag_oracle(fans, rules, start, i) for i in range(len(rules))]
    return t, theta, size(fans, rules), ds


def catalogue(n, fan, base, choices):
    """n includes S; A0..A(n-2) form a DAG, all directly reachable from S."""
    m = n-1
    fans = [fan]*m+[1]
    words = [('a',), ('b',), ('ab',), ('ba',)] if fan == 1 else [
        ('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]
    rules = [const(0, words[base])]
    for i, (letter, shape) in enumerate(choices, 1):
        rules.append(const(i, (letter,)*fan))
        if fan == 1:
            templates = [(((0, 0), 'b'),),
                         (((0, 0), (1, 0)),),
                         (((0, 0), 'a', (1, 0)),)]
        else:
            templates = [(((0, 0), 'b'), ((0, 1),)),
                         (((0, 0), (1, 0)), ((0, 1), (1, 1))),
                         (((0, 0), (1, 0)), ((1, 1), (0, 1)))]
        rules.append(Rule(i, (i-1,)*(1 if shape == 0 else 2), templates[shape]))
    for i in range(m):
        template = (((0, 0),),) if fan == 1 else (((0, 0), 'a', (0, 1)),)
        rules.append(Rule(m, (i,), template))
    return fans, rules, m


def print_rules(fans, rules, start):
    def name(a):
        return 'S' if a == start else 'A'+str(a)
    for i, r in enumerate(rules):
        rows = []
        for row in r.template:
            rows.append(''.join(t if isinstance(t, str) else 'x%d_%d' % (t[0]+1,t[1]+1)
                                for t in row))
        print('  R%d: %s -> (%s)(%s)' %
              (i, name(r.lhs), ','.join(rows), ','.join(map(name,r.children))))


def enumerate_catalogues():
    results = []
    options = list(product('ab', range(3)))
    for fan in (1, 2):
        for n in (4, 5, 6):
            count = 0
            best_scaled = None
            best_plain = None
            for base in range(4):
                for choices in product(options, repeat=n-2):
                    fans, rules, start = catalogue(n, fan, base, choices)
                    t, th, sz, ds = stats(fans, rules, start, oracle=(count < 2))
                    if n==4:
                        assert ds==finite_word_oracle(fans,rules)
                    scaled, plain = Fraction(t, sz*th), Fraction(t, th)
                    entry = (base, choices, t, th, sz)
                    if best_scaled is None or scaled > best_scaled[0]:
                        best_scaled = scaled, entry
                    if best_plain is None or plain > best_plain[0]:
                        best_plain = plain, entry
                    count += 1
            assert count == 4*6**(n-2)
            print('CATALOGUE fan=%d n=%d count=%d' % (fan,n,count))
            for label, best in [('max_t/(size*theta)',best_scaled),('max_t/theta',best_plain)]:
                val, (base, choices, t, th, sz) = best
                print(' ',label,'=',str(val),'decimal=%.12f' % float(val),
                      't=%d theta=%d size=%d base=%d choices=%s' % (t,th,sz,base,choices))
                fs, rs, st = catalogue(n, fan, base, choices)
                stats(fs, rs, st, oracle=True)
                print_rules(fs,rs,st)
            results.append(dict(fan=fan,n=n,count=count,scaled=str(best_scaled[0]),
                                plain=str(best_plain[0])))
    return results


def extension_family(q,fan):
    """Parameter extension of increasing-ratio catalogue examples, not a lower-bound conjecture."""
    if fan==1:
        choices=[('a',0)]+[('a',2)]*q+[('a',1)]
        return catalogue(q+4,1,3,choices)
    choices=[('b',1)]*q+[('a',2)]
    return catalogue(q+3,2,0,choices)


def linear_family(n, fan):
    # S has Sigma+ backbone, so the target is (f,h_ab)-substitutable for all f.
    fans = [fan]*(n+1)+[1]
    start = n+1
    rules = [const(0, ('b',)*fan)]
    for i in range(1,n+1):
        rules.append(const(i, ('a',)*fan))
        template = (((0,0),'b'),) if fan == 1 else (((0,0),'b'),((0,1),))
        rules.append(Rule(i,(i-1,),template))
    for i in range(n+1):
        template = (((0,0),),) if fan == 1 else (((0,0),'a',(0,1)),)
        rules.append(Rule(start,(i,),template))
    rules += [const(start,('a',)),const(start,('b',)),
              Rule(start,(start,start),(((0,0),(1,0)),))]
    return fans,rules,start


def test_hab():
    ws = [''.join(w) for n in range(6) for w in product('ab',repeat=n)]
    for u in ws:
        for v in ws:
            assert hmul(hab(u),hab(v)) == hab(u+v)
    for a,b,c in product(range(len(HT)),repeat=3):
        assert HM[HM[a][b]][c] == HM[a][HM[b][c]]
    # Local groups: test every positive idempotent's eTe for inverses.
    pos = [i for i in range(len(HT)) if i != EPS]
    idem = [e for e in pos if HM[e][e] == e]
    for e in idem:
        loc = {HM[HM[e][x]][e] for x in pos}
        assert e in loc and all(any(HM[x][y] == e == HM[y][x] for y in loc) for x in loc)
    print('H_AB states=%d positive=%d idempotents=%d word_pairs=%d associative_triples=%d PASS' %
          (len(HT),len(pos),len(idem),len(ws)**2,len(HT)**3))
    print('H_AB state list:', HT)
    # Adjacent replacements: individual changes xor to 0; joint change is 1.
    w00,w10,w01,w11 = 'aaaa','abaa','aaba','abba'
    ps = [hab(w)[3] for w in (w00,w10,w01,w11)]
    assert ps == [0,1,1,1]
    print('ADJACENCY_COUNTEREXAMPLE words=',[w00,w10,w01,w11],'parities=',ps)
    # Distinguishes rulewise thickness from simultaneous rule usage.
    fs, rs, st = [1], [const(0,('a',)),const(0,('b',))], 0
    assert thickness(fs,rs,st)[1] == [1,1]
    print('RULEWISE_THICKNESS S->a|b: per_rule=[1,1], theta=1; no derivation uses both rules PASS')


# Noncommutative group multiplication: p*q means p composed with q.
PERMS = list(permutations(range(3)))
IDENT = (0,1,2)


def pmul(p,q):
    return tuple(p[q[i]] for i in range(3))


def prodg(values):
    out = IDENT
    for x in values:
        out = pmul(out,x)
    return out


def gamma(w,k,nu):
    if len(w) < 2*k:
        return IDENT
    return prodg(nu[w[i:i+k+1]] for i in range(len(w)-k))


def window(w,k):
    return ('short',w) if len(w)<2*k else ('long',w[:k],w[-k:])


def rewrite(w, blocks, chosen):
    parts=[]
    p=0
    for l,r,o,rep in sorted(blocks):
        parts.extend((w[p:l], rep if o in chosen else w[l:r]))
        p=r
    parts.append(w[p:])
    return ''.join(parts)


def buffer_test(seed=20261030, cases=600):
    rng = random.Random(seed)
    total_subsets=0
    short_rows=0
    nonempty_sets=0
    merges=0
    for trial in range(cases):
        k=1+trial%3
        f=1+trial%3
        d=1+rng.randrange(f)
        owners=1+rng.randrange(6)
        nu={''.join(x):rng.choice(PERMS) for x in product('ab',repeat=k+1)}
        allocated=[[] for _ in range(d)]
        for o in range(owners):
            for _ in range(1+rng.randrange(f)):
                allocated[rng.randrange(d)].append(o)
        rows=[]
        allblocks=[]
        for ids in allocated:
            rng.shuffle(ids)
            w=''.join(rng.choice('ab') for _ in range(rng.randrange(2*k+1)))
            blocks=[]
            for o in ids:
                old=''.join(rng.choice('ab') for _ in range(1+rng.randrange(5)))
                rep=''.join(rng.choice('ab') for _ in range(1+rng.randrange(4)))
                l=len(w); w+=old; r=len(w)
                blocks.append((l,r,o,rep))
                w+=''.join(rng.choice('ab') for _ in range(rng.randrange(2*k+1)))
            if not w:
                w='a'
            rows.append(w); allblocks.append(blocks)
        eligible=set(range(owners))
        for w,blocks in zip(rows,allblocks):
            short_rows += int(len(w)<2*k)
            for l,r,o,rep in blocks:
                if len(w)<2*k or l<k or r>len(w)-k:
                    eligible.discard(o)
        graph={o:set() for o in eligible}
        for blocks in allblocks:
            bs=[b for b in blocks if b[2] in eligible]
            for i,(l,r,o,rep) in enumerate(bs):
                for l2,r2,p,rep2 in bs[i+1:]:
                    if p!=o and l2-r<2*k:
                        graph[o].add(p); graph[p].add(o)
        assert all(len(v)<=4*k*f for v in graph.values())
        chosen=[]
        for o in sorted(eligible):
            if all(p not in graph[o] for p in chosen):
                chosen.append(o)
        assert len(chosen)*(4*k*f+1)>=len(eligible)
        nonempty_sets += bool(chosen)
        expanded=[]
        for w,blocks in zip(rows,allblocks):
            intervals=sorted((l-k,r+k,o) for l,r,o,rep in blocks if o in chosen)
            clusters=[]
            for l,r,o in intervals:
                if clusters and l<clusters[-1][1]:
                    assert o==clusters[-1][2]
                    a,b,p=clusters[-1]
                    clusters[-1]=(a,max(b,r),p); merges+=1
                else:
                    clusters.append((l,r,o))
            ex=[]
            for l,r,o in clusters:
                inner=[(a-l,b-l,p,rep) for a,b,p,rep in blocks
                       if p==o and l<=a and b<=r]
                old=w[l:r]; new=rewrite(old,inner,{o})
                assert window(old,k)==window(new,k) and len(new)>=2*k+1
                ex.append((l,r,o,new))
            expanded.append(ex)
        for mask in range(1<<len(chosen)):
            J={o for i,o in enumerate(chosen) if mask>>i&1}
            total_subsets+=1
            for w,blocks,ex in zip(rows,allblocks,expanded):
                actual=rewrite(w,blocks,J)
                assembled=rewrite(w,ex,J)
                assert actual==assembled
                assert window(actual,k)==window(w,k)
                if not ex:
                    assert actual==w
                    continue
                factors=[nu[w[i:i+k+1]] for i in range(len(w)-k)]
                terms=[]; p=0
                for l,r,o,new in ex:
                    terms.extend(factors[p:l])
                    terms.append(gamma(new if o in J else w[l:r],k,nu))
                    p=r-k
                terms.extend(factors[p:])
                assert prodg(terms)==gamma(actual,k,nu)
    assert pmul((1,0,2),(0,2,1)) != pmul((0,2,1),(1,0,2))
    print('BUFFER_S3 seed=%d cases=%d k=1..3 f=1..3 subsets=%d short_rows=%d nonempty_independent=%d merges=%d PASS' %
          (seed,cases,total_subsets,short_rows,nonempty_sets,merges))


def main():
    print('Python',sys.version.split()[0])
    print('Exact fixed points: no length cutoff; integer/Fraction arithmetic.')
    p=Path(__file__).resolve().parents[1]/'main.tex'
    if p.exists():
        raw=p.read_bytes()
        print('MANUSCRIPT bytes=%d git_blob=%s' %
              (len(raw),hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()))
    test_hab()
    buffer_test()
    results=enumerate_catalogues()
    print('FINITE_WORD_ORACLE all 288 n=4 catalogues: full tuple languages match typed fixed point PASS')
    print('EXTENSION_FAMILY parameter fan n_nonterminals size theta t t/theta t/(size*theta)')
    for fan in (1,2):
        for q in range(1,11):
            fs,rs,st=extension_family(q,fan)
            t,th,sz,_=stats(fs,rs,st,oracle=True)
            print(q,fan,len(fs),sz,th,t,str(Fraction(t,th)),str(Fraction(t,sz*th)))
    print('LINEAR_FAMILY n fan size theta t t/theta t/(size*theta)')
    for fan in (1,2):
        for n in range(1,11):
            fs,rs,st=linear_family(n,fan)
            t,th,sz,_=stats(fs,rs,st,oracle=True)
            if fan==1:
                assert (sz,th,t)==(10*n+16,2,max(n+1,4))
            else:
                assert (sz,th,t)==(14*n+19,4,max(n+2,4))
            print(n,fan,sz,th,t,str(Fraction(t,th)),str(Fraction(t,sz*th)))
    print('ALL CHECKS PASSED')
    print('CATALOGUE_JSON',json.dumps(results,ensure_ascii=False))


if __name__=='__main__':
    main()
