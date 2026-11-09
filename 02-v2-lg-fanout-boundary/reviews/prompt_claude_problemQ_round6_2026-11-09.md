# 探索依頼（第6回）：問題 Q（三文字の $\mu_{\mathtt a}$）の場合 III・分岐 (B) を閉じる（`op:fanout-two`）

（論文 #2「MCFL の正データ学習：局所群とファンアウトの境界」用。2026-11-09 作成。

- 第5回（剛性のある標的）で、予想 R の $|M|=1$ の場合が、2026-11-01 から続く**問題 Q** そのものであることが分かった。今回はその問題 Q に戻る。
- 方針は「一回に一区画ずつ削る」。主課題は **場合 III の分岐 (B)** に絞る。これは 2026-11-06 に Astra 向けに書いた依頼（README (171)）と同じ区画で、その報告はまだない。
- 余力があれば副課題（分岐 (S) の観察、第1〜5回の道具との関係）に進む。）

## 0. 資料と成果物

**リポジトリ.** https://github.com/growupkuriyama-hub/Papers （論文は `02-v2-lg-fanout-boundary/`）。個々のファイルは `https://raw.githubusercontent.com/growupkuriyama-hub/Papers/main/02-v2-lg-fanout-boundary/<パス>` で読める。

**読むもの**（優先順）。引用する補題は、**使う前にすべて自分で確かめること**。

1. `reviews/STATUS_sl_fanout2_2026-11-01.md`：問題 Q の全体の経緯。2026-11-01〜07 の追記を含む。
2. `reviews/chatgpt_case2_branches_2026-11-04.md`
   - §1：記号と推論規則 SUB₁・SUB₂。
   - §3：鍵の補題 (KL)。場合 III で強制されるのは端点の文字の四乗であるという付記を含む。
   - §4–§6：場合 II の分岐 (B)。共通の根、損失 $d_X=\varphi j_X$、**定理 II-B**。
   - §8：場合 III で残った $\mathtt b\cdots\mathtt{cc}\cdots\mathtt b$。
3. `reviews/claude_straddle_2026-11-04.md`
   - §1：記号。
   - §3.1：補題 F′（自己融合）と系 C（収縮）。
   - §3.2–3.4：殻、SB₂、補題 E₂、型板 T、入れ子 N。
   - §4.1：分岐 (B)・(S) の定義。
   - §4.2：損失の線形化。
4. `reviews/check_claude_case3_bfusion_2026-11-04.py`：場合 III の $\mathtt b$-融合の証明書。$\mathtt{bcccb},\mathtt{bccb},\mathtt{bcbcb}$ から $\mathtt c^4$ が強制される。
5. `reviews/prompt_astra_case3_branchB_2026-11-06.md`：同じ区画の前回の依頼。(O1)〜(O3) の詳しい形がある。
6. 原稿 `main.tex`
   - `def:tuple-substitutable`：arity 2 の文脈の穴の間は空でない。
   - `lem:thickness-equivalence`
   - `prop:zeta-capacity`（下の §2）

リポジトリが読めない場合は、§1・§2 の要約だけで作業し、引用元を確かめられなかったことを報告に明記すること。

**成果物.**

1. 報告 `claude_problemQ_round6_2026-11-09.md` を1本。
   - 冒頭に主張ごとの判定の表を置く。
     - 引用した主張の判定：独立に確認／誤り／確認できず。
     - 新しい主張の判定：証明済み／反証／観察／未解決。
   - 証明は省略しない。
2. スクリプト `check_claude_problemQ_round6_2026-11-09.py` を1本。
   - 標準ライブラリのみで、数分以内に終わること。
   - 推論は SUB₁・SUB₂ だけを使い、強制された語は各段を種から再生する証明書として出力する。

## 1. 設定（問題 Q）

### 基本の設定

- $\Sigma=\{\mathtt a,\mathtt b,\mathtt c\}$ とし、型付けは内容型付け $c$ とする（語は現れる文字の集合に写り、組は成分ごとに写る）。
- $L\in\mathcal C_{2,c}$ とする。つまり arity 1 と 2 で $(2,c)$-タプル代入可能な 2-MCFL である。
- $G$ は $L\cap\Sigma^+$ の既約で良い表示で、ファンアウト $\le2$、ランク $\le r$ とする。$v=|V|$、$\theta=\bar\theta_G$ とおく。
- $k:=\mu_{\mathtt a}(L)=\min\{j:\mathtt a^j\in L\}\ge5$ とし、$T$ を $\mathtt a^k$ の導出木のうち節点数最小のもの（一様にとれる）とする。

**問題 Q.** $\mu_{\mathtt a}(L)\le\mathrm{poly}_r(v,\theta)$ か。

これは `op:fanout-two` の否定の候補が必ず通る核である。稀な型 $\{\mathtt a\}$ の場合にあたり、内容 $\{\mathtt a\}$ では剛性は自動的に成り立つ。

### 推論規則 SUB$_t$（$t=1,2$）

次の4つがすべて成り立つとき、$H[Y]\in L$ が従う。

- $E,H$ は許容文脈で、二穴の間の固定部分は空でない。
- $X,Y$ は各成分が空でない組で、成分ごとの内容が等しい。
- $E[X],E[Y]\in L$。
- $H[X]\in L$。

### 場合の分け方

- **場合 I**：$\mathtt b^4$ と $\mathtt c^4$ がともに $L$ の語に現れる。**定理 I** により $\mu_{\mathtt a}\le\max\{4\theta+12,K_I^{313}R^{312}\theta\}$ が成り立つ。Claude と ChatGPT が独立に検証済みで、**閉じている**。
- **場合 II**：どちらも現れない。
- **場合 III**：$\mathtt b^4$ だけが現れる（$\mathtt c^4$ だけの場合は対称）。

### 分岐

- **低い両文字型ラベル** $X$：短い代表 $\rho_X$（総長 $\le\theta$）が $\mathtt b,\mathtt c$ の両方を含み、損失 $d_X=\ell_X-|\rho_X|_{\mathtt a}$ が小さいもの。詳しくは `claude_straddle` §1・§4.1。
- **塊** $F_X$：$\rho_X$ の $\mathtt a$ を含まない因子をつないだ語。
- **SB$(F,d)$**：$s,t\ge1$、$s+t=k-d$ をみたすすべての $s,t$ について $\mathtt a^sF\mathtt a^t\in L$。
- **分岐 (B)**：二塊の語 $\mathtt a^{s_0}P\mathtt a^{s_1}Q\mathtt a^{s_2}\in L$（$P,Q$ は低い塊で SB をもつ）がある場合。このとき塊の任意の鎖が SB をもつ。
- **分岐 (S)**：そうでない場合。関係のあるラベルは、すべて両側型で型板をもつ。

### 分かっていること

- **場合 II・分岐 (B)**：**定理 II-B** により $\mu_{\mathtt a}\le\max\{4\theta+12,K_B^{10}R^9\theta\}$ が成り立つ。ここで $E_B=v(50\theta^3+\theta+23)$、$K_B=(2v+E_B)(2r+1)$、$R=\theta+2v+2$。ChatGPT が導き、Claude が検証した。
  - 鍵の補題 (KL)：$\mathtt{bb}$ か $\mathtt{cc}$ を含む塊は四乗を強制する。これで低い塊はすべて $(\mathtt{bc})^j$ か $(\mathtt{cb})^j$ になり、根は一つである。
- **場合 III で排除済みのもの**：$\mathtt{cc}$ を含み、少なくとも一端が $\mathtt c$ の塊。
- **場合 III で残っているもの**：両端が $\mathtt b$ で、内部に $\mathtt{cc}$ がある塊。最小の例は $\mathtt{bcccb}$。
- **未解決**：場合 II・III の分岐 (S)、場合 III の分岐 (B)。

## 2. 第1〜5回（2026-11-09）で得た、使えるかもしれない事実

以下はすべて検証済みである。$M=\{\mathtt a\}$ に当てはめた形で書く。

- **`prop:zeta-capacity`／定理 M$_\beta$**：$\mu_{\mathtt a}\le(1+\min\{\kappa,2\beta\})\,v(\rho_{\max}+r\theta)$。
  - $\kappa$ は語あたりの $\mathtt b,\mathtt c$ の最大個数、$\beta$ は語あたりの、$\mathtt a$ を含まない極大な塊の最大数である。
  - したがって問題 Q の反例では、塊の数 $\beta$ が超多項式でなければならない。
  - 代入可能性は使わない。
- **補題 T1（周期をまたぐ移送）**：$x_1rx_2$（$r=tv=vs$）が $L$ の語の因子で、$c(t)\subseteq c(x_1)\cap c(x_2)$ のとき、すべての $w_{\mathrm L},w_{\mathrm R}$ と $w_{\mathrm M}\ne\varepsilon$ について
  $$w_{\mathrm L}x_1t\,w_{\mathrm M}\,x_2w_{\mathrm R}\in L\iff w_{\mathrm L}x_1w_{\mathrm M}sx_2w_{\mathrm R}\in L.$$
  補題2.1（weighted_codes の $x^4$ による移送）は $r=x^2$ の特殊な場合である。T1 は長さと Parikh ベクトルを保つ。
- **補題 E**：剛性のある語の導出木で、比較不能・同じラベル・同じ長さの節点は、同じ組を生成する。$|M|=1$ では、これは既知の一様性 (U) と同じである。
- **補題 Q（第5回）**：$c(s)\subseteq c(y)$ で、$yy\,s\,yy$ の後にもう一度 $yy$ が来れば $sy=ys$。ただし $M=\{\mathtt a\}$ では $y,s$ が $\mathtt a$ の冪なので自明になり、**問題 Q には直接は効かない**。

## 3. 課題

### 課題1（主）：場合 III・分岐 (B) を閉じる

前回の依頼の (O1)〜(O3) を確かめ、証明する。

**(O1) 補題 F′ の文字の置き換え.**

- `claude_straddle` §3.1 の補題 F′ と系 C を、$\mathtt a$ を $\mathtt b$ に置き換えて読み直す。
- 次の3つの仮定で十分かを確かめる。
  - $\mathtt b^4$ が出現すること。
  - $\mathtt b$ の個数が、$\mathtt b$ の極大連の数 $+1$ 以上であること。
  - 置き換える部分が $\mathtt b$ で始まらないこと。
- 証明が $\mu_{\mathtt a}$、SB、場合 I に固有の性質を使っていないかを確かめる。

**(O2) $\mathtt b$-融合による排除.**

場合 III で、$\mathtt a$ を含まない塊 $F$ が次の3つをみたすとする。

- SB$(F^2,2d)$ をみたす。
- $\mathtt c$ を2つ以上含む。
- $\mathtt{bb}$ を含むか、両端がともに $\mathtt b$ である。

このとき F′ を繰り返して $\mathtt c$ の間の $\mathtt b$ の連を消すと、$\mathtt c^4$ を含む語が $L$ に入り、場合 III に矛盾する（例：$\mathtt{bcccb}\cdot\mathtt{bcccb}\to\mathtt{bb\,ccc\,ccc\,b}$）。

**一般の長さの塊について証明すること。** 証明の方法は次のどちらでもよい。

- F′ による直接の証明。
- 抽象的な文字の基礎の証明書を作り、準同型で持ち上げる。

**(O3) 共通の根.**

(KL)、前報 §8、(O2) を合わせると、場合 III の分岐 (B) で残る低い塊は $(\mathtt{bc})^j$、$(\mathtt{cb})^j$ と、$\mathtt c$ を一つだけ含む $\mathtt b^i\mathtt c\mathtt b^j$ になるはずである。次を確かめる。

- 鎖を塊として使うとき、どの冪まで SB が要るか。前報 §4 の予算で足りるか。
- 同じラベルの鎖 $F_XF_X$ も使えるか。
  - 使えるなら、$\mathtt b^i\mathtt c\mathtt b^j$ のうち $\mathtt{bc}$、$\mathtt{cb}$ 以外は消え、低い塊はすべて**一つの根 $u\in\{\mathtt{bc},\mathtt{cb}\}$ の冪**になる。
  - 使えないなら、$\mathtt c$ が一つの塊（例 $\mathtt{bcb}$）が根として残る。その場合も、すべての塊が一つの根の冪 $u^j$ になり、前報 §5 の損失の線形化が使えるかを確かめる。
- 前報 §6.2 の一色型の数え方（二文字の影の飽和／非飽和）が場合 III でも成り立つか。$\mathtt b^4$ が現れることで変わる点はないか。

**目標.**

> **定理 III-B（候補）.** 場合 III の分岐 (B) で $\mu_{\mathtt a}(L)\le\max\{4\theta+12,\ K^{10}R^{9}\theta\}$。$K,R$ は $\mathrm{poly}(v,\theta,r)$ で明示する。

- 定理 II-B と同じ形になるかを確かめる。
- 定数が変わるなら、変わった箇所と理由を示す。

### 課題2（副）：分岐 (S) について一点だけ

課題1が閉じたら（閉じなくても時間があれば）、場合 III の分岐 (S) について次の一点を調べる。

- 殻の中でも (O1) の $\mathtt b$-融合が使えるか。
- 殻の各側の骨格（$\mathtt b$ の連を縮めたもの）が交代語になり、`claude_straddle` の補題 Q（34個の細類）のように少数の類に分かれて損失が線形になるか。

結論が出なくても、止まった段を特定すればよい。

### 課題3（副）：塊の数の観点

`prop:zeta-capacity`（定理 M$_\beta$）により、問題 Q の反例には超多項式個の塊が要る。分岐 (B) と分岐 (S) の定義で、塊の数 $\beta$ がどう現れるかを整理する。そのうえで、次のどちらかを示せるかを試す。

- 「分岐 (S) では $\beta$ が多項式で抑えられる」。
- その逆の構成（$\beta$ が超多項式になる分岐 (S) の例）。

## 4. 計算（任意）

- 推論は SUB₁・SUB₂ だけを使い、各段を種から再生して検査する。
- 強制された語は証明書として扱い、見つからないことは観察として扱う。
- 有限の検査の結果から、無限の族の代入可能性を推定しない。
- `check_claude_case3_bfusion_2026-11-04.py` を土台にしてよい。

## 5. 守ってほしいこと

範囲を超えて書かない。具体的には次の4点を守る。

- 分岐 (B) の結果を分岐 (S) に広げて書かない。
- 場合 III の結果を場合 II に広げて書かない。
- $\mu_{\mathtt a}$ の結果を $\tau$（代表の長さ）や `op:fanout-two` そのものに広げて書かない。
- (O2) で消えるのは「$\mathtt c$ を4つ以上つなげられる塊」であって、場合 III 全体ではない。

その他：

- 「境界がファンアウトで動く」とは書かない。
- 新しい結果が文献で既知かどうかを、分かる範囲で書く。分からなければ「未確認」と書く。

閉じられない場合は、次の3つを書いて終える。

- 証明できたこと。
- 止まった場所（どの塊の型か、どの補題のどの段か）。
- 次に絞るべき一点。
