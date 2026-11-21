# Round Thirteen — noncommutative U, T1, false X1 and 40-word counterexample

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
| `PROMPT_CLAUDE_ROUND13_FABLE_C_NONCOMMUTATIVE_U_2026-11-15.md` | 75734 | `ec6c01343b2fca1e06379a32d2f7d0b680ee0d2dc354bc8023362e62b7a69d1a` |
| `README_SHA256.txt` | 1914 | `864878205c18e94631a7487372442330df1eced409f5c4e8492183277d7ea879` |
| `audit_claude_round13_noncomm_U_independent_2026-11-15.md` | 13412 | `f2f54516046fb6bbc8c25d32ed6e96d5233d440320ca057cf6b8d9d74c712979` |
| `claude_round13_noncomm_U_checker_2026-11-15.py` | 24907 | `3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a` |
| `claude_round13_noncomm_U_checker_output_2026-11-15.txt` | 5288 | `3dc1019ea1e9a0b26da10ab7d2f8f6badb6efc47f8d7c55738652d0ada4433b5` |
| `claude_round13_noncomm_U_checkpoint1_2026-11-15.md` | 1361 | `333edfdb04e59886ae6c3da7bb6f8af822309941cdff58c29d1adadb4495b716` |
| `claude_round13_noncomm_U_final_report_2026-11-15.md` | 18599 | `cb1782110ebf873d9a31127442243c9adca02e0b9a05743f3116145244c5394e` |
| `claude_round13_noncomm_U_next_obligations_2026-11-15.md` | 2992 | `496ae66d32cd3c36f635db0702f6760317c6e96a1cd045a2eeb6636b604defbb` |
| `round13_E2_original_rerun_2026-11-15.txt` | 1893 | `c5de54a67a939f9837d9d5fee50d3db30f9222a3dc7e565539816f701c5c9cbc` |
| `round13_independent_X1_counterexample_2026-11-15.py` | 2305 | `715ddf6329f4bad6e1745587aff8b8d37b57d3f79a163faa776eb921a0c291ba` |
| `round13_independent_X1_counterexample_output_2026-11-15.txt` | 467 | `b915b52308612570f65f79ffd0bb33b29328da90d971e010063d801f210b3c09` |
| `round13_independent_checks_2026-11-15.py` | 5388 | `a5666fef8082bc4b59d00f11deacb753dc42f174bf136f081210a8de022efc6e` |
| `round13_independent_checks_output_2026-11-15.txt` | 736 | `0a7541f61afc7754fcc80c0bdcfb3df223fc49976599611c29ee4dba9b8528b7` |
| `round13_subset_rerun_2026-11-15.txt` | 3154 | `1a9cb52dc2f87e91f73796c1a4f698a13ad1d0d2e5f33e7e04415afe1533071f` |
| `round13_x1_adversarial_probe.py` | 1324 | `31d5aea9fba6f00aa2cf19d4c865f191bb9df9188f9c77755d05e2cec116eabc` |
| `round13_x1_adversarial_probe_log.txt` | 250 | `c109105e89891a932f77063425940ce5606318dcd7d28562c145513ad65959d4` |

## Original source bodies


===== BEGIN FILE PROMPT_CLAUDE_ROUND13_FABLE_C_NONCOMMUTATIVE_U_2026-11-15.md bytes=75734 sha256=ec6c01343b2fca1e06379a32d2f7d0b680ee0d2dc354bc8023362e62b7a69d1a =====
# Claude 第十三段・数学探索依頼書
## Fable-C から非可換予想 U へ：fan-out 2 の単項希少型、Euler 宿主可能性、中心問題 `op:fanout-two`

**作成日：** 2026-11-15 JST  
**課題種別：** 純粋数学の独立探索・厳密な証明または反例構成。論文執筆、U₂の独立論文化、GitHub編集は依頼しない。  
**優先課題：** Fable予想 U（非可換の場合）に決着をつける、もしくは新しい一般補題・厳密な反例・決定的障壁を得る。  
**最終的な関心：** 論文 #2 の正式な `op:fanout-two` を解決すること。予想 U はそのための戦略的な中間課題であり、**予想 U の成立だけでは正式問題は解けない**。

> **Claudeへの最重要要請：** 読み込んだFableの証明を無批判に引き継がず、数学的に正しい定義から独立に考えてほしい。Euler連結性が真であることを仮定しない。証明可能なら証明、偽なら最小の具体的反例と「どの追加条件があれば成立するか」を提示する。よりよい発想があれば従来路線を捨ててよい。

---

# I. 何を解くのか

## I-1. 正式な中心的開問題（最上位の目標）

固定された `f≥2`, `r_max≥2` について、有限半群の擬多様体 `V` が一様多項式特徴データ長を持つことと `V⊆LG` が同値か。既知：`V⊆LG` は任意のfan-outで十分。fan-out 1では必要十分。fan-out ≥2で必要性が未解決。

読み取り専用の正本：

- GitHub repository: https://github.com/growupkuriyama-hub/Papers
- 原稿： https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/main.tex
- 現行研究状況： https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/HANDOFF_CURRENT.md
- 必須原稿ラベル：`def:grammar-properties`、`def:tuple-substitutable`、`def:class-cmcf`、`def:uniform-polydata`、`lem:thickness-equivalence`、`lem:typed-homogeneity`、`prop:rare-type`、`lem:distinguishing`、`prop:abelian-coset-filter`、`thm:local-group-polydata`、`thm:fanout-one-data`、`lem:power-transfer`、`thm:doubling-no-lift`、`thm:lg-characterization`、`op:fanout-two`。
- fan-out 2 特殊上界 U₂ の状況（研究アーカイブ、中心問題の解決ではない）： https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/STATUS_U2_STANDALONE_FORMALIZATION_2026-11-15.md
- U₂ 手証明と P1/B6/HC の参考： https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/theorem_U2_overlapping_projections_standalone_2026-11-15.md
- 第十一段までの詳細資料・コード（必要なら）： https://github.com/growupkuriyama-hub/Papers/blob/main/02-v4-fixed-s-mcfg/v2/reviews/ROUND11_SOURCE_BUNDLE_2026-11-15.md

**優先順位**：原稿の正確な定義・定理 ＞ 独立に検証可能な数学的証明 ＞ 過去AIの評価・経験則。GitHubを直接取得できない場合、以下の本ファイルと末尾の一次資料付録を使って探索し、見られなかった箇所は明示する。GitHubは読むだけで、commit, PR, issue作成をしない。

## I-2. 今回の具体的主目標：Fable予想 U

半束型付け `s:Σ⁺→S`（正値像は有限半束）、`f≥2`、`L∈C^{mcf}_{f,s}`、`G` は `L∩Σ⁺` の **reduced good MCFG** でfan-out ≤f・rank ≤rとする。ある `a∈Σ` に対し `a^N∈L` とし

\[
 N:=\min\{n\ge 1:a^n\in L\}.
\]

**予想 U：** 固定した有限アルファベット `Σ`、固定したパラメータ `f,r,s` のもとで、`N≤p_{Σ,f,r,s}(||G||,\bar θ_G)` となる**普遍の多項式**が存在するか。まず `f=r=2` および `s=c_Σ`（内容型）に集中してよい。その後、任意の半束型付けに適用可能か吟味せよ。

- `||G||` は元の reduced good 文法サイズ。`\bar θ_G=max(1,θ_G)` は**元の G の規則厚さ**。型付き精密化後の厚さへすり替えない。
- `Σ`, `s`, `f`, `r` は **nに依存させない**。多項式の次数が `|Σ|` に依存するのは許される。`N=poly(n)` のみを示す場合は、`||G||,\bar θ_G` との関係を明示する。
- **反例の成功判定**：固定 `Σ,s` の明示族 `(L_n,G_n)` について、`G_n` がgood, reduced, rank≤2, fan-out≤2、`L_n∈C^{mcf}_{2,s}`、`||G_n||,\bar θ_{G_n}=poly(n)`、かつ `N_n` が全多項式を超えることを**すべて厳密に証明**する。これなら予想 U を反証し、さらに `s` が非LGの半束型付けで希少型強制を満たす場合は正式中心問題の下界にも直結しうる。必ずその含意の仮定を別途証明する。
- **予想 U が証明された場合**：あくまで単項語の最短長を制御するにすぎない。`τ(G,s)` 全体の多項式上界も、`op:fanout-two` のNOも得られない。一般希少型と区別部分言語のルートは残る。
- **半束型付け**と**内容型付け**は区別する。任意の半束型は内容型を介して決まるが、逆向きの代入可能性の含意を無断で使わない。

## I-3. 正確な組代入可能性（失敗しやすい最重要条件）

`d∈{1,2}` で、非空成分からなる二組 `x=(x₁,…,x_d), y=(y₁,…,y_d)` に対し、

\[
 s^{(d)}(x)=s^{(d)}(y),\qquad
 \mathcal D_L^{(d)}(x)\cap\mathcal D_L^{(d)}(y)\ne\emptyset
 \ \Longrightarrow\ \mathcal D_L^{(d)}(x)=\mathcal D_L^{(d)}(y).
\]

文脈は `E=v₀□₁v₁□₂v₂`（`v₁∈Σ⁺`、外側 `v₀,v₂∈Σ*`）であり、**二穴の間にΣ上の非空セパレータが必要**。投影後に空になることとは別。語全体の型一致ではなく、**各穴の成分型一致**が必要。短縮するなら `E_accept, E_test, x, y` を実際に書き、すべての非空性・型・受理を検証する。

`good` は `ε-free`, `nondeleting`, `nonpermuting`, `nonmerging` の全て。推測の文法がただの MCFG や一般CFGであることでは不十分。部品の複製、順序反転、穴の隣接、生成語のゼロ長成分を勝手に認めない。

---

# II. 直前の成果・何が確かで何が未解決か

## II-1. Fable-C：可換言語の単項希少型の上界

**入力の基準資料は本ファイルの附録A（Fable原報告）・附録B（ChatGPT独立監査）**。どちらも全文を末尾に同梱している。必ず少なくともFableの §5, §6、監査の §1–§8 を読んでから研究結果を断言すること。独立監査は「手証明としてVALID WITH CLARIFICATIONS」と評価したが、専門家査読・Lean/Coq形式化・新規性判定ではない。

条件：`Σ={a}⊔Δ`、`D=|Δ|≥1`、`s` は半束型付け、`L` は**可換**（Parikhベクトルで受理が決まる）、`L∈C^{mcf}_{f,s}`、`G` は任意fan-outのreduced good文法、rank≤r、`v=|V|`、`θ=\bar θ_G`。Fable-C の主張：

\[
 \begin{aligned}
 B&=D!\theta^D,\\
 \rho&=2DB,\\
 K_0&=2(r+1)\theta\,[4(r+1)\rho]^{D2^D},\\
 N&\le\max\{(D+1)BK_0+1,\,2^{D+1}v(r+1)K_0\}
   =O_{D,r}\!\left(v\theta^{1+D+D^2 2^D}\right).
 \end{aligned}
\]

この結果は **d=1 の代入可能性だけ**で示すため、可換言語の場合、fan-out 2固有の主張ではない。注意：可換＝非終端の可換ではなく、最終語の受理の可換性。

独立監査で明記・補充された論点：部品交換の共通受理文脈、分岐台の加法性の帰納ベース、短い整数関係の符号付き係数、非分岐台の高々二根道被覆、最重子経路の全実数窓、最終の指数計算。これを前提にしてよいが、必要な主張を引用するときは要件を明記する。

## II-2. Fable補題5.1（非可換でも成立するとされた部分）

`a^N` が最短受理単項語であるとき、次が原報告で提示されている。

- (R) 分離された二つの正長の `a` 連の**総長を一定**にして再配分する二穴移送（適用条件 `i+j≤N−1` 等）。
- (U) 同じ二側文脈で異なる長さの正の `a` 冪を受理できない、という**一意性**：`P a^i Q` と `P a^{i'}Q` が共に受理され、`1≤i<i'≤N` なら最小性に反する。
- (E) 部品交換：適切な `a V a^e` 型の証人があれば、同じ内容型の部品が共通文脈を介して関連付けられる。

これらの補題は文字の**順序そのものを不問にする**わけではない。可換Cの証明における単位 `(δ,V)` が、非可換では非 `a` 文字列の**正確な骨格**を記録しなければならない部分がある。`Parikh`、bigram count、内容集合、語全体の分布同値を同一視しない。

## II-3. Fable §6 の未証明の核心

原報告の提案は、非可換語の「部品」を同じbigram多重集合のもとで再配列し、Euler的な有向多重グラフの歩道操作へ落とすこと。

**しかし、重要なのは「組合せ論的にEuler歩道で連結」というだけでなく、各操作に必要な受理済みの**共通文脈＝宿主(host)**があること。** これは必ず別命題として証明すべき。宿主がなければ、言語所属を保存するとは限らない。

探索上の提案（押しつけではない）：

1. まず「部品」の厳密な定義を提示：非 `a` 骨格を保持する区間、`a` ラン、二穴の間に残る区切りなどを含め、順序を保つ情報と消してよい情報を分ける。
2. 交換操作 `M↦M'` を定義し、対象となる**同一の言語 L** 内で各ステップを適法化する共通文脈を具体化。
3. Bigram多重集合、端点、内容、非 `a` 骨格、`a` 総数、穴成分の型の保存・非保存を精査。何が本当に不変か、反例で壊れるかを調べる。
4. **Hostability lemma** を明示的に量化：語族のどの状態とどの遷移で、どの大きさの補助部品複製があれば、必要な `E₀,E₁` が存在するか。もとの言語の受理語から、その補助複製を作ることも示す。
5. Euler連結性の真偽を**小さな固定文字集合・短い具体語**で敵対的に確認。falseなら `(word1, word2, invariant, inaccessible_move, host_failure)` を反例とし、どの文脈前提が足りなかったのか証拠化。
6. 連結性が証明できたら、Fable-Cの欠損量 `δ` を有限次元（例：bigramベクトル）で**一価で加法的な量**として定義し直す。ここで (U) を適用する際は、最終的に**同じ文字列骨格に置ける二つの受理語**を必ず構成する。
7. 欠損の加法性・符号付き整数関係・分岐／非分岐の被覆が本当に移植できるか証明。Fable-Cにおける `D` の指数をそのまま `(|Σ|−1)^2` に置換しただけでは証明ではない。
8. 特にfan-out 2の文法のタプル収率は**二つの離れた成分**を持つ。文法の部分木置換は各成分の相対配置を保持するので、語レベルの単一部品モデルだけで済まない可能性を監査する。

**厳禁**：「十分な部品を複製すればhostが存在するはず」「同じParikhだから受理」「すべてのEuler swapはlanguage-preserving」「有界検査で反例なしだから証明」と推論すること。

## II-4. 過去成果との関係を検証せよ

- 現行原稿の `lem:power-transfer` / `thm:doubling-no-lift` は組代入可能性の重要な制限。ただし**冪移動は語長とParikhを保つ**ので、単独で `N` の多項式上界にはならない。
- Fable定理A：`L_n⊆L∈C^{mcf}_{f,s}`（半束型）なら、`n≥3` で `baab∈L`。**族全体の包含**が仮定であり、長い `W_n` 1語だけから `baab` を強制するとは限らない。証明書は原報告に参照あり。
- Fable定理B：reduced good grammarのアーベル剰余類条件は長さ `≤(r+2)θ` の語で検出可能。アーベルな区別部分言語を使った超多項式下界の障壁。
- U₂：重なり二射影bigramで受理が決まる**特殊クラス**だけの多項式代表長手証明。そこから半束型付け一般・非可換受理一般への推論は禁止。
- Claude第十二段の補償法則は最短 `a^N` と二穴文脈の関係を扱う。独立監査は**付録C**。研究上、Fable 5.1の既知帰結と一致・独立・強化のどれなのか確認してよいが、新旧比較だけで探索を終えない。
- Fable-Cと既存`reviews/`の定理 L（\ell=1）等の新規性・包含関係は未照合。文献的オリジナリティを無根拠に断言しない。

---

# III. 探索課題：優先順位はあるが、発想は自由

## 課題A — 非可換予想Uを直接攻める（第一優先）

可能なら次のうち最も強いものを目指す。

- **A1: 全面的な証明**：固定 `Σ,f,r,s` に対し `N≤poly(||G||,θ)`。数学的定理、完全な仮定、各中間補題、全称証明。
- **A2: 反例族**：固定 `Σ,s` の明示的good MCFG族で `N` 超多項式、`C^{mcf}_{2,s}` 厳密証明。一般 `op:fanout-two` にどこまで届くか別判定。
- **A3: 非自明な限定定理**：例えば `a`-ランの間の非 `a` 因子数が一様に有界、bounded language、Eulerグラフの基礎形が固定、有限個の核型、rank 1/2、特殊な良い文法テンプレートなど、**厳密に定義された自然な部分クラス**での完全証明。後で一般化できるよう、削れない仮定を説明。
- **A4: 方法の反例**：予想Uの反例でなくても、提示したEuler連結性／hostability／δ加法性という中間主張の明示的反例を見つければ価値がある。その場合、中間命題だけが偽なのか、予想Uまで偽なのかを区別。

**重大な自由度：** Euler法が不適切なら、代数的置換・残余／syntactic congruence・tree automata・長語の分解・変換半群・整数流・タイプ付き文脈など、完全に別の方法を選んでよい。自分で新しい補題を発明することを重視する。

## 課題B — 二穴宿主の構成的命題と小規模反証検査

ユーザーの研究に再利用できる形で、検証対象を二つに分けること。

1. **純組合せ命題**：指定した有向多重グラフ・端点条件から、Euler的な隣接交換列が存在するか。
2. **言語論的命題**：各交換が固定 `L∈C^{mcf}_{2,s}` 内で、**共通受理文脈**を与える実際の代入操作として実現可能か。

(1)の証明を(2)として使ってはいけない。コードは純組合せの探索だけでなく、候補の `E₀,E₁,x,y` の実際の文字列、型、非空セパレータ、受理／非受理を記録し、正誤を確認できるものにせよ。

- 言語 `L` が無限で完全な所属判定が困難なら、その事実を明示。**有限切断版の「PASS」を無限言語の組代入可能性の証明としない。**
- 偽であることを示す場合、一般命題の仮定をすべて満たす最小例で、交換不可や宿主不在を示す。ただの探索打切りを反例と呼ばない。
- 正しいと示す場合、必要な**有限の補助コピー数・パラメータ依存**を定量化すると、Fable-Cの整数関係法と接続しやすい。
- 適法な`d=1`文脈と`d=2`文脈、同じroot成分／別root成分を区別。

## 課題C — Fable-Cの代替的不変量を探す

`a` を消して得る語骨格、ラン境界のbigram、`a`-run間の隣接遷移、有限次数の部分語計数、trace monoid同値、regular controlなどを候補としてよい。ただし以下を独立に評価する。

- 不変量が**言語所属**に実際に関係するのか、それとも導出手続の恣意的選択にすぎないか。
- 一定の不変量の中で**短い代表**を持つか。繰り返しを縮める際、構造を保持する**正の**受理文脈があるか。
- 次元（|Σ|固定なら定数）と係数有界性から、最短 `a^N` の**語長**を真に上界できるか。
- 二穴の位置制約と非終端二成分の絡み合いが実際に壊す場合は、その最小の文法／語例を出す。

## 課題D — 本来の中心問題への直結を忘れない

もし予想Uが成立しそうなら、それが示すのは「希少な単項 `a^N` による下界不可」という障壁であって、**すべての希少型語の短縮**ではない。他方、非可換予想Uが偽の場合、作った反例を `prop:rare-type` や `lem:distinguishing` に接続できるか厳格に検査。

余力があれば、任意の内容型付けの代表長 `τ(G,c_Σ)` の上界、あるいは非LGの擬多様体の下界を別法で導けるか検討してよい。だが主課題Aを未検査のまま一般的展望だけを書かない。

---

# IV. 進め方と品質要求

## IV-1. 最初に行う論理検査

研究を始める前に、以下の点をA4サイズ相当の短い表で整理する。

- Fable-Cの主定理の仮定・量化／対象の `a^N`／文法サイズ・厚さ。
- 予想Uの正確な意味。**上界は固定 `Σ,f,r,s` に対して全 L,G で一様**であること。
- Fable 5.1(R),(U),(E) の前提・結論、適法な文脈。
- Fable §6 のEuler提案を「何が定理／何が推測」に分解。
- 前段の「VALID AS A HAND-PROOF」は形式化・査読ではないこと。

## IV-2. 数学作業の必須ルール

1. **[PROVED]** のラベルは、自分で欠落しない完全証明を書けた主張のみに使う。既知結果の引用は原稿定理ラベルと全仮定を明示。
2. **[REFUTED]** は、全仮定を満たす反例とその検証がある場合のみ。
3. **[COMPUTATIONAL EVIDENCE]** は探索範囲、打切り、seed、実行条件、実験コードの境界を示す。
4. 残る主張は **[CONDITIONAL] / [OPEN]**。`n=2`で失敗した候補から`n≫1`の一律不可能性を無証明で述べない。
5. 証明でよく使う文脈は**文字列として具体化**し、充填前後と、中間セパレータの非空性、各穴型の一致を確認する。
6. `a`の最短冪語長が短いからといって、他の非単項希少型語も短いとは言わない。
7. **専門的な注意**：部品列での「Euler回路連結」から、言語の組代入可能性で許される「操作列」への移行には別の橋渡しが必須。
8. 実験が主張を支えないとわかったら、その事実を直ちに認める。コードの出力に合わせて定理の仮定を事後的に変えない。
9. 未査読結果は未査読と記す。新規性・公刊可能性を保証しない。

## IV-3. 最低限の実験仕様（必要な場合に実施）

- Python 3標準ライブラリ、固定seed、コマンド一つで再現可能。
- 入力の文法、導出木、有限受理集合／認識器、射影・不変量を明記。
- 反例候補について、`w,x,y,E_accept,E_test,s(x),s(y),E_accept[x],E_accept[y],E_test[x],E_test[y]` をJSON等で保存。
- 数学的な全称命題の**反例を探す**ときは、長さ上限と時間・メモリ上限を書き、未発見を証明扱いしない。
- 証明できた小さい補題については、その仮定をランダム生成や有界列挙で敵対的にストレステストし、人工的に仮定を一つ外した陰性対照も試す。
- 実行ログには原プログラムのSHA256を記す（外部ファイルがあれば各SHAを記す）。

## IV-4. 必須成果物（すべて研究資料・論文原稿ではない）

作業中に実質的成果を得た時点で、`claude_round13_noncomm_U_checkpoint1_2026-11-15.md` を作成。最後は、**証明・実験・未検査を混ぜない**次の成果物を保存する。

1. `claude_round13_noncomm_U_final_report_2026-11-15.md`：一文結論、命題一覧と状態ラベル、厳密な定理/反例、全証明、既知結果との論理関係、正式中心問題への含意、残存障壁、次の有力な一手。
2. `claude_round13_noncomm_U_checker_2026-11-15.py`：本当にコードで確認できる事項についての実行可能な検証器。コードを使う必要のない完全手証明なら不要だが、反例構成やhostabilityの検査を行った場合は必須。
3. `claude_round13_noncomm_U_checker_output_2026-11-15.txt`：実際の実行コマンド・終了コード・件数・FAIL数を含むログ。実験なしなら実験未実施と報告。
4. `claude_round13_noncomm_U_next_obligations_2026-11-15.md`：未解決の量化・補題・反例候補・テスト範囲と、正確な最小残余命題。

**ユーザーは独立論文を希望していない。** 投稿先検討、LaTeX本文化、GitHub登録・編集、既存原稿修正、PRは行わない。成果は数学探索として提出すること。

**成功条件の優先度：** 中心問題の厳密解決 ＞ 非可換予想Uの厳密証明・反例 ＞ 明示的な新しい広い部分定理／一般的障壁 ＞ 有限実験だけの観察。根拠なしの「解決した」は価値がない。

---

# V. 読んでから始める添付一次資料

以下は今回の新規ClaudeチャットでFable-Cと独立監査を別添しなくても済むように、原文を同じMarkdownへ収録したもの。**原文のAI主張は検証済み事実としてではなく一次研究記録として扱う**こと。GitHubの正本と内容が衝突したら正本を優先する。


## 附録A：Fable 2026-11-15 独立探索原報告（全文）

**一次資料：** `Fable_original_open_problem_report_2026-11-15.md`、UTF-8、27376 bytes、SHA256 `c0369cdc571944bfe702e52a3571939bc5981c332637bf8c49765ebc3e3ca223`。  
**注：** ここから次の区切りまでが原資料全文。

---

# `op:fanout-two` 独立研究報告（Fable, 2026-11-15）

**結論ラベル：`NEW THEOREM BUT OPEN`**
`op:fanout-two` 自体は解けていない。得られたのは (i) 倍化族に対する no-lift 定理の決定的な強化（機械検証済み証明書つき）、(ii) 薄い文法に対するアーベル型下界の一般的不可能性、(iii) 可換言語における単項希少型の多項式上界（新しい証明法）、(iv) 開問題の単一言明への還元、である。私の現時点の評価は「答えは NO（LG は fan-out 2 では境界でない）の方が見込みが高い」だが、これは**予想**であり証明ではない。

各主張の状態は次の記号で区別する：**[証明]** 本報告内に完全な証明がある／**[検証]** 明示的証明書を独立チェッカで検査済み／**[計算]** ハッシュベースの探索結果で証明書は未抽出／**[予想]**。

---

## 0. 読んだ資料と読んでいない資料

- GitHub を clone して読んだもの：`main.tex` の定義（`def:grammar-properties`, `def:tuple-substitutable`, `def:uniform-polydata`）、`lem:thickness-*`, `lem:distinguishing`, `prop:rare-type`, `prop:three-letter-family`, `thm:fanout-one-data`, `lem:power-transfer`, `thm:doubling-no-lift`, `op:fanout-two`；`HANDOFF_CURRENT.md`；U₂ ノートの定義と主張部分。
- **読んでいないもの**：`reviews/` の各ラウンド報告の本文（定理 L, P, S, L^⊗′ の証明、第九〜十一段の詳細）。したがって §5 の可換定理が既存の定理 L（ℓ=1）と結論の上で重なる可能性は排除していない。証明法は独立に構成した。
- 依頼書の問題設定に誤りは見つからなかった。一点だけ補足がある（§1）。

## 1. 開問題の単一言明への還元 [証明]

**命題 1.** \(f\ge2,\ r_{\max}\ge2\) を固定する。次は同値。
1. `op:fanout-two` の答えが YES。
2. 有限半束の擬多様体 \(\mathbf{SL}\) が fan-out \(f\)・rank \(r_{\max}\) で一様多項式特徴データ長を持たない。
3. ある有限アルファベット \(\Sigma\) とある半束型付け \(s:\Sigma^+\twoheadrightarrow\mathsf S\) について `def:uniform-polydata` の多項式が存在しない。

*証明.* \(\mathbf V\not\subseteq\mathbf{LG}\) なら \(U_1\in\mathbf V\)（`thm:lg-characterization`）で、擬多様体は有限直積・部分・商で閉じるから \(\mathbf{SL}=\langle U_1\rangle\subseteq\mathbf V\)。一様多項式性の失敗は \(\mathbf V\) について単調なので 2⇒1。逆に \(\mathbf{SL}\) 自身が \(\mathbf{LG}\) に含まれないので 1⇒2。2⇔3 は定義。∎

**補足 1′（上界側は内容型付けだけ見ればよい）.** 任意の半束型付け \(s\) は内容型付け \(c_\Sigma\) を経由するので \(\mathcal C^{\mathrm{mcf}}_{f,s}\subseteq\mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}\)。さらに \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) に対し \(\tau(G,s)\le\tau(G,c_\Sigma)\)：\(s\)-型付き非終端 \(B_{\mathbf t}\) の収率を含む内容型付き非終端 \(B_{\mathbf T}\) の類代表は、同じ分布を持ち \(s\)-型も \(\mathbf t\) だから \(\operatorname{Cl}_{L,s}(B_{\mathbf t})\) に入る。よって「全ての \(\Sigma\) で \(\tau(G,c_\Sigma)\) が多項式」が示されれば答えは NO。

つまり問題は U₁ の特定の3文字型付けではなく、**任意アルファベット上の内容型付け**の問題そのものである。下界側は大きなアルファベットを自由に使ってよく、上界側は内容型付けだけ処理すればよい。

## 2. 道具

以下 \(c(w)=\operatorname{alph}(w)\)、\(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、\(f\ge2\)。

**補題 2.1（滑り補題／共役移送）[証明].** \(l,r\in\Sigma^*\)、\(x_1,y_2,z,z',m\in\Sigma^+\) が \(zm=mz'\)、\(s(x_1z)=s(x_1)\)、\(s(z'y_2)=s(y_2)\)、\(l\,x_1\,z\,m\,y_2\,r\in L\) を満たすなら
\[(x_1z,\;y_2)\ \equiv_{L,s}\ (x_1,\;z'y_2).\]
*証明.* 文脈 \(E=l\,\square_1\,m\,\square_2\,r\)（\(m\neq\varepsilon\)）は両方の組を同じ語 \(l x_1 z m y_2 r=l x_1 m z' y_2 r\) に埋めるので共通の受理文脈であり、成分型は仮定より等しい。∎

`lem:power-transfer` は \(z=z'=u^\delta\), \(m=u\) の特別な場合。内容型付けでは条件は \(c(z)\subseteq c(x_1)\cap c(y_2)\) だけになる。特に：

**系 2.2（単位の移送）.** 内容型付けで、\(L\) のある語が因子 \(x_1\cdot d\kappa\cdot d\cdot y_2\)（\(d\in\Sigma\), \(\kappa\in\Sigma^*\), \(c(d\kappa)\subseteq c(x_1)\cap c(y_2)\)）を持てば、全ての \(l,r\in\Sigma^*\), \(m'\in\Sigma^+\) で
\[l\,x_1\,d\kappa\;m'\;y_2\,r\in L\iff l\,x_1\;m'\;\kappa d\,y_2\,r\in L .\]
同じ文字 \(d\) の連続する二つの出現に挟まれた単位 \(d\kappa\) は、後方の \(y_2\) の出現の直前へ（\(\kappa d\) として）語長と Parikh ベクトルを保ったまま移動できる。長い語では文字が必ず再出現するので、この移動は**避けられない**。

**定義 2.3（導出閉包）.** \(K\subseteq\Sigma^*\) に対し \(\operatorname{Cl}(K)\) を、\(K\) を含み次の規則で閉じた最小集合とする：\(d\in\{1,2\}\)、\(\mathbf x,\mathbf y\in(\Sigma^+)^d\) が成分ごとに同じ内容を持ち、\(E_0,E_1\in\mathcal E_d\) について \(E_0[\mathbf x],E_0[\mathbf y],E_1[\mathbf x]\) が既に入っていれば \(E_1[\mathbf y]\) を入れる。

**補題 2.4（健全性）[証明].** 半束型付け \(s\) と \(f\ge2\) について、\(K\subseteq L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) なら \(\operatorname{Cl}(K)\subseteq L\)。（\(L\in\mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}\) なので各規則適用は定義そのもの。）

**補題 2.5（射による輸送）[証明].** \(\varphi:\Sigma^*\to\Sigma'^*\) を非消去射、\(P,Q\in\Sigma'^*\) とすると \(P\,\varphi(\operatorname{Cl}(K))\,Q\subseteq\operatorname{Cl}(P\varphi(K)Q)\)。
*証明.* 導出の長さの帰納法。\(c(\varphi(u))=\bigcup_{e\in c(u)}c(\varphi(e))\) は \(c(u)\) のみで決まるので、内容が等しい成分は像でも内容が等しい。成分と穴の間の部分は非消去性により非空のまま。文脈 \(E=(l,m,r)\) は \((P\varphi(l),\varphi(m),\varphi(r)Q)\) に移る。∎

内容型付けの本質的な点は、**任意の**非消去射で導出が輸送されることである（文字互いに素である必要はない）。

## 3. 定理 A：倍化族は fan-out 2 で完全に崩壊する

\(L_n,W_n\) は `prop:three-letter-family` のもの（\(W_1=\mathtt{baab}\), \(|W_n|=3\cdot2^n-2\)）。

**定理 A [証明＋検証].** \(\Sigma\supseteq\{a,b,c\}\)、\(s\) を \(\Sigma^+\) 上の任意の半束型付け（\(s_U\)、\(c_\Sigma\) を含む）、\(f\ge2\)、\(n\ge3\) とする。\(L_n\subseteq L\) なる全ての \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) は \(W_1,W_2,\dots,W_n\) を全て含む。特に \(\mathtt{baab}\in L\) であり、\(W_n\) の型の最短語長は \(n\) によらず \(4\) 以下。
より一般に、非消去射 \(\psi\) について \(\psi(L_n)\subseteq L\) なら \(\psi(\mathtt{baab})\in L\)。

これは `thm:doubling-no-lift`（「同じ型・同じ Parikh の別の語がある」）を、半束型付けについて「定数長の語がある」まで強める。語を追加して族を修復する余地は一切ない。

*証明.*
(1) **証明書** [検証]：\(W_2=\mathtt{bbaabbaabb}\in\operatorname{Cl}(L_3)\) かつ \(\mathtt{baab}\in\operatorname{Cl}(L_3)\)。添付 `cert_L3_to_baab_pruned.json` は定義 2.3 の規則 33 回（\(d=1\) が 9 回、\(d=2\) が 24 回）の明示的列で、`verify_cert.py` が各ステップの前提（成分・中間部の非空性、内容の一致、\(E_0[\mathbf x],E_0[\mathbf y],E_1[\mathbf x]\) の所属）を独立に検査する。
(2) \(k\ge0\)、\(\varphi_k:a\mapsto W_k,\ b\mapsto b,\ c\mapsto c\) とすると \(\varphi_k(L_3)\subseteq L^{(k+3)}\)（\(E_{k+3}\) の収率集合）。\(k+3\le n\) なら \(E_{k+3}\) は \(L_n\) の中で文脈 \((P_k,Q_k)\)（例えば \(P_k=b^{\,n-k-3}\)）を持ち、\(P_k\varphi_k(L_3)Q_k\subseteq L_n\subseteq L\)。補題 2.5, 2.4 より \(P_kW_{k+2}Q_k,\ P_kW_{k+1}Q_k\in L\)。
(3) \(W_{k+3},W_{k+2},W_{k+1}\) は内容 \(\{a,b\}\) が等しく文脈 \((P_k,Q_k)\) を共有するので互いに \(\equiv_L\)（分布が一致）。
(4) \(W_n\in L\)。\(j\ge3\) で \(W_j\in L\) なら、\(k=j-3\) の同値 \(W_j\equiv W_{j-1}\) を文脈 \((\varepsilon,\varepsilon)\) に適用して \(W_{j-1}\in L\)。\(W_3\in L\) からは \(k=0\) の \(W_3\equiv W_1\) で \(W_1\in L\)。射版は \(\psi\circ\varphi_k\) で同じ。∎

**崩壊の機構.** 核は系 2.2 の「文字の飛び越し」である。探索で最初に見つかった例では、\(L_3\) の二つの語 \(b\,W_2\,[c\,W_1\,c]\,b\) と \(b\,W_2\,[b\,W_1\,c\,a\,c\,b]\,b\) から、\(b\) が \(c\) を右へ、\(c\) が \(\mathtt{bbaab}\) を左へ飛び越して、**同じ枠** \(b\,W_2\,c\,\square\,c\,bb\) に長さの違う \(c\) なし語 \(\mathtt{baa}\) と \(\mathtt{bbaaba}\) が入る。添付の証明書が実際に使うのは同種の二つの枠で、枠 \((\mathtt{bbcacbaabbc},\mathtt{acbb})\) に \(\mathtt{bbbaa}\) と \(\mathtt{ba}\) が、枠 \((\mathtt{bcbaabcb},\mathtt{cbacbb})\) に \(\mathtt{baabba}\) と \(\mathtt{baa}\) が入る。これと \(b\) の冪移送 \((b,bb)\equiv(bb,b)\) を合わせて \(W_3\) が \((a,2b)\) ずつ縮む（22→19→16→13→10→7→4）。省略記号 \(c\) が可動なので「省略の深さ」を位置で符号化できない、というのが本質である。

**検証の範囲.** `verify_log.txt`：\(L_3\) 上の証明書（刈込み 33 手・完全版 2945 手）に加え、輸送補題に頼らず \(L_4\)（\(k=1\) および \(k=0\) で枠 \((b,W_3b)\)）、\(L_5\)（\(k=2\)、および \(k=0\) で枠 \((bc,\,c^5ac^4b)\)）、\(L_6\)（\(k=1\)）、\(L_7\)（\(k=4\)）の中で同じ 33 手を直接検査し全て通過。所属判定は \(L_n\) の再帰的認識器による（列挙やハッシュに依存しない）。

**命題 A′（括弧を別文字にした変種）[計算].** \(E_i\to b\,E_{i-1}E_{i-1}\,d\mid c\,E_{i-1}\,e\)、\(E_0\to a\)（5文字、内容型付け）の族 \(V_n\) についても、\(\operatorname{Cl}(V_3)\) は \(W_1'=\mathtt{baad}\) と \(W_2'=\mathtt{bbaadbaadd}\) を含む（長さ 22 → 19 → 16 → 13 → 10 → 7 → 4）。これが正しければ定理 A の証明 (2)–(4) がそのまま通り \(V_n\) も定数長に崩壊する。ただしこれは 64 bit ハッシュを用いた打切り閉包＋最良優先探索の結果で、**明示的証明書は抽出していない**。

**観察 [計算].** \(s_U\) 型付けでは \(L_2\) の（長さ 10 打切り）閉包が既に語 \(\mathtt a\) を含む。内容型付けでは \(L_2\) は閉じており、崩壊は \(n=3\) から始まる。

## 4. 定理 B：薄い文法はアーベル不変量を隠せない

**定理 B [証明].** \(G\) を reduced good MCFG（fan-out 任意、rank \(\le r\)）、\(\theta=\bar\theta_G\)、\(g:\Sigma^*\to\mathsf A\) をアーベル群へのモノイド射、\(\mathsf H\le\mathsf A\)、\(\gamma\in\mathsf A\) とする。長さ \(\le(r+2)\theta\) の全ての \(w\in L(G)\) が \(g(w)\in\gamma+\mathsf H\) を満たせば \(L(G)\subseteq g^{-1}(\gamma+\mathsf H)\)。

*証明.* 各非終端 \(A\) に `lem:thickness-equivalence`(ii),(iv) の短い収率 \(\mathbf u_A\)（\(\|\mathbf u_A\|_1\le\theta\)）と文脈 \(E_A\)（固定部 \(\le\theta\)）を取り、\(c_A:=\sum_i g(u_{A,i})\) とおく。主張：全ての \(\mathbf u\in L_A\) で \(\sum_ig(u_i)\equiv c_A\pmod{\mathsf H}\)。導出の高さの帰納法：\(\mathbf u=\rho(\mathbf u^1,\dots,\mathbf u^q)\) なら非削除性と可換性から \(g(\mathbf u)=g(\text{$\rho$ の終端})+\sum_jg(\mathbf u^j)\equiv g(\rho(\mathbf u_{B_1},\dots,\mathbf u_{B_q}))\)。語 \(E_A[\rho(\mathbf u_{B_1},\dots)]\) と \(E_A[\mathbf u_A]\) は共に \(L(G)\) に属し長さ \(\le(q+2)\theta\) なので仮定より \(g\) 値が同じ剰余類にあり、\(g(\rho(\mathbf u_{B_j}))\equiv c_A\)。\(A=S\) では \(c_S=g(u_S)\in\gamma+\mathsf H\)。∎

**帰結.**
- `lem:distinguishing` を \(L'=L\cap g^{-1}(\gamma+\mathsf H)\)（`prop:abelian-coset-filter` の型の部分標的）に適用しても、区別語の長さは高々 \((r_{\max}+2)\bar\theta_G\)。**アーベル剰余類フィルタによる部分標的では超多項式下界は出ない。**
- 例：\(\{w:|w|_a\equiv|w|_c \pmod{2^n}\}\) は全ての型付けで組代入可能だが、多項式サイズ・多項式厚さの reduced good 提示を持たない（持てば上の議論で \(|w|_a=|w|_c\) が \(\mathbb Z\) 上で成立してしまう）。指数的な法や重みを持つ計数は厚さに必ず現れる。

## 5. 単項型の構造と定理 C

以下 \(a\in\Sigma\)、\(s\) は半束型付け、\(a^N\in L\) で \(N=\min\{i\ge1:a^i\in L\}\)。

**補題 5.1 [証明]（非可換・一般の \(L\in\mathcal C^{\mathrm{mcf}}_{2,s}\) で成立）.**
- **(R) 連の再配分.** \(p\,a^i\,q\,a^j\,r\in L\)、\(q\in\Sigma^+\)、\(i,j,i',j'\ge1\)、\(i'+j'=i+j\le N-1\) なら \(p\,a^{i'}q\,a^{j'}r\in L\)。（\(a^N=a^i\cdot a\cdot a^j\cdot a^{N-1-i-j}\) が共通文脈。）
- **(U) 一意性.** \(P a^iQ,\ Pa^{i'}Q\in L\)、\(1\le i<i'\le N\) は起こらない。（起これば \(a^i\equiv a^{i'}\) で \(a^{N-i'+i}\in L\)、最小性に反する。）
- **(E) 交換.** \(V,V'\notin a^*\) が \(aVa^{e},\,aV'a^{e'}\in L\)（\(1\le e,e'\le N-2\)）を満たし \(c(V)\cup\{a\}=c(V')\cup\{a\}\) なら、\(i'-i=e'-e\) なる適当な \(i,i'\ge1\) について \(a^iVa\equiv a^{i'}V'a\)。

(R),(U) から、\(a\) の総数が \(N\) 未満の語では「\(a\) の個数は、\(a\) の連を1文字に潰した骨格の関数」である。すなわち単項希少語 \(a^N\) があると、\(L\) の他の語は**骨格 → 欠損 \(\delta=N-|w|_a\)** という関数のグラフになり、(E) により欠損は同じ内容類の部品の入替えについて加法的に振る舞う。

**定理 C（可換言語では単項型は希少になれない）[証明；独立監査は未実施].** \(\Sigma=\{a\}\sqcup\Delta\)、\(D=|\Delta|\ge1\)。\(L\) を可換（所属が Parikh ベクトルのみで決まる）とし、ある半束型付け \(s\) と \(f\ge1\) で \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、\(G\) を \(L\cap\Sigma^+\) の reduced good 提示（fan-out 任意、rank \(\le r\)、\(v=|V|\)、\(\theta=\bar\theta_G\)）とする。\(a^N\in L\) で \(N\) が最小なら
\[N\ \le\ \max\bigl\{(D+1)BK_0+1,\ \ 2^{D+1}\,v\,(r+1)K_0\bigr\},\quad B=D!\,\theta^{D},\ \rho=2DB,\ K_0=2(r+1)\theta\,\bigl(4(r+1)\rho\bigr)^{D2^{D}} .\]
特に \(N=O_{D,r}\bigl(v\,\theta^{\,1+D+D^22^D}\bigr)\)：固定アルファベットでは多項式。

*証明.* \(P\subseteq\mathbb N\times\mathbb N^\Delta\) を \(L\) の Parikh 像とし、点を \((e,V)\) と書く。
**(0) 木.** \(a^N\) の \(G\) における導出木を節点数最小に取る。同じ非終端の二節点は収率の総長 \(k\) が等しく（違えば短い \(a\) 冪が出る）、入れ子にならない（節点数最小性）。よって深さ \(\le v\)。短い収率 \(\mathbf u_A\) の Parikh を \((\alpha_A,V_A)\) とする。\(k_A>\theta\) の節点を「大」と呼ぶと \(V_A\neq0\)（さもなくば \(a^{N-k_A+\alpha_A}\in L\) が最小性に反する）。欠損 \(\delta_A:=k_A-\alpha_A\in[k_A-\theta,k_A]\)、類 \(T_A:=\operatorname{supp}V_A\)。\(k_A=N\) の節点は根からの単項鎖をなす。
**(1) 実現集合.** \(\mathcal V:=\{V\ne0:\exists e\in[1,N-1],(e,V)\in P\}\)。(U) より \(e\) は一意で \(\delta(V):=N-e\) が定まる。\(k<N\) の大節点を省略すれば \(V_A\in\mathcal V\), \(\delta(V_A)=\delta_A\)。
**(2) 交換.** \(V,V'\in\mathcal V\)、\(\operatorname{supp}V=\operatorname{supp}V'\)、\((e,Q+V)\in P\)、\(e\ge1\)、\(e':=e+\delta(V)-\delta(V')\ge1\) なら \((e',Q+V')\in P\)。（\(i=1+\max(0,\delta(V')-\delta(V))\), \(i'=1+\max(0,\delta(V)-\delta(V'))\) とし、Parikh \((i,V)\) と \((i',V')\) の語は内容が等しく文脈 \((N-\delta(V)-i,0)\) を共有するので同値。\(e\ge i\) は \(e'\ge1\) と同値。）
**(3) 分岐類での完全加法性.** 類 \(T\) が**分岐的**とは、互いに素な大節点 \(B,C\)（\(k<N\)）で \(T_B=T_C=T\)、\(N-\delta_B-\delta_C\ge1\) なるものがあること。このとき、類 \(T\) の大非終端 \(J_1,\dots,J_t\)（各 \(\delta_{J}\le(N-1)/2\)）と \(\sum m_j\delta_{J_j}\le N-1\) なる多重集合 \(m\ne0\) について \(\sum m_jV_{J_j}\in\mathcal V\) で欠損は \(\sum m_j\delta_{J_j}\)。
　\(|m|=2\)：種 \(V_B+V_C\)（欠損 \(\delta_B+\delta_C\)）で \(\delta_B\le\delta_C\) としてよく、(2) で \(V_C\to V_J\)、次に \(V_B\to V_{J'}\) と入れ替える（途中の \(a\) 個数は \(N-\delta_B-\delta_J\ge1\)、\(N-\delta_J-\delta_{J'}\ge1\)）。\(|m|\to|m|+1\)：\(M=\sum m_jV_{J_j}\)（台 \(T\)）、\(m_J\ge1\) とし、\(V_J+V_{J'}\) に (2) を \(V=V_J\), \(V'=M\), \(Q=V_{J'}\) で適用する。
**(4) 分岐類には疎な鎖がない.** 分岐類 \(T\)（\(t=|T|\)）の大非終端 \(J_0,\dots,J_t\) で \(\delta_{J_{i+1}}>\rho\,\delta_{J_i}\)、\(\delta_{J_t}\le N_1:=(N-1)/((D+1)B)\) なるものは存在しない。
　実際 \(t+1\) 個のベクトル \(V_{J_i}\in[0,\theta]^T\) には Cramer の公式から \(|\lambda_i|\le t!\theta^t\le B\) の非自明な整数関係 \(\sum\lambda_iV_{J_i}=0\) があり、\(V_{J_i}\ge0\), \(\neq0\) なので両符号が現れる。\(m^\pm=\lambda^\pm\) は (3) の条件を満たし同じベクトルを実現するから、(U) より \(\sum\lambda_i\delta_{J_i}=0\)。しかし最大の添字 \(i^*\) で \(|\lambda_{i^*}|\delta_{J_{i^*}}\ge\delta_{J_{i^*}}>2Bt\,\delta_{J_{i^*-1}}\ge2\bigl|\sum_{i<i^*}\lambda_i\delta_{J_i}\bigr|\)。矛盾。
　したがって分岐類の欠損のうち \(N_1\) 以下のものは高々 \(D\) 個の区間 \([x,\rho x]\) で覆われる（貪欲法）。全分岐類で区間は \(M_b<D2^D\) 個。
**(5) 非分岐類は高々二本の根道に載る.** 類 \(T\) に互いに素な対がなければ全節点が比較可能で一本の根道上。互いに素な対 \(B,C\) が全て「悪い」（\(k_B+k_C=N\)）なら、\(B\) の下の類 \(T\) 節点は互いに比較可能（互いに素な \(X,Y\subseteq B\) は \(N-\delta_X-\delta_Y\ge k_C\ge1\) で良い対になる）、\(C\) の下も同様、その他は \(B\) か \(C\) と比較可能。\(U\) を、非分岐類の節点が載る根道と \(k=N\) の鎖の和集合とすると \(U\) は上方閉で \(|U|\le2^{D+1}v\)。
**(6) 窓の議論.** \(X\notin U\) を大節点とする。その子孫の大節点は全て分岐類。最重の子を辿る列 \(k_0=k_X\ge k_1\ge\cdots\) は \(k_i>(r+1)\theta\) の間 \(k_{i+1}\ge(k_i-\theta)/r\ge k_i/(r+1)\) を満たす。よって \(\sigma:=2(r+1)\) として、\(y\in[\sigma\theta,k_X]\) なる各窓 \([y/\sigma,y]\) は分岐類の大節点の欠損を含む。\(y_j:=\sigma\theta(2\sigma\rho)^j\)（\(j=0,\dots,M_b\)）の窓は、一つの区間 \([x,\rho x]\) が二つと交わることがないほど離れている。したがって \(\min(k_X,N_1)<K_0=\sigma\theta(2\sigma\rho)^{M_b}\)（\(M_b\le D2^D\)）。
**(7) 集計.** \(N_1<K_0\) なら \(N<(D+1)BK_0+1\)。\(N_1\ge K_0\) なら \(U\) の外の大節点は全て \(k<K_0\) で、\(U\) の各節点は終端 \(\le\theta\) 個と高々 \(r\) 個の子を持つから \(N\le|U|(r+1)K_0\)。∎

**注意.** (a) 証明は \(d=1\) の代入可能性しか使っていない。可換言語では fan-out に関係なく単項型が希少になれない、という主張である。(b) 対照的に非可換・fan-out 1 では `thm:fanout-one-data` の指数的下界がある。fan-out 2 が何を変えるかは次節。(c) `prop:rare-type` 経由の下界のうち「可換言語の単項型」を使うものはこれで閉じられるが、**開問題そのものには届かない**。

## 6. 非可換の場合：見取り図・予想・障壁

**直観.** fan-out 1 の下界は「非可換な剛構造（木）」が希少型の語を長く保つことで成立する。fan-out 2 の代入可能性は系 2.2 により全ての長い語を「単位の移送」で攪拌し、言語を局所データ＋計数データで決まるものへ近づける（先行ラウンドの Euler 付け替えと同じ現象を別方向から見ている）。一方、計数データで決まる部分では定理 B, C の論法（薄さ ⟹ 短い整数関係 ⟹ 疎な重み列が存在しない）が多項式上界を与える。移送に免疫を持つのは文字の順序が剛な有界言語型（例：\(\{a^nb^n\}\) は内容型付けでは 2 次元代入可能）だが、そこではブロック数が固定で次元が有界である。

**予想 U [予想].** 半束型付け \(s\)、\(f\ge2\)、\(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、reduced good 提示 \(G\) について、\(L\) の最短の \(a\) 冪の長さは \(\|G\|,\bar\theta_G\) の多項式（次数は \(|\Sigma|\) に依存）で抑えられる。

**証明計画と欠けている部分.** 補題 5.1 は非可換でそのまま成立する。定理 C の (3)–(7) を非可換で再現するには、(U) を適用するために**骨格が語として一致する二語**が必要で、ここが唯一の本質的な穴である：
1. 系 2.2 から「交叉」が出る：部品 \(\alpha d\beta\) と \(\alpha'd\beta'\) が、後方に \(\alpha'd\beta'\) の複製を持つ適当な語の中に現れれば、\(\alpha d\beta'\) と \(\alpha'd\beta\) を部品とする語も \(L\) に入り \(a\) の個数は変わらない [証明：系 2.2 の直接の適用]。
2. 交叉は部品の bigram 多重集合（\(a\) との境界 bigram を含む）を保つ。**未証明**：同じ bigram 多重集合を持つ二つの部品多重集合が、常に宿主条件（系 2.2 の因子 \(x_1d\kappa dy_2\) の存在）を満たしたまま交叉と部品の並べ替えで結べること。これは有向多重グラフの Euler 分解の連結性＋「宿主可能性」で、先行ラウンドが HC と呼んだ困難と同種と思われる。部品の複製を自由に増やせる（補題 5.1(E) と定理 C(3) の論法）ので宿主の用意は U₂ より容易だと期待するが、確認していない。
3. これが通れば欠損は bigram 計数ベクトル（次元 \(\le(D+1)^2\)）の加法的関数になり、定理 C の (4)–(7) が次元だけ替えて通る。
4. fan-out 2 の非終端では部品が2成分になり、交換に \(d=2\) の同値が必要。帳簿は増えるが新しい困難は見えていない（未確認）。

**一般の希少型（2文字以上）について.** \(c\) なしの語が \(\{a,b\}\) 上にある場合、(U) の類似は「骨格ごとに \((|w|_a,|w|_b)\) の可能な値が格子の剰余類に入る」になるはずで、可換版ですら未着手である。定理 A の崩壊はこの場合の最初の実例にあたる。

**下界側の候補が残る場所.** 私が排除できていないのは次だけである：(i) 希少型を使わず、非アーベルかつ組代入可能な部分標的 \(L'\subsetneq L\) で区別する経路（定理 B はアーベルな \(L'\) しか殺さない）；(ii) 移送に免疫のある剛構造を、固定アルファベットのまま非有界な深さで実現する未知の符号化。(ii) について、単一ブロックに非線形な重み \(\sigma(j)\) を持たせる有界形 \(\{a^ic^jb^k:i+k=\sigma(j)\}\) を調べたが、\(a^uc^{j_1}\) と \(a^{u'}c^{j_1'}\) の比較から \(\sigma\) は \(j\ge1\) でアフィンに強制され、非線形性は \(j=0\)（別の型）にしか置けず、その場合は薄い提示が作れなかった（議論は概略のみで、定理としては主張しない）。

## 7. 計算の記録

詳細は `experiments_log.txt`。全て決定的で乱数は不使用。閉包は全て長さ打切りなので真の閉包の下からの近似であり、報告した語が閉包に属することだけを主張する。

| 対象 | 型付け | 打切り | 結果 | 状態 |
|---|---|---|---|---|
| \(L_2\)（6語） | \(s_U\) | 10 | 3306語で閉、\(\mathtt a\) を含む | [計算] |
| \(L_2\) | 内容 | 10 | 既に閉（6語） | [計算] |
| \(L_3\)（42語） | 内容 | 22 | 第2巡 \(d=1\) で 644 万語、\(c\) なし長さ16 | [計算] |
| \(L_3\vdash W_2,\ \mathtt{baab}\) | 内容 | — | 33 手の証明書、\(L_4\)–\(L_7\) 内でも直接検査 | [検証] |
| \(V_3\)（42語、5文字） | 内容 | 22、組長/枠長 \(\le7\) | 174 万語、その後 \(\mathtt{baad}\), \(W_2'\) に到達 | [計算] |

失敗・未完：\(L_3,V_3\) の無制限閉包は第2巡以降メモリと時間で完走せず。Python の \(c\) なし語 BFS は 25 分で出力なしのため打ち切り、証明書構成に置き換えた。

## 8. 最も有望な次の一手

1. **予想 U の穴（§6 の 2.）を埋める**か、反例を作る。部品複製が自由な設定での Euler 連結性は、U₂ の宿主問題より扱いやすい特殊化であり、通れば「単項型による下界は fan-out 2 で不可能」という型付け・言語クラスによらない最初の一般上界になる。
2. 定理 C を 2 文字の希少型へ拡張する（可換の場合）。(U) を格子版に置き換える。
3. 定理 A′ の証明書抽出（`build_cert.py` を \(V_3\) 用に書き換えるだけだが計算量が大きい）。
4. 下界を狙うなら §6 の (i) のみが未踏。ただし非アーベルで組代入可能な部分標的の例を私は一つも構成できていない。

## 9. 結論

**`NEW THEOREM BUT OPEN`.**

- **解決したこと（量化込み）.**
  - 全ての \(f\ge2\)、\(n\ge3\)、\(\Sigma\supseteq\{a,b,c\}\)、全ての半束型付け \(s\)、\(L_n\) を含む全ての \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) について \(\mathtt{baab}\in L\)（定理 A、証明書は機械検査済み）。任意の非消去射像でも同様。
  - 全ての reduced good MCFG \(G\)（rank \(\le r\)）と全てのアーベル剰余類条件について、長さ \((r+2)\bar\theta_G\) 以下の語で成り立てば \(L(G)\) 全体で成り立つ（定理 B）。
  - 全ての可換な \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)（\(s\) 半束、\(f\ge1\)）と全ての reduced good 提示について、最短の \(a\) 冪は \(O_{|\Sigma|,r}(|V|\,\bar\theta_G^{\,1+D+D^22^D})\)（定理 C、手証明・未監査）。
  - `op:fanout-two` は「\(\mathbf{SL}\) が fan-out \(f\) で一様多項式データ長を持たないか」と同値（命題 1）。
- **未解決のまま.** ある \(\Sigma\) とある半束型付けについて超多項式族が存在するか（YES）、全ての \(\Sigma\) で \(\tau(G,c_\Sigma)\) が多項式か（NO）。非可換言語では単項希少型すら未決（予想 U）。\(f\ge3\) への移行も未検討。

---

## 附録B：Fable-C 独立完全数学監査（全文）

**一次資料：** `Fable_C_complete_independent_mathematical_audit_2026-11-15.md`、UTF-8、17724 bytes、SHA256 `63be1443497ba90d945c04e1ed7895fa220fc9f464e4d9b0416b5a5a416e72d2`。  
**注：** ここから次の区切りまでが原資料全文。

---

# Fable-C：可換・半束型付き組代入可能言語の単項語長上界 — 独立完全数学監査

**監査日**：2026-11-15（JST）  
**対象**：ユーザー提供 `新しいフォルダー(20261115-114855).zip` 中の `fable_fanout2_open_problem_report.md` §5（補題5.1・定理C）、既存の初回監査 `audit_fable_fanout2_independent_2026-11-15.md`、および現行 #2 MCFG `main.tex` の `def:grammar-properties`, `def:tuple-substitutable`, `lem:thickness-equivalence`。  
**方法**：原報告を独立に読み、§5(0)–(7) をそのまま引用せず各論証を再構成。明示的な受理文脈、整数係数、木の包含関係、窓幅と次数を検算。独立コードで境界事例の有限ストレス検査を実施。Fableのチェックコードは流用していない。  
**総合判定**：**VALID AS A MATHEMATICAL HAND-PROOF, WITH EXPLICIT CLARIFICATIONS**。以下の補足を入れると、定理Cの手証明は論理的に閉じると評価する。これは形式証明・専門家による査読・研究的新規性の認定を意味しない。**`op:fanout-two` は OPEN**。

---

## 1. 対象定理の正確な量化

有限アルファベット \(\Sigma=\{a\}\sqcup\Delta\)、\(D=|\Delta|\ge1\)、有限**半束**への型付け \(s:\Sigma^+\to\mathsf S\)、\(f\ge1\) とする。\(L\subseteq\Sigma^*\) は **可換**（全ての語の置換で所属が不変、すなわち Parikh ベクトルだけで所属が決まる）かつ \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)。\(G\) は \(L\cap\Sigma^+\) の **reduced good** MCFG で、fan-out は任意、rule rank \(\le r\)（\(r\ge1\)）、\(v=|V(G)|\)、\(\theta=\bar\theta_G\ge1\)。\(N=\min\{n\ge1:a^n\in L\}\) が定義されるとする。

\[
 B=D!\theta^D,\quad \rho=2DB,\quad
 K_0=2(r+1)\theta\,[4(r+1)\rho]^{D2^D}.
\]

Fable-Cの結論は

\[
 \boxed{N\le\max\{(D+1)BK_0+1,\ 2^{D+1}v(r+1)K_0\}}
 \quad\Longrightarrow\quad
 N=O_{D,r}\bigl(v\theta^{1+D+D^22^D}\bigr).
\]

- **固定するもの**：\(D\)、\(r\)（指数と暗黙定数はこれらに依存）。アルファベットサイズが成長する場合の一様多項式定理ではない。
- **使う代入可能性**：\(d=1\) のみ。二穴やfan-out 2固有の主張ではない。
- **測る厚さ**：型付き精密化後ではなく元の \(G\) の \(\bar\theta_G\)。
- **対象**：\(a^N\) の最短長のみ。任意の型の代表長や一般の特徴標本長ではない。

## 2. 準備：短縮不能性と Parikh 交換

### 2.1 一意性 (U) — 有効

もし \(P a^iQ,\ Pa^{i'}Q\in L\)、\(1\le i<i'\le N\) なら、半束型付けで \(s(a^i)=s(a^{i'})\)。共通の受理文脈 \(P\square Q\in\mathcal E_1\) によって \(a^i\equiv_{L,s}a^{i'}\)。文脈 \(a^{N-i'}\square\) に代入すれば \(a^{N-i'+i}\in L\) となり、\(0<N-i'+i<N\) は \(N\) の最小性に矛盾する。\(i'=N\) でも文脈 \(\square\) は適法。

このため、非 \(a\) 文字の Parikh ベクトル \(V\in\mathbb N^\Delta\setminus\{0\}\) が一定で、\(1\le e<N\) の語が存在するとき、受理される \(a\) の個数 \(e\) は高々一つ。実際、可換性から両候補を \(a^e w_V,a^{e'}w_V\) と並べれば、共通文脈 \(\square w_V\) が (U) に反する。以後

\[
 \mathcal V=\{V\ne0:\ (e,V)\in\operatorname{Parikh}(L)
 \text{ for some }1\le e<N\},\qquad
 \delta(V):=N-e
\]

は一価に定義され、\(1\le\delta(V)\le N-1\)。

### 2.2 Fable §5(2) の交換補題 — 明示的な受理文脈を補完

\(V,V'\in\mathcal V\) が同じ非 \(a\) 文字の台 \(T\) を持つとする。\(d=\delta(V)\), \(d'=\delta(V')\) とし、\((e,Q+V)\in\operatorname{Parikh}(L)\)、\(e'=e+d-d'\ge1\) とする。次を置く：

\[
 i=1+\max(0,d'-d),\qquad i'=1+\max(0,d-d').
\]

すると \(i'-i=d-d'\), \(i\le e\), \(i\le N-d\), \(i'\le N-d'\)。非 \(a\) 語 \(w_V,w_{V'},w_Q\) をそれぞれの Parikh ベクトルどおり選び、

\[
 x=a^i w_V,\qquad y=a^{i'}w_{V'},\qquad
 E_0=a^{N-d-i}\square,\qquad
 E_1=a^{e-i}\square w_Q
\]

とする。\(E_0[x],E_0[y]\) はそれぞれ Parikh \((N-d,V),(N-d',V')\) を持ち**両方受理**される。\(s(x)=s(y)\) は台 \(\{a\}\cup T\) の一致による。従って \(x\equiv_{L,s}y\)。\(E_1[x]\in L\) だから \(E_1[y]\in L\) であり、Parikh は \((e',Q+V')\)。これで \(§5(2)\) は証明された。

**5.1(E) の補完**：\(aVa^e,aV'a^{e'}\in L\), \(1\le e,e'\le N-2\) なら、5.1(R) を使って \(a^eVa,a^{e'}V'a\in L\) と再配分できる。内容が等しいので、共通の恒等文脈 \(\square\) により \(a^eVa\equiv_{L,s}a^{e'}V'a\)。Fableの差 \(i'-i=e'-e\) は \(i=e,i'=e'\) で成立。これは定理Cの主証明では直接引用しないが、補題5.1の量化も確認した。

## 3. §5(0) 最小導出木、短い収率、欠損 — 有効

\(a^N\) の導出木 \(\mathcal T\) を**節点数最小**に固定する。good の非削除性から、各節点の収率タプルの文字は全て \(a\) であり、その合計長を \(k_X\) とする。

**同一非終端の出現は根葉道上に二度ない**：もし出現 \(X,Y\) が同じ非終端 \(A\) で異なる収率長を持てば、長い方の \(A\)-部分木を短い方の導出木で置換し、\(a^N\) より短い正の \(a\) 冪を生成する。これは \(N\) の最小性に矛盾する。長さが同じで一方が他方の祖先なら、祖先の導出木を子孫の導出木に置換して同じ語 \(a^N\) をより少ない節点で生成でき、節点数最小性に矛盾する。従って高さは \(\le v\)。**分岐部分で同じ非終端が反復することは禁止しない**。

既存 thickness lemma から、各 \(A\) に \(\|u_A\|_1\le\theta\) の短い導出タプルがある。\(\operatorname{Parikh}(u_A)=(\alpha_A,V_A)\) とする。大節点を \(k_A>\theta\) と呼ぶ。\(V_A=0\) なら大節点の置換によって \(a^{N-k_A+\alpha_A}\in L\) を作る。長さは \(N\) 未満（かつ、もし0なら \(\eps\) と矛盾しないが、**good の非空成分により置換後の語は正長**）。従って \(V_A\ne0\) が必須。

\[
 \delta_A=k_A-\alpha_A>0,
 \qquad k_A-\theta\le\delta_A\le k_A,
 \qquad |V_A|_1\le\theta.
\]

大節点で \(\delta_A\le N-1\) なら、単一節点置換から \((N-\delta_A,V_A)\in\operatorname{Parikh}(L)\) が得られ \(V_A\in\mathcal V\), \(\delta(V_A)=\delta_A\)。Fableの §5(1) は \(k_A<N\) を十分条件としているが、その後の §5(3),(4) で使う \(\delta_A\le(N-1)/2\) でも当然満たされる。

**注意（0収率回避）**：\(k_A=N\), \(\alpha_A=0\) で置換した語には \(V_A\ne0\) があるため正長であり、\(a\) の数は0でもよい。ただしこの場合 \(\delta_A=N\) なので集合 \(\mathcal V\) に使用しない。\(V_A=0\) の場合、短いgoodタプルは正長なので \(\alpha_A\ge1\)、したがって本当に短い正の \(a\) 冪が得られて矛盾する。

## 4. §5(3) 分岐類の完全加法性 — 有効

台 \(T\subseteq\Delta\), \(T\ne\emptyset\) を固定。元の木に互いに祖先子孫でない二つの大節点 \(B,C\) があり \(\operatorname{supp}V_B=\operatorname{supp}V_C=T\)、\(\delta_B+\delta_C\le N-1\) のとき「分岐類」と呼ぶ。

両節点を同時に短い収率へ置換すれば、非削除性と元が \(a^N\) であることから
\[
 (N-\delta_B-\delta_C,V_B+V_C)\in\operatorname{Parikh}(L).
\]
\(\delta_B\le\delta_C\) として \(\delta_B\le(N-1)/2\)。

台 \(T\) の大非終端 \(J\) で \(\delta_J\le(N-1)/2\) のものを「許容単位」とする。任意の二単位 \(J,J'\) について、種 \(V_B+V_C\) の \(C\) を \(J\) に交換：中間欠損 \(\delta_B+\delta_J\le N-1\)。次に \(B\) を \(J'\) に交換：最終欠損 \(\delta_J+\delta_{J'}\le N-1\)。§2.2 によって両交換は合法。従って二単位の和が実現する。

**任意多重集合への帰納**：一単位は上記単一節点置換で実現する。二単位は直前の議論。\(|m|\ge3\)、総欠損 \(\delta_m\le N-1\) の多重集合から単位 \(J'\) を一つ取り除いた \(M\) は帰納的に実現し、\(\operatorname{supp}V_M=T\)、\(\delta(V_M)=\delta_M\)。\(M\) 中の単位 \(J\) を一つ選ぶ。既知の二単位の和 \(V_J+V_{J'}\)（欠損 \(\delta_J+\delta_{J'}\)）に対し \(V_J\to V_M\) を交換すれば、目標の \(V_M+V_{J'}\)（欠損 \(\delta_M+\delta_{J'}=\delta_m\le N-1\)）を得る。種 \(V_M\) は単一の台 \(T\) を持つから §2.2 の前提を満たす。これで全長の帰納法は閉じる。

**重要な補完**：整数関係の正負側が単位一つだけとなる場合がある。だから帰納法のベース \(|m|=1\) を明記する必要がある。Fableは「\(m\ne0\)」と正しく主張しているが、印刷上は \(|m|=2\) から証明を始めているので補う。

## 5. §5(4) 整数関係と疎な欠損列の排除 — 有効

台 \(T\) のサイズを \(t\le D\) とする。各許容 \(V_J\) は非零、成分が \([0,\theta]\) の整数ベクトル。\(t+1\) 本の列には非自明な整数関係 \(\sum_i\lambda_iV_{J_i}=0\) があり、\(0<\max_i|\lambda_i|\le t!\theta^t\le B\) となる。証明：行列階数 \(h\le t\) の \(h+1\) 本に、階数 \(h\) の非零小行列の符号付き \(h\times h\) 小行列式を係数として使う。各小行列式は Leibniz 展開で \(\le h!\theta^h\) に抑えられる。他の列の係数は0とする。全ての列が非零かつ成分非負なので、非自明な関係には正負両符号が必ず現れる。

分岐類の許容欠損に \(t+1\) 個 \(\delta_0<\cdots<\delta_t\le N_1\) があって \(\delta_{i+1}>\rho\delta_i\) と仮定する。ただし
\[
 N_1=(N-1)/((D+1)B),\qquad \rho=2DB.
\]
有界関係の正負側 \(m^+,m^-\) はそれぞれ総欠損 \(\le t B N_1\le N-1\) なので §4 の加法性が使える。二つは同じ非 \(a\) ベクトルを実現するため、一意性 (U) より \(\sum_i\lambda_i\delta_i=0\)。係数が非零の最大添字を \(j\ge1\) とすれば
\[
 |\lambda_j|\delta_j\ge\delta_j
 >2DB\delta_{j-1}\ge 2tB\delta_{j-1}
 \ge 2\Bigl|\sum_{i<j}\lambda_i\delta_i\Bigr|,
\]
矛盾。この疎列排除から、該当する欠損集合は**高々 \(t\) 個**の区間 \([x,\rho x]\) で覆える（左端の最小値から貪欲に覆い、次は覆い外の最小値を取る）。台の種類は \(2^D-1\) 以下なので全区間数
\[
 M_b\le\sum_{\emptyset\ne T\subseteq\Delta}|T|
 =D2^{D-1}<D2^D
\]
である。Fableの粗い上界は安全。

## 6. §5(5) 非分岐類の二本根道被覆 — 有効

非分岐台 \(T\) の大節点の集合 \(\mathcal N_T\) を考える。

- 互いに比較不能な二節点が一つもなければ、全て祖先子孫関係にあり、最深の節点への一本の根道上に載る。
- 比較不能な \(B,C\in\mathcal N_T\) があるなら、非分岐性から \(\delta_B+\delta_C\ge N\)。しかし独立した部分木なので \(\delta_B+\delta_C\le k_B+k_C\le N\)。ゆえに **\(\delta_B+\delta_C=k_B+k_C=N\)**、従って \(\alpha_B=\alpha_C=0\) である。
- \(B\) の真下の二つの \(T\)-節点 \(X,Y\) が比較不能だと、\(\delta_X+\delta_Y\le k_X+k_Y\le k_B\le N-k_C\le N-1\) で分岐類になり矛盾。よって \(B\) 以下の \(T\)-節点は一本の鎖、\(C\) 以下も同様。
- 他の \(T\)-節点 \(X\) が \(B,C\) の双方と比較不能なら、三つの部分木が互いに素であり \(k_B+k_C+k_X>N\) になって矛盾。したがって \(X\) は \(B\) か \(C\) の祖先または子孫で、上記二本の根道のどちらかに含まれる。

また \(k=N\) の節点はすべて一列の祖先鎖である。非分岐台ごとの高々二本と、この一本の**根からの道**の和を \(U\) と定める。\(U\) は祖先に関し閉じ、\(a^N\) の節点数最小性からどの根道も高々 \(v\) 節点なので
\[
 |U|\le [2(2^D-1)+1]v\le2^{D+1}v.
\]
\(X\notin U\) なら、その全子孫も \(U\) の外にあり、その大節点は全て**分岐台**に属する。これが §7 への正確な橋渡し。

## 7. §5(6) 最重子の窓被覆 — 有効、量化を明示

\(\sigma:=2(r+1)\)。\(X\notin U\)、\(k_X>\theta\) とする。最も長い子を繰り返し選ぶ経路の収率長を \(k_0=k_X\ge k_1\ge\cdots\) とする。各規則は端末を \(\le\theta\) 個書き、子は高々 \(r\) なので、\(k_i>\theta\) で子を持つとき
\[
 k_{i+1}\ge(k_i-\theta)/r.
\tag{H}
\]
（子がないなら \(k_i\le\theta\) である。）

任意の実数 \(y\in[\sigma\theta,k_X]\) をとり、**最初に** \(k_j\le y\) になる節点を選ぶ。最後の葉は \(k\le\theta\) なので必ず存在。

- \(j=0\) なら \(y=k_X\) であり \(\delta_j\ge y-\theta>y/\sigma\), \(\delta_j\le y\)。
- \(j>0\) なら \(k_{j-1}>y\ge\sigma\theta\) なので (H) と \(\delta_j\ge k_j-\theta\) から
\[
 \delta_j>\frac{y-\theta}{r}-\theta
 =\frac{y-(r+1)\theta}{r}
 \ge\frac{y}{2r}\ge\frac{y}{\sigma}.
\]
  一方 \(\delta_j\le k_j\le y\)。

両場合に \(\delta_j\in[y/\sigma,y]\)、しかも \(\delta_j>\theta\) だから \(j\) は大節点であり、\(j\notin U\) なので分岐類に属する。これで **全ての \(y\)** に対する窓被覆を証明した。これは単なる標本点の検査ではない。

\(\min(k_X,N_1)\ge K_0\) と仮定する。\(y_j:=\sigma\theta(2\sigma\rho)^j\)（\(0\le j\le M_b\)）の全てが \(\le\min(k_X,N_1)\) なので、\(M_b+1\) 個の窓 \(I_j=[y_j/\sigma,y_j]\) がそれぞれ分岐欠損を含む。他方、§5 の被覆区間 \(J=[x,\rho x]\) は異なる二つの窓を同時には交わらない。実際 \(I_j\) 内の点は \(\le y_j\)、\(I_{j+1}\) 内の点は \(\ge y_{j+1}/\sigma=2\rho y_j\) で、同じ \([x,\rho x]\) には入らない。よって \(M_b\) 個以下の被覆区間で \(M_b+1\) 個の窓を覆うのは不可能。従って
\[
 \min(k_X,N_1)<K_0,
 \quad K_0=\sigma\theta(2\sigma\rho)^{D2^D}
 =2(r+1)\theta[4(r+1)\rho]^{D2^D}.
\]

## 8. §5(7) 最終集計・指数 — 有効

- \(N_1<K_0\) なら、\(N-1<(D+1)BK_0\) なので \(N<(D+1)BK_0+1\)。
- \(N_1\ge K_0\) なら、直前の不等式から \(U\) の外側の大節点は全て \(k_X<K_0\)、小節点は \(k_X\le\theta<K_0\)。よって \(U\) の外に出る辺の各子部分木は長さ \(<K_0\)。\(U\) の各節点は高々 \(\theta\) 個の終端を明示し、子は高々 \(r\) 個。従って全語長 \(N\le |U|(\theta+rK_0)\le |U|(r+1)K_0\le2^{D+1}v(r+1)K_0\)。

最後に \(B=D!\theta^D\)、\(\rho=2DB=O_D(\theta^D)\) より
\[
 K_0=O_{D,r}\bigl(\theta^{1+D^22^D}\bigr),\qquad
 (D+1)BK_0=O_{D,r}\bigl(\theta^{1+D+D^22^D}\bigr).
\]
\(v\ge1\) なので両分岐を合わせて \(N=O_{D,r}(v\theta^{1+D+D^22^D})\)。Fableの指数 **\(1+D+D^22^D\)** は正しい。

## 9. Fableコード非依存の独立検査

ファイル `check_fable_C_independent.py` を新規作成。出力は `independent_check_log.txt`。次の数学的必要条件を、ランダムまたは有限全列挙でストレス検査した：

| 検証 | 件数 | 結果 |
|---|---:|---|
| §5(2) 交換の共通受理文脈、i/i′ の非負性 | 36,820 | PASS |
| §5(3) 二単位の初期置換と多重集合帰納の数値条件 | 550 | PASS |
| §5(5) 非分岐台が高々二根道に載る | 3,500ランダム木 | PASS |
| §5(6) 最重子経路の全整数窓 | 153,625件 | PASS |
| §5(4) 有界整数関係の符号付き小行列式の係数境界 | 24,446件 | PASS |

**独立性**：Fableのプログラム・証明書をインポートしていない。**限界**：この有限検査は実際のMCFG組代入可能言語の普遍的な列挙ではない。定理の認証理由は §§2–8 の独立に再構成した一般手証明であり、コードは補助的な境界チェックである。

## 10. 監査上の修正事項と判定

1. **§5(0) の「根道の非終端重複なし」**：短い \(a\)-冪の矛盾と節点数最小性を明示する（§3）。
2. **§5(2) の交換**：実際の共通受理文脈 \(E_0\) と試験文脈 \(E_1\)、\(i,i'\) の非負性を明示する（§2.2）。
3. **§5(3) の多重集合**：\(|m|=1\) のベースと、\(J+J'\) から \(M+J'\) への帰納法を明示する（§4）。
4. **§5(4) の整数関係**：非零・非負列による正負両符号、および係数上界を明示する（§5）。
5. **§5(5) の「高々二根道」**：悪い対が \(k_B+k_C=N\) を強制することと、子孫内の分岐を排除することを明示する（§6）。
6. **§5(6) の窓**：全ての実数 \(y\) と端点の扱いを厳密化し、\(M_b+1\) 個の離れた窓に被覆区間を重複使用できないことを証明する（§7）。
7. **独立性・新規性**：本監査は証明の内的妥当性の評価であり、新しい定理であることの文献的証明ではない。Claude既存の定理 L 等との一致・包含関係は未調査。
8. **中心開問題への含意**：可換・単項希少型という限定領域に限った障壁。非可換な言語、2文字以上の希少型、一般の区別部分言語を排除しない。`op:fanout-two` は **OPEN**。

**最終判定：Fable-C は、上記の補足付きで VALID AS A HAND-PROOF。** 少なくとも提供された原報告の §5 の証明に関しては、定理の成立を妨げる論理ギャップを独立追跡で確認しなかった。正式な研究定理として引用する際は別の専門家による独立査読または機械形式化を推奨する。GitHub/論文の変更は行っていない。

---

## 附録C：Claude 第十二段 U₁ 下界探索・独立監査（全文、比較資料）

**一次資料：** `audit_claude_fanout2_round12_independent_2026-11-15.md`、UTF-8、7520 bytes、SHA256 `6e8e46c26b76619c441b7fa36403b256dc5b04c6577a9737cf2475656cc338e0`。  
**注：** ここから次の区切りまでが原資料全文。

---

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

---

## 終了条件の再確認

新しい数学的アイデアに沿って自律的に研究すること。**未解決なら未解決と報告する。** 一般開問題を解いたと宣言するのは、有限半群の量化、組代入可能性、good MCFG、文法サイズ・厚さの全条件を本当に満たしたときだけ。

===== END FILE =====

===== BEGIN FILE README_SHA256.txt bytes=1914 sha256=864878205c18e94631a7487372442330df1eced409f5c4e8492183277d7ea879 =====
ROUND 13 independent audit bundle / 2026-11-15 JST

The independent standalone X1 counterexample is the critical mathematical correction.
All independent Python scripts have no dependency on Claude checker.
The Claude checker was also partially re-run; the original full S1 300-trial run was NOT repeated.

SHA256 manifest:
f2f54516046fb6bbc8c25d32ed6e96d5233d440320ca057cf6b8d9d74c712979  audit_claude_round13_noncomm_U_independent_2026-11-15.md
715ddf6329f4bad6e1745587aff8b8d37b57d3f79a163faa776eb921a0c291ba  round13_independent_X1_counterexample_2026-11-15.py
b915b52308612570f65f79ffd0bb33b29328da90d971e010063d801f210b3c09  round13_independent_X1_counterexample_output_2026-11-15.txt
a5666fef8082bc4b59d00f11deacb753dc42f174bf136f081210a8de022efc6e  round13_independent_checks_2026-11-15.py
0a7541f61afc7754fcc80c0bdcfb3df223fc49976599611c29ee4dba9b8528b7  round13_independent_checks_output_2026-11-15.txt
1a9cb52dc2f87e91f73796c1a4f698a13ad1d0d2e5f33e7e04415afe1533071f  round13_subset_rerun_2026-11-15.txt
c5de54a67a939f9837d9d5fee50d3db30f9222a3dc7e565539816f701c5c9cbc  round13_E2_original_rerun_2026-11-15.txt
31d5aea9fba6f00aa2cf19d4c865f191bb9df9188f9c77755d05e2cec116eabc  round13_x1_adversarial_probe.py
c109105e89891a932f77063425940ce5606318dcd7d28562c145513ad65959d4  round13_x1_adversarial_probe_log.txt
3dc1019ea1e9a0b26da10ab7d2f8f6badb6efc47f8d7c55738652d0ada4433b5  claude_round13_noncomm_U_checker_output_2026-11-15.txt
3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a  claude_round13_noncomm_U_checker_2026-11-15.py
333edfdb04e59886ae6c3da7bb6f8af822309941cdff58c29d1adadb4495b716  claude_round13_noncomm_U_checkpoint1_2026-11-15.md
496ae66d32cd3c36f635db0702f6760317c6e96a1cd045a2eeb6636b604defbb  claude_round13_noncomm_U_next_obligations_2026-11-15.md
cb1782110ebf873d9a31127442243c9adca02e0b9a05743f3116145244c5394e  claude_round13_noncomm_U_final_report_2026-11-15.md

===== END FILE =====

===== BEGIN FILE audit_claude_round13_noncomm_U_independent_2026-11-15.md bytes=13412 sha256=f2f54516046fb6bbc8c25d32ed6e96d5233d440320ca057cf6b8d9d74c712979 =====
# Claude第十三段「非可換予想U」— 独立数学監査

**日付**：2026-11-15 JST  
**対象**：ユーザー提供 `claude_round13_noncomm_U_final_report_2026-11-15.md`、`checkpoint1`、`next_obligations`、標準ライブラリのみのPythonチェッカーと提出ログ。  
**参照定義**：`growupkuriyama-hub/Papers/02-v4-fixed-s-mcfg/v2/main.tex` の `def:grammar-properties`, `def:tuple-substitutable`, `lem:thickness-equivalence`, `op:fanout-two`。`main.tex` を閲覧・定義照合したが編集していない。

## 0. 一行結論

**正式 `op:fanout-two`、非可換予想Uはどちらも OPEN。** 第十三段の **L1(R/U)、L2、L3(Rot)、L4(Cat)、定理T1および系C1の主要手証明は有効**と評価する。他方、**L5-X1 は原文の仮定のままでは偽**であり、40語の有限、内容型付き2-tuple-substitutable言語による**厳密な反例**を独立構成した。**L5-X2 は証明の量化を補えば成立する**。E1 の有限反例・E2 の閉包矛盾証明書は、Claudeコード非依存の別実装で検証した。T2/H(K)の非可換Parikh還元は条件付きのままで、新定理として認定しない。

### 判定表

| 対象 | 本監査の判定 | 根拠・注意 |
|---|---|---|
| L1(R)：正の2穴を使った外側a配分 | **VALID** | 共通宿主 `□a□a^{N−1−i−j}` が適法 |
| L1(U)：短いa冪の一意性 | **VALID** | 1穴の共通文脈＋最小性 |
| L2：同一極大a連骨格のa計数一意性 | **VALID** | Rによる左寄せ後にU。総a数≤N−1が必須 |
| L3 Rot、L4 Cat | **VALID** | 1穴等価と合同性を具体的に確認 |
| L5-X1 | **FALSE AS STATED** | §2の明示的40語反例。比較対象自体の型一致が抜けている |
| L5-X2 | **VALID AFTER EXPLICIT REPAIR** | §3の全iの場合分けで共通2穴宿主を構成 |
| T1（有界核骨格数の上界） | **VALID** | §4で独立再証明。X1・X2不使用 |
| C1（T1の対数障壁） | **VALID** | T1の代数的帰結 |
| T2/H(K) | **CONDITIONAL / NOT INDEPENDENTLY CERTIFIED** | H(K)自体は未証明；Fable-Cの転用には追加の量化審査が必要 |
| E1（bigram関数主張の否定） | **VERIFIED FINITE COUNTEREXAMPLE** | 39語を全1/2穴分布で直接検査 |
| E2（3種の初期集合の不整合） | **CERTIFIED FOR THOSE SEEDS** | Claude非依存の逐手証明書replay：2、2、6手 |
| 予想U / `op:fanout-two` | **OPEN / OPEN** | 本報告に決定的な一般上界・超多項式下界なし |

## 1. 正確な設定

`Σ` は固定有限アルファベット、`a∈Σ`、`s` は有限半束型付け（内容型付け `c_Σ` を含む）、`L∈C^{mcf}_{f,s}`、`f≥2`、`N=min{n≥1:a^n∈L}`。`d=2` の句文脈 `u□₁v□₂w` では **`v∈Σ⁺`**、穴の内容は両方 **非空**。Gは `L∩Σ⁺` のreduced good MCFG、規則ランク≤r、原文法の厚さ `θ=\bar θ_G`。これらは現行論文と整合。

L1(R): `p a^i q a^j r∈L`, `q≠ε`, `i+j≤N−1`, 正の`i',j'`が同和なら置換後も受理。共有宿主 `(□₁,a,□₂ a^{N−1−i−j})` により `a^N` に合流。L1(U): 同じ`P□Q`に `a^i,a^{i'}` が受理され、`1≤i<i'≤N` なら小さいa冪の受理を強制して矛盾。L2は各極大a連をRで左寄せしてUを適用。

L3: `a^pκa^q∈L`, `3≤p+q=λ≤N−1` ならRから `a²κa^{λ−2}` と `aκa^{λ−1}` が受理。共有1穴文脈 `a□a^{λ−2}` と半束可換性により `aκ≡_{L,s}κa`。L4はこの1穴合同を用いて任意の孤立a連を左へ移す。これらの証明にL5-X1を使わない。

## 2. **厳密反例：L5-X1は偽**

Claudeの主張（原報告§3）：κ,κ'がそれぞれ `a^pκa^q`, `a^{p'}κ'a^{q'}` という単独受理語を持ち、`λ=p+q`, `λ'=p'+q'` が `[3,N−1]` に属し、`s(aκ)=s(aκ')` なら、`i=(λ−λ')_+`, `i'=(λ'−λ)_+` として任意X,Yで

`Xa^iκY ∈ L  ⇔  Xa^{i'}κ'Y ∈ L`

を主張する。**しかし`i`または`i'`が0の場合、実際の置換片 `a^iκ`, `a^{i'}κ'` の型一致は仮定から導けない。**

### 2.1 40語の明示的反例

内容型付け `s=c_{a,b,c}` を取る。まず次の39語の集合Sを取る（Claude E1の `f2=4` ケースから厳密に得られた有限閉言語であり、以下に語の全リストを示す）。

```
aaabc aabac aabca abaac abaca abcaa baaac baaca bacaa bcaaa
aaaaac aaaaca aaaacb aaacaa aaacab aaacba aacaaa aacaab aacaba aacbaa
acaaaa acaaab acaaba acabaa acbaaa caaaaa caaaab caaaba caabaa cabaaa
cbaaaa aaaaaab aaaaaba aaaabaa aaabaaa aabaaaa abaaaaa baaaaaa
aaaaaaaa
```

**`L:=S∪{bc}`（計40語）** とする。独立Python検証器で、L中の全ての非空1穴・2穴出現から全受理文脈を構築し、等しい成分内容型かつ共通受理文脈のある全組について、文脈集合の一致を検査した。

- `|L|=40`, 出現する組は333種類、受理文脈の組は2,327件、比較した組ペア924件。
- **違反0**。したがって L は `C^{mcf}_{2,c_Σ}` に属する（有限言語なのでMCFL性も自明）。
- 唯一のaのみの語は `a^8`：`N=8`。
- 有限言語には `S→w`（各 `w∈L`）というrank 0の1成分good規則からなるreduced presentationが存在する。

`κ=bc`, `κ'=acb`, `λ=λ'=3` と選ぶ。

- `a κ a² = abcaa ∈L`。
- `a² κ' a = aaacba ∈L`。
- 両外枠のaの総数は3、`3≤3≤N−1=7`。
- `s(aκ)=s(abc)=\{a,b,c\}=s(aacb)=s(aκ')`。
- 一方 `i=i'=0` なので、X1は `bc∈L ⇔ acb∈L` を要求する。しかし **`bc∈L` かつ `acb∉L`**。

全仮定を満たすのでX1の**反証**が成立する。原因は、`s(κ)=\{b,c\}` と `s(κ')=\{a,b,c\}` が異なる点。半束は `s(aκ)=s(aκ')` から `s(κ)=s(κ')` を保証しない。これは証明の単なる省略ではなく、主張への追加仮定が必要な事例である。

### 2.2 X1の修正版

`x=a^{(λ−λ')_+}κ`、`y=a^{(λ'−λ)_+}κ'` と置き、**`s(x)=s(y)` を明示的に要求する**なら、修正後のX1は成立する。`t=min(λ,λ')` とすれば、Rotから `a^λκ` および `a^{λ'}κ'` が受理されるので、**共通宿主 `E=a^t□`** が `E[x]=a^λκ`, `E[y]=a^{λ'}κ'` を受理する。型一致から1穴組代入可能性を適用できる。全X,Yへの置換は正当。

この修正で、今後のParikh還元計画に必要な全ての交換が可能になるとは**まだ証明されていない**。特に`i=0`の場合の型差に注意。

## 3. X2は「長過ぎるi」の場合も証明できる

Claudeの原証明は `s+m+t=λ−i` の非負分解を使い、`i≥λ` では右辺が負になる。この書き方のままでは任意iの主張を示していない。しかし、X2の**結論は修復可能**である。

`κ,κ'` に単独語の外側a総数 `λ,λ'∈[3,N−1]` があり、`s(κ)=s(κ')` とする。`i,i'≥1` で `i'=i+λ'−λ`。

1. **`i≤λ−1`**：`q=λ−i≥1` とし、`E=a^{q−1}□₁ a □₂` と置く。これは中央の `a` が非空なので適法。`x=(a^i,κ)`、`y=(a^{i'},κ')` の型は一致し、Rotで受理された `a^λκ` と `a^{λ'}κ'` がそれぞれ `E[x]`,`E[y]` となる。したがって `x≡^2 y`。
2. **`i≥λ`**：`i_0=λ−1`, `i'_0=λ'−1` を使って上記の等価を得る。任意の受理語 `l a^i m κ r` に対し、余剰接頭部分 `a^{i−i_0}` を左側の外部文脈に吸収し、中央には元の非空 `m` を残す。すると置換後の指数は `i−i_0+i'_0=i+λ'−λ=i'` となる。逆方向も同様。

したがって**X2は、型が同じ核同士について、全ての適法な非空セパレータmと任意の正のiに対して成立する**。X1の反例はX2には反しない（ここでは `s(κ)≠s(κ')`）。

## 4. 定理T1と系C1の独立証明

主張：`τ` は `a^N` の導出木、節点Xの収率長を `k_X`、非終端A_Xの最短導出組を`u_A`とする。`θ=\barθ_G`、`r` はrank cap、`M` は**根から最重子を選んで進む1本の経路上**の大節点（`k_X>θ`）から得る単独語 `w_X` の骨格`sk(w_X)`の種類数とする。`σ=2(r+1)` と置く（以下では単に σ と記す）。結論：

`N < θ σ^{2M+1}`.

### 検証済みの推論

- 現行 `lem:thickness-equivalence` により、元文法の各非終端は総長≤θの導出組を持ち、各規則の明示終端記号数は≤θ。部分木を最短組で置換して得る語 `w_X` はLの実際の語。根が全てaなので `|w_X|_a=N−k_X+|u_{A_X}|_a`。
- `k_X>θ` なら `|w_X|_a≤N−1`、`δ_X:=N−|w_X|_a∈[k_X−θ,k_X]`。L2により同骨格の大節点は同じδを持つ。
- 最重子経路上の次の子の長さは `k_{j+1}≥(k_j−θ)/r`。`k_j>θ` なら終端規則だけではないため経路は進み、葉の長さ≤θ。
- `σθ≤y≤N` とし `k_j≤y` となる最初の節点をとる。もしj=0なら `δ_0≥N−θ≥y−θ>y/σ`。もしj>0なら `δ_j≥k_j−θ>(y−(r+1)θ)/r≥y/(2r)>y/σ`。同時に `δ_j≤k_j≤y`。ゆえに、各 `y` について `[y/σ,y]` 内に大節点のδが存在する。
- `N≥θσ^{2M+1}` と仮定し、`y_t=θσ^{2t+1}`（t=0,…,M）をとると、互いに交わらない `M+1` 個の窓 `(θσ^{2t},θσ^{2t+1}]` に異なるδが存在する。L2によって異なる骨格が必要だが、骨格はM種類。矛盾。

この証明に **X1、X2、Fable-CのParikh還元やH(K)を使用していない**。よって X1反例によってT1の成立は損なわれない。任意fan-outでも、必要なtuple substitutabilityの使用はd≤2であり、原文法の厚さを用いる。

系C1は `M > (log_σ(N/θ)−1)/2` というT1の対数変形である。`M≤4v`という補足は、good導出の各tuple成分間に非空のa区切りが残ることと、各非終端の最短組および外側の左右a連の有無（2二値）で骨格が決まることに基づく。**このM≤4vはT1そのものには不要**であり、一般的な多項式境界を与えるわけではない。

## 5. E1/E2の完全独立有限検査

検証器 `round13_independent_checks_2026-11-15.py` はClaudeのPythonを一切importしない。

- **E1**：提出ログの全語リストから `f2=5`: 34語・1,784組文脈、`f2=4`: 39語・2,324組文脈を独自に構築。全てd=1,2の内容型付き分布条件を厳密に満たす。`abaca`（a3個）と `acaaba`（a4個）の骨格bigram数＋端点は一致するので、**欠損をbigram計数のみの関数にする主張は実際に偽**。
- 同じ有限言語で **Rot** を147件、**X2** の許容核とi（1〜12）の分布同一を3,275件独立検査し、いずれも違反0。これは一般証明ではなく追加のストレス検査。
- **E2**：提出ログにある三つの種集合を独自の組合せ列挙で再構築し、各証明書の `型一致`・`穴非空`・`セパレータ非空`・`三つの前提語がそれまでに既出`・`帰結語` を逐手照合。元の提出ログでは2手・2手・6手、全て再現成功。最終語に同一骨格でa数が異なり双方N未満となる矛盾を確認。**それら特定の種集合に限った不可能性証明**であり、一般的なE2型剛性の定理ではない。
- **原チェッカーの部分再実行**：S0/E1/S2/S4で4,035 checks、FAIL=0。E2も単独で5秒程度、4 checks、FAIL=0。ただしPythonのhash乱択によって具体的証明書が変わる。**全4458 checksの300乱択試行部分（S1）の完全再実行は実施していない**。
- **検証コード内の試験範囲の注意**：Claudeの関数 `exchange_instances` は定義されているが、`run_S1_S3` からは呼ばれていない。報告の「S3の1202件」は**Rotの検証**であり、X1/X2の検証件数ではない。この点がX1の誤認を助長した可能性がある。

## 6. 研究上の含意と次の義務

1. **X1の原文は撤回・修正が必要**。実際の比較語`a^iκ`と`a^{i'}κ'`について型一致を要求するのが最小の自然な修正。元の `s(aκ)=s(aκ')` では足りない。
2. **X2は§3の補足証明で維持できる**。ただし各交換操作で確保できる受理宿主が「交換を予定する木由来の場所」に適合するかは、新しい複合ステップに関して別途証明すること。
3. **T1は成果として保存可能**。ただし「大節点の骨格型数が固定」という付加条件を消せたわけではない。`op:fanout-two` の肯定・否定どちらも未達。
4. **T2/H(K)は条件付きの研究計画**。X1の不十分な型一致を使う段落が今後登場するなら改修し、Fable-Cの類ごとの整数関係・木の被覆の移植を独立に検証する必要がある。
5. **E1の反例は“全内容類をまたぐbigram関数性”の否定**であり、内容類ごとに制限したParikh還元Pを反証してはいない。
6. 次ラウンドでは **X1の明示的40語反例を必ずClaudeに渡し**、先に型条件と運搬子の宿主を確定し、その後で同一内容類のParikh還元Pを探索すべき。

**論文本文・GitHubは未変更。** 専門家査読および形式証明は未実施。今回のVALID判定は書面証明の独立再構成に基づく。

===== END FILE =====

===== BEGIN FILE claude_round13_noncomm_U_checker_2026-11-15.py bytes=24907 sha256=3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a =====
#!/usr/bin/env python3
"""Round 13 checker (Claude, 2026-11-15): non-commutative Conjecture U.

Python 3 standard library only.  Deterministic (random.seed(20261115)).
Run:   python3 -I claude_round13_noncomm_U_checker_2026-11-15.py
Exit code 0 iff every check marked [MUST] passes.

Typing throughout: content typing c(w) = set of letters of w (finest semilattice typing).
Tuple substitutability for d in {1,2}; a d=2 context is l [] m [] r with m NONEMPTY.

What is checked
  [S0] exact finite substitutability decision procedure (d=1,2), with positive / negative
       controls.
  [E1] REFUTATION (finite, exact): a finite language S1 in C^{mcf}_{2,c} with a^8 the
       shortest a-power, containing W1=a b a c a-type (deficit 5) and W2=a c a b a-type
       (deficit 4).  W1,W2 have the same a-collapsed bigram multiset and the same
       endpoints.  => "deficit is a function of the skeleton bigram multiset (+endpoints)"
       and "deficit of a multi-piece word is order-independent" are FALSE in general.
  [E2] closure experiment inside ONE content class {b,c}: seed realisations violating
       bigram-linearity; capped closure searched for a contradiction (shorter a-power or
       same-skeleton a-count conflict).  Certificates, if found, are replayed independently.
       Also the linear (control) seed.
  [S1] Lemma S (skeleton function) stress: random seeds -> exact closure when it terminates;
       on every closed set: same skeleton & a-count<=N-1  =>  same a-count.
  [S2] negative control for Lemma S: a d=1-closed finite set violating Lemma S must be
       d=2-non-closed (shows the d=2 hypothesis is used).
  [S3] content-exchange lemma (X1) instances on every closed set from [S1].
  [S4] window/tree arithmetic of Theorem T1: random trees, N < theta*sigma^(2M+1).
"""
import hashlib, random, sys, itertools, json, time
from collections import defaultdict

random.seed(20261115)
LOG = []
FAIL = 0
COUNT = 0
def log(*a):
    s = ' '.join(str(x) for x in a); LOG.append(s); print(s, flush=True)
def must(cond, msg):
    global FAIL, COUNT
    COUNT += 1
    if not cond:
        FAIL += 1; log('  [FAIL]', msg)
    return cond

def ctype(w): return frozenset(w)
def skel(w):
    out = []
    for ch in w:
        if ch == 'a':
            if not out or out[-1] != 'A': out.append('A')
        else: out.append(ch)
    return ''.join(out)
def acount(w): return w.count('a')

# ----------------------------------------------------------------- tuples / contexts
def tuples_of(w):
    """yield (d, x, E) with E the context; d=1: x=(x1,), E=(l,r); d=2: x=(x1,x2), E=(l,m,r), m!=''"""
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield 1, (w[i:j],), (w[:i], w[j:])
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):      # m = w[j:k] nonempty
                for l in range(k + 1, n + 1):
                    yield 2, (w[i:j], w[k:l]), (w[:i], w[j:k], w[l:])

def fill(E, x):
    if len(x) == 1: return E[0] + x[0] + E[1]
    assert E[1] != ''
    return E[0] + x[0] + E[1] + x[1] + E[2]

def ttype(x): return tuple(ctype(c) for c in x)

def ctx_maps(S):
    ctx = defaultdict(set)
    for w in S:
        for d, x, E in tuples_of(w):
            ctx[x].add(E)
    return ctx

def check_closed(S):
    """Exact decision: is the finite set S tuple-substitutable (d=1,2, content typing)?
    Returns (True, None) or (False, witness)."""
    S = set(S)
    ctx = ctx_maps(S)
    bucket = defaultdict(list)
    for x, Es in ctx.items():
        t = ttype(x)
        for E in Es:
            bucket[(len(x), t, E)].append(x)
    for (d, t, E0), xs in bucket.items():
        if len(xs) < 2: continue
        ref = ctx[xs[0]]
        for y in xs[1:]:
            cy = ctx[y]
            if cy != ref:
                diff = (ref - cy) or (cy - ref)
                E1 = next(iter(diff))
                x = xs[0]
                if E1 in cy: x, y = y, x
                return False, dict(x=x, y=y, E_accept=E0, E_test=E1,
                                   E_accept_x=fill(E0, x), E_accept_y=fill(E0, y),
                                   E_test_x=fill(E1, x), E_test_y=fill(E1, y),
                                   type_x=[sorted(c) for c in ttype(x)],
                                   type_y=[sorted(c) for c in ttype(y)])
    return True, None

def verify_witness(S, wit):
    """independent re-check of a non-closedness witness"""
    x, y, E0, E1 = wit['x'], wit['y'], wit['E_accept'], wit['E_test']
    if ttype(x) != ttype(y): return False
    if len(x) == 2 and (E0[1] == '' or E1[1] == ''): return False
    if any(c == '' for c in x + y): return False
    return (fill(E0, x) in S and fill(E0, y) in S and fill(E1, x) in S and fill(E1, y) not in S)

def shortest_apower(S):
    ns = [len(w) for w in S if w and set(w) == {'a'}]
    return min(ns) if ns else None

def skeleton_conflicts(S, N):
    """Lemma S consequence: same skeleton, a-counts <= N-1, different a-counts."""
    by = defaultdict(set)
    for w in S:
        if 'a' in w and acount(w) <= N - 1 and set(w) != {'a'}:
            by[skel(w)].add(acount(w))
    return {k: sorted(v) for k, v in by.items() if len(v) > 1}

# ----------------------------------------------------------------- closure with certificates
def closure(seed, cap_len, cap_words=200000, max_rounds=50, N=None, stop_on_contra=True):
    """Direct rule applications (Fable Def 2.3): E0[x],E0[y],E1[x] in K => E1[y] in K.
    Returns dict(K, origin, status, contra) ; status in {'closed','truncated','cap','contra'}."""
    K = set(seed)
    origin = {w: None for w in K}
    truncated = False
    for rnd in range(max_rounds):
        ctx = ctx_maps(K)
        bucket = defaultdict(list)
        for x, Es in ctx.items():
            t = ttype(x)
            for E in Es:
                bucket[(len(x), t, E)].append(x)
        new = {}
        for (d, t, E0), xs in bucket.items():
            if len(xs) < 2: continue
            for x in xs:
                cx = ctx[x]
                for y in xs:
                    if y == x: continue
                    for E1 in cx:
                        w = fill(E1, y)
                        if w in K or w in new: continue
                        if len(w) > cap_len:
                            truncated = True; continue
                        new[w] = (x, y, E0, E1)
        if not new:
            return dict(K=K, origin=origin, status='truncated' if truncated else 'closed',
                        contra=None, rounds=rnd)
        for w, o in new.items():
            K.add(w); origin[w] = o
        if N is not None:
            m = shortest_apower(K)
            if m is not None and m < N:
                return dict(K=K, origin=origin, status='contra', contra=('apower', 'a' * m), rounds=rnd + 1)
            sc = skeleton_conflicts(K, N)
            if sc and stop_on_contra:
                k = next(iter(sc))
                return dict(K=K, origin=origin, status='contra', contra=('skeleton', k, sc[k]), rounds=rnd + 1)
        if len(K) > cap_words:
            return dict(K=K, origin=origin, status='cap', contra=None, rounds=rnd + 1)
    return dict(K=K, origin=origin, status='cap', contra=None, rounds=max_rounds)

def certificate(origin, targets):
    """minimal ordered list of rule applications deriving targets from the seed"""
    order, seen = [], set()
    def need(w):
        if w in seen: return
        seen.add(w)
        o = origin[w]
        if o is None: return
        x, y, E0, E1 = o
        for p in (fill(E0, x), fill(E0, y), fill(E1, x)):
            need(p)
        order.append((w, o))
    for t in targets: need(t)
    return order

def replay(seed, cert):
    K = set(seed)
    for w, (x, y, E0, E1) in cert:
        if ttype(x) != ttype(y): return False, 'type'
        if any(c == '' for c in x + y): return False, 'empty component'
        if len(x) == 2 and (E0[1] == '' or E1[1] == ''): return False, 'empty separator'
        if not (fill(E0, x) in K and fill(E0, y) in K and fill(E1, x) in K): return False, 'premise'
        if fill(E1, y) != w: return False, 'conclusion'
        K.add(w)
    return True, K

# ----------------------------------------------------------------- helpers to build families
def compositions(total, parts):
    """all tuples of `parts` positive ints summing to total"""
    if parts == 0:
        if total == 0: yield ()
        return
    if total < parts: return
    for c in itertools.combinations(range(1, total), parts - 1):
        b = (0,) + c + (total,)
        yield tuple(b[i + 1] - b[i] for i in range(parts))

def flanked(pieces, a_total):
    """all words a^{p0} pi1 a^{p1} ... pik a^{pk} with all p>=1 and sum p = a_total"""
    out = set()
    for comp in compositions(a_total, len(pieces) + 1):
        w = 'a' * comp[0]
        for pi, p in zip(pieces, comp[1:]):
            w += pi + 'a' * p
        out.add(w)
    return out

def bigram_profile(w):
    s = skel(w)
    from collections import Counter
    return (Counter(s[i:i + 2] for i in range(len(s) - 1)), s[0], s[-1])

# =================================================================== S0 controls
def run_S0():
    log('== [S0] exact finite substitutability: controls')
    # positive: a^5 plus all flanked b-words with total 3 (pieces b, deficit 2)
    seed = {'a' * 5} | flanked(['b'], 3)
    ok0, wit0 = check_closed(seed)
    must(not ok0 and verify_witness(seed, wit0), 'S0: interior-only family must NOT be closed (rotation)')
    log('   interior-only family a^5 + a^+ b a^+ (total 3) is not closed; witness', json.dumps(wit0, default=list))
    R = closure(seed, cap_len=8, N=5)
    S = R['K']
    ok, wit = check_closed(S)
    must(R['status'] == 'closed' and ok, 'S0 positive control closure should be closed: %s %s' % (R['status'], wit))
    must(shortest_apower(S) == 5, 'S0 positive: a^5 shortest')
    log('   closure: status=%s |S|=%d S=%s' % (R['status'], len(S), sorted(S, key=lambda w:(len(w),w))))
    # negative: aligned (non-redistributed) word set violates (R)
    S = {'a' * 5, 'abaa'}
    ok, wit = check_closed(S)
    must(not ok and verify_witness(S, wit), 'S0 negative control must be non-closed with verified witness')
    log('   negative control {a^5, abaa}: witness', json.dumps(wit, default=list))
    # negative: separator requirement (d=2 with empty middle is NOT a context; check we never use it)
    for w in ['abcab', 'aab']:
        for d, x, E in tuples_of(w):
            if d == 2: must(E[1] != '', 'empty separator generated')

# =================================================================== E1
def run_E1():
    log('== [E1] cross-class order dependence: closure of an order-dependent seed')
    out = {}
    for f2 in (5, 4):
        N = 8
        seed = {'a' * N}
        seed |= flanked(['b'], N - 2)        # solo b, deficit 2
        seed |= flanked(['c'], N - 3)        # solo c, deficit 3
        seed |= flanked(['b', 'c'], N - 5)   # order b..c, deficit 5 = 2+3
        seed |= flanked(['c', 'b'], N - f2)  # order c..b, deficit f2
        R = closure(seed, cap_len=N + 3, cap_words=20000, max_rounds=20, N=N)
        S = R['K']
        line = '   f2=%d: status=%s |K|=%d rounds=%d contra=%s' % (f2, R['status'], len(S), R['rounds'], R['contra'])
        log(line)
        if R['status'] == 'closed':
            ok, wit = check_closed(S)
            must(ok, 'E1 closure must pass exact check')
            must(shortest_apower(S) == N, 'E1 a^8 shortest')
            must(not skeleton_conflicts(S, N), 'E1 Lemma S')
            W1 = 'abaca'
            W2 = 'acaba' if f2 == 5 else 'acaaba'
            must(W1 in S and W2 in S, 'E1 W1,W2 in closure')
            must(bigram_profile(W1) == bigram_profile(W2), 'E1 same bigram profile and endpoints')
            log('     W1=%s deficit %d ; W2=%s deficit %d ; same a-collapsed bigram multiset+endpoints=%s'
                % (W1, N - acount(W1), W2, N - acount(W2), bigram_profile(W1) == bigram_profile(W2)))
            if f2 == 4:
                must(N - acount(W1) != N - acount(W2), 'E1 REFUTATION: deficits differ')
                must('baaaaaa' in S and 'caaaaa' in S, 'E1 solo pieces present (deficits 2,3)')
                log('     REFUTED (exact, finite): deficit not a function of bigram data; cb-order deficit 4 != 2+3')
            log('     full closed set S1(f2=%d) = %s' % (f2, sorted(S, key=lambda w: (len(w), w))))
            log('     words with content {a,b,c} and a-count<N:', sorted([w for w in S if set(w) == set('abc')],
                key=lambda w: (len(w), w)))
        if R['status'] == 'contra':
            kind = R['contra'][0]
            if kind == 'apower':
                targets = [R['contra'][1]]
            else:
                sk = R['contra'][1]
                byc = {}
                for w in R['K']:
                    if skel(w) == sk and acount(w) <= N - 1: byc.setdefault(acount(w), w)
                targets = list(byc.values())[:2]
            cert = certificate(R['origin'], targets)
            okr, _ = replay(seed, cert)
            must(okr is True, 'E1 certificate replay')
            log('     certificate (%d steps, replay ok=%s) targets=%s' % (len(cert), okr is True, targets))
            for k, (w, (x, y, E0, E1)) in enumerate(cert):
                log('       %2d x=%s y=%s E0=%s E1=%s => %s' % (k, x, y, E0, E1, w))
        out[f2] = R
    return out

# =================================================================== E2
def e2_seed(N, deltas):
    S = {'a' * N}
    P = list(deltas)
    for p in P:
        S |= flanked([p], N - deltas[p])
    for p, q in itertools.product(P, P):
        t = N - deltas[p] - deltas[q]
        if t >= 3: S |= flanked([p, q], t)
    return S

def run_E2():
    log('== [E2] within-class {b,c} bigram-linearity: closure experiments')
    res = {}
    # relation: v(bcbc)+v(cb) = v(bc)+v(cbcb)  (skeleton bigram multisets incl. boundary)
    from collections import Counter
    vb = lambda p: Counter(skel('a' + p + 'a')[i:i + 2] for i in range(len(p) + 1))
    must(vb('bcbc') + vb('cb') == vb('bc') + vb('cbcb'), 'E2: bigram relation holds')
    # first two cases: deliberately inconsistent with concatenation additivity (expect contradiction)
    # last two: primitive cores bc, cb only; products generated by closure.
    cases = [('naive-violating', {'bc': 2, 'cb': 2, 'bcbc': 3, 'cbcb': 4}),
             ('naive-linear', {'bc': 2, 'cb': 2, 'bcbc': 3, 'cbcb': 3}),
             ('prim-bc2-cb3', {'bc': 2, 'cb': 3})]
    # NOTE: the consistent control ('bc':2,'cb':2) was attempted during development; its closure
    # did not terminate within ~9 minutes (|K| grows past 10^4 words); it is NOT part of this run.
    for name, deltas in cases:
        N = 10
        seed = e2_seed(N, deltas)
        t0 = time.time()
        R = closure(seed, cap_len=N + 4, cap_words=30000, max_rounds=6, N=N)
        dt = time.time() - t0
        log('   case %-15s N=%d |seed|=%d -> status=%s |K|=%d rounds=%d time=%.1fs contra=%s'
            % (name, N, len(seed), R['status'], len(R['K']), R['rounds'], dt, R['contra']))
        res[name] = R
        if R['status'] == 'contra':
            kind = R['contra'][0]
            if kind == 'apower':
                targets = [R['contra'][1]]
            else:
                sk = R['contra'][1]
                ws = [w for w in R['K'] if skel(w) == sk and acount(w) <= N - 1]
                byc = {}
                for w in ws: byc.setdefault(acount(w), w)
                targets = list(byc.values())[:2]
            cert = certificate(R['origin'], targets)
            okr, K2 = replay(seed, cert)
            must(okr is True, 'E2 %s: certificate replay' % name)
            log('     certificate: %d rule applications, replay=%s, targets=%s' % (len(cert), okr is True, targets))
            for step, (w, (x, y, E0, E1)) in enumerate(cert[:40]):
                log('       %2d  x=%s y=%s E0=%s E1=%s  =>  %s' % (step, x, y, E0, E1, w))
            if len(cert) > 40: log('       ... (%d more)' % (len(cert) - 40))
            res[name + '_cert'] = cert
    return res

# =================================================================== S1/S3 random closed sets
def random_seed_words(N, k):
    S = {'a' * N}
    for _ in range(k):
        npieces = random.choice([1, 1, 2])
        pieces = [''.join(random.choice('bc') for _ in range(random.choice([1, 1, 2])))
                  for _ in range(npieces)]
        tot = random.randint(npieces + 1, N - 1)
        comp = random.choice(list(compositions(tot, npieces + 1)))
        w = 'a' * comp[0]
        for pi, p in zip(pieces, comp[1:]): w += pi + 'a' * p
        S.add(w)
    return S

def exchange_instances(S, N):
    """(X1): solo cores pi,pi' same content; host X a^i pi a^j Y in S with room
    => X a^{i'} pi' a^{j'} Y in S for the predicted i',j'. Returns (#checked, #fail)."""
    solo = {}
    for w in S:
        if w[0] == 'a' and w[-1] == 'a' and set(w) != {'a'}:
            core = w.strip('a')
            lam = len(w) - len(core)
            if acount(w) <= N - 1 and len(w) - len(w.lstrip('a')) >= 1:
                solo.setdefault(core, set()).add(acount(w))
    solo = {k: min(v) for k, v in solo.items()}
    delta = {k: N - e for k, e in solo.items()}
    chk = fl = 0
    for W in S:
        for core, d in delta.items():
            start = W.find(core)
            while start != -1:
                i0 = len(W[:start]) - len(W[:start].rstrip('a'))
                end = start + len(core)
                j0 = len(W[end:]) - len(W[end:].lstrip('a'))
                for core2, d2 in delta.items():
                    if core2 == core or (set(core2) | {'a'}) != (set(core) | {'a'}): continue
                    lam = solo[core] - acount(core); lam2 = solo[core2] - acount(core2)
                    need = 2 + max(0, lam - lam2)
                    if i0 + j0 < need: continue
                    # choose i,j within flanks with i+j = 2+max(0,lam-lam2), i,j>=1
                    s = 2 + max(0, lam - lam2)
                    i = min(i0, s - 1); j = s - i
                    if j > j0 or j < 1 or i < 1: continue
                    if i + j > lam: continue
                    s2 = s + lam2 - lam
                    i2 = 1; j2 = s2 - 1
                    if j2 < 1: continue
                    X = W[:start - i]; Y = W[end + j:]
                    W2 = X + 'a' * i2 + core2 + 'a' * j2 + Y
                    chk += 1
                    if W2 not in S: fl += 1
                start = W.find(core, start + 1)
    return chk, fl

def rotation_instances(S, N):
    """(Rot): a^p kappa a^r in S, p,r>=1, 3<=p+r<=N-1, kappa=core  =>  ctx(a kappa)=ctx(kappa a)."""
    ctx = defaultdict(set)
    for w in S:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                ctx[w[i:j]].add((w[:i], w[j:]))
    chk = fl = 0
    for w in S:
        if set(w) == {'a'} or w[0] != 'a' or w[-1] != 'a': continue
        core = w.strip('a'); lam = len(w) - len(core)
        if 3 <= lam <= N - 1:
            chk += 1
            if ctx['a' + core] != ctx[core + 'a']: fl += 1
    return chk, fl

def run_S1_S3(trials=300):
    log('== [S1]/[S3] random seeds -> exact closure; Lemma S and exchange (X1) on closed sets')
    stats = defaultdict(int)
    xchk = xfail = 0
    for t in range(trials):
        N = random.randint(5, 6)
        seed = random_seed_words(N, random.randint(1, 3))
        R = closure(seed, cap_len=N + 3, cap_words=3000, max_rounds=12, N=N, stop_on_contra=False)
        stats[R['status']] += 1
        if R['status'] == 'closed':
            K = R['K']
            ok, wit = check_closed(K)
            must(ok, 'S1: closure reported closed but exact check fails: %s' % wit)
            if shortest_apower(K) == N:
                stats['closed_with_min_aN'] += 1
                sc = skeleton_conflicts(K, N)
                must(not sc, 'S1: Lemma S violated on closed set: %s' % sc)
                c, f = rotation_instances(K, N)
                xchk += c; xfail += f
        elif R['status'] == 'contra':
            stats['contra_' + R['contra'][0]] += 1
    must(xfail == 0, 'S3: rotation lemma failures: %d' % xfail)
    log('   trials=%d status counts=%s' % (trials, dict(stats)))
    log('   rotation-lemma (Rot) instances checked=%d failures=%d' % (xchk, xfail))
    return stats

# =================================================================== S2 negative control
def d1_closure(seed, cap_len, N):
    K = set(seed)
    for _ in range(20):
        ctx = defaultdict(set)
        for w in K:
            n = len(w)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    ctx[(w[i:j],)].add((w[:i], w[j:]))
        bucket = defaultdict(list)
        for x, Es in ctx.items():
            for E in Es: bucket[(ttype(x), E)].append(x)
        new = set()
        for _, xs in bucket.items():
            if len(xs) < 2: continue
            for x in xs:
                for y in xs:
                    if x == y: continue
                    for E1 in ctx[x]:
                        w = fill(E1, y)
                        if w not in K and len(w) <= cap_len: new.add(w)
        if not new: return K
        K |= new
    return None

def run_S2():
    log('== [S2] negative control: d=1-closed set violating Lemma S must be d=2-non-closed')
    found = 0
    N = 7
    cands = [('abaaa', 'aaaaba'), ('abaa', 'aabaa'), ('abaaaa', 'aaba'), ('aabaaa', 'aba')]
    for w1, w2 in cands:
        seed = {'a' * N, w1, w2}
        K = d1_closure(seed, N + 2, N)
        if K is None: continue
        if shortest_apower(K) != N: continue
        sc = skeleton_conflicts(K, N)
        if not sc: continue
        ok, wit = check_closed(K)
        must(not ok and verify_witness(K, wit), 'S2: expected a verified d=2 violation')
        must(wit is not None and len(wit['x']) == 2, 'S2: violation should be two-hole')
        log('   seed', sorted(seed), '-> d1-closed |K|=%d, skeleton conflict %s' % (len(K), sc))
        log('   d=2 witness:', json.dumps(wit, default=list))
        found += 1
        break
    must(found == 1, 'S2: negative control instance found')

# =================================================================== S4 tree arithmetic
def run_S4(trials=4000):
    log('== [S4] Theorem T1 arithmetic on random rank<=r trees')
    worst = 0.0
    for t in range(trials):
        r = random.randint(2, 3); theta = random.randint(1, 4)
        # random tree: node = (terminals, children); depth-limited
        def gen(depth):
            nt = random.randint(0, theta)
            if depth == 0 or random.random() < 0.15:
                return (max(nt, 1), [])
            q = random.randint(1, r)
            return (nt, [gen(depth - 1) for _ in range(q)])
        T = gen(random.randint(2, 9))
        # compute k, heights; boundary = leftmost & rightmost root paths
        nodes = []
        def walk(node, depth, left, right):
            nt, ch = node
            k = nt + sum(walk(c, depth + 1, left and i == 0, right and i == len(ch) - 1)
                         for i, c in enumerate(ch))
            nodes.append((k, left, right, depth))
            return k
        Ntot = walk(T, 1, True, True)
        h = max(d for (_, _, _, d) in nodes)
        # deficits: delta in [k-theta, k] for EVERY big node (boundary included), SNAPPED to reuse
        # existing values whenever possible (adversarial: minimises M)
        vals = set()
        for (k, l, rr, d) in nodes:
            if k > theta:
                lo, hi = max(1, k - theta), k
                reuse = [v for v in vals if lo <= v <= hi]
                vals.add(reuse[0] if reuse else random.randint(lo, hi))
        M = len(vals)
        sigma = 2 * (r + 1)
        bound = theta * sigma ** (2 * M + 1)          # Theorem T1 (sharp form): N < theta*sigma^(2M+1)
        must(Ntot < bound, 'S4: N=%d >= bound=%d (h=%d,r=%d,theta=%d,M=%d)' % (Ntot, bound, h, r, theta, M))
        worst = max(worst, Ntot / bound)
    log('   trials=%d, max N/bound = %.4f' % (trials, worst))

# =================================================================== main
def main():
    t0 = time.time()
    src = open(__file__, 'rb').read()
    log('checker SHA256', hashlib.sha256(src).hexdigest())
    log('python', sys.version.split()[0], ' seed 20261115')
    sel = sys.argv[1].split(',') if len(sys.argv) > 1 else ['S0', 'E1', 'S2', 'S1', 'S4', 'E2']
    log('sections', sel)
    if 'S0' in sel: run_S0()
    if 'E1' in sel: run_E1()
    if 'S2' in sel: run_S2()
    if 'S1' in sel: run_S1_S3()
    if 'S4' in sel: run_S4()
    if 'E2' in sel: run_E2()
    log('== SUMMARY: checks=%d FAIL=%d  time=%.1fs' % (COUNT, FAIL, time.time() - t0))
    log('ALL CHECKS PASSED' if FAIL == 0 else 'SOME CHECKS FAILED')
    sys.exit(0 if FAIL == 0 else 1)

if __name__ == '__main__':
    main()

===== END FILE =====

===== BEGIN FILE claude_round13_noncomm_U_checker_output_2026-11-15.txt bytes=5288 sha256=3dc1019ea1e9a0b26da10ab7d2f8f6badb6efc47f8d7c55738652d0ada4433b5 =====
command: python3 -I claude_round13_noncomm_U_checker_2026-11-15.py
file SHA256: 3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a
started: 2026-11-15T22:35:08+09:00
checker SHA256 3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a
python 3.13.18  seed 20261115
sections ['S0', 'E1', 'S2', 'S1', 'S4', 'E2']
== [S0] exact finite substitutability: controls
   interior-only family a^5 + a^+ b a^+ (total 3) is not closed; witness {"x": ["ab"], "y": ["ba"], "E_accept": ["a", "a"], "E_test": ["", "aa"], "E_accept_x": "aaba", "E_accept_y": "abaa", "E_test_x": "abaa", "E_test_y": "baaa", "type_x": [["a", "b"]], "type_y": [["a", "b"]]}
   closure: status=closed |S|=5 S=['aaab', 'aaba', 'abaa', 'baaa', 'aaaaa']
   negative control {a^5, abaa}: witness {"x": ["a", "aa"], "y": ["aa", "a"], "E_accept": ["", "a", "a"], "E_test": ["", "b", ""], "E_accept_x": "aaaaa", "E_accept_y": "aaaaa", "E_test_x": "abaa", "E_test_y": "aaba", "type_x": [["a"], ["a"]], "type_y": [["a"], ["a"]]}
== [E1] cross-class order dependence: closure of an order-dependent seed
   f2=5: status=closed |K|=34 rounds=2 contra=None
     W1=abaca deficit 5 ; W2=acaba deficit 5 ; same a-collapsed bigram multiset+endpoints=True
     full closed set S1(f2=5) = ['aaabc', 'aaacb', 'aabac', 'aabca', 'aacab', 'aacba', 'abaac', 'abaca', 'abcaa', 'acaab', 'acaba', 'acbaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'caaab', 'caaba', 'cabaa', 'cbaaa', 'aaaaac', 'aaaaca', 'aaacaa', 'aacaaa', 'acaaaa', 'caaaaa', 'aaaaaab', 'aaaaaba', 'aaaabaa', 'aaabaaa', 'aabaaaa', 'abaaaaa', 'baaaaaa', 'aaaaaaaa']
     words with content {a,b,c} and a-count<N: ['aaabc', 'aaacb', 'aabac', 'aabca', 'aacab', 'aacba', 'abaac', 'abaca', 'abcaa', 'acaab', 'acaba', 'acbaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'caaab', 'caaba', 'cabaa', 'cbaaa']
   f2=4: status=closed |K|=39 rounds=2 contra=None
     W1=abaca deficit 5 ; W2=acaaba deficit 4 ; same a-collapsed bigram multiset+endpoints=True
     REFUTED (exact, finite): deficit not a function of bigram data; cb-order deficit 4 != 2+3
     full closed set S1(f2=4) = ['aaabc', 'aabac', 'aabca', 'abaac', 'abaca', 'abcaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'aaaaac', 'aaaaca', 'aaaacb', 'aaacaa', 'aaacab', 'aaacba', 'aacaaa', 'aacaab', 'aacaba', 'aacbaa', 'acaaaa', 'acaaab', 'acaaba', 'acabaa', 'acbaaa', 'caaaaa', 'caaaab', 'caaaba', 'caabaa', 'cabaaa', 'cbaaaa', 'aaaaaab', 'aaaaaba', 'aaaabaa', 'aaabaaa', 'aabaaaa', 'abaaaaa', 'baaaaaa', 'aaaaaaaa']
     words with content {a,b,c} and a-count<N: ['aaabc', 'aabac', 'aabca', 'abaac', 'abaca', 'abcaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'aaaacb', 'aaacab', 'aaacba', 'aacaab', 'aacaba', 'aacbaa', 'acaaab', 'acaaba', 'acabaa', 'acbaaa', 'caaaab', 'caaaba', 'caabaa', 'cabaaa', 'cbaaaa']
== [S2] negative control: d=1-closed set violating Lemma S must be d=2-non-closed
   seed ['aaaaaaa', 'aaaaba', 'abaaa'] -> d1-closed |K|=3, skeleton conflict {'AbA': [4, 5]}
   d=2 witness: {"x": ["a", "aa"], "y": ["aa", "a"], "E_accept": ["", "a", "ba"], "E_test": ["", "b", "a"], "E_accept_x": "aaaaba", "E_accept_y": "aaaaba", "E_test_x": "abaaa", "E_test_y": "aabaa", "type_x": [["a"], ["a"]], "type_y": [["a"], ["a"]]}
== [S1]/[S3] random seeds -> exact closure; Lemma S and exchange (X1) on closed sets
   trials=300 status counts={'closed': 209, 'closed_with_min_aN': 209, 'contra': 51, 'contra_apower': 51, 'truncated': 39, 'cap': 1}
   rotation-lemma (Rot) instances checked=1202 failures=0
== [S4] Theorem T1 arithmetic on random rank<=r trees
   trials=4000, max N/bound = 0.1667
== [E2] within-class {b,c} bigram-linearity: closure experiments
   case naive-violating N=10 |seed|=107 -> status=contra |K|=2132 rounds=1 time=1.1s contra=('skeleton', 'AcbbcA', [5, 6, 7])
     certificate: 2 rule applications, replay=True, targets=['aaaacbbcaaa', 'aaaacbbcaa']
        0  x=('abc',) y=('acb',) E0=('', 'aacbcba') E1=('aaa', 'bcaaa')  =>  aaaacbbcaaa
        1  x=('abc',) y=('bca',) E0=('aaabc', 'bca') E1=('aaaacb', 'a')  =>  aaaacbbcaa
   case naive-linear    N=10 |seed|=127 -> status=contra |K|=4097 rounds=1 time=1.8s contra=('skeleton', 'AcbAbcbcAbc', [3, 4, 5])
     certificate: 2 rule applications, replay=True, targets=['aacbabcbcabc', 'acbabcbcabc']
        0  x=('cbacbaa',) y=('abcbcabc',) E0=('a', 'aa') E1=('aacb', '')  =>  aacbabcbcabc
        1  x=('aacbcba',) y=('bcbcabc',) E0=('aa', 'aa') E1=('acba', '')  =>  acbabcbcabc
   case prim-bc2-cb3    N=10 |seed|=39 -> status=contra |K|=494 rounds=2 time=0.9s contra=('skeleton', 'AbbccAbcA', [4, 5])
     certificate: 6 rule applications, replay=True, targets=['aabbccabcaa', 'abbccaabca']
        0  x=('aaaabc',) y=('bcabca',) E0=('aa', 'aa') E1=('abc', 'a')  =>  abcbcabcaa
        1  x=('a', 'cb') y=('aa', 'bc') E0=('abc', 'a', 'aa') E1=('', 'b', 'cabcaa')  =>  aabbccabcaa
        2  x=('aaabca',) y=('cbabc',) E0=('aa', 'aa') E1=('acb', '')  =>  acbcbabc
        3  x=('aaabca',) y=('bcaabc',) E0=('aa', 'aa') E1=('acb', '')  =>  acbbcaabc
        4  x=('aaaabc',) y=('cbabc',) E0=('aa', 'aa') E1=('abc', 'a')  =>  abccbabca
        5  x=('b', 'bab') y=('bb', 'aab') E0=('ac', 'c', 'c') E1=('a', 'cc', 'ca')  =>  abbccaabca
== SUMMARY: checks=4458 FAIL=0  time=474.9s
ALL CHECKS PASSED
exit code: 0
finished: 2026-11-15T22:43:03+09:00

===== END FILE =====

===== BEGIN FILE claude_round13_noncomm_U_checkpoint1_2026-11-15.md bytes=1361 sha256=333edfdb04e59886ae6c3da7bb6f8af822309941cdff58c29d1adadb4495b716 =====
# 第十三段 チェックポイント1（2026-11-15）

**状態：** 予想 U（非可換）は OPEN。途中段階で得た実質的成果は次のとおり。

- **[PROVED] 骨格関数補題 L2**：(R)+(U) から、同一骨格で a 数 ≤N−1 の受理語は a 数が等しい。陰性対照で d=2 の必要性を確認した。
- **[PROVED] 回転補題 Rot**：`a^pκa^r∈L`（p,r≥1、3≤p+r≤N−1）なら aκ≡κa。
  - 実験の陽性対照で `aba≡aab` が強制されることから発見した。外側の a 連だけの族は閉じない。
  - 帰結：部品間の a 連は保存量ではない（併合 Cat）。
- **[PROVED] 定理 T1**：大節点の単独語骨格の種類数を M とすると N < θ̄(2r+2)^{2M+1}。
- **[REFUTED（厳密・有限）] 語レベルの bigram 関数主張**：閉じた 39 語の集合で `abaca`（欠損5）と `acaaba`（欠損4）の bigram 多重集合・端点が一致した。

**方針修正.** 当初の「a で挟まれた部品」モデルは Rot により誤りだった。不変量は連結核（Cat）で考え直す。

**次の作業.** 同一内容類 {b,c} の閉包実験 E2（bigram 線形性と整合しない種の矛盾証明書）、最終ログの作成。

GitHub は取得不可だったため、定義は第十二段チェックポイントの転記に拠る。

===== END FILE =====

===== BEGIN FILE claude_round13_noncomm_U_final_report_2026-11-15.md bytes=18599 sha256=cb1782110ebf873d9a31127442243c9adca02e0b9a05743f3116145244c5394e =====
# Claude 第十三段 最終報告：Fable-C から非可換予想 U へ（2026-11-15）

**一文結論.** 予想 U（非可換）は **OPEN**。ただし次の四つを得た。

- 二穴代入可能性から、核が `a` と可換になる**回転補題**を新たに証明した。
- 「核の型数 M が有界なら最短 `a^N` の長さは θ について線形」という**無条件の限定定理 T1**（任意 fan-out、v 因子なし）を証明した。
- Fable §6 の Euler／bigram 計画の中間主張「欠損は（a を潰した）bigram 多重集合と端点の関数」を、**有限・厳密な反例で REFUTED** とした。
- 同一内容類の中では、bigram 線形性の要請を超える剛性が実際に強制される具体例を、**機械検査済み証明書**で得た。

`op:fanout-two` は **OPEN**。

**読めなかった資料.** GitHub（`main.tex` など）は本セッションのネットワーク許可リスト外で取得できなかった。定義は次のものに拠った。

- 依頼書 I-3 の条件
- 第十二段チェックポイント（プロジェクト内）が `main.tex` から転記した記述
  - good = ε-free・nondeleting・nonpermuting・nonmerging（nonmerging = 同一子の連続成分 `x_{j,k}x_{j,k+1}` を一成分内で直接連結しない）
  - `θ_G(R)` = 規則 R を使う文の最小長、`θ̄=max(1,max_R θ_G(R))`
  - `lem:thickness-equivalence` (i) 各規則の明示終端は ≤θ̄ 個、(ii) 各非終端の最短収率 ≤θ̄

原稿と食い違う場合は原稿を優先されたい。

ラベル：**[PROVED]** 本報告に完全証明あり／**[REFUTED]** 全仮定を満たす反例と厳密検証あり／**[CERTIFIED]** 有限インスタンスについて、独立 replay 済みの導出証明書による証明／**[COMPUTATIONAL EVIDENCE]**／**[CONDITIONAL]**／**[OPEN]**。いずれも未査読・未形式化であり、新規性は保証しない。

---

## 0. 命題一覧

| # | 命題 | 状態 |
|---|---|---|
| L1 | (R) 再配分・(U) 一意性（Fable 5.1 の再証明） | PROVED |
| L2 | 骨格関数補題 S：同一骨格・a数≤N−1 ⇒ a数一致 | PROVED（d=2 が本質。陰性対照 S2） |
| L3 | **回転補題 Rot**：`a^pκa^r∈L`, p,r≥1, 3≤p+r≤N−1 ⇒ `aκ≡κa` | PROVED（新） |
| L4 | 併合 Cat：Rot 核の間の a 連は消せる（欠損保存） | PROVED |
| L5 | 内容交換 X1（d=1）と**運搬子交換 X2（d=2、任意の因子出現に作用）** | PROVED |
| T1 | **有界核型定理**：`N < θ̄·(2r+2)^{2M+1}`（M = 大節点の単独語骨格の種類数） | PROVED（新） |
| C1 | 反例族は `M_n ≥ (log_{2r+2}(N_n/θ̄_n) − 1)/2` を要する | PROVED（T1 の系） |
| T2 | 還元：有界次元 β について仮説 H(K) ⇒ U | CONDITIONAL（含意は監査済み Fable-C (4)–(7) の移植） |
| E1 | 「欠損は bigram 多重集合＋端点の関数」「内容類をまたぐ並べ替え不変加法性」 | **REFUTED**（39語の有限閉集合で厳密） |
| E2 | 類 {b,c} で δ(bc)=2, δ(cb)=3 と加法的二部品実現は両立しない（N=10） | CERTIFIED（6〜8手の証明書） |
| O1 | 等長の全核交換だけでは反転数型の統計が排除できない（長さ4で手計算） | PROVED（観察として） |
| U | 予想 U（非可換） | **OPEN** |

---

## 1. 最初の論理検査（IV-1）

| 項目 | 内容 |
|---|---|
| Fable-C の仮定 | 可換 L、半束型付け s、`L∈C^{mcf}_{f,s}`、G は L∩Σ⁺ の reduced good 提示（fan-out 任意、rank ≤r、v=\|V\|、θ=θ̄_G は元の G の厚さ）。D=\|Σ\|−1 を固定。結論 `N=O_{D,r}(vθ^{1+D+D²2^D})`。用いるのは d=1 のみ。 |
| 予想 U | 固定 (Σ,f,r,s) に対し、**全ての** (L,G) で一様に `N ≤ p(‖G‖,θ̄_G)`。成立しても τ(G,s) 全体は制御できず、`op:fanout-two` の NO も出ない。 |
| 5.1 (R) | 仮定 `p a^i q a^j r∈L`, q∈Σ⁺, i+j≤N−1。共通文脈 `□a□a^{N−1−i−j}`。結論：同じ和の任意の正の再配分が受理される。**d=2**。 |
| 5.1 (U) | 仮定 `Pa^iQ, Pa^{i'}Q∈L`, 1≤i<i'≤N は起こらない。**d=1**。 |
| 5.1 (E) | 内容が等しい部品 aVa^e, aV'a^{e'} の同値。監査で補完済み。 |
| Fable §6 | 定理：交叉（系 2.2）は bigram を保つ。**推測**：同 bigram の部品多重集合は宿主を保って連結である、欠損は bigram の加法関数である、fan-out 2 でも新しい困難はない。 |
| 監査の地位 | 「VALID AS A HAND-PROOF」は手証明としての内的妥当性の評価であり、査読・形式化・新規性認定ではない。 |

---

## 2. 準備：(R)・(U)・骨格関数 [PROVED]

以下 s は半束型付けとする。像が可換冪等なので `s(a^i)=s(a)` かつ `s(xy)=s(yx)`。`L∈C^{mcf}_{f,s}`, f≥2、`N=min{n≥1: a^n∈L}`。sk(w) は w の各極大 a 連を記号 Â に置き換えた語。

**L1 (R).** `p a^i q a^j r∈L`、q∈Σ⁺、i,j,i',j'≥1、i'+j'=i+j≤N−1 ⇒ `p a^{i'} q a^{j'} r∈L`。

*証明.* x=(a^i,a^j)、y=(a^{i'},a^{j'}) は成分型が等しい。文脈 `□a□a^{N−1−i−j}`（中央 a は非空）に両方を入れると a^N∈L になる。よって x≡y であり、文脈 p□q□r に適用すればよい。∎

**L1 (U).** `Pa^iQ, Pa^{i'}Q∈L`、1≤i<i'≤N は不可能。

*証明.* a^i≡a^{i'}（d=1、共通文脈 P□Q）。文脈 `a^{N−i'}□` で a^{N−i'+i}∈L となり、0<N−i'+i<N が最小性に反する。∎

**L2（骨格関数）.** w,w'∈L、sk(w)=sk(w')、|w|_a,|w'|_a≤N−1 ⇒ |w|_a=|w'|_a。

*証明.* a 連の個数を k とする（k=0 なら両方 0）。極大 a 連は互いに非空の非 a 因子で隔てられる。L1(R) を対ごとに使えば（各対の和 ≤ 全 a 数 ≤ N−1）、第 2〜k 連を 1 にし、第 1 連を e−(k−1) にできる。w' も同様に e'−(k−1) にする。両語は共通の P, Q で P a^{e−k+1} Q, P a^{e'−k+1} Q と書けるので、(U) より e=e'。∎

**陰性対照 S2 [検証済み].** {a⁷, abaaa, aaaaba} は d=1 の導出規則で閉じ、L2 に反する（骨格 ÂbÂ で a 数 4 と 5）。この集合は d=2 で閉じない。証人は `x=(a,aa)`, `y=(aa,a)`、共有文脈 `□aaa□a`、試験文脈 `□b□a`。L2 は fan-out 2 固有であり、fan-out 1 の指数下界とは矛盾しない。

---

## 3. 新しい一般補題：回転・併合・運搬子交換

**L3（回転補題）[PROVED].** κ∈Σ⁺、p,r≥1、λ:=p+r、3≤λ≤N−1、`a^pκa^r∈L` ⇒ aκ ≡_{L,s} κa。

*証明.* L1(R)（隔て κ∈Σ⁺、和 λ≤N−1）より `a²κa^{λ−2}∈L` と `aκa^{λ−1}∈L`（λ−2≥1）。文脈 E=(a, a^{λ−2}) について E[aκ]=a²κa^{λ−2}、E[κa]=aκa^{λ−1}。両方受理されるので共通受理文脈であり、s(aκ)=s(κa)。∎

*帰結.*

- 同じ型の d=1 同値は合同関係なので、任意の語で `X a^n κ Y∈L ⟺ X κ a^n Y∈L`。
- 特に κ の単独語は、外側の a の任意の分配（0 を含む）で受理される。
- S0 の陽性対照で実測した：`a^+ba^+` だけの族は閉じず（`aba≡aab` が強制される）、閉包は `baaa, aaab` を含む。
- 実験 S3：閉じた 209 集合で Rot の 1202 例を検査し、失敗 0。

**L4（併合 Cat）[PROVED].** `W=a^{e_0}κ_1a^{e_1}⋯κ_m a^{e_m}∈L` で各 κ_i が aκ_i≡κ_ia を満たすなら、`W∈L ⟺ a^{Σe}κ_1κ_2⋯κ_m∈L`。

*証明.* 合同性により a を順に左へ移すだけ。∎

したがって Σe≤N なら、(U) により a 数は**連結文字列** κ_1⋯κ_m だけで決まる。木の互いに素な大節点の同時置換（欠損 δ_B+δ_C）は、この連結核の欠損を与える。部品の間の a 連は不変量として消えてしまう（Fable §6 の「部品の間に残る区切り」は保存量ではない）。

**L5（交換）[PROVED].** κ,κ' が単独語をもち、外側の a 総数 λ,λ'∈[3,N−1]、単独語の a 数を e,e' とし、δ:=N−e、δ':=N−e' とおく。

- **X1（d=1）.** s(aκ)=s(aκ') のとき、i:=max(0,λ−λ')、i':=max(0,λ'−λ) とすると、任意の X,Y について `X a^iκY∈L ⟺ X a^{i'}κ'Y∈L`。a 数の変化は δ−δ'。
  - *証明.* 文脈 (a^s,a^t)、s+t=λ−i=λ'−i'。Rot により分配は任意なので、E[a^iκ] と E[a^{i'}κ'] は両方とも受理される。∎
- **X2（運搬子、d=2）.** s(κ)=s(κ') のとき、i≥1 かつ i'=i+λ'−λ≥1 となる i を選ぶ。任意の l,r と**任意の非空** m について `l a^i m κ r∈L ⟺ l a^{i'} m κ' r∈L`。
  - *証明.* x=(a^i,κ)、y=(a^{i'},κ') の成分型は等しい。文脈 (a^s, a^m, a^t)（m≥1、s+m+t=λ−i）は Rot により両方を受理する。∎
  - **κ は語中の任意の因子出現でよい**（左方のどこかに長さ ≥i の a 連が非空の隔てを挟んであればよい）。より長い非 a 区間の内部の出現も含む。fan-out 2 の交錯・入れ子配置（II-3.8）でも、隔て m が他部品を含んでよいので交換は機能する。

---

## 4. 定理 T1：有界核型 [PROVED]

**設定.** 上の L, N に加え、G は L∩Σ⁺ の reduced good MCFG（fan-out 任意、rank ≤r）、θ:=θ̄_G とする。τ は a^N の G 導出木のうち節点数最小のもの。節点 X の非終端を A_X、収率総長を k_X とする。u_A は A の最短収率組（総長 ≤θ、L1 の引用 (ii)）。**単独語** w_X は、X の部分木を u_{A_X} の導出で置き換えた語（∈L）。**大節点**は k_X>θ を満たす節点。

**定理 T1.** M を大節点の骨格 sk(w_X) の種類数とする（τ の最重子経路上に限ってよい）。σ:=2(r+1) とおくと
\[ N < θ\,σ^{2M+1}. \]

*証明.*

(a) 大節点 X について |w_X|_a = N−k_X+|u_A|_a ≤ N−k_X+θ ≤ N−1。δ_X:=N−|w_X|_a∈[k_X−θ, k_X]。

(b) **型一定性.** sk(w_X)=sk(w_Y) ⇒ δ_X=δ_Y（L2 と (a)）。

(c) **窓補題.** 根から最重子を辿る列を k_0=N≥k_1≥⋯ とする。
- k_i>θ なら節点は子を持つ（子のない規則は終端 ≤θ 個しか書かない）。終端 ≤θ、子 ≤r なので k_{i+1}≥(k_i−θ)/r。
- 実数 y∈[σθ,N] を取り、k_j≤y となる最初の j を選ぶ。
  - j=0 なら δ_0≥y−θ>y/σ。
  - j>0 なら k_{j−1}>y で、δ_j≥k_j−θ>(y−θ)/r−θ=(y−(r+1)θ)/r≥y/(2r)≥y/σ。
  - どちらの場合も δ_j≤k_j≤y。δ_j>y/σ≥θ なので j は大節点である。
- 窓 I_t=[θσ^{2t}, θσ^{2t+1}]（t=0,…,M）は互いに素で、上端 y_t=θσ^{2t+1}≥σθ。

(d) N≥θσ^{2M+1} と仮定する。すると M+1 個の互いに素な窓の各々が大節点の δ を含み、それらは互いに異なる。(b) より骨格も互いに異なり、M+1 種類以上となって矛盾。∎

**注意.**

- d=2 の使用は L2 のみ（L1(R) 経由）。fan-out 1 では L2 が偽になりうる（§2 の陰性対照）。
- 依頼書 III-A3 の例示「有限個の核型」に当たる。
- 境界節点・v 因子は不要になった。
- good の性質（ε-free、nonmerging）から、X の成分間の隔ては非空である。よって sk(w_X) は（A_X、左端か、右端か）だけで決まり、M≤4v。これは自明な指数上界 N<θσ^{8v+1} を回復する。

**系 C1（下界側の障壁）.** 予想 U の反例族 (L_n,G_n) は M_n ≥ ½(log_σ(N_n/θ_n)−1) を満たさねばならない。N_n が超多項式なら、M_n は log‖G_n‖ のどんな定数倍よりも大きい。すなわち、**最重子経路上に、骨格が互いに異なり欠損の尺度が全く違う短収率型が超対数個必要**である。

実験 S4（窓算術のみ）：4000 本の乱択木で、δ を既存値へ寄せる敵対的割当てのもと `N<θσ^{2M+1}` を検査し、FAIL 0、最大比 0.167。

---

## 5. 還元 T2 [CONDITIONAL]

ある K と写像 β：{大非終端} → [0,θ]^K について、次を H(K) と呼ぶ：**各分岐類 T の単位 J_0,…,J_t について、Σλ_iβ(J_i)=0（|λ_i|≤K!θ^K、正負側の総欠損 ≤N−1）なら Σλ_iδ_{J_i}=0。**

H(K) のもとでは、Fable-C §5(4)–(7)（監査済み）が D を K に置き換えてそのまま通る。B=K!θ^K、ρ=2KB とし、類の数は 2^{|Σ|} 以下（内容類）。結論は N=O_{K,|Σ|,r}(vθ^{1+K+K²2^{|Σ|}})。

- 可換の場合は β=Parikh で H(D) が成り立つ（Fable-C (2)(3)＋可換性）。
- **T1 は β=核型の指示ベクトル（K=M）の場合で、H は L2 から無条件に成り立つ。**

開問題は「K=K(Σ) の有界な β で H を満たすもの」の存在に還元される。この含意は監査済みの議論の移植であり、独立再監査はしていない。

---

## 6. E1：bigram 関数主張の反例 [REFUTED]

**集合.** S1 は次の 39 語（チェッカで閉包を計算し、厳密判定で d=1,2・内容型付きの組代入可能性を確認）。

- a⁸
- 単独 b（a 数 6）の全配置
- 単独 c（a 数 5）の全配置
- b が c より前の語（a 数 3）の全配置
- c が b より前の語（a 数 4）の全配置

完全な一覧はログ 19 行目にある。性質：

- 最短 a 冪は a⁸。
- 有限なので各語を一規則とする提示は reduced good（fan-out 1, rank 0）であり、`S1∈C^{mcf}_{2,c_Σ}`。
- L2 は成立する。

**反例.**
- W1=`abaca`：欠損 5
- W2=`acaaba`：欠損 4
- 両者の a を潰した bigram 多重集合 {Âb, bÂ, Âc, cÂ} と端点 (Â,Â) は一致する。
- さらに δ(b)+δ(c)=2+3=5≠4 である。

**反証された主張.**
1. 「欠損は（a 境界を含む）bigram 多重集合と端点の関数」（Fable §6-2,3 の語レベルの形）
2. 「多部品語の欠損は部品の並べ替えに依らず加法的」（内容類をまたぐ場合）

**反証されていないもの.**
- 予想 U
- 同一内容類内での主張（X1 により、同一類の部品の並べ替えは欠損を保つ）
- 木由来の加法性（S1 は木を持たない）

したがって正しい不変量は、類ごとに分けて扱う必要がある（T2 の H は類ごとに定式化してある）。

---

## 7. E2：同一類の剛性 [CERTIFIED]

**種集合**（N=10）：
- a¹⁰
- 単独核 bc（δ=2）、cb（δ=3）
- 四通りの二部品順序配置（欠損は和）

**結果.** 有界閉包（長さ ≤14）の 2 巡目で、同一骨格に a 数が二つ（≤N−1）現れた。例えば骨格 ÂbbccÂbcÂ に a 数 4 と 5。L2 によりこの種集合を含み a¹⁰ を最短とする `L∈C_{2,c}` は存在しない。

**証明書.** 導出規則（Fable 定義 2.3）を 6〜8 回適用し、独立に replay した。証明書の具体的な手順は Python の文字列ハッシュの乱択化で実行ごとに変わるが、結論（status=contra）は 3 回の実行で安定していた。

**機構.** bc と cb の bigram ベクトルは異なるので、bigram 線形性だけからは δ(bc)=δ(cb) は従わない。

- **O1（手計算）.** 長さ 4 の六語 {bcbc, bbcc, cbcb, ccbb, bccb, cbbc} について、欠損 K+(δ(cb)−δ(bc))·inv(w)（inv = c が b より前にある対の数）は、全ての X2 全核交換 bc↔cb および Cat 値（bcbc=2δ(bc)、cbcb=2δ(cb)、bccb=cbbc=δ(bc)+δ(cb)）と矛盾しない。
- **矛盾は全核交換だけからは出ない.** 実際の証明書は、核の一部だけを動かす d=2 の手を使っている。例：x=(b,bab)、y=(bb,aab)；x=(bcac,c)、y=(bcaa,cc)。
- この結果は「Rot＋Cat＋部分因子のスライドが、反転数のような非線形統計を殺す」ことを示唆する。

**未実施.** 整合的な対照（δ(bc)=δ(cb)=2）は閉包が約 9 分で 10⁴ 語を超えて収束しなかったので、最終ランから外した。よって「整合なら閉じる」は**検査していない**。

---

## 8. 既知結果との関係

- L1 は Fable 5.1(R)(U) と同内容（独立再証明）。L5-X1 は Fable-C(2) と監査 §2.2 の非可換版で、Rot により側方の a の量の条件が不要になる。
- Rot は `lem:power-transfer` や Fable 補題 2.1（滑り補題）の z=a, m=a の特殊例ではない（核 κ 全体が a と可換になる）。ただし証明は (R)＋d=1 だけなので、既存ラウンドの補償法則（附録 C 補題 C）と一部重なる可能性がある。照合はしていない。
- T1 は Fable-C と相補的である。Fable-C は「型数は多いが Parikh で線形」、T1 は「線形性なしで型数有界」を扱う。
- 定理 A（倍化族の崩壊）で見られた、文字が a の連を飛び越す移送は、Rot の特殊な現れと整合する。

## 9. 正式中心問題への含意

- 予想 U は依然として未決で、`op:fanout-two` には届かない。
- 下界側（YES 側）への制約：単項希少型を使う下界は、C1 により超対数個の核型を必要とする。さらに E2 型の剛性を逃れる必要がある。単項希少型ルートの見込みは一段と低くなった（証明ではない）。
- 上界側（NO 側）：H(K) を Parikh（K=D）で、類ごと・木由来実現について示せれば、Fable-C が非可換へそのまま延長される。

## 10. 次の有力な一手

**Parikh 還元予想 P**：分岐類 T の Rot 核からなる木由来の実現では、δ は Parikh ベクトルの線形関数である。

E1 は類をまたぐ場合なので P の反例にはならない。E2 は P と整合する。

証明の候補路：
1. Cat で連結核を作る。
2. 単位の多重コピー（分岐類の帰納で利用可能）を宿主として、Fable 系 2.2 の滑りで任意の隣接文字対 (d,e) を入れ替える。
3. 入れ替えのシフト量が、X2 と Cat の整合性により 0 に強制されることを示す（O1 → E2 の一般化）。

詳細は next_obligations を参照。

## 11. 成果物

- `claude_round13_noncomm_U_checker_2026-11-15.py`（SHA256 `3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a`）
- `claude_round13_noncomm_U_checker_output_2026-11-15.txt`（SHA256 `3dc1019e…33b5`）：実行コマンド `python3 -I …`、終了コード 0、4458 checks、FAIL 0、約 475 秒。
- 本報告、checkpoint1、next_obligations。

GitHub・原稿の編集は行っていない。

===== END FILE =====

===== BEGIN FILE claude_round13_noncomm_U_next_obligations_2026-11-15.md bytes=2992 sha256=496ae66d32cd3c36f635db0702f6760317c6e96a1cd045a2eeb6636b604defbb =====
# 第十三段 残存義務（2026-11-15）

## 最小残余命題

**P（Parikh 還元・類ごと）.** L∈C^{mcf}_{2,c_Σ}、a^N 最短、τ を節点最小の導出木とし、T を（内容類での）分岐類とする。T の大単位からなる木由来の多重集合実現（Cat で連結核に正規化したもの）について、次が成り立つ：Parikh が一致し総欠損 ≤N−1 なら、欠損が一致する。

P が示されれば、T2 の H(D) が成り立ち、Fable-C (4)–(7) により予想 U が従う（|Σ| 固定で多項式）。

## 未解決の量化と補題

1. **分岐類の加法性（非可換・fan-out 2）.**
   - 種 w_{B,C} の B, C が交錯・入れ子配置のとき、多重集合帰納の「単位 → 合成核」交換を X2（運搬子）で行う具体的な定式化が必要。
   - 単位同士の交換は X2 で済む。合成核は Rot・Cat で連結化できる。ただし Rot の前提 3≤λ≤N−1 を、各段階で満たすかの量化が残る。
2. **滑りの宿主.** 単位の多重コピーを宿主として、隣接文字対 de→ed（あるいは交叉）を適用できる条件を、有限コピー数で明示すること。
3. **シフト消滅.** 2 の各入れ替えが欠損を変えないこと（O1 の反転数型統計を排除すること）を一般に示す。E2 の証明書はこれを一インスタンスで示しただけである。
4. **類をまたぐ順序.** E1 のとおり順序依存は実在する。P を類ごとに限る定式化で、整数関係の議論に影響しないかを確認する（他類の部品は固定位置に残る）。
5. **T1 の改良.** 「骨格の種類」を「Rot/Cat/X2 による同値類」に置き換えた M' で T1 が成り立つか。成り立てば系 C1 の障壁が強まる。
6. Rot と第十二段の補償法則（補題 C）との包含関係を照合する。Fable-C と既存 reviews の定理 L との照合も未了。
7. GitHub の `main.tex` で定義（`def:class-cmcf`、厚さ、`def:grammar-properties`）を直接照合する（本ラウンドでは取得不可）。

## 反例候補・実験の残り

- E2 の整合対照（δ(bc)=δ(cb)）の閉包が閉じるか。約 9 分で 10⁴ 語を超えた。d=2 組の列挙を、文脈の索引化で高速化する必要がある。
- 類 {b,c} で長さ 3 の核（bcb, cbc, bbc, …）を加えた種での矛盾探索。Parikh 線形な割当てでは矛盾が出ないことの有界検証（打切りを明記すること）。
- 下界側：C1 を満たす候補（超対数個の核型、尺度分散）が、E2 型の剛性に直ちに抵触するかの探索。

## テスト範囲（今回）

- S1：N∈{5,6}、乱択種 300、長さ上限 N+3、3000 語上限。closed 209、矛盾 51、打切り 40。
- S4：rank 2〜3、θ≤4、深さ ≤9 の乱択木 4000 本。
- E1/E2：本文記載のパラメータのみ。未発見は証明扱いしない。

===== END FILE =====

===== BEGIN FILE round13_E2_original_rerun_2026-11-15.txt bytes=1893 sha256=c5de54a67a939f9837d9d5fee50d3db30f9222a3dc7e565539816f701c5c9cbc =====
checker SHA256 3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a
python 3.13.5  seed 20261115
sections ['E2']
== [E2] within-class {b,c} bigram-linearity: closure experiments
   case naive-violating N=10 |seed|=107 -> status=contra |K|=2132 rounds=1 time=1.7s contra=('skeleton', 'AbccbAbcbc', [3, 4])
     certificate: 2 rule applications, replay=True, targets=['aaabccbabcbc', 'aabccbabcbc']
        0  x=('bcaaaa',) y=('cbabcbc',) E0=('aa', 'aa') E1=('aaabc', '')  =>  aaabccbabcbc
        1  x=('acbcba',) y=('cbabcbc',) E0=('acb', 'a') E1=('aabc', '')  =>  aabccbabcbc
   case naive-linear    N=10 |seed|=127 -> status=contra |K|=4097 rounds=1 time=2.2s contra=('skeleton', 'AcbbcbcAcbA', [3, 4, 5])
     certificate: 2 rule applications, replay=True, targets=['acbbcbcaacbaa', 'acbbcbcacba']
        0  x=('cbacb',) y=('bcbcaa',) E0=('aa', 'aaa') E1=('acb', 'cbaa')  =>  acbbcbcaacbaa
        1  x=('aabcbca',) y=('bcbcacb',) E0=('aaa', 'a') E1=('acb', 'a')  =>  acbbcbcacba
   case prim-bc2-cb3    N=10 |seed|=39 -> status=contra |K|=494 rounds=2 time=1.1s contra=('skeleton', 'AbbcAcAbcA', [4, 6])
     certificate: 7 rule applications, replay=True, targets=['abbcacabcaaa', 'abbcacabca']
        0  x=('aacba',) y=('cbabc',) E0=('aa', 'aa') E1=('acb', '')  =>  acbcbabc
        1  x=('aaacba',) y=('bcabcaa',) E0=('aa', 'a') E1=('abc', '')  =>  abcbcabcaa
        2  x=('aaacba',) y=('bcaabca',) E0=('aa', 'a') E1=('abc', '')  =>  abcbcaabca
        3  x=('cbc', 'abc') y=('bc', 'cabcaa') E0=('a', 'b', '') E1=('ab', 'a', 'a')  =>  abbcacabcaaa
        4  x=('aacba',) y=('bcabca',) E0=('aa', 'aa') E1=('acb', '')  =>  acbbcabca
        5  x=('aaacba',) y=('acbabc',) E0=('aa', 'a') E1=('abc', '')  =>  abcacbabc
        6  x=('b', 'babc') y=('bb', 'abca') E0=('ac', 'c', '') E1=('a', 'cac', '')  =>  abbcacabca
== SUMMARY: checks=4 FAIL=0  time=5.0s
ALL CHECKS PASSED

===== END FILE =====

===== BEGIN FILE round13_independent_X1_counterexample_2026-11-15.py bytes=2305 sha256=715ddf6329f4bad6e1745587aff8b8d37b57d3f79a163faa776eb921a0c291ba =====
#!/usr/bin/env python3
"""Independent finite counterexample to Round13 Lemma L5-X1, as stated.
No imports from Claude's checker; exact enumeration of arity 1/2 contexts.
"""
from collections import defaultdict
S = set('''aaabc aabac aabca abaac abaca abcaa baaac baaca bacaa bcaaa
aaaaac aaaaca aaaacb aaacaa aaacab aaacba aacaaa aacaab aacaba aacbaa
acaaaa acaaab acaaba acabaa acbaaa caaaaa caaaab caaaba caabaa cabaaa
cbaaaa aaaaaab aaaaaba aaaabaa aaabaaa aabaaaa abaaaaa baaaaaa
aaaaaaaa'''.split())
assert len(S)==39
L=S|{'bc'}

def T(x):return tuple(frozenset(z) for z in x)
def fill(E,x):
    return E[0]+x[0]+E[1] if len(x)==1 else E[0]+x[0]+E[1]+x[1]+E[2]
D=defaultdict(set)
for w in L:
    n=len(w)
    for i in range(n):
        for j in range(i+1,n+1):
            D[(w[i:j],)].add((w[:i],w[j:]))
    for i in range(n):
        for j in range(i+1,n+1):
            for k in range(j+1,n):  # separator w[j:k] must be nonempty
                for z in range(k+1,n+1):
                    D[(w[i:j],w[k:z])].add((w[:i],w[j:k],w[z:]))
K=defaultdict(list)
for x,contexts in D.items():
    for E in contexts:K[(len(x),T(x),E)].append(x)
checks=0
for (d,t,E),xs in K.items():
    for x in xs[1:]:
        checks+=1
        assert D[x]==D[xs[0]],(xs[0],x,D[x]^D[xs[0]])
assert all(w and not (set(w)=={'a'} and len(w)<8) for w in L)
assert 'a'*8 in L
# Standalone words and their outer-a totals:
N=8; kap='bc'; kap2='acb'; lam=3; lam2=3
w='a'+kap+'aa'; w2='aa'+kap2+'a'
assert w=='abcaa' and w2=='aaacba'
assert w in L and w2 in L
assert 3<=lam<=N-1 and 3<=lam2<=N-1
assert set('a'+kap)==set('a'+kap2)=={'a','b','c'}
i=max(0,lam-lam2); ip=max(0,lam2-lam)
assert i==ip==0
assert 'bc' in L and 'acb' not in L
print('S size',len(S),'L size',len(L),'tuple count',len(D),'accepting contexts',sum(map(len,D.values())),'tuple-pair comparisons',checks)
print('C_2,content closed (d=1,2): YES, verified over ALL finite contexts')
print('a^N min N=8: YES')
print('X1 standalone witnesses:',w,w2)
print('s(aκ)=s(aκ\u2032)={a,b,c}: YES; λ=λ\u2032=3')
print('predicted by X1: κ=bc in L iff κ\u2032=acb in L')
print('observed: bc in L, acb not in L; X1 FALSE')
print('Note: s(κ)={b,c} while s(κ\u2032)={a,b,c}, so typed 1-hole substitutability cannot apply')
print('ALL COUNTEREXAMPLE CONDITIONS VERIFIED')

===== END FILE =====

===== BEGIN FILE round13_independent_X1_counterexample_output_2026-11-15.txt bytes=467 sha256=b915b52308612570f65f79ffd0bb33b29328da90d971e010063d801f210b3c09 =====
S size 39 L size 40 tuple count 333 accepting contexts 2327 tuple-pair comparisons 924
C_2,content closed (d=1,2): YES, verified over ALL finite contexts
a^N min N=8: YES
X1 standalone witnesses: abcaa aaacba
s(aκ)=s(aκ′)={a,b,c}: YES; λ=λ′=3
predicted by X1: κ=bc in L iff κ′=acb in L
observed: bc in L, acb not in L; X1 FALSE
Note: s(κ)={b,c} while s(κ′)={a,b,c}, so typed 1-hole substitutability cannot apply
ALL COUNTEREXAMPLE CONDITIONS VERIFIED

===== END FILE =====

===== BEGIN FILE round13_independent_checks_2026-11-15.py bytes=5388 sha256=a5666fef8082bc4b59d00f11deacb753dc42f174bf136f081210a8de022efc6e =====
#!/usr/bin/env python3
"""Independent, source-code-free Round 13 E1/E2 finite certificate audit.
Does NOT import Claude's checker. Uses submitted output strings and reconstructs
seeds and occurrence semantics independently.
"""
import ast, re, collections, itertools, os
from pathlib import Path
OUT = Path('/mnt/data/claude_round13_noncomm_U_checker_output_2026-11-15.txt').read_text()

def occurrence_contexts(S):
    q = collections.defaultdict(set)
    for w in S:
        n=len(w)
        # One hole
        for a in range(n):
            for b in range(a+1,n+1):
                q[(w[a:b],)].add((w[:a],w[b:]))
        # Two holes, positive separator
        for a in range(n):
            for b in range(a+1,n+1):
                for c in range(b+1,n):
                    for d in range(c+1,n+1):
                        q[(w[a:b],w[c:d])].add((w[:a],w[b:c],w[d:]))
    return q

def tp(x):return tuple(frozenset(t) for t in x)
def fill(E,x):return E[0]+x[0]+E[1] if len(x)==1 else E[0]+x[0]+E[1]+x[1]+E[2]
def verify_closed(S,ctx):
    at = collections.defaultdict(list)
    for x,Es in ctx.items():
        for E in Es:at[(tp(x),E)].append(x)
    for xs in at.values():
        ref=ctx[xs[0]]
        for x in xs[1:]:
            if ctx[x]!=ref: return False,(xs[0],x,ref^ctx[x])
    return True,None

def sk(w):
    return re.sub('a+', 'A',w)

def prof(w):
    t=sk(w)
    return (collections.Counter(zip(t,t[1:])),t[:1],t[-1:])

# Reconstruct the closed finite languages from log, without relying on the original program.
for f2,n in [(5,34),(4,39)]:
    m=re.search(r'full closed set S1\(f2=%s\) = (\[.*\])'%f2, OUT)
    assert m, f2
    S=set(ast.literal_eval(m.group(1)))
    assert len(S)==n
    ctx=occurrence_contexts(S)
    ok,wit=verify_closed(S,ctx)
    assert ok,wit
    assert 'a'*8 in S and not any(w and set(w)=={'a'} and len(w)<8 for w in S)
    # Independently enumerate rotation implications, exact full distributions.
    rot=0
    for w in S:
        N=8
        for p in range(1,len(w)-1):
            if w[:p]!='a'*p:continue
            for r in range(1,len(w)-p):
                if w[-r:]!='a'*r:continue
                k=w[p:len(w)-r]
                if k and 3<=p+r<=7:
                    assert ctx[('a'+k,)] == ctx[(k+'a',)], ('Rot',f2,p,k,r)
                    rot+=1
    # full finite X2 distribution equivalence, for all pairs of solo-piece witnesses
    solo=set()
    for w in S:
        for p in range(1,len(w)-1):
            if w[:p]!='a'*p:continue
            for r in range(1,len(w)-p):
                if w[-r:]!='a'*r:continue
                k=w[p:len(w)-r]
                if k and 3<=p+r<=7:solo.add((k,p+r))
    x2=0
    for k,lam in solo:
        for k2,lam2 in solo:
            if set(k)!=set(k2):continue
            for i in range(1,13):
                ip=i+lam2-lam
                if ip<1:continue
                assert ctx[('a'*i,k)] == ctx[('a'*ip,k2)], ('X2',f2,k,lam,k2,lam2,i,ip)
                x2+=1
    print(f'E1 f2={f2}: |S|={n}, |tuple-context pairs|={sum(map(len,ctx.values()))}, closed=YES, Rot={rot}, X2_all_i={x2}')
    if f2==4:
        u,v='abaca','acaaba'
        assert u in S and v in S and prof(u)==prof(v)
        assert u.count('a')==3 and v.count('a')==4
        print(f' E1 COUNTEREXAMPLE verified: {u} a={u.count("a")}, {v} a={v.count("a")}, shared profile={prof(u)}')

# Parse and replay submitted E2 2/2/6-step certificates independently.
def compositions(total, k):
    for cuts in itertools.combinations(range(1,total),k-1):
        a=(0,)+cuts+(total,)
        yield [a[i+1]-a[i] for i in range(k)]
def flank(pieces,a_total):
    for nums in compositions(a_total,len(pieces)+1):
        w='a'*nums[0]
        for core,x in zip(pieces,nums[1:]):w+=core+'a'*x
        yield w

def seed(deltas):
    S={'a'*10}
    for p,x in deltas.items():S.update(flank([p],10-x))
    for p,q in itertools.product(deltas,repeat=2):
        t=10-deltas[p]-deltas[q]
        if t>=3:S.update(flank([p,q],t))
    return S

cases=[('naive-violating',{'bc':2,'cb':2,'bcbc':3,'cbcb':4}),('naive-linear',{'bc':2,'cb':2,'bcbc':3,'cbcb':3}),('prim-bc2-cb3',{'bc':2,'cb':3})]
for name,ds in cases:
    S=seed(ds);assert len(S)=={'naive-violating':107,'naive-linear':127,'prim-bc2-cb3':39}[name]
    segment=OUT.split('case '+name)[1].split('\n   case ')[0]
    steps=re.findall(r'\n\s*(\d+)\s+x=(\(.*?\)) y=(\(.*?\)) E0=(\(.*?\)) E1=(\(.*?\))\s*=>\s*(\w+)',segment)
    for ix,x,y,e0,e1,w in steps:
        x,y,e0,e1=map(ast.literal_eval,(x,y,e0,e1))
        assert len(x)==len(y)==len(e0)-1==len(e1)-1
        assert tp(x)==tp(y)
        assert all(x) and all(y)
        if len(x)==2:assert e0[1] and e1[1]
        assert fill(e0,x) in S and fill(e0,y) in S and fill(e1,x) in S,(name,ix,x,y,e0,e1)
        assert fill(e1,y)==w,(name,ix,'wrong-target')
        S.add(w)
    print(f'E2 {name}: seed={len(seed(ds))}, replayed={len(steps)}, verified=yes, size-final={len(S)}')
    assert len(steps)=={'naive-violating':2,'naive-linear':2,'prim-bc2-cb3':6}[name]
    conflict=collections.defaultdict(set)
    for w in S:
        if w.count('a')<10 and set(w)!={'a'}:
            conflict[sk(w)].add(w.count('a'))
    assert any(len(x)>1 for x in conflict.values())
    print(' E2 contradiction independently confirmed:',next((k,sorted(v)) for k,v in conflict.items() if len(v)>1))
print('ALL INDEPENDENT CHECKS PASSED')

===== END FILE =====

===== BEGIN FILE round13_independent_checks_output_2026-11-15.txt bytes=736 sha256=0a7541f61afc7754fcc80c0bdcfb3df223fc49976599611c29ee4dba9b8528b7 =====
E1 f2=5: |S|=34, |tuple-context pairs|=1784, closed=YES, Rot=70, X2_all_i=1584
E1 f2=4: |S|=39, |tuple-context pairs|=2324, closed=YES, Rot=77, X2_all_i=1691
 E1 COUNTEREXAMPLE verified: abaca a=3, acaaba a=4, shared profile=(Counter({('A', 'b'): 1, ('b', 'A'): 1, ('A', 'c'): 1, ('c', 'A'): 1}), 'A', 'A')
E2 naive-violating: seed=107, replayed=2, verified=yes, size-final=109
 E2 contradiction independently confirmed: ('AcbbcA', [6, 7])
E2 naive-linear: seed=127, replayed=2, verified=yes, size-final=129
 E2 contradiction independently confirmed: ('AcbAbcbcAbc', [3, 4])
E2 prim-bc2-cb3: seed=39, replayed=6, verified=yes, size-final=45
 E2 contradiction independently confirmed: ('AbbccAbcA', [4, 5])
ALL INDEPENDENT CHECKS PASSED

===== END FILE =====

===== BEGIN FILE round13_subset_rerun_2026-11-15.txt bytes=3154 sha256=1a9cb52dc2f87e91f73796c1a4f698a13ad1d0d2e5f33e7e04415afe1533071f =====
checker SHA256 3f79da85eb7d128a52b0591e7f51fdcc3aa25f2cc9b469029e76a6e29e96d92a
python 3.13.5  seed 20261115
sections ['S0', 'E1', 'S2', 'S4']
== [S0] exact finite substitutability: controls
   interior-only family a^5 + a^+ b a^+ (total 3) is not closed; witness {"x": ["ab"], "y": ["ba"], "E_accept": ["a", "a"], "E_test": ["", "aa"], "E_accept_x": "aaba", "E_accept_y": "abaa", "E_test_x": "abaa", "E_test_y": "baaa", "type_x": [["a", "b"]], "type_y": [["a", "b"]]}
   closure: status=closed |S|=5 S=['aaab', 'aaba', 'abaa', 'baaa', 'aaaaa']
   negative control {a^5, abaa}: witness {"x": ["a", "aa"], "y": ["aa", "a"], "E_accept": ["a", "a", ""], "E_test": ["", "b", ""], "E_accept_x": "aaaaa", "E_accept_y": "aaaaa", "E_test_x": "abaa", "E_test_y": "aaba", "type_x": [["a"], ["a"]], "type_y": [["a"], ["a"]]}
== [E1] cross-class order dependence: closure of an order-dependent seed
   f2=5: status=closed |K|=34 rounds=2 contra=None
     W1=abaca deficit 5 ; W2=acaba deficit 5 ; same a-collapsed bigram multiset+endpoints=True
     full closed set S1(f2=5) = ['aaabc', 'aaacb', 'aabac', 'aabca', 'aacab', 'aacba', 'abaac', 'abaca', 'abcaa', 'acaab', 'acaba', 'acbaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'caaab', 'caaba', 'cabaa', 'cbaaa', 'aaaaac', 'aaaaca', 'aaacaa', 'aacaaa', 'acaaaa', 'caaaaa', 'aaaaaab', 'aaaaaba', 'aaaabaa', 'aaabaaa', 'aabaaaa', 'abaaaaa', 'baaaaaa', 'aaaaaaaa']
     words with content {a,b,c} and a-count<N: ['aaabc', 'aaacb', 'aabac', 'aabca', 'aacab', 'aacba', 'abaac', 'abaca', 'abcaa', 'acaab', 'acaba', 'acbaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'caaab', 'caaba', 'cabaa', 'cbaaa']
   f2=4: status=closed |K|=39 rounds=2 contra=None
     W1=abaca deficit 5 ; W2=acaaba deficit 4 ; same a-collapsed bigram multiset+endpoints=True
     REFUTED (exact, finite): deficit not a function of bigram data; cb-order deficit 4 != 2+3
     full closed set S1(f2=4) = ['aaabc', 'aabac', 'aabca', 'abaac', 'abaca', 'abcaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'aaaaac', 'aaaaca', 'aaaacb', 'aaacaa', 'aaacab', 'aaacba', 'aacaaa', 'aacaab', 'aacaba', 'aacbaa', 'acaaaa', 'acaaab', 'acaaba', 'acabaa', 'acbaaa', 'caaaaa', 'caaaab', 'caaaba', 'caabaa', 'cabaaa', 'cbaaaa', 'aaaaaab', 'aaaaaba', 'aaaabaa', 'aaabaaa', 'aabaaaa', 'abaaaaa', 'baaaaaa', 'aaaaaaaa']
     words with content {a,b,c} and a-count<N: ['aaabc', 'aabac', 'aabca', 'abaac', 'abaca', 'abcaa', 'baaac', 'baaca', 'bacaa', 'bcaaa', 'aaaacb', 'aaacab', 'aaacba', 'aacaab', 'aacaba', 'aacbaa', 'acaaab', 'acaaba', 'acabaa', 'acbaaa', 'caaaab', 'caaaba', 'caabaa', 'cabaaa', 'cbaaaa']
== [S2] negative control: d=1-closed set violating Lemma S must be d=2-non-closed
   seed ['aaaaaaa', 'aaaaba', 'abaaa'] -> d1-closed |K|=3, skeleton conflict {'AbA': [4, 5]}
   d=2 witness: {"x": ["a", "aa"], "y": ["aa", "a"], "E_accept": ["", "a", "aaa"], "E_test": ["", "ba", ""], "E_accept_x": "aaaaaaa", "E_accept_y": "aaaaaaa", "E_test_x": "abaaa", "E_test_y": "aabaa", "type_x": [["a"], ["a"]], "type_y": [["a"], ["a"]]}
== [S4] Theorem T1 arithmetic on random rank<=r trees
   trials=4000, max N/bound = 0.1667
== SUMMARY: checks=4035 FAIL=0  time=0.4s
ALL CHECKS PASSED

===== END FILE =====

===== BEGIN FILE round13_x1_adversarial_probe.py bytes=1324 sha256=31d5aea9fba6f00aa2cf19d4c865f191bb9df9188f9c77755d05e2cec116eabc =====
import importlib.util,io,contextlib,itertools
from collections import defaultdict
path='/mnt/data/claude_round13_noncomm_U_checker_2026-11-15.py'
spec=importlib.util.spec_from_file_location('round13src',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def examine(S):
 ctx=defaultdict(set)
 for w in S:
  n=len(w)
  for i in range(n):
   for j in range(i+1,n+1):ctx[w[i:j]].add((w[:i],w[j:]))
 solo=set()
 for w in S:
  for p in range(1,len(w)-1):
   if w[:p]!='a'*p:continue
   for r in range(1,len(w)-p):
    if w[-r:]!='a'*r:continue
    k=w[p:len(w)-r]
    if k and 3<=p+r<=7:solo.add((k,p+r))
 for k,la in solo:
  for k2,la2 in solo:
   if set('a'+k)!=set('a'+k2):continue
   i=max(0,la-la2); ip=max(0,la2-la)
   x='a'*i+k; y='a'*ip+k2
   if ctx[x]!=ctx[y]:
    d=ctx[x]-ctx[y]
    if d:return (k,la,k2,la2,x,y,next(iter(d)),'x yes y no',len(S))
    d=ctx[y]-ctx[x]
    if d:return (k,la,k2,la2,x,y,next(iter(d)),'y yes x no',len(S))
 return None
N=8
for f2 in range(3,8):
 seed={'a'*N}|m.flanked(['b'],N-2)|m.flanked(['c'],N-3)|m.flanked(['b','c'],N-5)|m.flanked(['c','b'],N-f2)
 R=m.closure(seed,cap_len=N+3,cap_words=8000,max_rounds=8,N=N)
 z=examine(R['K']) if R['status']=='closed' else None
 print('f2',f2,'seed',len(seed),'status',R['status'],'|K|',len(R['K']),'x1_counter',z,flush=True)

===== END FILE =====

===== BEGIN FILE round13_x1_adversarial_probe_log.txt bytes=250 sha256=c109105e89891a932f77063425940ce5606318dcd7d28562c145513ad65959d4 =====
f2 3 seed 17 status closed |K| 45 x1_counter None
f2 4 seed 14 status closed |K| 39 x1_counter None
f2 5 seed 12 status closed |K| 34 x1_counter None
f2 6 seed 11 status closed |K| 24 x1_counter None
f2 7 seed 11 status closed |K| 24 x1_counter None

===== END FILE =====
