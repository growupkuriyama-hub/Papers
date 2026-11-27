"""Independent finite regression checks. Standard library, no network or file I/O.
Run with Python 3. Output is stdout. Not a proof of the general statements.
ASCII: a = leaf, [] = binary, <> = unary. Empty word = ''.
"""
from itertools import product
from functools import lru_cache


def powerset(xs):
    xs = tuple(xs)
    for mask in range(1 << len(xs)):
        yield frozenset(x for i, x in enumerate(xs) if mask >> i & 1)


def cuts(w):
    return ((w[:i], w[i:j], w[j:]) for i in range(len(w)+1)
            for j in range(i, len(w)+1))


def frame(L, c):
    p, q = c
    return {w[len(p):len(w)-len(q)] for w in L
            if len(w) >= len(p)+len(q) and w.startswith(p) and w.endswith(q)}


def ctx(L, x):
    out=set()
    for w in L:
        i=w.find(x)
        while i>=0:
            out.add((w[:i],w[i+len(x):]))
            i=w.find(x,i+1)
    return out


def capture(L, R, T, U):
    return {w[:-len(T)] if T else w for w in L if w.endswith(T)
            and (w[:-len(T)] if T else w)+U not in L} == {R}


def local_capture(L, R, T, U):
    # Every interval in R, including zero-width ones. The set of candidate
    # exemplars is the full preimage of the reaching context. Testing the
    # rejecting frame on every candidate is exhaustive over possible kernels
    # because any kernel not containing x is a subset of those candidates.
    assert R+T in L and capture(L,R,T,U)
    count = 0
    for p,x,q0 in cuts(R):
        candidates = frame(L,(p,q0+T))
        assert x in candidates
        assert {e for e in candidates if p+e+q0+U not in L} == {x}
        count += 1
    return count


def small_general():
    words = [''.join(w) for k in range(3) for w in product('ab',repeat=k)]
    cap = intervals = deletions = 0
    boundary = [0,0,0]
    for L in powerset(words):
        for z in L:
            for i in range(len(z)+1):
                R,T = z[:i],z[i:]
                for U in words:
                    if capture(L,R,T,U):
                        cap += 1
                        intervals += local_capture(L,R,T,U)
                        boundary[0] += not R
                        boundary[1] += not T
                        boundary[2] += not U
                        # Independently check the actual Galois condition for
                        # ALL feasible local kernels at every captured interval.
                        for p,x,q0 in cuts(R):
                            for K in powerset(frame(L,(p,q0+T))):
                                common = set.intersection(*(ctx(L,e) for e in K)) if K else None
                                in_closure = common is not None and common <= ctx(L,x)
                                assert not in_closure or x in K
                    if T != U and R+U in L and all(
                        (w[:-len(T)] if T else w)+U in L for w in L if w.endswith(T)):
                        deletions += 1
                        assert capture(L-{R+U},R,T,U)
    print('binary words length <=2: languages=128, capture instances=',cap,
          'intervals=',intervals,'empty R/T/U=',boundary,'one-word deletions=',deletions)


@lru_cache(None)
def level(i):
    if not i: return frozenset({'a'})
    prev = level(i-1)
    return frozenset({'<'+x+'>' for x in prev} | {'['+x+y+']' for x in prev for y in prev})


def wstar(i):
    w='a'
    for _ in range(i): w='['+w+w+']'
    return w


def paths(w, d, pre='', post=''):
    if not d:
        yield pre,w,post
    else:
        half=(len(w)-2)//2
        l,r=w[1:1+half],w[1+half:-1]
        yield from paths(l,d-1,pre+'[',r+']'+post)
        yield from paths(r,d-1,pre+'['+l,']'+post)


def yields(rules):
    # All tested grammars are DAGs; nonterminals are tuples or integers.
    @lru_cache(None)
    def go(A):
        out=set()
        for rhs in rules.get(A,()):
            out.update(''.join(xs) for xs in product(*(go(x) if x in rules else {x} for x in rhs)))
        return out
    return go


def gen_base(n):
    rules={0:[('a',)]}
    for i in range(1,n+1): rules[i]=[('[',i-1,i-1,']'),('<',i-1,'>')]
    return rules


def fn(n):
    rules=gen_base(n-1)
    root=('S',)
    def template(pi):
        t=('<',n-len(pi)-1,'>')
        for k in reversed(range(len(pi))):
            sibling=n-k-1
            t=('[',)+t+(sibling,']') if pi[k]==0 else ('[',sibling)+t+(']',)
        return t
    rules[root]=[template(pi) for d in range(n) for pi in product((0,1),repeat=d)]
    return rules,root


def refine(rules, initial, types, typ, mul, identity, ideal):
    # Product construction with all copies, then delete disallowed initial
    # copies. Represent removed references as a failure (not as terminals).
    result={(A,t):[] for A in rules for t in types}
    for A,rs in rules.items():
        for rhs in rs:
            for rr in product(*[[(x,t) for t in types] if x in rules else [x] for x in rhs]):
                t=identity
                for x in rr: t=mul(t,x[1] if isinstance(x,tuple) else typ(x))
                result[A,t].append(rr)
    removed={(A,t) for A in initial for t in types if t not in ideal}
    for A in removed: del result[A]
    assert all(x not in removed for rs in result.values() for rhs in rs for x in rhs)
    return result,{(A,t) for A in initial for t in ideal}


def verify_ideal(rules, initial, L, frames, mark, bound):
    # Fresh identity -1; positive types 0..bound with saturated addition.
    def typ(w): return min(bound,sum(c in mark for c in w)) if w else -1
    def mul(x,y): return y if x==-1 else x if y==-1 else min(bound,x+y)
    types=list(range(-1,bound+1)); I={bound}
    # Additional explicit force test (post-lock source-alignment check).
    for A,(p,q) in frames.items():
        if A not in initial:
            assert all(mul(mul(typ(p),t),typ(q)) in I for t in types)
    result,starts=refine(rules,initial,types,typ,mul,-1,I)
    go=yields(result); target={w for w in L if typ(w)==bound}
    assert set().union(*(go(A) for A in starts))==target
    # Check each strong component, including all empty copies. Each frame
    # is nonempty and has exactly one context in these constructed instances.
    den={A:frame(target,c) for A,c in frames.items()}
    base=yields(rules)
    for A,t in result:
        expected={x for x in den[A] if typ(x)==t}
        assert go((A,t))==expected=={x for x in base(A) if typ(x)==t}
    assert max(map(len,(rhs for rs in result.values() for rhs in rs))) <= max(map(len,(rhs for rs in rules.values() for rhs in rs)))
    productive={A for A in result if go(A)}
    reachable=set(starts)&productive
    while True:
        nxt=reachable|{x for A in reachable for rhs in result[A]
                       if all(x not in result or x in productive for x in rhs)
                       for x in rhs if x in result}
        if nxt==reachable: break
        reachable=nxt
    trimmed_rules=sum(all(x not in result or x in reachable for x in rhs)
                      for A in reachable for rhs in result[A])
    return len(target),len(result),len(reachable),trimmed_rules


def tree_tests():
    for n in range(1,5):
        L=level(n); W=wstar(n); M=L-{W}
        assert len(W)==3*2**n-2
        rules,S=fn(n); go=yields(rules)
        assert go(S)==M
        assert len(rules)==n+1 and sum(map(len,rules.values()))==2**n+2*n-2
        assert max(len(rhs) for rs in rules.values() for rhs in rs)==3*n
        for i in range(n):
            assert frame(M,('<'*(n-i),'>'*(n-i)))==go(i)==level(i)
        assert frame(M,('',''))==M
        base=gen_base(n); frames={i:('<'*(n-i),'>'*(n-i)) for i in base}
        mark=verify_ideal(base,{n},L,frames,{'<'},1)
        assert mark[0]==len(M) and mark[2:]==(2*n,6*n-4)
        # In balanced yields the opening-only indicator agrees with s_U,
        # but the exact morphism of main.tex counts either unary bracket.
        # Check both on the entire raw refinement, including dead copies.
        assert verify_ideal(base,{n},L,frames,{'<','>'},1)==mark
        two=None
        if n>=3:
            frames[n-1]=('[','<'*(n-1)+'a'+'>'*(n-1)+']')
            assert len(frames[n-1][0]+frames[n-1][1])==2*n+1
            assert frame(L,frames[n-1])==level(n-1)
            two=verify_ideal(base,{n},L,frames,{'<'},2)
        mix=cap=marked=0
        @lru_cache(None)
        def contexts(x): return ctx(M,x)
        def closure(e):
            cs=contexts(e)
            assert cs
            c=min(cs,key=lambda c: len(frame(M,c)))
            return {x for x in frame(M,c) if all(p+x+q in M for p,q in cs)}
        for i in range(n):
            assert closure(wstar(i))==level(i)
        for i in range(1,n+1):
            u='<'*i+'a'+'>'*i
            assert closure(u)==level(i)-{wstar(i)}
        if n>=2:
            U='[aa]'+']'*(n-1); T='<a>'+']'*(n-1); R=W[:-len(U)]
            assert W==R+U and len(R)==3*2**n-n-5
            assert all(w[:-len(T)]+U in L for w in L if w.endswith(T))
            cap=local_capture(M,R,T,U)
            assert max(map(len,M))==3*2**n-3
            for j in range(1,n):
                v='<'+wstar(j-1)+'>'
                ps=list(paths(W,n-j))
                assert len(ps)==2**(n-j) and all(x==wstar(j) for _,x,_ in ps)
                for i,(p,_,q) in enumerate(ps):
                    z=p+v+q; assert z in M
                    for k,(_,_,q2) in enumerate(ps):
                        assert (p+v+q2 in L)==(i==k); mix+=1
                    # Every containing interval, all accepting frames of that
                    # substring which reject its unmarked replacement. The
                    # rejected word must be W, so outside lengths agree.
                    for a in range(len(p)+1):
                        for b in range(len(q)+1):
                            x=p[a:]+v+q[:b]; xx=p[a:]+wstar(j)+q[:b]
                            # All accepting contexts of x, not only its
                            # reaching context in z. Rejecting contexts must
                            # give W on replacement; check lengths as well.
                            assert len(xx)-len(x)==len(wstar(j-1))
                            assert p[:a]+xx+q[b:]==W
                            rejects=[(u,t) for u,t in contexts(x) if u+xx+t not in M]
                            assert rejects
                            assert all(u+xx+t==W and len(u)+len(t)==a+len(q)-b for u,t in rejects)
                            marked+=1
        print(f'tree n={n}: |L|={len(L)}, |M|={len(M)}, capture intervals={cap}, mixing pairs={mix}, marked intervals={marked}, ideal(mark)={mark}, ideal(two)={two}')


def flat_tests():
    for n in range(5):
        B=lambda i: {''.join(w) for w in product('ab',repeat=2**i)}
        tag=lambda i:'#'+'a'*i+'#'
        W='a'*(2**n); R=W[:-1]; T='b'; U='a'
        L=B(n)|set().union(*( {tag(i)+w for w in B(i)} for i in range(n+1)))
        M=L-{W}; assert all(w[:-1]+'a' in L for w in L if w.endswith('b'))
        cap=local_capture(M,R,T,U)
        rules={0:[('a',),('b',)]}
        for i in range(1,n+1): rules[i]=[(i-1,i-1)]
        S='S'; rules[S]=[(n,)]+[tuple(tag(i))+(i,) for i in range(n+1)]
        go=yields(rules); assert go(S)==L
        frames={i:(tag(i),'') for i in range(n+1)}; frames[S]=('','')
        assert all(frame(L,c)==go(A) for A,c in frames.items())
        result=verify_ideal(rules,{S},L,frames,{'b','#'},1)
        for i,j in product(range(2**n),repeat=2):
            mixed='a'*i+'b'+'a'*(2**n-1-j)
            assert (mixed in M)==(i==j)
        print(f'flat n={n}: |L|={len(L)}, capture intervals={cap}, mixing pairs={4**n}, ideal={result}')


def ideal_edges():
    # Original, unrepaired operation (only restrict starts) is not an SPP.
    L={'a','b'}; Lp={'b'}; C=('','')
    assert frame(L,C)==L and not ({'a'} <= frame(Lp,C))
    # Strong finite example after repair: delete S,unmarked and all its rules.
    assert verify_ideal({'S':[('a',),('b',)]},{'S'},L,{'S':C},{'b'},1)[0]==1
    # Weak (not strong) SPP, using the grammar S->bAc | baaac, A->a|aa
    # with context (b,c) for A and empty pair for S. Both force marker b
    # for noninitial A, and the ideal includes all L. The oversized A survives.
    L={'bac','baac','baaac'}; rules={'S':[('b','A','c'),tuple('baaac')], 'A':[('a',),('a','a')]}
    X={'S':frame(L,('','')),'A':frame(L,('b','c'))}
    assert X['A']=={'a','aa','aaa'} and X['A']!=yields(rules)('A')
    typ=lambda w: -1 if not w else int('b' in w)
    mul=lambda x,y:y if x==-1 else x if y==-1 else max(x,y)
    result,starts=refine(rules,{'S'},[-1,0,1],typ,mul,-1,{1})
    Xr={(A,t):{w for w in X[A] if typ(w)==t} for A,t in result}
    for A,rs in result.items():
        for rhs in rs:
            assert {''.join(xs) for xs in product(*(Xr[x] if x in result else {x} for x in rhs))} <= Xr[A]
    assert set().union(*(Xr[A] for A in starts))==L
    # The no-initial-on-RHS assumption is necessary for this construction.
    # If S->a, T->bS, both starts, L={a,ba}, the deleted S,0 is needed by T,1.
    L={'a','ba'}
    assert frame(L,('b',''))=={'a'} and frame(L,('',''))==L
    try:
        refine({'S':[('a',)],'T':[('b','S')]},{'S','T'},[-1,0,1],typ,mul,-1,{1})
    except AssertionError:
        pass
    else:
        raise AssertionError('Expected reference to deleted initial copy')
    # Empty ideal intersection: no retained initial type; all retained
    # noninitial components still satisfy the required inequalities.
    result,starts=refine({'S':[('a',)]},{'S'},[-1,0,1],typ,mul,-1,set())
    assert not result and not starts
    print('ideal edge cases: old operation fails; corrected strong/weak SPP pass; initial on RHS fails as expected; empty ideal passes')
    print('source-alignment check: exact two-bracket s_U and all-type forcing assertions passed')


if __name__=='__main__':
    small_general(); tree_tests(); flat_tests(); ideal_edges(); print('ALL ASSERTIONS PASSED')
