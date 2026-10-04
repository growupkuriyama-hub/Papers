# TCS-D-26-00494 Round 1 回答書 日本語確認版

> **用途**: このファイルは response_round1.tex の内容確認用日本語版です。TCS への提出用本文は英語版です。査読者コメントは要旨化していますが、著者側の回答方針・撤回点・修正箇所は英語版と対応するように整理しています。

## 全体方針

今回の改訂では、次の8点を主要変更として明示した。

1. **学習器の正しさ**  
   初回投稿版の sequential learner は、正例が増えるたびに batch grammar を再構成していたため、文法そのものが構文的に収束する保証がなかった。改訂版では finite-sample batch constructor \(\mathcal B_h\) と conservative sequential learner \(\mathcal A_h\) を分離した。

2. **outer-context typing の撤回**  
   初回投稿版の outer-context type はどの証明でも使われていなかったため削除した。完全性証明に本当に必要なのは yield type \(A_\mu\) だけである。

3. **terminal-rule completeness の修正**  
   一つの typed nonterminal が複数の terminal rule を持つ場合、canonical yield だけでは不十分だった。各 \(X\to a\) に対して \(u_Xav_X\) を witness に加え、必要に応じて Rule (R3) の後に Rule (R4) を使うよう修正した。

4. **空語の扱いの明確化**  
   fixed-\(h\) substitutability は内部断片 \(x,y\in\Sigma^+\) に対して定義し、\(\lambda\) は start symbol 側で別扱いにした。

5. **一般 fixed-\(h\) の quantitative boundary**  
   新しい §7 で typed thickness を導入した。一般の fixed-\(h\) では canonical witness の大きさを source grammar の ordinary thickness だけで抑えられるとは限らず、固定2元モノイドでも full yield typing により指数的ギャップが生じうることを Prop. 7.3 で示した。

6. **fixed-window との正確な対応**  
   Prop. 3.2 で \(h_{k,\ell}\) による fixed-monoid typing と Yoshinaka の \((k,\ell)\)-substitutability が正確に一致することを示した。§8 では Yoshinaka と同じ polynomial degree や normal form を主張せず、同じ2つのパラメータ（文法サイズと ordinary thickness）に関して polynomial な characteristic-data bound を得る、と限定した。

7. **linear theorem の非正規な射程と fixed-window との位置関係**  
   §9 に非正規 linear language \(L_{\pm,e}\) を追加し、fixed-\(h\) substitutable でありながら ordinary substitutable でも fixed-window substitutable でもない例を与えた。さらに §10.1 で、Clark–Eyraud の center-marker 例を踏まえた endpoint-complete variant \(P=\{a^ncb^n:n\ge0\}\) の代入可能性を直接証明し、fresh separator \(d\) から \(L_\times=PdP\) を構成して nonlinear な \((0,0)\)-substitutable CFL を与えた。これと \(L_{\pm,e}\) を合わせ、\(\Gamma=\{a,b,c,d,e\}\) 上で context-free fixed-window hierarchy と linear CFLs が比較不能であることを明示した。

8. **polynomial claim の切り分け**  
   polynomial-time finite-sample reconstruction と characteristic-data bounds は維持するが、修正後の sequential learner 自体を de la Higuera 型の “polynomial time-and-data learner” とは呼ばない。Gold identification と batch complexity を明確に分ける。

### 初回投稿版から撤回・限定した3つの主張

- sequential learner の **order-independence**
- outer-context type による分離が **必要** だという主張
- linear sequential learner に対する **“polynomial time-and-data”** というラベル

---

## Editor への回答

Editor の主懸念は、presentation の問題が科学的部分、とくに learning section の正しさにまで入り込んでいる点だった。

改訂版では、(i) learner を conservative learner に差し替え、(ii) terminal-rule gap を witness set と completeness proof の双方で修正し、(iii) 使われていない outer-context annotations を削除し、(iv) fixed-\(h\) substitutability を nonempty fragment に限定した。§4 で batch operator と sequential learner を先に定義し、§5 で completeness 用の yield typing を導入する構成にした。さらに §7 で一般 fixed-\(h\) における typed-thickness limitation を明示し、§8・§9 では special subclasses に対する stronger quantitative bounds を分離した。

**改訂箇所:** Def. 2.1, §4.2, §5.1, Thm. 5.3, Cor. 5.5, §§7–9.

---

# Reviewer 1

## R1-01 学習アルゴリズムの致命的誤り

**指摘要旨:** 初回投稿版の learning algorithm は収束しない。先行研究に倣えば修正可能。

**回答:** 指摘どおりであり、初回版の learner には genuine correctness problem があった。改訂版では set-driven batch operator \(\mathcal B_h(K)\) と conservative sequential learner \(\mathcal A_h\) を分離した。新しい正例が現 hypothesis に含まれる限り hypothesis を保持し、拒否されたときだけ accumulated sample 全体から再構成する。この conservative device は Clark–Eyraud の SGL (Algorithm 2) と Yoshinaka の \((k,\ell)\)-SGL (Algorithm 1) と同型である。finite witness set が現れた後は高々1回の hypothesis change で target language に一致し、その後は文法そのものが構文的に安定する。

order-independence の主張は撤回し、set-driven なのは batch operator のみとした。

**改訂箇所:** §2.1, §4.2, Cor. 5.5, Thm. 8.3, Thm. 9.3.

## R1-02 全体の presentation

**指摘要旨:** technical terms の未定義、長すぎる証明、metavariable の不統一、節の細分化を整理し、大幅に短くすべき。

**回答:** manuscript を大幅に圧縮・再編した。definitions と learning model は §2 に集約し、proof-local terminology は必要箇所だけで導入した。長い技術証明は Appendices A–C に移し、旧 boundary sections は §10 に統合した。固定的なページ数は回答書には書かず、最終ビルド依存の情報を避けた。

**改訂箇所:** §§1–2, §§4–5, §§7–10, Apps. A–C.

## R1-03 Introduction の位置づけ

**指摘要旨:** 分野における位置づけと対象クラスの意義を明確にし、technical details を減らすべき。

**回答:** Introduction の contribution を3本柱に整理した。(1) exact finite-witness reconstruction と conservative Gold learner、(2) fixed-window / linear quantitative results、(3) fixed-window hierarchy・deterministic CFL・Clark congruential family との構造的関係である。

## R1-04 \(D_L\), \(\mathcal C_h^{cf}\) の定義

**回答:** Introduction と §2 で明示的に定義した。“general context-free class” の曖昧な表現も削除した。

## R1-05 contribution の過剰列挙

**回答:** proof-local devices を contribution として数えず、実質的な3点に整理した。

## R1-06 Łukasiewicz language の名称と引用

**回答:** §10.3 で \(S\to aSS\mid b\) の言語を Łukasiewicz language と呼び、Autebert–Berstel–Boasson (1997) を引用した。現在の coding では \(L_{\mathrm{Luk}}=D_1b\) と記す。

## R1-07 order-independence と constructor / learner の混同

**回答:** batch constructor と sequential learner を分離した。§4.2 では、batch operator のみが set-driven であることを明示し、無限標的での提示順序依存性を独立した `\paragraph` を設けず、学習器の説明中に短く示した。長い語を先頭に加えると、同じ標的言語に収束しても極限文法の非終端記号集合が異なりうる。主張するのは標的言語を生成する文法への eventual syntactic stabilization である。

## R1-08 基本用語の定義

**回答:** CFG, derivation, reachable, productive, reduced, linear, binarization, encoding size, thickness などを §2 にまとめた。v90 点検で出現回数記号 $|w|_a$ も定義し、SGL と RNF を初出で展開、受理集合 $\mathsf{Acc}\subseteq M$ を明記した。未使用の $[x]_{\equiv_L}$ も削除した。

## R1-09 “finite typed reconstruction basis”

**回答:** 用語・概念とも削除し、実際に必要な finite witness set だけを残した。

## R1-10 \(\mathsf{RS}_h\) と \(\mathsf{RS}\) の順序、RS の非学習可能性

**回答:** fixed \(h\) の slice を先に定義し、その後 expressive union \(\mathsf{RS}\) を定義した。RS 全体は全 regular languages を含み superfinite なので positive data から Gold-identifiable ではないことを明記した。

## R1-11 \(\lambda\) の扱い

**回答:** compared fragments を \(\Sigma^+\) に限定し、\(\lambda\) を start symbol で別扱いにした。Clark–Eyraud の \(a^+\) の扱いと整合することを脚注で説明した。

## R1-12 fixed-window morphism の定義

**回答:** 短い語の場合も含め prefix/suffix の意味を明示し、Prop. 3.2 の証明で finite monoid の multiplication を与え、Yoshinaka の fixed-window condition との同値性を両方向で証明した。

## R1-13 “\(h\) is given as data” と linear CFG

**回答:** \(h\) は finite monoid の multiplication table と letter images で表現される fixed efficiently computable homomorphism とした。linear CFG も §2 で定義した。

## R1-14 “The proof for fixed \(h\)”

**回答:** 曖昧な表現を削除した。

## R1-15 reachable / productive

**回答:** §2 で先に定義し、口語的説明を削除した。

## R1-16 typing を導入する順序

**回答:** reviewer の提案に従い、§4 で learner を先に定義し、§5 で completeness proof のために target-side yield typing を導入する順序に変更した。

## R1-17〜R1-19 §4 の細部・重複 lemma・記号

**回答:** \(\omega\) は trimmed typed refinement の直後に定義して前方参照を解消し、\(\chi\) は witness set の直前に置いた。parity 例は脚注から本文へ移し、型なし source symbol に \(\omega\) を適用しない書き方に修正した。\(\alpha\) の型、NT(), Rule(), realized/exhibited などの不要・重複表現も削除または整理し、lifting は Prop. 5.2 に集約した。

## R1-20 learner が収束しない

**回答:** R1-01 と同じ問題であり、proof だけでなく learner 自体を conservative learner に差し替えた。

## R1-21 “soundness of a rule”

**回答:** Rules (R1)–(R5) の直後に \([x:u,v]\) の直観的意味を1文で説明し、その直後に数学的な soundness invariant と Thm. 4.2 を置いた。

## R1-22 不要 lemma と \(G\to\widetilde G\)

**回答:** trivial / definition-restating lemmas を削除し、typed refinement の language preservation と yield invariant を Prop. 5.2 に整理した。

## R1-23 theorem statement を数学的に

**回答:** Thm. 5.4 を
\[
\mathsf W(\widetilde G)\subseteq K\subseteq L
\Longrightarrow
L(\mathcal B_h(K))=L
\]
という明示的な implication にした。

## R1-24 Corollary の convergence proof

**回答:** 証明だけを修繕するのではなく learner 自体を変更した。Cor. 5.5 が hypothesis grammar の eventual syntactic stabilization を証明する。

## R1-25 §6 complexity

**回答:** 定義的な議論を削り、finite sample size に対する reconstruction complexity の数え上げを残した。多項式時間更新についての自明な独立した系は削除し、直後の短い本文説明に統合した。

## R1-26 linear section が長い

**回答:** 現在の §9 では Prop. 9.1 と Lemma 9.2 の statement と Thm. 9.3 の quantitative consequence を本体に残し、normalization と short-witness proof は Apps. B, C に移した。

## R1-27 capped counter の記号

**回答:** \(\{d,u,;\}\) を \(\{\uparrow,\downarrow,\#\}\) に変更し、CCL\(_p\) を CTR\(_\rho\) に改名した。§10.2 の fixed-window exclusion は2語だけを使う短い witness にした。また capped counter の正則性を述べる自明な命題は、DFA の説明とともに本文へ統合した。

## R1-28 boundary sections の統合

**回答:** 旧 §§8–10 を現 §10 に統合し、不要な corollary と “block” terminology を削除した。\(\Delta^*\) は nonlinear witness として1 proposition に圧縮した。さらに class positioning を明確にするため、§10.1 に新しい subsection・lemma・proposition を作らず、短い unnumbered comparison を置いた。center-marker 部分は再査読向けに大幅に圧縮した。Clark–Eyraud の center-marker 例を踏まえた endpoint-complete variant \(P=\{a^ncb^n:n\ge0\}\) の代入可能性を本文で直接証明し、fresh separator から nonlinear な context-free fixed-window language を得て、Prop. 9.4 の反対向きの分離と合わせ、context-free fixed-window hierarchy と linear CFLs が比較不能であることを示した。

## R1-29 標準事実を再証明しすぎ

**回答:** Dyck / Łukasiewicz の標準事実は Ginsburg–Greibach と Autebert–Berstel–Boasson を引用する形にし、旧 standalone lemma を削除した。

## R1-30 quotient lemma の配置

**回答:** 一般的な closure section を復活させず、実際に使う fixed-word right quotient の形だけを Lemma 10.6 として残し、その唯一の適用直前に置いた。

## R1-31 Clark congruential family

**回答:** Prop. 10.7 を追加した。Clark (2010) が ordinary substitutable と fixed-window substitutable classes を congruential family に含め、Dyck language を既知例として用いていることを本文で明示した。その上で、本稿では各 fixed-\(h\) slice に対して
\[
\mathcal C_h^{cf}\subseteq\mathsf{CONG}
\]
を証明し、union を取って
\[
\mathsf{RS}\cap\mathrm{CFL}\subseteq\mathsf{CONG}
\]
を得る。

## R1-32〜R1-37 その他の presentation / boundary 指摘

**回答:** proof-local lemmas の削除、標準事実の citation 化、right quotient lemma の局所配置、Clark family との比較追加まで含め、現 §§9–10 と Appendices に整理済み。

---

# Reviewer 2

## R2-01 fixed \(h\) の意義・typing / PDA / Takada との関係

**回答:** 一つの \(h\) を class 全体で固定することを明記し、Yoshinaka の fixed \((k,\ell)\) と同じ class-level bias として位置づけた。Coste et al. (2004) の typing/domain bias と関連づけ、Takada の control-set approach とは「regular control set が derivation representation に参加する」のに対し、本稿の finite monoid は比較可能な terminal yields を制御するものだと区別した。

また「未知の \(h\) をどうするか」については、既知の像サイズ上界 \(m\) がある場合とない場合を分けた。固定 alphabet \(\Sigma\) と \(|\operatorname{im}h|\le m\) が分かっていれば、サイズ \(m\) 以下の有限モノイド構造と文字写像は有限個しかないので、それらを総当たりして product を取ることで、すべてを refine する一つの universal observer にコンパイルできる。ただし \(m\) に関する多項式計算量は主張しない。上界を外すと、全有限 observer の union は全正則言語を含むため、Gold の superfinite obstruction により正例から同定不能である。したがって「bounded unknown observation」と「unrestricted observer selection」は質的に別問題である。

さらに新 §7 で、arbitrary fixed-\(h\) の quantitative limit を typed thickness により明示した。fixed-window は §8、linear は §9、pushdown / boundary は §10 に整理した。加えて §10 末尾で、有限群値の型付けだけを許した union を \(\mathsf{GRS}\) とおくと
\[
\mathsf{GRS}(\{a\})\subsetneq\mathsf{RS}(\{a\})
\]
となることを、一文字正則言語 \(L_{\ge2}=\{a^m:m\ge2\}\) で示した。したがって finite monoid を finite group に制限すること自体が表現力の真の損失であり、monoid を使うことは単なる抽象化上の飾りではない。この小分離は新しい主定理として押し出すのではなく、Reviewer 2 の「fixed-window の抽象的一般化以上に何が得られるのか」という広い懸念に対する具体的な応答の一つとして追加したもの、と英語版 Overview と R2-01 の双方で明示した。Overview にも置くことで、Reviewer 1 から見ても追加理由が分かる構成にした。

## R2-02 outer context type が transport に使われていない

**回答:** reviewer の指摘どおりであり、初回投稿版で outer-context typing が必要だとした主張は unsupported だったため撤回した。outer annotations は削除し、yield type \(A_\mu\) だけを残した。R2 は同じ observed factor \(x\) が実際に観測された contexts 間を移す規則であり、周囲の \(h\)-type は不要である。残した yield-type index の必要性が直観的に分かるよう、§5.1 に長さの偶奇を用いた短い例を本文として追加した。例は source grammar の shortest yields の型不一致として記述し、型なしの \(A,B,C\) に \(\omega\) を適用しない形にした。

## R2-03 linear theorem の射程

**回答:** §9 に \(L_{\pm,e}\) を追加し、Prop. 9.4 で linear・nonregular・fixed-\(h\) substitutable かつ ordinary / fixed-window substitutable ではないことを示した。Thm. 9.3 には genuine nonregular linear content がある。さらに §10.1 の短い unnumbered comparison で反対向きの分離も与え、endpoint-complete center-marker language \(P=\{a^ncb^n:n\ge0\}\) の代入可能性を直接証明した上で、\(L_\times=PdP\) が nonlinear な \((0,0)\) fixed-window CFL であることを示した。したがって \(\Gamma=\{a,b,c,d,e\}\) 上で context-free fixed-window hierarchy と linear CFLs は単純な包含関係ではなく比較不能である。

また §7 で general fixed-\(h\) の typed-thickness boundary、§8 で fixed-window quantitative compatibility、§10.1 で nonlinear witness \(\Delta^*\) を分けて提示する。

## R2-04 冗長な reachable / productive qualification

**回答:** trimmed refinement の convention を一度だけ述べ、以後の反復を削除した。

## R2-05 Prop. 3.1 の “In particular”

**回答:** finite-monoid characterization から直接 “Thus every regular language belongs to RS.” と結論する形に変更した。Introduction の同じ箇所も “Thus” に統一した。

## R2-06 未使用の \(B(\widetilde G)\), NT(), Rule()

**回答:** 削除した。

## R2-07 Example 4.3 が SSBNF でない

**回答:** 例自体を削除した。

## R2-08 terminal rules が複数ある場合

**回答:** genuine gap と認め、各 typed terminal rule \(X\to a\) に対して \(u_Xav_X\) を witness set に追加した。terminal base case は必要なら R3 で canonical yield から \(a\) に代表を変え、その後 R4 を適用する。

## R2-09 Lemmas 5.3, 5.4

**回答:** 不要なので削除した。

## R2-10 Corollary の fixed \(h\) の明示

**回答:** Cor. 5.5 を “For a fixed homomorphism \(h:\Sigma^*\to M\) into a finite monoid \(M\), ...” で開始する形にした。

## R2-11 SSLNF normalization が長い

**回答:** 本文 §9 には Prop. 9.1, Lemma 9.2, Thm. 9.3 の必要な statement だけを残し、詳細な normalization と short-witness proof を Apps. B, C に移した。

---

# 今回の round-2 precheck で追加した修正

- §4.2 に Clark–Eyraud SGL Algorithm 2 と Yoshinaka \((k,\ell)\)-SGL Algorithm 1 と同型の conservative wrapper であることを明記。
- §4.2 の学習器の説明中に、独立した見出しを設けず stabilized grammar の提示順序依存性を短く記述。査読者の \(a^ncb^n\) 例は order-dependence の証明としては使わず、batch grammar を毎回再計算すると構文的に安定しないことの例として位置づける、と回答書でも明確化。
- 新 §7 typed thickness / Prop. 7.3 を response letter の Overview と Reviewer 2 回答に追加。
- fixed-window を §8、linear を §9、boundary を §10 とする現行 numbering に response letter を同期。
- 本 preflight では本文をさらに編集したため、response letter の page / numbered-line locator は一旦「final frozen PDF から再生成」に戻した。structural locator は維持し、提出直前の freeze 後に全 locator を再付与する。
- Lemma 8.2 の fixed-window bounds を proof で実際に得ている \((N_t-1)B\) と \((N_t+1)B\) に統一。
- linear = one-turn PDA の箇所に Autebert–Berstel–Boasson (1997) を追加引用。
- Clark (2010) が既に ordinary / fixed-window substitutable classes と Dyck example を congruential family の文脈で述べていることを §10 で明示。
- Yoshinaka 2008, Takada 1995, Coste et al. 2004 の series 表記を LNAI に修正。
- thickness の帰属は Yoshinaka (2008) 経由で述べ、Wakatsuki–Tomita (1993) を直接確認済みの根拠としては扱わない形に修正。
- 制限付き範疇文法の正例学習可能性は Kanazawa (1998) のモノグラフではなく、該当結果を直接支える Kanazawa (1996) の査読論文を本文で引用。
- 正則言語の有限モノイド特徴づけは Eilenberg (1974) への直接依存を外し、実際に確認した Pin (2025) の現代的記述へ差し替え。
- Reviewer 2 の outer-context typing への回答は、弁明から始めず「指摘どおり unsupported だったので撤回した」と最初に述べる形へ変更。
- 回答書冒頭の過剰な謝辞と “23 pages” というビルド依存の記述を削除。
- Introduction / Conclusion の fixed-window hierarchy の strict inclusion は、一般の alphabet \(\Gamma\) に対する主張に読めないよう、regular は \(\{\uparrow,\downarrow,\#\}\)、nonregular linear は \(\{a,b,c,d,e\}\)、nonlinear は \(\{a,b\}\) と明示。
- Abstract を1段落に圧縮し、SSBNF・canonical yields など proof-internal な用語密度を下げた。
- §8 の “same scale as Yoshinaka” は削除し、「文法サイズと ordinary thickness という同じ2パラメータに関して polynomial」と限定。normal form と polynomial degree は同一と主張しない。
- Lemma 8.2 は “has a terminal reaching context” ではなく canonical context \(\chi(X)=(u_X,v_X)\) の bound として記述。
- §4.1 で observed nonterminal を明示的に定義。
- §10.1 の reviewer が問題視した block は segment に変更。
- §10.1 の center-marker witness は endpoint-complete variant \(P=\{a^ncb^n:n\ge0\}\) に統一し、\(P\) の代入可能性を本文内で自己完結に証明した。これにより準同型像は直接 \(\Delta\Delta\) となり、非線形性の議論も簡潔化した。
- Clark–Eyraud Def. 5 が all strings で書かれている一方、同論文 §6.1 の \(a^+\) と Clark 2013 が nonempty-fragment reading を支持することを本文で明示。
- §10 末尾に finite-group typing と finite-monoid typing の分離を追加。\(\mathsf{GRS}(\{a\})\subsetneq\mathsf{RS}(\{a\})\) を、\(L_{\ge2}=\{a^m:m\ge2\}\) で示し、Conclusion にも「有限モノイドを使うことが本質的」と一文で回収。
- Response letter の Overview と R2-01 に、この分離は独立の headline claim ではなく、Reviewer 2 の「単なる Yoshinaka の抽象化以上の意義があるのか」という問題意識への具体的な応答の一つとして追加した、と控えめに明記。Overview にも入れ、Reviewer 1 にも追加理由が伝わるようにした。
- Data availability / 回答書の Lean 記述は full formalization と誤解されないよう “parts of the development” に弱めた。

---

## 現時点での提出前チェック項目

英語版 response_round1.tex が提出用の正本であり、この日本語版は内容確認用である。最終提出前には、本文を凍結した後で PDF をビルドし、必要であれば response letter の revision locations に最終ページ・行番号を一括で付け直す。Lean/Zenodo については、現行の theorem numbering と主張の範囲が archive と矛盾していないかだけ最終確認する。
