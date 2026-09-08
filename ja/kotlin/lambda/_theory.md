**ラムダ**は名前のない小さな関数で、波括弧の中に式として直接記述します。
最初にパラメータを書き、次に矢印 `->`、その後に関数本体を続けます:
```kotlin
val add = { a: Int, b: Int -> a + b }
```
ラムダは他の値と同じように扱える値です。変数に格納し、後で関数とまったく同じように括弧を付けて呼び出せます:
```kotlin
println(add(2, 3)) // 5
```
パラメータを持たないラムダには矢印がまったくありません: `val hello = { println("Hello!") }`。

---

すべてのラムダには**関数型**があります。これは、括弧で囲んだパラメータの型、矢印、戻り値の型として記述します。
ラムダ `{ a: Int, b: Int -> a + b }` の型は `(Int, Int) -> Int` で、2つの `Int` 値を受け取って `Int` を返します。
変数に関数型を宣言すると、コンパイラがすでに型を知っているため、ラムダの中のパラメータの型は省略できます:
```kotlin
val add: (Int, Int) -> Int = { a, b -> a + b }
val greet: (String) -> Unit = { name -> println("Hi, $name") }
```
何も返さないラムダの戻り値の型は `Unit` です。

---

ラムダの本体は複数行にまたがることができます。`return` キーワードはなく、**最後の式**の値がラムダの返す値になります。
```kotlin
val describe: (Int) -> String = { n ->
    val half = n / 2
    "half of $n is $half" // returned
}
println(describe(10)) // half of 10 is 5
```
Kotlinでは `if` が式であるため、それを最後の行に置いて結果を決めることができます:
```kotlin
val parity: (Int) -> String = { n -> if (n % 2 == 0) "even" else "odd" }
```

---

ラムダのパラメータがちょうど**1つ**のときは、その宣言を省略できます。Kotlinが `it` という名前を付けてくれます。
```kotlin
// val double: (Int) -> Int = { n -> n * 2 }
val double: (Int) -> Int = { it * 2 } // same thing
```
`it` はパラメータが明示的に宣言されていないときにだけ存在し、単一パラメータのラムダでのみ使えます。
短いラムダを簡潔に保てますが、長い本体には実際の名前のほうが分かりやすいでしょう。

---

ラムダは他の関数の引数として使われることがほとんどです。コレクションにはラムダを受け取る多くの関数があります:
- `forEach` はすべての要素に対してラムダを1回ずつ実行します
- `map` はすべての要素に対するラムダの結果から新しいリストを作ります
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map({ it * 2 }) // [2, 4, 6]
```
ラムダが**最後の**引数であれば、それを括弧の外に移動できます。ラムダが唯一の引数であれば、括弧自体を省略できます。これは**末尾ラムダ**構文と呼ばれ、一般的な書き方です:
```kotlin
val doubled = numbers.map { it * 2 }
doubled.forEach { println(it) }
```

---

`Boolean` を返すラムダは**述語**と呼ばれます。これを受け取るコレクション関数はいくつもあります:
- `filter` は述語が `true` になる要素だけを残します
- `count` は条件を満たす要素の数を返します
- `any` と `all` は、一部またはすべての要素が条件を満たすかどうかを教えてくれます
```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)
println(numbers.filter { it % 2 == 0 }) // [2, 4, 6]
println(numbers.count { it > 4 })        // 2
println(numbers.any { it > 5 })          // true
```
呼び出しは**連結**できます。各関数は新しいリストを返し、次の関数がそれを処理します。
```kotlin
println(numbers.filter { it % 2 == 0 }.map { it * 10 }) // [20, 40, 60]
```

---

ラムダはソートや集計にも使われます:
- `sortedBy` は各要素についてラムダが計算した値を基準に並んだ新しいリストを返します。`sortedByDescending` はその逆です
- `reduce` はすべての要素を1つの値にまとめます。ラムダはこれまでの累積結果と次の要素を受け取ります
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })          // [fig, kiwi, banana]
println(words.sortedByDescending { it.length }) // [banana, kiwi, fig]

val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n })   // 10
```
`reduce` は最初の要素を `acc` として開始し、残りの各要素に対してラムダを実行します。

---

`reduce` では結果の形はラムダ次第です。2つの値を組み合わせる操作なら何でも使えます。合計、積、大きい方を残す、などです。
```kotlin
val numbers = listOf(3, 9, 4)
println(numbers.reduce { acc, n -> if (n > acc) n else acc }) // 9
```
`reduce` は空のリストに対しては例外をスローすることに注意してください。開始点となる最初の要素が存在しないからです。

---

ラムダは、その周囲で宣言された変数を使うことができます。周囲のコードが先に進んだ後でも使えます。これは**クロージャ**と呼ばれ、ラムダは必要な変数を*キャプチャ*します。
他の多くの言語とは異なり、Kotlinではラムダはキャプチャした `var` を**変更**できます:
```kotlin
var clicks = 0
val onClick = { clicks++ }
onClick()
onClick()
println(clicks) // 2
```
`onClick` を呼び出すたびに、外側のコードから見える同じ `clicks` 変数が更新されます。

---

ラムダは値なので、関数はラムダを**返す**ことができます。戻り値の型は関数型になります:
```kotlin
fun multiplier(factor: Int): (Int) -> Int {
    return { it * factor }
}
val triple = multiplier(3)
println(triple(5)) // 15
```
返されたラムダは `factor` をキャプチャするので、`multiplier` を呼び出すたびに異なる関数が作られます。
関数を受け取ったり返したりする関数は**高階関数**と呼ばれます。

---

返されたラムダは、関数の中で宣言された `var` をキャプチャできます。その変数は関数が返った後も生き続け、ラムダからだけアクセスできます。つまりプライベートな状態です。
```kotlin
fun makeGreeter(): () -> String {
    var calls = 0
    return { calls++; "hello #$calls" }
}
val greeter = makeGreeter()
println(greeter()) // hello #1
println(greeter()) // hello #2
```
`makeGreeter()` を呼び出すたびに新しい `calls` が宣言されるので、2つのグリーターは独立して数えます。

---

自分で高階関数を書くこともできます。関数型のパラメータはその形のラムダであれば何でも受け取り、関数の中では通常の関数と同じように呼び出せます。
```kotlin
fun repeatTwice(text: String, transform: (String) -> String): String {
    return transform(transform(text))
}
println(repeatTwice("a", { it + "!" })) // a!!
println(repeatTwice("a") { it + "!" })  // same, with a trailing lambda
```
関数型のパラメータを**最後**に置くことで、呼び出し側が末尾ラムダ構文を使えるようになります。

---

必要な関数がすでに存在する場合は、それをラムダで包む必要はありません。**関数リファレンス** `::name` は、名前付き関数を一致する関数型の値に変えます。
```kotlin
fun isEven(n: Int) = n % 2 == 0
val numbers = listOf(1, 2, 3, 4)
println(numbers.filter { isEven(it) }) // [2, 4]
println(numbers.filter(::isEven))      // [2, 4], same thing
```
メンバー関数はその型を通して参照します。例えば `String::uppercase` のようになります:
```kotlin
println(listOf("a", "b").map(String::uppercase)) // [A, B]
```

---

**匿名関数**は `fun` で宣言された名前のない関数です。関数の値を作るもう1つの方法です:
```kotlin
val square = fun(x: Int): Int {
    return x * x
}
println(square(4)) // 16
```
ラムダとは異なり、戻り値の型を明示的に宣言でき、値を生成するために `return` を使います。
匿名関数とラムダは互いに置き換えられます。どちらも `map`、`filter`、関数型を受け取る任意の関数に渡せます。

---

高階関数は、関数を受け取ることも返すこともできます。古典的な例が**合成**です。1つの関数を実行し、その結果を別の関数に渡す新しい関数を作ることです。
```kotlin
fun andThen(first: (Int) -> Int, second: (Int) -> Int): (Int) -> Int {
    return { n -> second(first(n)) }
}
val addOneThenDouble = andThen({ it + 1 }, { it * 2 })
println(addOneThenDouble(3)) // 8
```
返されたラムダは `first` と `second` の両方をキャプチャするので、`andThen` が返った後もずっと動き続けます。

---

**レシーバ付きラムダ**を受け取る関数もあります。ラムダの中では `this` が特定のオブジェクトを指すため、その名前を書かずにメンバーを直接呼び出せます。
`buildString` はよくある例です。そのラムダの中では `this` が `StringBuilder` なので、`append` をローカル関数のように呼び出せます:
```kotlin
val text = buildString {
    append("Hello")
    append(", ")
    append("world")
}
println(text) // Hello, world
```
`buildString` は最終的な文字列を返します。ループの中で `+` で連結する代わりとして便利です。
