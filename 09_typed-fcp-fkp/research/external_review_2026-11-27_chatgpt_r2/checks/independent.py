#!/usr/bin/env python3
"""Independent round-2 tests, no imports from author's tools.
Finite-language identities are exhaustive only over the indicated domains.
The universal CFG claims are proved in the review, not by these tests.
"""
from itertools import product, combinations
from functools import lru_cache


def cuts(w):
    for i in range(len(w) + 1):
        yield w[:i], w[i:]


def left(L, t):
    return {p for w in L for p, q in cuts(w) if q == t}


def fill(L, p, q):
    return {w[len(p):len(w)-len(q)] for w in L
            if len(w) >= len(p)+len(q) and w.startswith(p) and w.endswith(q)}


def capture(L, r, t, t0):
    assert left(L, t) - left(L, t0) == {r}
    z = r+t
    count = 0
    for i in range(len(r)+1):
        for k in range(i, len(r)+1):
            p, x, q = z[:i], z[i:k], z[k:]
            q0 = r[k:]+t0
            assert fill(L, p, q)-fill(L, p, q0) == {x}
            count += 1
    return count


def tiny():
    words = ['']+[''.join(p) for k in (1, 2) for p in product('ab', repeat=k)]
    a = b = c = 0
    for k in range(len(words)+1):
        for subset in combinations(words, k):
            L = set(subset)
            for z in L:
                for r,t in cuts(z):
                    for t0 in words:
                        if left(L,t)-left(L,t0)=={r}:
                            a += 1
                            c += capture(L,r,t,t0)
            for w in L:
                for r,t0 in cuts(w):
                    for t in words:
                        if t!=t0 and r+t in L and left(L,t)<=left(L,t0):
                            b += 1
                            assert left(L-{w},t)-left(L-{w},t0)=={r}
    assert capture({'a'}, 'a', '', 'b') == 3  # T=epsilon boundary
    print('tiny: 128 languages, capture instances',a,'span checks',c,'one-word instances',b)


@lru_cache(None)
def shapes(h):
    if h == 0:
        return ((),)
    prev=shapes(h-1)
    return tuple((x,) for x in prev)+tuple(product(prev,repeat=2))


def encode(tree):
    if not tree:
        return 'a'
    if len(tree)==1:
        return '{'+encode(tree[0])+'}'
    return '['+''.join(map(encode,tree))+']'


def full(h):
    t=()
    for _ in range(h):
        t=(t,t)
    return t


def sites(t, path=(), pos=0):
    yield path,t,pos
    start=pos+1
    for i,child in enumerate(t):
        yield from sites(child,path+(i,),start)
        start+=len(encode(child))


def depth(word):
    # Stack validator: close a constructor only if arity and heights match.
    stack=[('root',[])]
    for a in word:
        if a=='a':
            stack[-1][1].append(0)
        elif a in '[{':
            stack.append((a,[]))
        elif a in ']}':
            if len(stack)<2:
                return None
            op,children=stack.pop()
            if (op,a) not in {('[',']'),('{','}')}:
                return None
            if len(children)!=(2 if op=='[' else 1) or len(set(children))!=1:
                return None
            stack[-1][1].append(children[0]+1)
        else:
            return None
    return stack[0][1][0] if len(stack)==1 and len(stack[0][1])==1 else None


def families():
    for n in range(2,5):
        L={encode(t) for t in shapes(n)}
        W=encode(full(n)); M=L-{W}
        last=max((p,t,o) for p,t,o in sites(full(n)) if len(p)==n-1)
        _,node,o=last
        r=W[:o]; t0=W[o:]; t='{a}'+W[o+len(encode(node)):]
        assert len(r)==3*2**n-n-5 and left(L,t)<=left(L,t0)
        count=capture(M,r,t,t0)
        assert all(depth(w)==n for w in L)
        # All typed components for the corrected ideal construction.
        for threshold in (1,2):
            if threshold==2 and n<3:
                continue
            typ=lambda w: min(threshold,w.count('{'))
            Lp={w for w in L if typ(w)==threshold}
            for i in range(n):
                E={encode(x) for x in shapes(i)}
                if threshold==2 and i==n-1:
                    p,q='[','{'*(n-1)+'a'+'}'*(n-1)+']'
                else:
                    p,q='{'*(n-i),'}'*(n-i)
                assert typ(p+q)==threshold
                assert fill(Lp,p,q)==E
                for mu in range(threshold+1):
                    assert {w for w in fill(Lp,p,q) if typ(w)==mu}=={w for w in E if typ(w)==mu}
            assert fill(Lp,'','')==Lp
        print(f'n={n}: |M|={len(M)}, |R|={len(r)}, capture spans={count}; ideal fibres OK (retained roots)')
        # For every possible marked-containing factor in every singly marked
        # test word, check all contexts rejecting its unmarked replacement.
        checked=0
        for path,node,o in sites(full(n)):
            j=n-len(path)
            if not 1<=j<n:
                continue
            wj=encode(node); v=encode((node[0],))
            z=W[:o]+v+W[o+len(wj):]
            assert z in M
            for a in range(o+1):
                for b in range(o+len(v),len(z)+1):
                    x=z[a:b]; xp=z[a:o]+wj+z[o+len(v):b]
                    for m in M:
                        pos=m.find(x)
                        while pos!=-1:
                            p,q=m[:pos],m[pos+len(x):]
                            if p+xp+q not in M:
                                assert p+xp+q==W
                                assert len(p)+len(q)==len(z)-len(x)
                                checked+=1
                            pos=m.find(x,pos+1)
        print(f'n={n}: marked-node rejecting-context occurrences={checked}')


def mixing():
    for n in range(2,7):
        W=encode(full(n)); pairs=0
        for j in range(1,n):
            parts=[]
            for path,t,o in sites(full(n)):
                if len(path)==n-j:
                    parts.append((W[:o],W[o+len(encode(t)):]))
            v=encode((full(j-1),)); wj=encode(full(j))
            assert len(parts)==2**(n-j)
            assert (len(v)%2==len(wj)%2)==(j>=2)
            for a,(p,q) in enumerate(parts):
                for b,(_,q2) in enumerate(parts):
                    assert (depth(p+v+q2)==n)==(a==b)
                    pairs+=1
            assert len({p+v+q for p,q in parts})==len(parts)
        print(f'n={n}: mixing pairs={pairs}')


def ideal_counterexample():
    # Original S->a|b, initial S, context (epsilon,epsilon), h_b.
    L={'a','b'}; Lp={'b'}; unmarked=lambda w: 'b' not in w and w!=''
    retained_rule_yield={'a'}  # (S,1)->a remains if only I changes.
    new_component={w for w in fill(Lp,'','') if unmarked(w)}
    assert not retained_rule_yield<=new_component
    assert {w for w in fill(Lp,'','') if 'b' in w}=={'b'}
    print('6.6 counterexample confirmed: excluded initial copy produces a, its relative component is empty; deleting copy repairs')
    # Non-tree example of repaired 6.9, S->AB; A->a|d; B->b|c.
    L={'ab','ac','db','dc'}; Lp=L-{'ab'}
    assert fill(Lp,'','c')=={'a','d'} and fill(Lp,'d','')=={'b','c'}
    assert capture(Lp,'a','c','b')==3
    print('6.9 flat example: ab deletion, indicator {c,d}; capture and forcing OK')



def flat_family():
    # Different mechanism: fixed-length binary payload, short prefix tags.
    # b never occurs in the tag; both b and # count as marked.
    for n in range(1,4):
        E=[{''.join(p) for p in product('ab',repeat=2**i)} for i in range(n+1)]
        tags=['#'+'a'*i+'#' for i in range(n+1)]
        L=E[-1] | {tags[i]+x for i in range(n+1) for x in E[i]}
        W='a'*(2**n); M=L-{W}
        assert {w for w in L if 'b' not in w and '#' not in w}=={W}
        for i,tag in enumerate(tags):
            assert fill(L,tag,'')==fill(M,tag,'')==E[i]
        R=W[:-1]
        assert left(L,'b')<=left(L,'a')
        spans=capture(M,R,'b','a')
        # Marked-node rejecting-context identity for all marked-containing
        # intervals, and all mixed prefix/suffix pairs in the flat payload.
        marked=0
        for i in range(len(W)):
            z=W[:i]+'b'+W[i+1:]
            for a in range(i+1):
                for b in range(i+1,len(W)+1):
                    x=z[a:b]; xp='a'*len(x)
                    for m in M:
                        pos=m.find(x)
                        while pos!=-1:
                            p,q=m[:pos],m[pos+len(x):]
                            if p+xp+q not in M:
                                assert p+xp+q==W
                                assert len(p)+len(q)==len(W)-len(x)
                                marked+=1
                            pos=m.find(x,pos+1)
            for j in range(len(W)):
                assert ('a'*i+'b'+'a'*(len(W)-1-j) in M)==(i==j)
        print(f'flat n={n}: |M|={len(M)}, |R|={len(R)}, capture spans={spans}, marked contexts={marked}, mixing pairs={len(W)**2}')


if __name__=='__main__':
    tiny(); ideal_counterexample(); families(); mixing(); flat_family(); print('ALL INDEPENDENT CHECKS OK')
