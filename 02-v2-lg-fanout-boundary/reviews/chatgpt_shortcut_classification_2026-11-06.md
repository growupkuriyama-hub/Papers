# ファンアウト2・三文字の稀な内容型 `{a,b}`：近道の文字位置一致、スロット移送、侵入反鎖の条件付き上界

**研究日：2026-11-06**  
**対象：** `op:fanout-two` の三文字部分問題。**判定：一般問題は未解決。**  
**証明・検査した範囲：** 近道の「最終橋」の二分類、位相ずれによる任意の短縮率を持つ2段証明書族、二穴スロット移送の一般補題、`c` の出現数／連数を制限した場合の反鎖上界、既存10件の証明書の独立再生。

## 0. 出典と定義の固定

### 0.1 参照・版

以下の順で条件を照合した。

1. 現行英文原稿 [`02-v2-lg-fanout-boundary/main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)（取得時 Git blob `ed2d7493a597687e63d8c23d15abd7b2072dca94`）。`def:class-cmcf`（参照時行650付近）、`prop:rare-type`（同1380付近）、`lem:thickness-equivalence`、`thm:doubling-no-lift`。
2. [前報 (153) `claude_mu_ab_2026-11-05.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_mu_ab_2026-11-05.md)（blob `ecce657e701da86b14aaaab407162a3b8ab7de67`）の補題1、3、7、7′、命題5、および m=3 証明書。
3. [前報 (155) `chatgpt_virtual_length_2026-11-05.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_virtual_length_2026-11-05.md)（blob `5f7307cfeb72bf1e2c4ebbb3b8454a4a60bc4c2e`）の修正条件、K、(VN)、定理6.1、m=3 の追加3証明書。
4. Project の参考資料：`03_Multiple_Context-Free_Grammars_Foundations_and_Learning_v9.pdf`（MCFG 定義、Yoshinaka の多次元代入可能性）、`02_Substitutability_and_Positive-Data_Grammar_Learning_v6.pdf`、`TCS-D-26-00494_R1.pdf`、`project-master-v17-2026-11-04.md`。これらは一次定義の背景であり、以下の新しい補題が既知文献で未発表という保証ではない。

**版の注意：** 2026-11-06 の focused rewrite により、`prop:sl-reduction`、二文字・full-content 節の一部は現行 `main.tex` から [`parked/2026-11-06_focus/main_before_focus_59pp.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/parked/2026-11-06_focus/main_before_focus_59pp.tex) へ退避されている（README Change log (157)）。したがって依頼文の `prop:sl-reduction` が**現行 focused 本文に残っている**とは扱わない。数学的主張は提示された既知事項として条件付きで利用する。 (137), (139), (142), (149), (150) も今回の対象となる以前の研究系列を指し、(153), (155) の報告書とは別物である。

### 0.2 記号・SUB の厳密な意味

\(\Sigma=\{a,b,c\}\)、\(\operatorname{cont}(w)\subseteq\Sigma\) を出現文字の集合、内容型付けを \(c_\Sigma\) と書く。ここでは \(c\) の一字と型付け \(c_\Sigma\) を区別する。\(L\in C_{2,c_\Sigma}\) は **ファンアウト \(\le2\) の MCFL** であり、**arity 1 と arity 2 の双方**について以下を満たすこととする。

\(1\le d\le 2\) に対し、許容文脈 \(E=v_0\square_1v_1\cdots v_{d-1}\square_dv_d\) は両端 \(v_0,v_d\in\Sigma^*\)、内部 \(v_1,\dots,v_{d-1}\in\Sigma^+\) とする。穴に入る各成分も**非空**である。

\[
 E[x],\ E[y],\ F[x]\in L,\quad
 \forall j\ \operatorname{cont}(x_j)=\operatorname{cont}(y_j)
 \quad\Longrightarrow\quad F[y]\in L.\tag{SUB_d}
\]

\(\mathrm{SUB}_{1,2}\) はこの二つの関係の推移的閉包。\(\mathrm{SUB}_1\) は単に一穴の一段で、\(\mathrm{SUB}_2\) は二穴の一段を表す。`SUB₂` の内部固定部分は空であってはならない。文法の部分木交換は、`SUB` とは別の、文法から直接得られる所属証明である。

\(G\) は reduced good MCFG、ファンアウト \(\le2\)、規則ランク \(\le r\)、\(v=|V|\)、\(\theta=\bar\theta_G\ge1\)。厚さ補題より、各非終端に総長 \(\le\theta\) の生成があり、各規則の直接書く終端は \(\le\theta\) 個。\(\mu_{ab}(L)=\min\{|w|:w\in L,\operatorname{cont}(w)=\{a,b\}\}\) とし、該当語がない場合には論じない。最短語 \(W\) の最小節点数の成功導出 \(T\) で、生成総長 \(>\theta\) の節点を重い節点、短い代替生成が必ず \(c\) を含むものを **\(c\)-強制節点**と呼び、その反鎖最大幅を \(q(T)\) とする。

**既知で使用する式**は (153) 補題1の
\[
\mu_{ab}(L)\le 3(r+1)v\theta\,(q(T)+2).\tag{0.1}
\]
のみ。定理6.1 \(\mu_{ab}\le(r+1)\theta^2\) は言語全体が一つの非負加法的水準で \(\lambda(a)=\lambda(b)>0\) という**追加条件つき**であり、一般の上界には移さない。

## 1. 主張のステータス表

| 主張 | ステータス | 正確な範囲 |
|---|---|---|
| 長さが初めて変わる \(c\)-free 帰結の共通文脈には \(c\) がある | **[証明済み]** | 種の全 \(c\)-free 語が同一長 \(N\) である場合（§2） |
| \(S_k=\{a^kba,ca^kb,ca^{2k}b\}\) は一段では短い \(ab\) 語を生まないが、2段で `ba` を生む | **[証明済み]** | 任意の整数 \(k\ge1\)、arity 制限なし（§3） |
| 同族の短縮率 \(2/(k+2)\) は0へ近づく | **[証明済み]** | 上の2段証明書についてだけ |
| 周期ブロックの二穴スロット移送：\(p^M,p^i\beta p^j\in L\Rightarrow p^h\beta p^{i+j-h}\in L\) | **[証明済み]** | \(M\ge i+j+1\)、\(1\le h\le i+j-1\)、\(\beta\ne\varepsilon\)、\(L\in C_{2,c_\Sigma}\)（§4） |
| 前報7設計および未決3設計の近道証明書 | **[証明済み：個々の証明書の再生]** | m=3、文法から完全列挙した種集合、合計10件・計27段（§5、付録A） |
| `L_n` 二段証明書 | **[証明済み]** | 全 \(n\ge3\) は記号的証明、\(n=3,\ldots,8\) は別実装で種の所属を再検査（§5） |
| \(L\) の全語が \(c\) を高々 \(B\) 個含めば \(q\le B\) | **[条件付き（全語への一様制限）・証明済み]** | 任意の上記 \(G,T\)（§6） |
| \(L\) の全語の \(c\) の連数が高々 \(B\) なら \(q\le5B\) | **[条件付き（全語への一様制限）・証明済み]** | ファンアウト2、上記 \(G,T\)（§6） |
| 一般に \(q\le\operatorname{poly}_r(v,\theta)\) | **[予想／未解決]** | 一般の \(C_{2,c_\Sigma}\) |
| 条件1–3を同時に満たす超多項式族 | **[未構成]** | §7の候補はいずれも失敗か未立証 |

**重要：** §2の二分類は「証明書の共通文脈が \(c\) を含むか」による**必要な骨格**であって、全ての局所的な文字の一致を有限個の十分条件へ分類し尽くしたという意味ではない。

## 2. 課題A：証明書の形と文字位置の分類

### 命題2.1［証明済み］最初の **長さ変更** には必ず `c`-bridge がある

種集合 \(S\subseteq\Sigma^+\) の \(c\)-free 語が**全て同一長** \(N\) であるとする。`SUB₁`・`SUB₂` の有限導出で、初めて長さ \(N\) と異なる \(c\)-free 語 \(Z\) が生成された段を \(E[x],E[y],F[x]\Rightarrow F[y]=Z\) と書く。この段の共通文脈 \(E\) は \(c\) を含む。

**証明。** 各成分の内容が同じなので、\(\operatorname{cont}(F[x])=\operatorname{cont}(F[y])\) である。\(F[y]\) は \(c\)-free だから \(F[x]\) も \(c\)-free である。選んだ段より前に生成済みの全ての \(c\)-free 語は長さ \(N\) なので \(|F[x]|=N\)。\(|F[y]|\ne N\) だから、文脈の固定部分の長さが相殺され、\(\|x\|_1\ne\|y\|_1\) である。もし \(E\) が \(c\)-free なら、\(x,y\) の各成分も \(c\)-free（\(F[y]\) が \(c\)-free かつ対応成分の内容が等しい）なので、\(E[x],E[y]\) も \(c\)-free である。ともに以前から存在するため長さは \(N\) であり、\(|E[x]|-|E[y]|=\|x\|_1-\|y\|_1=0\) となって矛盾する。ゆえに \(E\) は \(c\) を含む。□

**注意。** この命題は「最初の \(c\)-free **新語**」一般には成立しない。`SUB₂` では同じ \(E\) に異なる二組を代入して \(E[x]=E[y]\) となる場合があり、**長さを変えずに**別の \(c\)-free 語を得る可能性を否定していない（§4の周期移送を参照）。そのため、一段の "新語" と一段の "長さ変更" は区別する。最終段の \(E\) に \(c\) が必要だとも言わない。

### 完全な前提を持つ既知の局所型（十分条件）

**型 P（親逃げ道の右側因子一致、補題7）[証明済み・既知]：** \(W=lYY'r\)、\(lY\beta r\in L\)、\(ls\beta r\in L\)、\(\operatorname{cont}(lY)=\operatorname{cont}(ls)\)、\(|s|<|Y|\)。ここで \(\beta\) は \(Y'\) と同じ非終端からの代替生成とし、\(W\in L\)。\(E=\square\beta r\)、\(x=lY\)、\(y=ls\)、\(F=\square Y'r\) とすると `SUB₁` 一段で \(lsY'r\in L\)、長さは \(|W|-(|Y|-|s|)\)。必要な所属は**全て仮定した**。例えば親逃げ道 \(e_C=s\beta\) の文法生成から \(ls\beta r\) が得られる場合に適用する。鏡像型 \(\beta s\) は左右反転し、同じ計算を行う。

**型 PP（不足する文字を別の文脈で補う二段、補題7′）[証明済み・既知]：** \(W=UZUZ\) と、\(\beta\beta,\beta Ue,UZUZ,UZUe,s\beta\in L\)、\(\operatorname{cont}(\beta)=\operatorname{cont}(Ue)\)、\(\operatorname{cont}(UZU)=\operatorname{cont}(sU)\)、\(|s|<|UZ|\) を仮定する。証明書は次の二段である。

| 段 | \(E\) | \(x\) | \(y\) | \(F\) | 新語 |
|---|---|---|---|---|---|
| 1 | \(\beta\square\) | \(\beta\) | \(Ue\) | \(s\square\) | \(sUe\) |
| 2 | \(\square e\) | \(UZU\) | \(sU\) | \(\square Z\) | \(sUZ\) |

段1の三前提は \(\beta\beta,\beta Ue,s\beta\)、段2は \(UZUe,sUe,UZUZ\)。\(sUZ\) の内容は \(\{a,b\}\) で、長さは \(|W|-(|UZ|-|s|)\)。**\(e_C=s\beta\) だけを見てこの五つの所属を省いてはいけない。**

**型 R（\(c\) の連の長さ・区切りの重なり）[証明済み：具体例のみ]：** \(e_i=c^i\) および \(e_i=ac^ib\) について、m=3で2段の証明書が再生できた。\(c,cc\) 等の具体的な同一文字区間が異なる階層の文脈として再利用される。これを「任意の \(c\) の連の一致だけで近道」という一般補題にするのは**誤り**である。証明書の \(E,x,y,F\) は付録Aに全記録する。

**型 T（複数橋が連鎖した混合位相）[証明済み：具体例のみ]：** `(ac,cc,c)`、`(ca,bbc,abc)`、`(cc,ac,c)` はそれぞれ6、7、5段。途中で \(c\)-free でない埋め草が交換され、最後に \(ab\) 型の因子が同じ \(c\)-含有枠に置かれる。これらを型Pまたは型Rの単一の局所等式だけに帰着する一般論は得られなかった。

**型 V（\(c\)-bridge で伸長した後の純 \(ab\) 位相一致）[新規・証明済み]：** §3の \(S_k\)。最終段の \(E=a^k\square\) は \(c\) を含まない。これは型P・Rと異なる**証明書の形**である。

**型 S（二穴での周期ブロックの位置一致）[新しい一般形・証明済み]：** §4のスロット移送。\(\square p^t\square\) の二つの穴をずらしても詰めた語 \(p^M\) が**文字ごとに同じ**という位置一致を使う。これは必ずしも長さを縮めず、しばしば `C₂` への所属を直接否定する。

## 3. 課題Aの新しい定理：任意の縮小率を持つ「伸長→位相一致」族

### 定理3.1［証明済み］

任意の \(k\ge1\) で
\[
 W_k=a^kba,\qquad X_k=ca^kb,\qquad Y_k=ca^{2k}b,
 \qquad S_k=\{W_k,X_k,Y_k\}.
\]

(i) \(S_k\) の**一段帰結**には、内容が \(\{a,b\}\)、長さ \(<k+2\) の語はない。これは任意の arity \(d\ge1\) の許容 `SUB_d` について成立する。  
(ii) `SUB₁` **ちょうど二段**で `ba` が強制される。短縮量は \(k\)、元の長さに対する最終長さの比は \(\frac{2}{k+2}\to0\)。  
(iii) したがって \(S_k\) を含むどの \(C_{1,c_\Sigma}\) または \(C_{2,c_\Sigma}\) の言語にも `ba` が入る。\(S_k\) 自身はどちらのクラスにも属さない。

#### 証明：(ii) と (iii)

一段目の4要素は
\[
 E_1=c\square,\quad x_1=a^kb,\quad y_1=a^{2k}b,\quad F_1=\square a.
\]
\(E_1[x_1]=X_k\)、\(E_1[y_1]=Y_k\)、\(F_1[x_1]=W_k\)。\(x_1,y_1\) の内容はいずれも \(\{a,b\}\) で、\(E_1,F_1\) は許容一穴文脈だから
\[
 T_k=F_1[y_1]=a^{2k}ba=a^kW_k
\]
が強制される。\(|T_k|=2k+2>|W_k|=k+2\) であり、この段では**短縮していない**。

二段目は
\[
 E_2=a^k\square,\quad x_2=W_k=a^kba,\quad y_2=ba,\quad F_2=\square.
\]
\(E_2[x_2]=a^kW_k=T_k\)、\(E_2[y_2]=a^kba=W_k\)、\(F_2[x_2]=W_k\)。\(\operatorname{cont}(x_2)=\operatorname{cont}(y_2)=\{a,b\}\) で、`SUB₁` により \(F_2[y_2]=ba\) が入る。\(|ba|=2\)、\(k+2-2=k\)、比は \(2/(k+2)\) である。\(k\ge1\) なら `ba` は \(S_k\) のどの語にも等しくないので、\(S_k\) 自身は代入可能でない。□

#### 証明：(i) ——全ての arity に対する一段除外

一段の証明書 \(E[x],E[y],F[x]\in S_k\) から \(Z=F[y]\) が \(c\)-free で \(|Z|<k+2\) と仮定する。内容保存から \(F[x]\) も \(c\)-free、したがって \(F[x]=W_k\) であり、\(x,y\) はすべて \(c\)-free となる。

\(|Z|<|W_k|\) なので \(\|y\|_1<\|x\|_1\) であり、\(|E[y]|<|E[x]|\)。したがって \(E[x],E[y]\) は異なる長さの二語であり、\(S_k\) のうち内容 \(\{a,b,c\}\) を持つ二語 \(X_k,Y_k\) に限られる。異なる2語が同じ文脈を受け入れるために各穴は \(c\)-free であるから、\(E\) の固定部分に \(c\) が入り、\(W_k\) は共通文脈の語にならない。\(|Z|<|W_k|\) なので \(|y|_1<|x|_1\) であり、長い方の \(Y_k\) が \(E[x]\)、短い方の \(X_k\) が \(E[y]\)。よって
\[
 |x|_1-|y|_1=|Y_k|-|X_k|=k.\tag{3.1}
\]
各穴は非空なので \(|y|_1\ge d\)、したがって \(|x|_1\ge k+d\)。また \(F[x]=W_k\) で、\(F\) の \(d-1\) 本の内部固定区間はすべて非空だから
\[
 |x|_1\le |W_k|-(d-1)=k+3-d.\tag{3.2}
\]
結合すると \(k+d\le k+3-d\)、すなわち \(2d\le3\)。\(d\) は正整数なので \(d=1\) しか残らない。

一穴では \(k+1\le|x|\le k+2\)。\(|x|=k+2\) なら \(F\) の固定文字は0個で \(x=W_k=a^kba\) だが、\(Y_k=ca^{2k}b\) の部分語に `ba` が現れないので \(x\) は \(Y_k\) の因子になれず矛盾。\(|x|=k+1\) なら、\(Y_k\) と \(W_k\) に共通する長さ \(k+1\) の \(c\)-free 因子は \(a^kb\) しかない。理由は、\(Y_k\) の \(c\)-free 因子は \(a\) の連または末尾が \(b\) の \(a^tb\) である一方、\(W_k\) の最大の \(a\) の連長は \(k\) であり、\(b\) を含む共通候補は \(a^kb\) に限られるからである。すると \(\operatorname{cont}(x)=\{a,b\}\) だが (3.1) より \(|y|=1\) であり、一文字語が内容 \(\{a,b\}\) を持つことはできない。矛盾。したがって一段短縮は存在しない。□

**位置一致の本体：** \(X_k,Y_k\) で先頭の `c` と末尾 `b` が一致し、中間の `a` が \(k\) 個増減する。そこで生まれた \(T_k\) が \(a^kW_k\) に**文字単位で重なる**。2段目は \(a^k\) だけ左へ開始位置をずらし、より短い `ba` を取り出す。単なる長さ・Parikh ベクトル一致ではこの2段目の因子一致は導けない。

**分類上の意味：** 原稿で見つかっている証明書の最終段の `c`-bridge だけを分類した場合に抜ける型である。ただし \(S_k\) は倍増文法の種と同一ではなく、\(q\) の多項式上界をこれだけで与えない。

## 4. 課題Cの必要条件：二穴スロットの全位置移送

### 補題4.1［証明済み］周期ブロックにおける任意位置の移送

\(p\in\Sigma^+\)、\(\beta\in\Sigma^+\)、\(i,j\ge1\)、\(n=i+j\)、\(M\ge n+1\) とする。内容型付けで \(L\in C_{2,c_\Sigma}\) かつ
\[
 p^M\in L,\quad p^i\beta p^j\in L
\]
なら、**すべての** \(1\le h\le n-1\) について
\[
 p^h\beta p^{n-h}\in L.\tag{4.1}
\]

**証明。** \(t=M-n\ge1\) と置く。\(E=\square_1p^t\square_2\)、\(F=\square_1\beta\square_2\)、\(x=(p^i,p^j)\)、\(y=(p^h,p^{n-h})\) とする。内部固定語 \(p^t,\beta\) は非空、全穴成分も指数が正なので非空。内容型付けでは \(\operatorname{cont}(p^s)=\operatorname{cont}(p)\) が任意の \(s\ge1\) で成立し、\(x,y\) は成分ごとに同型。さらに
\[
 E[x]=p^{i+t+j}=p^M=E[y],\qquad F[x]=p^i\beta p^j\in L.
\]
したがって `SUB₂` の三前提が成立し、\(F[y]=p^h\beta p^{n-h}\in L\)。\(h\) は所定の範囲で任意だった。□

**適用例（既知の (149) を一段で排除する形を一般化）：** \(p=ab\)、\(i=1,j=2,n=3,M=4,t=1,h=2,\beta=c\) とする。
\[
 E=\square_1ab\square_2,\ x=(ab,abab),\ y=(abab,ab),\ F=\square_1c\square_2.
\]
\(E[x]=E[y]=abababab\)、\(F[x]=abcabab\) は \(A_2\) の生成にあり、\(F[y]=ababcab\) はその生成集合にはない。このため \(L(A_2)\notin C_{2,c_\Sigma}\)（後者は有限言語の文法上の厳密な所属不成立）。これは**短い \(ab\) 語を作らずとも**二穴の代入可能性が崩れる例である。

**判定に使える帰結［条件付き］：** ある候補文法が \(p^M\) と一つの \(p^i\beta p^j\) を持つ一方、同じ \(n=i+j\) の他の \(p^h\beta p^{n-h}\) を禁止するなら、\(C_{2,c_\Sigma}\) には属さない。反例設計は \(\beta\) の全位置移送を受け入れる必要がある。しかしこれは \(c\) を含む語の位置を増やすだけで、\(c\)-free の短縮は与えない。トークンの障壁を破ってはいない。

## 5. 既存証明書の独立再生と収縮率

### 5.1 m=3 の7設計と未決3設計

\(A_0\to ab,\ A_i\to A_{i-1}A_{i-1}\mid e_i\) の \(m=3\) とし \(|W_3|=16\)。\(S=L(A_3)\) を**文法に従って完全列挙**し、前報 (155) に記録された各証明書 \((E,x,y,F)\) を全段、別実装の `goodstep` が三前提・成分ごとの内容・許容文脈を検査する。これらは**既存の具体的結果の再検証**であって、新しい広域探索の全数完了ではない。

| 逃げ道設計 \((e_1,e_2,e_3)\) | 一致の形（証明書依存） | 段数 | 強制長 | 短縮量 | 長さ比 |
|---|---|---:|---:|---:|---:|
| `(c,cc,ccc)` | `c` の連の重なり | 2 | 12 | 4 | 12/16 |
| `(c,ac,aac)` | 親の接頭 `a·c`、左側因子 | 1 | 13 | 3 | 13/16 |
| `(c,ca,caa)` | 親の接尾 `c·a`、右側因子 | 1 | 13 | 3 | 13/16 |
| `(c,cb,cbb)` | 親の接尾 `c·b`、位相 `b` | 1 | 13 | 3 | 13/16 |
| `(c,bc,bbc)` | 親の接頭 `b·c`、位相 `b` | 1 | 13 | 3 | 13/16 |
| `(c,cab,cabab)` | 接尾 `ab` ブロックの一致 | 1 | 14 | 2 | 14/16 |
| `(acb,accb,acccb)` | `c` の連と外枠の結合 | 2 | 14 | 2 | 14/16 |
| `(ac,cc,c)` | 多段、\(c\) 枠と `ab` 位相の再結合 | 6 | 14 | 2 | 14/16 |
| `(ca,bbc,abc)` | 多段、`b` 側の位相移動 | 7 | 13 | 3 | 13/16 |
| `(cc,ac,c)` | 多段、`cc` と `ac` をまたぐ結合 | 5 | 7 | 9 | 7/16 |

**各段の完全な証明書は付録Bに列挙**する。付録Aの `CASES` も同じ列をプログラムに直接読ませ、全段 `assert` に通ったことを付録Cの標準出力に示す。

**収縮量の注意：** m=3 の証明書を、固定の \(c\)-free 外側語 \(l,r\) で全て包むと、各 `SUB_d` の \(E,F\) を同じように \(l,r\) で包めば証明書は保たれる。穴の成分、型、内部固定区間の非空性は変わらない。短縮**量** \(\delta=|W|-|w|\) は不変だが、長さ比は
\[
 \frac{|l|+|w|+|r|}{|l|+|W|+|r|}
 =1-\frac{\delta}{|l|+|W|+|r|}.
\]
したがって m=4 への埋め込みで近道があることは証明できても、**全 m で一様な定数割合が縮む**とは主張しない。前報 (155) の m=4 の強制長28、29、29、29、29、30、30はこの特別な持ち上げである。

### 5.2 (149)(150) の全 n に対する記号的な2段証明書［既知・再確認］

\(n\ge3\)、\(i=n-1\)、\(U=(ab)^{2^i-2}\)、\(Z=abab\)、\(e=abc\)、\(\beta=a^icb\)、\(s=a\)。\(A_i\) の全倍増生成は \(UZ=(ab)^{2^i}\)、右端の \(A_1\) だけを \(abc\) に逃がした生成は \(Ue\)、\(A_i\) の直接の逃げ道は \(\beta\) である。ゆえに
\[
 \beta\beta,\ \beta Ue,\ UZUZ,\ UZUe\in L(A_n),
\]
かつ \(s\beta=a^ncb\in L(A_n)\)（\(A_n\) の直接の逃げ道）。前述の型PPの段1・段2を順番に適用すると
\[
 aUZ=a(ab)^{2^{n-1}}\in\operatorname{Cl}_{SUB_1}(L(A_n)).
\]
その長さは \(2^n+1\)、元の唯一の \(ab\) 語は \(|W_n|=2^{n+1}\)。短縮量 \(2^n-1\)、比は \(\tfrac12+2^{-(n+1)}\)。この結論は **\(L(A_n)\) を含む任意の代入可能言語**に成立し、\(L(A_n)\) 自身が代入可能という前提は置いていない。コードでは \(n=3,4,5,6,7,8\) の5種の所属を再帰的な完全所属判定で再検査した。

### 5.3 小さな反例 K の監査［証明済み］

\(K=\{abab,abc,cab,cc,ac\}\) について、**全ての**一穴・二穴出現を列挙し、前提を満たすが結論の欠けた `SUB₁` / `SUB₂` が0件だった。有限語集合の全出現について調べているので、打ち切り近似ではない。\(K\) は \(S\to BB\mid ac,\ B\to ab\mid c\) の有限 CFG であり、arity 1/2 条件を満たすので \(K\in C_{1,c_\Sigma}\cap C_{2,c_\Sigma}\)。\(\mu_{ab}(K)=4\)。

\(e_C=ac=a\cdot c\) は**生の因子一致**であるが、型Pの必要な \(\operatorname{cont}(a)=\operatorname{cont}(ab)\) は偽である。型PPの五前提、型Vの3種の種形、型Sの反例を生む禁止位置などの**完全な十分条件**は満たされない。`c` と `cc` がともに現れても型Rの**全前提**を持つわけではない。したがって「文字の一致らしきもの」を十分条件と呼ぶ分類は過大になる。

## 6. 課題B：侵入反鎖に対する条件付き多項式上界

### 定理6.1［条件付き・証明済み］`c` の出現数を制限する場合

全ての \(z\in L\) が \(|z|_c\le B\) を満たすと仮定する。このとき
\[
 q(T)\le B,\qquad
 \boxed{\mu_{ab}(L)\le3(r+1)v\theta(B+2)}.\tag{6.1}
\]

**証明。** \(T\) で最大の \(c\)-強制重い節点反鎖 \(Q\) を取り、\(|Q|=q(T)\) とする。各 \(u\in Q\) について、同じ非終端の短い生成 \(\omega_u\) を選ぶ。厚さ補題から \(|\omega_u|_1\le\theta\)、元の節点が重いので \(\omega_u\) は元の生成より短く、\(c\)-強制性の定義から必ずどれかの成分に \(c\) を含む。反鎖の節点は互いに祖先・子孫関係にないから、対応する部分木を**同時に** \(\omega_u\) の導出へ置き換えられる。good 文法の非削除性・線形性により、異なる \(u\) の生成文字が根の語内で占める位置は重ならず、どの短い生成の \(c\) も消されない。この結果は \(L\) の語で、少なくとも \(q(T)\) 個の \(c\) を含む。仮定より \(q(T)\le B\)。式 (0.1) に代入して (6.1) を得る。□

### 定理6.2［条件付き・証明済み］`c` の連数を制限する場合

全ての \(z\in L\) に現れる \(c\) の極大連（`c`-run）の数が高々 \(B\) と仮定すると
\[
 q(T)\le5B,\qquad
 \boxed{\mu_{ab}(L)\le3(r+1)v\theta(5B+2)}.\tag{6.2}
\]

**証明。** \(Q\) の各節点の生成の成分は、最短の \(W\) 内で高々2個の非空の互いに離れた区間を占める。反鎖なので異なる節点の全区間は重ならない。二つの節点の区間のどれかが \(W\) 内で隣接しているとき辺を張るグラフ \(H\) を作る。各節点は区間を高々2個持ち、各区間には左右2端点しかない。各端点に隣接する他節点の区間は高々1個なので次数は \(\le4\)。次数 \(\le4\) の有限グラフは、頂点を一つ選びその隣接頂点高々4個を削除する貪欲法で、\(|I|\ge\lceil|Q|/5\rceil\) の独立集合 \(I\) を持つ。

\(I\) の節点だけ、定理6.1と同じく \(c\) を含む短い生成へ交換する。隣接しない任意の別節点の区間の間には元の \(W\) の \(a\) または \(b\) が少なくとも一つ残り、その文字は \(I\) の交換では消えない。このため異なる \(I\) の節点から得られた \(c\) は同一の \(c\)-run に合体しない。生成された \(L\) の語には \(|I|\) 個以上の極大 \(c\)-run がある。よって \(B\ge|I|\ge q(T)/5\)、すなわち \(q(T)\le5B\)。式(0.1)を適用する。□

**限定と障壁との関係。** これらの定理は、外から与えられた言語の \(c\) 出現数／連数の**一様な上界**を使う。\(B\le\operatorname{poly}(v,\theta)\) なら所望の多項式評価になるが、一般の内容型付き代入可能言語にそのような \(B\) があるとは言えない。逃げ道を原子的なトークンとして扱う命題5の障壁は、**有限個の \(c\) 文字が実際に何回、どこに残るか**という追加条件を与えない。ここでは交換後の具体的な文字 `c` を数えることによって障壁を迂回しているが、一般の \(q\) 上界に昇格させていない。また定理6.2の独立集合手法は (153) 補題4の特殊化・直接の帰結であり、新規性を主張しない。

## 7. 課題C：候補族と却下証明書

| 候補 | 文法サイズ・\(\theta\) | 短い \(ab\) 語／反鎖 | `C₁`・`C₂` 条件 | 判定 |
|---|---|---|---|---|
| (149) \(A_i\to A_{i-1}A_{i-1}\mid a^icb\) | \(O(n^2)\) 以下の明示記述、\(\theta=O(n^2)\) | 唯一の \(ab\) 語が \((ab)^{2^n}\) | n=2で型Sの二穴違反、n≥3で型PPの2段近道 | **[証明済み：失格]** |
| m=3の7設計 | \(O(m\theta)\) の倍増文法表示 | 純 \(ab\) 語長16 | 全件 m=3で `SUB₁` 短縮証明書 | **[証明済み：失格]** |
| m=3の停止3設計 | 同上 | 純 \(ab\) 語長16 | 6、7、5段の `SUB₁` 短縮 | **[証明済み：失格]** |
| \(S_k\)（本報） | 有限3語の種集合 | 唯一の純 \(ab\) 種長 \(k+2\) | 全 arity で2段近道、種集合自体は `C₁` ですらない | **[証明済み：失格]** |
| \(K\) | 定数サイズの reduced good CFG | \(\mu_{ab}=4\) | `C₁∩C₂` に入る | **[証明済み：条件2失敗]** |
| `(c,cc,c)` の m=3 倍増**種** | 有限の倍増文法 | 純 \(ab\) 種長16 | 種集合の一段 `SUB` で未収録語が実際に生じる。閉包の終状態の議論と区別 | **[証明済み：提示した文法のままでは失格]** |

特に (153) の「17通りが closed」は**探索が閉包を追加して固定点に達した**意味であり、元の倍増文法が初めから代入可能という証明ではない。仮に最小閉包が有限で `C₁∩C₂` に入っても、それを生成する reduced good fan-out 2・ランク2・低 \(\theta\) の**小さい文法の存在**は別の条件である。今回、条件1–3を同時に満たす無限族は構成できなかった。

「全ての型を避ける逃げ道」という要求に対しては、局所的な型P/Rだけを避けても型V（純粋位相による二段短縮）や型S（二穴全位置移送）が残る。型Tの全てを排除する有限個の局所文字一致のリストは**未構成**である。

## 8. 何が完成し、どこが未解決か

### (i) 得られた結果の一覧

1. **[証明済み]** 種の全 \(c\)-free 語が同一長のとき、最初に**長さが変わる** \(c\)-free 語の証明書には `c` を含む共通文脈が必ずある（命題2.1）。ただし最終段とは限らない。
2. **[証明済み・本報の中心]** 無限個の \(S_k\) で、全 arity 一段短縮不能かつ二段で `ba` を強制する（定理3.1）。最終共通文脈は \(c\)-free、縮小率は \(2/(k+2)\)。
3. **[証明済み]** 二穴の周期ブロックによる逃げ道の**全内部位置への一段移送**（補題4.1）。元の (149) の `C₂` 障害を一般化した必要条件。
4. **[証明済み：再生確認]** (153)(155) の7+3設計の10証明書を別実装で全27段再生し、収縮量2、3、4、9を確認。\(L_n\) の一般の2段証明も記号的に再確認。
5. **[条件付き・証明済み]** \(|w|_c\le B\) なら \(q\le B\)；`c`-run 数 \(\le B\) なら \(q\le5B\)。\(B\) 多項式という追加仮定の下で \(\mu_{ab}\) が多項式。
6. **[未達]** 全ての局所文字一致を尽くす分類、一般の \(q\) 多項式上界、同時に条件1–3を満たす反例族は得られていない。`op:fanout-two` の解決は主張しない。

### (ii) 残った穴を一つの命題にまとめる

**未解決命題 Q（反鎖幅の一様な多項式境界）。** 各固定ランク \(r\ge2\) に対し多項式 \(P_r\in\mathbb R[X,Y]\) が存在し、任意の reduced good fan-out 2・ランク \(\le r\) 文法 \(G\) が \(L(G)\in C_{2,c_\Sigma}\) を生成し、\(\mu_{ab}(L(G))\) が定義されるなら、その最短語の最小節点数導出 \(T\) における \(c\)-強制重い節点の反鎖幅は
\[
 q(T)\le P_r(|V|,\bar\theta_G)
\]
を満たす。

肯定なら (0.1) から開始型 \(\{a,b\}\) の多項式上界が従う。しかしその先にも**二成分の各型付き非終端を含む全 \(\tau(G,c_\Sigma)\) への移行**が残る。否定の族が見つかっても、文法が生成する言語の `C₂` 所属と、その \(q\) が真に超多項式であることの双方が必要である。

### (iii) 次に試すべきこと（3件以内）

1. **型Vの位相衝突を倍増へ持ち上げる。** 逃げ道の位置を `p^M` に対してスロット移送で全位置に広げ、\(a^kW\) 型の \(c\)-free 伸長が必ず生まれるか／生まれない模型を構成する。伸長が生まれても短縮へ結び付く**因子一致**が別に必要。
2. **小さい閉包を小さい文法へ変換できるかを検査する。** `(c,cc,c)` から始めた `SUB₁,₂` 完全閉包について、最小文法の非終端数・規則厚さを同時に上から抑えられるか調べる。閉包の閉性と小文法性を混同しない。
3. **\(c\)-run を用いた反鎖の構造分解。** 定理6.2の独立な \(c\)-run を、型Sの位置移送で強制される多数の相異なる `c`-bridge と交差させ、\(B\) を仮定する代わりに `SUB` から \(q\le\operatorname{poly}_r(v,\theta)\) を導けるか検査する。

---

## 付録A. 実行した Python 3 スクリプト全文

- 標準ライブラリのみ、乱数・wall-time打ち切りなし。
- `implications(S,(1,2))` は指定の**有限種集合 S からの一段帰結だけ**を、全ての非空穴区間と非空の二穴中央について列挙する（全閉包の計算ではない）。`K` は全数の閉性判定、`S_k` は \(k=1,\ldots,8\) の一段の全数判定。後者の全 \(k\) については本文に**別途一般証明**がある。
- 探索部分は \(N\in\{4,5\}\)、\(W\in\{a,b\}^N\)、内容 \(\{a,b\}\) の因子 \(x\)、\(y\in\{a,b\}^{|x|+1}\cup\{a,b\}^{|x|+2}\)、8種の \(c\) 枠を順に走査し、最初の2段純 \(ab\) 型の発見で停止する。**1,361候補を検査したところで早期終了**。全空間の不在を証明していない。
- `CASES` 10件は前報 (155) に掲載された既存証明書の**再生**であって、新規な網羅探索ではない。各段の所属・成分内容・許容文脈を照合した。
- `L_n` の再帰的所属判定は \(n=3,\ldots,8\) に限る。全 \(n\) の証明は本文に与えた。

```python
from itertools import combinations
from collections import defaultdict
from functools import lru_cache

ALPH='abc'
def content(s): return frozenset(s)
def fill(context, parts):
    assert len(context)==len(parts)+1
    return ''.join(context[i]+parts[i] for i in range(len(parts)))+context[-1]
def occurrences(w,d):
    n=len(w)
    if d==1:
        for i in range(n):
            for j in range(i+1,n+1):
                yield (w[i:j],),(w[:i],w[j:])
    if d==2:
        for i in range(n):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    for l in range(k+1,n+1):
                        yield (w[i:j],w[k:l]),(w[:i],w[j:k],w[l:])
def implications(words,ds=(1,2)):
    known=set(words); dists=defaultdict(set); shared=defaultdict(set)
    for w in sorted(known):
        for d in ds:
            for x,e in occurrences(w,d):
                dists[x].add(e)
                shared[(d,tuple(content(t) for t in x),e)].add(x)
    res={}
    for (d,t,e), xs in sorted(shared.items(), key=lambda kv:str(kv[0])):
        if len(xs)<2:continue
        for x in sorted(xs):
            for y in sorted(xs):
                if x==y:continue
                for f in sorted(dists[x]):
                    z=fill(f,y)
                    if z not in known:
                        res.setdefault(z,(e,x,y,f))
    return res

def goodstep(s,e,x,y,f):
    assert len(x)==len(y)==len(e)-1==len(f)-1
    assert 1<=len(x)<=2
    assert all(xi and yi and content(xi)==content(yi) for xi,yi in zip(x,y))
    assert len(x)==1 or (e[1] and f[1])
    assert fill(e,x) in s,(e,x,y,f,'E[x]')
    assert fill(e,y) in s,(e,x,y,f,'E[y]')
    assert fill(f,x) in s,(e,x,y,f,'F[x]')
    return fill(f,y)

def language(es):
    x={'ab'}
    for e in es:
        x={u+v for u in x for v in x}|{e}
    return x

# Independently check user/provided archive statements about finite K and a new 2-step example.
K={'abab','abc','cab','cc','ac'}
rK=implications(K)
print('K size',len(K),'C2 implications',len(rK),'min-ab',min(len(x) for x in K if content(x)=={'a','b'}))

Sdeg=language(('c','cc','c'))
extra_deg=implications(Sdeg,(1,2))
assert extra_deg
print('degenerate m3 seeds',len(Sdeg),'missing one-step consequences',len(extra_deg),
      'first',sorted(extra_deg)[0])

# New parametric two-step case, and exhaustive *one-step* C_{2,c} check for k<=8.
for k in range(1,9):
    w='a'*k+'ba'; seeds={w,'c'+'a'*k+'b','c'+'a'*(2*k)+'b'}
    direct=implications(seeds,(1,2))
    assert not any(content(z)=={'a','b'} and len(z)<len(w) for z in direct)
    state=set(seeds)
    steps=[(('c',''),('a'*k+'b',),('a'*(2*k)+'b',),('','a')),
           (('a'*k,''),(w,),('ba',),('',''))]
    for step in steps:state.add(goodstep(state,*step))
    assert 'ba' in state
    print('S_k k',k,'N',len(w),'one-step-consequences',len(direct),'direct-shortcuts',0,
          'two-step-result','ba','ratio',f'2/{len(w)}')
    if k==2:
        for z,st in sorted(direct.items()):print('  direct-candidate',z,'step=',st)

# Two-hole slot transport (general result instantiated by the n=2 doubling grammar).
seeds=language(('abc','aacb'))
e=('','ab','');x=('ab','abab');y=('abab','ab');f=('','c','')
assert fill(e,x)==fill(e,y)=='abababab'
out=goodstep(seeds,e,x,y,f)
assert out=='ababcab' and out not in seeds
print('L2 slot transfer E[x]=E[y]=',fill(e,x),'F[x]=',fill(f,x),'F[y]=',out,'absent=',out not in seeds)

# Exact lifted symbolic two-step certificate, n=3,...,8.
for n in range(3,9):
    es=['abc' if i==1 else 'a'*i+'cb' for i in range(1,n+1)]
    u='ab'*(2**(n-1)-2); z='abab';beta='a'*(n-1)+'cb'; e='abc';s='a'
    seeds={beta+beta,beta+u+e,u+z+u+z,u+z+u+e,s+beta}
    # verify only explicitly required seeds using grammar exact membership with recursion, no exponential enumeration
    @lru_cache(None)
    def member(i,w):
        if i==0:return w=='ab'
        if w==es[i-1]:return True
        for t in range(1,len(w)):
            if member(i-1,w[:t]) and member(i-1,w[t:]):return True
        return False
    assert all(member(n,w) for w in seeds)
    steps=[((beta,''),(beta,),(u+e,),(s,'')),(('',e),(u+z+u,),(s+u,),('',z))]
    known=set(seeds)
    for ee,xx,yy,ff in steps:known.add(goodstep(known,ee,xx,yy,ff))
    target=s+u+z
    assert target in known
    print('L_n n',n,'N',2**(n+1),'result',len(target),'ratio',str(len(target))+'/'+str(2**(n+1)))

from itertools import product
alpha='ab'
seen=0;hits=[];both=0
for N in (4,5):
    for Wt in map(''.join,product(alpha,repeat=N)):
        if content(Wt)!={'a','b'}:continue
        for i in range(N):
            for j in range(i+1,N+1):
                orig=Wt[i:j];ty=content(orig)
                if ty!={'a','b'}:continue
                for m in (len(orig)+1,len(orig)+2):
                    for ytuple in product(alpha,repeat=m):
                        longer=''.join(ytuple)
                        if content(longer)!=ty:continue
                        for p,q in (('c',''),('','c'),('ca',''),('','ac'),('bc',''),('','cb'),('c','a'),('b','c')):
                            seeds={Wt,p+orig+q,p+longer+q}
                            if len(seeds)<3:continue
                            seen+=1
                            s1=implications(seeds,(1,))
                            if any(content(z)=={'a','b'} and len(z)<N for z in s1):continue
                            # all one-step consequences with length <=N+5
                            mids={z for z in s1 if len(z)<=N+5}
                            S2=seeds|mids
                            s2=implications(S2,(1,))
                            for z,cert in s2.items():
                                if content(z)=={'a','b'} and len(z)<N and 'c' not in ''.join(cert[0]):
                                    hits.append((Wt,orig,longer,p,q,z,cert,len(s1)))
                                    print('FOUND',hits[-1]);break
                            if hits:break
                        if hits:break
                    if hits:break
                if hits:break
            if hits:break
        if hits:break
    if hits:break
print('EXP search checked=',seen,'hits=',len(hits))

# Replay ten concrete archived certificates, without importing their previous solver.
# Each entry is (case name, (e1,e2,e3), explicit E/x/y/F steps).
CASES = [
 ('c^i',('c','cc','ccc'), [
  (('','cc'),('cc',),('c',),('abababab','')),
  (('','abababc'),('ababab',),('ab',),('','ababababab'))]),
 ('a^(i-1)c',('c','ac','aac'), [
  (('','c'),('abababababab',),('ababababa',),('','abab'))]),
 ('ca^(i-1)',('c','ca','caa'), [
  (('c',''),('abababababab',),('aabababab',),('','abab'))]),
 ('cb^(i-1)',('c','cb','cbb'), [
  (('c',''),('abababababab',),('babababab',),('','abab'))]),
 ('b^(i-1)c',('c','bc','bbc'), [
  (('','bc'),('abababababa',),('abababab',),('','babab'))]),
 ('c(ab)^(i-1)',('c','cab','cabab'), [
  (('ababababc',''),('abab',),('ab',),('','abababababab'))]),
 ('ac^ib',('acb','accb','acccb'), [
  (('ac',''),('cbabababab',),('bababababacb',),('ababa','')),
  (('','abababababacb'),('abab',),('ab',),('','abababababab'))]),
 ('priority ac,cc,c',('ac','cc','c'), [
  (('',''),('c',),('cccc',),('ababa','abababab')),
  (('',''),('ccabababab',),('ababacacac',),('ababacc','')),
  (('','c'),('ababababaca',),('ababacc',),('','bab')),
  (('',''),('c',),('cccc',),('ababa','acac')),
  (('',''),('ababaccc',),('ababaccbab',),('','cacac')),
  (('ababacc','cacac'),('ababa',),('bab',),('','bababababab'))]),
 ('priority ca,bbc,abc',('ca','bbc','abc'), [
  (('',''),('abc',),('ababababbbc',),('bbcab','a')),
  (('',''),('abc',),('caababbbc',),('bbcab','a')),
  (('','ababbbca'),('bbcababab',),('bbcabca',),('','ab')),
  (('',''),('abc',),('bbcabababab',),('bbc','aab')),
  (('','c'),('ab',),('ababababbb',),('bbcca','ab')),
  (('','abab'),('caabababab',),('bbcabab',),('bbc','bbab')),
  (('bbcbbc','ab'),('ababababa',),('ababbb',),('','bababab'))]),
 ('priority cc,ac,c',('cc','ac','c'), [
  (('abab',''),('ababababcc',),('ababac',),('','cc')),
  (('',''),('c',),('cccccccc',),('abab','cac')),
  (('',''),('ababcccccc',),('ababababac',),('','cccac')),
  (('',''),('ababaccc',),('ababababac',),('abab','cac')),
  (('','ccac'),('ababababababa',),('abab',),('','bab'))]),
]
for name,es,steps in CASES:
    known=language(es)
    for i,step in enumerate(steps,1):
        z=goodstep(known,*step)
        known.add(z)
    assert content(z)=={'a','b'} and len(z)<16
    finale=steps[-1]
    e_has_c=('c' in ''.join(finale[0]))
    print('ARCHIVED',name,'steps',len(steps),'result',z,'length',len(z),'saved',16-len(z),
          'last-E-has-c',e_has_c)
```

## 付録B. 10件の段別、完全な再生用証明書

以下は `CASES` の全段を、順に既知語集合へ追加しながら表示したもの。各行で `E[x]`, `E[y]`, `F[x]` はその段の開始時点で存在する。`F[y]` がその段で新しく追加される。成分ごとの内容一致および内部の非空条件も付録Aの `goodstep` が検査する。最終語はいずれも内容 `{a,b}` で、長さ16未満である。

### `c^i` — escapes `('c', 'cc', 'ccc')`

| 段 | E | x → y | F | E[x] / E[y] / F[x] → F[y] |
|---:|---|---|---|---|
| 1 | `(;cc)` | `(cc)` → `(c)` | `(abababab;)` | `cccc` / `ccc` / `ababababcc` → **`ababababc`** |
| 2 | `(;abababc)` | `(ababab)` → `(ab)` | `(;ababababab)` | `ababababababc` / `ababababc` / `abababababababab` → **`abababababab`** |

### `a^(i-1)c` — escapes `('c', 'ac', 'aac')`

| 段 | E | x → y | F | E[x] / E[y] / F[x] → F[y] |
|---:|---|---|---|---|
| 1 | `(;c)` | `(abababababab)` → `(ababababa)` | `(;abab)` | `ababababababc` / `ababababac` / `abababababababab` → **`ababababaabab`** |

### `ca^(i-1)` — escapes `('c', 'ca', 'caa')`

| 段 | E | x → y | F | E[x] / E[y] / F[x] → F[y] |
|---:|---|---|---|---|
| 1 | `(c;)` | `(abababababab)` → `(aabababab)` | `(;abab)` | `cabababababab` / `caabababab` / `abababababababab` → **`aabababababab`** |

### `cb^(i-1)` — escapes `('c', 'cb', 'cbb')`

| 段 | E | x → y | F | E[x] / E[y] / F[x] → F[y] |
|---:|---|---|---|---|
| 1 | `(c;)` | `(abababababab)` → `(babababab)` | `(;abab)` | `cabababababab` / `cbabababab` / `abababababababab` → **`babababababab`** |

### `b^(i-1)c` — escapes `('c', 'bc', 'bbc')`

| 段 | E | x → y | F | E[x] / E[y] / F[x] → F[y] |
|---:|---|---|---|---|
| 1 | `(;bc)` | `(abababababa)` → `(abababab)` | `(;babab)` | `ababababababc` / `ababababbc` / `abababababababab` → **`ababababbabab`** |

### `c(ab)^(i-1)` — escapes `('c', 'cab', 'cabab')`

| 段 | E | x → y | F | E[x] / E[y] / F[x] → F[y] |
|---:|---|---|---|---|
| 1 | `(ababababc;)` | `(abab)` → `(ab)` | `(;abababababab)` | `ababababcabab` / `ababababcab` / `abababababababab` → **`ababababababab`** |

### `ac^ib` — escapes `('acb', 'accb', 'acccb')`

| 段 | E | x → y | F | E[x] / E[y] / F[x] → F[y] |
|---:|---|---|---|---|
| 1 | `(ac;)` | `(cbabababab)` → `(bababababacb)` | `(ababa;)` | `accbabababab` / `acbababababacb` / `ababacbabababab` → **`abababababababacb`** |
| 2 | `(;abababababacb)` | `(abab)` → `(ab)` | `(;abababababab)` | `abababababababacb` / `ababababababacb` / `abababababababab` → **`ababababababab`** |

### `priority ac,cc,c` — escapes `('ac', 'cc', 'c')`

| 段 | E | x → y | F | E[x] / E[y] / F[x] → F[y] |
|---:|---|---|---|---|
| 1 | `(;)` | `(c)` → `(cccc)` | `(ababa;abababab)` | `c` / `cccc` / `ababacabababab` → **`ababaccccabababab`** |
| 2 | `(;)` | `(ccabababab)` → `(ababacacac)` | `(ababacc;)` | `ccabababab` / `ababacacac` / `ababaccccabababab` → **`ababaccababacacac`** |
| 3 | `(;c)` | `(ababababaca)` → `(ababacc)` | `(;bab)` | `ababababacac` / `ababaccc` / `ababababacabab` → **`ababaccbab`** |
| 4 | `(;)` | `(c)` → `(cccc)` | `(ababa;acac)` | `c` / `cccc` / `ababacacac` → **`ababaccccacac`** |
| 5 | `(;)` | `(ababaccc)` → `(ababaccbab)` | `(;cacac)` | `ababaccc` / `ababaccbab` / `ababaccccacac` → **`ababaccbabcacac`** |
| 6 | `(ababacc;cacac)` | `(ababa)` → `(bab)` | `(;bababababab)` | `ababaccababacacac` / `ababaccbabcacac` / `abababababababab` → **`babbababababab`** |

### `priority ca,bbc,abc` — escapes `('ca', 'bbc', 'abc')`

| 段 | E | x → y | F | E[x] / E[y] / F[x] → F[y] |
|---:|---|---|---|---|
| 1 | `(;)` | `(abc)` → `(ababababbbc)` | `(bbcab;a)` | `abc` / `ababababbbc` / `bbcababca` → **`bbcabababababbbca`** |
| 2 | `(;)` | `(abc)` → `(caababbbc)` | `(bbcab;a)` | `abc` / `caababbbc` / `bbcababca` → **`bbcabcaababbbca`** |
| 3 | `(;ababbbca)` | `(bbcababab)` → `(bbcabca)` | `(;ab)` | `bbcabababababbbca` / `bbcabcaababbbca` / `bbcabababab` → **`bbcabcaab`** |
| 4 | `(;)` | `(abc)` → `(bbcabababab)` | `(bbc;aab)` | `abc` / `bbcabababab` / `bbcabcaab` → **`bbcbbcababababaab`** |
| 5 | `(;c)` | `(ab)` → `(ababababbb)` | `(bbcca;ab)` | `abc` / `ababababbbc` / `bbccaabab` → **`bbccaababababbbab`** |
| 6 | `(;abab)` | `(caabababab)` → `(bbcabab)` | `(bbc;bbab)` | `caabababababab` / `bbcabababab` / `bbccaababababbbab` → **`bbcbbcababbbab`** |
| 7 | `(bbcbbc;ab)` | `(ababababa)` → `(ababbb)` | `(;bababab)` | `bbcbbcababababaab` / `bbcbbcababbbab` / `abababababababab` → **`ababbbbababab`** |

### `priority cc,ac,c` — escapes `('cc', 'ac', 'c')`

| 段 | E | x → y | F | E[x] / E[y] / F[x] → F[y] |
|---:|---|---|---|---|
| 1 | `(abab;)` | `(ababababcc)` → `(ababac)` | `(;cc)` | `ababababababcc` / `ababababac` / `ababababcccc` → **`ababaccc`** |
| 2 | `(;)` | `(c)` → `(cccccccc)` | `(abab;cac)` | `c` / `cccccccc` / `ababccac` → **`ababcccccccccac`** |
| 3 | `(;)` | `(ababcccccc)` → `(ababababac)` | `(;cccac)` | `ababcccccc` / `ababababac` / `ababcccccccccac` → **`ababababaccccac`** |
| 4 | `(;)` | `(ababaccc)` → `(ababababac)` | `(abab;cac)` | `ababaccc` / `ababababac` / `ababababaccccac` → **`ababababababaccac`** |
| 5 | `(;ccac)` | `(ababababababa)` → `(abab)` | `(;bab)` | `ababababababaccac` / `ababccac` / `abababababababab` → **`ababbab`** |

## 付録C. 標準出力（実行結果を無変更で採録）

実行コマンド：`python3 chatgpt_shortcut_classification_2026-11-06.py`。本環境での実測約2.2秒（環境依存）。`S_k` の一段帰結は各 `k` で入力3語のすべての出現から列挙し、数値は重複を除いた帰結語数。`EXP search` は最初の発見で終了し、総当たり完了ではない。

```text
K size 5 C2 implications 0 min-ab 4
degenerate m3 seeds 17 missing one-step consequences 33 first ababababababcccc
S_k k 1 N 3 one-step-consequences 3 direct-shortcuts 0 two-step-result ba ratio 2/3
S_k k 2 N 4 one-step-consequences 4 direct-shortcuts 0 two-step-result ba ratio 2/4
  direct-candidate aaaaba step= (('c', ''), ('aab',), ('aaaab',), ('', 'a'))
  direct-candidate aabaaa step= (('c', 'ab'), ('a',), ('aaa',), ('aab', ''))
  direct-candidate abaa step= (('c', 'a', 'b'), ('aa', 'a'), ('a', 'aa'), ('', 'b', ''))
  direct-candidate caaaaaab step= (('c', ''), ('aab',), ('aaaab',), ('caa', ''))
S_k k 3 N 5 one-step-consequences 7 direct-shortcuts 0 two-step-result ba ratio 2/5
S_k k 4 N 6 one-step-consequences 10 direct-shortcuts 0 two-step-result ba ratio 2/6
S_k k 5 N 7 one-step-consequences 13 direct-shortcuts 0 two-step-result ba ratio 2/7
S_k k 6 N 8 one-step-consequences 16 direct-shortcuts 0 two-step-result ba ratio 2/8
S_k k 7 N 9 one-step-consequences 19 direct-shortcuts 0 two-step-result ba ratio 2/9
S_k k 8 N 10 one-step-consequences 22 direct-shortcuts 0 two-step-result ba ratio 2/10
L2 slot transfer E[x]=E[y]= abababab F[x]= abcabab F[y]= ababcab absent= True
L_n n 3 N 16 result 9 ratio 9/16
L_n n 4 N 32 result 17 ratio 17/32
L_n n 5 N 64 result 33 ratio 33/64
L_n n 6 N 128 result 65 ratio 65/128
L_n n 7 N 256 result 129 ratio 129/256
L_n n 8 N 512 result 257 ratio 257/512
FOUND ('aaba', 'aab', 'aaaab', 'c', '', 'ba', (('aa', ''), ('aaba',), ('ba',), ('', '')), 3)
EXP search checked= 1361 hits= 1
ARCHIVED c^i steps 2 result abababababab length 12 saved 4 last-E-has-c True
ARCHIVED a^(i-1)c steps 1 result ababababaabab length 13 saved 3 last-E-has-c True
ARCHIVED ca^(i-1) steps 1 result aabababababab length 13 saved 3 last-E-has-c True
ARCHIVED cb^(i-1) steps 1 result babababababab length 13 saved 3 last-E-has-c True
ARCHIVED b^(i-1)c steps 1 result ababababbabab length 13 saved 3 last-E-has-c True
ARCHIVED c(ab)^(i-1) steps 1 result ababababababab length 14 saved 2 last-E-has-c True
ARCHIVED ac^ib steps 2 result ababababababab length 14 saved 2 last-E-has-c True
ARCHIVED priority ac,cc,c steps 6 result babbababababab length 14 saved 2 last-E-has-c True
ARCHIVED priority ca,bbc,abc steps 7 result ababbbbababab length 13 saved 3 last-E-has-c True
ARCHIVED priority cc,ac,c steps 5 result ababbab length 7 saved 9 last-E-has-c True
```

## 付録D. 検査の限界と採用判断

**[証明済み]** 付録Aの有限計算は、提示された種からの `SUB₁`/`SUB₂` の一段全列挙と、指定した証明書の有限段再生について完全である。`K` の閉性は有限集合全体で判定した。`S_k` の全 `k` での一段不能性は計算ではなく定理3.1の一般証明に依存する。

**[未証明]** 任意の長さの種の `SUB` 閉包の完備計算、全ての文字位置一致の有限型分類、深い倍増の一般反例排除、一般の `q` 上界、一般の `τ` 上界、反例の文法サイズと所属条件の同時達成。今回の有限の計算結果からこれらを外挿しない。
