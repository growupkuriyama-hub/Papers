"""Check that the untyped H_n with two frames per zeta-category is a
2-context presentation of M_n (paragraph after Theorem 6.11, Astra B10).

Usage: python3 -I tools/check_untyped_two_frames.py [N]   (default N = 4)

For n = 2..N: builds L_n, M_n = L_n minus w*_n, the grammar H_n of
Proposition 4.2(b), and the contexts
  (E_i,1):      {c_i}
  (E_i,zeta):   {c_i, (p_i,q_i)}   (i < n)
  (E_n,zeta):   {(eps,eps)}
where c_i = ([^(n-i), ]^(n-i)) and (p_i,q_i) is the context of the last
E_i-node of w*_n.  Each set X_A = C_A^lhd (relative to M_n) is computed over
all factors of words of M_n (a word outside these factors has no context
accepting it), and the script checks that
  (1) X_(E_i,1) = L(G_n,E_i), X_(E_i,zeta) = L(G_n,E_i) minus {w*_i},
      X_(E_n,zeta) = M_n;
  (2) every production maps the X-sets of its children into the X-set of its
      left-hand side (pre-fixed point), and X of the initial symbol is in M_n;
  (3) it prints sum |alpha|, the maximal context length ell, and 2^(n-2).
A finite check, not a proof.  Exit code 0 iff all checks pass.
"""
import sys
from itertools import product

A, LB, RB, LM, RM = "a", "[", "]", "<", ">"   # [ ] binary, < > mark


def levels(n):
    E = [{A}]
    for i in range(1, n + 1):
        prev = E[-1]
        E.append({LB + x + y + RB for x in prev for y in prev} |
                 {LM + x + RM for x in prev})
    return E


def wstar(i):
    w = A
    for _ in range(i):
        w = LB + w + w + RB
    return w


def marked(x):
    return LM in x


def main(N):
    ok = True
    for n in range(2, N + 1):
        E = levels(n)
        Ln = E[n]
        Mn = Ln - {wstar(n)}
        factors = set()
        for m in Mn:
            for i in range(len(m)):
                for j in range(i + 1, len(m) + 1):
                    factors.add(m[i:j])
        wn = wstar(n)
        ctx = {}
        for i in range(n):
            c = (LM * (n - i), RM * (n - i))
            ctx[(i, "1")] = [c]
            if i >= 1:
                wi = wstar(i)
                k = wn.rfind(wi)          # last E_i-node of w*_n
                ctx[(i, "z")] = [c, (wn[:k], wn[k + len(wi):])]
        ctx[(n, "z")] = [("", "")]
        X = {A_: {x for x in factors if all(u + x + v in Mn for u, v in C)}
             for A_, C in ctx.items()}
        # (1)
        for (i, t), S in X.items():
            want = E[i] if t == "1" else (Mn if i == n else E[i] - {wstar(i)})
            if S != want:
                print(f"n={n}: X({i},{t}) differs from the expected set")
                ok = False
        # productions of H_n
        prods = [((0, "1"), [A])]
        for i in range(1, n):
            prods.append(((i, "1"), [LB, (i - 1, "1"), (i - 1, "1"), RB]))
        for i in range(1, n + 1):
            kids = [t for t in ("1", "z") if (i - 1, t) in X]
            for a_, b_ in product(kids, kids):
                if (a_, b_) != ("1", "1"):
                    prods.append(((i, "z"), [LB, (i - 1, a_), (i - 1, b_), RB]))
            for a_ in kids:
                prods.append(((i, "z"), [LM, (i - 1, a_), RM]))
        # (2)
        for lhs, rhs in prods:
            sets = [[s] if isinstance(s, str) else X[s] for s in rhs]
            for parts in product(*sets):
                if "".join(parts) not in X[lhs]:
                    print(f"n={n}: production for {lhs} leaves X")
                    ok = False
                    break
        if not X[(n, "z")] <= Mn:
            ok = False
        sum_alpha = sum(len(r) for _, r in prods)
        ell = max(len(u) + len(v) for C in ctx.values() for u, v in C)
        print(f"n={n}: productions {len(prods)} (6n-4={6*n-4}), "
              f"sum|alpha|={sum_alpha} (<= 4(6n-4)={4*(6*n-4)}), "
              f"ell={ell} (3*2^n-6={3*2**n-6}), 2^(n-2)={2**(n-2)}")
        if len(prods) != 6 * n - 4 or ell != 3 * 2 ** n - 6:
            ok = False
    print("all pass" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1]) if len(sys.argv) > 1 else 4))
