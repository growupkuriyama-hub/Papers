# MCFG §§4–6 referee audit — 2026-10-28

## 対象と比較基準

英語版 `02_fixed-h-mcfg/main.tex` の `Characteristic-Data Bounds` (§4), `Further Quantitative Results` (§5), `Comparison with Multidimensional Substitutability` (§6) を、これらを大きく改稿した PR #89, #90, #91 の差分から点検した。同時に PR #92 で整理・短縮された Appendix A–F にある証明依存も追跡し、`japanese/main_JP.tex` と対応を確認した。§2・§3の質的再構成原理は既存の独立した査読（PR #86–#88）を前提にした。

## 今回の確定修正

**(1) §4冒頭のLG二分法の射程（中程度：誤解を招く量化）**
「exactly when this happens」は、個々の文法での指数的増大を判定するかのように読める。系 `cor:refinement-dichotomy` が示すのは**擬多様体に属する任意の固定全射typingについて、全てのreduced good Gにわたり多項式上界を一様に取れるか**という境界であり、個々の入力文法の増大の判定法ではない。英語・日本語ともこの量化を明示。

**(2) §4 refinement-baseline と Yoshinaka の鋭い型なし定数との相違（軽微〜中程度）**
`lem:typed-thickness-baseline` の表示は本稿の `Wit` に対し `C_s(G)` を含み、これだけで原著の `|K_G|≤|P|`, `||K_G||≤|P|θ_G` という鋭い係数を文字どおり回復したわけではない。多項式オーダーで先行結果と整合するが、証拠集合の構成と定数は同一ではないと区別。

## 依存関係の数学的点検

### §4 Witness / short representatives

- `lem:thickness-equivalence`: reduced+good の条件で、成功導出を使う規則厚さと非終端厚さの関係、各非終端の導出的受理文脈が成立する筋を点検。非消去性・子成分の非空性が重要。
- `lem:witness-length-template`: auxiliary monoid morphism \(\lambda\) が \(s\) を正語上で精密化するとき、非空成分の型付き持ち上げと証拠長計数を点検。\(C_s(G)\) はtyped非終端と規則の上界であり、特徴データの**個数**と**総符号長**を区別。
- `lem:heavy-node-count`: 同じ非終端名／\(\lambda\)-vector の祖先・子孫を短縮する最小性、重い節点の反鎖幅×パス長による節点計数を点検。
- `prop:block-replacement-interface`: 可換群は \(A^f\) での非空零和部分列、非可換群はAppendix Aの同一パターン抽出・順序均質化・複数行の同時区間選択を用いる。群値を各所有者ごとに保存する**必要はない**。Appendixの証明を完全に形式化したわけではない。
- `lem:marked-heavy-window-group`: marked boundary positionsを置換外に保持し、各根成分の順序付き群積を同時保存する論理を追跡。指数・係数の次数は \(O(\|G\|\bar\theta_G)\) を与える。
- `thm:local-group-polydata`: Appendix Cで得られる \(\beta_\lambda=O(\|G\|^2\bar\theta_G)\) と \(C_s(G)=O(\|G\|)\) の組合せからデータ \(O(\|G\|^3\bar\theta_G)\)。細分化の厚さに関するLG二分法とは別の主張。
- `cor:refinement-dichotomy`: 良形CFG由来の\(U_1\)型反例とLG側上界は、**full yield-type refinementの厚さ**に関する必要十分性。**characteristic-dataの下界ではない**。
- `prop:pattern-thickness-transfer`: 標準MCFGからgoodへの変換で、空成分patternごとの最短長を必要とする。sourceの\(\theta_H\)だけで一般に置換できないことを確認。

### §5 Rank-one / constructive / abelian-filtered

- `thm:rankone-polydata`: rank 1 の成功導出が単項鎖であり、最短鎖の型付き非終端が重複しないことから、typed witness長の多項式を得る。元の\(\theta_G\)もサイズで抑えられる。
- `prop:effective-char-data`: inside最短導出DAGとoutside文脈の最短路、rule-only budgetを点検。バイナリで短く持てる大きな長さの値と、実際の特徴語を全文字列に展開する時間を区別。
- `prop:mcfg-relaxed-witnesses`: 代表\(\iota(X)\)は非終端から導出可能でなくてもよいが、同じ分布同値類・同じ型の必要性が残る。
- `thm:mcfg-abelian-filter-data`: 有限半群型のregular fibreのParikh半線形性、\(\Lambda_T\) を用いる移動、整数非負解の小ささから指数\(3|\Sigma|+2\)が出る計数を確認。標的が特殊なabelian-filter表示を持つ場合の存在上界であり、任意の\(\Cmcf{f}{s}\)への主定理ではない。

### §6 Separation / feature sample / intrinsic rank

- `prop:feature-cross-typed`, `cor:feature-relation-family`: 同じ固定typingが全ての有限素性関係\(R\)を扱い、cross-serial長さの整合と許可対の認可を分ける。自明型とboundary-onlyの反例は明示的な文字列で確認。
- `prop:feature-family-witness-budget`: 4語/対の費用 \(7+9+9+11=36\)、二追加語の \(11+11=22\)、lower bound 7/対を点検。これは指定した集合駆動型作用素と全\(R\)を同時に扱う作用素に関する主張である。
- `lem:flag-separation`, `prop:lg-needed-target`, `prop:nonabelian-needed-target`: 値が一致する\(u,v\)と、許可・非許可の四語による分離を点検。これは**typingクラスの分離**であり短い特徴データを得るためにLG/非可換群が必要という下界ではない。
- `lem:rank-one-edt0l`, `thm:intrinsic-ranktwo-witness`: rank-one MCFGからfinite-index EDT0Lへの構成、\(\mathrm{MIX}_2\)を介する外部下界の依存を点検。2026年のBishop–Elder–Evetts–Gallot–Levineは無限巡回群の語問題が非EDT0Lであることを証明している。

## 独立に確認できた外部文献

- Yoshinaka / Clark の解説中のMCFGランク階層に \(\mathsf{MCFL}(2,2)=\mathsf{MCFL}(2,3)\) が記載されている。
- Bishop et al., *On groups with EDT0L word problem*, International Journal of Algebra and Computation (2026) の大学リポジトリと出版情報に非EDT0L結果が記載されている。

## なお残る検証上の限界

本査読は本文定理の論理・定数の伝播を主要な付録補題へ追う手作業の数学査読であり、非可換な順序均質化の全ての場合分け、正規化変換の全ての個別テンプレートや外部文献の全証明を形式証明化したものではない。ビルドの成功・定理ラベル一致は証明の正当性を保証しない。特に重大な新規下界や特徴データ長の必要条件を加える編集は行っていない。
