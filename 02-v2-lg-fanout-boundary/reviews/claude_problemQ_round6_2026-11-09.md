# 問題 Q・第6回：場合 III・分岐 (B) を閉じる（`op:fanout-two` の三文字の核の一区画）

**研究日**：2026-11-09
**依頼文**：`reviews/prompt_claude_problemQ_round6_2026-11-09.md`（2026-11-09 作成）
**資料**：公開リポジトリ `growupkuriyama-hub/Papers` を取得（commit `05d915e`、2026-11-09 20:37 JST）。`main.tex`（`def:tuple-substitutable`、その直前の許容文脈 $\mathcal E_d$ の定義、`lem:thickness-equivalence`、`prop:zeta-capacity`、`lem:app-two-runs`、`lem:app-two-alternate`）、`reviews/STATUS_sl_fanout2_2026-11-01.md`、`chatgpt_case2_branches_2026-11-04.md`（全文）、`claude_straddle_2026-11-04.md`（§0–§6）、`check_claude_case3_bfusion_2026-11-04.py`、`prompt_astra_case3_branchB_2026-11-06.md`、`chatgpt_nested_bc_chain_2026-11-04.md`（§1–§3）、`claude_fanout2_transfer_round4_2026-11-09.md`（§3.1、定理 M$_\beta$）を直接読んだ。
**スクリプト**：`check_claude_problemQ_round6_2026-11-09.py`（標準ライブラリのみ、この環境で約5秒）。出力は §9 にそのまま載せた。
**立場**：研究ノートである。書いたのも確かめたのも Claude で、独立の検証ではない。

**要点.** **場合 III の分岐 (B) は閉じた**（定理 III-B）。上界の形も定数も定理 II-B と同じで、$\mu_{\mathtt a}(L)\le\max\{4\theta+12,K_B^{10}R^9\theta\}$ となる。鍵は次の二つである。

- $\mathtt b$ による自己融合 F′$_{\mathtt b}$ が使える。$\mathtt b^4$ が現れることと「余分な $\mathtt b$」（$\mathtt b$ の個数 $\ge$ $\mathtt b$ の極大連の数 $+1$）があることだけを仮定する。
- 分岐 (B) では、同じラベルの鎖 $F_XF_X\cdots$ も SB をもつ。

この二つで、低い塊のうち少なくとも一端が $\mathtt b$ で余分な $\mathtt b$ をもつもの（$\mathtt{bcccb}$、$\mathtt{bcb}$、$\mathtt{cbb}$ など）は $F^4$ から $\mathtt c^4$ を強制する。少なくとも一端が $\mathtt c$ のものは (KL) が $\mathtt c^4$ を強制する。その結果、残る低い塊は**ただ一つの根 $u\in\{\mathtt{bc},\mathtt{cb}\}$ の冪**だけになる。依頼文 (O3) が想定した「$\mathtt c$ が一つの塊（$\mathtt{bcb}$ など）が根として残る」場合は起こらない。

途中で、分岐 (B) の定義に足りない点が一つ見つかった。二塊の語の $\mathtt a$ の個数が $k-d_P-d_Q$ であることを、定義に含める必要がある（§2.3）。分岐 (S) については、入れ子の語の $\mathtt b$ の連が全て長さ 1 になることまでは示せた。止まったのは $\mathtt c$ の連の長さのところである（§7）。

---

## 0. 主張ごとの判定

### 0.1 引用した主張

| 主張（出典） | 判定 | 根拠・限定 |
|---|---|---|
| 推論規則 SUB$_1$・SUB$_2$（`chatgpt_case2_branches` §1、原稿 `def:tuple-substitutable`） | **独立に確認** | §1.1。二穴の中央の固定部分が空でないことは、原稿の $\mathcal E_d$ の定義（$v_1\in\Sigma^+$）から来る |
| 補題2.1・系2.2（$x^4$ による連の移送と再配分。`claude_straddle` §1） | **独立に確認**（$x=\mathtt a,\mathtt b$） | §1.2 |
| 補題 F′・系 C（`claude_straddle` §3.1） | **独立に確認** | §1.3。$\mathtt a$ を他の文字に置き換えても証明は同じ |
| 定理S（同じ $\mathtt a$ 骨格の二語の $\mathtt a$ の個数の差は $(0,k)$ に入らない） | **独立に確認** | §1.4 |
| (KL) の五つの基礎証明書と準同型による持ち上げ（`chatgpt_case2_branches` §1–§3、付録A） | **独立に確認** | 基礎証明書のデータをこのファイルの検査器で再生した（§9 [1]）。持ち上げの健全性の議論は §1.5 で読み直した |
| (KL) の付記（場合3で強制されるのは端点の文字の四乗） | **独立に確認** | §1.5 |
| 「分岐 (B) では塊の任意の鎖が SB をもつ」（`chatgpt_case2_branches` §4 (ii)、`claude_straddle` 補題 P*） | **独立に確認。ただし定義に一点の補いが要る** | §2。二塊の語の $\mathtt a$ の個数が $k-d_P-d_Q$ であることを定義に含める（補題 T・V から出る語はこれをみたす）。同じラベルの繰り返しも許される |
| 低い内部ラベル $X$ が SB$(F_X,d_X)$ をもつこと（`claude_straddle` §2.3、系 C） | **独立に確認**（F′ の部分） | 「内部」の定義と $\mathtt a$ の連の数 $\le\theta+1$ は既報どおりに使った |
| 補題 5.1 の論法（$d_X=\varphi j_X$、`chatgpt_case2_branches` §5） | **独立に確認** | §4。定理S だけを使い、(R) は使わない。場合 III でもそのまま成り立つ |
| 一色型の数え方（`chatgpt_nested_bc_chain` §3.1–3.2 → `chatgpt_case2_branches` §6.2） | **独立に確認**（場合 III への適用） | §5.2。非飽和の場合の論法は、$L_x$ に $x^4$ が現れる場合と現れない場合の両方を扱っている。$\mathtt b^4$ が現れても何も変わらない |
| 尺度補題 3.1・3.2（第十一報。`claude_straddle` §1 で読み直し済み） | **確認できず（本報では読み直していない）** | 定理 II-B と同じ形で仮定を満たすことだけを確かめた（§5） |
| 補題 N（入れ子、`claude_straddle` §3.4） | **確認できず（証明を読んだのみ）** | §7 と §8 だけで使う。定理 III-B には使わない |
| 定理 M$_\beta$（`claude_fanout2_transfer_round4` §3.1） | **独立に確認**（証明を読んだ） | §8 |

### 0.2 新しい主張

| 主張 | 判定 | 節 |
|---|---|---|
| **(O1)** 補題 F′$_{\mathtt b}$（とその鏡像）は、$\mathtt b^4$ の出現・余分な $\mathtt b$・消す連の極大性だけで成り立つ。$\mu_{\mathtt a}$、SB、場合 I は使わない | **証明済み** | §1.3 |
| **補題 B-del**：余分な $\mathtt b$ のある語では、生き残る $\mathtt b$ の連を一つ残せば、他の $\mathtt b$ の連を任意に消せる | **証明済み** | §1.3 |
| **(O2)**（少なくとも一端が $\mathtt b$ の塊）：$\mathtt a^sF^2\mathtt a^t\in L$ の語が一つあれば、$\mathtt c$ を2つ以上含み「$\mathtt{bb}$ を含むか両端が $\mathtt b$」の塊 $F$ は $\mathtt c^4$ を強制する | **証明済み** | §3.1 |
| (O2)（両端が $\mathtt c$ の塊） | SB$(F^2)$ だけでは**未解決**。分岐 (B) の中では (KL) で証明済み | §3.1。$\mathtt{cbbc}$ には SB$(F)$・SB$(F^2)$ だけからの3段の証明書がある。$\mathtt{cbbbc}$ は打ち切りの探索で見つからなかった（観察） |
| **鎖の補題**：分岐 (B*) では、内容 $\{\mathtt b,\mathtt c\}$ の SB の塊の任意の列（繰り返しを許す）の連結が、損失の和で SB をもつ。任意の二つは正の全配分で離して並べられる | **証明済み** | §2 |
| **補題 III.1**：場合 III・分岐 (B*) の低い内部の塊は全て $(\mathtt{bc})^j$ か $(\mathtt{cb})^j$ | **証明済み** | §3.2 |
| **補題 III.2**：根は一つ | **証明済み**（二通りの証明） | §3.3 |
| **定理 III-B**：$\mu_{\mathtt a}\le\max\{4\theta+12,K_B^{10}R^9\theta\}$（$E_B,K_B,R$ は定理 II-B と同じ） | **証明済み**（尺度補題 3.1・3.2 と例外の数え方に依存する合成定理） | §5 |
| **補題 B-cap**：場合 III で、余分な $\mathtt b$ をもつ受理語の $\mathtt a$ を含まない極大因子は、どれも $\mathtt c$ を6個以下しか含まない | **証明済み** | §6 |
| **命題 S-III**：場合 III で、型板をもつ両側型ラベルの入れ子の語では、$\mathtt b$ の連が全て長さ1である（殻の両側に $\mathtt{bb}$ がない、両端が $\mathtt b$ でない、など） | **証明済み**（補題 N に依存） | §7.1 |
| 命題 S-III-cond：さらに入れ子が $\mathtt c$ の連も長さ1（交代語）なら、細類ごとに損失は1変数の線形関数 | **証明済み**（条件付きの含意） | §7.2 |
| 場合 III・分岐 (S) の多項式上界 | **未解決** | §7.3。止まったのは殻の中の $\mathtt{cc}$ |
| **命題 β**：小さい損失の塊・殻は、塊の多い語を強制する（(B) では $\beta(L)\ge\lfloor (k-1)/(d_X+2)\rfloor$、型板をもつ殻では $\beta(L)\ge2\lfloor k/(4d_X+4)\rfloor$） | **証明済み**（後者は補題 N に依存） | §8 |
| 「分岐 (S) では $\beta$ が多項式」／その逆の構成 | **未解決** | §8 |
| 新しい結果の文献上の新規性 | **未確認** | §10 |

---

## 1. 記号と基本の道具

### 1.1 設定と推論規則

- $\Sigma=\{\mathtt a,\mathtt b,\mathtt c\}$ とする。$c(w)$ は語 $w$ に現れる文字の集合で、組には成分ごとに適用する。
- $L\in\mathcal C_{2,c}$ とし、$k=\mu_{\mathtt a}(L)\ge5$ とする。
- **場合 III**：ある受理語が $\mathtt b^4$ を因子にもち、どの受理語も $\mathtt c^4$ を因子にもたない。
- 許容文脈は $\mathcal E_1=\{u\square v\}$ と $\mathcal E_2=\{v_0\square_1v_1\square_2v_2: v_1\ne\varepsilon\}$ である（原稿 `def:tuple-substitutable` の直前の定義）。
- 内容が成分ごとに等しく、分布が交わる組は、分布が等しい。

ここから **SUB$_t$** が出る。$E,H\in\mathcal E_t$、$X,Y\in(\Sigma^+)^t$、$c(X_i)=c(Y_i)$ とする。このとき
$$E[X],E[Y],H[X]\in L\ \Longrightarrow\ H[Y]\in L.$$
$E$ が $X,Y$ の両方を受理するので分布が交わり、したがって分布が等しく、$H$ も $Y$ を受理するからである。以下の推論は全てこの二つの規則の具体例である。スクリプトは各段をこの形で記録し、種から再生する。

### 1.2 連の移送（補題2.1・系2.2）

**補題2.1.** $x\in\Sigma$ とし、$x^4$ がある受理語 $px^4q$ の因子として現れるとする。このとき、任意の $U,V$ と空でない $Z$ について
$$UxZxxV\in L\iff UxxZxV\in L.$$

**証明.** 文脈 $p\square_1x\square_2q\in\mathcal E_2$ は $(x,xx)$ と $(xx,x)$ をどちらも $px^4q$ に写す。二つの組の型はどちらも $(\{x\},\{x\})$ なので、arity 2 の分布が等しい。$Z\ne\varepsilon$ なので $U\square_1Z\square_2V\in\mathcal E_2$ であり、主張が従う。∎

この補題では、$Z$ の中身（$x$ を含むか、$\mathtt a$ を含むか）は関係しない。

**系2.2.** $w\in L$ の $x$ の極大連の長さは、総数を保ち各連を $\ge1$ に保つ限り、自由に配り直せる。

**証明.** 長さ $\ge2$ の連から別の連へ $x$ を一つ移す操作が補題2.1 である。連が極大なので、二つの連の間の語は空でない。成分が正の二つの組成は、この操作の列で互いに移り合う。∎

$\mathtt a$ については $\mathtt a^k$（$k\ge4$）から $\mathtt a^4$ が現れ、場合 III では $\mathtt b$ についても使える。

### 1.3 (O1)：自己融合 F′$_x$ とその鏡像

**補題 F′$_x$.** $x\in\Sigma$ で $x^4$ が現れるとする。$W\in L$ の $x$ の極大連 $R_S$、$R_D$（$R_S$ が左）があり、$W$ の $x$ の個数が $x$ の極大連の数 $+1$ 以上だとする。このとき、$R_D$ を取り除き、$R_S$ の長さを取り除いた $x$ の分だけ増やした語は $L$ に入る（他の $x$ の連の長さも配り直してよい）。

**証明.**

1. 系2.2 で、$R_D$ を長さ1にし、$R_S$ を長さ $\ge2$ にする（余分な $x$ があるので可能）。この語を
   $$W_1=U\,xx\,u\,x\,V$$
   と書く。$xx$ は $R_S$ の最後の2文字、$x$ は $R_D$、$u$ はその間の語で空でない。$R_D$ は極大なので、$V$ は $x$ で始まらない。
2. 補題2.1 で $R_S$ から $R_D$ へ $x$ を一つ移すと、$W_2=U\,x\,u\,xx\,V\in L$。
3. SUB$_1$ を、$E=(U,\ xV)$、$X=xux$、$Y=xxu$、$H=(Ux,\ V)$ で使う。
   - $E[X]=Uxuxx V=W_2$
   - $E[Y]=Uxxux V=W_1$
   - $H[X]=Uxxux V=W_1$
   - $c(X)=c(Y)=\{x\}\cup c(u)$
   
   したがって $H[Y]=Ux\,xxu\,V\in L$。この語では $R_D$ が消え、$R_S$ が1つ長くなっている。∎

**鏡像 F′$_x{}^R$**（$R_S$ が右）。$W_1=U\,x\,u\,xx\,V$（$x$ が $R_D$、$xx$ は $R_S$ の最初の2文字、$U$ は $x$ で終わらない）とする。補題2.1 で $W_2=U\,xx\,u\,x\,V$ を得る。SUB$_1$ を $E=(Ux,\ V)$、$X=xux$、$Y=uxx$、$H=(U,\ xV)$ で使い、$U\,uxx\,xV\in L$ を得る。

**(O1) の答え.** 依頼の三つの仮定で十分である。

- $\mathtt b^4$ の出現は、補題2.1 の種として使う。
- 「$\mathtt b$ の個数 $\ge$ 連の数 $+1$」は、系2.2 で $R_S\ge2$、$R_D=1$ にするために使う。
- 「消す部分の右（鏡像では左）が $\mathtt b$ で始まらない（終わらない）」は、$R_D$ が極大であることにあたる。

証明が使うのは、補題2.1（$x^4$ の種一つ）と SUB$_1$ だけである。$\mu_{\mathtt a}$、SB、$\mathtt a$ の存在、場合 I、語が $\mathtt b$ で始まり終わることは、どれも使わない。$u$ は $\mathtt a$ を含んでもよい。原稿の `lem:app-two-runs` (i) の論法と同じ種類の操作である。

**補題 B-del（反復）.** $x^4$ が現れ、$W\in L$ の $x$ の個数が連の数 $+1$ 以上だとする。$W$ の $x$ の極大連の空でない集合 $\mathcal D$ で、その補集合も空でないものをとる。このとき、$\mathcal D$ の連を全て消し、$x$ の総数を残りの連に（各 $\ge1$ で）任意に配った語は $L$ に入る。

**証明.** 補集合から連 $R_S$ を一つ固定する。$\mathcal D$ の連を一つずつ、F′$_x$（$R_S$ が左のとき）か鏡像（右のとき）で消す。消した連の両隣は $x$ 以外の文字なので、消しても他の $x$ の連は合わさらない。各段で連の数は1減り、$x$ の総数は変わらないので、「個数 $\ge$ 連の数 $+1$」は保たれる。最後に系2.2 で配り直す。∎

### 1.4 定理S

二語 $w_1,w_2\in L$ が同じ $\mathtt a$ 骨格をもち（$\mathtt a$ の連を一文字に縮めた語が等しい）、$\mathtt a$ の個数を $n_1<n_2$、$\delta=n_2-n_1$ とする。このとき $0<\delta<k$ は起こらない。

**証明.** 系2.2 で、両語の $\mathtt a$ の連を一つ $R$ を除いて全て長さ1にする。すると $w_1=U\mathtt aV$、$w_2=U\mathtt a^{1+\delta}V$ と書ける。

- 文脈 $U\square V$ が $\mathtt a$ と $\mathtt a^{1+\delta}$ をともに受理する。両者は型 $\{\mathtt a\}$ が等しいので、分布が等しい。
- $1+\delta\le k$ なので、$\mathtt a^k=\mathtt a^{k-1-\delta}\cdot\mathtt a^{1+\delta}$ の $\mathtt a^{1+\delta}$ を $\mathtt a$ に替えると、$\mathtt a^{k-\delta}\in L$。

これは $k$ の最小性に反する。∎

スクリプト [5] はこの議論の具体例を、SUB の段として再生する。

### 1.5 (KL) とその持ち上げ

**(KL) の種.** 塊 $F\in\{\mathtt b,\mathtt c\}^+$（両文字を含む）と $d\ge1$、$k\ge6d$ について、次の語の集合を (KL) の種と呼ぶ。

- $\mathtt a^k$
- $j=1,2,3$ について、$\mathtt a^sF^j\mathtt a^t$（$s,t\ge1$、$s+t=k-jd$）の全て
- $\mathtt a^pF\mathtt a^qF\mathtt a^r$（$p,q,r\ge1$、$p+q+r=k-2d$）の全て

**(KL) の結論.** $F$ が $\mathtt{bb}$ か $\mathtt{cc}$ を含めば、次のように四乗が強制される。

| 形 | 強制される四乗 | 用いる型板 |
|---|---|---|
| $F=xxU$ | $x^4$ | $\mathtt{bbc}$ |
| $F=Uxx$ | $x^4$ | $\mathtt{bcc}$ |
| $F=zUz$（両端が同じ文字） | 端点の文字 $z$ の $z^4$ | $\mathtt{bcb}$ |
| $F=xPxxQ$、$PxxQx$（$P,Q\ne\varepsilon$） | $x^4$ | $\mathtt{xpxxq}$、$\mathtt{pxxqx}$ |

**持ち上げの健全性（読み直した）.** $h$ を非消去の準同型とし、$h(\mathtt a)=\mathtt a^d$ とする。文脈の像を $E'=(\mathtt a^{k-6d}h(e_0),h(e_1),\dots)$ とおくと、次が成り立つ。

- $E'[h(X)]=\mathtt a^{k-6d}h(E[X])$。
- 中央の $h(e_1)$ は空でない（非消去）。
- $c(h(u))=\bigcup_{z\in c(u)}c(h(z))$ なので、内容の一致は保たれる。
- 基礎の種（$k=6$、$d=1$）の像は、$F$ の (KL) の種に入る。例えば $\mathtt a^sB^j\mathtt a^{6-j-s}\mapsto\mathtt a^{k-6d+ds}F^j\mathtt a^{d(6-j-s)}$ で、$\mathtt a$ の個数は $k-jd$、両端の連はどちらも正である。

五つの基礎証明書は、このファイルの検査器で再生した（§9 [1]）。

**場合 III での帰結.** $\mathtt c^4$ が強制されるのは、次の三つの場合である。

- $F$ が $\mathtt{cc}$ で始まるか終わる。
- 両端が $\mathtt c$ である（$\mathtt{bcb}$ 型、$z=\mathtt c$）。
- 一端が $\mathtt c$ で、他端は $\mathtt b$、内部に $\mathtt{cc}$ がある。$F=\mathtt cP\mathtt{cc}Q$ と書くと、$F$ が $\mathtt{cc}$ で始まらないので $P\ne\varepsilon$、$F$ が $\mathtt b$ で終わるので $Q\ne\varepsilon$。$F=P\mathtt{cc}Q\mathtt c$ も同様である。

まとめると、**少なくとも一端が $\mathtt c$ で $\mathtt{cc}$ を含む塊と、両端が $\mathtt c$ の塊は、(KL) の種があれば $\mathtt c^4$ を強制する。** これは既報 §8 の結論と一致する。

---

## 2. 分岐 (B) の鎖の補題

### 2.1 交換（補題E）

**補題E.** $P,C$ を $\mathtt a$ を含まない空でない語で $c(P)=c(C)$ とし、SB$(P,d_P)$、SB$(C,\delta)$ をみたすとする。$d_P,\delta\le k-2$ とする。

- $\delta\ge d_P$ なら $D(\mathtt a^{1+\delta-d_P}P)=D(\mathtt aC)$。
- $\delta<d_P$ なら $D(\mathtt aP)=D(\mathtt a^{1+d_P-\delta}C)$。

**証明.** 前者だけ示す（後者も同じ）。

- 文脈 $\square\,\mathtt a^{k-\delta-1}$ は $\mathtt a^{1+\delta-d_P}P$ を、$\mathtt a$ の個数 $k-d_P$ で両端の連が正の語に写す。SB$(P)$ によりこれは $L$ に入る。
- 同じ文脈は $\mathtt aC$ を、個数 $k-\delta$ の語に写す。SB$(C)$ によりこれも $L$ に入る。
- 型はどちらも $\{\mathtt a\}\cup c(P)$ である。∎

### 2.2 鎖

**分岐 (B*) の定義.** 次の語が存在する場合を分岐 (B*) と呼ぶ。
$$W_0=\mathtt a^{s_0}P\mathtt a^{s_1}Q\mathtt a^{s_2}\in L,\qquad s_i\ge1,\qquad \mathtt a\text{ の個数 } k-d_P-d_Q.$$
ここで $P,Q$ は $\mathtt a$ を含まず $\mathtt b,\mathtt c$ をともに含み、SB$(P,d_P)$、SB$(Q,d_Q)$、$d_P,d_Q\le k/(2N)$（$N=25\theta^3$）をみたす。

内容 $\{\mathtt b,\mathtt c\}$ の塊 $C$ で SB$(C,\delta)$ をもつものの対 $(C,\delta)$ を、**SB の塊**と呼ぶ。

**主張1（離れた二塊）.** 分岐 (B*) で、SB の塊 $(C,\delta)$、$(C',\delta')$ が $\delta+\delta'\le k-3$ をみたすとする（$C=C'$ でもよい）。このとき、全ての $p,q,r\ge1$、$p+q+r=k-\delta-\delta'$ について $\mathtt a^pC\mathtt a^qC'\mathtt a^r\in L$。

**証明.**

1. 系2.2 で $W_0$ の連を $(k-d_P-d_Q-2,1,1)$ にする。
2. 補題E で、$P$ の直前の $\mathtt a^{1+\max(0,\delta-d_P)}P$（または $\mathtt aP$）を、$\mathtt aC$（または $\mathtt a^{1+d_P-\delta}C$）に替える。$\mathtt a$ の個数は $k-\delta-d_Q$ になる。
   - $\delta-d_P\le k-d_P-d_Q-3$ なので、$P$ の直前の連は十分に長い。
3. 連を $(1,\ k-\delta-d_Q-2,\ 1)$ に配り直す。
4. 同じく $Q$ を $C'$ に替える。$\mathtt a$ の個数は $k-\delta-\delta'$ になる。
   - 中央の連の長さ $k-\delta-d_Q-2\ge1+\max(0,\delta'-d_Q)$ は、$\delta+\delta'\le k-3$ から出る。
5. 系2.2 で任意の正の配分 $(p,q,r)$ にする。∎

**主張2（融合）.** 同じ仮定で、さらに $\delta+\delta'\le k-4$ とする。このとき $(CC',\ \delta+\delta')$ は SB の塊である。

**証明.** 主張1 の語 $\mathtt a^{k-\delta-\delta'-2}C\mathtt a C'\mathtt a$ に、F′$_{\mathtt a}$ を適用する（$R_S$ は左の連、$R_D$ は中央の連）。

- $\mathtt a$ の個数 $k-\delta-\delta'\ge4$ は、$\mathtt a$ の連の数 $3$ に $1$ を足したもの以上である。
- 中央の連の右は $C'$ で、$\mathtt a$ で始まらない。

こうして $\mathtt a^{k-\delta-\delta'-1}CC'\mathtt a\in L$ を得て、系2.2 で任意の $(s,t)$ にする。∎

**系（鎖の補題）.** 分岐 (B*) で、SB の塊 $(C_1,\delta_1),\dots,(C_m,\delta_m)$（繰り返しを許す）が $\sum\delta_i\le k-4$ をみたせば、$C_1\cdots C_m$ は SB$(\cdot,\sum\delta_i)$ をもつ。どの二つの鎖も、損失の和が $k-3$ 以下なら、全ての正の配分で離して並べられる。∎

**(O3) の一点目の答え（同じラベルの鎖）.** 使える。主張1・2 は $C\ne C'$ を一度も使わない。したがって $F_X^m$ も SB$(F_X^m,md_X)$ をもつ。

### 2.3 分岐 (B) の定義について（補い）

`claude_straddle` §4.1 の分岐 (B) の定義は、二塊の語の $\mathtt a$ の個数を指定していない。

- **指定がないと、鎖の損失が足し算になることが出てこない。**
  - $W_0$ の個数が $n$ なら、上の論法で得られる $PP$ の損失は $k-n-d_Q+d_P$ である。
  - これが $2d_P$ であることを強制する仕組みは、見つからなかった。
- 一方、分岐 (B) の語が実際に生じる場所では、個数は $k-d_P-d_Q$ である。
  - 補題 T (i)(ii) では、同じラベルの二出現を同時に替えるので $k-2d_X$。
  - 補題V では $k-d_X-d_Y$。
  - 範囲の中の融合は個数を変えない。
- したがって、**(B) を (B*) に置き換えても、(B)/(S) の二分（分岐 (S) では関係のあるラベルは全て両側型で型板をもつ）はそのまま成り立つ。**

既報の補題 P*・定理 II-B は暗にこの個数を使っている。定理 II-B の結論は変わらないが、定義の文面を (B*) に直すことを勧める。

### 2.4 予算

本報で使う鎖は、次のとおりである。

| 用途 | 原子の数 |
|---|---|
| $F^4$（§3.2 (a)–(c)） | 4 |
| (KL) の種 $F^j$（$j\le3$）と離れた二塊 | 3 |
| 混ざった根の鎖 $(PQ)^2$ または $(QP)^j$（§3.3） | 8 以下 |
| $F_X^{j_Y}$（§4） | $\theta/2$ 以下 |

いずれも原子は $\max\{8,\lfloor\theta/2\rfloor\}\le24\theta^3$ 個以下で、既報 §4 の範囲に入る。損失の和は、低い塊について $8\cdot k/(50\theta^3)\le 4k/25$、または $(\theta/2)\cdot k/(50\theta^3)\le k/(100\theta^2)$ 以下である。したがって次の三つがすべて成り立つ。

- $\le k-4$（$k\ge5$ で $4k/25\le k-4$）
- $\le k/2$
- (KL) の $k\ge6\delta$（$6\cdot 2k/(50\theta^3)\le k$。(KL) を当てるのは原子2個以下の鎖だけ）

---

## 3. (O2) と低い塊の分類

### 3.1 (O2)

**命題 O2.** 場合 III とする。$F$ は $\mathtt a$ を含まず、$\mathtt c$ を $\gamma\ge2$ 個含み、$\mathtt{bb}$ を含むか両端がともに $\mathtt b$ であるとする。

**(a)** $F$ の少なくとも一端が $\mathtt b$ で、ある $s,t$ について $\mathtt a^sF^2\mathtt a^t\in L$ なら、$\mathtt c^4$ を含む語が $L$ に入る（矛盾）。

**(b)** 両端が $\mathtt c$ の場合、この方法は使えない。分岐 (B*) の中では、(KL)（$F=\mathtt cU\mathtt c$）で $\mathtt c^4$ が強制される。

**証明 (a).** $W=\mathtt a^sFF\mathtt a^t$ とおく。$\beta=|F|_{\mathtt b}$、$\rho=F$ の $\mathtt b$ の極大連の数、$J=[F$ が $\mathtt b$ で始まり $\mathtt b$ で終わる$]$ とすると、
$$|W|_{\mathtt b}=2\beta,\qquad W\text{ の }\mathtt b\text{ の連の数}=2\rho-J.$$

- $F$ が $\mathtt{bb}$ を含めば $\beta\ge\rho+1$ なので、$2\beta\ge2\rho+2\ge2\rho-J+1$。
- 両端が $\mathtt b$ なら $J=1$ で、$2\beta\ge2\rho=2\rho-J+1$。

どちらの場合も、余分な $\mathtt b$ がある。$F$ が $\mathtt b$ で始まるなら、$W$ の最初の $\mathtt b$ の連は $FF$ の最初の $\mathtt c$ より左にある（$\mathtt b$ で終わるなら、最後の連が最後の $\mathtt c$ より右にある）。これを生き残りとし、$FF$ の最初の $\mathtt c$ と最後の $\mathtt c$ の間にある $\mathtt b$ の連を全て、補題 B-del で消す。その区間は $\mathtt a$ を含まないので、$\mathtt c$ が $\mathtt c^{2\gamma}$ と一続きになる。$2\gamma\ge4$ である。∎

依頼の例 $\mathtt{bcccb}\cdot\mathtt{bcccb}\to\mathtt{bb\,cccccc\,b}$ は、この証明の2段の具体例である（§9 [2]）。

**(b) について.** 両端が $\mathtt c$ だと、$\mathtt b$ の連は全て $\mathtt c$ の間にあり、生き残りを外に置けない。生き残りを中に置くと、片側の $\mathtt c$ の個数しか集まらない（$F=\mathtt c\mathtt b^m\mathtt c$ では $\mathtt c^3$ までしか集まらない）。

- SB$(F)$・SB$(F^2)$ だけの種（$\mathtt a^5$、$\mathtt{bbbb}$）で打ち切りの閉包探索を行った。
  - $\mathtt{cbbc}$ は3段の証明書で $\mathtt c^4$ を強制した（§9 [8]、再生済み）。
  - $\mathtt{cbbbc}$ では、長さ14・3周の範囲で見つからなかった（観察）。
- よって、(O2) を両端 $\mathtt c$ まで含めて SB$(F^2)$ だけから証明することは**未解決**である。
- ただし定理 III-B にはこれは要らない。分岐 (B*) では、(KL) の種が鎖の補題で全て得られるからである。

### 3.2 補題 III.1：低い塊は交代語

**補題 III.1.** 場合 III・分岐 (B*) で、$F$ を SB$(F,d)$ をもつ内容 $\{\mathtt b,\mathtt c\}$ の塊とし、$4d\le k-4$、$6d\le k$ とする（低い塊はこれをみたす）。このとき $F\in\{(\mathtt{bc})^j,(\mathtt{cb})^j\}$。

**証明.** 鎖の補題により、SB$(F^j,jd)$（$j\le4$）と離れた二塊が全て得られる。特に (KL) の種がそろう。$\gamma=|F|_{\mathtt c}\ge1$ とし、$F$ の両端で場合を分ける。

**(a) 両端が $\mathtt b$.** $W=\mathtt a^sF^4\mathtt a^t$ とする。

- $|W|_{\mathtt b}=4\beta$、連の数 $4\rho-3$ で、$4\beta\ge4\rho\ge4\rho-2$ なので、余分な $\mathtt b$ がある。
- 最初の連を生き残りとし、$F^4$ の最初と最後の $\mathtt c$ の間の連を、補題 B-del で全て消す。
- 結果は $\mathtt a^s\mathtt b^x\mathtt c^{4\gamma}\mathtt b^y\mathtt a^t$ で、$\mathtt c^4$ を含み矛盾する。

この場合は $\mathtt c$ が一つの塊（$\mathtt{bcb}$、$\mathtt b^i\mathtt c\mathtt b^j$）も含む。

**(b) $\mathtt b$ で始まり $\mathtt c$ で終わる.**

- $\mathtt{cc}$ を含めば、(KL)（$F=U\mathtt{cc}$ か $F=P\mathtt{cc}Q\mathtt c$）で $\mathtt c^4$ が出る。
- $\mathtt{bb}$ を含めば、$F^4$ の $\mathtt b$ の個数 $4\beta\ge4\rho+4$、連の数 $4\rho$ である（$F$ が $\mathtt c$ で終わり $\mathtt b$ で始まるので、つなぎ目で連は合わさらない）。最初の連は最初の $\mathtt c$ の前にあり、他の連は全て $\mathtt c$ と $\mathtt c$ の間にある。最初の連以外を全て消すと $\mathtt a^s\mathtt b^{4\beta}\mathtt c^{4\gamma}\mathtt a^t$ となり、矛盾する。
- どちらも含まなければ $F=(\mathtt{bc})^j$。

**(c) $\mathtt c$ で始まり $\mathtt b$ で終わる.** (b) の鏡像である（最後の連を生き残りとし、鏡像の F′ を使う）。結論は $F=(\mathtt{cb})^j$。

**(d) 両端が $\mathtt c$.** (KL)（$F=\mathtt cU\mathtt c$、端点の文字 $z=\mathtt c$）で $\mathtt c^4$ が出る。∎

**機械的な確認.** スクリプト [3] は、$|F|\le9$ の全ての塊（両文字を含み $\mathtt c^4$ を含まないもの）について、上の場合分けどおりに証明書を作った。

- 種は $\mathtt a^{12}$、$\mathtt{bbbb}$、SB$(F,1)$、SB$(\mathtt{bc},1)$、二塊の語 $\mathtt aF\mathtt a\,\mathtt{bc}\,\mathtt a^{8}$ だけである。鎖・離れた二塊・$F^4$ も種から導いた。
- 証明書は 811 本、計 68970 段で、全てを再生した。
- 証明書を作らなかったのは $(\mathtt{bc})^j,(\mathtt{cb})^j$（$j\le4$）だけである。
- [7] では $d=2$、$k=24$ で七つの塊を繰り返した。

これらは一般の証明の具体例であり、一般の長さへの保証は上の証明による。

### 3.3 補題 III.2：根は一つ

**補題 III.2.** 場合 III・分岐 (B*) で、低い塊 $F_X=(\mathtt{bc})^i$、$F_Y=(\mathtt{cb})^j$ が両方あることはない。したがって、ある $u\in\{\mathtt{bc},\mathtt{cb}\}$ があり、全ての低い内部の両文字型ラベルについて $F_X=u^{j_X}$。

**証明（二通り）.**

- **(i)** 鎖 $C=F_XF_Y=(\mathtt{bc})^i(\mathtt{cb})^j$ は SB$(C,d_X+d_Y)$ をもち、両端が $\mathtt b$ である。補題 III.1 (a) を $C$ に当てる（$C^2$ で足りる。$2(i+j)\ge4$ 個の $\mathtt c$ が集まる）と、$\mathtt c^4$ が出る。
- **(ii)** 逆順の鎖 $F_YF_X=(\mathtt{cb})^j(\mathtt{bc})^i$ は両端が $\mathtt c$ である。(KL) の場合3で $\mathtt c^4$ が出る。これは既報 §4 の「両端が同じ文字」の論法で、場合 II では $z^4$ のどちらでも矛盾したが、場合 III では $z=\mathtt c$ になる順を選ぶ必要がある。分岐 (B*) では鎖の順を自由に選べるので、これで足りる。∎

スクリプト [4] は $(i,j)=(1,1),(1,2),(2,1)$ について、(i)・(ii) の両方の証明書を再生した。

**(O3) の残りの答え.**

- (KL)、既報 §8、(O2) を合わせると、残るのは $(\mathtt{bc})^j,(\mathtt{cb})^j$ と $\mathtt b^i\mathtt c\mathtt b^j$ だ、という依頼の見通しは、一歩手前で止まっている。
- 同じラベルの鎖 $F^4$ を使うと、$\mathtt b^i\mathtt c\mathtt b^j$（$\mathtt{bcb}$ を含む）も消える。
- 結局、全ての低い塊は**一つの根 $u\in\{\mathtt{bc},\mathtt{cb}\}$ の冪**になる。
- 「$\mathtt{bcb}$ が根として残る」場合は起こらない。

---

## 4. 損失の線形化（既報 §5 がそのまま使えること）

**補題 III.3.** 場合 III・分岐 (B*) で、全ての低い内部の両文字型ラベル $X$ について $d_X=\varphi j_X$（$\varphi\in\mathbb Q_{>0}$ は共通）。

**証明.** 既報 §5 と同じである。

1. 補題 III.2 より $F_X^{j_Y}=u^{j_Xj_Y}=F_Y^{j_X}$ は、文字列として等しい。
2. 鎖の補題（§2.4 の予算）より、$\mathtt a\,u^{j_Xj_Y}\mathtt a^{k-j_Yd_X-1}$ と $\mathtt a\,u^{j_Xj_Y}\mathtt a^{k-j_Xd_Y-1}$ がともに $L$ に入る。
3. 二語は同じ $\mathtt a$ 骨格をもち、$\mathtt a$ の個数はともに $[2,k)$ にある。定理S（§1.4）より、個数は等しい。
4. よって $j_Yd_X=j_Xd_Y$。∎

使うのは定理S だけで、(R)（$\mathtt b$ の連の配り直しを含む剛性）は要らない。$\mathtt b^4$ が現れることは、この段では何も変えない。スクリプト [5] は、$d$ が線形でない具体例（SB$(\mathtt{bc},1)$、SB$(\mathtt{bcbc},3)$）から $\mathtt a^{11}$（$k=12$）を強制する証明書を再生した。

---

## 5. 定理 III-B

### 5.1 主張と証明

**定理 III-B.** $\Sigma=\{\mathtt a,\mathtt b,\mathtt c\}$、内容型付け、$L\in\mathcal C_{2,c}$ とし、場合 III（$\mathtt b^4$ は現れ、$\mathtt c^4$ は現れない）・分岐 (B*) とする。$G$ を $L\cap\Sigma^+$ の既約で良い、ファンアウト $\le2$・ランク $\le r$ の表示とし、$v=|V|$、$\theta=\bar\theta_G\ge1$ とする。
$$E_B:=v(50\theta^3+\theta+23),\quad K_B:=(2v+E_B)(2r+1),\quad R:=\theta+2v+2$$
とおくと、
$$\mu_{\mathtt a}(L)\le\max\{4\theta+12,\ K_B^{10}R^9\theta\}.$$
$\mathtt c^4$ だけが現れる場合も、$\mathtt b,\mathtt c$ を入れ替えて同じである。

**証明.** $k:=\mu_{\mathtt a}(L)\ge4\theta+12$ とし、$T$ を一様な節点数最小の導出とする。重い節点を、定理 II-B の証明（既報 §6）と同じ表で分ける。

| 区分 | 扱い | 場合 III での確認 |
|---|---|---|
| 二文字の影が非飽和な一色型 | 例外、$\le18v$ | §5.2 |
| 飽和で出現 $\le\theta$ の一色型 | 例外、$\le v\theta$ | 両文字型を差し替えない数え方。場合によらない |
| 両文字型で内部でない節点 | 例外、$\le2v$ | 場合によらない |
| 高い両文字型（$\ell_X>k/(2N)$） | 例外、$\le2Nv=50\theta^3v$ | 一つの深さの出力は互いに素。場合によらない |
| 低く内部の出現が1個のラベル | 例外、$\le3v$ | 場合によらない |
| 飽和で頻出の一色型 | 色ごとに $d=\alpha_xq$（$q\in[1,\theta]$）の1次元群 | §5.2 |
| 低い内部の両文字型 | $d_X=\varphi j_X$（$j_X\in[1,\theta/2]$）の1次元群 | §4。窓は $\ell_X\in[d_X,d_X+\theta]$ |

例外の合計は $v(18+\theta+2+50\theta^3+3)=E_B$ で、分類にもれはない。線形の区分の次元の和は $D\le1+2=3$ である（両文字型の根は一つ、飽和の色は高々二つ）。

尺度補題 3.1・3.2 の仮定は、次の三つである。

- 例外の数は $\le E_B$。
- 群の値の窓が $[D_g,D_g+\theta]$。
- 群の値は、固定次元の整数点の、定数項のない線形形式で与えられる。

上の分類はこれらをみたすので、$k\le K_B^{3D+1}R^{3D}\theta\le K_B^{10}R^9\theta$。∎

**定理 II-B との比較.** 形も定数も同じである。変わったのは、§4 の「共通の根」を出す段だけである。

- 場合 II では、(KL) と「両端が同じ文字」の論法で根が一つになった。
- 場合 III では、(KL) が $\mathtt b^4$ しか出さない塊がある。これを、余分な $\mathtt b$ による融合（補題 B-del）と同じラベルの鎖 $F^4$ で消した。
- 混ざった根も、鎖の順を選んで（$\mathtt c$ が両端に来る順）消した。

例外と群の表は、どの行も変わらない。

### 5.2 一色型の数え方は場合 III でも成り立つ

`chatgpt_nested_bc_chain` §3.1–3.2 を読み直した。

- **非飽和.** 二文字の部分言語 $L_x=L\cap\{\mathtt a,x\}^+$ は、arity 1・2 の内容代入可能性を受け継ぐ。共有文脈が二文字上にあれば三文字上にもあり、分布の一致は二文字の文脈に制限してよいからである。同じ深さの一色型の重い節点が10個あれば、二つを替えて、$\mathtt{aa}$ と離れた二つの内部の $x$ の連をもつ $L_x$ の語ができる。これと矛盾を作る補題は、$L_x$ の場合で分かれる。
  - $L_x$ に $x^4$ が現れないなら、原稿 `lem:app-two-runs` (iv)。
  - 現れるなら、`lem:app-two-alternate`（$\mathtt a^4,x^4$ がともに現れ非飽和なら、連が4つ以上の語の連は全て長さ1）。
  
  場合 III の $x=\mathtt b$ では、$\mathtt b^4$ が $L_{\mathtt b}$ に現れる場合と現れない場合（$\mathtt b^4$ が $\mathtt c$ を含む語にしかない場合）があるが、どちらも覆われている。両補題の証明（原稿付録）を読み、二文字の中で完結していることを確かめた。
- **飽和.** 同じ $x$ の個数で $\mathtt a$ の個数の違う二点から、$\mathtt a^{k-\delta}$ が出る剛性である。$x^4$ は使わない。

したがって、$\mathtt b^4$ が現れることで変わる点はない。

---

## 6. 補題 B-cap（場合 III の一般の事実）

**補題 B-cap.** 場合 III で、$W\in L$ が余分な $\mathtt b$ をもつ（$|W|_{\mathtt b}\ge$ $\mathtt b$ の極大連の数 $+1$）とする。$W$ の $\mathtt a$ を含まない極大因子 $G$ が $\mathtt b$ を含むとき、次が成り立つ。

- $G$ の最初の $\mathtt b$ の連より右にある $\mathtt c$ は、3個以下である。
- 最後の $\mathtt b$ の連より左にある $\mathtt c$ も、3個以下である。

特に、$|G|_{\mathtt c}\le6$ である。

**証明.** $G$ の最初の $\mathtt b$ の連を生き残りとし、$G$ の他の $\mathtt b$ の連を補題 B-del で全て消す。$G$ のその連より右の部分は $\mathtt c$ だけになり、$\mathtt a$ を含まないので一つの $\mathtt c$ の連になる。$\mathtt c^4$ がないので、その長さは $\le3$ である。後半は鏡像で示す。最後の主張は、最初の $\mathtt b$ の連より左の $\mathtt c$（一つの連なので $\le3$）と合わせて得られる。∎

補題 III.1 (a)–(c) と命題 O2 (a) は、この補題の特別な場合と読める。スクリプト [6] に具体例がある。

---

## 7. 課題2：場合 III・分岐 (S)

### 7.1 殻の中でも $\mathtt b$-融合は使える。その結果、$\mathtt b$ の連が細くなる

**命題 S-III.** 場合 III とし、$X$ を型板をもつ両側型の低いラベル（分岐 (S) の関係のあるラベルはこれ）、$(A,B)=(A_X,B_X)$ をその殻とする。$m\ge6$ を、補題 N の予算 $(m+1)d_X\le k/2$ に入る範囲でとる。このとき、入れ子の語
$$N_m:=A^m\,F_X\,B^m=A^{m+1}B^{m+1}$$
の $\mathtt b$ の極大連は全て長さ1である。特に次が成り立つ。

- $A$、$B$ はどちらも $\mathtt{bb}$ を含まない。
- $A$ は「$\mathtt b$ で始まり $\mathtt b$ で終わる」ことがない（つなぎ目 $A|A$ が $\mathtt{bb}$ を作る）。$B$ も同様である。
- 「$A$ が $\mathtt b$ で終わり $B$ が $\mathtt b$ で始まる」ことはない。

同じ型の型板があれば、別のラベルの殻を混ぜた入れ子にも同じことが言える。

**証明.** 補題 N（$S_1=\dots=S_m=(A,B)$、$P=F_X=AB$、$\Lambda=(m+1)d_X$）により、SB$(N_m,\Lambda)$ が成り立つ。

- 両側型の両文字型ラベルなので、$A,B$ の合わせて $\mathtt c$ を少なくとも1個含む。よって $|N_m|_{\mathtt c}\ge m+1\ge7$。
- $\mathtt a^sN_m\mathtt a^t$ が余分な $\mathtt b$ をもつと、補題 B-cap により $|N_m|_{\mathtt c}\le6$ となり、矛盾する。
- したがって余分な $\mathtt b$ はなく、$\mathtt b$ の個数は連の数に等しい。つまり全ての連が長さ1である。∎

**予算.** 低いラベルでは $(m+1)d_X\le7k/(50\theta^3)\le k/2$、$d_X\le k/8$、$k\ge4\theta+12$ で、補題 N の仮定が成り立つ。

### 7.2 交代語なら損失は線形になる（条件付き）

**命題 S-III-cond.** 場合 III・分岐 (S) で、細類 $\pi$（殻の各側の内容と先頭・末尾の文字）の関係のあるラベルについて、型 $\tau(\pi)$ の殻の入れ子 $A_1\cdots A_mPB_m\cdots B_1$（$P=F_{X_0}$ を固定）が常に $\mathtt{bb}$ も $\mathtt{cc}$ も含まない、と仮定する。このとき、ある $\varphi_\pi$ があり、全てのラベルについて $d_X=\varphi_\pi n_X$（$n_X=|A_X|+|B_X|$）。

**証明.**

1. 交代語は、先頭の文字と長さで決まる。先頭の文字は $\pi$ の $f_A$ で、長さは $\sum(|A_i|+|B_i|)+|P|$ である。
2. ラベルの多重集合 $\mathcal A=\{n_Y$ 個の $X\}$ と $\mathcal B=\{n_X$ 個の $Y\}$（それぞれ $\le\theta$ 個）は、長さの和が等しい。したがって入れ子の語は文字列として等しい。
3. 補題 N によりどちらも SB をもち、$\mathtt a$ の個数は $[k/2,k)$ にある。定理S により $n_Yd_X=n_Xd_Y$。∎

この仮定の下では、補題 Q の 34 細類 × 3 次元は、細類ごとに 1 次元になる。ただし仮定そのものは証明していない。

### 7.3 止まった場所

命題 S-III により、入れ子の $\mathtt b$ は全て孤立する。$\mathtt c$ の連の長さは 1〜3 のまま残る。

- $\mathtt b$ が全て孤立しているので、余分な $\mathtt b$ はない。$\mathtt b$-融合はこれ以上何もできない。
- (R) も、$\mathtt b$ の配り直しの余地がないので、定理S（文字列として等しい語どうしの比較）に退化する。
- したがって線形化には、二つの多重集合の入れ子の語が文字列として一致する必要がある。$\mathtt c$ の連の長さの並び（$\mathtt b$ で区切られた $\{\mathtt c,\mathtt{cc},\mathtt{ccc}\}$ の列）が、細類と少数の数で決まらない限り、比較ができない。

**止まった段**：補題 Q の (a)（入れ子の核が細類と少数の数で決まること）。場合 III では、殻の片側か継ぎ目に $\mathtt{cc}$ があると、この段が成り立たない。

**最小の対照**：殻 $(A,B)=(\mathtt{bcc},\mathtt{cb})$。

- $A^mB^m=(\mathtt{bcc})^m(\mathtt{cb})^m$ は $\mathtt b$ が全て孤立し、$\mathtt c$ の連は $\le3$ である。
- したがって命題 S-III と $\mathtt c^4$ の禁止の両方をすり抜ける。

---

## 8. 課題3：塊の数 $\beta$

定理 M$_\beta$：$\mu_{\mathtt a}\le(1+\min\{\kappa,2\beta\})\,v\,(\rho_{\max}+r\theta)$。ここで $\beta=\beta(L)$ は、$L$ の語あたりの $\mathtt a$ を含まない極大因子の数の上限である。$\beta$ は**言語全体**の量で、分岐は $\mathtt a^k$ の導出 $T$ から定まる。この点に注意して整理する。

**命題 β.** $X$ を低いラベルとする。

**(i)** 分岐 (B*) で、$X$ が低い内部の両文字型なら、$\beta(L)\ge\lfloor(k-1)/(d_X+2)\rfloor$。

**(ii)**（場合・分岐によらない）$X$ が型板をもつ両側型なら、$\beta(L)\ge2\lfloor k/(4d_X+4)\rfloor$。

**証明 (i).** $t$ を $t(d_X+2)\le k-1$ となる最大の整数とする。

1. 鎖の補題で $\mathtt a^sF_X^t\mathtt a^{s'}$（$\mathtt a$ の個数 $k-td_X$）を得る。
2. SB$(F_X)$ の二語 $\mathtt a^{s}F_X\mathtt a^{s''}$、$\mathtt a^{s-1}F_X\mathtt a^{s''+1}$（$s\ge2$）は、文脈 $\mathtt a^{s-2}\square\,\mathtt a^{s''-1}$ を共有する。よって $D(\mathtt a^2F_X)=D(\mathtt aF_X\mathtt a)$（型は等しい）。
3. 系2.2 で塊の直前の連を2以上にしては、$\mathtt a^2F_X\to\mathtt aF_X\mathtt a$ と置き換える。これを繰り返すと、$t$ 個の塊が $\mathtt a$ で隔てられる。必要な $\mathtt a$ の個数 $\ge2t+1$ は $k-td_X\ge2t+1$ で確保される。∎

**証明 (ii).** $m=\lfloor k/(4d_X+4)\rfloor-1$ とする。

1. 補題 N で SB$(A^{m+1}B^{m+1},(m+1)d_X)$ を得る。$(m+1)d_X\le k/4$ である。
2. SB$_2$ の語から $D(\mathtt a^2A)=D(\mathtt aA\mathtt a)$、$D(\mathtt a^2B)=D(\mathtt aB\mathtt a)$ を得る（文脈 $\mathtt a^{s-2}\square\,\mathtt a^{g-1}B\mathtt a^t$、および $\mathtt a^sA\mathtt a^{g-2}\square\,\mathtt a^{t-1}$）。
3. (i) と同じく、$2m+2$ 個の塊を離す。$\mathtt a$ の個数 $\ge3k/4\ge2m+3$ で確保される。∎

**整理.**

- 分岐 (B) では、鎖はいつも一つの塊に融合して使う。$\beta$ は証明に現れない。定理 III-B は $\beta$ によらない。
- 分岐 (S) では、入れ子も一つの塊として使う。ただし命題 β (ii) により、損失の小さい関係のあるラベルがあれば、$\beta(L)$ は $k/d_X$ の程度まで必ず大きい。
- したがって「分岐 (S) では $\beta\le\mathrm{poly}$」は、「関係のある全てのラベルの損失が $k/\mathrm{poly}$ 以上」を含意する。後者が成り立てば、関係のある節点は一つの深さに $\mathrm{poly}$ 個しかなく（$\ell\ge d$、出力は互いに素）、例外として数えられる。つまりこの主張は、分岐 (S) を閉じることとほぼ同じ強さである。
- 分岐の定義だけから $\beta$ を抑える道は見つからなかった。逆向きの構成（$\beta$ が超多項式になる分岐 (S) の言語）も作れなかった。**どちらも未解決。**

---

## 9. 計算（スクリプトの出力をそのまま）

`check_claude_problemQ_round6_2026-11-09.py` の仕組みは次のとおりである。

- **証明器**：§1–§4 の証明の段を、そのまま SUB$_1$・SUB$_2$ の具体例として書き出す。使う段は、補題2.1 の移送、F′ とその鏡像、補題E の交換、鎖、(KL) の持ち上げ、定理S である。
- **検査器** `replay`：記録された全段を、種だけから再生する。各段で次の五つを確かめる。
  - 各成分が空でないこと。
  - 成分ごとの内容が等しいこと。
  - arity 2 では中央の固定部分が空でないこと。
  - 三つの前提が、種か既に導いた語であること。
  - 結論が $H[Y]$ であること。
- [1] の基礎証明書のデータは `chatgpt_case2_branches` 付録A から写した。再生はこのファイルの検査器で行った。
- [8] の閉包探索は、`check_claude_case3_bfusion_2026-11-04.py` の方法を書き直したものである。

この環境で `python3 -I` により実行した。以下は出力から、証明書の各段を示す行（字下げ6文字）を除いたものである。

```text
[1] replay of the (KL) base certificates
    xpxxq steps 4 terminal aaxpxqxpxxxxqxpxqa contains xxxx
    pxxqx steps 4 terminal apxqxpxxxxqxpxqxaa contains xxxx
    bcc steps 3 terminal abccbcbccccbca contains cccc
    bbc steps 3 terminal abbcbbbbccbbca contains bbbb
    bcb steps 4 terminal abcbcbbbbcbcba contains bbbb
[2] (O2) literal: seeds a^k, bbbb, one word a F F a^t (k=7, loss 2d=2)
    F=bcccb  seed abcccbbcccbaaaa  steps  2 forced abbbccccccbaaaa
    F=bccb   seed abccbbccbaaaa    steps  2 forced abbbccccbaaaa
    F=bcbcb  seed abcbcbbcbcbaaaa  steps  7 forced abbbbbccccbaaaa
    F=bbcbc  seed abbcbcbbcbcaaaa  steps  7 forced abbbbbbccccaaaa
    F=cbcbb  seed acbcbbcbcbbaaaa  steps  7 forced accccbbbbbbaaaa
[3] branch (B*): all blocks F over {b,c}, 2<=|F|<=9, k=12, d=1
    certificates by route: {'KL:bbc': 18, 'KL:bcb': 190, 'KL:bcc': 18, 'KL:pxxqx': 12, 'KL:xpxxq': 12, 'bfusion': 561} total steps 68970
    no certificate attempted (alternating, one end b one end c): ['bc', 'cb', 'bcbc', 'cbcb', 'bcbcbc', 'cbcbcb', 'bcbcbcbc', 'cbcbcbcb']
    example F=bcccb route=bfusion steps=77 forced=abbbbbccccccbcccbcccbaaaaaaa (last 12 steps shown)
    example F=bcb route=bfusion steps=81 forced=abbbbbbbccccbaaaaaaa (last 12 steps shown)
    example F=cbb route=bfusion steps=80 forced=accccbbbbbbbbaaaaaaa (last 8 steps shown)
    example F=cbcc route=KL:bcb steps=85 forced=aaaaaaaacbccccbccbcca (last 6 steps shown)
[4] mixed roots P=(bc)^i, Q=(cb)^j
    PQ=bccb (both ends b) b-fusion on (PQ)^2: steps 57 forced abbbccccbaaaaaaaaa
    QP=cbbc (both ends c) lifted bcb: steps 118 forced aaaacbbcbbccccbbcbbcaa
    PQ=bccbcb (both ends b) b-fusion on (PQ)^2: steps 87 forced abbbbcccccbcbaaaaaaaaaaaaa
    QP=cbcbbc (both ends c) lifted bcb: steps 196 forced aaaaacbcbbcbcbbccccbcbbcbcbbcaaa
    PQ=bcbccb (both ends b) b-fusion on (PQ)^2: steps 88 forced abbbbccccbccbaaaaaaaaaaaaa
    QP=cbbcbc (both ends c) lifted bcb: steps 200 forced aaaaacbbcbcbbcbccccbbcbcbbcbcaaa
[5] Theorem S on a common root u=bc: SB(bc,1), SB(bcbc,3), k=12
    forced aaaaaaaaaaa (a-word shorter than k: contradiction with mu_a = k); steps 28
[6] b-cap lemma: a b-spare word with >=4 c after the first b-run
    N=cbbcbcbcbc steps 6 forced acbbbbbccccaaaa
    N=bcbcbbcbcb steps 7 forced abbbbbccccbaaaa
    N=ccbcbcbcbcbb steps 7 forced accbbbbbccccbaaaa
[7] d=2, dG=1, k=24 (unequal losses)
    F=bcccb  route=bfusion    steps= 172 forced=abbbbbccccccbcccbcccbaaaaaaaaaaaaaaa
    F=bcb    route=bfusion    steps= 176 forced=abbbbbbbccccbaaaaaaaaaaaaaaa
    F=cbb    route=bfusion    steps= 175 forced=accccbbbbbbbbaaaaaaaaaaaaaaa
    F=cbcc   route=KL:bcb     steps= 280 forced=aaaaaaaaaaaaaaaacbccccbccbccaa
    F=ccbc   route=KL:bcb     steps= 280 forced=aaaaaaaaaaaaaaaaccbccccbccbcaa
    F=bcbcc  route=KL:bcc     steps= 279 forced=aaaaaaaaaaaaaabcbccbcbcbcbccccbcbcaa
    F=cbbc   route=KL:bcb     steps= 280 forced=aaaaaaaaaaaaaacbbcbbccccbbcbbcaa
[8] (O2) literal, both ends c: seeds a^5, bbbb, SB(F,1), SB(F^2,2)
    F=cbbc: certificate, 3 steps, forced acbbbccccbbbca
    F=cbbbc: no c^4 within maxlen 14, 3 rounds (observation only)
ALL CHECKS PASSED  (5.2 s)
```

[2] の $\mathtt{bcccb}$ の証明書（全2段）：

```text
1 SUB_2 E=('', 'b', '') X=('b', 'bb') Y=('bb', 'b') H=('a', 'ccc', 'cccbaaaa') => abbcccbcccbaaaa
2 SUB_1 E=('a', 'bcccbaaaa') X=('bcccb',) Y=('bbccc',) H=('ab', 'cccbaaaa') => abbbccccccbaaaa
```

[8] の $\mathtt{cbbc}$ の証明書（全3段）：

```text
1 SUB_2 E=('', 'b', '') X=('b', 'bb') Y=('bb', 'b') H=('ac', 'bcc', 'caa') => acbbbccbcaa
2 SUB_2 E=('', 'b', '') X=('bb', 'b') Y=('b', 'bb') H=('aac', 'cc', 'bca') => aacbccbbbca
3 SUB_1 E=('', 'bcaa') X=('aacb',) Y=('acbbbcc',) H=('', 'ccbbbca') => acbbbccccbbbca
```

**計算の読み方.**

- 強制された語は、そこに示した種を含む $L\in\mathcal C_{2,c}$ が $\mathtt c^4$ を避けられない（[5] では $\mu_{\mathtt a}=k$ でありえない）ことの証明書である。
- 証明書を作らなかったこと（[3] の交代語）や見つからなかったこと（[8] の $\mathtt{cbbbc}$）は、何の証明でもない。
- 有限の検査から、無限の族の所属は推定していない。

---

## 10. 範囲、文献、結了の三点

**範囲.**

- 定理 III-B は、**場合 III・分岐 (B*)** の **$\mu_{\mathtt a}$** の上界である。
- 分岐 (S)、場合 II、代表の長さ $\tau$、他の稀な型、`op:fanout-two` そのものは扱っていない。
- (O2) で消えるのは、「$\mathtt c$ を4つ以上つなげられる塊」（余分な $\mathtt b$ と、$\mathtt c$ の範囲の外の $\mathtt b$ の連をもつ語の塊）だけである。場合 III 全体ではない。
- 命題 S-III・補題 B-cap は場合 III の事実で、場合 II には $\mathtt b^4$ がないので使えない。

**文献.** 補題2.1・F′ の型の連の交換は、原稿 `lem:app-two-runs` と同種の操作である。補題 B-del、補題 B-cap、鎖の補題、補題 III.1–III.3、定理 III-B、命題 S-III、命題 β が刊行文献で既知かは**未確認**である。

**結了の三点.**

1. **証明できたこと.**
   - (O1)：補題 F′$_{\mathtt b}$ と補題 B-del。
   - (O2)：少なくとも一端が $\mathtt b$ の塊。
   - 分岐 (B*) の鎖の補題：同じラベルの鎖を含む。
   - (O3)：低い塊は一つの根 $u\in\{\mathtt{bc},\mathtt{cb}\}$ の冪。
   - 損失の線形化と**定理 III-B**：定理 II-B と同じ形・同じ定数。
   - 補題 B-cap、命題 S-III、命題 β。
2. **止まった場所.**
   - 分岐 (S)：補題 Q (a) の段。殻の片側か継ぎ目に $\mathtt{cc}$ があるとき、入れ子の語が細類と少数の数で決まらない。最小の対照は殻 $(\mathtt{bcc},\mathtt{cb})$。
   - (O2) を SB$(F^2)$ だけから両端 $\mathtt c$ の塊まで示すこと。$\mathtt{cbbbc}$ が未判定。定理 III-B には不要。
3. **次に絞るべき一点.** 場合 III・分岐 (S) で、型板と入れ子の種（$\mathtt a A\mathtt a A\mathtt a B\mathtt a B\mathtt a$、SB$_2$ の語、$A^mPB^m$）から、殻の片側の $\mathtt{cc}$ に対して $\mathtt c^4$ を強制する二穴の SUB$_2$ の証明書があるかを調べる。最小の対照は殻 $(A,B)=(\mathtt{bcc},\mathtt{cb})$。もしあれば、命題 S-III と合わせて入れ子は交代語になる。そうなれば、命題 S-III-cond から場合 III・分岐 (S) も線形化される（そこから定数付きの上界を出すには、定理 I の例外の数え方を場合 III に合わせて確かめる必要がある）。
