# #2 の査読：#1（TCS-D-26-00494）第1回査読の観点を当てた模擬査読

- **対象：** `02-v2-lg-fanout-boundary/main.tex`、コミット `1343abb`（README (164)）。42ページ。
- **基準：** #1 の第1回査読（`01_fixed-h-cfg/response/response_round1.tex` に引用された Editor E.1、Reviewer 1 の R1.1–R1.37、Reviewer 2 の R2.1–R2.11）。同じ編集者・同じ査読者に回る可能性を想定し、彼らが #1 で突いた**型の指摘**を #2 に当てた。
- **限界：** 改訂を手がけた側（Claude）によるレビューなので、独立査読の代わりにはならない。行番号は上記コミットのもの。

## 0. #1 の査読者が何を見ていたか（要約）

| 査読者 | 主な関心 | 代表的な指摘 |
|---|---|---|
| Editor E.1 | 学習部分の正しさ | 「表現の問題が科学的内容に漏れている、特に学習部分」 |
| R1 | 学習アルゴリズムの正しさ、定義の完備、用語の氾濫、長すぎる証明、定理文の余計な言葉、記号の衝突 | R1.24（学習器が収束しない＝致命的）、R1.7（学習器と構成アルゴリズムの混同）、R1.8/1.9（定義のない用語）、R1.13（定理文から技術的に不要な語を除け）、R1.22（自明な系）、R1.32（民間伝承の命題に2ページ）、R1.33（文字・記号の選択） |
| R2 | 設定の意義、型付けが満たすべき条件、クラスの広さ、使われない定義、使用前の参照 | R2.1（型付けの条件を研究せよ）、R2.2（どの証明にも読まれない成分）、R2.3（クラスはどれだけ広いか）、R2.4（使用前の参照、繰り返し）、R2.6（使われない定義）、R2.11（正規化は付録へ） |

**総評（模擬）：** 主結果（定理 A–C）と下界の論理に誤りは見つからなかった。#1 で致命傷になった型の誤り（学習器の非収束）は #2 にはない。一方、R1・R2 が #1 で繰り返し突いた**表現上の型**、つまり用語と記号の過多、定理文に混ざった注釈、使われない定義、クラスの広さの説明不足が #2 にも残っている。模擬判定は **minor〜major revision の境目**。M1–M3 を直せば minor に寄る。

---

## 1. 主要な指摘（Major）

### M1. クラスの広さが示されていない（R2.3 の型）
#2 が示す要素は、有限言語（定理 B・C の族）、正則言語 ŝ⁻¹(Acc)、それらの共通部分だけである。読者には次が分からない。
- (a) 非自明な型付きクラス C^mcf_{f,s} は、Yoshinaka の多次元置換可能クラス C^mcf_{f,s_triv} より**真に**大きいのか（包含は項目 (a), 646行）。
- (b) f≥2 で、文脈自由でない要素が実際にあるのか。
- (c) f≥2 で、局所群の型付けが追加で何を学習可能にするのか。

#1 の R2.3 は、線形の場合について「クラスの範囲が不明なので技術的強化に見える」と書いた。#2 でも同じ反応が予想される。

**提案：** 例を一つ置く。材料はすでに原稿にある。`prop:abelian-coset-filter`(ii)（677行）は現在、自明群でしか使われていない。これを使って、例えば {aⁿbⁿcⁿdⁿ} 型の 2-MCFL と偶奇の共通部分を作り、自明な型付けでは置換可能でないが群の型付けでは置換可能な 2-MCFL を一つ示す（証明が要る）。退避した `prop:feature-cross-typed` や `sec:comparison` の一部を戻す手もある。これは削除ではなく、主張を支える最小の例の追加である。

### M2. 用語の重複と記号の衝突（R1.8・R1.9・R1.33 の型）
R1 は #1 で「用語の氾濫そのものが読者の負担になる」と書き、`{d,u,;}` の文字選択まで指摘した。#2 には次がある。

**同じ物に複数の名前：**
- `(k,ℓ)-boundary-determined` / `boundary typing` / `window typing`（531–533行）。
- `local-group typing` が二つの意味で使われている。定義 `def:local-group-typing`（1595行）では λ_{k,ν} 自体を指す。一方、節題や定理名（「Local-Group Typings」「local-group typings at every fan-out」）では「正の像が LG である typing s」を指す。

**記号の多重使用（重い順）：**

| 記号 | 意味 |
|---|---|
| λ | 補助的なモノイド準同型 λ、Rees 座標 λ∈Λ（付録 B）、λ-free |
| τ | 代表長 τ_X・τ(G,s)、LI∨Grp 補題の準同型 τ:Σ⁺→S′、Yoshinaka の τ_G（1060行） |
| h | 補題の準同型 h、`thm:doubling-no-lift` の準同型 h、印の数 h=f(k+ℓ+1)、短縮の原理の h、マーカー添字 d_h |
| k | 窓の長さ、族の添字 L^{(f)}_{q,k}、`lem:order-homogenize` の k:=\|𝒪\|（2379行） |
| ρ | テンプレート、LI∨Grp 補題の準同型 ρ=(τ,g) |
| N | N_{G,f}、有限モノイド 𝖭、N_typ、Lemma 2380 の N、N_0 |
| c | 群定数 c_{G,f}、文字 c、短縮の原理の c |
| e | 冪等元、出力のアリティ e、型の数 e（`lem:group-block-order`） |
| d | アリティ d、Davenport の 𝖽、冪移動の周期 d、マーカー文字 d_h |
| q | 周期 q、語数 q、ブロック数 q_ϱ、ランク q |

**提案：** 補題の内部でしか使わない局所的な記号（印の数 h、`lem:order-homogenize` の k、LI∨Grp 補題の τ・ρ、族の添字 k）を別の文字にする。名前の重複は、boundary typing を window typing に一本化し、λ_{k,ν} を「sliding-factor typing」などと呼び分ける。

### M3. 定理文に注釈が混ざっている（R1.13 の型）
R1 は「技術的に不要な語は、特に定理文から除け」と書いた。#2 の定理・補題の本文に次の注釈文がある。どれも正しいが、主張ではない。
- 943行 `prop:completeness`：「Neither substitutability nor ι(X)∈L_X is assumed; ι=ω is the case …」
- 1143行 `lem:witness-length-template`：「Items (i)–(iii) do not use substitutability.」
- `thm:data-from-typed-thickness`：「The numerical length estimate holds for any typing; substitutability is used only for …」
- 882行 `lem:typed-homogeneity`：「This semantic class notation is distinct from …」
- 1448行 `prop:block-replacement-interface`：「Individual block or owner values need not be preserved.」
- 2690行 `lem:local-group-shortest`：「Substitutability is not used.」
- 690行 `prop:abelian-coset-filter`：「Such factorizations are not supplied to the learner.」
- `thm:window-group-polydata`：「The group may be noncommutative and its blocks may interleave …」

**提案：** すべて定理環境の外、直後の地の文に出す。内容は消さない。

### M4. 「learner」と「operator」の混同（R1.7 の型）
R1 は #1 で「学習アルゴリズムと、それが使う文法構成アルゴリズムを混同している」と指摘した。#2 の本文は set-driven **operator** と conservative sequential **learner** を区別している（`def:characteristic-sample`, `def:conservative-learner`）。ところが要旨（94–95行）は「for every set-driven **learner** that has characteristic samples throughout the class」、導入（201行）は「for set-driven **learners**」と書いている。

**提案：** 要旨と導入を「set-driven operator」（あるいは「set-driven learning algorithm, i.e. a map from finite samples to grammars」）に揃える。下界は sequential learner の収束段階には何も言わない。この点は Scope の段落にあるが、要旨の語がそれと食い違っている。

---

## 2. 中程度の指摘（Moderate）

### m1. 使われない定義・結果（R2.6・R2.2 の型）
R2 は #1 で「基底 B(G̃) は一度も使われない」「どの証明にも読まれない成分」を突いた。#2 で後に一度も参照されないもの：
- `boundary-typed`（648行）：定義だけで使用 0 回。
- `lem:boundary-short-canonical`（1510行、窓の系）：引用 0 回。
- `lem:typed-thickness-equivalence` と θ_typ（1150–1170行）、`lem:witness-length-template`(iii)：この補題にしか使われない。
- `prop:abelian-coset-filter`(ii)：自明群の場合しか使われない（M1 で使えば解消）。
- `lem:semigroup-transfer`(ii)：地の文の注意でしか使われない。

**提案：** 著者方針（省略しない）に沿って、消すのではなく位置づける。「boundary-typed」は語ごと不要。窓の系は窓–群定理の一文にする。θ_typ は `thm:data-from-typed-thickness` の後の注意（Yoshinaka の thickness との比較）として一段落にまとめる。abelian 篩は M1 の例で使う。

### m2. §5.2 は §5.3 の特別な場合（R1.31 の型）
R1 は #1 で「先行節の議論の特別な場合で、ずっと短くできる。説明が長すぎると焦点がぼける」と書いた。#2 では、窓–群 typing は局所群 typing の特別な場合である（`prop:li-g-strict`(i)）。§5.2（窓–群の補題・定理・注意・前史の段落）は、定数が明示されている点を除けば定理 A に含まれる。

**提案：** §5.2 の定理を定理 A の系（明示定数つき）に格下げする。f≥2 の新規性（owner-wise 置換）は `prop:block-replacement-interface` に集約されているので、主張は失われない。

### m3. 定理 B(ii) の上界は Yoshinaka の既知結果（R1.1・R1.3 の型、帰属）
主定理 B(ii) の前半「自明な typing では O(‖G‖θ̄_G)」は、本文（1188–1193行）が認めるとおり、Yoshinaka 2011 の |K_G|≤|P|, ‖K_G‖≤|P|θ_G に含まれる。新しいのは「この上界が定数倍まで達成される」という後半だけである。主定理の文で帰属が見えないと、新規性の過大表示と読まれうる。

**提案：** 主定理 B(ii) を「Yoshinaka's bound O(‖G‖θ̄_G) for the trivial typing [Yoshinaka2011] is attained up to a constant factor」の形にする。

### m4. 「典型的な typing」の例が定理 A の範囲外を含む（R2.1 の型）
導入（136行）は典型例に「DFA transition morphisms」を挙げている。しかし、恒等的に作用する文字とリセット文字を持つ DFA の遷移半群は {恒等, 定数}≅U₁ を含み、LG に入らない。R2 は #1 で「型付けが満たすべき条件を研究せよ」と書いた。#2 はまさにその答え（定理 C）なので、どの典型例が LG に入り、どれが入らないかを導入で一言示すと、R2.1 への直接の回答として効く。

**提案：** 「windows (LI), groups, their products and sliding-factor typings are local groups; transition morphisms of DFAs with a reset are not」程度の一文を足す。カバーレターでも、R2.1 への回答として #2 を位置づける。

### m5. IPTtD の否定を「set-driven」に限る必要があるか（E.1・R1.7 の型、強化案・要確認）
`cor:iptd`(ii) は「no set-driven algorithm」と書いている。EHY 2016 の Definition 2.12 では、アルゴリズムの入力は標本（有限集合）なので、そこで考えるアルゴリズムは定義上 set-driven のはずである。そうなら (ii) は「no algorithm」と書けて、主張が強くなる。

**要確認：** EHY の Definition 2.12 で、標本が集合か列か（Eyraud の HDR の該当ページで確認）。

### m6. 正規化の付録（R1.32・R2.11 の型）
R1 は #1 で「既知の制限の組合せで民間伝承なのに2ページ」と書き、R2 は「付録で圧縮可」と書いた。#2 の付録 E は約1.5ページで、正しさは既知の構成の引用、サイズの数え上げは自前である。

**提案：** 表（各段階のコピー数）と、段階 (c)（空成分）の恒等式だけを残し、(a)(b)(d) の証明文は引用で済ませる。著者の「省略しない」方針と衝突する場合は現状維持でよい。ただし R1 が同じ反応をする可能性は高い。

### m7. 繰り返される限定句（R2.4・R1.17 の型）
R2 は #1 で「trimmed なので到達可能かつ生産的なのは定義から。毎回繰り返すのは長くするだけ」と書いた。#2 では「Let G be reduced and good」などの限定が節の冒頭と各補題の両方にある。§4 冒頭（1019–1022行）で G を固定しているのに、`lem:thickness-equivalence` が「Let G be reduced and good」と繰り返している。

**提案：** 節冒頭の約束に一本化し、補題では繰り返さない。

---

## 3. 軽微な指摘（Minor）

1. **「fixed」が58回出る（R1.10 の型、#1 R1 は「h が固定であることを過度に強調」と書いた）：** 要旨・導入・Scope・表で同じ断り書きを繰り返している。Scope の段落に一度まとめ、他は減らせる。
2. **導入で定義前の語を使っている（R2.4 の型）：** 「Const/Link/Comp reconstruction operator」（151行）、「reduced good presentation」「positive image」が定義前に出る。導入なので許容範囲だが、Const/Link/Comp は「Yoshinaka's reconstruction operator」と言い換えれば足りる。
3. **`def-monoid-morphism` などの古いラベル：** 一つの定義に3ラベルが付いている（476–478行）。出力に影響はないが、整理するとよい。
4. **主定理 C(ii) と `thm:fanout-one-data`(iii)、`prop:three-letter-family`(iv) の三重記述：** 同じ下界が3回述べられている。本文の定理は主定理を参照するだけにできる。
5. **R1.37 の型：** 「C^mcf_{f,s} と Clark–Yoshinaka の congruential MCFG の関係」は、`lem:typed-homogeneity` の後に一文あるだけである。包含関係の向き（反例の有無）を一言足すと、R1 型の査読者が満足しやすい。

---

## 4. 確認した正しさ（E.1 の観点）

- **学習器の収束（#1 で致命傷だった R1.24 の型）：** 保守的学習器 `def:conservative-learner` と `cor:gold-explanatory` の議論は正しい。特性標本が現れた後に仮説が変われば新しい仮説は正しく、変わらなければ健全性と「すべてのデータを生成する」ことから正しい。
- **`lem:distinguishing`、`prop:rare-type`：** 正しい。
- **数値の検算（すべて一致）：**
  - `prop:linear-factor-all-fanout` のサイズ式 (7f+11)q+6k+3f+10：非終端 2q+k+3 と各規則サイズから再計算。
  - `prop:three-letter-family`：‖G_n‖=13n+7、θ̄=4n。
  - `prop:typed-thickness-exponential`：θ_{G_n}≤2。
  - 結論の例：‖G_n‖=10n+16、θ̄=2、b^{n+1} が A_n の型 ⟨b,b⟩ の唯一の yield、τ≤2。

## 5. 優先順位

| 順 | 項目 | 作業量 | 効果 |
|---|---|---|---|
| 1 | M4 learner/operator の統一 | 2か所 | R1.7 の再来を防ぐ |
| 2 | M3 定理文の注釈を外へ | 8か所 | R1.13 |
| 3 | m3 定理 B(ii) の帰属 | 1文 | 新規性の過大表示を防ぐ |
| 4 | M2 用語・記号の整理 | 中 | R1.8/1.33 |
| 5 | m1 使われない定義の位置づけ | 小〜中 | R2.6 |
| 6 | m4 典型例と LG の関係 | 1文 | R2.1 への直接回答 |
| 7 | M1 クラスの広さの例 | 中（証明が要る） | R2.3 |
| 8 | m2 §5.2 の系への格下げ | 中 | R1.31 |
| 9 | m5 IPTtD の強化（要確認） | 小 | 主張の強化 |
| 10 | m6, m7, Minor | 小 | 読みやすさ |
