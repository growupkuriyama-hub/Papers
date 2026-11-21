"""Finite consistency checks for the accompanying proof. Python 3, standard library."""
from functools import lru_cache
from itertools import product
from hashlib import sha256


@lru_cache(None)
def pure(level):
    if level == 0:
        return 'a', 'ab'
    return combine(pure(level - 1), pure(level - 1))


def combine(left, right):
    return left[0], right[0] + left[1] + right[1]


def escaped(level, path):
    if not path:
        return 'c', 'bab'
    children = [pure(level - 1), pure(level - 1)]
    children[path[0]] = escaped(level - 1, path[1:])
    return combine(*children)


def sentence(pair):
    return pair[0] + 'b' + pair[1]


def check_example():
    n = 11
    whole = sentence(pure(n))
    z = pure(n - 2)[1]
    slices = {}
    for depth in range(n):
        words = {sentence(escaped(n, path)) for path in product(range(2), repeat=depth)}
        lengths = {len(w) for w in words}
        assert len(lengths) == 1 and all(w.count('c') == 1 for w in words)
        (length,) = lengths
        assert length not in slices
        slices[length] = words
    target_slice = slices[len(sentence(escaped(n, (0, 0, 0))))]
    for word in sorted(target_slice):
        p, r = word.find(z), word.rfind(z)
        if 0 <= p and p + len(z) <= word.index('c') < r:
            break
    else:
        raise AssertionError('two copies surrounding the marker were required')
    pre, middle, post = word[:p], word[p + len(z):r], word[r + len(z):]
    buckets = {}
    for i in range(1, len(z) - 1):
        key = (z[i], frozenset(z[:i]), frozenset(z[i + 1:]))
        buckets.setdefault(key, []).append(i)
    cuts = max(buckets.values(), key=len)[:9]
    assert len(cuts) == 9
    i = cuts[0]
    separator = z[i:] + middle + z[:i + 1]
    start = whole.index(z)
    def shared(k):
        return whole[:start] + z[:k] + z[i] + z[k + 1:] + whole[start + len(z):]
    def test(k):
        return pre + z[:k] + separator + z[k + 1:] + post
    assert all(shared(k) == whole for k in cuts)
    outputs = {test(k) for k in cuts}
    assert test(i) == word and len(outputs) == 9
    assert all(len(v) == len(word) and v.count('c') == 1 for v in outputs)
    k = next(k for k in cuts if test(k) not in target_slice)
    print('One-escape example n=11. Pure word length', len(whole), 'buffer length', len(z))
    print('Test slice length', len(word), 'members', len(target_slice), 'distinct test outputs', len(outputs))
    for label, value in [('E0[x]', shared(i)), ('E0[y]', shared(k)), ('E1[x]', word), ('E1[y]', test(k))]:
        print(label, 'IN' if value == whole or value in target_slice else 'OUT', 'sha256', sha256(value.encode()).hexdigest())


def check_internal():
    for modulus in range(2, 17):
        accepted = lambda length: length > 0 and (length - 1) % modulus == 0
        for d in (1, 2):
            for a, b in product(range(d, 2 * modulus + d), repeat=2):
                for fixed in range(d - 1, d - 1 + modulus):
                    if accepted(fixed + a) and accepted(fixed + b):
                        assert all(accepted(t + a) == accepted(t + b) for t in range(d - 1, d - 1 + modulus))
        assert min(k for k in range(modulus + 2) if k >= modulus + 1 and accepted(k)) == modulus + 1
    print('Unary internal-class example: M=2..16, both arities and all context residues passed.')


if __name__ == '__main__':
    check_internal()
    check_example()
