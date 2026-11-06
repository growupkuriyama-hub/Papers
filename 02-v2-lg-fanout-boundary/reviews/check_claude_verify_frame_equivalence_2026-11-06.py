"""Independent re-check of chatgpt_frame_equivalence_2026-11-06 (Claude)."""
import itertools, random
from collections import defaultdict

ok = True
def report(name, cond, extra=''):
    global ok
    ok &= bool(cond)
    print(('PASS ' if cond else 'FAIL ') + name + (('  ' + extra) if extra else ''))

def plug(ctx, parts):
    out = ctx[0]
    for p, c in zip(parts, ctx[1:]): out += p + c
    return out

def violations(L, ds=(1, 2)):
    """Exact one-step SUB_d violations of a finite language (interior nonempty)."""
    L = set(L); by_ctx = defaultdict(set); ctxs = defaultdict(set)
    for w in L:
        n = len(w)
        for i in range(n):
            for j in range(i+1, n+1):
                if 1 in ds:
                    E, x = (w[:i], w[j:]), (w[i:j],); by_ctx[E].add(x); ctxs[x].add(E)
                if 2 in ds:
                    for k in range(j+1, n):
                        for l in range(k+1, n+1):
                            E, x = (w[:i], w[j:k], w[l:]), (w[i:j], w[k:l]); by_ctx[E].add(x); ctxs[x].add(E)
    for E, xs in by_ctx.items():
        g = defaultdict(list)
        for x in xs: g[tuple(frozenset(t) for t in x)].append(x)
        for grp in g.values():
            for x in grp:
                for y in grp:
                    if x == y: continue
                    for F in ctxs[x]:
                        if plug(F, y) not in L: return (E, x, y, F, plug(F, y))
    return None

# 1. Example A3 certificate
L = {'ab' + X + 'ab' + Y + 'ab' for X in 'ac' for Y in 'ac'} | {'abbabaab'}
E, x, y, F = ('', 'a', ''), ('ab', 'abaab'), ('abaab', 'ab'), ('', 'b', '')
prem = [plug(E, x), plug(E, y), plug(F, x)]
report('A3: premises in L, conclusion absent, contents match',
       all(p in L for p in prem) and plug(F, y) not in L and all(set(a) == set(b) for a, b in zip(x, y)),
       f'{prem} -> {plug(F, y)}')

# 2. Lemma B1: L_nu substitutable (exhaustive one-step SUB1/SUB2 on finite L_nu)
random.seed(3)
types = [frozenset(s) for r in (1, 2, 3) for s in itertools.combinations('abc', r)]
bad = []
for trial in range(40):
    nu = {T: random.randint(len(T), len(T) + 3) for T in types if random.random() < 0.8}
    Lnu = {''.join(w) for T, m in nu.items() for w in itertools.product(sorted(T), repeat=m) if frozenset(w) == T}
    v = violations(Lnu)
    if v: bad.append((nu, v))
report('Lemma B1: 40 random nu, exhaustive SUB1+SUB2, no violation', not bad, str(bad[:1]))

# 3. Layer grammar: generate L(G_n) from the rules, compare with H_n; size; theta
def layer_rules(n):
    R = [('A0a', (), 'a'), ('A0b', (), 'b')]
    have = {0: {'a': 'A0a', 'b': 'A0b'}}
    for i in range(1, n+1):
        Ts = ['ab'] if i == n else ['a', 'b', 'ab']
        have[i] = {}
        for T in Ts:
            name = f'A{i}{T}'
            for U, Unm in have[i-1].items():
                for V, Vnm in have[i-1].items():
                    if set(U) | set(V) == set(T):
                        R.append((name, (Unm, Vnm), None)); have[i][T] = name
    R += [('S', (), 'a'), ('S', (), 'b'), ('S', (), 'c'), ('S', (f'A{n}ab',), None)]
    return R
for n in (1, 2, 3):
    R = layer_rules(n); M = 2**n
    lang = defaultdict(set)
    for _ in range(n + 3):
        for h, ch, t in R:
            if t is not None: lang[h].add(t)
            elif len(ch) == 1: lang[h] |= lang[ch[0]]
            else: lang[h] |= {u + v for u in lang[ch[0]] for v in lang[ch[1]]}
    H = {'a', 'b', 'c'} | {''.join(w) for w in itertools.product('ab', repeat=M) if set(w) == {'a', 'b'}}
    V = {h for h, _, _ in R}
    size = len(V) + sum(1 + len(ch) + (len(t) if t else len(ch)) for h, ch, t in R)
    # thickness via inside/outside lengths
    ins = {v: float('inf') for v in V}
    for _ in range(len(V) + 2):
        for h, ch, t in R:
            ins[h] = min(ins[h], (len(t) if t else 0) + sum(ins[c] for c in ch))
    out = {v: float('inf') for v in V}; out['S'] = 0
    for _ in range(len(V) + 2):
        for h, ch, t in R:
            for k, c in enumerate(ch):
                out[c] = min(out[c], out[h] + sum(ins[d] for j, d in enumerate(ch) if j != k))
    theta = max(out[h] + (len(t) if t else 0) + sum(ins[c] for c in ch) for h, ch, t in R)
    report(f'layer n={n}: L(G)=H_n, size=48n-21, theta=M', lang['S'] == H and size == 48*n - 21 and theta == M,
           f'size={size}, theta={theta}')

# 4. Bridge(P) circularity: for the frame (u_t,v_t) itself, |u|+|v|+|m| = N - l_t.
#    (proof-level remark; numeric illustration on candidate A n=3 is unnecessary)
print('ALL PASS' if ok else 'SOME FAIL')
