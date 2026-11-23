# 方向A：R16 の検証と仕上げ（Claude, 2026-11-23）

**対象**：R16（Astra）`R16_astra_unified_decoration_2026-11-23.zip`（report.md、unified_theorem.tex、code/）と、R14 の $L^{\mathsf G}$・$E_{\rm ev}$ の定理。
**担当**：Claude Opus 5.5。R14・R16 を書いた Astra（OpenAI 系）とは別の系列による確認です。ただし定理L の原証明は Claude の第四段なので、定理L そのものについては独立ではありません。
**ラベル**：[VALID（確認）] は本メモで手で確かめたもの。[文献] は原典または二次文献の記述によるもの。[導出] は文献の定理を組み合わせて本メモで導いたもの（原典で要照合）。

---

## 0. 結論

1. **課題2：$\mathcal W=\mathbf{SL}*\mathbf{LG}$ は、ちょうど $\mathbf{L}\,\mathbf{ECom}$（すべての局所モノイドで冪等元が可換な有限半群）に一致する。** [導出]
   擬恒等式で書くと、$e=z^\omega$ について $(exe)^\omega(eye)^\omega=(eye)^\omega(exe)^\omega$。
   R16 §6 が示した必要条件は、そのまま十分条件でもある。主定理の仮定は「骨格の統語半群の局所モノイドで、冪等元が可換」と一文で書ける。
2. **課題3：** LTT の統語的な特徴づけは、Beauquier–Pin が「Straubing の結果と Thérien–Weiss の結果の組み合わせ」として与えたもの。$\mathbf{Com}*\mathbf D$ の等式による特徴づけは Thérien–Weiss の定理3.1。R16 §5.3 の自前の導出は、この帰属と矛盾しない。
3. **課題1：** R16 §5.2（極小イデアルでの左からの補正と、法 $n+1$ のカウンタ）と DT の五段に、誤りは見つからなかった。補うべき論拠を 3 点挙げる（§3）。R14 の $L^{\mathsf G}$ と $E_{\rm ev}$ は DT の系として出るので、論文では DT 経由の証明を主にすればよい。
4. **課題4：** 指数 $D=f(|Q|k)^m$ は、整合する装飾窓だけを数えれば $D'=f|Q|k^m$ に下げられる（補題 L′、§4）。定理Lの元の指数 $fk^\ell$ を、装飾を通して一般に回復することはできていない。群の場合は R14 の直接証明が $fk^\ell$ を与えるので、論文では両方を載せればよい。

---

## 1. 課題2：$\mathcal W=\mathbf{L}\,\mathbf{ECom}$

### 1.1 主張

$$
\mathbf{SL}*\mathbf{LG}\;=\;\mathbf{SL}*(\mathbf G*\mathbf D)\;=\;(\mathbf{SL}*\mathbf G)*\mathbf D\;=\;\mathbf{ECom}*\mathbf D\;=\;\mathbf{L}\,\mathbf{ECom}.
$$

### 1.2 各等号の根拠

**(a) $\mathbf{LG}=\mathbf G*\mathbf D$。** [文献]
Thérien–Weiss (1985) の例1.3 と定理2.8 から、自明でない群の擬多様体 $\mathbf H$ について $\mathbf H*\mathbf D=\mathbf L\mathbf H$ が従う。本文 p.212 に、例1.3 から $\mathbf H*\mathbf D=\mathbf L\mathbf H$ が従う旨の明記がある。

**(b) 結合律。** 擬多様体の半直積の結合律（Eilenberg、Tilson）による。[標準的な事実]

**(c) $\mathbf{SL}*\mathbf G=\mathbf{ECom}$。** [導出]
- $\supseteq$ の向き：
  - Ash (1987) により、冪等元が可換な有限半群全体は、有限逆半群が生成する擬多様体と一致する。
  - McAlister の被覆定理の有限版により、有限逆半群は有限の E-unitary な被覆を持つ。
  - O'Carroll により、有限の E-unitary な逆半群は、半束と群の有限の半直積に埋め込める。
  - したがって、有限逆半群は $\mathbf{SL}*\mathbf G$ の元を割り切る。$\mathbf{ECom}\subseteq\mathbf{SL}*\mathbf G$。
- $\subseteq$ の向き：$V*\mathbf G\subseteq V\,ⓜ\,\mathbf G$ は常に成り立つ。また $\mathbf{SL}\,ⓜ\,\mathbf G$ は冪等元が可換な半群の擬多様体である（Rhodes–Steinberg、*The q-theory of finite semigroups*）。直接確かめることもできる。半束と群の半直積の冪等元は $(s,1)$ の形で、互いに可換になる。
- 監査メモ：R16 §5.3 の $\mathbf{ACom}\subseteq\mathbf{SL}*\mathbf G$ は、$\mathbf{ACom}\subseteq\mathbf{ECom}$ から即座に従う。R16 の自前の証明とも整合する。

**(d) $\mathbf{ECom}$ は局所的で、$\mathbf{ECom}*\mathbf D=\mathbf L\,\mathbf{ECom}$。** [導出。本メモの論証]
- Thérien–Weiss の定理1.5：$B_2\in\mathbf V$ なら、グラフ合同 $\beta$ が $\mathbf V$-合同であることと $M_\beta\in\mathbf V$ は同値。
  - $B_2$ はここでは 6 元の Brandt モノイド $\{(i,j)\}\cup\{0,1\}$ で、逆モノイドなので $\mathbf{ECom}$ に入る。
  - $M_\beta=P/\beta\cup\{0,1\}$ は、つながる道は合成し、つながらない道の積は $0$ とするモノイド（本文 p.207）。
- **$M_\beta$ の冪等元は $0$、$1$、ループの類だけである。**
  - 頂点の違うループどうしの積は、どちらの順でも $0$ になるので可換。
  - 同じ頂点のループは、その頂点の局所モノイドの中で可換になる（局所的な仮定）。
  - よって、局所的に $\mathbf{ECom}$-合同なら $M_\beta\in\mathbf{ECom}$、したがって $\mathbf{ECom}$-合同である。
- Thérien–Weiss の定理2.8（$\mathbf V*\mathbf D=\mathbf L\mathbf V$ ⟺ 局所的に $\mathbf V$-合同なものはすべて $\mathbf V$-合同）から、$\mathbf{ECom}*\mathbf D=\mathbf L\,\mathbf{ECom}$ が従う。
- 文献の状況：$\mathbf{DH}\cap\mathbf{ECom}$ が局所的であることは既知（Almeida ら, 2019）。$\mathbf{ECom}$ 自体が局所的であるという明示的な記述は、今回の検索では見つからなかった。上の論証は 2 行で済むので既知の可能性が高いが、投稿前に原典で照合すること。

### 1.3 R16 の例との整合（[VALID（確認）]）

| 骨格 | 統語半群 | 局所モノイドの冪等元 | $\mathbf L\,\mathbf{ECom}$ | R16 の判定 |
|---|---|---|---|---|
| $E_{\rm ev}$ | $I_2$（逆モノイド） | 可換 | 入る | (i) 内 |
| 「ab の個数が偶数」 | LG | 群なので可換 | 入る | 内（LTT∗G の外） |
| $R_{\rm last}$ | $T_2$ | $b$ と $ba$ が非可換 | 外 | (iii) 外 |
| 中立な $c$ を足した「散在する ab」 | 位数 5 | $a$ と $b$ が非可換 | 外 | (iii) 外 |
| 恒等の文字を足した flip-flop | $\{1,r_0,r_1\}$ | $r_0r_1\ne r_1r_0$ | 外 | (iii) 外 |
| reset 文字だけ（右零半群） | $\mathbf D$ | 局所モノイドが自明 | 入る | (i) 内 |

### 1.4 論文での位置づけ

| 層 | 境界 | 定義 |
|---|---|---|
| 学習器に渡す型付け（#1、02-v3、Theorem A） | $\mathbf{LG}$ | 局所モノイドが**群** |
| 標的の骨格（方向A） | $\mathbf L\,\mathbf{ECom}$ | 局所モノイドの**冪等元が可換** |

$\mathbf{LG}\subsetneq\mathbf L\,\mathbf{ECom}$。両方とも「局所モノイドについての条件」で揃い、看板の対比がきれいになる。

---

## 2. 課題3：LTT の帰属

- **Beauquier–Pin**（*Languages and scanners*、TCS；ICALP 1989 版は *Factors of words*）：LTT（threshold locally testable）の統語的な特徴づけは、Straubing の結果と Thérien–Weiss の結果の組み合わせで得られる、と明記している。 [文献]
- **Thérien–Weiss (1985) 定理3.1 と系：** $S\in\mathbf{Com}*\mathbf D$ ⟺ 冪等元 $e_1,e_2$ と任意の $s,t,u$ について $e_1se_2te_1ue_2=e_1ue_2te_1se_2$。また例1.4 により $\mathbf{Com}*\mathbf D\ne\mathbf L\,\mathbf{Com}$（$\mathbf{Com}$ は局所的でない）。 [文献、本文 pp.208, 212]
- **Straubing (1985)**：$\mathbf V*\mathbf D$ を窓の合同で記述する（定理4.3）。LT については §7.1。 [文献。R16 が照合済み]
- **LT の起源**：Brzozowski–Simon (1973)、McNaughton (1974)。 [文献]
- **論文での書き方（案）：** 「$\mathbf{LT}=\mathbf{SL}*\mathbf D$（Brzozowski–Simon, McNaughton, Straubing）、$\mathbf{LTT}=\mathbf{ACom}*\mathbf D$（Straubing と Thérien–Weiss の結果から。Beauquier–Pin による LTT の特徴づけを参照）」。
- 主定理には LTT の等式は要らない。$\mathbf{SL}*\mathbf{LG}=\mathbf{LTT}*\mathbf{LG}$ の等号は、§1 から $\mathbf{SL}\subseteq\mathbf{LTT}\subseteq\mathbf{ACom}*\mathbf D\subseteq\mathbf{ECom}*\mathbf D$ で直接従う。

---

## 3. 課題1：独立監査

### 3.1 R16 §5.2（十分性の構成）[VALID（確認）、論拠を補う 3 点つき]

1. **$T^n\subseteq K$（$n=|T|$）。** 長さ $n$ 以上の積は、接頭部の積の鳩の巣で $p=p\,t$ となる因子を持つ。よって $p=p\,t^\omega\in TE(T)T$。LG では冪等元はすべて完全単純な極小イデアル $K$ に入るので（arXiv:1509.01533 §2.6 に、文献 [13] の命題2.1 として記述あり）、$TE(T)T\subseteq K$。
   - R16 は `thm:lg-characterization` を引くだけで済ませている。**この一行を本文に補うこと。**
2. **左からの補正 $hxp=p$。** $p\in K$、$x\in T^1$ なら $xp\le_{\mathcal L}p$。$K$ の中ではすべての元が $\mathcal J$-同値なので、有限性（安定性）から $xp\,\mathcal L\,p$。したがって、$p=h\,(xp)$ となる $h\in T^1$ がある。
   - R16 の「Rees 行列表示で同じ列」は、この事実の言い換えとして正しい。
   - 帰結：仮想の入口 $y$ からの走りは、接頭部のあとでは $yh\cdot(\text{実際の状態})$ になる。上の層は半束なので順序も重複も効かず、接頭部のあとに現れるイベントの**集合**だけで値が決まる。
3. **法 $n+1$ のカウンタ。** イベントごとのカウンタの値は、出現のたびに 1 進む。したがって出現する値の種類数は、入口の値によらず $\min(n+1,N)$ になる。接頭部（長さ $n$）の中の出現数は $\le n$ なので、「接頭部のあとにもう一度現れるか」が正確に判定できる。
   - 下の層は $(\mathbb Z_{n+1})^{\rm events}\wr T$ を割り切る。$\mathbf G*\mathbf{LG}\subseteq\mathbf{LG}*\mathbf{LG}=\mathbf{LG}$ なので、LG のまま。
   - **$\mathbf{LG}*\mathbf{LG}=\mathbf{LG}$**（R16 §5.1）も、手で確かめた。局所モノイドの冪等元 $Z=(H,b)$ は、まず $qb=q$ のところで $H(q)=F(q)$ となる（$F(q)UF(q)$ が群）。一般の $q$ でも $H(q)=F(q)H(qb)=F(q)$。よって冪等元は一つで、局所モノイドは群。
   - 補足：§1 の $\mathbf{LG}=\mathbf G*\mathbf D$ と結合律からも従う（$\mathbf G*\mathbf D*\mathbf G*\mathbf D$ の中央の $\mathbf D*\mathbf G\subseteq\mathbf{LG}$ を経由する）。ただし R16 の直接の証明のほうが短い。
- 仮想の入口 $y=1$ の値が下の層の元 $1\cdot w=hz_{\rm end}$ を与えるので、花輪積の元が全座標で復元できる。$\rho(w)$ はその商として得られる。

### 3.2 DT の五段（R16 §3.3）[VALID（確認）]

| 段 | 確認したこと |
|---|---|
| 1 復元 | $m\ge\max(2,d,\ell)$ なら、$(b_m,N_m)$ から整合性（隣接の対の検査）、短い窓の計数、$N_\ell$（射影）が出る。正しい |
| 2 Rect の移送 | 共有された受理文脈があれば各成分は内部で整合し、端の装飾文字から入口と出口が一致する。(C2) から射影の $\rho$ が、$c_\Gamma$ から $c_\Sigma$ が、$b_m$ から $b_\ell$ が、それぞれ一致する。試験文脈の不整合は、文脈片の内部・つなぎ目・語頭のどれかで起き、どれも両方の組で同時に起きる。網羅されている |
| 3 文法の積 | $[A;(p_i,q_i)]$ の構成で fan-out、rank、good 性が保たれる。$v'\le1+v|Q|^{2f}$。正しい |
| 4 厚さ | 入口と出口だけを指定した生成組の長さは、変換全体を指定した最短長以下（存在するものについて）。`thm:local-group-polydata` の $t_{\rm typ}=O(\|G\|\bar\theta_G)$ がそのまま使える。$\bar\theta_{G^\#}\le(v'+1)(\theta+r\beta)$。正しい |
| 5 戻し | $\pi F$ が $x$ と $\pi Y$ の共有受理文脈になり、元の代入可能性で分布が回復する。正しい |

**注意点（誤りではない）：** 第4段で使う $t_{\rm typ}$ の上界は、`thm:local-group-polydata` の証明の中の `cor:lg-type-level-shortest` に依存している。この系自体は compendium 第 V 部（l.10397）にあり、今回は読み直していない。

### 3.3 R14 の $L^{\mathsf G}$ と $E_{\rm ev}$

- どちらも DT の系として出る（R16 U2）。DT 経由の証明は Euler 再配線で群の値を指定する段（R14 §3.4 の 3〜4）を使わないので、**論文では DT 経由を主の証明にし、R14 の直接証明は次数のよい別証明として載せる**のが安全である。
- $E_{\rm ev}$ の統語半群 $S_E\cong I_2$（7 元）、$bS_Eb\cong U_1$、どの LG 型付けでも 1 穴の代入が成り立たないこと（R14 §4.3）は、前回すでに手で確かめた。
- R14 §3.2 の補題G(ii)（閾値 $n(n-1)$、Dénes–Hermann の定理8 による）：各元に短い語を予約し、ブロックを並べ替える構成は正しい。ただし DT 経由なら、この補題は主定理には不要になる。

---

## 4. 課題4：次数の回復

### 4.1 補題 L′（使われる窓だけを数える）[証明の概略。要確認]

定理Lの指数 $K=|\Gamma|^m$ は、証明の中で次の三か所にしか現れない。

- W2 の頻度の隙間に使う区間の数（$K+1$）
- 色の数 $C_L$ の中の不純窓の多重集合（$Kf$ 座標）
- 被覆路の長さ $\lambda$（頂点数と辺数）

どれも「標的の語に実際に現れうる辺の種類数」で置き換えられる。Euler 再配線は頻出成分 $J$ の中だけで行うので、$J$ は現れうる辺の部分グラフに含まれる。

装飾語の $m$ 窓 $((q_1,a_1),\dots,(q_m,a_m))$ は、$q_{i+1}=q_ia_i$ を満たすものだけが現れる。したがって種類数は $|Q|k^m$ 以下で、

$$
D=f(|Q|k)^m\quad\longrightarrow\quad D'=f\,|Q|\,k^m .
$$

| 系 | R16 の指数 | 補題 L′ 後 | 直接証明 |
|---|---|---|---|
| $E_{\rm ev}$（$|Q|=2$、$k=2$、$m=\max(2,\ell)$） | $f\,4^m$ | $f\,2^{m+1}$ | R14：$f\,4^{\max(2,\ell)}$ |
| $L^{\mathsf G}$（$|Q|=h=|\mathrm{im}\,\varphi|$） | $f(kh)^{\max(2,\ell)}$ | $f\,h\,k^{\max(2,\ell)}$ | R14：$fk^\ell$ |
| 定理P（$|Q|=1$、$m=2$） | $fk^2$ | 現れる二文字の数（$\le k\cdot$ 最大出次数） | 元の P：$fk$ |

### 4.2 回復できないもの

- 装飾を通す限り、$m\ge2$（隣接の整合性の検査）が必要なので、$\ell=1$ でも $k^2$ 程度の因子が残る。元の $fk^\ell$ を一般に回復する方法は見つかっていない。[OPEN]
- 群の場合は、R14 の直接証明（色に群の値と辺の計数の法 $n$ を入れる）が $fk^\ell$ を与える。論文では「統一定理は $D'$、群の場合は別証明で $fk^\ell$」と書けば足りる。

---

## 5. 残る義務

1. **§1(d) の文献照合：** $\mathbf{ECom}$ の局所性の既出の文献を探すこと。見つからなければ、本メモの 2 行の論証（Thérien–Weiss の定理1.5 と定理2.8）を本文に入れる。
2. **補題 L′ の確認：** 定理Lの修正版 tex（R14）の中で $K$ が現れる箇所をすべて洗い出し、置き換えが通ることを確かめる。
3. **主定理の書き直し：** 仮定を「骨格の正の統語半群が $\mathbf L\,\mathbf{ECom}$ に入る」とし、R16 §6 の 3 例を、$\mathbf L\,\mathbf{ECom}$ の外の最小例として載せる。

## 参照した文献

- D. Thérien, A. Weiss, *Graph congruences and wreath products*, J. Pure Appl. Algebra 36 (1985) 205–215（研究者が添付。例1.3、定理1.5、定理2.8、定理3.1、例1.4）
- C. J. Ash, *Finite semigroups with commuting idempotents*, J. Austral. Math. Soc. (A) 43 (1987) 81–90
- D. B. McAlister の被覆定理と O'Carroll の埋め込み定理（*Structure theory of regular semigroups*, arXiv:1909.05280 の記述による）
- J. Rhodes, B. Steinberg, *The q-theory of finite semigroups*（$\mathbf{SL}\,ⓜ\,\mathbf G$ が冪等元可換な半群の擬多様体であること）
- D. Beauquier, J.-E. Pin, *Languages and scanners*（LTT の特徴づけの帰属）
- J. Almeida ほか, *Bases for pseudovarieties closed under bideterministic product*, Algebra Universalis (2019)（$\mathbf{DH}\cap\mathbf{ECom}$ の局所性）
- R16 report.md §§3–7、R14 report.md §§3–4、compendium `thm:local-group-polydata`
