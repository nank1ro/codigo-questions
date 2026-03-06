特定の条件が満たされた場合にのみコードを実行したいとき、意思決定が必要になります。
天気が良い場合にのみ外で遊びたいとしましょう。
プログラミングでは、ブール変数 `niceWeather` を保存し、この変数が `true` の場合に外で遊ぶというアクションを `if` で実行できます：
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```

---

前の例の続きを見てみましょう。
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```
`if` 文は条件が `true` の場合にのみコードブロックを実行することがわかりました。
もう一つ重要なことは、コードブロックを示す**波括弧** `{}` です。

---

条件が成立した場合にコードブロックを実行する方法を見ましたが、次に最初の条件が成立しなかった場合に別のコードブロックを実行する方法を見てみましょう。
天気が良ければ外で遊び、そうでなければ家にいます。
Swiftでは `else` 文を次のように使用できます：
```swift
var niceWeather = true
if niceWeather {
    // play outside
} else {
    // stay home
}
```

---

別の条件を確認したい場合を考えてみましょう。次の例のようになります：
```swift
var num = 3
if num == 2 {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else {
    print("do something else")
}
```
このコードの出力は `the number is 3` です。
まず、数値が2に等しいかどうかを確認しますが、これは偽です。
次に2番目の文に進み、`num` が3に等しいかどうかを確認します。これは真なので、次のコードブロックを実行して `the number is 3` を出力します

---

`else if` 文はいくつでも追加でき、制限はありません
```swift
var num = 4
if (num == 2) {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else if (num == 4) {
    print("the number is 4")
} else if (num == 5) {
    print("the number is 5")
} else if (num == 6) {
    print("the number is 6")
}
```
このコードの出力は `the number is 4` です。

---

条件文（`if`、`else if`、`else`）を別の条件文の中にネストして、より複雑な構造を作ることもできます。
```swift
var num = 4
if num < 3 {
    print("the number is lower than 3")
} else {
    if num == 3 {
        print("the number is 3")
    } else if num == 4 {
        print("the number is 4")
    } else {
        print("the number is greather than 4")
    }
}
```
このコードの出力は `the number is 4` です。

---

三項条件演算子は3つの部分からなる特別な演算子で、`question ? answer1 : answer2` の形式をとります。
`question` が真か偽かに基づいて、2つの式のうち1つを評価するためのショートカットです。
`question` が真の場合、`answer1` を評価してその値を返します。そうでなければ、`answer2` を評価してその値を返します。
```swift
let a = 10, b = 20, c: Int
if (a < b) {
    c = a
} else {
    c = b
}
print(c)
```
上記のコードの省略形は次のとおりです：
```swift
let a = 10, b = 20, c: Int
c = a < b ? a : b
print(c)
```
条件 `a < b` が真だったので、`c` は `a` に等しく設定されます

---

_nil合体演算子_ `a ?? b` は、オプショナル `a` に値が含まれている場合はアンラップし、`a` が `nil` の場合はデフォルト値 `b` を返します。
式 `a` は常にオプショナル型です。
式 `b` は `a` の中に格納されている型と一致する必要があります。
nil合体演算子は以下のコードの省略形です：
```swift
a != nil ? a! : b
```
