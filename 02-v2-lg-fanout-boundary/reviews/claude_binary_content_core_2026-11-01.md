# 二文字の内容型付け・ファンアウト2の残りの核：a 塊の再配分、二つの冪がそろう場合の線形上界、純な a の穴への帰着

**研究日**：2026年11月1日
**対象**：`growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary`（clone 時の先頭 commit `39eefef`）。`main.tex` の §2–§4、`lem:typing-monotone`、`prop:sl-reduction`、`op:fanout-two`、`reviews/chatgpt_sl_positive_2026-11-01.md`（出発点）、退避 `parked/parked_fanout2_and_comparison.tex` の `lem:app-u1-*`、`reviews/chatgpt_sl_fanout2_2026-11-01.md`、`reviews/chatgpt_parikh_closed_family_2026-11-01.md`。
**判定の意味**：「証明済み」はこの報告の中に証明を書いたこと（または明示した既存の証明への還元）を指し、外部査読や文献上の新規性を意味しない。「観察」は有限の計算で、証明ではない。

---

## 0. 結論と判定

記号：$\Sigma=\{a,b\}$、$c=c_\Sigma$、ファンアウト $\le2$、ランク $\le r$（$r\ge2$）、$v=|V|$、$g=\lVert G\rVert$、$\theta=\bar\theta_G$。「$a^4$ が現れる」は「$L$ のある語が因子 $a^4$ を持つ」の意味。

| 主張 | 判定 | 根拠 |
|---|---|---|
| **a 塊の再配分**：$L\in\mathcal C_{2,c}$ のある語が $a^4$ を持てば、語の所属は「a 骨格（a の各塊を一文字に縮めた語）」と $\lvert w\rvert_a$ だけで決まる | **証明済み** | 補題2.1 |
| 上の仮定で、ある語が $aaba$ か $abaa$ を持てば Parikh 飽和。特に非飽和なら、b の内部の一文字の塊を持つ語では a の塊がすべて長さ1 | **証明済み** | 系2.2 |
| 上の仮定で、ある骨格に a の個数が $t<t+\delta$ の二語があれば $\mathcal D_L(a)=\mathcal D_L(a^{1+\delta})$ | **証明済み** | 系2.3 |
| **挿入補題**（代入可能性を使わない）と、その系：$L$ の語の塊の数が $k$ 以下なら $t_{\rm typ}(G,c)\le 9(r+1)v\theta(8+5k)$ | **証明済み** | 補題3.1、系3.2 |
| **場合 I**：$a^4$ と $b^4$ がともに現れ、$L$ が Parikh 飽和でなければ、$t_{\rm typ}(G,c)\le117(r+1)v\theta$（深い挿入の有無を問わない） | **証明済み** | 補題4.1、定理4.2 |
| (A)(B)(C) と核（深い挿入あり・非飽和）で二文字の全ての $L$ を覆う。核の中で残るのは「a 深い挿入、$b^4$ なし、非飽和」（とその対称）だけ | **証明済み** | §5.1 |
| 場合 II で、成分型に $\{a\}$ を含まない型付き非終端は $\tau_X\le252(r+1)v\theta$ | **証明済み**（既存の定理2.1の適用） | §5.2 |
| $a^4$ が現れれば、型 $(\{a\},\{a,b\})$・$(\{a,b\},\{a\})$ の $X$ は $\tau_X\le(r+1)\theta(\theta+3)(\theta+4)v$（場合 II に限らない） | **証明済み** | 補題5.1、定理5.2 |
| 場合 II の残り（型 $(\{a\})$, $(\{a\},\{a\})$, $(\{a\},\{b\})$, $(\{b\},\{a\})$）は、純な a の一穴の問題 $P_a(C)$ に帰着し、$P_a(C)\le\min\{\delta_L,\ (\theta+4)(\theta+5)v(\theta+r\max\{\theta,\Pi_G\})\}$ | **証明済み** | 補題5.3、定理5.4 |
| 場合 II の増分の障害：長さ2の b の塊を3に伸ばした骨格がともに現れるなら、伸ばした語の a の余りは $\lvert\Delta\rvert$ 未満 | **証明済み** | 補題6.1 |
| 退避 `lem:app-u1-deep`（$e\ge2$）の代わりに $(a,b^ea)$ と $(aa,b^e)$ を比べる手がかり | **反証**（内容が $(\{a\},\{a,b\})$ と $(\{a\},\{b\})$ で一致しない） | §1.3 |
| 手がかり「一文字の橋が無いので、z の中の b は2個以上の塊でしか a の塊と接しない」 | **証明済み**（正確な形：$aa$ を含む語では、b の内部の塊は長さ2以上） | 系2.2(ii) |
| 手がかり「塊の長さの多重集合を保つ並べ替えに閉じる」 | a の塊は**証明済み**（並べ替えより強く、和を保つ任意の再配分）。b の塊は $b^4$ が現れるときだけ証明済み、場合 II では**未解決** | 補題2.1、§6 |
| 二文字の全ての $L\in\mathcal C_{2,c}$ で $\tau$ が多項式か | **未解決**。残りは場合 II の「剛い」部分だけで、反例族の必要条件を §6 に列挙 | §5.4、§6、§7 |
| 有限の検査：$a^*bba^*$ は長さ ≤11 で違反なし。b の塊の長さを制限した自由な言語と剛い玩具の言語は全て違反（塊の合流、または補題6.1の増分の機構） | **観察**（違反の例そのものは、その言語が代入可能でないことの証明） | §6.3、付録 |
| 補題2.1・定理4.2・定理5.2・定理5.4 が文献で既知か | **未確認** | §8 |

**今回の到達点**：二文字の内容型付けで多項式上界が言えない可能性があるのは、次の全てを満たす $L$ だけである（$a$ と $b$ を入れ替えた場合も同様）。

1. a の深い挿入があり、$b^4$ を因子に持つ語が無く、Parikh 飽和でない（場合 II）。
2. 問題になるのは、成分が全て純（$\{a\}$ または長さ $\le3$ の $\{b\}$）でその中に $\{a\}$ がある型付き非終端だけで、それは一穴の量 $P_a(C)$ に帰着する。
3. $P_a(C)$ が超多項式なら、(i) 同じ a 骨格で a の個数が異なる二語の差 $\delta_L$ が全て超多項式（または差が一つも無い＝剛い）、(ii) 純な a の組の最短の長さ $\Pi_G$ が超多項式、(iii) 塊の数が超多項式の語を含む、(iv) 補題6.1の増分の障害を満たす。

肯定・否定のどちらも完結していない。ただし核は (1)–(3) まで狭まった。

---

## 1. 設定と、使う既知の事実の検証

### 1.1 設定

$L\in\mathcal C_{2,c}$、$G$ は $L\cap\Sigma^+$ の reduced good な表示（ファンアウト $\le2$、ランク $\le r$）。各非終端 $B$ に $\lVert\omega_B\rVert_1\le\theta$ の生成組 $\omega_B\in L_B(G)$ を固定し、各 $A$ に `lem:thickness-equivalence`(iv) の文脈 $E_A$（$\lvert E_A\rvert_{\rm fix}\le\theta$、$E_A[L_A(G)]\subseteq L$）を固定する。各規則が直接書く終端は $\le\theta$ 個（同 (i)）。

型付き非終端 $X=A_{\mathbf S}$、$\mathbf S=(S_1,\dots,S_d)$（$d\le2$、$S_i\in\{\{a\},\{b\},\{a,b\}\}$）について、退避 `lem:app-u1-fillers` の証明は型付けの種類を使わないので、内容型付けでも

$$
\tau_X=\min\{\lVert\mathbf z\rVert_1:\ c(z_i)=S_i\ (i\le d),\ E_A[\mathbf z]\in L\}. \tag{1.1}
$$

（`lem:typed-homogeneity` により $L_X$ は一つの同値類に入り、型が同じで $E_A$ に受理される組は代入可能性で同じ分布を持つ。）`cor:distribution-representatives` から、$\mathcal B^{\le r}_{2,c}$ と $\mathcal B_{2,c}$ に共通の特徴標本 $K$ があり

$$
\lVert K\rVert_+\le 4^{2r}g\,(1+2\theta+r\,\tau(G,c))+\mathbf 1_{\{\varepsilon\in L\}}. \tag{1.2}
$$

（$\lvert\mathcal P_+(\Sigma)^\sharp\rvert=4$、$N_{\rm typ}\le4^{2r}g$。）以下の上界は全て $\tau$ または $t_{\rm typ}\ge\tau$ の上界で、(1.2) により同じ二つの作用素の特徴標本の上界になる。

語 $w$ について、$\rho_a(w)$ は a の極大な塊の数、**a 骨格** $\sigma(w)$ は a の各極大な塊を一文字 $a$ に置き換えた語とする（例：$\sigma(aabbaaab)=abbab$）。b の塊の長さの列と、語が a で始まるか・終わるかは $\sigma(w)$ に記録される。

### 1.2 先行結果の検証

- **(A)**（`chatgpt_sl_positive` 定理2.1・系2.2）：印の数 $d(2h+m)$、パス上の型付きラベル $\le(2^m-1)^2v$、成分ごとの禁止挿入の議論を確認した。正しい。$h=6$、$m=2$ で $\tau\le252(r+1)v\theta$。
- **(B)**（同 定理3.3）：補題3.1の (3.1) は Parikh 飽和の下で正しい。補題3.2が使う代入可能性は $a$ と $a^{1+\delta}$（ともに内容 $\{a\}$）の一穴の比較だけであることを確認した。
- **(C)**（同 補題4.1）：$a^6ba^6$ は $a^4$ と $aaba$ を含むので、`lem:app-u1-transfer`(ii) の内容型付け版（比較する組の内容はそれぞれ $(\{a\},\{a\})$ と $\{a,b\}$）がそのまま使える。正しい。系2.2はこれを強める。
- **(D)**（同 定理4.2）：場合分け $j=0,1,2$ を確認した。$j=1$ で $S_i=\{b\}$ のとき成分は語 $b$ そのもの、という点も正しい。有限の観察（付録、長さ ≤11、arity 1・2）でも違反は無い。
- `lem:app-u1-transfer`(i)（$a^m$ を持つ語があれば、$i+j=i'+j'\le m-1$ の $(a^i,a^j)$ と $(a^{i'},a^{j'})$ は全ての許容二穴文脈で交換できる）は、成分の内容が全て $\{a\}$ なので内容型付けでも成り立つ。補題2.1はこれを使う。

### 1.3 誤りの指摘

1. **手がかりの組 $(a,b^ea)$ と $(aa,b^e)$**：二つ目の成分の内容が $\{a,b\}$ と $\{b\}$ で一致しないので、内容型付けの代入可能性は比較を許さない。$e\ge1$ のどの値でも同じ。しかも (D) により「深い挿入 ⇒ Parikh 飽和」は偽なので、どんな組を選んでも退避の結論は出せない。正しく言えるのは系2.2（$aaba$ または $abaa$ が現れるときだけ飽和）である。
2. `chatgpt_sl_positive` §4.1 の表は `lem:app-u1-runs` を「直接移植しない」としているが、補題3.1・系3.2の通り、塊の数を「純な成分に入った異文字の塊」として数えれば内容型付けでも成り立つ（誤りではなく、埋まっていなかった部分）。
3. `deepseek_sl_fanout2_search` の §2.3・補題4（指示文で誤りと指摘済み）は本報告では使っていない。

---

## 2. 新しい道具：a 塊の再配分

### 補題2.1（a 塊の再配分）【証明済み】

$L\in\mathcal C_{2,c}$ とし、$L$ のある語が因子 $a^4$ を持つとする。$w,w'\in\Sigma^+$ が $\sigma(w)=\sigma(w')$ かつ $\lvert w\rvert_a=\lvert w'\rvert_a$ を満たせば、$w\in L\iff w'\in L$。

**証明。** $pa^4q\in L$ とする。組 $\mathbf x=(a,aa)$、$\mathbf y=(aa,a)$ は成分の内容がともに $(\{a\},\{a\})$ で、許容文脈 $p\,\square_1\,a\,\square_2\,q$（穴の間は $a\neq\varepsilon$）がどちらも $pa^4q$ にする。よって $\mathcal D^{(2)}_L(\mathbf x)=\mathcal D^{(2)}_L(\mathbf y)$。

$w$ の a の極大な塊 $R_i$（長さ $\ge2$）から別の塊 $R_j$ へ一文字 a を移す操作を考える。$R_j$ が $R_i$ より左なら、$R_j$ の最後の一文字を第一の穴、$R_i$ の最初の二文字を第二の穴とし、$w=U\,a\,Z\,aa\,V$ と書く。$Z$ は二つの塊の間にあるので b を含み、空でない。文脈 $U\square_1Z\square_2V$ は許容で、$\mathbf x$ を受理するかは $w\in L$ と同じ。分布が等しいので $U\,aa\,Z\,a\,V\in L\iff w\in L$。右へ移す場合は $\mathbf x,\mathbf y$ の役割を入れ替える。この操作は a 骨格と $\lvert w\rvert_a$ を変えない。

$\sigma(w)=\sigma(w')$ なら二語の a の塊の数 $\rho$ は等しく、塊の長さの列は和 $t=\lvert w\rvert_a$ の正の整数への $\rho$ 分割である。正の分割どうしは「長さ $\ge2$ の部分から別の部分へ1を移す」操作で互いに移り合うので、$w$ から $w'$ へ所属を保ったまま到達できる。□

**注意。** この補題は `lem:app-u1-transfer`(i) を全ての塊の組に繰り返し使っただけだが、「所属は（骨格, a の個数）の関数」という形にまとめると、以下の場合分けの基礎になる。b について同じことが言えるのは $b^4$ が現れるときだけである。

### 系2.2（禁止因子）【証明済み】

$L\in\mathcal C_{2,c}$ で $a^4$ が現れるとする。

(i) ある語が $aaba$ または $abaa$ を因子に持てば、$L$ は Parikh 飽和。
(ii) $L$ が Parikh 飽和でないなら、b の**内部**の塊（両側に a がある塊）で長さ1のものを持つ語 $w\in L$ は、a の塊が全て長さ1（$\lvert w\rvert_a=\rho_a(w)$）。特に $aa$ を因子に持つ語では、b の内部の塊は全て長さ $\ge2$。

**証明。** (i) $UaabaV\in L$ なら、組 $(aa,a)$ と $(a,aa)$（間は $b$）の交換で $UabaaV\in L$（補題2.1の証明と同じ）。文脈 $(Ua,aV)$ は内容 $\{a,b\}$ の $ab$ と $ba$ をともに受理するので $\mathcal D^{(1)}_L(ab)=\mathcal D^{(1)}_L(ba)$。隣り合う $ab\leftrightarrow ba$ の交換で同じ Parikh ベクトルの語は全てつながる。$abaa$ も同様。

(ii) $w$ が内部の一文字の b の塊 $\beta$ を持ち、ある a の塊が長さ $\ge2$ だとする。補題2.1で a を $\beta$ の左隣の塊に移せば（その塊がすでに長さ $\ge2$ なら何もしない）、左隣の塊が長さ $\ge2$ の語が $L$ に入り、因子 $aaba$ を持つ。(i) に反する。□

### 系2.3（a の個数の漏れ）【証明済み】

$L\in\mathcal C_{2,c}$ で $a^4$ が現れ、ある骨格 $\sigma$ について a の個数が $t$ と $t+\delta$（$\delta\ge1$）の二語が $L$ にあるとする。このとき $\mathcal D^{(1)}_L(a)=\mathcal D^{(1)}_L(a^{1+\delta})$。

**証明。** a の個数 $t$ の語 $w$ を取り、$\sigma$ の a の塊の一つ $R$ を選ぶ。$t>\rho_a$ なら補題2.1で $R$ 以外に余りを移して $R$ を長さ1にできる（$\rho_a=1$ のときは $R$ の一文字を穴にする）。$w=UaV$ と書くと、$Ua^{1+\delta}V$ は骨格 $\sigma$、a の個数 $t+\delta$ なので補題2.1により $L$ に入る。$a$ と $a^{1+\delta}$ はともに内容 $\{a\}$ で共通の文脈 $(U,V)$ を持つ。□

**定義。** 骨格が同じで a の個数が異なる二語の差の集合を $\Delta_L$ とし、空でなければ $\delta_L:=\min\Delta_L$ とする。$\Delta_L=\varnothing$ のとき $L$ は **a 剛**（骨格ごとに a の個数が一つ）と呼ぶ。

---

## 3. 挿入補題と塊の数の上界（代入可能性を使わない）

型付き非終端 $X=A_{\mathbf S}$ について、$\widetilde G_0$ における $X$ からの導出 $T$ のうち、生成組 $\mathbf u$ の総長が最小で、その中で節点数が最小のものを固定する。同じ型付きラベル（非終端と成分の内容の組）がパス上で繰り返せば、上を下に差し替えると $X$ からの導出で生成組が長くならず節点が減るので、繰り返しは無い。型付きラベルは $\le9v$ 個なので、パスの節点数は $\le9v$。

**印**：内容 $\{a\}$ または $\{b\}$ の成分（純な成分）では最初の $\min\{2,\lvert u_i\rvert\}$ 文字と最後の $\min\{2,\lvert u_i\rvert\}$ 文字、内容 $\{a,b\}$ の成分では a と b を一つずつ。印は $\le8$ 個。生成組の総長が $>\theta$ の節点を**重い**と呼ぶ。

### 補題3.1（挿入補題）【証明済み】

$Q$ を重い節点の反鎖とする。$Q$ のうち部分木が印を書かないものを $Q_0$ とすれば $\lvert Q\setminus Q_0\rvert\le8$ で、ある $I\subseteq Q_0$、$\lvert I\rvert\ge\lvert Q_0\rvert/5$ について、$I$ の全ての節点 $h$ の部分木を $\omega_{C_h}$（$C_h$ は $h$ の非終端）の導出に同時に差し替えた組 $\mathbf u^I\in L_A(G)$ は次を満たす。

各 $h\in I$ について、根の純な成分（長さ $\ge5$）の内部に、その成分の文字でない文字（**異文字**）の塊が新しく一つ以上でき、異なる $h$ の作る異文字の塊は別の塊である。異文字が入った純な成分の最初の二文字と最後の二文字は変わらない。

**証明。** 印は一つの節点が書くので、$Q$ の部分木は互いに交わらず $\lvert Q\setminus Q_0\rvert\le8$。

$h\in Q_0$ を単独で差し替えた組 $\mathbf u^h$ は $L_A(G)$ に入り、非削除性により $h$ の生成組の文字は全て $\mathbf u$ に現れるので、$\lVert\mathbf u^h\rVert_1<\lVert\mathbf u\rVert_1$（$\lVert\omega_{C_h}\rVert_1\le\theta<\ell_h$）。印は変わらないので、内容 $\{a,b\}$ の成分は内容を保つ。全ての成分の内容が保たれれば `lem:witness-length-template`(i)（$\lambda=\hat c$）により $\mathbf u^h\in L_X$ となり $T$ の選び方に反する。よってある純な成分に異文字が入り、それは $h$ のブロック（$h$ の生成組の成分が根の成分に占める区間）の中にある。ブロックは印を含まないので、その成分は長さ $\ge5$ で、ブロックは最初の二文字の後・最後の二文字の前にある。

各 $h$ のブロックは $\le2$ 個。同じ根成分の中で二つのブロックが間に文字なしで隣り合うとき持ち主を辺で結ぶと、最大次数は $\le4$ なので、大きさ $\ge\lvert Q_0\rvert/5$ の独立集合 $I$ がある。$I$ を同時に差し替えると、各 $h\in I$ のブロックの中身は単独の差し替えと同じなので、各 $h$ が異文字を入れる。純な成分の中で $I$ の異なる持ち主のブロックの間には、空でない隙間か $I$ 以外の持ち主のブロックがあり、どちらも元の文字（その成分の文字）のまま残る。よって異なる持ち主の異文字は別の塊に属し、各塊は両側を元の文字で囲まれた、語 $E_A[\mathbf u^I]$ の極大な塊である。□

### 系3.2（塊の数による上界）【証明済み】

$L\cap\Sigma^+$ の全ての語の極大な塊（a の塊と b の塊）の数が $\le k$ なら

$$
t_{\rm typ}(G,c)\le 9(r+1)v\theta\,(8+5k).
$$

**証明。** 補題3.1の $W=E_A[\mathbf u^I]\in L$ は $\lvert I\rvert$ 個以上の異なる塊を持つので $\lvert I\rvert\le k$、$\lvert Q_0\rvert\le5k$、$\lvert Q\rvert\le8+5k$。重い節点は祖先について閉じ、同じ深さの重い節点は反鎖で、深さは $\le9v$。よって重い節点は $\le9v(8+5k)$ 個。$\mathbf u$ の各文字は重い節点が直接書くか（$\le\theta$）、重い節点の軽い子（$\le r$ 個、各 $\le\theta$）に属する。根が軽ければ $\lVert\mathbf u\rVert_1\le\theta$。□

これは退避 `lem:app-u1-runs` の内容型付け版である。**反例族は、塊の数が超多項式の語を含まなければならない。**

---

## 4. 場合 I：$a^4$ と $b^4$ がともに現れる

### 補題4.1（分類）【証明済み】

$L\in\mathcal C_{2,c}$ が Parikh 飽和でなく、$a^4$ と $b^4$ がともに現れるとする。$L$ の各語 $w$ は次のどちらか。

(i) 極大な塊が3個以下。3個のとき中央の塊の長さは $\ge2$、または $w\in\{aba,bab\}$。
(ii) 全ての塊の長さが1（$a$ と $b$ が交互）。

**証明。** 補題2.1・系2.2は、$a$ と $b$ を入れ替えても成り立つ（$b^4$ が現れるので）。

塊が4個以上なら、a の塊と b の塊がそれぞれ2個以上あり、b の内部の塊 $\beta$ が少なくとも一つある。b の再配分で $\beta$ の余分を別の b の塊に移して $\beta$ を長さ1にできる（所属は変わらない）。このとき a の塊の長さが全て1でなければ、a の再配分で $\beta$ の左隣を長さ $\ge2$ にでき、因子 $aaba$ が現れ系2.2(i) に反する。よって元の $w$ の a の塊は全て長さ1（b の再配分は a の塊を変えない）。a の内部の塊も存在するので、対称に b の塊も全て長さ1。

塊が3個で $a^xb^ya^z$ なら、$y=1$ のとき $x+z\ge3$ なら一方を $\ge2$ にして $aaba$ か $abaa$、よって $x=z=1$。$b^xa^yb^z$ も対称。□

### 定理4.2（場合 I の線形上界）【証明済み】

補題4.1の仮定の下で、全ての型付き非終端について

$$
t_{\rm typ}(G,c)\le117(r+1)v\theta,\qquad \tau(G,c)\le117(r+1)v\theta,
$$

従って (1.2) により $\lVert K\rVert_+\le4^{2r}g\,(1+2\theta+117r(r+1)g\theta)+\mathbf 1_{\{\varepsilon\in L\}}$。深い挿入の有無は使わない。

**証明。** 補題3.1で $\lvert I\rvert\ge2$ とする。$W=E_A[\mathbf u^I]\in L$ を考える。異文字が入った純な成分（文字 $x$）は最初の二文字 $xx$ を保つので、$W$ は因子 $xx$ を持つ。

- 二つの異文字の塊が同じ純な成分（文字 $x$、異文字 $y$）にあれば、その成分の中に $x,y,x,y,x$ の塊が並ぶ。
- 別々の純な成分 $i<j$ にあれば、成分 $i$ に $x,y,x$、成分 $j$ に $x',y',x'$ の塊が並ぶ（$y,y'$ の塊はそれぞれ成分の内部で極大）。$x=x'$ なら $W$ には $x,y,x,y,x$ の塊が少なくともあり（真ん中の $x$ は合流しうる）、$x\ne x'$ なら6個以上。

どちらでも $W$ は4個以上の塊と因子 $xx$ を持ち、補題4.1に反する。よって $\lvert I\rvert\le1$、$\lvert Q_0\rvert\le5$、$\lvert Q\rvert\le13$。系3.2の証明と同じ数え上げで、重い節点は $\le13\cdot9v=117v$ 個、$\lVert\mathbf u\rVert_1\le117(r+1)v\theta$。□

**位置づけ**：二文字の両方の冪が現れる非飽和の言語は、塊が3個以下か完全に交互な語しか持たず、短縮で異文字が二箇所に入ると必ずその形を壊す。これが場合 I が易しい理由である。

---

## 5. 場合 II：核の切り分け

### 5.1 場合分けの網羅性【証明済み】

$L\in\mathcal C_{2,c}$ を任意に取る。

1. a の深い挿入（$a^6za^6$、$z$ に b）も b の深い挿入も無い → (A)。
2. 深い挿入があり Parikh 飽和 → (B)。
3. 深い挿入があり非飽和（このとき (C) により一文字の橋は自動的に無い）：
   - $a^4$ と $b^4$ がともに現れる → 定理4.2。
   - そうでなければ、深い挿入の側の文字（a とする）は $a^6$ を持つので $a^4$ が現れ、もう一方は $b^4$ が現れない。b の深い挿入は $b^6$ を要するので無い。これを**場合 II** と呼ぶ（対称の場合も同様）。

従って、残るのは場合 II だけである。場合 II では、全ての語の b の塊は長さ $\le3$、系2.2(ii) により $aa$ を含む語の b の内部の塊は長さ2か3。

### 5.2 $\{a\}$ を含まない型【証明済み】

場合 II では $b^6$ が現れないので、($\{b\},6$)-深い挿入は無い。`chatgpt_sl_positive` 定理2.1は成分型 $\{b\}$・$\{a,b\}$ だけの $X$ に適用でき、$\tau_X\le252(r+1)v\theta$。

### 5.3 $\{a\}$ と $\{a,b\}$ が混ざる型

#### 補題5.1（純な成分を一文字に縮める）【証明済み】

$a^4$ が現れるとし、$X=A_{(\{a\},\{a,b\})}$、$E_A=v_0\square_1v_1\square_2v_2$ とする。$(a^k,y)\in\operatorname{Cl}(X)$ なら、ある $y^+$（内容 $\{a,b\}$、$\lvert y^+\rvert=\lvert y\rvert+k-1$）について $(a,y^+)\in\operatorname{Cl}(X)$。$(\{a,b\},\{a\})$ も同様。

**証明。** $W=v_0a^kv_1yv_2\in L$。第一の穴を含む a の塊を $R$、$y$ の最初の a を含む a の塊を $R'$ とする。$R'\ne R$ なら、補題2.1で $R$ の（第一の穴の）a を $k-1$ 個 $R'$ の $y$ の中の部分に移す。骨格も a の個数も変わらない。$R'=R$ なら $v_1\in a^+$ で $y$ は a で始まり、$v_0a^kv_1yv_2=v_0\,a\,v_1\,(a^{k-1}y)\,v_2$ は同じ語である。どちらでも (1.1) から $(a,y^+)\in\operatorname{Cl}(X)$。□

#### 定理5.2（一穴の最短の詰め物）【証明済み】

$a^4$ が現れれば（場合 II に限らない）、型 $(\{a\},\{a,b\})$ と $(\{a,b\},\{a\})$ の $X$ について

$$
\tau_X\le(r+1)\theta(\theta+3)(\theta+4)v.
$$

**証明。** 補題5.1により、一穴文脈 $C:=v_0\,a\,v_1\,\square\,v_2$（$\lvert C\rvert_{\rm fix}\le\theta+1$）について、内容 $\{a,b\}$ の $y$ で $C[y]\in L$ となるものの最短の長さを抑えれば $\tau_X\le1+\lvert y\rvert$。最短の $y^*$ を取り、$W=C[y^*]\in L(G)$ の節点数最小の導出 $T$ を取る。$C$ の固定部分の全ての文字と、$y^*$ の a と b を一つずつに印を付ける。印は $M\le\theta+3$ 個で、印の無い文字は全て穴 $y^*$ の中にある。

(a) **印の無い節点は軽い**：部分木が印を書かない節点 $h$ のブロックは穴の中の区間なので、$\omega_{C_h}$ に差し替えると $C[y']$（$y'$ は印の a, b を保つ）で、重ければ短くなり $y^*$ の最小性に反する。

(b) **パスの長さ**：一つのパス上で同じ非終端 $B$ の節点 $u$（祖先）と $u'$ があり、その間の「環」（$u$ の生成組から $u'$ の生成組を除いた文字）が印を含まないとする。環の文字は全て穴の中にある。$u$ を $u'$ の部分木に差し替える。
   - $B$ のファンアウトが1、または $u'$ の二成分が $u$ の別々の成分にある場合：環の文字が消えるだけで、残りの順序は変わらない。
   - $u'$ の二成分 $y_1,y_2$ がともに $u$ の一つの成分にある場合：$u$ の生成組は $(p\,y_1\,m\,y_2\,q,\ s)$（または対称に $(s,\ p\,y_1\,m\,y_2\,q)$）。good な規則の合成では $y_1$ と $y_2$ の間の $m$ は空でなく（同じ子の二つの変数は、非結合性によりどの段でも空でない語を挟む）、$s$ も空でない（$\lambda$-free）。$m,s$ は環の文字なので穴の中にあり、穴は区間なので、$m$ と $s$ の間の全ての文字（$y_2$ と、$u$ の二成分の間の隙間 $g$）も穴の中にある。差し替え後は $[y_1]\,g\,[y_2]$ となり、動く文字は穴の中だけ。
   
   どの場合も結果は $C[y'']$（$y''$ は印の a, b を保つ）で、環が空でなければ短く、空なら `lem:app-u1-identity` により同じ語を少ない節点で導出する。いずれも矛盾。よって同じ $B$ の連続する出現の間の環は印を含み、環は互いに交わらないので、一つのパス上の $B$ の出現は $\le M+1$ 個、パスの長さは $\le v(M+1)$。

(c) **数え上げ**：生成組が印を含む節点は印へのパスの上にあり $\le Mv(M+1)$ 個。各々は $\le\theta$ 文字を書き、印の無い子（$\le r$ 個）は (a) により $\le\theta$。よって $\lvert W\rvert\le(r+1)\theta M(M+1)v$、$\tau_X\le1+\lvert y^*\rvert\le\lvert W\rvert$。□

**注意**：(b) が一穴でだけ成り立つ点が要である。二穴の両方に動く部分があると、$y_2$ が固定部分 $v_1$ を飛び越えうる。

### 5.4 純な a の穴への帰着

**定義。** 一穴文脈 $C=v_0\square v_1$ で $C[a^+]\cap L\neq\varnothing$ のものについて $P_a(C):=\min\{k\ge1:C[a^k]\in L\}$。また

$$
\Pi_G:=\max\{\pi_B\},\qquad \pi_B:=\min\{\lVert\mathbf x\rVert_1:\mathbf x\in L_B(G)\cap(a^+)^{\mathrm{fan}(B)}\}
$$

（純な a の組を持つ $B$ の上の最大）。

#### 補題5.3（純な型の帰着）【証明済み】

場合 II で、$X$ の型が $(\{a\})$、$(\{a\},\{a\})$、$(\{a\},\{b\})$、$(\{b\},\{a\})$ のいずれかなら、$\lvert C\rvert_{\rm fix}\le\theta+3$ のある一穴文脈 $C$（$C[a^+]\cap L\ne\varnothing$）について $\tau_X\le3+P_a(C)$。

**証明。** $(\{a\})$ は $C=E_A$。$(\{a\},\{a\})$：$E_A[(a^{k_1},a^{k_2})]$ の骨格は $k_1,k_2\ge1$ に依らないので、補題2.1により所属は $k_1+k_2$ だけで決まり、$C=v_0\,a\,v_1\square v_2$ で $\tau_X\le1+P_a(C)$。$(\{a\},\{b\})$：$L_X$ の元 $(a^k,b^j)$ を取ると $j\le3$（$b^4$ なし）。$C=v_0\square v_1b^jv_2$ で $\tau_X\le j+P_a(C)$。□

#### 定理5.4（$P_a$ の二つの上界）【証明済み】

場合 II（実際には $a^4$ が現れることだけを使う）で、$\lvert C\rvert_{\rm fix}\le\theta+3$ の一穴文脈 $C$ について

$$
P_a(C)\le\delta_L\ (\Delta_L\ne\varnothing\text{ のとき}),\qquad
P_a(C)\le(\theta+4)(\theta+5)\,v\,\bigl(\theta+r\max\{\theta,\Pi_G\}\bigr).
$$

**証明。** 第一式：系2.3で $\mathcal D_L(a)=\mathcal D_L(a^{1+\delta_L})$。$C[a^k]\in L$ で $k>\delta_L$ なら、穴の中の $a^{1+\delta_L}$ を $a$ に替えて $C[a^{k-\delta_L}]\in L$。繰り返して $k\le\delta_L$。

第二式：$k=P_a(C)$、$W=C[a^k]$ の節点数最小の導出を取り、固定部分の全ての文字と穴の最初の a に印を付ける（$M\le\theta+4$）。印の無い節点の生成組は穴の中、すなわち純な a の組で、その長さは $\pi_B$ に等しい（より短い純な組があれば差し替えて $C[a^{k'}]$、$1\le k'<k$）。定理5.2の (b) と同じ議論（環の文字は全て穴の中の a で、穴の最初の a は印で残るので結果は $C[a^{k''}]$、$k''\ge1$）でパスの長さは $\le v(M+1)$。印を含む節点は $\le Mv(M+1)$ 個、各々は $\le\theta$ 文字を書き、印の無い子は $\le r$ 個で各 $\le\max\{\theta,\Pi_G\}$。□

#### 系5.5（場合 II の上界のまとめ）【証明済み】

場合 II で

$$
\tau(G,c)\le\max\Bigl\{252(r+1)v\theta,\ (r+1)\theta(\theta+3)(\theta+4)v,\ 3+\min\bigl\{\delta_L,(\theta+4)(\theta+5)v(\theta+r\max\{\theta,\Pi_G\})\bigr\}\Bigr\}
$$

（$\Delta_L=\varnothing$ なら $\min$ は第二項）。特に $\delta_L$ または $\Pi_G$ が $g,\theta$ の多項式で抑えられる族では、$\tau$ と (1.2) の特徴標本は多項式。

**限界**：$\Pi_G$ は文法の量で、超多項式になりうる（`prop:typed-thickness-exponential` の文法では $L=\Sigma^+$ で $\tau=1$ なのに純な組は指数的に長い）。従って系5.5は「$\tau$ が超多項式なら $\Pi_G$ も超多項式」という必要条件を与えるが、$\Pi_G$ が大きいとき $\tau$ が大きいとは言わない。

---

## 6. 否定の向き：反例族の必要条件と有限の観察

### 6.1 増分の障害

#### 補題6.1（b の塊を2から3に伸ばす障害）【証明済み】

$L\in\mathcal C_{2,c}$ で $a^4$ が現れ、$b^4$ を持つ語が無いとする。$w\in L$ が長さ2の b の塊 $\beta$ を持ち、$\beta$ の左隣が a の塊で、$w^+\in L$ の骨格は $\sigma(w)$ の $\beta$ を長さ3にしたものとする。$\Delta:=\lvert w\rvert_a-\lvert w^+\rvert_a$ と置くと

$$
\lvert w^+\rvert_a<\rho_a(w^+)+\lvert\Delta\rvert.
$$

特に $\Delta=0$ の組は存在しない。右隣が a の塊の場合も対称。

**証明。** 反対に $\lvert w^+\rvert_a\ge\rho_a(w^+)+\lvert\Delta\rvert$ とする。$p:=\max\{1,1-\Delta\}$ と置くと $p\ge1$、$p+\Delta\ge1$、$\max\{p,p+\Delta\}=1+\lvert\Delta\rvert$。補題2.1で $w^+$ の $\beta$ の左隣の塊を長さ $\ge1+\lvert\Delta\rvert$ にした語 $w_3\in L$ を取る。

$w_3=U\,a^p\,bb\,b\,V$（$a^p$ は左隣の塊の最後の $p$ 文字、$bb$ は $\beta$ の最初の二文字）と書き、$x:=a^pbb$、$y:=a^{p+\Delta}b$（ともに内容 $\{a,b\}$）、$E:=(U,bV)$ とする。$E[x]=w_3\in L$。$E[y]=Ua^{p+\Delta}bbV$ は左隣の塊の長さが $\ge1$、$\beta$ の長さが2、a の個数が $\lvert w^+\rvert_a+\Delta=\lvert w\rvert_a$ で骨格 $\sigma(w)$ なので、補題2.1により $L$ に入る。よって $\mathcal D^{(1)}_L(x)=\mathcal D^{(1)}_L(y)$。

次に $w_3=U'\,a^{p+\Delta}\,b\,bb\,V'$（左隣の塊の最後の $p+\Delta$ 文字、$\beta$ の最初の一文字）と書き $F:=(U',bbV')$ とすると、$F[y]=w_3\in L$ なので $F[x]=U'a^pbbbbV'\in L$。これは $b^4$ を含み、仮定に反する。□

この補題は arity 1 しか使わない（補題2.1を通して arity 2 も使う）。b の塊の長さの「符号」で情報を運ぶ設計は、伸ばす操作ごとに、その語の a の余り（$\lvert w\rvert_a-\rho_a(w)$）を超える a の個数の変化を伴わなければならない。

### 6.2 反例族が満たすべき条件（まとめ）

$\Sigma=\{a,b\}$、固定の $r\ge2$ で、$\lVert G_n\rVert,\bar\theta_{G_n}=n^{O(1)}$ なのに $\tau(G_n,c)$ が超多項式な族 $(L_n,G_n)$ があれば、$a,b$ を適当に入れ替えて、十分大きな $n$ で次が全て成り立つ。

1. **場合 II**（§5.1、定理4.2）：a の深い挿入があり、$b^4$ を持つ語は無く、Parikh 飽和でない。
2. **a 塊の再配分**（補題2.1）：所属は（a 骨格, a の個数）の関数。$aa$ を持つ語の b の内部の塊は長さ2か3（系2.2）。
3. **純な型でだけ大きい**（系5.5）：大きな $\tau_X$ は型 $(\{a\})$、$(\{a\},\{a\})$、$(\{a\},\{b\})$、$(\{b\},\{a\})$ に限られ、$P_a(C)$ が超多項式。
4. **a の剛さ**（定理5.4）：$\Delta_L=\varnothing$ か、$\delta_L$ が超多項式。
5. **純な組が長い**（定理5.4）：$\Pi_{G_n}$ が超多項式。最短の純な組が長い非終端 $B$ の短い組 $\omega_B$ は b を含む。
6. **塊が多い**（系3.2）：塊の数が超多項式の語を含む。
7. **増分の障害**（補題6.1）：骨格が「一つの b の塊を2から3に伸ばしただけ」異なる二語は、a の余りが小さい語でしか共存できない。

加えて、先行報告の条件（長さの種類の定理により、有限族なら語の長さが超多項式種類、`lem:power-transfer`、同じ語の切り直し）も満たす必要がある。条件 4 と 7 を合わせると、b の塊の長さの列（骨格）で桁を符号化し、骨格ごとに a の個数を一つに固定する設計が残る候補だが、その設計で骨格の部分列どうしの交換（内容 $\{a,b\}$ の一穴・二穴の組）を全て制御できるかは確かめていない。

### 6.3 有限の観察

付録のスクリプト（標準ライブラリのみ）は、述語で与えた言語の受理語（長さ ≤ LMAX）に現れる全ての arity 1・2 の組と許容文脈を集め、内容が成分ごとに等しく共通の受理文脈を持つ二組について、観察された文脈で所属が食い違わないかを調べる。所属は述語で判定するので、LMAX より長い語も判定に使われる。**観察であって証明ではない。**

| 言語 | 結果 | 解釈 |
|---|---|---|
| $a^*bba^*$（長さ ≤11） | arity 1・2 とも違反なし | (D) と整合 |
| b の塊が全て長さ2か3（端も含む。長さ ≤9） | arity 1 で $a^4bba$ と $a^7bb$ が文脈 $(\varepsilon,\varepsilon)$ を共有し、文脈 $(\varepsilon,bb)$ で後者だけ $b^4$ を作る | 内容 $\{a,b\}$ の組の「b の塊の位置」の違いが、別の文脈で塊の合流を起こす |
| b の塊が全て長さ2（長さ ≤11） | 同じ形の違反（$a^6bba$ と $a^9bb$、文脈 $(\varepsilon,bb)$） | 同上。b の塊の長さを一つにしても防げない |
| 剛い玩具：b の塊 $\{2,3\}$、$\lvert w\rvert_a=12-2\#_2-3\#_3$（長さ ≤14） | arity 1 で $a^9bb$ と $a^8bba$ が文脈 $(\varepsilon,a)$ を共有し、文脈 $(\varepsilon,b)$ で前者は長さ3の塊（a を一つ減らして受理）、後者は長さ1の塊を作り不受理 | 補題6.1と同じ機構（塊を2から3に伸ばす代わりに a を一つ払う、$\Delta=1$） |
| 剛い玩具：b の塊は長さ2だけ、$\lvert w\rvert_a=14-3\#$（長さ ≤14） | 違反（$a^7bba$ と $a^8bb$、文脈 $(\varepsilon,bb)$ で $b^4$） | 剛さ（骨格ごとに a の個数が一つ）だけでは塊の合流を防げない |
| 補題2.1の確認（$a^*bba^*$ と「b の塊が全て長さ2」、長さ ≤10） | 所属は（骨格, a の個数, 長さ）の関数 | 補題2.1と整合（後者は代入可能でないが、骨格の関数であることは定義から明らか） |

剛い玩具が二つとも壊れることは、条件 4 だけでは足りず、内容 $\{a,b\}$ の組の交換（b の塊の位置・長さの変化）が全ての文脈で塊の合流や長さ1の塊を生まないような骨格の設計が必要であることを示唆する（観察）。

---

## 7. 二文字の場合の全体の結論

**言えたこと（証明済み）**：$\Sigma=\{a,b\}$、内容型付け、ファンアウト2、ランク $\le r$ で、$L\in\mathcal C_{2,c}$ の reduced good な表示 $G$ について、$\tau(G,c)$（従って `cor:distribution-representatives` により $\mathcal B^{\le r}_{2,c}$ と $\mathcal B_{2,c}$ の共通の特徴標本の長さ）は、次のどれかなら $g,\theta$ の多項式で抑えられる。

- 深い挿入が無い（(A)、$O_r(v\theta)$）。
- Parikh 飽和（(B)、$O_r(v^2\theta^5)$）。
- $a^4$ と $b^4$ がともに現れる（定理4.2、$117(r+1)v\theta$。飽和なら (B)）。
- 場合 II で、$\delta_L$ または $\Pi_G$ が多項式（系5.5）。
- 塊の数が多項式の語しか持たない（系3.2）。

場合 II でも、成分に $\{a,b\}$ を含む型と $\{a\}$ を含まない型は常に多項式（§5.2、定理5.2）。

**言えなかったこと（未解決）**：場合 II で a 剛（または $\delta_L$ が超多項式）、かつ $\Pi_G$ と塊の数が超多項式の言語について、$P_a(C)$ が多項式か。止まった場所は次の一点である：純な a の穴 $C[a^k]$ の最短の $k$ を、文法の短縮（短い組 $\omega_B$ は b を含む）と、内容 $\{a,b\}$ の組の交換（純な側とは内容が違うので直接は比べられない）の二つだけで抑える議論が無い。この量を抑えれば、二文字の内容型付けは肯定で解決する。逆に、§6.2 の 1–7 を満たす族を作り、$L_n\in\mathcal C_{2,c}$（arity 1 と 2）を証明すれば否定で解決する。

**論文の未解決問題 `op:fanout-two` との関係**：二文字でも結論は出ていないので、`prop:sl-reduction` による $\mathbf{SL}$ の判定にはまだ使えない。三文字以上では、補題2.1は各文字について同じ形で成り立つ（成分の内容は $\{x\}$ だけ）が、骨格が多文字になるので、本報告の場合分けはそのままでは移らない。

---

## 8. 文献

- Yoshinaka, *Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*, TCS 412 (2011) 1821–1831：組代入可能性と許容文脈の定義。
- Clark–Eyraud, *Polynomial identification in the limit of substitutable context-free languages*, JMLR 8 (2007)：代入可能性の原型。
- 栗山 `main.tex`、退避 `lem:app-u1-*`、`reviews/chatgpt_sl_positive_2026-11-01.md`、`reviews/chatgpt_sl_fanout2_2026-11-01.md`、`reviews/chatgpt_parikh_closed_family_2026-11-01.md`：本報告の直接の依存先。
- 補題2.1（再配分による骨格飽和）、補題3.1・系3.2（内容型付けの挿入補題）、定理4.2、定理5.2、定理5.4、補題6.1 が文献に同じ形であるか：**未確認**（網羅的な文献調査はしていない）。補題2.1は `lem:app-u1-transfer`(i) の繰り返しであり、独立の新規性は主張しない。

---

## 付録：スクリプト全文と出力

保存名 `binary_core_check.py`、Windows では `py -3 binary_core_check.py`。Python 3 の標準ライブラリだけを使う。結果は**観察**であり、無限の言語や全ての長さについての証明ではない。

```python
# binary_core_check.py -- Python 3 standard library only.
# Run on Windows with:  py -3 binary_core_check.py
#
# Finite OBSERVATION tool (not a proof).  For a language given by a
# membership predicate over {a,b}, it enumerates the accepted words of
# length <= LMAX, collects every arity-1 and arity-2 tuple occurrence with
# its admissible context (holes nonempty, the gap between the two holes
# nonempty), and looks for a violation of (d, c)-tuple substitutability for
# the content typing c(w) = set of letters of w:
#   x, y with componentwise equal contents, a common accepting context E,
#   and an observed context F accepting one of them but not the other.
# Membership of F[x], F[y] is decided by the predicate, so words longer
# than LMAX are also tested; only the contexts are limited to observed ones.
# "PASS" therefore means: no violation among observed contexts up to LMAX.

from collections import defaultdict
from itertools import product, combinations
import re


def content(w):
    return "".join(sorted(set(w)))


def fill(ctx, parts):
    return "".join(ctx[i] + parts[i] for i in range(len(parts))) + ctx[-1]


def occurrences(w, d):
    n = len(w)
    for cuts in combinations(range(n + 1), 2 * d):
        iv = [(cuts[2 * j], cuts[2 * j + 1]) for j in range(d)]
        if any(s == e for s, e in iv):
            continue
        if any(iv[j][0] == iv[j - 1][1] for j in range(1, d)):
            continue  # inner gap must be nonempty
        parts = tuple(w[s:e] for s, e in iv)
        ctx = tuple([w[:iv[0][0]]]
                    + [w[iv[j][1]:iv[j + 1][0]] for j in range(d - 1)]
                    + [w[iv[-1][1]:]])
        yield parts, ctx


def check(member, lmax, arities=(1, 2), name=""):
    words = [w for n in range(1, lmax + 1)
             for w in map("".join, product("ab", repeat=n)) if member(w)]
    report = []
    for d in arities:
        dist = defaultdict(set)      # tuple -> observed accepting contexts
        for w in words:
            for parts, ctx in occurrences(w, d):
                dist[parts].add(ctx)
        groups = defaultdict(list)   # (types, context) -> tuples
        for parts, ctxs in dist.items():
            typ = tuple(map(content, parts))
            for c in ctxs:
                groups[(typ, c)].append(parts)
        found = None
        checked = set()
        for (typ, shared), members in sorted(groups.items()):
            if found:
                break
            members = sorted(members)
            lead = members[0]
            for other in members[1:]:
                key = (lead, other)
                if key in checked:
                    continue
                checked.add(key)
                for x, y in ((lead, other), (other, lead)):
                    for F in sorted(dist[x]):
                        if not member(fill(F, y)):
                            found = (x, y, shared, F, fill(F, x), fill(F, y))
                            break
                    if found:
                        break
                if found:
                    break
        if found is None:
            report.append("  arity %d: PASS (observed contexts, length <= %d)"
                          % (d, lmax))
        else:
            x, y, E, F, wx, wy = found
            report.append("  arity %d: FAIL  x=%s y=%s shared E=%s;"
                          " F=%s gives %s in L but %s not in L"
                          % (d, x, y, E, F, wx, wy))
    print(name)
    print("  accepted words up to length %d: %d" % (lmax, len(words)))
    for line in report:
        print(line)


def b_runs(w):
    return [len(m) for m in re.findall(r"b+", w)]


def a_runs(w):
    return [len(m) for m in re.findall(r"a+", w)]


# (D) of the prompt: a* bb a*.
def L_D(w):
    return w.count("b") == 2 and "bb" in w


# Free Case-II-like language: every b-run (also at the ends) has length
# 2 or 3.  Prediction (Section 6): NOT substitutable.
def L_free23(w):
    return all(e in (2, 3) for e in b_runs(w))


# Every b-run has length exactly 2 (no condition at the ends).
def L_bb_only(w):
    return all(e == 2 for e in b_runs(w))


# A rigid toy (Section 6.3): skeleton = sequence of b-run lengths in {2,3};
# membership iff every b-run is in {2,3} and
# |w|_a = N - 2*(#2-runs) - 3*(#3-runs).  Predicted to fail (increment).
def make_rigid(N):
    def L(w):
        r = b_runs(w)
        if any(e not in (2, 3) for e in r):
            return False
        return w.count("a") == N - 2 * r.count(2) - 3 * r.count(3)
    return L


# Rigid toy with a single b-run length (2): |w|_a = N - 3*(#runs).
def make_rigid_bb(N):
    def L(w):
        r = b_runs(w)
        if any(e != 2 for e in r):
            return False
        return w.count("a") == N - 3 * len(r)
    return L


# Redistribution lemma sanity check: for a predicate that passed, verify
# that among accepted words containing aaaa, membership depends only on
# (a-skeleton, |w|_a) within the enumerated range.
def skeleton(w):
    return re.sub(r"a+", "a", w)


def redistribution_observation(member, lmax, name):
    seen = defaultdict(set)
    words = [w for n in range(1, lmax + 1)
             for w in map("".join, product("ab", repeat=n))]
    has_a4 = any(member(w) and "aaaa" in w for w in words)
    bad = None
    for w in words:
        seen[(skeleton(w), w.count("a"), len(w))].add(member(w))
    for key, vals in seen.items():
        if len(vals) > 1:
            bad = key
            break
    print(name, "| a^4 present:", has_a4,
          "| membership a function of (skeleton, |w|_a, |w|):",
          bad is None)


if __name__ == "__main__":
    check(L_D, 11, name="L_D = a* bb a*")
    check(L_free23, 9, name="L_free23 (b-runs in {2,3})")
    check(L_bb_only, 11, name="L_bb_only (all b-runs = 2)")
    check(make_rigid(12), 14, name="rigid toy N=12, weights 2/3")
    check(make_rigid_bb(14), 14, name="rigid toy N=14, only bb, weight 3")
    redistribution_observation(L_D, 10, "L_D")
    redistribution_observation(L_bb_only, 10, "L_bb_only")
```

出力（Python 3、Linux、約3秒。探索順は整列してあり、`PYTHONHASHSEED` を変えても同じ出力になることを確認した）：

```text
L_D = a* bb a*
  accepted words up to length 11: 55
  arity 1: PASS (observed contexts, length <= 11)
  arity 2: PASS (observed contexts, length <= 11)
L_free23 (b-runs in {2,3})
  accepted words up to length 9: 166
  arity 1: FAIL  x=('aaaabba',) y=('aaaaaaabb',) shared E=('', ''); F=('', 'bb') gives aaaabbabb in L but aaaaaaabbbb not in L
  arity 2: FAIL  x=('a', 'aabba') y=('a', 'aaaaabb') shared E=('', 'a', ''); F=('', 'a', 'bb') gives aaaabbabb in L but aaaaaaabbbb not in L
L_bb_only (all b-runs = 2)
  accepted words up to length 11: 186
  arity 1: FAIL  x=('aaaaaabba',) y=('aaaaaaaaabb',) shared E=('', ''); F=('', 'bb') gives aaaaaabbabb in L but aaaaaaaaabbbb not in L
  arity 2: FAIL  x=('a', 'aaaabba') y=('a', 'aaaaaaabb') shared E=('', 'a', ''); F=('', 'a', 'bb') gives aaaaaabbabb in L but aaaaaaaaabbbb not in L
rigid toy N=12, weights 2/3
  accepted words up to length 14: 273
  arity 1: FAIL  x=('aaaaaaaaabb',) y=('aaaaaaaabba',) shared E=('', 'a'); F=('', 'b') gives aaaaaaaaabbb in L but aaaaaaaabbab not in L
  arity 2: FAIL  x=('a', 'bbaaaaaaaa') y=('a', 'aaaaaaaabb') shared E=('', 'a', ''); F=('', 'b', '') gives abbbaaaaaaaa in L but abaaaaaaaabb not in L
rigid toy N=14, only bb, weight 3
  accepted words up to length 14: 69
  arity 1: FAIL  x=('aaaaaaabba',) y=('aaaaaaaabb',) shared E=('', 'aaa'); F=('', 'bb') gives aaaaaaabbabb in L but aaaaaaaabbbb not in L
  arity 2: FAIL  x=('a', 'aaaaaaabb') y=('a', 'bbaaaaaaa') shared E=('', 'a', 'aa'); F=('', 'bb', '') gives abbaaaaaaabb in L but abbbbaaaaaaa not in L
L_D | a^4 present: True | membership a function of (skeleton, |w|_a, |w|): True
L_bb_only | a^4 present: True | membership a function of (skeleton, |w|_a, |w|): True
```

**検査の位置づけ**：FAIL は具体的な違反の組と文脈なので、その言語が $(d,c)$-代入可能でないことの**証明**として読める（示された二語の所属を確かめればよい）。PASS は観察された文脈の範囲での観察に過ぎない。最後の二行は、列挙した長さの範囲で、所属が（骨格, a の個数, 長さ）の関数であることの観察である。
