特定の条件が満たされた場合にのみコードを実行したいとき、意思決定が必要になります。
天気が良い場合にのみ外で遊びたいとしましょう。
プログラミングでは、ブール変数`niceWeather`を保存し、この変数が`true`の場合に外で遊ぶという動作を`if`で実行できます:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```

---

前の例の続きを見てみましょう。
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
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
    // play outside
} else {
    // stay home
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
// prints 10
```
上記のコードの省略形は次の通りです:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// prints 10
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
