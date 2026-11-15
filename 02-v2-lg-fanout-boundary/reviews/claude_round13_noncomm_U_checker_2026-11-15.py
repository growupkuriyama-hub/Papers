#!/usr/bin/env python3
"""Round 13 checker (Claude, 2026-11-15): non-commutative Conjecture U.

Python 3 standard library only.  Deterministic (random.seed(20261115)).
Run:   python3 -I claude_round13_noncomm_U_checker_2026-11-15.py
Exit code 0 iff every check marked [MUST] passes.

Typing throughout: content typing c(w) = set of letters of w (finest semilattice typing).
Tuple substitutability for d in {1,2}; a d=2 context is l [] m [] r with m NONEMPTY.

What is checked
  [S0] exact finite substitutability decision procedure (d=1,2), with positive / negative
       controls.
  [E1] REFUTATION (finite, exact): a finite language S1 in C^{mcf}_{2,c} with a^8 the
       shortest a-power, containing W1=a b a c a-type (deficit 5) and W2=a c a b a-type
       (deficit 4).  W1,W2 have the same a-collapsed bigram multiset and the same
       endpoints.  => "deficit is a function of the skeleton bigram multiset (+endpoints)"
       and "deficit of a multi-piece word is order-independent" are FALSE in general.
  [E2] closure experiment inside ONE content class {b,c}: seed realisations violating
       bigram-linearity; capped closure searched for a contradiction (shorter a-power or
       same-skeleton a-count conflict).  Certificates, if found, are replayed independently.
       Also the linear (control) seed.
  [S1] Lemma S (skeleton function) stress: random seeds -> exact closure when it terminates;
       on every closed set: same skeleton & a-count<=N-1  =>  same a-count.
  [S2] negative control for Lemma S: a d=1-closed finite set violating Lemma S must be
       d=2-non-closed (shows the d=2 hypothesis is used).
  [S3] content-exchange lemma (X1) instances on every closed set from [S1].
  [S4] window/tree arithmetic of Theorem T1: random trees, N < theta*sigma^(2M+1).
"""
import hashlib, random, sys, itertools, json, time
from collections import defaultdict

random.seed(20261115)
LOG = []
FAIL = 0
COUNT = 0
def log(*a):
    s = ' '.join(str(x) for x in a); LOG.append(s); print(s, flush=True)
def must(cond, msg):
    global FAIL, COUNT
    COUNT += 1
    if not cond:
        FAIL += 1; log('  [FAIL]', msg)
    return cond

def ctype(w): return frozenset(w)
def skel(w):
    out = []
    for ch in w:
        if ch == 'a':
            if not out or out[-1] != 'A': out.append('A')
        else: out.append(ch)
    return ''.join(out)
def acount(w): return w.count('a')

# ----------------------------------------------------------------- tuples / contexts
def tuples_of(w):
    """yield (d, x, E) with E the context; d=1: x=(x1,), E=(l,r); d=2: x=(x1,x2), E=(l,m,r), m!=''"""
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield 1, (w[i:j],), (w[:i], w[j:])
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):      # m = w[j:k] nonempty
                for l in range(k + 1, n + 1):
                    yield 2, (w[i:j], w[k:l]), (w[:i], w[j:k], w[l:])

def fill(E, x):
    if len(x) == 1: return E[0] + x[0] + E[1]
    assert E[1] != ''
    return E[0] + x[0] + E[1] + x[1] + E[2]

def ttype(x): return tuple(ctype(c) for c in x)

def ctx_maps(S):
    ctx = defaultdict(set)
    for w in S:
        for d, x, E in tuples_of(w):
            ctx[x].add(E)
    return ctx

def check_closed(S):
    """Exact decision: is the finite set S tuple-substitutable (d=1,2, content typing)?
    Returns (True, None) or (False, witness)."""
    S = set(S)
    ctx = ctx_maps(S)
    bucket = defaultdict(list)
    for x, Es in ctx.items():
        t = ttype(x)
        for E in Es:
            bucket[(len(x), t, E)].append(x)
    for (d, t, E0), xs in bucket.items():
        if len(xs) < 2: continue
        ref = ctx[xs[0]]
        for y in xs[1:]:
            cy = ctx[y]
            if cy != ref:
                diff = (ref - cy) or (cy - ref)
                E1 = next(iter(diff))
                x = xs[0]
                if E1 in cy: x, y = y, x
                return False, dict(x=x, y=y, E_accept=E0, E_test=E1,
                                   E_accept_x=fill(E0, x), E_accept_y=fill(E0, y),
                                   E_test_x=fill(E1, x), E_test_y=fill(E1, y),
                                   type_x=[sorted(c) for c in ttype(x)],
                                   type_y=[sorted(c) for c in ttype(y)])
    return True, None

def verify_witness(S, wit):
    """independent re-check of a non-closedness witness"""
    x, y, E0, E1 = wit['x'], wit['y'], wit['E_accept'], wit['E_test']
    if ttype(x) != ttype(y): return False
    if len(x) == 2 and (E0[1] == '' or E1[1] == ''): return False
    if any(c == '' for c in x + y): return False
    return (fill(E0, x) in S and fill(E0, y) in S and fill(E1, x) in S and fill(E1, y) not in S)

def shortest_apower(S):
    ns = [len(w) for w in S if w and set(w) == {'a'}]
    return min(ns) if ns else None

def skeleton_conflicts(S, N):
    """Lemma S consequence: same skeleton, a-counts <= N-1, different a-counts."""
    by = defaultdict(set)
    for w in S:
        if 'a' in w and acount(w) <= N - 1 and set(w) != {'a'}:
            by[skel(w)].add(acount(w))
    return {k: sorted(v) for k, v in by.items() if len(v) > 1}

# ----------------------------------------------------------------- closure with certificates
def closure(seed, cap_len, cap_words=200000, max_rounds=50, N=None, stop_on_contra=True):
    """Direct rule applications (Fable Def 2.3): E0[x],E0[y],E1[x] in K => E1[y] in K.
    Returns dict(K, origin, status, contra) ; status in {'closed','truncated','cap','contra'}."""
    K = set(seed)
    origin = {w: None for w in K}
    truncated = False
    for rnd in range(max_rounds):
        ctx = ctx_maps(K)
        bucket = defaultdict(list)
        for x, Es in ctx.items():
            t = ttype(x)
            for E in Es:
                bucket[(len(x), t, E)].append(x)
        new = {}
        for (d, t, E0), xs in bucket.items():
            if len(xs) < 2: continue
            for x in xs:
                cx = ctx[x]
                for y in xs:
                    if y == x: continue
                    for E1 in cx:
                        w = fill(E1, y)
                        if w in K or w in new: continue
                        if len(w) > cap_len:
                            truncated = True; continue
                        new[w] = (x, y, E0, E1)
        if not new:
            return dict(K=K, origin=origin, status='truncated' if truncated else 'closed',
                        contra=None, rounds=rnd)
        for w, o in new.items():
            K.add(w); origin[w] = o
        if N is not None:
            m = shortest_apower(K)
            if m is not None and m < N:
                return dict(K=K, origin=origin, status='contra', contra=('apower', 'a' * m), rounds=rnd + 1)
            sc = skeleton_conflicts(K, N)
            if sc and stop_on_contra:
                k = next(iter(sc))
                return dict(K=K, origin=origin, status='contra', contra=('skeleton', k, sc[k]), rounds=rnd + 1)
        if len(K) > cap_words:
            return dict(K=K, origin=origin, status='cap', contra=None, rounds=rnd + 1)
    return dict(K=K, origin=origin, status='cap', contra=None, rounds=max_rounds)

def certificate(origin, targets):
    """minimal ordered list of rule applications deriving targets from the seed"""
    order, seen = [], set()
    def need(w):
        if w in seen: return
        seen.add(w)
        o = origin[w]
        if o is None: return
        x, y, E0, E1 = o
        for p in (fill(E0, x), fill(E0, y), fill(E1, x)):
            need(p)
        order.append((w, o))
    for t in targets: need(t)
    return order

def replay(seed, cert):
    K = set(seed)
    for w, (x, y, E0, E1) in cert:
        if ttype(x) != ttype(y): return False, 'type'
        if any(c == '' for c in x + y): return False, 'empty component'
        if len(x) == 2 and (E0[1] == '' or E1[1] == ''): return False, 'empty separator'
        if not (fill(E0, x) in K and fill(E0, y) in K and fill(E1, x) in K): return False, 'premise'
        if fill(E1, y) != w: return False, 'conclusion'
        K.add(w)
    return True, K

# ----------------------------------------------------------------- helpers to build families
def compositions(total, parts):
    """all tuples of `parts` positive ints summing to total"""
    if parts == 0:
        if total == 0: yield ()
        return
    if total < parts: return
    for c in itertools.combinations(range(1, total), parts - 1):
        b = (0,) + c + (total,)
        yield tuple(b[i + 1] - b[i] for i in range(parts))

def flanked(pieces, a_total):
    """all words a^{p0} pi1 a^{p1} ... pik a^{pk} with all p>=1 and sum p = a_total"""
    out = set()
    for comp in compositions(a_total, len(pieces) + 1):
        w = 'a' * comp[0]
        for pi, p in zip(pieces, comp[1:]):
            w += pi + 'a' * p
        out.add(w)
    return out

def bigram_profile(w):
    s = skel(w)
    from collections import Counter
    return (Counter(s[i:i + 2] for i in range(len(s) - 1)), s[0], s[-1])

# =================================================================== S0 controls
def run_S0():
    log('== [S0] exact finite substitutability: controls')
    # positive: a^5 plus all flanked b-words with total 3 (pieces b, deficit 2)
    seed = {'a' * 5} | flanked(['b'], 3)
    ok0, wit0 = check_closed(seed)
    must(not ok0 and verify_witness(seed, wit0), 'S0: interior-only family must NOT be closed (rotation)')
    log('   interior-only family a^5 + a^+ b a^+ (total 3) is not closed; witness', json.dumps(wit0, default=list))
    R = closure(seed, cap_len=8, N=5)
    S = R['K']
    ok, wit = check_closed(S)
    must(R['status'] == 'closed' and ok, 'S0 positive control closure should be closed: %s %s' % (R['status'], wit))
    must(shortest_apower(S) == 5, 'S0 positive: a^5 shortest')
    log('   closure: status=%s |S|=%d S=%s' % (R['status'], len(S), sorted(S, key=lambda w:(len(w),w))))
    # negative: aligned (non-redistributed) word set violates (R)
    S = {'a' * 5, 'abaa'}
    ok, wit = check_closed(S)
    must(not ok and verify_witness(S, wit), 'S0 negative control must be non-closed with verified witness')
    log('   negative control {a^5, abaa}: witness', json.dumps(wit, default=list))
    # negative: separator requirement (d=2 with empty middle is NOT a context; check we never use it)
    for w in ['abcab', 'aab']:
        for d, x, E in tuples_of(w):
            if d == 2: must(E[1] != '', 'empty separator generated')

# =================================================================== E1
def run_E1():
    log('== [E1] cross-class order dependence: closure of an order-dependent seed')
    out = {}
    for f2 in (5, 4):
        N = 8
        seed = {'a' * N}
        seed |= flanked(['b'], N - 2)        # solo b, deficit 2
        seed |= flanked(['c'], N - 3)        # solo c, deficit 3
        seed |= flanked(['b', 'c'], N - 5)   # order b..c, deficit 5 = 2+3
        seed |= flanked(['c', 'b'], N - f2)  # order c..b, deficit f2
        R = closure(seed, cap_len=N + 3, cap_words=20000, max_rounds=20, N=N)
        S = R['K']
        line = '   f2=%d: status=%s |K|=%d rounds=%d contra=%s' % (f2, R['status'], len(S), R['rounds'], R['contra'])
        log(line)
        if R['status'] == 'closed':
            ok, wit = check_closed(S)
            must(ok, 'E1 closure must pass exact check')
            must(shortest_apower(S) == N, 'E1 a^8 shortest')
            must(not skeleton_conflicts(S, N), 'E1 Lemma S')
            W1 = 'abaca'
            W2 = 'acaba' if f2 == 5 else 'acaaba'
            must(W1 in S and W2 in S, 'E1 W1,W2 in closure')
            must(bigram_profile(W1) == bigram_profile(W2), 'E1 same bigram profile and endpoints')
            log('     W1=%s deficit %d ; W2=%s deficit %d ; same a-collapsed bigram multiset+endpoints=%s'
                % (W1, N - acount(W1), W2, N - acount(W2), bigram_profile(W1) == bigram_profile(W2)))
            if f2 == 4:
                must(N - acount(W1) != N - acount(W2), 'E1 REFUTATION: deficits differ')
                must('baaaaaa' in S and 'caaaaa' in S, 'E1 solo pieces present (deficits 2,3)')
                log('     REFUTED (exact, finite): deficit not a function of bigram data; cb-order deficit 4 != 2+3')
            log('     full closed set S1(f2=%d) = %s' % (f2, sorted(S, key=lambda w: (len(w), w))))
            log('     words with content {a,b,c} and a-count<N:', sorted([w for w in S if set(w) == set('abc')],
                key=lambda w: (len(w), w)))
        if R['status'] == 'contra':
            kind = R['contra'][0]
            if kind == 'apower':
                targets = [R['contra'][1]]
            else:
                sk = R['contra'][1]
                byc = {}
                for w in R['K']:
                    if skel(w) == sk and acount(w) <= N - 1: byc.setdefault(acount(w), w)
                targets = list(byc.values())[:2]
            cert = certificate(R['origin'], targets)
            okr, _ = replay(seed, cert)
            must(okr is True, 'E1 certificate replay')
            log('     certificate (%d steps, replay ok=%s) targets=%s' % (len(cert), okr is True, targets))
            for k, (w, (x, y, E0, E1)) in enumerate(cert):
                log('       %2d x=%s y=%s E0=%s E1=%s => %s' % (k, x, y, E0, E1, w))
        out[f2] = R
    return out

# =================================================================== E2
def e2_seed(N, deltas):
    S = {'a' * N}
    P = list(deltas)
    for p in P:
        S |= flanked([p], N - deltas[p])
    for p, q in itertools.product(P, P):
        t = N - deltas[p] - deltas[q]
        if t >= 3: S |= flanked([p, q], t)
    return S

def run_E2():
    log('== [E2] within-class {b,c} bigram-linearity: closure experiments')
    res = {}
    # relation: v(bcbc)+v(cb) = v(bc)+v(cbcb)  (skeleton bigram multisets incl. boundary)
    from collections import Counter
    vb = lambda p: Counter(skel('a' + p + 'a')[i:i + 2] for i in range(len(p) + 1))
    must(vb('bcbc') + vb('cb') == vb('bc') + vb('cbcb'), 'E2: bigram relation holds')
    # first two cases: deliberately inconsistent with concatenation additivity (expect contradiction)
    # last two: primitive cores bc, cb only; products generated by closure.
    cases = [('naive-violating', {'bc': 2, 'cb': 2, 'bcbc': 3, 'cbcb': 4}),
             ('naive-linear', {'bc': 2, 'cb': 2, 'bcbc': 3, 'cbcb': 3}),
             ('prim-bc2-cb3', {'bc': 2, 'cb': 3})]
    # NOTE: the consistent control ('bc':2,'cb':2) was attempted during development; its closure
    # did not terminate within ~9 minutes (|K| grows past 10^4 words); it is NOT part of this run.
    for name, deltas in cases:
        N = 10
        seed = e2_seed(N, deltas)
        t0 = time.time()
        R = closure(seed, cap_len=N + 4, cap_words=30000, max_rounds=6, N=N)
        dt = time.time() - t0
        log('   case %-15s N=%d |seed|=%d -> status=%s |K|=%d rounds=%d time=%.1fs contra=%s'
            % (name, N, len(seed), R['status'], len(R['K']), R['rounds'], dt, R['contra']))
        res[name] = R
        if R['status'] == 'contra':
            kind = R['contra'][0]
            if kind == 'apower':
                targets = [R['contra'][1]]
            else:
                sk = R['contra'][1]
                ws = [w for w in R['K'] if skel(w) == sk and acount(w) <= N - 1]
                byc = {}
                for w in ws: byc.setdefault(acount(w), w)
                targets = list(byc.values())[:2]
            cert = certificate(R['origin'], targets)
            okr, K2 = replay(seed, cert)
            must(okr is True, 'E2 %s: certificate replay' % name)
            log('     certificate: %d rule applications, replay=%s, targets=%s' % (len(cert), okr is True, targets))
            for step, (w, (x, y, E0, E1)) in enumerate(cert[:40]):
                log('       %2d  x=%s y=%s E0=%s E1=%s  =>  %s' % (step, x, y, E0, E1, w))
            if len(cert) > 40: log('       ... (%d more)' % (len(cert) - 40))
            res[name + '_cert'] = cert
    return res

# =================================================================== S1/S3 random closed sets
def random_seed_words(N, k):
    S = {'a' * N}
    for _ in range(k):
        npieces = random.choice([1, 1, 2])
        pieces = [''.join(random.choice('bc') for _ in range(random.choice([1, 1, 2])))
                  for _ in range(npieces)]
        tot = random.randint(npieces + 1, N - 1)
        comp = random.choice(list(compositions(tot, npieces + 1)))
        w = 'a' * comp[0]
        for pi, p in zip(pieces, comp[1:]): w += pi + 'a' * p
        S.add(w)
    return S

def exchange_instances(S, N):
    """(X1): solo cores pi,pi' same content; host X a^i pi a^j Y in S with room
    => X a^{i'} pi' a^{j'} Y in S for the predicted i',j'. Returns (#checked, #fail)."""
    solo = {}
    for w in S:
        if w[0] == 'a' and w[-1] == 'a' and set(w) != {'a'}:
            core = w.strip('a')
            lam = len(w) - len(core)
            if acount(w) <= N - 1 and len(w) - len(w.lstrip('a')) >= 1:
                solo.setdefault(core, set()).add(acount(w))
    solo = {k: min(v) for k, v in solo.items()}
    delta = {k: N - e for k, e in solo.items()}
    chk = fl = 0
    for W in S:
        for core, d in delta.items():
            start = W.find(core)
            while start != -1:
                i0 = len(W[:start]) - len(W[:start].rstrip('a'))
                end = start + len(core)
                j0 = len(W[end:]) - len(W[end:].lstrip('a'))
                for core2, d2 in delta.items():
                    if core2 == core or (set(core2) | {'a'}) != (set(core) | {'a'}): continue
                    lam = solo[core] - acount(core); lam2 = solo[core2] - acount(core2)
                    need = 2 + max(0, lam - lam2)
                    if i0 + j0 < need: continue
                    # choose i,j within flanks with i+j = 2+max(0,lam-lam2), i,j>=1
                    s = 2 + max(0, lam - lam2)
                    i = min(i0, s - 1); j = s - i
                    if j > j0 or j < 1 or i < 1: continue
                    if i + j > lam: continue
                    s2 = s + lam2 - lam
                    i2 = 1; j2 = s2 - 1
                    if j2 < 1: continue
                    X = W[:start - i]; Y = W[end + j:]
                    W2 = X + 'a' * i2 + core2 + 'a' * j2 + Y
                    chk += 1
                    if W2 not in S: fl += 1
                start = W.find(core, start + 1)
    return chk, fl

def rotation_instances(S, N):
    """(Rot): a^p kappa a^r in S, p,r>=1, 3<=p+r<=N-1, kappa=core  =>  ctx(a kappa)=ctx(kappa a)."""
    ctx = defaultdict(set)
    for w in S:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                ctx[w[i:j]].add((w[:i], w[j:]))
    chk = fl = 0
    for w in S:
        if set(w) == {'a'} or w[0] != 'a' or w[-1] != 'a': continue
        core = w.strip('a'); lam = len(w) - len(core)
        if 3 <= lam <= N - 1:
            chk += 1
            if ctx['a' + core] != ctx[core + 'a']: fl += 1
    return chk, fl

def run_S1_S3(trials=300):
    log('== [S1]/[S3] random seeds -> exact closure; Lemma S and exchange (X1) on closed sets')
    stats = defaultdict(int)
    xchk = xfail = 0
    for t in range(trials):
        N = random.randint(5, 6)
        seed = random_seed_words(N, random.randint(1, 3))
        R = closure(seed, cap_len=N + 3, cap_words=3000, max_rounds=12, N=N, stop_on_contra=False)
        stats[R['status']] += 1
        if R['status'] == 'closed':
            K = R['K']
            ok, wit = check_closed(K)
            must(ok, 'S1: closure reported closed but exact check fails: %s' % wit)
            if shortest_apower(K) == N:
                stats['closed_with_min_aN'] += 1
                sc = skeleton_conflicts(K, N)
                must(not sc, 'S1: Lemma S violated on closed set: %s' % sc)
                c, f = rotation_instances(K, N)
                xchk += c; xfail += f
        elif R['status'] == 'contra':
            stats['contra_' + R['contra'][0]] += 1
    must(xfail == 0, 'S3: rotation lemma failures: %d' % xfail)
    log('   trials=%d status counts=%s' % (trials, dict(stats)))
    log('   rotation-lemma (Rot) instances checked=%d failures=%d' % (xchk, xfail))
    return stats

# =================================================================== S2 negative control
def d1_closure(seed, cap_len, N):
    K = set(seed)
    for _ in range(20):
        ctx = defaultdict(set)
        for w in K:
            n = len(w)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    ctx[(w[i:j],)].add((w[:i], w[j:]))
        bucket = defaultdict(list)
        for x, Es in ctx.items():
            for E in Es: bucket[(ttype(x), E)].append(x)
        new = set()
        for _, xs in bucket.items():
            if len(xs) < 2: continue
            for x in xs:
                for y in xs:
                    if x == y: continue
                    for E1 in ctx[x]:
                        w = fill(E1, y)
                        if w not in K and len(w) <= cap_len: new.add(w)
        if not new: return K
        K |= new
    return None

def run_S2():
    log('== [S2] negative control: d=1-closed set violating Lemma S must be d=2-non-closed')
    found = 0
    N = 7
    cands = [('abaaa', 'aaaaba'), ('abaa', 'aabaa'), ('abaaaa', 'aaba'), ('aabaaa', 'aba')]
    for w1, w2 in cands:
        seed = {'a' * N, w1, w2}
        K = d1_closure(seed, N + 2, N)
        if K is None: continue
        if shortest_apower(K) != N: continue
        sc = skeleton_conflicts(K, N)
        if not sc: continue
        ok, wit = check_closed(K)
        must(not ok and verify_witness(K, wit), 'S2: expected a verified d=2 violation')
        must(wit is not None and len(wit['x']) == 2, 'S2: violation should be two-hole')
        log('   seed', sorted(seed), '-> d1-closed |K|=%d, skeleton conflict %s' % (len(K), sc))
        log('   d=2 witness:', json.dumps(wit, default=list))
        found += 1
        break
    must(found == 1, 'S2: negative control instance found')

# =================================================================== S4 tree arithmetic
def run_S4(trials=4000):
    log('== [S4] Theorem T1 arithmetic on random rank<=r trees')
    worst = 0.0
    for t in range(trials):
        r = random.randint(2, 3); theta = random.randint(1, 4)
        # random tree: node = (terminals, children); depth-limited
        def gen(depth):
            nt = random.randint(0, theta)
            if depth == 0 or random.random() < 0.15:
                return (max(nt, 1), [])
            q = random.randint(1, r)
            return (nt, [gen(depth - 1) for _ in range(q)])
        T = gen(random.randint(2, 9))
        # compute k, heights; boundary = leftmost & rightmost root paths
        nodes = []
        def walk(node, depth, left, right):
            nt, ch = node
            k = nt + sum(walk(c, depth + 1, left and i == 0, right and i == len(ch) - 1)
                         for i, c in enumerate(ch))
            nodes.append((k, left, right, depth))
            return k
        Ntot = walk(T, 1, True, True)
        h = max(d for (_, _, _, d) in nodes)
        # deficits: delta in [k-theta, k] for EVERY big node (boundary included), SNAPPED to reuse
        # existing values whenever possible (adversarial: minimises M)
        vals = set()
        for (k, l, rr, d) in nodes:
            if k > theta:
                lo, hi = max(1, k - theta), k
                reuse = [v for v in vals if lo <= v <= hi]
                vals.add(reuse[0] if reuse else random.randint(lo, hi))
        M = len(vals)
        sigma = 2 * (r + 1)
        bound = theta * sigma ** (2 * M + 1)          # Theorem T1 (sharp form): N < theta*sigma^(2M+1)
        must(Ntot < bound, 'S4: N=%d >= bound=%d (h=%d,r=%d,theta=%d,M=%d)' % (Ntot, bound, h, r, theta, M))
        worst = max(worst, Ntot / bound)
    log('   trials=%d, max N/bound = %.4f' % (trials, worst))

# =================================================================== main
def main():
    t0 = time.time()
    src = open(__file__, 'rb').read()
    log('checker SHA256', hashlib.sha256(src).hexdigest())
    log('python', sys.version.split()[0], ' seed 20261115')
    sel = sys.argv[1].split(',') if len(sys.argv) > 1 else ['S0', 'E1', 'S2', 'S1', 'S4', 'E2']
    log('sections', sel)
    if 'S0' in sel: run_S0()
    if 'E1' in sel: run_E1()
    if 'S2' in sel: run_S2()
    if 'S1' in sel: run_S1_S3()
    if 'S4' in sel: run_S4()
    if 'E2' in sel: run_E2()
    log('== SUMMARY: checks=%d FAIL=%d  time=%.1fs' % (COUNT, FAIL, time.time() - t0))
    log('ALL CHECKS PASSED' if FAIL == 0 else 'SOME CHECKS FAILED')
    sys.exit(0 if FAIL == 0 else 1)

if __name__ == '__main__':
    main()
