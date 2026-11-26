reviewer: ChatGPT
target_commit: d7804c4
date: 2026-11-27
status: complete
progress: §0–8, appendix A, CSV, independent checks and logs complete
verdict_editor: Major
verdict_R1: Major
verdict_R2: Major

# 0. 結論（先に）

Major revision（投稿前修正を推奨）。主定理 A・C の撤回を求めるものではない。命題4.3、定理4.5、4.6、6.6(d) の核心は正しい。主な問題は、非自明な型付けについての偽の一般化、個別パラメータと全長の区別、未解決問題についての過剰な解釈、検証コードの型判定である。全長下界は現在の捕獲補題から平方根に強化できる。行番号はすべて英語 main.tex @d7804c4（blob 8599c931d2c9e7cd39e0a2fa471596bae834c655）。

# 1. 数学の検証

| 主張 | 行 | 判定 | 根拠 |
|---|---:|---|---|
| ガロア閉包・積・SPP・型付き細分化 | 433–610, 765–786 | 正しい、既知部分を含む | 閉包積の両側包含、型の積、初期集合の和、到達文脈から導出。 |
| 定義3.4 | 672–686 | 定義可能、明確化要 | A ごとの和、空集合最大値、符号長でなく明示的記号数、型表の費用を明示する。 |
| 型付き学習器 | 696–738 | 使用する健全性は正しい | 更新の有限性と reset の議論。未使用の逆向きは断定せず削除可。 |
| 節点構造・上界 | 795–887 | 正しい | 括弧の種類・位置から部分木の階層が定まる。型付き各成分の閉包の一致。 |
| 命題4.3 | 889–920 | 正しい | 最初の単項節点までの二分枝経路を列挙。兄弟部分木は各 E_k に任せる。根の規則は 2^n−1、下位規則は 2n−1。最大右辺3n。独立列挙 n=1,…,4。 |
| 捕獲補題・定理4.5 | 922–969 | 正しい | カットをまたぐ節点は一本の鎖。最小導出木では同一非終端記号を反復しない（長さを増す反復なら有限性矛盾、空なら短縮）。R は右辺由来の高々 rho|N| 個の断片で覆われ、捕獲補題で各長さが max(kappa,1) 以下。 |
| 定理4.5直後 | 978–980 | 訂正必要 | H_n は rho,|N| が小さい。列挙文法は |N|,kappa が小さい。個々のパラメータがそれぞれ必ず指数的ではない。 |
| 定理4.6・定理A | 995–1022, 207–231 | 正しい、解釈要修正 | パラメータ積の隔たりであって全長の隔たりではない。特定二構成の全長比較だけでは最小全長の比較にならない。 |
| Rec・注意5.3 | 1071–1138 | 数学的主張妥当、再現性注意 | 正しい型は両標識括弧を検出する。独立計算で n=2,3 と11語標本を調べた。 |
| primal/dual 下界 | 1148–1201 | 正しい、適用範囲限定 | 固定 r,k、指定された全候補アルゴリズム。型付き primal は非空核により型が一意。任意の学習器の下界ではない。 |
| 比較表 | 1227–1228 | 偽 | 非自明な長さ偶奇型付けでも L_n は O(n) 規則、最大核長 O(n) の提示を持つ。 |
| 注意5.8 | 1264–1287 | 正しい | 同じ型の x と同じ文脈に入る語は分布同値。合同文法を型で細分化し、各非空収量の分布類を採用すると SPP。空語・空言語を明記する。 |
| 双対性と厳密包含 | 1295–1438 | 正しい | 型付き核の同種制限、枠の型による制限。反単調性は very weak/weak FKP に限定。 |
| weak FCP 非単調性 | 1459–1476, 1703–1831 | 本稿の論証に矛盾なし | KY2017 の補題への依存を明記。原典照合の限界は §6。 |
| 定理6.6(d) | 1484–1513 | 正しい、強化可能 | 生産的でない記号と到達不能記号を除去しても言語・SPP は保存され、全長は増えない。T≥|N|,rho,max(kappa,1) より T³≥R。 |
| 未解決問題8.3・命題8.4 | 1608–1639 | 命題は正しい、解釈過剰 | 証明は標識部分木の全体を含む収量の長さのみを制限する。文法導出木の深さや標識端末を導入する規則の位置は制限しない。 |

## 新しい強化（定理6.6(d)）
R=3·2^(n−1)−1 とする。定理4.5の最小導出木においてカットをまたぐ鎖に現れる非終端記号はすべて異なる。したがって使われる生成規則も異なる。それらの右辺長の和を q と置けば、R≤q·max(kappa,1)。全長Tは q+max(kappa,1) 以上（有限非空の対象では少なくとも一つ非空の核が必要）。よって T²≥4q·max(kappa,1)≥4R、すなわち T≥2√R。元の立方根下界は誤りではなく、この強化は追加提案である。全長の下界証明において未使用非終端記号の除去はこの直接証明では不要。

## 非自明な型付けの反例
s(w)=|w| mod 2 を非空語上の全射半群準同型とする。L_n では各階層 E_i の収量が同一の分布を持つ。奇数長は u_i（2i+1）、偶数長は i≥1 における二項構造 [u_(i−1)u_(i−1)]（4i）で代表可能。G_n をこの2型で細分化・刈り込み、各非空の型付き成分にその代表語を核として置けば、強1-FKPとなる。規則数 O(n)、最大核長 O(n)。従って 1227–1228 行の「自明型付けのみ」は偽である。これは s_U についての定理6.6を反駁しない。

# 2. Reviewer 1 の報告（Major／Minor／Typo）

推薦：Major revision。定理の量化と比較対象を正確にすること。#1 R1 の基準（特に R1.2, 3, 7, 8, 10, 22, 24–25, 29–35）を適用した。主結果は短く、適切な修正で支持できる。

## Major

- R1-M1（1227–1228）：「only for the trivial typing」は偽。§1 の長さ偶奇反例を採用するか、「under the trivial typing (or none); in contrast, s_U forces ...」に限定する。前回の「全型付けで短い」という誤りの逆方向への過修正である。
- R1-M2（978–980）：「each parameter must be exponential separately」は直後の列挙文法と H_n 自身により否定される。未知なのは最適な trade-off や特定の文法サイズ制約下で必要な核長、特性標本の最長語など。n=2 では u_n の方が w*_(n−1) より長いので suffices の文も漸近的とする。
- R1-M3（226–229, 360–367）：既知の二つの上界の比較から型なしの最小全長が分離しないことは従わない。最小全長を明示し、型なしの場合は open とする。型付きの分離は正しい。
- R1-M4（1615–1619）：命題8.4が言うのは完全な部分語 v を含む節点の収量長である。個々の標識端末を含むだけの収量ではない。収量長が大きいことは導出木の深さが小さいことを意味しない。単位規則で任意に深くでき、括弧を別々の規則で導入できる。主張を「every node spanning the entire occurrence of v leaves at most ell symbols outside its yield」に限定する。
- R1-M5（1120–1138, 1504–1512）：付属 check_rec_samples.py の sU は開き標識のみを判定し、閉じ標識だけの因子を誤分類する。長さを打ち切った飽和を exact とするのも不十分（別途健全性を証明すれば可）。独立実装で両括弧の OR・長さ打ち切りなしに11語標本と閾値9,16を確認したので数学的主張自体は支持。check_untyped_frames.py の H_n の枠の総長の式は +1 が欠落。これも独立集計で訂正値46,86,130（n=2,3,4）を得た。漸近結果は不変。

## Minor

- R1-m1（1504–1512, 953–966）：平方根下界への強化を推奨（§1）。現在の証明でも刈り込み後の SPP と T の非増加を一文補えば十分。元の立方根は正しい。
- R1-m2（672–686）：A ごとに K_A,C_A を数えること、空集合の最大値を0とする規約、型写像・初期集合・識別子のビット長を数えない記号数尺度であることを明記。固定観測器ならこの差は多項式評価に無害。
- R1-m3（1236–1287）：注意5.8の論証は成立する。空言語、{epsilon} を別扱いし、L に epsilon を戻す際は閉包を L 相対で取り直して規則の妥当性を Lemma 5.1 と同様に確認すること。型付きの一枠提示と型なしの一核提示を混同しない。合同文法からの直接の帰結として位置付ける。
- R1-m4（373–419, 696–758, 1236–1262, 1295–1352）：自明な系・既知の定理の再証明を縮め、序論、比較表、考察、結論の反復を減らす。型付き学習器の必要な健全性だけを述べ、未使用の逆方向は削除又は根拠を明示。JoLLI 読者に必要な閉包と SPP の説明は維持。
- R1-m5（1120–1138, 1681–1682）：有限計算のデフォルト範囲・シード・上限・終了コードを明示。toy の表示だけのチェックと、失敗時も終了コード0になる rec/untyped_frames に assert 又は sys.exit を導入。再現用URLは提出コミットに固定。
- R1-m6（1609, 1579–1580）：最小全長 f(n) を定義し f(n)=2^{Omega(n)} かと問う。指数下界否定と多項式上界成立は同値でない。規則数と全長の下界も同値でない。

Typo：定理を無効にする数式の英日相違は重点箇所で見つからなかった。R1-M5 は誤植ではなく検証の実装上の指摘である。

# 3. Reviewer 2 の報告

推薦：Major revision（ただし前稿より採録可能性は高まった）。#1 R2.1 の「型付けが満たすべき条件」、R2.2 の「証明で使われない成分」、R2.3 の「技術的強化の射程」を重視した。

## R2-M1（207–231, 344–371, 1484–1522）：尺度による見かけの隔たり
Theorem A は重要な trade-off であるが、F_n は 2^n+2n−2 規則を持つ。rho|N|ell だけを数えるとこれを無視する。従って通常の grammar succinctness として売り込まないこと。Theorem C(d) が正当な主役となる。特に同じ H_n、同じ固定 s_U、同じ生成規則、同じ strong カテゴリーを枠と核で提示でき、枠は O(n²)、あらゆる核提示は指数的、という公平な比較が説得的。型なしの最小全長は依然 open。Theorem A/C を独立の問いとして一つの表で示す。

## R2-M2（360–371, 1515–1522, 1651–1668）：観測器の効果の定義域
「観測器が枠を助ける」は具体的構成での上界の改善と、強・極弱FCPのクラス包含の二種類。「never helps exemplars」は弱・極弱FKPの存在の反単調性又は homogeneous kernel の制約についてであり、あらゆる提示、strong FKP、学習時間についてではない。観測器が全長の隔たりを生じさせるために必要であるとは未証明。長さ偶奇の反例を併記すると、観測器の効用が型付け依存であることが鮮明になる。

## R2-M3（373–419, 795–887, 1525–1582）：一つの人工的有限族
一語削除族は #1 由来だが、今回の任意 CFG/SPP に対する核下界は別の強い主張である。有限で人工的な族だけでも worst-case separation として意味がある。ただし自然言語の獲得、任意の文法、任意の学習器の優劣の実証ではない。二つの学習器とも長いデータが必要になるという結果が、表現の簡潔性と学習の容易さの乖離を示す。ここを本文の含意として強調し、独立した自然言語への適用や族に依存しない捕獲条件は将来の課題とする。前稿 R2 の一般化要求は未解決だが、今回の全長分離を明瞭にすれば投稿の必須条件とまではしない。

## R2-m1（696–758, 1236–1287, 1703–1831）：使用されない構成
#1 の外側文脈型付けに相当する明白な不要観測成分は本稿には見当たらない。s_U の標識ビットは H_n で実際に使用される。fresh identity は空語の処理に使うが非空削除族では本質でない。EXREG の説明、既知の学習器の逆方向、weak 非単調性の長い付録は主定理の証明には不要だが、前二者は短い位置づけに、後者は独立結果として維持可能。

## R2-m2（71–96, 135–180, 1651–1668）：JoLLI への訴求
toy の一致・Python の分類例は数学の動機付けとして有用。実際の形態論でこの observer が与えられるという主張ではない。frame/exemplar/category を概念束の外延に対して使っていることを最初に明示し、同じ言語を生成する異なる文法の統語分析を同一視しない。同じカテゴリーを比較する場合は H_n に限る。タイトルは維持可能だが abstract 冒頭で固定観測器と明示的全長を明記する。

# 4. 観点別の点数（10点満点）

| 観点 | 点 | コメント |
|---|---:|---|
| 数学的正しさ | 9 | 主要定理は正しい。周辺の偽の一般化と過剰解釈を訂正 |
| 新規性 | 8 | 削除族の任意SPP下界と全長分離。既知結果は区別 |
| 意義（R2への耐性） | 8 | 同一H_n・固定観測器の全長比較が強い。有限族に限定 |
| 主張と定理の一致 | 6 | 型なし非分離・only trivial・8.4の解釈を修正 |
| 構成・一貫性 | 7 | 前稿より改善、重複と比較表の尺度混在が残る |
| JoLLIの読者への分かりやすさ | 7 | 例は有用だが用語と定理の層が多い |
| 検証・再現性 | 7 | 7本終了0。型判定・総長集計の不備と上限を明示 |
| 全体 | 8 | Major revision。主要定理の撤回や追加大定理は不要 |

以前の Major 判定は維持するが、今回は定理Aの上界・観測器なし枠・明示的全長の区別により意義が改善。点数は今回の版についての独立評価であり、異なる査読者の旧スコアと直接比較しない。

# 5. 主張の範囲

| 箇所 | 評価・推奨 |
|---|---|
| 題・Abstract（71–96） | 題は最悪例の存在として許容。全長の指数分離は固定観測器つき枠とすべての核提示の比較であると明記。 |
| 定理A（207–231） | 正しい。尺度は rho|N|×最大証人長。規則数を除外する。226–229行は「These particular presentations have comparable exponential total lengths; the optimum untyped frame length is open.」へ。 |
| 定理B（323–336） | 強FCP・極弱FCP の単調性、極弱/弱FKPの反単調性、弱FCP非単調性を区別する。strong FKP は未解決。 |
| 定理C（344–357） | 正しい。平方根強化は任意。固定 s_U のもとで同じ H_n を使えると明示。 |
| 結論（1651–1668） | 最小全長の型なし比較、学習モデルの一般化、同一統語カテゴリーの意味を限定。 |

推奨する一文：For the same fixed mark observer, the same grammar has a polynomial-length strong frame presentation and an exponential-length strong exemplar presentation; moreover, every exemplar presentation of the language, even with a different grammar or observer, has exponential total length. The optimal total length of untyped frame presentations remains open.

この一文が本論文の最も強い主張である。

# 6. 英日の食い違いと書誌

英語1947行、日本語版の定理環境（種類・順序）と label の並びは133項目で一致。数式の抽出比較も行った（英1958、日本1975の数式断片。インライン/ディスプレイの分割、翻訳した text、句読点の差があるため文字列比較だけでは一致しない）。重点7箇所について定理の量化、上下界、添字、式、参照先を目視照合した。定理を変える翻訳差は確認できなかった。1227–1228行および1615–1619行の誤った記述は日本語にも同様に残るので両方修正する。完全な訳文一語ずつの校正や LaTeX のビルドは行っていない。

書誌の照合（1833–1945行）：
| 文献 | 結果 |
|---|---|
| Clark 2010 | 6339, 38–51 一致。著者所属機関書誌 https://pure.royalholloway.ac.uk/en/publications/learning-context-free-grammars-with-the-syntactic-concept-lattice/ |
| Clark 2011 | FG2009, LNAI5591, 183–198。一致。https://doi.org/10.1007/978-3-642-20169-1_12 |
| Clark 2015 | JLC 25(5),1203–1229、online 2013 一致。https://doi.org/10.1093/logcom/ext037 |
| Clark–Eyraud 2007 | JMLR 8,1725–1745。プロジェクト情報源02 pp.2–22 と一致。 |
| Clark–Yoshinaka 2016 | Springer 書誌 pp.143–172、章 DOI 一致。https://doi.org/10.1007/978-3-662-48395-4_6 |
| Coste–Nicolas 2019 | PMLR 93:155–168。2018開催の会議、2019刊行。本文の年で可。 |
| Gold 1967 | 10(5),447–474 DOI一致。https://doi.org/10.1016/S0019-9958(67)91165-5 |
| Harris 1954 | Word 10(2–3):146–162。https://doi.org/10.1080/00437956.1954.11659520 |
| Kanazawa 1998 | CSLI 出版者書誌一致。https://web.stanford.edu/group/cslipublications/cslipublications/site/1575860961.shtml |
| KY2017 | Springer 目次で LNCS10168,77–88、章リンク末尾 _5 一致。https://link.springer.com/book/10.1007/978-3-319-53733-7 |
| KY2023 | PMLR217:8–22、一致。 |
| Kuriyama 2026 | Project の TCS R1 表紙および固定 GitHub #1 のタイトル一致。arXiv v5 の参照先は投稿時再確認。査読中を刊行済みとは扱わない。 |
| Leiß 2014 | LNCS8612,121–137、章書誌一致。 |
| Marcus 1993 | Cognition46(1):53–85。https://pubmed.ncbi.nlm.nih.gov/8432090/ |
| Ogden 1968 | Math. Systems Theory2(3):191–194。DBLPと一致。 |
| Python 3.12 | §6.2.9 yield expressions。https://docs.python.org/3.12/reference/expressions.html#yield-expressions |
| Yoshinaka 2011 | DLT 6795:429–440。Springer目次・書誌一致。 |
| Yoshinaka 2015 | MoL14:87–98、正式題名は単数 General perspective。https://doi.org/10.3115/v1/W15-2308 |

KY2017の最終刊行PDFは取得できず、Project 情報源04の著者稿を参照。特に合本127頁 Lemma13に、非終端記号 D の収量に a^m$a^l が入り、その閉包から大きな c^id^ie^i が除かれる一方、有限文脈集合の閉包には残る論証を確認。付録Aで使う外部結果と整合する。書誌確認は定理の世界初性の保証ではない。

# 7. 過去の査読記録との照合

独立の主要判断を固めた後、REVIEW_RESPONSE_2026-11-24/25/26、LEDGER、11-24報告・指摘一覧、11-26 lens/lens_v2 報告を参照。11-27 Astra の記録・ブランチは開いていない。

| 旧指摘 | 現在 |
|---|---|
| 11-24 I-01/02 新規性・Yoshinakaのsignature比較 | 改善。既知・新規を区別し、主定理を削除族に集中。 |
| I-03 型の積に中間終端ブロックがない | 修正維持。 |
| I-04/06 厳密包含の k=1 と存在しない型コピー | 修正維持。 |
| I-05/08 空証人・EXREG・学習器 | reset および空文脈の補足を確認。一部の既知の証明の長さは残る。 |
| I-07 サイズの区別 | 定義3.4、定理A/Cによって大幅改善したが、226行の否定的断定に新しい誤り（R1-M3）。 |
| I-09 単一標識の構成素補題 | 命題8.4として証明あり。ただし8.3での解釈は過剰（R1-M4）。 |
| 11-25 3.1 L_n の任意型付けでの短核 | s_U の下界は修正維持。一方、1227–1228行の「自明型のみ」は逆方向への新しい過修正（R1-M1）。 |
| 11-25 3.2/3.3 weak FCP 非単調性 | s_0 版・付録Aの明示的論証を維持。 |
| 11-25 型の閉じ括弧検出 | check_deletion_family.py は修正維持。新しい check_rec_samples.py に同型の誤りが再出現（R1-M5、regression と分類。ただし同じファイルへの巻戻しではない）。 |
| 11-26 見本側上界、n=3反例、最長語閾値 | 追加済み。独立の正しい型判定で再現。 |
| 11-26 学習器の射程、dual 別論証、既知の下界の帰属 | 改善維持。 |
| 11-26 R2 の観測器の役割・人工族・一般化 | 全長分離の新規定理で大きく改善。ただし型なし最適値・族を超える一般化は未解決。後者は persisting の指摘、投稿の必須条件ではない。 |
| 旧来のデータ可用性のURL・空言語・長さ | persisting。 |
 
台帳の古い番号・主定理の記載は現版と同期していない部分があるので、次の著者改稿時に更新するのが望ましい。今回は査読記録以外を編集しない。

今回初めての主要指摘：長さ偶奇反例、平方根全長下界、型なし非分離の推論、構成素補題から根近傍の規則への推論、H_n 枠全長の +1 欠落。11語標本・上界は過去の結果の再現であって今回の新規発見とは数えない。

# 8. 投稿前に直すべき項目の優先順位

| 優先度 | ID | 修正 |
|---|---|---|
| P0 | R1-M1 | 自明型のみの偽の断定を修正、偶奇反例を入れるなら短い注意で。 |
| P0 | R1-M2 | 各パラメータ個別の指数下界という誤記を削除。 |
| P0 | R1-M3/R2-M1 | 型なし最小全長はopen、定理Cが明示的全長分離。Abstract/序論/表/結論を整合。 |
| P0 | R1-M4 | 命題8.4の結論を完全なvを含む収量に限定。 |
| P0 | R1-M5 | 両括弧型判定、全長集計、飽和の健全性を修正して再実行。 |
| P1 | R1-m1 | 平方根への強化（現定理の正しさには不要）。 |
| P1 | R1-m2/m3/R2-M2 | 尺度・空語・強/弱/極弱の射程を明記。 |
| P1 | R2-M3 | 人工有限族、学習器の限定、固定型付けの意義を明示。 |
| P2 | R1-m4/m5/m6/R2-m1/m2 | 文章圧縮、再現性、記号・説明・比較表、コミット固定URL。 |

編集者として、P0を直し、P1を合理的に処理した後は JoLLI への投稿を支持する。OP8.3 の解決や自然言語実験を必須とはしない。今回の主結果は、それなしでも自己完結した最悪例分離となる。

指摘一覧は findings.csv に記録した。status は、旧レビューで同型の指摘があったものを persisting、修正済みだった型判定の不備の再出現を regression、その他を new とした。

## 検証実行の記録

著者の7スクリプトはすべて対象コミットから取得し、Git blob SHA-1 を照合したコピーを python3 -I で実行。終了コード0を確認した。check_untyped_frames.py は n=5 の言語が3,263,442語になるため引数4、reduction は4000試行、その他は既定引数。全通過の表示はコードの正しさを意味しない（R1-M5参照）。

独立コード checks/independent.py は命題4.3、H_n の規則数と枠全長、命題8.4の左端の標識置換の有限検証（n≤4）、全長下界の断片予算（2≤n≤8、各最大断片長）、偶奇型の短い代表語、注意5.8の分布と枠の同一性・H_n の型付き閉包（n≤3）を調べた。断片予算の計算は任意CFG全数検証ではなく、一般証明とは別の有限検査。checks/rec_independent.py は union-find と二項規則飽和を独立実装し、n=3の別の11語標本を見つけた。著者の標本も正しい型判定・長さ打ち切りなしで厳密に再現し、n=2,3 の最長語閾値9,16と列挙文法を確認した。

全長の厳密集計（n≥2）：H_n の規則部分 28n−22、枠部分 2n²+2n、従って T=2n²+30n−22。著者ツールの枠部分は1小さい。F_n の枠提示は T=(3n−2)2^n+n²+11n−4。H_n の見本提示は T=3·2^n+n²+30n−25。いずれも規則と証人の明示的記号数、Def 3.4 の尺度。詳細は output.txt。

作業手順の限界：ローカル git clone/ls-remote はネットワーク接続不可であったため、GitHub APIで完全なSHAのコミット・blob・枝を固定し、枝参照を親SHAで保護して更新した。git rev-parse HEAD の実行結果は得られていない。独立コードの作成・実行が既存ツール全実行より先になり、一部追加検査は過去記録参照後に実施した。初期の数学的判断および11語標本の独立探索は旧査読を読む前に行った。初回のWIPは数学査読後であり、開始直後は枝作成のみ。§0–1は同一コミット、以降は区切ってコミット。既存原稿、PDF、tools、mainは一切編集していない。

# 付録 A：英語版の査読報告

## Report of Reviewer 1

**Recommendation: Major revision.**

The paper studies finite context and kernel presentations of context-free languages, with particular attention to the effect of finite-semigroup typing. The central deletion-family lower bound is convincing. The new untyped frame grammar (Proposition 4.3), Theorem 4.6, and the explicit total-length separation (Theorem 6.6(d)) are mathematically sound in my reading. I have not found a counterexample to any of these main results. However, several surrounding statements exceed what has been proved.

1. Lines 1227–1228 assert that a linear kernel presentation of L_n is available only with trivial typing or no typing. This is false. Consider the length-parity morphism into the group of order two. The words of each level have the same distribution in L_n; the odd fibre has a representative u_i of length 2i+1, and the nonempty even fibre has a representative obtained by combining two u_(i−1)'s, of length 4i. The standard typed refinement therefore yields a strong singleton-kernel presentation with O(n) productions and O(n) maximum kernel length. The assertion should be limited to the mark observer s_U.

2. Lines 978–980 confuse the product lower bound with separate lower bounds. The displayed grammar H_n and the subsequent listing grammar demonstrate that none of the individual parameters is necessarily exponential in all presentations. State the actual unresolved trade-off instead.

3. Lines 226–229 infer an absence of a total-length gap without typing from the sizes of two particular presentations. The minimum total length of untyped frame presentations is unknown. This inference should be removed, and the introduction should agree with Open Problem 8.3.

4. Proposition 8.4 bounds the span of a constituent containing the entire occurrence of v. It says nothing about the depth of that constituent in an arbitrary derivation tree, nor about the rules introducing its individual brackets. The interpretation in lines 1615–1619 should be restricted to the precise statement.

5. The program checking the characteristic sample implements the mark observer by testing only the opening mark. A closing mark alone must also have the marked type. The current saturation is length-capped; absence of longer words requires an independent soundness argument. I reproduced the published eleven-word sample and the minimum longest-word lengths 9 and 16 using an uncapped independent union-find implementation with the correct observer. In the other new script, the H_n frame-length sum is one unit too small. These defects do not invalidate the stated asymptotic results, but the reproducibility record needs correction.

The total-length estimate can also be improved. Let R=3·2^(n−1)−1. In the minimum derivation tree used in the proof of Theorem 4.5, the chain productions are distinct. If q is the sum of their right-hand-side lengths, then R≤q max(kappa,1), while total length T≥q+max(kappa,1). Consequently T≥2 sqrt(R). This is an optional strengthening, not a necessary correction of the existing cube-root bound.

I encourage the author to define the accounting convention for total length explicitly, to handle the empty and epsilon-only languages separately in the remarks on uniform learning and substitutability, and to shorten repeated background results. The central theorem warrants publication after these corrections.

## Report of Reviewer 2

**Recommendation: Major revision.**

The comparison of distributional frames and exemplars is an attractive question for this journal. The paper now makes a substantially clearer contribution than a parameter-only separation. In particular, under the same fixed two-element mark observer, the same grammar H_n has a polynomial-total-length strong frame presentation and an exponential-total-length strong exemplar presentation, whereas every alternative exemplar presentation of the language has exponential total length. The lower bound is not a lower bound on ordinary CFG description length. Its force lies in the additional requirement that categories admit the specified sound closed-set interpretation.

The distinction between Theorems A and C is essential. The first ignores the number of productions, and the exhibited untyped frame grammar pays an exponential cost in this parameter. The second counts all productions and witnesses, and establishes a genuine separation of explicit descriptions in the typed setting. I recommend giving the second result priority in the abstract and discussion. It remains open whether the same total-length separation holds without the observer. The construction is not a proof that the observer is necessary.

The claims about the observer's effects should be stated with their quantifiers. Refinement preserves the strong and very weak context properties, while homogeneous kernels give the stated reverse inclusions for weak and very weak kernel properties. The argument does not apply to strong kernel properties in general, or to the running times of arbitrary learners. The length-parity example in the other report illustrates why the choice of observer matters rather than merely its nontriviality.

The family is finite and deliberately constructed. This is acceptable for a worst-case succinctness theorem, provided that the linguistic motivation is not treated as empirical validation. It would be valuable to understand a wider sufficient condition for capture or for the mark observer's benefit, but I do not require resolution of the open problem as a precondition for publication. The observation that both specified learning algorithms can require large data despite a short frame presentation is a particularly useful qualification. The paper must distinguish it from an information-theoretic lower bound for arbitrary learners.

The discussion of the classical Galois connection and the toy agreement example can assist the journal's readers. Several known consequences and repeated descriptions can be compressed. I found no analogue of the wholly unused outer-context typing criticized in the earlier fixed-typing paper: the mark bit really is used in H_n. The scope of the claim about categories should nevertheless be clarified when different grammars are compared.

## Editorial recommendation

Major revision, not rejection. The main results support a publishable theoretical contribution if the author corrects the false generalization and the overstatements, repairs the validation scripts, and foregrounds the genuine total-length separation. The open questions themselves need not be resolved for acceptance.
