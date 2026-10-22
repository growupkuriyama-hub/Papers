# #2 MCFG v82-stage2 — 日本語査読用作業稿

対象論文: *Positive-Data Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing*（I&C 投稿準備中、未投稿）

英語版 `../main.tex` と付録が**数学的な正本**です。日本語版は独立査読・定理の仮定の確認用であり、英語版と同じ数学的主張・同じ `\\label` の集合を保ちます。

## v82半群化作業（2026-10-22）

TCS #1 R1に合わせて $s:\Sigma^+\to S$ を基本型、$\widehat{s}:\Sigma^*\to S^\sharp$ を生成語計算用とする改稿を実施。非空成分に限った既存のMCFG代入可能性は変わらない。学習定理、二次・三次上界、希少型、Yoshinaka対応と結論節の配置を英日で対応させた。3本の独立付録（局所群を含む）にも読み替えを明記した。

**本作業稿は主張と証明の最終独立監査が未了であり、mainブランチの既存PDFはv81のままです。** 詳細：[`../revision/v82_semigroup_migration_stage2.md`](../revision/v82_semigroup_migration_stage2.md)。

## v75 の更新（2026-10-18）

- 要旨の「同じ多項式次数」を修正し、窓のみ `O(||G||^2 θ̄_G)` と窓＋任意有限群 `O(||G||^3 θ̄_G)` を区別。
- #1 CFG 関連原稿の指数下界を、公開 GitHub の**特定コミット** `834e99a1f35b4a5fb949acc55a080658388d4480` に固定して引用。arXiv v5 は未公開で、公開後に別途追記する。
- 任意有限群の付録Dで、block-order の逆方向の場合分け、Ramsey 抽出の最終頂点を明示し、一般群用の独立した短い正準タプル補題 `lem:window-group-short` を追加。
- 日本語版の `r_max>=1` 仮定漏れ、参照先の「付録 付録 X」重複を修正。
- 先行研究として Duncan–Elder–Frenkel–Lyu (2026) の MCFL 非所属のための置換補題との目的の違いを追記。

## ファイル

- `main_JP.tex` — 日本語全文（要旨、本文、既存の通常の付録、Yoshinaka 比較、文献）
- `appendix_window_abelian_JP.tex` — 可換有限群の零和証明
- `appendix_window_group_JP.tex` — 非可換群を含む任意有限群の Ramsey 型短縮・総長上界の証明
- `../revision/v74_to_v75_final_referee_hardening.md` — 変更履歴・査読ゲート

## 対応する英語正本

- `../main.tex`
- `../appendix_window_abelian.tex`
- `../appendix_window_group.tex`

## ビルド

```bash
cd 02_fixed-h-mcfg/japanese
latexmk -lualatex -interaction=nonstopmode -halt-on-error main_JP.tex
```

両言語をコンパイルする pull request 検証ワークフローは
`../../.github/workflows/verify-mcfg-bilingual-pr.yml`。
main への反映後には `publish-mcfg-bilingual-pdf.yml` が英日PDFを
`../main.pdf` と `main_JP.pdf` に公開します。

機械的な文法検査・ビルド合格は、翻訳の完全一致や数学的正しさの形式的証明を意味しません。