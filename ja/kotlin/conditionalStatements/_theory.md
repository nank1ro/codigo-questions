特定の条件が満たされた場合にのみコードを実行したいとき、意思決定が必要になります。
天気が良い場合にのみ外で遊びたいとしましょう。
プログラミングでは、ブール変数 `niceWeather` を保存し、この変数が `true` の場合に外で遊ぶという動作を `if` で実行できます：
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```

---

前の例を続けましょう。
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```
`if` 文は条件が `true` の場合にのみコードブロックを実行することを見てきました。
もう一つ重要なことは、コードブロックを示す**波括弧** `{}` です。

---

条件が成立した場合にコードブロックを実行する方法を見てきましたが、次に最初の条件が成立しなかった場合に別のコードブロックを実行する方法を見てみましょう。
天気が良ければ外で遊びます。そうでなければ、家にいます。
Kotlinでは `else` 文を使用できます：
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

もう一つチェックする条件があるとしましょう。この例のように：
```kotlin
var num = 3
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else {
    println("do something else")
}
```
このコードの出力は `the number is 3` です。
まず、数値が2に等しいかチェックします。これはfalseです。
次に2番目の文に移り、`num` が3に等しいかチェックします。trueなので、続くコードブロックを実行し `the number is 3` を出力します。

---

`else if` 文はいくつでも追加できます。制限はありません。
```kotlin
var num = 4
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else if (num == 4) {
    println("the number is 4")
} else if (num == 5) {
    println("the number is 5")
} else if (num == 6) {
    println("the number is 6")
}
```
このコードの出力は `the number is 4` です。

---

条件文（`if`、`else if`、`else`）を別の条件文の中にネスト（入れ子に）して、より複雑な構造を作ることもできます。
```kotlin
var num = 4
if (num < 3) {
    println("the number is lower than 3")
} else {
    if (num == 3) {
        println("the number is 3")
    } else if (num == 4) {
        println("the number is 4")
    } else {
        println("the number is greather than 4")
    }
}
```
このコードの出力は `the number is 4` です。

---

_エルビス演算子_ `a ?: b` は、オプショナル `a` に値が含まれている場合はそれをアンラップし、`a` が `null` の場合はデフォルト値 `b` を返します。
式 `a` は常にオプショナル型です。
式 `b` は `a` に格納されている型と一致する必要があります。
エルビス演算子は以下のコードの省略形です：
```kotlin
if (a != null) a else b
```
