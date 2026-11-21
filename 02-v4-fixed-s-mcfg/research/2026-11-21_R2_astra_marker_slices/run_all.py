"""R2 finite checks. Run with Python 3. No network or third-party packages."""
from collections import defaultdict
from itertools import combinations
from functools import lru_cache


def check_layered(mark_deep):
    n, h, t = 12, 3, 2

    def children(level, state):
        first = (level + state) % 2
        return first, 1 - first

    def join(level, state, left, right):
        first = left[0] + right[0] if state == 0 else right[0] + left[0]
        second = right[1] + left[1] if level % 2 else left[1] + right[1]
        return first, second

    def escape(level, variant):
        pair = ('c', 'a' if variant == 0 else 'b')
        return pair if mark_deep and level == n - h - t else pair[::-1]

    @lru_cache(None)
    def pure(level, state):
        if level == 0:
            return ('ababa', 'a') if state == 0 else ('baaab', 'b')
        u, v = children(level, state)
        return join(level, state, pure(level - 1, u), pure(level - 1, v))

    def occurrence(path):
        level, state = n, 0
        for side in path:
            state = children(level, state)[side]
            level -= 1
        return level, state

    def root_word(path, variant):
        def marked(level, state, depth):
            if depth == len(path):
                return escape(level, variant)
            side = path[depth]
            kid = children(level, state)
            args = [pure(level - 1, k) for k in kid]
            args[side] = marked(level - 1, kid[side], depth + 1)
            return join(level, state, *args)
        first, second = marked(n, 0, 0)
        return first + 'b' + second

    def paths_at(k):
        return [tuple(map(int, format(j, '0%db' % k))) if k else ()
                for j in range(2 ** k)]

    # Each entry in this list is a component interval of a depth-h node.
    component = 0 if mark_deep else 1
    def order(level, state, path):
        if len(path) == h:
            return [(path, state)]
        u, v = children(level, state)
        a = order(level - 1, u, path + (0,))
        b = order(level - 1, v, path + (1,))
        reverse = state != 0 if component == 0 else level % 2 != 0
        return b + a if reverse else a + b

    ordered = order(n, 0, ())
    repeated = [j for j, item in enumerate(ordered) if item[1] == 0]
    lo, mid, hi = repeated[:3]
    path = ordered[mid][0] + ((0,) * t if mark_deep else ())
    vword = root_word(path, 0)
    z = pure(n-h, 0)[component]
    lengths = [len(pure(n-h, state)[component]) for _, state in ordered]
    # The marked node can also change the length of the other root component.
    prefix_len = 0
    lev, st = occurrence(path)
    if component == 1:
        # Reconstruct the first component's actual length from the one changed
        # subtree (every rule preserves the component index).
        prefix_len = len(pure(n, 0)[0]) - len(pure(lev, st)[0]) + len(escape(lev, 0)[0]) + 1
    first_pos = prefix_len + sum(lengths[:lo])
    delta = len(escape(lev, 0)[component]) - len(pure(lev, st)[component])
    last_pos = prefix_len + sum(lengths[:hi]) + delta
    assert vword[first_pos:first_pos+len(z)] == vword[last_pos:last_pos+len(z)] == z
    p, gap, r = vword[:first_pos], vword[first_pos+len(z):last_pos], vword[last_pos+len(z):]
    assert 'c' in gap

    target_len = len(vword)
    pure_length = sum(map(len, pure(n, 0))) + 1
    members = set()
    configurations = 0
    for k in range(n):
        for candidate in paths_at(k):
            lev, st = occurrence(candidate)
            if pure_length - sum(map(len, pure(lev, st))) + 2 == target_len:
                for variant in range(2):
                    members.add(root_word(candidate, variant))
                    configurations += 1
    assert vword in members and 18 * len(members) < len(z) - 2
    groups = defaultdict(list)
    for i in range(1, len(z)-1):
        groups[z[i], frozenset(z[:i]), frozenset(z[i+1:])].append(i)
    positions = max(groups.values(), key=len)
    i0 = positions[0]
    fixed = z[i0:] + gap + z[:i0+1]
    assert p + z[:i0] + fixed + z[i0+1:] + r == vword
    for i in positions:
        forced = p + z[:i] + fixed + z[i+1:] + r
        if forced not in members:
            assert len(forced) == len(vword) and forced.count('c') == 1
            assert z[:i] + z[i0] + z[i+1:] == z
            print(f'layered deep={mark_deep} n={n} k={len(path)} z={len(z)} '
                  f'configurations={configurations} slice_words={len(members)} '
                  f'cut0={i0} missing_cut={i}')
            break
    else:
        raise AssertionError('missing fourth word expected')


def grammar_rules(t):
    mass = 3 * t * t
    rules = [[] for _ in range(mass+1)]
    for j in range(1, mass+1):
        for char, cost in [('a', 1), ('b', 1), ('c', t)]:
            if j >= cost:
                rules[j].append((char, (j-cost,) if j > cost else ()))
    rules[t].append(('a'*t, ()))
    rules[mass].append(('', (t*t, 2*t*t)))
    rules[2*t*t].append(('', (t*t, t*t)))
    return mass, rules


def check_weight(t):
    m, rules = grammar_rules(t)
    infinity = 10**12
    inside = [0]*(m+1)
    nodes = [0]*(m+1)
    outside = [infinity]*(m+1)
    outside[m] = 0
    size = m
    for j in range(1, m+1):
        inside[j] = min(len(word) + sum(inside[k] for k in kids) for word, kids in rules[j])
        pure_costs = [(1 + sum(nodes[k] for k in kids), kids)
                      for word, kids in rules[j] if set(word) <= {'a'}]
        nodes[j] = min(cost for cost, _ in pure_costs)
        if j in (m, 2*t*t):
            assert all(len(kids) == 2 for cost, kids in pure_costs if cost == nodes[j])
        size += sum(1 + len(word) + 2*len(kids) for word, kids in rules[j])
    theta = 0
    for j in range(m, 0, -1):
        for word, kids in rules[j]:
            witness = outside[j] + len(word) + sum(inside[k] for k in kids)
            theta = max(theta, witness)
            for k in kids:
                outside[k] = min(outside[k], witness-inside[k])
    assert nodes[m] == m - 3*(t-1) + 2
    assert theta == 4*t - 1 and size == 13*m-3*t+9
    return size, theta


def check_rect(m, t):
    @lru_cache(None)
    def words(j):
        if j == 0:
            return {''}
        return {letter+rest for letter, cost in [('a', 1), ('b', 1), ('c', t)]
                if cost <= j for rest in words(j-cost)}
    language = words(m)
    sizes = []
    for d in (1, 2):
        distribution = defaultdict(set)
        for w in language:
            for cuts in combinations(range(len(w)+1), 2*d):
                x = tuple(w[i:j] for i, j in zip(cuts[::2], cuts[1::2]))
                e = (w[:cuts[0]],) + tuple(w[i:j] for i, j in zip(cuts[1:-1:2], cuts[2::2])) + (w[cuts[-1]:],)
                distribution[x].add(e)
        for typing in (lambda s: frozenset(s), lambda s: 'c' in s):
            known = {}
            for x, contexts in distribution.items():
                types = tuple(map(typing, x))
                for e in contexts:
                    assert known.setdefault((types, e), contexts) == contexts
        sizes.append(len(distribution))
    print(f'finite full Rect mass={m} c_weight={t} words={len(language)} '
          f'observed_tuples={sizes} both_typings=pass')


if __name__ == '__main__':
    for deep in (False, True):
        check_layered(deep)
    for t in range(4, 21):
        size, theta = check_weight(t)
        if t in (4, 8, 12, 16, 20):
            print(f'weight t={t} shortest={3*t*t} size={size} original_theta={theta}')
    for value in (6, 7, 8):
        check_rect(value, 3)
    print('PASS')
