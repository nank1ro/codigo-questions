特定の条件が満たされた場合にのみコードを実行したいとき、意思決定が必要になります。
天気が良い場合にのみ外で遊びたいとしましょう。
プログラミングでは、ブール変数`niceWeather`を保存し、この変数が`true`の場合に外で遊ぶという動作を`if`で実行できます:
```javascript
var niceWeather = true;
if (niceWeather) {
    // 外で遊ぶ
}
```

---

前の例の続きを見てみましょう。
```javascript
var niceWeather = true;
if (niceWeather) {
    // 外で遊ぶ
}
```
`if`文は条件が`true`の場合にのみコードブロックを実行することがわかりました。
もう一つ重要なことは、コードブロックを示す**波括弧**`{}`です。

---

条件が成立した場合にコードブロックを実行する方法を学びました。次に、最初の条件が成立しなかった場合に別のコードブロックを実行する方法を見てみましょう。
天気が良ければ外で遊び、そうでなければ家にいます。
JavaScriptでは`else`文を使うことができます:
```javascript
var niceWeather = true;
if (niceWeather) {
    // 外で遊ぶ
} else {
    // 家にいる
}
```

---

もう一つの条件をチェックしたい場合を考えてみましょう。次の例のようになります:
```javascript
var num = 3;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else {
    console.log("do something else");
}
```
このコードの出力は`the number is 3`です。
まず、数値が2に等しいかチェックします。これはfalseです。
次に、2番目の文に進み`num`が3に等しいかチェックします。trueなので、続くコードブロックが実行され`the number is 3`と出力されます。

---

`else if`文は好きなだけ追加でき、制限はありません。
```javascript
var num = 4;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else if (num == 4) {
    console.log("the number is 4");
} else if (num == 5) {
    console.log("the number is 5");
} else if (num == 6) {
    console.log("the number is 6");
}
```
このコードの出力は`the number is 4`です。

---

条件文（`if`、`else if`、`else`）を別の条件文の中にネスト（入れ子に）して、より複雑な構造を作ることもできます。
```javascript
var num = 4;
if (num < 3) {
    console.log("the number is lower than 3");
} else {
    if (num == 3) {
        console.log("the number is 3");
    } else if (num == 4) {
        console.log("the number is 4");
    } else {
        console.log("the number is greather than 4");
    }
}
```
このコードの出力は`the number is 4`です。

---

三項条件演算子は3つの部分を持つ特別な演算子で、`question ? answer1 : answer2`の形式をとります。
`question`がtrueかfalseかに基づいて、2つの式のうち1つを評価するためのショートカットです。
`question`がtrueの場合、`answer1`を評価してその値を返します。そうでなければ`answer2`を評価してその値を返します。
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// 10 を出力
```
上記のコードの省略形は次の通りです:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// 10 を出力
```
条件`a < b`がtrueだったため、`c`には`a`が代入されます

---

_nil合体演算子_ `a ?? b`は、オプショナルの`a`に値が含まれている場合はそれをアンラップし、`a`が`nil`の場合はデフォルト値`b`を返します。
式`a`は常にオプショナル型です。
式`b`は`a`の中に格納されている型と一致する必要があります。
nil合体演算子は以下のコードの省略形です:
```javascript
a != nil ? a! : b;
```

---

`if`はJavaScriptで条件文を導入するキーワードです。ここには`elif`というキーワードはありません — 2番目の条件は、2つの別々の単語として書かれる`else if`で導入されます。

---

JavaScriptのブールリテラルは小文字の`true`と`false`であり、`True`/`False`ではなく、また文字列の`"true"`/`"false"`でもありません。

---

コードブロックが実行されないようにするには、括弧内の条件が`false`と評価される必要があります。

---

`if`とその括弧の間のスペースは単なる見た目の問題です。`if(true)`と`if (true)`はJavaScriptにとって同じ文です。

---

波括弧は複数の文を1つのブロックにまとめるものです。波括弧がなければ、`if`はその直後の1つの文だけを制御します。そのため`if (true) console.log("Hello!");`は有効なJavaScriptです。

---

条件はブロックが始まる前に一度だけ評価されます。波括弧の間にある文が実行されている間、JavaScriptは条件を再度確認することはありません。

---

`false`の条件はブロックを完全にスキップし、プログラムは閉じ波括弧の後の最初の文から続行します。

---

条件はブール値である必要はありません。JavaScriptは見つけたものを何でもブール値に変換するので、`if (1)`はブロックを実行し、`if (0)`は実行しません。リテラルの`true`はそもそも変換を必要としません。

---

コードブロックは1行に限定されません — 条件が`true`のとき、波括弧の中にあるすべての文が順番に実行されます。
```javascript
if (true) {
    console.log("First line");
    console.log("Second line");
}
```
出力は`First line`に続いて`Second line`になります。

---

ブロック内の文は上から下へ次々と実行されるので、同じブロック内の2つの`console.log`呼び出しは2つの別々の行に出力されます。

---

ブロック内の文をインデントするのは読みやすさのための慣習にすぎません。JavaScriptはブロックに何が属するかを決めるのに波括弧を使い、インデントは使いません。

---

`if`、`else if`、`else`のように、条件が`true`か`false`かによってコードを実行またはスキップする文は、**条件文**と呼ばれます。

---

`isAfternoon`のように`!`による否定から作られたものでも、ブール変数はそのまま`if`の条件として使うことができ、比較は必要ありません。

---

`if`文の条件は常に括弧`()`の中に置かれ、`if`キーワードの直後、開き波括弧の前に配置されます。

---

ブロックにはいくつでも文を入れることができ、まったく入れないこともできます。`if (true) {}`は何もしないだけの有効なJavaScriptです。

---

`if`文のコードブロックとは、波括弧`{ }`の中にある命令の集まりであり、条件が`true`のときに実際に実行される部分です。
