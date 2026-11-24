# op:weak-fcp：second-marker候補の部分結果

対象：`main.tex` 877–888行（`op:weak-fcp`）。これは査読中の追加論証であり、原稿の主定理の判定とは分離する。

## 結果と限界

KY2017 Theorem 14の言語L'に、第一成分の中心markerだけを新文字@へ変えたコピーを追加した言語L+は、

1. **untyped weak 2-FCP**を持つ。
2. **h_{\{@\}}-typed weak FCPを、どんな有限kでも持たない**。

従って「untyped weak FCP ⊆ 任意sでtyped weak FCP」は偽。この包含は原稿のTheorem Aでは主張されていないので、主定理の反例ではない。

**s0-typed weak FCPの正側は未証明**。したがってs≼hでのtyped-to-typed単調性というop:weak-fcpそのものは解決していない。以下は単なる有限実験でなく、KY2017 Lemmas 8,12,13を使う数学的部分結果である。

## 1. 言語と文法

Σ0={a,b,c,d,e,f,#,$,%}、Σ=Σ0∪{@}。

\[
\begin{aligned}
L_1&=\{v\$z:v\in\{a,b,\#\}^*,\ z=(erase_\#v)^R\},\\
L_2&=\{wyc^id^ie^jz:w,z\in\{a,b\}^*,y\in(\#\{a,b\}^*)^*, |w|_a\ge|w|_b\},\\
L_3&=\{wyc^id^je^jz:w,z\in\{a,b\}^*,y\in(\#\{a,b\}^*)^*, |w|_a\le|w|_b\},\\
L_4&=\{v\$zc^k\%f^l:v\in\{a,b,\#\}^*,z\in\{a,b\}^*\},\\
L_5&=\{vc^id^ie^jzc^k\%f^l:v\in\{a,b,\#\}^*,z\in\{a,b\}^*,j\ne k\}.
\end{aligned}
\]

全指数は非負。L'=L1∪…∪L5。L1@はL1の$を@に置換したもの。L+=L'∪L1@。

初期集合I={S1,S2,S3,S45}とし、文法は以下。

```
S1  -> $ | @ | aS1a | bS1b | #S1
Q   -> epsilon | aQbQ | bQaQ
F   -> Q# | Fa | Fb | F#
H   -> epsilon | cHd
E   -> epsilon | Ee
C   -> epsilon | cC
J   -> epsilon | dJe
S2  -> HE | FS2 | QS2 | aS2 | S2a | S2b
S3  -> CJ | FS3 | QS3 | bS3 | S3a | S3b
T   -> epsilon | Ta | Tb
U   -> EeT | TcC | eUc
S45 -> $TC% | HU% | aS45 | bS45 | #S45 | S45f
```

これはKY2017 Lemmas 8,12の文法にS1→@を加えただけ。S1は他の非終端記号の規則から参照されないので、S1以外の生成言語は不変。S1の生成言語がL1∪L1@になり、全体はL+。

## 2. 全非終端記号のweak contexts

以下で閉包はL+に対する通常閉包。V={a,b,#}*、Z={a,b}*、D={vc^id^ie^iz:v∈V,z∈Z,i≥0}。

| 非終端記号 | 生成言語の閉包 | context集合 |
|---|---|---|
| S1 | L1∪L1@∪D | {(a#,a),(b#,b)} |
| S2 | L2∪D | {(ε,ε),(a#,b)} |
| S3 | L3∪D | {(ε,ε),(b#,a)} |
| Q | {w∈{a,b}*:|w|a=|w|b} | {(ε,#cd),(a,b#de)} |
| F | {w#v:|w|a=|w|b,w∈{a,b}*,v∈V} | {(ε,cd),(ε,ade)} |
| H | {c^i d^i:i≥0} | {(a#c,d)} |
| E | e* | {(a#cd,e)} |
| C | c* | {(b#c,de)} |
| J | {d^i e^i:i≥0} | {(b#d,e)} |
| T | {a,b}* | {($,a%)} |
| U | {e^j z c^k:z∈Z,j≠k} | {(e,c%)} |
| S45 | L4∪L5 | {(ε,f)} |

### S1の確認

KY2017 Lemma 12が記すD_{L'}(L1)は、mirror contextsに加え、L4を完成させるsuffix-% contextsを含む。L1@を同時に受け入れる文脈はmirror contextsだけ。$と@を両方含む語はL+に存在せず、@語はL4型のsuffixも持たない。

従ってD_{L+}(L1∪L1@)はmirror contexts全体で、その共通解はL1∪L1@∪D。二文脈(a#,a),(b#,b)では、markerなしの候補は一方からc,d個数の一致、他方からd,e個数の一致を強制される。markerありの候補はそれぞれ正しいmirror語に限定される。%を含む候補は文脈右端a,bでL4,L5の形から外れる。これで表の等式。

### 他の11非終端記号の確認

生成言語は変わらない。新たな共通文脈が存在するなら@を文脈に含み、すべてのyieldをL1@へ送る必要がある。しかし以下のyieldでそれを排除できる。

- Qはεとab、Fは#とab#、Tはεとaを生成する。@がcontext中に固定されると、これらの対を挿入するのは@の片側だけである。#を消した左右長の一致を両方で満たすことはできない。
- Hはcd、Eはe、Cはc、Jはde、S2はcd、S3はde、Uはeを生成する。これらの文字を含む語はL1@には入らない。
- S45のyieldは%を含むのでL1@へ入らない。

従って各生成言語の共通文脈集合は旧L'のものと同じ。そのclosureに新たな@語が入る可能性も、表の有限contextで排除される。

- S2でx∈L1@ならa#xbは左右末端のa/bが一致せずL1@に入らない。S3はb#xaで同様。
- Q,F,H,E,C,Jの表の少なくとも一文脈にはc,d,eのいずれかが固定され、@語との完成はL+に入らない。
- Tの文脈は$と%、Uの文脈はeと%、S45の文脈は右端fを持ち、@語との完成は入らない。

旧アルファベット上ではKY2017 Lemmas 8,12のclosure等式をそのまま使える。これで12記号全てが有限context≤2で弱く特徴づけられ、untyped weak 2-FCPが成立。

## 3. @-indicatorでの負側

h=h_{\{@\}}とする。型1はΣ0+、型ζは@を含む語、型1sharpはε。

L+を生成するh-typed weak FCP文法Gが存在すると仮定する。ζ型の非終端記号と@を含む規則を除き、型1または1sharpの初期記号を残す。型1や1sharpの規則の子にはζ型が現れえない（ζはabsorbing）。従って得られるCFG G0はちょうどL'を生成し、残った各Aの生成言語はGの時と同じ。

KY2017 Lemma 13のproofをG0に適用すると、ある非終端記号Bが非空のa^p $ a^qを生成し、その生成言語のclosureは有限contextsでは特徴づけられない。その反証では、どんな有限contextsでも十分大きい非空c^i d^i e^iを余計に受け入れることが使われる。

Bの型は1。Bのyieldに$語があるので、L+に関する共通文脈は@を含まない。Σ0語への評価はL'とL+で同じなので

\[
D_{L+}(L(G,B))=D_{L'}(L(G_0,B)).
\]

Bを弱く特徴づける有限typed contexts Cがあれば、各c∈Cはその$語を受け入れるため@を含まない。そして

\[
L(G_0,B)^{\rhd_{L'}\lhd_{L'}}\cap\Sigma_0^+
=C^{\lhd_{L'}}\cap\Sigma_0^+.
\]

これはLemma 13の非空c^i d^i e^iによる矛盾に反する。εの削除はこの矛盾を解消しない。従ってh-typed weak FCPは存在しない。

## 4. 残る問題

上の正側文法はnullableなQ,H,E,C,J,T等を持ち、s0-typedではない。正長成分へ分割すると、その正長生成言語のclosureが表の旧closureをΣ+と交わしたものより小さくなる可能性がある。新しい有限context群を全成分に与えるか、nullable成分を避ける別の構成が必要である。この不足を隠してop:weak-fcpを解いたとはしない。

計算 `scripts/check_weak_candidate.py` は32,691語×12成分について、表の候補集合と有限context intersectionを正確な無限言語membershipで比較した。全通過。ただし生成言語closureとの等式、および全てのCFGに対する負側は上の数学的論証による。
