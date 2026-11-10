ファンアウト2の境界問題：全体地図・障壁・有限群認識からの新しい短縮
2026-11-10

1. 冒頭の要約（5行）
[証明済み] 有限群で認識される非空言語では、内容付き SUB_1・SUB_2 は「有限可換群の一つの値の原像」と同値である。
[証明済み] 順序付き文字群×任意の可換群の一原像という新しい部分クラスで、全型の τ=O_{k,f,r}(θ^{2k}) を得た。有限群だけなら O(θ^k) に改善する。
[証明済み] 任意の群の単位元原像についても、正の像の単元群が可換であることが SUB_2 の必要十分条件である。
地図の量化・肯否の向き・τ とデータの混同を指摘し、B7 の反転漏れと、型条件を落とした B1 を反証した。
一般の正則標的、三文字以上の一般の τ、op:fanout-two 自体は未解決である。

2. 判定の表
主張 | ラベル | 判定 | 根拠
有限群認識＋内容 SUB_1 ⇒ 正規部分群の一つの剰余類 | [証明済み] | 成立 | 全内容の正の代表を使った統語合同 (§3.2)
上に SUB_2 を追加 ⇒ 商群は可換 | [証明済み] | 成立 | 中央を替える交換子の四語証明書 (§3.2)
任意群の単位元原像：SUB_2 ⇔ 正の像の単元群が可換 | [証明済み] | 成立 | 受理語の全因子は正の像の単元 (§3.3)
すべての内容 SUB_2 言語が可換不変量で認識される | [証明済み] | この一般化は偽 | a^+b^+c^+ は全 arity で代入可能だが順序を区別 (§3.4)
有限群認識部分クラスの全 τ ≤ k(f+((r+2)θ)^k-1) | [証明済み] | 成立 | 短い規則差分の格子と内容を保つ剰余短縮 (§4)
順序付き文字群×任意の可換群の一原像の全 τ | [証明済み] | O_{k,f,r}(θ^{2k}) | 階数不足も許す格子の直交象限短縮 (§4)
無型代入可能な部分標的では最短差 ≤ (r+2)θ | [証明済み] | 成立 | 元の G の短い証人をすべて含めば G 全体を含む (§3.1)
μ の上界だけ、または τ の下界だけで元の問題が解ける | [条件付き] | 不足 | τ→標本は上界のみ。逆向きには別の定理が必要 (§6)
地図の全詳細補題・全数値定数 | [条件付き] | 確認できず | 本報告の新証明には使用しない。点検範囲は §6 に限定

以下の [証明済み] は本報告内の数学的証明を指す。計算結果による格上げではない。
「新しい」は今回読めた地図・参照報告に対しての意味であり、未閲覧の約250回の全記録や文献上の優先権を保証するものではない。

3. 課題1：障壁の分析

3.0 記法と方向

G は文法、Γ は群とし、群を文法 G と混同しない。k=|Σ|、r は規則の最大 rank、θ=max(1,θ_G)。
本報告は「多項式データを示す方向」「下界を示す方向」と書く。
op:fanout-two の原文への YES は LG が境界のままであることであり、依頼 §2 の「肯定（境界が動く）」とは向きが逆である。
新しい上界は全て与えられた reduced good 表示そのものに対するもの。正規化・型付き積文法の厚さには移さない。

3.1 障壁 I：無型の部分標的では長い差を隠せない

命題 W0 [証明済み]。
G を reduced good、fan-out≤f、rank≤r とし、L=L(G)⊆Σ+ とする。
L'⊊L が無型の arity 1,...,f のタプル代入可能性を満たすなら、
  min{|w|: w∈L\L'} ≤ (r+2)θ。
L 自体の代入可能性も、L' の MCFL 所属性も、この命題には不要である。

証明。
各非終端 A について総長≤θ の生成組 u_A と、固定文字数≤θ の適法な A-文脈 E_A を選ぶ。
これは A のある規則を使用する長さ≤θ の成功導出から得られる。u_A と E_A は別の短い成功導出から選んでもよい。
E_A は A の任意の生成組を受け入れる。E_S=□ とする。
各規則 R:A→ρ(B_1,...,B_t) が直接書く終端数も≤θ である。
したがって次の有限集合 W は L の部分集合で、各語の長さは≤(r+2)θ：
  E_A[u_A]、および E_A[ρ(u_B1,...,u_Bt)]。
W⊆L' と仮定する。同じ E_A に入る u_A と ρ(u_B1,...,u_Bt) は L' で無型分布が一致する。
good テンプレートへの代入はこの分布同値を保存する。理由は、一つの子だけを替えるとき、他の子と外部文脈を固定すれば、その子に対する適法な文脈ができるからである。
この事実を子ごとに適用し、導出木について帰納すると、A の全生成組は u_A と L' で分布同値になる。
S では □ が u_S を受け入れるので L⊆L'。矛盾。従って W の少なくとも一語が差に属する。□

地図 C7 の「超多項式の差を狙うなら L' は無型代入可能であってはならない」は、上の正確な意味では「独立に確認」。
ただし、任意の proper subtarget が無型代入可能であってはならない、という無条件の読み方はしない。
この障壁は、部分標的法そのものを排除しない。少数の内容型による区別が、本当に無型の短い証人の連結を妨げる設計を要求する。

3.2 障壁 II：群の非可換性は、見えている中央の差によって検出される

補題 C0（中央化群の正確な式）[証明済み]。
群準同型 φ の値を A=φ(x1), B=φ(x2), A'=φ(y1), B'=φ(y2) と置く。
中央の値 t で A t B=A' t B' が成り立つとする。ε=B'B^{-1} とすると、別の中央 t' で等式が成り立つことは
  ε∈C_Γ(t^{-1}t')
と同値である。
実際、最初の等式は A'^{-1}A=t ε t^{-1}、二番目は A'^{-1}A=t' ε t'^{-1}。両式を比べればよい。□

単一値原像 L=φ^{-1}(g) では、同じ外部接頭辞・接尾辞を持つ二つの受理語から、群の相殺で上の等式が出る。
しかし SUB_2 が t' を検査できるのは、同じ組を入れた適法な成功文脈が本当に存在するときだけである。
従って一般の正しい形は「実現可能な型差 ε は、実現可能な中央比 t^{-1}t' を中央化する」である。
無条件に「Γ 全体が可換」としてはいけない。次の定理では、この実現可能性を正の全内容代表によって満たす。

定理 G1（有限群認識の完全な崩壊）[証明済み]。
φ:Σ*→Γ を有限群への全射準同型、P⊆Γ とし、L=φ^{-1}(P)∩Σ+ とする。
P≠∅ のとき、次は同値である。
  (i) L は内容型付けの SUB_1 と SUB_2 を満たす。
  (ii) ある正規部分群 N◁Γ と p∈Γ について P=pN、かつ Γ/N は可換である。
  (iii) L は有限可換群への準同型の一つの値の原像である。
この場合 L は無型でも全 arity のタプル代入可能性を満たす。
また SUB_1 だけの必要十分条件は P が正規部分群の一つの剰余類であること。
P=∅ は空言語なので別扱いで自明である。

証明。
(1) 全内容の代表を用意する。
各文字 a について o_a=ord(φ(a)) とし、z を全ての a^{o_a} の連結とする。
φ(z)=1、cont(z)=Σ、z≠ε である。有限群では各逆元を正の語で表せるため、全ての g∈Γ が正の語で表せる。
その代表に z を足せば、全ての g は内容がちょうど Σ の非空語で表せる。

(2) SUB_1 が受理集合を一つの統語類にする。
Γ 上の合同を u≈v ⇔ 全ての l,r∈Γ に対して lur∈P ⇔ lvr∈P、と定める。
p,q∈P を全内容語で表すと、空の外部文脈 □ を共有する。SUB_1 により分布が等しい。
任意の l,r も語で表せるので p≈q。逆に ≈ は P への所属を保存するため、P はちょうど一つの ≈-類になる。
群の両側合同は正規部分群 N=[1]_≈ の剰余類合同である。
具体的には、≈ の左右乗法との両立から N は積と逆元で閉じ、gNg^{-1}=N であり、u≈v ⇔ u^{-1}v∈N となる。
よって P=pN。逆に P=pN、N 正規なら商群で相殺できるので、無型 SUB_1 が成り立つ。

(3) SUB_2 で商群の交換子を消す。
商群 H=Γ/N、受理値 h=pN とし、任意の s,t∈H を取る。
各値の全内容代表 r(g) を固定し、
  X=(r(s),r(s^{-1})), Y=(r(1),r(1)),
  E=(ε,r(1),r(h)), F=(ε,r(t),r(t^{-1}h))
とする。E,F の中央は非空なので適法であり、X,Y は成分ごとに同じ内容である。
E[X], E[Y], F[Y] は全て受理値 h を持つ。
SUB_2 を Y から X に適用すれば F[X] も受理され、
  s t s^{-1} t^{-1} h=h。
従って任意の s,t は可換である。

(4) 可換群の一原像では、E[X] と E[Y] の受理から成分値の総和が一致する。
別の文脈でも固定部分の総和だけが加わるため、全 arity の無型 SUB が成り立つ。□

§6(iii) の観察について：arity 1 は相殺で成立し、arity 2 は一般に成立しない、という部分は「独立に確認」。
有限群の単位元原像なら、単なる「一般には」でなく「可換のとき、かつそのときに限る」と言える。
さらに定理 G1 は、受理集合 P が任意の場合まで含む。

3.3 無限群の単位元原像への拡張

定理 G2 [証明済み]。
Γ は任意の群、φ:Σ*→Γ とし、P0=φ(Σ*)、U=P0∩P0^{-1}（正の像 P0 の単元群）とする。
L=φ^{-1}(1)∩Σ+ について、
  L が内容付き SUB_2 を満たす ⇔ U が可換。
SUB_1 は無型で常に成り立つ。右辺が成り立てば、全 arity の無型 SUB も成り立つ。

証明。
受理語を uvw と分解すると φ(v)^{-1}=φ(wu)∈P0。従って受理語の各因子の値は U に属する。
Σ_U={a:φ(a)∈U} とすれば L⊆Σ_U*、また U=φ(Σ_U*) である。
後者は、P0 の単元 g を正の語で表したとき、その全因子も P0 の単元であることから従う。
Σ_U≠∅ なら各 a∈Σ_U に対して φ(a) の逆元の正の代表を選べる。その代表も Σ_U 上にある。
a とその逆元代表を全 a について連結すると、内容 Σ_U、値1の非空語が得られる。
従って U の全ての値に内容 Σ_U の非空代表がある。定理 G1(3) の交換子証明を U で適用すれば必要性が出る。
Σ_U=∅ なら U={1} かつ L は空で、同じ結論である。
十分性では、三つの受理語に現れる全因子と文脈片が U の値を持つことを使い、可換性と相殺を適用する。□

限界：これは非単位元 g の原像 φ^{-1}(g) に、そのままは移らない。
正の像が群にならない場合、g に至る経路の途中で使う非単元を逆向きに戻せないためである。
この差は、正のモノイドの非可換な設計を全て排除したと誤読しないために重要である。

3.4 障壁 III：文法内部の大きさと意味論的な代表の大きさは別物

命題 R0 [証明済み]。
Σ={a,c} 上で
  S→SS | a | c | A_0 | ... | A_n,
  A_0→a,
  A_i→A_{i-1} A_{i-1} | c  (1≤i≤n)
とする。||G_n||=11n+16、θ=2、L=Σ+ である。
内容 a の A_n の最短生成は a^{2^n} なのに、分布代表は a でよく、τ(G_n,c_Σ)≤2。
内容 {a,c} には ac、単文字内容には各一文字を使えばよい。
原稿の U_1 型付けなら τ=1。地図の原稿例と区別するためここでは内容型付けで述べた。

証明。
規則費用は S の SS,a,c が5+2+2、各 S→A_i が3、A_0→a が2、各 i≥1 が5+2。
非終端数 n+2 を加えて11n+16。各規則を長さ≤2の文で使え、SS 規則から θ=2。
A_n の c を含まない生成では倍増を毎回選ぶしかない。
L=Σ+ の全ての適法な文脈は全ての組を受け入れるので、分布代表には内部導出の制約がない。□

従って、型付き積の厚さや最短「生成組」を抑えられないことは、τ の上界の失敗ではない。
また τ が大きいこと自体は、標本下界ではない。原稿の系は τ から標本への上界しか述べていない。

命題 R1（可換認識への無条件拡張は偽）[証明済み]。
L0=a^+{b,c}^+ は、内容型付けについて全 arity でタプル代入可能だが、可換モノイド準同型の受理集合の原像ではない。
後半は ab∈L0、ba∉L0 が同じ Parikh ベクトルを持つため。
前半は §4.1 の群を自明にした場合の証明を参照。
つまり群の「可逆な値」の可換化と、経路・順序による不可逆な制約の消失は同じではない。
この反例が退けるのは「全言語が Parikh 飽和になる」という一般化であり、補題 C0 の局所的な中央化群条件ではない。

課題1(c) の一文：
肯定の証明の鍵は、短い規則から得る不変量を「同じ内容を持つ実際の分布代表」へ戻すことにあり、否定例はその戻しを妨げる不可逆な文脈制約を必要とする。

ここまでの節は完結。

4. 課題2：新しい攻め方――規則差分の格子から全型の分布代表を直接短くする

選んだ理由。
有限群の場合に可換化が成立しても、群の位数が標的ごとに増大すれば、それだけでは多項式評価にならない。
一方、文法を自動機械と直積してから厚さを測り直すと、障壁 III に戻ってしまう。
そこで元の文法の短い生成組だけから整数格子を作り、その格子の中で全型を一度に短縮する。
得られる短いベクトルが実際の分布代表になることを、順序付き文字群のクラスで証明する。
新しい点は非可換性を温存することではなく、μ ではなく τ、生成組ではなく分布代表、有限位数ではなく階数不足も含む格子を直接扱う点である。

4.1 対象クラスと手による所属証明

Σ=Γ_1⊔...⊔Γ_t を非空な文字群への順序付き分割とし、
  R=Γ_1^+ Γ_2^+ ... Γ_t^+
と置く。各 Γ_i の内部では文字の順序も回数も自由である。
A を任意の可換群（有限でなくてよい）、φ:Σ*→A を準同型、g∈A とし、
  L=R∩φ^{-1}(g)
を考える。群演算は加法表記を用いる。
このクラスには、少なくとも与えられた good f-MCFG 表示が存在するものを対象とする。無限群を使った全ての原像に MCFL 性を主張しているわけではない。
有限群なら L は正則なので MCFL である。

補題 S1 [証明済み]。
上の L は、内容型付けについて全 arity のタプル代入可能性を満たす。

証明。
各文字 a に、その属する段 j(a)∈{1,...,t} を割り当てる。
R の語は段番号が非減少で、全ての段を含む語にほかならない。
E[X],E[Y]∈L、X,Y の成分内容が等しいとする。
各成分 x_i,y_i は段非減少で、先頭・末尾の段番号も同じである。これは内容の最小・最大の段番号で決まる。
従って任意の適法文脈 F について、F[X]∈R なら F[Y]∈R であり、逆も同様。
全ての段を含むという条件も、語全体の内容が変わらないので保存される。
さらに E[X],E[Y] が同じ群値 g を持ち、群が可換なので、成分値の総和が等しい。
よって F[X] と F[Y] の群値も等しい。以上から分布が等しい。□

以下の証明はこの全 arity の所属証明を使用する。有界長検査を所属の代用にはしない。

4.2 短い規則差分

補題 S2 [証明済み]。
G を上の L の reduced good 表示とする。各非終端 A の短い生成組 u_A（総長≤θ）を選び、その総 Parikh ベクトルを p_A とする。
各規則 R0:A→ρ(B_1,...,B_s) に対し、直接書く終端の Parikh ベクトルを t_R0 として
  d_R0=t_R0+Σ_j p_Bj-p_A,
  H=span_Z{d_R0:R0∈P}, B=(r+2)θ
と定める。このとき、
  (a) ||d_R0||_1≤B。
  (b) H⊆ker(Φ)、ただし Φ:Z^k→A は文字値からの群準同型。
  (c) 全ての w∈L について Ψ(w)-p_S∈H。

証明。
(a) t_R0 の長さ≤θ、各 p_B の長さ≤θ、p_A の長さ≤θ なので三角不等式でよい。
(b) A の全生成組は同じ固定文脈 E_A に入れて L の文にできる。
可換性と相殺から、その総群値は g-Φ(Ψ(E_A)) で一定。
特に u_A と ρ(u_B1,...,u_Bs) の総群値が一致するので Φ(d_R0)=0。
(c) 成功導出木の全節点について d_R0 を足すと、各内部非終端の p_A が親からの加算と自分での減算で打ち消される。
残るのは Ψ(w)-p_S だけである。これは有限の木の恒等式であり、循環文法でも各成功導出に適用できる。□

4.3 場合分けのない整数格子短縮補題

補題 O（直交象限内の短縮）[証明済み]。
H≤Z^k が、各座標の絶対値≤B の整数ベクトルで生成され、B≥1 とする。
c∈Z^k、||c||_∞≤C、C≥1。J⊆{1,...,k} とし、
  (c+H)∩{y∈Z^k:y≥0、i∉J なら y_i=0}
が空でないと仮定する。
T=k!B^k と置けば、この集合には
  ||y||_1≤kC+k^2 T(T+C)
を満たす点がある。
さらに任意の実現点から、座標集合を高々 k 回縮める操作でその上界を満たす点に移れる。

証明。
元の短い生成ベクトルから実線形独立な h 本を選び、k×h 行列 D に並べる。h=rank(H)。
整数格子として D の列が H 全体を生成する必要はない。span_Z(D)⊆H だけを使う。
h=0 なら唯一の点は y=c であり、結論は自明。以下 h≥1。

現在の実現点 y に対して I={i:y_i≥T} と置く。
もし span_R(D)∩R^I≠{0} なら、次の小さい整数ベクトル z を取れる：
  0≠z∈span_Z(D)⊆H、supp(z)⊆I、||z||_∞≤T。
理由：I の外の行だけの行列 D_{I^c} の階数は h 未満。
その列の極小な線形従属集合に小行列式を使うと、非零整数核ベクトル λ があり、各 |λ_j|≤(h-1)!B^{h-1}。
零列だけの場合は対応する単位ベクトルを使う。
D は列独立なので z=Dλ≠0、そして |z_i|≤h!B^h≤k!B^k=T。

z の符号を選んで Σ_i z_i≥0 とする。この z は正の座標を少なくとも一つ持つ。
q=min_{z_i>0} floor(y_i/z_i) とし、y を y-qz に替える。
z の支持上では y_i≥T≥|z_i| なので q≥1。
全座標は非負のまま、I の外は変わらず、総和は増えない。
最小を実現する座標の新しい値は z_i 未満、従って T 未満になる。よって I は真に小さくなる。
また J の外は初めから0なので I に入らず、禁止座標を変えない。
この操作を高々 k 回行えば、span_R(D)∩R^I={0} となる。

最後の点も y=c+Dλ（λ は実数でよい）と書ける。
D_{I^c} は列階数 h を持つので、I の外から h 行を選んで可逆な整数行列 M を作る。
その行で Mλ=(y-c) を解く。右辺の各座標の絶対値は T+C 以下。
det(M) は非零整数なので絶対値≥1。Cramer の公式により
  |λ_j|≤h!B^{h-1}(T+C)。
従って全座標について
  y_i≤C+h h!B^h(T+C)≤C+kT(T+C)。
I の外の y_i<T にも同じ上界が通る。k 座標を足して結論を得る。□

これは固定次元の整数格子に関する補題である。
「非負実数解があるから短い整数解がある」としていない。
小さい整数移動が本当に H に入り、禁止座標を変えず、各段階で実現点を保つことが証明の要点である。

4.4 全型の τ の上界

定理 S（順序付き文字群×可換群の全代表）[証明済み]。
§4.1 の L とその任意の reduced good fan-out≤f、rank≤r 表示 G について、
  B=(r+2)θ, T=k!B^k, C=2θ+f,
  U=kf+kC+k^2 T(T+C)
と置く。このとき
  τ(G,c_Σ)≤U=O_{k,f,r}(θ^{2k})。
特に k=3,f=2 では θ の6次の上界である。定数は粗いが、v や群の位数には依存しない。

証明。
型付き非終端 X=A_(M_1,...,M_d) を任意に取り、その生成組 x を一つ選ぶ。
短い無型文脈 E_A を取り、e=Ψ(E_A)、n=Σ_i Ψ(x_i)、z0=p_S-e とする。
E_A[x] は G の文なので、補題 S2(c) により n∈z0+H。
各文字 a について b_a=#{i:a∈M_i}、J=∪_i M_i とする。
すると n_a≥b_a、J の外では n_a=0、Σ_a b_a≤dk≤fk。
y=n-b、c=z0-b と置けば、補題 O の仮定を満たす。|c_a|≤2θ+f=C である。
よって同じ格子剰余類で禁止座標を保ち、非負の y' で
  ||y'||_1≤kC+k^2T(T+C)
のものを得る。n'=y'+b とする。

n' を d 成分に配る：a∈M_i の各組 (a,i) に一個ずつ配り、a の残りは a を含む成分のどれか一つに配る。
各成分内では Γ_1,...,Γ_t の順に文字を並べる。これを x'_i とする。
各 x'_i は非空で、内容はちょうど M_i。総長は≤U。
x_i と x'_i は段非減少で始終段が同じなので、§4.1 の議論により任意の適法文脈 F で R への所属が一致する。
また n'-n∈H⊆kerΦ より、成分の総群値が同じ。
したがって任意の F で F[x]∈L ⇔ F[x']∈L。
よって x' は Cl_{L,c}(X) に入り、τ_X≤U。X は任意なので結論を得る。□

重要な点：x' を A が生成できるとは主張していない。
必要なのは全ての適法文脈での分布同値であり、これを手で証明した。
この点が障壁 III を迂回する。

系 S-data [証明済み]。
固定した k,f,r（r≥2）で、このクラスの標準作用素の特徴標本は
  ||K||_+≤2^{kfr}||G|| (1+2θ+rU)
で取れる。従って O_{k,f,r}(||G|| θ^{2k})。
ε を別に加えた言語については右辺に1を足す。

根拠。
各型付き非終端に上で得た代表を置き、E_A と組み合わせた非終端証人・規則証人を作る。
一語の長さは≤2θ+rU。型付き非終端数と規則数の和は≤2^{kfr}||G||。
代表の分布同値と good テンプレートの合成保存により全ての証人は L に属する。
これらを含む標本から標準作用素が各規則を模倣でき、健全性と合わせて正確な再構成となる。
これは原稿 cor:distribution-representatives の証明を読み直して確認したものである（「独立に確認」）。
本報告の新しい入力は τ≤U の部分である。

4.5 有限群の場合の改善

定理 F [証明済み]。
§4.1 の群 A の文字生成部分群が有限で、その位数を q とする。このとき
  q≤B^k,
  τ(G,c_Σ)≤k(f+q-1)≤k(f+B^k-1)。
従って標本長は O_{k,f,r}(||G|| θ^k) で足りる。
特に定理 G1 により、有限群で認識される内容 SUB_2 言語の全てにこの上界が適用される。

証明。
群は文字値で生成されるものに制限する。
各文字 a の位数 o_a に対して、受理語に同じ段の中で a^{o_a} を挿入すれば、再び R と群値条件を満たす。
各段は非空なので、挿入する位置は常に選べる。
この二つの受理語の Parikh 差 o_a e_a は H に属する（補題 S2(c)）。よって H は階数 k。
規則差分から独立な k 本を選んだ行列 D0 に対し、
  span_Z(D0)⊆H⊆kerΦ,
  q=[Z^k:kerΦ]≤[Z^k:span_Z(D0)]=|det D0|≤B^k。
最後は列の Euclid ノルム≤1-ノルム≤B と Hadamard の不等式である。

X の成分内容から前節の b_a を定め、元の総個数 n_a を
  n'_a=b_a+((n_a-b_a) mod o_a)  (b_a>0),
  n'_a=0                       (b_a=0)
に替える。
総群値と各成分内容を保って配り直せるので、同じ分布の代表が得られる。
総長は≤Σ_{b_a>0}(b_a+o_a-1)≤kf+k(q-1)。□

4.6 既知の地図に含まれない具体的な部分クラス

例 S∞ [証明済み]。
Σ={a,b,c}、Γ_1={a}、Γ_2={b,c}、φ(a)=1、φ(b)=-1、φ(c)=0（値群 Z）、g=0 とする。
  L∞={a^p u : p≥1, u∈{b,c}^+, |u|_b=p}。
次の good、fan-out1、rank2 文法が表示する：
  S→a S T | a T,
  T→b | c T | T c。
||G||=22、θ=4。
T は c*bc*、S は p 個の a に続く p 個の T を生成し、逆に任意の u は各 b の間の c を配ってこの形に分解できる。
規則費用は6,4,2,4,4、非終端数2。再帰規則 S→aST の最短成功文は aabb、他の規則は長さ≤3の文で使用できるので θ=4。
短い代表 p_S=(1,1,0)、p_T=(0,1,0) を使うと、非零規則差分は (1,1,0) と (0,0,1)。
H は階数2であり、有限群の位数による議論は適用できないが、補題 O と定理 S は適用できる。

実際の fan-out2 非終端も入れたい場合、上の文法に
  S→(ξ_1^1 c ξ_1^2)(A),
  A→(a,b) | (a ξ_1^1,b ξ_1^2)(A) | (ξ_1^1,ξ_1^2 c)(A)
を追加する。A の生成は (a^p,b^p c^N)、p≥1,N≥0。
追加された S の生成は元の L∞ に含まれるので言語は変わらない。追加規則は全て good で到達可能・生産的。
文法サイズは42、厚さは5（A の増分規則を使う最短文 aacbb の長さが5、他は≤4）。
A の内容 ({a},{b,c}) のどんなに長い組も (a,bc) と分布同値である。
スクリプトでは p=2^80,N=2^96 の総個数から、同じ型の代表 (a,bc) を整数演算だけで構成して確かめる。

この L∞ は A3 の「各文字が一本の辺」の経路×可換群×内容の形では表せない。
実際 aabb∈L∞ なので、その経路を読む唯一の a 辺・b 辺はいずれもループで、同じ頂点上にある。
従って abab も同じ始終点の経路になり、Parikh ベクトルも内容も aabb と同じである。
可換群条件では両者を区別できないが abab∉L∞。矛盾。
また c も任意個挿入でき、a,b も同時に増やせるため、言語全体を非自明な非負重みの一水準に載せることはできない。
適切な内容に対する外字の個数・塊数は無限になり、A4 の容量仮定から全型の評価は出ない。
A1 は全内容型だけ、A2 は μ_a、A3 は μ_ab、A6 は条件付きの幅評価なので、このクラスの任意表示に対する全 τ の無条件上界を述べていない。
全ての A1–A6 と言語集合として互いに素だとは主張しない。A1 のように全言語の一部の型を扱う結果とは当然重なる。

例 S_q [証明済み]。
  L_q={a^p u:p≥1,u∈{b,c}^+,p+|u|≡0 (mod q)}。
これは複数の同一ラベル辺を必要とする正則な順序制約と、任意に大きくできる有限巡回群の積である。
補題 S1 により全 arity で所属し、定理 F は q を自由な定数として隠さず、任意の good 表示から q≤((r+2)θ)^3 と抑える。

4.7 どこまで届いたか

主結果は全ての型付き非終端の τ に対する評価であり、μ のみの評価ではない。
一般の言語については補題 S2(c) の格子包含は作れても、短い格子点を受理語・分布代表に戻せない。
例えば「同じ格子剰余類なら受理される」は一般の文法にも一般の内容代入可能言語にも与えられていない。
順序付き文字群と一つの可換群値という仮定が、ここでその戻しを保証している。
従って op:fanout-two の解決、全正則言語への拡張、内容ごとに任意の異なる群値を指定した言語への拡張は主張しない。
定理 S 自体は f=1 にも成立する。今回の上界でファンアウトの境界が動くと結論することはできない。

5. 試した候補の表

今回は多項式データを示す方向を選んだため、超多項式下界候補の文法族は提出していない。
負の候補に必要な五項目を実施済みと装うことはしない。検査対象は次の正の部分クラス・反例である。

対象 | 表示・認識 | 検査の目的 | 結論
有限群の任意の受理集合 | 有限乗法表 | G1 の有限完全検査 | §8 に実出力
S3 の単位元原像 | a=(12),b=(23),c=1 | 群の非可換性を検出する四語 | SUB_2 違反を出力
L∞ | S→aST|aT、T→b|cT|Tc | 新しい階数不足の例 | 手で所属証明、||G||22、θ4
L_q | a^+{b,c}^+∩長さ0 mod q | 有限群×順序の例 | 手で所属証明、有界検査も実行
{ba^{N-1}} | S→ba^{N-1} | 地図 B7 の向きの欠落 | 手で全 arity の所属証明を §6 に記す

ここまでの節は完結。

6. 課題3：地図の点検（疑わしい箇所は最大5項目）

6.1 肯否・字母数・ファンアウトの量化
判定：「誤り」（§2 の肯否の呼び方と、三文字だけへの無条件な限定）。

prop:sl-reduction が与えるのは、固定 f,r ごとに
  SL が失敗 ⇔ ある固定有限 Σ の内容型付けが失敗、
  SL が成功 ⇔ 全ての固定有限 Σ の内容型付けが成功
という量化である。多項式の次数・係数は Σ に依存してよい。
従って三文字で全ての τ を抑えても、四文字以上への還元なしには SL の成功は出ない。
逆に下界は、一つの固定有限字母（四文字以上でもよい）で十分。
三文字上界は「最初に残る場合」の解決であって、元の問い全部との同値ではない。
また f=2 の結論を全ての f≥2 に自動的に持ち上げることもできない。
例えば f=2 の反例候補が f=3 の SUB_3 を満たすとは限らない。

確認方法：main.tex の prop:sl-reduction と op:fanout-two の量化を直接照合した。
帰着の半束部分も、半束型が内容型を通じて因数分解すること、細かい型の Link が粗い型の Link に含まれることから「独立に確認」。
非 LG 擬多様体が SL を含む半群論の前提定理までは今回独立再証明していないため、その部分は「確認できず」として引用扱いに留める。

6.2 μ、τ、特徴標本、および二つの下界手段の非同値
判定：「誤り」（十分条件を必要十分条件として読む場合）。

μ*≤τ と、標本長≤N_typ(1+2θ+rτ) は、どちらも片方向の不等式である。
μ を全型で抑えても一般の非終端の分布代表が短くなるとはまだ言えない。
また τ の超多項式下界は、標準作用素の最短特徴標本の超多項式下界をそのまま意味しない。
従って C5 の「τ で攻める」は、今の上界戦略を否定するものと、op 自体を否定・肯定するものを区別すべきである。
§2 の (a) 稀な型、(b) 一つの長い差 は有効な十分手段だが、全てのデータ下界を尽くすとの定理はない。
多数の短い差を同時に打つための下界や、作用素固有の再構成上の障害を排除できていない。

ここで B9 は「独立に確認」。
L={a,b}^3\{aaa,bbb}、K={aab,aba,abb} とすると、共有による非自明な因子 Link は ab~ba と全語間の Link だけ。
観測された分解から生成する語は K と、その ab/ba 因子を替えた語であり、
  L(B(K))={aab,aba,baa,abb,bab}=L\{bba}。
二穴の観測は一文字成分二つなので追加の非自明な Link を作らず、rank3 も一文字分解だけなので結果を変えない。
この集合では E=□b が ab,ba を受け入れるが、H=b□ は ab を受け入れ ba を受け入れない。
従って (Hyp) は偽であり、全 proper subtarget の差への hitting set と特徴標本を無条件で同一視できない。
スクリプトは L の所属と、L\{bba} の違反を全ての正の語を用いて再検査する。

確認方法：τ と最短特徴標本の間に逆向きの定理を新たに証明するか、対象の作用素について反例を作ること。
現状で逆向きは「確認できず」。今回の上界は逆向きを使わない。

6.3 C3–C5 の局所的な必要条件を一般化しすぎている
判定：「確認できず」（一般の q・影・核数に関する必要条件）。

A6 が提示している q を使った τ 評価には「場合 I」という範囲がある。
その式だけから、場合 II・III を含む全反例に「q が超多項式でなければならない」を要求することはできない。
もし他の一般補題で同じ含意が証明済みなら、その補題と、q が何の導出・代表・侵入集合について最小化または最大化されるかを明示すべきである。
特に、ある悪い表示や非最短導出で q を大きくできることと、全ての短縮に必要な q が大きいことは別である。
「二つの影がともに超多項式に厚い」も、影の具体的定義、trim 後の規則、比較対象のサイズを明示しない限り独立な必要条件として使用できない。

C3 の Ω(n/log n) も、n の意味と狙う増大率を固定する必要がある。
K^{3D+1} 型の評価からは、指数下界 μ≈2^n と K=poly(n) なら D=Ω(n/log n) 型の推論が可能だが、単に μ が超多項式というだけで同じ速度は導けない。
一般には log μ、log K、および残りの多項式因子を残した不等式で記録すべきである。

確認方法：各必要条件を「対象族」「元のパラメータ」「最小化する導出・代表」「仮定→結論」の四列で書き直す。
今回の定理 S は q や核の仮定を使用しないため、ここが未確認でも新しい上界は影響されない。

6.4 B7 の唯一語の分類に逆向きが落ちている
判定：「誤り」（依頼文の列挙を文字どおり読む場合）。

反例 [証明済み]：N≥7、W=ba^{N-1}。
{W} は内容型付けについて全 arity で代入可能だが、W は記載された
  x^N、x^{N-1}y、y x^{N-2}y、交互語
のどれでもない（x,y が異なる二文字の場合）。

所属の手による証明。
E[X]=E[Y]=W、各成分内容が等しく、F[X]=W とする。
同じ E で得る語の長さが等しいので、X,Y の総長は同じ。
b が組の外にある場合、全ての成分は a の冪であり、F[Y] でも唯一の b は固定部分の先頭に残る。
b が組の中にある場合、W の先頭の唯一の b なので、それを含む成分は第一成分で、その先頭に b がある。
同じ内容を持ち E に入る Y でも同じことが成り立つ。F[X]=W なら F の接頭辞は空で、固定部分に b はない。
従って F[Y] は b で始まり、他の全文字は a、長さも N。よって F[Y]=W。□

少なくとも xy^{N-1}（または「反転を含む」）を追加する必要がある。
元の完全分類で反転を暗黙に同一視していた可能性はあるが、地図にはその規約が書かれていない。
本報告は修正後の一覧が完全であるとは主張しない（完全性は「確認できず」）。
確認方法：分類文に文字交換・反転の同一視を明記し、残りの型の完全性を別途証明する。
N=7,8,9 では全正例から作る arity1・2 の検査も通った。

6.5 B1・A5・B4 に必要な仮定が要約で省かれている
判定：B1 の型条件の省略は「誤り」、A5 の正確な仮定は「確認できず」、B4 の全面排除は「確認できず」。

B1 の二穴のはさみには、x_i と y_i の内容が成分ごとに等しいことが必要。
「同じ中央で二つの語が受理される」だけから分布一致は出ない。
三文字での明示反例 [証明済み]：L={aba,cbb,aaa}、X=(a,a)、Y=(c,b)、E=□b□、H=□a□。
E[X],E[Y],H[X]∈L だが、H[Y]=cab∉L。両方の中央は非空なので適法。
全語の長さが3なので、共有する因子は等長。長さ1で同型なら同一文字であり、全語の内容は互いに異なる。
長さ2の相異なる同型因子は ab,ba だけだが、ab の文脈は □a、ba の文脈は a□ で、共有しない。
従って arity1 で同型の相異なる因子の共有はない。
arity2 では総長3の文の第一・第三文字だけが穴に入るので、同型の組は同一組である。
arity3以上の出現は長さ3の文にはない。従ってこの L は内容付き全 arity の代入可能性を満たす。
この反例は型条件を除いた B1 が偽であることを示す。型条件付きなら B1 はまさに SUB_2 であり「独立に確認」。

A5 の「非負重み」には、少なくともゼロ重みを排除する、あるいは短くしたい文字の重みを正とするなどの、元の正確な条件が必要。
全零重みまで許す記述では、全ての言語が水準0に乗ってしまい、提示された部分結果という位置づけと両立しない。
これは A5 の元の証明への反証ではなく、地図の要約からは適用条件を復元できないという指摘である。
B4 の「加法的不変量・可換群の剰余類は使えない」も、確認済みの μ の対象・内容・経路条件を保った範囲で読む必要がある。
任意の正則制約との積、任意の受理値集合、内容ごとに変わる値、または τ による障害まで A3・A5 が排除したとは読めない。

確認方法：B1 は SUB_2 の型条件と非空中央を明記する。A5 は元の重みの仮定を式で引用する。B4 は上界を適用できる言語の形と、抑えられる量を併記する。

6.6 使用した地図の補題と、使用しなかったもの

「独立に確認」：good 文脈の取り出し、各規則の直接終端数≤θ、各非終端の短い生成組≤θ、分布代表からの標本構成、型付き SUB の基本推論、C7 の定量形、B9 の小反例。
「独立に確認」：A4 の κ による容量評価の骨格。内容の各文字に印を付け、同じ印集合を持つ道ではラベルを重複させず、印の外の重い葉は同時置換で外字を一つずつ出せる。このため葉数≤κ、各道の長さ≤v と数える。
「確認できず」：A4 の β への改良の全証明、A1 の定数付き全証明、A2 の全場合分け、A3 の個別定数、A6 の全依存関係、C4 の一般化。本報告の新定理はこれらに依存しない。
「確認できず」は反証を意味しない。未確認の主張を今回の証明の暗黙の前提にしないという意味である。

7. 課題4：次の一手（見込み順、最大3つ）

7.1 第一候補：内容ごとに値が変わる可換群模型へ、全 τ の短縮を拡張する
位置づけ：[条件付き] 以下の拡張命題はまだ証明していない。
次の依頼：L=R∩{w:cont(w)∈M_family, Φ(Ψ(w))∈g_cont(w)+H_cont(w)} について、SUB_1・SUB_2 から得られる「同じ内容面内の規則差分」だけを使い、元の θ で有界な格子生成系を作れるか調べる。
狙い：今回一つの群値で済んだ場所を、有限個の内容面の整合条件に置き換える。型付き文法の厚さを使わないことを条件とする。
成功したときの定理の形：固定 k,f,r に対する τ(G,c)≤poly(||G||,θ)、対象は順序付き文字群と内容別の可換剰余類を組み合わせたクラス。
失敗しても得られるもの：短い規則差分では結び付かない具体的な二つの内容面、または μ は短いのに τ の補完が失敗する具体例。
今回の証明との差分が小さく、最初に試す価値が最も高い。

7.2 第二候補：一般の正則言語を、可逆な局所群と不可逆な遷移に分ける
位置づけ：[条件付き] G1 の局所版と状態数を消す評価は未証明。
次の依頼：内容 SUB_1・SUB_2 を満たす正則言語の最小自動機械で、成功する中央の変更から観測可能な局所群の商を分類する。
特に、全内容代表を作れない状態間で、補題 C0 の中央化群条件が何に弱まるかを明記する。
狙い：有限群認識の完全分類 G1 を、同一文字が複数の辺を持つ一般の正則制約へ拡げる。
成功したときの定理の形：全 τ の上界を、群の位数や全状態数ではなく、短い成功文脈に現れる不可逆な段数と ||G||,θ で評価する。
失敗しても得られるもの：非可換な局所作用が SUB_2 を保ったまま残る、具体的で所属を手証明できる正則言語。
最初の計算は小さい DFA の全探索とし、「各文字一本の辺」への持ち上げによる θ の増大を回避する。

7.3 第三候補：部分標的法を、短い無型証人がどこで切れるかから設計する
位置づけ：[条件付き] 超多項式の族の存在は未証明。
次の依頼：W0 の有限証人集合を出発点に、L'⊊L がそのほとんどを含みながら、内容型の異なる Link だけを遮断する具体的構造を探す。
狙い：群の非可換性や一語の倍増ではなく、型の異なる証人をつなぐために必要な文脈の長さを下界の主役にする。
成功したときの定理の形：一つの固定 Σ、L_n,L'_n∈C_{2,c}、サイズ・厚さ poly(n)、min|L_n\L'_n| が超多項式。
失敗しても得られるもの：無型証人から内容付き証人へ修復する補題、または修復が必要になる箇所の有限な obstruction。
(Hyp) を仮定しない。一つの差による下界を示せばよく、全下界の完全な特徴づけを最初から要求しない。

8. 検証スクリプトの全ソースと出力

8.1 検査範囲と意味

以下の計算結果のラベルは全て [観察（計算のみ）]。
一般定理の証明は前節までの手証明であり、計算から一般化していない。
標準ライブラリのみの Python 3、乱数種20261110。ネットワーク・外部ファイル・追加パッケージは不要。
本文の BEGIN/END 間をそのまま保存して python3 で実行できる。

・有限群6種では、全ての受理集合 P と全ての群値の組・文脈の分布を計算する。
  各群値を全内容の正の語で表せるため、この有限計算は、その群の全受理集合に対する内容 SUB_1・SUB_2 の厳密な検査となる。
  ただし一般の有限群についての証明を、この6例の検査で置き換えてはいない。
・S3 の非可換核について、正の語による四語の違反証明書を出す。
・無限言語の語レベル検査は、三つの正の前提文の長さ≤6 の範囲で全探索する。
  結論の語は長さ上限を理由に拒否せず、本来の所属述語で判定する。上限による偽の違反を作らない。
・有限 singleton と B9 の言語では全ての正の前提を列挙する。
・格子短縮は400例、うち階数不足225例を実行する。非原始な部分格子、階数0、禁止座標の保存も検査する。
・fan-out2 の大きな組の例は語を展開せず個数で検査する。群値と内容の保存は数学的に証明済みである。

8.2 全ソース

----- BEGIN SCRIPT -----
#!/usr/bin/env python3
"""Reproducible checks; Python 3 standard library only. Seed: 20261110.
No bounded word test is used as a proof of infinite-language membership.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial, gcd
import random
import time

SEED = 20261110


def indexed_group(elements, mul, identity):
    elements = list(elements)
    idx = {g: i for i, g in enumerate(elements)}
    table = [[idx[mul(g, h)] for h in elements] for g in elements]
    e = idx[identity]
    inv = [next(j for j in range(len(elements))
                if table[i][j] == e and table[j][i] == e)
           for i in range(len(elements))]
    return table, e, inv, idx


def test_groups():
    groups = []
    for n in (2, 3, 4):
        groups.append(("C" + str(n), indexed_group(
            range(n), lambda a, b, n=n: (a+b) % n, 0)))
    groups.append(("C2xC2", indexed_group(
        list(product(range(2), repeat=2)),
        lambda a, b: ((a[0]+b[0]) % 2, (a[1]+b[1]) % 2), (0, 0))))
    groups.append(("S3", indexed_group(
        permutations(range(3)),
        lambda a, b: tuple(a[b[i]] for i in range(3)), (0, 1, 2))))
    groups.append(("D8", indexed_group(
        list(product(range(4), range(2))),
        lambda a, b: ((a[0]+(-1 if a[1] else 1)*b[0]) % 4,
                      (a[1]+b[1]) % 2), (0, 0))))
    return groups


def distribution_masks(tab, e, d):
    n = len(tab)
    tuples = list(product(range(n), repeat=d))
    contexts = list(product(range(n), repeat=d+1))
    rows = []
    for x in tuples:
        masks = [0]*n
        for j, ctx in enumerate(contexts):
            val = ctx[0]
            for i, a in enumerate(x):
                val = tab[tab[val][a]][ctx[i+1]]
            masks[val] |= 1 << j
        rows.append(masks)
    return rows


def overlap_equal(rows, accepted):
    sigs = []
    for masks in rows:
        sig = 0
        for a in accepted:
            sig |= masks[a]
        sigs.append(sig)
    for i, a in enumerate(sigs):
        for b in sigs[i+1:]:
            if a & b and a != b:
                return False
    return True


def predicted(tab, e, inv, accepted):
    n = len(tab)
    if not accepted:
        return True, True
    p = min(accepted)
    normal = {tab[inv[p]][a] for a in accepted}
    if e not in normal:
        return False, False
    if any(tab[a][b] not in normal for a in normal for b in normal):
        return False, False
    if any(tab[tab[g][a]][inv[g]] not in normal
           for g in range(n) for a in normal):
        return False, False
    abelian_quotient = all(
        tab[tab[tab[a][b]][inv[a]]][inv[b]] in normal
        for a in range(n) for b in range(n))
    return True, abelian_quotient


def finite_group_check():
    print("[1] Exact finite-group distribution checks (all accepting subsets)")
    for name, (tab, e, inv, idx) in test_groups():
        n = len(tab)
        rows1 = distribution_masks(tab, e, 1)
        rows2 = distribution_masks(tab, e, 2)
        count1 = count2 = mismatches = 0
        for mask in range(1 << n):
            p = {i for i in range(n) if mask >> i & 1}
            a1 = overlap_equal(rows1, p)
            a2 = overlap_equal(rows2, p)
            b1, b2 = predicted(tab, e, inv, p)
            mismatches += ((a1, a1 and a2) != (b1, b2))
            count1 += a1
            count2 += a1 and a2
        assert mismatches == 0
        print(name, "subsets", 1 << n, "SUB1", count1,
              "SUB1+2", count2, "mismatches", mismatches)


def full_content_reps(tab, e, letters):
    keys = sorted(letters)
    target = (1 << len(keys))-1
    seen = {(e, 0): ""}
    queue = deque([(e, 0)])
    while queue:
        g, mask = queue.popleft()
        for j, a in enumerate(keys):
            nxt = (tab[g][letters[a]], mask | (1 << j))
            if nxt not in seen:
                seen[nxt] = seen[(g, mask)] + a
                queue.append(nxt)
    return {g: seen[(g, target)] for g in range(len(tab))}


def fill(ctx, x):
    out = ctx[0]
    for i, w in enumerate(x):
        out += w + ctx[i+1]
    return out


def s3_certificate():
    name, data = next(x for x in test_groups() if x[0] == "S3")
    tab, e, inv, idx = data
    letters = {"a": idx[(1, 0, 2)], "b": idx[(0, 2, 1)], "c": e}
    reps = full_content_reps(tab, e, letters)
    s, t = letters["a"], letters["b"]
    x = (reps[s], reps[inv[s]])
    y = (reps[e], reps[e])
    E = ("", reps[e], "")
    F = ("", reps[t], reps[inv[t]])

    def val(w):
        v = e
        for a in w:
            v = tab[v][letters[a]]
        return v

    words = [fill(E, x), fill(E, y), fill(F, y), fill(F, x)]
    flags = [val(w) == e for w in words]
    assert flags == [True, True, True, False]
    assert list(map(set, x)) == list(map(set, y))
    print("[2] S3 kernel certificate: X,Y,E,F =", x, y, E, F)
    print("words E[X],E[Y],F[Y],F[X] =", words)
    print("accepted =", flags)


def words_upto(alphabet, cap):
    for n in range(1, cap+1):
        for t in product(alphabet, repeat=n):
            yield "".join(t)


def occurrences(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i+1, n+1):
                yield (w[i:j],), (w[:i], w[j:])
    else:
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for ell in range(k+1, n+1):
                        yield (w[i:j], w[k:ell]), (w[:i], w[j:k], w[ell:])


def word_check(accepted_words, member, d):
    # Every premise sentence is in accepted_words. The conclusion is checked
    # against the actual membership predicate, even if it exceeds the bound.
    dist = defaultdict(set)
    shared = defaultdict(set)
    for w in accepted_words:
        for x, ctx in occurrences(w, d):
            typ = tuple("".join(sorted(set(a))) for a in x)
            dist[x].add(ctx)
            shared[(ctx, typ)].add(x)
    seen_pairs = set()
    for (E, typ), values in sorted(shared.items()):
        for x, y in combinations(sorted(values), 2):
            if (x, y) in seen_pairs:
                continue
            seen_pairs.add((x, y))
            for a, b in ((x, y), (y, x)):
                for H in sorted(dist[a]):
                    result = fill(H, b)
                    if not member(result):
                        return {"X": a, "Y": b, "E": E, "H": H,
                                "premises": [fill(E, a), fill(E, b), fill(H, a)],
                                "missing": result}, len(seen_pairs)
    return None, len(seen_pairs)


def stage(w):
    pos = 0
    while pos < len(w) and w[pos] == "a":
        pos += 1
    return 0 < pos < len(w) and all(a in "bc" for a in w[pos:])


def bounded_checks():
    print("[3] Bounded word checks: all three premise sentences length <= 6")
    universe = list(words_upto("abc", 6))
    predicates = [("stage+Z", lambda w: stage(w) and w.count("a") == w.count("b"))]
    for q in (1, 2, 3, 4):
        predicates.append(("stage+C"+str(q),
                           lambda w, q=q: stage(w) and len(w) % q == 0))
    for name, member in predicates:
        language = [w for w in universe if member(w)]
        counts = []
        for d in (1, 2):
            bad, checked = word_check(language, member, d)
            assert bad is None, (name, d, bad)
            counts.append(checked)
        print(name, "positive words", len(language), "tuple pairs", counts,
              "violations 0 (bounded only)")
    print("[4] Finite-language checks (all positive premises enumerated)")
    for n in (7, 8, 9):
        w = "b" + "a"*(n-1)
        for d in (1, 2):
            bad, _ = word_check([w], lambda x, w=w: x == w, d)
            assert bad is None
        print("singleton", w, "SUB1+2 pass; literal B7 list omits this reversal")
    L = {"".join(w) for w in product("ab", repeat=3)} - {"aaa", "bbb"}
    S = L - {"bba"}
    for d in (1, 2):
        assert word_check(sorted(L), lambda w: w in L, d)[0] is None
    bad, _ = word_check(sorted(S), lambda w: w in S, 1)
    assert bad is not None
    print("B9 target SUB1+2 pass; S violation:", bad)
    Lsmall = {"aba", "cbb", "aaa"}
    for d in (1, 2):
        assert word_check(sorted(Lsmall), lambda w: w in Lsmall, d)[0] is None
    X, Y, E, H = ("a", "a"), ("c", "b"), ("", "b", ""), ("", "a", "")
    assert all(w in Lsmall for w in (fill(E, X), fill(E, Y), fill(H, X)))
    assert fill(H, Y) == "cab" and "cab" not in Lsmall
    print("B1 without equal types: target SUB1+2 pass; aba,cbb,aaa accepted; cab rejected")


def rref(matrix, width):
    a = [[Fraction(x) for x in row] for row in matrix]
    pivots = []
    row = 0
    for col in range(width):
        p = next((i for i in range(row, len(a)) if a[i][col]), None)
        if p is None:
            continue
        a[row], a[p] = a[p], a[row]
        value = a[row][col]
        a[row] = [x/value for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                factor = a[i][col]
                a[i] = [x-factor*y for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def integer_null_vector(matrix, width):
    a, pivots = rref(matrix, width)
    free = next((j for j in range(width) if j not in pivots), None)
    if free is None:
        return None
    v = [Fraction(0)]*width
    v[free] = 1
    for i, p in enumerate(pivots):
        v[p] = -a[i][free]
    denom = 1
    for x in v:
        denom = denom*x.denominator // gcd(denom, x.denominator)
    ints = [int(x*denom) for x in v]
    divisor = 0
    for x in ints:
        divisor = gcd(divisor, abs(x))
    return [x//divisor for x in ints]


def matvec(D, x):
    return [sum(a*b for a, b in zip(row, x)) for row in D]


def orthant_shorten(D, c, coefficients, allowed):
    k, h = len(D), len(coefficients)
    B = max(1, max((abs(a) for row in D for a in row), default=0))
    C = max(1, max(map(abs, c)))
    T = factorial(k)*B**k
    delta = list(coefficients)
    y = [a+b for a, b in zip(c, matvec(D, delta))]
    assert all(a >= 0 for a in y)
    assert all(y[i] == 0 for i in range(k) if i not in allowed)
    before = sum(y)
    steps = 0
    while True:
        large = {i for i in range(k) if y[i] >= T}
        lam = integer_null_vector([D[i] for i in range(k) if i not in large], h)
        if lam is None:
            break
        z = matvec(D, lam)
        assert any(z)
        assert max(map(abs, z)) <= T
        assert all(z[i] == 0 for i in range(k) if i not in large)
        if sum(z) < 0:
            lam, z = [-a for a in lam], [-a for a in z]
        q = min(y[i]//z[i] for i in range(k) if z[i] > 0)
        assert q >= 1
        y = [a-q*b for a, b in zip(y, z)]
        delta = [a-q*b for a, b in zip(delta, lam)]
        assert y == [a+b for a, b in zip(c, matvec(D, delta))]
        assert all(a >= 0 for a in y)
        new_large = {i for i in range(k) if y[i] >= T}
        assert new_large < large
        steps += 1
    bound = k*C+k*k*T*(T+C)
    assert steps <= k and sum(y) <= before and sum(y) <= bound
    assert all(y[i] == 0 for i in range(k) if i not in allowed)
    return steps, before, sum(y), y


def lattice_checks():
    rng = random.Random(SEED)
    tested = deficient = max_steps = 0
    largest_before = 0
    for k in range(1, 5):
        for trial in range(100):
            active = k if trial % 3 else max(1, k-1)
            h = rng.randint(1, active)
            while True:
                D = [[rng.randint(1, 3)] + [rng.randint(-3, 3) for _ in range(h-1)]
                     for _ in range(active)]
                D += [[0]*h for _ in range(k-active)]
                if len(rref(D, h)[1]) == h:
                    break
            c = [rng.randint(-5, 5) for _ in range(active)] + [0]*(k-active)
            coeff = [rng.randint(10**5, 10**6)] + [rng.randint(-1000, 1000)
                                                  for _ in range(h-1)]
            steps, before, after, result = orthant_shorten(D, c, coeff, set(range(active)))
            tested += 1
            deficient += h < k
            max_steps = max(max_steps, steps)
            largest_before = max(largest_before, before)
    print("[5] Constructive orthant lemma tests; seed", SEED)
    print("cases", tested, "rank-deficient", deficient, "max steps", max_steps,
          "largest initial l1", largest_before, "failures 0")
    D = [[1, 0], [1, 0], [0, 1]]
    p, N = 2**80, 2**96
    steps, before, after, y = orthant_shorten(
        D, [0, 0, -2], [p-1, N+1], {0, 1, 2})
    n = [y[i]+1 for i in range(3)]
    assert n == [1, 1, 1]
    print("two-component example (a^p,b^p c^N), p=2^80,N=2^96:",
          "short counts", n, "steps", steps, "representative (a,bc)")
    steps, before, after, y = orthant_shorten(
        [[2, 0], [0, 2]], [0, 0],
        [Fraction(2**80+1, 2), Fraction(2**90+1, 2)], {0, 1})
    assert y == [1, 1]
    print("nonprimitive sublattice basis test:", list(map(int, y)),
          "in H=< (2,0),(0,2),(1,1) >; parity coset preserved")
    assert orthant_shorten([[], []], [3, 0], [], {0})[3] == [3, 0]
    print("rank-zero lattice test passed")


def grammar_checks():
    # S -> a S T | a T; T -> b | c T | T c.
    pS, pT = (1, 1, 0), (0, 1, 0)
    rules = [("S", (1, 0, 0), [pS, pT], 3),
             ("S", (1, 0, 0), [pT], 2),
             ("T", (0, 1, 0), [], 1),
             ("T", (0, 0, 1), [pT], 2),
             ("T", (0, 0, 1), [pT], 2)]
    deltas = []
    size = 2
    for head, term, children, template_length in rules:
        parent = pS if head == "S" else pT
        d = tuple(term[i]+sum(p[i] for p in children)-parent[i] for i in range(3))
        deltas.append(d)
        size += 1+len(children)+template_length
    assert size == 22
    assert set(deltas) == {(0, 0, 0), (1, 1, 0), (0, 0, 1)}
    print("[6] Grammar S_infinity: size", size, "rule deltas", deltas,
          "rank", len(rref(deltas, 3)[1]))
    for n in range(1, 6):
        size = (n+2)+5+2+2+3*(n+1)+2+7*n
        assert size == 11*n+16
    print("Refinement example size=11n+16 checked for n=1..5")
    augmented_size = 22
    augmented_size += 1+(1+1+3)+(1+0+2)+(1+1+4)+(1+1+3)
    assert augmented_size == 42
    print("Fan-out-2 redundant extension: size", augmented_size,
          "thickness 5 by explicit shortest rule witnesses in report")


def main():
    start = time.monotonic()
    finite_group_check()
    s3_certificate()
    bounded_checks()
    lattice_checks()
    grammar_checks()
    print("ALL CHECKS PASSED")
    print("Elapsed seconds (machine dependent):", round(time.monotonic()-start, 3))


if __name__ == "__main__":
    main()
----- END SCRIPT -----

8.3 実行出力と要点

[観察（計算のみ）] 実行結果は以下。所要時間の行だけは環境により変わる。

[1] Exact finite-group distribution checks (all accepting subsets)
C2 subsets 4 SUB1 4 SUB1+2 4 mismatches 0
C3 subsets 8 SUB1 5 SUB1+2 5 mismatches 0
C4 subsets 16 SUB1 8 SUB1+2 8 mismatches 0
C2xC2 subsets 16 SUB1 12 SUB1+2 12 mismatches 0
S3 subsets 64 SUB1 10 SUB1+2 4 mismatches 0
D8 subsets 256 SUB1 20 SUB1+2 12 mismatches 0
[2] S3 kernel certificate: X,Y,E,F = ('abbc', 'abbc') ('aabbc', 'aabbc') ('', 'aabbc', '') ('', 'aabc', 'aabc')
words E[X],E[Y],F[Y],F[X] = ['abbcaabbcabbc', 'aabbcaabbcaabbc', 'aabbcaabcaabbcaabc', 'abbcaabcabbcaabc']
accepted = [True, True, True, False]
[3] Bounded word checks: all three premise sentences length <= 6
stage+Z positive words 26 tuple pairs [444, 264] violations 0 (bounded only)
stage+C1 positive words 114 tuple pairs [5052, 1453] violations 0 (bounded only)
stage+C2 positive words 78 tuple pairs [2910, 883] violations 0 (bounded only)
stage+C3 positive words 68 tuple pairs [2366, 774] violations 0 (bounded only)
stage+C4 positive words 14 tuple pairs [53, 3] violations 0 (bounded only)
[4] Finite-language checks (all positive premises enumerated)
singleton baaaaaa SUB1+2 pass; literal B7 list omits this reversal
singleton baaaaaaa SUB1+2 pass; literal B7 list omits this reversal
singleton baaaaaaaa SUB1+2 pass; literal B7 list omits this reversal
B9 target SUB1+2 pass; S violation: {'X': ('ab',), 'Y': ('ba',), 'E': ('', 'a'), 'H': ('b', ''), 'premises': ['aba', 'baa', 'bab'], 'missing': 'bba'}
B1 without equal types: target SUB1+2 pass; aba,cbb,aaa accepted; cab rejected
[5] Constructive orthant lemma tests; seed 20261110
cases 400 rank-deficient 225 max steps 4 largest initial l1 10326262 failures 0
two-component example (a^p,b^p c^N), p=2^80,N=2^96: short counts [1, 1, 1] steps 2 representative (a,bc)
nonprimitive sublattice basis test: [1, 1] in H=< (2,0),(0,2),(1,1) >; parity coset preserved
rank-zero lattice test passed
[6] Grammar S_infinity: size 22 rule deltas [(1, 1, 0), (0, 0, 0), (0, 0, 0), (0, 0, 1), (0, 0, 1)] rank 2
Refinement example size=11n+16 checked for n=1..5
Fan-out-2 redundant extension: size 42 thickness 5 by explicit shortest rule witnesses in report
ALL CHECKS PASSED
Elapsed seconds (machine dependent): 0.21

有限群の全364受理集合で、直接計算と G1 の予測の不一致は0。
無限言語の所属は補題 S1 で手証明済みであり、有界長6の結果だけで所属を認定していない。
格子短縮の400例と追加例は証明の整数性・禁止座標・非原始格子の扱いを点検する補助である。
本文の新定理はいずれも、この有限計算を一般の場合への証明に使っていない。

8.4 参照原稿と照合範囲

参照日は2026-11-10。下の公開ファイルを実際に取得し、本文で挙げた関連箇所を読んだ。
全ファイルの全証明を独立検証したという意味ではない。今回依存する部分と未確認部分は §6.6 に区別した。
記録した SHA は取得時のファイル blob の SHA であり、コミット SHA ではない。

main.tex
https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex
blob SHA: d7bb4f7d3c51d1a050d9f082e03726f342543621

claude_algebraic_closure_2026-11-07.md
https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_algebraic_closure_2026-11-07.md
blob SHA: be6a81e8ef25b2da542d5d162879fdd968e93250

claude_fanout2_content_round3_2026-11-09.md
https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_fanout2_content_round3_2026-11-09.md
blob SHA: 9b31d448386d7c7fb340f19ab821a2a3ac6268d5

claude_fanout2_transfer_round4_2026-11-09.md
https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_fanout2_transfer_round4_2026-11-09.md
blob SHA: 43fde3e3d2da6fb89bf6e425f22ae75a2ac5aeb9

main.tex：定義、厚さ、cor:distribution-representatives とその証明、prop:sl-reduction、op:fanout-two、容量評価を照合。
claude_algebraic_closure：特に §5.1 の一般自動機械への持ち上げと厚さの問題を照合。
claude_fanout2_content_round3：容量証明と、部分標的・(Hyp) の条件付き議論を照合。
claude_fanout2_transfer_round4：§5 の (Hyp) 反例を照合。
その他の取得したレビューは関連箇所の探索に留まり、独立検証済みの根拠として数えていない。

完了。中断箇所なし。op:fanout-two は未解決。

