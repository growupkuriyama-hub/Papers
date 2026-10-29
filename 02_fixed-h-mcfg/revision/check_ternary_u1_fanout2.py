#!/usr/bin/env python3
# Bounded checks accompanying revision/astra_ternary_u1_fanout2_2026-10-30.md
# (Astra report, 2026-10-30): P_{N,m} and W_{K,M,N} substitutability, K_2 two-hole
# violation, singleton certificates at length 7, doubling+c-shortcut failure.
# Re-run by Claude: exit 0, ALL_ASSERTIONS_PASSED true. Not used as a proof.
"""Standard library only; Python 3.11+. Exact finite language tests.
All comparisons use nonempty components and strictly nonempty inner gaps.
No bounded search is described as a decision procedure for infinite closure.
"""
from collections import defaultdict
from itertools import product, combinations
from functools import lru_cache
import json, hashlib, sys

def typ(x, marked='c'):
    return tuple(int(any(z in marked for z in u)) for u in x)

def occurrences(w, d):
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if d == 1:
                yield (w[i:j],), (w[:i], w[j:])
            else:
                for k in range(j + 1, n):
                    for l in range(k + 1, n + 1):
                        yield (w[i:j], w[k:l]), (w[:i], w[j:k], w[l:])

def fill(E, x):
    return ''.join(a + b for a, b in zip(E, x)) + E[-1]

def distribution(L, x):
    out = set()
    for w in L:
        i = w.find(x[0])
        while i >= 0:
            j = i + len(x[0])
            if len(x) == 1:
                out.add((w[:i], w[j:]))
            else:
                k = w.find(x[1], j + 1)
                while k >= 0:
                    out.add((w[:i], w[j:k], w[k + len(x[1]):]))
                    k = w.find(x[1], k + 1)
            i = w.find(x[0], i + 1)
    return frozenset(out)

def check(L, ds=(1, 2), marked='c'):
    L = frozenset(L)
    for d in ds:
        seen, cache = {}, {}
        for w in sorted(L, key=lambda w: (len(w), w)):
            for x, E in occurrences(w, d):
                key = (E, typ(x, marked))
                if key not in seen:
                    seen[key] = x
                    continue
                y = seen[key]
                if x == y:
                    continue
                for z in (x, y):
                    if z not in cache:
                        cache[z] = distribution(L, z)
                if cache[x] != cache[y]:
                    F = min(cache[x] ^ cache[y])
                    return dict(d=d, x=x, y=y, E=E, F=F,
                                Ex=fill(E, x), Ey=fill(E, y),
                                Fx=fill(F, x), Fy=fill(F, y))
    return None

def validate_certificate(L, cert, marked='c'):
    x, y, E, F = (cert[k] for k in ('x', 'y', 'E', 'F'))
    assert all(x) and all(y)
    assert len(x) == len(y) in (1, 2)
    assert len(E) == len(F) == len(x) + 1
    if len(x) == 2:
        assert E[1] and F[1]
    assert typ(x, marked) == typ(y, marked)
    assert fill(E, x) in L and fill(E, y) in L
    assert (fill(F, x) in L) != (fill(F, y) in L)

def closure(L, max_length=12, max_words=120, rounds=8, marked='c'):
    """Sound forward inference. Returns CLOSED only after a complete sweep.
    Limits stop additions, never certify a truncated fixed point as CLOSED.
    """
    L = set(L)
    trace = []
    for it in range(rounds):
        pending = {}
        for d in (1, 2):
            D, groups = defaultdict(set), defaultdict(set)
            for w in sorted(L):
                for x, E in occurrences(w, d):
                    D[x].add(E)
                    groups[E, typ(x, marked)].add(x)
            for (E, _), xs in sorted(groups.items()):
                xs = sorted(xs)
                x = xs[0]
                for y in xs[1:]:
                    for u, v in ((x, y), (y, x)):
                        for F in sorted(D[u] - D[v]):
                            z = fill(F, v)
                            if z not in L and z not in pending:
                                pending[z] = dict(round=it+1, x=u, y=v, E=E, F=F,
                                                  premises=[fill(E,u),fill(E,v),fill(F,u)],
                                                  added=z)
        if not pending:
            assert check(L, marked=marked) is None
            return L, 'CLOSED', trace
        ordered = sorted(pending, key=lambda w:(len(w),w))
        hit = False
        for z in ordered:
            if len(z) > max_length or len(L) >= max_words:
                hit = True
                continue
            item = pending[z]
            assert all(w in L for w in item['premises'])
            assert typ(item['x'],marked) == typ(item['y'],marked)
            L.add(z)
            trace.append(item)
        if hit:
            return L, 'TRUNCATED: length/word limit', trace
    return L, 'TRUNCATED: round limit', trace

def parikh_saturated(L):
    counts = defaultdict(int)
    for w in L:
        counts[tuple(w.count(a) for a in 'abc')] += 1
    import math
    for v, k in counts.items():
        m = math.factorial(sum(v))
        for q in v:
            m //= math.factorial(q)
        if m != k:
            return False
    return True

# CFG representation: integer nonterminals, string terminal blocks.
# All examples are acyclic, reduced, fan-out one, rank <= 2.
def grammar_stats(rules, start, substitutable):
    V = sorted({a for a,_ in rules})
    byhead = {a: [] for a in V}
    for a,rhs in rules:
        byhead[a].append(rhs)
    @lru_cache(None)
    def words(a):
        ans = set()
        for rhs in byhead[a]:
            factors = [words(z) if isinstance(z,int) else (z,) for z in rhs]
            ans.update(''.join(z) for z in product(*factors))
        return frozenset(ans)
    L = words(start)
    shortest = {a:min(words(a),key=lambda w:(len(w),w)) for a in V}
    outside = {start: ('','')}
    changed = True
    while changed:
        changed = False
        for a,rhs in rules:
            if a not in outside:
                continue
            p,q = outside[a]
            for i,b in enumerate(rhs):
                if not isinstance(b,int):
                    continue
                left = ''.join(shortest[z] if isinstance(z,int) else z for z in rhs[:i])
                right = ''.join(shortest[z] if isinstance(z,int) else z for z in rhs[i+1:])
                E = (p+left,right+q)
                key = lambda e:(sum(map(len,e)),e)
                if b not in outside or key(E) < key(outside[b]):
                    outside[b] = E
                    changed = True
    assert set(outside) == set(V)
    rule_minima = []
    size = len(V)
    for a,rhs in rules:
        rank = sum(isinstance(z,int) for z in rhs)
        assert rank <= 2
        term = sum(len(z) for z in rhs if isinstance(z,str))
        size += 1 + 2*rank + term
        rule_minima.append(sum(map(len,outside[a])) + term +
                           sum(len(shortest[z]) for z in rhs if isinstance(z,int)))
    mu = max(min(len(w) for w in L if typ((w,)) == (t,))
             for t in {typ((w,))[0] for w in L})
    tau = None
    if substitutable:
        vals = []
        for a in V:
            p,q = outside[a]
            for t in {typ((w,))[0] for w in words(a)}:
                eligible = []
                for w in L:
                    if len(w) <= len(p)+len(q) or not w.startswith(p) or not w.endswith(q):
                        continue
                    u = w[len(p):len(w)-len(q) if q else len(w)]
                    if typ((u,)) == (t,):
                        eligible.append(len(u))
                assert eligible
                vals.append(min(eligible))
        tau = max(vals)
    return L, dict(size=size, theta=max(rule_minima), mu_star=mu, tau=tau,
                   rule_minima=rule_minima, words=len(L), maxlen=max(map(len,L)))

def periodic_grammar(n):
    # P_i=2*i; C_i=2*i+1; S=2*n+2
    rules = [(0,('ab',)), (1,('c',))]
    for i in range(1,n+1):
        rules += [(2*i,(2*i-2,2*i-2)),
                  (2*i+1,(2*i-1,2*i-2)), (2*i+1,(2*i-2,2*i-1))]
    S = 2*n+2
    rules += [(S,(2*n,)), (S,(2*n+1,))]
    return rules,S

def shortcut_grammar(n):
    rules = [(0,('ab',))]
    for i in range(1,n+1):
        rules += [(i,(i-1,i-1)),(i,('c',))]
    return rules,n

def K(n):
    L={'a'}
    for _ in range(n):
        L = {'b'+x+y+'b' for x in L for y in L} | {'c'+x+'c' for x in L}
    return L

def out(tag, data):
    print(tag, json.dumps(data,sort_keys=True,ensure_ascii=False),flush=True)

def main():
    out('ENV',dict(python=sys.version.split()[0],alphabet='abc',f=2,rank_cap=2))
    L=K(2)
    assert check(L,(1,)) is None
    cert=check(L,(2,)); assert cert;validate_certificate(L,cert)
    out('K2',dict(language=sorted(L),d1=True,d2=False,certificate=cert))
    x,y,E=('bcac','cb'),('c','cc'),('','ca','')
    Dx,Dy=distribution(L,x),distribution(L,y)
    assert E in Dx&Dy and Dx!=Dy
    F=min(Dx^Dy)
    out('K2_USER_WITNESS',dict(x=x,y=y,E=E,F=F,Fx=fill(F,x),Fy=fill(F,y)))
    fs8={'a'*8}|{'a'*i+'bc'+'a'*(6-i) for i in range(7)}
    assert check(fs8,marked='bc') is None
    out('FS8',dict(language=sorted(fs8),marked='bc',d1_d2=True))
    C={'aaa','abaa'}
    assert check(C,marked='b') is None
    out('FS_C_COUNTEREXAMPLE',dict(language=sorted(C),marked='b',d1_d2=True))
    out('SINGLETON_LENGTH7_BEGIN',{})
    passes=[];fails=[]
    for p in product('ab',repeat=7):
        w=''.join(p);cert=check({w})
        predicted=len(set(w[1:-1]))==1 or all(w[i]!=w[i+1] for i in range(6))
        assert (cert is None)==predicted
        if cert is None:passes.append(w)
        else:
            validate_certificate({w},cert)
            fails.append((w,cert))
            out('SINGLETON_FAIL',dict(w=w,certificate=cert))
    out('SINGLETON_LENGTH7_END',dict(passed=passes,failed=len(fails)))
    for N in range(1,5):
        for m in range(1,5):
            L={'ab'*N}|{'ab'*i+'c'+'ab'*(m-i) for i in range(m+1)}
            assert check(L) is None
            out('PERIODIC_GRID',dict(N=N,m=m,words=len(L),d1_d2=True,
                                     parikh_saturated=parikh_saturated(L)))
    weighted_cases=0
    for K0 in range(1,5):
        for M in range(1,4):
            for N in range(M,M+4):
                L={'ab'*K0}
                for q in range(1,N//M+1):
                    p=N-M*q
                    for pos in combinations(range(p+q),q):
                        pos=set(pos)
                        L.add(''.join('c' if i in pos else 'ab' for i in range(p+q)))
                assert check(L) is None
                weighted_cases+=1
    out('WEIGHTED_PHASE_FAMILY',dict(cases=weighted_cases,K='1..4',M='1..3',N='M..M+3',all_pass=True))
    for n in range(1,5):
        r,S=periodic_grammar(n)
        L,stats=grammar_stats(r,S,True)
        assert check(L) is None
        assert stats['size']==17*n+14 and stats['theta']==2**(n+1)
        assert stats['tau']==stats['mu_star']==2**(n+1)
        out('PERIODIC_GRAMMAR',dict(n=n,**stats,d1_d2=True))
    for n in range(1,5):
        r,S=shortcut_grammar(n)
        L,stats=grammar_stats(r,S,False)
        cert=check(L)
        if cert:validate_certificate(L,cert)
        else:L,stats=grammar_stats(r,S,True)
        assert stats['size']==8*n+4 and stats['theta']==n+3
        assert stats['mu_star']==2**(n+1)
        out('SHORTCUT_GRAMMAR',dict(n=n,**stats,d1_d2=cert is None,certificate=cert))
    # Exhaustive pairs: pure words length 3..5, exactly-one-c words length 3..5.
    pure=[''.join(z) for n in range(3,6) for z in product('ab',repeat=n)]
    marked=[''.join(z) for n in range(3,6) for z in product('abc',repeat=n) if z.count('c')==1]
    counts=[0,0]; maxratio=(-1,None); histogram=defaultdict(int)
    for u in pure:
        for v in marked:
            cert=check({u,v})
            counts[cert is None]+=1
            if cert is None:
                histogram[len(u),len(v)]+=1
                ratio=max(len(u),len(v))/min(len(u),len(v))
                if ratio>maxratio[0]:maxratio=(ratio,(u,v))
    out('EXHAUSTIVE_PAIRS',dict(pure_count=len(pure),marked_count=len(marked),
        total=len(pure)*len(marked),fail=counts[0],pass_count=counts[1],
        max_length_ratio=maxratio,histogram={str(k):v for k,v in sorted(histogram.items())}))
    # Every subset of size <=3 of all words of length 1 or 2 over abc.
    pool=[''.join(z) for n in (1,2) for z in product('abc',repeat=n)]
    hist={}
    for k in (1,2,3):
        good=bad=noncomm=0
        for S in combinations(pool,k):
            L=set(S)
            if check(L) is None:
                good+=1
                noncomm+=not parikh_saturated(L)
            else:bad+=1
        hist[k]=dict(passed=good,failed=bad,passed_nonparikh=noncomm)
    out('EXHAUSTIVE_SMALL_SUBSETS',dict(pool=pool,by_size=hist))
    r,S=shortcut_grammar(2)
    L,_=grammar_stats(r,S,False)
    closed,status,trace=closure(L,max_length=10,max_words=80,rounds=6)
    for item in trace:out('FORCED',item)
    out('CLOSURE_RESULT',dict(seed=sorted(L),status=status,words=len(closed),steps=len(trace),
        shortest_pure=min((w for w in closed if 'c' not in w),key=lambda w:(len(w),w)),
        pure_lengths=sorted({len(w) for w in closed if 'c' not in w}),
        parikh_saturated=parikh_saturated(closed)))
    out('ALL_ASSERTIONS_PASSED',True)

if __name__=='__main__':main()
