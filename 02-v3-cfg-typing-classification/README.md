# 02-v3 — CFG typing classification (new paper #2)

**Working title:** *Which Fixed Typings Give Polynomial Characteristic Data? A Classification for Substitutable Context-Free Languages*
**Author:** Takayuki Kuriyama
**Status:** submission preparation (2026-11-20). Two AI referee rounds (Astra) addressed; Section 4 rewritten after round 2. Not submitted.

## Concept

This is the third-generation paper #2 of the doctoral-thesis track (#1 → #2 → MOINE). It restricts to **fan-out one (context-free grammars)** and collects the results of `02-v2-lg-fanout-boundary` that are closed there:

1. **Pseudovariety level:** a pseudovariety has uniform polynomial characteristic-data length (rank cap ≥ 2) iff it is contained in **LG**.
2. **Typing level:** a typing onto the two-element semilattice U₁ has polynomial data iff exactly one letter has type 1 (isolated-letter theorem; letter-disjoint obstruction).
3. **Shape of the bound:** the factor ‖G‖θ̄ is necessary for every typing; the binary U₁ typing needs θ̄².
4. Optional: rank one is polynomial for every typing.

It answers the question left open by #1 (TCS-D-26-00494), which proves sufficiency for LI∨Grp and an obstruction U₁ but claims no necessity.

## Files

- [`OUTLINE.md`](OUTLINE.md) — design decisions, section plan and **source map** (which label of which archived file each part comes from). Start here.
- [`PAPER.yaml`](PAPER.yaml) — metadata and status.
- [`main.tex`](main.tex) — English manuscript (27 pp). Source-mapping comments were removed for submission; see OUTLINE.md and git history for provenance.
- [`japanese/main_JP.tex`](japanese/main_JP.tex) — Japanese translation (ltjsarticle, LuaLaTeX, 31 pp); labels, references and all math are kept identical to `main.tex`.

## Relation to other directories

- `02-v2-lg-fanout-boundary/` is **frozen** as the MCFG asset store (Theorem A at every fan-out, fan-out-two research). Do not edit it from here; copy and record sources in `OUTLINE.md`.
- `01_fixed-h-cfg/` (#1) is under review at TCS; cite it by arXiv:1409.6247v5 numbering.

## Change log

- 2026-11-21: Conclusion shortened to one paragraph in the style of #1 (EN and JP): the two criteria, the price outside LG, learner-independence, three open problems.

- 2026-11-21: introduction rewritten to be readable without #1 (EN and JP): self-contained explanation of substitutability, typings, characteristic samples and thickness; a worked example (three-letter doubling family under s_{U,3}: size 13n+7, thickness 2n+1, one word of type 1 of length 3·2^n−2) with the group / single-letter contrast; “Answer in brief” paragraph (pseudovariety boundary algebraic, typing boundary combinatorial, lower bounds learner-independent, upper bounds by Rec_s of #1). The summary sentence after Theorem C, now redundant, was removed. Method and Relation paragraphs unchanged.

- 2026-11-21: acknowledgments added (EN and JP; Makoto Kanazawa and Ryo Yoshinaka, wording as in #1).

- 2026-11-21: standalone-presentation pass (EN and JP). Introduction: motivation from polynomial characteristic sets [de la Higuera 1997, added to references] and the pseudovariety viewpoint [Pin 1986]; the open question stated without “companion” framing; new remark that every lower bound holds for every set-driven operator with characteristic samples throughout C_s (checked: Prop. rare-type needs samples for L and L^{\m}, both in C_s; Thm A(ii) via Prop. three-letter-family(iv); Thm B(ii) via Cor. typing-level-obstruction; Thm B(i) non-linearity and Thm C via Props. binary-quadratic and linear-factor). Theorem A(ii) now uses the paper's own typing s_{U,3} (Prop. three-letter-family: ‖G_n‖=13n+7, τ≤4n, data ≥3·2^n−1) instead of s_U of #1, so item (Q5) was removed from Section 2. Section 2 renamed “Preliminaries”; definition-level citations of #1 consolidated; “companion” removed throughout; Remark rem:scope (a),(d) and the Conclusion rephrased. No mathematical claim changed.

- 2026-11-21: abstract rewritten (EN and JP) to read as a standalone paper: opens with the question rather than with the companion paper, no reference to the prior result, and the BUNF typed-thickness estimate is left to Theorem A(i). Claims unchanged.

- 2026-11-21: Japanese translation added. Corrections found while translating, applied to both `main.tex` and `japanese/main_JP.tex`: Theorem A.5 proof (`K = K^k ⊆ S^k` by complete simplicity, not by ideality); Lemma 4.1 proof (`γ^J_i`, `g_i`, `g'_i` defined); Lemma 3.3 proof (path-read context renamed `(ū_X, v̄_X)`, no clash with the canonical `χ(X)`); Theorem 4.3(ii) proof (`t_ρ` → `t_R`); Corollary 6.2 (morphism `h` defined, “length” → “size”, base rule added to the rule-thickness count); after Proposition 7.1 (the constant-factor claim is now proved for every reduced presentation: `q+1 ≤ 12‖G‖`, `‖G_{q,k}‖ ≤ 276‖G‖`); three-letter typing renamed `s_{U,3}` (was `s_U`, too close to `s_{\mathrm U}` of #1); `s_triv` replaced by the one-element typing `s_0`; `≡_{L,s}` defined explicitly in Appendix C; `λ(w)` → `ℓ(w)` in Appendix D; unused alias label `lem:app-tl-recognition` on Lemma B.2 renamed `lem:app-tl-exchange`.

- 2026-11-20: submission cleanup — removed draft date and all source/status comments, added the generative-AI declaration (wording as in #1).

- 2026-11-20: Section 4 rewritten with the direct proof supplied by Astra (reviews/astra_lg_quadratic_proof_2026-11-20.txt): typed thickness O(N(τ+1)) for BUNF and characteristic data O(‖G_*‖² max{1,τ}) for every reduced CFG; the gap to the linear-factor lower bound is now one factor of symbol size. Not yet independently audited.

- 2026-11-20: addressed the Astra round-2 report (Minor Revision); Theorem C(i) strengthened to two letters; see [reviews/RESPONSE_TO_ASTRA_ROUND2_2026-11-20.md](reviews/RESPONSE_TO_ASTRA_ROUND2_2026-11-20.md).

- 2026-11-20: addressed the Astra referee report (Major Revision; 5 Major, several Minor); see [reviews/RESPONSE_TO_ASTRA_2026-11-20.md](reviews/RESPONSE_TO_ASTRA_2026-11-20.md).

- 2026-11-20: introduction and Section 6 explain why the typing-level classification starts with U₁ (the minimal obstruction outside LG).

- 2026-11-20: directory created; outline, metadata and manuscript skeleton.
- 2026-11-20: switched to the framework of #1 (arbitrary reduced CFGs, BUNF, `Rec_s`, `tau_G`, typed thickness). Added draft bridge lemmas (lambda-elimination with thickness control, typed-thickness transfer, master transfer corollary, rare-type principle for `Rec_s`); restated Theorems A–C in #1's measures. New mathematics is marked DRAFT-NEW and is not yet audited.
- 2026-11-20: Section 4 and Appendix A — self-contained fan-out-one proof of local-group sufficiency. Sections 6–7 and Appendices B–E ported (three-letter family, typing-level obstruction, isolated-letter theorem, U₁ classification, binary quadratic family, linear factor), with operators replaced by `Rec_s`. Added the representative-witness lemma needed because the isolated-letter theorem bounds representatives, not yields. 25 pp.
