# 定理A の ‖G‖ 一つ分の差：窓の型付け $s_{1,1}$ と族 $F_n$（Claude 報告、2026-11-02）

依頼：`reviews/prompt_claude_gap_window_2026-11-02.md`（方向性 B1）。
対象：$\Sigma=\{\mathtt a,\mathtt c,\mathtt l,\mathtt r\}$、$E_0\to\mathtt a$、$E_i\to\mathtt lE_{i-1}E_{i-1}\mid\mathtt cE_{i-1}\mathtt r$（$1\le i\le n$）、$F_n=L(E_n)$、ファンアウト1、ランク2、型付け $s=s_{1,1}$、作用素 $\mathcal B_{1,s}$ と $\mathcal B^{\le2}_{1,s}$。
長さは原稿どおり $\|K\|_+=\sum_{w\in K}(|w|+1)$。$\|G_n\|=12n+3$、$\bar\theta_{G_n}=4n-1$（README (17)）。

## 判定表

| # | 主張 | 判定 | 根拠 |
|---|---|---|---|
| 1 | $n\ge2$ で、明示的な標本 $K_n=K^{\mathrm{int}}_n\cup K^{\mathrm{seg}}_n\subseteq F_n$ は $\mathcal B^{\le2}_{1,s_{1,1}}$ と $\mathcal B_{1,s_{1,1}}$ の両方について $F_n$ の特徴標本であり、$\|K^{\mathrm{seg}}_n\|_+\le4n^2(\lceil\log_2n\rceil+1)+4n(\lceil\log_2n\rceil+1)+88n^2$ | **証明済み**（$K^{\mathrm{int}}_n$ の部分は Astra 第5回 §2 の定理を引用。README (26) で検証済み） | §2 |
| 2 | したがって $n^2+7n+4\le\mathrm{cs}_{\mathcal B,s_{1,1}}(F_n)=\mathrm{cs}_{\mathcal B^{\le2},s_{1,1}}(F_n)\le O(n^2\log n)=O(\|G_n\|\bar\theta_{G_n}\log\|G_n\|)$。**$\Omega(n^3)$ は偽**であり、$F_n$ は（この作用素・型付けで）$\Omega(\|G\|^2\bar\theta_G)$ を与える族ではない | **証明済み**（1 から） | §2.5 |
| 3 | 上の構成法（区間の二分木で背骨を分ける「区分クラス」の方法）は、木をどう選んでも $\Omega(n^2\log n)$ を要する | **証明済み（この構成法に限る）**。作用素 $\mathcal B$ の下界ではない | §2.6 |
| 4 | $\mathrm{cs}(F_n)$ は $\Theta(n^2)$ か $\Theta(n^2\log n)$ か | **未解決** | §4 |
| 5 | 「各段 $j$ に、左の子が $\mathtt a$ で終わる $\mathtt l$ 節点が標本の構文木に現れる必要がある」（README (17) の Claude の注、(19)(e) の重み不等式による $\Omega(n^3)$ の道筋）は $s_{1,1}$ でも成り立たない | **反証**（Astra 第5回 (7) と語長の評価から） | §3.1 |
| 6 | ファンアウト1の任意の型付けで、Comp 節点の型板をどこで切っても、観測語の左右の部分と導出された語の左右の部分は型付き合同になる（切れ目の両隣の文字は一致する） | **証明済み**（原稿の補題の組合せ） | §3.2 |
| 7 | $n=2,3,4$ で $K_n$ が $F_n$ の全語を生成する。$n=5$ で構造的な128語と無作為な約4,500語を生成する。Astra (8)（$b=\mathtt l$）は $n\le5$ の全事例で成り立つ。特徴標本 $K_n$ の語に現れる「左の子が $\mathtt a$ で終わる $\mathtt l$ 節点」の段は $\{2,3\}$ だけ（$n=4,5,8,12$） | **観察**（有限の検査） | §5 |
| 8 | $K^{\mathrm{int}}_n$ に足す末尾 $\mathtt a$ の語の必要数（限られた候補から）：$n=4$ で2語（全504語で検査）、$n=5$ で3語（2語では120組すべて失敗、抽出検査） | **観察** | §5 |
| 9 | Q2：窓の型付け・ファンアウト1での $\Lambda=O(\|G\|\bar\theta_G)$、または $\Lambda$ が大きい族 | **未解決**（一般化の方向だけを記す） | §4.2 |
| 10 | 以前の報告の誤り | 新たな誤りは見つからなかった。README (26) の「$F_n$ は $s_{1,1}$ で $\Omega(\|G\|^2\bar\theta_G)$ の最有力候補」は本報告で否定される（誤りではなく、更新）。第6回 ChatGPT 報告の「未解決 A」（総長 $O(n^2)$ の追加語）は $O(n^2\log n)$ まで進むが、$O(n^2)$ としては未解決のまま | §2.5 |

**要旨.** Q1 の答えは「$\Theta(n^3)$ ではない」。末尾 $\mathtt a$ の背骨を、段の区間の二分木に沿って「区分」に分け、各区分クラスに2語ずつの短い包み文脈を与えると、背骨の乗り換えの費用が各段あたり $O(i\log n)$ に下がる。$\Theta(n^2)$ と $\Theta(n^2\log n)$ のどちらかは未決着である。結果として、$F_n$ と $s_{1,1}$ からは「定理A(i) が $\mathcal B$ について鋭い」という結論は得られない。

---

## 1. 記号

- $C_i=\mathtt c^i\mathtt a\mathtt r^i$、$D_0^{\mathtt a}=\mathtt a$、$D_i^{\mathtt c}=C_i$、$D_i^{\mathtt l}=\mathtt lC_{i-1}C_{i-1}$（$i\ge1$）、$U_0=\mathtt a$、$U_i=\mathtt lC_{i-1}U_{i-1}$。$|C_i|=2i+1$、$|D_i^{\mathtt l}|=4i-1$。
- $P(0)=\{\mathtt a\}$、$P(i)=\{\mathtt c,\mathtt l\}$（$i\ge1$）。$P(i)$ は $L_i:=L(E_i)$ の語の先頭文字の集合。
- $s_{1,1}$：長さ2以上の語 $w$ には $\langle w_1,w_{|w|}\rangle$、1文字の語にはその語自身（別の札）を対応させる（`def:prefix-suffix-typing`、$k=\ell=1$、$m_0=2$）。
- 文脈 $\mathcal E_1$ は $u\blank v$（$u,v\in\Sigma^*$）。
- $F_n$ は Clark–Eyraud 代入可能（README (17)）。ファンアウト1では、共通の文脈を持つ同じ型の2語は型付き合同なので、$F_n$ は $(1,s)$-代入可能である。よって `prop:reconstruction-soundness` により、任意の有限 $K\subseteq F_n$ で $L(\mathcal B^{\le r}_{1,s}(K))\subseteq F_n$。
- **単調性.** $K\subseteq K'$ なら $\mathcal B^{\le2}_{1,s}(K)$ の規則はすべて $\mathcal B^{\le2}_{1,s}(K')$ の規則である（観測、文脈、合成の証人が増えるだけ）。また $\mathcal B^{\le2}_{1,s}(K)$ の規則は $\mathcal B_{1,s}(K)$ の規則でもある（$\|K\|_+\ge2$）。したがって $F_n\subseteq L(\mathcal B^{\le2}_{1,s}(K))$ を示せば、$K$ は両作用素の特徴標本になる（`def:characteristic-sample`）。

## 2. 上界：$\mathrm{cs}_{\mathcal B,s_{1,1}}(F_n)=O(n^2\log n)$

### 2.1 区分

$0\le b<a\le n$ に対し、区分の集合を
$$
\mathrm{seg}(a,b)=
\begin{cases}
\{x_{a-1}\,\mathtt l\,x_{a-2}\,\mathtt l\cdots x_b\,\mathtt l : x_i\in L_i\} & (b\ge1),\\[2pt]
\{x_{a-1}\,\mathtt l\,x_{a-2}\,\mathtt l\cdots x_1\,\mathtt l\,\mathtt a\,\mathtt a : x_i\in L_i\} & (b=0)
\end{cases}
$$
と定める（$b=0$ の末尾 $\mathtt a\mathtt a$ は $x_0\,V_0=\mathtt a\,\mathtt a$）。区分 $s$ の第 $i$ 段の語 $x_i$ を「$s$ の段 $i$」と呼ぶ。

**補題2.1.**
(a) $b<c<a$ なら $\mathrm{seg}(a,b)=\mathrm{seg}(a,c)\cdot\mathrm{seg}(c,b)$。$s\in\mathrm{seg}(a,b)$ をこの形に $s=s_1s_2$ と分けると、$\mathrm{first}(s_1)=\mathrm{first}(s)=\mathrm{first}(x_{a-1})$、$\mathrm{first}(s_2)=\mathrm{first}(x_{c-1})\in P(c-1)$。
(b) $F_n$ の末尾 $\mathtt a$ の語は、ちょうど $\mathtt l\cdot\mathrm{seg}(n,0)$ の語である。
(c) $Q_b:=C_{b-1}C_{b-1}$（$b\ge1$）、$Q_0:=\varepsilon$、$E_{a,b}:=\mathtt c^{n-a}\mathtt l\,\blank\,Q_b\mathtt r^{n-a}$ とおく。任意の $s\in\mathrm{seg}(a,b)$ で $E_{a,b}[s]\in F_n$。
(d) $\mathrm{seg}(a,b)$ の語はすべて長さ2以上で、型は $b\ge1$ なら $\langle\mathrm{first}(x_{a-1}),\mathtt l\rangle$、$b=0$ なら $\langle\mathrm{first}(x_{a-1}),\mathtt a\rangle$。

*証明.* (a) 定義から直ちに従う（段の列を $c$ で切る）。(b) $\mathtt c$ 規則の語は $\mathtt r$ で終わるので、$L_i$ の末尾 $\mathtt a$ の語は $\mathtt l\,x\,V$（$x\in L_{i-1}$、$V$ は $L_{i-1}$ の末尾 $\mathtt a$ の語）であり、$L_1$ の末尾 $\mathtt a$ の語は $\mathtt{laa}$ だけ。段数の帰納法で、$L_a$ の末尾 $\mathtt a$ の語は $\mathtt l\cdot\mathrm{seg}(a,0)$。$a=n$ とすればよい。(c) $b\ge1$ のとき $\mathtt l\,s\,Q_b=\mathtt l x_{a-1}(\mathtt l x_{a-2}(\cdots(\mathtt l x_b(\mathtt lC_{b-1}C_{b-1}))\cdots))$ は内側から $L_b,L_{b+1},\dots,L_a$ の語になる。$b=0$ のときは (b) の証明から $\mathtt l s\in L_a$。最後に $\mathtt c^{n-a}L_a\mathtt r^{n-a}\subseteq L_n$。(d) $\mathrm{seg}(1,0)=\{\mathtt{aa}\}$、それ以外は $x\,\mathtt l$ 以上の長さを持つ。末尾は $b\ge1$ なら背骨の $\mathtt l$、$b=0$ なら $\mathtt a$。$\square$

### 2.2 区間の二分木と区分クラスの代表

**木 $T_n$.** 根は $(n,0)$。$a-b\ge2$ の節点 $(a,b)$ は $c=\lceil(a+b)/2\rceil$ で子 $(a,c)$、$(c,b)$ を持つ。$a-b=1$ の節点は葉。$T_n$ は葉が $n$ 個の二分木で、節点数 $2n-1$、高さ $h\le\lceil\log_2n\rceil$。同じ深さの節点の区間 $[b,a)$ は互いに素である。

**代表.** $(a,b)\in T_n$、$p\in P(a-1)$ に対し、$\mathrm{can}(a,b,p)\in\mathrm{seg}(a,b)$ を
$$
\mathrm{can}(a,b,p)=
\begin{cases}
\mathtt{aa} & (a,b)=(1,0),\\
D_{a-1}^p\,\mathtt l & a-b=1,\ b\ge1,\\
\mathrm{can}(a,c,p)\cdot\mathrm{can}(c,b,q_0) & a-b\ge2,\ q_0:=\min P(c-1)
\end{cases}
$$
で定め（$\min P(c-1)$ は $\mathtt a$ または $\mathtt c$）、**区分クラス $(a,b,p)$ の成員**を
$$
M(a,b,p)=
\begin{cases}
\{\mathrm{can}(a,b,p)\} & a-b=1,\\
\{\mathrm{can}(a,c,p)\cdot\mathrm{can}(c,b,q): q\in P(c-1)\} & a-b\ge2
\end{cases}
$$
とする。$\mathrm{can}(a,b,p)\in M(a,b,p)$ であり、$M(a,b,p)$ の語はすべて先頭が $p$ で、型は補題2.1(d)により $(a,b,p)$ だけで決まる。

**標本.**
$$
K^{\mathrm{seg}}_n=\{E_{a,b}[m]:(a,b)\in T_n,\ p\in P(a-1),\ m\in M(a,b,p)\},\qquad
K_n=K^{\mathrm{int}}_n\cup K^{\mathrm{seg}}_n .
$$
ここで $K^{\mathrm{int}}_n$ は Astra 第5回報告 §2.4 の内部標本 (6)（総長 $O(n^2)$）。補題2.1(c) により $K_n\subseteq F_n$。根 $(n,0)$ では $E_{n,0}=\mathtt l\blank$ なので、$\mathtt l\,m$（$m\in M(n,0,p)$）は末尾 $\mathtt a$ の文として $K_n$ に入る。

例（$n=4$）：$T_4$ は $(4,0)\to(4,2),(2,0)$、$(4,2)\to(4,3),(3,2)$、$(2,0)\to(2,1),(1,0)$。$M(4,0,\mathtt c)=\{C_3\mathtt l\,C_2\mathtt l\,C_1\mathtt l\,\mathtt{aa},\ C_3\mathtt l\,C_2\mathtt l\,D_1^{\mathtt l}\mathtt l\,\mathtt{aa}\}$ で、$K^{\mathrm{seg}}_4$ は15語、$\|K^{\mathrm{seg}}_4\|_+=308$。

### 2.3 引用する補題（Astra 第5回 §2、README (26) で検証済み）

**補題2.2.** $K^{\mathrm{int}}_n\subseteq K$ なら、$\mathcal B^{\le2}_{1,s_{1,1}}(K)$ で
(i) 末尾 $\mathtt r$ の $F_n$ の語はすべて導出できる（Astra (7)）。
(ii) $1\le i\le n-1$、$p\in\{\mathtt c,\mathtt l\}$、$w\in L_i$、$\mathrm{first}(w)=p$ なら $[D_i^p\mathtt l]\Rightarrow^*w\mathtt l$（Astra (8) の $b=\mathtt l$。$(i,\mathtt l)\in\mathcal I_n$）。

単調性により、$K$ が $K^{\mathrm{int}}_n$ を含めばよい。§5 で (ii) を $n\le5$ の全事例で独立に確かめた（観察）。

### 2.4 主補題

**補題2.3.** $K\supseteq K_n$ とする。任意の $(a,b)\in T_n$、$p\in P(a-1)$、$m\in M(a,b,p)$、および $\mathrm{first}(s)=p$ を満たす任意の $s\in\mathrm{seg}(a,b)$ について、$\mathcal B^{\le2}_{1,s_{1,1}}(K)$ で $[m]\Rightarrow^*s$。

*証明.* $a-b$ の帰納法。

*葉.* $(1,0)$：$m=s=\mathtt{aa}$、Const。$a-b=1$、$b\ge1$：$m=D_{a-1}^p\mathtt l$、$s=w\mathtt l$（$w\in L_{a-1}$、先頭 $p$）。$a-1\in[1,n-1]$ なので補題2.2(ii)。

*内部の節点.* $a-b\ge2$、$c=\lceil(a+b)/2\rceil$。補題2.1(a) で $s=s_1s_2$、$s_1\in\mathrm{seg}(a,c)$（先頭 $p$）、$s_2\in\mathrm{seg}(c,b)$、$q:=\mathrm{first}(s_2)\in P(c-1)$ と分ける。$m_q:=\mathrm{can}(a,c,p)\,\mathrm{can}(c,b,q)\in M(a,b,p)$ とする。

1. **Link.** $m\ne m_q$ なら、$m$ と $m_q$ は型が等しく（補題2.1(d)）、同じ文脈 $E_{a,b}$ で $K$ に入っている（$E_{a,b}[m],E_{a,b}[m_q]\in K^{\mathrm{seg}}_n$）。よって Link 規則 $[m]\to[m_q]$ がある。
2. **Comp.** $m_q$ は観測され（$K$ の語の因子）、$\mathrm{can}(a,c,p)$ と $\mathrm{can}(c,b,q)$ は空でない因子なので、隙間のない二項の合成の証人 $[m_q]\to[\mathrm{can}(a,c,p)][\mathrm{can}(c,b,q)]$ がある（ランク2）。
3. **帰納法.** $(a,c),(c,b)\in T_n$ であり、$\mathrm{can}(a,c,p)\in M(a,c,p)$、$\mathrm{can}(c,b,q)\in M(c,b,q)$。区間が短いので、帰納法の仮定から $[\mathrm{can}(a,c,p)]\Rightarrow^*s_1$、$[\mathrm{can}(c,b,q)]\Rightarrow^*s_2$。

以上で $[m]\Rightarrow^*s_1s_2=s$。$\square$

**注意（何が効いているか）.** 区分クラス $(a,b,p)$ の型は $\langle p,\mathtt l\rangle$ または $\langle p,\mathtt a\rangle$ で、内部の段の選択に依存しない。区分の右端は背骨の $\mathtt l$（または文末の $\mathtt a$）で、選択に依存しない。分割点 $c$ で露出するのは $\mathrm{first}(x_{c-1})$ の1文字だけで、これを成員2語で賄う。成員どうしは長さ $O(n)$ の共通の包み文脈 $E_{a,b}$ で Link される。区分クラスは木の節点ごとに一つで、親ごとに複製されない（$\mathcal B$ の非終端は観測された語そのものなので、親の成員の因子 $\mathrm{can}(c,b,q)$ は、子の包み文の中の同じ語と同じ非終端である）。Astra 第5回 §4 と第6回 ChatGPT 報告 §3 の設計は、段ごとに長さ $\Theta(i^2)$ の背骨の断片を別々に観測していた（各段で $\Theta(i^2)$、合計 $\Theta(n^3)$）。本構成では段 $i$ を含む区分語は高々 $4(h+1)$ 個しかない。

### 2.5 定理

**定理2.4.** $n\ge2$、$\Sigma=\{\mathtt a,\mathtt c,\mathtt l,\mathtt r\}$、$s=s_{1,1}$、ファンアウト1、ランク2。$K_n=K^{\mathrm{int}}_n\cup K^{\mathrm{seg}}_n$ は $\mathcal B^{\le2}_{1,s}$ と $\mathcal B_{1,s}$ のそれぞれについて $F_n$ の特徴標本である。また
$$
\|K^{\mathrm{seg}}_n\|_+\le4n^2(\lceil\log_2n\rceil+1)+4n(\lceil\log_2n\rceil+1)+88n^2 .
$$
したがって
$$
n^2+7n+4\ \le\ \mathrm{cs}_{\mathcal B_{1,s_{1,1}}}(F_n)=\mathrm{cs}_{\mathcal B^{\le2}_{1,s_{1,1}}}(F_n)\ \le\ 4n^2\log_2n+O(n^2)
=O(\|G_n\|\bar\theta_{G_n}\log\|G_n\|).
$$
（左辺の稀な型の下界は README (26)。両作用素の値の一致はファンアウト1でのランク2化（README (19)(a)）による。）

*証明.* $K_n\subseteq K\subseteq F_n$ とする。末尾 $\mathtt r$ の語は補題2.2(i)。末尾 $\mathtt a$ の語 $w$ は補題2.1(b) で $w=\mathtt l s$、$s\in\mathrm{seg}(n,0)$、$p:=\mathrm{first}(s)\in P(n-1)$。$m:=\mathrm{can}(n,0,p)$ とすると $\mathtt lm\in K$ なので Start $\widehat S\to[\mathtt lm]$、単項の合成 $[\mathtt lm]\to\mathtt l[m]$（型板 $\mathtt l\xi$）、補題2.3で $[m]\Rightarrow^*s$。よって $F_n\subseteq L(\mathcal B^{\le2}_{1,s}(K))$。§1 の健全性と単調性で両作用素について特徴標本。

*長さ.* $(a,b)\in T_n$ の語 $E_{a,b}[m]$ を数える。$m$ の段 $i$ の部分は $D_i^{p_i}\mathtt l$（$b=0$ の最下段は $\mathtt{aa}$）。$|C_i\mathtt l|=2i+2$、$|D^{\mathtt l}_i\mathtt l|=4i$ で、$D^{\mathtt l}$ を使う段は高々2つ（段 $a-1$ と $c-1$）。よって $|m|\le\sum_{i=b}^{a-1}(2i+2)+4n=(a^2-b^2)+(a-b)+4n$。包みは $2(n-a)+1+|Q_b|\le6n$ 文字を足す。1節点あたり語は高々4個（$p$ が2通り、成員が2個）。したがって
$$
\|K^{\mathrm{seg}}_n\|_+\le4\sum_{(a,b)\in T_n}\bigl[(a^2-b^2)+(a-b)+11n\bigr].
$$
同じ深さの区間は互いに素なので、各深さで $\sum(a^2-b^2)\le n^2$、$\sum(a-b)\le n$。深さは $h+1\le\lceil\log_2n\rceil+1$ 通り、節点数は $2n-1$。これで主張の評価を得る。$\|K^{\mathrm{int}}_n\|_+=O(n^2)$（Astra §2.4）。$\square$

**系2.5（Q1 への答え）.** $s_{1,1}$、ファンアウト1、ランク2、アルファベット4文字で、$\mathcal B_{1,s}$ と $\mathcal B^{\le2}_{1,s}$ について $\mathrm{cs}(F_n)\ne\Omega(n^3)$。したがって $F_n$ からは「定理A(i) の上界 $O(\|G\|^2\bar\theta_G)$ が $\mathcal B$ について鋭い」という結論は出ない。$F_n$ が示すのは高々 $\|G\|\bar\theta_G$ と $\|G\|\bar\theta_G\log\|G\|$ の間の差である。

### 2.6 この構成法の限界（$\log n$ はこの方法では除けない）

区分クラスの方法を、「葉が段 $0,\dots,n-1$ の順に並ぶ任意の二分木 $T$ と、各内部節点 $(a,b)$ で分割点 $c$ を露出させ、成員を区分 $\mathrm{seg}(a,b)$ の語として観測する方法」と定める。成員の長さは $\sum_{i=b}^{a-1}(|x_i|+1)\ge\sum_{i=b}^{a-1}(2i+1)=a^2-b^2$ 以上なので、
$$
\sum_{(a,b)\text{ 内部}}(a^2-b^2)=\sum_{i=0}^{n-1}(2i+1)\,d_T(i),
$$
$d_T(i)$ は段 $i$ の葉の深さ。Kraft の不等式 $\sum_i2^{-d_T(i)}\le1$ と Gibbs の不等式から、重み $w_i=2i+1$（$W=\sum w_i=n^2$）について $\sum_iw_id_T(i)\ge W\cdot H(w/W)$。$w_i/W\le2/n$ なので $H\ge\log_2(n/2)$。よって **この方法は木の選び方によらず $\ge n^2(\log_2n-1)$ を要する**。これは構成法の限界であって、$\mathcal B$ の下界ではない。$O(n^2)$ にするには、区分クラスを使わない別の共有か、内部標本 $K^{\mathrm{int}}_n$ の文脈を背骨の乗り換えに流用する仕組みが要る（§5 の観察8 がその可能性を示唆する）。

## 3. 下界の側で分かったこと

### 3.1 「各段の $\mathtt a$ 終わりの左の子」は不要（$s_{1,1}$ でも）

README (17) の Claude の注は「各段 $j$ について、左の子が $\mathtt a$ で終わる $\mathtt l$ 節点が標本の構文木に現れる」なら総長 $\Omega(n^3)$ と述べ、第2回 ChatGPT 報告 §5（README (19)(e)）がその重み不等式を証明した。$s_{0,1}$ ではこの条件が不要であることを第2回報告が示した（$\mathtt{carc}\to\mathtt{laac}$ の Link）。$s_{1,1}$ ではこの Link は型 $\langle\mathtt c,\mathtt c\rangle\ne\langle\mathtt l,\mathtt c\rangle$ のため使えないので、条件が $s_{1,1}$ では必要になる可能性が残っていた。

**命題3.1.** $s_{1,1}$、$\mathcal B^{\le2}_{1,s}$ で、$F_n$ の末尾 $\mathtt r$ の語（左の子が $\mathtt a$ で終わる $\mathtt l$ 節点を段 $2,\dots,n$ のどこにでも持つ語を含む）は、すべて $K^{\mathrm{int}}_n$ から生成される。一方、$K^{\mathrm{int}}_n$ の語の長さは $O(n)$ なので、段 $j+1$ の $\mathtt l$ 節点で左の子が $\mathtt a$ で終わるものを含む語は、$A_j+1=j^2+j+2$ が最大語長を超える $j=\Omega(\sqrt n)$ 以上の段では $K^{\mathrm{int}}_n$ に存在しない。

*証明.* 前半は補題2.2(i)。後半：$L_j$ の末尾 $\mathtt a$ の語の最短長は $A_j=j^2+j+1$（README (17)、(21)）。$K^{\mathrm{int}}_n$ の語は $e_Y[h_Y]$ または $e_Y[z_\rho]$ で、文脈・代表・規則の右辺がいずれも長さ $O(n)$（Astra §2.1–2.2 の表）。$\square$

さらに §2 の特徴標本 $K_n=K^{\mathrm{int}}_n\cup K^{\mathrm{seg}}_n$ 全体でも同じである。$K^{\mathrm{seg}}_n$ の語の $\mathtt l$ 節点の左の子は $D^p_i$（$i\ge2$ では末尾 $\mathtt r$）、$C_{b-1}$、$\mathtt a$ のいずれかで、段1以上で $\mathtt a$ で終わる左の子は $D^{\mathtt l}_1=\mathtt{laa}$（段2の節点の左の子）だけだからである。よって、**左の子が $\mathtt a$ で終わる節点を段 $O(\sqrt n)$ までにしか持たない特徴標本が存在する**。$s_{1,1}$ での超二次の下界は、左の子の側（文の内部）からは出ない。重みが生じるのは**文末の背骨**だけであり、その背骨も §2 で $O(n^2\log n)$ に抑えられる。$n=4,5,8,12$ で $K_n$ に現れる該当の段は $\{2,3\}$ だけだった（§5、観察）。

### 3.2 型板の切れ目での合同（今後の下界のための道具）

**補題3.2.** $f=1$、型付け $s$ は任意、$L$ は $(1,s)$-代入可能、$K\subseteq L$ 有限、$r_{\max}\ge1$。$\widehat G_{\le r_{\max}}(K)$ の導出で、Comp $[z]\to\alpha_0[u_1]\alpha_1\cdots[u_r]\alpha_r$ を使い $[u_j]\Rightarrow^*y_j$ とし、$y=\alpha_0y_1\alpha_1\cdots y_r\alpha_r$ とする。型板の記号列（端末の各文字と各変数）のどこか一か所で切り、$z=z'z''$、$y=y'y''$ とそれに対応して分けると、$z',z''$ が空でなければ $z'\equiv_{L,s}y'$、$z''\equiv_{L,s}y''$。特に $s=s_{1,1}$ なら、切れ目の両隣の文字は $z$ と $y$ で一致する。

*証明.* `prop:reconstruction-soundness` より $u_j\equiv_{L,s}y_j$。切れ目の左右は、それぞれ元の型板の連続部分を型板とする合成であり、その型板は good（変数の順序と非空性はそのまま）。`lem:witnessed-composition` を左右それぞれに適用する。$\square$

**系3.3.** $K$ の同じ型の文はすべて空文脈 $\blank$ で互いに Link される。したがって根のクラスでの乗り換えは自由であり、背骨の乗り換えに費用がかかるのは根より下の節点である。

補題3.2 は「どの切れ目もどこかの段の情報を露出させる」ことを形式化する道具になる。§2 の構成は、露出を区分クラスの分割点に集め、各分割点の費用を区分の長さ $a^2-b^2$ に抑えている。$\Omega(n^2\log n)$ を示すには、任意の導出について「段 $i$ の情報の露出は、段 $i$ を含む長い観測語の中で起きる」ことを、§2.6 の Kraft の議論に乗る形で示す必要がある。区分以外の分け方（区分の内部で切る、内部標本の Link を背骨に流用するなど）を排除する方法は、まだ持っていない。

## 4. 未解決の問いと次の手

### 4.1 Q1 の残り：$\Theta(n^2)$ か $\Theta(n^2\log n)$ か

- **下界側.** 現在の最良は稀な型の $n^2+7n+4$。$n^2\log n$ を示すには、§3.2 の露出と、背骨の区間を含む観測語の長さ（文末の背骨の部分は $L$ の末尾 $\mathtt a$ の語で終わるので長い。README (17) の $A_j$）を組み合わせ、各段の露出に「その段を含む観測語の長さ」を課金する。課金の重複は Kraft の不等式で抑える、という形が自然に見える。ただし、区分の途中で切る導出や、文の内部の Link（$K^{\mathrm{int}}_n$ 型）を背骨に流用する導出があり、まだ排除できていない。
- **上界側.** §5 の観察8（$K^{\mathrm{int}}_n$ に足す末尾 $\mathtt a$ の語は $n=4$ で2語、$n=5$ で3語）は、$K^{\mathrm{int}}_n$ の $Z$ 記号（末尾 $\mathtt r$ の右の背骨の連鎖）の文脈が、末尾 $\mathtt a$ の背骨の乗り換えの一部を肩代わりしていることを示す。足す語の数が $O(1)$ で済むなら $O(n^2)$ になる。限られた候補の中では $n=4\to5$ で増えているが、候補を広げれば減る可能性があり、$O(1)$ で済むかどうかは分からない。足す語の数が $\Theta(\log n)$ で増えるなら $\Theta(n^2\log n)$ と整合する。

### 4.2 Q2（一般の上界の改良）について

本報告では一般定理は示していない。§2 の方法を一般化するには、(i) Astra の「ずらした断片」で文の内部の型を文脈の性質にする、(ii) 長い型（文末に達する部分）の証明書を、背骨の区間の二分木に沿った区分クラスに分け、各クラスに短い共通文脈を用意する、の2点が要る。(ii) が一般の $G$ でできれば、窓の型付け・ファンアウト1で $\Lambda=O(\|G\|\bar\theta_G\log\|G\|)$ が見込めるが、背骨が一本の鎖にならない文法、短い共通文脈が存在しない文法があり、未確認である。

### 4.3 原稿への影響（提案）

§9「Tightness of the exponents」に、$F_n$ と $s_{1,1}$ について $n^2+7n+4\le\mathrm{cs}\le O(n^2\log n)$ を記録し、この族からは $\|G\|$ 一つ分の差が閉じないことを書ける。定理A(i) の上界の鋭さを示す族は、まだ知られていない。

## 5. 計算（観察）

スクリプトは §7 に全文を載せる（標準ライブラリのみ、`py -3 claude_gap_window_check.py`）。メンバーシップの判定は第6回 ChatGPT 報告の正規化（補題2.1・2.2：単項の端末の隙間つき Comp と隙間なしの二項 Comp、Link の連結成分）をそのまま使い、部分語ごとのメモ化だけを加えた。$K^{\mathrm{int}}_n$ は Astra 第5回 §2 の表と規則 (4)–(6) から生成した。

出力（Linux、Python 3）：

```
(1) exhaustive check of K_n = K_int | K_seg
  n=2 |F_n|=6 |K|=6 ||K||+=44 (K_seg 22) missing=0
  n=3 |F_n|=42 |K|=26 ||K||+=344 (K_seg 118) missing=0
  n=4 |F_n|=1806 |K|=54 ||K||+=1072 (K_seg 308) missing=0
(2) n=5, sampled words
  ||K||+=2092; tested 128 structured + 3000 random a-ending + 1499 random r-ending; missing=0 (71s)
(3) Astra (8) with b=l: [D_i^p l] =>* w l for all w in L_i with first letter p
  n=3 cases=8 failures=0
  n=4 cases=50 failures=0
  n=5 cases=1856 failures=0
(4) levels j+1 of l-nodes with a-ending left child, in words of K_n = K_int | K_seg
  n=4 levels=[2, 3] max|w| in K_int=27
  n=5 levels=[2, 3] max|w| in K_int=41
  n=8 levels=[2, 3] max|w| in K_int=83
  n=12 levels=[2, 3] max|w| in K_int=139
(5) lengths
  n=2 ||K_seg||+=22  /(n^2 log2 n)=5.50  bound=400 ok=True  ||K_int||+=44
  n=3 ||K_seg||+=118  /(n^2 log2 n)=8.27  bound=936 ok=True  ||K_int||+=284
  n=4 ||K_seg||+=308  /(n^2 log2 n)=9.62  bound=1648 ok=True  ||K_int||+=876
  n=8 ||K_seg||+=1864  /(n^2 log2 n)=9.71  bound=6784 ok=True  ||K_int||+=5884
  n=16 ||K_seg||+=9368  /(n^2 log2 n)=9.15  bound=27968 ok=True  ||K_int||+=28572
  n=32 ||K_seg||+=43600  /(n^2 log2 n)=8.52  bound=115456 ok=True  ||K_int||+=124636
  n=64 ||K_seg||+=195320  /(n^2 log2 n)=7.95  bound=476928 ok=True  ||K_int||+=519516
  n=128 ||K_seg||+=856768  /(n^2 log2 n)=7.47  bound=1970176 ok=True  ||K_int||+=2120284
  n=256 ||K_seg||+=3710792  /(n^2 log2 n)=7.08  bound=8135680 ok=True  ||K_int||+=-
  n=512 ||K_seg||+=15938128  /(n^2 log2 n)=6.76  bound=33574912 ok=True  ||K_int||+=-
```

読み取り：
1. $n=2,3,4$ で $K_n\subseteq F_n$、$F_n$ の全語（6、42、1806語）を生成。定理2.4の観察による確認。
2. $n=5$ で、各段の語を $\{C_j,D^{\mathtt l}_j,U_j,\mathtt lU_{j-1}C_{j-1}\}$ から選んだ末尾 $\mathtt a$ の128語、無作為な末尾 $\mathtt a$ の3,000語、無作為な末尾 $\mathtt r$ の語をすべて生成。$n\ge6$ はこの環境のメモリ（8GB）で単純な区間DPが動かず、検査していない。
3. Astra (8)（$b=\mathtt l$）は $n\le5$ の全事例で成立。
4. 特徴標本 $K_n$ に現れる「左の子が $\mathtt a$ で終わる $\mathtt l$ 節点」の段は $\{2,3\}$ だけ（$n=4,5,8,12$）。それでも $F_n$ の全語が生成される（命題3.1）。$K^{\mathrm{int}}_n$ の最長の語は $14n-29$（$n=4,5,8,12$）で、線形である。
5. $\|K^{\mathrm{seg}}_n\|_+/(n^2\log_2n)$ は $n=256$ で約7.1、$n=512$ で約6.8 と下がり続け、定理2.4の評価の範囲に入る。$\|K^{\mathrm{int}}_n\|_+/n^2$ は $n=128$ で約129（定数は大きいが二次）。小さい $n$ では $K_n$ は既知の標本より長い（$n=3$ で344、既知の上界は144）。

**観察8（別途実行）.** $K^{\mathrm{int}}_4$ に、各段の語を $\{C_j,D^{\mathtt l}_j,U_j\}$ から選んだ末尾 $\mathtt a$ の18語のうち2語を足すと、504語ある末尾 $\mathtt a$ の語をすべて生成する組が36組あった（例：$U_4$ と $\mathtt lC_3\,\mathtt lU_2\,\mathtt lC_1\,\mathtt{laa}$、計46点）。1語では足りない。$n=5$ では、各段の語を $\{C_j,U_j\}$ から選んだ16語について、検査語（構造的な81語と無作為な300語）を全部生成する組は、1語では0組、2語でも120組中0組で、3語では成功する組が見つかった（例：$\mathtt lC_4\,\mathtt lC_3\,\mathtt lC_2\,\mathtt lC_1\,\mathtt{laa}$、$\mathtt lC_4\,\mathtt lC_3\,\mathtt lC_2\,\mathtt lU_1\,\mathtt{laa}$、$\mathtt lC_4\,\mathtt lU_3\,\mathtt lC_2\,\mathtt lC_1\,\mathtt{laa}$。3語の全560組の検査は時間制限で途中終了）。$n=3$ の2語（第6回 ChatGPT 報告、末尾 $\mathtt r$ の全語を補助にした場合）、$n=4$ の2語、$n=5$ の3語という増え方は、$\log n$ 程度の増加（§2 の木の深さ）とも線形の増加（三次）とも矛盾しない。小さい $n$ からは判断できない。

## 6. 文献

区間の二分木で重み付きの道の長さを最小化する問題と、その下界 $W\cdot H$ は古典的である（Kraft–McMillan の不等式、Hu–Tucker のアルファベット順の木）。それを特徴標本の長さの構成に使った例が既知かどうかは**未確認**。定理2.4そのもの（$F_n$、$s_{1,1}$、$\mathcal B$ について $O(n^2\log n)$）が文献にあるかどうかも**未確認**（これまでの報告と README の文献調査 `literature_check_2026-11-01.md` には見当たらない）。

## 7. スクリプト全文

`claude_gap_window_check.py`：

```python
# claude_gap_window_check.py  (Claude, 2026-11-02)
# F_n (E_0 -> a, E_i -> l E_{i-1} E_{i-1} | c E_{i-1} r), typing s_{1,1}, operator B^{<=2}_{1,s}.
# Checks (observations, not proofs) for the sample K_n = K_int(n) | K_seg(n) of the report:
#   (1) K_n is a subset of F_n and generates all of F_n (n = 2,3,4 exhaustive);
#   (2) n = 5: structured + random words;
#   (3) Astra's interior lemma (8) with b = l:  [D_i^p l] =>* w l  (n <= 5, all w);
#   (4) a-ending left-child levels present in K_n (n = 4,5,8,12);
#   (5) ||K_seg||_+ and the bound 4 n^2 (ceil(log2 n)+1) + 4 n (ceil(log2 n)+1) + 88 n^2.
# Standard library only.  Windows:  py -3 claude_gap_window_check.py
import sys, math, random, itertools, time
from collections import defaultdict
sys.setrecursionlimit(20000)

# ---------- the language and named words ----------
def language(n):
    ws = ['a']
    for _ in range(n):
        ws = ['c' + u + 'r' for u in ws] + ['l' + u + v for u in ws for v in ws]
    return ws

def typ(x):                      # s_{1,1}: short words (length 1) keep their own tag
    return ('s', x) if len(x) == 1 else ('p', x[0], x[-1])

def cost(K):                     # ||K||_+
    return sum(len(w) + 1 for w in K)

def C(i): return 'c' * i + 'a' + 'r' * i
def D(i, p):
    if i == 0: return 'a'
    return C(i) if p == 'c' else 'l' + C(i - 1) + C(i - 1)
def U(i): return 'a' if i == 0 else 'l' + C(i - 1) + U(i - 1)
def P(i): return ['a'] if i == 0 else ['c', 'l']

# ---------- exact membership for B^{<=2}_{1,s11}(K) ----------
# Comp normalized to unary rules with terminal gaps and gapless binary rules
# (ChatGPT round 6, Lemma 2.1); Link classes are union-find components (Lemma 2.2).
class Grammar:
    def __init__(self, sample):
        self.sample = sorted(set(sample))
        fac = sorted({w[i:j] for w in self.sample for i in range(len(w))
                      for j in range(i + 1, len(w) + 1)}, key=lambda x: (len(x), x))
        ids = {s: k for k, s in enumerate(fac)}
        par = list(range(len(fac)))
        def root(x):
            while par[x] != x:
                par[x] = par[par[x]]; x = par[x]
            return x
        ctx = defaultdict(list)
        for w in self.sample:
            for i in range(len(w)):
                for j in range(i + 1, len(w) + 1):
                    x = w[i:j]
                    ctx[(w[:i], w[j:], typ(x))].append(ids[x])
        for b in ctx.values():
            for y in b[1:]:
                ra, rb = root(b[0]), root(y)
                if ra != rb: par[rb] = ra
        self.state = {x: root(ids[x]) for x in fac}
        self.start = frozenset(self.state[w] for w in self.sample)
        un = defaultdict(lambda: defaultdict(set)); bi = defaultdict(set)
        for z in fac:
            sz = self.state[z]; L = len(z)
            for i in range(L):
                for j in range(i + 1, L + 1):
                    if i == 0 and j == L: continue
                    un[(z[:i], z[j:])][self.state[z[i:j]]].add(sz)
            for i in range(1, L):
                bi[(self.state[z[:i]], self.state[z[i:]])].add(sz)
        self.un = {k: {s: frozenset(v) for s, v in d.items()} for k, d in un.items()}
        self.bi = {k: frozenset(v) for k, v in bi.items()}
        self.memo = {}
    def states(self, x):         # set of Link classes deriving x
        m = self.memo.get(x)
        if m is not None: return m
        S = set()
        if x in self.state: S.add(self.state[x])
        N = len(x)
        for k in range(1, N):
            A = self.states(x[:k])
            if not A: continue
            B = self.states(x[k:])
            if not B: continue
            for a in A:
                for b in B:
                    r = self.bi.get((a, b))
                    if r: S |= r
        for la in range(N):
            a = x[:la]
            for lb in range(N - la):
                if la == 0 and lb == 0: continue
                rule = self.un.get((a, x[N - lb:] if lb else ''))
                if rule is None: continue
                for s in self.states(x[la:N - lb]):
                    r = rule.get(s)
                    if r: S |= r
        S = frozenset(S); self.memo[x] = S
        return S
    def derives(self, w):
        return bool(self.states(w) & self.start)

# ---------- K_int(n): Astra round 5, Section 2.4 ----------
def K_int(n):
    assert n >= 2
    def Pc(i, b):
        if b == 'r': return ('c' * (n - i), 'r' * (n - i - 1))
        if i >= 1: return ('c' * (n - i - 1) + 'l', D(i, b)[1:] + 'r' * (n - i - 1))
        if b == 'a': return ('c' * (n - 1) + 'l', 'r' * (n - 1))
        return ('c' * (n - 2) + 'lla', D(1, b)[1:] + 'r' * (n - 2))
    I = [(0, b) for b in 'aclr'] + [(i, b) for i in range(1, n) for b in 'clr']
    sym = {}
    for (i, b) in I:
        for p in P(i):
            sym[('X', i, p, b)] = (D(i, p) + b, Pc(i, b))
        if i == 0:
            sym[('T', 0, 'a', b, None)] = (b, (Pc(0, b)[0] + 'a', Pc(0, b)[1]))
        else:
            for q in P(i - 1):
                sym[('T', i, 'c', b, q)] = (D(i - 1, q) + 'r' + b, (Pc(i, b)[0] + 'c', Pc(i, b)[1]))
                sym[('T', i, 'l', b, q)] = (D(i - 1, q) + C(i - 1) + b, (Pc(i, b)[0] + 'l', Pc(i, b)[1]))
    for i in range(1, n + 1):
        for q in P(i - 1):
            sym[('Z', i, 'c', q)] = (D(i - 1, q) + 'r', ('c' * (n - i) + 'c', 'r' * (n - i)))
            if i >= 2:
                sym[('Z', i, 'l', q)] = (D(i - 1, q) + C(i - 1), ('c' * (n - i) + 'l', 'r' * (n - i)))
    for p in 'cl':
        sym[('R', p)] = (D(n, p), ('', ''))
    K = set()
    def put(name, z):
        h, (pp, qq) = sym[name]
        K.add(pp + h + qq); K.add(pp + z + qq)
    for name, (h, _) in sym.items():
        put(name, h)
    for (i, b) in I:
        if i >= 1:
            for p in P(i):
                for q in P(i - 1):
                    put(('X', i, p, b), p + sym[('T', i, p, b, q)][0])
            for q in P(i - 1):
                for t in P(i - 1):
                    if i - 1 == 0:
                        put(('T', i, 'l', b, q), sym[('X', 0, 'a', 'a')][0] + sym[('T', 0, 'a', b, None)][0])
                    elif (i - 1, t) in I:
                        for v in P(i - 2):
                            put(('T', i, 'l', b, q), D(i - 1, q) + t + sym[('T', i - 1, t, b, v)][0])
    for i in range(2, n + 1):
        for q in P(i - 1):
            for t in (['c'] if i == 2 else ['c', 'l']):
                for v in P(i - 2):
                    if ('Z', i - 1, t, v) in sym:
                        put(('Z', i, 'l', q), D(i - 1, q) + t + sym[('Z', i - 1, t, v)][0])
    for p in 'cl':
        for q in P(n - 1):
            if ('Z', n, p, q) in sym:
                put(('R', p), p + sym[('Z', n, p, q)][0])
    return K

# ---------- K_seg(n): the hierarchical segment sample of the report ----------
def split(a, b): return (a + b + 1) // 2

def tree(n):
    out, st = [], [(n, 0)]
    while st:
        a, b = st.pop(); out.append((a, b))
        if a - b >= 2:
            c = split(a, b); st += [(a, c), (c, b)]
    return out

_can = {}
def can(a, b, p):
    key = (a, b, p)
    if key not in _can:
        if a - b == 1:
            _can[key] = 'aa' if b == 0 else D(a - 1, p) + 'l'
        else:
            c = split(a, b); _can[key] = can(a, c, p) + can(c, b, P(c - 1)[0])
    return _can[key]

def members(a, b, p):
    if a - b == 1: return [can(a, b, p)]
    c = split(a, b)
    return [can(a, c, p) + can(c, b, q) for q in P(c - 1)]

def wrap(n, a, b, s):
    return 'c' * (n - a) + 'l' + s + (C(b - 1) * 2 if b >= 1 else '') + 'r' * (n - a)

def K_seg(n):
    return {wrap(n, a, b, m) for (a, b) in tree(n) for p in P(a - 1) for m in members(a, b, p)}

# ---------- helpers for the checks ----------
def parse(w, k, p=0):
    ch = w[p]
    if k == 0:
        assert ch == 'a'; return p + 1, ('a', 0, p, p + 1, [])
    if ch == 'c':
        q, s = parse(w, k - 1, p + 1); assert w[q] == 'r'
        return q + 1, ('c', k, p, q + 1, [s])
    assert ch == 'l'
    q, s1 = parse(w, k - 1, p + 1); r, s2 = parse(w, k - 1, q)
    return r, ('l', k, p, r, [s1, s2])

def a_left_levels(w, n):         # levels of l-nodes whose left child (level >= 1) ends in a
    end, rt = parse(w, n); assert end == len(w)
    out, st = set(), [rt]
    while st:
        nd = st.pop()
        if nd[0] == 'l' and nd[1] >= 2 and w[nd[4][0][3] - 1] == 'a': out.add(nd[1])
        st.extend(nd[4])
    return out

def rand_word(i, pa=0.5):
    if i == 0: return 'a'
    if random.random() < pa: return 'c' + rand_word(i - 1, pa) + 'r'
    return 'l' + rand_word(i - 1, min(0.9, pa + 0.15)) + rand_word(i - 1, min(0.9, pa + 0.15))

def a_word(xs): return ''.join('l' + x for x in xs) + 'laa'

if __name__ == '__main__':
    random.seed(2026)
    print('(1) exhaustive check of K_n = K_int | K_seg')
    for n in (2, 3, 4):
        L = language(n); K = K_int(n) | K_seg(n)
        assert K <= set(L)
        g = Grammar(K); miss = [w for w in L if not g.derives(w)]
        print('  n=%d |F_n|=%d |K|=%d ||K||+=%d (K_seg %d) missing=%d'
              % (n, len(L), len(K), cost(K), cost(K_seg(n)), len(miss)), flush=True)
    print('(2) n=5, sampled words')
    n = 5; K = K_int(n) | K_seg(n); g = Grammar(K); t = time.time()
    reps = {j: sorted({C(j), D(j, 'l'), U(j), 'l' + U(j - 1) + C(j - 1)}) for j in range(1, n)}
    S = [a_word(xs) for xs in itertools.product(*[reps[j] for j in range(n - 1, 0, -1)])]
    R = [a_word([rand_word(j) for j in range(n - 1, 0, -1)]) for _ in range(3000)]
    Rr = [w for w in (rand_word(n) for _ in range(1500)) if w.endswith('r')]
    assert all(parse(w, n)[0] == len(w) for w in S + R + Rr)
    miss = [w for w in S + R + Rr if not g.derives(w)]
    print('  ||K||+=%d; tested %d structured + %d random a-ending + %d random r-ending; missing=%d (%.0fs)'
          % (cost(K), len(S), len(R), len(Rr), len(miss), time.time() - t), flush=True)
    print("(3) Astra (8) with b=l: [D_i^p l] =>* w l for all w in L_i with first letter p")
    for n in (3, 4, 5):
        g = Grammar(K_int(n)); tot = bad = 0
        for i in range(1, n):
            for w in language(i):
                tot += 1
                if g.state[D(i, w[0]) + 'l'] not in g.states(w + 'l'): bad += 1
        print('  n=%d cases=%d failures=%d' % (n, tot, bad), flush=True)
    print('(4) levels j+1 of l-nodes with a-ending left child, in words of K_n = K_int | K_seg')
    for n in (4, 5, 8, 12):
        K = K_int(n) | K_seg(n)
        print('  n=%d levels=%s max|w| in K_int=%d' % (n, sorted(set().union(*[a_left_levels(w, n) for w in K])),
                                                     max(len(w) for w in K_int(n))), flush=True)
    print('(5) lengths')
    for n in (2, 3, 4, 8, 16, 32, 64, 128, 256, 512):
        s = cost(K_seg(n)); h = math.ceil(math.log2(n))
        bound = 4 * n * n * (h + 1) + 4 * n * (h + 1) + 88 * n * n
        print('  n=%d ||K_seg||+=%d  /(n^2 log2 n)=%.2f  bound=%d ok=%s  ||K_int||+=%s'
              % (n, s, s / (n * n * math.log2(n)), bound, s <= bound,
                 cost(K_int(n)) if n <= 128 else '-'), flush=True)
```

観察8のスクリプト（同じフォルダに上のファイルを置いて実行。引数は $n$ と足す語数の上限。`py -3 exp_int_spines.py 4 2`）：

```python
SPINE# claude_gap_window_check.py  (Claude, 2026-11-02)
# F_n (E_0 -> a, E_i -> l E_{i-1} E_{i-1} | c E_{i-1} r), typing s_{1,1}, operator B^{<=2}_{1,s}.
# Checks (observations, not proofs) for the sample K_n = K_int(n) | K_seg(n) of the report:
#   (1) K_n is a subset of F_n and generates all of F_n (n = 2,3,4 exhaustive);
#   (2) n = 5: structured + random words;
#   (3) Astra's interior lemma (8) with b = l:  [D_i^p l] =>* w l  (n <= 5, all w);
#   (4) a-ending left-child levels present in K_n (n = 4,5,8,12);
#   (5) ||K_seg||_+ and the bound 4 n^2 (ceil(log2 n)+1) + 4 n (ceil(log2 n)+1) + 88 n^2.
# Standard library only.  Windows:  py -3 claude_gap_window_check.py
import sys, math, random, itertools, time
from collections import defaultdict
sys.setrecursionlimit(20000)

# ---------- the language and named words ----------
def language(n):
    ws = ['a']
    for _ in range(n):
        ws = ['c' + u + 'r' for u in ws] + ['l' + u + v for u in ws for v in ws]
    return ws

def typ(x):                      # s_{1,1}: short words (length 1) keep their own tag
    return ('s', x) if len(x) == 1 else ('p', x[0], x[-1])

def cost(K):                     # ||K||_+
    return sum(len(w) + 1 for w in K)

def C(i): return 'c' * i + 'a' + 'r' * i
def D(i, p):
    if i == 0: return 'a'
    return C(i) if p == 'c' else 'l' + C(i - 1) + C(i - 1)
def U(i): return 'a' if i == 0 else 'l' + C(i - 1) + U(i - 1)
def P(i): return ['a'] if i == 0 else ['c', 'l']

# ---------- exact membership for B^{<=2}_{1,s11}(K) ----------
# Comp normalized to unary rules with terminal gaps and gapless binary rules
# (ChatGPT round 6, Lemma 2.1); Link classes are union-find components (Lemma 2.2).
class Grammar:
    def __init__(self, sample):
        self.sample = sorted(set(sample))
        fac = sorted({w[i:j] for w in self.sample for i in range(len(w))
                      for j in range(i + 1, len(w) + 1)}, key=lambda x: (len(x), x))
        ids = {s: k for k, s in enumerate(fac)}
        par = list(range(len(fac)))
        def root(x):
            while par[x] != x:
                par[x] = par[par[x]]; x = par[x]
            return x
        ctx = defaultdict(list)
        for w in self.sample:
            for i in range(len(w)):
                for j in range(i + 1, len(w) + 1):
                    x = w[i:j]
                    ctx[(w[:i], w[j:], typ(x))].append(ids[x])
        for b in ctx.values():
            for y in b[1:]:
                ra, rb = root(b[0]), root(y)
                if ra != rb: par[rb] = ra
        self.state = {x: root(ids[x]) for x in fac}
        self.start = frozenset(self.state[w] for w in self.sample)
        un = defaultdict(lambda: defaultdict(set)); bi = defaultdict(set)
        for z in fac:
            sz = self.state[z]; L = len(z)
            for i in range(L):
                for j in range(i + 1, L + 1):
                    if i == 0 and j == L: continue
                    un[(z[:i], z[j:])][self.state[z[i:j]]].add(sz)
            for i in range(1, L):
                bi[(self.state[z[:i]], self.state[z[i:]])].add(sz)
        self.un = {k: {s: frozenset(v) for s, v in d.items()} for k, d in un.items()}
        self.bi = {k: frozenset(v) for k, v in bi.items()}
        self.memo = {}
    def states(self, x):         # set of Link classes deriving x
        m = self.memo.get(x)
        if m is not None: return m
        S = set()
        if x in self.state: S.add(self.state[x])
        N = len(x)
        for k in range(1, N):
            A = self.states(x[:k])
            if not A: continue
            B = self.states(x[k:])
            if not B: continue
            for a in A:
                for b in B:
                    r = self.bi.get((a, b))
                    if r: S |= r
        for la in range(N):
            a = x[:la]
            for lb in range(N - la):
                if la == 0 and lb == 0: continue
                rule = self.un.get((a, x[N - lb:] if lb else ''))
                if rule is None: continue
                for s in self.states(x[la:N - lb]):
                    r = rule.get(s)
                    if r: S |= r
        S = frozenset(S); self.memo[x] = S
        return S
    def derives(self, w):
        return bool(self.states(w) & self.start)

# ---------- K_int(n): Astra round 5, Section 2.4 ----------
def K_int(n):
    assert n >= 2
    def Pc(i, b):
        if b == 'r': return ('c' * (n - i), 'r' * (n - i - 1))
        if i >= 1: return ('c' * (n - i - 1) + 'l', D(i, b)[1:] + 'r' * (n - i - 1))
        if b == 'a': return ('c' * (n - 1) + 'l', 'r' * (n - 1))
        return ('c' * (n - 2) + 'lla', D(1, b)[1:] + 'r' * (n - 2))
    I = [(0, b) for b in 'aclr'] + [(i, b) for i in range(1, n) for b in 'clr']
    sym = {}
    for (i, b) in I:
        for p in P(i):
            sym[('X', i, p, b)] = (D(i, p) + b, Pc(i, b))
        if i == 0:
            sym[('T', 0, 'a', b, None)] = (b, (Pc(0, b)[0] + 'a', Pc(0, b)[1]))
        else:
            for q in P(i - 1):
                sym[('T', i, 'c', b, q)] = (D(i - 1, q) + 'r' + b, (Pc(i, b)[0] + 'c', Pc(i, b)[1]))
                sym[('T', i, 'l', b, q)] = (D(i - 1, q) + C(i - 1) + b, (Pc(i, b)[0] + 'l', Pc(i, b)[1]))
    for i in range(1, n + 1):
        for q in P(i - 1):
            sym[('Z', i, 'c', q)] = (D(i - 1, q) + 'r', ('c' * (n - i) + 'c', 'r' * (n - i)))
            if i >= 2:
                sym[('Z', i, 'l', q)] = (D(i - 1, q) + C(i - 1), ('c' * (n - i) + 'l', 'r' * (n - i)))
    for p in 'cl':
        sym[('R', p)] = (D(n, p), ('', ''))
    K = set()
    def put(name, z):
        h, (pp, qq) = sym[name]
        K.add(pp + h + qq); K.add(pp + z + qq)
    for name, (h, _) in sym.items():
        put(name, h)
    for (i, b) in I:
        if i >= 1:
            for p in P(i):
                for q in P(i - 1):
                    put(('X', i, p, b), p + sym[('T', i, p, b, q)][0])
            for q in P(i - 1):
                for t in P(i - 1):
                    if i - 1 == 0:
                        put(('T', i, 'l', b, q), sym[('X', 0, 'a', 'a')][0] + sym[('T', 0, 'a', b, None)][0])
                    elif (i - 1, t) in I:
                        for v in P(i - 2):
                            put(('T', i, 'l', b, q), D(i - 1, q) + t + sym[('T', i - 1, t, b, v)][0])
    for i in range(2, n + 1):
        for q in P(i - 1):
            for t in (['c'] if i == 2 else ['c', 'l']):
                for v in P(i - 2):
                    if ('Z', i - 1, t, v) in sym:
                        put(('Z', i, 'l', q), D(i - 1, q) + t + sym[('Z', i - 1, t, v)][0])
    for p in 'cl':
        for q in P(n - 1):
            if ('Z', n, p, q) in sym:
                put(('R', p), p + sym[('Z', n, p, q)][0])
    return K

# ---------- K_seg(n): the hierarchical segment sample of the report ----------
def split(a, b): return (a + b + 1) // 2

def tree(n):
    out, st = [], [(n, 0)]
    while st:
        a, b = st.pop(); out.append((a, b))
        if a - b >= 2:
            c = split(a, b); st += [(a, c), (c, b)]
    return out

_can = {}
def can(a, b, p):
    key = (a, b, p)
    if key not in _can:
        if a - b == 1:
            _can[key] = 'aa' if b == 0 else D(a - 1, p) + 'l'
        else:
            c = split(a, b); _can[key] = can(a, c, p) + can(c, b, P(c - 1)[0])
    return _can[key]

def members(a, b, p):
    if a - b == 1: return [can(a, b, p)]
    c = split(a, b)
    return [can(a, c, p) + can(c, b, q) for q in P(c - 1)]

def wrap(n, a, b, s):
    return 'c' * (n - a) + 'l' + s + (C(b - 1) * 2 if b >= 1 else '') + 'r' * (n - a)

def K_seg(n):
    return {wrap(n, a, b, m) for (a, b) in tree(n) for p in P(a - 1) for m in members(a, b, p)}

# ---------- helpers for the checks ----------
def parse(w, k, p=0):
    ch = w[p]
    if k == 0:
        assert ch == 'a'; return p + 1, ('a', 0, p, p + 1, [])
    if ch == 'c':
        q, s = parse(w, k - 1, p + 1); assert w[q] == 'r'
        return q + 1, ('c', k, p, q + 1, [s])
    assert ch == 'l'
    q, s1 = parse(w, k - 1, p + 1); r, s2 = parse(w, k - 1, q)
    return r, ('l', k, p, r, [s1, s2])

def a_left_levels(w, n):         # levels of l-nodes whose left child (level >= 1) ends in a
    end, rt = parse(w, n); assert end == len(w)
    out, st = set(), [rt]
    while st:
        nd = st.pop()
        if nd[0] == 'l' and nd[1] >= 2 and w[nd[4][0][3] - 1] == 'a': out.add(nd[1])
        st.extend(nd[4])
    return out

def rand_word(i, pa=0.5):
    if i == 0: return 'a'
    if random.random() < pa: return 'c' + rand_word(i - 1, pa) + 'r'
    return 'l' + rand_word(i - 1, min(0.9, pa + 0.15)) + rand_word(i - 1, min(0.9, pa + 0.15))

def a_word(xs): return ''.join('l' + x for x in xs) + 'laa'

if __name__ == '__main__':
    random.seed(2026)
    print('(1) exhaustive check of K_n = K_int | K_seg')
    for n in (2, 3, 4):
        L = language(n); K = K_int(n) | K_seg(n)
        assert K <= set(L)
        g = Grammar(K); miss = [w for w in L if not g.derives(w)]
        print('  n=%d |F_n|=%d |K|=%d ||K||+=%d (K_seg %d) missing=%d'
              % (n, len(L), len(K), cost(K), cost(K_seg(n)), len(miss)), flush=True)
    print('(2) n=5, sampled words')
    n = 5; K = K_int(n) | K_seg(n); g = Grammar(K); t = time.time()
    reps = {j: sorted({C(j), D(j, 'l'), U(j), 'l' + U(j - 1) + C(j - 1)}) for j in range(1, n)}
    S = [a_word(xs) for xs in itertools.product(*[reps[j] for j in range(n - 1, 0, -1)])]
    R = [a_word([rand_word(j) for j in range(n - 1, 0, -1)]) for _ in range(3000)]
    Rr = [w for w in (rand_word(n) for _ in range(1500)) if w.endswith('r')]
    assert all(parse(w, n)[0] == len(w) for w in S + R + Rr)
    miss = [w for w in S + R + Rr if not g.derives(w)]
    print('  ||K||+=%d; tested %d structured + %d random a-ending + %d random r-ending; missing=%d (%.0fs)'
          % (cost(K), len(S), len(R), len(Rr), len(miss), time.time() - t), flush=True)
    print("(3) Astra (8) with b=l: [D_i^p l] =>* w l for all w in L_i with first letter p")
    for n in (3, 4, 5):
        g = Grammar(K_int(n)); tot = bad = 0
        for i in range(1, n):
            for w in language(i):
                tot += 1
                if g.state[D(i, w[0]) + 'l'] not in g.states(w + 'l'): bad += 1
        print('  n=%d cases=%d failures=%d' % (n, tot, bad), flush=True)
    print('(4) levels j+1 of l-nodes with a-ending left child, in words of K_n = K_int | K_seg')
    for n in (4, 5, 8, 12):
        K = K_int(n) | K_seg(n)
        print('  n=%d levels=%s max|w| in K_int=%d' % (n, sorted(set().union(*[a_left_levels(w, n) for w in K])),
                                                     max(len(w) for w in K_int(n))), flush=True)
    print('(5) lengths')
    for n in (2, 3, 4, 8, 16, 32, 64, 128, 256, 512):
        s = cost(K_seg(n)); h = math.ceil(math.log2(n))
        bound = 4 * n * n * (h + 1) + 4 * n * (h + 1) + 88 * n * n
        print('  n=%d ||K_seg||+=%d  /(n^2 log2 n)=%.2f  bound=%d ok=%s  ||K_int||+=%s'
              % (n, s, s / (n * n * math.log2(n)), bound, s <= bound,
                 cost(K_int(n)) if n <= 128 else '-'), flush=True)
```
