**スコープ関数**は、*オブジェクトのコンテキストの中で*コードのブロックを実行します。新しい言語機能を追加するわけではなく、1つのオブジェクトに対して動作するコードをより短く、読みやすくするだけのものです。Kotlinには `let`、`run`、`with`、`apply`、`also` の5つがあります。

これらが異なるのはわずか**2**点です。ブロックの中でオブジェクトをどう参照するか、そして呼び出しが何を返すかです。まずは `let` から見ていきます。ブロックの中ではオブジェクトは `it` という名前になり、呼び出しはブロックの**最後の式の結果**を返します。
```kotlin
val word = "kotlin"
val letters = word.let { it.length } // 6
println(letters)
```
`let` がなければ一時変数が必要になりますが、`let` を使えばブロックが続く間、オブジェクトを `it` という短い名前で利用できます。

---

`let` は最後の式の値を返すので、中間変数に名前を付けずに**値を別のものへ変換する**ための便利な方法になります:
```kotlin
val price = 12
val label = price.let { "$it EUR" }
println(label) // 12 EUR
```
ブロックの中では `it` を必要なだけ何度でも使えます:
```kotlin
println("kiwi".let { "${it.uppercase()} has ${it.length} letters" })
// KIWI has 4 letters
```

---

`let` はセーフコールと組み合わせると真に役立ちます。`?.let { ... }` は値が `null` でないときに**だけ**ブロックを実行し、ブロックの中の `it` は非nullの値になるので、追加のチェックは不要です:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to ${it.uppercase()}") }
```
値が `null` のときは式全体が `null` になり、ブロックは決して実行されません。そのため、フォールバックを用意するにはElvis演算子 `?:` が自然な相棒になります:
```kotlin
fun label(city: String?): String {
    return city?.let { "City: $it" } ?: "No city"
}
```

---

`let` ブロックの中でも、オブジェクトを `it` と呼ぶ必要はありません。ラムダのパラメータに名前を付けると、ブロックがネストしているときや `it` では何を指すのか分かりにくいときに、コードを読みやすく保てます。
```kotlin
val price: Int? = 12
println(price?.let { amount -> "$amount EUR" }) // 12 EUR
```
同じ名前付けは、`it` を使うすべてのスコープ関数、つまり `let` と `also` でも使えます。

---

`apply` は2つの軸の両方で一度に進みます。ブロックの中ではオブジェクトはレシーバー `this` になり（そのメンバーは**プレフィックスなしで**使えます）、呼び出しはブロックの結果ではなく**オブジェクトそのもの**を返します。

この組み合わせにより、`apply` はオブジェクトを作ったその場で**設定**するための道具になります:
```kotlin
class Server {
    var host = "localhost"
    var port = 80
}

val server = Server().apply {
    host = "example.com"
    port = 8080
}
println("${server.host}:${server.port}") // example.com:8080
```
ブロックの中の `host` と `port` は `this.host` と `this.port` です。`apply` は設定済みの `Server` を返すので、そのまま代入できます。

---

`apply` は作ったばかりのオブジェクトに限定されません。任意のオブジェクトに対して動作し、オブジェクトを返すので、オブジェクトが期待される場所ならどこでも式全体を使えます。
```kotlin
val box = Box()
box.apply { label = "tools" }        // changes box and returns it
println(listOf(Box().apply { label = "nails" }).size) // 1
```
ブロックは普通のコードブロックなので、必要な数の文を含められます。

---

`also` は `apply` の鏡像です。オブジェクトは `it` として参照され、呼び出しは**オブジェクトそのもの**を返します。ブロックの結果は捨てられるので、`also` はログ出力や検査のような**副作用**のための関数であり、チェーンが作り出すものを変えずにチェーンの途中に差し込めます:
```kotlin
val total = listOf(1, 2, 3)
    .also { println("size: ${it.size}") } // size: 3
    .sum()
println(total) // 6
```
*"そして、その値に対してさらにこの処理もする"*と読みます。値は手を加えられないまま次のステップへ流れ続けます。

---

ブロックがオブジェクトを何かの**引数**として必要とするときは、`apply` より `also` の方が読みやすくなります。`it` はそのまま渡せますが、`this` は明示的に書かなければなりません。
```kotlin
val names = mutableListOf<String>()
val user = "ada".also { names.add(it) }
println(user)  // ada
println(names) // [ada]
```
式の値はやはり `"ada"` です。`also` は値が通り過ぎるのを見ているだけです。

---

`run` は、オブジェクトの名前の付け方が違う `let` です。ブロックの中ではオブジェクトは `this` なのでメンバーにプレフィックスは不要で、呼び出しは**最後の式の結果**を返します。

1つの値を計算するために同じオブジェクトの複数のメンバーを読むときに適しています:
```kotlin
class Rect(val w: Int, val h: Int)

val area = Rect(3, 4).run { w * h }
println(area) // 12
```
同じように `this` を使いながら、ブロックの結果の代わりにオブジェクトを返す `apply` と比べてみてください。

---

`with` は `run` と同じ仕事をしますが、拡張関数では**ありません**。ドット呼び出しのレシーバーになる代わりに、オブジェクトが最初の引数として渡されます。
```kotlin
val text = with(StringBuilder()) {
    append("Hello")
    append(", world")
    toString()
}
println(text) // Hello, world
```
ブロックの中ではオブジェクトは `this` になり、呼び出しは最後の式を返します。`run` とまったく同じです。非nullのオブジェクトがすでに手元にあり、それに対する複数の呼び出しをまとめたいときは `with` を、オブジェクトがチェーンから出てきたりセーフコールが必要になったりする可能性があるときは `run` を選んでください（`obj?.run { ... }`）。

---

5つのスコープ関数がすべて揃いました。それぞれは2つの軸の上の1点にすぎません:
- `let` - オブジェクトは `it`、ブロックの結果を返す
- `run` - オブジェクトは `this`、ブロックの結果を返す
- `with` - オブジェクトは `this`（引数として渡す）、ブロックの結果を返す
- `apply` - オブジェクトは `this`、オブジェクトを返す
- `also` - オブジェクトは `it`、オブジェクトを返す

必要な行を選びましょう。オブジェクトを何かに渡すときは `it` の方が読みやすく、多くのメンバーに触れるときは `this` の方が読みやすくなります。新しい値が欲しいときはブロックの結果を返し、オブジェクトを使い続けたいときはオブジェクトを返します。
