# 新規性監査

対象行番号はすべてZIP内 `manuscript/main.tex`。KNOWNは正しさを否定するものではない。添付の著者先行稿を「既刊」とはみなさず、既にその資料に書かれている内容との重複を区別する。

## Theorem A（151–161行；thm:dualityほか）

**総合：基本包含は既存理論の短い帰結。具体的strict witnessesには追加内容がある。**

| 構成要素 | 照合先 | 判断 |
|---|---|---|
| closureと積の両立、lem:clark / lem:star | Clark 2013/2015 Props. 3.26, 3.28；KY2017 §3 Eq.(1) | KNOWN。starは中間集合を挟む直接の帰結 |
| kernel規則validityの文脈テスト | KY2017 §4 p.6、Algorithm 2直前の同値 | KNOWN |
| homogeneous typed kernelのreduction | 上記同値＋restricted Galois | 正しい直接の導出。独立の新しい代数原理としては弱い |
| typed VW-FKP=W-FKP | KY2017 Prop.10のterminal-rule addition | 型整合性を確認するだけの移植 |
| context refinement | product construction、Yoshinaka2015 §8のsort refinement | routine。ただし2015年は本稿のvery weak性をそのまま定式化していない |
| 核のcoarsening包含 | reduction＋型写像π | 明示した比較命題として有用だが証明は短い |
| context側のstrict witness | KY2017 Prop.2(i)の同じL・同じpumping obstruction | U1での救済とs0のε分離を追加したもの |
| kernel側のL_K | KY2017 Prop.2(ii)のimbalance下界を二markerで埋め込む | この具体的構成は照合範囲で見つからなかった。k1への強化が可能 |

**重要な引用訂正（145–147行）**：Yoshinaka2015 §8は、signatureの拡張・有限sort refinementを定義し、対応するsubstitutable/congruential/context-deterministic classesを比較している。「neither framework addresses comparison of different observers」という一般的否定は過剰。公平な記述は「本稿のhomogeneous-kernel SPPとcontext SPPの反対方向の包含、および二つの具体的分離を明示的に比較する」である。

## Theorem B（163–170行；thm:uniform、rem:uniform-known）

**判定：KNOWN（添付先行稿＋既知の定理からの直接の帰結）。**

1. 著者先行稿 `Kuriyama_TCS1_fixed_typing_CFG.pdf` **Proposition 9.7**、PDF pp.20–21、印刷行803–816：全固定sのクラスがCONGに入る。その証明は任意のCFGをtyped refinementしてtrimし、同型yieldが到達文脈を共有することから分布同値を得る。空語も処理されている。
2. Yoshinaka2015 **§6.3 Definition 3 と直後の記述**：congruential grammarは1-FKP。これはclosureの定義からも、全yieldの分布が代表一語の分布と等しいことで直ちに従う。
3. 元のCFGを先にbinaryにしてからProp.9.7の証明を行えばrank≤2が保存される。新しいtyped refinementの結果を忘却するだけで、untyped weak 1-FKPのrank2文法を得る。
4. KY2017 **Theorem 6**をr=2,k=1に適用する。これがpositive presentation＋membership queriesという同じモデルの、同じuntyped学習器への帰結。

したがって「全観測を一つの学習器で扱う」ことも追加のhard theoremではない。これはClarkのMAT学習定理を誤ってMQ-onlyへ移した批判ではない。上で明示的に使用する学習定理はKY2017 Theorem 6である。

Yoshinaka2015 §6.1はsort別substitutabilityとpositive-only learnerを扱う。これだけから観測未知の合併クラスがpositive-onlyで学べるとはならない。原稿のGoldによる非学習性の説明は正しい。

## Theorem C（172–183行；thm:deletionと学習器の系）

**判定：今回の照合範囲では同じ主張は確認されず、有望な追加結果。**

既出なのは著者先行稿 **Proposition 6.4**のL_n、w_n*、M_n、およびpositive-only characteristic-dataのdistinguishing-pair下界。さらに同稿 **Remark 6.5**は有限言語のlinear grammarで無益なcycleを除く長さ議論を使っている。

本稿で追加されるのは以下。

- `lem:capture`：削除語を完成させる一つの変更文脈を使い、任意SPP文法の特定のconstituent yieldをkernelそのものへ強制する。
- `thm:deletion`：任意の非線形CFGも含め、cutをまたぐpathとその付随piecesを数え、ρ|N|max(κ,1)に下界を与える。
- `cor:primal-data`：指定のAlgorithm 2のkernel候補数・RHS長と結び付けた収束時データ下界。
- `prop:dual-refutation`：短いtyped context表示があっても、Algorithm 1に残る実際の候補規則の反駁に長い語が必要。

これらは先行稿の「正例のみで二言語を識別する」議論からは直ちに従わない。MQを持つ学習器に、正例のみの識別下界をそのまま流用しているわけではない。

新規性未発見は世界初の保証ではない。表現下界・核の有限生成の文献全体を網羅したとはしていない。

## KY2023との正確な包含

`rem:exreg`（432–441行）は **§2.1 extended regular closure、§2.2 closure property、§3.2 guarded expressions、Lemmas 2,4、Theorem 6**により正しい。

非空Cのsize m、fiber regular expressionのsize b_μなら、guarded expressionはsize (2m+b_\mu)。空Cは到達文脈一つへ正規化。多開始記号は新たなS→Aで処理し、Sの式は空文脈query atom。このため対象はEXREG_{max(r,1)}(max(1,2k+max b_μ))に入る。regular expressionへの変換が多項式とは限らないので、観測器を可変にした計算量の主張を付け足してはいけない。

KY2023は冒頭脚注1でdualのみを扱うと明記しており、homogeneous kernelの比較を同論文が明示しているわけではない。

## 追加一次資料の確認状況

- **Clark 2013/2015**：著者公開PDFのProps. 3.26,3.28を実際に確認。積closureの基礎は既知。
  [著者公開PDF](https://alexc17.github.io/static/pdfs/JLC2013.pdf)
- **Kanazawa–Kappé2019**：Definition 3はClark-congruentiality、Lemma 5は同稿Lemma 2の文法変換がそれを保存する旨。本稿のobserver比較や削除族下界を示す文献ではない。rankの議論の補助引用にはなるが、Theorem Bの重複判定に必須ではない。
  [PMLR原文](https://proceedings.mlr.press/v93/kanazawa19a/kanazawa19a.pdf)
- **Leiß2014**：著者長版Theorem 2はCNFとFCPの仮定の下で修正学習器の極限同定を述べる。22頁長版と刊行短版の番号の同一性までは確認していない。typed kernelや本稿の下界の直接の先行ではない。
  [著者長版](https://www.cis.uni-muenchen.de/~leiss/cfg-learning.FG-14.dyck.pdf)
- **Clark2010 ICGI**：本文未確認。KY2017・2016概説およびLeißの議論による間接確認に留め、直接の定理番号を記載しない。
- **Yoshinaka2011 DLT**：本文未確認。学習定理の直接根拠には添付KY2017 Theorems 3–6を用いた。

## 論文をどう位置づけ直すか

Theorem Bを「先行理論からの帰結」として短縮する。基本closure計算を既知の道具として整理し、Theorem Aの厳密分離とTheorem Cの表示・反駁コストを中心にする。abstractの「observer is redundant」はprimalの質的可学習範囲についてのみ述べ、全学習モデル・データ量への普遍的主張にしない。
