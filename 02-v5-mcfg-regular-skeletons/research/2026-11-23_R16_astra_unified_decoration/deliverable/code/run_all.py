"""Finite audits for R16. All products act on the right."""
from itertools import permutations, product
from random import Random


def words(alphabet, max_length):
    for length in range(1, max_length + 1):
        yield from product(alphabet, repeat=length)


def compose(x, y):
    return tuple(y[i] for i in x)


def closure(gens):
    seen = set(gens)
    pending = list(gens)
    while pending:
        x = pending.pop()
        for a in gens:
            z = compose(x, a)
            if z not in seen:
                seen.add(z)
                pending.append(z)
    return seen


def bad_corner(s):
    idem = sorted(x for x in s if compose(x, x) == x)
    for e in idem:
        local = [x for x in idem if compose(e, x) == compose(x, e) == x]
        for x, y in product(local, repeat=2):
            if compose(x, y) != compose(y, x):
                return True
    return False


def boundary(w, d):
    h = d - 1
    if len(w) < max(1, 2*h):
        return ('short', w)
    return ('long', w[:h], w[len(w)-h:])


def small_semigroups():
    swap, off, identity = (1, 0), (0, 0), (0, 1)
    cases = [
        ('I2', [(1, 0, 2), (0, 2, 2)], 7, False),
        ('last-run', [swap, off], 4, True),
        ('two resets', [off, (1, 1)], 2, False),
        ('reset monoid', [identity, off, (1, 1)], 3, True),
        ('scattered ab, binary', [(1, 1, 2), (0, 2, 2)], 4, False),
        ('scattered ab, neutral c', [(1, 1, 2), (0, 2, 2), (0, 1, 2)], 5, True),
    ]
    for label, gens, size, bad in cases:
        s = closure(gens)
        assert (len(s), bad_corner(s)) == (size, bad)
        print(f'{label}: order={size}, noncommuting local idempotents={bad}')


def group_and_counts():
    group = list(permutations(range(3)))
    identity = (0, 1, 2)
    gens = [(1, 0, 2), (1, 2, 0)]
    checks = 0
    for w in words(range(2), 6):
        for u, v in product(group, repeat=2):
            shift = next(h for h in group if compose(h, u) == v)
            p, q = u, v
            for a in w:
                assert compose(shift, p) == q
                p, q = compose(p, gens[a]), compose(q, gens[a])
            checks += 1
    central = [h for h in group if all(compose(h, a) == compose(a, h) for a in gens)]
    assert central == [identity]
    for d in range(1, 33):
        flank = 'b' * (2*d)
        u, v = flank + 'a' + flank, flank + 'aa' + flank
        assert (set(u), boundary(u,d)) == (set(v), boundary(v,d))
        assert (u.count('a') >= 2) != (v.count('a') >= 2)
    print(f'S3 regular translations={checks}, natural-action centralizer order=1')
    print('fixed trivial lower: threshold collision for every tested width 1..32')


def rare_endpoint():
    # Min-plus evaluation of A0 -> a | b, Ai -> A(i-1)A(i-1) | b.
    # a acts as the identity and b as constant one.
    ident, reset = (0, 1), (1, 1)
    costs = {ident: 1, reset: 1}
    table = []
    for i in range(13):
        best = min(n for t,n in costs.items() if t[0] == 0)
        assert best == 2**i
        table.append(best)
        new = {reset: 1}
        for (x, m), (y, n) in product(costs.items(), repeat=2):
            z = compose(x, y)
            new[z] = min(new.get(z, m+n), m+n)
        costs = new
    print('rare 0->0 shortest yields for n=0..12:', *table)


def even_run():
    count = 0
    for w in words('ab', 8):
        for u in range(2):
            z, support = u, set()
            for a in w:
                if a == 'b':
                    support.add(z)
                else:
                    z ^= 1
            for y in range(2):
                actual = y
                for a in w:
                    if a == 'b' and actual == 1:
                        actual = 2
                    if a == 'a' and actual < 2:
                        actual ^= 1
                allowed = all((v ^ u ^ y) == 0 for v in support)
                recovered = y ^ u ^ z if allowed else 2
                assert actual == recovered
                count += 1
    print('even-run whole partial maps, coordinate checks:', count)


# Regular lower semigroup: a non-group completely simple Rees matrix semigroup.
K = tuple(product(range(2), repeat=3))
ONE = (2, 0, 0)
STATES = (ONE,) + K
LETTERS = ((0, 1, 0), (1, 0, 1))
WIDTH = len(K)
MOD = WIDTH + 1


def mul(x, y):
    if x == ONE:
        return y
    if y == ONE:
        return x
    i,g,j = x
    l,h,k = y
    return i, (g + j*l + h) % 2, k


def event(z, a):
    return 2 * STATES.index(z) + a


def read(w, x):
    upper = set()
    for a in w:
        upper.add(event(x,a))
        x = mul(x, LETTERS[a])
    return upper, x


def observe(w, x, offset):
    counters = [(offset + i) % MOD for i in range(2*len(STATES))]
    # The real tag contains all counters. Its content projects onto this
    # smaller observable: the active counter is the only one used.
    observed = set()
    for a in w:
        j = event(x,a)
        observed.add((j,counters[j]))
        counters[j] = (counters[j]+1) % MOD
        x = mul(x,LETTERS[a])
    return observed, x


def decode(w_prefix, x, end, observed):
    if len(w_prefix) < WIDTH:
        return [read(w_prefix,y)[0] for y in STATES], read(w_prefix,ONE)[1]
    p = read(w_prefix,ONE)[1]
    h = next(t for t in STATES if mul(t,mul(x,p)) == p)
    residues = [set() for _ in range(2*len(STATES))]
    for j,c in observed:
        residues[j].add(c)
    prefix_counts = [0] * len(residues)
    z = x
    for a in w_prefix:
        prefix_counts[event(z,a)] += 1
        z = mul(z,LETTERS[a])
    tail = [divmod(j,2) for j,rs in enumerate(residues) if len(rs) > prefix_counts[j]]
    upper = []
    for y in STATES:
        value, _ = read(w_prefix,y)
        for state_index,a in tail:
            value.add(event(mul(mul(y,h), STATES[state_index]), a))
        upper.append(value)
    return upper, mul(h,end)


def wreath_decoder():
    assert all(mul(mul(x,y),z) == mul(x,mul(y,z)) for x,y,z in product(STATES,repeat=3))
    assert all(any(mul(h,mul(x,p)) == p for h in STATES) for x,p in product(STATES,K))
    rng = Random(20261123)
    sample = list(words(range(2), 8))
    sample += [tuple(rng.randrange(2) for _ in range(n)) for n in range(9,64) for _ in range(3)]
    sample += [(a,)*n for a in (0,1) for n in (9,17,63,97)]
    count = 0
    for w in sample:
        upper = [read(w,y)[0] for y in STATES]
        bottom = read(w,ONE)[1]
        for x in STATES:
            for offset in (0,4):
                obs, end = observe(w,x,offset)
                assert decode(w[:WIDTH],x,end,obs) == (upper,bottom)
                count += 1
    print(f'Rees wreath decoding: words={len(sample)}, entrance/counter trials={count}, upper coordinates per trial={len(STATES)}')


def neutral_loops():
    # A permutation lower. A long neutral buffer also synchronizes the fixed
    # boundary register: guarded loops start at the same parity and suffix.
    from collections import Counter
    count = 0
    for m in range(1, 6):
        for toggles in product(range(2), repeat=3):
            def observation(w):
                q = 0
                trace = []
                for a in w:
                    trace.append((q,a))
                    q ^= toggles['abc'.index(a)]
                tags = tuple(trace)
                freq = Counter(tags[i:i+m] for i in range(len(tags)-m+1))
                return boundary(tags,m), freq
            c = 'c'*(2*m)
            u, v = (c+'a'+c)*2, (c+'b'+c)*2
            x, y = c+u+v, c+v+u
            assert observation(x) == observation(y)
            assert x.replace('c','') == 'aabb' and y.replace('c','') == 'bbaa'
            count += 1
    print('guarded-loop raw-count collisions for scattered ab:', count)


if __name__ == '__main__':
    small_semigroups()
    group_and_counts()
    rare_endpoint()
    even_run()
    wreath_decoder()
    neutral_loops()
    print('PASS (finite checks only)')
