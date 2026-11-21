"""check_claude_S1_content_2026-11-09.py  (standard library only)

Run:  python3 -I check_claude_S1_content_2026-11-09.py      (about 1-2 minutes)

Numerical sanity checks for claude_S1_content_2026-11-09.md.  Not a proof.

Random minimal DFAs over {a,b} (<= 7 states).  The transition monoid of a minimal
DFA is the syntactic monoid, so x == y (same distribution) iff same transformation.
Typing: s = s_{U,2} (pure-a / contains b) or c = content (a / b / ab).
L in C_{1,tau}: no two distinct classes of the same type share a context.

Checks (for tau = c, and also tau = s):
 (S')  Lemma S': if z has non-empty distribution and a^p z == z (p >= 1),
       then N <= p   (N = shortest pure-a word).  Same for z a^p == z.
 (Pi)  Lemma Pi for every z of type ab (mixed): P0 = p0*N, and every
       F(l, r) = {f : l a^f z r in L} equals (f_min + p0 Z) cap N with f_min < p0.
 (R)   Lemma R in c, including the bad case (omega of type b, g = 0):
       W1 = a^x w w a^y, W2 = a^x w a^{d+y}, W3 = a^{x+d} w a^y in L, x + y >= 1
       ==> z0 := w a^d satisfies a^d z0 == z0 a^d and z0 z0 == a^{2d} z0.
       General case (g >= 1 or w mixed): z0 := w a^g, a^d z0 == z0 a^d == z0 z0.
 Also counts how often the bad case occurs and how often the s_{U,2}-version of
 Lemma R (w w == w a^d) actually FAILS in c (to show the fix is needed).
"""
import random, time

random.seed(20261109)

def minimize(nq, delta, F, q0):
    reach = {q0}; st = [q0]
    while st:
        q = st.pop()
        for ch in (0, 1):
            r = delta[q][ch]
            if r not in reach: reach.add(r); st.append(r)
    reach = sorted(reach)
    cls = {q: int(q in F) for q in reach}
    while True:
        sig = {q: (cls[q], cls[delta[q][0]], cls[delta[q][1]]) for q in reach}
        ids = {}; new = {}
        for q in reach: new[q] = ids.setdefault(sig[q], len(ids))
        if len(ids) == len(set(cls.values())): cls = new; break
        cls = new
    n = len(set(cls.values()))
    d2 = [[0, 0] for _ in range(n)]
    for q in reach: d2[cls[q]] = [cls[delta[q][0]], cls[delta[q][1]]]
    return n, d2, {cls[q] for q in reach if q in F}, cls[q0]

def build(n, dl, F, q0, typing, LIM=2500):
    A = tuple(dl[q][0] for q in range(n)); Bt = tuple(dl[q][1] for q in range(n))
    comp = lambda f, g: tuple(g[f[q]] for q in range(n))     # first f, then g
    idt = tuple(range(n))
    def ty(mask):                     # mask bit0 = a, bit1 = b
        return mask if typing == 'c' else (1 if mask == 1 else 2)
    elems = {(A, 1), (Bt, 2)}; frontier = list(elems)
    while frontier:
        nf = []
        for (f, m) in frontier:
            for (g, u) in ((A, 1), (Bt, 2)):
                key = (comp(f, g), m | u)
                if key not in elems: elems.add(key); nf.append(key)
        frontier = nf
        if len(elems) > LIM: return None
    J = {(p, q) for p in F for q in F}; st = list(J)
    pre = [[[] for _ in range(n)] for _ in range(2)]
    for q in range(n):
        for ch in (0, 1): pre[ch][dl[q][ch]].append(q)
    while st:
        p, q = st.pop()
        for ch in (0, 1):
            for p2 in pre[ch][p]:
                for q2 in pre[ch][q]:
                    if (p2, q2) not in J: J.add((p2, q2)); st.append((p2, q2))
    keys = list(elems)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            (f, t), (g, u) = keys[i], keys[j]
            if ty(t) != ty(u) or f == g: continue
            if any((f[s], g[s]) in J for s in range(n)): return None   # not C1
    return dict(A=A, comp=comp, idt=idt, elems=elems, J=J, F=F, q0=q0, n=n)

def run(typing, trials, B=30):
    st = dict(C1=0, withpure=0, S=0, Pi=0, ctx=0, R=0, Rbad=0, Rbad_naive_fail=0)
    viol = 0
    for _ in range(trials):
        nq = random.randint(2, 7)
        delta = [[random.randrange(nq), random.randrange(nq)] for _ in range(nq)]
        F = {q for q in range(nq) if random.random() < .4}
        if not F: continue
        n, dl, F2, q0 = minimize(nq, delta, F, 0)
        if n < 2: continue
        res = build(n, dl, F2, q0, typing)
        if res is None: continue
        st['C1'] += 1
        A, comp, J, idt = res['A'], res['comp'], res['J'], res['idt']
        apow = [idt]
        for _k in range(1, 4 * B): apow.append(comp(apow[-1], A))
        inL = lambda f: f[q0] in F2
        pure = [k for k in range(1, 3 * B) if inL(apow[k])]
        if not pure: continue
        st['withpure'] += 1
        N = pure[0]
        coreach = {p for (p, q) in J if p == q}
        nonempty = lambda f: any(f[s] in coreach for s in range(n))
        # contexts: left = any state reachable (all are, minimal DFA), right = element
        rights = [idt] + [f for (f, m) in list(res['elems'])[:80]]
        for (z, m) in res['elems']:
            if m == 1 or not nonempty(z): continue
            # (S')
            for p in range(1, B):
                if comp(apow[p], z) == z or comp(z, apow[p]) == z:
                    st['S'] += 1
                    if N > p: viol += 1; print(typing, "Lemma S' viol", N, p)
                    break
            # (Pi) for mixed z (in c) / any b-word (in s)
            if typing == 'c' and m != 3: continue
            P0 = [p for p in range(2 * B) if comp(apow[p], z) == z]
            p0 = P0[1] if len(P0) > 1 else None
            st['Pi'] += 1
            if p0 and P0 != list(range(0, 2 * B, p0)):
                viol += 1; print(typing, "P0 not p0N", P0)
            for s in range(n):
                for r in rights:
                    Fs = [f for f in range(2 * B) if r[z[apow[f][s]]] in F2]
                    if not Fs: continue
                    st['ctx'] += 1
                    if p0 is None:
                        if len(Fs) != 1: viol += 1; print(typing, "ctx viol (no period)", Fs)
                    else:
                        if Fs[0] >= p0 or Fs != list(range(Fs[0], 2 * B, p0)):
                            viol += 1; print(typing, "ctx viol", Fs, p0)
        # (R) Lemma R, words w = elements with b
        for (w, m) in res['elems']:
            if m == 1: continue
            for g in range(3):
                for nn in range(1, 4):
                    dd = g + nn
                    for x in range(3):
                        for y in range(3):
                            if x + g + y == 0 and m == 2: continue   # W1 in b+: trivial case
                            wgw = comp(comp(w, apow[g]), w)
                            W1 = inL(comp(comp(apow[x], wgw), apow[y]))
                            W2 = inL(comp(comp(apow[x], w), apow[dd + y]))
                            W3 = inL(comp(comp(apow[x + dd], w), apow[y]))
                            if not (W1 and W2 and W3): continue
                            st['R'] += 1
                            bad = (typing == 'c' and m == 2 and g == 0)
                            if bad:
                                st['Rbad'] += 1
                                if comp(w, w) != comp(w, apow[dd]): st['Rbad_naive_fail'] += 1
                                z0 = comp(w, apow[dd])
                                ok = (comp(apow[dd], z0) == comp(z0, apow[dd]) and
                                      comp(z0, z0) == comp(apow[2 * dd], z0))
                            else:
                                z0 = comp(w, apow[g])
                                ok = (comp(apow[dd], z0) == comp(z0, apow[dd]) == comp(z0, z0))
                            if not ok: viol += 1; print(typing, "Lemma R viol", g, nn, x, y, bad)
    print(f"[{typing}] C1 languages {st['C1']} (with a pure word {st['withpure']}); "
          f"Lemma S' instances {st['S']}; Lemma Pi classes {st['Pi']}, contexts {st['ctx']}; "
          f"Lemma R instances {st['R']} (bad case {st['Rbad']}, of which naive "
          f"w w == w a^d fails {st['Rbad_naive_fail']}); violations {viol}")
    return viol

if __name__ == "__main__":
    t0 = time.time()
    v = run('c', 40000) + run('s', 20000)
    print("TOTAL violations:", v, f"({time.time() - t0:.0f} s)")
