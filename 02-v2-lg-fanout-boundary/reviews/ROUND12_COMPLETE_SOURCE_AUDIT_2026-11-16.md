# Round Twelve — U1 lower-bound exploration, independent audit, source and logs

**Research archive — original unmodified inputs**, not changes to `main.tex`.

Each file body is UTF-8 text preserved byte-for-byte. Extract by reading the `bytes` value and slicing that many bytes after the header newline. SHA-256 verifies integrity.

The boundaries use bytes, so an original file without a final newline is preserved.

```python
from pathlib import Path
import re, hashlib
b=Path(__file__).read_bytes()
pat=re.compile(rb"^===== BEGIN FILE (.*?) bytes=(\d+) sha256=([a-f0-9]{64}) =====\n",re.M)
for m in pat.finditer(b):
    name=m.group(1).decode("utf-8")
    size=int(m.group(2)); data=b[m.end():m.end()+size]
    assert hashlib.sha256(data).hexdigest()==m.group(3).decode()
    p=Path("extracted")/name; p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(data)
```

## Manifest

| Path | Size (bytes) | SHA-256 |
|---|---:|---|
| `PROMPT_CLAUDE_FANOUT2_ROUND12_SUPERPOLYNOMIAL_LOWER_BOUND_2026-11-15.md` | 25024 | `e61de85d8c495b1156ba9ed9f418417e75721fa73f773a3137bd9b1715b79496` |
| `SHA256SUMS.txt` | 434 | `171d680cd928c318ab89caeaae7352633ac17f289110df5e3cc33636bd90bd06` |
| `audit_claude_fanout2_round12_independent_2026-11-15.md` | 7520 | `6e8e46c26b76619c441b7fa36403b256dc5b04c6577a9737cf2475656cc338e0` |
| `check_round12_lower_bound_2026-11-15.py` | 37809 | `7571974956a1bcadc8163b08c175e3501d2305fd47902bee5b43a37062d38709` |
| `claude_fanout2_round12_candidate_rules_2026-11-15.md` | 6374 | `7d1a44927df75120d5f0cb6ec2be15140596809a28ad5676b88d42afe22b38c0` |
| `claude_fanout2_round12_lower_bound_checkpoint1_2026-11-15.md` | 4565 | `84753472ece195c9d07ec2a54e3cf3d3fff0b82b1418731695bbcb5201cb4c29` |
| `claude_fanout2_round12_lower_bound_report_2026-11-15.md` | 24257 | `b8997dfd1f03152ef4844ee3adc692d180d8b343fb3c79cc53eca76089ff045a` |
| `independent_presence_check.py` | 2295 | `0ef227cd79df4232a6a26e9b0654f8e256a8a77a7f3def14b066d7135cd24c6f` |
| `independent_presence_result.txt` | 271 | `82137f6002dff273e1192023714343f4da49e928dd2fede67f99cee3a4cb8e6a` |
| `independent_rerun_round12_lower_bound_2026-11-15.txt` | 18794 | `e82ee6dd5927c4c598eab0bea4c7b1c800336158232604af51652d3cab5e32cb` |
| `out_check_round12_lower_bound_2026-11-15.txt` | 18794 | `08dcf90851d4cdfdb6f0e03318baa22af20650af566081532bdd8a17b056b0af` |

## Original source bodies


===== BEGIN FILE PROMPT_CLAUDE_FANOUT2_ROUND12_SUPERPOLYNOMIAL_LOWER_BOUND_2026-11-15.md bytes=25024 sha256=e61de85d8c495b1156ba9ed9f418417e75721fa73f773a3137bd9b1715b79496 =====
# Claude 第十二段：`op:fanout-two` 本題への復帰 — U₁型付けにおける超多項式特徴標本長の探索

**日付**：2026-11-15 JST  
**区分**：純粋な数学研究・探索依頼。論文制作・別論文化・GitHub編集の依頼ではない。  
**優先度**：最重要。**この依頼は既存の特殊上界 U₂ を拡張する課題ではなく、正式な中心的未解決問題の下界を狙う課題である。**  
**目的**：新しい独立Claudeセッションが、このファイルを最初に読み、既存の定義・負の定理・下界原理を踏まえ、実際に証明可能な新しい反例族か、それを阻む新しい構造定理を探索すること。

---

## 0. 最重要命令：目的を取り違えない

これまでの第六〜十一段では、三文字・内容型・重なる二射影bigramデータで定義される特殊クラスについて、代表長の多項式上界 `U₂` の手証明案が完成し、独立のAI数学監査は `VALID WITH CLARIFICATIONS` と判定した。ただし専門家査読・形式証明は未実施である。

**ユーザーはその独立論文化を希望していない。** U₂の再執筆・論文化・LaTeX整備・既存結果の精緻化には探索時間を使わない。前進のために必要な障壁情報だけ参照する。

本段では、次の正式な開問題の肯定方向を直接狙う。

> 固定 `f≥2`, `r_max≥2` に対し、有限半群の擬多様体 `V` が一様多項式特徴データ長をもつための必要十分条件は `V⊆LG` か？ 特に `f=2`, `r_max=2` の **LG必要性** を示す超多項式下界を構成できるか。

**一つの明示的な固定 `U₁` 型付けに対して、fan-out 2・rank 2・組代入可能な言語族で超多項式下界を構成できれば、`f=2` におけるすべての `V⊈LG` への必要性を示せる。** ただし、`f=2` での構成は **自動的には `f≥3` の構成にならない**。`(2,s)`-組代入可能性は `(3,s)`-組代入可能性を含意しないので、`f≥3` は別途証明を要する。

「反例がないからLGが境界ではない」「局所計数クラスが多項式だからU₁型付け全体も多項式」などの論理飛躍を絶対にしない。

---

## 1. 最初に読む正本（GitHubは読み取り専用）

**リポジトリ**：`https://github.com/growupkuriyama-hub/Papers`  
**論文 #2**：`02-v2-lg-fanout-boundary/`、論文題目 *Characteristic-Data Length for Multiple Context-Free Languages under Fixed Finite-Semigroup Typing*。

以下の順で読む。少なくとも第1〜6項は実際に本文を開いて定義・定理の正確な量化を確認する。リポジトリがアクセス不能なら、この依頼書§2〜5の正確な基本データを用いて着手し、未確認点を明示する。

1. [最新版ハンドオフ](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/HANDOFF_CURRENT.md)。研究と投稿済み本文の区別を確認。
2. [現行英文LaTeX原稿](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex) — **必読ラベル**：`def:tuple-substitutable`, `def:class-cmcf`, `def:uniform-polydata`, `lem:distinguishing`, `lem:type-deletion`, `prop:rare-type`, `prop:three-letter-family`, `lem:power-transfer`, `thm:doubling-no-lift`, `thm:lg-characterization`, `op:fanout-two`。`def:grammar-properties` と `lem:thickness-equivalence` も読む。
3. [現行のU₂研究状態](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/STATUS_U2_STANDALONE_FORMALIZATION_2026-11-15.md)。**U₂は特殊な上界であり、本題の下界にはならない**。
4. [U₂定理ノート（障壁の参照用のみ）](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/theorem_U2_overlapping_projections_standalone_2026-11-15.md)。既存手法が多項式化してしまう局所順序・射影計数の類を把握する。
5. [第十一段の完全ソース＋検証器＋監査](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/ROUND11_SOURCE_BUNDLE_2026-11-15.md)。必要なときだけ参照。
6. [研究探索の旧ハンドオフ](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/STATUS_sl_fanout2_2026-11-01.md) と関係する `reviews/` 内の以前の探索。過去に反証された戦略の焼き直しを避けるため、目次・障壁・明示的反例を読む。

この依頼書と原稿の記述が異なるとき、**原稿の定義・量化を優先**し、その差を報告する。先行AI報告の `PROVED` を自動的に引用定理とせず、必要な段落を数学的に検証する。

---

## 2. 正確な定義と成功判定

### 2.1 型付けと固定パラメータ

- 最初の候補として **`Σ={a,b,c}` を固定**する。必要なら**最初から固定した**有限アルファベット `Σ={a,b,c,d,...}` に広げてよいが、`n` とともに新しい文字を増やしてはいけない。
- 半群 `U₁={1,ζ}` は `1` が単位元、`ζ²=ζ`。
- 標準の固定型付け `s_U: Σ⁺→U₁` は `s_U(c)=ζ`、`s_U(a)=s_U(b)=1`（追加文字の像は先に固定）。つまり標準三文字版では `s_U(w)=1` ⇔ `w≠ε` かつ `c` を含まない。
- `f=2`、文法のrank `≤2`。必要なら `r_max≥2` への系を検討。
- `G` は **reduced good MCFG**（ε-free、線形、非削除、非順序反転、非結合など、原稿 `def:grammar-properties` に従う）。文法サイズ `‖G‖` と**元の文法**の規則厚さ `\bar θ_G` の双方を測る。後付け型精密化文法のサイズや厚さだけを計ってはいけない。

### 2.2 `(2,s_U)`-組代入可能性は絶対条件

原稿通り、`d=1,2` のすべてについて、非空成分タプル `x⃗,y⃗∈(Σ⁺)^d` が

` s_U^{(d)}(x⃗)=s_U^{(d)}(y⃗) `

かつ `D_L^{(d)}(x⃗)∩D_L^{(d)}(y⃗)≠∅` を満たせば、

` D_L^{(d)}(x⃗)=D_L^{(d)}(y⃗) `

となることを示せ。

ここで適法な `d=2` 文脈は

`E=v₀ □₁ v₁ □₂ v₂` で **`v₁∈Σ⁺`**、`v₀,v₂∈Σ*` である。二つの穴は**非空・非隣接**。型は**穴ごとのU₁型**であり、単語全体の型が等しいだけでは足りない。

必ず次を分けて証明・検査する：`d=1`、`d=2`、両穴の順序、真ん中の非空区切り、型一致、共通受理文脈、**すべての他文脈での同時受理**。任意のMCFGや通常のCFGであるだけでは組代入可能とは言えない。

### 2.3 真の下界成功条件

**主目標（YESを導く下界）**：固定 `Σ,s_U` と族 `(L_n,G_n)` を構成し、

1. `L_n=L(G_n)`（または `L_n∩Σ⁺=L(G_n)` とεの扱いを明記）、`L_n∈C^{mcf}_{2,s_U}`。
2. `G_n` はrank≤2、fan-out≤2のreduced good文法。
3. `‖G_n‖` と `\bar θ_{G_n}` は `poly(n)`。
4. すべての特徴標本 `F`（まず `B^{≤2}_{2,s_U}`、可能なら全クラス型のset-driven learner）について、`‖F‖_+` が `n` の超多項式、できれば `2^{Ω(n)}`。より厳密には**どの固定多項式** `p(‖G_n‖,\bar θ_{G_n})` も最終的に超える。

十分な強い証明書は、ある実現型 `m∈U₁` の**最短の言語語長** `μ_m(L_n)` が超多項式であること。原稿の `prop:rare-type` により、その型の語がどんな特徴標本にも必要となる。単に「長い特殊語がある」だけでは下界にならない。

**第二の本格的証明書（希少型以外）**：`L'_n⊊L_n` で双方が `C^{mcf}_{2,s_U}` に属し、`min{|w|:w∈L_n\L'_n}` が超多項式となる。原稿 `lem:distinguishing` によって、L_nの特徴標本は差集合の語を必ず含む。これなら **同じU₁型に短い語が存在しても構わない**。また、差集合の一語が長い方式に限らず、多数の区別すべき下位ターゲットにより標本総長を増やす方式も許す。ただし必要な下界証明を厳密に与える。

**論理上の注意**：上界 `τ(G,s)` が証明できないこと、学習器が一度失敗すること、ある大きな語を強制できたと「思う」ことは、下界の証明ではない。

### 2.4 正式問題全体への含意を正しく述べる

`U₁∉LG` かつ `V⊈LG` なら `U₁∈V`（原稿 `thm:lg-characterization`）。従って**固定 `f=2`** で上記の `s_U` の下界が証明できれば、`f=2`、`r_max≥2` においてLGの必要性が導かれ、Theorem Aと合わせて境界を定められる。

しかし **`f≥3` は別問題**。また、逆方向のNOを主張するには、例えば `⟨U₁⟩` など一つの非LG擬多様体の**全ての許された型付け、全アルファベット、全対象**に対する一様多項式特徴標本上界を示さねばならない。`U₂`という特殊族だけの上界ではNOにならない。

---

## 3. 必ず乗り越える既知の負の結果

### 3.1 旧倍増族と不可能性

fan-out oneの基準構成は、

`E₀→a`, `E_i→b E_{i-1} E_{i-1} b | c E_{i-1} c`, `S→E_n`

で、`W₀=a`, `W_i=b W_{i-1}W_{i-1}b`, `|W_i|=3·2^i−2`。同族 `L_n` の唯一の `c` 無し語が `W_n` であり、`‖G_n‖=13n+7`, `\bar θ_{G_n}=4n`。fan-out 1では指数下界を与える。

**`thm:doubling-no-lift`**：十分大きなnについて、この `L_n` と、三文字を互いに素な文字集合の非空語に置き換えた像は、fan-out≥2の組代入可能なクラスに入らない。より強く、同じ型付けのどの `(f,s)`-組代入可能言語が `W_n`（あるいは該当像）を含んでも、同型・同Parikhの別語を含む。単純な入れ子拡張や文字置換では障壁は消えない。

**`lem:power-transfer`**：有限半群の任意の元の冪の最終周期 `i₀,p` と、**同じ語 `u` の長い反復**を受理語に含む状況から、二つの非隣接穴への冪移動が強制される。適法な中間文脈 `w_M≠ε` のもとで、

`w_L u^i w_M u^{δ+j} w_R∈L  ⇔  w_L u^{i+δ} w_M u^j w_R∈L`

（`i,j≥i₀`, `δ∈pℤ_{>0}`）。

**決定的な注意**：この移動は**総語長とParikhベクトルを保存**する。よって旧倍増族の唯一性を破るが、これだけで**最短U₁型語長が多項式**とは証明できない。これを実際に短縮へ繋げる追加の構造があるかも独立課題。

### 3.2 U₂から何を学び、何を推論してはならないか

第十一段研究のU₂は、内容型 `c_Σ`、**重なる二射影の長さ2の端点・窓計数**によって所属が決まる特殊な組代入可能言語の代表長に多項式上界を与える手証明案である。

- そこから得る**探索上のヒント**：bigramの有限計数＋端点・単純Parikh相関・特定の秩序配置だけでは、超多項式希少性を作りにくい可能性がある。これは**研究上の推測**であって一般不可能定理ではない。
- **誤用禁止**：内容型 `c_Σ` と `s_U` は同じ型付けではない。`dat_ov` は固定有限半群の型ではなく、計数値を無制限に持つデータである。U₂の結論を一般の `s_U` 言語に適用できるとは主張しない。
- これまでの局所上界の補題を下界の構成へ無理に流用しない。既知の反例・障壁だけ抜き出して、未知の構造に挑む。

---

## 4. 研究戦略：一つに固執せず競わせる

**探索時間配分の目安**：A 45%、B 30%、C 15%、D 10%。ただし数学的に強い新しい方向が見つかれば即時に組み替えてよい。既存のU₂を再び証明しない。

### A. 新しい「希少U₁型」族を実際に作る

目標は `μ_1(L_n)≥2^{Ω(n)}`（または超多項式）。典型的に `c` のない受理語は非常に長く、それ以外に `c` のある早期停止語があるような分岐を考えられるが、**従来の `b E E b | cE c` を形だけ変えただけ**ではなく、新しい不変量・言語構造を用いること。

検討する材料（例示であり採用義務なし）：

- 同期的な二成分導出／交差依存により、**長い同一文字冪ではなく**、短い冪移動が「正しい状態遷移」に見えない構造。
- 深さnを2分岐で符号化するが、文字集合は固定し、**局所マーカーの新鮮さを毎段仮定しない**再帰的符号・反復最小因子の設計。
- 語の一意性ではなく、同型語の全体が長いという**希少型語集合**。冪移動による同長の別語が生まれることは許容する。
- 最短のc無し語を長く保ちながら、`d=2`組代入閉包を**文法で生成可能**にする方法。単に閉包を定義してから有限生成を仮定しない。
- 型ごとの受理が有限状態で簡単に決まるものや、既知のアーベル・局所計数の上界が直ちに効く族を先に除外する。

**必須試験**：候補 `(L_n,G_n)` があれば、小さい n（例 n=1,2,3）で全生成語・型・最短語を実算し、受理文脈の具体的な**二穴の相違**を探す。最初に現れた `(2,s_U)`-違反は、`x⃗,y⃗,E_accept,E_reject`（各文字列・型・非空区切り付き）の形式で提示する。**違反が見つかれば、その候補は証明に使えない**。修正案は別の候補として記録する。

### B. 希少型に依らない下界（distinguishing subtargets）

ここを第二主力とする。`μ_1` が短いことが分かっても探索終了ではない。

`L'_n⊊L_n` を両方 `(2,s_U)`-組代入可能なfan-out2-MCFLとして構成し、`L_n\L'_n` の**最短語長**が超多項式となるようにする。

アイデアの方向：

- 全型から一部を削除する `lem:type-deletion` だけでなく、**同じ型の長い構造的部分族**を選択的に削り、組代入可能性を壊さない独立構成。
- 部分言語差の最初の語だけが非常に長く、両言語がそれ以前には一致する「遅い分岐」構成。
- `L_n` に小さい型1語があるとしても、`L_n\L'_n` が長いことだけで `lem:distinguishing` が発動する。したがって古い倍増族の「唯一性」の失敗を避け得る。
- もっとも、`L'_n` が `L_n` に含まれる・厳密に異なる・両方の組代入可能性を満たすことは、すべて**別々の証明義務**。単なる有限集合差を勝手に削ってよいとは限らない。
- 多数の区別対象 `L'_{n,j}` を用いて、短い単一証人が存在しても**総標本長**を超多項式にするルートも検討。ただし各差集合の重複による証人の使い回しを計数し、実際のヒッティングセット下界を証明。

### C. 新規二穴強制律または障壁定理

A/Bで実際の候補が壊れるなら、経験談ではなく再利用できる**普遍的な短縮・移動補題**へ一般化する。

問うべきこと：

- U₁型付けで、十分長いc無し語を含む任意の `(2,s_U)`-組代入可能fan-out2-MCFLに、必ず同型の**短い**語があると証明できるか。できるならこれは希少型手法の一般的な障壁であり、重要な部分成果。ただし**それでも中心的open problemのNOを示さない**。
- 任意の文法導出と `d=2` 受理文脈から、どのタイプの変形が必ず発生するか。冪移動は語長を保つが、別の代入手法と合成すれば短縮できるか。
- 型付き根最短導出の高い経路に対して、二穴を用いた置換をどう利用するか。**型付き導出自体の最短長**と**分布同値の最短代表長**を混同しない。
- U₂の局所上界と正反対の「local dataでは表せない依存」を具体的に特徴付けられるか。

証明できない一般化については、最小の失敗例と必要な追加仮定を残す。安易に不可能性を断言しない。

### D. 非LG境界を直接狙う別路線

候補があれば、`s_U`の希少型以外の 

- 固定された別の `U₁` 全射型付け（有限アルファベットは固定）
- ほかの有限非LG半群への型付け（ただし「すべての非LG擬多様体」への拡張が本当に可能か、`U₁`還元を確認）
- 特徴標本に含ませる別の識別証人

を検討する。通常はA/B優先。難しいというだけで標的を「U₂の上界」に戻さない。

---

## 5. 初手で試すべき adversarial audit（具体的な作業）

第十二段で何を試すかを曖昧にしないため、最初のチェックポイントまでに以下を実行せよ。

1. **障壁レジストリ**：研究候補を壊しやすい操作を小さいリストに分類：二穴冪移動、同色2穴文脈の共有、同長Parikh保存再配置、非空区切り、型別削除後の組代入、既知の局所・交差射影上界。
2. **新候補3件以上**：実際に説明できる候補言語構造と、なぜ従来の倍増族から本質的に異なるかを書く。うち少なくとも1件は**希少型でない差言語L\L'**を目標とする。
3. **最低1件を形式的に検査**：曖昧な `grammar idea` で終わらせず、最初の数段の**規則をすべて列記**。文法性質と極小の受理・非受理証人をコードに含める。
4. **二穴違反の探索**：有限語長・有限文脈長を明示した`d=1,2`の全探索または制約探索。`d=2`について常に `v₁≠ε` をassertする。同型比較・共通受理文脈・差分受理文脈を三つとも検査。実際の違反なら**完全な文字列**を出力。
5. **候補の修復または棄却**：違反があれば、修復で文法サイズや最短型語長をどう変えるか見積もる。気づかないふりをして「おおむねsubstitutable」と扱わない。

有限判定器の設計に関する注意：有限長で受理語を切り詰めた言語の組代入可能性は、無限言語の組代入可能性と一般に一致しない。有限探索のPASSは**有界証拠のみ**。FAILは実際の完全な有限長証人があれば真の反例だが、その文脈で候補の受理・非受理を正確に判定する必要がある。

**コードは非空の分岐を必ずassertする**（単なる`if`でスキップ、`assert ... or True`は禁止）。モデルが対象族の大事な例を実際に生成しているかをチェックする。反例探索では負の対照として旧倍増族の小さいn（可能なら）を含め、既知のtuple違反を検出できることを確認する。

---

## 6. 新しい補題・下界族をPROVEDとするチェックリスト

どんな定理候補も、以下のうち関係する項目を**全て**満たさなければ `PROVED` と書かない。

1. **量化**：`Σ` と `s` は `n` に依存せず固定。`L_n`、`G_n` は全nについて明示。
2. **文法**：有限規則スキーマ、start、arity、rank、linear/nondeleting/nonpermuting/nonmerging/ε-free、reduced性、`L(G_n)=L_n` の両包含。
3. **計数**：`‖G_n‖` と `θ̄_{G_n}` の上界を明示し、型付き精密化後の指数的厚さを代用していない。
4. **`d=1,2`代入可能性**：任意の非空タプル・全admissible文脈で定義通りに証明。共通受理文脈の存在だけで結論を飛ばさず、全文脈へ移す機構を記述。
5. **下界の証人**：型ごとの最短語、あるいは差集合の最短語、あるいは識別族のヒッティングセットに対する厳密な下界。単に特殊語 `W_n` が指数長なのは不十分。
6. **演算子適用**：`prop:rare-type` または `lem:distinguishing` のどの仮定により `B^{≤2}_{2,s}` の全特徴標本が拘束されるか。class-wide learnerの主張はその仮定を別途確認。
7. **漸近比較**：`n` に対する `2^{Ω(n)}` などを、`‖G_n‖,θ̄_{G_n}` の任意の多項式を超えることとして示す。
8. **負の定理との整合**：`lem:power-transfer`/`thm:doubling-no-lift` との衝突を明示的に検査。衝突する場合は主張を撤回・修正する。
9. **ファンアウトの射程**：f=2のみか、一般fにも通るか（3-hole以上のsubstitutabilityを証明したか）。未証明の拡張を主張しない。
10. **証明の出自**：コードのPASS、Claudeによる手証明、第三者の独立監査、形式証明を混同しない。

**反例分類**：
- `A`：提案した作戦・補題・実装への反例（元の中心問題への反例ではない）。
- `B`：候補言語の`d=2`組代入可能性に対する具体的違反。
- `C`：文法/型/量化/厚さ/希少型などの仮定違反。
- `D`：真の下界族の完全証明（中心問題のYESへの成果）。
- `E`：真の全対象上界に基づくNO方向の完全な反証（必要な擬多様体量化を明示）。
- `OPEN`：未解決。再利用可能な補題があれば部分成果として明示。

---

## 7. 出力物・チェックポイント（必ずファイルで返す）

**新しいClaudeには、最初の実質的発見時点でcheckpointをファイルとして出し、最終出力を必ず数学的に再検査可能な形にすることを依頼する。** ただし、AIが実際に進められる現在の作業で完結させること。GitHubへの書き込み・PR・論文本文・独立論文の作成はしない。

1. `claude_fanout2_round12_lower_bound_checkpoint1_2026-11-15.md`  
   - 原稿と既知障壁を確認した事実／新しい候補A/B/C／最初の数段の文法／最初の二穴判定結果／`D`を得たか。これを出した後も探索は続けてよい。
2. `claude_fanout2_round12_lower_bound_report_2026-11-15.md`  
   - 一文結論を冒頭に置く。`PROVED / CONDITIONAL / COUNTEREXAMPLE / OPEN`。本題へどの程度接近したか。候補の成功・失敗と失敗理由、形式的な命題・証明・具体的反例、未解決義務、次の最短の一手。
3. `check_round12_lower_bound_2026-11-15.py`  
   - Python 3標準ライブラリのみ。固定seed、明示的な文法生成・語列挙・tuple文脈・型検査・最短語・文法サイズ/厚さ推定。**全テストのPASS/FAILが可視**。既知のnegative controlも用意。
4. `out_check_round12_lower_bound_2026-11-15.txt`  
   - 上記スクリプトの実出力。数値・ログを架空にしない。
5. 可能なら `claude_fanout2_round12_candidate_rules_2026-11-15.md`  
   - 反例で棄却した候補も含め、文法規則を再利用可能な一覧として残す。

最終報告の冒頭に、次の**成否表**を必ず載せる。

| 探索対象 | 正確な状態 | 根拠・反例 | 残る仮定 |
|---|---|---|---|
| 希少U₁型による超多項式下界 | ? | ? | ? |
| 区別部分言語による超多項式下界 | ? | ? | ? |
| `(2,s_U)`-substitutability | ? | ? | ? |
| fixed `Σ,s`、rank2 good MCFG、poly-size/thickness | ? | ? | ? |
| `op:fanout-two` at f=2 | OPEN または厳密な解決 | ? | ? |
| `op:fanout-two` at f≥3 | 原則OPEN | ? | ? |

**成果が出なくても、棄却された候補を明示することが価値である。** 何を試し、どの短い二穴文脈が壊し、どの不変量が残ったかを、次の探索者がすぐ再開できる具体的な資料として残す。新規補題を捏造して「解決間近」と飾らない。

---

## 8. 最後の研究指示

可能な限り**新しい構成**へ計算・推論を投入する。本文を読むだけで終わらず、候補を最低3件比較し、1件以上で実際の規則・文脈・最短語を計算せよ。旧倍増族の微修正、U₂特殊上界の再演、証明済みの局所補題の繰り返しは避ける。

**最も望む結論は**：

> 「固定 `U₁` 型付け、fan-out2/rank2の good MCFG族、`(2,s_U)`-組代入可能性、元文法の多項式サイズ・厚さを厳密に満たし、`prop:rare-type` または `lem:distinguishing` により全特徴標本に超多項式長を強制する」という具体的な新定理。

**次善の真の成果は**：

> 「希少型手法が一般に困難である理由を新しい補題で定式化し、別の下界戦略を強制する」または「有力な候補を反例で確実に排除した」こと。

どちらでも **正式な `op:fanout-two` の状態を過大に書き換えない**。結論が得られるまでは `OPEN` を維持する。

**論文執筆なし／別論文化なし／GitHub編集なし。探索と数学的な研究記録の返却のみ。**

===== END FILE =====

===== BEGIN FILE SHA256SUMS.txt bytes=434 sha256=171d680cd928c318ab89caeaae7352633ac17f289110df5e3cc33636bd90bd06 =====
6e8e46c26b76619c441b7fa36403b256dc5b04c6577a9737cf2475656cc338e0  audit_claude_fanout2_round12_independent_2026-11-15.md
e82ee6dd5927c4c598eab0bea4c7b1c800336158232604af51652d3cab5e32cb  independent_rerun_round12_lower_bound_2026-11-15.txt
0ef227cd79df4232a6a26e9b0654f8e256a8a77a7f3def14b066d7135cd24c6f  independent_presence_check.py
82137f6002dff273e1192023714343f4da49e928dd2fede67f99cee3a4cb8e6a  independent_presence_result.txt

===== END FILE =====

===== BEGIN FILE audit_claude_fanout2_round12_independent_2026-11-15.md bytes=7520 sha256=6e8e46c26b76619c441b7fa36403b256dc5b04c6577a9737cf2475656cc338e0 =====
# 第十二段 U₁ 超多項式下界探索 — 独立監査メモ

日付：2026-11-15 JST。対象：ユーザー提供 ZIP `新しいフォルダー(20261115-093725).zip` 内の原報告・候補規則・チェックポイント・Python検証器・ログ。本メモは研究記録であり、査読または形式証明ではない。

## 1. 正確な最終判定

**`op:fanout-two` は OPEN。** U₁ 型付けの固定三文字アルファベットで、fan-out ≤2、rank ≤2、reduced good な小型文法により型1最短語が指数的に長くなる候補は作られたが、**(2,s_U)-tuple substitutability** に対する具体的な違反がそれぞれ発見された。したがって、希少型補題を適用する所要条件が満たされず、超多項式の特徴標本長は証明されていない。

## 2. 再現実験

- ZIPの 6 エントリを展開。`check_round12_lower_bound_2026-11-15.py` の SHA256 は `7571974956a1bcadc8163b08c175e3501d2305fd47902bee5b43a37062d38709` で、報告書記載と一致。
- 提出コードをPython 3で独立に全量再実行。**終了コード 0、72 tests / 72 PASS / 0 FAIL**。
- 提出された標準出力と再実行出力の差は、T1・T2セクションの所要時間と最終所要時間の3行だけ。候補数、違反証人、検証結果は一致。
- T1: 405件、T2: 2,688件。いずれも n=2 で1穴または2穴の違反が発見された。A1（n=3）、A3（n=2）、A4（n=2）も違反。正例および既知のfan-out 1倍増族を対照にした。
- **限定:** 「n=2 で違反」は、その族が *すべての n* で属するという主張を否定するが、「十分大きい n のみなら成立する」可能性を一般に排除する証明ではない。

## 3. 理論的結果の精査

### R（LG型付けで代入可能な部分標的との短い区別語）

**既存定理からの妥当な系。** `thm:local-group-polydata`（定理A）と `lem:distinguishing` を同じ LG 型付け t について適用すると、特性標本の一語が L\L' に属し、総長上界から短い区別語が得られる。論理は直接的。系 R1・R2 の量化も、L、L' が *ともに* C_{f,t} に属することを保てば正しい。「新規定理」と呼ぶより **既存定理の明示的な帰結**と表現する方が適切。

### S（c-freeの各長さの切片）

**支持。** `K_l=L ∩ s_U^{-1}(1) ∩ len^{-1}(l)` は可換群 ℤ での剰余類（部分群 0）によるフィルタと型フィルタで得られ、有限ゆえ f-MCFL。すべての非空成分が c-free なので組の s_U 型は自動的に 1。したがって K_l の型なしの組代入可能性が従う。唯一語形の分類は、現行 main.tex にはない退避原稿 `thm:app-singleton` に依存することを明記すべき。

### P2・P3・C・U（a冪の希少語の補償法則）

**補題Cの中心的な2穴移送は数学的に整合的。** 最短 c-free語として a^μ を共有受理文脈に使う際、2穴の中間区切り a^(μ−T) が非空となる `T≤μ−1` が重要。補題Cの α=max(1,1−Δ) は両成分の非空性と E/E' の指数の非負性を確保している。U(ii)のアフィン性には報告書の `T_d≥2+M` の余裕条件が本質的であり、余裕なしの一般命題に拡張してはならない。

**提示証人の表記に誤植あり。** A1（n=3）の二穴違反について、報告本文は共有文脈を `□a□` と書いて `a^8` を得ると述べるが、提出コードが出力する正しい共有文脈は **`□a□a`**。組 `x=(aa,aaaa)`, `y=(a,aaaaa)` からどちらも a^8 を得る。区別文脈は `□cbbc□` で、`aacbbcaaaa∈L` と `acbbcaaaaa∉L`。コード上の具体的反例自体は有効。

### LS（局所的存在パターンの最短証人）

文法の軽重節点の交換による一般論証は有望だが、**公刊可能な一般証明としては追加検査が必要**。反復する `(非終端, 成分番号)` の間で置換を行う際、固定された k 個の原位置が、子の成分から祖先の対応する成分へ同じ順序で写ること、語頭・語末アンカーが保持されることを独立補題として完全に書き下すべき。提示された数値検査はfan-out 1のランダム文法だけで、fan-out 2一般の形式証明ではない。

## 4. 正則篩いの分類：実装上の問題と独立再検証

§2.2/§4 は「3状態以下のDFAについて、有界検査を通った197例がすべて Parikh 決定か presence 型」と報告する。しかし**元のpresence判定器は数学的定義と一致していない**。

報告のパターン `(u,π,σ)` は `π=1 => prefix`、`σ=1 => suffix` という**含意条件**。`π=0` なら、語頭への出現も許される。一方、`classify_presence` は `(u, i==0, j==n)` を**完全一致のキー**として利用しており、`π=0` を「語頭ではない」と扱っている。

**分類器単体への反例：** 長さ7以下の語について「`abc` が厳密な内部に現れない」語を良い語とする。元の `classify_presence` はこの集合を k=3 のpresence型と判定するが、含意条件どおりの禁止パターンではその補集合を k≤3 で表せない。これは**分類器の方法上の反例**であり、代入可能性の主張への反例ではない。

**追加で独立再検査を実行した結果：** 定義どおりの `(u,π,σ)` による156パターンを長さ1〜7の3,279語に対して事前計算し、元の全DFA探索を再実行。生き残った197候補を、訂正した判定法で全件照合したところ**分類結果は同じ**だった。内訳は `(Parikh, proper-presence)` = `(両方14, Parikhのみ97, presenceのみ86)`、どちらでもないもの0。したがって報告の**有限観察そのものは再現された**が、元の関数の実装差異は修正対象である。

この結果はあくまで**長さ≤7における**有限観察であり、全ての長さについてpresence型と表現できることの証明ではない。また、DFAの同一性は長さ6までのシグネチャによるので、40812は無限言語の異なり数ではなく、長さ≤6で区別できるクラスの個数。

## 5. 現在の研究への示唆

- **希少型経路：** (a) `a^μ` を希少型最短語とする場合の P2/P3/C が深さ依存ラベルの障壁を定量化する。(b) 次は各受理語の非-a核の数を一定 k 以下に制限し、予想 A の部分クラスを証明するか反例を探す。
- **区別部分言語経路：** RはLG型付けで既に代入可能な L' を排除する。非LG型への本質的な依存を持つ L'、とくに剰余類フィルタと希少型の複合および非正則の部分標的を調べる。
- **探索設計：** n=2の有限反例を全nの不可能性と誤認しない。候補族の量化を明示し、十分大きいnで成り立つ可能性を別途判定する。
- **正式問題：** `op:fanout-two` は全ての f≥2 で未解決。今回の成果を `main.tex` の定理へ昇格させない。GitHub編集もしない。

**監査判定:** 下界構成について **NEGATIVE SEARCH RESULT / OPEN**。R、S、P2/P3/C/U は少なくとも主要な論証が支持される（Rは既存結果の系）。LSの一般論証と正則篩い分類の厳密化には別作業が必要。

===== END FILE =====

===== BEGIN FILE check_round12_lower_bound_2026-11-15.py bytes=37809 sha256=7571974956a1bcadc8163b08c175e3501d2305fd47902bee5b43a37062d38709 =====
#!/usr/bin/env python3
"""check_round12_lower_bound_2026-11-15.py  --  Round 12 verifier (Python 3 stdlib only).

Sections
  0  core MCFG library: goodness asserts, ||G||, exact theta-bar, exact mu_1,
     bounded enumeration, bounded (d,s_U)-substitutability with full witnesses
  1  controls: positive (Sigma+, {a,b}+, (ab)+) and negative (three-letter doubling
     family, n=2, manuscript values ||G||=13n+7, theta=4n, mu_1=3*2^n-2)
  2  template search T1 (fan-out 1) and T2 (fan-out 2) doubling-with-escape families
  3  designed candidates A1 (depth-labelled escapes), A3 (Thue-Morse), A4 (two-track)
     and membership-defined weight languages
  4  Route-B: regular sieves with <=3 states, bounded (2,s_U) screen, classification
  5  Corollary R2 sanity (CE family minus its rare word is not untyped 1-substitutable)
  6  Corollary U numeric check and Prop LS randomized sanity
Every reported violation is re-verified by an independent routine (verify_violation).
A bounded PASS is evidence only; a FAIL with a verified witness is a genuine violation
of the infinite language (all words involved have length <= N and membership of all
words of length <= N is computed exactly).
"""
import itertools, random, time, sys, io, contextlib, os
from collections import Counter
# All iteration over sets is sorted, so the log is reproducible independently of PYTHONHASHSEED.
random.seed(20261115)
RESULTS = []
def test(name, cond, info=''):
    RESULTS.append((name, bool(cond)))
    print('[%s] %s %s' % ('PASS' if cond else 'FAIL', name, info))
"""(core) Core library for round-12 lower-bound exploration (Python 3 stdlib only).

MCFG representation
-------------------
A grammar is a dict with keys
  'start' : name of start nonterminal (fan-out 1)
  'fan'   : {nonterminal: fan-out}
  'rules' : list of (lhs, children_tuple, template)
            template = tuple of components; each component is a tuple of tokens;
            a token is either a terminal (str of length 1) or a pair (j, k)
            meaning component k (0-based) of child j (0-based).

Typing: s_U on {a,b,c}: a,b -> 1, c -> z (zeta).  Type of a nonempty word is
'1' iff it contains no 'c'.
"""
from itertools import combinations

ZETA_LETTERS = {'c'}


def stype(w):
    assert len(w) > 0
    return 'z' if any(ch in ZETA_LETTERS for ch in w) else '1'


def ttype(t):
    return tuple(stype(x) for x in t)


# ---------------------------------------------------------------- grammar checks
def check_good(G):
    """Assert linear, nondeleting, nonpermuting, nonmerging, eps-free, fan-outs."""
    fan = G['fan']
    assert fan[G['start']] == 1
    for (A, ch, tpl) in G['rules']:
        assert len(tpl) == fan[A], (A, ch, tpl)
        occ = []
        for comp in tpl:
            assert len(comp) >= 1, ('eps component', A, tpl)      # eps-free
            for tok in comp:
                if isinstance(tok, tuple):
                    occ.append(tok)
        # nondeleting + linear: each variable exactly once
        need = [(j, k) for j, B in enumerate(ch) for k in range(fan[B])]
        assert sorted(occ) == sorted(need), ('linearity/nondeleting', A, tpl)
        # nonpermuting: for each child j, components appear in order
        flat = [tok for comp in tpl for tok in comp]
        for j, B in enumerate(ch):
            ks = [tok[1] for tok in flat if isinstance(tok, tuple) and tok[0] == j]
            assert ks == list(range(fan[B])), ('permuting', A, tpl)
        # nonmerging: no factor xi_j^k xi_j^{k+1} inside a component
        for comp in tpl:
            for t1, t2 in zip(comp, comp[1:]):
                if isinstance(t1, tuple) and isinstance(t2, tuple):
                    assert not (t1[0] == t2[0] and t2[1] == t1[1] + 1), ('merging', A, tpl)
    return True


def rank(G):
    return max(len(ch) for (_, ch, _) in G['rules'])


def max_fan(G):
    return max(G['fan'].values())


def size(G):
    """||G|| = |V| + sum_R (1 + r + sum_i |alpha_i|)."""
    tot = len(G['fan'])
    for (A, ch, tpl) in G['rules']:
        tot += 1 + len(ch) + sum(len(c) for c in tpl)
    return tot


def nterm(tpl):
    return sum(1 for comp in tpl for tok in comp if not isinstance(tok, tuple))


INF = float('inf')


def min_inside(G, rule_filter=None):
    """minimal total yield length per nonterminal (optionally restricted rules)."""
    m = {A: INF for A in G['fan']}
    changed = True
    while changed:
        changed = False
        for R in G['rules']:
            A, ch, tpl = R
            if rule_filter is not None and not rule_filter(R):
                continue
            v = nterm(tpl) + sum(m[B] for B in ch)
            if v < m[A]:
                m[A] = v
                changed = True
    return m


def min_outside(G, mi):
    mo = {A: INF for A in G['fan']}
    mo[G['start']] = 0
    changed = True
    while changed:
        changed = False
        for (A, ch, tpl) in G['rules']:
            if mo[A] == INF:
                continue
            base = mo[A] + nterm(tpl) + sum(mi[B] for B in ch)
            for j, B in enumerate(ch):
                v = base - mi[B]
                if v < mo[B]:
                    mo[B] = v
                    changed = True
    return mo


def check_reduced(G):
    mi = min_inside(G)
    mo = min_outside(G, mi)
    for A in G['fan']:
        assert mi[A] < INF, ('unproductive', A)
        assert mo[A] < INF, ('unreachable', A)
    return True


def thickness(G):
    mi = min_inside(G)
    mo = min_outside(G, mi)
    th = 0
    for (A, ch, tpl) in G['rules']:
        th = max(th, mo[A] + nterm(tpl) + sum(mi[B] for B in ch))
    return max(1, th)


def mu_type1(G):
    """shortest c-free word of L(G) (exactly: derivations of c-free words use only c-free rules)."""
    def cfree(R):
        return all(tok not in ZETA_LETTERS for comp in R[2] for tok in comp if not isinstance(tok, tuple))
    return min_inside(G, cfree)[G['start']]


# ---------------------------------------------------------------- enumeration
def apply_tpl(tpl, kids):
    out = []
    for comp in tpl:
        s = []
        for tok in comp:
            if isinstance(tok, tuple):
                s.append(kids[tok[0]][tok[1]])
            else:
                s.append(tok)
        out.append(''.join(s))
    return tuple(out)


def enumerate_yields(G, N):
    """All yield tuples of every nonterminal with total length <= N."""
    Y = {A: set() for A in G['fan']}
    changed = True
    while changed:
        changed = False
        for (A, ch, tpl) in G['rules']:
            t0 = nterm(tpl)
            if t0 > N:
                continue
            lists = [sorted(Y[B], key=lambda t: sum(map(len, t))) for B in ch]
            new = []

            def rec(j, acc, tot):
                if j == len(ch):
                    new.append(apply_tpl(tpl, acc))
                    return
                for y in lists[j]:
                    l = sum(map(len, y))
                    if tot + l > N:
                        break
                    rec(j + 1, acc + [y], tot + l)
            rec(0, [], t0)
            for y in new:
                if y not in Y[A]:
                    Y[A].add(y)
                    changed = True
    return Y


def language(G, N):
    return {t[0] for t in enumerate_yields(G, N)[G['start']]}


# ---------------------------------------------------------------- substitutability
def tuple_occurrences(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[i:j],), (w[:i], w[j:])
    elif d == 2:
        for i1 in range(n):
            for j1 in range(i1 + 1, n):
                for i2 in range(j1 + 1, n):        # v1 = w[j1:i2] nonempty
                    assert i2 > j1
                    for j2 in range(i2 + 1, n + 1):
                        yield (w[i1:j1], w[i2:j2]), (w[:i1], w[j1:i2], w[j2:])
    else:
        raise ValueError


def fill(ctx, t):
    if len(t) == 1:
        return ctx[0] + t[0] + ctx[1]
    assert len(ctx[1]) >= 1, 'inadmissible d=2 context'
    return ctx[0] + t[0] + ctx[1] + t[1] + ctx[2]


def check_substitutable(Lset, N, d, max_report=3, typed=True):
    """Bounded check of (d, s_U)-substitutability (typed=False: untyped).

    Returns list of violations; each violation is a dict with full strings:
    x, y, shared context E0 (accepting both), context E with E[x] in L and
    E[y] not in L (|E[y]| <= N, so non-membership is exact)."""
    D = {}
    by_ctx = {}
    for w in sorted(Lset):
        for t, ctx in tuple_occurrences(w, d):
            D.setdefault(t, set()).add(ctx)
            by_ctx.setdefault(ctx, set()).add(t)
    viol = []
    checked_pairs = 0
    seen = set()
    for ctx in sorted(by_ctx):
        ts = by_ctx[ctx]
        groups = {}
        for t in sorted(ts):
            key = ttype(t) if typed else ('*',) * d
            groups.setdefault(key, []).append(t)
        for key in sorted(groups):
            lst = groups[key]
            if len(lst) < 2:
                continue
            lst.sort()
            x0 = lst[0]
            lx = sum(map(len, x0))
            for y in lst[1:]:
                if (x0, y) in seen:
                    continue
                seen.add((x0, y))
                checked_pairs += 1
                ly = sum(map(len, y))
                for (a, b) in ((x0, y), (y, x0)):
                    lb = sum(map(len, b))
                    for E in sorted(D[a]):
                        if sum(map(len, E)) + lb <= N:
                            if fill(E, b) not in Lset:
                                viol.append(dict(x=a, y=b, E0=ctx, E=E,
                                                 E0x=fill(ctx, a), E0y=fill(ctx, b),
                                                 Ex=fill(E, a), Ey=fill(E, b)))
                                break
                    if len(viol) >= max_report:
                        return viol, checked_pairs
    return viol, checked_pairs


def fmt_viol(v):
    def c(E):
        if len(E) == 2:
            return "%r[]%r" % E
        return "%r[]%r[]%r" % E
    return ("x=%r type=%s, y=%r type=%s; shared E0=%s: E0[x]=%r, E0[y]=%r in L; "
            "E=%s: E[x]=%r in L but E[y]=%r NOT in L" % (
                v['x'], ttype(v['x']), v['y'], ttype(v['y']), c(v['E0']), v['E0x'], v['E0y'],
                c(v['E']), v['Ex'], v['Ey']))


# ===== candidates
"""Designed candidate families for round 12 (explicit grammars)."""


def R(l, ch, *comps):
    return (l, tuple(ch), tuple(tuple(c) for c in comps))


def A1_aligned(n):
    """Depth-labelled escape blocks.  E_0 -> a ; E_i -> E_{i-1} E_{i-1} | c B_{n-i} c (i<n);
    E_n -> E_{n-1} E_{n-1};  B_1 -> b ; B_k -> b B_{k-1};  S -> E_n.
    Escape block c b^d c stands for weight 2^(n-d); c-free word a^(2^n)."""
    fan = {'S': 1}
    rules = [R('E0', [], ['a'])]
    fan['E0'] = 1
    for k in range(1, n):
        fan['B%d' % k] = 1
        rules.append(R('B1', [], ['b']) if k == 1 else R('B%d' % k, ['B%d' % (k - 1)], ['b', (0, 0)]))
    for i in range(1, n + 1):
        E, P = 'E%d' % i, 'E%d' % (i - 1)
        fan[E] = 1
        rules.append(R(E, [P, P], [(0, 0), (1, 0)]))
        if i < n:
            rules.append(R(E, ['B%d' % (n - i)], ['c', (0, 0), 'c']))
    rules.append(R('S', ['E%d' % n], [(0, 0)]))
    return dict(start='S', fan=fan, rules=rules)


def A3_thue_morse(n, esc='cc'):
    """Thue-Morse doubling with CE-type escapes.  P_0->a, Q_0->b,
    P_i -> P_{i-1} Q_{i-1} | c P_{i-1} c ;  Q_i -> Q_{i-1} P_{i-1} | c Q_{i-1} c ; S -> P_n.
    c-free word: Thue-Morse prefix t_n of length 2^n (overlap-free: no u^4, so
    lem:power-transfer is not applicable to it)."""
    fan = {'S': 1, 'P0': 1, 'Q0': 1}
    rules = [R('P0', [], ['a']), R('Q0', [], ['b'])]
    for i in range(1, n + 1):
        P, Q, p, q = 'P%d' % i, 'Q%d' % i, 'P%d' % (i - 1), 'Q%d' % (i - 1)
        fan[P] = 1
        rules.append(R(P, [p, q], [(0, 0), (1, 0)]))
        rules.append(R(P, [p], ['c', (0, 0), 'c']))
        if i < n:                  # Q_n would be unreachable
            fan[Q] = 1
            rules.append(R(Q, [q, p], [(0, 0), (1, 0)]))
            if esc == 'cc':
                rules.append(R(Q, [q], ['c', (0, 0), 'c']))
            elif esc == 'cb':      # side-distinguished escapes
                rules.append(R(Q, [q], ['c', 'b', (0, 0), 'b', 'c']))
    rules.append(R('S', ['P%d' % n], [(0, 0)]))
    return dict(start='S', fan=fan, rules=rules)


def A4_two_track(n):
    """Fan-out-2 'two-track' family: D_i has yield (X_i, Y_i).
    c-free:  D_i -> (x1 b y1, y2 b x2)   [children x=D_{i-1}, y=D_{i-1}]
    escape:  D_i -> (c x1, x2 c)  ;  D_0 -> (a, a) ; S -> x1 a x2.
    The two tracks are mirror images; escapes are synchronized across tracks
    (one fan-out-2 escape marks both tracks at once)."""
    fan = {'S': 1, 'D0': 2}
    rules = [R('D0', [], ['a'], ['a'])]
    for i in range(1, n + 1):
        D, P = 'D%d' % i, 'D%d' % (i - 1)
        fan[D] = 2
        rules.append(R(D, [P, P], [(0, 0), 'b', (1, 0)], [(1, 1), 'b', (0, 1)]))
        rules.append(R(D, [P], ['c', (0, 0)], [(0, 1), 'c']))
    rules.append(R('S', ['D%d' % n], [(0, 0), 'a', (0, 1)]))
    return dict(start='S', fan=fan, rules=rules)


# ===== template search
"""Systematic template search over doubling-with-escape grammar families.
Fan-out 1 (family T1) and fan-out 2 (family T2).  For each template:
 (1) goodness/reducedness asserted for n=1..6,
 (2) mu_1 growth >= 2^(n-1) and thickness linear checked (filter F),
 (3) bounded (2,s_U) check at n=2 (and n=3 if passing), N bound given.
"""
import itertools, random, time, sys


def toks(s):
    return list(s)

# ---------------------------------------------------------------- fan-out 1
def T1(n, p, q, r, esc):
    fan = {'S': 1}
    rules = [R('E0', [], ['a'])]
    fan['E0'] = 1
    for i in range(1, n + 1):
        E, P = 'E%d' % i, 'E%d' % (i - 1)
        fan[E] = 1
        rules.append(R(E, [P, P], toks(p) + [(0, 0)] + toks(q) + [(1, 0)] + toks(r)))
        kind, s, t = esc
        if kind == 'wrap':
            rules.append(R(E, [P], toks(s) + [(0, 0)] + toks(t)))
        else:
            rules.append(R(E, [], toks(s)))
    rules.append(R('S', ['E%d' % n], [(0, 0)]))
    return dict(start='S', fan=fan, rules=rules)

def T1_space():
    ins = ['', 'a', 'b']
    escs = [('wrap', s, t) for s, t in [('c', 'c'), ('c', ''), ('', 'c'), ('cb', 'c'), ('c', 'bc'),
                                         ('cc', 'c'), ('c', 'cc'), ('ca', 'c'), ('c', 'ac'), ('bc', 'cb')]]
    escs += [('const', s, '') for s in ['c', 'cc', 'cac', 'cbc', 'cbbc']]
    for p in ins:
        for q in ins:
            for r in ins:
                for e in escs:
                    yield (p, q, r, e)

# ---------------------------------------------------------------- fan-out 2
X1, X2, Y1, Y2 = (0, 0), (0, 1), (1, 0), (1, 1)

def arrangements():
    out = []
    for inter in set(itertools.permutations([X1, X2, Y1, Y2])):
        if inter.index(X1) > inter.index(X2) or inter.index(Y1) > inter.index(Y2):
            continue
        for cut in (1, 2, 3):
            c1, c2 = list(inter[:cut]), list(inter[cut:])
            ok = True
            for comp in (c1, c2):
                for t1, t2 in zip(comp, comp[1:]):
                    if t1[0] == t2[0] and t2[1] == t1[1] + 1:
                        ok = False
            if ok:
                out.append((tuple(c1), tuple(c2)))
    return sorted(out)

def T2(n, arr, ins, esc, mid, base):
    """arr: arrangement; ins: dict position->letter (positions: ('L',k) prefix of comp k, ('R',k) suffix)"""
    fan = {'S': 1, 'D0': 2}
    rules = [R('D0', [], toks(base[0]), toks(base[1]))]
    for i in range(1, n + 1):
        D, P = 'D%d' % i, 'D%d' % (i - 1)
        fan[D] = 2
        comps = []
        for k in range(2):
            comps.append(toks(ins.get(('L', k), '')) + list(arr[k]) + toks(ins.get(('R', k), '')))
        rules.append(R(D, [P, P], *comps))
        if esc[0] == 'wrap':
            (s1, t1, s2, t2) = esc[1]
            rules.append(R(D, [P], toks(s1) + [X1] + toks(t1), toks(s2) + [X2] + toks(t2)))
        else:
            rules.append(R(D, [], toks(esc[1][0]), toks(esc[1][1])))
    rules.append(R('S', ['D%d' % n], [X1] + toks(mid) + [X2]))
    return dict(start='S', fan=fan, rules=rules)

def T2_space():
    arrs = arrangements()
    insopts = [{}, {('L', 0): 'b'}, {('R', 1): 'b'}, {('L', 0): 'b', ('R', 1): 'b'},
               {('R', 0): 'b', ('L', 1): 'b'}, {('L', 0): 'a'}, {('L', 0): 'b', ('R', 1): 'a'}]
    escs = [('wrap', e) for e in [('c', '', '', 'c'), ('', 'c', 'c', ''), ('c', '', 'c', ''),
                                  ('', 'c', '', 'c'), ('c', 'c', '', ''), ('', '', 'c', 'c'),
                                  ('c', '', '', ''), ('', '', '', 'c'), ('bc', '', '', 'cb')]]
    escs += [('const', e) for e in [('c', 'c'), ('cac', 'c'), ('c', 'cbc')]]
    for arr in arrs:
        for ins in insopts:
            for esc in escs:
                for mid in ('a', 'b'):
                    for base in (('a', 'a'), ('a', 'b')):
                        yield (arr, ins, esc, mid, base)

# ---------------------------------------------------------------- evaluation
def screen(builder, args, nmax=6):
    rows = []
    for n in range(1, nmax + 1):
        G = builder(n, *args)
        check_good(G)
        assert max_fan(G) <= 2 and rank(G) <= 2
        check_reduced(G)
        rows.append((n, size(G), thickness(G), mu_type1(G)))
    mu = [r[3] for r in rows]
    th = [r[2] for r in rows]
    exp_ok = mu[-1] < INF and mu[-1] >= 2 ** (nmax - 1)
    thin_ok = th[-1] <= 12 * nmax
    return rows, exp_ok, thin_ok

def subst(builder, args, n, N):
    G = builder(n, *args)
    L = language(G, N)
    for d in (1, 2):
        v, p = check_substitutable(L, N, d, max_report=1)
        if v:
            return d, v[0], len(L)
    return None, None, len(L)

def run(family, seed=20261115, limit=None, N2=18, N3=26, budget=900):
    random.seed(seed)
    space = list(T1_space()) if family == 'T1' else list(T2_space())
    random.shuffle(space)
    if limit:
        space = space[:limit]
    builder = T1 if family == 'T1' else T2
    stats = dict(total=0, bad_grammar=0, not_exp=0, thick=0, fail_n2_d1=0, fail_n2_d2=0,
                 fail_n3_d1=0, fail_n3_d2=0, survive=0)
    survivors, examples = [], {}
    t0 = time.time()
    for args in space:
        if time.time() - t0 > budget:
            break
        stats['total'] += 1
        try:
            rows, e, t = screen(builder, args)
        except AssertionError:
            stats['bad_grammar'] += 1
            continue
        if not e:
            stats['not_exp'] += 1
            continue
        if not t:
            stats['thick'] += 1
            continue
        d, v, nl = subst(builder, args, 2, N2)
        if v:
            k = 'fail_n2_d%d' % d
            stats[k] += 1
            key = (k, ttype(v['x']))
            examples.setdefault(key, (args, v))
            continue
        d, v, nl = subst(builder, args, 3, N3)
        if v:
            k = 'fail_n3_d%d' % d
            stats[k] += 1
            key = (k, ttype(v['x']))
            examples.setdefault(key, (args, v))
            continue
        stats['survive'] += 1
        survivors.append((args, rows))
    return stats, examples, survivors, time.time() - t0



# ===== sieves
"""Route B screen: regular sieves R (complete DFAs, <=3 states, alphabet abc)
that pass bounded (1,s_U) and (2,s_U) substitutability.  If R in C_{2,s_U},
then for every L in C_{2,s_U}, L' = L cap R is in C_{2,s_U} (prop i) and an
MCFL; rare type is the special case R = s_U^{-1}(zeta).
We classify surviving languages by a few known shapes."""
import itertools, sys, time

SIG = 'abc'

def words(N):
    for l in range(1, N + 1):
        for t in itertools.product(SIG, repeat=l):
            yield ''.join(t)

_TRIE = {}
def _trie(N):
    if N not in _TRIE:
        order = []  # (word, parent_index, letter_index)
        idx = {'': -1}
        frontier = ['']
        for l in range(N):
            nxt = []
            for p in frontier:
                for k, ch in enumerate(SIG):
                    w = p + ch
                    idx[w] = len(order)
                    order.append((w, idx[p], k))
                    nxt.append(w)
            frontier = nxt
        _TRIE[N] = order
    return _TRIE[N]

def dfa_lang(delta, fin, N):
    order = _trie(N)
    st = [0] * len(order)
    out = set()
    for i, (w, p, k) in enumerate(order):
        q = delta[0 if p < 0 else st[p]][k] if p >= 0 else delta[0][k]
        st[i] = q
        if q in fin:
            out.add(w)
    return out

def classify(L, N):
    """crude shape tags"""
    tags = []
    allw = list(words(N))
    if L == set(allw):
        tags.append('Sigma+')
    if not L:
        tags.append('empty')
    # union of s_U-type classes?
    has1 = {w for w in allw if 'c' not in w}
    hasz = set(allw) - has1
    if L in (has1, hasz):
        tags.append('type-class')
    # depends only on Parikh vector mod small groups / letters present?
    def parikh(w):
        return (w.count('a'), w.count('b'), w.count('c'))
    byP = {}
    for w in allw:
        byP.setdefault(parikh(w), set()).add(w in L)
    if all(len(v) == 1 for v in byP.values()):
        tags.append('parikh-determined')
    return tags or ['OTHER']

def run_sieves(nstates, N1=7, N2=5, budget=1500, N3=6):
    t0 = time.time()
    seen = {}
    for trans in itertools.product(range(nstates), repeat=nstates * 3):
        delta = [trans[3 * q:3 * q + 3] for q in range(nstates)]
        for k in range(1, 2 ** nstates):
            fin = {q for q in range(nstates) if k >> q & 1}
            L = frozenset(dfa_lang(delta, fin, N3))
            if L not in seen:
                seen[L] = (delta, fin)
        if time.time() - t0 > budget:
            print('budget hit during enumeration')
            break
    print('states<=%d: distinct languages (length<=%d signature): %d' % (nstates, N3, len(seen)))
    surv = []
    for L, (delta, fin) in seen.items():
        if not L:
            continue
        L5 = {w for w in L if len(w) <= N2}
        v, _ = check_substitutable(L5, N2, 1, max_report=1)
        if v:
            continue
        v, _ = check_substitutable(L5, N2, 2, max_report=1)
        if v:
            continue
        surv.append((L, delta, fin))
    # re-verify survivors at larger bounds (N3 then N1)
    surv6 = []
    for L, delta, fin in surv:
        L6 = dfa_lang(delta, fin, N3)
        v1, _ = check_substitutable(L6, N3, 1, max_report=1)
        if v1:
            continue
        v2, _ = check_substitutable(L6, N3, 2, max_report=1)
        if not v2:
            surv6.append((L, delta, fin))
    print('pass at N=%d: %d' % (N3, len(surv6)))
    final = []
    for L, delta, fin in surv6:
        L7 = dfa_lang(delta, fin, N1)
        v1, _ = check_substitutable(L7, N1, 1, max_report=1)
        v2, _ = check_substitutable(L7, N1, 2, max_report=1)
        if not v1 and not v2:
            final.append((L7, delta, fin))
    print('pass bounded d=1,2 at N=%d: %d ; at N=%d: %d' % (N2, len(surv), N1, len(final)))
    for L7, delta, fin in sorted(final, key=lambda z: sorted(z[0])[:5]):
        short = sorted(L7, key=lambda w: (len(w), w))[:8]
        print('  ', classify(L7, N1), 'delta=%s fin=%s' % (delta, sorted(fin)), 'shortest:', short)
    return final



# ======================================================================== verification helpers
def verify_violation(v, Lset, N):
    """Independent re-check of a reported (d,s_U) violation."""
    x, y, E0, E = v['x'], v['y'], v['E0'], v['E']
    d = len(x)
    assert len(y) == d and all(len(t) > 0 for t in x + y)
    assert ttype(x) == ttype(y), 'types differ'
    for ctx in (E0, E):
        assert len(ctx) == d + 1
        if d == 2:
            assert len(ctx[1]) >= 1, 'middle separator empty'
    def f(ctx, t):
        return ''.join(ctx[i] + t[i] for i in range(d)) + ctx[d]
    ok = (f(E0, x) in Lset and f(E0, y) in Lset and f(E, x) in Lset
          and f(E, y) not in Lset and len(f(E, y)) <= N and len(f(E, x)) <= N)
    return ok


def classify_presence(L7, N=7, k=3):
    allw = list(words(N))
    bad = set(w for w in allw if w not in L7)
    occ = {}
    for w in allw:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, min(n, i + k) + 1):
                occ.setdefault((w[i:j], i == 0, j == n), []).append(w)
    good_key = {key: all(x in bad for x in ws) for key, ws in occ.items()}
    unw = [w for w in bad if not any(good_key[(w[i:j], i == 0, j == len(w))]
                                      for i in range(len(w)) for j in range(i + 1, min(len(w), i + k) + 1))]
    return unw


def CE(n):
    fan = {'S': 1}; rules = []
    for i in range(n + 1):
        fan['E%d' % i] = 1
    rules.append(R('E0', [], ['a']))
    for i in range(1, n + 1):
        E, P = 'E%d' % i, 'E%d' % (i - 1)
        rules.append(R(E, [P, P], ['b', (0, 0), (1, 0), 'b']))
        rules.append(R(E, [P], ['c', (0, 0), 'c']))
    rules.append(R('S', ['E%d' % n], [(0, 0)]))
    return dict(start='S', fan=fan, rules=rules)


def blocks(w):
    i = 0; out = []
    while i < len(w):
        if w[i] == 'a':
            out.append(None); i += 1
        elif w[i] == 'c':
            j = i + 1
            while j < len(w) and w[j] == 'b':
                j += 1
            if j >= len(w) or w[j] != 'c' or j == i + 1:
                return None
            out.append(j - i - 1); i = j + 1
        else:
            return None
    return out


def mem_weight(n, aligned, dmax):
    def f(w):
        b = blocks(w)
        if b is None or any(d is not None and d > dmax for d in b):
            return False
        pos = 0
        for d in b:
            wt = 1 if d is None else 2 ** (n - d)
            if aligned and pos % wt:
                return False
            pos += wt
        return pos == 2 ** n
    return f


def lang_from_membership(mem, N, alph='abc'):
    return {''.join(t) for l in range(1, N + 1) for t in itertools.product(alph, repeat=l) if mem(''.join(t))}


def report_subst(name, L, N, expect_violation):
    """run d=1,2 bounded check; print first violation; verify it independently"""
    first = None
    for d in (1, 2):
        v, p = check_substitutable(L, N, d, max_report=1)
        print('    %s: |L_{<=%d}|=%d d=%d compared-pairs=%d violations=%d' % (name, N, len(L), d, p, len(v)))
        if v:
            if first is None:
                first = v[0]
            print('      WITNESS d=%d:' % d, fmt_viol(v[0]))
            test('%s d=%d witness independently verified' % (name, d), verify_violation(v[0], L, N))
    if expect_violation:
        test('%s violates (2,s_U)-substitutability (bounded, verified witness)' % name, first is not None)
    else:
        test('%s passes bounded (1,s_U),(2,s_U) check' % name, first is None)
    return first


# ======================================================================== main
def main():
    T0 = time.time()
    print('=' * 78)
    print('SECTION 1: controls')
    Sig = dict(start='S', fan={'S': 1, 'X': 1}, rules=[R('S', ['X'], [(0, 0)]), R('S', ['S', 'X'], [(0, 0), (1, 0)])] + [R('X', [], [ch]) for ch in 'abc'])
    AB = dict(start='S', fan={'S': 1, 'X': 1}, rules=[R('S', ['X'], [(0, 0)]), R('S', ['S', 'X'], [(0, 0), (1, 0)])] + [R('X', [], [ch]) for ch in 'ab'])
    ABp = dict(start='S', fan={'S': 1}, rules=[R('S', [], 'ab'), R('S', ['S'], ['a', 'b', (0, 0)])])
    for nm, G, N in [('POS Sigma+', Sig, 7), ('POS {a,b}+', AB, 9), ('POS (ab)+', ABp, 16)]:
        check_good(G); check_reduced(G)
        report_subst(nm, language(G, N), N, expect_violation=False)
    for n in range(1, 6):
        G = CE(n); check_good(G); check_reduced(G)
        test('CE n=%d: ||G||=13n+7, theta=4n, mu_1=3*2^n-2' % n,
             (size(G), thickness(G), mu_type1(G)) == (13 * n + 7, 4 * n, 3 * 2 ** n - 2),
             '(%d,%d,%d)' % (size(G), thickness(G), mu_type1(G)))
    G = CE(2); L = language(G, 30)
    report_subst('NEG CE n=2 (thm:doubling-no-lift family)', L, 30, expect_violation=True)
    v, _ = check_substitutable(L, 30, 1, max_report=1)
    test('NEG CE n=2 is (1,s_U)-substitutable (manuscript prop:three-letter-family(ii))', not v)

    print('=' * 78)
    print('SECTION 2: template search (doubling with escapes)')
    for fam in ('T1', 'T2'):
        st, ex, sv, dt = run(fam, budget=900)
        print('  family %s: %s  (%.1fs)' % (fam, st, dt))
        builder = T1 if fam == 'T1' else T2
        for key, (args, vv) in sorted(ex.items(), key=str):
            print('   example', key, 'template=', args)
            print('     ', fmt_viol(vv))
            nn = 2 if 'n2' in key[0] else 3
            Lchk = language(builder(nn, *args), 18 if nn == 2 else 26)
            test('  %s example %s re-verified' % (fam, key), verify_violation(vv, Lchk, 18 if nn == 2 else 26))
        test('%s: every template that is good/reduced/exponential/thin violates at n<=3' % fam,
             st['survive'] == 0 and st['total'] == (405 if fam == 'T1' else 2688), 'total=%d' % st['total'])

    print('=' * 78)
    print('SECTION 3: designed candidates')
    fams = [('A1_aligned', A1_aligned), ('A3_TM_cc', lambda n: A3_thue_morse(n, 'cc')),
            ('A3_TM_cb', lambda n: A3_thue_morse(n, 'cb')), ('A4_two_track', A4_two_track)]
    for nm, B in fams:
        rows = []
        for n in range(1, 8):
            G = B(n); check_good(G); check_reduced(G)
            assert max_fan(G) <= 2 and rank(G) <= 2
            rows.append((n, size(G), thickness(G), mu_type1(G)))
        print('  %s (n, ||G||, theta-bar, mu_1): %s' % (nm, rows))
        test('%s: mu_1 >= 2^n and theta-bar <= 4(n+1)^2 for n<=7 (poly size/thickness, exponential rare type)' % nm,
             all(r[3] >= 2 ** r[0] and r[2] <= 4 * (r[0] + 1) ** 2 for r in rows))
        for n, N in ((2, 14), (3, 16)):
            L = language(B(n), N)
            if nm == 'A1_aligned':
                L12 = lang_from_membership(mem_weight(n, True, n - 1), 12)
                test('A1 n=%d grammar language = aligned depth-labelled membership (len<=12)' % n,
                     {w for w in L if len(w) <= 12} == L12)
            report_subst('%s n=%d' % (nm, n), L, N, expect_violation=(not (nm == 'A1_aligned' and n == 2)))
    print('  membership-defined weight languages (block c b^d c has weight 2^(n-d))')
    for aligned in (False, True):
        for n in (2, 3):
            L = lang_from_membership(mem_weight(n, aligned, n), 12)
            report_subst('W%s n=%d' % ('-aligned' if aligned else '-sum', n), L, 12, expect_violation=True)

    print('=' * 78)
    print('SECTION 4: Route B regular sieves (complete DFAs, <=3 states)')
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fin2 = run_sieves(2)
        fin3 = run_sieves(3)
    print(buf.getvalue().split('\n')[0]); 
    for line in buf.getvalue().split('\n'):
        if line.startswith('states') or line.startswith('pass'):
            print('   ', line)
    cross = Counter(); np_other = 0
    for L7, delta, f in fin3:
        par = 'parikh-determined' in classify(L7, 7)
        pres = not classify_presence(L7)
        cross[(par, pres)] += 1
        if not par and not pres:
            np_other += 1
    print('    3-state survivors cross-tab (Parikh-determined?, presence-witnessed?):', dict(cross))
    test('sieves: 22 survivors (<=2 states), 197 survivors (<=3 states)', len(fin2) == 22 and len(fin3) == 197)
    test('sieves: every survivor is Parikh-determined or presence-witnessed (bounded, N=7)', np_other == 0)

    print('=' * 78)
    print('SECTION 5: Corollary R2 sanity (fan-out 1)')
    for n in (2, 3):
        N = 3 * 2 ** n
        L = language(CE(n), N)
        W = min((w for w in L if 'c' not in w), key=len)
        v1, _ = check_substitutable(L, N, 1, typed=False)
        v2, _ = check_substitutable(L - {W}, N, 1, typed=False, max_report=1)
        test('CE n=%d untyped 1-substitutable (bounded)' % n, not v1)
        ok = False
        # verify_violation checks types equal; for the untyped test types may differ, so check membership only
        if v2:
            vv = v2[0]
            def f(ctx, t):
                return ctx[0] + t[0] + ctx[1]
            ok = (f(vv['E0'], vv['x']) in L - {W} and f(vv['E0'], vv['y']) in L - {W}
                  and f(vv['E'], vv['x']) in L - {W} and f(vv['E'], vv['y']) not in L - {W})
            print('      untyped witness:', fmt_viol(vv))
        test('CE n=%d minus W_n is NOT untyped 1-substitutable (as Cor. R2 forces)' % n, ok)

    print('=' * 78)
    print('SECTION 6: Corollary U on A1 data, Prop LS randomized sanity')
    # Corollary U: in a language with a^mu (mu=mu_1) and cores c b^d c realized for an interval of d,
    # totals T_d must be affine.  In A1 (n=3) the cores c b c, c b b c have T = 4, 6 -> slope -2 ;
    # Cor. U forces c b^3 c with total 8 (= mu) or an inconsistency; A1 has no such word ->
    # the predicted violation is the one found in Section 3.
    n = 3; L = language(A1_aligned(n), 16)
    tot = {}
    for w in L:
        b = blocks(w)
        if b is not None and sum(1 for d in b if d is not None) == 1:
            d = [d for d in b if d is not None][0]
            tot.setdefault(d, set()).add(w.count('a'))
    print('    A1 n=3 single-core words: totals of a by label d:', sorted((d, sorted(s_)) for d, s_ in tot.items()))
    mu = 2 ** n
    Tc1, Tc2 = min(tot.get(1, {0})), min(tot.get(2, {0}))
    pred_total = Tc2 + (Tc2 - Tc1)          # Lemma C with nu=b, nu'=bb, frames (c,c) vs (cb,c)
    hyp = (tot.get(1) == {4} and tot.get(2) == {6} and 2 <= Tc1 <= mu - 1 and 2 <= Tc2 <= mu - 1 and pred_total >= 2)
    predicted = ['a' * g + 'cbbbc' + 'a' * (pred_total - g) for g in range(1, pred_total)]
    absent = all(w not in L and len(w) <= 16 for w in predicted)
    print('    Lemma C/Cor. U prediction: some a^g cbbbc a^h with g+h=%d must lie in L; present in A1? %s'
          % (pred_total, not absent))
    test('A1 n=3: Lemma C hypotheses hold and the forced word a^g c b^3 c a^h (g+h=%d) is absent => A1 not in C_{2,s_U}' % pred_total,
         hyp and absent)
    # Prop LS sanity: random small good CFG/MCFG, random presence pattern; shortest bad word <= bound
    cnt = 0; nonvac = 0
    for trial in range(300):
        nv = random.randint(2, 4)
        names = ['S'] + ['N%d' % i for i in range(1, nv)]
        fan = {x: 1 for x in names}
        rules = []
        for A in names:
            for _ in range(random.randint(1, 3)):
                k = random.choice([0, 1, 2])
                ch = [random.choice(names) for _ in range(k)]
                comp = []
                for j in range(k):
                    if random.random() < 0.5:
                        comp.append(random.choice('abc'))
                    comp.append((j, 0))
                if not comp or random.random() < 0.5:
                    comp.append(random.choice('abc'))
                rules.append(R(A, ch, comp))
        G = dict(start='S', fan=fan, rules=rules)
        try:
            check_good(G); check_reduced(G)
        except AssertionError:
            continue
        cnt += 1
        th = thickness(G); V = len(fan); rr = max(1, rank(G))
        u = ''.join(random.choice('abc') for _ in range(random.randint(1, 3)))
        k = len(u)
        bound = max(th, k * (k + 1) * 1 * V * (rr + 1) * th)
        # exact shortest word of L(G) containing u: DP over KMP automaton states (fan-out 1)
        def step(q, ch):
            if q == k:
                return k
            t = u[:q] + ch
            while t and not u.startswith(t):
                t = t[1:]
            return len(t)
        Q = range(k + 1)
        best = {(A, p_, q_): INF for A in fan for p_ in Q for q_ in Q}
        changed = True
        while changed:
            changed = False
            for (A, ch, tpl) in rules:
                comp = tpl[0]
                for p_ in Q:
                    states = {p_: 0}
                    for tok in comp:
                        new_states = {}
                        for q_, l_ in states.items():
                            if isinstance(tok, tuple):
                                B = ch[tok[0]]
                                for q2 in Q:
                                    vv = best[(B, q_, q2)]
                                    if vv < INF and l_ + vv < new_states.get(q2, INF):
                                        new_states[q2] = l_ + vv
                            else:
                                q2 = step(q_, tok)
                                if l_ + 1 < new_states.get(q2, INF):
                                    new_states[q2] = l_ + 1
                        states = new_states
                    for q2, l_ in states.items():
                        if l_ < best[(A, p_, q2)]:
                            best[(A, p_, q2)] = l_
                            changed = True
        sb = best[('S', 0, k)]
        if sb < INF:
            nonvac += 1
            # cross-check with brute force when small
            if sb <= 12:
                Lw = language(G, sb)
                assert min(len(w) for w in Lw if u in w) == sb
            assert sb <= bound, (sb, bound)
    test('Prop LS randomized sanity: shortest pattern-containing word <= k(k+1)f|V|(r+1)theta in all non-vacuous trials',
         nonvac > 20, 'grammars=%d nonvacuous=%d' % (cnt, nonvac))

    print('=' * 78)
    npass = sum(1 for _, c in RESULTS if c); nfail = len(RESULTS) - npass
    print('SUMMARY: %d tests, %d PASS, %d FAIL, elapsed %.1fs' % (len(RESULTS), npass, nfail, time.time() - T0))
    for nme, c in RESULTS:
        if not c:
            print('  FAILED:', nme)


if __name__ == '__main__':
    main()

===== END FILE =====

===== BEGIN FILE claude_fanout2_round12_candidate_rules_2026-11-15.md bytes=6374 sha256=7d1a44927df75120d5f0cb6ec2be15140596809a28ad5676b88d42afe22b38c0 =====
# 第十二段 候補文法の一覧（棄却されたものを含む）

**共通の設定**：`Σ={a,b,c}`、`s_U(a)=s_U(b)=1`、`s_U(c)=ζ`。規則は `A→(α₁,…,α_d)` と書く。変数 `x_k`、`y_k` は子0・子1の第k成分である。

検査の内容：

- すべての族について `n=1..7` で good・reduced・fan-out≤2・rank≤2 を assert で確認した。
- `‖G‖`、`θ̄`、`μ₁` は厳密に計算した。
- 証人は `check_round12_lower_bound_2026-11-15.py` の出力（`out_…txt`）からの写しである。
- 証人はすべて独立の関数 `verify_violation` で再検査した。中央の区切りが空でないこと、型が等しいこと、四つの語の所属、`|E[y]|≤N` を確認している。

## 1. テンプレート族 T1（fan-out 1、405件）

規則：

- `E₀→a`
- `E_i→ p E_{i−1} q E_{i−1} r`。`p,q,r∈{ε,a,b}`。
- `E_i→` 逃げ道。次の二種類のどちらか。
  - `s E_{i−1} t`。`(s,t)` は `(c,c)`、`(c,ε)`、`(ε,c)`、`(cb,c)`、`(c,bc)`、`(cc,c)`、`(c,cc)`、`(ca,c)`、`(c,ac)`、`(bc,cb)` のどれか。
  - 定数。`c`、`cc`、`cac`、`cbc`、`cbbc` のどれか。
- `S→E_n`

結果：

- 405件すべてで、`μ₁≥2^{n−1}`、`θ̄≤12n`（n≤6）が成り立つ。
- **405件すべてが n=2 で違反した**。内訳は d=1 で 241件、d=2 で 164件。

代表的な証人：

- `(p,q,r)=(b,ε,ε)`、逃げ道 `E→E c`、d=1：
  `x=b`、`y=bba` が文脈 `□aac` を共有する（`baac`、`bbaaac∈L`）。文脈 `□acac` で `bacac∈L` だが `bbaacac∉L`。
- `(ε,b,a)`、逃げ道 `cb E c`、d=2 の (1,1)：
  `x=(abaabab,a)`、`y=(ab,ababaa)` が `□a□a` を共有する。`□aa□` で `abaaababaa∉L`。
- `(a,ε,ε)`、逃げ道 `bc E cb`、d=2 の (ζ,ζ)：
  `x=(bca,acb)`、`y=(aaaabc,cb)` が `□a□` を共有する。`a□cbbc□` で `aaaaabccbbccb∉L`。

## 2. テンプレート族 T2（fan-out 2、2,688件）

規則：

- `D₀→(β₁,β₂)`。`β∈{(a,a),(a,b)}`。
- `D_i→(α₁,α₂)`。`α` は `x₁,x₂,y₁,y₂` を nonpermuting かつ nonmerging に二成分へ並べたもの（8通り）に、端の文字の挿入（7通り）を加えたもの。
- 逃げ道は二種類（計12通り）。
  - 一成分の子をとる `(s₁x₁t₁, s₂x₂t₂)`。c の配置は9通り。
  - 定数 `(c,c)`、`(cac,c)`、`(c,cbc)`。
- `S→x₁ m x₂`。`m∈{a,b}`。

結果：**2,688件すべてが n=2 で違反した**。内訳は d=1 で 1,952件、d=2 で 736件。

代表的な証人（d=2、(1,ζ)）：

- 並べ方 `(y₁x₁, x₂y₂)`、挿入 `L0=b, R1=a`、逃げ道 `(x₁, x₂c)`：
  `x=(baabbb,c)`、`y=(b,abbbac)` が `□a□` を共有する。`ba□ab□a` で `babababbbaca∉L`。

## 3. 設計した族

### A1 深さラベル付きの逃げ道（新規）

規則：

- `E₀→a`
- `E_i→E_{i−1}E_{i−1}`（1≤i≤n）
- `E_i→c B_{n−i} c`（1≤i≤n−1）
- `B₁→b`、`B_k→b B_{k−1}`
- `S→E_n`

性質：

- 逃げ道の塊 `c b^d c` は重み `2^{n−d}` を表す。
- 言語は、重みが整列した敷き詰めになっている語の全体である。長さ12まで、所属判定による定義と一致することを確認した。
- `‖G‖=16n−5`（n≥2）。`θ̄`：2, 5, 9, 14, 19, 25, 32。`μ₁=2ⁿ`。

判定：

- n=2 は有界検査を通る（言語は4語）。
- **n=3 で違反した。**
  - d=1：`x=aaaacbbc`、`y=cbcaa` が `□aa` を共有する。`aa□` で `aacbcaa∉L`。
  - d=2：`x=(aa,aaaa)`、`y=(a,aaaaa)` が c を含まない語 `a⁸` の中で `□a□` を共有する。`□cbbc□` で `acbbcaaaaa∉L`（整列が崩れる）。これは補題 P2 そのものである。
- 理論的な予言（補題 C、系 U）：`cb`・`cbb` の二つの塊の総計 4・6 から、`a^g cbbbc a^h`（g+h=8）が L に属さなければならない。A1 には含まれないので、A1 は C に属さない。

### A3 Thue–Morse（重なりのない c を含まない語。`lem:power-transfer` は使えない）

規則：

- `P₀→a`、`Q₀→b`
- `P_i→P_{i−1}Q_{i−1} | c P_{i−1} c`
- `Q_i→Q_{i−1}P_{i−1} | c Q_{i−1} c`（i<n）
- 変種 cb では `Q_i→cbQ_{i−1}bc`

性質：`μ₁=2ⁿ`。`θ̄` は線形（cc：3, 5, 8, 14, 20, 26, 32）。

判定：**n=2 で違反した。**

- cc 版、d=1：`abc` と `ca` が `□bc` を共有する。`c□` で `cca∉L`。
- cc 版、d=2：`(c,bc)` と `(c,cba)` が `□a□` を共有する。`□acc□` で `cacccba∉L`。
- 冪の移動がなくても、ζ 型の組の併合（N4）で壊れる。

### A4 二軌道（fan-out 2 を本質的に使う）

規則：

- `D₀→(a,a)`
- `D_i→(x₁ b y₁, y₂ b x₂) | (c x₁, x₂ c)`
- `S→x₁ a x₂`

性質：`‖G‖=16n+10`、`θ̄=4n+3`、`μ₁=2^{n+2}−1`。

判定：**n=2 で違反した。**

- d=1：`abcaaacba` と `caaac` が `c□c` を共有する。`ab□ba` で `abcaaacba∉L`。
- d=2 の (ζ,1)：`(c,bab)` と `(cab,b)` が `□a□aaababac` を共有する。`□ababaaa□ac` で `cabababaaabac∉L`。

### W-sum と W-aligned（所属判定で定義した重みの言語。比較用）

定義：`(a | c b^d c)⁺`（d≤n）のうち、重みの和が `2ⁿ` の語。aligned 版は二進の整列を課す。

判定：n=2,3 で、どちらも d=1 と d=2 の違反がある（ログの §3 末尾）。

## 4. 区別部分言語の候補（正則篩い R、`L′=L∩R`）

- 3状態以下の完全 DFA を全部列挙した。長さ6までの所属で区別すると 40,812 言語になる。
- `(2,s_U)` の有界検査（N=5,6,7）を通ったものは 197個（2状態以下では 22個）。
- 197個は、すべて次のどちらかに分類された。
  - Parikh 決定（111個）。可換群の剰余類と型の集合の組合せである。
  - presence 型（100個）。補集合が長さ3以下の局所的な証人の存在で決まる。presence 型には命題 LS が適用でき、多項式になる。
  - 両方に当てはまるものが14個ある。**どちらでもないものは0個**だった。
- 代表例：
  - `(ab)⁺`（presence 型）
  - 「c は末尾にだけ現れる」（presence 型）
  - `#c` の偶奇（Parikh 決定）
  - `s_U^{-1}(ζ)`（Parikh 決定。希少型そのもの）

===== END FILE =====

===== BEGIN FILE claude_fanout2_round12_lower_bound_checkpoint1_2026-11-15.md bytes=4565 sha256=84753472ece195c9d07ec2a54e3cf3d3fff0b82b1418731695bbcb5201cb4c29 =====
# 第十二段 チェックポイント1：`op:fanout-two` 超多項式下界の探索（2026-11-15）

**状態：`D` は得ていない（中心問題は OPEN のまま）。** 候補はすべて `B`（具体的な二穴または一穴の違反）で棄却した。下界の経路を制約する新しい命題を証明した（§4）。

## 1. 原稿で確認した事実（`main.tex`、2026-11-15 に clone した版）

- `def:tuple-substitutable`（514行）。`d=1..f` で成分ごとの型が等しい非空の組 `x⃗,y⃗` が受理文脈を一つ共有すれば、分布は等しい。`d=2` の文脈は `v₀□v₁□v₂`（`v₁∈Σ⁺`）。
- `def:grammar-properties`（468行）。good は ε-free・nondeleting・nonpermuting・nonmerging。reduced は全非終端記号が到達可能かつ生成的。
- 厚さ（1008行）。`θ_G(R)` は R を使う文の最小長、`θ̄=max(1,max_R θ_G(R))`。`lem:thickness-equivalence` (i) 各規則が明示的に書く終端記号は `θ_G` 個以下、(ii) `t_G≤θ_G`、(iv) 短い文脈 `E_A`。
- `prop:abelian-coset-filter`（554行）。(i) 共通部分で閉じる、(ii) 可換群の剰余類で閉じる（無限群でもよい）、(c) `ŝ^{-1}(Acc)` は代入可能。
- `lem:type-deletion`、`lem:distinguishing`（1178行）、`prop:rare-type`（1195行）。
- `thm:local-group-polydata`（1527行、定理 A）。`S∈LG` なら `Wit(G̃₀)` は `B^{≤r}_{f,s}` の特徴標本で、総長は `O(‖G‖²θ̄)`。**自明型付けにも適用できる**。
- `prop:three-letter-family`、`lem:power-transfer`、`thm:doubling-no-lift`、`op:fanout-two`（2131行）。依頼書 §2–3 の記述と一致した。差異はない。
- 退避された原稿 `parked/2026-11-06_focus/main_before_focus_59pp.tex` の `lem:unique-word-rigid`、`prop:unique-two-letter-shapes`（5つの形）、`lem:unique-word-gap`（密度）、`prop:unique-word-route` も参照した。

## 2. 検証器と対照

`check_round12_lower_bound_2026-11-15.py`（標準ライブラリのみ、seed 20261115、約4分）の機能：

- good の4性質を assert で検査する。
- `‖G‖`、`θ̄`（内側最小長と外側最小長の不動点）、`μ₁`（c を含まない規則だけの最小内側長）を厳密に計算する。
- 長さ `≤N` の言語を列挙する。
- `d=1,2` の有界な代入可能性検査を行う。`d=2` では `v₁≠ε` を assert する。
- 違反は独立の `verify_violation` で再検査する。

対照の結果：

- 正の対照 `Σ⁺`、`{a,b}⁺`、`(ab)⁺` はすべて違反なし。
- 負の対照：三文字倍増族 `n=1..5` は `‖G‖=13n+7`、`θ̄=4n`、`μ₁=3·2ⁿ−2` を再現した。`n=2` で既知の二穴違反を検出した。
  - `x=(c,cc)`、`y=(bcac,cb)`。共有文脈 `□ca□`。`E=b□a□acb` で `E[y]=bbcacacbacb∉L`。

## 3. 最初の候補と二穴判定

| 候補 | 規則（要点） | ‖G‖, θ̄, μ₁ | 判定 |
|---|---|---|---|
| T1/T2 テンプレート 3,093 件 | 倍増と逃げ道（fan-out 1 と 2） | 多項式, 多項式, ≥2ⁿ⁻¹ | すべて `n=2` で違反 |
| A1 深さラベル | `E_i→E E \| c b^{n−i} c` | `16n−5`（n≥2）, `O(n²)`, `2ⁿ` | `n=3` で違反（§4 補題C の予言どおり） |
| A3 Thue–Morse | `P_i→P Q \| cPc` | 多項式, 線形, `2ⁿ` | `n=2` で違反 |
| A4 二軌道 | `D_i→(x₁by₁, y₂bx₂) \| (cx₁, x₂c)` | `16n+10`, `4n+3`, `2ⁿ⁺²−1` | `n=2` で違反 |
| B 正則篩い | 3状態以下の DFA 40,812 言語 | — | 197個が代入可能。すべて Parikh 決定か presence 型 |

完全な証人文字列は報告書の §5 と実行ログにある。

## 4. この時点での新しい命題（証明は最終報告）

- **定理 R**：L と L′ がともに LG 型付けで代入可能なら、`L∖L′` に `O(‖G‖²θ̄)` 以下の語がある。系として、区別部分言語の経路は「型に本質的に依存する」対でなければならない。
- **命題 LS**：L∖L′ が「長さ k 以下の局所的な証人の存在」で定まるなら、最短差語は `≤k(k+1)f|V|(r+1)θ̄`。
- **補題 S**：c を含まない語の各長さの切片は、型なしで f-代入可能である。
- **補題 C（補償）**：`a^{μ₁}∈L` のとき、同じ型の二つの枠の a の不足の差は、中央に依存しない。
  - 系 U：単項の深さラベルは重みがアフィンになる。

## 5. 判定

`D` は得ていない。探索を続けて最終報告へ進む。

===== END FILE =====

===== BEGIN FILE claude_fanout2_round12_lower_bound_report_2026-11-15.md bytes=24257 sha256=b8997dfd1f03152ef4844ee3adc692d180d8b343fb3c79cc53eca76089ff045a =====
# 第十二段 最終報告：`op:fanout-two` の超多項式下界の探索（U₁ 型付け、fan-out 2）

Claude（Opus 5.5）、2026-11-15 JST。この報告は数学の研究記録である。論文の原稿ではなく、GitHub も編集していない。

## 一文結論

**OPEN。** 超多項式の下界をもつ族は構成できなかった。その代わり、下界の二つの経路（希少型の経路と区別部分言語の経路）を狭める新しい命題を四つ証明した。

- 定理 R：LG 型付けで代入可能な部分標的は短い区別語をもつ。
- 命題 LS：presence 型の篩いでは最短の差語が多項式長になる。
- 補題 S：c を含まない語の長さの切片は、型なしで代入可能である。
- 補題 C と系 U：a 冪の希少語のもとでの補償法則。

候補は全部で 3,093 のテンプレートと、設計した 4 族＋比較用 2 種である。すべて具体的な二穴（または一穴）の違反で棄却した。

### 成否表

| 探索対象 | 正確な状態 | 根拠・反例 | 残る仮定 |
|---|---|---|---|
| 希少 U₁ 型による超多項式下界 | **OPEN（構成なし）** | 候補はすべて違反した（§4）。補題 C・系 U により、単項の深さラベルによる設計は（余裕条件の下で）不可能（証明済み） | 予想 A（§5）は未証明 |
| 区別部分言語による超多項式下界 | **OPEN（構成なし）** | 定理 R：LG 型付けで代入可能な対は不可。命題 LS：presence 型の篩いは不可。3状態以下の正則篩いはすべて Parikh 決定か presence 型（有界な全数調査） | Parikh 決定の篩い（希少型と剰余類の組合せ）、非正則の L′ |
| `(2,s_U)`-substitutability | 全候補で**違反あり**（`B`）。正の対照は有界 PASS | 証人は完全な文字列で記録し、独立に再検査した（ログ 72/72 PASS） | 有界の PASS は所属の証明ではない |
| 固定 `Σ,s`、rank2 の good MCFG、多項式の大きさ・厚さ | 全候補で満たす（assert で検査）。たとえば A1 は `‖G‖=16n−5`、`θ̄=O(n²)`、`μ₁=2ⁿ` | `check_round12…py` の §2–3 | — |
| `op:fanout-two` at f=2 | **OPEN** | — | — |
| `op:fanout-two` at f≥3 | **OPEN** | 定理 R と命題 LS は任意の f で成り立つ。補題 S は任意の f、補題 C は f≥2 で成り立つ | 下界の構成はない |

反例の分類：候補への違反はすべて `B` である。補題 C は A1 型の設計方針への反例 `A` を与える。`D` と `E` はない。

---

## 1. 原稿の確認

`main.tex` を読み、依頼書が挙げた全ラベルの量化を照合した。依頼書 §2–3 との差異はなかった。追加で次の点を確認した。

- `prop:abelian-coset-filter` (ii) は無限の可換群（例：長さ写像 Σ*→ℤ）でも代入可能性を保つ。MCFL であることは別の問題である。
- `thm:local-group-polydata`（定理 A）は自明型付け（`|T|=1`）を含む任意の `S∈LG` に適用できる。
- 退避された 59ページ版から、`lem:unique-word-rigid`、`prop:unique-two-letter-shapes`（5つの形）、`lem:unique-word-gap`（密度）を参照した。**これらは現行の原稿には含まれていない。**

以下で、G は reduced で good な MCFG とする。`θ:=θ̄_G` とし、rank は ≤r、fan-out は ≤f とする。`x_η`、`o_η` は節点 η の内側と外側である。事実 F（`y∈L_A`、`o∈Out(A)` なら `o[y]∈L(G)`）、`lem:thickness-equivalence` (i)(ii) を使う。

---

## 2. 新しく証明した結果

### 2.1 定理 R（LG で型付けされた部分標的は短く区別される）［証明済み・新規と判断］

**定理 R.** 次を仮定する。

- `f,r≥1`、`t:Σ⁺↠T` は `T∈LG` への型付け。
- `L,L′∈C^{mcf}_{f,t}`、`L′⊊L`。
- G は `L∩Σ⁺` の presentation。

このとき `L∖L′` は ε を含むか、長さ `≤‖Wit(G̃₀)‖_+=O_{f,r,|T|}(‖G‖²θ̄_G)` の語を含む。

*証明.* 定理 A より、`F:=Wit(G̃₀)∪({ε}∩L)` は `B^{≤r}_{f,t}` の特徴標本である。`lem:distinguishing`（型付け t のもとで適用）より、`F∩(L∖L′)≠∅`。F の各語は ε か、長さが `‖F‖_+` 以下である。∎

**系 R1（区別の経路は型に本質的に依存しなければならない）.** 任意の型付け s について、次を仮定する。

- `L,L′∈C_{f,s}`、`L′⊊L`。
- `min|L∖L′|` が定理 A の定数 `C_{f,r,|T|}‖G‖²θ̄` を超える。

このとき、同じ Σ 上の**どの** LG 型付け t についても、L と L′ の少なくとも一方は `C_{f,t}` に属さない。特に、どちらか一方は型なしでは f-代入可能でない。

**系 R2（希少型）.** `L∈C_{f,s}`、`m∈S_L`、`μ_m(L)>C‖G‖²θ̄` とする。このとき、どの LG 型付け t についても、`L∉C_{f,t}` または `L^{∖m}∉C_{f,t}` である。

*証明.* `L′=L^{∖m}`（`lem:type-deletion`）として系 R1 を適用する。差集合の最短語の長さは `μ_m` である。∎

**検算.** fan-out 1 の三文字倍増族 `L_n` は型なしで代入可能であり、`μ₁` は指数的である。したがって、系 R2 から `L_n∖{W_n}` は型なしの 1-代入可能性を満たさないはずである。実際、n=2,3 で証人が見つかった（ログ §5）。

- n=2 の証人：`bcac` と `bbaab` が文脈 `□cacb` を共有する。文脈 `□baabb` では `bbaabbaabb∉L∖{W}` である。
- この証人では型の違う組が比べられている。これが「型への本質的依存」の具体的な姿である。

**意義.**

- 過去の報告 `chatgpt_distinguishing_route` の D2-G（一般の L′ に対する区別語の上界）は未解決だった。定理 R は、そのうち L′ が LG 型付けで代入可能な場合を解決する。
- これまでに知られている型なしの代入可能な言語（`Σ⁺`、`(ab)⁺`、可換群の篩い）だけを組み合わせても、区別の経路は成立しない。

### 2.2 命題 LS（presence 型の篩いは短い）［証明済み・文法だけの事実］

**定義.** パターンとは `(u,π,σ)` のことである。`u∈Σ⁺`、`|u|≤k`、`π,σ∈{0,1}` とする。`w=puq` で、`π=1⇒p=ε` かつ `σ=1⇒q=ε` が成り立つとき、パターンは w に出現するという。パターンの集合 `𝒫` に対し、`B(𝒫)` をいずれかのパターンが出現する語の全体とする。

**命題 LS.** `L(G)∩B(𝒫)≠∅` ならば、それは長さ `≤max{θ, k(k+1)f|V|(r+1)θ}` の語を含む。代入可能性は使わない。

*証明.* 準備として次を固定する。

- `w∈L(G)∩B(𝒫)` を長さ最小にとり、その中で節点数が最小の導出 T をとる。
- パターンの出現位置の区間を O とする（`|O|≤k`）。
- `Y(η)` を `x_η` の文字の位置の集合とする。`|x_η|>θ` の節点を重いと呼ぶ。

**(1) 重い節点は O と交わる。** `Y(η)∩O=∅` と仮定する。

- O は区間であり、穴の区間とは交わらない。よって O は `o_η` のある固定部分 `v_t` に含まれる。
- `y∈L_{A_η}` で `‖y‖≤θ` のものがある（厚さ補題 (ii)）。`w′=o_η[y]∈L(G)` は O を、π と σ の位置関係を保ったまま含む（`v₀` は先頭に、`v_d` は末尾に残る）。
- しかも `|w′|<|w|` なので、最小性に反する。

**(2) 連鎖の長さ.** `p∈O` に対し、`C_p:=` {重い η で `p∈Y(η)`} とおく。これは根からの一本の鎖である。`κ(η)` を、`x_η` の中で p を含む成分の番号とする。

主張：状態 `(A,κ)` が同じ節点は、`C_p` の中に高々 `k+1` 個しかない。

- 同じ状態の連続する二節点 `η⊋η′` をとり、`D:=Y(η)∖Y(η′)` とおく。
- `w′:=o_η[x_{η′}]∈L(G)` の導出は、T より節点数が少ない。また `|w′|=|w|−|D|` である。
- 成分の埋め込み写像 φ（`x_{η′}` の第 j 成分 `I_j` が `x_η` の第 φ(j) 成分 `J_{φ(j)}` に入る）は、nonpermuting な合成なので単調である。p の位置から `φ(κ)=κ` である。
- 同じ `J` に入る二つの `I` の間には、少なくとも1文字ある（ε-free と nonmerging の合成から）。

`D∩O=∅` と仮定する。O を p から左へたどる。

- `I_κ` の左端で O が止まらないのは、`I_κ` が `J_κ` の先頭にあり、その左が外側部分 `v_{κ−1}` である場合だけである。`w′` でも、穴 κ の内容 `I_κ` の左は `v_{κ−1}` である。
- さらに `v_{κ−1}` を越えて左へ進むなら、次の文字は `J_{κ−1}` の末尾である。上の性質から、そこは `I_{κ−1}` の末尾で、`φ(κ−1)=κ−1` となる。

帰納法により、O の文字は w でも `w′` でも同じ並びの断片になる。断片は外側の固定部分と、`I_j`（穴 j に入る）である。右へも同様である。先頭・末尾の条件も保たれる。

よって `w′∈B(𝒫)` となり、最小性に反する。同じ状態の節点 `η₁⊋…⊋η_m` の連続対がつくる `D_s` は互いに素なので、O と交わるものは高々 k 個である。ゆえに `m−1≤k`。状態は `≤f|V|` 個なので、`|C_p|≤(k+1)f|V|` となる。

**(3) 数え上げ.** (1) より、重い節点は `⋃_{p∈O}C_p` に含まれる。その個数は `≤k(k+1)f|V|` である。w の各文字は、重い節点の規則が直接書く文字（`≤θ`）であるか、重い節点の軽い子（`≤r` 個、各 `≤θ`）に含まれる。根が軽ければ `|w|≤θ` である。∎

**系 LS（区別の経路）.** `L′=L∖B(𝒫)` が `C_{f,s}` に属するとき、`min|L∖L′|≤k(k+1)f|V|(r+1)θ̄`。L′ が正則であることは要らない。

**正則篩いの全数調査（有界）.**

- 3状態以下の完全 DFA を列挙し、長さ6までの所属で区別して 40,812 言語を得た。
- `(2,s_U)` の有界検査（N=5,6,7）を通ったものは 197個だった。
- 197個は、Parikh 決定（111個）か presence 型（長さ3以下のパターン、100個）のどちらかである。両方に当てはまるものが14個、**どちらでもないものは0個**。
- presence 型には命題 LS が適用でき、多項式になる。
- Parikh 決定のものは、可換群の剰余類（D1-A により短い）と型の集合との組合せである。型の集合の部分は希少型そのものである。
- したがって、**小さな正則篩いによる区別の経路は、結局「希少型と剰余類の組合せ」に帰着する**（観察）。

**補足（`Σ⁺` の部分標的）.** `L′∈C_{1,s}` かつ `L′⊊Σ⁺` なら、`Σ⁺∖L′` は長さ `≤|S|+1` の語を含む。

*証明.* 最短の `w=σw′∉L′` をとり、`|w|≥|S|+2` と仮定する。

- 型 `s(w′)` を実現する語 y で `|y|≤|S|` のものがある。
- `w′,y∈L′` は文脈 `(ε,ε)` を共有するので、等価である。
- したがって `σy∉L′` となるが、`|σy|<|w|` なので最小性に反する。∎

### 2.3 補題 S（c を含まない長さの切片）と系 S［証明済み］

**補題 S.** `L∈C_{f,s_U}`、`ℓ≥1` とする。`K_ℓ:=L∩{a,b}^ℓ` は、型なしで f-代入可能な有限言語である。

*証明.*

- `K_ℓ=L∩ŝ^{-1}(1)∩len^{-1}(ℓ)` と書ける。`prop:abelian-coset-filter` の (c)、(i)、(ii)（`ℤ`、`H=0`）により、`(f,s_U)`-代入可能である。
- `K_ℓ` で文脈を共有する組は、すべて `{a,b}` 上の組であり、型はすべて 1 である。
- よって型付きの条件と型なしの条件は一致する。∎

**系 S.** `W∈L∩{a,b}⁺` が、`L∩{a,b}^{|W|}` の中で唯一の語であり、`|W|≥7` であるとする。このとき W は 5つの形（`x^n`、`x^{n−1}y`、`yx^{n−1}`、`yx^{n−2}y`、交互の語）のどれかである。

- 退避された `thm:app-singleton` を、`{W}=K_{|W|}` に適用すればよい。
- 退避された `prop:unique-two-letter-shapes` は、**型 1 の語全体の中での唯一性**を仮定していた。系 S は、それを**同じ長さの中での唯一性**に弱めたものである。
- 特に、最短の c を含まない語がその長さで唯一なら、5つの形のどれかである。

### 2.4 a 冪を最短とする希少語のもとでの補償法則［証明済み］

以下、`L∈C_{2,s_U}`、`a^μ∈L`、`μ=μ₁(L)≥3` を仮定する。μ は最短の型 1 の語の長さであり、唯一性は仮定しない。

**補題 P2（すべり）.** `Pa^αMa^βQ∈L` で、`α,β≥1`、`M∈Σ⁺`、`α+β≤μ−1` とする。このとき、`α′+β′=α+β`、`α′,β′≥1` をみたす全ての組について `Pa^{α′}Ma^{β′}Q∈L`。

*証明.* `(a^α,a^β)` と `(a^{α′},a^{β′})` は型 (1,1) で、文脈 `□a^{μ−α−β}□`（中央は空でない）を共有する。よって等価である。∎

**補題 P3（総計の剛性）.**

- 二穴：`Pa^αMa^βQ` と `Pa^{α′}Ma^{β′}Q` がともに L に属し、指数がすべて ≥1、和が ≤μ−1 なら、`α+β=α′+β′`。
- 一穴：`Pa^αQ` と `Pa^{α′}Q` がともに L に属し、`1≤α,α′≤μ` なら、`α=α′`。

*証明.* 二つの組は文脈を共有するので等価である。和の大きい方を `a^μ` の文脈に入れ、和の小さい方と取り替えると、μ より短い c を含まない語が得られる。∎

**補題 C（補償）.** 次を仮定する。

- `t₁,t₂,t̃₁,t̃₂∈Σ*` で、`[c∈t_i ⇔ c∈t̃_i]`（i=1,2）。
- `ν,ν′∈Σ⁺`。
- `a^g t₁νt₂ a^h`、`a^{g̃} t̃₁νt̃₂ a^{h̃}`、`a^{g′} t₁ν′t₂ a^{h′}` がすべて L に属する。
- 指数はすべて ≥1。和 `T=g+h`、`T̃=g̃+h̃`、`T′=g′+h′` は `[2,μ−1]` に入る。
- `Δ:=T̃−T` について `T′+Δ≥2`。

このとき、ある分割で `a^{·} t̃₁ν′t̃₂ a^{·}∈L` となり、その a の総数は `T′+Δ` である。`T′+Δ≤μ−1` なら、全ての分割で成り立つ。言い換えると、**型が同じ二つの枠の a の不足の差は、中央 ν によらない。**

*証明.* `α:=max(1,1−Δ)` とし、組 `x=(a^αt₁, t₂a)`、`y=(a^{α+Δ}t̃₁, t̃₂a)` をとる。成分ごとの型は等しい。

- 文脈 `E=a^{T−α−1}□ν□` を考える。
  - `E[x]` は a の総数 T で、P2 により L に属する。
  - `E[y]` は a の総数 T̃ で、P2 により L に属する。
  - したがって `x≡y`。
- 文脈 `E′=a^{T′−α−1}□ν′□` では、P2 により `E′[x]∈L`。よって `E′[y]∈L` で、その a の総数は `T′+Δ` である。
- 必要な不等式 `α≤T−1`、`α≤T′−1` は、`T̃≥2` と `T′+Δ≥2` から従う。∎

**系 U（単項ラベル）.** d が区間 `D=[d₀,d₁]`（`d₀≥1`、`d₁>d₀`）を動くとき、`a^{g_d} c b^d c a^{h_d}∈L`（`g_d,h_d≥1`）とし、`T_d:=g_d+h_d`、`κ_d:=T_{d+1}−T_d` とおく。

**(i) 強制される語.** `e,e+1,e′∈D` で `T_e,T_{e+1},T_{e′}∈[2,μ−1]`、`T_{e′}+κ_e≥2` とする。このとき、L は a の総数 `T_{e′}+κ_e` の語 `a^{·}cb^{e′+1}c a^{·}` を含む。

- 補題 C を、枠 `(c,c)` と `(cb,c)`、中央 `b^e` と `b^{e′}` に適用すればよい。
- `e′+1∉D` でもよい。たとえば `e′=d₁` の場合も含む。

**(ii) アフィン性.** `M:=max_{d}|κ_d|` とし、すべての `d∈D` で `T_d∈[2+M, μ−1]` とする。このとき κ は D 上で一定、すなわち `T_d` はアフィンである。

*証明.* `e,e′` を `e,e+1,e′,e′+1∈D` かつ `κ_e<κ_{e′}` ととれたと仮定する。

- (i) より、総計 `T_{e′}+κ_e` をもつ核 `cb^{e′+1}c` の語が L にある。条件 `≥2` は、`T_{e′}≥2+M` から従う。
- 同じ核の語として、総計 `T_{e′+1}=T_{e′}+κ_{e′}` のものもある。
- 二つの総計のうち大きい方は `T_{e′+1}≤μ−1` である。よって P3 が適用でき、二つの総計は等しくなければならない。これは `κ_e<κ_{e′}` に反する。
- e と e′ を入れ替えれば、`κ_e>κ_{e′}` も同様に排除できる。∎

**帰結.** `c b^d c` に重み `ω_d=μ−T_d≈2^{n−d}` を割り当てる設計では、κ が等比的に変わる。μ に十分な余裕があり、(ii) の仮定が満たされれば、|D|≥3 で破綻する。

**A1（n=3）での確認.** (i) だけで足りる。`T₁=4`、`T₂=6` から、e=1、e′=2 として `a^g cbbbc a^h`（g+h=8）が強制される。しかし A1 はこの語を含まない（ログ §6）。

- 計算で見つかった d=2 の違反は、`(aa,aaaa)` と `(a,aaaaa)` が `a⁸` の中で `□a□` を共有し、`□cbbc□` で崩れるというものである。これは P2（すべり）が整列を壊す直接の例である。
- **注意**：P3 は「大きい方の総計 ≤μ−1」を必要とする。`L∩a⁺={a^μ}`（一意性）を仮定しない限り、総計が μ 以上の語との比較はできない。

**位置づけ.** 内容型付けについては、「重み 2^i の接頭符号はアフィンに強制される」という先行の観察がある（README (94)）。補題 C は、その U₁ 型付け版を、最短語が a 冪である一般の状況で、一般の枠について厳密化したものである。

---

## 3. 障壁の一覧（§5.1 の要求）

| 操作・障壁 | 何を壊すか | 状態 |
|---|---|---|
| 二穴での冪の移動（`lem:power-transfer`） | 唯一性（長さは保たれる） | 原稿 |
| ζ 型の文脈の共有（N4） | c を含む組が粗く併合される。T1/T2 の d=1 違反の大半と、A3、A4 の d=1 | 観察（今回も最多） |
| すべり P2・総計の剛性 P3 | `a^μ` の中の c を含まない二つ組は、どの c 文脈でも和だけで振る舞う | **証明済み** |
| 補償 C・系 U | 枠の不足の差が中央によらない。指数的なラベル付けが崩れる | **証明済み** |
| 中央が空でない区切り | 隣接する穴は禁止。P2 は中央 `a^{μ−α−β}` が空でないことに依存する | 定義 |
| 型の削除後の組代入 | `L^{∖m}` が LG で型付けされていれば、希少型は短い | **定理 R・系 R2** |
| presence 型の篩い | 区別語は ≤`k(k+1)f|V|(r+1)θ̄` | **命題 LS** |
| 可換群の篩い（D1-A） | 区別語は ≤θ̄ | 過去の報告 |
| 局所計数・射影（U₂ など） | 特殊クラスでは多項式 | 過去の報告（流用はしない） |
| 密度（`lem:unique-word-gap`(ii)） | 長い希少語には、c を多く含む短い語が必要 | 退避された原稿 |

---

## 4. 候補と棄却の理由

規則の全文は `claude_fanout2_round12_candidate_rules_2026-11-15.md` にある。証人はログからの写しで、すべて独立に再検査した。

| 候補 | 新しい点 | `‖G‖`, `θ̄`, `μ₁` | 最初の違反 | 分類 |
|---|---|---|---|---|
| T1（405件） | fan-out 1 の倍増と、多様な逃げ道 | 多項式, ≤12n, ≥2^{n−1} | 全件が n=2 で違反（d=1 で 241件、d=2 で 164件） | B |
| T2（2,688件） | fan-out 2 の二成分テンプレートの全配置 | 同上 | 全件が n=2 で違反（d=1 で 1,952件、d=2 で 736件） | B |
| A1 深さラベル | 塊 `cb^dc` が 2^{n−d} を表す。c を含まない語は `a^{2ⁿ}` | `16n−5`, `O(n²)`, `2ⁿ` | n=3、d=2：`(aa,aaaa)` と `(a,aaaaa)`、共有 `□a□`（`a⁸`）、`□cbbc□` で `acbbcaaaaa∉L` | B（補題 C の予言どおり） |
| A3 Thue–Morse | 重なりのない c を含まない語（冪の移動が使えない） | 線形, 線形, `2ⁿ` | n=2、d=1：`abc` と `ca`、共有 `□bc`、`c□` で `cca∉L` | B（N4） |
| A4 二軌道 | fan-out 2 で両軌道を同時に逃がす | `16n+10`, `4n+3`, `2^{n+2}−1` | n=2、d=2：`(c,bab)` と `(cab,b)`、`□ababaaa□ac` で `cabababaaabac∉L` | B |
| W-sum / W-aligned | 所属判定で定義した重みの和 | 文法なし | n=2,3 で d=1 と d=2 の違反 | B |
| 区別部分言語：正則篩い ≤3状態 | `L′=L∩R` | — | 197個の生き残りはすべて Parikh 決定か presence 型 | 経路の障壁（命題 LS、D1-A） |

**修復の見積もり.** A1 を補題 C に従って修復すると、ラベルの重みがアフィンになる。すると言語は加法的な重みの一つの水準に入り、既存の重み付き水準の定理により多項式になる。したがって修復しても A1 は救えない。

---

## 5. 未解決の義務と次の一手

**予想 A（OPEN）.** `L∈C_{2,s_U}` で、`a^{μ₁}∈L` とする。このとき `μ₁≤poly(‖G‖,θ̄)` か。

- **証拠**：補題 P2、P3、C により、核（a を含まない極大な因子）の重みは枠ごとに加法的に分離される。核の重みが文字ごとに加法的で、文脈（状態）に依存しないなら、目盛りの隙間の議論で多項式になる。理由は次のとおり。
  - 重い経路では、大きさが比 `≤r+1` で減っていく。
  - 長さ `≤θ` の核の重みは、`θ·max(文字の重み)` の倍数の近くにしか集まらない。
- **障壁**：状態に依存する重み（CE 型の深さの符号）は、まだ排除できていない。補題 C は「同じ型の枠の対の中央がずれる」場合だけを拘束する。剛直な（中央の置き換えが利かない）核の族が存在しうる。
- **意義**：予想 A と系 S を合わせると、「最短の c を含まない語が、その長さで唯一の `x^n`」という形の希少型の経路が閉じる。残る4形は同様の扱いが必要である。

**次の最短の一手.**

1. 予想 A を、「各語の核が ≤k 個」の部分クラスで、まず補題 C を使って証明する。
2. 区別部分言語の経路の残りは「希少型と剰余類の組合せ」と非正則の L′ である。前者は、`L∩ŝ^{-1}(m)∩g^{-1}(γ+H)` の最短語が希少型の最短語から多項式で抑えられるかという問題に帰着できるか確かめる。
3. 下界の側では、系 R1 により L または L′ が「型付きでしか代入可能でない」必要がある。そこで、型なしの違反を一つだけ持つ（型の違う組を比べたときだけ壊れる）言語を出発点に設計する。
4. f≥3 は手つかず。

## 6. 証明の出自

- §2 の証明はすべて Claude の手証明であり、第三者による監査や形式証明は受けていない。
- コードは、有界の数値によってのみ裏づけを与える。
  - 系 R2 の検算：n=2,3。
  - 系 U の予言：A1、n=3。
  - 命題 LS：乱数で生成した文法 93件（うち非空のもの 72件）。fan-out 1 で、KMP オートマトンとの積の DP による厳密な最短長を、上界と比較した。
- 原稿の定理（定理 A、`lem:distinguishing`、`prop:abelian-coset-filter`、退避された `thm:app-singleton`）は引用したもので、ここでは再証明していない。

## 7. ファイル

| ファイル | 内容 |
|---|---|
| `claude_fanout2_round12_lower_bound_checkpoint1_2026-11-15.md` | チェックポイント |
| `claude_fanout2_round12_lower_bound_report_2026-11-15.md` | 本報告 |
| `claude_fanout2_round12_candidate_rules_2026-11-15.md` | 候補規則の一覧 |
| `check_round12_lower_bound_2026-11-15.py` | 検証器。`python3 -I` で実行し、約4–5分。SHA256 `7571974956a1bcadc8163b08c175e3501d2305fd47902bee5b43a37062d38709` |
| `out_check_round12_lower_bound_2026-11-15.txt` | 実行ログ。**72 tests / 72 PASS / 0 FAIL**。二回の実行で、時間の表示以外は同一。SHA256 `08dcf90851d4cdfdb6f0e03318baa22af20650af566081532bdd8a17b056b0af` |

===== END FILE =====

===== BEGIN FILE independent_presence_check.py bytes=2295 sha256=0ef227cd79df4232a6a26e9b0654f8e256a8a77a7f3def14b066d7135cd24c6f =====
#!/usr/bin/env python3
"""Independent correction of Round12 finite presence-pattern classification.
For patterns (u,pi,sigma), the conditions pi=1 => prefix, sigma=1 => suffix.
pi/sigma=0 do NOT forbid prefix/suffix occurrences.
"""
import contextlib, io, itertools, importlib.util, time, json
from collections import Counter
from pathlib import Path
P=Path(__file__).parent
spec=importlib.util.spec_from_file_location('round12',P/'check_round12_lower_bound_2026-11-15.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
words=[''.join(w) for n in range(1,8) for w in itertools.product('abc',repeat=n)]
ix={w:j for j,w in enumerate(words)}
ALL=(1<<len(words))-1
pats=[]
for k in range(1,4):
 for t in itertools.product('abc',repeat=k):
  u=''.join(t)
  for pre,suf in itertools.product((0,1),repeat=2):
   mask=0
   for i,w in enumerate(words):
    if pre and not w.startswith(u):continue
    if suf and not w.endswith(u):continue
    if u in w and (not pre or w.startswith(u)) and (not suf or w.endswith(u)):
     mask|=1<<i
   pats.append((u,pre,suf,mask))
print('patterns',len(pats), 'words',len(words),flush=True)
start=time.time()
with contextlib.redirect_stdout(io.StringIO()):
 survivors=mod.run_sieves(3)
print('survivors',len(survivors),'s',round(time.time()-start,1),flush=True)
ctr=Counter();examples=[]
for L,delta,fin in survivors:
 good=0
 for w in L:good|=1<<ix[w]
 bad=ALL^good
 safe=[(u,pre,suf,mask) for u,pre,suf,mask in pats if not (mask&good)]
 cover=0
 for _u,_p,_s,mask in safe:cover|=mask
 correct_presence=((cover&bad)==bad)
 original_presence=(mod.classify_presence(L)==[])
 par='parikh-determined' in mod.classify(L,7)
 ctr[('parikh',par,'orig',original_presence,'correct',correct_presence)]+=1
 if original_presence and not correct_presence and len(examples)<7:
  missed=bad&~cover
  w=words[(missed & -missed).bit_length()-1]
  examples.append({'delta':delta,'finals':sorted(fin),'missed_word':w,'original_presence':original_presence, 'correct_presence':correct_presence, 'parikh':par})
print('counter',dict((str(k),v) for k,v in ctr.items()),flush=True)
print('examples',json.dumps(examples,ensure_ascii=False),flush=True)
print('NONPARIKH_ORIGINAL_YES_CORRECT_NO',sum(v for k,v in ctr.items() if not k[1] and k[3] and not k[5]),flush=True)

===== END FILE =====

===== BEGIN FILE independent_presence_result.txt bytes=271 sha256=82137f6002dff273e1192023714343f4da49e928dd2fede67f99cee3a4cb8e6a =====
patterns 156 words 3279
survivors 197 s 184.8
counter {"('parikh', True, 'orig', True, 'correct', True)": 14, "('parikh', True, 'orig', False, 'correct', False)": 97, "('parikh', False, 'orig', True, 'correct', True)": 86}
examples []
NONPARIKH_ORIGINAL_YES_CORRECT_NO 0

===== END FILE =====

===== BEGIN FILE independent_rerun_round12_lower_bound_2026-11-15.txt bytes=18794 sha256=e82ee6dd5927c4c598eab0bea4c7b1c800336158232604af51652d3cab5e32cb =====
==============================================================================
SECTION 1: controls
    POS Sigma+: |L_{<=7}|=3279 d=1 compared-pairs=4660 violations=0
    POS Sigma+: |L_{<=7}|=3279 d=2 compared-pairs=6275 violations=0
[PASS] POS Sigma+ passes bounded (1,s_U),(2,s_U) check 
    POS {a,b}+: |L_{<=9}|=1022 d=1 compared-pairs=1021 violations=0
    POS {a,b}+: |L_{<=9}|=1022 d=2 compared-pairs=3075 violations=0
[PASS] POS {a,b}+ passes bounded (1,s_U),(2,s_U) check 
    POS (ab)+: |L_{<=16}|=8 d=1 compared-pairs=27 violations=0
    POS (ab)+: |L_{<=16}|=8 d=2 compared-pairs=349 violations=0
[PASS] POS (ab)+ passes bounded (1,s_U),(2,s_U) check 
[PASS] CE n=1: ||G||=13n+7, theta=4n, mu_1=3*2^n-2 (20,4,4)
[PASS] CE n=2: ||G||=13n+7, theta=4n, mu_1=3*2^n-2 (33,8,10)
[PASS] CE n=3: ||G||=13n+7, theta=4n, mu_1=3*2^n-2 (46,12,22)
[PASS] CE n=4: ||G||=13n+7, theta=4n, mu_1=3*2^n-2 (59,16,46)
[PASS] CE n=5: ||G||=13n+7, theta=4n, mu_1=3*2^n-2 (72,20,94)
    NEG CE n=2 (thm:doubling-no-lift family): |L_{<=30}|=6 d=1 compared-pairs=18 violations=0
    NEG CE n=2 (thm:doubling-no-lift family): |L_{<=30}|=6 d=2 compared-pairs=12 violations=1
      WITNESS d=2: x=('bb', 'abb') type=('1', '1'), y=('bba', 'bb') type=('1', '1'); shared E0=''[]'a'[]'aabb': E0[x]='bbaabbaabb', E0[y]='bbaabbaabb' in L; E=''[]'aabba'[]'': E[x]='bbaabbaabb' in L but E[y]='bbaaabbabb' NOT in L
[PASS] NEG CE n=2 (thm:doubling-no-lift family) d=2 witness independently verified 
[PASS] NEG CE n=2 (thm:doubling-no-lift family) violates (2,s_U)-substitutability (bounded, verified witness) 
[PASS] NEG CE n=2 is (1,s_U)-substitutable (manuscript prop:three-letter-family(ii)) 
==============================================================================
SECTION 2: template search (doubling with escapes)
  family T1: {'total': 405, 'bad_grammar': 0, 'not_exp': 0, 'thick': 0, 'fail_n2_d1': 241, 'fail_n2_d2': 164, 'fail_n3_d1': 0, 'fail_n3_d2': 0, 'survive': 0}  (0.8s)
   example ('fail_n2_d1', ('1',)) template= ('b', '', '', ('wrap', '', 'c'))
      x=('b',) type=('1',), y=('bba',) type=('1',); shared E0=''[]'aac': E0[x]='baac', E0[y]='bbaaac' in L; E=''[]'acac': E[x]='bacac' in L but E[y]='bbaacac' NOT in L
[PASS]   T1 example ('fail_n2_d1', ('1',)) re-verified 
   example ('fail_n2_d1', ('z',)) template= ('b', 'b', '', ('const', 'cbc', ''))
      x=('cbc',) type=('z',), y=('bbababcbc',) type=('z',); shared E0=''[]'': E0[x]='cbc', E0[y]='bbababcbc' in L; E='b'[]'bbaba': E[x]='bcbcbbaba' in L but E[y]='bbbababcbcbbaba' NOT in L
[PASS]   T1 example ('fail_n2_d1', ('z',)) re-verified 
   example ('fail_n2_d2', ('1', '1')) template= ('', 'b', 'a', ('wrap', 'cb', 'c'))
      x=('abaabab', 'a') type=('1', '1'), y=('ab', 'ababaa') type=('1', '1'); shared E0=''[]'a'[]'a': E0[x]='abaababaaa', E0[y]='abaababaaa' in L; E=''[]'aa'[]'': E[x]='abaababaaa' in L but E[y]='abaaababaa' NOT in L
[PASS]   T1 example ('fail_n2_d2', ('1', '1')) re-verified 
   example ('fail_n2_d2', ('1', 'z')) template= ('a', 'b', 'a', ('wrap', '', 'c'))
      x=('aab', 'ac') type=('1', 'z'), y=('a', 'abaabaca') type=('1', 'z'); shared E0=''[]'a'[]'': E0[x]='aabaac', E0[y]='aaabaabaca' in L; E='a'[]'aab'[]'a': E[x]='aaabaabaca' in L but E[y]='aaaababaabacaa' NOT in L
[PASS]   T1 example ('fail_n2_d2', ('1', 'z')) re-verified 
   example ('fail_n2_d2', ('z', '1')) template= ('a', 'b', 'a', ('wrap', 'c', ''))
      x=('c', 'abaa') type=('z', '1'), y=('aaabaabc', 'a') type=('z', '1'); shared E0=''[]'a'[]'': E0[x]='caabaa', E0[y]='aaabaabcaa' in L; E='a'[]'aba'[]'a': E[x]='acabaabaaa' in L but E[y]='aaaabaabcabaaa' NOT in L
[PASS]   T1 example ('fail_n2_d2', ('z', '1')) re-verified 
   example ('fail_n2_d2', ('z', 'z')) template= ('a', '', '', ('wrap', 'bc', 'cb'))
      x=('bca', 'acb') type=('z', 'z'), y=('aaaabc', 'cb') type=('z', 'z'); shared E0=''[]'a'[]'': E0[x]='bcaaacb', E0[y]='aaaabcacb' in L; E='a'[]'cbbc'[]'': E[x]='abcacbbcacb' in L but E[y]='aaaaabccbbccb' NOT in L
[PASS]   T1 example ('fail_n2_d2', ('z', 'z')) re-verified 
[PASS] T1: every template that is good/reduced/exponential/thin violates at n<=3 total=405
  family T2: {'total': 2688, 'bad_grammar': 0, 'not_exp': 0, 'thick': 0, 'fail_n2_d1': 1952, 'fail_n2_d2': 736, 'fail_n3_d1': 0, 'fail_n3_d2': 0, 'survive': 0}  (7.7s)
   example ('fail_n2_d1', ('1',)) template= ((((1, 0), (0, 0)), ((0, 1), (1, 1))), {('R', 0): 'b', ('L', 1): 'b'}, ('wrap', ('', '', '', 'c')), 'b', ('a', 'a'))
      x=('aabbb',) type=('1',), y=('aaabbbbba',) type=('1',); shared E0=''[]'aac': E0[x]='aabbbaac', E0[y]='aaabbbbbaaac' in L; E=''[]'acac': E[x]='aabbbacac' in L but E[y]='aaabbbbbaacac' NOT in L
[PASS]   T2 example ('fail_n2_d1', ('1',)) re-verified 
   example ('fail_n2_d1', ('z',)) template= ((((1, 0),), ((0, 0), (1, 1), (0, 1))), {}, ('const', ('c', 'cbc')), 'a', ('a', 'b'))
      x=('cac',) type=('z',), y=('aacabbc',) type=('z',); shared E0=''[]'bc': E0[x]='cacbc', E0[y]='aacabbcbc' in L; E=''[]'cbccbc': E[x]='caccbccbc' in L but E[y]='aacabbccbccbc' NOT in L
[PASS]   T2 example ('fail_n2_d1', ('z',)) re-verified 
   example ('fail_n2_d2', ('1', '1')) template= ((((0, 0), (1, 0)), ((1, 1), (0, 1))), {('L', 0): 'b', ('R', 1): 'a'}, ('const', ('c', 'cbc')), 'b', ('a', 'b'))
      x=('bb', 'ab') type=('1', '1'), y=('bba', 'b') type=('1', '1'); shared E0=''[]'a'[]'aabbbabbaa': E0[x]='bbaabaabbbabbaa', E0[y]='bbaabaabbbabbaa' in L; E=''[]'aaba'[]'bbabbaa': E[x]='bbaabaabbbabbaa' in L but E[y]='bbaaababbbabbaa' NOT in L
[PASS]   T2 example ('fail_n2_d2', ('1', '1')) re-verified 
   example ('fail_n2_d2', ('1', 'z')) template= ((((1, 0), (0, 0)), ((0, 1), (1, 1))), {('L', 0): 'b', ('R', 1): 'a'}, ('wrap', ('', '', '', 'c')), 'b', ('a', 'b'))
      x=('baabbb', 'c') type=('1', 'z'), y=('b', 'abbbac') type=('1', 'z'); shared E0=''[]'a'[]'': E0[x]='baabbbac', E0[y]='baabbbac' in L; E='ba'[]'ab'[]'a': E[x]='babaabbbabca' in L but E[y]='babababbbaca' NOT in L
[PASS]   T2 example ('fail_n2_d2', ('1', 'z')) re-verified 
   example ('fail_n2_d2', ('z', '1')) template= ((((1, 0), (0, 0)), ((0, 1), (1, 1))), {('R', 0): 'b', ('L', 1): 'b'}, ('wrap', ('', 'c', '', 'c')), 'b', ('a', 'a'))
      x=('acaabbbbb', 'a') type=('z', '1'), y=('ac', 'abbbbbaa') type=('z', '1'); shared E0=''[]'a'[]'ac': E0[x]='acaabbbbbaaac', E0[y]='acaabbbbbaaac' in L; E=''[]'aa'[]'c': E[x]='acaabbbbbaaac' in L but E[y]='acaaabbbbbaac' NOT in L
[PASS]   T2 example ('fail_n2_d2', ('z', '1')) re-verified 
[PASS] T2: every template that is good/reduced/exponential/thin violates at n<=3 total=2688
==============================================================================
SECTION 3: designed candidates
  A1_aligned (n, ||G||, theta-bar, mu_1): [(1, 13, 2, 2), (2, 27, 5, 4), (3, 43, 9, 8), (4, 59, 14, 16), (5, 75, 19, 32), (6, 91, 25, 64), (7, 107, 32, 128)]
[PASS] A1_aligned: mu_1 >= 2^n and theta-bar <= 4(n+1)^2 for n<=7 (poly size/thickness, exponential rare type) 
[PASS] A1 n=2 grammar language = aligned depth-labelled membership (len<=12) 
    A1_aligned n=2: |L_{<=14}|=4 d=1 compared-pairs=6 violations=0
    A1_aligned n=2: |L_{<=14}|=4 d=2 compared-pairs=5 violations=0
[PASS] A1_aligned n=2 passes bounded (1,s_U),(2,s_U) check 
[PASS] A1 n=3 grammar language = aligned depth-labelled membership (len<=12) 
    A1_aligned n=3: |L_{<=16}|=25 d=1 compared-pairs=38 violations=1
      WITNESS d=1: x=('aaaacbbc',) type=('z',), y=('cbcaa',) type=('z',); shared E0=''[]'aa': E0[x]='aaaacbbcaa', E0[y]='cbcaaaa' in L; E='aa'[]'': E[x]='aaaaaacbbc' in L but E[y]='aacbcaa' NOT in L
[PASS] A1_aligned n=3 d=1 witness independently verified 
    A1_aligned n=3: |L_{<=16}|=25 d=2 compared-pairs=57 violations=1
      WITNESS d=2: x=('aa', 'aaaa') type=('1', '1'), y=('a', 'aaaaa') type=('1', '1'); shared E0=''[]'a'[]'a': E0[x]='aaaaaaaa', E0[y]='aaaaaaaa' in L; E=''[]'cbbc'[]'': E[x]='aacbbcaaaa' in L but E[y]='acbbcaaaaa' NOT in L
[PASS] A1_aligned n=3 d=2 witness independently verified 
[PASS] A1_aligned n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
  A3_TM_cc (n, ||G||, theta-bar, mu_1): [(1, 21, 3, 2), (2, 43, 5, 4), (3, 65, 8, 8), (4, 87, 14, 16), (5, 109, 20, 32), (6, 131, 26, 64), (7, 153, 32, 128)]
[PASS] A3_TM_cc: mu_1 >= 2^n and theta-bar <= 4(n+1)^2 for n<=7 (poly size/thickness, exponential rare type) 
    A3_TM_cc n=2: |L_{<=14}|=6 d=1 compared-pairs=5 violations=1
      WITNESS d=1: x=('abc',) type=('z',), y=('ca',) type=('z',); shared E0=''[]'bc': E0[x]='abcbc', E0[y]='cabc' in L; E='c'[]'': E[x]='cabc' in L but E[y]='cca' NOT in L
[PASS] A3_TM_cc n=2 d=1 witness independently verified 
    A3_TM_cc n=2: |L_{<=14}|=6 d=2 compared-pairs=1 violations=1
      WITNESS d=2: x=('c', 'bc') type=('z', 'z'), y=('c', 'cba') type=('z', 'z'); shared E0=''[]'a'[]'': E0[x]='cabc', E0[y]='cacba' in L; E=''[]'acc'[]'': E[x]='caccbc' in L but E[y]='cacccba' NOT in L
[PASS] A3_TM_cc n=2 d=2 witness independently verified 
[PASS] A3_TM_cc n=2 violates (2,s_U)-substitutability (bounded, verified witness) 
    A3_TM_cc n=3: |L_{<=16}|=42 d=1 compared-pairs=41 violations=1
      WITNESS d=1: x=('cabcb',) type=('z',), y=('abcbcb',) type=('z',); shared E0=''[]'aab': E0[x]='cabcbaab', E0[y]='abcbcbaab' in L; E=''[]'cc': E[x]='cabcbcc' in L but E[y]='abcbcbcc' NOT in L
[PASS] A3_TM_cc n=3 d=1 witness independently verified 
    A3_TM_cc n=3: |L_{<=16}|=42 d=2 compared-pairs=24 violations=1
      WITNESS d=2: x=('abbacb', 'c') type=('z', 'z'), y=('abbabac', 'c') type=('z', 'z'); shared E0=''[]'a'[]'': E0[x]='abbacbac', E0[y]='abbabacac' in L; E=''[]'c'[]'ac': E[x]='abbacbccac' in L but E[y]='abbabacccac' NOT in L
[PASS] A3_TM_cc n=3 d=2 witness independently verified 
[PASS] A3_TM_cc n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
  A3_TM_cb (n, ||G||, theta-bar, mu_1): [(1, 21, 3, 2), (2, 45, 7, 4), (3, 69, 10, 8), (4, 93, 14, 16), (5, 117, 22, 32), (6, 141, 30, 64), (7, 165, 38, 128)]
[PASS] A3_TM_cb: mu_1 >= 2^n and theta-bar <= 4(n+1)^2 for n<=7 (poly size/thickness, exponential rare type) 
    A3_TM_cb n=2: |L_{<=14}|=6 d=1 compared-pairs=7 violations=1
      WITNESS d=1: x=('ca',) type=('z',), y=('abcbb',) type=('z',); shared E0=''[]'bc': E0[x]='cabc', E0[y]='abcbbbc' in L; E=''[]'cba': E[x]='cacba' in L but E[y]='abcbbcba' NOT in L
[PASS] A3_TM_cb n=2 d=1 witness independently verified 
    A3_TM_cb n=2: |L_{<=14}|=6 d=2 compared-pairs=1 violations=1
      WITNESS d=2: x=('c', 'bc') type=('z', 'z'), y=('c', 'cba') type=('z', 'z'); shared E0=''[]'a'[]'': E0[x]='cabc', E0[y]='cacba' in L; E=''[]'accbb'[]'': E[x]='caccbbbc' in L but E[y]='caccbbcba' NOT in L
[PASS] A3_TM_cb n=2 d=2 witness independently verified 
[PASS] A3_TM_cb n=2 violates (2,s_U)-substitutability (bounded, verified witness) 
    A3_TM_cb n=3: |L_{<=16}|=41 d=1 compared-pairs=40 violations=1
      WITNESS d=1: x=('cabcb',) type=('z',), y=('abcbbbcb',) type=('z',); shared E0=''[]'aab': E0[x]='cabcbaab', E0[y]='abcbbbcbaab' in L; E=''[]'bbcc': E[x]='cabcbbbcc' in L but E[y]='abcbbbcbbbcc' NOT in L
[PASS] A3_TM_cb n=3 d=1 witness independently verified 
    A3_TM_cb n=3: |L_{<=16}|=41 d=2 compared-pairs=31 violations=1
      WITNESS d=2: x=('c', 'bcbaab') type=('z', 'z'), y=('abbabac', 'c') type=('z', 'z'); shared E0=''[]'a'[]'': E0[x]='cabcbaab', E0[y]='abbabacac' in L; E=''[]'accbb'[]'': E[x]='caccbbbcbaab' in L but E[y]='abbabacaccbbc' NOT in L
[PASS] A3_TM_cb n=3 d=2 witness independently verified 
[PASS] A3_TM_cb n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
  A4_two_track (n, ||G||, theta-bar, mu_1): [(1, 26, 7, 7), (2, 42, 11, 15), (3, 58, 15, 31), (4, 74, 19, 63), (5, 90, 23, 127), (6, 106, 27, 255), (7, 122, 31, 511)]
[PASS] A4_two_track: mu_1 >= 2^n and theta-bar <= 4(n+1)^2 for n<=7 (poly size/thickness, exponential rare type) 
    A4_two_track n=2: |L_{<=14}|=5 d=1 compared-pairs=20 violations=1
      WITNESS d=1: x=('abcaaacba',) type=('z',), y=('caaac',) type=('z',); shared E0='c'[]'c': E0[x]='cabcaaacbac', E0[y]='ccaaacc' in L; E='ab'[]'ba': E[x]='ababcaaacbaba' in L but E[y]='abcaaacba' NOT in L
[PASS] A4_two_track n=2 d=1 witness independently verified 
    A4_two_track n=2: |L_{<=14}|=5 d=2 compared-pairs=25 violations=1
      WITNESS d=2: x=('c', 'bab') type=('z', '1'), y=('cab', 'b') type=('z', '1'); shared E0=''[]'a'[]'aaababac': E0[x]='cababaaababac', E0[y]='cababaaababac' in L; E=''[]'ababaaa'[]'ac': E[x]='cababaaababac' in L but E[y]='cabababaaabac' NOT in L
[PASS] A4_two_track n=2 d=2 witness independently verified 
[PASS] A4_two_track n=2 violates (2,s_U)-substitutability (bounded, verified witness) 
    A4_two_track n=3: |L_{<=16}|=6 d=1 compared-pairs=61 violations=1
      WITNESS d=1: x=('abcaaacba',) type=('z',), y=('caaac',) type=('z',); shared E0='cc'[]'cc': E0[x]='ccabcaaacbacc', E0[y]='cccaaaccc' in L; E='cab'[]'bac': E[x]='cababcaaacbabac' in L but E[y]='cabcaaacbac' NOT in L
[PASS] A4_two_track n=3 d=1 witness independently verified 
    A4_two_track n=3: |L_{<=16}|=6 d=2 compared-pairs=32 violations=1
      WITNESS d=2: x=('cc', 'bab') type=('z', '1'), y=('ccab', 'b') type=('z', '1'); shared E0=''[]'a'[]'aaababacc': E0[x]='ccababaaababacc', E0[y]='ccababaaababacc' in L; E=''[]'ababaaa'[]'acc': E[x]='ccababaaababacc' in L but E[y]='ccabababaaabacc' NOT in L
[PASS] A4_two_track n=3 d=2 witness independently verified 
[PASS] A4_two_track n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
  membership-defined weight languages (block c b^d c has weight 2^(n-d))
    W-sum n=2: |L_{<=12}|=24 d=1 compared-pairs=46 violations=1
      WITNESS d=1: x=('aac',) type=('z',), y=('aaacb',) type=('z',); shared E0=''[]'bc': E0[x]='aacbc', E0[y]='aaacbbc' in L; E=''[]'bbca': E[x]='aacbbca' in L but E[y]='aaacbbbca' NOT in L
[PASS] W-sum n=2 d=1 witness independently verified 
    W-sum n=2: |L_{<=12}|=24 d=2 compared-pairs=16 violations=1
      WITNESS d=2: x=('aa', 'c') type=('1', 'z'), y=('a', 'ac') type=('1', 'z'); shared E0=''[]'a'[]'bbc': E0[x]='aaacbbc', E0[y]='aaacbbc' in L; E=''[]'acbb'[]'': E[x]='aaacbbc' in L but E[y]='aacbbac' NOT in L
[PASS] W-sum n=2 d=2 witness independently verified 
[PASS] W-sum n=2 violates (2,s_U)-substitutability (bounded, verified witness) 
    W-sum n=3: |L_{<=12}|=72 d=1 compared-pairs=208 violations=1
      WITNESS d=1: x=('aaaaaacb',) type=('z',), y=('aaaaac',) type=('z',); shared E0=''[]'bbca': E0[x]='aaaaaacbbbca', E0[y]='aaaaacbbca' in L; E=''[]'bc': E[x]='aaaaaacbbc' in L but E[y]='aaaaacbc' NOT in L
[PASS] W-sum n=3 d=1 witness independently verified 
    W-sum n=3: |L_{<=12}|=72 d=2 compared-pairs=342 violations=1
      WITNESS d=2: x=('aaaaaa', 'c') type=('1', 'z'), y=('a', 'aaaaac') type=('1', 'z'); shared E0=''[]'a'[]'bbbc': E0[x]='aaaaaaacbbbc', E0[y]='aaaaaaacbbbc' in L; E=''[]'acbbb'[]'': E[x]='aaaaaaacbbbc' in L but E[y]='aacbbbaaaaac' NOT in L
[PASS] W-sum n=3 d=2 witness independently verified 
[PASS] W-sum n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
    W-aligned n=2: |L_{<=12}|=20 d=1 compared-pairs=24 violations=1
      WITNESS d=1: x=('aacbbc',) type=('z',), y=('cbca',) type=('z',); shared E0=''[]'a': E0[x]='aacbbca', E0[y]='cbcaa' in L; E='a'[]'': E[x]='aaacbbc' in L but E[y]='acbca' NOT in L
[PASS] W-aligned n=2 d=1 witness independently verified 
    W-aligned n=2: |L_{<=12}|=20 d=2 compared-pairs=16 violations=1
      WITNESS d=2: x=('aa', 'c') type=('1', 'z'), y=('a', 'ac') type=('1', 'z'); shared E0=''[]'a'[]'bbc': E0[x]='aaacbbc', E0[y]='aaacbbc' in L; E=''[]'acbb'[]'': E[x]='aaacbbc' in L but E[y]='aacbbac' NOT in L
[PASS] W-aligned n=2 d=2 witness independently verified 
[PASS] W-aligned n=2 violates (2,s_U)-substitutability (bounded, verified witness) 
    W-aligned n=3: |L_{<=12}|=36 d=1 compared-pairs=37 violations=1
      WITNESS d=1: x=('aaaaaacbbbc',) type=('z',), y=('aaaacbbca',) type=('z',); shared E0=''[]'a': E0[x]='aaaaaacbbbca', E0[y]='aaaacbbcaa' in L; E='a'[]'': E[x]='aaaaaaacbbbc' in L but E[y]='aaaaacbbca' NOT in L
[PASS] W-aligned n=3 d=1 witness independently verified 
    W-aligned n=3: |L_{<=12}|=36 d=2 compared-pairs=111 violations=1
      WITNESS d=2: x=('aa', 'aaaa') type=('1', '1'), y=('a', 'aaaaa') type=('1', '1'); shared E0=''[]'a'[]'a': E0[x]='aaaaaaaa', E0[y]='aaaaaaaa' in L; E=''[]'cbbc'[]'': E[x]='aacbbcaaaa' in L but E[y]='acbbcaaaaa' NOT in L
[PASS] W-aligned n=3 d=2 witness independently verified 
[PASS] W-aligned n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
==============================================================================
SECTION 4: Route B regular sieves (complete DFAs, <=3 states)
states<=2: distinct languages (length<=6 signature): 106
    states<=2: distinct languages (length<=6 signature): 106
    pass at N=6: 22
    pass bounded d=1,2 at N=5: 22 ; at N=7: 22
    states<=3: distinct languages (length<=6 signature): 40812
    pass at N=6: 197
    pass bounded d=1,2 at N=5: 197 ; at N=7: 197
    3-state survivors cross-tab (Parikh-determined?, presence-witnessed?): {(True, True): 14, (True, False): 97, (False, True): 86}
[PASS] sieves: 22 survivors (<=2 states), 197 survivors (<=3 states) 
[PASS] sieves: every survivor is Parikh-determined or presence-witnessed (bounded, N=7) 
==============================================================================
SECTION 5: Corollary R2 sanity (fan-out 1)
[PASS] CE n=2 untyped 1-substitutable (bounded) 
      untyped witness: x=('bcac',) type=('z',), y=('bbaab',) type=('1',); shared E0=''[]'cacb': E0[x]='bcaccacb', E0[y]='bbaabcacb' in L; E=''[]'baabb': E[x]='bcacbaabb' in L but E[y]='bbaabbaabb' NOT in L
[PASS] CE n=2 minus W_n is NOT untyped 1-substitutable (as Cor. R2 forces) 
[PASS] CE n=3 untyped 1-substitutable (bounded) 
      untyped witness: x=('bbcacb',) type=('z',), y=('bbbaabb',) type=('1',); shared E0=''[]'aabbbbaabcacbb': E0[x]='bbcacbaabbbbaabcacbb', E0[y]='bbbaabbaabbbbaabcacbb' in L; E=''[]'aabbbbaabbaabbb': E[x]='bbcacbaabbbbaabbaabbb' in L but E[y]='bbbaabbaabbbbaabbaabbb' NOT in L
[PASS] CE n=3 minus W_n is NOT untyped 1-substitutable (as Cor. R2 forces) 
==============================================================================
SECTION 6: Corollary U on A1 data, Prop LS randomized sanity
    A1 n=3 single-core words: totals of a by label d: [(1, [4]), (2, [6])]
    Lemma C/Cor. U prediction: some a^g cbbbc a^h with g+h=8 must lie in L; present in A1? False
[PASS] A1 n=3: Lemma C hypotheses hold and the forced word a^g c b^3 c a^h (g+h=8) is absent => A1 not in C_{2,s_U} 
[PASS] Prop LS randomized sanity: shortest pattern-containing word <= k(k+1)f|V|(r+1)theta in all non-vacuous trials grammars=93 nonvacuous=72
==============================================================================
SUMMARY: 72 tests, 72 PASS, 0 FAIL, elapsed 241.5s

===== END FILE =====

===== BEGIN FILE out_check_round12_lower_bound_2026-11-15.txt bytes=18794 sha256=08dcf90851d4cdfdb6f0e03318baa22af20650af566081532bdd8a17b056b0af =====
==============================================================================
SECTION 1: controls
    POS Sigma+: |L_{<=7}|=3279 d=1 compared-pairs=4660 violations=0
    POS Sigma+: |L_{<=7}|=3279 d=2 compared-pairs=6275 violations=0
[PASS] POS Sigma+ passes bounded (1,s_U),(2,s_U) check 
    POS {a,b}+: |L_{<=9}|=1022 d=1 compared-pairs=1021 violations=0
    POS {a,b}+: |L_{<=9}|=1022 d=2 compared-pairs=3075 violations=0
[PASS] POS {a,b}+ passes bounded (1,s_U),(2,s_U) check 
    POS (ab)+: |L_{<=16}|=8 d=1 compared-pairs=27 violations=0
    POS (ab)+: |L_{<=16}|=8 d=2 compared-pairs=349 violations=0
[PASS] POS (ab)+ passes bounded (1,s_U),(2,s_U) check 
[PASS] CE n=1: ||G||=13n+7, theta=4n, mu_1=3*2^n-2 (20,4,4)
[PASS] CE n=2: ||G||=13n+7, theta=4n, mu_1=3*2^n-2 (33,8,10)
[PASS] CE n=3: ||G||=13n+7, theta=4n, mu_1=3*2^n-2 (46,12,22)
[PASS] CE n=4: ||G||=13n+7, theta=4n, mu_1=3*2^n-2 (59,16,46)
[PASS] CE n=5: ||G||=13n+7, theta=4n, mu_1=3*2^n-2 (72,20,94)
    NEG CE n=2 (thm:doubling-no-lift family): |L_{<=30}|=6 d=1 compared-pairs=18 violations=0
    NEG CE n=2 (thm:doubling-no-lift family): |L_{<=30}|=6 d=2 compared-pairs=12 violations=1
      WITNESS d=2: x=('bb', 'abb') type=('1', '1'), y=('bba', 'bb') type=('1', '1'); shared E0=''[]'a'[]'aabb': E0[x]='bbaabbaabb', E0[y]='bbaabbaabb' in L; E=''[]'aabba'[]'': E[x]='bbaabbaabb' in L but E[y]='bbaaabbabb' NOT in L
[PASS] NEG CE n=2 (thm:doubling-no-lift family) d=2 witness independently verified 
[PASS] NEG CE n=2 (thm:doubling-no-lift family) violates (2,s_U)-substitutability (bounded, verified witness) 
[PASS] NEG CE n=2 is (1,s_U)-substitutable (manuscript prop:three-letter-family(ii)) 
==============================================================================
SECTION 2: template search (doubling with escapes)
  family T1: {'total': 405, 'bad_grammar': 0, 'not_exp': 0, 'thick': 0, 'fail_n2_d1': 241, 'fail_n2_d2': 164, 'fail_n3_d1': 0, 'fail_n3_d2': 0, 'survive': 0}  (0.9s)
   example ('fail_n2_d1', ('1',)) template= ('b', '', '', ('wrap', '', 'c'))
      x=('b',) type=('1',), y=('bba',) type=('1',); shared E0=''[]'aac': E0[x]='baac', E0[y]='bbaaac' in L; E=''[]'acac': E[x]='bacac' in L but E[y]='bbaacac' NOT in L
[PASS]   T1 example ('fail_n2_d1', ('1',)) re-verified 
   example ('fail_n2_d1', ('z',)) template= ('b', 'b', '', ('const', 'cbc', ''))
      x=('cbc',) type=('z',), y=('bbababcbc',) type=('z',); shared E0=''[]'': E0[x]='cbc', E0[y]='bbababcbc' in L; E='b'[]'bbaba': E[x]='bcbcbbaba' in L but E[y]='bbbababcbcbbaba' NOT in L
[PASS]   T1 example ('fail_n2_d1', ('z',)) re-verified 
   example ('fail_n2_d2', ('1', '1')) template= ('', 'b', 'a', ('wrap', 'cb', 'c'))
      x=('abaabab', 'a') type=('1', '1'), y=('ab', 'ababaa') type=('1', '1'); shared E0=''[]'a'[]'a': E0[x]='abaababaaa', E0[y]='abaababaaa' in L; E=''[]'aa'[]'': E[x]='abaababaaa' in L but E[y]='abaaababaa' NOT in L
[PASS]   T1 example ('fail_n2_d2', ('1', '1')) re-verified 
   example ('fail_n2_d2', ('1', 'z')) template= ('a', 'b', 'a', ('wrap', '', 'c'))
      x=('aab', 'ac') type=('1', 'z'), y=('a', 'abaabaca') type=('1', 'z'); shared E0=''[]'a'[]'': E0[x]='aabaac', E0[y]='aaabaabaca' in L; E='a'[]'aab'[]'a': E[x]='aaabaabaca' in L but E[y]='aaaababaabacaa' NOT in L
[PASS]   T1 example ('fail_n2_d2', ('1', 'z')) re-verified 
   example ('fail_n2_d2', ('z', '1')) template= ('a', 'b', 'a', ('wrap', 'c', ''))
      x=('c', 'abaa') type=('z', '1'), y=('aaabaabc', 'a') type=('z', '1'); shared E0=''[]'a'[]'': E0[x]='caabaa', E0[y]='aaabaabcaa' in L; E='a'[]'aba'[]'a': E[x]='acabaabaaa' in L but E[y]='aaaabaabcabaaa' NOT in L
[PASS]   T1 example ('fail_n2_d2', ('z', '1')) re-verified 
   example ('fail_n2_d2', ('z', 'z')) template= ('a', '', '', ('wrap', 'bc', 'cb'))
      x=('bca', 'acb') type=('z', 'z'), y=('aaaabc', 'cb') type=('z', 'z'); shared E0=''[]'a'[]'': E0[x]='bcaaacb', E0[y]='aaaabcacb' in L; E='a'[]'cbbc'[]'': E[x]='abcacbbcacb' in L but E[y]='aaaaabccbbccb' NOT in L
[PASS]   T1 example ('fail_n2_d2', ('z', 'z')) re-verified 
[PASS] T1: every template that is good/reduced/exponential/thin violates at n<=3 total=405
  family T2: {'total': 2688, 'bad_grammar': 0, 'not_exp': 0, 'thick': 0, 'fail_n2_d1': 1952, 'fail_n2_d2': 736, 'fail_n3_d1': 0, 'fail_n3_d2': 0, 'survive': 0}  (8.7s)
   example ('fail_n2_d1', ('1',)) template= ((((1, 0), (0, 0)), ((0, 1), (1, 1))), {('R', 0): 'b', ('L', 1): 'b'}, ('wrap', ('', '', '', 'c')), 'b', ('a', 'a'))
      x=('aabbb',) type=('1',), y=('aaabbbbba',) type=('1',); shared E0=''[]'aac': E0[x]='aabbbaac', E0[y]='aaabbbbbaaac' in L; E=''[]'acac': E[x]='aabbbacac' in L but E[y]='aaabbbbbaacac' NOT in L
[PASS]   T2 example ('fail_n2_d1', ('1',)) re-verified 
   example ('fail_n2_d1', ('z',)) template= ((((1, 0),), ((0, 0), (1, 1), (0, 1))), {}, ('const', ('c', 'cbc')), 'a', ('a', 'b'))
      x=('cac',) type=('z',), y=('aacabbc',) type=('z',); shared E0=''[]'bc': E0[x]='cacbc', E0[y]='aacabbcbc' in L; E=''[]'cbccbc': E[x]='caccbccbc' in L but E[y]='aacabbccbccbc' NOT in L
[PASS]   T2 example ('fail_n2_d1', ('z',)) re-verified 
   example ('fail_n2_d2', ('1', '1')) template= ((((0, 0), (1, 0)), ((1, 1), (0, 1))), {('L', 0): 'b', ('R', 1): 'a'}, ('const', ('c', 'cbc')), 'b', ('a', 'b'))
      x=('bb', 'ab') type=('1', '1'), y=('bba', 'b') type=('1', '1'); shared E0=''[]'a'[]'aabbbabbaa': E0[x]='bbaabaabbbabbaa', E0[y]='bbaabaabbbabbaa' in L; E=''[]'aaba'[]'bbabbaa': E[x]='bbaabaabbbabbaa' in L but E[y]='bbaaababbbabbaa' NOT in L
[PASS]   T2 example ('fail_n2_d2', ('1', '1')) re-verified 
   example ('fail_n2_d2', ('1', 'z')) template= ((((1, 0), (0, 0)), ((0, 1), (1, 1))), {('L', 0): 'b', ('R', 1): 'a'}, ('wrap', ('', '', '', 'c')), 'b', ('a', 'b'))
      x=('baabbb', 'c') type=('1', 'z'), y=('b', 'abbbac') type=('1', 'z'); shared E0=''[]'a'[]'': E0[x]='baabbbac', E0[y]='baabbbac' in L; E='ba'[]'ab'[]'a': E[x]='babaabbbabca' in L but E[y]='babababbbaca' NOT in L
[PASS]   T2 example ('fail_n2_d2', ('1', 'z')) re-verified 
   example ('fail_n2_d2', ('z', '1')) template= ((((1, 0), (0, 0)), ((0, 1), (1, 1))), {('R', 0): 'b', ('L', 1): 'b'}, ('wrap', ('', 'c', '', 'c')), 'b', ('a', 'a'))
      x=('acaabbbbb', 'a') type=('z', '1'), y=('ac', 'abbbbbaa') type=('z', '1'); shared E0=''[]'a'[]'ac': E0[x]='acaabbbbbaaac', E0[y]='acaabbbbbaaac' in L; E=''[]'aa'[]'c': E[x]='acaabbbbbaaac' in L but E[y]='acaaabbbbbaac' NOT in L
[PASS]   T2 example ('fail_n2_d2', ('z', '1')) re-verified 
[PASS] T2: every template that is good/reduced/exponential/thin violates at n<=3 total=2688
==============================================================================
SECTION 3: designed candidates
  A1_aligned (n, ||G||, theta-bar, mu_1): [(1, 13, 2, 2), (2, 27, 5, 4), (3, 43, 9, 8), (4, 59, 14, 16), (5, 75, 19, 32), (6, 91, 25, 64), (7, 107, 32, 128)]
[PASS] A1_aligned: mu_1 >= 2^n and theta-bar <= 4(n+1)^2 for n<=7 (poly size/thickness, exponential rare type) 
[PASS] A1 n=2 grammar language = aligned depth-labelled membership (len<=12) 
    A1_aligned n=2: |L_{<=14}|=4 d=1 compared-pairs=6 violations=0
    A1_aligned n=2: |L_{<=14}|=4 d=2 compared-pairs=5 violations=0
[PASS] A1_aligned n=2 passes bounded (1,s_U),(2,s_U) check 
[PASS] A1 n=3 grammar language = aligned depth-labelled membership (len<=12) 
    A1_aligned n=3: |L_{<=16}|=25 d=1 compared-pairs=38 violations=1
      WITNESS d=1: x=('aaaacbbc',) type=('z',), y=('cbcaa',) type=('z',); shared E0=''[]'aa': E0[x]='aaaacbbcaa', E0[y]='cbcaaaa' in L; E='aa'[]'': E[x]='aaaaaacbbc' in L but E[y]='aacbcaa' NOT in L
[PASS] A1_aligned n=3 d=1 witness independently verified 
    A1_aligned n=3: |L_{<=16}|=25 d=2 compared-pairs=57 violations=1
      WITNESS d=2: x=('aa', 'aaaa') type=('1', '1'), y=('a', 'aaaaa') type=('1', '1'); shared E0=''[]'a'[]'a': E0[x]='aaaaaaaa', E0[y]='aaaaaaaa' in L; E=''[]'cbbc'[]'': E[x]='aacbbcaaaa' in L but E[y]='acbbcaaaaa' NOT in L
[PASS] A1_aligned n=3 d=2 witness independently verified 
[PASS] A1_aligned n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
  A3_TM_cc (n, ||G||, theta-bar, mu_1): [(1, 21, 3, 2), (2, 43, 5, 4), (3, 65, 8, 8), (4, 87, 14, 16), (5, 109, 20, 32), (6, 131, 26, 64), (7, 153, 32, 128)]
[PASS] A3_TM_cc: mu_1 >= 2^n and theta-bar <= 4(n+1)^2 for n<=7 (poly size/thickness, exponential rare type) 
    A3_TM_cc n=2: |L_{<=14}|=6 d=1 compared-pairs=5 violations=1
      WITNESS d=1: x=('abc',) type=('z',), y=('ca',) type=('z',); shared E0=''[]'bc': E0[x]='abcbc', E0[y]='cabc' in L; E='c'[]'': E[x]='cabc' in L but E[y]='cca' NOT in L
[PASS] A3_TM_cc n=2 d=1 witness independently verified 
    A3_TM_cc n=2: |L_{<=14}|=6 d=2 compared-pairs=1 violations=1
      WITNESS d=2: x=('c', 'bc') type=('z', 'z'), y=('c', 'cba') type=('z', 'z'); shared E0=''[]'a'[]'': E0[x]='cabc', E0[y]='cacba' in L; E=''[]'acc'[]'': E[x]='caccbc' in L but E[y]='cacccba' NOT in L
[PASS] A3_TM_cc n=2 d=2 witness independently verified 
[PASS] A3_TM_cc n=2 violates (2,s_U)-substitutability (bounded, verified witness) 
    A3_TM_cc n=3: |L_{<=16}|=42 d=1 compared-pairs=41 violations=1
      WITNESS d=1: x=('cabcb',) type=('z',), y=('abcbcb',) type=('z',); shared E0=''[]'aab': E0[x]='cabcbaab', E0[y]='abcbcbaab' in L; E=''[]'cc': E[x]='cabcbcc' in L but E[y]='abcbcbcc' NOT in L
[PASS] A3_TM_cc n=3 d=1 witness independently verified 
    A3_TM_cc n=3: |L_{<=16}|=42 d=2 compared-pairs=24 violations=1
      WITNESS d=2: x=('abbacb', 'c') type=('z', 'z'), y=('abbabac', 'c') type=('z', 'z'); shared E0=''[]'a'[]'': E0[x]='abbacbac', E0[y]='abbabacac' in L; E=''[]'c'[]'ac': E[x]='abbacbccac' in L but E[y]='abbabacccac' NOT in L
[PASS] A3_TM_cc n=3 d=2 witness independently verified 
[PASS] A3_TM_cc n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
  A3_TM_cb (n, ||G||, theta-bar, mu_1): [(1, 21, 3, 2), (2, 45, 7, 4), (3, 69, 10, 8), (4, 93, 14, 16), (5, 117, 22, 32), (6, 141, 30, 64), (7, 165, 38, 128)]
[PASS] A3_TM_cb: mu_1 >= 2^n and theta-bar <= 4(n+1)^2 for n<=7 (poly size/thickness, exponential rare type) 
    A3_TM_cb n=2: |L_{<=14}|=6 d=1 compared-pairs=7 violations=1
      WITNESS d=1: x=('ca',) type=('z',), y=('abcbb',) type=('z',); shared E0=''[]'bc': E0[x]='cabc', E0[y]='abcbbbc' in L; E=''[]'cba': E[x]='cacba' in L but E[y]='abcbbcba' NOT in L
[PASS] A3_TM_cb n=2 d=1 witness independently verified 
    A3_TM_cb n=2: |L_{<=14}|=6 d=2 compared-pairs=1 violations=1
      WITNESS d=2: x=('c', 'bc') type=('z', 'z'), y=('c', 'cba') type=('z', 'z'); shared E0=''[]'a'[]'': E0[x]='cabc', E0[y]='cacba' in L; E=''[]'accbb'[]'': E[x]='caccbbbc' in L but E[y]='caccbbcba' NOT in L
[PASS] A3_TM_cb n=2 d=2 witness independently verified 
[PASS] A3_TM_cb n=2 violates (2,s_U)-substitutability (bounded, verified witness) 
    A3_TM_cb n=3: |L_{<=16}|=41 d=1 compared-pairs=40 violations=1
      WITNESS d=1: x=('cabcb',) type=('z',), y=('abcbbbcb',) type=('z',); shared E0=''[]'aab': E0[x]='cabcbaab', E0[y]='abcbbbcbaab' in L; E=''[]'bbcc': E[x]='cabcbbbcc' in L but E[y]='abcbbbcbbbcc' NOT in L
[PASS] A3_TM_cb n=3 d=1 witness independently verified 
    A3_TM_cb n=3: |L_{<=16}|=41 d=2 compared-pairs=31 violations=1
      WITNESS d=2: x=('c', 'bcbaab') type=('z', 'z'), y=('abbabac', 'c') type=('z', 'z'); shared E0=''[]'a'[]'': E0[x]='cabcbaab', E0[y]='abbabacac' in L; E=''[]'accbb'[]'': E[x]='caccbbbcbaab' in L but E[y]='abbabacaccbbc' NOT in L
[PASS] A3_TM_cb n=3 d=2 witness independently verified 
[PASS] A3_TM_cb n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
  A4_two_track (n, ||G||, theta-bar, mu_1): [(1, 26, 7, 7), (2, 42, 11, 15), (3, 58, 15, 31), (4, 74, 19, 63), (5, 90, 23, 127), (6, 106, 27, 255), (7, 122, 31, 511)]
[PASS] A4_two_track: mu_1 >= 2^n and theta-bar <= 4(n+1)^2 for n<=7 (poly size/thickness, exponential rare type) 
    A4_two_track n=2: |L_{<=14}|=5 d=1 compared-pairs=20 violations=1
      WITNESS d=1: x=('abcaaacba',) type=('z',), y=('caaac',) type=('z',); shared E0='c'[]'c': E0[x]='cabcaaacbac', E0[y]='ccaaacc' in L; E='ab'[]'ba': E[x]='ababcaaacbaba' in L but E[y]='abcaaacba' NOT in L
[PASS] A4_two_track n=2 d=1 witness independently verified 
    A4_two_track n=2: |L_{<=14}|=5 d=2 compared-pairs=25 violations=1
      WITNESS d=2: x=('c', 'bab') type=('z', '1'), y=('cab', 'b') type=('z', '1'); shared E0=''[]'a'[]'aaababac': E0[x]='cababaaababac', E0[y]='cababaaababac' in L; E=''[]'ababaaa'[]'ac': E[x]='cababaaababac' in L but E[y]='cabababaaabac' NOT in L
[PASS] A4_two_track n=2 d=2 witness independently verified 
[PASS] A4_two_track n=2 violates (2,s_U)-substitutability (bounded, verified witness) 
    A4_two_track n=3: |L_{<=16}|=6 d=1 compared-pairs=61 violations=1
      WITNESS d=1: x=('abcaaacba',) type=('z',), y=('caaac',) type=('z',); shared E0='cc'[]'cc': E0[x]='ccabcaaacbacc', E0[y]='cccaaaccc' in L; E='cab'[]'bac': E[x]='cababcaaacbabac' in L but E[y]='cabcaaacbac' NOT in L
[PASS] A4_two_track n=3 d=1 witness independently verified 
    A4_two_track n=3: |L_{<=16}|=6 d=2 compared-pairs=32 violations=1
      WITNESS d=2: x=('cc', 'bab') type=('z', '1'), y=('ccab', 'b') type=('z', '1'); shared E0=''[]'a'[]'aaababacc': E0[x]='ccababaaababacc', E0[y]='ccababaaababacc' in L; E=''[]'ababaaa'[]'acc': E[x]='ccababaaababacc' in L but E[y]='ccabababaaabacc' NOT in L
[PASS] A4_two_track n=3 d=2 witness independently verified 
[PASS] A4_two_track n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
  membership-defined weight languages (block c b^d c has weight 2^(n-d))
    W-sum n=2: |L_{<=12}|=24 d=1 compared-pairs=46 violations=1
      WITNESS d=1: x=('aac',) type=('z',), y=('aaacb',) type=('z',); shared E0=''[]'bc': E0[x]='aacbc', E0[y]='aaacbbc' in L; E=''[]'bbca': E[x]='aacbbca' in L but E[y]='aaacbbbca' NOT in L
[PASS] W-sum n=2 d=1 witness independently verified 
    W-sum n=2: |L_{<=12}|=24 d=2 compared-pairs=16 violations=1
      WITNESS d=2: x=('aa', 'c') type=('1', 'z'), y=('a', 'ac') type=('1', 'z'); shared E0=''[]'a'[]'bbc': E0[x]='aaacbbc', E0[y]='aaacbbc' in L; E=''[]'acbb'[]'': E[x]='aaacbbc' in L but E[y]='aacbbac' NOT in L
[PASS] W-sum n=2 d=2 witness independently verified 
[PASS] W-sum n=2 violates (2,s_U)-substitutability (bounded, verified witness) 
    W-sum n=3: |L_{<=12}|=72 d=1 compared-pairs=208 violations=1
      WITNESS d=1: x=('aaaaaacb',) type=('z',), y=('aaaaac',) type=('z',); shared E0=''[]'bbca': E0[x]='aaaaaacbbbca', E0[y]='aaaaacbbca' in L; E=''[]'bc': E[x]='aaaaaacbbc' in L but E[y]='aaaaacbc' NOT in L
[PASS] W-sum n=3 d=1 witness independently verified 
    W-sum n=3: |L_{<=12}|=72 d=2 compared-pairs=342 violations=1
      WITNESS d=2: x=('aaaaaa', 'c') type=('1', 'z'), y=('a', 'aaaaac') type=('1', 'z'); shared E0=''[]'a'[]'bbbc': E0[x]='aaaaaaacbbbc', E0[y]='aaaaaaacbbbc' in L; E=''[]'acbbb'[]'': E[x]='aaaaaaacbbbc' in L but E[y]='aacbbbaaaaac' NOT in L
[PASS] W-sum n=3 d=2 witness independently verified 
[PASS] W-sum n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
    W-aligned n=2: |L_{<=12}|=20 d=1 compared-pairs=24 violations=1
      WITNESS d=1: x=('aacbbc',) type=('z',), y=('cbca',) type=('z',); shared E0=''[]'a': E0[x]='aacbbca', E0[y]='cbcaa' in L; E='a'[]'': E[x]='aaacbbc' in L but E[y]='acbca' NOT in L
[PASS] W-aligned n=2 d=1 witness independently verified 
    W-aligned n=2: |L_{<=12}|=20 d=2 compared-pairs=16 violations=1
      WITNESS d=2: x=('aa', 'c') type=('1', 'z'), y=('a', 'ac') type=('1', 'z'); shared E0=''[]'a'[]'bbc': E0[x]='aaacbbc', E0[y]='aaacbbc' in L; E=''[]'acbb'[]'': E[x]='aaacbbc' in L but E[y]='aacbbac' NOT in L
[PASS] W-aligned n=2 d=2 witness independently verified 
[PASS] W-aligned n=2 violates (2,s_U)-substitutability (bounded, verified witness) 
    W-aligned n=3: |L_{<=12}|=36 d=1 compared-pairs=37 violations=1
      WITNESS d=1: x=('aaaaaacbbbc',) type=('z',), y=('aaaacbbca',) type=('z',); shared E0=''[]'a': E0[x]='aaaaaacbbbca', E0[y]='aaaacbbcaa' in L; E='a'[]'': E[x]='aaaaaaacbbbc' in L but E[y]='aaaaacbbca' NOT in L
[PASS] W-aligned n=3 d=1 witness independently verified 
    W-aligned n=3: |L_{<=12}|=36 d=2 compared-pairs=111 violations=1
      WITNESS d=2: x=('aa', 'aaaa') type=('1', '1'), y=('a', 'aaaaa') type=('1', '1'); shared E0=''[]'a'[]'a': E0[x]='aaaaaaaa', E0[y]='aaaaaaaa' in L; E=''[]'cbbc'[]'': E[x]='aacbbcaaaa' in L but E[y]='acbbcaaaaa' NOT in L
[PASS] W-aligned n=3 d=2 witness independently verified 
[PASS] W-aligned n=3 violates (2,s_U)-substitutability (bounded, verified witness) 
==============================================================================
SECTION 4: Route B regular sieves (complete DFAs, <=3 states)
states<=2: distinct languages (length<=6 signature): 106
    states<=2: distinct languages (length<=6 signature): 106
    pass at N=6: 22
    pass bounded d=1,2 at N=5: 22 ; at N=7: 22
    states<=3: distinct languages (length<=6 signature): 40812
    pass at N=6: 197
    pass bounded d=1,2 at N=5: 197 ; at N=7: 197
    3-state survivors cross-tab (Parikh-determined?, presence-witnessed?): {(True, True): 14, (True, False): 97, (False, True): 86}
[PASS] sieves: 22 survivors (<=2 states), 197 survivors (<=3 states) 
[PASS] sieves: every survivor is Parikh-determined or presence-witnessed (bounded, N=7) 
==============================================================================
SECTION 5: Corollary R2 sanity (fan-out 1)
[PASS] CE n=2 untyped 1-substitutable (bounded) 
      untyped witness: x=('bcac',) type=('z',), y=('bbaab',) type=('1',); shared E0=''[]'cacb': E0[x]='bcaccacb', E0[y]='bbaabcacb' in L; E=''[]'baabb': E[x]='bcacbaabb' in L but E[y]='bbaabbaabb' NOT in L
[PASS] CE n=2 minus W_n is NOT untyped 1-substitutable (as Cor. R2 forces) 
[PASS] CE n=3 untyped 1-substitutable (bounded) 
      untyped witness: x=('bbcacb',) type=('z',), y=('bbbaabb',) type=('1',); shared E0=''[]'aabbbbaabcacbb': E0[x]='bbcacbaabbbbaabcacbb', E0[y]='bbbaabbaabbbbaabcacbb' in L; E=''[]'aabbbbaabbaabbb': E[x]='bbcacbaabbbbaabbaabbb' in L but E[y]='bbbaabbaabbbbaabbaabbb' NOT in L
[PASS] CE n=3 minus W_n is NOT untyped 1-substitutable (as Cor. R2 forces) 
==============================================================================
SECTION 6: Corollary U on A1 data, Prop LS randomized sanity
    A1 n=3 single-core words: totals of a by label d: [(1, [4]), (2, [6])]
    Lemma C/Cor. U prediction: some a^g cbbbc a^h with g+h=8 must lie in L; present in A1? False
[PASS] A1 n=3: Lemma C hypotheses hold and the forced word a^g c b^3 c a^h (g+h=8) is absent => A1 not in C_{2,s_U} 
[PASS] Prop LS randomized sanity: shortest pattern-containing word <= k(k+1)f|V|(r+1)theta in all non-vacuous trials grammars=93 nonvacuous=72
==============================================================================
SUMMARY: 72 tests, 72 PASS, 0 FAIL, elapsed 315.6s

===== END FILE =====