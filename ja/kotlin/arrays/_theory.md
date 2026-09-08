**配列**は、同じ型の値を固定数だけ1つの変数名の下に格納します。
`arrayOf`で作成し、角括弧と`0`から始まる**インデックス**で要素を読み取り、`size`で要素数を取得します：
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
最後の要素はインデックス`size - 1`にあります。

---

`arrayOf(1, 2, 3)`は`Array<Int>`を作成し、各要素はボックス化されたオブジェクトになります。
プリミティブ型に対して、Kotlinは`IntArray`、`DoubleArray`、`BooleanArray`のような専用のより効率的な型を提供します：
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
また、各インデックスを受け取る**init**ラムダを使って指定したサイズの配列を作成したり、ゼロで埋められた`IntArray`を作成したりできます：
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

すべての配列には、インデックスを扱うための便利なプロパティが2つあります：
- `indices`は有効なインデックスの範囲で、`0`から最後のインデックスまでです
- `lastIndex`は最後の要素のインデックス、つまり`size - 1`です
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

配列が`val`で宣言されていても、インデックスに代入することで**要素**を置き換えることができます：
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
すべての要素を巡回するには、`for`ループや`forEach`を使用できます：
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
`n`と`it`は値の読み取り専用コピーであり再代入できないため、要素を変更するにはそのインデックスが必要であることに注意してください。

---

配列がある値を保持しているかを確認するには`in`または`contains`を使用し、どちらも`Boolean`を返します。
`indexOf`は最初に出現したインデックスを返し、値が存在しない場合は`-1`を返します：
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

配列をそのまま出力しても要素は表示されず、`[Ljava.lang.String;@1b6d3586`のようなものが出力されます。
読みやすい文字列を作るには`joinToString`を使用し、必要に応じて区切り文字を指定できます（デフォルトは`", "`です）。角括弧で囲まれた要素を得るには`contentToString`を使用します：
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

配列は**その場で**並べ替えることも、新しくソートされたコレクションにコピーすることもできます：
- `sort()`と`sortDescending()`は配列自体を並べ替え、何も返しません
- `reverse()`は配列自体の順序を反転させます
- `sorted()`、`sortedDescending()`、`reversed()`は配列を変更せず、新しい`List`を返します
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

数値配列には集計関数が用意されています：
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()`と`min()`は空の配列に対して例外をスローするため、配列が空の可能性がある場合は`maxOrNull()`と`minOrNull()`を使用してください。

---

配列と`MutableList`の主な違いは、配列が**固定サイズ**であることです：一度作成すると要素を置き換えることはできますが、追加したり削除したりすることは決してできず、`add`関数もありません。
`nums + 4`のような式は`nums`を大きくするのではなく、まったく新しい配列を作成します：
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
要素数が時間とともに変化する場合は`MutableList`を、要素数があらかじめ分かっている場合やプリミティブなパフォーマンスが必要な場合は配列を選んでください。

---

配列はリストと同じ変換関数をサポートします。`filter`は条件に一致する要素を残し、`map`はすべての要素を変換します。
どちらも配列ではなく新しい`List`を返します：
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
結果はリストなので、そのまま出力すると要素が表示されます。

---

ループ中にインデックスと値の両方が必要な場合は、`withIndex()`を使って各ペアを分解するか、`forEachIndexed`を使用します：
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

配列とリストは簡単に相互変換できます：
- `toList()`と`toMutableList()`は配列をリストにコピーします
- `toTypedArray()`はリストを`Array<T>`にコピーします
- `toIntArray()`は`Int`のリストを`IntArray`にコピーします
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
どの変換も**コピー**を作成するため、結果を変更しても元のものには影響しません。

---

リストとは異なり、同じ要素を持つ2つの配列は`==`では**等しくなりません**：配列は参照で比較されるため、`==`が`true`になるのはまったく同じ配列オブジェクトの場合だけです。
内容を比較するには`contentEquals`を使用します：
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

配列は固定サイズなので、その一部を取り出すには新しい配列を作成する必要があります：
- `copyOf()`は配列全体をコピーし、`copyOf(n)`は最初の`n`個の要素をコピーします
- `copyOfRange(from, to)`はインデックス`from`から`to`の**手前まで**の要素をコピーします
- `sliceArray(range)`は範囲の両端を含むインデックスの要素をコピーします
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
