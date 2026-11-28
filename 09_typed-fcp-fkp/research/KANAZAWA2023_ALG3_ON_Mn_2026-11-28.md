# Kanazawa (WoLLIC 2023) の Algorithm 3 は $M_n$ で指数的に長いデータを要するか（Claude、2026-11-28）

著者がアップロードした著者稿（16 頁）の全文を読んで確かめた。頁は著者稿のもの。**結論：要する。** 命題 5.5 の論法は Algorithm 3 にそのまま通る。しかも演算に正則演算を含めると、目標の文法は小さく（短い原子だけで）書けるので、長いデータは文法の大きさでは説明できない。人間による検証、計算機での検証はまだ。

## Algorithm 3（p.11–13）の要点

- パラメータ $r,s,k$、演算の集合 $\Gamma\ni\cap$。非終端記号は、質問原子 $(u,v)/$（$\llbracket(u,v)/\rrbracket=u\backslash L_*/v$）から $\Gamma$ の演算を高々 $k$ 回使ったガード付きの式。$N_i=E_k(Q^{r,s}(J_i,E_i),\Gamma)$、初期記号は $(\varepsilon,\varepsilon)/$。
- $E_i=\bigcup_{j\le i}\mathrm{Sub}(t_j)$。$J_i$ は $T_i\not\subseteq L(G_{i-1})$ のときだけ $\mathrm{Con}(T_i)$ に置き直し、それ以外は据え置き。
- $Q^{r,s}(J,E)$：$(u_1,u_2)\in J$ を、$\prec_2$ で小さいどの $(v_1,v_2)\in J$ とも $\Sigma^{\le s}(E\Sigma^{\le s})^{\le r}$ 上で商が異なるときに残す（観測で同値な原子の重複を除く）。
- 生成規則 $A\to w_0B_1w_1\cdots B_nw_n$（$n\le r$、$|w_j|\le s$）を、$\llbracket A\rrbracket\supseteq w_0(E\cap\llbracket B_1\rrbracket)w_1\cdots(E\cap\llbracket B_n\rrbracket)w_n$ のとき採る（$E=E_i$、所属は質問で判定）。

## 主張

$n\ge2$、$\Gamma\ni\cap$、$r\ge2$、$s\ge1$、$k\ge1$ とする。Algorithm 3 が $M_n$ のある正の提示で段階 $i$ に収束する（$G_l=G_i$、$l\ge i$）なら、$w^*_{n-1}$ は $T_i$ のある語の因子である。とくに長さ $3\cdot2^{n-1}-2$ 以上のデータがある。

## 証明

1. $M_n$ は有限なので、ある段階 $l\ge i$ で $E_l=\mathrm{Sub}(M_n)$ となる。$G_l=G_i$ は正しい（定理 7）ので、$i$ 以後に $J$ の置き直しはなく $J_l=J_i$。
2. $E_l=\mathrm{Sub}(M_n)$ のとき、$\Sigma^{\le s}(E_l\Sigma^{\le s})^{\le r}\supseteq\mathrm{Sub}(M_n)$ はどの商も含むので、観測での同値は真の同値に一致する。よって $Q^{r,s}(J_l,E_l)$ は、$J_l$ の各商の類の $\prec_2$ で最小の代表を含む。同じ理由で、$P_l$ の生成規則はすべて真に妥当である（$\llbracket B\rrbracket\subseteq\mathrm{Sub}(M_n)=E_l$）。
3. $J_l=\mathrm{Con}(T_t)$（$t$ は最後の置き直しの段階）で、$T_t$ は $M_n$ の語 $m$ を含む。命題 5.5 の証明と同じく、$m=\lceil y\rceil$ なら $(\lceil,\rceil)$、$m=\lfloor yy'\rfloor$ で $y'$ が標識を持てば $(\lfloor,y'\rfloor)$、$y$ が標識を持てば $(\lfloor y,\rfloor)$ が $\mathrm{Con}(T_t)$ にあり、その商は $M_n$ に相対的に $L(G_n,E_{n-1})$ である。よって商が $L(G_n,E_{n-1})$ の原子 $e$ が $N_l$ にある。$(\varepsilon,\varepsilon)/$ も $N_l$ にある（$\prec_2$ で最小）。
4. 候補 $(\varepsilon,\varepsilon)/\to\lfloor\,e\,e\,\rfloor$（$n=2\le r$、$|w_j|\le1\le s$）は妥当でない：$w^*_n=\lfloor w^*_{n-1}w^*_{n-1}\rfloor\notin M_n$。よって $P_l$ にない。$G_i=G_l$ なので $P_i$ にもない。
5. $P_i$ にないのは、$x_1,x_2\in E_i\cap L(G_n,E_{n-1})$ で $\lfloor x_1x_2\rfloor\notin M_n$ となるものがあるときに限る。$\lfloor x_1x_2\rfloor\in L_n$ なので、これは $x_1=x_2=w^*_{n-1}$ のとき、そのときだけ。よって $w^*_{n-1}\in E_i=\mathrm{Sub}(T_i)$。∎

命題 5.5 の型なしの場合と同じ論法である。違いは、KY2017 の双対学習器の文脈の集合が、Algorithm 3 では重複を除いた原子の集合になることだけで、商の類の代表が残るので影響しない。

## 目標の文法は小さい（$\Gamma$ が拡張正則の演算のとき）

$\Gamma$ を Kanazawa の (iii)（ブール演算、$\emptyset,\varepsilon,a$、連接、スター）とする。$c_i=(\lceil^{n-i},\rceil^{n-i})$ とし、$H_n$（命題 4.2(b)、型を名前として読む）に

- $(E_i,1)\mapsto c_i/$、$(E_i,\zeta)\mapsto c_i/\cap(\overline{\emptyset}\,\lceil\,\overline{\emptyset})$（$i<n$）、$(E_n,\zeta)\mapsto(\varepsilon,\varepsilon)/$

を与える。$M_n$ に相対的に、それぞれ $L(G_n,E_i)$、$L(G_n,E_i)$ の標識を持つ語、$M_n$ を表す。これは、定理 6.11 の後の段落の二つの枠の SPP と同じ集合族で、長い文脈 $(p_i,q_i)$ を正則な集合 $\Sigma^*\lceil\Sigma^*$ に置き換えたものである。式はガード付き（$c_i/$ が先頭）で、演算は高々 8 回。よって $M_n$ は、非終端記号 $2n$、$r=2$、$s=1$、原子の長さ $\le2n$ の、拡張正則閉包性を持つ文法を持つ。原子はどれも $\mathrm{Con}(u_n)$ に入る（$u_n=\lceil^n a\rceil^n$、長さ $2n+1$）。$r\ge2$、$s\ge1$、$k\ge8$ なら定理 8 により Algorithm 3 は $M_n$ に収束する。それでも主張により、収束するどの実行も長さ $3\cdot2^{n-1}-2$ 以上の語を見ている。

本稿の序論の一文（型付きの文脈集合は KY2023 の拡張正則閉包に入る）の具体例にあたる。

## (d†′) との関係

- Kanazawa（p.15）は、$Q_*\subseteq\mathrm{Con}(D)$ となる最小の $D$ について $|D|\le k|N_*|$ としたうえで、$D$ には表現の大きさについて指数的に長い語がありうると注意し、そのあとに収束までの性質 (d†′) を入れ子の形で述べている。(d†′) は追加の集合 $D'$、$D''$ と語 $t$ の**個数**を抑えるが、**長さ**は抑えない。
- $M_n$（上の文法の原子の選び方による）では、原子 $Q_*$ を集めるには短い語 $u_n$ 一つで足りる。指数的に長い語は、妥当でない生成規則を除くための例（Kanazawa の Case 1 の後半、(d†′) の $D'$ または $D''$）として要る。したがって、**$D$ の語が短くても、(d†′) の追加の例の長さは目標の文法の表現の大きさの多項式では抑えられない**。Kanazawa の論文は、この長さを抑えられるかどうかについては何も述べていない。
- $\Gamma=\{\cap\}$ のときは、$k$ 個以下の原子の共通部分による SPP は $(k)$-文脈の提示そのものなので、定理 6.11 により $M_n$ のどの文法も全長 $2^{n/2}$ 以上を持ち、長いデータは文法の大きさで説明できる。ブール演算だけ（正則演算なし）で短い文法が書けるかは確かめていない。

## 本稿への反映の候補

命題 5.5 の後の一文（現状は「関連する双対学習器について Kanazawa は…と注意しており、ここでは $\mathrm{Dual}^{s_U}_{r,k}$ についてそれが避けられない」）を、「命題 5.5 の証明はそのまま Kanazawa (2023) の Algorithm 3 にも通り（$\Gamma\ni\cap$、$r\ge2$、$s\ge1$）、拡張正則の演算のもとでは $M_n$ は長さ $2n$ 以下の原子だけの文法を持つので、(d†′) の追加の例の長さは目標の文法の大きさの多項式では抑えられない」という趣旨に強める。著者の判断待ち。反映するなら、Algorithm 3 の定義に依存する主張なので、独立の検証（Astra または ChatGPT）を勧める。

## 追記：ChatGPT の独立検証（2026-11-28）と修正

検証：`external_review_2026-11-28_chatgpt_alg3/`（依頼文 `PROMPT.md`、`review.md`、`findings.csv`、`checks/check_mn.py`。Claude が `python3 -I` で再実行し、$n=2,3,4$ で全件 PASS を確認）。総合判定は「局所的な修正で正しい」。主張 1（下界）と主張 2（小さな文法）は独立に再構成され、反例なし。指摘と対応：

- **K01（gap）原子の正規化**：Kanazawa（p.13）は $Q_*$ の原子を $\prec_2$ で最小の代表に取り替えてよいとする。$\lceil$ が $\lfloor$ より前の順序なら代表は $c_i$ のままで $D=\{u_n\}$（長さ $2n+1$）。$\lfloor$ が前なら代表は $(\lfloor^{n-i},\,u_i\rfloor u_{i+1}\rfloor\cdots u_{n-1}\rfloor)$ で、すべて左端の背骨の語 $z=\lfloor^n a\,u_0\rfloor u_1\rfloor\cdots u_{n-1}\rfloor$（長さ $(n+1)^2$）の文脈に入る。どちらの順序でも原子は長さ $(n+1)^2$ 以下の一語に現れる。上の本文の「原子はどれも $\mathrm{Con}(u_n)$ に入る」は順序によっては偽なので、この形に改める。
- **K04（gap）長い例の場所**：長い例が $D'$ か $D''$ のどちらかにあるとは言えない。言えるのは「$D'\cup\{t\}\cup D''$ のどれかの語が長い」、すなわち (d†′) の追加の例の長さをすべて多項式で抑えることはできない、まで。
- **K05（minor）尺度**：下界は $n$ について $2^{\Omega(n)}$、目標の文法の明示的な大きさ（多項式）について超多項式。「表現の大きさについて指数的」とは言わない。
- **K03（minor）**：$k=8$ は短い原子の証人の上界で、最小の $k$ とは限らない。定理 8 の証明は与えた証人が $E_k$ に入ることだけを使う。
- **K02（minor）**：$(E_0,1)$ にも $c_0/$ を明示する。
- **K06（minor）**：共通部分だけの式で演算 $k$ 回なら原子は $k+1$ 個。上の「$(k)$-文脈の提示」は「$(k+1)$-文脈の提示」に。定理 6.11 の結論には影響なし。

**ブール演算だけの場合（ChatGPT の追加の結果、未検証）**：$F_n$ は共通部分閉包性を持ち原子は短いが規則は指数個。さらに、ブール閉包性の任意の SPP について、原子の長さの上界を $\ell$ とすると $2(\ell+1)\sum|\alpha|\ge2^{n-1}$（定理 6.11 の数え上げを、二語を区別する原子の存在に置き換えて拡張）。正しければ、短い原子と小さな文法を両立させるのは正則演算（連接）であることになる。本文には入れていない。入れるなら別途検証が要る。

## 原稿への反映（英日とも、2026-11-28）

命題 5.5 の直後の文を、ChatGPT の文案をもとに K01・K04・K05 を反映して書き換えた：$\mathrm{Dual}^{s_U}_{r,k}$ は $H_n$ の全長が $O(n^2)$ でも長いデータを要する。同じ論法は Algorithm 3（演算に共通部分を含み、$r\ge2$、$s\ge1$）に通る。拡張正則の演算のもとで $H_n$ は $\{c_i\}^\lhd$ と $\{c_i\}^\lhd\cap\Gamma^*\lceil\Gamma^*$ による SPP を持ち、Kanazawa の正規化のあとでも原子は長さ $(n+1)^2$ 以下の一語に現れる。よって (d†′) は追加の例の個数を抑えるが、その長さまで目標の文法の大きさの多項式で抑えることはできない。英語版 23 頁、日本語版 26 頁。

## 追記：ブール演算だけの場合の主張の検証（Claude、2026-11-28）

**主張（ChatGPT の T4）。** $M_n$ の CFG $G$ が、各成分が質問原子 $(u,v)/$（$M_n$ に相対的な商 $u\backslash M_n/v=\{(u,v)\}^\lhd$）のブール結合で表される SPP を持ち、現れる原子の長さ $|u|+|v|$ が $\ell$ 以下なら、$2(\ell+1)\sum_{A\to\alpha}|\alpha|\ge2^{n-1}$。

**判定：正しい。** 定理 6.11（`thm:frame-total`）の $j=1$ の場合の不等式 $(\ell+1)\sum|\alpha|\ge2^{n-2}$ と同じもので、証明もほとんどそのまま通る。より一般に、どの $1\le j<n$ についても $(3\cdot2^{j-1}-1)(\ell+1)\sum|\alpha|\ge2^{n-j}$。

**理由。** 定理 6.11 の証明で枠を使うのは補題 6.9（`lem:marked-node`）の一か所だけで、そこでは「$x$ は $A$ の成分に入り、$x'$（$x$ の中の $v_j$ を $w^*_j$ に置き換えた語）は入らないので、ある $c\in C_A$ が $x$ を受理し $x'$ を拒否する」を使う。ブール結合の場合はこう置き換わる。

1. $x\in L(G,A)\subseteq X_A$。$x'\in X_A$ なら、前不動点の性質（補題 2.2 `lem:reach`）で $w^*_n=px'q\in X_S\subseteq M_n$ となり矛盾。よって $x'\notin X_A$。ここまでは成分の形によらない。
2. $X_A$ は原子への所属の真理値のブール関数なので、$x$ と $x'$ の所属が違う原子 $c$ が少なくとも一つある。
3. 向きは一つに決まる：$c[x']\in M_n$ なら、$x'$ の中の $w^*_j$ の出現は $E_j$-節点で（補題 4.1）、これを $v_j$ に戻した $c[x]$ も $L_n$ に入り標識を持つので $M_n$ に入る。よって $c$ は $x$ を受理し $x'$ を拒否する。
4. 以下は補題 6.9 の証明と同じ：$c[x']\in L_n\setminus M_n$ なので $c[x']=w^*_n$、よって $|p|+|q|=|c|\le\ell$。定理 6.11 の数え上げ（補題 6.10 の混合）は文法と補題 6.9 の結論しか使わないので、そのまま通る。

**拡張正則の演算では通らない理由。** 手順 2 は、成分への所属が $x$ 自身の商への所属だけで決まることを使う。連接やスターを含む式（例 $\Gamma^*\lceil\Gamma^*$）では所属が $x$ の部分語についての質問で決まる（Kanazawa の性質 (∗)）ので、$x$ と $x'$ を区別する原子が短くてよい。実際、主張 2 の文法では原子の長さは $O(n^2)$ 以下。

**整理。** $M_n$ について、
- 共通部分だけ（$\Gamma=\{\cap\}$、very weak FCP）：$F_n$（原子は短いが規則は指数個）、または二つの枠の $H_n$（規則は $O(n)$ だが文脈の長さ $3\cdot2^n-6$）。どれも $(\ell+1)\sum|\alpha|\ge2^{n-2}$。
- ブール演算：同じ下界が成り立つ。$H_n$ の規則のままなら、$(E_1,\zeta)$ の成分が $\lceil a\rceil$ を含み $\lfloor aa\rfloor$ を含まないので、二つを区別する原子の長さは $|w^*_n|-4=3\cdot2^n-6$ 以上要る。
- 拡張正則の演算：規則 $O(n)$、原子は正規化後も長さ $(n+1)^2$ 以下の一語の文脈に入る。
- それでも Algorithm 3 は、どの $\Gamma\ni\cap$ でも、収束までに長さ $3\cdot2^{n-1}-2$ 以上のデータを要する（主張 1）。

短い原子と小さな文法を両立させているのは正則演算（連接）であり、データの長さの下界は演算の選び方によらない。

**原稿への反映**（2026-11-28、著者の指示で反映、英日とも）：定理 6.11 の後の「因子 $\ell+1$ は除けない」段落の末尾に、次の趣旨の一文を加えた（最初の案）。"Only Lemma 6.9 uses the frames, through a context that separates $x$ from $x'$; so Theorem 6.11 holds verbatim when the components are Boolean combinations of sets $\{c\}^\lhd$ with $|c|\le\ell$, but not for the extended regular operations, under which $H_n$ needs only short atoms (Section 5)."

反映した英文："The proof of Lemma 6.9 uses the frames only through a context separating $x$ from $x'$, so Theorem 6.11 holds verbatim when the components are Boolean combinations of sets $\{c\}^\lhd$ with $|c|\le\ell$ (by Lemma 4.1 a separating $c$ accepts $x$), but not for the extended regular operations, under which $H_n$ needs only short atoms (Section 5)." 23 頁を保つため、参考文献の KY2017・Leiß・Clark–Yoshinaka・Selkirk の書誌を略記した（LNCS、編者名の省略、出版地の省略）。英語版 23 頁、日本語版 26 頁。
