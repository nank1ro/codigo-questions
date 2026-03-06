> `for`キーワードは、シーケンス内の各値に対してコードブロックを実行します。

`for`ループは、イテレータを提供するものを反復処理します。

`for`の構文は以下の通りです：
```kotlin
for (item in collection) print(item)
```

`for`の本体はブロックにすることもできます
```kotlin
for (item in collection) {
    print(item)
}
```

ループを通過するたびに、`item`に値の次の要素が代入されます。

以下は、固定回数のアクションを繰り返す`for`ループです：

```kotlin
for (i in 1..3) {
    println(i)
}
// prints 1, 2, 3
```

出力は、インデックス`i`が_1_から_3_までの範囲の各値を受け取ることを示しています。

---

_範囲_は、一対の端点で定義される値の区間です。
範囲を定義する基本的な方法は2つあります：

```kotlin
var firstRange = 1..3           // [1]
var secondRange = 1 until 3     // [2]
println(firstRange)
println(secondRange)

/* prints
1..3
1..2
*/
```

- __[1]__ `..`構文を使用すると、結果の範囲に両方の境界が含まれます。
- __[2]__ `until`は終端を除外します。出力は、_3_が範囲に含まれないことを示しています。

---

範囲を逆順で反復処理することができます。

`3..1`が動作すると思うかもしれませんが、残念ながら、Kotlinチームはこの機能を別の方法でインポートすることを決定しました。

実際に、このコードスニペットを実行してみると：
```kotlin
for (i in 3..1) println(i)
```

何も出力されないことがわかります。
これを動作させるには、`downTo`キーワードを使用する必要があります：

```kotlin
for (i in 3 downTo 1) println(i)
// prints 3, 2, 1
```

`downTo`は減少する範囲を生成します。

---

範囲のデフォルトの_ステップ_は__1__ですが、別の値を明示的に設定することができます。

`step`キーワードを使用して、`for`ループの__ステップ__を定義できます。

```kotlin
for (i in 1..10 step 2) {
    println(i)
}
// prints 1, 3, 5, 7, 9
```

ご覧の通り、コードブロックは_1_ではなく_2_のステップで実行され、出力が完全に変わります。

---

_文字_の範囲を生成することもできます。
```kotlin
for (char in 'a'..'z') print(char)
// prints abcdefghijklmnopqrstuvwxyz
```

---

__文字列__を反復処理することができます。
```kotlin
for (char in 'abc') print(char + 1)
// prints bdc
```

上の例では、各文字に1を加えて出力しているので、`'a'`は`'b'`になり、`'b'`は`'c'`になります。

これは、文字が[ASCIIコード](https://en.wikipedia.org/wiki/ASCII)に対応する数値として保存されているため可能です。

したがって、文字に整数を加えると、新しいコード値に対応する新しい文字が生成されます。

---

コードブロックを単に`n`回繰り返す必要がある場合は、`repeat(times: Int)`関数を使用できます。

```kotlin
repeat(3) {
    println("repeat")
}
// prints repeat 3 times
```

インデックスにアクセスすることもできます
```kotlin
repeat(3) { index ->
    println(index)
}
// prints 0, 1, 2
```

---

Kotlinでは、反復可能なコレクションに対して`for-in`を使用し、各要素に対して指定されたクロージャを呼び出すこともできます：
```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(2, 4, 6, 8, 10)
for (num in numbers) {
    println(num)
}
// prints (2, 4, 6, 8, 10)
```

---

Kotlinには`forEach`ループもあります。
`for-in`ループと同じ順序で、シーケンスの各要素に対して指定されたクロージャを呼び出します：

```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(1, 3, 5, 7, 9)
numbers.forEach {
    println(it)
}
```

`forEach`メソッドの使用は、`for-in`ループとは2つの重要な点で異なります：
1. 本体のクロージャの現在の呼び出しを終了したり、後続の呼び出しをスキップしたりするために、`break`や`continue`文を使用できません。（_実際にはアノテーションを使えば可能ですが、ここでは扱わないやや複雑なトピックです。_）
2. 本体のクロージャで`return`文を使用すると、クロージャからのみ終了し、外側のスコープからは終了せず、後続の呼び出しもスキップされません。
