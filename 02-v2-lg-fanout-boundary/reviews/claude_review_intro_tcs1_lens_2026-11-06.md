# #2 序論（§1）の査読：#1（TCS-D-26-00494）第1回査読の観点

- **対象：** `02-v2-lg-fanout-boundary/main.tex` §1（Introduction）、コミット `1417ad3`（README (172)、要旨の改稿直後）。PDF で1〜5ページ。地の文 1568語（表を除く）、表2つ。
- **基準：** #1 の第1回査読（R1 の回答書に引用された E.1、R1.1–R1.37、R2.1–R2.11）。特に R1.2（定義のない用語・長さ）、R1.3（分野での位置づけ、技術偏重）、R1.5（序論で意味の分からない用語、技術的細部を貢献に数えるな）、R1.29（主張を数学的に書け）、R2.1（設定の意義）、R2.4（使用前の参照、繰り返し）。
- **前回の模擬査読との関係：** `reviews/claude_review_tcs1_lens_2026-11-06.md`（README (165)）のうち、M1〜M4、m3〜m5 は (166)〜(169) で対応済み。本稿はそれ以降の序論だけを扱い、未対応の項目（前回の Minor 2・4）はここで再掲する。
- **照合したもの：** 主定理 A〜C と `thm:local-group-polydata`、`prop:linear-factor-all-fanout`、`def:uniform-polydata`、`thm:fanout-one-data`、`cor:iptd`、`prop:typed-separation`、`thm:doubling-no-lift`、`prop:li-g-strict`、§4.1 の厚さの定義。表1の #1 側の番号は、Project に置いた R1 の clean tex（`TCS-D-26-00494_Manuscript_Clean.tex`）で確認した。
- **限界：** 改訂を手がけてきた側（Claude）の査読なので、独立査読の代わりにはならない。Yoshinaka 2011 の §4.3 の厚さの定義そのものは今回は原典で確認していない。

## 段落ごとの分量

| 段落 | 語数 | 所見 |
|---|---:|---|
| 冒頭 | 144 | 問いの後半（ファンアウト依存）に本稿は答えない（M1） |
| The setting | 322 | 6つの話題が一段落に混在（M4） |
| Main results | 285 | 定理文が不完全（M2） |
| The remaining question | 105 | 推測文が誤解を招く（M1） |
| Approach | 277 | 未定義語が密集（M3） |
| Relation to prior work | 98 | Const/Link/Comp が未定義（前回 Minor 2） |
| Relation to the companion | 107 | ＋表1（9行） |
| Scope of the claims | 120 | ＋表2（8行）、定理文と重複（M5） |
| Organization | 87 | |

---

## 1. 主要な指摘（Major）

### M1. 冒頭の問いの後半に本稿は答えない。結びの推測文は誤解を招く（R1.3・R2.1 の型）
- 冒頭の問いは「for which comparison biases is this length polynomial, **and does the answer depend on the fan-out?**」。後半は Open Problem のまま残る。答えない問いを看板に掲げると、査読者に「未完成」と書く材料を渡す。
- 「The remaining question」の最後の文「A typing that needs superpolynomial data at fan-out one but polynomial data at fan-out two would show that raising the fan-out can make learning strictly cheaper」は推測であり、しかも誤解を招く。`thm:doubling-no-lift` が示すとおり、ファンアウト2ではタプルの代入可能性が強い条件になり、困難な CFL の族がクラスから**出ていく**。「安くなる」のは主にクラスが縮むためで、学習が強くなるからではない。査読者がこの点を突けば、文全体の信用が落ちる。

**提案：** 問いを「for which typings is this length polynomial?」に絞る（要旨 (172) と同じ）。ファンアウトは「答えが CFG で完全に決まり、MCFG では上界側が全ファンアウトに持ち上がる」という構成で語る。推測文は削除する。

### M2. 主定理の文が不完全（R1.29「Make the statement mathematical」の型）
1. **定理A：** 次の3点が文に書かれていない。
   - どの作用素についての特徴標本か（本文の定理は $\mathcal B^{\le r_{\max}}_{f,s}$ と $\mathcal B_{f,s}$）。
   - $G$ が $L\cap\Sigma^+$ のファンアウト $\le f$、ランク $\le r_{\max}$ の表示であること。
   - 定数が $f,r_{\max},s,\Sigma$ に依存すること。

   また前置きの「a rule-rank bound $r_{\max}\ge2$」が定理Aにもかかるが、`thm:local-group-polydata` は $r_{\max}\ge1$ で成り立ち、表2も定理Aでは $r_{\max}\ge2$ を要求していない。
2. **定理C(i)：** 「uniform polynomial characteristic-data length」が序論では未定義。この概念の中身は量化子の順序（多項式は型付けごとに選んでよいが、標的や表示には依存しない）だけで、それを書かないと主張が読めない。
3. **定理C(ii)：** $U_1$ が序論で定義されていない（The setting で「a copy of $U_1$」と名前だけ出る）。
4. **前置き「Fix the alphabet, the fan-out $f$ …」と定理Cの「Let $f=1$」が重なる。**
5. **同じ下界の三重記述（前回 Minor 4、未対応）：** 主定理C(ii)、`thm:fanout-one-data`(iii)、`prop:three-letter-family`(iv)。

**書き換え案（定理Aと定理C(i)）：**

> **Theorem A (Local groups).** Let $r_{\max}\ge1$ and suppose $s(\Sigma^+)\in\mathbf{LG}$. For every $L\in\Cmcf{f}{s}$ and every reduced good presentation $G$ of $L\cap\Sigma^+$ of fan-out $\le f$ and rank $\le r_{\max}$, the operators $\mathcal B^{\le r_{\max}}_{f,s}$ and $\mathcal B_{f,s}$ have a common characteristic sample for $L$ of total length $O(\|G\|^2\bar\theta_G)$; the constant depends only on $f$, $r_{\max}$, $s$ and $\Sigma$.

> **Theorem C(i).** Let $f=1$, $r_{\max}\ge2$, and let $\mathbf V$ be a pseudovariety of finite semigroups. Then $\mathbf V\subseteq\mathbf{LG}$ if and only if for every typing $s$ with $s(\Sigma^+)\in\mathbf V$ there is a polynomial $p$, depending on $s$ but not on the target, such that every $L\in\Cmcf{1}{s}$ has a characteristic sample for $\mathcal B^{\le r_{\max}}_{1,s}$ of length at most $p(\|G\|,\bar\theta_G)$ for each of its reduced good presentations $G$ of rank $\le r_{\max}$.

（$\mathcal B$ の記号を序論に出したくなければ「Yoshinaka's reconstruction operator with typed links」を一度定義して、それを指す。）

### M3. 定義前の用語が約20個ある（R1.5・R2.4 の型）
R1 が #1 で最も強く突いた点（「at this point the text uses many terms whose technical meaning has not yet been made clear」）が、序論にそのまま残っている。序論で定義も言い換えもなく使われる語：

- **代数：** pseudovariety、$\mathbf{LG}$、$\mathbf{LI}$、$\mathbf{Grp}$、$\mathbf{LI}\vee\mathbf{Grp}$、$U_1$、positive image
- **文法：** reduced good presentation、$\mathsf{MCFL}(f,r_{\max})$、tuple-substitutable（定義番号の参照のみ）
- **学習：** typed links、Const/Link/Comp（前回 Minor 2、未対応）、IPTtD（表2で略号のみ）、canonical / class-wide（表2の caption で定義）、$s_{\mathrm{triv}}$
- **証明手法（Approach）：** full yield-type refinement、distribution-equivalent representatives、owner-wise、owners、sliding factors、rare types、marker families、two-hole transfer of powers

**提案：**
- 代数の語は The setting で一度だけ定義する：「a finite semigroup $\mathsf S$ is a *local group* if $e\mathsf Se$ is a group for every idempotent $e$; $\mathbf{LG}$ is the pseudovariety of local groups; $U_1=\{1,0\}$ is the two-element semilattice」。$\mathbf{LI}\vee\mathbf{Grp}$ は companion の段落で「divisors of products of a locally trivial semigroup and a group」と一句添える。
- Approach の手法名は、名前を出さずに中身を一文で言うか、本文へ回す（M6）。

### M4. The setting（322語）に6つの話題が一段落で詰まっている（R1.2 の型）
次が一段落に並んでいる：(1) 型付けとクラスの定義、(2) 型付けで真にクラスが広がる例（`prop:typed-separation`）、(3) 型付けバイアスの文献（Coste、Takada、Coste–Nicolas）、(4) 典型的な型付けの列挙と $S_3$ の非可換性、(5) 局所群の定義と ab の偶奇の例、(6) DFA の遷移半群が $U_1$ を含む例。

**提案：** 三段落に分ける。
- **(a) 設定**（約100語）：(1)＋(3)。
- **(b) なぜ型付けか**（約60語）：(2)。#1 の R2.1（「設定の意義が不明」）への答えになっている部分なので、独立させて目立たせる。
- **(c) どの型付けが局所群か**（約120語）：(4)〜(6)。M3 の定義もここに置く。定理Cの読み方（「窓・群・その積・sliding factor は内側、リセットを持つ DFA は外側」）がここで先に分かるので、主定理が読みやすくなる。

### M5. 繰り返し（R2.4 の型）
- **ファンアウト2の非持ち上げ**が序論で5回出る：The remaining question、Approach の最後の文、表1の最終行、表2の行、Organization。
- **「every set-driven operator with characteristic samples throughout the class」**が4回：The setting の最後、定理C(ii)、Scope、表2の caption。
- **Scope の段落と表2**は、M2 で定理文を正確にすれば、ほぼ定理文の再掲になる。

**提案：** 非持ち上げは「The remaining question」の一文だけにする。表2は §7 の末尾か結論へ移す。序論に残すなら Scope の段落を表2の caption に吸収する。序論から表を1つ減らすと約0.7ページ短くなる。

### M6. Approach（277語）は読者が追えない密度（R1.2・R1.5 の型）
最初の2文（型による細分は高くつく、`prop:typed-thickness-exponential`）は重要で、良い。そのあとは、補題名と手法名が説明なしに続く。序論の Approach で読者に必要なのは次の3点だけである。
1. 型付きの細分ではなく元の表示で測る理由（1文）。
2. ファンアウト1では一つの連続したブロックを置き換えるだけで済み、群の値の前置積に鳩の巣原理を使えば十分であること（1文）。
3. ファンアウト $\ge2$ では、部分木が複数のブロックを別々の根成分に交互に送り込むので、非可換群では同時置換の順序が効く。これを解決するのが owner ごとの同時選択であり、局所群ではブロックの境界をまたぐ sliding factor を、離れたブロックと境界の拡張で処理する（2文）。

**書き換え案（約120語）：**

> Refining the grammar by types can make it exponentially thicker even for a two-element typing (Proposition~\ref{prop:typed-thickness-exponential}), so we bound characteristic data in terms of the original presentation. Short tuples of prescribed type are obtained by replacing long subderivations by short ones whose group values may differ, chosen so that the product of the whole is preserved. At fan-out one a replaced subtree occupies one contiguous block, and a pigeonhole argument on prefix products suffices. At fan-out $f\ge2$ a subtree sends up to $f$ blocks to different components, interleaved with the blocks of other subtrees, and in a noncommutative group the effect of simultaneous replacements depends on this order. The key step is a simultaneous choice of replacements that preserves the ordered product of every component at once (Proposition~\ref{prop:block-replacement-interface}); for local groups, whose values depend on factors straddling block boundaries, choosing blocks far apart reduces to the same step (Lemma~\ref{lem:lg-buffered-owners}).

下界の手法の文（marker families、rare types）と power transfer の文は、M5 に従って削るか、それぞれの節の冒頭へ移す。

### M7. #1 との記号の衝突：同じ査読者が両方を読む前提で（R1.33 の型）
TCS に投稿すれば、#1 の査読者に回る可能性が高い。
- #1 では $\tau_G$ が**非終端の厚さ**（各非終端の最短 yield の最大）であり、#1 の上界はすべて $\tau_G$ で書かれている。
- #2 では同じ量が $t_G$、$\theta_G/\bar\theta_G$ は**規則の厚さ**（規則を使う最短の文の長さ）、$\tau(G,s)$ は**分布代表の長さ**で、別物である。
- IPTtD の定義（EHY 2016, Def. 2.12）の厚さは $\tau_R$（非終端の厚さ）である。序論で「Theorems A and C say … are so identifiable」と書くなら、$\bar\theta_G$ と $t_G$ が多項式的に同値であること（`lem:thickness-equivalence`）に一言触れないと、定義に合っていないと読まれる。

**提案：** 序論の $\bar\theta_G$ の導入箇所に「polynomially equivalent to the nonterminal thickness $t_G$ used in the companion (there $\tau_G$) and in [EHY16]」と一句添える。$\tau(G,s)$ は別の文字に変えるのが最善だが、影響範囲が広いので著者の判断に任せる。

---

## 2. 中程度の指摘（Moderate）

### m1. 表1（companion との対照）の番号
R1 の clean tex で照合した結果、行の番号はすべて正しい：Theorem 4.2、Theorems 5.2–5.3、Corollary 5.4、Lemma 6.2、Corollary 6.3、Proposition 3.5（局所自明 ⇔ 窓）、Lemma 7.1、Theorem 7.2、Lemma 7.4、Corollary 7.5、Lemma 7.6、Proposition 6.4、Corollary 6.6、Appendix C（5文字 $\{\mathtt a,\lfloor,\rfloor,\lceil,\rceil\}$）、Proposition 6.4(iii)–(iv)。直すと良いのは次の2点。
- 「Fan-out-one pseudovariety boundary」行の「Sufficiency for LI∨Grp only (Remark 7.7)」：十分性は Corollary 7.5 で、Remark 7.7 は必要性を主張しないという注意。「Corollary 7.5; necessity not claimed (Remark 7.7)」が正確。
- 「Typed versus untyped class」行の「Separations at $f=1$」だけ番号がない。#1 の該当は Proposition 6.4（$L_n^-\notin\mathcal C^{\mathrm{cf}}_{s_0}$、証明末尾）と Proposition 8.4。

### m2. companion の位置づけと、#1 への移し替えの可能性（戦略）
- 序論は「Theorem C is a statement about context-free languages; it turns the sufficient condition of the companion into a characterization」と書く。査読者・編集者はまず「なぜ CFG の結果が CFG の論文にないのか」「二本に分けた理由は何か」を問う。
- ファンアウト1の LG の結果を #1 の R2 に入れる場合、表1の「Local-group typings」「Fan-out-one pseudovariety boundary」の2行と、この文、定理Cの位置づけがすべて変わる。どちらに転ぶかで序論の重心が変わるので、序論の書き直しの前に方針を決めておくのがよい。
- bib の `kuriyamaCFG` は URL だけである。「under revision for Theoretical Computer Science (TCS-D-26-00494)」の状態を書くと、編集者に対して透明になる。

### m3. 型付けで広がるクラスの例は、一言の動機があると強い（R2.1・R2.3 の型）
`prop:typed-separation` の $L_{\mathrm{sep}}$ は、偶奇の型付けで区別するとクラスに入る例で、R2.1 への答えとして有効である。ただし The setting の中では一文に埋もれている。M4(b) で独立させ、「the untyped operator over-generalizes on a three-word sample」まで書くと、型付けの利益が具体的に見える。

### m4. Organization（87語）
内容は正しいが、§3 の小節番号まで挙げる必要はない。2〜3行で足りる。

---

## 3. 軽微な指摘（Minor）

1. 局所群の定義で $\mathsf T$ を使っている（「finite semigroups $\mathsf T$ with $e\mathsf Te$ a group」）。要旨は $\mathsf S$ と $e\mathsf Se$。揃える。
2. 「for the noncommutative groups such as $S_3$ the order of interleaved components matters」は、Approach（M6）と内容が重なる。どちらか一方に。
3. 定理B(i) の「within a constant factor of the smallest reduced good ones」の定数は $f$ に依存する（$(7f+17)$）。$f$ は固定なので正しいが、「for fixed $f$」と添えると誤読がない。
4. 冒頭の「Polynomially many words may still be exponentially long, so we measure …」は良い一文。#1 の Example（$\{a^{2^n}\}$）を引くと、さらに具体的になる。
5. 「Const/Link/Comp construction used here are his」：「the reconstruction operator used here is his」で足りる（前回 Minor 2）。

---

## 4. 再構成の案（地の文 約1000語、表は1つ）

| 段落 | 目安 | 内容 |
|---|---:|---|
| 冒頭 | 120 | 正データ学習、総長で測る理由、問い「どの型付けで多項式か」 |
| 設定 | 100 | 型付け、クラス、バイアスの文献 |
| なぜ型付けか | 60 | `prop:typed-separation` |
| どの型付けが局所群か | 120 | LG と $U_1$ の定義、窓・群・積・ab の偶奇、リセット付き DFA |
| 主結果 | 250 | 定理A〜C（M2 の正確な文）、IPTtD と CFG の一文、厚さの同値（M7） |
| 残る問い | 50 | Open Problem と非持ち上げを一文ずつ |
| 手法 | 120 | M6 の案 |
| 先行研究と companion | 180 | ＋表1（m1 の修正） |
| 構成 | 40 | |

表2（Scope）は §7 の末尾か結論へ移す。

## 5. 優先順位
1. M2（定理文）と M1（問いと推測文）：査読者が最初に読む箇所で、R1.29 の型の指摘をそのまま招く。
2. M3・M4（用語と The setting の分割）：R1.5 の型。#1 で最も強く言われた点。
3. M5・M6（重複と Approach）：約0.7〜1ページ短くなる。
4. M7・m2（#1 との関係）：TCS に出すなら必須。m2 は方針の決定が先。
