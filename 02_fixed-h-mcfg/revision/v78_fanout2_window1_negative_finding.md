# #2 MCFG v78 research memo: obstruction to a trivial higher-fan-out lift

Date: 2026-10-18. Research-note branch \`mcfg2-v78-fanout2-lower-bound-notes\`.
**Not a theorem of the I&C manuscript. No change to the v77 main TeX.**

## Exact problem

Open Problem \`op:fanout-two\` asks for fixed f>=2 and rank>=2, a fixed finite
typing h and reduced good presentations G_n in \`C_mcf(f,h)\`, of polynomial
size and original thickness, for which *every* characteristic sample of the
specified rank-capped observed-tuple constructor has superpolynomial
encoded length. The original CFG family does not automatically lie in
\`C_mcf(2,h)\`; arity-2 substitutability checks **all** sentence contexts
with nonempty internal separators, not just grammar-derived contexts.

## A counterexample to the width-one sliding-window rescue

TCS #1, Proposition \`prop:typed-thickness-gap\`, defines
\`E_0 -> a\` and
\`E_i -> floor E_{i-1} E_{i-1} floorclose | ceiling E_{i-1} ceilingclose\`.
Take n=3, for which \`L_3\` consists of 42 words, and type components
with the product of the width-(1,1) prefix/suffix morphism and the
two-element semilattice morphism \`h_U\` (ceiling brackets map to zeta).

Let (using Unicode mathematical floor and ceiling bracket symbols)

\`\`\`
x = ("⌊⌈a⌉⌈",  "⌉⌋")
y = ("⌊⌈",     "⌉⌊aa⌋⌋")
E[z1,z2] = "⌈" + z1 + "a" + z2 + "⌉"
F[z1,z2] = "⌊" + z1 + "a⌉⌋⌈⌈a⌉" + z2
\`\`\`

Both tuples have componentwise equal width-(1,1) and semilattice
values: first components start with \`⌊\` and end with \`⌈\`;
second components start with \`⌉\` and end with \`⌋\`;
all four contain a ceiling bracket.

Yet:
\`\`\`
E[x] = ⌈⌊⌈a⌉⌈a⌉⌋⌉              in L_3
E[y] = ⌈⌊⌈a⌉⌊aa⌋⌋⌉             in L_3
F[x] = ⌊⌊⌈a⌉⌈a⌉⌋⌈⌈a⌉⌉⌋         in L_3
F[y] = ⌊⌊⌈a⌉⌋⌈⌈a⌉⌉⌊aa⌋⌋        not in L_3
\`\`\`
The corresponding E and F both belong to the allowed \`E_2\` sentence
contexts and share their internal separators. This violates the required
distributional implication. For \`F[y]\`, the root would need to split
the inner word into two members of \`L_2\`, but its initial bracket prefix
is not the beginning of any \`L_2\` word.

The Python script \`revision/check_fanout2_window1_counterexample.py\`
constructs \`L_0,..,L_3\`, verifies cardinalities (1,2,6,42), the typing
equality, and all four membership facts. This finite exhaustive computation
checks the witness but **does not constitute a general no-go theorem**.

## Implications and next avenues

- Simply replacing \`h_U\` by \`h^{1,1}_Sigma x h_U\` does not make
  the original doubling family (2,h)-substitutable.
- The example does **not** rule out widths k>=2 or a different family,
  nor does it establish any lower bound for a higher-fan-out learner.
- Next, test a bounded width k against successive n, and record the first
  failing tuple/context with a machine-verifiable trace. A general theorem
  requires a construction for **fixed k independent of n**.
- An alternative is an explicit *new* family of languages whose arbitrary
  2-hole exchanges preserve derivability (not merely unique grammar
  parses), while retaining a rare exponentially long typed word.
- Keep operator-specific and all-operator lower bounds logically separate,
  as in TCS #1's Proposition 6.3.

No manuscript statement or theorem number is changed by this memo.
