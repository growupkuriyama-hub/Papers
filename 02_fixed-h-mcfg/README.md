# #2 — finite-semigroup-typed MCFG

**Title (v87 logically condensed Yoshinaka (2015)-based draft):** Positive-Data Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing  
**Author:** Takayuki Kuriyama  
**Target journal:** Information and Computation  
**Public preprint:** arXiv:2605.11644

## v88 後半の共通補題統合と定量的証明の圧縮（PR #70・未統合）

英文v87の前半は保持し，Claudeのv86後半案を現行v87へ直接接続して
第4節・第5節・結論・正規化付録および群／局所群付録を論理的に再構成した．
**英文38ページ（v87: 44ページ）**．旧可換群・一般有限群付録の内容は，
英文では本文の群値短縮定理と新 `appendix_group_blocks.tex` へ統合し，
旧2ファイルは参照されない履歴資料として保持する．

数学的修正：導出可能代表元の実効的標本へ分布的緩和代表元の上界を
誤適用しないよう `prop:effective-char-data` の適用範囲を限定（R1）．
v87で統合済みの完全性補題を用いて `prop:mcfg-relaxed-witnesses` を
直接証明し，古い未定義ラベルの引用を削除．
共通補題4件（窓スケルトン／重い節点の計数／群ブロック置換／
局所群短縮）の数学的条件追跡・監査記録を追加．
GitHub Actionsの新付録監視パスと stale-source guard も追加．

日本語版は**54ページ**で，R1と局所群の非可換ブロック置換の証明を
数学的に同期させた．英文v88と日本語版は主要定理・上界の内容は対応するが，
日本語の付録統合・文章圧縮は未実施である．
英日ビルドと相互参照のCIは成功．本PRは**draft**で，mainには未統合．
完全な数学的独立最終査読と全頁目視はなお必要である．

[独立4補題監査](revision/v88_quantitative_four_lemma_independent_audit.md) ／
[PR #70](https://github.com/growupkuriyama-hub/Papers/pull/70)

## v87 前半1–3節の論理的圧縮（main執筆正本、I&C未投稿）

Claude圧縮案をもとに前半の定性理論を再構成し、六項目の形式的・数学的監査
（空の非空核、ランク0、節ラベル、Yoshinaka (2015) の型付き関数列挙、
`SUBST_P` の恒等関数証拠、任意代表元による完全性）を反映した。
**英文PDFは44ページ（v86: 49ページ）**。第4節以降の英文定量的結果と独立付録の
数学的主張は変更していない。日本語版は斉次性・任意代表元の完全性・
ランク0を含む再構成定理・先行研究への帰属・緩和代表元の証明適用を同期し、
**日本語PDFは53ページ（v86: 52ページ）**。日本語の文章構成全体の圧縮は未実施。

[六項目監査](revision/v87_english_compression_six_point_audit.md) ／
[PR #69](https://github.com/growupkuriyama-hub/Papers/pull/69)

英日両方のLaTeXコンパイルと引用・相互参照検証はGitHub Actionsで成功。
独立した数学的最終監査・PDF全頁目視・著者最終承認はなお必要。
**mainへの統合はI&Cへの投稿や査読を意味しない。**

## v86 質的学習の説明と証明を圧縮（改訂履歴）

v85で実装したYoshinaka (2015)の有限ソートsignatureへの特殊化と
`SUBST_P`の有限標本対応は維持し，重複する紹介文・再構成の説明・
健全性やGold学習の証明文を英日で圧縮した．
全ての定理・命題・系・定義の数学的主張とラベル，特徴データ総長の主定理，
ランク無制限の独立論証および三つの付録は維持している．

PR #68 の両言語ビルドにおけるPDFページ数は，
**英語49ページ（v85: 51ページ），日本語52ページ（v85: 54ページ）**．
TeXコンパイルおよび引用・相互参照チェックは成功．
この圧縮はページ詰めや付録への単純移動ではない．
PDFの全頁目視と数学的独立最終監査は未完了であり，
I&C投稿用最終稿とは扱わない．

[圧縮記録](revision/v86_qualitative_compression.md) ／
[関連PR #68](https://github.com/growupkuriyama-hub/Papers/pull/68)

## v85 Yoshinaka (2015)を質的学習の基盤とする再編（改訂履歴）

規則ランク有界なMCFGの型付きsignatureとYoshinaka (2015)から導く正例同定を，第3節の冒頭へ移動。\`SUBST_D\` と \`SUBST_P\` の相違を区別し，具体的再構成器との標本単位の対応を保持。質的学習の一般論の重複証明を削り，特徴証拠語の総文字数とrank無制限の直接論証は維持した。英日とも同じ構成。

[改訂記録](revision/v85_yoshinaka2015_qualitative_reorganization.md)。全頁目視と独立数学監査を経るまでは投稿確定稿ではない。

## v84 M6（正規化と厚み移送）証明補強（改訂履歴）

Claude集中査読を吟味し，良形正規化の非消去化・成分置換・非融合化について，生成タプル集合の像の等式と証拠語長の不等式を英日双方で詳細に証明した。縮約済み入力で省略する子の生産性を明記し，Seki・Kanazawa・Yoshinakaの引用の射程を訂正。固定窓の入力文法に対する総特徴データ長を $O(\|G_{\mathrm{in}}\|^3\max\{1,t_{G_{\mathrm{in}}}\})$ と明示。

[**v84改訂記録**](revision/v84_m6_thickness_transfer_proof_audit.md)。定理自体は弱めていない。数学的独立最終監査・PDF全頁目視は引き続き必要。

## v83 I&C短縮版・Claude査読反映（改訂履歴）

49ページ実験版を基に、半群移行補題、Yoshinakaのソート、空語と正語の扱い、TCS R1引用、関連arXiv原稿の開示を英日で修正し、**v83をmainの正本として統合**。英語版は50ページ、日本語版は54ページ（公開PDFはGitHub Actionsが本ブランチ上で再生成）。
[改訂と未解決事項](revision/v83_claude_review_corrections.md) を参照。
**この段落はv83時点の記録：** 当時未完了だったM6の証明をv84で拡充した。mainは執筆正本であり，I&Cへの最終投稿確定稿ではない。

## v82半群化（改訂履歴）

#1 TCS R1凍結版に合わせ、基本学習型を $s:\Sigma^+\to S$ にし、空語とテンプレートの評価だけに新単位元添加 $\widehat s$ を使う作業中です。英日本文・独立付録を改稿し、Gold学習器、主要特徴データ上界、希少型、倍化族、Yoshinakaとの対応を半群側へ移しています。

- [v82移行 Stage 1](revision/v82_semigroup_migration_stage1.md) ／ [v82移行 Stage 2](revision/v82_semigroup_migration_stage2.md)
- v82専用PDFビルド検査は履歴ブランチに保存。mainでは既存のPR検査とPDF公開を使用。
- main上の固定PDFは統合後の公開ワークフローでv83に更新する。過去のv81版は履歴として保持。

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

## 日本語査読版（v87 数学的同期版、構成圧縮は未実施）

v86からの日本語版にv87の主要な定理・証明変更を反映した対照版を
[`japanese/main_JP.tex`](japanese/main_JP.tex) に置きました。
有限アーベル群の独立付録と任意有限群の追加付録も
[`japanese/appendix_window_abelian_JP.tex`](japanese/appendix_window_abelian_JP.tex)
および [`japanese/appendix_window_group_JP.tex`](japanese/appendix_window_group_JP.tex) として訳してあり，本文から読み込まれます。
局所群の付録 `appendix_local_group.tex` と `japanese/appendix_local_group_JP.tex` も読み込まれます。
[`japanese/README.md`](japanese/README.md) に英語原稿の固定版，
対応検査，LuaLaTeX PDF のビルド方法を記録しています。
英語正本と日本語対照版をmain上で同時管理し、双方のTeXを更新する。

**#1 companion CFG paper:** [arXiv:1409.6247v5](https://arxiv.org/abs/1409.6247v5) — *Distributional Learning of Context-Free Languages under Fixed Finite-Semigroup Typing*. For exact R1 theorem locators, retain the [frozen TCS-D-26-00494R1 Clean TeX](https://github.com/growupkuriyama-hub/Papers/blob/bbbcabfd948dea815b94bd21a3d78999a6a3e54f/01_fixed-h-cfg/archive/tcs-r1-2026-10-22/TCS-D-26-00494_Manuscript_Clean.tex) (2026-10-22); the public arXiv release and TCS submission are separate version references.

## Historical v81 reference (not current main source)

- `main.tex` — **v87が現行正本**。v81は過去のI&C投稿準備版として比較できる： Davenport constants, order homogenization, effective characteristic data, rule-only witnesses, LG appendix, and LI∨Grp corollary. External mathematical review and author signoff remain open.
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
