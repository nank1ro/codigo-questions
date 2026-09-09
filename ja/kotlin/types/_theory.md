Kotlinのすべての値には**型**があり、型はそのデータがどんな種類のものか、そして何ができるかをコンパイラに伝えます。
基本的な型は次のとおりです：
- `Int`：`42`や`-7`のような整数
- `Long`：`Int`よりはるかに大きな整数を扱える型
- `Double`：`3.14`のような小数部を持つ数値
- `Float`：`Double`の半分のメモリを使う小数ですが、精度は低くなります
- `Char`：`'a'`のようなシングルクォートで囲まれた1文字
- `Boolean`：`true`または`false`
- `String`：`"Hello"`のようなダブルクォートで囲まれたテキスト

変数のレッスンで見たように、名前の後にコロンを付けて型を明示できます：
```kotlin
val age: Int = 36
val name: String = "Ada"
```
ある型の値を別の型の変数に格納することはできません。`val age: Int = "36"`はコンパイルエラーになります。

---

ほとんどの場合、型を書く必要はありません。Kotlinはいくつかのリテラルのルールに従って、代入する値から型を**推論**します：
- `42`のような整数は`Int`になります
- `3.14`のような小数点を含む数値は`Double`になります
- ダブルクォートで囲まれたテキストは`String`になります
- シングルクォートで囲まれた1文字は`Char`になります
- `true`と`false`は`Boolean`になります
```kotlin
val count = 42     // Int
val price = 9.99   // Double
val name = "Ada"   // String
val grade = 'A'    // Char
val isOpen = true  // Boolean
```
Kotlinが推論した型を確認するには、`::class.simpleName`で任意の値の型の名前を出力できます：
```kotlin
println(count::class.simpleName) // Int
println(price::class.simpleName) // Double
```
小数リテラルが`Float`と推論されることはありません。`val ratio = 0.5`は`Double`です。

---

`Int`は約20億までの整数を格納できます。正確には`2147483647`である`Int.MAX_VALUE`までです。
`Int`には大きすぎる整数リテラルは自動的に`Long`と推論され、接尾辞`L`を付ければ任意のリテラルを`Long`にできます：
```kotlin
val big = 3000000000  // Long, too big for an Int
val small = 3L        // Long, thanks to the suffix
```
同様に、接尾辞`f`を付けると小数リテラルが`Float`になります。`val ratio = 0.5f`のようになります。
桁数の多い数値は読みにくいため、Kotlinでは桁と桁の間の任意の場所にアンダースコア`_`を置けます。アンダースコアはコンパイラに無視されます：
```kotlin
val population = 8_000_000_000L
val million = 1_000_000
println(million) // 1000000
```

---

Kotlinは値を代入するときに数値型を自動的に変換することはありません。小さい型から大きい型への代入でさえもです。`Int`を`Long`や`Double`の変数に格納するのはコンパイルエラーです。
```kotlin
val count = 3
val total: Long = count      // error: Int is not a Long
val price: Double = count    // error: Int is not a Double
```
すべての数値型には、必要な型の新しい値を作る**変換関数**があります。`toInt()`、`toLong()`、`toDouble()`、`toFloat()`、そしてテキストを得るための`toString()`です。
```kotlin
val total: Long = count.toLong()
val price: Double = count.toDouble() // 3.0
println(count.toString() + "!")      // 3!
```
小数から整数への変換は**切り捨て**になります。`toInt()`は単に小数部を捨てるので、`3.99.toInt()`は`3`になり、`(-3.99).toInt()`は`-3`になります。

---

除算の動作はオペランドの型で決まります。両方が`Int`のとき、`/`演算子は**整数除算**を行います。結果は`Int`になり、余りは捨てられます。
少なくとも1つのオペランドが`Double`のとき、`/`は浮動小数点除算を行い、小数部を保持します：
```kotlin
println(7 / 2)              // 3
println(7.0 / 2)            // 3.5
val slices = 7
println(slices.toDouble() / 2) // 3.5
```
したがって、2つの`Int`変数から小数の結果を得るには、除算の**前に**少なくとも1つを変換する必要があります。`(7 / 2).toDouble()`は`3.0`になります。これは整数除算がすでに終わっているためです。

---

整数から計算した小数の結果を関数が返す必要があるときは、除算の前にオペランドを`Double`に変換し、戻り値の型を`Double`として宣言します：
```kotlin
fun ratio(part: Int, total: Int): Double {
    return part.toDouble() / total
}
println(ratio(1, 4)) // 0.25
```
`List<Int>`の`sum()`と`size`も`Int`の値であることを覚えておいてください。同じ変換が必要です。

---

すべての`Char`は数値、つまりその**コード**として格納されます。`code`プロパティは文字の背後にある`Int`を返し、`toChar()`はその逆で、`Int`をそのコードを持つ`Char`に変換します：
```kotlin
println('A'.code)        // 65
println(66.toChar())     // B
println(('A'.code + 2).toChar()) // C
```
文字のコードは連続しているため、コードに加算するとアルファベットに沿って進みます。
`'7'`のコードは`7`ではなく`55`であることに注意してください。`Char`が表す桁の数字を読み取るには`digitToInt()`を使います。これは`7`を返します。

---

`Char`のコードは`Int`なので、そのコードに対して算術演算を行い、結果を`Char`に戻すことができます。これがアルファベットに沿って進む方法です：
```kotlin
val next = ('a'.code + 1).toChar() // 'b'
```
Kotlinでは`Int`を`Char`に直接加えることもできます。`'a' + 1`は`'b'`になり、2つの文字`'d' - 'a'`の差は`Int`の`3`になります。

---

ユーザーが入力したテキストは、数字に見えても常に`String`として受け取ります。それを使って計算するには**パース**が必要です。`toInt()`は`"42"`を`Int`の`42`に変換し、`toDouble()`は`"3.5"`を`Double`の`3.5`に変換します。
```kotlin
val typed = "42"
println(typed.toInt() + 1) // 43
```
すべてのテキストが数値とは限りません。`"4x2".toInt()`は`NumberFormatException`をスローし、プログラムを停止させます。
安全な代替である`toIntOrNull()`と`toDoubleOrNull()`は、スローする代わりに`null`を返します。Null安全性のレッスンで学んだように、`?:`でデフォルト値を指定できます：
```kotlin
println("4x2".toIntOrNull())      // null
println("4x2".toIntOrNull() ?: 0) // 0
```

---

`toIntOrNull()`は、テキスト全体が符号付きの有効な整数であるときにのみ成功します：
```kotlin
println("42".toIntOrNull())   // 42
println("-7".toIntOrNull())   // -7
println("3.5".toIntOrNull())  // null, not a whole number
println(" 42".toIntOrNull())  // null, spaces are not allowed
println("abc".toIntOrNull())  // null
```
小数のテキストには`toDoubleOrNull()`を使います。これは`"3.5"`を受け入れ、同じように`Double?`を返します。

---

`Int`は固定サイズなので、最小値と最大値があります。`Int.MIN_VALUE`は`-2147483648`、`Int.MAX_VALUE`は`2147483647`です。
限界を超えてもエラーは**発生しません**。値はサイレントに範囲の反対側の端へ**折り返します**。この動作はオーバーフローと呼ばれます。
```kotlin
println(Int.MAX_VALUE)     // 2147483647
println(Int.MAX_VALUE + 1) // -2147483648
```
結果が20億を超える可能性があるときは`Long`を使います。その限界`Long.MAX_VALUE`は約922京です。演算の前に変換することを忘れないでください。`Int.MAX_VALUE.toLong() + 1`は`2147483648`です。

---

`Double`は小数を2進数で格納するため、正確に表せない値があり、最後の桁に小さな誤差が現れます：
```kotlin
println(0.1 + 0.2) // 0.30000000000000004
```
小数の桁数を固定して表示するには、書式文字列を指定して`String.format`を使います。`"%.2f"`は「小数点以下2桁の小数」を意味します。結果はその桁数に丸められた`String`になります：
```kotlin
println(String.format("%.2f", 0.1 + 0.2)) // 0.30
println(String.format("%.1f", 3.14159))   // 3.1
println(String.format("%.2f", 2.0))       // 2.00
```

---

`Any`は階層の最上位にある型です。すべてのKotlinの値は`Any`なので、`Any`型の変数は`Int`、`String`、`Boolean`など何でも格納できます。
実際に何が格納されているかを調べるには`is`演算子を使います。これは値がその型を持つときに`true`を返します：
```kotlin
val value: Any = 42
println(value is Int)    // true
println(value is String) // false
```
チェックが通ると、コンパイラは値を**スマートキャスト**します。`if`の中（または`when`の分岐の中）では、変換なしでその型として使えます：
```kotlin
if (value is Int) println(value + 1) // 43, value is an Int here
when (value) {
    is String -> println(value.length)
    is Boolean -> println(!value)
}
```
