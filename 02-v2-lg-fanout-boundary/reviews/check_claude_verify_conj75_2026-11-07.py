#!/usr/bin/env python3
"""check_claude_verify_conj75_2026-11-07.py  (standard library only)

Verifier-side check of reviews/claude_conj75_2026-11-07.md (README (197)).  No code of
check_claude_conj75_2026-11-07.py is used.  Routines for closedness, rank, condition (T)
(directly from Theorem 2.1 of the closure report), (N1)-(N5') and the level test are imported
from this repository's earlier verifier script check_claude_verify_prop73_2026-11-07.py
(written independently of the report scripts).

  V1  E1 = {(1,8,1),(2,3,4),(4,4,2),(8,1,1)}, P = (6,5): closed, det, (T) for {P} u E1,
      least theta of (N1)-(N5'), all points shorter than P, no positive level;  same for E2.
  V2  family F_n (3 <= n <= 16): the same, plus det = 29 - 50n, K_c = n+1, the Delta formula,
      and the set of admissible theta.
  V3  Lemma C (mu <= 3v theta + 3rv(theta + Delta)) on random CFGs with cycles (Parikh vectors
      enumerated up to a length bound) and acyclic CFGs with many low-c abc words.
Run: python3 -u check_claude_verify_conj75_2026-11-07.py
"""
import importlib.util, os, random, itertools
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('v73', os.path.join(here, 'check_claude_verify_prop73_2026-11-07.py'))
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)

def norm(p): return sum(p)

def full(name, F, P, thmax):
    Q = [(P[0], P[1], 0)] + list(F)
    th = v.N_conditions(F, P, thmax)
    ok = dict(closed=v.closed(F), rank=v.rank(F), T_viol=v.cond_T(Q), N_least_theta=th,
              all_short=all(norm(p) < norm(P) for p in F), level=v.find_level(F) is not None)
    print('  ', name, ok)
    return ok

def Delta(F, P, t): return max([0] + [norm(P) - f[0] - f[1] for f in F if f[2] <= t])

def V1():
    E1 = [(1, 8, 1), (2, 3, 4), (4, 4, 2), (8, 1, 1)]
    A, B, C, D = E1
    print('V1 det(B-A,C-A,D-A) =', v.det(v.vsub(B, A), v.vsub(C, A), v.vsub(D, A)), ' 2C-B =', v.vsub(v.vadd(C, C), B))
    full('E1', E1, (6, 5), 11)
    E2 = [(1, 1, 4), (2, 8, 1), (4, 4, 2), (8, 2, 1)]
    full('E2', E2, (6, 6), 12)

def family(n):
    return [(3*n + 2*k, 1 + 5*k, 2*(n - k)) for k in range(n)] + [(1, 10*n - 8, 1), (10*n - 4, 1, 1)], (5*n, 5*n + 1)

def V2(nmax=16):
    bad = []
    for n in range(3, nmax + 1):
        F, P = family(n)
        s0, s1 = F[0], F[1]; A, B = F[n], F[n + 1]
        d = v.det(v.vsub(s1, s0), v.vsub(A, s0), v.vsub(B, s0))
        r = dict(closed=v.closed(F), rank=v.rank(F), T=v.cond_T([(P[0], P[1], 0)] + F) == 0,
                 theta=v.N_conditions(F, P, 7), theta6=v.N_conditions(F, P, 6),
                 short=all(norm(p) < norm(P) for p in F), level=v.find_level(F) is not None,
                 det=d, Kc=len({p[2] for p in F}),
                 Delta=all(Delta(F, P, t) == max(8, 7 * (min(t, 2*n) // 2)) for t in range(1, 3*n)),
                 apex=v.vsub(v.vadd(F[n-1], F[n-1]), F[n-2]) == (P[0], P[1], 0))
        good = (r['closed'] and r['rank'] == 3 and r['T'] and r['theta'] == 7 and r['theta6'] is None
                and r['short'] and not r['level'] and r['det'] in (29 - 50*n, 50*n - 29)
                and r['Kc'] == n + 1 and r['Delta'] and r['apex'])
        if not good: bad.append((n, r))
    print('V2 family F_n, 3 <= n <=', nmax, ': not as claimed:', bad)

def V3(rng, trials=400, Lmax=14):
    st = dict(grammars=0, low_c_abc=0, VIOL=0, max_ratio=0.0)
    for _ in range(trials):
        G = v.reduce(v.rand_grammar(rng, rng.randint(2, 6)), 0)
        if G is None: continue
        S = v.parikh_upto(G, Lmax)[0]
        ab = [p for p in S if p[0] and p[1] and not p[2]]
        if not ab: continue
        mu = min(map(norm, ab))
        if mu > Lmax // 2: continue          # all abc words of length <= Lmax/2 known only up to Lmax: keep mu small
        vv, r, th = v.params(G)
        abc = [p for p in S if all(p)]
        # Delta needs all abc words with c <= th; words longer than Lmax are unknown, so only test when
        # the bound is already violated by the known part (a violation would need |W| large; with Delta from
        # the known part we get a LOWER estimate of Delta, so a non-violation is a valid test).
        for P in [p for p in ab if norm(p) == mu]:
            D = max([0] + [norm(P) - f[0] - f[1] for f in abc if f[2] <= th])
            st['grammars'] += 1
            if any(f[2] <= th for f in abc): st['low_c_abc'] += 1
            b = 3*vv*th + 3*r*vv*(th + D)
            if mu > b: st['VIOL'] += 1
            st['max_ratio'] = max(st['max_ratio'], round(mu / b, 3))
    print('V3 Lemma C on random CFGs (cycles allowed):', st)

if __name__ == '__main__':
    V1(); V2(); V3(random.Random(11))
