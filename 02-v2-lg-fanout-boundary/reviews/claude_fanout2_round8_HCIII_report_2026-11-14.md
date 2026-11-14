# 第八段 最終報告：HC_III（同一根成分に二つの削除）、ℓ=2・fan-out 2・rank 2・共有一文字

**日付**：2026-11-14　／　**作成**：Claude（Opus 5.5、新規セッション）　／　**状態**：研究アーカイブ・未査読
**原稿への変更**：なし（GitHub `main`、英日 LaTeX、PDF、定理A/B/C、`op:fanout-two` に触れていない。commit・PR なし）
**前段**：`claude_fanout2_round8_checkpoint1_2026-11-14.md`

## ① 一文結論

**PROVED（引用補題のもと）**：HC_III は成り立つ。$c_*=3$ のとき、$m'=0$ なら 2 つの一文字穴 $\mathtt a,\mathtt b$（F 側は $W_{j'}$ そのまま）、$m'>0$ なら $S_6=\{\mathtt{abc},\mathtt{bac},\mathtt{cab},\mathtt{cba},\mathtt{acb},\mathtt{bca}\}$ から選ぶ一つの穴で、補題R の (Y)(F) が同時に成り立つ。前提として引用し、本段で再証明していないのは P1^⊗（span 版）、B6、補題R の前提（DFS／色）である。反例は (A)〜(D) のいずれも見つからなかった。

---

## ② 読んだ資料と依存関係

資料の一覧はチェックポイント1 §0 にある。GitHub commit は `552f840`。添付 ZIP はこの会話に無かったので、GitHub の `reviews/round7_hc/` を正本とした（補助 3 本の SHA256 は GitHub 版と一致）。

| 依存 | 内容 | 状態 |
|---|---|---|
| 補題G（第六段） | $\operatorname{dat}_{\rm ov}\leftrightarrow\Gamma$ | 独立証明済み。本段で有界検査 [1] |
| 補題H\*（第六段） | 万能穴 $t=\mathrm{expand}(h,D)$ | 独立証明済み。本段 [2] で毎回 assert |
| 補題R（第六段報告 §3.1） | 同期を (Y)(F) に帰着 | 本段 §4.0 で**再導出**し、F 側の要件を確定した |
| P1^⊗（span 版、L^⊗′ 監査 B4） | $Z_\kappa\ge0$、circulation、$Z_{\kappa,b}$ は $\pi_b\varphi_\kappa$ の**印なし内部窓**を数える、$\operatorname{dat}(W_j)-\operatorname{dat}(W_{j'})=\sum Z_\kappa$、色が $\widehat s_2(\pi_b\psi_\kappa)$ を含む | **引用** |
| B6（同監査） | 削除は原 $x$ の印なし出現で、段ごとに互いに素 | **引用**（補題P が依存） |
| 補題K（保存則） | κ ごとに $c$ の増減が A・B で一致 | 独立証明済み |

---

## ③ 仮定・量化・記法

- $\Sigma=\{a,b,c\}$、$A=\{a,c\}$、$B=\{b,c\}$、ℓ=2、$f=2$、rank $\le2$、型付け $s=c_\Sigma$（窓型との直積には精密化しない）。
- $L\cap\Sigma^+=\{w:\operatorname{dat}_{\rm ov}(w)\in\mathcal Q\}$（**$\mathcal Q$ 任意**）、$L\in\mathcal C^{\rm mcf}_{2,c_\Sigma}$、$G$ は $L\cap\Sigma^+$ の任意の reduced good MCFG。
- 根成分 $x$（$\Gamma$ の記法は補題G：$n,\ |w|_a,|w|_b,\ \nu_A,\nu_B,\ a_0,a_n,b_0,b_n$）。区間 $x=u_0\,c\,u_1\cdots c\,u_{n_0}$。
- 印：各根成分・各射影・各窓種の最初の $c_*$ 個の出現の文字。**$c_*=3$**（§4.4 で十分性を示す）。
- η は印なしの極大自由節点で、成分 $\varphi=x[s{:}e]$（κ）と $\varphi'=x[s'{:}e']$（κ′）が**同じ根成分 $x$** にある（順序・隣接は任意。$\varphi$ が $\varphi'$ の接頭部 $P'$ に入る場合や、その逆も含む）。
- $Z_\kappa=(p\,aa,\ p'\,bb)$（$p,p'>0$）、$Z'=Z_{\kappa'}=(q\,aa+q_c\,cc+r(ac+ca),\ q'\,bb+q'_c\,cc+r'(bc+cb))\ne0$、$m'=q_c+r=q'_c+r'$（補題K）。H\* で許される全ての型が、この一般形に含まれる。
- $W=W_{j'}=E_0[x^{(j')}]$。$x$ は $W$ の中で $x'$（$\varphi\to\psi$、$\varphi'\to\psi'$）になる。$T$ は**次の状態**（$=S-Z_\kappa-Z'$）。補題P の範囲 $\min(N_0(w),c_*)\le N_T(w)\le N_0(w)$、$\widehat s_2$ 不変、の**任意の** $T$ を扱う。
- 「Γ が穴 $(h_1,\dots,h_e)$ を **hosting する**」とは、Γ をもつ語であって、穴が順に・重ならず・間に全文字上で非空の区切りをもって因子として現れるものがある、という意味である（判定器 `hosts`、構成器 `realize`）。

---

## ④ 既存補題の監査結果

| 項目 | 分類 | 根拠・注記 |
|---|---|---|
| 1. 補題G′（O1–O3） | **VERIFIED** | Γ を変えない。根成分の境界が $c$ 区間を切る場合も、W 全体の Γ が保たれればよい。窓 span は射影で消えた文字を跨いでも補題G が厳密に数える。「領域に閉じる」は §4.0 により不要 |
| 2. 補題FO | **VERIFIED** | 印付き窓の文字が $\varphi$ の中にあると η が印を含むことになる。$P$ に他の自由成分があっても印は η の外 |
| 2. 補題P | **DEPENDS-ON-UNPROVED-LEMMA**（B6） | B6 を認めれば正しい。旗（$a_0,a_n,b_0,b_n$、$[\nu\ge1]$）の一致は $c_*\ge2$ で成り立つ |
| 3. 補題YB | **VERIFIED**（$c_*\ge2$） | 独立に再証明（§4.2）。端区間（$\widehat s_2$ で持続）、内側（$\nu\ge1$ で持続）、$\varphi\ni c$（遷移窓が印なしなので $\nu\ge c_*-1$）の 3 場合 |
| 4. 補題FL | **VERIFIED** | 隠れた仮定は「$\varphi$ が両文字を含む」「$P$ が最後の区間まで届く」の二つで、どちらも成り立つ |
| 5. 補題AB (2b) | **VERIFIED（再構成）** | $m_2<t$ なら $J=p_{m_2}$ の両端の $c$ は $P$ の中。$m_2=t$ で $\psi\not\ni c$ なら $\psi$ が $X$ を含み (2a) に戻る。本段の証明では使わない |
| 6. 補題OT $\{a,b,c\}$ 行 | **NEEDS-REPAIR（軽微、修復済み）** | $R'=\{a,b,c\}$ は $r=r'=0$ でも起きる。そのとき遷移窓は $ac$ と $ca$ の**片方**しか内部にないことがある。存在する方の印付き出現 2 個のうち後の方の区間は内側で、両端の $c$ ごと $P'$ に入るので、そこを $I_a$ とすればよい。本段では使わない |
| 7. HC_I・HC_II | **VERIFIED（引用前提のもと）** | HC_I の証明は「同じ根成分に削除 0 の成分がある」場合を含む。HC_II は別の根成分にある場合だけで、場合 III とは混ぜていない |

**最重要の監査所見（§4.0）**：依頼書 §5.5 の「全保護領域が不変」は**補題R の要件ではない**。この点は、第七段で F 側局所化（依頼書 §0.1）を未解決とした理由に直接関わる。

---

## ⑤ 場合 III の分類表

$\varphi,\varphi'$ の相対順序、隣接、$c$ を跨ぐかどうか、$P'$ への包含は**分類の軸にならない**。証明が使うのは次の三つの量だけだからである。

| 枝 | 条件 | 穴 | F 側の証人 | Y 側 |
|---|---|---|---|---|
| **A** | $m'=0$（$Z'=(q\,aa,q'\,bb)$、$R'\subseteq\{a,b\}$） | $\mathtt a,\mathtt b$（W の文字の順） | $W^\*=W$ そのまま | YB |
| **B-rich** | $m'>0$、$\nu^T_A,\nu^T_B\ge1$ | Γ$(W)$ が置ける $S_6$ の語 | 補題F6 | 補題Y6（$S_6$ 全部） |
| **B-X0-first** | $m'>0$、$\nu^T_X=0$、$\varphi\subseteq u_0$ | $XYc$ | $P$ の印付き $X,Y$ と $x$ の最初の $c$ | $X_0\wedge Y_0$ |
| **B-X0-last-both** | $\nu^T_X=0$、$\varphi\subseteq u_{n_0}$、$\Lambda\ni Y$ | $cXY$ | $\Lambda$（最後の $c$ から $\varphi$ の前まで） | $X_n\wedge Y_n$ |
| **B-X0-last-sep** | $\nu^T_X=0$、$\varphi\subseteq u_{n_0}$、$\Lambda\not\ni Y$ | $YcX$ | $\nu^F_Y\ge1$ と $K\ge2$ | $\nu^T_Y\ge1$、$X_n$ |

（$X\in\{a,b\}$、$Y$ はもう一方の文字。$X=b$ の枝は $a\leftrightarrow b$ の鏡像。）

---

## ⑥ 定理と証明

### 4.0 補題R′（F 側は Γ だけで決まる）[独立証明]

**主張.** 根成分 $x$ の差分の和 $Z_\kappa+Z'$ を、保存則を満たす非零の $D_1,\dots,D_e$（$e\le2$、$\sum D_i=Z_\kappa+Z'$）に分ける。穴 $h_i\in\Sigma^+$ は $R(D_i)$ を含み、$t_i=\mathrm{expand}(h_i,D_i)$ とする。

- (Y) Γ$(T)$ が $(h_1,\dots,h_e)$ を hosting する；
- (F) Γ$(W_{j'})$ が**同じ順序で** $(h_1,\dots,h_e)$ を hosting する。

この二つが成り立てば、$y^\pi\equiv_{L,c_\Sigma}y'$ で、状態は $S\mapsto T$ と更新される。

*証明.*
1. (F) の語を $W^\*=F[h]$ とする。$\operatorname{dat}(W^\*)=\operatorname{dat}(W_{j'})$ なので $W^\*\in L$（$L\cap\Sigma^+$ は $\operatorname{dat}$ の逆像）。
2. H\* は**どの文脈でも**、穴ごとに差 $D_i$ を足し、位置に依らない。また $\pi_A W^\*,\pi_BW^\*$ は長さ $\ge2$ なので $\widehat s_2$ も変わらない。よって $\operatorname{dat}(F[t])=\operatorname{dat}(W_{j'})+\sum Z=\operatorname{dat}(W_j)$（P1^⊗）、$F[t]\in L$。
3. $F\in\mathcal E_e$（区切りは非空）。$\operatorname{alph}(t_i)=\operatorname{alph}(h_i)$ なので型が一致し、$\mathcal D(h)\cap\mathcal D(t)\ni F$。$(2,c_\Sigma)$-代入可能性から $\mathcal D(h)=\mathcal D(t)$。
4. (Y) の語 $y'$ に対し、$y^\pi=y'[h\to t]$ は H\* により状態 $T+\sum D_i=S$ を実現する。$y^\pi$ の受理文脈 $E$ は、$t$ を穴にした admissible 文脈 $E'$ を与える（同じ成分内の穴の間は非空、成分間には $E$ の $v_1\ne\varepsilon$ がある）。よって $E\in\mathcal D(y^\pi)\iff E'\in\mathcal D(t)=\mathcal D(h)\iff E\in\mathcal D(y')$。内容も一致する。
5. $\operatorname{dat}$ が成分ごとに等しい組は同じ分布をもつ（$(\widehat s_2,N_2)$ は連接で合成される）。∎

**帰結.**
- $W^\*$ は $W_{j'}$ と同じデータの語でありさえすればよく、$\psi$、印、凍結部分、root の外を保つ必要はない。$F$ は一段の証人にすぎず、次段は新しい $W_{j'}$ を使う。
- 穴を η 成分に 1 対 1 で紐づける必要もない。使うのは総和と保存則だけである。
- 依頼書 §4 の「操作区間が他方の φ に接触する個数の上界」は、この定式化では不要になる。
- 状態の実現可能性：補題P の範囲の $T$ は、Γ の整合式（$n_A=n_B$ は補題K、$\nu_X=N(cX)-[X_n]\le n-1$ など）を満たすので語で実現される。`state_range` はその Γ を列挙している。

### 4.1 補題F6（F 側）[独立証明]

**主張.** $W$ が $c$ を含み、$P=x[0{:}s]$ が印付きの $a$ と $b$ を含み（補題FO）、$\psi$ が $W$ の中でそれらより後にあり、$|\pi_A\psi|,|\pi_B\psi|\ge2$ とする。このとき Γ$(W)$ は $S_6$ のいずれかを hosting する。

*証明.* $n=n^F\ge1$ とする。
- 両持ち区間を作れる場合：$(a_0\wedge b_0)$ なら $\mathtt{abc}$、$(a_n\wedge b_n)$ なら $\mathtt{cab}$、$(\nu_A\ge1\wedge\nu_B\ge1)$ なら内側の区間に $\mathtt{abc}$。
- $\nu_A\ge1$、$\nu_B=0$ で両持ちなしの場合：$b_0$ なら内側区間 1 に $a$ を置いて $\mathtt{bca}$、$b_n$ なら区間 $n-1$ に $a$ を置いて $\mathtt{acb}$。逆の場合も対称。
- $\nu_A=\nu_B=0$ で両持ちなしの場合：$a$ と $b$ は互いに逆の端にある。$n=1$ なら $\mathtt{acb}$ か $\mathtt{bca}$。

残るのは $W=a^\alpha c^n b^\beta$ または $b^\beta c^n a^\alpha$（$n\ge2$）だけである。前者では印付きの $b$ は $b$ ブロックにあり、$\psi$ はその後なので $\psi\in b^+$ となり、$\pi_A\psi=\varepsilon$ で矛盾する。後者では $\psi\in a^+$ となり矛盾する。∎

$|\pi_A\psi|\ge2$ の理由：P1^⊗ から $Z_{\kappa,A}=N(\pi_A\psi^{(j)})-N(\pi_A\psi)\ni aa$ なので $\pi_A\psi^{(j)}$ は長い。色が $\widehat s_2$ を含むので $\pi_A\psi$ も長い。$B$ も同様。

### 4.2 補題YB・Y6（Y 側）[独立証明]

**YB.** $T$ は、$a$・$b$ を含み 3 文字以上をもつ区間を作れる。
- $\varphi\not\ni c$ のとき：$\varphi$ の区間は $a,b$ を 2 個ずつ含む。それが端なら旗が持続し、内側なら $\nu_A,\nu_B\ge1$ が持続して同じ内側区間に揃えられる。
- $\varphi\ni c$ のとき：$\pi_A\varphi$ に印なしの遷移窓があるので $\nu^T_A\ge c_*-1\ge1$。$B$ も同様。
- どの場合も $N_T(aa)\ge c_*\ge1$ なので、余分の $a$ をその区間に寄せられる。

よって $T$ は $\mathtt{ab}$、$\mathtt{ba}$、$(\mathtt a,\mathtt b)$、$(\mathtt b,\mathtt a)$（間を非空に）を全て hosting する。

**Y6.** $\nu^T_A,\nu^T_B\ge1$ かつ $n_T\ge3$ なら、$T$ は $S_6$ の全ての語を hosting する。
- 内側区間 1 を両持ちにすれば $\mathtt{abc},\mathtt{bac},\mathtt{cab},\mathtt{cba}$。
- 内側区間 1・2 に $a$／$b$ を独立に置けば $\mathtt{acb},\mathtt{bca}$（補題G より $\alpha$ 列と $\beta$ 列は独立に選べる）。

### 4.3 定理 III-A（$m'=0$）[独立証明]

穴 $h_a=\mathtt a$（$D_a=((p+q)aa,0)$）と $h_b=\mathtt b$（$D_b=(0,(p'+q')bb)$）を使う。どちらも $m=0$ で保存則を満たし、和は $Z_\kappa+Z'$ である。

- **F 側.** $\varphi$ に印なしの $aa$ があるので $N(aa)\ge c_*+1$。印付きの $aa$ の 2 文字 $u_1<u_2$ と $bb$ の 2 文字 $v_1<v_2$ は η の外にあり、$W$ に文字どおり残る。4 組の $(u_i,v_j)$ が全て隣接することはない：$v_1=u_1-1$、$v_2=u_1+1$ となるので、$u_2$ が両方に隣接するには $u_2=u_1$ でなければならない。距離 $\ge2$ の組をその順に穴にすれば $W^\*=W$ で、区切りは非空である。
- **Y 側.** YB により両方の向きを置ける。∎

### 4.4 定理 III-B（$m'>0$）[独立証明]

穴は一つ（$e=1$）、$D=Z_\kappa+Z'$。$R(D)=\{a,b,c\}$ なので、$S_6$ の語はどれも必要文字を含む。

**(i) $\nu^T_A,\nu^T_B\ge1$.** $n_T\ge3$ を示す。
- $q_c>0$ なら、内側で $a$ を持たない区間が $\ge c_*$ 個、持つ区間が $\ge1$ 個ある。
- $q_c=0$ なら $r>0$ で、$ac=\nu_A+[a_0]\ge c_*$ から $\nu_A\ge c_*-1\ge2$。

よって $c_*\ge3$ で $n_T\ge3$。補題F6 で選んだ語を、Y6 により $T$ も置ける。

**(ii) $\nu^T_A=0$**（$\Leftrightarrow\nu^x_A=0$、補題P）.
- **(1)** $r=0$。$r>0$ なら $\varphi'$ に印なしの $ac$ があり、$\nu^x_A\ge c_*$ となる。したがって $q_c=m'\ge1$ で、$\pi_A\varphi'$ は印なしの内部 $cc$ をもつ。補題FO から、$x$ には $\varphi'$ より前に $c_*+1$ 個以上の $c$（印付き）がある。
- **(2)** $\varphi\not\ni c$。含むなら印なしの遷移窓から $\nu_A\ge c_*-1$。$a$ を含む区間は端だけなので、$\varphi\subseteq u_0$ か $\varphi\subseteq u_{n_0}$。

**(I) $\varphi\subseteq u_0$.**
- $a_0=b_0=1$ なので、$T$ は $\mathtt{abc}$ を置ける。
- F 側：$\varphi'\ni c$ なので $\varphi'\not\subseteq P\subseteq u_0$。$P$ は $W$ に文字どおり残り、印付きの $a,b$ を同じ $W$ 区間に含む。$x$ の最初の $c$ は (1) により $\varphi'$ の前にあり、η の外である。したがってその区間は最後の区間ではなく、Γ$(W)$ は $\mathtt{abc}$ を置ける。

**(II) $\varphi\subseteq u_{n_0}$.**
- $a_n=b_n=1$ なので、$T$ は $\mathtt{cab}$ を置ける。
- $\nu_A=0$ なので $ca$ 窓はちょうど 1 回現れ、印付きである。すなわち $x$ の最後の $c$ と、$u_{n_0}$ の最初の $a$（$=a^\*$）は η の外にあり、$a^\*$ は $\varphi$ より前にある。
- $\varphi'$ は $c$ を含むので、最後の $c$ より前で終わる。よって $\Lambda=x[\text{最後の }c:s]$ は $W$ に文字どおり残り、$a^\*$ の $W$ 区間 $K$ は $K\ge1$ を満たす。さらに (1) の印付き $c$ により $K\ge2$。
- **(II.1) $\Lambda\ni b$**：区間 $K$ が両持ちになり、Γ$(W)$ は $\mathtt{cab}$ を置ける。
- **(II.2) $\Lambda\not\ni b$**：$u_{n_0}$ の最初の $b$ は $\varphi$ の中にある。
  - $\nu^x_B=0$ なら $cb$ 窓は一意で印付きになり矛盾する。よって $\nu^T_B\ge1$ で、$T$ は $\mathtt{bca}$ を置ける（区間 $n_T-1$ に $b$、区間 $n_T$ に $a$）。
  - F 側：$\pi_Bx$ の最初の $cb$ 窓は内側区間にあり、印付きである。その $b$ は η の外で、$W$ の中で前に $x$ の最初の $c$、後に最後の $c$ をもつので $\nu^F_B\ge1$。$K-1\ge1$ は内側なので、区間 $K-1$ に $b$ を置き、$a^\*$ を区間 $K$ に残せば $\mathtt{bca}$ になる。

**(iii) $\nu^T_B=0$** は $a\leftrightarrow b$ の鏡像。$S_6$ は鏡像で閉じている。∎

**$c_*$ の十分性.**
- $c_*\ge2$：補題P の旗、YB、(1)、(2) で使う。
- $c_*\ge3$：(i) の $n_T\ge3$ で使う（$r>0$、$q_c=0$ の場合）。

よって $c_*=3$ で十分である。$c_*\ge5$ は不要。$c_*=2$ で (i) が崩れうることは [4] で確認したが、その範囲では崩れた例は出なかった。

### 4.5 定理 HC_III（まとめ）

§③ の仮定と、P1^⊗（span 版）・B6・補題R の DFS／色の前提のもとで、$c_*=3$ とする。同じ根成分に $\{a,b\}$ 型の κ と、任意の $Z'\ne0$ をもつ κ′ があるとき、穴 $e\le2$ で補題R の (Y)(F) が成り立つ。

依頼書 §5 の義務との対応：
- 1・2：引用と補題K。
- 3：穴は非空、$\le2$、$c_\Sigma(h)=c_\Sigma(t)$。
- 4：Y 側は 4.2〜4.4。
- 5：F 側は §4.0 により Γ だけでよい（III-A では $W^\*=W$ のまま）。
- 6・7：§4.0。
- 8：$D\ne0$ なので、穴を戻すたびにデータは厳密に減る。

---

## ⑦ Python 検証（網羅・乱数・未検査の区別）

`check_round8_HCIII_2026-11-14.py`（新規、標準ライブラリ、固定シード 801–804、87 秒、exit 0）。出力は `out_check_round8_HCIII_2026-11-14.txt`。補助モジュールは新規の `hc3_construct.py` と、第七段の `hc_core.py`・`hc_construct.py`・`hc_search_case2.py`（**無変更**、SHA256 は GitHub 版と一致）。

| 節 | 内容 | 結果 |
|---|---|---|
| [1] **網羅** | 長さ $\le7$ の全語の Γ（841 類）× 穴の組 290145 通りで、新しい構成器 `realize` と判定器 `hosts` が一致。証人ごとに Γ の一致、穴の文字どおりの出現、順序、区切り $\ge1$ を確認 | 不一致 0（証人 47108） |
| [2] **乱数＋狙った形** | $c_*=3,4,5$、2200 配置（乱数 1100、$\nu=0$ 型の狙い撃ち 1100）、全ての状態 $T$（64 を超える場合だけ、端 16 個と乱数 48 個に間引いた）。証明の各段の事実（FO、$r_X=0$、$\varphi\not\ni c$、区間位置、$\Lambda$、$\nu^x_Y\ge1$、$n_T\ge3$）を assert。実際に $y'$ と $W^\*$ を作り、$\Gamma(y')=T$、$\operatorname{dat}(W^\*)=\operatorname{dat}(W)$、穴の位置・順序・区切り、H\* の差 $=Z+Z'$、$\widehat s_2$ 不変、内容型、保存則を assert | **136168 件全て通過** |
| [3] カバレッジ | 8 枝すべてに到達（A 59983、B-rich 47223、a0-first 2745、a0-last-both 8380、a0-last-sep 6450、b0-first 1856、b0-last-both 2367、b0-last-sep 7164） | 未到達の枝なし |
| [4] 陰性対照 | 穴を $S_6$ の固定の 1 語にすると、どの語でも失敗例が出る（128〜960 件）。したがって場合分けは必要で、検査は空ではない | 失敗を検出 |
| 別探索 `hc3_search.py` | 1 穴と**全ての**保存則つき 2 分割、長さ $\le3$ の語と $c$ の連で存在を探す（構成を使わない）。出力 `out_hc3_search_2026-11-14.txt` | 約 3.7 万件で NOT FOUND WITHIN BOUND は 0 |

**限界.**
- モデルは第七段と同じく実際の文法より広い（$\psi$ には $|\pi_X\psi|\ge2$ だけを課し、状態は補題P の範囲全体）。
- **実際の good MCFG の導出木と極大 η から作った場合 III の例は検査していない**（依頼書 §7.5 は未達）。
- `assert … or True` は使っていない。失敗時は配置を出力して停止する。
- 有限検査は証明ではない。証明は ⑥ による。

---

## ⑧ 論文 #2 と一般未解決問題への影響

- 第六段の条件付き定理U₂（$\tau(G,c_\Sigma)=O_r(v^{18}\bar\theta_G^{17})$）の未証明条件 HC-sim は、場合 I・II・III すべてで**引用補題のもと解消**した。
- ただし U₂ は**まだ確立していない**。重なる射影での P0/P1/DFS/W2、型付き高さ、頻度ギャップ、元 $G$ の厚さの評価は、別途の独立監査が必要である。特徴標本**総長**への移行には `cor:distribution-representatives` の全仮定を元の $\bar\theta_G$ で確認する必要がある。
- **`op:fanout-two` は OPEN のまま**。この結果は、$U_1$ 型付けによる下界（YES 方向）の候補を「共有一文字・ℓ=2」の範囲で一つ減らすだけで、YES／NO を決めない。原稿の変更根拠はない。

## ⑨ 次の最短の一手

1. **独立監査**：§4.0（補題R′：F 側は Γ だけ）と §4.4 (II.2)。証明全体の要はこの二つである。
2. 第六段の例R を拡張し、実際の good MCFG で場合 III（同じ根成分に $\{a,b\}$ 削除と $cc$ 削除）を作り、文法・導出木・切り口から `hc3_holes` を走らせる。
3. U₂ の残りの引用補題（重なり版 P0/P1/DFS/W2、型付き高さ）の再監査。