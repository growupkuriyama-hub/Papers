# 指摘一覧（重大度順）

主定理を崩すcriticalな数学的反例は未発見。以下のmajorは主に新規性と先行研究の位置づけに関するもの。各修正の詳細証明はREVIEW_REPORT.md。

## I-01 — major：Theorem Bの主な結論が著者先行稿から既に導ける

- **位置**：163–170行 `main:B`（監査用ID）；628–668行 `thm:uniform`；670–687行 `rem:uniform-known`。
- **問題**：675–676行は全観測の合併をuntyped learnerが扱えることを新しい点とする。しかし添付先行稿Prop.9.7は既に全固定sについてCONGへの包含を示す。その証明をbinary CFGから始め、congruential→weak 1-FKP、KY2017 Thm.6を適用すれば同じr=2,k=1の学習器を得る。
- **修正**：先行稿Prop.9.7、Yoshinaka2015 §6.3、KY2017 Thm.6を明記して系と位置づける。型付き表示を説明する独立証明を残してもよいが新規定理と数えない。
- **確信度**：high。先行稿の命題と証明を直接確認。既刊性までは主張しない。

## I-02 — major：観測の比較を先行研究が扱っていないという記述が過剰

- **位置**：135–147行 `sec:intro`、405–430行 `prop:learners`。
- **問題**：Yoshinaka2015 §8はsignatureの拡張、有限sort refinement、対応する可学習クラスの比較を明示している。「neither framework addresses」の一般的否定は不正確。
- **修正**：§8を引用し、その比較と、本稿のSPP・homogeneous-kernelの反単調性・具体的分離を区別する。§6.4のweak FCP十分性をvery weak FCP必要十分性と混同しない。
- **確信度**：high。

## I-03 — minor：product規則の型積で中間terminal blocksを脱落

- **位置**：297–318行 `lem:product`、特に304行。
- **問題**：表示どおりの式はw1,…,w_{n−1}の型を掛けない。S→AcB, A→a, B→bとc-indicatorで型不整合になる。
- **修正**：ν=ĥ(w0)ν1ĥ(w1)…νnĥ(wn)。反例詳細はcounterexamples/product_formula.md。
- **影響**：字面どおりなら補題は偽だが意図の明確な式修正で全依存定理が回復するのでCORRECT-WITH-FIX。
- **確信度**：high。

## I-04 — minor：任意kのstrictnessに対し本文の証人はk=2のみ

- **位置**：151–161行 `main:A`；530–531行 `sec:strict`；564–611行 `prop:strict-kernel`。
- **問題**：Main Aのk≥1という量化のままstrictと読むと、元のL_Kの上界k2ではk1が未証明。さらに「both chains」がuntyped–s0の端点包含までstrictと読める。
- **修正**：二つの初期記号S+,S−を使い、S+→a|z|aS+|aS+b、S−→b|y|S−b|aS−b。生成言語はそれぞれ{z}closure,{y}closureで、s0-typed strong 1-FKP。h側非存在は同じ証明。strictnessはs0対indicatorのtyped包含であると限定する。
- **確信度**：high。数学的証明と有界計算を併記。

## I-05 — minor：学習器の移植証明に正規化・出力sortの説明が不足

- **位置**：405–430行 `prop:learners`、386–403行 `def:typed-props`。
- **問題**：性質定義は空C,Kを許し、学習器は非空に限る。またfibresだけをsortとする説明にはYoshinakaのdistinguished output sortがない。「verbatim」ではこれらを処理できない。
- **修正**：trimして空Kをyield singleton、空Cを到達context singletonに置換。dualのdenotation⊆Sub(L)、primalの反駁context∈Con(L)を説明する。sortedの対応にはoutput sortと埋込みを追加するか、KY2017の直接移植を主証明にする。
- **確信度**：high。結論の反例ではない。

## I-06 — minor：H_nの存在しない子コピーを除く規約が未記載

- **位置**：728–734行 `prop:deletion-upper`。
- **問題**：i=1で(E0,ζ)は存在せず、type1 floor規則にはi≥1が必要。
- **修正**：全iの範囲と「表示した非終端記号集合の中に全ての子が存在する規則だけを含める」を明記。
- **確信度**：high。

## I-07 — minor：表示サイズと最大証人長の指標が曖昧

- **位置**：174–182行 `main:C`；723–734行 `prop:deletion-upper`；853–872行 `rem:deletion-table`。
- **問題**：文法size O(n)、最大context長 O(n)、context総文字数 O(n²)は違う。kernel下界もρ|N|max(κ,1)であり、文法単独の下界ではない。
- **修正**：表に「grammar size / maximum witness length」を明記。初期記号S0のwitnessも一言補う。
- **確信度**：high。

## I-08 — minor：EXREGのguardとparameter対応を省略している

- **位置**：432–441行 `rem:exreg`。
- **問題**：集合としての包含は正しいが、学習器の適用にはguarded expressionと単一開始記号への対応が必要。
- **修正**：非空Cについて式sizeは2|C|+b_μ。空Cを到達contextで補い、開始記号を追加。rank≤max(r,1)、parameter≤max(1,2k+max b_μ)。KY2023 Lemmas 2,4、Thm.6を引用。
- **確信度**：high。

## I-09 — minor：未解決問題内の部分下界の定義と証明が省略

- **位置**：899–906行 `op:Mn-context`。
- **問題**：single-ζ-node、j、ℓの意味、O項の定数が説明されず「what we can show」の証明がない。
- **修正**：ceiling規則がちょうど1回、level jの節点と定義し、|x|≥|w_n*|−ℓ−|w_{j−1}*|を証明する。REVIEW_REPORT §10に短い補完証明を示した。open problem全体を解いたとはしない。
- **確信度**：high（明示した解釈に対して）。

## I-10 — minor：計算範囲・seedの再現性の説明

- **位置**：924–938行 `app:comp`；付属check_reduction_identity.py。
- **問題**：4000 trial×5型ではなくtrialごとに一型を選ぶ。ε・空K・共通文脈なしclosureは著者scriptでは未検査。set順序がrandom sampleを変えるためseedだけではrule件数を固定しない。
- **修正**：sampling条件とseed、hash順序依存性を記載し、リストをsortして乱数選択する。今回の実測値は4000 identity、2186 rule tests、反例0。
- **確信度**：high。

## I-11 — minor：書誌・主張の強さ

- **位置**：967–984行、997–1000行；470–473行 `lem:reduction`後；513–525行 `cor:primal-dominated`。
- **問題**：KY2017刊行情報が未完成。Yoshinaka2015の正式題名は単数の「General Perspective on Distributionally Learnable Classes」。本文のprimal dominationを速度比較と読む余地がある。
- **修正**：KY2017はpp.77–88と刊行巻情報を確認して補う。著者版番号を用いることは維持。Yoshinaka題名を修正。支配は質的可学習クラスの包含であり同じtext上の早さではないと明記。
- **確信度**：high。刊行巻番号を今回未確認のまま推測して挿入しない。
