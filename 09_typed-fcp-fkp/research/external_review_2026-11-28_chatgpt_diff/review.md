# 論文09：2026-11-28 差分の独立査読

対象：*Frames versus Exemplars: An Exponential Gap for Syntactic Categories*  
基準コミット `61f8a16b0658abc6fa826ea7cddc4f123e72c64b` → `5cdba4f16c1ae8ea0d29f413908d8b62cd99ed52`。  
対象ファイル `09_typed-fcp-fkp/main.tex` のみ。最終 Git blob `f0f6c03b2cdb9de5ad8dafdefbb3f9dbf94cbbda`、基準 blob `da9cc94010c5598ba7e12a1b18b146cc41a4208a`。物理行番号はすべて最終版。

## 総合判定

**局所的な修正で投稿してよい（下記の修正を条件とする）。**

最重要は D3 の (d†′) の量化と D2 の observer necessity の言い過ぎ。D4 の構成・Boolean extension は正しいが、l.1487 の x の定義域を補う。A(i) が production count を追加したのに l.206 がそれを否定している。D3 の長い正例の下界は Q^{r,s} の重複除去を考慮しても成立する。主定理の再証明・大規模改稿は今回の差分からは必要と判断しない。

方法：GitHubから両版の main.tex を読み、行単位の LCS 差分を照合。research/ と japanese/ は開いていない。Kanazawa 著者稿はプロジェクト合本02 v8 pp.171–186（原著者稿 pp.1–16）および会議公開稿を使用。言語学資料は合本11の該当原典ページを確認した。原稿 main.pdf の版・23頁・組版は独立検証できていないため、TeXソースの査読であり、修正後のページ数も保証しない。Kishimoto は公開抄録・本文抜粋、Bybee は公開抄録・関連書誌に基づく。原典全ページの再査読、引用文献すべての版面の確認、完全な先行研究網羅調査は行っていない。web PDFスクリーンショット取得はキャッシュミスだったため、Kanazawa は合本の抽出テキストと会議サイト本文で照合した。

表の判定は指定の分類に従う。修正案は差替え英文（TeX記法を含む）；「—」は必須修正なし。OKは当該差分の主張への判定であって、依存する定理全体の独立認証ではない。

## D1

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
|---|---|---|---|---|
| 76–78 | FCP/FKP and successful learners | OK | KY2017 Thms. 3–6 (Fact 2.3(b) in substance) give the very weak conditions for the specified learners; the abstract does not say all learners. Shared frames means shared by every exemplar. | — |
| 79–83 | Uniform-depth family and F_n size | OK | §4, l.779–809: the n+1 nonterminals, maximum RHS 3n and maximum context 2n are correct. The start has 2^n−1 path productions, plus 2n−1 internal productions. | — |
| 84–85 | Exemplar product is exponential; optimality | UNCLEAR (C01) | Theorem A(ii) proves a lower bound on the product with max(κ,1), not an upper bound for every presentation. A(iii) proves the lower bound tight within O(n) for the minimum; redundant rules or symbols may enlarge arbitrary presentations. | whereas the corresponding exemplar product is at least exponential in $n$, a bound tight up to $O(n)$; |
| 85–86 | Specific learner data bounds | OK | Corollaries in §5 and Proposition 5.5 prove bounds for Rec_s with its class assumption, fixed-parameter primal, and the specified dual learners; not all learners. | — |
| 86–91 | Total-length statements | OK | Theorem C(iii),(iv) gives polynomial frames for s_U and exponential lower bounds on exemplars and on frames for nonseparating observers. Read exponential as at least exponential; this is not a matching asymptotic estimate for arbitrary presentations. | — |
| 91–92 | Both bounds extend to general one-word deletions | GAP (C02) | Theorem 6.8 requires a finite L, a suitable ideal, an untyped presentation with separated initial symbols and ideal-forcing frames, and the capture condition of Lemma 4.5. It does not give an arbitrary-deletion theorem or extend the observer-free frame lower bound in general (Open Problem 7.3). | The frame upper and exemplar lower bounds extend to suitable one-word deletions, the latter via a prefix length. |
| 92–94 | Monotonicity qualifications | OK | Theorem B: strong and very weak FCP monotone; weak and very weak FKP antitone; weak FCP nonmonotone; strong FKP remains open. The qualification is necessary. | — |
| 73–94 | 248 words and 250-word limit | OK | Exact source whitespace split yields 248 tokens (including nine inline math expressions); TeXcount yields 239 prose words and 9 inline formulae. JoLLI official guideline is 150–250 words. A small margin is advisable after edits. | — |

## D2

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
|---|---|---|---|---|
| 108–110 | Fries, Bod, Bybee | OK | Fries pp.74–75 explicitly uses three minimal test frames, followed by expanded frames, preserving structural meaning. Bod 2006 pp.291–294 uses stored experiences/tree fragments; Bybee 2006 treats instances as bases of categories. The following paragraph distinguishes linguistic exemplars from mathematical kernels. | — |
| 153–156 | Measures through which data bounds go | STYLE (C03) | The bound for Rec and primal is obtained via ρ, N, κ; the dual bound is a separate refutation and does not derive from ℓ. The expression 'bounds ... go' is colloquial and may imply all four measures are used directly. | the measures used in our presentation bounds and their learning consequences (Section~\ref{sec:applications}), and separately by its total length |
| 168–169 | Strict layer consequence | OK | Selkirk p.26 explicitly posits immediate domination by next lower category; Nespor–Vogel p.7 Principle 1 does likewise. Hence each path between fixed levels has the same length under classical SLH; not a claim about modern prosodic theory generally. | — |
| 169–171 | Japanese nominative requirement and oblique subjects | OK | Kishimoto 2010 describes a persistent nominative-case requirement with oblique-marked subjects as exceptions. The requirement is structural, not that an overt ga-marked phrase always occurs; the current wording says argument rather than overt phrase. Full publisher text not independently obtained; verified accessible abstract/excerpts. | — |
| 171–172 | Multiple nominatives | OK | Kuno (1973) p.34 §5.17 ex.(82b,c) explicitly illustrates double and triple ga subjects and directs readers to Chapter 3. Chapter reference is reasonable; adding p.34 would pinpoint the examples. | — |
| 182–183 | Same categories need w*_(n−1) | OK | For the actual categories of F_n (not arbitrary SPP overestimates), Prop.4.2(c) gives closure of {w_i*} equal to L(G_n,E_i); any kernel for that exact category is a subset of it, and if it omits w_i* the unmarked context (p_i,q_i) excludes w_i* from its closure. The start M_n is named by {u_n}. Thus at least one kernel must include w*_(n−1). | — |
| 188–190 | Theorem A(i) exact rule count | OK | Sum_{d=0}^{n−1}2^d + 1 + 2(n−1) = 2^n+2n−2; templates are distinct by depth and ordered path to the exposed unary mark. The context and RHS bounds match Prop.4.3. | — |
| 203–206 | Capture explanation | OK | Lemma 4.4 forces x∈K_B for any nonterminal yield occurrence wholly in R; Lemma 4.5 explicitly constructs RT. Read 'node' as nonterminal node as in the lemma, and 'category' as the SPP component; a frame can supply a mark outside its hole. | — |
| 206–207 | Theorem A does not count productions | FALSE (C04) | The revised A(i) explicitly counts productions, namely 2^n+2n−2. The separation measure, not the theorem as a whole, omits them; the compression now contradicts l.189 literally. | Theorem~A's separation does not use production counts; the gap in total length is Theorem~C. |
| 231–233 | Membership query as negative evidence | UNCLEAR (C05) | A query requests a judgment, but only a negative answer supplies negative evidence; yes answers are positive. Marcus 1993 distinguishes information about ungrammatical strings and unreliable feedback, not equivalence of the two mechanisms. | A membership query requests a grammaticality judgement and can supply negative evidence, long regarded as scarce in child language acquisition \citep{marcus1993}. |
| 233–237 | Fixed class vs union | OK | Fixed-s identification is cited; the union contains regular languages and hence a superfinite class. Remark 5.6 supports the MQ claim, subject to the proof clarification below. | — |
| 242–244 | Dual learner scope and length | OK | Prop.5.5 requires n≥2, r≥2, k≥1, untyped or s_U, convergence. k≥1 is the default for these learners (l.459–460); n≥2 is the scope of A. w*_(n−1) length is 3·2^(n−1)−2. | — |
| 295–297 | Observer is needed for the gap in total length | OVERCLAIM (C06) | C(iii),(iv) establish necessity of an observer for polynomial frame total length, not necessity for any exponential ratio between minimum frame and exemplar lengths. Both untyped minima are exponential but their ratio is unresolved (Open Problem 7.3, l.1552–1554). Also not every observer helps. | By (iii) and (iv), the mark observer yields a gap in total length, and an observer is needed for polynomial total frame length; its choice matters: |
| 323–325 | Initial symbols and ideal restriction | OK | Prop.6.5 l.1276–1309 assumes exactly the added no-initial-on-RHS condition and ideal-forcing contexts of noninitial categories. The context lengths and nonterminal multiplier are in the proposition. The initial introductory sentence 'hold in general' should be understood subject to these stated conditions. | — |
| 353–355 | Clark 2016 comparison | UNCLEAR (C07) | Clark 2016 pp.42–53 investigates random CFGs under specific sampling distributions and approximate tests; it does not exactly decide the prevalence of FCP/FKP. The paper is not a matched-size separation. The absolute 'none' is defensible only for the cited works, not a literature-wide negative assertion. | are qualitative \citep{yoshinaka2011dlt,yoshinaka2012lata,ky2021} or estimate their prevalence in random grammars \citep{clark2016icgi}; none of these works compares the sizes of two presentations of one language. |

## D3

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
|---|---|---|---|---|
| 1063–1064 | Typed dual long example despite short H_n | OK | Prop.5.5 establishes the lower bound for the specified candidate-generation mechanism; Prop.6.7 counts 6n−4 productions of length ≤4 and 2n contexts of length ≤2n. | — |
| 1065–1068 | Algorithm 3 refutation argument 'verbatim' | GAP (C08) | Kanazawa p.12 filters atoms through Q^{r,s}; unlike KY2017 it fixes the terminal block length and uses one initial atom. At stability J is fixed and Q retains a representative of each quotient of J, as shown below. The long-word conclusion is correct, but these extra facts are not literally the preceding argument. | The argument also applies to Algorithm~3 of \citet{kanazawa2023wollic} ($r\ge2$, $s\ge1$, $k\ge1$). At convergence, $J$ is fixed and $Q^{r,s}$ eventually separates distinct quotients since $E$ exhausts $\Sub(M_n)$. Thus an atom $e$ denotes $L(G_n,E_{n-1})$, and the candidate $(\eps,\eps)^\lhd\to\Lfl e e\Rfl$ fails only on $(w^*_{n-1},w^*_{n-1})$. |
| 1069–1071 | Extended regular SPP and guards | OK | For the noninitial type-1 labels take Q_i=L(G_n,E_i); for marked labels take Q_i∩Γ*⌈Γ*. Binary and unary rules preserve height and marking; the initial component is M_n. This is a sound, not generally strong, pre-fixed point; the formulas are guarded. In Theorem 8 use c_n alone for the start atom, as its proof fixes (ε,ε)^◁. | — |
| 1071–1072 | Normalized atoms all occur in one short word | OK | Using the actual pair order of p.12 and p.13–14, the least representative of Q_i is found along the all-unary spine or all-binary left spine, depending on opener order. The common witness has length 2n+1 or (n+1)^2; proof below. This is not the same as optional expression normal forms (footnote 8). | — |
| 1072–1073 | k≥8 and Theorem 8 | OK | With full extended regular operations, Σ* = complement ∅; the marked expression uses 8 operation occurrences (including nullary symbols), rank 2 and terminal blocks of length 1. Start atom has zero operations; k≥8 works for r≥2 and s≥1 as stated earlier. | — |
| 1073–1076 | (d†′) cannot bound additional example lengths | OVERCLAIM (C09) | The property existentially chooses D of polynomial cardinality, without bounding lengths of D (p.15). It may already contain a long word, so the lower bound does not disprove an existential length bound only on D′, t, D″. For the explicit short atom-covering initial D, no polynomial length bounds on all later examples can hold. | For this short atom-covering initial set, the additional examples in the proof of (d$^{\dagger\prime}$) cannot all have length polynomial in the target grammar size. |
| 1066,1070 | Reuse of s and Γ | STYLE (C10) | In the present paper s denotes a typing and Γ a terminal alphabet; in Kanazawa s bounds terminal blocks and Γ is the operation set. Formula Γ* is correct here, but explicitly identify which notation is local. | (with $r\ge2$ and terminal-block bound $s\ge1$ in Kanazawa's notation) |
| 1078–1083 | Remark 5.6, add epsilon | GAP (C11) | Lemma 5.1 assumes ε∉L; adding ε to the target can enlarge double closures, so merely adjoining the rule to its former SPP does not establish a new SPP relative to L. The conclusion follows by repeating the same B/U/L invariant relative to L: contexts of all nonempty kernels are unchanged, and Clark inclusion works for any L. The added singleton ε kernel gives a sound initial component. Empty language is vacuous for positive presentations and allows I=∅. | directly, apply the proof of Lemma~\ref{lem:rec-kernel} relative to $L$ to a characteristic sample of $L\setminus\{\eps\}$ (if nonempty), and, if $\eps\in L$, add an initial $A\to\eps$ with kernel $\{\eps\}$ |

## D4

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
|---|---|---|---|---|
| 1483–1486,1488 | Untyped H_n two-context SPP; ell factor necessary | OK | Set X_(i,1)=Q_i and X_(i,ζ)=Q_i∩{(p_i,q_i)}^◁=Q_i minus w_i*. For i=n the initial component is M_n. The grammar is still H_n without typing; all rules preserve the required components and initial soundness. | — |
| 1487 | p_i x q_i in M_n iff x marked | GAP (C12) | As written there is no stated domain for x. Take x to be a single opening unary bracket: it is marked but p_i x q_i is unbalanced and outside M_n. The equivalence is true for x∈L(G_n,E_i); the intersection with c_i already imposes this in the proof. | $p_ixq_i\in M_n$ iff $x$ is marked, for $x\in L(G_n,E_i)$, |
| 1489 | Maximum context length and inequality | OK | Marked labels exist for 1≤i<n, so max \|p_i\|+\|q_i\|=\|w_n*\|−\|w_1*\|=3·2^n−6; c_i length ≤2n≤this for n≥2. 4(6n−4)<2^(n−2) starts at n=10 (224<256) and follows inductively since LHS increases by 24 and RHS doubles. | — |
| 1490–1493 | Boolean extension of theorem 6.11 | OK | Any Boolean combination distinguishing x from x′ has a distinguishing atom. No atom can accept x′ and reject x: x′ contains the entire w_j*, and if c[x′]∈M_n, Lemma 4.1 replaces that node by v_j and retains membership. Thus the atom accepts x, rejects x′; the original proof follows, including the typed same-fibre condition. | — |
| 1494–1495 | Not for extended regular operations | OK | The D3 guarded expressions for H_n provide a counterexample with atom length ≤2n and O(n) RHS sum for arbitrarily large n. Thus (ell+1)·sum\|α\| is polynomial and cannot dominate 2^(n−2). This concerns context-atom lengths, not arbitrary regular-expression encoding conventions. | — |

## D5

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
|---|---|---|---|---|
| 1547–1553 | Delete subquestion on ell+1 | OK | The new H_n construction at l.1483–1489 answers that subquestion negatively. The remaining minimum-length exponent and ratio questions are genuinely not resolved by the stated bounds; the 2^(n/2) ≤ f(n) = O(n2^n) interval is justified by §4 and Theorem 6.11. | — |
| 1586–1588 | Two-mark illustration | OK | Remark 6.6 applies ideal restriction to keep ≥2 marks, so the deleted structures are precisely those with fewer than two; the frame result carries over, while the paper gives no corresponding exemplar lower bound. | — |
| 1590–1591 | Classical categorial grammars and types | OK | The qualification 'classical' limits the weak-context-free claim to basic categorial grammars, not all extensions. The reference to types is consistent with the classical category assignment; it does not say these types are finite-semigroup observations. | — |

## D6

| 行 | 主張・文 | 判定 | 根拠（一、二文） | 修正案 |
|---|---|---|---|---|
| 1777–1780 | Clark (2016), ICGI, PMLR 57:42–53 | OK | Author, title, event and pages match original PDF header (2016); PMLR collection metadata gives Jan.16, 2017 as online publication date, whereas the original PDF and paper citation year say 2016. Retain 2016 consistently; optionally note online 2017. | — |
| 1792 | Clark–Yoshinaka book chapter | OK | Title, authors, pp.143–172 and year agree with publication records. Removing editors makes entry shorter but still identifiable. For book chapters, retaining editors may be preferable under publisher house style. | — |
| 1798 | Coste–Nicolas ICGI 2019 | FALSE (C13) | PMLR 93 is the proceedings of ICGI 2018 (published February 2019); the abbreviation newly conflates publication year and event year. PMLR 93:155–168 and bibliography year 2019 are correct. | In \textit{ICGI 2018}, PMLR 93, pp.~155--168, 2019. |
| 1826–1829 | Kanazawa (2023) bibliographic entry | OK | Springer DOI 10.1007/978-3-031-39784-4_1 confirms title, author, WoLLIC 2023, LNCS 13923, pp.3–18. This review uses the author manuscript page numbers; the published page numbers have not been mapped individually. | — |
| 1834 | KY2017 LATA LNCS 10168 | OK | Author publication list confirms title, LATA 2017, volume 10168, pp.77–88; year correct. Abbreviations fit same pattern as WoLLIC. | — |
| 1840 | KY2021 ICGI PMLR 153 | OK | PMLR record confirms August 2021, pp.18–31, vol.153, title and author names. | — |
| 1846 | KY2023 ICGI PMLR 217 | OK | PMLR record confirms July 2023, pp.8–22, vol.217, title and author names. | — |
| 1869 | Leiß FG LNCS 8612 | OK | Springer proceedings confirms title, pp.121–137, LNCS 8612, 2014. LNCS abbreviation is consistent with other entries. | — |
| 1884 | Ogden Math. Systems Theory | STYLE (C14) | Volume 2(3), pages 191–194 and 1968 match bibliographic records. Only this journal is shortened while e.g. Information and Control and Journal of Logic and Computation are spelled out; title is short enough to keep full form for consistency. | \textit{Mathematical Systems Theory} 2(3):191--194, 1968. |
| 1889 | Selkirk MIT Press 1984 | OK | Title, author, imprint and year agree with the supplied edition (copyright 1984; paperback 1986). Place omission is permissible as a compact convention but other books retain places. | — |
| 1906 | Yoshinaka MoL 2015 | STYLE (C15) | ACL Anthology W15-2308 confirms the title, author, event and pages. Removing ACL leaves this conference with no publisher, unlike LNCS entries; restoring ACL costs only one token and improves bibliographic consistency. | In \textit{MoL 2015}, pp.~87--98, ACL, 2015. |
| 1792,1889,1906 | Overall abbreviation policy | STYLE (C16) | ICGI, LATA, WoLLIC, DLT and MoL short forms are sufficiently unambiguous with years/series/pages. Publisher and place omission is not uniform across chapters and books; JoLLI examples favor complete bibliographic identifiers, so adopt a consistent compact policy rather than arbitrarily omitting a single field. | Use full journal names consistently; retain publishers for proceedings and editors for edited books if required by the journal. |


## D3 補足：Algorithm 3 の独立検証

### 1. Q^{r,s} と収束時の refutation

Kanazawa 著者稿 pp.11–13: Γ_K は intersection を含む演算集合、r,s,k は正整数。E_i=Sub(T_i)、J_i はリセット時に Con(T_i) となり、それ以外は保持される。Q^{r,s}(J,E) は Σ^{≤s}(EΣ^{≤s})^{≤r} における商の制限が同一のものの最小代表を選ぶ。原子は guarded で、演算回数0として E_k に入る。初期記号は (ε,ε)^◁ 固定。

収束時 i 以後は Theorem 7 により文法が M_n を生成し、J_i はリセットされない。最後のリセット時のデータに少なくとも一語ある。その語が unary root なら c=(⌈,⌉)、binary root なら有標の兄弟を固定した左／右の hole を取れば、c∈J_i かつ quotient(c)=L(G_n,E_{n−1})。ここで後者は高さ n−1 の語を有標兄弟と任意に組み合わせられるから成立する。

有限性からある段階で E=Sub(M_n)。非空 quotient の全要素は Sub(M_n) に含まれる。Σ^{≤s}(EΣ^{≤s})^{≤r} ⊇ E なので、その段階の Q は真の商ごとの代表を保持する。N_i が以後同じ（収束の定義）であるから、該当する atom e は既に N_i にある。これは Q が単に恒久的に同一視するという誤った仮定を使わない。

r≥2, s≥1 なら (ε,ε)^◁→⌊ e e ⌋ は候補。これは両子が w*_{n−1} のときに限り不正（w*_n を作る）。P^{r,s}(N_i,E_i) がこの候補を含まないためには w*_{n−1}∈E_i が必要。従って収束時の正例のどれかが長さ ≥3·2^{n−1}−2 を持つ。Γ_K が intersection を含むのは原論文の前提であり、この下界そのものには新たな演算を必要としない。任意の追加の pruning を持つ変種には主張しない。

### 2. SPP・式の演算回数・開始記号

Q_i={c_i}^◁=L(G_n,E_i) (i<n)、Q_n=M_n。H_n の型を忘れ、type-1 label の成分を Q_i、marked label の成分を Q_i∩Σ*⌈Σ*、開始ラベルを Q_n とする。後二者は marked yields、type-1 の成分は上からの近似。なおこの SPP は type-1 側が一般に真の yield より大きいので **strong ではなく sound**（i≥1 の type-1 label の生成言語は singleton）。実際の強いSPPが必要なら type-1 に Q_i∩complement(Σ*⌈Σ*) を使えるが演算数は増える。本論文の主張と Theorem 8 は SPP だけを必要とし、k≥8 のためには前者が適切。

具体的な guarded 式 Q_i∩((complement ∅)·⌈·(complement ∅)) は intersection 1、complement 2、∅ 2、letter constant 1、concatenation 2 = 8 operations。初期は (ε,ε)^◁ 単独、RHS rank ≤2、terminal block ≤1。Thm.8 の直前（p.13）の k の定義と証明（pp.13–14）を含めて適用する。Theorem 8 の箱内だけには k の条件が再掲されていないが、直前の文脈が不可欠。

### 3. 正規化された atom が一語に共存する証明

原稿 l.1071 の normalisation は著者稿 p.13 の「商の最小代表への交換」を指す。≺_2 は u の shortlex を最優先し、その後 v の shortlex（p.12）。これは |u|+|v| の最小化と一般には違う。

Q_i を表す任意の (p,q) は w_i* を受け入れるので、p w_i* q∈M_n。Lemma 4.1 によりこの occurrence は高さ i の node。祖先 n−i 個が各1個以上の opening bracket を先行させるので |p|≥n−i。等号なら左端 path で、p は祖先の opener だけからなる。従って unary opener が先なら p=⌈^{n−i}、binary opener が先なら p=⌊^{n−i} が shortlex 最小候補。

前者では q=⌉^{n−i} が最短、全 i を u_n が証言する。後者では q が各右兄弟（高さ i,…,n−1）と対応する closing bracket からなる。最短の各兄弟は一意な u_j（長さ2j+1）。n≥2 なので u_{n−1} が marked で、w_i* を入れても M_n に属す。よってこの候補は真に Q_i を表し、これより短い q はない。全 i の最小代表は W_0=a, W_j=⌊W_{j−1}u_{j−1}⌋ の一語 W_n に現れる。|W_j|=|W_{j−1}|+2j+1 なので |W_n|=(n+1)^2。Q_n の最小代表は (ε,ε)。どの固定 alphabet order でも二つのケースで十分。従って (n+1)^2 は正しい。

### 4. (d†′) の正確な射程

p.15 の (d†′) は ∃D（多項式 cardinality、長さ上界なし）、∀初期列 covering D、∃D′、∀次の列、∃t、∀次の列、∃D″、∀次の列、という順序。D′,D″ の cardinality はそれぞれ先行データ総長の多項式で、単独 t も許す。この性質の証明では atom cover を D に取れる。

上記 D={u_n} または {W_n} を初期列に取れば総長 O(n²)。もしこの D に関して D′, t, D″ の全単語長が target representation size の多項式で一様に抑えられるなら、余計な例を挟まず順番にそれらを提示し、任意の positive presentation に延長することで長さ下界に反する。従ってこの **short initial cover に対する強化** は不可能。ただし (d†′) の ∃D を別の長いデータ集合に変更することまで排除していない。原文の帰結はこの区別を明示する必要がある。

## D4 補足：型なし H_n と Boolean combinations

Q_i の交差に限定した構成は SPP であり、type-1 label の yield は singleton でも SPP は Q_i 全体を許せる。すべての ζ-rule は unary mark を追加するか ζ-child を持つため、型なしの文法規則でも SPP が保存される。i=n の開始成分 M_n で soundness。最大 context length は i=1 の (p_1,q_1) に達する。n=10 以後の不等式はチェックコードと帰納法の双方で確認。

Boolean の場合、x は v_j の occurrence を含み、x′ はそこを w_j* に置換した語。ある原子 c が x′ を受け入れたなら c[x′]∈M_n⊆L_n。Lemma 4.1 でその w_j* occurrence は E_j node なので v_j への置換は L_n に残り、かつ有標のため c[x]∈M_n。よって x′ だけを受け入れる原子は存在しない。Boolean formula の値が異なるなら少なくとも一原子の値が違うので、必ず x を受け入れ x′ を拒否するものがある。typed の場合は同じ fibre に属するため、fibre 制約自身は区別を生じさせない。これで Lemma 6.9 と Theorem 6.11 の証明が通る。

## 数値チェック

- F_n：1+2(n−1)+(2^n−1)=2^n+2n−2。
- H_n：n+1+5(n−1)=6n−4。w*_0 の長さ1、w*_i の長さ2|w*_{i−1}|+2 より 3·2^i−2。
- ell=|w*_n|−|w*_1|=3·2^n−6。n=10 で 224<256、増分24対倍増。全 n≥10。
- 捕獲 prefix：|T°|=4+n−1=n+3、|R|=3·2^n−n−5。
- W_n の長さ (n+1)^2；w*_{n−1} の長さ 3·2^{n−1}−2。
- Abstract：whitespace split 248。TeXcount 239 prose words、9 inline math。公式サイトは150–250。提出システム独自の数え方は未確認。修正後再計数が必要。
- checks/check_numbers.py（標準ライブラリのみ）、同 .txt、および抽象の転記を同梱。

## 確認した外部資料（原典・書誌）

- Kanazawa 2023 著者稿、pp.8, 11–15: https://www.mathstat.dal.ca/wollic2023/papers/kanazawa-invited.pdf ; 出版書誌 https://doi.org/10.1007/978-3-031-39784-4_1
- Clark 2016 pp.42–53、特に冒頭の近似試験とサンプリングの限定： https://proceedings.mlr.press/v57/clark16.pdf ; https://proceedings.mlr.press/v57/clark16.html ; https://proceedings.mlr.press/v57/
- Fries 1952 pp.74–75、Bod 2006 pp.291–292、Selkirk 1984 p.26、Kuno 1973 p.34 example (82)（画像を確認）、Nespor–Vogel 1986 p.7 Principle 1（合本11 v3の該当原典）。
- Bybee 2006: https://doi.org/10.1353/lan.2006.0186 ; Kishimoto 2010: https://www.researchgate.net/publication/249933618_Subjects_and_constituent_structure_in_Japanese ; Marcus 1993: https://pubmed.ncbi.nlm.nih.gov/8432090/
- Coste–Nicolas: https://proceedings.mlr.press/v93/coste19a.html ; KY2017: https://makotokanazawa.ws.hosei.ac.jp/publications/index.html ; KY2021: https://proceedings.mlr.press/v153/kanazawa21a.html ; KY2023: https://proceedings.mlr.press/v217/kanazawa23a.html ; Leiß: https://link.springer.com/book/10.1007/978-3-662-44121-3 ; Yoshinaka 2015: https://aclanthology.org/W15-2308/
- Clark–Yoshinaka chapter: https://www.researchgate.net/publication/301914522_Distributional_Learning_of_Context-Free_and_Multiple_Context-Free_Grammars；Ogden: https://dblp.org/pid/o/WilliamFOgden.html
- JoLLI guidelines: https://link.springer.com/journal/10849/submission-guidelines

## 投稿前の修正一覧

必須：Abstract の下界と一般化の条件、l.206 の自己矛盾、l.295–296 の必要性、l.1065–1068 の Q^{r,s} の根拠、l.1073–1076 の短い初期 cover への限定、Remark 5.6 の ε 追加時の SPP の根拠、l.1487 の x の範囲、l.1798 の会議年。文体上の推奨：membership query、Clark の近似試験、記号の区別、参考文献の統一。D3 の追加証明は本文に数文を追加するか、著者が既存の短い段落を適切に置換する。修正後の語数・組版を再確認すること。
