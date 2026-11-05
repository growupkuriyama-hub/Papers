# Parked on 2026-11-06: the focused version of paper #2

On 2026-11-06 `main.tex` was cut from 59 to 41 pages so that it makes one claim:
local groups are the boundary of polynomial characteristic data (README (157)).
Nothing was deleted. The material removed from `main.tex` is kept here.

- `main_before_focus_59pp.tex` — the whole manuscript just before the cut (59 pages, README (147)). It builds as it is.
- `removed_blocks.tex` — the removed blocks one by one, each headed by `%% REMOVED: ...`. `tools/check_port.py` reads this file.

## What was removed

| Block | Labels | Where it could go next |
|---|---|---|
| Membership in the class is undecidable (§2) | `prop:class-undecidable` | a short note or the fan-out-two paper |
| Finite targets admit no typed insertion (§4) | `lem:no-insertion` | with the U₁ results |
| Individual typings onto U₁ (§7.1) and Appendix G | `subsec:u1-typings`, `cor:typing-level-obstruction`, `prop:binary-u1-quadratic`, `app:u1-typings`, `lem:app-u1-insertion`, `lem:app-u1-code` | a paper on typings onto U₁ (with `op:S1`) |
| Unique words at fan-out two (§8) and Appendix J | `lem:unique-word-rigid`, `prop:unique-two-letter-shapes`, `app:singleton`, `thm:app-singleton`, `tab:singleton-certificates`, `lem:app-singleton-runs`, `lem:app-singleton-periodic` | the fan-out-two paper |
| Reduction to semilattices (§8) | `lem:typing-monotone`, `prop:sl-reduction` | the fan-out-two paper |
| Content typings on two letters (§8) and Appendix I | `thm:two-letter-content`, `cor:two-letter-semilattice`, `app:two-letter-content`, `lem:app-two-*`, `prop:app-two-nonsaturated` | the fan-out-two paper |
| Full-content types (§8) | `prop:full-content-types` | the fan-out-two paper |
| Old conclusion: U₁ paragraph, `op:S1`, the rare-type route, long unique words need long companions, abelian filters | `op:S1`, `prop:unique-word-route`, `lem:unique-word-gap`, `prop:abelian-filter-short` | the fan-out-two or U₁ paper |
| Comparison with multidimensional substitutability (Appendix K) and the example L_R in the introduction | `sec:comparison`, `prop:feature-cross-typed`, `def:yoshinaka-pd-substitutability`, `lem:sl2-boundary-control` | a separate note |

The results of the central-question series (Theorems I and II-B, the μ_ab exploration and so on) are not in any manuscript. They are in `reviews/`; see `reviews/STATUS_sl_fanout2_2026-11-01.md`.
