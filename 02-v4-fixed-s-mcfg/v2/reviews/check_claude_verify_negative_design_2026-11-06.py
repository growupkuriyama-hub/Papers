"""Independent re-check of chatgpt_negative_design_2026-11-06 (Claude).
Own implementations: language of candidate (a) by its own generator, membership of
D_n-words by a recursive parser (no enumeration, large n), thickness by an
inside-outside computation (different algorithm from the report's)."""
from functools import lru_cache

ok = True
def report(name, cond, extra=''):
    global ok
    ok &= bool(cond)
    print(('PASS ' if cond else 'FAIL ') + name + (('  ' + extra) if extra else ''))

def cont(s): return set(s)
def plug(ctx, parts):
    out = ctx[0]
    for p, c in zip(parts, ctx[1:]): out += p + c
    return out
def check_step(isin, E, x, y, F):
    assert len(x) in (1, 2) and len(E) == len(F) == len(x) + 1
    assert all(a and b and cont(a) == cont(b) for a, b in zip(x, y))
    if len(x) == 2: assert E[1] and F[1]
    for w in (plug(E, x), plug(E, y), plug(F, x)): assert isin(w), w
    return plug(F, y)

# ---- candidate (a): own generator ----
def gen_a(n):
    D = {0: {'ab'}}
    for i in range(1, n + 1):
        D[i] = {u + v for u in D[i-1] for v in D[i-1]} | {'a'*i + 'cb'}
    A = {1: {('ab', 'ab')}}
    for i in range(2, n + 1):
        A[i] = ({(d + x, y) for (x, y) in A[i-1] for d in D[i-1]}
                | {(x, y + d) for (x, y) in A[i-1] for d in D[i-1]}
                | {(d1, d2) for d1 in D[i-1] for d2 in D[i-1]})
    return {w + 'ab' for w in D[n]} | {x + 'c' + y for (x, y) in A[n]}

def D_member(n):
    @lru_cache(None)
    def m(i, w):
        if i == 0: return w == 'ab'
        if w == 'a'*i + 'cb': return True
        return any(m(i-1, w[:t]) and m(i-1, w[t:]) for t in range(1, len(w)))
    return m

# 1. mu_ab, pure words, slots (exact, n=2..4)
for n in (2, 3, 4):
    L = gen_a(n); M = 2**n
    pure = {w for w in L if 'c' not in w}
    slots = all(('ab'*h) + 'c' + ('ab'*(M-h)) in L for h in range(1, M))
    report(f'(a) n={n}: pure words = {{(ab)^(M+1)}}, all slots present', pure == {'ab'*(M+1)} and slots, f'|L|={len(L)}')

# 2. scissors certificate (Thm A3) for n=2..12 via parser, absence via c-free uniqueness
for n in range(2, 13):
    M = 2**n; m = D_member(n)
    isin = lambda w: w.endswith('ab') and m(n, w[:-2])  # S -> D_n ab part suffices for premises
    z = check_step(isin, ('', 'c', ''), ('a', 'b' + 'ab'*(M-1)), ('a'*n, 'bab'), ('', 'ba', ''))
    assert z == 'a'*n + 'babab' and len(z) == n + 5 and 'c' not in z and z != 'ab'*(M+1)
report('(a) Thm A3 scissors certificate n=2..12 (premises by parser; F[y] c-free and != (ab)^(M+1))', True)

# 3. SUB1 certificate absence, exact for n=2..4
for n in (2, 3, 4):
    L = gen_a(n); u = 'a'*(n-1) + 'cb'
    z = check_step(lambda w: w in L, ('a', 'ab'), (u,), (u[1:] + u,), ('', u + 'ab'))
    report(f'(a) n={n}: SUB1 certificate, F[y] absent', z not in L, z)

# 4. size and thickness by inside-outside (own computation)
def grammar_a(n):
    R = [('D0', (), 2, 2)]  # (head, children, terminals, template length)
    for i in range(1, n+1):
        R += [(f'D{i}', (f'D{i-1}', f'D{i-1}'), 0, 2), (f'D{i}', (), i+2, i+2)]
    R += [('A1', (), 4, 4)]
    for i in range(2, n+1):
        R += [(f'A{i}', (f'D{i-1}', f'A{i-1}'), 0, 3), (f'A{i}', (f'A{i-1}', f'D{i-1}'), 0, 3),
              (f'A{i}', (f'D{i-1}', f'D{i-1}'), 0, 2)]
    R += [('S', (f'D{n}',), 2, 3), ('S', (f'A{n}',), 1, 3)]
    return R
for n in range(2, 9):
    R = grammar_a(n)
    V = {r[0] for r in R}
    size = len(V) + sum(1 + len(ch) + tl for (_, ch, _, tl) in R)
    inside = {v: float('inf') for v in V}
    for _ in range(len(V) + 2):
        for h, ch, t, _ in R:
            inside[h] = min(inside[h], t + sum(inside[c] for c in ch))
    outside = {v: float('inf') for v in V}; outside['S'] = 0
    for _ in range(len(V) + 2):
        for h, ch, t, _ in R:
            for k, c in enumerate(ch):
                rest = t + sum(inside[d] for j, d in enumerate(ch) if j != k)
                outside[c] = min(outside[c], outside[h] + rest)
    theta = max(outside[h] + t + sum(inside[c] for c in ch) for h, ch, t, _ in R)
    good = size == n*(n+1)//2 + 27*n + 3 and theta <= (n+3)**2
    report(f'(a) n={n}: size={size}, theta={theta} <= (n+3)^2={(n+3)**2}', good)

# 5. candidate (b): closure spot check (random) and mu_ab
import random
random.seed(0)
for n in (1, 2, 3):
    M = 2**n
    inb = lambda w: w and w.count('a') % M == 0 and w.count('b') % M == 0
    words = [w for w in (''.join(random.choice('abc') for _ in range(random.randint(1, 3*M))) for _ in range(4000)) if inb(w)]
    words = list(set(words))[:60]
    viol = 0
    for w1 in words:
        for i in range(len(w1)):
            for j in range(i+1, len(w1)+1):
                for w2 in words:
                    for k in range(len(w2)):
                        for l in range(k+1, len(w2)+1):
                            x, y = w1[i:j], w2[k:l]
                            if set(x) != set(y): continue
                            E1 = (w1[:i], w1[j:]);
                            if inb(plug(E1, (y,))) and not inb(plug((w2[:k], w2[l:]), (x,))):
                                viol += 1
    mu = min(len(w) for w in (('a'*p + 'b'*q) for p in range(1, 3*M) for q in range(1, 3*M)) if inb(w))
    report(f'(b) n={n}: SUB1 spot check no violation, mu_ab=2M', viol == 0 and mu == 2*M, f'{len(words)} words')

print('ALL PASS' if ok else 'SOME FAIL')
