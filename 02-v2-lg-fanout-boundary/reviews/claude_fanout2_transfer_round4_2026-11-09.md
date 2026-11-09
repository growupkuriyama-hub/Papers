# 探索報告（第4回）：冪の移送の一般化と容量の配置（`op:fanout-two`）

Claude, 2026-11-09。依頼文「探索依頼（第4回）」への報告である。記号は依頼文 §1・§2 に従う。型付けは断らない限り内容型付け $c=c_\Sigma$ とし、$\Psi$ を Parikh 写像とする。スクリプトは `check_claude_fanout2_transfer_round4_2026-11-09.py`（標準ライブラリのみ、約10秒、乱数の種 20261109）で、節番号 [2]〜[6] はスクリプトの出力の節を指す。

## 1. 要約（3行）

1. **移送補題 [証明済み].** 冪の移送は「周期的な因子をまたぐ移送」（補題 T1）に一般化できる。同じ語の中で文脈を共有する2-組の対は、共役のずらしで完全に記述できる（補題 T0）。ただし T0/T1 の移送は長さと Parikh ベクトルを保つ。したがって予想 T の「より短い語」は移送からは出ない（命題 N）。出るのは**一意性の破れ**で、ここから剛性補題 R が得られる。応用として、内容型付けでは倍増族は $n\ge3$ で $\mathcal C_{2,c}$ に入らない（原稿の閾値 $n\ge2|\mathsf S|+2=16$ を改善）。$n\le2$ では入る（網羅）。
2. **部分クラス [証明済み＋予想].** 定理 M の $\kappa$ は**ブロック数** $\beta$（外の文字の極大連の数）に置き換えられる（定理 M$_\beta$、ファンアウトによらない）。よって「外の文字が語ごとに $\le k$ 連」の部分クラス (c) は全ファンアウトで多項式になる。ただし倍増族はこのクラスに入らない（$\beta=3\cdot2^{n-2}$）。(a)(b) で $\kappa$ によらない上界は証明できなかった。代わりに「剛性のある標的」（希少な語が Parikh ベクトルごとに一意）ではファンアウト2で多項式になるという予想 R を立て、そのための構造補題 R・系 R1 を示した。予想 R はファンアウト1では偽である。
3. **候補と (Hyp) [観察＋証明済み].** 13族を試した。ファンアウト2に固有の崩れは、すべて同じ語の中での小周期（$\pi\in\{1,2\}$）の T1 移送だった。(Hyp) は**偽**である [証明済み]（$\{\mathtt a,\mathtt b\}^3\setminus\{\mathtt{aaa},\mathtt{bbb}\}$）。さらに $h(L)$ と最短の特徴標本の長さは一致しないことがある（8 対 12）。反復作用素 $\mathcal B^\infty$ の不動点は、調べた範囲ではつねにクラスに入った [観察]。

---

## 2. 課題1：移送補題

### 2.1 問い1a への答え

**命題 1a [証明済み].** $\eta_1,\eta_2$ が同じ導出木 $T$ の比較不能な節点で、ラベルが $A_1,A_2$、$W=o[x_{\eta_1},x_{\eta_2}]$ とする。

- (i) すべての $y_1\in\mathrm{In}(A_1)$、$y_2\in\mathrm{In}(A_2)$ について $o[y_1,y_2]\in L$ である。二つの部分木は交わらないので、(F1) を二回使えばよい。代入可能性もファンアウトも使わない。
- (ii) $L\in\mathcal C_{2,s}$ とする。成分ごとに $y_i\equiv^{(1)}_{L,s}x_i$（1-組として分布が等しい）なら、$\mathcal D^{(2)}(y_1,y_2)=\mathcal D^{(2)}(x_1,x_2)$ である。

*証明.* (ii) $E=v_0\square v_1\square v_2$ について $E[y_1,y_2]\in L$ とする。これは1-文脈 $(v_0,\ v_1y_2v_2)$ での $y_1$ の所属なので、$E[x_1,y_2]\in L$ と同値である。$v_1\ne\varepsilon$ だからこの1-文脈は許容される。同様に第2成分も置き換えられる。∎

**訂正.** 依頼文の「両方を同時に置き換えた語は、$o$ が文法上の文脈でない限り保証されない」について。二つの節点が同じ木にあれば、$o$ は二穴の文法上の文脈そのものであり、(i) で同時置換が保証される。

**帰結.** 2-代入可能性が新しく効くのは、成分が $\equiv^{(1)}$ で結ばれない2-組だけである。典型は次の二つ。

- 一つの節点の**枠** $(P,Q)$（第1回の補題 A）。
- 構成素ではない**断片**の組。冪の移送の $(u^i,u^{\delta+j})$ がこれに当たる。

以下の T0・T1 は後者を完全に扱う。

### 2.2 同じ語の中での共有：補題 T0

**補題 T0 [証明済み].** $w\in\Sigma^+$ と $E=(v_0,v_1,v_2)$（$v_1\ne\varepsilon$）について、相異なる2-組 $\mathbf x,\mathbf y$ が $E[\mathbf x]=E[\mathbf y]=w$ をみたすとする。$|y_1|>|x_1|$ と仮定し、$\pi:=|y_1|-|x_1|$ とおく。このとき、ある $t,s\in\Sigma^\pi$ が存在して次が成り立つ。
$$y_1=x_1t,\qquad x_2=sy_2,\qquad tv_1=v_1s.$$
したがって $r:=tv_1=v_1s$ は周期 $\pi$ をもち、$|r|>\pi$ であり、$w$ は因子 $x_1\,r\,y_2$ をもつ。逆に、このような因子 $x_1ry_2$（$r=tv=vs$、$v\ne\varepsilon$）があれば、2-組 $(x_1t,\ y_2)$ と $(x_1,\ sy_2)$ は文脈 $(\cdot,v,\cdot)$ を共有する。

*証明.* 長さを比べると $|\mathbf x|=|\mathbf y|$ である。$\pi=0$ なら $x_1=y_1$ となり、$v_0x_1v_1$ が共通の接頭辞なので $\mathbf x=\mathbf y$ となって仮定に反する。よって $\pi>0$。$v_0x_1v_1x_2v_2=v_0x_1t\,v_1y_2v_2$ から $y_1=x_1t$ と $v_1x_2=tv_1y_2$ が出る。長さから $x_2=sy_2$（$|s|=\pi$）と書け、$v_1s=tv_1$ となる。逆は代入すれば確かめられる。∎

Lyndon–Schützenberger の定理により、$tv=vs$ なら $t=pq$、$s=qp$、$v=(pq)^kp$ と書ける。とくに $t$ と $s$ は共役であり、$c(t)=c(s)$、$\Psi(t)=\Psi(s)$ である。[2]：ランダムな語で 13589 対を調べ、例外は 0 [観察]。

### 2.3 周期的な移送：補題 T1（冪の移送の一般化）

**補題 T1 [証明済み].** $f\ge2$、$L\in\mathcal C_{f,s}$（$s$ は任意の型付け）とする。$L$ のある語が因子 $x_1\,r\,x_2$ をもつと仮定する。ここで $x_1,x_2\in\Sigma^+$、$r=tv=vs$、$|t|=|s|=\pi\ge1$、$v\in\Sigma^+$ で、さらに
$$s(x_1t)=s(x_1),\qquad s(sx_2)=s(x_2)$$
とする（**吸収条件**。$s$ の文字が型付け写像の名前と重なるが、文脈で区別する）。このとき、すべての $w_{\mathrm L},w_{\mathrm R}\in\Sigma^*$、$w_{\mathrm M}\in\Sigma^+$ について
$$w_{\mathrm L}\,x_1t\,w_{\mathrm M}\,x_2\,w_{\mathrm R}\in L\iff w_{\mathrm L}\,x_1\,w_{\mathrm M}\,sx_2\,w_{\mathrm R}\in L .$$

*証明.* その語を $y\,x_1rx_2\,z$ と書く。2-組 $X=(x_1t,x_2)$ と $Y=(x_1,sx_2)$ は、吸収条件により成分ごとの型が等しい。許容文脈 $y\square v\square z$ について $E[X]=yx_1tvx_2z$、$E[Y]=yx_1vsx_2z$ で、どちらも同じ語に等しい。よって分布が等しい。これを文脈 $w_{\mathrm L}\square w_{\mathrm M}\square w_{\mathrm R}$ で試せばよい。∎

**注.**

- **内容型付けでは**、吸収条件は $c(t)\subseteq c(x_1)\cap c(x_2)$ と同値である（$c(s)=c(t)$ だから）。
- **`lem:power-transfer` は特殊な場合である。** $x_1=u^i$、$x_2=u^j$、$t=s=u^\delta$、$v=u$（$r=u^{\delta+1}$）とすればよい。吸収条件は最終周期性そのものである。
- **(T1 は保存的)** 移送の両辺は長さ・Parikh ベクトル・内容が等しい。

**補題 U（移送はいたるところにある）[証明済み].** $w=x_1mx_2$ で $x_1,x_2\ne\varepsilon$、$c(m)\subseteq c(x_1)\cap c(x_2)$、$|m|\ge|c(m)|+1$ なら、$w$ は $\pi\le|c(m)|$ の T1 の型の因子をもつ。

*証明.* $m$ の最初の $|c(m)|+1$ 文字の中に、同じ文字 $\sigma$ が位置 $i<j$（$j-i\le|c(m)|$）で二度現れる。$r:=m[i..j]=\sigma z\sigma$ は周期 $j-i$ をもつ。$x_1':=x_1m[..i)$、$x_2':=m(j..]x_2$ とおけば、内容の条件がみたされる。∎

したがって、長い $M$-語で両端の近くにすべての文字が現れるものは、短い周期の移送の起点を必ず多数もつ。

### 2.4 予想 T の結論について：命題 N

**補題 Short（補題 B(i) の $d\le f$ への一般化）[証明済み].** $L\in\mathcal C_{f,c}$、$W$ を内容 $M$ の最短語、$W=E[\mathbf x]$（$E\in\mathcal E_d$、$d\le f$）とする。$c(y_i)=c(x_i)$ が各 $i$ で成り立ち、$\mathcal D(\mathbf y)\cap\mathcal D(\mathbf x)\ne\emptyset$ なら、$|\mathbf y|\ge|\mathbf x|$ である。等号のとき $E[\mathbf y]$ も内容 $M$ の最短語である。

*証明.* 分布が等しいので $E[\mathbf y]\in L$。内容は $M$ で、長さは $|W|-|\mathbf x|+|\mathbf y|$。∎

**命題 N [証明済み].** T0 の共有、すなわち同じ語の中での共有から得られる移送（T1）は、長さと Parikh ベクトルを保つ。また補題 Short により、$W$ の組の出現は、それより短く同じ内容の組と文脈を共有しない。したがって予想 T の前半「より短い語」を導くには、$W$ 以外の語 $W_1\in L$ を経由して、長さの異なる組の共有を作る必要がある。T0/T1 だけでは不可能である。

T1 から実際に出るのは予想 T の後半「同じ長さの別の語」であり、その強い形が次の剛性補題である。

### 2.5 剛性補題と倍増族

**補題 R（剛性）[証明済み].** $L\in\mathcal C_{2,c}$、$W\in L$ とし、$W$ は Parikh ベクトルが $\Psi(W)$ の $L$ の唯一の語だとする。内容 $M$ の最短語が一意なら、これはみたされる（同じ Parikh ベクトルの語は同じ内容・同じ長さをもつ）。$(x_1,r=tv=vs,x_2)$ を $L$ の語の中の T1 の型の因子で、$c(t)\subseteq c(x_1)\cap c(x_2)$ をみたすものとする。このとき、$W$ の分解 $W=w_{\mathrm L}x_1t\,w_{\mathrm M}\,x_2w_{\mathrm R}$（$w_{\mathrm M}\ne\varepsilon$）はすべて $tw_{\mathrm M}=w_{\mathrm M}s$ をみたす。すなわち $t=pq$、$s=qp$、$w_{\mathrm M}\in(pq)^*p$ で、$x_1$ の出現の直後から $x_2$ の出現まで、$W$ は周期 $\pi$ をもつ。$W=w_{\mathrm L}x_1w_{\mathrm M}sx_2w_{\mathrm R}$ の形の分解についても同様である。

*証明.* T1 により $W':=w_{\mathrm L}x_1w_{\mathrm M}sx_2w_{\mathrm R}\in L$ で、$\Psi(W')=\Psi(W)$。仮定より $W'=W$、すなわち $tw_{\mathrm M}=w_{\mathrm M}s$。あとは Lyndon–Schützenberger の定理による。∎

**系 R1（文字の連）[証明済み].** 補題 R の状況で、ある文字 $\sigma$ について $\sigma^4$ が $L$ のある語に現れるとする。このとき、$W$ が $\sigma$ の連を二つ以上もつなら、$W$ の $\sigma$ の連はすべて長さ1である。

*証明.* $t=s=v=\sigma$、$x_1=x_2=\sigma$ の T1（冪の移送）を使う。長さ $\ge2$ の連 $R_2$ と別の連 $R_1$ があれば、$W=U\sigma Z\sigma\sigma V$ と書ける（$R_1$ が左にある場合。反対側も同様）。$Z$ は二つの連を隔てるので $\sigma$ 以外の文字を含み、$\sigma Z\ne Z\sigma$ となって補題 R に反する。∎

**系 R2（倍増族、内容型付け）[証明済み].** $n\ge3$ なら、$W_n$ を含む $L\in\mathcal C_{2,c}$ は、$W_n$ と Parikh ベクトルが等しい別の $\{\mathtt a,\mathtt b\}$-語
$$W_n':=\mathtt b^{n+1}\,w_{\mathrm M}\,\mathtt b^{n-1}\quad(W_n=\mathtt b^n w_{\mathrm M}\mathtt b^n)$$
を含む。よって $n\ge3$ で $L_n\notin\mathcal C_{2,c}$。

*証明.* $W_n$ は $W_{n-1}W_{n-1}$ の継ぎ目に $\mathtt b^{2(n-1)}\supseteq\mathtt b^4$ をもつ。$W_n$ は $\mathtt b^n\mathtt a$ で始まり $\mathtt a\mathtt b^n$ で終わるので、二つの連の長さはどちらも $n\ge2$ である。冪の移送（$i=\delta=j=1$）により、末尾の連から先頭の連へ $\mathtt b$ を一つ移せる。$L_n$ の $\mathtt c$ を含まない語は $W_n$ だけである（原稿どおり）。∎

**観察 [3]（網羅）.**

- $L_1,L_2\in\mathcal C_{2,c}$ である。よって内容型付けでの閾値はちょうど $n=3$ である。
- $n=3$ の最小の破れは $(\mathtt b,\mathtt{bb})\sim(\mathtt{bb},\mathtt b)$（共有文脈 $(\mathtt{bbbaabbaa},\mathtt b,\mathtt{aabbaabbb})$）。
- 区別する文脈は $(\mathtt{bb},W_3[3..18],\mathtt b)$ で、$W_3'=\mathtt{bbbbaabbaabbbbaabbaabb}\notin L_3$ を与える。

原稿の `thm:doubling-no-lift` は任意の型付けについて $n\ge2|\mathsf S|+2$ を要する（三文字の内容型付けでは $|\mathsf S|=7$ なので 16）。内容型付けに限れば、本文に「内容型付けでは $\mathtt b^4$ が $W_3$ に現れるので $n\ge3$ で足りる」と一文添えられる。

### 2.6 問い1b：$W_n$ の中での一致と共有

[3] で、$W_n$ の中の同じ型の2-組の共有を、周期 $\pi$ ごとに数えた [観察]。

| $n$ | $\|W_n\|$ | 共有の対の数 | 周期の分布（小さい順） |
|---|---|---|---|
| 2 | 10 | 8 | $\pi=1$：4、$\pi=3$：4 |
| 3 | 22 | 2453 | 1：645、2：189、3：217、4：360、… |
| 4 | 46 | 124285 | 1：12963、2：5813、3：5393、4：12944、… |

T0 により、これらはすべて「周期 $\pi$ の因子 $r$ の前後に、$c(r[1..\pi])$ を含む $x_1,x_2$ がある」形である。

**$W_2$ での例.**

- $(\mathtt{baa},\mathtt{baab})\sim(\mathtt{baab},\mathtt{aab})$：文脈 $(\mathtt b,\mathtt b,\mathtt b)$、$r=\mathtt{bb}$、$\pi=1$。
- $(\mathtt{ba},\mathtt{bbaab})\sim(\mathtt{baabb},\mathtt{ab})$：$r=\mathtt{abba}$、$\pi=3$。

$n=2$ ではこれらの移送がどれも $L_2$ の外に出ないので、$L_2$ はクラスに入る。

**一般形.** 抽出できる形は三つある。

- **(α) 連の継ぎ目** $\cdots\mathtt b\mathtt b\cdots$（$\pi=1$）。$n\ge3$ で $\mathtt b^4$ になり、致命的になる。
- **(β) 兄弟の平方** $W_iW_i$（$\pi=|W_i|$）。
- **(γ) 括弧の回文的な継ぎ目**（$\pi=3$ など）。

第1回の観察（$s_U$ での $(\mathtt b,\mathtt{aabb})\sim(\mathtt{bbaa},\mathtt b)$）は、型 $1$ をまとめる $s_U$ でだけ成り立つ共有である。内容型付けでは型が合わないので起こらない。

---

## 3. 課題2：部分クラスでの上界

### 3.1 定理 M$_\beta$（(c) の扱い）

$\beta_{\overline M}(L):=\sup_{w\in L}\#\{w\text{ の中の }\overline M\text{ の文字の極大連}\}$ とおく（$\beta\le\kappa$）。

**定理 M$_\beta$ [証明済み].** 定理 M と同じ仮定で、
$$\mu_M(L)\le\bigl(2|M|-1+\min\{\kappa_{\overline M},\,2\beta_{\overline M}\}\bigr)\,|V|\,(\rho_{\max}+r\bar\theta_G).$$
ファンアウトは任意で、代入可能性は使わない。

*証明.* 定理 M の証明のうち、段階 (3c)「$H$ の葉 $q$ 個 $\le\kappa$」だけを $q\le2\beta$ に置き換える。

- 各葉 $\eta_i$ について、(3a) の $\overline M$ の文字を含む組 $\mathbf y_i'$ を選ぶ。その文字を含む成分が $W$ の中で占める区間を $J_i$ とする。
- 葉どうしは比較不能なので、$J_i$ は互いに交わらない。位置の順に $J_{(1)}<\dots<J_{(q)}$ と並べる。
- 奇数番目の葉だけを同時に置き換える (F1)。$J_{(t)}$ と $J_{(t+2)}$ の像の間には、置き換えない $J_{(t+1)}$ が残る。これは空でなく、$M$ の文字だけからなる（外の節点の内側）。また、置き換えた節点の他の成分は $J_{(t+1)}$ と交わらない。
- よって $\overline M$ の極大連は $\ge\lceil q/2\rceil$ 個できる。したがって $q\le2\beta$。∎

**帰結.**

- (c) を「各語で $\overline M$ の文字が $\le k$ 連」と読むと、全ファンアウトで $\mu_M\le(2|M|-1+2k)|V|(\rho_{\max}+r\bar\theta)$。$\kappa$ にはよらない。しかしファンアウトも分けない。
- 倍増族は $\beta_{\mathtt c}(L_n)=3\cdot2^{n-2}$（$n\ge2$、[4]）なので、この読みの (c) には**入らない**。依頼文の「倍増族は (a)(b)(c) すべてに入る」は、(c) を「$\mathtt c$ は連として現れる」（自明な条件）と読んだときにだけ正しい。その読みの (c) は $|\Sigma|=3$、$M=\{\mathtt a,\mathtt b\}$ の一般の場合と同じになる。
- [4] の確認 [観察]：$L_1$〜$L_4$ で成立。ランダムな有限言語の良い文法 3904 件で違反は 0（比の最大は 1.000、自明な文法で等号）。

### 3.2 (a)・(b)：倍増族の所属と、得られなかったもの

- **(a)** 倍増族の文法はファンアウト1なので、重い節点もすべてファンアウト1である。所属する [証明済み]。
- **(b)** $W_n$ の最小の木で $\mathrm{St}$ の外にあり $\lambda>\bar\theta=4n$ の節点は、規則 $E_i\to\mathtt bE_{i-1}E_{i-1}\mathtt b$ を使う。これは倍増型である。所属する [証明済み]。

**$\kappa$ によらない上界：未解決。** 理由は命題 N にある。

- ファンアウト2で新たに効くのは T1 の移送で、これは保存的である。
- 短縮を生む「$\overline M$ の文字を消す」仕組みは、内容型付けの代入可能性にはない。系 6c も補題5も文字を増やす向きにしか働かない。
- 二文字の定理（付録 `app:two-letter-content`）は、挿入される文字が $M$ の他方の文字だったので、連の交換と Parikh 飽和が使えた。三文字では、挿入されるのが $M$ の外の $\mathtt c$ であり、飽和からも $\mathtt c$ のない短い語は出てこない。

**効く事例の特定 [証明済み].**

- 倍増族がファンアウト2で崩れる2-代入可能性の事例は、$\pi=1$ の T1（$\mathtt b^4$ による冪の移送）と、一意性（剛性）の組み合わせである（系 R1・R2）。
- (b) の空の中間 $A\to u_0BBu_2$ は平方 $yy$（$\pi=|y|$）を作る。補題 R により、剛性のある標的ではこの平方の前の $x_1y$ と後ろの $x_2$ の出現の間がすべて $|y|$ 周期でなければならない。

**予想 R [予想].** $f\ge2$、$L\in\mathcal C_{2,c}$ で、内容 $M$ の最短語が一意なら、$\mu_M(L)\le\mathrm{poly}(\|G\|,\bar\theta_G)$。

- ファンアウト1では偽である（倍増族）。したがって、成り立てば**剛性のある標的の部分クラスでファンアウトを分ける主張**になる。
- ただし op:fanout-two そのものは、剛性のない標的が残るので解決しない。
- 証明の筋道は、補題 R の周期性の要求と文法の自己相似性（同じラベルの重い節点のコピーが離れた位置に $x_2$ を作る）を組み合わせることである。(b) で中間が空の場合を最初の標的にするのがよい。

---

## 4. 課題3：移送を逃れる配置の候補

[5] の結果。$n\le3$ は $d\le2$ の網羅検査、$n=4$ は $d=1$ の網羅と T1 の反例証明書の探索。証明書は、共有文脈と区別する文脈と、厳密に判定した四つの語の所属からなるので、非所属の証明になる。$M=\{\mathtt a,\mathtt b\}$、D 系は $M=\{\mathtt a,\mathtt b,\mathtt d\}$。$\|G\|,\bar\theta,\mu,\kappa,\beta$ は崩れた $n$ での値である。

| 候補 | 方向 | 崩れた $n$ | $\|G\|$ | $\bar\theta$ | $\mu$ | $\kappa$/$\beta$ | 最小の破れ | 分類 |
|---|---|---|---|---|---|---|---|---|
| C0 $E\to\mathtt bEE\mathtt b\mid\mathtt cE\mathtt c$ | 基準 | 3 | 46 | 12 | 22 | 8/6 | $(\mathtt b,\mathtt{bb})\sim(\mathtt{bb},\mathtt b)$ | α：$\pi=1$ |
| C2 $\mathtt bE\mathtt aE\mathtt b$ | (ii) | 2 | 35 | 9 | 13 | 4/4 | $(\mathtt{ab},\mathtt{aa})\sim(\mathtt{aba},\mathtt a)$ | α |
| C3 段ごとの区切り $\mathtt a^i$ | (ii) | 2 | 36 | 10 | 14 | 4/4 | 同上の形 | α |
| C4 $\mathtt c$/$\mathtt d$ 枝を段で交互に | (iii) | 3 | 46 | 12 | 22 | 8/6 | $(\mathtt b,\mathtt{bb})\sim(\mathtt{bb},\mathtt b)$ | α |
| C4′ $\mathtt cE\mathtt d$ | (iii) | 3 | 46 | 12 | 22 | 8/6 | 同上 | α |
| C6 Thue–Morse 型 | (ii) | 2 | 43 | 5 | 4 | 4/3 | $d=1$：$\mathtt{ca}\sim\mathtt{cacc}$ | γ：ファンアウト1で崩れる |
| K2 対の倍増 | (i) | 2 | 38 | 9 | 9 | 4/4 | $d=1$：$\mathtt{ab}\sim\mathtt{aabb}$ | γ |
| K3 $\mathtt b$ 付き対の倍増 | (i) | 2 | 42 | 11 | 15 | 4/4 | $(\mathtt b,\mathtt{bb})\sim(\mathtt{bb},\mathtt b)$ | α |
| K5 二位相の $\mathtt c$ | (i) | 2 | 54 | 11 | 15 | 4/4 | $d=1$ | γ |
| K7 $\mathtt c$ を成分の間に | (i) | 2 | 38 | 9 | 9 | 2/2 | $d=1$：$\mathtt{aacb}\sim\mathtt{acbc}$ | γ |
| D1 括弧 $\mathtt b/\mathtt d$ 交互 | (ii) | 2 | 35 | 9 | 13 | 4/4 | $(\mathtt{bada},\mathtt{bb})\sim(\mathtt{badab},\mathtt b)$ | α |
| D5′ $M$-語に文字の平方なし | (ii) | 3 | 49 | 13 | 29 | 8/8 | $(\mathtt c,\mathtt{cac})\sim(\mathtt{cc},\mathtt{ac})$ | α（外の文字 $\mathtt c$ の連） |
| D5″ どの語にも文字の平方なし（5文字） | (ii)(iii) | 3 | 49 | 13 | 29 | 8/8 | $(\mathtt{ca},\mathtt{acac})\sim(\mathtt{caca},\mathtt{ac})$ | β：$\pi=2$ |

**崩れ方の分類 [観察].**

- **(α) $\pi=1$ の連の移送（冪の移送）.** 文字の平方 $\sigma\sigma$ の前後に $\sigma$ があれば起こる。$\sigma$ は $M$ の文字でも外の文字でもよい（D5′ では $\mathtt c$ の連）。
- **(β) $\pi=2$ の移送.** 文字の平方をすべて除いても（D5″）、区切りと $\mathtt c$ 枝の組み合わせが $(\mathtt{ca})^3\mathtt c$ のような周期2の因子を作り、$n=3$ で崩れた。
- **(γ) $d=1$ の崩れ（異なる二語での共有）.** ファンアウト1の条件で崩れており、ファンアウト2固有ではない。

ファンアウト2固有の崩れはすべて「同じ語の中」の T1 で、二語にまたがる $d=2$ の共有が最小の破れになった例はなかった。

**課題1の仮定への反映.** 補題 U により、T1 の起点は避けられない。崩れないためには、$L$ がその移送で閉じている必要がある（下の N12）。剛性のある族（一意の希少な語）は、補題 R の周期性の要求を、少なくとも試した族では満たせなかった。したがって否定の向きの次の候補は、**移送で閉じた（Parikh 的に柔らかい）$M$-部分**をもつ非剛性の族である。

---

## 5. 課題4：(Hyp) の判定

$\mathcal B^{\le2}_{2,c}$ を定義どおりに実装した（[6]）。標的 $L$ が有限なら、健全性から $L(\mathcal B(K))\subseteq L$ なので、長さ $\max|L|$ で切っても**厳密**である（到達可能な非終端記号の組はすべて $L$ の語の中に現れるため）。

**命題 4.1（(Hyp) は偽）[証明済み].** $L=\{\mathtt a,\mathtt b\}^3\setminus\{\mathtt{aaa},\mathtt{bbb}\}$、$K=\{\mathtt{aab},\mathtt{aba},\mathtt{abb}\}$ とする。

- (i) $L\in\mathcal C_{f,c}$（すべての $f$）。
- (ii) $L(\mathcal B^{\le2}_{2,c}(K))=L(\mathcal B_{2,c}(K))=S:=L\setminus\{\mathtt{bba}\}$。
- (iii) $S\notin\mathcal C_{1,c}$。

*証明.*

- **(i)** 組 $\mathbf x$ が二種類の文字を含むか、異なる単一文字の成分をもつなら、$\mathcal D(\mathbf x)$ は「固定部分の長さが $3-|\mathbf x|$ の許容文脈すべて」である。すべての成分が同じ $\sigma$ だけなら、そのうち固定部分が $\sigma$ 以外の文字を含むものである。どちらも成分の内容と $|\mathbf x|$ だけで決まり、共有があれば $|\mathbf x|$ は等しい。
- **(ii)** Link を列挙する。
  - 長さ3の語の2-出現は $(w_1,w_3)$ と文脈 $(\varepsilon,w_2,\varepsilon)$ だけである。同じ型の相異なる2-組で文脈を共有するものはない。
  - 1-組で同じ型の相異なるものが文脈を共有するのは、$(\mathtt{ab})\sim(\mathtt{ba})$（文脈 $(\mathtt a,\varepsilon)$）と、三語の全体（文脈 $(\varepsilon,\varepsilon)$）だけである。純な組は長さで分かれる。
  - よって $[\mathbf x]$ が自分以外を生成するのは、$[\mathtt{ab}],[\mathtt{ba}]$（$\{\mathtt{ab},\mathtt{ba}\}$）と三語の非終端記号だけである。2-組の成分はすべて長さ1なので、$\mathtt{ab}$ を成分にもたない。
  - 語の水準の Comp は $K$ の語の分解なので、生成される語は $K$ の語の中の因子 $\mathtt{ab}/\mathtt{ba}$ を一箇所入れ替えたものに限られる：$\{\mathtt{aab},\mathtt{aba}\}\cup\{\mathtt{aba},\mathtt{baa},\mathtt{aab}\}\cup\{\mathtt{abb},\mathtt{bab}\}=S$。
  - 一様版で加わる rank 3 の規則は、子が1文字ずつで生成は自明なので、何も変えない。
- **(iii)** $(\mathtt{ab})$ と $(\mathtt{ba})$ は文脈 $(\varepsilon,\mathtt b)$ を共有する（$\mathtt{abb},\mathtt{bab}\in S$）。しかし $(\mathtt b,\varepsilon)$ では $\mathtt{bab}\in S$、$\mathtt{bba}\notin S$。∎

**弱めた形も偽 [証明済み].**

- **「間にクラスの元が挟まる」.** $S\subseteq L''\subsetneq L$ をみたすのは $L''=S$ だけで、$S\notin\mathcal C$。
- **命題 H(ii) の結論そのもの.** $K$ は $\mathcal F_L$ のすべての元と交わる。$K\subseteq L'\in\mathcal C_{1,c}$ なら $(\mathtt{ab})\sim(\mathtt{ba})$ から $\mathtt{baa},\mathtt{bab},\mathtt{bba}\in L'$ となり、$L'=L$ だからである。それでも $K$ は特徴標本でない。

**命題 4.2（$h(L)$ は特徴標本の長さに届かないことがある）.** $L=\{w\in\{\mathtt a,\mathtt b\}^4:|w|_{\mathtt a}=2\}$（6語）とする。

- (i) $L\in\mathcal C_{f,s}$（任意の $f$、任意の型付け）[証明済み]。Parikh の切片では、分布は $(|\mathbf x|,\Psi(\mathbf x))$ だけで決まり、共有があればこれらは等しいからである。
- (ii) $F=\{\mathtt{aabb},\mathtt{abab}\}$ は $\mathcal F_L$ のすべての元と交わるので、$h(L)=8$ [証明済み]。$F\subseteq L'\in\mathcal C_{1,c}$ とする。$(\mathtt{ab})\sim(\mathtt{ba})$（文脈 $(\mathtt a,\mathtt b)$）なので、隣り合う $\mathtt{ab}\leftrightarrow\mathtt{ba}$ の入れ替えで閉じ、6語すべてが出る。
- (iii) $L(\mathcal B(F))=L\setminus\{\mathtt{bbaa}\}$（$r_{\max}=2$ でも 4 でも）。2語の特徴標本はなく、最短の特徴標本の長さは 12 [観察（網羅、有限なので厳密）]。

  手での理由は次のとおり。語の水準の Comp で $K$ の語の位置0を覆う子は、$\{\mathtt a,\mathtt{aa},\mathtt{ab},\mathtt{aab},\mathtt{aba},\dots\}$ の接頭辞の組である。その生成は $\mathtt a$ か $\mathtt{ba}$ で始まるので、$\mathtt{bb}$ で始まる語は出ない。

**数値 [観察].**

| 標的 | 調べた $K$ | $L(\mathcal B(K))\notin\mathcal C$ | 不動点 $\notin\mathcal C$ | $h(L)$ | 最短の特徴標本 |
|---|---|---|---|---|---|
| $\{\mathtt a,\mathtt b\}^3\setminus\{\mathtt{aaa},\mathtt{bbb}\}$ | 63 | 12 | 0 | 9 | 9 |
| $\{\mathtt a,\mathtt b\}^3$ | 255 | 48 | 0 | 15 | 15 |
| $\|w\|=4,\ \|w\|_{\mathtt a}=2$ | 63 | 8 | 0 | 8 | 12 |
| ランダムな有限の標的 150 個 | 2386 | 0 | — | — | — |

ランダムな標的では $\mathcal B$ がほとんど何も加えないので、反例は出ない。反例は「自由」に近い標的で出る。

**提案.** 作用素の反復 $K\mapsto L(\mathcal B(K))$ の不動点を $K^\infty$ とし、学習器 $\mathcal B^\infty(K):=\mathcal B(K^\infty)$ を考える。

- **(Hyp$^\infty$)**「$K^\infty\in\mathcal C_{f,s}$」**[予想]**。上の表の全例で成立した（反復は高々5回）。
- (Hyp$^\infty$) のもとでは、命題 H(ii) と同じ証明により、$\mathcal B^\infty$ の最短の特徴標本の長さは $h(L)$ に等しい [条件付き]。
- 単調性から、$h(L)\le\mathrm{char}_{\mathcal B^\infty}(L)\le\mathrm{char}_{\mathcal B}(L)$ [証明済み]。$\mathcal B$ の単調性は、$K$ を増やすと Obs・Link・Comp が増えるだけであることから出る。
- 残る問いは「$\mathrm{char}_{\mathcal B}\le\mathrm{poly}(\mathrm{char}_{\mathcal B^\infty},\|G\|,\bar\theta)$ か」である。
- 失敗の原因ははっきりしている。Link は $K$ の中に共通の文脈を要求するが、クラスの閉包は $L$ の新しい語を経由する推移的な連鎖である（例 4.2 では $\mathtt{baba}$ を経由して $\mathtt{bbaa}$ に至る）。

---

## 6. 否定例の必要条件（N1〜N9 への追加）

- **N10 [証明済み、定理 M$_\beta$].** 稀な内容 $M$ による否定例では、$\kappa$ だけでなく**ブロック数** $\beta_{\overline M}(L_n)$ も超多項式でなければならない。ファンアウトは分けない（倍増族は $\beta=3\cdot2^{n-2}$）。
- **N11 [証明済み、補題 R・系 R1].** 希少な語 $W$ がその Parikh ベクトルで一意（剛性）なら、次が成り立つ。
  - $L$ のどの T1 の起点 $(x_1,r,x_2)$ についても、$W$ の中の $x_1t$ と後ろの $x_2$ の間は周期 $\pi$ でなければならない。
  - $\sigma^4$ が現れる文字 $\sigma$ については、$W$ の $\sigma$ の連は一つしかないか、すべて長さ1である。
  - ファンアウト1の剛性のある倍増族は、内容型付けでは $n\ge3$ で死ぬ。
- **N12 [証明済み、T1＋補題 U].** $L$ は自分の語が生む T1 の移送すべてで閉じていなければならない。長い $M$-語は周期 $\le|M|$ の起点を必ずもつ。したがって長さ $\mu_M$ の $M$-語の集合は、移送で閉じた（多くは大きな）集合である。
- **N13 [観察].** 試した13族で、ファンアウト2固有の崩れはすべて同じ語の中での $\pi\in\{1,2\}$ の T1 だった。
- **N14 [証明済み].** (Hyp) は偽で、$h(L)$ による下界は $\mathcal B^{\le2}_{2,c}$、$\mathcal B_{2,c}$ について正確ではない（例 4.2）。下界の道具としては依然として使える（$h\le\mathrm{char}$）。

## 7. 次の一手

1. **予想 R の証明.** 剛性のある標的でファンアウト2なら多項式になることを、(b) の中間が空の場合から示す。補題 R の周期性の要求と、同じラベルの重い節点のコピーが作る離れた $x_2$ の出現を組み合わせる。成り立てば、`thm:doubling-no-lift` を「剛性のある族はすべて持ち上がらない」に一般化でき、本文に入れる価値がある。
2. **非剛性の否定候補.** $M$-部分が T1 で閉じた族を設計する（Parikh 的に柔らかい $M$-語の集合と、$\mathtt c$ の括弧構造の組み合わせ）。あるいは逆に、移送で閉じていることが多項式を強いることを示す。後者は二文字の飽和補題を「周期ブロック」に一般化する方向である。
3. **(Hyp$^\infty$) の検証と証明.** 不動点 $K^\infty$ がクラスに入るか。入るなら、$\mathrm{char}_{\mathcal B}$ と $\mathrm{char}_{\mathcal B^\infty}=h(L)$ の差を評価する。

## 8. スクリプト

`check_claude_fanout2_transfer_round4_2026-11-09.py`。単体で動き、標準ライブラリのみ、約10秒、種 20261109。

**内容.**

- **[1]** MCFG の基本操作（良さの検査、$\|G\|$、厳密な $\theta$、$(A,\text{内容})$ の動的計画法による $\mu_M$、列挙）と、有限言語の $d\le2$ の網羅検査。
- **[2]** T0 の検査。
- **[3]** 倍増族の所属（$n\le3$）、最小の破れ、$W_3\to W_3'$、$W_n$ の中の共有の周期分布。
- **[4]** 定理 M$_\beta$ の検査。
- **[5]** 候補13族と、T1 の反例証明書の探索。
- **[6]** $\mathcal B^{\le2}_{2,c}$ の実装、(Hyp) の反例、$h(L)$ と最短の特徴標本の比較、$\mathcal B^\infty$。

**出力の要点 [観察].** 本文 §2.5、§3.1、§4、§5 の表に記した。とくに次の三点。

- $L_1,L_2\in\mathcal C_{2,c}$、$L_3\notin\mathcal C_{2,c}$、$W_3'\notin L_3$。
- 定理 M$_\beta$ の違反は 0/3904。
- (Hyp) の反例は $\{\mathtt a,\mathtt b\}^3$ 系で 12〜48 件、例 4.2 で $h=8<12$。

有限言語の網羅検査と反例証明書を除き、計算は所属の証明ではない。
