# Decision: restore a light Theorem C (2026-11-17)

**Premise (author's instruction):** the companion CFG paper (TCS-D-26-00494, arXiv:1409.6247v5) is assumed to pass TCS review. The manuscript itself still cites it as *under review*; nothing in the text claims acceptance.

## What changed
- New Section 6 "The Boundary at Fan-Out One" (EN `sec:fanout-one`, JA 「ファンアウト1での境界」):
  - `def:uniform-polydata` (from parked Plan A source),
  - `lem:fanout-one-classes` (new): C^mcf_{1,s} = C^cf_s of [kuriyamaCFG, Def. 2.1]; sample notions coincide,
  - bracketed doubling family over Γ_br = {a, ⌊, ⌋, ⌈, ⌉}, typing s_U onto U_1 (from [kuriyamaCFG, §6]),
  - `prop:fanout-one-lower` (new): ‖G_n‖ = 13n+7, θ̄ = 4n, every characteristic sample contains w*_n, ‖F‖_+ ≥ 3·2^n−1 ≥ 2^{(‖G_n‖+θ̄)/17},
  - `thm:fanout-one-data` and `rem:fanout-one-data` (adapted from parked Plan A source).
- Intro main theorem `thm:C` (prints as Theorem B); abstract, companion paragraph, contribution sentence, scope sentence and conclusion updated in both languages.
- The former self-contained 3-letter family and its appendix remain parked (`parked/planA_2026-11-16/`).

## Dependence on the companion
Only the lower-bound family is used: its membership in C^cf_{s_U} and the uniqueness of the type-1 word ([kuriyamaCFG, Prop. 6.4(i),(iv); App. C]). The distinguishing-pair argument is recalled in full. Theorem A and all upper-bound proofs remain independent of the companion.

If the companion's numbering changes in its final version, update the five `\cite[...]{kuriyamaCFG}` locators in each language.

## Checks (local)
- `tools/check_port.py`: exit 0 (new labels registered).
- EN/JA: labels 89/89 in identical order; statement-level math diff unchanged from main (4 pre-existing diffs); new section math identical up to one punctuation mark.
- `tools/check_jp_alignment.py`: same FAIL categories as on main (pre-existing).
- Builds: EN pdfLaTeX 30 pp, JA LuaLaTeX 33 pp (local TeX Live), 0 overfull boxes, no undefined references.
