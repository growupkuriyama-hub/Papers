#!/usr/bin/env python3
"""Uniform obstruction for the CFG doubling family at higher arity.

For any k,l >= 0 and n >= max(3,k+l+1), the original L_n fails
(2,h_{Sigma}^{k,l})-tuple substitutability; the same witness works for
its product with the two-element semilattice typing h_U.

This script verifies the algebraic formulas and finite instances.
The general theorem is proved symbolically in main.tex; a finite test is
NOT the proof.

Run: python3 revision/check_fixed_window_general_obstruction.py
"""
from __future__ import annotations

def wstar(n: int) -> str:
    word = "a"
    for _ in range(n):
        word = "⌊" + word + word + "⌋"
    return word

def window(word: str, k: int, ell: int) -> tuple:
    m0 = max(1, k + ell)
    if len(word) < m0:
        return ("short", word)
    return ("long", word[:k], word[-ell:] if ell else "")

def semilattice(word: str) -> int:
    return int("⌈" in word or "⌉" in word)

def check_one(k: int, ell: int, n: int) -> None:
    assert k >= 0 and ell >= 0
    assert n >= max(3, k + ell + 1)
    B = "⌊" * (n - 1)
    prev = wstar(n - 1)
    assert prev.startswith(B + "a")
    R = prev[len(B) + 1:]
    assert len(B) >= k + ell and len(R) >= k + ell

    x = (B, R + B + "a" + R)
    y = (B + "a" + R + B, R)
    E = lambda z: "⌊" + z[0] + "a" + z[1] + "⌋"
    F = lambda z: z[0] + "⌊a" + z[1] + "⌋"
    h = lambda z: tuple((window(part, k, ell), semilattice(part)) for part in z)

    W = wstar(n)
    assert h(x) == h(y), ("typing equality fails", n, k, ell)
    assert E(x) == E(y) == F(x) == W
    assert F(y) != W
    assert semilattice(F(y)) == 0
    # Since the unique ceiling-free member of L_n is W,
    # this proves F(y) is not in L_n.
    assert F(y).find("a") == n - 1
    assert W.find("a") == n

def main() -> None:
    checked = 0
    for n in range(3, 18):
        for k in range(n):
            for ell in range(n - k):
                check_one(k, ell, n)
                checked += 1
    print(f"PASS: {checked} cases across n=3..17 and all k+ell<=n-1.")
    for k, ell in [(1,1),(2,2),(3,3),(4,4)]:
        n = max(3,k + ell + 1)
        check_one(k,ell,n)
        print(f"k=ell={k}, n={n}, |W_n|={len(wstar(n))}: PASS")

if __name__ == "__main__":
    main()
