#!/usr/bin/env python3
"""R15 (direction C) -- finite checks.  Python 3 standard library only, no network.

Run:  python3 -I run_all.py      (exit code 0 iff every check passes)

All output is deterministic (no use of hash ordering in printed results; random
grammars come from random.Random with fixed seeds).

Sections
  [A] dimension (Strahler bound of all derivation trees): SCC criterion + Kleene
      iteration; examples of C1 (rank one, ultralinear, nonexpansive, expansive)
  [B] C2 inequality checked label by label on many grammars (fan-out 1 and 2):
      shortest typed yield <= l_max * Nd(h, m(X), r), where m(X) is the least
      Strahler number of a derivation of the label X and h the number of labels;
      typed refinement has the same dimension as the grammar
  [C] the family G_{n,b}: size, thickness, dimension, unique c-free word and its
      length, against the closed formulas of the report
  [D] Clark--Eyraud substitutability of L_{n,b}: exact brute force on small n,b
      and the parser lemmas (determinism, weight, injectivity on reachable stacks)
  [E] fan-out two: the explicit two-hole Rect violation (power transfer) for
      L_{n,b}, n>=4
  [F] numeric table of the lower bound against (||G|| theta)^((b+1)/2)
"""
import sys
import random
import itertools
from math import comb

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("  FAIL:", msg)
    return cond


INF = float("inf")

# ---------------------------------------------------------------------------
# General MCFG representation
#   rule = (lhs, children(tuple), template(tuple of components))
#   component = tuple of items; item = terminal (str, len 1) or (j, k) variable
# ---------------------------------------------------------------------------


class Grammar:
    def __init__(self, fan, rules, start):
        self.fan = dict(fan)
        self.rules = list(rules)
        self.start = start
        self.V = sorted(self.fan, key=repr)

    def letters(self, rule):
        return sum(1 for comp in rule[2] for it in comp if isinstance(it, str))

    def size(self):
        s = len(self.fan)
        for (A, ch, tpl) in self.rules:
            s += 1 + len(ch) + sum(len(c) for c in tpl)
        return s

    def rank(self):
        return max((len(r[1]) for r in self.rules), default=0)


def check_good(G):
    """epsilon-free, nondeleting, nonpermuting, nonmerging, arity-consistent"""
    for (A, ch, tpl) in G.rules:
        if len(tpl) != G.fan[A]:
            return False
        seen = []
        for comp in tpl:
            if len(comp) == 0:
                return False
            prev = None
            for it in comp:
                if not isinstance(it, str):
                    j, k = it
                    if k >= G.fan[ch[j]]:
                        return False
                    if prev is not None and not isinstance(prev, str) and prev[0] == j and prev[1] + 1 == k:
                        return False  # merging
                    seen.append(it)
                prev = it
        for j, B in enumerate(ch):
            ks = [k for (jj, k) in seen if jj == j]
            if ks != list(range(G.fan[B])):
                return False  # deleting or permuting or duplicated
    return True


def shortest_yields(G):
    short = {A: INF for A in G.fan}
    changed = True
    while changed:
        changed = False
        for (A, ch, tpl) in G.rules:
            c = G.letters((A, ch, tpl)) + sum(short[B] for B in ch)
            if c < short[A]:
                short[A] = c
                changed = True
    return short


def shortest_contexts(G, short):
    ctx = {A: INF for A in G.fan}
    ctx[G.start] = 0
    changed = True
    while changed:
        changed = False
        for (A, ch, tpl) in G.rules:
            if ctx[A] == INF:
                continue
            base = ctx[A] + G.letters((A, ch, tpl)) + sum(short[B] for B in ch)
            for j, B in enumerate(ch):
                c = base - short[B]
                if c < ctx[B]:
                    ctx[B] = c
                    changed = True
    return ctx


def thickness(G):
    short = shortest_yields(G)
    ctx = shortest_contexts(G, short)
    th = 0
    for (A, ch, tpl) in G.rules:
        th = max(th, ctx[A] + G.letters((A, ch, tpl)) + sum(short[B] for B in ch))
    return max(1, th)


def is_reduced(G):
    short = shortest_yields(G)
    ctx = shortest_contexts(G, short)
    return all(short[A] < INF and ctx[A] < INF for A in G.fan)


def strahler_combine(vals):
    if not vals:
        return 0
    m = max(vals)
    return m + 1 if sum(1 for v in vals if v == m) >= 2 else m


def sccs(nodes, edges):
    """iterative Tarjan; returns dict node -> scc id"""
    index, low, onst, st, comp = {}, {}, set(), [], {}
    counter = [0]
    cid = [0]
    for root in nodes:
        if root in index:
            continue
        stack = [(root, iter(edges.get(root, ())))]
        index[root] = low[root] = counter[0]
        counter[0] += 1
        st.append(root)
        onst.add(root)
        while stack:
            v, it = stack[-1]
            advanced = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = counter[0]
                    counter[0] += 1
                    st.append(w)
                    onst.add(w)
                    stack.append((w, iter(edges.get(w, ()))))
                    advanced = True
                    break
                elif w in onst:
                    low[v] = min(low[v], index[w])
            if advanced:
                continue
            stack.pop()
            if stack:
                low[stack[-1][0]] = min(low[stack[-1][0]], low[v])
            if low[v] == index[v]:
                while True:
                    w = st.pop()
                    onst.discard(w)
                    comp[w] = cid[0]
                    if w == v:
                        break
                cid[0] += 1
    return comp


def dimension(nodes, rules, start):
    """sup of Strahler numbers of derivation trees (reduced grammar assumed).
    rules: list of (lhs, children).  Returns INF if expansive."""
    edges = {}
    for (A, ch) in rules:
        edges.setdefault(A, [])
        for B in ch:
            edges[A].append(B)
    comp = sccs(nodes, edges)
    for (A, ch) in rules:
        if sum(1 for B in ch if comp[B] == comp[A]) >= 2:
            return INF
    val = {A: -1 for A in nodes}  # -1 = no tree found yet
    changed = True
    while changed:
        changed = False
        for (A, ch) in rules:
            if any(val[B] < 0 for B in ch):
                continue
            v = strahler_combine([val[B] for B in ch])
            if v > val[A]:
                val[A] = v
                changed = True
    return max(val.values())


def dim_of(G):
    return dimension(G.V, [(A, ch) for (A, ch, t) in G.rules], G.start)


# ---------------------------------------------------------------------------
# typings: finite monoid with identity 'e' (fresh identity for the empty word)
# ---------------------------------------------------------------------------


class Typing:
    def __init__(self, name, letter_type, mul):
        self.name = name
        self.lt = letter_type
        self.mul = mul  # function (x,y)->z; 'e' is the identity

    def prod(self, xs):
        r = "e"
        for x in xs:
            r = x if r == "e" else (r if x == "e" else self.mul(r, x))
        return r


def u1_mul(x, y):
    return "1" if (x == "1" and y == "1") else "z"


S_U3 = Typing("s_U3", {"a": "1", "b": "1", "c": "z"}, u1_mul)


def content_mul(x, y):
    return "".join(sorted(set(x) | set(y)))


C_ABC = Typing("c_abc", {"a": "a", "b": "b", "c": "c"}, content_mul)


def typed_labels(G, s):
    """realized labels X=(A, typevector) with shortest total yield length and
    least Strahler number over derivations of X; also the realized typed rules."""
    dist, mst = {}, {}
    trules = set()
    changed = True
    while changed:
        changed = False
        bylhs = {}
        for X in dist:
            bylhs.setdefault(X[0], []).append(X)
        for X in bylhs:
            bylhs[X].sort(key=repr)
        for rule in G.rules:
            A, ch, tpl = rule
            pools = [bylhs.get(B, []) for B in ch]
            if any(len(p) == 0 for p in pools):
                continue
            lets = G.letters(rule)
            for combo in itertools.product(*pools):
                tv = []
                for comp in tpl:
                    xs = []
                    for it in comp:
                        if isinstance(it, str):
                            xs.append(s.lt[it])
                        else:
                            j, k = it
                            xs.append(combo[j][1][k])
                    tv.append(s.prod(xs))
                X = (A, tuple(tv))
                d = lets + sum(dist[Y] for Y in combo)
                m = strahler_combine([mst[Y] for Y in combo])
                tr = (X, tuple(combo))
                if tr not in trules:
                    trules.add(tr)
                    changed = True
                if X not in dist or d < dist[X]:
                    dist[X] = d
                    changed = True
                if X not in mst or m < mst[X]:
                    mst[X] = m
                    changed = True
    return dist, mst, trules


def Nd(h, b, r):
    """max number of nodes of a tree of height <= h (h nodes on a path),
    rank <= r, Strahler <= b"""
    return sum(comb(i, j) * (r - 1) ** j for i in range(h) for j in range(min(i, b) + 1))


def c2_check(G, s, label):
    """check, for every realized label X: dist[X] <= lmax * Nd(h, m(X), r)."""
    dist, mst, trules = typed_labels(G, s)
    h = len(dist)
    r = max(1, G.rank())
    lmax = max(G.letters(rule) for rule in G.rules)
    th = thickness(G)
    ok = True
    worst = 0.0
    for X in sorted(dist, key=repr):
        bound = lmax * Nd(h, mst[X], r)
        if dist[X] > bound:
            ok = False
        worst = max(worst, dist[X] / bound)
    # typed refinement (trimmed) dimension
    roots = [X for X in dist if X[0] == G.start]
    reach = set(roots)
    stack = list(roots)
    tr_by = {}
    for (X, combo) in trules:
        tr_by.setdefault(X, []).append(combo)
    while stack:
        X = stack.pop()
        for combo in tr_by.get(X, []):
            for Y in combo:
                if Y not in reach:
                    reach.add(Y)
                    stack.append(Y)
    tnodes = sorted(reach, key=repr)
    trs = [(X, combo) for (X, combo) in sorted(trules, key=repr) if X in reach]
    tdim = dimension(tnodes, trs, None)
    gdim = dim_of(G)
    check(ok, f"C2 inequality fails for {label} under {s.name}")
    check(tdim == gdim, f"typed refinement dimension {tdim} != dim(G) {gdim} for {label}")
    check(lmax <= th, f"l_max > theta for {label}")
    return dict(h=h, r=r, lmax=lmax, theta=th, dim=gdim, tdim=tdim,
                ttyp=max(dist.values()), worst=worst, maxmst=max(mst.values()))


# ---------------------------------------------------------------------------
# CFG helper: rhs list of symbols -> MCFG rule of fan-out one
# ---------------------------------------------------------------------------


def cfg(rules_rhs, start):
    """rules_rhs: list of (A, [symbols]) where nonterminals are non-str or str
    longer than one char; terminals are single-char str"""
    fan = {}
    rules = []
    for (A, rhs) in rules_rhs:
        assert not (isinstance(A, str) and len(A) == 1), "nonterminal names must not be letters"
        fan[A] = 1
    for (A, rhs) in rules_rhs:
        ch = []
        comp = []
        for x in rhs:
            if isinstance(x, str) and len(x) == 1:
                comp.append(x)
            else:
                ch.append(x)
                comp.append((len(ch) - 1, 0))
        rules.append((A, tuple(ch), (tuple(comp),)))
    return Grammar(fan, rules, start)


# ---------------------------------------------------------------------------
# The family G_{n,b}
# ---------------------------------------------------------------------------


def lev(t, n):
    return (t + n - 1) // n - 1  # ceil(t/n)-1 for t>=1


def anc(t, n):
    return lev(t, n) * n


def family(n, b):
    N = (b + 1) * n
    R = [(("E", 0), ["a"])]
    for t in range(1, N + 1):
        R.append((("E", t), ["c", ("E", t - 1), "c"]))
        if lev(t, n) == 0:
            R.append((("E", t), ["b", ("E", t - 1), "b"]))
        else:
            R.append((("E", t), ["b", ("E", anc(t, n)), ("E", t - 1), "b"]))
    return cfg(R, ("E", N)), N


def family_language(n, b):
    N = (b + 1) * n
    L = [{"a"}]
    for t in range(1, N + 1):
        S = {"c" + w + "c" for w in L[t - 1]}
        if lev(t, n) == 0:
            S |= {"b" + w + "b" for w in L[t - 1]}
        else:
            A = L[anc(t, n)]
            S |= {"b" + u + v + "b" for u in A for v in L[t - 1]}
        L.append(S)
    return L


def W_word(n, b):
    N = (b + 1) * n
    W = ["a"]
    for t in range(1, N + 1):
        if lev(t, n) == 0:
            W.append("b" + W[t - 1] + "b")
        else:
            W.append("b" + W[anc(t, n)] + W[t - 1] + "b")
    return W[N]


# stack machine (parser) for L_{n,b}: symbols ('E',t), ('B',t) = b-hat, ('C',t) = c-hat


def moves(sym, x, n):
    """returns the replacement (tuple, top first) or None"""
    kind, t = sym
    if kind == "E":
        if t == 0:
            return () if x == "a" else None
        if x == "c":
            return (("E", t - 1), ("C", t))
        if x == "b":
            if lev(t, n) == 0:
                return (("E", t - 1), ("B", t))
            return (("E", anc(t, n)), ("E", t - 1), ("B", t))
        return None
    if kind == "B":
        return () if x == "b" else None
    if kind == "C":
        return () if x == "c" else None


def run(word, stack, n):
    st = list(stack)
    for x in word:
        if not st:
            return None
        rep = moves(st[0], x, n)
        if rep is None:
            return None
        st = list(rep) + st[1:]
    return tuple(st)


def member(word, n, b):
    N = (b + 1) * n
    return run(word, (("E", N),), n) == ()


def weight(st):
    return sum(4 ** t if k == "E" else 1 for (k, t) in st)


# ---------------------------------------------------------------------------
# exact Clark--Eyraud substitutability for a finite language
# ---------------------------------------------------------------------------


def ce_substitutable(L):
    parent = {}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    edges = 0
    for w in sorted(L):
        m = len(w)
        for i in range(m):
            for j in range(i + 1, m + 1):
                f = ("f", w[i:j])
                c = ("c", w[:i], w[j:])
                if f not in parent:
                    parent[f] = f
                if c not in parent:
                    parent[c] = c
                union(f, c)
                edges += 1
    nf, nc, ne = {}, {}, {}
    for x in parent:
        r = find(x)
        if x[0] == "f":
            nf[r] = nf.get(r, 0) + 1
        else:
            nc[r] = nc.get(r, 0) + 1
    for w in L:
        m = len(w)
        for i in range(m):
            for j in range(i + 1, m + 1):
                r = find(("f", w[i:j]))
                ne[r] = ne.get(r, 0) + 1
    for r in nf:
        if ne.get(r, 0) != nf[r] * nc.get(r, 0):
            return False, edges
    return True, edges


# ---------------------------------------------------------------------------
# random good grammars (fan-out <= 2, rank <= 2) for section [B]
# ---------------------------------------------------------------------------


def random_grammar(rng, nv, nrules, alphabet="abc", maxfan=2, maxrank=2):
    names = ["S"] + [f"N{i}" for i in range(1, nv)]
    fan = {"S": 1}
    for x in names[1:]:
        fan[x] = rng.randint(1, maxfan)
    rules = []
    # guarantee productivity: one constant rule per nonterminal
    for A in names:
        comps = tuple(tuple(rng.choice(alphabet) for _ in range(rng.randint(1, 2)))
                      for _ in range(fan[A]))
        rules.append((A, (), comps))
    for _ in range(nrules):
        A = rng.choice(names)
        r = rng.randint(1, maxrank)
        ch = tuple(rng.choice(names[1:] if len(names) > 1 else names) for _ in range(r))
        # variable sequence respecting per-child order, random interleaving
        seqs = [[(j, k) for k in range(fan[B])] for j, B in enumerate(ch)]
        order = []
        ptr = [0] * r
        total = sum(len(s_) for s_ in seqs)
        while len(order) < total:
            j = rng.choice([jj for jj in range(r) if ptr[jj] < len(seqs[jj])])
            order.append(seqs[j][ptr[j]])
            ptr[j] += 1
        # split into fan[A] nonempty components (pad with terminals)
        d0 = fan[A]
        cuts = sorted(rng.sample(range(1, total), d0 - 1)) if total >= d0 and d0 > 1 else []
        parts = []
        prev = 0
        for c in cuts:
            parts.append(order[prev:c])
            prev = c
        parts.append(order[prev:])
        while len(parts) < d0:
            parts.append([])
        comps = []
        for p in parts:
            comp = []
            if rng.random() < 0.5:
                comp.append(rng.choice(alphabet))
            last = None
            for it in p:
                if last is not None and last[0] == it[0] and last[1] + 1 == it[1]:
                    comp.append(rng.choice(alphabet))  # nonmerging
                comp.append(it)
                last = it
            if rng.random() < 0.5 or not comp:
                comp.append(rng.choice(alphabet))
            comps.append(tuple(comp))
        rules.append((A, ch, tuple(comps)))
    G = Grammar(fan, rules, "S")
    # trim unreachable nonterminals
    short = shortest_yields(G)
    ctx = shortest_contexts(G, short)
    keep = {A for A in fan if ctx[A] < INF and short[A] < INF}
    rules2 = [rl for rl in rules if rl[0] in keep and all(B in keep for B in rl[1])]
    G2 = Grammar({A: fan[A] for A in keep}, rules2, "S")
    return G2


# ===========================================================================


def section_A():
    print("[A] dimension: examples of C1")
    # rank one / linear: dim 0
    G = cfg([("S0", ["a", "S0", "b"]), ("S0", ["c"])], "S0")
    check(dim_of(G) == 0, "linear grammar should have dim 0")
    # expansive: S -> SS | a
    G = cfg([("S0", ["S0", "S0"]), ("S0", ["a"])], "S0")
    check(dim_of(G) == INF, "S->SS|a should be expansive")
    # 02-v3 doubling family L_n: dim n
    for n in range(1, 7):
        R = [("S0", [("E", n)]), (("E", 0), ["a"])]
        for i in range(1, n + 1):
            R.append((("E", i), ["b", ("E", i - 1), ("E", i - 1), "b"]))
            R.append((("E", i), ["c", ("E", i - 1), "c"]))
        check(dim_of(cfg(R, "S0")) == n, f"02-v3 family n={n} should have dim n")
    # ultralinear with levels A0={T}, A1={S}: S -> aSb | TT ; T -> cTd | e   (dim <= 1)
    G = cfg([("S0", ["a", "S0", "b"]), ("S0", ["T0", "T0"]), ("T0", ["c", "T0", "d"]), ("T0", ["e"])], "S0")
    check(dim_of(G) == 1, "ultralinear level-1 example should have dim 1")
    # nonexpansive, not ultralinear: S -> a S T | a ; T -> b T c | b c   (dim 1)
    G = cfg([("S0", ["a", "S0", "T0"]), ("S0", ["a"]), ("T0", ["b", "T0", "c"]), ("T0", ["b", "c"])], "S0")
    check(dim_of(G) == 1, "nonexpansive example should have dim 1")
    # expansive through a cycle: S -> A ; A -> B B | a ; B -> A
    G = cfg([("S0", ["A0"]), ("A0", ["B0", "B0"]), ("A0", ["a"]), ("B0", ["A0"])], "S0")
    check(dim_of(G) == INF, "A->BB, B->A should be expansive")
    # Kleene iteration vs brute force on random acyclic CFGs (enumerate all trees)
    rng = random.Random(15)
    nchk = 0
    for trial in range(300):
        k = rng.randint(2, 5)
        names = [f"X{i}" for i in range(k)]
        R = [(names[0], ["a"])]
        for i in range(1, k):
            R.append((names[i], ["a"]))
            for _ in range(rng.randint(1, 3)):
                r = rng.randint(1, 3)
                R.append((names[i], [rng.choice(names[:i]) for _ in range(r)]))
        G = cfg(R, names[-1])
        # brute force: sup St over all trees, by recursion over acyclic structure
        memo = {}

        def allst(A):
            if A in memo:
                return memo[A]
            vals = set()
            for (B, ch, tpl) in G.rules:
                if B != A:
                    continue
                pools = [allst(C) for C in ch]
                for combo in itertools.product(*pools):
                    vals.add(strahler_combine(list(combo)))
            memo[A] = vals
            return vals
        if not is_reduced(G):
            continue
        bf = max(allst(names[-1]))
        check(dim_of(G) == bf, f"dimension mismatch on random acyclic grammar {trial}")
        nchk += 1
    print(f"  examples OK; Kleene dimension = brute force on {nchk} random acyclic CFGs")


def section_B():
    print("[B] C2 inequality label by label; dim(typed refinement) = dim(G)")
    rows = []
    # family G_{n,b}
    for (n, b) in [(1, 0), (2, 0), (3, 1), (2, 2), (2, 3), (3, 2), (4, 1)]:
        G, N = family(n, b)
        for s in (S_U3, C_ABC):
            info = c2_check(G, s, f"G_{{{n},{b}}}")
            rows.append((f"G_{n},{b}", s.name, info))
        dist, mst, _ = typed_labels(G, S_U3)
        X = (("E", N), ("1",))
        check(dist.get(X) == len(W_word(n, b)), f"t_typ label (E_N,1) != |W_N| for n={n},b={b}")
        check(mst.get(X) == b, f"least Strahler of (E_N,1) != b for n={n},b={b}")
    # 02-v3 doubling family: label (E_n,1) needs Strahler n
    for n in range(1, 6):
        R = [("S0", [("E", n)]), (("E", 0), ["a"])]
        for i in range(1, n + 1):
            R.append((("E", i), ["b", ("E", i - 1), ("E", i - 1), "b"]))
            R.append((("E", i), ["c", ("E", i - 1), "c"]))
        G = cfg(R, "S0")
        info = c2_check(G, S_U3, f"02v3_L{n}")
        rows.append((f"02v3_L{n}", "s_U3", info))
        dist, mst, _ = typed_labels(G, S_U3)
        check(mst[("S0", ("1",))] == n, "02-v3 rare label should need Strahler n")
        check(dist[("S0", ("1",))] == 3 * 2 ** n - 2, "02-v3 rare word length")
    # random good grammars of fan-out <= 2
    rng = random.Random(2026)
    nrand = nfan2 = nrank2 = nfin = 0
    for trial in range(120):
        G = random_grammar(rng, rng.randint(2, 4), rng.randint(2, 5))
        if "S" not in G.fan or not check_good(G) or not is_reduced(G):
            continue
        if dim_of(G) == INF:
            # dimension is infinite; the label-wise inequality still uses m(X)
            pass
        for s in (S_U3, C_ABC):
            dist, mst, trules = typed_labels(G, s)
            h = len(dist)
            r = max(1, G.rank())
            lmax = max(G.letters(rule) for rule in G.rules)
            for X in dist:
                check(dist[X] <= lmax * Nd(h, mst[X], r), f"C2 label inequality, random grammar {trial}")
            if dim_of(G) < INF:
                c2_check(G, s, f"random{trial}")
        nrand += 1
        if any(d == 2 for d in G.fan.values()):
            nfan2 += 1
        if G.rank() >= 2:
            nrank2 += 1
        if dim_of(G) < INF:
            nfin += 1
    for (g, s, info) in rows:
        print(f"  {g:10s} {s:6s} h={info['h']:4d} r={info['r']} dim={info['dim']} "
              f"tdim={info['tdim']} lmax={info['lmax']} theta={info['theta']:4d} "
              f"t_typ={info['ttyp']:6d} max(dist/bound)={info['worst']:.4f}")
    print(f"  random reduced good grammars checked: {nrand} (with a fan-out-2 nonterminal: {nfan2}, "
          f"rank 2: {nrank2}, finite dimension: {nfin}); label inequality checked under s_U3 and c_abc")


def section_C():
    print("[C] family G_{n,b}: size, thickness, dimension, unique c-free word")
    for b in range(0, 5):
        for n in range(1, 8):
            G, N = family(n, b)
            check(check_good(G) and is_reduced(G), f"G_{n},{b} not reduced good")
            sz = G.size()
            check(sz == (13 * b + 11) * n + 3, f"size formula n={n} b={b}: {sz}")
            th = thickness(G)
            exp = (4 * b + 2) * n + 2 if b >= 1 else 2 * n + 1
            check(th == exp, f"thickness formula n={n} b={b}: {th} vs {exp}")
            check(dim_of(G) == b, f"dimension n={n} b={b}")
            W = W_word(n, b)
            check(len(W) == (n + 1) ** b * (2 * n + 3) - 2, f"|W| formula n={n} b={b}")
            check(member(W, n, b), f"W not accepted n={n} b={b}")
            check(W.startswith("b" * (n + b) + "a" + "b" * n), f"W prefix n={n} b={b}")
            # the c-free subgrammar has a single tree, of Strahler number b
            Gc = Grammar(G.fan, [rl for rl in G.rules if "c" not in rl[2][0]], G.start)
            check(dim_of(Gc) == b, f"c-free tree Strahler n={n} b={b}")
            check(sum(1 for rl in G.rules if "c" not in rl[2][0]) == N + 1,
                  "exactly one c-free rule per nonterminal")
    # explicit enumeration on small cases: unique c-free word, membership = parser
    for (n, b) in [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (3, 1), (1, 2), (1, 3)]:
        L = family_language(n, b)[-1]
        cfree = [w for w in L if "c" not in w]
        check(cfree == [W_word(n, b)], f"unique c-free word n={n} b={b}")
        check(all(member(w, n, b) for w in L), f"parser rejects a word n={n} b={b}")
        # parser rejects all other words of the same lengths over {a,b,c}? sample
        rng = random.Random(n * 100 + b)
        for _ in range(2000):
            w = rng.choice(sorted(L))
            i = rng.randrange(len(w))
            w2 = w[:i] + rng.choice("abc") + w[i + 1:]
            check(member(w2, n, b) == (w2 in L), f"parser/membership disagree n={n} b={b}")
    print("  formulas: ||G||=(13b+11)n+3, theta=(4b+2)n+2 (b>=1) / 2n+1 (b=0), dim=b, "
          "|W|=(n+1)^b(2n+3)-2  -- verified for 0<=b<=4, 1<=n<=7")


def section_D():
    print("[D] Clark--Eyraud substitutability of L_{n,b}")
    for (n, b) in [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (1, 1), (2, 1), (1, 2), (1, 3), (3, 1)]:
        L = family_language(n, b)[-1]
        ok, edges = ce_substitutable(L)
        check(ok, f"L_{n},{b} not CE-substitutable")
        print(f"  n={n} b={b}: |L|={len(L):5d}  factor occurrences={edges:8d}  CE-substitutable={ok}")
    # parser lemmas on reachable stacks
    for (n, b) in [(1, 1), (2, 1), (3, 1), (2, 2), (1, 3), (3, 2), (4, 1), (2, 3)]:
        N = (b + 1) * n
        start = (("E", N),)
        seen = {start}
        frontier = [start]
        while frontier:
            nxt = []
            for st in frontier:
                if not st:
                    continue
                for x in "abc":
                    rep = moves(st[0], x, n)
                    if rep is None:
                        continue
                    st2 = tuple(rep) + st[1:]
                    check(weight(st2) < weight(st), "weight does not decrease")
                    if st2 not in seen:
                        seen.add(st2)
                        nxt.append(st2)
            frontier = nxt
        # injectivity of every letter on reachable stacks
        for x in "abc":
            img = {}
            for st in seen:
                if not st:
                    continue
                rep = moves(st[0], x, n)
                if rep is None:
                    continue
                st2 = tuple(rep) + st[1:]
                check(st2 not in img, f"letter {x} not injective on reachable stacks n={n} b={b}")
                img[st2] = st
        # determinism: at most one move per (top, letter): structural; also no move from empty
        print(f"  n={n} b={b}: reachable stacks={len(seen):6d}; weight decreases; letters injective")


def section_E():
    print("[E] fan-out two: explicit two-hole Rect violation in L_{n,b} (n>=4)")
    for b in range(0, 4):
        for n in range(4, 10):
            W = W_word(n, b)
            pre = "b" * (n + b) + "a" + "b" * n
            assert W.startswith(pre)
            Rp = W[len(pre):]              # R' : W = b^{n+b} a b^n R'
            # shared context E0 = b^b [1] b [2] a b^n R'
            x = ("b", "b" * (n - 2))
            xp = ("bb", "b" * (n - 3))
            E0 = ("b" * b, "b", "a" + "b" * n + Rp)
            E1 = ("b", "b" * (n + b - 2) + "a" + "bb", Rp)

            def fill(E, t):
                return E[0] + t[0] + E[1] + t[1] + E[2]
            w1, w2, w3, w4 = fill(E0, x), fill(E0, xp), fill(E1, x), fill(E1, xp)
            check(w1 == W and w2 == W and w3 == W, "Rect words 1-3 should equal W")
            check(len(E1[1]) > 0 and len(E0[1]) > 0, "middle of two-hole context must be nonempty")
            check(all(len(c) > 0 for c in x + xp), "tuple components nonempty")
            check(not member(w4, n, b), f"fourth word should be rejected n={n} b={b}")
            check("c" not in w4 and len(w4) == len(W) and sorted(w4) == sorted(W),
                  "fourth word has the same Parikh vector and no c")
        print(f"  b={b}: for n=4..9, x=(b,b^(n-2)), x'=(bb,b^(n-3)), types (1,1)/(1,1); "
              f"E0,E1 accept x, E0 accepts x', E1 rejects x'")


def section_F():
    print("[F] lower bound table: |W|+1 versus (||G|| theta)^((b+1)/2)")
    print("   b    n      ||G||    theta          |W|+1   log(|W|+1)/log(||G|| theta)")
    import math
    for b in range(1, 6):
        for n in (10, 100, 1000, 10000):
            G_size = (13 * b + 11) * n + 3
            th = (4 * b + 2) * n + 2
            W1 = (n + 1) ** b * (2 * n + 3) - 1
            ratio = math.log(W1) / math.log(G_size * th)
            print(f"  {b:2d} {n:6d} {G_size:9d} {th:8d} {W1:14.4g}   {ratio:.4f}")
        # the inequality |W|+1 >= (||G|| theta/((13b+14)(4b+4)))^((b+1)/2) for n >= 1
        for n in range(1, 200):
            G_size = (13 * b + 11) * n + 3
            th = (4 * b + 2) * n + 2
            W1 = (n + 1) ** b * (2 * n + 3) - 1
            lhs = W1
            rhs = (G_size * th / ((13 * b + 14) * (4 * b + 4))) ** ((b + 1) / 2)
            check(lhs >= rhs, f"lower bound inequality b={b} n={n}")
    print("  inequality |W|+1 >= (||G||*theta/((13b+14)(4b+4)))^((b+1)/2): checked 1<=b<=5, 1<=n<200")


def main():
    section_A()
    section_B()
    section_C()
    section_D()
    section_E()
    section_F()
    print()
    if FAIL:
        print(f"RESULT: {len(FAIL)} FAILURES")
        return 1
    print("RESULT: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
