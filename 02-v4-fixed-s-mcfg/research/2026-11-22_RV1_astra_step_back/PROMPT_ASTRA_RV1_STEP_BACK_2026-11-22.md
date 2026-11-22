# Astra 依頼 RV1：見直しラウンド — 土台の監査と well-nested 性による問題の分割 — 2026-11-22

あなたは、有限半群型付けのもとで MCFG の分布学習を研究する数学者です。研究者（論文の著者）の開問題 `op:fanout-two` には、これまで次の担当が取り組んできました。

- R1〜R3：ChatGPT（Astra）
- R4〜R11：別スレッドの Claude（すべて同じモデル系列）

R12（Claude）は計算資源の上限で止まり、報告はありません。

**今回は R12 の続きではありません。** 次の二点を、独立した立場から判定する見直しのラウンドです。

- **ここまでの筋道の土台は正しいか。**
- **この筋道を続けるのが最適か。**

前任者の結論や「VALID」の判定は、すべて検証の対象です。前提にしないでください。R4〜R11 の確認メモは同じモデル系列が書いたもので、独立した監査ではありません。

**成果物は 1 つの .zip ファイルだけ**です（§7）。チャットの本文には、zip を渡すときの 5 行以内の要約だけを書いてください。

---

## 0. 資料（実際に開いて読むこと）

公開リポジトリは https://github.com/growupkuriyama-hub/Papers （ブランチ `main`）です。以下のパスはすべて `02-v4-fixed-s-mcfg/` から見た相対パスです。取得は `git clone --depth 1` か、`https://raw.githubusercontent.com/growupkuriyama-hub/Papers/main/02-v4-fixed-s-mcfg/<パス>` を使ってください。

1. `research/README.md`：研究台帳。**最初に読む**こと。
2. `v2/reviews/PAUSE_FALSE_ROUTES_2026-11-16.md`：反証済みの推論と、数学的な不可侵条件の一覧。**次に読む**こと。
3. `main.tex`（compendium、英語）の次の箇所。
   - 第 I 部：`def:tuple-substitutable`、`def:uniform-polydata`、`op:fanout-two` とその直後の段落（l.2802 付近）、`prop:good-normalization`（l.960 付近）、`cor:distribution-representatives`（l.1406 付近）、`lem:thickness-equivalence`、`lem:power-transfer`、`thm:two-letter-content`、`thm:doubling-no-lift`
   - `def:component-pattern-thickness`、`prop:pattern-thickness-transfer`（l.5228〜5300 付近、**証明を全文**）、`lem:normalization-stages`（l.10582 付近、**本体を全文**）
   - `conj:rare-types`（l.8243 付近）と、その注記
   - 第 IV 部：`sec:p4-resume-R4`〜`sec:p4-resume-R11`、`sec:p4-open`（l.9513 付近）
4. R4：`research/2026-11-21_R4_claude_IC_fanout2/deliverable/report.md`。特に §3（補題 1〜4、定理 A）、系 B、§6 を読むこと。確認メモ `claude_check_R4_2026-11-21.md` も読む。
5. R9：`research/2026-11-22_R9_claude_virtual_algebra/deliverable/report.md`。読む箇所は §2.1〜§2.3（V0、P1〜P7、NF）、§3.1（**定理 HΞ**）、§3.4、§6。
6. R10：`research/2026-11-22_R10_claude_single_letter/deliverable/report.md`。読む箇所は §2.2〜§2.3（定理 A）、§3.1（HΞ\*）、§3.2（D2・Φ2）、系 C。
7. R11：`research/2026-11-22_R11_claude_crossings/deliverable/report.md`。読む箇所は §2.0（設定と記号）、§3.1〜§3.3（PNF・命題 5・**系 6**）、§4.1〜§4.3。確認メモも読む（§4.2 の括弧内に、肯定と否定の向きを取り違えた誤りがある）。
8. R15：`v2/reviews/astra_fanout2_round15_report_2026-11-16.md`。読む箇所は §4（補題 ST と反例言語 L_{N,d}）、§5.1〜§5.4（**明示的な文法 G^{cross}_{d,q} と G^{nest}_{d,q}**、厚さ、最小木）。あわせて `STATUS_ASTRA_FANOUT2_ROUND15_2026-11-16.md` も読む。
9. R12 の依頼文：`research/2026-11-22_R12_claude_multiletter/PROMPT_CLAUDE_R12_MULTILETTER_2026-11-22.md`。止まったラウンドが何を求めていたかを知るために読む。

**外部の文献**（課題 T2〜T4 で使う。読んだものだけを使うこと）

- Seki, Matsumura, Fujii, Kasami (1991), *On multiple context-free grammars*
- Kanazawa (2009), *The pumping lemma for well-nested multiple context-free languages*（DLT 2009）
- Kanazawa, Kobele, Michaelis, Salvati, Yoshinaka (2014), *The failure of the strong pumping lemma for multiple context-free languages*（Theory of Computing Systems）
- Gómez-Rodríguez, Kuhlmann, Satta (2010), *Efficient parsing of well-nested linear context-free rewriting systems*
- Salvati（MIX が 2-MCFL であること）、Kanazawa–Salvati (2012), *MIX is not a tree-adjoining language*
- well-nested な fan-out 2 の MCFG と TAG の等価性については、原典を確かめてから引用すること

ネットワークから取得できない資料は、作業を始める前に研究者に添付を頼んでください。読めなかった資料は、報告の読了表に「未読」と明記してください。**記憶だけに基づく文献の主張は「記憶による。未確認」と明記すること。** 読んだふりは絶対にしないでください。

---

## 1. ここまでの到達点（台帳の要約。これ自体を検証の対象とすること）

- **問題。** `op:fanout-two` は、fan-out $f\ge2$ で **LG** が擬多様体の境界かどうかを問う。
  - **肯定の答え** = LG が境界である。
  - **否定の答え** = 境界でない。LG の外のある擬多様体が、一様多項式の特徴データを持つ。
  - 十分性は全 fan-out で証明済みである。`prop:sl-reduction` により、問題は内容型付け $c_\Sigma$（$|\Sigma|\ge3$）の問いに帰着する。
- **R4 系 B（定理 A と補題 4 に依存）。** fan-out 2 では次が成り立つとされる。
  - 肯定の答え ⟺ ある有限アルファベットの内容型付けで、根の希少型が超多項式になる族がある。
  - 否定の答え ⟺ すべてのアルファベットの内容型付けで、希少型予想 `conj:rare-types` が成り立つ。
  - 補題 4 は、拡大アルファベット $\Gamma_f(\Sigma)$ の上に「小さく薄い提示」$G^X$ を作り、`prop:pattern-thickness-transfer` を適用している。**R4 自身はこの命題の証明を独立に再検査しておらず**、その証明が引用する `lem:normalization-stages` も未読である。
- **R1〜R8（肯定方向の構成の排除）。** 次の構成が排除されたとされる。
  - 倍増型（R1 定理 2、R2 定理 B）
  - 周期枠での一つの手による段の符号化（R5、R6）
  - Parikh 差の異なる符号（R7 定理 E）
  - 錠のかかった符号（R8 定理 H4）。H4 は、文法の非終端数の下界 $2^{M/(3r)}/\mathrm{poly}$ による。
- **R9〜R11（根の型 $m=\{\mathtt a\}$ の上界）。**
  - R9 定理 HΞ（H4 の抽象形。「最も監査を要する」と自己申告されている）は、周期的な宿主での数え上げで、文法の大きさの下界を与える。
  - R10 定理 A は HΞ\* を使い、強制部分木の重い節点が実質 fan-out 1 なら $\Lambda_{\mathtt a}$ と $\mu_{\mathtt a}$ が多項式であることを示す。
  - R11 定理 4 は、この仮定を「非 a の文字を二つ以上持つ類」だけに弱めた。
  - **依存の鎖：HΞ → HΞ\* → R10 定理 A → R11 定理 4。**
- **残る障害（R11 系 6）。** 非 a の文字を二つ以上持つ類 $K$ で、比較できない $K$ 節点の対がすべて次のどちらかになる場合が残る。
  - **(R1\*) 交差**：成分の射影が可換でない。
  - **(R2\*) 離れているか入れ子**：関係する成分の内容が $K$ を含まない（分裂）。
- 既知の例は R15 の L_{N,d} だけである。L_{N,d} は分裂型で、$N=O(\bar\theta^2)$ にとどまる。
- **未着手の部分。** $|m|\ge2$ で周期的でない宿主の場合、fan-out $\ge3$ への持ち上げ。

---

## 2. 課題

課題は五つあります。**優先順位は T2 > T1a > T1b > T3 > T4 > T5** です。計算資源の上限が近づいたら、その時点までの結果を zip にまとめて出してください（§7 の「中間提出」）。R12 は全部を一度にやろうとして止まりました。同じ失敗を避けてください。

### T1. 土台の独立監査（読み通しではなく、再構成）

主張文と仮定だけを見て、**自分で証明を組み立て直してください。** そのあとで原証明と照合し、食い違いを列挙すること。

**T1a. R4 補題 4 と `prop:pattern-thickness-transfer`。**

1. `prop:pattern-thickness-transfer` の証明を、`lem:normalization-stages` を含めて全文で検査する。特に次の三点を確かめる。
   - 正規化の各段階で、元厚さ $\bar\theta$ とパターン厚さ $\bar t_{\rm pat}$ がどう変わるか。
   - fan-out と rank が保たれるか。
   - reduced good になるか。
2. R4 補題 4 で、$H$（$\varphi^{-1}(L)\cap R$ の提示）が `prop:pattern-thickness-transfer` の仮定を本当に満たすかを確かめる。確かめる点は次のとおり。
   - $\|H\|$ と $\bar t_{\rm pat}$ の評価
   - 文脈とずれた導出の扱い
   - 拘束節点の反鎖・路の評価
3. 補題 4 が成り立たない場合は、系 B のどちらの向きが壊れるかを特定する。壊れる向きは次の二つ。
   - 希少型予想 ⇒ IC
   - IC ⇒ 否定の答え

**T1b. R9 定理 HΞ。**

1. 数え上げを再構成する。対象は、仮定 (PH)、溶解の対と原型、重みの部分和が互いに異なること、$|V|\ge2^{M/(3r)}/(2\Delta^4)$ の導出。
2. 特に次の三点を確かめる。
   - 「$W$ は $L$ の**実際の**最短語」という仮定が、R10 と R11 の適用場面で毎回確認されているか。
   - 「同じ非終端の部分木の交換（文脈自由性）」と「代入可能性（Rect）」が混同されていないか。
   - $\Delta$ が本当に $\|G\|$ と $\bar\theta_G$ の多項式か。
3. HΞ → HΞ\* → R10 定理 A → R11 定理 4 の各段で、仮定が正しく引き継がれているかを表にする。

判定は、VALID（自分で再構成できた）、GAP（どこが埋まらないか）、REFUTED（反例つき）のいずれかで付けてください。

### T2. 障害 (R1\*)・(R2\*) と well-nested 性の照合

**well-nested** の定義は Kanazawa (2009) に従います。規則の右辺で、異なる子の成分が $x_i\cdots y_j\cdots x_k\cdots y_l$ の形で交互に並ばないことです。fan-out 2 なら、二つの子 $B(x_1,x_2)$ と $C(y_1,y_2)$ の成分が $x_1\,y_1\,x_2\,y_2$ の順に現れないことになります。原典で定義を確認し、確認した定義を報告に書いてください。

1. reduced good な fan-out 2 文法の導出木で、比較できない二つの節点の成分が交差して並ぶ（R11 の意味の「交差」）とき、その最小共通祖先へ至る路のどこかに well-nested でない規則があるかを調べる。「交差 ⇒ ill-nested な規則」を証明するか、反例を示すこと。逆向き（ill-nested な規則があれば、交差する $K$ 節点の対が現れるか）も調べる。
2. したがって、**well-nested な文法では (R1\*) が消えるか**を判定する。
3. (R2\*)（分裂型）は well-nested な文法でも残るかを判定する。R15 の L_{N,d} について、次を確かめる。
   - G^{cross}_{d,q} と G^{nest}_{d,q} がそれぞれ well-nested かを、規則を書き出して判定する。
   - L_{N,d} が well-nested な fan-out 2 文法を、同程度の $\|G\|$ と $\bar\theta_G$ で持つかを調べる。
4. well-nested 性が、`prop:good-normalization` と `prop:pattern-thickness-transfer` の正規化で保たれるかを調べる。保たれない段階があれば特定する。

**注意。** well-nested 性は文法の性質であり、言語の性質ではありません。「言語が well-nested な文法を持つ」ことと「議論で使う最小の文法が well-nested である」ことを区別してください。

### T3. well-nested な場合の問題を、既存の理論から攻める

1. **問題を定式化する。** 対象言語を「well-nested で reduced good な fan-out 2 の文法を持つ言語」に制限し、$\|G\|$ と $\bar\theta_G$ もそのような文法の上で測る。この場合に `def:uniform-polydata` と `op:fanout-two` の類似物を正確に書くこと。
2. **R4 系 B の帰着が、well-nested の範囲で閉じるかを調べる。** 補題 4 の構成（$\varphi^{-1}(L)\cap R$、拡大アルファベット $\Gamma_f$）は well-nested 性を保つか。保たないなら、well-nested 版の希少型予想と well-nested 版の問題の関係はどうなるか。
3. **既存の理論を使って、well-nested な fan-out 2 の内容型付けで $\mu_m$（希少型の長さ）を多項式で抑えることを試みる。** 使える道具の例を挙げる。
   - well-nested MCFL のポンピング補題（Kanazawa 2009）
   - TAG と等価な構造（背骨の分解、adjunction の木）
   - 交差のない成分の入れ子構造
   - R9〜R11 の結果のうち、T1 を通過したもの
   - 成功すれば、**well-nested な場合の否定の答え**になる。
4. **逆に、well-nested な場合に超多項式の希少型を持つ族が作れるかも検討する。** 作れれば、well-nested な場合の肯定の答えの候補になる。
5. いずれの場合も、**一般の $m$（$|m|\ge2$）を含めて**扱うこと。$m=\{\mathtt a\}$ だけで終えない。

### T4. non-well-nested な配置に絞った、肯定方向の族の再探索

肯定の答えには、超多項式の希少型を持つ族が要ります。そうした族があるとすれば、ill-nested な規則を本質的に使う配置にあるはずです（T2 の結果による）。

1. 2-MCFL が TAL を真に超える既知の例（MIX など）と、強いポンピング補題の破れ（Kanazawa et al. 2014）の構成を調べる。原典で、そこで使われている fan-out と構成を確認すること。そのうえで、それらが「超多項式に長い最短語を持つ型」を作る機構として使えるかを検討する。
2. 交差で射影が可換でない配置（R1\*）を、重みの運び手として使う族を設計し、次を評価する。
   - **すべての**一穴・二穴の Rect（内容型付け）
   - 元厚さ $\bar\theta_G$
   - $\|G\|$
   - 実際の最短語の長さ
3. 必ず照合すること。照合先は、反証済みの経路（§3）、R1 定理 2・R2 定理 B の no-go、R5〜R8 の剛性・排除の定理、R12 の 3,093 テンプレートの探索空間である。既存の no-go に当たる設計は、早めに捨ててよい。

### T5. 筋道の判断（1〜2 段落）

T1〜T4 を踏まえて、次の四つのどれを推すかを、根拠とともに述べてください。

- (A) 今の筋道（R12：$m=\{\mathtt a\}$ の (R1\*)・(R2\*)）を続ける
- (B) well-nested / non-well-nested で問題を分け、well-nested な場合を先に閉じに行く
- (C) 肯定方向の構成に資源を移す
- (D) 別の筋道（具体的に示す）

確信度（予想であること）を明記してください。肯定と否定は §1 のとおりの向きで書くこと。

---

## 3. 必須検査（違反した論証は無効）

- 型は、穴ごとの**実際の文字内容**で決まる。語全体の Parikh ベクトルの一致から、代入の合法性を導かない。
- 穴の語は非空とし、二穴の中央も非空とする。外側文脈は空でよい。3 つ目の穴を密かに追加しない。
- 各 Rect では、次をすべて書き出す。比較タプル $x,y$、成分ごとの型、共有文脈 $E_0$、試験文脈 $E_1$、四つの語。全 Rect の主張では、場合分けが網羅的であることを論証する。
- 文法についての主張では、$\|G\|$、**元**厚さ $\bar\theta_G$、reduced/good、fan-out/rank、well-nested か否かを明示する。アルファベットは族の中で固定する。
- 一般の定理では、$L$ の実際の最短の語 $W$ から出発する。
- 部分木の入れ替えで得られる語が $L$ に入るのは、同じ非終端の部分木の交換（文脈自由性）による。代入可能性と混同しない。
- トークンの段階の閉性を、文字の段階の閉性と取り違えない。計算で「閉じた」「出ない」と出ても、予算や上限のもとでは何も示さない。
- 次の反証済みの推論を前提にしない：R13 原文 X1、R14 原文 CA、R15 一般 IH、R2 の退化した短縮補題。小さい $n$ の反例で大きい $n$ の一般定理を反証しない。有限検査を全称証明と呼ばない。
- 前任者の「VALID」を、自分の判定の根拠にしない。

## 4. 検証の作法

- 主張には VALID / CONDITIONAL（条件を明記）/ GAP / REFUTED / OPEN / CERTIFIED FINITE のいずれかを付ける。自己判定であることを明記する。
- 計算を使う場合は、`python3 -I run_all.py` 一本で全検査が走り、終了コード 0 で終わる形にする（15 分以内）。Python 3 の標準ライブラリだけを使い、ネットワークは使わない。出力は `PYTHONHASHSEED` によらず決定的にする。計算を使わない場合は、その旨を README に書けばよい。
- T1 の主要な判定には、「自己監査」節を付ける。自分の再構成を、別の観点から読み直した結果を書くこと。

## 5. 報告の構成（`report.md`、日本語、数式は LaTeX）

1. 読了表（資料、読んだ範囲、未読）
2. T2：照合の結果（定義、命題と証明または反例、R15 の文法の判定表）
3. T1a・T1b：再構成、原証明との食い違い、依存の鎖の表、判定
4. T3：定式化、帰着の可否、結果（定理と証明、または障害の正確な形）
5. T4：検討した機構、族の候補と評価、既存の no-go との照合
6. T5：筋道の判断
7. 既存結果との照合表（R1〜R11 の主要結果、R15 の L_{N,d}・補題 ST、`conj:rare-types`、`thm:doubling-no-lift`）
8. 自己監査
9. 次の最小義務（3 項目以内）

## 6. 研究上の注意

- 「既知の理論で一行で済む」と思った箇所こそ、原典の正確な主張（fan-out、well-nested の定義、言語のクラスか文法のクラスか）を確認すること。
- 失敗を報告してかまわない。「OPEN のまま。障害はここ」「T1a に GAP。系 B は片側だけ残る」は正当な成果である。
- 途中で誤りに気づいたら、取り繕わずに、その時点の結論を報告すること。

## 7. 成果物：1 つの .zip のみ

ファイル名は `RV1_astra_step_back_<YYYY-MM-DD>.zip` とし、中身は次の構成にしてください。

```
RV1_astra_step_back_<日付>/
  README.md        … 中身の一覧、結論 3 行、どの課題まで終えたか、再実行コマンドと所要時間
  report.md        … §5 の報告本体
  code/run_all.py  … 全有限検査（計算を使った場合）
  code/run_all.log … 実際の実行ログ
  SHA256SUMS.txt   … 上記全ファイルの sha256
```

- zip 以外のファイルは渡さないこと。
- zip を渡す前に、自分で展開し、`run_all.py` を実行して `SHA256SUMS.txt` が一致することを確認すること。
- **中間提出**：資源の上限が近づいたら、終えた課題までで zip を作って渡すこと。README の「どの課題まで終えたか」に、未着手の課題を明記する。次の担当は、そこから続ける。
- GitHub への反映は研究者側が行います。あなたは行わないでください。
