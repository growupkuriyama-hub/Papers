# 論文09・最終差分査読（2026-11-28 夜）

## 対象・検査範囲

- リポジトリ: https://github.com/growupkuriyama-hub/Papers
- 固定比較元: `5cdba4f16c1ae8ea0d29f413908d8b62cd99ed52`
- 固定対象: `0f10a5e4b9c9dd69259c824646a62693763c9757`
- 対象ファイル: `09_typed-fcp-fkp/main.tex`（Git blob `5023c71b66bbd76d98ea06e3792dc8024ece7297`、1911物理行）。旧blob `f0f6c03b2cdb9de5ad8dafdefbb3f9dbf94cbbda`。
- 2版の全文をGitHub connectorで取得し、行単位LCS差分を計算。48追加・46削除（GitHub比較結果と一致）、指定E1–E5のみ。以下の原稿行番号はすべて新コミットの物理行番号。
- 許可された前回の `findings.csv` のみ参照し、他の `research/`、`japanese/`、以後の更新を開いていない。GitHubへの書き込みなし。
- §5の典拠は添付プロジェクト資料02 v8の合本pp.171–186に収録されたKanazawa (WoLLIC 2023) 著者稿（単独 `kanazawa-invited.pdf` は作業環境になく、独立ファイルのバイト同一性は未確認）。原稿pp.2–4,8–15を直接読んだ。本文主張の数学的照合を実施。対象 `main.pdf` はraw URL取得失敗のため目視・24頁の照合・再コンパイルは未実施（UNCHECKED）。本査読は差分限定であり、全定理の独立再証明ではない。

**判定：局所的な修正で投稿してよい。** 今回の差分から主要定理の新たな反例や数値的矛盾は発見しなかった。ただしAbstractの因果関係の圧縮は修正すべき。以下のGAPは説明・依存関係の問題であり、§5の定理そのものの反証ではない。

## E1 Abstract（l.73–95）

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
| --- | --- | --- | --- | --- |
| 73–76 | frames / exemplars の定義 | OK | l.113–129の閉包の説明と整合。フレーム側も全指定フレームに適合する表現の集合であることを明示すると対称的。 | Distributional approaches name syntactic categories by frames or exemplars: expressions fitting all given frames or all frames shared by the exemplars. |
| 76–77 | KY2017の学習成功の特徴づけ（F01） | UNCLEAR | l.123–126, 444–453。特徴づけは very weak 版で、所属質問つきの対応アルゴリズムについてのもの。 | Kanazawa and Yoshinaka (2017) characterized learners' success with membership queries by very weak finite context and kernel properties. |
| 78–79 | 二つの表示の指数分離 | OK | 定理A・Cは同一言語族での表示尺度の分離を与える。任意の二つの表示同士の比や、観測器なしの最小総長の比は主張しない。 | — |
| 79–81 | abstract licensing condition / n levels（F02） | UNCLEAR | l.159–179, 681–694。単一葉記号、各根葉路の構成子数n、少なくとも一つの印を要求する。言語学的な実証主張はない。 | Consider an abstract licensing condition: structures over one leaf symbol, built by binary combination and unary marking with exactly $n$ constructors on every branch, must contain a mark. |
| 81–85 | need only n+1; 2n, 3n; exponentially many productions | OK | 定理A(i), l.186–197、命題4.3 l.780–794。実在するF_nの規則数は2^n+2n−2。need only は通常上界の意味で最小性を断定しない。 | An untyped frame grammar has $n+1$ nonterminals, one frame of length at most $2n$ per nonterminal, and right-hand sides of length at most $3n$, but exponentially many productions. |
| 85–86 | the three quantities / tight（F03） | UNCLEAR | 定理A(ii),(iii), 定理4.7 l.880–899。最大長と max(kappa,1) を明示すべき。下界B_n=3·2^n−n−5=Theta(2^n)、実例の上界O(n·2^n)であり、最小積の近似である。 | For every exemplar presentation, the product of nonterminal count, maximal right-hand-side length and the greater of one and the maximal exemplar length has an exponential lower bound, attainable within a factor $O(n)$. |
| 86–87 | Hence specific learners（F04） | GAP | l.925–928, 970–1061。Rec_sとprimalは積の下界から、dualは規則の反証から出る。This yields ... への置換だけではdualも含むなら同じ因果の問題。 | Specific reconstruction and learning algorithms also require data of exponential total length. |
| 87–90 | mark observer / total length（F05） | UNCLEAR | 定理C(iii), 命題6.7 l.1330–1349。総長は全規則と全witnessを数える（l.582–599）。型なしも明示的に含まれる。any observer は型なしを文字どおりには含まない（s_0も型なしとは異なる）。 | Counting all productions and witnesses, a two-valued observer recording mark presence permits a frame presentation of total length $O(n^2)$; every exemplar presentation has at least exponential total length, typed or untyped. |
| 90–92 | without an observer ... marked leaf / unmarked pair（F05） | UNCLEAR | 定理C(iv), l.290–292、l.1380–1483。特定の unary-marked a と binary-combined aa の型が一致する場合、または型なしの場合の下界。分離が十分とはいっていない。裸のaaではない。 | Frames likewise have exponential total-length lower bounds without an observer separating a unary-marked leaf from the binary combination of two unmarked leaves. |
| 92–93 | frame upper and exemplar lower bounds extend to suitable one-word deletions | OK | 定理6.8 l.1357–1378は有限L、理想、初期記号の分離、ideal-forcing frames、capture条件を仮定。suitable と upper/lower の明示でC02は閉鎖。一般の無観測フレーム下界までは含まない。 | — |
| 93–95 | Refining the observer ... some, but not all | OK | 定理B l.259–272、命題l.1098–1139。strong/very weak FCPは単調、weak/very weak FKPは反単調、weak FCPは非単調、strong FKPは未解決（l.1560–1563）。help/hurtはクラス包含であり全表示のサイズ比較ではない。 | Refinement can only enlarge strong and very weak finite context classes and shrink weak and very weak finite kernel classes; the weak finite context property is not monotone. |
| 73–95 | JoLLI向け表現・語数（F12） | STYLE | 現行版は空白区切り248語。ハイフン分割では251語。略語の未定義はなく、残る数式は n, n+1, 2n, 3n, O(n), O(n^2) のみ。l.81–86の長文は分けるのがよい。 | 下記の全文差し替え案（240語）。 |

### 個別論点の補足

- **need only**：存在定理として自然であり、n+1が最小であるという主張には通常ならない。もっとも、A(i)はF_nの存在とその仕様だけを述べるので、a frame grammar hasが誤読されにくい。
- **tightness**：A(ii)の普遍下界は \(B_n=3\cdot2^n-n-5\)、A(iii)の具体的上界は \(8n\max(3\cdot2^{n-1}-2,2n+1)\)。したがって最小積は両者の間にある。l.889–899のlisting grammarの例も同じO(n)因子内。任意の表示の積に上界を課すのではない。M_nは非空でεを含まないため、初期の非空SPP成分に少なくとも一つの非空kernel wordが必要で、実際のκ≥1。それでも一般定義のmaxを保つ方が安全。
- **learning**：Rec_sはM_n∈C_sのsに限る。primalは固定r,kで指数下界、dualはuntypedまたはs_U、r≥2での長いデータの必要性。Abstractのspecificで一般学習器への量化は避けられているが、Henceがdualの独立証明まで含むと誤った依存関係となる。単にThis yieldsと置換しても同じ。alsoで切る。
- **total length**：定義l.582–599では規則とkernel/frameの全長を数え、観測器そのもの、型ラベル、初期集合は数えない。定理C(iii)の下界は \(2\sqrt{B_n}\)、C(iv)は \(2^{n/2}\)。いずれも指数的下界。未型付けをtrivial typingと同一視できない（l.604–606）。型なしの両最小総長の比はOpen Problem（l.1549–1557）。
- **観測器条件**：C(iv)の対は正確には $\Lce a\Rce$ と $\Lfl aa\Rfl$。この二語を区別することは多項式総長の必要条件にすぎず、十分ではない。実際、長さparityはj=1を区別するがj=2を区別せず指数下界（l.1475–1479）。
- **一般化**：定理6.8では有限L、二側理想によるちょうど一語の除去、initial nonterminalがRHSに出ないこと、non-initial framesが理想をforceすること、Lemma 4.5のcapture条件が必要。一般の場合のexemplar下界は|R|、総長下界は2sqrt(|R|)。多項式総長上界が任意の削除で成立するという主張は避ける。固定観測器と元の提示が小さいという条件下の上界である。
- **言語学的含意**：l.159–179およびl.1579–1593で、stress/caseのモデルではなく存在型条件の論理形式の抽象化、worst-case separationであると明記。Abstractのabstract licensing condition自体は過大ではない。一葉記号の明示によりモデルの制約がより見える。
- **投稿規程**：Springer JoLLI公式 https://link.springer.com/journal/10849/submission-guidelines は150–250語、未定義略語や特定不能な参照を避けることを要求する。引用著者・年は特定可能。下の案は両方のカウント規約で250以下。

### Abstract差し替え案（全文）

Distributional approaches name syntactic categories by frames or exemplars: expressions fitting all given frames or all frames shared by the exemplars. Kanazawa and Yoshinaka (2017) characterized learners' success with membership queries by very weak finite context and kernel properties. These presentations can differ exponentially for context-free languages. Consider an abstract licensing condition: structures over one leaf symbol, built by binary combination and unary marking with exactly $n$ constructors on every branch, must contain a mark. An untyped frame grammar has $n+1$ nonterminals, one frame of length at most $2n$ per nonterminal, and right-hand sides of length at most $3n$, but exponentially many productions. For every exemplar presentation, the product of nonterminal count, maximal right-hand-side length and the greater of one and the maximal exemplar length has an exponential lower bound, attainable within a factor $O(n)$. Specific reconstruction and learning algorithms also require data of exponential total length. Counting all productions and witnesses, a two-valued observer recording mark presence permits a frame presentation of total length $O(n^2)$; every exemplar presentation has at least exponential total length, typed or untyped. Frames likewise have exponential total-length lower bounds without an observer separating a unary-marked leaf from the binary combination of two unmarked leaves. The frame upper and exemplar lower bounds extend to suitable one-word deletions. Refinement can only enlarge strong and very weak finite context classes and shrink weak and very weak finite kernel classes; the weak finite context property is not monotone.

語数：240（空白区切り、各数式1語、ハイフン語1語）；ハイフン区切りを分割する保守的計数で248。現行はそれぞれ248 / 251。checks/word_count.pyで再現可能。引用は元の著者名・年を維持した。n≥2の範囲は指数漸近と本文の定理に従う。

## E2 序論

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
| --- | --- | --- | --- | --- |
| 154–155 | primal dataを測る量（F06） | UNCLEAR | l.945–953, 983–985, 1018–1026では rho, \|N\|, kappa のみ。ellも含むように読めるためC03はpartly。 | the quantities used in our presentation bounds (the exemplar parameters also enter the primal data bounds of Section~\ref{sec:applications}), and |
| 207–208 | The gap in Theorem A does not count productions | OK | A(i)が規則数も報告する一方、Aの積尺度の分離は規則数を含まない。gapを主語にした修正でC04閉鎖。 | — |
| 232–234 | membership query ... can supply negative evidence | OK | yes/noのうち否定応答が負の証拠となる。can supply は正しく限定する。C05閉鎖。 | — |
| 296–297 | mark observer yields a gap; observer needed for frames of polynomial total length | OK | 定理C(iii),(iv)。型なしでのフレーム最小総長は指数下界、フレームとexemplarの型なし最小値の比は未解決 l.1549–1557。今回の修正はそれを断定しない。 | — |
| 354–355 | estimate prevalence in random grammars / none of these | OK | ClarkのランダムCFGの近似的検査という限定に合う。none of theseは引用された研究に量化範囲を限定する。C07閉鎖。 | — |

C06の修正は特に重要で、今回の文は正しい。観測器なしで両者が指数的であることから「比が指数的でない」とは導けない。length parityの一文はL_nのexemplar側についてであり、M_nのframe側にも有効だとは述べていない（l.902–920,1475–1479）。C07のClarkについてPMLR公式サイトは出版年2017、会議は2016、著者稿の年表示は2016であるため、C13と同じ出版年基準に統一するならl.1780–1783の年を2017にする選択肢がある。これは今回の変更で導入された誤りではなく、既存の書誌表記に関する任意確認事項である。

## E3 §5

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
| --- | --- | --- | --- | --- |
| 1066–1071 | Algorithm 3 / Q^{r,s} / stable atom（F07） | UNCLEAR | 原典著者稿pp.12–14。QはJに現れる商の代表を最終的に選ぶ。収束G_iの非終端が将来も同じことを介し、未飽和E_i上の反証へ戻れる。論理は成立するが添字とJの範囲を明記したい。 | The argument carries over to Algorithm~3 of \citet{kanazawa2023wollic} ($\cap$ available, rank $r\ge2$, terminal-block bound $s\ge1$). After stabilisation at stage $i$, $J$ is fixed; once $E$ exhausts $\Sub(M_n)$, $Q^{r,s}(J,E)$ represents every quotient of a context in $J$. Thus the stable grammar $G_i$ contains an atom $e$ denoting $L(G_n,E_{n-1})$, and the absent rule $(\eps,\eps)^\lhd\to\Lfl e\,e\Rfl$ must fail the test on $E_i$, requiring $w^*_{n-1}\in E_i$. |
| 1067 | r>=2, s>=1 in its notation | OK | 原典p.11。rはRHS非終端数、sは連続終端ブロック長。候補規則はr=2,s=1で許容される。C10のsについては修正済み。 | rank $r\ge2$ and terminal-block bound $s\ge1$ in Kanazawa's notation |
| 1072–1075 | extended regular SPP / normalized atoms in a short word / k>=8 | OK | 原典pp.8,11,13–14およびl.713–777。SPPの構成、ガード、正規化と長さ、演算数8を下記で独立に確認した。 | — |
| 1073 | Gamma* の局所記法（F08） | STYLE | 原稿では終端アルファベット、Kanazawaでは演算集合。式は局所記法で正しい。 | $\{c_i\}\Lc$ and $\{c_i\}\Lc\cap\Gamma^*\Lce\Gamma^*$ (where $\Gamma$ is our terminal alphabet and $c_i$ is as in the |
| 1076–1078 | this word / additional examples in (d†′)（F09） | STYLE | C09の本質は閉鎖。先行する短い一語が先行詞であるが、単集合D={d}を明示した方が量化の取り違えを防ぐ。 | Let $d$ be such a word. With initial data $D=\{d\}$, the additional examples in (d$^{\dagger\prime}$), which bounds their number, cannot all have length polynomial in the size of the target grammar. |
| 1083–1085 | apply proof of Lemma 5.1 relative to L | OK | 非空語の文脈集合はepsilon追加で変化せず、B/U/L不変条件はLに対して成立。epsilonの新しい初期成分もLに含まれる。詳細は下記。C11閉鎖。 | — |
| 1081–1085 | rank 2 / empty language（F10） | STYLE | rankは高々2と明記すると空言語や{epsilon}を含む主張がより厳密。空言語はI=emptysetで扱える。 | Every language of $\bigcup_s\Ccf s$ has a CFG of rank at most $2$ with the very weak $1$-FKP (\citealp[Prop.~9.7]{kuriyama-tcs1} with \citealp[Sec.~6.3]{yoshinaka2015}; directly, for $L=\emptyset$ take $I=\emptyset$; otherwise apply the proof of Lemma~\ref{lem:rec-kernel} relative to $L$ to a characteristic sample of $L\setminus\{\eps\}$ (if nonempty) and, if $\eps\in L$, add an initial $A\to\eps$ with kernel $\{\eps\}$). |

### Algorithm 3の反証下界：原典との突合せ

典拠：Kanazawa, *Learning Context-Free Grammars from Positive Data and Membership Queries*, WoLLIC 2023著者稿 pp.11–15（合本pp.181–185）。p.12の定義、p.13のAlgorithm 3とTheorem 7、p.14のTheorem 8、p.15の(d†′)を参照。

1. 正確な段階記法は \(E_i=\operatorname{Sub}(T_i)\), \(J_i=J_{i-1}\) または \(\operatorname{Con}(T_i)\), \(N_i=\mathcal E_k(Q^{r,s}(J_i,E_i),\Gamma_{\rm op})\), \(P_i=P^{r,s}(N_i,E_i)\)。ここで \(\Gamma_{\rm op}\) はKanazawaの演算集合で、本稿のアルファベットΓではない。Qは \(B(E)=\Sigma^{\le s}(E\Sigma^{\le s})^{\le r}\) 上での商のトレースが等しい文脈のうち≺₂最小のものを選ぶ。
2. \(G_i\) が安定したならTheorem 7より \(L(G_i)=M_n\)。以後resetは起きずJは固定。最初の正例でresetし、以後Jは過去のreset時のCon(T)である。M_nは非空で初期Jには少なくとも一つの正例に由来する文脈がある。
3. その正例の根がunaryなら \(c=(\Lce,\Rce)\)、binaryなら印付き兄弟のある穴の文脈を選ぶ。l.1043–1046の論証より \(c^\lhd=L(G_n,E_{n-1})\)。\(c\in J\)。\((\eps,\eps)\in J\) も成立し≺₂最小である。
4. 有限M_nなのでいずれ \(E_j=\operatorname{Sub}(M_n)\)。Jの各商はSub(M_n)に含まれ、\(E_j\subseteq B(E_j)\)。したがって異なる商のトレースは区別される。Qは**Jに現れる**各商を一つずつ残す。原典p.12の定義から直ちに成立する。
5. その段階j≥iの \(N_j\) に、上記商を表すquery atom \(e\) がある。原子は0個の演算を使うguarded expressionなのでk≥1で十分。\(G_j=G_i\) より同じeは \(N_i\) にも存在する。ここが「once E exhausts」から元の収束時点へ戻るための重要な一歩である。
6. 候補 \((\eps,\eps)^\lhd\to\Lfl e e\Rfl\) はr≥2, s≥1ならPの形式条件を満たす。\(w^*_n\notin M_n\) なので全域では無効で、Theorem 7（p.12の(3)）により安定したP_iに存在しない。よって \(E_i\cap\llbracket e\rrbracket\) から二つの反例入力を選べるはずであり、その唯一の組は \((w^*_{n-1},w^*_{n-1})\)。したがって \(w^*_{n-1}\in E_i\)、すなわち時点iまでの正例の一つが長さ \(3\cdot2^{n-1}-2\) 以上である。
7. 結論：l.1066–1071の論法は成立する。Qが言語の全商を表すのではないという限定、安定非終端をE_iの反証に戻す一文を明記すれば、C08の懸念は解消される。F07は説明の強化であり、反例の発見ではない。

### Extended regular closure・短いatom-covering word・k=8

- H_nの型を忘れ、unmarked成分に \(c_i^\lhd\)、marked成分に \(c_i^\lhd\cap\Gamma^*\Lce\Gamma^*\) を与える。最初は全E_iへ過大近似し、marked側は正確。unmarked規則の結果は全E_i、marked規則は必ずunary constructorまたはmarked childを含むのでpre-fixed。初期marked成分はM_n。rootのatom \(c_n=(\eps,\eps)\) だけでもM_nを表せる。従ってSPPである。
- 原典p.8では定数∅・各文字も0項演算として数えられる。 \(\Gamma^*=\overline{\emptyset}\) と書くと左右のコピーで2+2、印文字定数1、連接2、交差1、計8演算。左辺のquery atomをガードとする。文字の和集合から二つのstarを直接作る数え方なら8を超えうるが、上記の補集合表現でk=8が確実。rank≤2、終端ブロック長1。Theorem 8の条件を満たす。
- 正規化の短語の主張も成立。原典pp.12–13の≺₂は文脈の左成分をshortlexで先に比較し、次に右成分。i<nについて、\(E_i\) 全体を商とする文脈は少なくともn−i個の祖先の開始括弧を左側に含む（node lemma）。最短左成分では全て左端路をたどる。もしunary開き括弧がbinary開き括弧より小さければ、正規形は全unaryの \(c_i\)、共通語は \(u_n\)（長さ2n+1）。逆順なら正規形は全binary左端路を選び、右兄弟を各高さjの最短語 \(u_j\) とする。右側もshortlex最小で、根の右兄弟 \(u_{n-1}\) が印付き（n≥2）なのでどのiの商も全E_i。共通語の長さは \(1+2n+\sum_{j=0}^{n-1}(2j+1)=(n+1)^2\)。c_nは空文脈で常に共通語に現れる。よって正規化後も単一の短語が全必要atomを覆う。順序を任意の全順序に変更した版ではこの長さ保証を無条件に移さない。
- (d†′) の量化：p.15では最初のDは多項式**個数**のみ保証される存在量化。長い語を含んでよい。今回のl.1076–1078は、上記短語dを選んだ特定の初期D={d}に限定しているので、存在的な性質そのものへの否定にはなっていない。初期データをちょうど{d}とし、途中に他の長語を挿入せずD′、t、D″を順に提示する場合を考えれば、収束時点までの全正例のどれかが指数長でなければならない。|d|≤(n+1)^2なので、その長語は追加正例の側にある。固定r,s,k≥8、ターゲット文法とSPPの表示サイズは多項式(n)。従って追加正例全てに一律の多項式長上界は置けない。this wordの先行詞は自然だがD={d}の明記を推奨。

### Remark 5.6：εを含む場合の直接論証

\(L\in\mathcal C_s\)、\(L'=L\setminus\{\eps\}\) とする。任意の非空語xについてuxvは非空なので \(\mathcal D_L(x)=\mathcal D_{L'}(x)\)。従ってL'もs-substitutableかつCFL。L'≠∅なら、そのRec_sの特徴サンプルKを選んでG_Kを作る。各非空factor xの成分をLに相対的な \(\{x\}^{\rhd\lhd}_L\) とする。BはClark inclusionが任意のLで成立、UはLのs-substitutabilityとK⊆Lから成立、L規則はextensivityから成立。各初期w∈Kは(ε,ε)を文脈に持つので成分⊆L。ε∈Lなら独立な初期記号A→εを加え、成分を \(\{\eps\}^{\rhd\lhd}_L\) とする。これはεを含み、同じ空文脈によってLに含まれる。他の規則からAを参照しないのでpre-fixed性は保存され、初期成分の和がLを覆いかつL以下となる。L'が空ならεだけの文法、L=∅ならI=∅の文法（正例提示は存在せず学習主張は自明）でよい。rankは高々2。したがって修正後の「apply the proof ... relative to L」は正当で、C11は閉じた。KY2017のTheorem 6への適用はl.448–453の定式化と整合する。

## E4 §6

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
| --- | --- | --- | --- | --- |
| 1489 | p_i x q_i in M_n iff x is marked, for x in L(G_n,E_i) | OK | l.752–762, 696–710。固定p_i,q_iは無印であり、当該型の部分木を置換するとL_nに留まる。印がない場合は唯一の削除語になる。範囲が補われC12閉鎖。 | — |

## E5 参考文献

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
| --- | --- | --- | --- | --- |
| 1800 | Coste–Nicolas: ICGI 2018, PMLR 93, 155–168, 2019 | OK | PMLR公式論文メタデータと巻93。会議は2018-09-05〜07、刊行は2019-02-04。C13閉鎖。 | — |
| 1886 | Ogden: Mathematical Systems Theory 2(3):191–194, 1968 | OK | DBLP巻2・Ogdenの著者書誌と一致。誌名は当時の正式名。C14閉鎖。DOI 10.1007/BF01694004 の出版社ページは取得不能だった。 | — |
| 1908 | Yoshinaka: MoL 2015, 87–98, ACL, 2015 | OK | ACL Anthology W15-2308の書誌と一致。C15閉鎖。 | — |

書誌確認に用いた公開記録：
- Coste–Nicolas: https://proceedings.mlr.press/v93/coste19a.html ; https://proceedings.mlr.press/v93/
- Ogden: https://dblp.org/pid/o/WilliamFOgden.html ; https://dblp1.uni-trier.de/db/journals/mst/mst2.html （DOI出版社ページの取得失敗を補う書誌照合）。
- Yoshinaka: https://aclanthology.org/W15-2308/
- Clark: https://proceedings.mlr.press/v57/clark16.html ; https://proceedings.mlr.press/v57/
- JoLLI: https://link.springer.com/journal/10849/submission-guidelines （利用可能なDOIを完全なリンクとして示す方針もある。全参考文献のDOI整備は今回の限定差分の外。）

## 前回指摘の閉鎖状況

| ID | 閉じたか（closed／partly／not） | 理由 |
| --- | --- | --- |
| C01 | partly | at least とtightの導入で改善。最大長とmax(kappa,1)、下界の達成可能性を明示（F03）。 |
| C02 | closed | suitable one-word deletions と frame upper / exemplar lower を明示。 |
| C03 | partly | primalに限定したがellを含むように読める（F06）。 |
| C04 | closed | 定理全体ではなくgapを主語に変更。 |
| C05 | closed | can supply negative evidenceで肯定応答を含めない。 |
| C06 | closed | 必要性を多項式総長のフレーム表示に限定。未解決の型なし比は主張しない。 |
| C07 | closed | estimate、none of theseの限定が適切。 |
| C08 | closed | verbatimを削除し、J固定とQ代表の条件を加えた。論法自体は成立。F07は追加の明示性の改善。 |
| C09 | closed | 短いatom-covering初期集合に限定。F09は明示的な単集合への書き換え。 |
| C10 | partly | sはin its notationで区別。Gammaが原稿の終端アルファベットであることを補うと完了（F08、軽微）。 |
| C11 | closed | Lemma自体の適用でなくLに相対化した証明を反復することで成立。 |
| C12 | closed | xの所属範囲を追加。 |
| C13 | closed | ICGI 2018 / publication 2019。 |
| C14 | closed | 当時の正式誌名を復元。 |
| C15 | closed | ACLを復元。 |
| C16 | partly | 指定3箇所は改善。全書誌の統一方針は変更範囲外であり、網羅的には検査していない。 |

C08/C09/C11は数理的な内容として閉じた。C10のGammaの明示とC03のellの切り分けは残る。C16は依頼のC01–C15外だが、参考として併記した。

## Abstract・序論・結論の横断確認

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
| --- | --- | --- | --- | --- |
| 149–157, 81–92, 1567–1577 | 二つの尺度と学習への帰結（F03,F04,F06,F11） | UNCLEAR | 本文は積尺度と全長を明確に区別。結論はdualの独立証明も明示するが、AbstractのHenceだけが因果を圧縮している。結論のκも定義のmaxにそろえるとよい。 | while every exemplar presentation has an exponential lower bound on $\rho\|N\|\max(\kappa,1)$, which yields data bounds for $\mathsf{Rec}_s$ and the primal learner; a separate argument bounds the dual learners. In total length, frames become short under the mark observer but are exponentially bounded below without an observer or if $\Lce\ta\Rce$ and $\Lfl\ta\ta\Rfl$ get one type; exemplars have exponential lower bounds, typed or untyped. |
| 159–179, 79–81, 1579–1593 | 言語学的主張の強さ | OK | 抽象モデルであって自然言語や学習者一般の経験的主張ではないことが一致。culminativity（exactly one mark）は扱わない。 | — |
| 259–272, 93–95, 1575–1577, 1560–1563 | refinement | OK | 結論は対象の強・弱・very weakを明示し、強FKPを断定していない。Abstractにも性質名を具体化すると整合が高まる。 | — |
| 296–297, 90–93, 1549–1557 | 観測器の必要性と一般化 | OK | 型なしの最小総長同士の比は未解決のまま。観測器の必要性は多項式総長のframeに限る。suitable deletionは観測器なしframe下界の一般化を意味しない。 | — |

## 総合判定

**局所的な修正で投稿してよい（修正の一覧）**

投稿前に優先して修正：F01–F07（Abstractを上記全文で置換、序論l.154–155を切り分け、§5 l.1066–1071のJ・E_iの範囲を明示）。F08–F11は小さな記法・量化・結論の整合改善。F12は語数の安全余裕であり、差し替え案で解消する。主要数値、A/B/Cの主張、一般化の条件、Algorithm 3の反証の核心、εの修正、参考文献3件に新たなFALSEは認めなかった。新しい長い証明や定理の差し替えは不要。

この判定は指定TeXの差分に限る。対象PDFの再生成・紙面照合、全参考文献のDOI/版・全原稿の独立査読は未完。投稿前には修正後TeXとPDFの対応、語数、変更された文だけの量化・仮定・参照の最終照合を行うこと。禁止されたresearch資料は開いておらず、著者側の修正説明から判定を逆算していない。
