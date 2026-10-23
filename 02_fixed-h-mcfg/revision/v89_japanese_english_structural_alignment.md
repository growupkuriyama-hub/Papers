# v89: 英語版v88との日本語版完全構成同期監査

基準：GitHub mainの英文MCFG v88（38ページ）、日本語v88（55ページ）。
編集：PR #71、英語版は変更しない。

## 同期内容

- 第2節は正例学習、有限半群型付け、MCFG、タプル文脈の四項目。良形標準化をMCFG節に統合し、filling-identityを文脈節へ移動。
- 第3節は再構成、健全性、生成語型精密化、完全性、実効的再構成と保守的学習、Yoshinaka 2015の順序。semigroup-transferを型付き精密化に移動。Yoshinakaの定性系を英文と同じ「引き継ぐもの／引き継がないもの」の注意に再編集。
- 第4節は厚みと証拠語長、基準上界とランク1、窓＋補助不変量、有限群不変量、代数的判定、実効的特徴データ、分布代表元とアーベル型フィルタの七項目。
- 英文の厚みの三つのラベルは、日本語でも単一の補題に集約。共通 witness-length template と type-preserving replacement を先に配置。
- 窓スケルトン補題の本来の一般形（有限モノイド不変量を伴う窓、可換性を要しない積の保存）を維持し、旧アーベル・群固有の短縮ラベルを同じ補題に対応させた。
- finite-group invariant の節に heavy-node-count、任意有限群の prescribed-type short tuple theorem、window-group theorem、window-abelian theorem を英文と同じ順序で配置。群の可換性は零和の場合だけ要求。
- Rule-only witnessesとcomputable budgetを一命題に統合（両ラベルに一つの命題が対応）。
- 正規化付録には、英文の「非消去化・非置換化・空成分除去・非融合化」の四段階タプル言語恒等式を一補題として配置。
- 二つの旧日本語群論付録を本文の入力から外し、Appendix Bを新たな `appendix_group_blocks_JP.tex` に統合。可換の場合の零和証明、非可換の場合のブロック順序均質化・区間置換はともに完全な日本語証明で保持。旧2付録は履歴資料としてリポジトリに残し、ビルド対象から除外。
- LG付録は主要な定理、群ブロック値の非可換な順序、局所群の特徴づけ、擬多様体の帰結を保持。
- GitHub Actionsの英日検証と公開時stale-source guardに新日本語付録を追加。

## 対応表・機械的整合検査

英文の `\label` 105個はすべて日本語現行入力ファイル側にも存在する。
日本語版には、証明をより明示的にする以下の補助項目が意図的に残る。
- `lem:composition-witness-materialization`
- `lem:general-witness-enumeration`
- `def:output-map`
- `lem:signature-contexts`
- `lem:reusable-context-bound`
- `subsec:rankone-polydata`
- `lem:type-filter`

いずれも英文と異なる主要結論を主張するためではなく、定義・導出・計算量の内訳を日本語で明示するためのもの。
現行日本語入力（main_JP.tex、group_blocks_JP.tex、local_group_JP.tex）では、未定義 \\ref は0件、重複 \\label は0件。
旧非入力付録が一部ラベル名を共有するのは履歴ファイルとして意図的であり、コンパイル対象ではない。

## 数学的安全性と限界

- R1訂正：計算可能な導出的代表元の最短証拠集合へ、導出不能な緩和分布代表元に関する存在的な総文字数上界を転用しない。
- 文法ランク0・空語・正語像半群と新単位元添加の区別、正規化時のfan-out/rankの保存を維持。
- arbitrary finite groupの非可換積は交換しない。アーベル零和短縮と一般有限群の順序均質化を区別。
- Appendix CのLG-shorteningでは、長い成分のγ群積と短い成分の文字列同一性を区別。
- 日本語と英語は主定理、仮定、評価次数、依存ラベル、節・付録の位置づけを合わせたが、日本語の説明が英文と文字単位で一対一ではない。両言語の独立した最終数学査読・全頁ビジュアル校閲・著者の投稿判断はなお必要。

I&Cへの投稿やarXiv更新は本PRに含まない。
