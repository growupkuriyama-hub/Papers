| 項目 | 判定 | 結論・必要な修正 | 依存する未独立検証の前提 |
|---|---|---|---|
| P1 | [正しい] | 楔の反鎖性。反復点は整数格子・平面にも残る | 抽象補題にはなし。言語への適用は C23 |
| P2 | [正しい] | 2つの挿入点の許容性と隣接間隔の一致 | 同上 |
| P3 | [正しい] | 始切片、頂点、最後の矛盾は成立 | 同上 |
| P4 | [正しい] | 半帯の上端 U は各段で保たれる | 同上 |
| P5 | [正しい] | 法線の4型は網羅的、各射影は単射 | 言語への適用は C23 |
| P6 | [正しい] | rank 1 の混合符号と正の直交重み | なし |
| P7 | [正しい] | M3 の両端が Π₃ にあることだけで足りる | C23（←C21） |
| Q1 | [正しいが記述を直すべき] | F₄は成立。「36通り」の対象と D₃∩E={0}、D₂={0} を修正 | 所属：C21,C22。F_Lの定義域：C24 |
| Q2 | [正しい] | 一般の X,Y≥4 で成立。24式を確認 | 所属：C21,C22。F_L：C24 |
| Q3 | [正しい] | 一般の n≥3 で成立。全移動の型を確認 | 所属：C21,C22。F_L：C24 |
| Q4 | [正しい] | θ最小値7。証人と θ≤6 の排除を手計算で提示 | 所属：C21,C22。F_L：C24 |
| R1 | [正しい] | (★)、cの出現、3語すべての狭義短縮 | なし（Hの許可された前提） |
| R2 | [正しい] | (2|F|−1)vθ。Hの旧誤記 v|F| は使っていない | なし |
| R3 | [正しい] | 最短生成だけで F1/F2 の全用途を満たす | なし |
| R4 | [正しい] | λ(W)=C、最初の閾値交差、γ≤θα | なし |
| R5 | [正しい] | aの個数と背骨の節点数の評価 | なし |
| R6 | [正しい] | B0〜B3を含め定数11、指数4を支持 | 報告の引用経路は P72a。本報告で場合(i)をHから再確認 |
| R7 | [正しい] | Mirskyと寄与の分割で (K_c+3)vθ | なし |
| R8 | [正しい] | 頂点・支配。支配点qに短さは要求されない | なし |
| S1 | [正しいが記述を直すべき] | 系10は成立。独立した命題文には Q₂≠∅ を明記 | rank版：C23。短い水準版：なし。引用上P72a |
| S2 | [正しいが記述を直すべき] | SUB₁、Q₃有限非空、Q₂≠∅ の文脈を残す | C24（許容格子の存在）、C23（P⁺排除） |
| S3 | [正しいが記述を直すべき] | Y₂₃の高さは5,1,2,1。命題11の結論は成立 | 所属を言う場合C21,C22。上界の引用上P72a |
| S4 | [正しいが記述を直すべき] | 命題12は成立。W_t=A等はπ(W_t)=A等へ | 所属C21,C22。上界の引用上P72a |
| S5 | [正しい] | 命題13は成立。重複点も含め全頂点を排除 | 所属C21,C22。上界の引用上P72a |
| S6 | [穴] | N1〜N5′自体は正しい必要条件。しかし一般Qから「Q={P}∪Q₃」の予想7.5を適用する橋がない | C21,C23。詳細§5.6。分類(iii)候補、修復未完 |
| S7 | [正しいが記述を直すべき] | μ_abの部分結果。特徴データ・τ全体・op:fanout-twoの解決ではない | 全一頂点への縮約には追加で未監査の7.2定理A、閉包系3.6等 |

# 命題7.3報告の独立検証

2026-11-07。ChatGPTによる検証。ユーザー指定の `astra_check_prop73_2026-11-07.md` として提出。

**総合判定：定理4・定理6・補題5〜9・系10・命題11〜13の主要な数学的結論を支持する。定数の変更は不要。ただし「予想7.5が真なら一般の命題7.3が閉じる」という適用には、Q₂を一点に制限していることに由来する穴がある。命題7.4への有限Q₃内の帰着そのものは支持できる。**

表の略号：C21＝閉包報告定理2.1、C22＝同系2.2、C23＝同補題2.3、C24＝同補題2.4、P72a＝命題7.2報告系2(a)の「場合(i)」の証明。これらは依頼の指定に従って前提として扱った。閉包報告・7.2報告全体を独立検証済みと宣言するものではない。H報告の指定された補題・T1〜T3・S1〜S3は許可された前提である。

**穴の分類**：S6は定理4・6や定数を壊すものではない。現状で崩れるのは「記載された予想7.5を一般Qにそのまま適用できる」という証明段である。(iii)に相当する修復（追加補題、あるいは予想の対象の拡張）が考えられるが、修復が既にできたとは判定しない。(i)に当たる主定理の反例、(ii)に当たる定数の誤りは発見しなかった。

## 1. 対象・正本・検証の境界

対象は [命題7.3報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_prop73_2026-11-07.md)。取得したblob SHAは `671363036e95658850ee64b52d790ebb77efb6dc`。同じフォルダのH報告、閉包報告、7.2報告、README (184)〜(192)、および指定の `parked/2026-11-06_focus/main_before_focus_59pp.tex` を照合した。

独自スクリプトは標準ライブラリだけで新規作成した。`check_claude_verify_prop73_2026-11-07.py` は読まず、再利用していない。報告付属スクリプトは独立検査の実装と別に、そのまま実行して再現性だけを確認した。報告に記載された式・例の数値は、もちろん検査対象として使用した。

正本との対応は次のとおり。

- c_Σは非空語の内容集合。比較するタプル成分は非空で、arity dの内側の区切りも非空。C_{2,c_Σ}は代入可能性だけでなく2-MCFLであることを要求する。今回の有限Qの例はパリク逆像も有限なので、有限言語としてこの文法的条件を満たす。
- reducedは到達可能かつ生成可能。goodはλ-free・nondeleting・nonpermuting・nonmerging。今回の文法証明は線形・非削除から来る加法性と置換、および既約性を使い、追加のgood条件は使わない。
- 正本の規則厚さは、規則を使う**成功導出全体の語長**の最小値の最大。ρ(R)=|t_R|+Στ(B_j)は部分木の局所量であり、同一ではない。成功導出のR部分木の長さ≥ρ(R)から θ_loc≤θ̄_G。この区別は7.3報告で正しく修正されている。
- 以下、μ_abを有限の数として使う箇所は必ずQ₂≠∅（一般文法ならab語の存在）を前提にする。§1の「7.2と同じ」という継承の下では問題ないが、補題7や系10を切り出すときに省略してはいけない。Q₃=∅の場合はK_c=0で処理でき、定理4の空集合の場合も正の水準という条件は空虚に成立する。

## 2. P：平面の補題と定理4

### P1 [正しい]

u,vがアフィン座標なので、d=q−p≠0なら(u(d),v(d))≠(0,0)。両成分が非負なら、α,β>0の下でκ(d)≥0。したがって各k≥0について

u(q+kd)≥u(q)≥0、v(q+kd)≥v(q)≥0、κ(q+kd)≥κ(q)≥κ₀。

またq+kdは整数格子と平面Aに残る。閉包を `x+q−p` に適用して、x=q,q+d,…と帰納する。最初の段は2q−pなので、p=qを許す閉包の定義が本当に必要である。点はd≠0により全て異なる。有限性と矛盾する。

同じuを持つ異なる2点はvが異なり、向きを選べば比較可能となる。ゆえにuは単射。uの増加順でvが狭義減少しなければ、再び比較可能な組が生じる。

### P2 [正しい]

(2)で x=s_{j−1}+d_j：u(x)≥0、v(x)>v_{j+1}≥0、κ(x)=κ(s_{j−1})+κ(d_j)≥κ₀。格子点かつ平面上であり、閉包の3点はいずれもFにある。

Δu_j<Δu_{j−1}なら u_{j−1}<u(x)<u_j。逆の不等号なら u_j<u(x)<u_{j+1}。どちらも隣接点の間にFの点があることになり矛盾する。等号の場合、uがF上で単射であることからx=s_jであり、uの間隔だけでなく**ベクトル全体**の差が等しくなる。

(3)の x=s_{j+2}−d_jも、u(x)>u_j≥0、v(x)≥0、κ(x)≥κ(s_{j+2})≥κ₀。Δu_jとΔu_{j+1}の大小によって、u(x)は(j,j+1)または(j+1,j+2)の開区間に入る。等号ならx=s_{j+1}。切り落としκ≥κ₀を忘れた議論にはなっていない。

### P3 [正しい]

κ(d_j)≥0なら(2)が一つ左へ等しい差を伝播するのでJ⁺は始切片。残りはκ(d_j)<0で、(3)が右へ伝播する。κ(d_j)=0の場合は両方向への伝播が可能であり、境界の取りこぼしはない。

s*=s_{m+1}で、s*+dのuとκは許容。vも許容なら右側の等差列に属してd=id′となるが、κ(d)≥0とκ(d′)<0に反する。よってv(s*)<|Δv|。同様にs*−d′はvとκが許容で、uまで非負なら左側の列に入りd′=idとなり矛盾。よってu(s*)<Δu′。

両端の非負性から

Δu≤mΔu≤u(s*)<Δu′、

|Δv′|≤(n−1−m)|Δv′|≤v(s*)<|Δv|。

したがってκ(d)<κ(d′)<0≤κ(d)。α,β>0を符号評価に使うのは、(1)の単調性と、この最後の厳密比較である。(2)(3)(5)はκ(d),κ(d′)の符号だけを使う。なお最後の比較自体には「α,β≥0かつ少なくとも一方が正」でも足りる。**両方が狭義正であることが各段で不可欠というわけではない**が、報告の十分条件は正しい。

### P4 [正しい]

半帯ではuが増え続ける方向への無限反復は使えないため、(1)は同じuの2点だけを排除している。この違いは適切である。

(2)の挿入点は 0≤u_{j−1}+Δu_j<u_{j+1}≤U。(3)は u_j<u_{j+2}−Δu_j<u_{j+2}≤U。いずれもvの非負性はΔv_jの仮定で保証される。

頂点でs*+dが排除される原因は上端を越えること、s*−d′が排除される原因は下端を越えることになる。両端s₁,s_nの許容性を合わせると

Δu≤u(s*)<Δu′≤U−u(s*)<Δu

となり矛盾する。空集合・2点以下は自明、U=0でもuの単射性から高々1点である。

### P5 [正しい]

非零法線の符号型は、非零成分数が1、2、3のいずれか。2成分なら同符号／異符号、3成分なら全て同符号／混合符号。この分類を座標置換・法線の符号反転で割ると、正の法線の場合と(a)〜(d)で尽きる。

| 型 | 平面上で消去する座標 | 自由座標 | Π₃の条件 |
|---|---|---|---|
| (a) 一つだけ非零 | a | b,c | 楔、切り落としなし |
| (b) 二つ非零・異符号 | b | a,c | aの下限を平行移動した楔 |
| (c) 二つ非零・同符号 | b | a,c | aの上下限とcの下限、半帯 |
| (d) 三つ非零・混合 | c | a,b | 楔＋αu+βv≥κ₀ |

消去する座標の係数は非零なので、自由座標の値から残りの座標が一意に復元される。アフィン座標であることも、射影の単射性も満たす。(a)ではFが空でないため固定されたa≥1が分かる。各補題によりaff Fの次元≤1となりrank 2に矛盾する。

rank 0は一点（または空集合）として処理できる。Fが正の水準に乗る方向の含意は、λが全差を消すことだけで成立する。

### P6 [正しい]

rank 1でH=ℤdと書いても、dそのものがF−Fに実現されているとは限らない。報告はp,p+kdという**実現された非零倍**を使っており、この点は正しい。その差を非負向きに取り、2q−p以降を反復すれば無限になる。

混合符号の場合、I={i:d_i>0}, J={j:d_j<0}として、I上でΣ_J|d_j|、J上でΣ_I d_i、零成分上で1という重みは全成分が正で、内積は積の差で0になる。

### P7 [正しい]

d=q−r∈D₃、p,p+d∈Π₃なら、supp dの各座標でp_σ≥1かつp_σ+d_σ≥1。これはC23の条件そのもの。supp dの外では座標が不変であり、追加条件はない。d=0は自明。C23を「格子H₃の任意の元で移動できる」と誤引用してはいない。

## 3. Q：例の独立検算

### Q1 [正しいが記述を直すべき]

A=(1,3,12), B=(4,8,1), C=(6,4,4), D=(12,1,3)とする。非自明式はrを固定し、p,qを残り3点から重複可・順序なしで選んだ6式ずつで尽くせる。手計算の座標は次のとおり。

| 引く点r | p,qの順 | p+q−r（順序対応） |
|---|---|---|
| A | BB, BC, BD, CC, CD, DD | (7,13,−10), (9,9,−7), (15,6,−8), (11,5,−4), (17,2,−5), (23,−1,−6) |
| B | AA, AC, AD, CC, CD, DD | (−2,−2,23), (3,−1,15), (9,−4,14), (8,0,7), (14,−3,6), (20,−6,5) |
| C | AA, AB, AD, BB, BD, DD | (−4,2,20), (−1,7,9), (7,0,11), (2,12,−2), (10,5,0), (18,−2,2) |
| D | AA, AB, AC, BB, BC, CC | (−10,5,21), (−7,10,10), (−5,6,13), (−4,15,−1), (−2,11,2), (0,7,5) |

全てΠ₃の外。q≠rだけを課した順序付き3点は48通りで、p=rの自明な12通りを除いたものが36通りである。報告の「36通りのうちp=rだけ」はこの2つを混同している。修正は「非自明な36通りは全て外、残り12通りはp=rで自明」。

行列式は (-3,-5,11)·((2,-4,3)×(8,-7,2))=59。B+D−C=(10,5,0)なのでVの主張も直接成立する。

(T)：非零差は全てc成分が非零であるため、その(T)の両辺はc≥1。ab点には作用しない。abc支持の両端については上の閉包性が(T)の同値を保証する。その他の支持では両辺ともQに入らない。Q₂が一点なので、そこから非零差は生じない。

**零差の修正**：D₃=Q₃−Q₃、D₂=Q₂−Q₂という定義なら、D₃∩E={0}、D₂={0}であって空集合ではない。非零差だけを意味するならその旨を明記する。F_L=∞は§5.2のrank議論による。これは有限計算の推測ではない。

### Q2 [正しい]

非自明式は4個のr×6個のunordered p,q＝24個。報告の24式は漏れなくこの集合に対応する。以下は各式がΠ₃の外になる座標だけを抜き出した手検算表である。

| r | p,qの順 | 非正となる座標値（同じ順） |
|---|---|---|
| A | BB, BM, BZ, MM, MZ, ZZ | b=1−Y, b=2−Y, b=1−Y, b=3−Y, b=2−Y, b=1−Y |
| B | AA, AM, AZ, MM, MZ, ZZ | a=1−X, a=2−X, a=1−X, a=3−X, a=2−X, a=1−X |
| M | AA, AB, AZ, BB, BZ, ZZ | a=0, c=0, a=0, b=0, b=0, a=0 |
| Z | AA, AB, AM, BB, BM, MM | c=−2, c=−2, c=−1, c=−2, c=−1, c=0 |

これはX,Y≥3で有効。行列式は報告どおり3X+3Y−2XY。X,Y≥4なら2XY−3X−3Y≥5Y−12>0で非零。

(T)でab支持にも作用し得る非零差は±(X,−Y,0)だけで、Pからの両移動先は(2X,0,0),(0,2Y,0)。abc支持では閉包性、その他では両辺不所属。P=A+B−M。4点全ての長さがX+Y未満であるため、短い部分もrank 3。

独自計算は4≤X,Y≤20の289組と(30,5),(25,40),(60,7)の計292組。一般の場合の根拠はこの手計算であり、範囲計算から一般化したものではない。

### Q3 [正しい]

差は、線分内の±md、Zと線分の±差、Aと線分の±差、AとZの±差で全て。各差の始点も線分、Z、Aの3型で尽くせる。

- 線分差ではs_j+md=s_{j+m}。範囲外ではaまたはb≤0。Zではmの符号によりaまたはb≤0、Aではm>0でb≤0、m<0でc≤0。
- Z−s_kでは始点s_jに対しj−kの符号でaまたはb≤0、等号ならZ。始点Zでは2Z−s_kのa≤0、始点Aではb≤0。逆差ではs_j+s_k−Zのc≤0、始点Zは自明、始点Aもc≤0。
- A−s_kでは始点s_jに対しj<kでc≤0、j>kでb≤0、等号ならA。始点A,Zではb≤0。逆差ではs_j+s_k−Aのa≤0、始点Aは自明、始点Zではa≤0。
- Z−Aでは始点Aは自明、始点s_j,Zでa≤0。逆差では始点Zは自明、始点s_j,Aでc≤0。

したがって報告の列挙は全ての移動を尽くしている。d=(2,−2,1)、Z−s₁=(−1,1−2n,2n−1)、A−s₁=(4n−2,1−2n,0)を展開して行列式2n−1を得る。

同じcの差はs₁,Aの間だけで、P±(4n−2,1−2n,0)は一方でb=4−2n≤0、他方でa=−1。Q2と同じ(T)の証明が使える。

Vの式の右辺は(4n−5,3−2n,−1)=P−s₁に一致する。短い部分はs₁,…,s_n,Zで、λ(d)=2(2n−1)−2(4n−1)+4n=0、λ(Z)=8n²+6n−2=λ(s₁)。λは狭義正。n≥3により3n+2<4n、2n+2<4nを使う。K_c=n+1、B_ab=4n+1も直接得る。独自計算は3≤n≤30。

### Q4 [正しい]

Q₃={(1,4,6),(3,9,3),(9,3,1),(1,27,1)}。最初の点からの3差の行列式は−112、従ってrank 3。非自明閉包式は全てΠ₃の外。同じcの差は(±8,∓24,0)だけで、P=(5,14,0)からの両移動はΠ₂の外なので(T)。最初の3点の重み(2,1,3)は24、衛星は32である。

P=2(3,9,3)−(1,4,6)。θ=7の証人は

p₁=p₂=(3,9,3)、p₁₂=(1,4,6)、r₁=r₂=(0,1,3)、Y₁=Y₂=(2,6)、q₁=q₂=(3,9,3)、M₁=M₂=(2,5)。

|r_i|=4≤7<8=|Y_i|、Y₁+Y₂=(4,12)≤P_ab−(1,1)=(4,13)、|M_i|=7。N1〜N5′を全て満たす。

θ≤6の排除は、4点に対する不足ベクトルが順に(4,10),(2,5),(0,11),(4,0)であることからできる。合計≤6となる候補qは衛星だけなので、両iでM_{i,a}≥4、Y_{i,a}≥4が必要。しかしN4はY_{1,a}+Y_{2,a}≤4を要求し矛盾する。これは浮動小数点や探索の上限に依存しない。

## 4. R：文法側の証明

### R1 [正しい]

非削除・線形性により、比較不能な2部分木は出力のパリク寄与として重複せず、同時置換の効果は加法的。Y_i=π(y(t_i)), R_i=π(ω_{t_i})と書けば

π(W_t)=P−Y₁+R₁、π(W_{t′})=P−Y₂+R₂、π(W_{tt′})=P−Y₁−Y₂+R₁+R₂。

これが(★)を与える。2つの印はどちらの部分木にもないので全ての置換後もa,bが残る。|ω_t|≤θ<|y(t)|であるため、ω_tにcがなければより短いab語が生じる。これはH補題4.1の正確な使用である。各置換で長さが狭義に減り、cが加わるため、3語とも長さ<μのabc語である。代入可能性は使わない。

### R2 [正しい]

Fの各文字の1出現を**区別した印**にする。短絡する祖先・子孫で印集合が同じなら、上側部分木の全印が下側に残り、Fの文字は失われない。文字の順序が変わり得ても内容の議論には影響しない。

比較不能な2節点の部分木は交わらないので、同じ非空印集合を持てない。したがって一つの印集合を持つ節点は鎖をなし、短絡後に同じラベルは反復しない。非空の異なる印集合は層状族で高々2|F|−1個。これは印を葉として加え、単子節点を抑制した木の節点数としても数えられる。

各集合に高々v節点、各節点の「直接端末＋印を含まない子の最短生成」の寄与はT3で≤θ。合計(2|F|−1)vθを得る。|F|=2では3vθであり、H報告の旧記述v|F|を誤用していない。

### R3 [正しい]

F1は任意の生成uに使える。印のない部分木をcなしのuで置換すれば、a,bの印が残り、長さはμ以上でなければならないので|u|≥|y(z)|。

F2は特に最短生成を使う。τ(A_z)<|y(z)|なら、F1よりuはcを含み、置換語はabcかつμ未満。したがって仮定の水準を適用できる。定理6で必要なτの下界は、常に「もし最短生成がこれより短ければ」という矛盾で得ている。他の長い生成まで水準に乗ると仮定する段はない。

実際には任意の短縮生成にもF2型の議論は成り立つが、その強化を必要としていない。

### R4 [正しい]

(★)の3語にλ=Cを適用してλ(W)=C。W自体はab語なので、これは仮定の直接適用ではなく(★)からの帰結である。

λ(W_t)=λ(W)よりλ(y(t))=λ(ω_t)≥γ。有限のt部分木でλ(y(z))≥γの最深節点z*を選べる。各子z′はλ(y(z′))<γであり、τ(A_{z′})<|y(z′)|ならF2により、cを含む最短生成が同じ重み<γを持つことになって矛盾。従ってτ(A_{z′})≥|y(z′)|。

ρ(R)=|t_R|+Στ(B_j)、パリク加法性から

θ≥ρ(R(z*))≥|t_R|+Σ|y(z′)|=|y(z*)|。

y(z*)はWの一部なのでcなし。a↔bの交換は仮定、μ_ab、結論を保つのでα≥βとしてよく、γ≤λ(y(z*))≤α|y(z*)|≤αθ。ここで最短の全生成にcがあることと、実際のW側の生成にcがないことを混同していない。

### R5 [正しい]

場合(ii)ではabc語が存在する。μ≤5vθなら既に最終上界以下。そうでなければ補題5のabc語u₀はμより短く、λ(u₀)=Cを使える。γ≤αθ、α≥β、θ≥1からC≤5αvθ²、よって|W|_a≤5vθ²。

全a出現とbの1出現を印にする。同じラベル・同じ印集合の祖先を子孫に置換すると、除かれる端末は印を持たず、従ってbだけである。全aと少なくとも1個のbが残り、長さは増えず節点数は減るため、辞書式最小性に反する。k=|W|_a+1に対し背骨≤(2k−1)v≤11v²θ²。

背骨外ではaを一つも生成していない。また元のWにcがないのでcもない。したがってy(z)はbだけ（空の生成を許す一般化ではb*）で、λ(y(z))=βk_z。この主張は「その非終端の**全生成**がbだけ」という主張ではない。

### R6 [正しい]

Aでは各背骨外の子の寄与≤θなので、背骨1節点の寄与≤(r+1)θ。

B0ではk_{j₀}>θ≥τ(A_{j₀})なのでF2が使える。βk_{j₀}≥γが得られ、最深のγ交差をR4と同様に選ぶことでγ≤βθ。

B1ではβk_z≤α。最短生成が短い場合はcを含み同じ重みβk_zを持つ。もしaも含めば重み≥α+γ>αとなるためaは含めない。このため

|u|≥βk_z/max(β,γ)≥k_z/θ。

短くない場合は|u|≥k_z≥k_z/θなので、どちらもτ(A_z)≥k_z/θ。

B2ではβk_{z*}>αとなる最深点の各子にB1が使える。端末寄与を1/θ倍して小さくできるのはθ≥1だからであり、

θ≥|t_R|+Στ(B_j)≥(|t_R|+Σk_j)/θ=k_{z*}/θ。

よってα<βθ²。既存のu₀でC≤5vθ·max(α,β,γ)≤5βvθ³。Wはcなし・α≥βなのでμ≤C/β≤5vθ³。

B3では全ての背骨外の子にB1とT1を使いk_j≤θτ(A_j)≤θ²。従ってμ≤11v²θ²(θ+rθ²)≤11(r+1)v²θ⁴。

Aの11(r+1)v²θ³、B2の5vθ³、初期の5vθはいずれも最終の11(r+1)v²θ⁴以下。場合(i)の9(r+1)vθと合わせて報告の定数が出る。

**場合(i)の引用の再確認**：重い節点は祖先閉。重い木の葉は、印を含むもの≤2、印なし≤1。各根葉路の印集合は高々3区間で、同一区間にラベル反復があればH補題3.1の短絡が最小性に反する。従って重い節点≤9v、各節点の端末と軽い子の寄与≤(r+1)θ。根が軽い場合はμ≤θを直接使う。この最後の自明な場合を明示すれば、P72aの量的評価はHの許可された前提だけから再現できる。

### R7 [正しい]

c可能性の祖先閉性は、子でcを含む生成を使い、他の子を元の生成のままにすることで従う。線形・非削除だからcは消えない。印のない部分の中での祖先閉性であり、印のある祖先まで「印なし」と言ってはいない。

印なし鎖で同じラベルが反復すれば、短絡はa,bの2印を残す。従って鎖長≤v。c可能な反鎖z₁,…,z_mの各部分木を順にcを含む生成へ置換すると、元のWにはcがないため、c数は正の整数を順次加えた狭義増加列になる。全ての語にa,bの印が残るので、m個の異なるc数はK_cに数えられる。

この有限半順序にMirskyの定理を適用して、高々v個の反鎖に分割できる。各反鎖≤K_cより、c可能な印なし節点≤vK_c。印あり節点は3v以下。

この両者の和集合を背骨とすると祖先閉である。外側の根となる子はc不可能なので、全生成がcなしでF1からτ(B_j)≥|y(j)|。実際のy(j)も生成なので逆向きの不等式もあり、等号である。各背骨節点の寄与をT3で≤θと数えて、μ≤(3v+vK_c)θ。K_c=∞なら有限上界の主張ではないが、不等式は拡張実数として自明である。

### R8 [正しい]

補題8はR1そのもの。𝒜(Q)のp_iはp₁,p₂,p₁₂全てがQ₃^{<μ}に入るという意味に固定する。p₁=p₂を排除してはいけない。Q₃有限なら𝒜(Q)も有限。

補題9で子孫z′はπ(y(z′))≤π(y(z))なので、要求される下界P−π(y(z′))の方が大きく、E_{z′}⊆E_z。E_t≠∅はω_tによる置換で証明できる。E_z≠∅な最深のz*を取れば全ての子でE=∅。

子にcを含む生成が一つでもあれば、その置換語はa,bの印を保持し、パリクab部分がP−π(y(z′))以上なのでE_{z′}の元となり矛盾。従って全生成がcなしで、F1からτ(A_{z′})≥|y(z′)|。ρの式で|M|=|y(z*)|≤θ。包含からM≤π(y(t))。

ここで得るw（後のq）は短いとは限らない。N5′がq∈Q₃とだけ指定し、Q₃^{<μ}を要求していないのは正しい。

## 5. S：帰結・適用範囲

### S1 [正しいが記述を直すべき]

定理4をQ₃全体に適用し、L=π⁻¹(Q)から全abc語の重みが共通になるので定理6が使える。実際、π(L)上での水準から語上の水準へ移す操作自体には飽和性まで要らないが、Q₃の閉包性をSUB₁から得る段ではこの設定を使っている。

(P⁺)とV∩Q₂は使わない。短い部分の水準版にはSUB₁・有限性さえ不要。ただし**ab語の存在は残る**。独立した系の文面には「Q₂≠∅」を加える。これを完全に落とした文字通りの文では、L={abc}、Q₃一点、μ_ab=∞が反例となるが、報告全体の継承された設定の下では主結果の反例ではない。

なおQ₃^{<μ}は一般に閉じていないため、そのrank≤2だけから定理4を再適用して正の水準を得てはいけない。報告はその誤用をしていない。

### S2 [正しいが記述を直すべき]

rank H₃=3なら、c座標射影の核H₃⁰のrankは2。許容格子K₂にrank 2があれば、あるm≥1について(m,m,0)∈K₂。q₂+k(m,m,0)が全てQ₂に入り(P⁺)を生む。従って¬(P⁺)ではrank K₂≤1、rank(K₂+H₃⁰)=2なので指数は無限。全許容K₂で無限だからF_L=∞。

許容格子が存在すること（例えばH₂）はC24に依存する。またSUB₁・Q₃有限非空の設定では、(P⁺)は実際に不可能である：Q₂の狭義正の差hを任意のQ₃点から反復すると、C23によりQ₃が無限になる。この一文を補えば、¬(P⁺)を省略した見出しも説明できる。

「有限のrank 3集合」だけで任意のQ₂についてF_L=∞と言ってよいわけではない。SUB₁およびQ₂≠∅の文脈を外さないこと。

### S3 [正しいが記述を直すべき]

Y₂₃の高さは5,1,2,1。和が既存の高さになるのは1+1=2だけで、2個の高さ1点を重複可・順序なしで選ぶ3通りを報告は全て列挙している。Π₂に残るのは(14,19,0)だけでP=(10,23,0)とは異なる。高さ5は、他との和が既存の高さを越えるため候補にならない。

Xでは高さが1,2,3で、候補は1+1=2と1+2=3だけ。対応する頂点は(5,1,0),(2,4,0)。しかし全abc点の長さは6=μなので短い部分は空。従ってP∉𝒜(Q)。結論は修正不要。

### S4 [正しいが記述を直すべき]

命題12の `W_t=A` 等は語とベクトルを同一視しているので `π(W_t)=A` と直す。また例の点Mと補題9の不足を覆うベクトルMは、M₀とM*などに分けると誤読を避けられる。

高さ1,1,2,4からの組は1+1=2と2+2=4だけ。2M₀−Z=(3,3,0)≠P、2A−M₀と2B−M₀はΠ₂の外なので、A,B,M₀の組に限定される。

ω,ω′のab成分を(x,y),(x′,y′)とするとY₁=(X−1+x,−1+y)、Y₂=(−1+x′,Y−1+y′)。非負性からy≥1,x′≥1。印が両部分木の外にあることからY₁+Y₂≤(X−1,Y−1)であり、x+x′≤1,y+y′≤1。従って(x,y)=(0,1)、(x′,y′)=(1,0)、Y₁=(X−1,0)、Y₂=(0,Y−1)。

補題9をtに使うとq_b≥Y。Q₃中でこれを満たすのはAだけ（Y≥4を使用）。q_a=1なのでM*_a≥X−1だがM*≤Y₁よりM*=Y₁。|Y₁|≤θとなり重さに反する。これは全てのX,Y≥4に有効。

### S5 [正しい]

短い点の高さは1,…,nおよび2n。3点とも線分上の場合はi+j≤nのときだけs_{i+j}を引けて、結果は(0,2n+2,0)なのでΠ₂の外。p₁₂=Zならi+j=2nなのでi=j=nに限り、2s_n−Z=(4n−1,3,0)≠P。p₁またはp₂がZなら和の高さ>2nで短い点に対応するp₁₂がない。これでp₁=p₂を含め尽くしている。

### S6 [穴]：必要条件は正しいが、予想の対象が狭い

**数式の翻訳そのものは正しい。** R1の置換式からN1。3語の長さ<μからN2。R_i=π(ω_i)、Y_i=π(y(t_i))とすればN3。印が外にあることと2部分木の非重複性からN4。補題9を各t_iに適用すればN5′。θ=θ_locで全て成り立つ。Mは非負整数ベクトル、N2のiは1,2,12を意味すると明記するとよい。

**欠けているのは、Qに関する仮定の移送である。** 命題7.3・7.4のQは一般のQ₂や他の支持の点を持てる。しかし予想7.5は冒頭で `Q={P}∪Q₃` と限定している。N1〜N5′が元のQから得られたことだけでは、Q₂の他点を除いたQ′={P}∪Q₃が(T)を満たすことは従わない。

この懸念は単なる形式上のものではなく、**最短点P∈Vを残す削除が(T)を壊す例**がある。

Q₃=F_{5,4}={(1,5,1),(6,1,1),(2,2,2),(1,1,4)}、

Q₂={(1,15,0),(6,11,0),(11,7,0),(16,3,0)}。

Q=Q₂∪Q₃は(T)を満たす。Q₂はh=(5,−4,0)方向の完全な正領域内の列で、Q₂の差は±h,±2h,±3h。Q₃上で±hは同じ高さのA,Bを交換するか領域外へ出し、±2h,±3hは有効な新しい移動を生じない。Q₃の高さが異なる差はab支持に作用しない。独自コードも(T)の定理2.1の式を直接確認した。

P=(1,15,0)は長さ16の一意の最短ab点で、他の長さは17,18,19。A=(1,5,1), B=(6,1,1), M₀=(2,2,2), Z=(1,1,4)として

P−A=2(B−A)−10(M₀−A)+3(Z−A)

だからP∈V。Q₃は有限非空、¬(P⁺)で、元の命題7.3の設定に入る。

ところがQ′={P}∪Q₃では、h=(5,−4,0)とγ=(0,10,0)に対し、(T)の左辺(1,15,0)は所属し、右辺(6,11,0)は不所属。従ってQ′は(T)を満たさない。

**この例は予想7.5の反例でも、場合(ii)からの適用に対する反例でもない。** Pのa座標が1なのでN4からY₁,Y₂のa座標は0となり、この例で場合(ii)が起こると主張してはいない。示したのは、報告にない「最短点だけを残せばよい」という一般的な補助命題では穴を埋められないということに限る。

修復候補は次のいずれか。

1. 予想を一般の(T)を満たすQに拡張し、P∈Q₂を最短点、Q₃を有限とした形で述べ直す。その**強い予想が真なら**定理6への帰着は通る。
2. 場合(ii)の追加条件の下で、必要なsingletonへの縮約を証明する。単なる最短性・P∈Vだけでは上の例により不十分。
3. 現行予想7.5の帰結をQ₂={P}の言語に限定する。他の支持全体を削除する操作は、(T)の両端が同じ支持を持つため問題ない。問題は同じab支持内の一部だけを削除することにある。

従って「場合(ii)ならN1〜N5′」は支持するが、「だから記載どおりの予想7.5で一般の穴が空になる」は現状では支持しない。分類は(iii)の修復を目指す穴であり、主定理の結論を否定する(i)や定数修正(ii)ではない。

### S7 [正しいが記述を直すべき]：範囲を一文で

**これらは指定された一頂点の条件下で稀な内容型{a,b}の最短長μ_abが文法量に対し多項式であることを示し、その型を使う `prop:rare-type` の超多項式下界の経路をその範囲で排除するが、他の型、タプルの厚さτ、特徴データ全体の多項式上界、または `op:fanout-two` の解決は与えない。**

## 6. 独自計算と再現性

### 6.1 方法

全て整数計算。rankと正の水準の判定は定理4を仮定せず実装した：差が0なら任意の正重み、rank 1なら方向に正負両成分があること、rank 2なら外積による法線の3成分が全て狭義同符号であることを確認し、rank 3は不成立とする。これは3次元の線形代数による独立判定である。

(T)はC21の `h⁻+1_supp h+γ∈Q ⇔ h⁺+1_supp h+γ∈Q` を直接実装。有限QではどちらかがQの点となるγだけで十分。閉包性を(T)検査の代用にはしていない。

N5′のMの列挙は、D=(P−q)^+_abを使い「D≤Y_iかつ|D|≤θ」と完全に同値なので、M=Dを選ぶ形で消去した。N3のrのc座標を固定し、a,b座標を非負整数で全列挙した。

再現コマンド：

```bash
python3 astra_check_prop73_2026-11-07.py --seed 731107
```

`--part examples`、`--part closures`、`--part grammars`、`--part conjecture`でも各部分を実行できる。各部分は同じseedで独立に初期化するので、分割実行と一括実行の結果は一致する。

### 6.2 定理4の反例探索

閉包は3〜5点の種からp+q−rを飽和する。座標が上端24に達したら破棄し、集合の要素数が160を超えた場合も未確定として破棄した。**破棄したものを有限閉包に数えていない。** 下端1はΠ₃そのものの境界であり、箱による人工的切断ではない。座標≤0の移動先は閉包の定義どおり不採用。

| 抽出 | 種の数 | 上端に接触・破棄 | 160点超・未確定 | 完全に飽和した有限閉包 | rank1 / rank2 / rank3 | 反例 |
|---|---:|---:|---:|---:|---|---:|
| [1,3]³の異なる3点を全列挙 | 2,925 | 1,940 | 701 | 284 | 12 / 272 / 0 | 0 |
| [1,8]³から3,4,5点を各1,000回 | 3,000 | 2,003 | 855 | 142 | 0 / 142 / 0 | 0 |
| 上と同じ、各点の一座標を1または2に偏らせる | 3,000 | 2,029 | 735 | 236 | 3 / 233 / 0 | 0 |

計662個の完全閉包は全てrank≤2で正の水準に乗った。これは重複を除いた集合の数ではなく、種ごとの成功件数である。rank 3を得られなかったことを不存在の根拠にはしない（例および§6.5では実際に得ている）。

### 6.3 例の検査

F₄、F_{X,Y}の292組、𝒮_nの28組、例4、X、Y₂₃を検査。全て閉包性・該当する行列式・(T)・記載のV所属式・短い部分の水準・頂点の主張に違反なし。F_L=∞は§5.2の証明を適用するものであり、有限探索で無限を推定していない。例4はθ=1,…,7を全探索し最小7、§3.4の手計算とも一致。

### 6.4 小文法の探索

v≤4、規則ランク≤2のCFGを使用。CFGはここで要求される線形・非削除文法の部分クラスである。fan-out 2以上のテンプレート全体を計算で検査したわけではない。

通常の乱択では、各非終端に長さ1〜3の端末規則1〜3本と、下位ラベルへのランク1または2の規則を作る。到達不能なラベルは除く。全ラベルは端末規則を持ち生成可能。巡回群では自己単位規則、または端末を加える巡回規則を加えた。最短ab長は、各非終端×8個の支持について最短長の固定点を計算して厳密に求めた。θはτからρを計算した正確なθ_loc。

非巡回・単位巡回・重み同次群ではパリク集合を固定点まで計算してK_cを厳密に求めた。成長巡回群では長さ<μの生成だけを固定点計算し、定理6のみを厳密検査した。**この群のK_cは認定していないので、補題7の検査数には含めない。**

重み同次群はλ_a,λ_b∈[1,3]、λ_c∈[2,5]、非終端のエネルギー4〜12を選び、端末寄与＋子エネルギーの和が親エネルギーに等しい規則だけを使う。正重みなので生成集合は有限で、全語が一つの水準に乗る。生成不能なエネルギー割当75件は不採用。

| 群（各1,000試行） | abあり | 短いabcなし（空虚） | 非空で正の水準 | 非空で仮定不成立 | 定理6検査数 | 補題7検査数 |
|---|---:|---:|---:|---:|---:|---:|
| 非巡回 | 534 | 464 | 47 | 23 | 511 | 534 |
| 単位自己巡回あり | 540 | 454 | 54 | 32 | 508 | 540 |
| 端末を加える巡回あり | 648 | 527 | 65 | 56 | 592 | 0 |
| 重み同次 | 795 | 418 | 377 | 0 | 795 | 795 |
| 明示的な相互巡回同次例1件 | 1 | 0 | 1 | 0 | 1 | 1 |

全検査で違反0。定理6の非空虚な検査は544件、定理6検査合計2,407件、補題7検査合計1,870件。明示例はS→A | aabb、A→S | abcで、λ=(1,1,2)、μ=4、短いabc点=(1,1,1)。相互巡回を含むが有限言語である。

最大比μ/((K_c+3)vθ)=1/3。定理6の最大比μ/max{9(r+1)vθ,11(r+1)v²θ⁴)}≈0.00568182。従って、検査は定数の鋭さにはほとんど迫っていない。反例0を証明の代わりにしない。

### 6.5 予想7.5の任意探索

座標≤8の次の26点のプールを固定した：少なくとも2座標が1である全22点と、(2,2,2),(2,2,3),(2,3,2),(3,2,2)。このプールの4点部分集合14,950個と5点部分集合65,780個を**全列挙**した。閉じたrank 3集合は計346個。その全てについて、候補Pをp₁+p₂−p₁₂から列挙し、Q={P}∪Fの(T)、短い点条件、N1〜N5′を検査した。

θは1≤θ≤floor((|P|−2)/2)−1を全列挙すれば足りる。理由はN3,N4から2(θ+1)≤|Y₁|+|Y₂|≤|P|−2だからである。θを実数としても|r_i|≤θ<|Y_i|と|M_i|≤θの可否は整数θに丸められる。

この限定プールではN条件を全て満たす候補は0件。追加で、一座標を1にした[1,8]³の4〜5点を10,000回抽出したが、閉じたrank 3集合は0件だった。**予想に対する正の証拠としては極めて弱い。** 箱[1,8]³全体の4〜5点集合を全列挙したとは主張しない。例4でN条件が実際に成立することは別途確認した。

### 6.6 元スクリプトの再実行

`reviews/check_claude_prop73_2026-11-07.py --seed 1` を実行し終了コード0。報告§8のE1〜E6の主要な件数・値を再現した：

- E1：乱択有限395、全列挙種41,664・有限5,606、反例0。
- E2：F₄のdet59、F_{X,Y}84組の不一致0、𝒮_nの3〜15、例4の最小θ7。
- E3：rank 3集合82、頂点38、短い頂点20、N条件成立0。
- E4：土台48、衛星追加rank 3が130、N条件成立87、短い部分の水準違反0。
- E5：X、Y₂₃の頂点リスト一致。
- E6：abあり非巡回9,071、仮定成立8,799、同次1,035、違反0、最大比も一致。

実行時間はE1約130秒、E2約2秒、E3約11秒、E4約17秒、E5ほぼ0秒、E6約15秒。環境差により報告の約1分45秒とは異なるが、数学的出力は一致した。これは独自検証件数に重ねて加算していない。

## 7. 別稿への採用判定

### 7.1 そのまま使える（明示された共通設定の下で）

- **抽象補題2・3、定理4の有限集合版。** 閉包を仮定する純粋な整数幾何の命題として使える。言語版のSUB₁⇒閉包はC23依存であり、C23の独立監査を完了したことにはならない。
- **補題5、定理6、補題7〜9。** 既約・線形・非削除、Σ={a,b,c}、ab語の存在、θ=θ_locを明記する。Hの指定された前提だけで証明を再現できる。定理6の定数max{9(r+1)vθ,11(r+1)v²θ⁴}を支持する。
- **例2、例3の幾何的主張、および例4のN条件の最小θ=7。** 一般パラメータの証明と有限検算が一致する。SUB₁およびC_{2,c_Σ}所属の宣言には未独立検証前提C21,C22への依存を付ける。
- **命題13。** 補題8と場合(i)の数え上げで上界を支持する。族のクラス所属はC21,C22依存。

### 7.2 直せば使える

- **例1**：36/48の通り数、D₃∩EとD₂の零差を修正。結論の変更なし。
- **系10**：独立した命題文にQ₂≠∅を入れる。rank版はC23依存、短い水準版は文法定理6から直接得られる。
- **命題11**：Y₂₃の高さの誤記だけを修正。上界は変更なし。
- **命題12**：語とパリクベクトルの等号を修正し、2種類のMを区別する。上界は変更なし。
- **rank 3⇒F_L=∞**：SUB₁・Q₃有限非空・Q₂≠∅という設定、または¬(P⁺)を明示する。C24による許容格子の存在を依存関係に残す。
- **命題7.4への帰着**：有限Q₃の場合のμ_abの問題として使用する。「一頂点の学習問題全体を閉じる」等の表現にはしない。

### 7.3 現状では使えない

- **命題7.3全体を解決済みとする主張。** 報告自体も部分結果であり、残りは未解決。
- **記載された予想7.5だけを一般Qに適用して、命題7.3が閉じるとする証明。** S6のsingletonへの縮約の穴を修復するか、帰結の対象を限定する必要がある。
- **予想7.5そのものを証明済みの命題とすること。** 有限探索はその代わりにならない。
- **τや特徴データの全体上界、op:fanout-twoの肯定。** μ_abの上界からは出ない。

### 7.4 「一頂点で残るのは命題7.4だけ」への最終判定

**限定された意味では支持するが、無条件の総合認定はしない。**

Q₂≠∅、Q₃有限という現在の命題7.3の範囲では、短い部分が正の水準なら定理6、そうでなくても選んだ最短点Pが𝒜(Q)に入らなければ補題8で場合(ii)を排除できる。従って残りを命題7.4として切り出すことは正しい。支配条件に違反する文法も補題9で除けるが、θ依存なので命題7.4の言語だけの仮定と同一視しない。

一方、**全ての一頂点言語のμ_ab問題**で残りが7.4だけというためには、Q₃無限の場合の7.2報告定理A、(P⁺)の場合の閉包報告の結果等を使う。今回前提として許可された7.2補題1・系2(a)だけでは、その大域的な主張は認定できない。これらの追加結果が正しいという条件付きなら、その意味での縮約を支持する。さらにS6により、現行の予想7.5を証明するだけでこの一般的縮約の残りまで消える、とまでは言えない。

採用上の推奨は、**定理4と定理6を独立した確定命題として置き、系10と命題11〜13を依存関係付きで採用し、命題7.4と予想7.5は未解決部分として明確に分ける**ことである。

## 付録A：独自スクリプト全文

以下は提出した `.py` と同一の全文。標準ライブラリのみ。

```python
#!/usr/bin/env python3
"""Independent audit; standard library only. No imports from supplied scripts.
Run: python3 astra_check_prop73_2026-11-07.py --seed 731107
All vector/rank/level/condition checks use exact integers.
"""
import itertools as it, random, json, argparse, collections
Z=(0,0,0)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def mask(a): return sum((x>0)<<i for i,x in enumerate(a))
def pos(a): return min(a)>0
def rank_level(F):
    F=list(F)
    if len(F)<2:return 0,True
    D=[sub(p,F[0]) for p in F[1:] if p!=F[0]]
    if not D:return 0,True
    d=D[0]; normal=next((cross(d,e) for e in D if cross(d,e)!=Z),None)
    if normal is None:return 1,min(d)<0<max(d)
    if any(dot(normal,e) for e in D):return 3,False
    return 2,min(normal)>0 or max(normal)<0

def closed(F):
    F=set(F)
    return all(not pos(x) or x in F for p,q,r in it.product(F,repeat=3) for x in [sub(add(p,q),r)])
def closure(seed,B=24,cap=160):
    F=set(seed)
    if any(max(p)>=B for p in F):return None,'boundary'
    while True:
        extra=set()
        for p,q,r in it.product(tuple(F),repeat=3):
            x=sub(add(p,q),r)
            if pos(x) and x not in F:
                if max(x)>=B:return None,'boundary'
                extra.add(x)
                if len(F)+len(extra)>cap:return None,'cap'
        if not extra:return F,'complete'
        F.update(extra)

def Tcheck(Q):
    Q=set(Q)
    for q,q1 in it.product(Q,repeat=2):
        if q==q1 or mask(q)!=mask(q1):continue
        h=sub(q1,q)
        lo=tuple(max(-x,0)+(x!=0) for x in h)
        hi=tuple(max(x,0)+(x!=0) for x in h)
        # If either side belongs to Q, gamma is exactly p-lo or p-hi.
        gs={sub(p,b) for p in Q for b in [lo,hi] if min(sub(p,b))>=0}
        for g in gs:
            a,b=add(lo,g),add(hi,g)
            if (a in Q)!=(b in Q):return {'h':h,'gamma':g,'ends':[a,b]}
    return None

def apexes(F,P=None):
    if P is not None:F=[q for q in F if sum(q)<sum(P)]
    return [(p,q,r,sub(add(p,q),r)) for p,q,r in it.product(F,repeat=3)
            if sub(add(p,q),r)[2]==0 and min(sub(add(p,q),r)[:2])>0]

def Nwitness(F,P,theta):
    # Enumerate all p1,p2,p12, r1,r2; eliminate M exactly via minimal deficit.
    opts={}
    for p in F:
        if sum(p)>=sum(P):continue
        o=[]
        for a in range(max(0,theta-p[2]+1)):
            for b in range(theta-p[2]-a+1):
                r=(a,b,p[2]); Y=(P[0]-p[0]+a,P[1]-p[1]+b)
                if min(Y)<0 or sum(Y)<=theta:continue
                for q in F:
                    D=(max(P[0]-q[0],0),max(P[1]-q[1],0))
                    if sum(D)<=theta and all(x<=y for x,y in zip(D,Y)):
                        o.append((r,Y,q,D));break
        opts[p]=o
    for p,q,r,p0 in apexes(F,P):
        if p0!=P:continue
        for u,v in it.product(opts.get(p,[]),opts.get(q,[])):
            if all(u[1][i]+v[1][i]<=P[i]-1 for i in range(2)):
                return {'p1':p,'p2':q,'p12':r,'r1':u[0],'Y1':u[1],'q1':u[2],'M1':u[3],
                        'r2':v[0],'Y2':v[1],'q2':v[2],'M2':v[3]}
    return None

def examples():
    out={}; F=[(1,3,12),(4,8,1),(6,4,4),(12,1,3)];P=(10,5,0)
    cases=[(p,q,r,sub(add(p,q),r)) for p,q,r in it.product(F,repeat=3) if q!=r]
    nontr=[x for p,q,r,x in cases if p!=r]
    assert closed(F) and Tcheck(F+[P]) is None
    assert sub(add(F[1],F[3]),F[2])==P
    out['F4']={'q_ne_r':len(cases),'nontrivial_ordered':len(nontr),
      'nontrivial_positive':sum(pos(x) for x in nontr),
      'det':det(sub(F[0],F[1]),sub(F[2],F[1]),sub(F[3],F[1])),
      'nontrivial_unique_expressions':24}
    rows=[]
    for X,Y in it.chain(it.product(range(4,21),repeat=2),[(30,5),(25,40),(60,7)]):
        A,B,M,C=(1,Y+1,1),(X+1,1,1),(2,2,2),(1,1,4);F=[A,B,M,C];P=(X,Y,0)
        assert closed(F) and Tcheck(F+[P]) is None
        assert det(sub(A,M),sub(B,M),sub(C,M))==3*X+3*Y-2*X*Y
        assert sub(add(A,B),M)==P and rank_level(F)==(3,False)
        assert all(sum(p)<sum(P) for p in F)
        assert Nwitness(F,P,min(X,Y)-2) is None
        rows.append((X,Y))
    out['FXY']={'parameter_count':len(rows),'range':'4..20 squared plus (30,5),(25,40),(60,7)'}
    rows=[]
    for n in range(3,31):
        s=[(2*k,2*(n+1-k),k) for k in range(1,n+1)]; C=(1,1,2*n);A=(4*n,1,1);F=s+[C,A];P=(4*n-3,3,0)
        d=sub(s[1],s[0]);h=sub(C,s[0]);j=sub(A,s[0])
        assert closed(F) and Tcheck(F+[P]) is None
        assert det(d,h,j)==2*n-1
        assert add(tuple(-2*n*x for x in d),add(h,tuple(2*x for x in j)))==sub(P,s[0])
        lam=(2*n-1,4*n-1,4*n)
        short=[q for q in F if sum(q)<sum(P)]
        assert set(short)==set(s+[C]) and {dot(lam,q) for q in short}=={8*n*n+6*n-2}
        assert not any(x[3]==P for x in apexes(F,P))
        assert len({q[2] for q in F})==n+1
        rows.append(n)
    out['Sn']={'range':[3,30],'count':len(rows)}
    F=[(1,4,6),(3,9,3),(9,3,1),(1,27,1)];P=(5,14,0)
    assert closed(F) and Tcheck(F+[P]) is None and rank_level(F)==(3,False)
    assert sub(tuple(2*x for x in F[1]),F[0])==P
    assert {dot((2,1,3),p) for p in F[:3]}=={24}
    ws={t:Nwitness(F,P,t) for t in range(1,8)}
    assert all(ws[t] is None for t in range(1,7)) and ws[7] is not None
    out['example4']={'theta1to7':ws,'det':det(*[sub(p,F[0]) for p in F[1:]])}
    for name,F,P in [('X',[(3,2,1),(1,3,2),(2,1,3)],(5,1,0)),
          ('Y23',[(1,2,5),(1,26,1),(11,10,2),(24,3,1)],(10,23,0))]:
        assert Tcheck(F+[P]) is None
        assert not any(t[3]==P for t in apexes(F,P))
        out[name]={'apexes':sorted({t[3] for t in apexes(F)}),'short_apexes':sorted({t[3] for t in apexes(F,P)})}
    F=[(1,5,1),(6,1,1),(2,2,2),(1,1,4)];P=(1,5,0);P1=(6,1,0)
    assert Tcheck(F+[P,P1]) is None and Tcheck(F+[P]) is not None
    out['singleton_deletion']={'Q3':F,'Q2':[P,P1],'failure':Tcheck(F+[P])}
    P=(1,15,0);Q2=[(1,15,0),(6,11,0),(11,7,0),(16,3,0)]
    assert Tcheck(F+Q2) is None and Tcheck(F+[P]) is not None
    ds=[sub(p,F[0]) for p in F[1:]]
    assert add(add(tuple(2*x for x in ds[0]),tuple(-10*x for x in ds[1])),tuple(3*x for x in ds[2]))==sub(P,F[0])
    out['singleton_deletion_in_V']={'Q3':F,'Q2':Q2,'P_in_V_coefficients':[2,-10,3],'failure':Tcheck(F+[P])}
    return out

def seed_search(rng):
    out={}
    for mode in ['exhaustive3','uniform','biased']:
        stats=collections.Counter();witness=[]
        if mode=='exhaustive3': seeds=it.combinations(list(it.product(range(1,4),repeat=3)),3)
        else:
            seeds=[]
            for _ in range(3000):
                F=set()
                while len(F)<3+_%3:
                    p=[rng.randint(1,8) for i in range(3)]
                    if mode=='biased':p[rng.randrange(3)]=rng.randint(1,2)
                    F.add(tuple(p))
                seeds.append(F)
        for seed in seeds:
            stats['seeds']+=1;F,status=closure(seed)
            stats[status]+=1
            if F is not None:
                r,level=rank_level(F);stats['rank'+str(r)]+=1
                if r<=2 and not level:witness.append(sorted(F))
        out[mode]={'counts':dict(stats),'violations':witness}
    return out

# Rules: (lhs, terminal Parikh vector, ordered tuple of child labels).
# These are ordinary CFGs, a subclass of the stipulated linear nondeleting grammars.
def accessible(rules):
    seen={0}
    while True:
        s=seen|{b for a,t,ch in rules if a in seen for b in ch}
        if s==seen:return sorted(seen)
        seen=s

def minimums(rules,v):
    inf=10**30;m=[[inf]*8 for _ in range(v)]
    while True:
        change=False
        for a,t,ch in rules:
            for ms in it.product(*[[i for i in range(8) if m[b][i]<inf] for b in ch]):
                s=mask(t);cost=sum(t)
                for b,k in zip(ch,ms):s|=k;cost+=m[b][k]
                if cost<m[a][s]:m[a][s]=cost;change=True
        if not change:return m,inf

def yields(rules,v,limit=None,cap=20000):
    sets=[set() for _ in range(v)]
    while True:
        change=False
        for a,t,ch in rules:
            for ps in it.product(*[tuple(sets[b]) for b in ch]):
                q=t
                for p in ps:q=add(q,p)
                if limit is not None and sum(q)>=limit:continue
                if q not in sets[a]:sets[a].add(q);change=True
                if len(sets[a])>cap:return None
        if not change:return sets

def assess_grammar(rules,v,stats,finite=True):
    keep=accessible(rules); mp={x:i for i,x in enumerate(keep)}
    rules=[(mp[a],t,tuple(mp[b] for b in ch)) for a,t,ch in rules if a in mp];v=len(keep)
    m,inf=minimums(rules,v)
    if any(min(row)>=inf for row in m):stats['unproductive_skipped']+=1;return
    mu=m[0][3]
    if mu>=inf:stats['no_ab']+=1;return
    tau=[min(row) for row in m];theta=max(sum(t)+sum(tau[b] for b in ch) for a,t,ch in rules)
    r=max(1,max(len(ch) for a,t,ch in rules))
    stats['with_ab']+=1
    if finite:
        sets=yields(rules,v)
        if sets is None:stats['set_cap_skipped']+=1;return
        Q=sets[0];K=len({p[2] for p in Q if mask(p)==7})
        stats['lemma7_tested']+=1
        assert mu<=(K+3)*v*theta,(rules,mu,K,v,theta)
        stats['max_lemma7_ratio']=max(stats['max_lemma7_ratio'],mu/((K+3)*v*theta))
        short=[p for p in Q if mask(p)==7 and sum(p)<mu]
    else:
        sets=yields(rules,v,mu)
        if sets is None:stats['set_cap_skipped']+=1;return
        short=[p for p in sets[0] if mask(p)==7]
        stats['lemma7_not_certified']+=1
    lev=rank_level(short)[1]
    stats['vacuous' if not short else 'nonvacuous_level' if lev else 'hypothesis_false']+=1
    if lev:
        bound=max(9*(r+1)*v*theta,11*(r+1)*v*v*theta**4)
        assert mu<=bound,(rules,mu,v,theta)
        stats['theorem6_tested']+=1
        stats['max_theorem6_ratio']=max(stats['max_theorem6_ratio'],mu/bound)

def grammar_search(rng):
    out={}
    terminals=list(it.product(range(3),repeat=3));terminals=[p for p in terminals if 1<=sum(p)<=3]
    for mode in ['acyclic','identity_cycles','growing_cycles','homogeneous']:
        stats=collections.Counter()
        for trial in range(1000):
            v=rng.randint(1,4);rules=[]
            if mode=='homogeneous':
                lam=(rng.randint(1,3),rng.randint(1,3),rng.randint(2,5))
                energies=[rng.randint(4,12) for _ in range(v)];energies[0]=max(energies)
                ts=[p for p in it.product(range(13),repeat=3) if sum(p)>0 and dot(lam,p)<=12]
                for a in range(v):
                    allowed=[p for p in ts if dot(lam,p)==energies[a]]
                    if not allowed:break
                    for t in rng.sample(allowed,min(4,len(allowed))):rules.append((a,t,()))
                    choices=[(t,ch) for k in [1,2] for ch in it.product(range(v),repeat=k)
                             for t in [Z]+ts if dot(lam,t)+sum(energies[b] for b in ch)==energies[a]]
                    for t,ch in rng.sample(choices,min(4,len(choices))):rules.append((a,t,ch))
                else:
                    assess_grammar(rules,v,stats);continue
                stats['unrepresentable_energy']+=1;continue
            for a in range(v):
                for _ in range(rng.randint(1,3)):rules.append((a,rng.choice(terminals),()))
                for _ in range(rng.randint(1,3)):
                    children=list(range(a+1,v))
                    if children:
                        ch=tuple(rng.choice(children) for _ in range(rng.randint(1,2)))
                        rules.append((a,rng.choice([Z]+terminals),ch))
                if mode=='identity_cycles':rules.append((a,Z,(a,)))
                if mode=='growing_cycles':rules.append((a,rng.choice(terminals),(rng.randrange(v),)))
            assess_grammar(rules,v,stats,finite=mode!='growing_cycles')
        out[mode]=dict(stats)
    # Explicit homogeneous, nonvacuous, productive cyclic example.
    rules=[(0,Z,(1,)),(1,Z,(0,)),(0,(2,2,0),()),(1,(1,1,1),())]
    st=collections.Counter();assess_grammar(rules,2,st);out['explicit_homogeneous_cycle']=dict(st)
    return out

def conjecture_search(rng):
    # Complete enumeration within a stated biased pool, not the whole cube.
    pool=[p for p in it.product(range(1,9),repeat=3) if sum(x==1 for x in p)>=2] + [(2,2,2),(2,2,3),(2,3,2),(3,2,2)]
    stats=collections.Counter();viol=[]
    for k in [4,5]:
        for F in it.combinations(pool,k):
            stats['seeds'+str(k)]+=1
            if rank_level(F)[0]!=3 or not closed(F):continue
            stats['closed_rank3']+=1
            Ps={t[3] for t in apexes(F)}
            for P in Ps:
                if Tcheck(list(F)+[P]) is not None:continue
                for theta in range(1,max(1,(sum(P)-2)//2)):
                    w=Nwitness(F,P,theta)
                    if w:
                        stats['admissible']+=1
                        if not rank_level([p for p in F if sum(p)<sum(P)])[1]:viol.append([F,P,theta,w])
                        break
    # Complement with biased random points in [1,8]^3.
    for _ in range(10000):
        F=set()
        while len(F)<4+_%2:
            p=[rng.randint(1,8) for i in range(3)];p[rng.randrange(3)]=1
            F.add(tuple(p))
        stats['random_seeds']+=1
        if rank_level(F)[0]!=3 or not closed(F):continue
        stats['random_closed_rank3']+=1
        for P in {x[3] for x in apexes(F)}:
            if Tcheck(list(F)+[P]) is not None:continue
            for theta in range(1,max(1,(sum(P)-2)//2)):
                w=Nwitness(F,P,theta)
                if w:
                    stats['random_admissible']+=1
                    if not rank_level([p for p in F if sum(p)<sum(P)])[1]:viol.append([sorted(F),P,theta,w])
                    break
    return {'pool':pool,'counts':dict(stats),'violations':viol}

def main():
    p=argparse.ArgumentParser();p.add_argument('--seed',type=int,default=731107);p.add_argument('--part',default='all');args=p.parse_args()
    rng=random.Random(args.seed)
    funcs={'examples':lambda:examples(),'closures':lambda:seed_search(random.Random(args.seed)),'grammars':lambda:grammar_search(random.Random(args.seed)),'conjecture':lambda:conjecture_search(random.Random(args.seed))}
    for name,f in funcs.items():
        if args.part in ['all',name]:print(json.dumps({'part':name,'seed':args.seed,'result':f()},ensure_ascii=False),flush=True)
if __name__=='__main__':main()

```
