#!/usr/bin/env python3
"""Theorem thm:frame-total (Lemmas lem:marked-node, lem:mixing): total length of frame presentations of M_n without (or with a
mark-blind) observer.  Checks the combinatorial core of the mixing argument:

  For 1 <= j < n, let the E_j-nodes of w*_n be indexed by their paths pi in {l,r}^{n-j},
  z_pi = w*_n with that node replaced by v_j = ⌈w*_{j-1}⌉, and z_pi = P_pi v_j Q_pi.
  (1) z_pi in M_n, there are 2^{n-j} of them, P_pi is a prefix and Q_pi a suffix of w*_n;
  (2) P_pi v_j Q_pi' in L_n  iff  pi = pi'          (the mixing lemma);
  (3) |z_pi| = |w*_n| - |w*_{j-1}|, so the constituent bound |x| >= |w*_n| - l - |w*_{j-1}|
      leaves an outer context of length <= l;
  (4) observers: s_U separates v_j from w*_j for every j; the length-parity typing
      separates them only for j = 1;
  (5) the counting bound 2^{n-j} <= (3*2^{j-1}-1)(l+1) Σ|α| against F_n
      (l = 2n, Σ|α| of F_n) -- a consistency check only.
Usage: python3 -I check_frame_total_length.py [N]   (default N = 6)
Encoding: a, ⌊ -> '[', ⌋ -> ']', ⌈ -> '{', ⌉ -> '}'.
"""
import sys
from itertools import product


def wstar(i):
    w = 'a'
    for _ in range(i):
        w = '[' + w + w + ']'
    return w


def parse(s, k):
    """return (end, depth) of the E-node starting at s[k], or None."""
    if k >= len(s):
        return None
    c = s[k]
    if c == 'a':
        return k + 1, 0
    if c == '{':
        r = parse(s, k + 1)
        if r and r[0] < len(s) and s[r[0]] == '}':
            return r[0] + 1, r[1] + 1
        return None
    if c == '[':
        r1 = parse(s, k + 1)
        if not r1:
            return None
        r2 = parse(s, r1[0])
        if r2 and r2[1] == r1[1] and r2[0] < len(s) and s[r2[0]] == ']':
            return r2[0] + 1, r1[1] + 1
    return None


def in_L(s, n):
    r = parse(s, 0)
    return bool(r) and r[0] == len(s) and r[1] == n


def node_offset(n, j, pi):
    """offset of the E_j-node with path pi in w*_n"""
    off, i = 0, n
    for d in pi:
        off += 1                       # the bracket ⌊ of the current node
        if d == 'r':
            off += len(wstar(i - 1))   # skip the left child
        i -= 1
    assert i == j
    return off


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    ok = True
    for n in range(2, N + 1):
        W = wstar(n)
        for j in range(1, n):
            v = '{' + wstar(j - 1) + '}'
            wj = wstar(j)
            parts = {}
            for pi in product('lr', repeat=n - j):
                o = node_offset(n, j, pi)
                assert W[o:o + len(wj)] == wj
                P, Q = W[:o], W[o + len(wj):]
                z = P + v + Q
                ok &= in_L(z, n) and z != W and len(z) == len(W) - len(wstar(j - 1))
                parts[pi] = (P, Q)
            cnt = len(parts)
            mix = all(in_L(parts[p][0] + v + parts[q][1], n) == (p == q) for p in parts for q in parts)
            ok &= cnt == 2 ** (n - j) and mix
            if n <= 4 or j == 1:
                print(f'n={n} j={j}: {cnt} marked words z_pi (2^(n-j)={2 ** (n - j)}), '
                      f'P_pi v Q_pi\' in L_n iff pi=pi\': {mix}')
    # observers
    for j in range(1, 8):
        v, wj = '{' + wstar(j - 1) + '}', wstar(j)
        sU = ('{' in v) != ('{' in wj)
        par = len(v) % 2 != len(wj) % 2
        ok &= sU and (par == (j == 1))
    print('s_U separates v_j from w*_j for all j; parity separates them only for j=1: '
          + str(ok))
    # consistency with F_n (frames of length <= 2n, Σ|α| of F_n)
    for n in range(2, N + 1):
        sigma = 0
        sigma += 1 + sum(3 for _ in range(1, n))          # E_0 -> a ; E_k -> {E}: |α| = 3
        sigma += sum(4 for _ in range(1, n))              # E_k -> [E E]: |α| = 4
        sigma += sum(2 ** d * (2 * (d + 1) + 1 + d) for d in range(n))  # S -> T_pi
        l = 2 * n
        good = all(2 ** (n - j) <= (3 * 2 ** (j - 1) - 1) * (l + 1) * sigma for j in range(1, n))
        ok &= good
        print(f'n={n}: F_n has Σ|α|={sigma}, l={l}; counting bound consistent: {good}')
    print('ALL OK' if ok else 'SOME CHECK FAILED')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
