# #2 — fixed-h MCFG

**Title:** Positive-Data Learning of Multiple Context-Free Languages under Fixed Finite-Monoid Typing  
**Author:** Takayuki Kuriyama  
**Target journal:** Information and Computation  
**Public preprint:** arXiv:2605.11644

## いつでも同じURLで読める最新PDF（英語／日本語）

GitHub の **main ブランチ**上に固定したPDFパスです。論文を改訂してもURLを変更する必要はありません。

- [#2 MCFG 英語版PDF — 最新公開版](https://github.com/growupkuriyama-hub/Papers/blob/main/02_fixed-h-mcfg/main.pdf)
- [#2 MCFG 日本語版PDF — 最新公開版](https://github.com/growupkuriyama-hub/Papers/blob/main/02_fixed-h-mcfg/japanese/main_JP.pdf)
- [#1 TCS CFG 英語版Clean PDF — 最新公開版](https://github.com/growupkuriyama-hub/Papers/blob/main/01_fixed-h-cfg/TCS-D-26-00494_Manuscript_Clean.pdf)
- [#1 TCS CFG 日本語版PDF — 最新公開版](https://github.com/growupkuriyama-hub/Papers/blob/main/01_fixed-h-cfg/japanese/main_JP.pdf)

#2 については
[Publish MCFG #2 English and Japanese PDFs](../../.github/workflows/publish-mcfg-bilingual-pdf.yml)
が，英語 \`main.tex\` とその別付録，日本語 \`japanese/main_JP.tex\` とその別付録の
いずれかが変更されるとPDFの両方をビルドし，成功後に固定パスへコミットします。
**日本語の翻訳文は英語原稿の変更に自動追従しません。**
英語本文を修正した場合は，対応する日本語TeXも更新する必要があります。
このワークフローは，既存の日本語TeXを再コンパイルするものであり，
改訂箇所を機械翻訳して自動同期するものではありません。

## 日本語査読版（v81 投稿前点検版）

英語版 v81 の定理・数式・証明・文献に対応する日本語版を
[`japanese/main_JP.tex`](japanese/main_JP.tex) に置きました。
有限アーベル群の独立付録と任意有限群の追加付録も
[`japanese/appendix_window_abelian_JP.tex`](japanese/appendix_window_abelian_JP.tex)
および [`japanese/appendix_window_group_JP.tex`](japanese/appendix_window_group_JP.tex) として訳してあり，本文から読み込まれます。
局所群の付録 `appendix_local_group.tex` と `japanese/appendix_local_group_JP.tex` も読み込まれます。
[`japanese/README.md`](japanese/README.md) に英語原稿の固定版，
対応検査，LuaLaTeX PDF のビルド方法を記録しています。
提出用の英語版 `main.tex` は変更しません。

**#1 companion manuscript (version-locked, prior to arXiv v5):** [TCS Clean PDF at commit 834e99a1](https://github.com/growupkuriyama-hub/Papers/blob/834e99a1f35b4a5fb949acc55a080658388d4480/01_fixed-h-cfg/TCS-D-26-00494_Manuscript_Clean.pdf). The public arXiv:1409.6247v4 is an earlier baseline; the new citation will be supplemented when v5 is actually released.

## v88 Claude independent-audit mathematical corrections (I&C draft)

Based on the independent adversarial report of v87 (0 Critical, 0 Major,
3 Moderate, 7 Minor findings), v88 adds rigorous ordered-product
and local-group heavy-antichain transfer lemmas in both EN/JP appendices;
corrects the overly broad computed-witness length claim; removes
the unproved exact SUBST_P correspondence; and tightens semigroup
attribution, antichain wording and the conditional CFG lower bound.
The theorem assumptions and asserted polynomial degrees are unchanged.
See `revision/v88_claude_audit_repairs.md`. The working branch is
`mcfg-v88-claude-audit-math-repairs`; v87 remains preserved.

## v87 TCS-style referee preflight (review draft)

- Active stacked review branch: `mcfg-v87-tcs-style-review-preflight`, based on v86. Both main algebraic theorems now have their formal statements in the **main text**, while the finite-group/local-group proofs remain in the corresponding appendices.
- Clarified fixed-parameter quantifiers, original thickness vs typed-refinement thickness, sample-length polynomial bounds vs time polynomial in the observed sample, and generated rule-only witnesses vs existential short distributional witnesses.
- The restored fan-out-two rank-one witness is also outside the LG typing condition via its four-element semilattice quotient.
- The proof-dependency audit and open external-verification points are documented in [`revision/v87_tcs_referee_math_audit.md`](revision/v87_tcs_referee_math_audit.md).
- Complete v86 source remains at branch `mcfg-v86-fanout-two-separation-return` / Draft PR #56; main and arXiv remain unchanged. No independent mathematical referee report or submission is implied.

## v86 restored fan-out-two non-CFL rank-one separation (I&C draft)

Branch `mcfg-v86-fanout-two-separation-return` restores the complete EN/JP proof and strict-2-local supporting lemma for `thm:arbitrary-filter-separation` from `archive/trim-v83`. It exhibits a genuine fan-out-two, rank-one typed non-CFL outside every arbitrary regular filter of Yoshinaka's untyped substitutable class. The larger minimum-rank-two example remains archived. No local-group or semilattice-coset theorem, open lower-bound question, or v85 source was modified. See `revision/v86_fanout2_separation_restoration.md`.

## v85 absorbed-theorems I&C review draft

Active branch: `mcfg-v85-ic-theorem-absorption`. Original complete v84 is frozen at commit `ed945ec8792f3840cdb108b09c49780f8fa4d404` on `archive/mcfg-v84-preabsorption-full-20261018`.

- **Typing-side main theorem:** positive-image local groups (LG). The cubic window+arbitrary-finite-group theorem is now explicitly a special case, with separate proof archived.
- **Sharp subcase retained:** locally trivial positive images (LI) keep the better quadratic estimate.
- **Target-side main theorem:** finite-semilattice-indexed abelian cosets. Abelian-filter and marker results remain short corollaries.
- **Proof integrity:** noncommutative interval/order/antichain shortening lemmas stay in the compiled appendix. The abelian zero-sum/Davenport appendix and pseudovariety lower-bound detail are archived, not destroyed.
- `archive/trim-v85/README.md` explains restoration. `revision/v85_theorem_absorption_trim_manifest.md` records scope and pending checks.
- Six compiled EN/JP TeX source SHA-256 checksums are maintained in `PAPER.yaml`. No main-branch or arXiv changes.

## v84 concise exposition and inline math (review draft)

Active working branch: `mcfg-v84-ic-inline-prose-tightening`.
This is a **reversible presentation-only refinement** of the focused v83 paper.
- EN/JP introductions, Yoshinaka comparison and conclusions shortened to eliminate repeated scope statements while retaining attribution, key theorems and the open problem.
- Short standalone display equations moved inline in the main paper and all three original algebraic appendices, with major multi-line proof equations retained as displays.
- All bilingual TeX sources have matching updated SHA256 metadata. Bilingual PDF CI and visual overfull checks are required.
- `mcfg-v83-ic-focused-trim` and PR #52 remain untouched as the immediate restoration baseline. Earlier complete v82 and archived theorems also remain available.
- See `revision/v84_inline_exposition_trim.md` for checks and what is *not* changed.

## v83 I&C Focused Manuscript (review draft)

**Current review branch:** `mcfg-v83-ic-focused-trim`. The official `main` manuscript remains at v81; this draft has not been submitted or merged.

- EN `main.tex` / JP `japanese/main_JP.tex`: targeted trim, retaining the two complementary algebraic polynomial-data results: positive-image local groups (typing-side) and semilattice-indexed abelian cosets (target-side). Exact learning, rank-one, window and arbitrary finite-group bounds, relaxed and computable witness results remain.
- Entire untrimmed v82 at commit `bcc0caf0eade66f552127171c0de24d2b92950b0` on archive branch `archive/mcfg-v82-pretrim-full-20261018`.
- **Restorable exact excerpts** for separation and lower-bound results in [`archive/trim-v83/README.md`](archive/trim-v83/README.md), with full EN and JP proof sections.
- [`revision/v83_ic_focus_trim_manifest.md`](revision/v83_ic_focus_trim_manifest.md) documents editorial scope and mathematical/proof dependencies.
- Full algebraic appendices remain, including the noncommutative-group lemmas used by the local-group theorem and the original Davenport refinement.
- Mandatory author journal declarations and `\\appendix` are preserved.

Both PDF builds and proof/source audits must pass before promotion to `main`. The ordinary stable PDF links above still point to v81.

## v82 draft（有限半束ねじれ定理への統合、レビュー中）

このブランチは **v82-draft（未マージ・未投稿）** です。英語・日本語の両TeX原稿を同期し、`main` 上のv81とその固定パスPDFは変更していません。

- 新しい主定理 `thm:mcfg-semilattice-twisted-polydata`: 有限半束で添字付けした共通部分群アーベル剰余類言語に対する一様な多項式特徴データ長上界。
- 新補題 `lem:mcfg-coset-representative-transfer`: 緩和分布同値証人への整数計画転送を共通化。
- 新補題 `lem:mcfg-sl-rectangle`、`lem:mcfg-sl-height`、`lem:mcfg-sl-short-value`: 長方形剛性・高さの狭義低下・経路費用の短縮。
- 既存 `thm:mcfg-abelian-filter-data` は **ラベルを保存し系に変更**。空語を除いたコアを主張し、空語は追加サンプルとして別処理。
- 一マーカー特殊例 `cor:mcfg-one-marker-split-polydata` を明記。
- 補助群に一様な存在論的上界であり、任意の補助群表示に対する多項式時間構成は主張しません。
- ワークフロー `.github/workflows/validate-mcfg-v82.yml` はレビュー用で、日英PDFをビルドして成果物をアップロードするだけです。mainの公開PDFを更新しません。

**投稿前の確認事項：** 日英ビルドの成功、全頁視認、数理の独立監査、原典・先行研究・引用の最終照合、著者承認。現行v81の論文を正式に置換したものではありません。

## Current working baseline

- `main.tex` — **v81 on main / v82-draft on this branch** I&C pre-submission working revision: Davenport constants, order homogenization, effective characteristic data, rule-only witnesses, LG appendix, and LI∨Grp corollary. External mathematical review and author signoff remain open.
- `revision/v81_submission_preflight_review.md` — bilingual pre-submission editorial/mathematical source audit, repaired abstract/conclusion, journal disclosure and visual-PDF gates.
- `revision/v80_mobility_distributional_review.md` — type-deletion lower-bound criterion, two-component mobility, universal finite-typing nonmembership, relaxed distribution classes and abelian-filtered polynomial data; algebraic/effective scope checked.
- `revision/v79_rule_only_witness_budget.md` — proves redundant nonterminal samples can be dropped when minimizing canonical tuples, improving cardinality and computable encoded budget.
- `revision/v78_fanout2_window1_negative_finding.md` — uniform fixed-window impossibility result for the bracketed family, plus finite test histories.
- `revision/check_fixed_window_general_obstruction.py` — executable bounded verification of the new all-window theorem.
- `revision/v77_computable_witness_budget.md` — presentation-sensitive computable characteristic-data budget; attribution of LG algebraic characterization to Almeida et al. (2009) integrated in bilingual text.
- `revision/v75_to_v76_strengthening_drafts.md` — Davenport/order/algorithm strengthening.
- `revision/v76_stage1_lg_dichotomy.md` — local-group pseudovariety extension, experimental checks and remaining independent verification.
- `revision/v76_li_grp_algebraic_corollary_note.md` — intrinsic LI∨Grp sufficient condition and proof-hardening audit.
- `revision/v74_to_v75_final_referee_hardening.md` — final adversarial-referee corrections, version-locked companion GitHub reference, primary-source citation audit, and bilingual verification status.
- `revision/v73_to_v74_finite_group_shortening.md` — independently audited Ramsey block-order/finite-group extension and verification gates.
- `appendix_window_group.tex` — arbitrary finite-group short-tuple theorem and window--group polynomial characteristic-data bound (nonabelian groups included).
- `revision/v71_to_v72_referee_p1p2_and_sharper_bounds.md` — v72 correction log, new untyped canonical-context bound, and outstanding author/publication checks.
- `revision/v71_retired_results_archive.md` — the removed v70 results and the entire former doubling-family appendix, preserved for reuse in a thesis or separate paper; **not compiled** in v71.
- `revision/v70_to_v71_selective_results_note.md` — v71 scope decisions, retained results and validation gates.
- `appendix_window_abelian.tex` — retained direct window + finite-abelian-group theorem with the sharper explicit abelian constant. The former limitation is resolved in the subsequent general-group appendix.
- `revision/v69_to_v70_ic_referee_revision_note.md` — referee-audit revision, mathematical verification, and remaining submission gates.
- `revision/v68_to_v69_ic_referee_corrections.md` — I&C independent-review corrections: resolves the false fan-out-one open problem using the companion CFG lower bound, strengthens the SUBST_P proof, checks Gallot's exact theorem scope, reorders and focuses the introduction.
- `revision/v67_to_v68_yoshinaka2015_revision_note.md` — prior Yoshinaka 2015 exact-correspondence revision.
- `revision/v64_to_v65_revision_note.md` — earlier pre-submission hardening after independent review.
- `revision/v64_to_v65.diff` — sequential unified diffs for the v64 → v65 hardening.
- `revision/v63_to_v64_revision_note.md` — citation-hardening pass after independent audit: expands the Bishop et al. corroboration chain while retaining Gallot as the direct non-branching MCFG lower-bound source; no mathematical statement changes.
- `revision/v63_to_v64.diff` — unified manuscript diff for the v63 → v64 citation hardening.
- `revision/v62_to_v63_revision_note.md` — final planned page-reduction pass: compresses characteristic-data exposition and normalization appendix bookkeeping without removing named results.
- `revision/v62_to_v63.diff` — unified manuscript diff for the v62 → v63 compression.
- `revision/v61_to_v62_revision_note.md` — safe page-reduction pass confined to the comparison section; compresses proof narration while preserving named result statements and the intrinsic-rank-two audit core.
- `revision/v61_to_v62.diff` — unified manuscript diff for the v61 → v62 comparison-section compression.
- `revision/v60_to_v61_revision_note.md` — final submission-hardening pass after two independent audits: fixes recognition/normalization citation scope, sharpens intrinsic-witness novelty positioning, strengthens the Gallot/Bishop bridge, and reduces defensive prose without changing theorem statements.
- `revision/v60_to_v61.diff` — unified manuscript diff for the v60 → v61 revision.
- `revision/v59_to_v60_revision_note.md` — safe pre-submission compression pass: trims repeated exposition and one unused secondary example while preserving theorem/proposition/lemma counts and the mathematical core.
- `revision/v59_to_v60.diff` — sequential unified patches for the v59 → v60 compression revision.
- `revision/v58_to_v59_revision_note.md` — pre-submission citation and positioning hardening after independent review; corrects the COPY attribution, strengthens the Gallot/Bishop source bridge, clarifies the modular intrinsic witness, and removes an unused bibliography entry.
- `revision/v58_to_v59.diff` — unified diff for the v58 → v59 revision.
- `revision/v57_to_v58_revision_note.md` — strengthens the intrinsic-rank-two witness to a non-context-free minimum-fan-out-two target while retaining the all-finite-fan-out rank lower bound.
- `revision/v57_to_v58.diff` — unified diff for the v57 → v58 revision.
- `revision/v56_to_v57_revision_note.md` — adds a corrected intrinsic-rank-two boundary-typed witness based on the non-branching lower bound for MIX2.
- `revision/v56_to_v57.diff` — unified diff for the v56 → v57 revision.
- `revision/v55_to_v56_revision_note.md` — withdraws the invalid minimum-rank-two witness, reframes the higher-rank theorem as presentation-sensitive, and records intrinsic rule rank as an open problem.
- `revision/v55_to_v56.diff` — unified diff for the v55 → v56 correction.
- `revision/v54_to_v55_revision_note.md` — stable ACL Anthology locator for Kato--Seki--Kasami (2004).
- `revision/v54_to_v55.diff` — unified diff for the v54 → v55 revision.
- `revision/v53_to_v54_revision_note.md` — explicit empty-word clause in the rank-one characteristic-data theorem.
- `revision/v53_to_v54.diff` — unified diff for the v53 → v54 revision.
- `revision/v52_to_v53_revision_note.md` — primary-PDF citation audit and locator tightening for Yoshinaka/Seki sources.
- `revision/v52_to_v53.diff` — unified diff for the v52 → v53 citation-audit revision.
- `revision/v51_to_v52_revision_note.md` — targeted prose-compression pass in the quantitative characteristic-data section.
- `revision/v51_to_v52.diff` — compact diff summary for the v51 → v52 revision.
- `revision/v50_to_v51_revision_note.md` — abstract scope precision for the higher-rank characteristic-data theorem.
- `revision/v50_to_v51.diff` — unified diff for the v50 → v51 revision.
- `revision/v49_to_v50_revision_note.md` — explicit Kato dimension/rank ↔ fan-out/rule-rank notation bridge.
- `revision/v49_to_v50.diff` — unified diff for the v49 → v50 revision.
- `revision/v48_to_v49_revision_note.md` — citation-provenance precision pass for the minimum-rank-two lower-bound chain.
- `revision/v48_to_v49.diff` — unified diff for the v48 → v49 revision.
- `revision/v47_to_v48_revision_note.md` — summary of the v47 → v48 genuine-rank-two witness revision.
- `revision/v47_to_v48.diff` — unified diff for the v47 → v48 revision.
- `revision/v46_to_v47_revision_note.md` / `revision/v46_to_v47.diff` — retained history for the preceding revision.
- `revision/v45_to_v46_revision_note.md` / `revision/v45_to_v46.diff` — retained history for the preceding revision.
- `revision/v44_to_v45_revision_note.md` / `revision/v44_to_v45.diff` — earlier retained history.

The public arXiv record currently corresponds to an earlier manuscript baseline; the working source in this directory has advanced substantially beyond that version.

## Scope

The manuscript studies positive-data learning of bounded-fan-out multiple context-free languages under fixed finite-monoid typing, including exact finite-sample reconstruction, conservative TxtEx learning, quantitative characteristic-data bounds, and expressiveness/separation results.
