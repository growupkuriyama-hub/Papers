#!/usr/bin/env python3
"""v79 research library: finite MCFG evaluation and exact (f,h)-tuple
substitutability checking for FINITE languages.

Conventions follow main.tex (v78):
  * tuple components are nonempty;
  * an arity-d sentence context u0 [] u1 [] ... [] ud has nonempty
    internal separators u1..u_{d-1}; outer parts may be empty;
  * (f,h)-substitutability: for every d<=f and all x,y in (Sigma^+)^d,
    equal componentwise h-types and one shared accepting context imply
    equal distributions D_L(x)=D_L(y).

For a FINITE language L every tuple with nonempty distribution occurs in
some word of L, so enumerating all occurrences is an EXACT decision
procedure (optionally restricted to tuples with bounded component length;
the restriction is then reported and the check is only a partial test).

Nothing here proves a general theorem; the scripts only test finite
instances and symbolic formulas.
"""
from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

# ---------------------------------------------------------------------------
# Finite monoids / typings
# ---------------------------------------------------------------------------


class Typing:
    """A finite-monoid homomorphism given by letter images and a product.

    `mul(a,b)` must be associative with identity `one`.  Types of words are
    computed left to right; results are memoised per word.
    """

    def __init__(self, name: str, letter: Callable[[str], object],
                 mul: Callable[[object, object], object], one: object):
        self.name = name
        self.letter = letter
        self.mul = mul
        self.one = one
        self._cache: Dict[str, object] = {}

    def __call__(self, w: str):
        c = self._cache.get(w)
        if c is not None:
            return c
        t = self.one
        for ch in w:
            t = self.mul(t, self.letter(ch))
        self._cache[w] = t
        return t


def trivial_typing() -> Typing:
    return Typing("triv", lambda c: 0, lambda a, b: 0, 0)


def content_typing(markers: Iterable[str], name: str = "content") -> Typing:
    """Semilattice of subsets: h(w) = set of marker letters occurring in w.
    With a single marker this is the two-element semilattice h_U."""
    ms = frozenset(markers)
    return Typing(name, lambda c: frozenset([c]) if c in ms else frozenset(),
                  lambda a, b: a | b, frozenset())


def window_typing(k: int, l: int, name: Optional[str] = None) -> Typing:
    """Prefix-suffix typing h^{k,l}_Sigma realised directly on words."""
    m0 = max(1, k + l)

    class _W(Typing):
        def __call__(self, w: str):
            if len(w) < m0:
                return ("s", w)
            return ("l", w[:k], w[len(w) - l:] if l else "")

    t = _W(name or f"win{k},{l}", None, None, None)
    return t


def product_typing(*ts: Typing) -> Typing:
    class _P(Typing):
        def __call__(self, w: str):
            return tuple(t(w) for t in ts)

    return _P("x".join(t.name for t in ts), None, None, None)


def transformation_typing(n_states: int, maps: Dict[str, Tuple[int, ...]],
                          name: str = "trans") -> Typing:
    """Transition monoid of a DFA: letters act on {0..n-1} (left-to-right
    composition f then g)."""
    ident = tuple(range(n_states))

    def mul(f, g):
        return tuple(g[f[i]] for i in range(n_states))

    return Typing(name, lambda c: maps[c], mul, ident)


# ---------------------------------------------------------------------------
# Tuple occurrences and the exact check
# ---------------------------------------------------------------------------

Ctx = Tuple[str, ...]          # (u0, u1, ..., ud)
Tup = Tuple[str, ...]          # (x1, ..., xd)


def occurrences(w: str, d: int, max_comp: Optional[int] = None):
    """Yield (x, E) for every arity-d tuple occurrence in w.
    Components and internal separators are nonempty."""
    n = len(w)
    if d == 1:
        for i in range(n):
            top = n if max_comp is None else min(n, i + max_comp)
            for j in range(i + 1, top + 1):
                yield (w[i:j],), (w[:i], w[j:])
        return
    if d == 2:
        for i1 in range(n):
            top1 = n if max_comp is None else min(n, i1 + max_comp)
            for j1 in range(i1 + 1, top1 + 1):
                x1 = w[i1:j1]
                u0 = w[:i1]
                for i2 in range(j1 + 1, n):
                    top2 = n if max_comp is None else min(n, i2 + max_comp)
                    sep = w[j1:i2]
                    for j2 in range(i2 + 1, top2 + 1):
                        yield (x1, w[i2:j2]), (u0, sep, w[j2:])
        return
    raise ValueError("only d in {1,2} implemented")


def fill(E: Ctx, x: Tup) -> str:
    out = [E[0]]
    for i, xi in enumerate(x):
        out.append(xi)
        out.append(E[i + 1])
    return "".join(out)


class Violation:
    def __init__(self, d, x, y, shared, F, accepts_x, accepts_y):
        self.d, self.x, self.y, self.shared, self.F = d, x, y, shared, F
        self.accepts_x, self.accepts_y = accepts_x, accepts_y

    def size(self):
        return sum(map(len, self.x)) + sum(map(len, self.y)) + sum(map(len, self.F))

    def __repr__(self):
        return (f"Violation(d={self.d}, x={self.x}, y={self.y}, "
                f"shared={self.shared}, F={self.F}, F[x] in L={self.accepts_x}, "
                f"F[y] in L={self.accepts_y})")


def check_substitutable(L: Iterable[str], h: Typing, f: int = 2,
                        max_comp: Optional[int] = None,
                        find_min: bool = True,
                        arities: Optional[Sequence[int]] = None):
    """Exact test of (f,h)-tuple substitutability for a finite language.

    Returns (ok, violation_or_None, stats).  If max_comp is given, only
    tuples whose components all have length <= max_comp are compared
    (a partial test)."""
    Ls = set(L)
    stats = {}
    best: Optional[Violation] = None
    for d in (arities or range(1, f + 1)):
        dist: Dict[Tup, set] = defaultdict(set)
        for w in Ls:
            for x, E in occurrences(w, d, max_comp):
                dist[x].add(E)
        stats[d] = len(dist)
        sig = {x: frozenset(Es) for x, Es in dist.items()}
        # invert: context -> tuples
        by_ctx: Dict[Ctx, List[Tup]] = defaultdict(list)
        for x, Es in dist.items():
            for E in Es:
                by_ctx[E].append(x)
        for E, xs in by_ctx.items():
            groups: Dict[object, List[Tup]] = defaultdict(list)
            for x in xs:
                groups[tuple(h(c) for c in x)].append(x)
            for _, g in groups.items():
                if len(g) < 2:
                    continue
                first = sig[g[0]]
                for y in g[1:]:
                    if sig[y] != first:
                        x0 = g[0]
                        diff = first ^ sig[y]
                        # pick the smallest distinguishing context
                        F = min(diff, key=lambda c: (sum(map(len, c)), c))
                        v = Violation(d, x0, y, E, F, F in first, F in sig[y])
                        if not find_min:
                            return False, v, stats
                        if best is None or v.size() < best.size():
                            best = v
        if best is not None and find_min:
            # report the smallest violation at the lowest failing arity
            return False, best, stats
    return best is None, best, stats


def minimize_violation(L, h, v: Violation):
    """Given a violation, verify it independently (membership + types)."""
    Ls = set(L)
    assert tuple(h(c) for c in v.x) == tuple(h(c) for c in v.y)
    assert all(v.x) and all(v.y)
    assert all(v.shared[1:-1]) and all(v.F[1:-1])
    assert fill(v.shared, v.x) in Ls and fill(v.shared, v.y) in Ls
    assert (fill(v.F, v.x) in Ls) != (fill(v.F, v.y) in Ls)
    return True


# ---------------------------------------------------------------------------
# Finite (acyclic) MCFG evaluation, goodness and thickness
# ---------------------------------------------------------------------------
# A rule is (lhs, children, template) where template is a tuple of
# components; each component is a list of items, an item being either a
# terminal string or a pair (j, k) meaning component k of child j
# (0-based).


class MCFG:
    def __init__(self, fan: Dict[str, int], rules: List[tuple], start: str):
        self.fan = fan
        self.rules = rules
        self.start = start

    # -- structural checks ---------------------------------------------
    def check_good(self) -> List[str]:
        problems = []
        for (A, ch, tpl) in self.rules:
            if len(tpl) != self.fan[A]:
                problems.append(f"fan-out mismatch in {A}->{tpl}")
            seen = []
            for comp in tpl:
                if not comp or all(isinstance(it, str) and it == "" for it in comp):
                    problems.append(f"empty component (not lambda-free) in {A}")
                prev = None
                for it in comp:
                    if isinstance(it, tuple):
                        seen.append(it)
                        if prev is not None and prev[0] == it[0] and it[1] == prev[1] + 1:
                            problems.append(f"merging {A}: {prev}{it}")
                        prev = it
                    else:
                        if it != "":
                            prev = None
            need = [(j, k) for j, B in enumerate(ch) for k in range(self.fan[B])]
            if sorted(seen) != sorted(need):
                problems.append(f"deleting/nonlinear rule for {A}: {seen} vs {need}")
            for j in range(len(ch)):
                order = [k for (jj, k) in seen if jj == j]
                if order != sorted(order):
                    problems.append(f"permuting rule for {A}, child {j}")
        return problems

    def size(self) -> int:
        s = 0
        for (A, ch, tpl) in self.rules:
            s += 1 + len(ch)
            for comp in tpl:
                for it in comp:
                    s += len(it) if isinstance(it, str) else 1
        return s

    # -- evaluation (assumes acyclic dependency) -----------------------
    def topo(self) -> List[str]:
        deps = defaultdict(set)
        for (A, ch, _) in self.rules:
            deps[A] |= set(ch)
        order, state = [], {}

        def visit(A):
            if state.get(A) == 2:
                return
            if state.get(A) == 1:
                raise ValueError("cyclic grammar; finite evaluation not supported")
            state[A] = 1
            for B in deps[A]:
                visit(B)
            state[A] = 2
            order.append(A)

        for A in self.fan:
            visit(A)
        return order

    @staticmethod
    def apply(tpl, kids):
        out = []
        for comp in tpl:
            parts = []
            for it in comp:
                parts.append(it if isinstance(it, str) else kids[it[0]][it[1]])
            out.append("".join(parts))
        return tuple(out)

    def tuples(self, limit: int = 2_000_000) -> Dict[str, set]:
        from itertools import product
        T: Dict[str, set] = {A: set() for A in self.fan}
        for A in self.topo():
            for (B, ch, tpl) in self.rules:
                if B != A:
                    continue
                for kids in product(*[T[c] for c in ch]):
                    T[A].add(self.apply(tpl, kids))
                    if len(T[A]) > limit:
                        raise MemoryError("tuple language too large")
        return T

    def language(self, **kw) -> set:
        return {t[0] for t in self.tuples(**kw)[self.start]}

    # -- thickness (min successful sentence length using each rule) ----
    def thickness(self) -> Tuple[int, Dict[int, int]]:
        INF = float("inf")
        lam = {A: INF for A in self.fan}
        order = self.topo()
        for A in order:
            for (B, ch, tpl) in self.rules:
                if B == A:
                    c = sum(len(it) for comp in tpl for it in comp if isinstance(it, str))
                    lam[A] = min(lam[A], c + sum(lam[x] for x in ch))
        mu = {A: INF for A in self.fan}
        mu[self.start] = 0
        for A in reversed(order):
            if mu[A] == INF:
                continue
            for (B, ch, tpl) in self.rules:
                if B != A:
                    continue
                c = sum(len(it) for comp in tpl for it in comp if isinstance(it, str))
                for j, X in enumerate(ch):
                    val = mu[A] + c + sum(lam[Y] for i, Y in enumerate(ch) if i != j)
                    mu[X] = min(mu[X], val)
        th = {}
        for idx, (A, ch, tpl) in enumerate(self.rules):
            c = sum(len(it) for comp in tpl for it in comp if isinstance(it, str))
            th[idx] = mu[A] + c + sum(lam[x] for x in ch)
        return max(th.values()), th


def rare_type_profile(L: Iterable[str], h: Typing) -> Dict[object, int]:
    """For each realised type m, the minimum length of a word of type m."""
    best: Dict[object, int] = {}
    for w in L:
        t = h(w)
        if t not in best or len(w) < best[t]:
            best[t] = len(w)
    return best
