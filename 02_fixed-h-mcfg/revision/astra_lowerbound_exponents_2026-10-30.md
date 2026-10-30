# MCFG の特徴データ長：高ファンアウトでの線形因子下界と、単項群型付けでの指数改善

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| **T1：fan-out≤2、任意の固定型付けに対する Ω(‖G_n‖θ̄) 下界** | **証明済み** | §3–§5。九文字の固定アルファベット、定数1/31 |
| 全ての部分集合が、全ての d≤2 について自明型付き組代入可能 | **証明済み** | §3。任意の非空組・全許容文脈を扱う解析的証明 |
| T1 の族の全ての reduced good fan-out≤2 表示で ‖G‖≥q+1、θ̄=W | **証明済み** | §5。特定の提示文法だけの評価ではない |
| 任意の固定 f≥1 への T1 の拡張 | **証明済み** | §3–§5。アルファベットは f ごとに固定し、4f+1文字。下界定数1/(7f+17) |
| 一つの固定アルファベット上で、同一族について全ての f を同時に扱う拡張 | **未解決** | §5.4。本構成はこの追加要求を満たすとは主張しない |
| **T2 の上界側：Σ={a}、s(a)=1∈ℤ_m、m≥2 固定で O(‖G‖θ̄)** | **証明済み** | §6–§7。任意の固定 fan-out・rank cap、全対象・全表示。τ≤2mθ̄ |
| 多文字アルファベットで、例えば a が奇型・他の文字が単位元となる型付けの指数一致 | **未解決** | §8。単項結果を多文字へ拡張していない |
| 群を含む多文字型付けの Ω(‖G_n‖²θ̄) 下界 | **未解決** | §8。本報告はその下界を得ていない |
| 同じ構成でマーカーを二つ・三つに減らしても hereditary な二穴代入可能性を保つ | **反証済み** | §8.1。二語の部分集合への明示的な反例 |
| 元の `prop:linear-factor-sharp` の族をそのまま fan-out 2 に持ち上げる | **反証済み** | §8.1。原稿の二穴反例を再現 |

**文献上の新規性：未調査。** 本報告の「証明済み」は以下に完全な証明を記した数学的主張に限る。原稿の一般的な復元定理・代表長による標本構成は、明示して利用する既存結果である。数値実験は「観測」として別記し、普遍命題の証明には用いない。

主目標 T1 は達成した。挑戦目標 T2 は、依頼が許す「非自明な群を含む固定型付け」の一例である**単項アルファベットの巡回群型付け**では上界側を達成した。ただし T1 の九文字アルファベットと同じ設定で上下界の指数が一致したわけではない。**多文字の群・LG 型付け一般では、二次上界と本報告の線形下界の間に ‖G‖ 一つ分が残る。**

## 1. 取得した原稿と定義の照合

対象：[Takayuki Kuriyama, main.tex](https://github.com/growupkuriyama-hub/papers/blob/main/02_fixed-h-mcfg/main.tex)。2026-10-30 の調査で `main` を取得した。

- **Git blob SHA：`970dad4a7f699af5599f09f792bb203cd8513000`**。
- 取得内容：217407 bytes。
- `SHA1(b"blob "+str(len(data)).encode()+b"\0"+data)` で一致を確認した。blob SHA と commit SHA は区別する。
- 可変の `main` の現在地ではなく、上記内容を本報告の照合版とする。
- プロジェクトマスター v15 の「現行原稿を数理的正本とする」「原典・計算・証明を混同しない」という方針に従う。過去の研究メモ、二文字 U₁ の定理、未査読のコンパニオン論文を本証明の前提には用いない。

| label／箇所 | 確認した内容と本報告との対応 |
|---|---|
| `def:standard-mcfg` | ‖G‖=|V|+Σ_R(1+rank(R)+テンプレートの端末・変数出現数)。非終端名のビット長ではなく記号単位のサイズ |
| `def:grammar-properties` | good は線形・非削除・非置換・非併合・λ-free。非併合は**同一の子の連続成分変数**を隣接させない条件。異なる子の一成分どうしの連接は許される |
| `def:tuple-substitutable` | 1≤d≤f、組の全成分は非空。E=v₀□₁v₁…□_dv_d の内部 v₁,…,v_{d−1} は非空、両端は空でもよい |
| `def:reconstruction` | B_{f,s}^{≤r} は rank cap r の標本復元作用素、B_{f,s} は uncapped。上界ではこの二作用素を対象とする |
| `def:uniform-polydata` | 固定 f,r,s,Σ の後で全 L、全 reduced good 表示 G を量化する。係数は G,L に依存してはならない |
| `lem:thickness-equivalence` | θ_G(R) は R を一度以上使う成功語の最短長、θ_G=max_R θ_G(R)、θ̄=max(1,θ_G)。各規則の最短成功使用は**別々に**取る。全規則を一導出で使う条件ではない |
| `thm:data-from-typed-thickness` | 特徴標本の語数≤N_typ。自明型では N_typ=|V|+|P|≤‖G‖。これを全表示に対するサイズ下界に用いる |
| `cor:distribution-representatives` | τ は生成組に限定しない同型・同分布の最短代表長。標本長≤N_typ(1+2θ̄+rτ)+1_{ε∈L}。単項群型付けの改善は τ を抑える |
| `lem:heavy-node-count` | λ-最小導出の経路上のラベル数が上界のもう一つの ‖G‖ 因子。今回の単項上界はこの経路評価を使わない |
| `thm:window-group-polydata` / `thm:local-group-polydata` | 現行の標本長上界は O(‖G‖²θ̄)。本下界で一般に一致したとは主張しない |
| `prop:rare-type` / `cor:typed-sandwich` | 各実現型の例を標本に要求する下界。本報告の T1 は型数に依存せず、全ての単語の必要性を示す |
| `prop:linear-factor-sharp` | 元の三文字族の線形因子下界は fan-out 1。今回、別の語形により高ファンアウトに拡張する |
| `thm:doubling-no-lift` / `lem:power-transfer` | 二穴での移送が元の下界族を壊すことを確認。新しい語形では各連に異なる文字を使い、複数のマーカーを残す |
| “Tightness of the exponents” | t_typ が大きい Σ⁺ の表示でも τ は小さくなり得る、という方法上の限界を確認。t_typ の下界を標本下界と同一視しない |

特徴標本の定義は、集合駆動型作用素 O に対して、有限 F⊆L が

\[
 F\subseteq K\subseteq L,\quad K\text{ finite}
 \quad\Longrightarrow\quad O(K)=L
\tag{1.1}
\]

を満たすこととする。出力が文法なら O(K) はその言語を意味する。符号長は ‖F‖₊=Σ_{w∈F}(|w|+1)。一般の逐次 Gold 学習器への下界とは主張しない。

## 2. 二つの準備補題

### 補題2.1：各文字が一つの辺を指定する経路

有向グラフで各文字がただ一つの辺をラベル付けしているとする。始点と終点を固定した経路のラベル言語を R とする。非空組 x,y が同じ許容文脈 E を共有し、E[x],E[y]∈R なら、各成分 x_j,y_j は同じ始点・終点を持つ経路である。従って任意の許容文脈 F について

\[
 F[x]\in R\quad\Longleftrightarrow\quad F[y]\in R.
\tag{2.1}
\]

**証明。** 各非空固定文字列の最初の文字からその始点、最後の文字からその終点が一意に決まる。全ての内部区切りが非空なので、各穴の両端の状態が固定される。先頭・末尾固定部が空の場合は、経路全体の指定始点・終点がその状態を決める。よって x_j と y_j の端点は一致する。F[x] が有効経路なら、成分ごとに同じ端点を持つ y_j と交換しても有効経路のままである。逆も同様。□

この補題は内部区切りが空でもよいという別の定義にはそのまま適用できない。本報告の全ての適用で、原稿の非空条件を使用する。

### 補題2.2：全削除対象がクラスに残る有限言語

有限 L の全ての部分集合がクラス C に属し、O が C 全体に特徴標本を持つ集合駆動型作用素とする。このとき L の特徴標本は L 自身に限る。

**証明。** F が L の特徴標本で w∈L\F とする。L′=L\{w}∈C の特徴標本 F′ を取り、H=F∪F′ と置く。H は有限で、F⊆H⊆L、かつ F′⊆H⊆L′。従って (1.1) より O(H)=L と O(H)=L′ が同時に成立し矛盾する。よって F=L。

逆に C 全体での仮定から L に何らかの特徴標本 F₀ が存在する。F₀⊆L より O(L)=L。L を含み L に含まれる有限集合は L だけなので、L 自身は特徴標本である。作用素の一般的な健全性・一貫性は仮定していない。□

## 3. T1 の言語族と、全部分集合に対する完全な証明

f≥1 を固定し、t=2f と置く。互いに異なる文字からなるアルファベット

\[
 \Sigma_f=\{a_1,\ldots,a_t,d_1,\ldots,d_t,z\}
\]

を固定する。したがって |Σ_f|=4f+1。q≥k≥1、M=2^k とし、

\[
 \begin{aligned}
 w_i&=a_1^i d_1 a_2^i d_2\cdots a_t^i d_t
       z^{t(q-i)+M}\qquad(0\le i\le q),\\
 L^{(f)}_{q,k}&=\{w_i:0\le i\le q\},\\
 W&=tq+M+t=2fq+2^k+2f.
 \end{aligned}
\tag{3.1}
\]

各 a_j,d_j は一文字であり、添字は文字名の一部として記法上付けている。全語の長さは W、語数は q+1。d_j は各語に一度だけ現れ、その1始まりの位置は

\[
 \operatorname{pos}_{w_i}(d_j)=j(i+1),
 \qquad
 \operatorname{pos}_{w_i}(d_v)-\operatorname{pos}_{w_i}(d_u)
 =(v-u)(i+1).
\tag{3.2}
\]

つまり、**一つのマーカーの絶対位置**も、**二つのマーカーの距離**も添字 i を決める。

### 定理3.1：hereditary な f-組代入可能性

任意の J⊆L^{(f)}_{q,k} は自明型付けの下で f-組代入可能である。従って、任意の固定型付け s:Σ_f⁺→S に対して

\[
 J\in\mathcal C^{\rm mcf}_{f,s_{\rm triv}}
 \subseteq\mathcal C^{\rm mcf}_{f,s}.
\tag{3.3}
\]

**証明。** J、1≤d≤f、任意の非空 d-組 x,y、許容文脈
E=v₀□₁v₁…□_dv_d を固定し、E[x]=w_i∈J、E[y]=w_j∈J とする。全ての文脈 F における受理を比較する。

まず

\[
 R=a_1^*d_1a_2^*d_2\cdots a_t^*d_tz^*
\tag{3.4}
\]

を考える。状態0,…,t、辺 a_h:(h−1)→(h−1)、d_h:(h−1)→h、z:t→t、始点0・終点tで R を認識する。各文字は一つの辺だけを指定する。補題2.1により F[x]∈R ⇔ F[y]∈R。また R の語は Parikh ベクトルで一意に決まる。文字の現れる順番が (3.4) に固定されているからである。Ψ を全ての文字数を数える Parikh 準同型とする。

**場合1：i=j。** E[x]=E[y] から
Σ_h Ψ(x_h)=Σ_h Ψ(y_h)。F[x]∈J なら F[x]∈R であり、F[y] も R に属して同じ Parikh ベクトルを持つ。従って F[y]=F[x]∈J。対称性により分布が一致する。

**場合2：i≠j。** 固定接頭部 v₀ にマーカーがあれば、その絶対位置が w_i,w_j で等しくなり (3.2) から i=j となる。固定接尾部 v_d でも、語長 W が共通なので、末尾からの距離から同じ矛盾が出る。従って両端固定部にマーカーはない。

内部固定部 v_h が二つのマーカー d_u,d_v を含めば、その距離は固定文字列中で同じであり、(3.2) から再び i=j。従って各内部固定部が持つマーカーは高々一つ。固定部全体には高々 d−1 個のマーカーしかない。

残りの少なくとも

\[
 t-(d-1)=2f-d+1\ge d+1
\]

個のマーカーは d 個の穴に入る。鳩の巣原理により、x のある成分は二つ以上のマーカーを含む。その成分にあるマーカー間距離により、**x を埋めて L^{(f)}_{q,k} の語になる場合の添字は必ず i**である。同様に y も、受理される場合の添字を j に固定する。

任意の F について F[x]∈J とする。この添字固定性から F[x]=w_i=E[x]。従って

\[
 \Psi(F_{\rm fix})
 =\Psi(w_i)-\sum_h\Psi(x_h)
 =\Psi(E_{\rm fix}).
\]

ゆえに Ψ(F[y])=Ψ(E[y])=Ψ(w_j)。補題2.1で F[y]∈R でもあるので、R の Parikh 一意性により F[y]=w_j∈J。逆向きも同様。よって全分布が等しい。

以上は任意の J,d,x,y,E,F についての証明である。空の J では前件が成立せず自明。各 J は有限なので、語を定数規則として列挙する CFG を持ち、f-MCFL でもある。自明型での条件はどの型付けの同型組についても適用できるため、(3.3) が従う。□

**二穴に限った核心。** f=2 ではマーカー四つ。異なる添字を共有する文脈は、両端にマーカーを置けず、中央にも高々一つしか置けない。残る三つ以上のマーカーを二穴に入れると、必ず一方の成分に二つ残る。これが「どの語の組か」を固定する。単一文字の連を別の場所へ移すことだけでは、他の添字の語を新たに作れない。

## 4. rank 2、fan-out f の圧縮表示

非終端 P₀,…,P_q は fan-out f、S₀,…,S_q と C₀,…,C_k は fan-out 1。開始記号は S_q。規則は次の通り。

\[
\begin{array}{ll}
 P_0\to(d_1,d_3,\ldots,d_{2f-1}),\\
 P_i\to
 (a_1\xi_1^1a_2,\ a_3\xi_1^2a_4,\ldots,
  a_{2f-1}\xi_1^fa_{2f})(P_{i-1})
 & (1\le i\le q),\\
 S_j\to
 (\xi_1^1d_2\xi_1^2d_4\cdots\xi_1^fd_{2f}\xi_2^1)(P_j,C_k)
 & (0\le j\le q),\\
 S_j\to(\xi_1^1 z^{2f})(S_{j-1})
 & (1\le j\le q),\\
 C_0\to z,\qquad
 C_h\to(\xi_1^1\xi_2^1)(C_{h-1},C_{h-1})
 & (1\le h\le k).
\end{array}
\tag{4.1}
\]

f=1 の第三行は ξ₁¹d₂ξ₂¹ と読む。

### 命題4.1：表示の正確な評価

(4.1) の文法を G^{(f)}_{q,k} とすると reduced good、rank cap 2、fan-out f であり、

\[
 \begin{aligned}
 L(G^{(f)}_{q,k})&=L^{(f)}_{q,k},\\
 \|G^{(f)}_{q,k}\|&=(7f+11)q+6k+3f+10
 \le(7f+17)(q+1),\\
 \bar\theta_{G^{(f)}_{q,k}}&=W.
 \end{aligned}
\tag{4.2}
\]

**証明。** P_i の唯一の組は

\[
 (a_1^id_1a_2^i,\ a_3^id_3a_4^i,\ldots,
 a_{2f-1}^id_{2f-1}a_{2f}^i)
\]

である。C_h は z^{2^h} を生成する。S_q から q−i 回の S_j→S_{j−1}z^{2f} を経て P_i,C_k を結合すると、ちょうど w_i が得られる。逆に全導出はこの形なので他の語はない。

全規則で各変数は一度ずつ使われ、同じ子の変数は順序通り。P_i の各成分には変数が一つだけである。S_j の結合規則では P_j の連続成分の間に d₂,d₄,… があり、非併合条件を満たす。C_h の隣接変数は異なる二つの子のものである。全テンプレート成分は非空。各 S_j は S_q から到達でき、そこから P_j と C_k、さらにその下位の全非終端へ到達できる。全非終端は生成可能。従って reduced good である。

非終端数は 2q+k+3。規則の個数・一規則のサイズは以下の通り。

| 規則群 | 個数 | 一規則のサイズ |
|---|---:|---:|
| P₀ 定数 | 1 | f+1 |
| P_i の伸長 | q | 3f+2 |
| S_j の結合 | q+1 | 2f+4 |
| S_j の z 追加 | q | 2f+3 |
| C₀ 定数 | 1 | 2 |
| C_h の倍増 | k | 5 |

これらと非終端数を加えると (4.2) のサイズ式になる。k≤q と 3f+10≤7f+17 を使えば右の上界を得る。全成功語長が W で、全規則に成功使用があるから、各規則の最短成功使用も W、従って θ̄=W。□

**f=2 の具体形。** アルファベットを {a,b,c,d,A,B,C,D,z} とすれば

\[
 w_i=a^i A b^i B c^i C d^i D z^{4(q-i)+2^k},
 \quad W=4q+2^k+4,
 \quad\|G_{q,k}^{(2)}\|=25q+6k+16.
\tag{4.3}
\]

文字 d は連の文字、D はマーカーであり、別の文字である。

## 5. 特徴標本下界と、全表示へのサイズ下界

### 定理5.1：T1 の達成

f≥1、任意の型付け s を Σ_f 上で固定する。q≥k≥1 とし、L=L^{(f)}_{q,k} とする。

1. C^{mcf}_{f,s} 全体で特徴標本を持つ任意の集合駆動型作用素について、L の特徴標本は L 自身だけである。
2. L の**任意の reduced good fan-out≤f 表示 G**について
   \[
   \bar\theta_G=W,\qquad\|G\|\ge q+1.
   \tag{5.1}
   \]
   規則ランクを二に制限しない表示にも、この二つの下界は成立する。
3. (4.1) の表示に対し、全ての特徴標本 F は
   \[
   \|F\|_+=(q+1)(W+1)
   \ge\frac1{7f+17}\,\|G^{(f)}_{q,k}\|\bar\theta_{G^{(f)}_{q,k}}.
   \tag{5.2}
   \]

**証明。** (1) は定理3.1と補題2.2から従う。

(2) の厚さは、全成功語の長さが W であることと reduced 性から直ちに従う。任意の G に対し、同じ G を**自明型付け**で考える。定理3.1により L は自明型でもクラスに属する。原稿 `thm:data-from-typed-thickness` は、uncapped の B_{f,s_triv} に対して高々 |V|+|P|≤‖G‖ 語からなる特徴標本を与える。一方 (1) を自明型の canonical 作用素に適用すると、その標本は L 全体を含まなければならず、語数は q+1。従って ‖G‖≥q+1。この議論は fan-out≤f の全ての G に適用でき、特定の規則表の不可圧縮性を仮定していない。

(3) は F=L と ‖G^{(f)}_{q,k}‖≤(7f+17)(q+1)、θ̄=W を合わせたもの。□

### 5.2 T1 の定数と漸近的最小性

f=2 では c₁=c₂=1、標本下界の c=1/31。q=k=n とすると

\[
 \|G_n\|=31n+16,\quad
 \bar\theta_{G_n}=2^n+4n+4,\quad
 \|F\|_+=(n+1)(2^n+4n+5).
\tag{5.3}
\]

最小表示サイズは n+1 以上、提示表示は31(n+1)以下なので、提示文法は最小サイズの定数倍以内である。不要非終端・不要規則を追加して比率を作っていない。k を固定し q→∞ とする別の系列でも線形因子が必要であり、この場合 θ̄=Θ(q)。

### 5.3 上界との対応

自明型では元の上界 O(‖G‖θ̄) と (5.2) が、全ての固定 fan-out で定数因子まで一致する。任意の型付け s に対して下界自体は成立するが、群・LG 型付けの一般上界 O(‖G‖²θ̄) との残る差はまだ ‖G‖ 一つである。

この族では、任意の表示で t_typ≤W である。各生成組が成功語に埋め込まれ、非削除性によりその総長は≤Wだからである。型付き開始非終端の最短語は W なので t_typ=W。同様に μ*=τ=W。従ってこの族は**経路因子を必要とする下界ではない**。語数 q+1 を標本に要求することが下界の源である。

### 5.4 一般 f への拡張の量化

証明したのは「各固定 f ごとに、固定アルファベット Σ_f と族を与える」である。Σ_f は n,q,k と独立だが f に依存する。同じ九文字アルファベットの同じ族が全ての f で hereditary である、とは主張しない。f を増やすと穴でより多くのマーカーを分割できるためである。

## 6. T2 の上界側：単項の非自明巡回群型付け

本節からは別の固定アルファベット Σ={a} を使う。m≥2 を固定し、s(a)=1∈ℤ_m、従って s(a^n)=n mod m とする。これは非自明な群を正語像に持つ型付けである。

### 定理6.1：単項型付き代入可能言語の正確な形

A⊆ℤ_{>0}、L_A={a^n:n∈A} とする。L_A が一穴 s-代入可能であることは、次のどちらかと同値である。

- **有限の場合：** A は有限で、各 mod m 剰余類に高々一つの元を持つ。
- **無限の場合：** m の正の倍数 P と、mod m で互いに異なる剰余を持つ集合 R⊆{0,…,P−1} が存在し、
  \[
  A=\{n\ge1:n\bmod P\in R\}.
  \tag{6.1}
  \]
  すなわち |R|≤m。

さらに、このいずれかを満たす言語は全ての arity で組代入可能である。

**必要性の証明。** u,v∈A、u<v、u≡v (mod m) とし、δ=v−u>0 とする。x=a、y=a^{1+δ} は同型で、文脈 a^{u−1}□ を共有する。代入可能性から任意の n≥1 について

\[
 n\in A\quad\Longleftrightarrow\quad n+\delta\in A
\tag{6.2}
\]

が成立する。実際、文脈 a^{n−1}□ で x,y を比較すればよい。有限 A でこのような u,v があれば (6.2) により無限個の長さが生じるため矛盾し、有限の場合の形を得る。

無限 A なら鳩の巣原理により正の差 δ が少なくとも一つある。全ての同剰余受理長差の正値を集めた集合 D を取り、P=gcd(D) とする。D⊆mℤ なので m|P。(6.2) により各 δ∈D は A の正の全域での周期である。

gcd も周期であることを境界込みで確認する。一つの δ₀∈D を使い、整数 z に対し z+tδ₀≥1 となる十分大きい t での所属により A の指示関数を ℤ 全体に拡張する。(6.2) により t の選び方に依らない。各 δ∈D もこの拡張の周期となる。D の有限部分で gcd=P が得られ、Bézout の等式から P は整数周期の整数線形結合なので周期である。元の正整数への制限を戻せば (6.1)。

もし異なる r,r′∈R が mod m で等しければ、それぞれの剰余にある正の受理長を選ぶと、その差は m の倍数だが P の倍数ではない。これは D の全要素が P の倍数であることに反する。従って R は mod m で相異なる。

**十分性、全 arity の証明。** 同型の d-組 x,y が E を共有すると、総長 T_x,T_y は mod m で等しく、受理語の全長も mod m で等しい。有限の場合は各剰余に受理長が一つしかないので E[x],E[y] の長さは等しく、T_x=T_y。任意の F でも全長が等しく、受理は一致する。

無限の場合、E[x],E[y] は mod m で同じなので (6.1) の同一の r∈R に対応する。従って T_x≡T_y (mod P)。任意の F について F[x],F[y] の長さも mod P で等しく、受理が一致する。全成分が非空なので、全ての填充語は正の長さであり、0 の境界問題は生じない。□

この定理は文法を仮定せずに成り立つ。結果としてこれらの言語は全て正則である。ε の所属は非空組の分布に影響せず、独立に扱える。

## 7. 周期を元の規則厚さで抑える

### 補題7.1：受理長を θ̄−μ 以下ずつ減らせる

G を任意の非空言語の reduced good MCFG、μ を最短成功語長、θ=θ̄_G とする。長さℓ>μの成功語から、別の成功語の長さℓ′を得られて

\[
 1\le\ell-\ell'\le\theta-\mu.
\tag{7.1}
\]

**証明。** 非終端 B の最短組総長を d_B、B 部分木を除いた成功導出の外側固定部の最短総長を o_B とする。規則 R:B→ρ(B₁,…,B_r) の端末数を c_R とすれば、線形性・非削除性により

\[
 \theta_G(R)=o_B+c_R+\sum_jd_{B_j}.
\tag{7.2}
\]

外側と各子を独立に最短で選ぶことで右辺を実現でき、どの成功使用も各項を下回れないので等号である。また o_B+d_B≥μ。

長さℓ>μの導出で、自分の非終端に対する最短組長より長い生成組を持つ最深の節点を選ぶ。根がその性質を持つので存在する。子の組長は全て最短であり、その節点の規則を R とすると、最短 B-組への置換による減少量は

\[
 \Delta=c_R+\sum_jd_{B_j}-d_B>0.
\]

(7.2) と o_B+d_B≥μ より Δ≤θ_G(R)−μ≤θ−μ。導出は正当なまま、非削除性により全長がちょうど Δ 減る。□

### 命題7.2：単項群型付けでは τ≤2mθ̄

定理6.1の言語 L_A、任意の reduced good 表示 G、任意の fan-out cap f に対し

\[
 \tau(G,s)\le2m\bar\theta_G.
\tag{7.3}
\]

**証明。** θ=θ̄_G。まず A が有限とする。受理長の個数 h は≤m。最大受理長 M から補題7.1を繰り返して最小長 μ に至る下降列を作ると、下降回数≤h−1。従って

\[
 M\le\mu+(h-1)(\theta-\mu).
\]

h=1 なら M=μ≤θ、h≥2 なら M≤(h−1)θ≤mθ。全生成組は成功語に埋め込めるので総長≤M。従って τ≤t_typ≤M≤mθ。

次に A が無限で、(6.1) の P,R を取る。P 周期中に h=|R|≤m 個の受理剰余があるので、受理長の隣接する二項の間には、周期的に少なくとも P/h≥P/m の空隙が現れる。十分大きい隣接受理長 u<v でその最大空隙を取る。補題7.1による v からの下降先は u 以下なので、

\[
 P/m\le v-u\le\theta-\mu,
 \qquad P\le m(\theta-\mu)\le m\theta.
\tag{7.4}
\]

任意の型付き非終端 X を取り、arity を d、生成組の成分長を n₁,…,n_d、総長を T とする。各成分型に対応する最小正長を ρ_j∈{1,…,m} とし、b=Σ_jρ_j≤md。元の文法で X の元非終端には総長≤θの無型組があるので、非空成分数 d≤θ。ゆえに b≤mθ。

T′を T mod P に合同な b 以上の最小整数とする。すると

\[
 b\le T'<b+P\le2m\theta.
\]

P は m の倍数であり T≡b (mod m) なので、T′−b は非負の m の倍数。長さ ρ₁+(T′−b),ρ₂,…,ρ_d の非空単項組 y を取れば、成分型は元の組と一致する。さらに総長は T と mod P で合同なので、任意の許容文脈で受理が一致する。従って y は X と同じ全分布を持つ代表で、必ずしも生成組である必要はない。この y の総長から (7.3) が従う。□

### 定理7.3：非自明な単項群型付けの線形サイズ上界

Σ={a}、s(a)=1∈ℤ_m、m≥2 とし、f,r≥1 を固定する。全ての L∈C^{mcf}_{f,s} と、その全ての reduced good fan-out≤f、rank≤r 表示 G に対して、B^{≤r}_{f,s} と B_{f,s} は

\[
 \begin{aligned}
 \|K\|_+
 &\le m^{fr}\|G\|\bigl(1+(2+2mr)\bar\theta_G\bigr)
      +\mathbf1_{\{\varepsilon\in L\}}\\
 &\le (3+2mr)m^{fr}\|G\|\bar\theta_G
      +\mathbf1_{\{\varepsilon\in L\}}
 \end{aligned}
\tag{7.5}
\]

の特徴標本を持つ。

**証明。** 非空成分の型は m 種類。元非終端一つの型付きコピーは高々 m^f、元規則一つのコピーは高々 m^{fr} であり、出力型は子型から一意に決まる。従って、補助開始記号を数えない原稿の N_typ について
N_typ≤m^f|V|+m^{fr}|P|≤m^{fr}‖G‖。fresh identity は非空成分に現れない。命題7.2と `cor:distribution-representatives` を組み合わせる。θ̄≥1 を使うと第二行。正語部分が空なら標本は ∅ または {ε} で、別途自明である。□

**m=2 の具体値。** fan-out 1、rank cap 2 なら 44‖G‖θ̄+1_{ε∈L}。fan-out 2、rank cap 2 なら 176‖G‖θ̄+1_{ε∈L}。固定型付けが非自明な群を持っていても、追加の経路因子 ‖G‖ が必ず必要になるわけではない。

**限界。** 単項の型付き言語の分類を使った証明であり、多文字アルファベットでの同じ群型付けには適用しない。また T1 の多文字下界と (7.5) を同一の固定型付けでの上下界一致として結び付けてはならない。

## 8. 失敗した構成と未解決の範囲

### 8.1 具体的な失敗証明書

**(a) 元の三文字族。** L_{2,1}={aadccdaa,adaccada,daaccaad} で

\[
 x=(d,ac),\quad y=(da,c),\quad
 E=(\varepsilon,a,caad),\quad F=(\varepsilon,ac,aad).
\]

E[x]=E[y]=daaccaad∈L_{2,1}、F[y]=daaccaad∈L_{2,1} だが F[x]=dacacaad∉L_{2,1}。両方の内部区切りは非空。この族は全体ですでに二穴条件に反する。

**(b) 二つの独立した端の長さを移送する簡単な族。**
U_i=a^iDzzEb^{3−i}、J={U₀,U₁,U₃} とする。

\[
 x=(D,Ebb),\quad y=(aaD,E),\quad
 E=(a,zz,\varepsilon),\quad F=(\varepsilon,zz,b).
\]

E[x]=U₁、E[y]=U₃、F[x]=U₀ は J に属するが、F[y]=U₂∉J。全体集合が代入可能でも、任意の部分集合まで保存されるとは限らない。

**(c) 新構成のマーカーを三つに減らす。**

\[
 J=\{ABCz^{11},\ aAbBcCz^8\},\quad
 x=(A,Cz^8),\quad y=(aAb,cCz^5),
\]

E=(ε,B,z³)、F=(a,bBc,ε) とすると、E[x]=ABCz¹¹、E[y]=aAbBcCz⁸、F[x]=aAbBcCz⁸ は J に属するが、F[y]=aaAbbBccCz⁵ は属さない。内部区切りは B と bBc で非空。三つのマーカーは「穴・中央・穴」に一つずつ分かれ、どの成分にも距離による添字識別が残らない。

二マーカー版も、J={ABz⁸,aAbBz⁶}、x=(A,z⁶)、y=(aAb,z⁴)、E=(ε,B,z²)、F=(a,bB,ε) で同様に失敗する。F[y]=aaAbbBz⁴ が強制される。これらは §11 のログで文字列連結を直接検証している。

### 8.2 なぜ T1 の族だけでは T2 の二次下界にならないか

全受理語が W なので、全表示で θ̄=W。O(q) 語それぞれの長さを qW にしても θ̄ 自体が qW になり、比率は増えない。長い語を短絡で作る案では、短絡の使用を含む他の受理語が必要となり、「全語が同じ長さ」という保護を失う。

型を変えて短絡からの同一視を避けることは原理的には可能だが、固定群では型数は一定である。個々の長語が必要であることを示すには、単なる稀な型の存在では足りず、長語を削除した対象が同じクラスに残る等の別の議論が必要になる。本報告では、その条件を満たす短絡付き多文字群型付けの族を構成できていない。

### 8.3 残る多文字 T2 に十分な、正確な未証明命題

T1 は完結しているため、そのための未証明補題は残らない。多文字 T2 の上界側については次が十分である。

**未証明命題 MR。** Σ={a,b,c}、g(a)=1、g(b)=g(c)=0∈ℤ₂、fan-out cap 1、rank cap 2 を固定する。ある C>0 が存在して、全ての L∈C^{mcf}_{1,g}、全ての reduced good 表示 G、各非終端 A の厚さ補題で得られる導出文脈 E_A、各実現型 t について、

\[
 g(v)=t,\qquad E_A[v]\in L,\qquad |v|\le C\bar\theta_G
\]

を満たす非空 v が存在する。

**十分性。** 任意の A_t 生成語と v は同型で E_A を共有するため、代入可能性により全分布が一致する。よって τ≤Cθ̄ となり、原稿の代表長による系が O(‖G‖θ̄) を与える。これは v が A から生成されることを要求しない。MR 自体は証明していない。

下界側の別の十分条件は、同じような固定多文字群型付けについて、全削除言語 L_n\{w} がクラスに残る Ω(n) 個の語 w（それぞれ長さΩ(nθ_n)）を持つ L_n と、サイズΘ(n)、元の厚さΘ(θ_n)の漸近的最小表示を構成することである。補題2.2の削除論法がそれらの語を全て要求する。この条件を実現する族も未構成である。

## 9. 計算の設計、範囲、観測

### 9.1 厳密な有限判定器

`occurrences` は、全ての非空成分と非空内部区切りの出現を列挙する。有限言語 L について全ての組 x と文脈 E に対し E[x]∈L となるものを記録する。L に現れない組は分布が空なので、代入可能性の前件を満たさない。従って有限語の最大長までの出現列挙は有限言語に対する**完全判定**であって、無限対象の打切り判定ではない。

全部分集合の判定には次の有限基準を使う。

**補題9.1（保守的な四隅の基準）。** 有限 L の全ての部分集合が自明型で f-組代入可能であることは、任意の d≤f、任意の非空組 x,y、任意の許容 E,F について

\[
 u=E[x]\in L,\quad v=E[y]\in L,\quad w=F[x]\in L
 \ \Longrightarrow\ F[y]\in\{u,v,w\}
\tag{9.1}
\]

が成立することと同値である。

**証明。** 全部分集合で成立するなら、J={u,v,w} に代入可能性を適用して F[y]∈J。逆に (9.1) があれば、任意の J⊆L で u,v,w∈J のとき F[y]∈{u,v,w}⊆J。x,y を交換して逆包含も得る。□

これにより、L の全出現の台帳を一度作ることで指数個の部分集合を正確に扱える。別途小さい例では部分集合を実際に全列挙して、独立に照合した。**定理3.1はこの有限観測を用いずに証明している。**

### 9.2 文法の計算

MCFG の各規則を、左辺、子非終端列、成分ごとの端末・変数列として保持する。各変数の一回使用、子内の順序、非併合、非空テンプレート、rank≤2、到達性・生成可能性を検証する。

inside(A) は最短生成組総長、outside(A) は成功導出から A 部分木を除いた固定部の最短総長。各規則の最短成功使用は (7.2) で個別に求める。今回の文法は非循環なので inside は再帰的動的計画、outside は最小値の伝播で正確に計算できる。小さい n では全生成組も列挙し、(3.1) の明示集合との一致を検証する。

### 9.3 観測の範囲と結果

- **文法40件：** f=1,2,3,4、q=k=n=1,…,10。サイズ・各規則の最短成功使用長を厳密計算。n≤5 では言語全体も展開し明示族と一致。
- **全部分集合の厳密判定9件：** f=1,2 で q=1,…,4、k=1、および f=3,q=k=1。各ケースで全ての d≤f を検査し、全部分集合が通過した。
- **部分集合の直接全列挙：** f=2,k=1,q=1,2,3。それぞれ4,8,16部分集合を個別に検査し、全て通過。
- **失敗例：** 1～3マーカーへの削減、元の L_{2,1}、簡単な二端分割族。全て違反証明書の文字列連結を再検証。
- **単項有限言語：** A⊆{1,…,10} の全1024集合を、m=2,3それぞれで一穴・二穴まで厳密判定。定理6.1の有限の場合と全て一致。通過は m=2で36、m=3で80。
- **単項周期モデル：** m=2,3、P=m,2m,…,5m、mod m で重複しない全非空 R。520モデルについて、arity 1,2,3、各成分長1,…,2Pの計8665994組で代表構成を計算。型・総長の合同・長さ上限と四つの固定長文脈での一致を検証。これは**観測**であり、全長・全文脈の主張は §6–§7 の解析的証明による。

fan-out 2、q=k=n の主要数値：

| n | ‖G_n‖ | θ̄=W | 必須語数 | 必須総符号長 |
|---:|---:|---:|---:|---:|
| 1 | 47 | 10 | 2 | 22 |
| 2 | 78 | 16 | 3 | 51 |
| 3 | 109 | 24 | 4 | 100 |
| 4 | 140 | 36 | 5 | 185 |
| 5 | 171 | 56 | 6 | 342 |
| 6 | 202 | 92 | 7 | 651 |
| 7 | 233 | 160 | 8 | 1288 |
| 8 | 264 | 292 | 9 | 2637 |
| 9 | 295 | 552 | 10 | 5530 |
| 10 | 326 | 1068 | 11 | 11759 |

実行は Python 3.12.14、標準ライブラリのみ。末尾に再現ソースと最終実行の標準出力・標準エラー全文を収録する。実行成功は普遍命題の証明の代用ではない。

## 10. 論文に挿入する英語 LaTeX 案

以下は定理と証明の挿入案である。既存の `prop:linear-factor-sharp` の後に高ファンアウト版を追加し、単項結果を別節に置くことを想定する。多文字群型付けの二次下界が得られたとは書かない。

```latex
\begin{proposition}[The linear size factor at every fixed fan-out]
\label{prop:linear-factor-sharp-higher-fanout}
Fix $f\ge1$ and let
$\Sigma_f=\{a_1,\ldots,a_{2f},d_1,\ldots,d_{2f},z\}$
consist of distinct letters. For $q\ge k\ge1$, put $M=2^k$,
$W=2fq+M+2f$, and
\[
 w_i=a_1^id_1a_2^id_2\cdots a_{2f}^id_{2f}
 z^{2f(q-i)+M},\qquad
 L^{(f)}_{q,k}=\{w_i:0\le i\le q\}.
\]
For every typing $s$ on $\Sigma_f$, the following hold.
\begin{enumerate}
\item Every subset of $L^{(f)}_{q,k}$ belongs to
$\Cmcf{f}{s_{\mathrm{triv}}}\subseteq\Cmcf{f}{s}$.
\item Every set-driven operator admitting characteristic samples
throughout $\Cmcf{f}{s}$ has $L^{(f)}_{q,k}$ itself as the only
characteristic sample of this language.
\item There is a reduced good presentation $G^{(f)}_{q,k}$ of
fan-out $f$ and rank two with
\[
 \|G^{(f)}_{q,k}\|=(7f+11)q+6k+3f+10
 \le(7f+17)(q+1),\qquad
 \bar\theta_{G^{(f)}_{q,k}}=W.
\]
Every reduced good fan-out-$\le f$ presentation $G$ of this
language satisfies $\bar\theta_G=W$ and $\|G\|\ge q+1$.
\end{enumerate}
Consequently every characteristic sample $F$ in (ii) satisfies
\[
 \|F\|_+=(q+1)(W+1)
 \ge\frac{1}{7f+17}\|G^{(f)}_{q,k}\|
                         \bar\theta_{G^{(f)}_{q,k}}.
\]
\end{proposition}

\begin{proof}
Let
$R=a_1^*d_1\cdots a_{2f}^*d_{2f}z^*$.
It is the path language from state $0$ to state $2f$ in the graph
with loops $a_j$ at state $j-1$, edges $d_j:j-1\to j$, and a
loop $z$ at state $2f$. Each letter specifies one edge.
If two nonempty tuples share an admissible context producing
words in $R$, their corresponding components have the same path
endpoints: each nonempty internal separator fixes its endpoints,
and empty exterior strings use the prescribed endpoints of the
whole path. Hence replacement of one tuple by the other preserves
membership in $R$ in every context. Also, a word of $R$ is uniquely
determined by its Parikh vector $\Psi$.

Fix $J\subseteq L^{(f)}_{q,k}$, an arity $d\le f$, and a common
accepting context $E$ with $E[\tuple x]=w_i$ and
$E[\tuple y]=w_j$ in $J$. If $i=j$, the sums of the component
Parikh vectors agree. In any accepting context $F$, the two
fillings are therefore the same word of $R$, and membership in
$J$ agrees.

Suppose $i\ne j$. The position of $d_h$ in $w_i$ is $h(i+1)$.
Since all words have length $W$, a marker in either exterior
fixed part of $E$ would imply $i=j$. Likewise, two markers in
one internal fixed part would have distance $(v-u)(i+1)$ and
would imply $i=j$. Thus at most $d-1$ markers lie in the fixed
part of $E$. At least $2f-d+1\ge d+1$ markers lie in the $d$
holes. Some component of $\tuple x$ contains two markers, whose
distance fixes the index $i$ of every accepted word containing
that tuple. The same holds for $\tuple y$ and $j$.

If $F[\tuple x]\in J$, it follows that
$F[\tuple x]=w_i=E[\tuple x]$. Cancelling the tuple contribution
in the Parikh vectors gives
$\Psi(F_{\mathrm{fix}})=\Psi(E_{\mathrm{fix}})$.
Thus $F[\tuple y]\in R$ has Parikh vector $\Psi(w_j)$, so it is
$w_j\in J$. The reverse implication is symmetric. This proves
(i), including all arities at most $f$; finite languages are
context-free, and trivial typing implies every finer typing.

For (ii), if a characteristic sample omits $w$, the language
$L'=L^{(f)}_{q,k}\setminus\{w\}$ still belongs to the class.
The union of the alleged sample and a characteristic sample of
$L'$ is a finite subset of $L'$ on which the same set-driven
operator would have to output both languages. Conversely, the
whole finite target is characteristic whenever some characteristic
sample exists.

For (iii), use fan-out-$f$ nonterminals $P_0,\ldots,P_q$ and
fan-out-one nonterminals $S_0,\ldots,S_q,C_0,\ldots,C_k$,
with start symbol $S_q$ and rules
\[
\begin{array}{ll}
P_0\to(d_1,d_3,\ldots,d_{2f-1}),\\
P_i\to(a_1\xi_1^1a_2,\ldots,
 a_{2f-1}\xi_1^fa_{2f})(P_{i-1}) &(1\le i\le q),\\
S_j\to(\xi_1^1d_2\xi_1^2d_4\cdots
 \xi_1^fd_{2f}\xi_2^1)(P_j,C_k)&(0\le j\le q),\\
S_j\to(\xi_1^1z^{2f})(S_{j-1})&(1\le j\le q),\\
C_0\to z,\qquad
C_h\to(\xi_1^1\xi_2^1)(C_{h-1},C_{h-1})&(1\le h\le k).
\end{array}
\]
The unique $P_i$-tuple consists of
$a_{2j-1}^id_{2j-1}a_{2j}^i$ for $1\le j\le f$.
Choosing the branch through $P_i$ after $q-i$ suffix steps
therefore yields exactly $w_i$. All variables occur once in order;
consecutive components of $P_j$ are separated by marker letters.
All templates are nonempty and every nonterminal is reachable
and productive, so the grammar is reduced and good.
There are $2q+k+3$ nonterminals; the six displayed rule groups
have counts $1,q,q+1,q,1,k$ and sizes
$f+1,3f+2,2f+4,2f+3,2,5$, respectively. This gives the stated size.

Every successful word has length $W$, so every reduced good
presentation has rule thickness $W$. For any fan-out-$\le f$
presentation, Theorem~\ref{thm:data-from-typed-thickness} with
trivial typing gives a characteristic sample with at most
$|V|+|P|\le\|G\|$ words. By (ii) that sample has $q+1$ words.
This proves the presentation-independent size lower bound.
The final inequality follows from (ii) and the displayed upper
bound on the size of our presentation.
\end{proof}

\begin{lemma}[Unary cyclic-group substitutability]
\label{lem:unary-group-language-form}
Fix $m\ge2$ and $s(a^n)=n\bmod m$. A positive unary language
$L=\{a^n:n\in A\}$ is one-dimensionally $s$-substitutable if and
only if either $A$ is finite with at most one member in each
residue class modulo $m$, or
\[
 A=\{n\ge1:n\bmod P\in R\},
\]
where $m\mid P$ and the residues in $R\subseteq\{0,\ldots,P-1\}$
are pairwise distinct modulo $m$. Each such language is tuple-
substitutable in every arity.
\end{lemma}

\begin{proof}
If $u<v$ are accepted lengths congruent modulo $m$, set
$\delta=v-u$. The strings $a$ and $a^{1+\delta}$ have the same
type and share the context $a^{u-1}\blank$. Substitutability gives
$n\in A\iff n+\delta\in A$ for all $n\ge1$.
Thus a finite $A$ cannot contain two such lengths.

For infinite $A$, let $D$ be the nonempty set of positive
differences between accepted lengths congruent modulo $m$ and
put $P=\gcd D$. All elements of $D$ are periods and multiples
of $m$. To handle the left endpoint, extend the indicator of
$A$ to all integers using any one period $\delta_0\in D$.
The extension is well-defined and every member of $D$ remains
a period. A finite subset of $D$ has gcd $P$, so Bezout's identity
makes $P$ a period. Restricting back to positive integers gives
the stated form. Two accepted residues modulo $P$ congruent
modulo $m$ would yield a difference in $D$ not divisible by $P$,
a contradiction.

Conversely, equal-type tuples sharing a context have total
lengths congruent modulo $m$. In the finite case their accepted
fillings must have equal lengths. In the periodic case they must
have the same accepted residue modulo $P$. The tuple totals are
therefore equal, or congruent modulo $P$, respectively. The same
remains true after filling any other admissible context, proving
tuple substitutability in every arity.
\end{proof}

\begin{proposition}[Linear-size data for unary group typings]
\label{prop:unary-group-linear-data}
For $\Sigma=\{a\}$ and $s(a)=1\in\mathbb Z_m$, $m\ge2$, every
reduced good presentation $G$ of a language in $\Cmcf{f}{s}$
satisfies
\[
 \tau(G,s)\le2m\bar\theta_G.
\]
For a fixed rank cap $r\ge1$, both canonical reconstruction
operators consequently have characteristic samples of length
\[
 (3+2mr)m^{fr}\|G\|\bar\theta_G
 +\mathbf1_{\{\varepsilon\in L\}}.
\]
\end{proposition}

\begin{proof}
Write $\theta=\bar\theta_G$ and let $\mu$ be the shortest positive
accepted length. We first verify a length-decrease bound for
arbitrary reduced good grammars. Let $d_B$ be the shortest tuple
length at $B$, and $o_B$ the shortest derivational outside length.
For a rule $R:B\to\rho(B_1,\ldots,B_t)$ writing $c_R$ terminals,
its shortest successful use has length
$o_B+c_R+\sum_jd_{B_j}$.
In a derivation longer than $\mu$, choose a deepest node whose
yield is not shortest for its nonterminal. Its children have
shortest lengths. Replacing it by a shortest yield decreases
the whole length by
$\Delta=c_R+\sum_jd_{B_j}-d_B>0$.
Since $o_B+d_B\ge\mu$, one has $\Delta\le\theta-\mu$.

By Lemma~\ref{lem:unary-group-language-form}, a finite positive
language has at most $m$ lengths. Repeated decreases imply that
its maximum length is at most $m\theta$. Every nonterminal yield
embeds into a successful word, so $\tau\le m\theta$ in this case.
For an infinite language use the period $P$ from that lemma.
There are at most $m$ accepted residues per period, so some
recurring gap between consecutive accepted lengths is at least
$P/m$. A decrease from the upper endpoint of such a gap is at
least the gap. Hence $P\le m(\theta-\mu)\le m\theta$.

For a typed nonterminal of arity $d$, let $T$ be the total length
of a generated tuple. Let $\rho_j\in\{1,\ldots,m\}$ be the
shortest positive length of its $j$th type, and put
$b=\sum_j\rho_j$. The untyped thickness bound gives $d\le\theta$,
so $b\le m\theta$. Choose the least $T'\ge b$ congruent to $T$
modulo $P$. Then $T'<b+P\le2m\theta$. Since $m\mid P$, the
nonnegative difference $T'-b$ is divisible by $m$. The tuple
with component lengths $\rho_1+T'-b,\rho_2,\ldots,\rho_d$
has the same types and the same distributions as the original
tuple: every filling has the same total length modulo $P$.
This proves the representative bound without requiring the
representative to be generated by that nonterminal.

Nonempty components realize only the $m$ group types, so
$N_{\mathrm{typ}}\le m^{fr}\|G\|$. Apply
Corollary~\ref{cor:distribution-representatives} and $\theta\ge1$.
The empty positive language is handled separately by the empty
sample, with $\varepsilon$ added when present.
\end{proof}
```

結論段落には、少なくとも次の区別が必要である：高ファンアウトの既知下界は本命題により Ω(‖G‖θ̄) へ強化されるが、多文字の群・LG の一般上界の残る因子は未解消。単項の非自明群型付けでは別途 O(‖G‖θ̄) が成り立つ。

## 11. 再現用 Python ソース全文と実行ログ全文

次のソースを `verify.py` として保存し、`python3 -u verify.py` で再現できる。標準ライブラリ以外を使用しない。生成する文字名は検証した f≤4 の範囲で全て相異なる。一般 f の定理は §3–§5 の記号アルファベット上の証明である。

最終実行は終了コード0、全62行、末尾は `ALL_ASSERTIONS_PASSED true`。先行の探索試行と最終検証を区別し、以下にはこの最終ソースの実行結果を省略せず載せる。

### 11.1 ソース全文

```python
#!/usr/bin/env python3
"""Standard-library exact finite-language and MCFG checks.
All components and all internal separators are strictly nonempty.
Experiments do not replace the analytic proofs in the accompanying report.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product, combinations
from fractions import Fraction
import json, sys


def out(tag, data):
    print(tag, json.dumps(data, ensure_ascii=False, sort_keys=True), flush=True)


def occurrences(w, d):
    def rec(pos, xs, es):
        if len(xs) == d:
            yield tuple(xs), tuple(es + [w[pos:]])
            return
        lower = pos if not xs else pos + 1
        for i in range(lower, len(w)):
            for j in range(i+1, len(w)+1):
                yield from rec(j, xs+[w[i:j]], es+[w[pos:i]])
    yield from rec(0, [], [])


def fill(E, x):
    return ''.join(a+b for a,b in zip(E,x)) + E[-1]


def ledger(L, d):
    D, groups = defaultdict(dict), defaultdict(set)
    for w in sorted(L):
        for x,E in occurrences(w,d):
            D[x][E] = w
            groups[E].add(x)
    return D,groups


def check(L, f=2):
    """Exact untyped substitutability for the finite language L."""
    for d in range(1,f+1):
        D,groups = ledger(L,d)
        for E,xs in sorted(groups.items()):
            xs=sorted(xs);x=xs[0]
            for y in xs[1:]:
                if D[x].keys() != D[y].keys():
                    F=min(D[x].keys() ^ D[y].keys())
                    return dict(d=d,x=x,y=y,E=E,F=F,
                                Ex=fill(E,x),Ey=fill(E,y),Fx=fill(F,x),Fy=fill(F,y))
    return None


def hereditary_check(L, f=2):
    """Exact all-subsets test via the conservative rectangle criterion."""
    counts=[]
    for d in range(1,f+1):
        D,groups=ledger(L,d);pairs=0
        for E,xs in sorted(groups.items()):
            for x,y in combinations(sorted(xs),2):
                pairs+=1
                if D[x] == D[y]:
                    continue
                u,v=fill(E,x),fill(E,y)
                for a,b in ((x,y),(y,x)):
                    for F,w in sorted(D[a].items()):
                        z=fill(F,b)
                        if z not in {u,v,w}:
                            J={u,v,w}
                            cert=dict(d=d,x=a,y=b,E=E,F=F,Ex=fill(E,a),
                                      Ey=fill(E,b),Fx=w,Fy=z)
                            return dict(subset=sorted(J),certificate=cert),counts
        counts.append(dict(d=d,tuples=len(D),contexts=len(groups),pairs=pairs))
    return None,counts


def validate(L,C):
    x,y,E,F=(C[k] for k in ('x','y','E','F'))
    assert len(x)==len(y) and all(x) and all(y)
    assert all(E[1:-1]) and all(F[1:-1])
    assert fill(E,x) in L and fill(E,y) in L
    assert (fill(F,x) in L) != (fill(F,y) in L)


def words(f,q,k):
    t=2*f;M=2**k
    return {''.join(chr(97+j)*i+chr(65+j) for j in range(t))+
            'z'*(t*(q-i)+M) for i in range(q+1)}


# Rule=(head, children, tuple of component templates).
# Template atoms are terminal strings or (child_index,component_index).
def grammar(f,q,k):
    fan={};R=[]
    for i in range(q+1):fan['P'+str(i)]=f;fan['S'+str(i)]=1
    for j in range(k+1):fan['C'+str(j)]=1
    R.append(('P0',(),tuple((chr(65+2*j),) for j in range(f))))
    for i in range(1,q+1):
        temp=tuple((chr(97+2*j),(0,j),chr(98+2*j)) for j in range(f))
        R.append(('P'+str(i),('P'+str(i-1),),temp))
    for i in range(q+1):
        temp=[]
        for j in range(f):temp.extend(((0,j),chr(66+2*j)))
        temp.append((1,0))
        R.append(('S'+str(i),('P'+str(i),'C'+str(k)),(tuple(temp),)))
    for i in range(1,q+1):
        R.append(('S'+str(i),('S'+str(i-1),),(((0,0),'z'*(2*f)),)))
    R.append(('C0',(),(('z',),)))
    for j in range(1,k+1):
        R.append(('C'+str(j),('C'+str(j-1),'C'+str(j-1)),(((0,0),(1,0)),)))
    return fan,R,'S'+str(q)


def validate_grammar(fan,R,S):
    graph=defaultdict(set)
    for a,ch,ts in R:
        assert len(ts)==fan[a] and all(ts) and len(ch)<=2
        refs=[z for t in ts for z in t if isinstance(z,tuple)]
        expected=[(j,k) for j,b in enumerate(ch) for k in range(fan[b])]
        assert sorted(refs)==sorted(expected)
        for j,b in enumerate(ch):
            assert [z[1] for z in refs if z[0]==j]==list(range(fan[b]))
        for t in ts:
            for x,y in zip(t,t[1:]):
                assert not (isinstance(x,tuple) and isinstance(y,tuple)
                            and x[0]==y[0] and x[1]+1==y[1])
        graph[a].update(ch)
    reachable={S};stack=[S]
    while stack:
        for b in graph[stack.pop()]:
            if b not in reachable:reachable.add(b);stack.append(b)
    assert reachable==set(fan)


def stats(fan,R,S,expand=True):
    validate_grammar(fan,R,S)
    byhead=defaultdict(list)
    for a,ch,ts in R:byhead[a].append((ch,ts))
    def terminals(ts):return sum(len(z) for t in ts for z in t if isinstance(z,str))
    @lru_cache(None)
    def inside(a):
        return min(terminals(ts)+sum(inside(b) for b in ch) for ch,ts in byhead[a])
    for a in fan:assert inside(a)>0
    outside={S:0};change=True
    while change:
        change=False
        for a,ch,ts in R:
            if a not in outside:continue
            for j,b in enumerate(ch):
                v=outside[a]+terminals(ts)+sum(inside(c) for i,c in enumerate(ch) if i!=j)
                if b not in outside or v<outside[b]:outside[b]=v;change=True
    rulemins=[outside[a]+terminals(ts)+sum(inside(b) for b in ch) for a,ch,ts in R]
    size=len(fan)+sum(1+len(ch)+sum(sum(len(z) if isinstance(z,str) else 1 for z in t)
                                  for t in ts) for a,ch,ts in R)
    @lru_cache(None)
    def yields(a):
        ans=set()
        for ch,ts in byhead[a]:
            for cs in product(*(yields(b) for b in ch)):
                ans.add(tuple(''.join(z if isinstance(z,str) else cs[z[0]][z[1]] for z in t) for t in ts))
        return frozenset(ans)
    L={z[0] for z in yields(S)} if expand else None
    return dict(size=size,theta=max(rulemins),rule_minima=rulemins,
                nonterminals=len(fan),rules=len(R)),L


def unary_check(A,m,f=2):
    """Exact finite unary checker: distributions depend on fixed total length."""
    if not A:return None
    N=max(A)
    for d in range(1,f+1):
        seen={}
        for xs in product(range(1,N+1),repeat=d):
            n=sum(xs)
            D=frozenset(v-n for v in A if v-n>=d-1)
            ty=tuple(v%m for v in xs)
            for c in sorted(D):
                key=(ty,c)
                if key in seen and seen[key][1]!=D:
                    ys,Dy=seen[key]
                    return dict(d=d,x=xs,y=ys,common=c,separating=min(D^Dy))
                seen[key]=(xs,D)
    return None


def main():
    out('ENV',dict(python=sys.version.split()[0],standard_library_only=True))
    for f in (1,2,3,4):
        for n in range(1,11):
            fan,R,S=grammar(f,n,n);st,L=stats(fan,R,S,expand=(n<=5))
            W=2**n+2*f*n+2*f
            assert st['size']==(7*f+17)*n+3*f+10
            assert st['theta']==W and set(st['rule_minima'])=={W}
            if L is not None:assert L==words(f,n,n)
            out('GRAMMAR',dict(f=f,n=n,size=st['size'],theta=W,
                words=n+1,sample_cost=(n+1)*(W+1),ratio=str(Fraction((n+1)*(W+1),st['size']*W))))
    for f,q,k in [(1,q,1) for q in range(1,5)]+[(2,q,1) for q in range(1,5)]+[(3,1,1)]:
        L=words(f,q,k)
        bad,counts=hereditary_check(L,f)
        assert bad is None
        out('HEREDITARY_EXACT',dict(f=f,q=q,k=k,words=len(L),all_subsets=2**len(L),counts=counts))
    for q in (1,2,3):
        L=sorted(words(2,q,1));total=0
        for mask in range(1<<len(L)):
            J={w for i,w in enumerate(L) if mask>>i&1}
            assert check(J,2) is None;total+=1
        out('DIRECT_SUBSETS',dict(f=2,q=q,tested=total,all_pass=True))
    # Fewer markers: full failure certificate, not an extrapolation.
    for t in (1,2,3):
        L={''.join(chr(97+j)*i+chr(65+j) for j in range(t))+
           'z'*(t*(3-i)+2) for i in (0,1)}
        cert=check(L,2);assert cert;validate(L,cert)
        out('TOO_FEW_MARKERS',dict(markers=t,subset=sorted(L),certificate=cert))
    old={'a'*i+'d'+'a'*(2-i)+'cc'+'a'*(2-i)+'d'+'a'*i for i in range(3)}
    cert=check(old,2);assert cert;validate(old,cert)
    out('ORIGINAL_FAMILY_FAILURE',dict(language=sorted(old),certificate=cert))
    simple={'a'*i+'DzzE'+'b'*(3-i) for i in (0,1,3)}
    C=dict(d=2,x=('D','Ebb'),y=('aaD','E'),E=('a','zz',''),F=('','zz','b'))
    validate(simple,C)
    out('ONE_SPLIT_FAILURE',dict(subset=sorted(simple),certificate=C,
                                forced=fill(C['F'],C['y'])))
    for m in (2,3):
        passing=0
        for mask in range(1<<10):
            A={i+1 for i in range(10) if mask>>i&1}
            predicted=len({a%m for a in A})==len(A)
            actual=unary_check(A,m,2) is None
            assert actual==predicted
            passing+=actual
        out('UNARY_FINITE_EXHAUSTIVE',dict(m=m,lengths='1..10',tested=1024,passed=passing))
    # Exact algebraic checks of the representative construction for periodic models.
    models=vectors=0
    for m in (2,3):
        for P in range(m,5*m+1,m):
            for h in range(1,m+1):
                for rs in combinations(range(P),h):
                    if len({r%m for r in rs})<h:continue
                    models+=1
                    for d in (1,2,3):
                        for lens in product(range(1,2*P+1),repeat=d):
                            base=[n%m or m for n in lens];b=sum(base);T=sum(lens)
                            Tnew=b+(T-b)%P
                            new=[base[0]+Tnew-b]+base[1:]
                            assert all(new) and all(a%m==b%m for a,b in zip(lens,new))
                            assert sum(new)%P==T%P and sum(new)<P+m*d
                            # These are finite observations; the proof handles all contexts.
                            for c in (d-1,d,d+P,2*P+d):
                                assert ((T+c)%P in rs)==((sum(new)+c)%P in rs)
                            vectors+=1
    out('UNARY_PERIODIC_REPRESENTATIVES',dict(models=models,tuple_cases=vectors,all_pass=True))
    out('ALL_ASSERTIONS_PASSED',True)

if __name__=='__main__':main()
```

### 11.2 実行ログ全文

```text
ENV {"python": "3.12.14", "standard_library_only": true}
GRAMMAR {"f": 1, "n": 1, "ratio": "7/111", "sample_cost": 14, "size": 37, "theta": 6, "words": 2}
GRAMMAR {"f": 1, "n": 2, "ratio": "33/610", "sample_cost": 33, "size": 61, "theta": 10, "words": 3}
GRAMMAR {"f": 1, "n": 3, "ratio": "1/20", "sample_cost": 68, "size": 85, "theta": 16, "words": 4}
GRAMMAR {"f": 1, "n": 4, "ratio": "135/2834", "sample_cost": 135, "size": 109, "theta": 26, "words": 5}
GRAMMAR {"f": 1, "n": 5, "ratio": "135/2926", "sample_cost": 270, "size": 133, "theta": 44, "words": 6}
GRAMMAR {"f": 1, "n": 6, "ratio": "553/12246", "sample_cost": 553, "size": 157, "theta": 78, "words": 7}
GRAMMAR {"f": 1, "n": 7, "ratio": "145/3258", "sample_cost": 1160, "size": 181, "theta": 144, "words": 8}
GRAMMAR {"f": 1, "n": 8, "ratio": "495/11234", "sample_cost": 2475, "size": 205, "theta": 274, "words": 9}
GRAMMAR {"f": 1, "n": 9, "ratio": "2665/60914", "sample_cost": 5330, "size": 229, "theta": 532, "words": 10}
GRAMMAR {"f": 1, "n": 10, "ratio": "1047/24058", "sample_cost": 11517, "size": 253, "theta": 1046, "words": 11}
GRAMMAR {"f": 2, "n": 1, "ratio": "11/235", "sample_cost": 22, "size": 47, "theta": 10, "words": 2}
GRAMMAR {"f": 2, "n": 2, "ratio": "17/416", "sample_cost": 51, "size": 78, "theta": 16, "words": 3}
GRAMMAR {"f": 2, "n": 3, "ratio": "25/654", "sample_cost": 100, "size": 109, "theta": 24, "words": 4}
GRAMMAR {"f": 2, "n": 4, "ratio": "37/1008", "sample_cost": 185, "size": 140, "theta": 36, "words": 5}
GRAMMAR {"f": 2, "n": 5, "ratio": "1/28", "sample_cost": 342, "size": 171, "theta": 56, "words": 6}
GRAMMAR {"f": 2, "n": 6, "ratio": "651/18584", "sample_cost": 651, "size": 202, "theta": 92, "words": 7}
GRAMMAR {"f": 2, "n": 7, "ratio": "161/4660", "sample_cost": 1288, "size": 233, "theta": 160, "words": 8}
GRAMMAR {"f": 2, "n": 8, "ratio": "879/25696", "sample_cost": 2637, "size": 264, "theta": 292, "words": 9}
GRAMMAR {"f": 2, "n": 9, "ratio": "553/16284", "sample_cost": 5530, "size": 295, "theta": 552, "words": 10}
GRAMMAR {"f": 2, "n": 10, "ratio": "11759/348168", "sample_cost": 11759, "size": 326, "theta": 1068, "words": 11}
GRAMMAR {"f": 3, "n": 1, "ratio": "5/133", "sample_cost": 30, "size": 57, "theta": 14, "words": 2}
GRAMMAR {"f": 3, "n": 2, "ratio": "69/2090", "sample_cost": 69, "size": 95, "theta": 22, "words": 3}
GRAMMAR {"f": 3, "n": 3, "ratio": "33/1064", "sample_cost": 132, "size": 133, "theta": 32, "words": 4}
GRAMMAR {"f": 3, "n": 4, "ratio": "235/7866", "sample_cost": 235, "size": 171, "theta": 46, "words": 5}
GRAMMAR {"f": 3, "n": 5, "ratio": "207/7106", "sample_cost": 414, "size": 209, "theta": 68, "words": 6}
GRAMMAR {"f": 3, "n": 6, "ratio": "749/26182", "sample_cost": 749, "size": 247, "theta": 106, "words": 7}
GRAMMAR {"f": 3, "n": 7, "ratio": "59/2090", "sample_cost": 1416, "size": 285, "theta": 176, "words": 8}
GRAMMAR {"f": 3, "n": 8, "ratio": "2799/100130", "sample_cost": 2799, "size": 323, "theta": 310, "words": 9}
GRAMMAR {"f": 3, "n": 9, "ratio": "2865/103246", "sample_cost": 5730, "size": 361, "theta": 572, "words": 10}
GRAMMAR {"f": 3, "n": 10, "ratio": "12001/434910", "sample_cost": 12001, "size": 399, "theta": 1090, "words": 11}
GRAMMAR {"f": 4, "n": 1, "ratio": "19/603", "sample_cost": 38, "size": 67, "theta": 18, "words": 2}
GRAMMAR {"f": 4, "n": 2, "ratio": "87/3136", "sample_cost": 87, "size": 112, "theta": 28, "words": 3}
GRAMMAR {"f": 4, "n": 3, "ratio": "41/1570", "sample_cost": 164, "size": 157, "theta": 40, "words": 4}
GRAMMAR {"f": 4, "n": 4, "ratio": "285/11312", "sample_cost": 285, "size": 202, "theta": 56, "words": 5}
GRAMMAR {"f": 4, "n": 5, "ratio": "243/9880", "sample_cost": 486, "size": 247, "theta": 80, "words": 6}
GRAMMAR {"f": 4, "n": 6, "ratio": "847/35040", "sample_cost": 847, "size": 292, "theta": 120, "words": 7}
GRAMMAR {"f": 4, "n": 7, "ratio": "193/8088", "sample_cost": 1544, "size": 337, "theta": 192, "words": 8}
GRAMMAR {"f": 4, "n": 8, "ratio": "2961/125296", "sample_cost": 2961, "size": 382, "theta": 328, "words": 9}
GRAMMAR {"f": 4, "n": 9, "ratio": "2965/126392", "sample_cost": 5930, "size": 427, "theta": 592, "words": 10}
GRAMMAR {"f": 4, "n": 10, "ratio": "12243/524864", "sample_cost": 12243, "size": 472, "theta": 1112, "words": 11}
HEREDITARY_EXACT {"all_subsets": 4, "counts": [{"contexts": 39, "d": 1, "pairs": 3, "tuples": 29}], "f": 1, "k": 1, "q": 1, "words": 2}
HEREDITARY_EXACT {"all_subsets": 8, "counts": [{"contexts": 97, "d": 1, "pairs": 14, "tuples": 60}], "f": 1, "k": 1, "q": 2, "words": 3}
HEREDITARY_EXACT {"all_subsets": 16, "counts": [{"contexts": 194, "d": 1, "pairs": 40, "tuples": 104}], "f": 1, "k": 1, "q": 3, "words": 4}
HEREDITARY_EXACT {"all_subsets": 32, "counts": [{"contexts": 340, "d": 1, "pairs": 90, "tuples": 163}], "f": 1, "k": 1, "q": 4, "words": 5}
HEREDITARY_EXACT {"all_subsets": 4, "counts": [{"contexts": 107, "d": 1, "pairs": 3, "tuples": 86}, {"contexts": 555, "d": 2, "pairs": 175, "tuples": 423}], "f": 2, "k": 1, "q": 1, "words": 2}
HEREDITARY_EXACT {"all_subsets": 8, "counts": [{"contexts": 302, "d": 1, "pairs": 16, "tuples": 210}, {"contexts": 3004, "d": 2, "pairs": 2583, "tuples": 1998}], "f": 2, "k": 1, "q": 2, "words": 3}
HEREDITARY_EXACT {"all_subsets": 16, "counts": [{"contexts": 650, "d": 1, "pairs": 50, "tuples": 410}, {"contexts": 10312, "d": 2, "pairs": 16151, "tuples": 6132}], "f": 2, "k": 1, "q": 3, "words": 4}
HEREDITARY_EXACT {"all_subsets": 32, "counts": [{"contexts": 1195, "d": 1, "pairs": 120, "tuples": 704}, {"contexts": 27382, "d": 2, "pairs": 66004, "tuples": 14908}], "f": 2, "k": 1, "q": 4, "words": 5}
HEREDITARY_EXACT {"all_subsets": 4, "counts": [{"contexts": 207, "d": 1, "pairs": 3, "tuples": 171}, {"contexts": 2308, "d": 2, "pairs": 904, "tuples": 1774}, {"contexts": 7223, "d": 3, "pairs": 6751, "tuples": 5764}], "f": 3, "k": 1, "q": 1, "words": 2}
DIRECT_SUBSETS {"all_pass": true, "f": 2, "q": 1, "tested": 4}
DIRECT_SUBSETS {"all_pass": true, "f": 2, "q": 2, "tested": 8}
DIRECT_SUBSETS {"all_pass": true, "f": 2, "q": 3, "tested": 16}
TOO_FEW_MARKERS {"certificate": {"E": ["", "z"], "Ex": "Azzzzz", "Ey": "aAzzzz", "F": ["a", ""], "Fx": "aAzzzz", "Fy": "aaAzzz", "d": 1, "x": ["Azzzz"], "y": ["aAzzz"]}, "markers": 1, "subset": ["Azzzzz", "aAzzzz"]}
TOO_FEW_MARKERS {"certificate": {"E": ["", "B", "zz"], "Ex": "ABzzzzzzzz", "Ey": "aAbBzzzzzz", "F": ["a", "bB", ""], "Fx": "aAbBzzzzzz", "Fy": "aaAbbBzzzz", "d": 2, "x": ["A", "zzzzzz"], "y": ["aAb", "zzzz"]}, "markers": 2, "subset": ["ABzzzzzzzz", "aAbBzzzzzz"]}
TOO_FEW_MARKERS {"certificate": {"E": ["", "B", "zzz"], "Ex": "ABCzzzzzzzzzzz", "Ey": "aAbBcCzzzzzzzz", "F": ["a", "bBc", ""], "Fx": "aAbBcCzzzzzzzz", "Fy": "aaAbbBccCzzzzz", "d": 2, "x": ["A", "Czzzzzzzz"], "y": ["aAb", "cCzzzzz"]}, "markers": 3, "subset": ["ABCzzzzzzzzzzz", "aAbBcCzzzzzzzz"]}
ORIGINAL_FAMILY_FAILURE {"certificate": {"E": ["", "a", "caad"], "Ex": "daaccaad", "Ey": "daaccaad", "F": ["", "ac", "aad"], "Fx": "dacacaad", "Fy": "daaccaad", "d": 2, "x": ["d", "ac"], "y": ["da", "c"]}, "language": ["aadccdaa", "adaccada", "daaccaad"]}
ONE_SPLIT_FAILURE {"certificate": {"E": ["a", "zz", ""], "F": ["", "zz", "b"], "d": 2, "x": ["D", "Ebb"], "y": ["aaD", "E"]}, "forced": "aaDzzEb", "subset": ["DzzEbbb", "aDzzEbb", "aaaDzzE"]}
UNARY_FINITE_EXHAUSTIVE {"lengths": "1..10", "m": 2, "passed": 36, "tested": 1024}
UNARY_FINITE_EXHAUSTIVE {"lengths": "1..10", "m": 3, "passed": 80, "tested": 1024}
UNARY_PERIODIC_REPRESENTATIVES {"all_pass": true, "models": 520, "tuple_cases": 8665994}
ALL_ASSERTIONS_PASSED true
```

再現ファイルの SHA-256：

- `verify.py`: `4cf48f00ee2eb5e771c3235fe396081a8e590bb50647bacd07998727e79cd35c`
- `verify.log`: `18c20d3e01bce45be969075dba9cb97a7c8d5ea8cd7fba9a41edd8697dc80217`

## 12. 自己点検

| 項目 | 点検結果 |
|---|---|
| 内部区切りの非空性 | **確認済み。** 経路端点の補題で不可欠。コードは前成分終了位置より真に後に次成分を開始する |
| 一穴と二穴の区別 | **確認済み。** T1 は任意の d≤f を一括証明し、f=2 では d=1,2 を検査。T2 は一穴から分類し、全 arity の十分性を別途証明 |
| 「全ての部分集合」を本当に量化したか | **はい。** 定理3.1は最初に任意の J を固定し、J の中で全文脈の分布一致を示す。有限検査からの外挿ではない |
| 任意の非空組・全文脈を扱ったか | **はい。** 共通受理文脈を持つ任意組に対する証明。非観測組は前件が偽。検査器もこの論理を明示 |
| ‖G‖ の下界は全 fan-out≤2 表示か | **はい。** 自明型の既存標本語数上界を任意の G に適用して q+1≤‖G‖ を導く。特定の導出形の仮定なし |
| θ̄ の下界は全表示か | **はい。** 全語長 W と reduced 性から全規則の最短成功使用が W。元の規則厚さを使用 |
| 提示文法は漸近的に最小か | **はい、定数倍の意味で。** f=2 では最小≥q+1、提示≤31(q+1)。rank2、good、reduced を確認 |
| 任意の作用素への下界と特定作用素への上界を区別したか | **はい。** T1 はクラス全体で特徴標本を持つ任意の集合駆動型作用素。T2 の上界は二つの canonical 作用素のみ |
| arbitrary Gold learner への下界と混同していないか | **はい。** (1.1) の集合駆動型特徴標本に限定 |
| t_typ、τ、実際の標本下界を区別したか | **はい。** T1 は全削除言語を使って標本自体を要求。T2 は生成されない代表を許して τ を評価 |
| f,r,s,Σ を族全体で固定したか | **はい。** f=2 は九文字固定。一般化は f ごとに4f+1文字を固定。n,q,k と独立。一つのΣで全f同時という結果ではない |
| 定数を明示したか | **はい。** T1 は c₁=c₂=1、c=1/31（一般fは1/(7f+17)）。単項上界は (3+2mr)m^{fr} |
| ε を扱ったか | **はい。** T1 の族に ε はない。T2 は正語部分を扱い、ε∈L なら1を加える。正語部分が空のケースを分離 |
| 群型付けの追加因子を一般に除いたと誤記していないか | **はい。** 単項巡回群では証明、多文字では未解決と冒頭・本文で区別 |
| 計算と証明を区別したか | **はい。** 数値結果を観測と明記。一般の部分集合閉性・群周期分類・代表長上界はいずれも解析的証明 |
| 再現コードとログは全文か | **はい。** 最終ソース全文とその最終実行の62行を収録。有限言語の全分布検査と周期モデルの有限観測を区別 |
| 原稿の取得版を特定したか | **はい。** blob `970dad4a7f699af5599f09f792bb203cd8513000`。指定の全labelと結論段落を照合 |
| 未査読コンパニオンの結果を前提にしたか | **いいえ** |
| 文献上の新規性 | **未調査** |
