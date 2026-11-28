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
