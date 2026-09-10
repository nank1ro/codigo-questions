**高階メソッド**とは、関数を引数として受け取るメソッドのことです。Kotlin のコレクションには高階メソッドが数多く用意されていて、渡す関数は普通 **ラムダ**、つまり波かっこの中に書く小さな匿名関数です。
`map` は最もよく使われるもので、すべての要素に対してラムダを呼び出し、その結果を入れた**新しいリスト**を返します。元のリストはそのまま残ります。
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map { it * 2 }
println(doubled) // [2, 4, 6]
println(numbers) // [1, 2, 3]
```
ラムダの引数が 1 つだけのときは宣言する必要がありません。Kotlin がそれを `it` と名付けます。ラムダはメソッド名のあと、丸かっこの外に書き、ラムダが唯一の引数のときは丸かっこを省略できます。これが **trailing lambda** の書き方で、このトピックのすべての演習で使います。

---

`filter` は `Boolean` を返すラムダ（**述語**と呼びます）を受け取り、述語が `true` になる要素だけを含む新しいリストを返します。
```kotlin
val numbers = listOf(4, -2, 7, 0)
println(numbers.filter { it > 0 }) // [4, 7]
```
`it` の代わりに、引数に名前を付けて矢印 `->` を続けることもできます。名前を付けると長いラムダが読みやすくなり、ラムダを別のラムダの中に入れ子にするときは必須です。内側の `it` が外側の要素を隠してしまうからです。
```kotlin
val minLength = 4
val words = listOf("fig", "banana", "kiwi")
println(words.filter { word -> word.length >= minLength }) // [banana, kiwi]
```

---

`forEach` は各要素に対してラムダを 1 回ずつ実行し、何も返しません。`for` ループの高階メソッド版で、出力のような副作用のために使います。
```kotlin
listOf("a", "b").forEach { println(it) }
```
`forEachIndexed` は各要素の位置も渡してくれます。そのラムダは引数が**2 つ**なので、名前を付けなければなりません。`it` は引数がちょうど 1 つのラムダにしか存在しないからです。
```kotlin
listOf("a", "b").forEachIndexed { index, letter ->
    println("$index: $letter") // 0: a、次に 1: b
}
```

---

`reduce` はすべての要素を 1 つの値にまとめます。そのラムダは 2 つの引数、つまり**アキュムレータ**（そこまでの結果）と次の要素を受け取ります。最初の要素をアキュムレータとして始め、残りのすべての要素についてラムダを実行します。
```kotlin
val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n }) // 10
```
空のリストでは、開始できる最初の要素がないため `reduce` は例外を投げます。`fold` はそれを解決します。アキュムレータの**初期値**を引数として渡すと、最初の要素も含めてすべての要素についてラムダが実行されます。
```kotlin
println(numbers.fold(0) { acc, n -> acc + n })   // 10
println(listOf<Int>().fold(0) { acc, n -> acc + n }) // 0
```
`fold` ではアキュムレータが要素と違う型でもかまいません。たとえば数値のリストから `String` を組み立てることもできます。

---

高階メソッドの中には、新しいコレクションを作るのではなく、コレクションについての問いに答えるものがあります。どれも述語を受け取ります。
- `any` は**少なくとも 1 つ**の要素が述語を満たすとき `true` を返します
- `all` は**すべての**要素が述語を満たすとき `true` を返します
- `none` は**どの**要素も述語を満たさないとき `true` を返します
- `count` は述語を満たす要素が**いくつあるか**を返します
```kotlin
val numbers = listOf(1, 2, 3)
println(numbers.any { it > 2 })   // true
println(numbers.all { it > 2 })   // false
println(numbers.none { it > 2 })  // false
println(numbers.count { it > 1 }) // 2
```
空のリストでは `any` は `false` を返し、`all` と `none` は `true` を返します。ルールを破る要素が 1 つもないからです。

---

集約メソッドはコレクション全体を 1 つの値に変えます。
- `sum()` は数値のリストを合計し、`sumOf` はラムダが各要素について計算した値を合計します
- `maxByOrNull` と `minByOrNull` は、ラムダの値が最大または最小になる**要素**を返し、空のリストでは `null` を返します
```kotlin
val words = listOf("fig", "banana", "kiwi")
println(words.sumOf { it.length })      // 13
println(words.minByOrNull { it.length }) // fig
println(listOf(1, 2, 3).sum())           // 6
```
`maxOf { it.length }` との違いに注意してください。こちらはその値を生んだ要素ではなく、最大の**値**（`6`）を返します。

---

`sortedBy` は、ラムダが各要素について計算した値の小さい順に並べた新しいリストを返します。`sortedByDescending` は大きい順に並べます。比較したいのが要素そのものであれば、`sorted()` と `sortedDescending()` にラムダは不要です。
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })            // [fig, kiwi, banana]
println(words.sortedByDescending { it.length })  // [banana, kiwi, fig]
println(words.sorted())                          // [banana, fig, kiwi]
```
このソートは**安定**です。キーが同じ要素は元の相対的な順序を保ちます。元のリストが変更されることはありません。

---

`take(n)` は最初の `n` 個の要素を持つ新しいリストを返し、`drop(n)` は最初の `n` 個の要素を**除いた**新しいリストを返します。どちらもラムダを取りませんが、ラムダを取るメソッドのあとにつなげて使うことがよくあります。
```kotlin
val numbers = listOf(5, 3, 8, 1)
println(numbers.take(2))                    // [5, 3]
println(numbers.drop(2))                    // [8, 1]
println(numbers.sortedDescending().take(2)) // [8, 5]
```
`takeWhile` と `dropWhile` は述語を取る版です。述語が `true` である**かぎり**先頭から要素を取り続ける、あるいは捨て続け、述語を満たさない最初の要素で止まります。
```kotlin
println(numbers.takeWhile { it > 2 }) // [5, 3, 8]
```

---

`groupBy` はコレクションを `Map` に分けます。ラムダが各要素の**キー**を計算し、各キーにはそのキーを生んだ要素のリストが元の順序で対応づけられます。
```kotlin
val words = listOf("fig", "kiwi", "pear")
val byLength = words.groupBy { it.length }
println(byLength)    // {3=[fig], 4=[kiwi, pear]}
println(byLength[4]) // [kiwi, pear]
```
結果の型は `Map<K, List<T>>` で、`K` はラムダが返す型、`T` は要素の型です。キーは最初に現れた順に並びます。

---

ラムダが各要素について**リスト**を返すとき、`map` はリストのリストを作ります。`flatMap` は同じことをしたうえで、それらのリストをすべて 1 つの平らなリストにつなげます。
```kotlin
val numbers = listOf(1, 2)
println(numbers.map { listOf(it, -it) })     // [[1, -1], [2, -2]]
println(numbers.flatMap { listOf(it, -it) }) // [1, -1, 2, -2]
```
順序は保たれます。まず最初の要素から生まれた値がすべて並び、次に 2 番目の要素の値、というように続きます。すでにリストのリストがある場合は、`flatten()` がラムダなしでつなげてくれます。

---

`zip` は 2 つのリストの要素を位置ごとに組み合わせます。ラムダなしなら `Pair` の値のリストを返し、その両側は `.first` と `.second` で読み取ります。ラムダを渡すと、各位置の 2 つの要素がラムダに渡され、その結果がリストにまとめられます。
```kotlin
val names = listOf("Ann", "Bob")
val ages = listOf(31, 25)
println(names.zip(ages))                            // [(Ann, 31), (Bob, 25)]
println(names.zip(ages) { name, age -> "$name:$age" }) // [Ann:31, Bob:25]
```
結果の長さは 2 つのリストのうち**短いほう**に合わせられ、長いほうの余った要素は無視されます。

---

ラムダの形は、メソッドが期待するものと一致していなければなりません。
- 一度に 1 つの要素を扱うメソッド（`map`、`filter`、`sortedBy`、`groupBy` など）は**引数が 1 つ**のラムダを取り、そこでは `it` が使えます
- `reduce`、`fold`、`forEachIndexed`、そしてラムダ付きの `zip` は**2 つ**の値を渡すので、`a, b ->` のように引数に明示的な名前を付けなければなりません
```kotlin
val numbers = listOf(1, 2, 3)
numbers.map { it * 2 }                  // ok: 引数が 1 つ、it が使える
numbers.reduce { acc, n -> acc + n }    // ok: 引数が 2 つ、名前付き
numbers.reduce { it + 1 }               // エラー: 引数が 2 つのとき it は存在しない
```
引数に名前を付けるのは常に許されていて、引数が 1 つでもかまいません: `numbers.map { n -> n * 2 }`。

---

高階メソッドは**つなげる**ことができます。それぞれが新しいコレクションを返し、次のメソッドがそれを処理するので、計算全体が左から右へのパイプラインのように読めます。
```kotlin
val words = listOf("kiwi", "fig", "banana", "date")
println(words.filter { it.length == 4 }.map { it.uppercase() }.sorted()) // [DATE, KIWI]
```
マップにも高階メソッドがあります。`mapValues` はキーをそのまま残し、各値をラムダの結果に置き換えます。ラムダは `.key` と `.value` を持つ**エントリ**を受け取ります。
```kotlin
val byLength = words.groupBy { it.length }      // {4=[kiwi, date], 3=[fig], 6=[banana]}
println(byLength.mapValues { it.value.size })   // {4=2, 3=1, 6=1}
```

---

チェーンの中では `it` の型が段階ごとに変わります。`List<String>` に `filter` をかけたあとはまだ文字列ですが、`map { it.length }` のあとは `List<Int>` になるので、次のラムダには数値が渡されます。
```kotlin
val words = listOf("kiwi", "fig")
println(words.map { it.length }.filter { it > 3 }) // [4]
```
どの段階も**新しい**リストを返し、前のリストには決して手を触れません。ですからチェーンは、結果を変えずに名前付きの中間の値へ分割できます。

---

ラムダの中にさらに別の高階メソッドの呼び出しを書くことができます。内側のラムダの中では `it` は**内側**の要素を指し、外側の要素を隠してしまうので、両方に手が届くように外側の引数には明示的な名前を付けましょう。
```kotlin
val sales = listOf("north" to 120, "south" to 80, "north" to 30)
val byRegion = sales.groupBy { it.first }
val totals = byRegion.mapValues { entry -> entry.value.sumOf { it.second } }
println(totals) // {north=150, south=80}
```
`"north" to 120` は `Pair` を作ります。ここでは外側のラムダがマップのエントリを扱い、内側のラムダがそのエントリのリストにあるペアを扱っています。

---

`Map` はエントリのリストのように処理できます。`filter` と `map` はマップに直接使え、`.key` と `.value` を持つ各エントリを受け取ります。マップに対する `filter` はマップを返し、`map` はリストを返します。`sortedBy` のような並べ替えのメソッドはマップには定義されていません。まずエントリのコレクションである `scores.entries` を経由してください。
```kotlin
val scores = mapOf("Ann" to 90, "Bob" to 72)
println(scores.filter { it.value > 80 })              // {Ann=90}
println(scores.entries.sortedBy { it.value }.map { it.key }) // [Bob, Ann]
```
`scores.entries` はすべてのエントリの集合で、`scores.keys` と `scores.values` は片側だけを返します。
