# #2 v2 — Local Groups and the Fan-Out Dependence of Characteristic-Data Length in Typed Distributional Learning of Multiple Context-Free Languages

**Author:** Takayuki Kuriyama
**Target journal:** Information and Computation
**Status:** full English draft; first external comparison review (ChatGPT) addressed; shortening, Japanese version and independent proof review pending

This folder is the restructured ("new-born") version of paper #2. The mathematics is taken from the frozen v1 in [`../02_fixed-h-mcfg/`](../02_fixed-h-mcfg/) and reorganized around one claim and three main theorems:

- **Theorem A** — local-group upper bound $O(\|G\|^2\bar\theta_G)$ at every fan-out; linear factor $\Omega(\|G\|\bar\theta_G)$ under every typing at every fan-out; $\Theta(\|G\|\bar\theta_G)$ for the trivial typing.
- **Theorem B** — the boundary at fan-out one: pseudovarieties ⇔ $\mathbf{LG}$; two letters of type 1 in a copy of $U_1$ force exponential data; the single-neutral-letter typing needs data quadratic in $\bar\theta_G$, sharp for constant weight.
- **Theorem C** — the boundary moves at fan-out two: the single-neutral-letter typing admits polynomial data; the exponential fan-out-one family does not lift.

**Start here:** [`INSTRUCTIONS_FOR_AI.md`](INSTRUCTIONS_FOR_AI.md) (status, structure, next phases, rules, checklist).

## Files

- `main.tex` — English master (51 pages: body 26, appendices A–L 22, references 3). Builds with `latexmk -pdf main.tex`, no warnings.
- `parked/parked_from_v1.tex` — v1 material not used in v2 (one-letter cyclic typing).
- `reviews/` — external reviews of v2 (ChatGPT comparison v1/v2, 2026-10-30).
- `tools/check_port.py` — checks that every v1 label is in v2 or parked, and lists ported statements that differ from v1.
- `INSTRUCTIONS_FOR_AI.md`, `PAPER.yaml`.

## Change log

- **2026-10-30 (4)** ChatGPT comparison review (`reviews/chatgpt_compare_v1_v2_2026-10-30.md`; v1 37/60, v2 46/60; two real errors in v2, both fixed): (a) Theorem A(ii) lacked the alphabet condition of `prop:linear-factor-all-fanout` (a one-letter alphabet is a counterexample) — now "if Σ has at least 4f+1 letters (3 if f=1)", also in the abstract, the ported sentence before `prop:linear-factor-sharp` and the Conclusion; (b) `cor:trivial-exact` spoke of the *largest* characteristic sample, which is unbounded (supersets of characteristic samples are characteristic) — restated as an upper bound for every target plus attainment by the marker family, with a remark that only shortest samples are meaningful; Theorem A(iii), abstract and Tightness paragraph synchronized. Also: C(ii) now states the threshold $n\ge2|\mathsf S|+3$; the existence of the critical node in `prop:binary-u1-weight-slice` is spelled out; v1 §6.1–6.2 (multidimensional substitutability, typing separations by explicit non-CFL targets) restored as Appendix K with the $L_R$ example in §1 and a summary paragraph at the end of §5 (reviewer: MCFG-specific evidence was lost); rank one is now Appendix L; `\port`/xcolor removed. 51 pages.
- **2026-10-30 (3)** Phase 4 started: proof of `prop:linear-factor-sharp` moved to Appendix I (body unchanged in content).
- **2026-10-30 (2)** Phases 1–3: all v1 mathematics ported (labels unchanged); new abstract, Introduction (Theorems A–C, remaining question, approach, prior work, companion table, scope, organization) and Conclusion (Open Problems S1 and fan-out two, tightness of exponents). New: `cor:trivial-exact`; `prop:binary-u1-weight-slice` (constant-weight targets: $\mu^\star\le\lfloor(\bar\theta_G+1)^2/4\rfloor$, attained by the compressed block family; from Astra's 2026-10-30 report, verified and rewritten by Claude). Rank one moved to Appendix K; v1 §6.1–6.2 and `prop:unary-cyclic-linear` parked. `check_port.py` passes (intended changes: `rem:fanout-one-data`, `op:fanout-two`).
- **2026-10-30 (1)** Skeleton created: new title and abstract, Introduction with Theorems A–C, section stubs with port boxes, Open Problem S1, port plan.
