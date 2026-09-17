**例外**とは、文を実行できないことをKotlinが報告するための仕組みです。`"abc"` を数値に変換すること、整数をゼロで割ること、リストの末尾を越えて読むこと — これらはすべて例外をスローします。

```kotlin
fun main() {
    println("before")
    val n = "abc".toInt()
    println("after")
}
```
このプログラムは `before` を出力したあとで止まります。`toInt()` は `"abc"` を読むことができないため、`NumberFormatException` を**スロー**します。プログラムの中のどこもそれに対処していないので、Kotlinはエラー報告とともにプログラムを終了させ、`after` が決して出力されることはありません。

`throw` キーワードを使えば、自分で例外をスローすることもできます：
```kotlin
throw Exception("something went wrong")
```

誰も処理しない例外は警告ではありません。実行の終わりです。

---

プログラムを動かし続けるには、危険が伴う文を `try` ブロックの中に置き、回復の方法を `catch` ブロックに記述します：
```kotlin
try {
    println("abc".toInt())
} catch (e: Exception) {
    println("cannot read that number")
}
println("still running")
```
Kotlinは `try` ブロックを実行します。その中の文がスローすると直ちにブロックの残りがスキップされ、制御は `catch` ブロックへ移ります。括弧の中の名前 — ここでは `e` — が例外オブジェクトで、`Exception` がキャッチされる型です。

`catch` ブロックが終わると、プログラムは `try`/`catch` 全体の後の行から通常どおり続行します。

---

`Exception` をキャッチするとすべてがキャッチされますが、それはめったに望むところではありません。ブロック内の別の場所でのタイプミスまで飲み込まれてしまいます。代わりに、回復方法を知っている**正確な型**を指定してください。

失敗の種類ごとに固有の型があります。`"abc".toInt()` は `NumberFormatException` をスローするので、キャッチするのはこの型です：
```kotlin
try {
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("that is not a number")
}
```
ブロックの中で別の種類の例外がスローされた場合、この `catch` には合致せず、例外は関数の外へ伝わっていきます。

---

1つの `try` には複数の `catch` ブロックを続けられ、それぞれが異なる型を処理します：
```kotlin
val letters = listOf("a", "b")
val index = 5
val text = "abc"
try {
    println(letters[index] + text.toInt())
} catch (e: NumberFormatException) {
    println("not a number")
} catch (e: IndexOutOfBoundsException) {
    println("no such letter")
} catch (e: Exception) {
    println("something else went wrong")
}
```
Kotlinはブロックを**上から下へ**試し、型が合致した最初のブロックを実行します。実行されるブロックは常に1つだけです。

したがって順序が重要です。`NumberFormatException` と `IndexOutOfBoundsException` はどちらも `Exception` の一種なので、`catch (e: Exception)` を最初に書くとあらゆる失敗に合致してしまい、その下のブロックが実行されることはありません。最も具体的な型を最初に、最も一般的な型を最後に書いてください。

---

`finally` ブロックは最後に追加できます。これは**何が起ころうとも**実行されます。`try` が成功したあとでも、`catch` が回復したあとでも、例外がまったくキャッチされなかったときでさえもです。

```kotlin
try {
    println("reading")
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("bad number")
} finally {
    println("closing")
}
```
```
reading
bad number
closing
```
そのため、ファイルを閉じるといったスキップできない後片付けの場所として適しています。`try` には `catch` か `finally` の少なくとも一方が必要ですが、両方を持つこともできます。

---

Kotlinでは `try` は文であるだけでなく、値を生み出す**式**でもあります。その値は、実行されたブロックの最後の式です。何も失敗しなければ `try` ブロックの、失敗すれば `catch` ブロックのものになります。

```kotlin
val n = try { "abc".toInt() } catch (e: NumberFormatException) { 0 }
println(n) // 0
```
これはKotlinの慣用的な形です。`var` を宣言して2箇所で代入し、すべての経路が値を設定してくれることを期待する代わりに、常に使える値を保持する1つの `val` が手に入ります。

`finally` ブロックは値を決して変えないことに注意してください。これは副作用のためだけに実行されます。

---

`try` は式なので、値が期待される場所ならどこでも使えます。`=` で書かれた関数の本体全体としても使えます：
```kotlin
fun length(text: String): Int = try {
    text.toInt()
} catch (e: NumberFormatException) {
    -1
}
```
両方のブロックは同じ型の値を生み出さなければなりません。ここでは `Int` です。フォールバックは `catch` ブロックの最後の式として書いてください。どちらのブロックの中にも `return` はありません。

---

スローやキャッチは無料ではなく、よく使われる変換のために、Kotlinはスローする代わりに単に `null` を返すより安価な変種を用意しています。`toIntOrNull()`、`toDoubleOrNull()`、`toLongOrNull()` です。

```kotlin
println("42".toIntOrNull())  // 42
println("abc".toIntOrNull()) // null
```
左側の値が `null` のときに代替値を供給するElvis演算子 `?:` と組み合わせると、`try`/`catch` の全体が1行に収まります：
```kotlin
val n = "abc".toIntOrNull() ?: 0
println(n) // 0
```
失敗が本当に例外的なときには `try`/`catch` を、不正な入力が想定されるときには `toIntOrNull()` を選んでください。

---

自分の関数も、標準ライブラリと同じように `throw` で不正な入力を拒否できます。ライブラリは最もよくあるケースのために型をすでに用意しています。`IllegalArgumentException` は「渡された値を受け付けられない」という意味です。

```kotlin
fun half(n: Int): Int {
    if (n < 0) throw IllegalArgumentException("n must not be negative")
    return n / 2
}
```
`throw` は関数を直ちに終了させます。その下にある `return` が実行されることはありません。どう対処するかは呼び出し側が決めます：
```kotlin
try { println(half(-4)) }
catch (e: IllegalArgumentException) { println("rejected") }
```
でっち上げの値を黙って返すよりスローする方が良いのです。間違った答えは遠くまで運ばれますが、例外は対処する準備ができている最初の呼び出し元で止まります。

---

すべての例外は、作られたときに渡されたテキストを持っています。`catch` ブロックの中では、例外オブジェクトの `message` プロパティからそれを読めます：
```kotlin
try {
    throw IllegalArgumentException("price must be positive")
} catch (e: IllegalArgumentException) {
    println(e.message) // price must be positive
}
```
`message` はnull許容です。テキストを持たずに例外が作られることもあるためです。`e.message ?: "unknown"` は、プレーンな `String` が必要なときの安全な代替を与えてくれます。

例外オブジェクトそのものを出力するより `e.message` を出力する方が好まれます。オブジェクト自身のテキストにはクラス名も含まれており、出力を読む人にとってはノイズになるからです。

---

すべての引数に `if (...) throw IllegalArgumentException(...)` と書くと煩雑になるため、Kotlinは平文のように読める2つの省略形を用意しています：

```kotlin
require(n >= 0) { "n must not be negative" }   // IllegalArgumentException をスロー
check(started) { "not started" }               // IllegalStateException をスロー
```
どちらも条件とメッセージを生み出すブロックを受け取り、どちらも**条件が偽のとき**にスローします。唯一の違いは例外の型で、その違いが読み手へのメッセージになります：

* `require` は呼び出し元が渡した**引数**を守り、`IllegalArgumentException` で失敗します。
* `check` はオブジェクトやプログラムの**状態**を守り、`IllegalStateException` で失敗します。

ブロックはチェックが失敗したときにだけ評価されるので、正常な経路ではメッセージの構築にコストがかかりません。

---

組み込みの型のどれもあなたの失敗をうまく表せないときは、独自の型を宣言してください。例外は `Exception` を継承し、そのテキストを親に渡す普通のクラスです：

```kotlin
class InsufficientFundsException(message: String) : Exception(message)
```
その1行だけで完全な例外型になります。他の例外と同じようにスローされ、キャッチされ、`e.message` は作られたときのテキストを返します：
```kotlin
try {
    throw InsufficientFundsException("balance too low")
} catch (e: InsufficientFundsException) {
    println(e.message) // balance too low
}
```
メリットは正確さです。呼び出し元は `InsufficientFundsException` だけをキャッチし、他のすべての失敗はそのまま通すことができます。

---

`runCatching` はブロックを実行し、例外が外へ逃げることを決して許しません。代わりに `Result` を返します。これは、ブロックが生み出した値**または**ブロックがスローした例外の**どちらか**を保持するオブジェクトです：

```kotlin
val ok = runCatching { "42".toInt() }
val bad = runCatching { "abc".toInt() }

println(ok.isSuccess)   // true
println(bad.isFailure)  // true
```
値はそのあとで読み出します。失敗を何に変えるかはあなたが選べます：
```kotlin
println(ok.getOrNull())      // 42
println(bad.getOrNull())     // null
println(bad.getOrElse { 0 }) // 0
```
`getOrNull()` は失敗を `null` に変え、`getOrElse { ... }` はブロックを実行して代替値を作ります。呼び出し場所で何かがスローされることはないので、失敗は持ち運んで後で対処できます。

---

`Result` は開封しなくても調べられます。`onFailure` は結果が例外を保持しているときにだけブロックを実行し、`onSuccess` は値を保持しているときにだけ実行します。そして**両方とも同じ `Result` を返す**ので、呼び出しをチェーンできます：

```kotlin
runCatching { "abc".toInt() }
    .onFailure { println("could not read it") }
    .onSuccess { println("read $it") }
```
ブロックの中では例外（または値）が `it` として利用できるので、`it.message` が失敗のテキストになります。

これが「記録して続行」の形です。問題が起きた場所で報告してから続行します。早期の `return` も、2箇所から代入される `var` もありません。

---

`try` をどこに置くかで、1つの不正な値がどれだけの作業をだめにするかが決まります。**ループ全体**を包めば最初の失敗で残りのバッチが諦められ、**本体**を包めばその1要素だけが失われます：

```kotlin
var total = 0
for (value in listOf("3", "x", "5")) {
    try {
        total += value.toInt()
    } catch (e: NumberFormatException) {
        // この値はスキップする
    }
}
println(total) // 8
```
これはスローする検証関数と自然に組み合わさります。関数は1つのルールを述べてそれに反するものを拒否し、ループは拒否されても1要素分しか損しないと判断します。
