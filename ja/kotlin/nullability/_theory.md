値が単に存在しないことがあります：ミドルネームを持たないユーザー、何も見つからない検索、数値に変換できないテキストなどです。
Kotlinでは、存在しない値を`null`で表しますが、通常の変数が`null`を持つことは決してできません。すべての型はデフォルトで**非null**です：
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
存在しない値を許可するには、型の後に疑問符`?`を付けて**null許容型**を宣言します。
`String?`は`String`または`null`のどちらかを保持します：
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String`と`String?`は2つの異なる型です：`String`は決して欠けることがなく、`String?`は欠ける可能性があります。

---

`String`と`String?`の違いは、実行時ではなく**コンパイラ**によってチェックされます。
非null型に`null`を代入することや、非nullの値が期待される場所にnull許容の値を渡すことはコンパイルエラーになるため、プログラムはそもそも開始されません：
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
これにより、Kotlinは他の言語でよくある「ヌルポインタ」クラッシュを回避できます。値が欠けているのは、`?`で明示的に宣言した場所だけです。

---

`?`は型が書かれる場所であればどこでも機能します：関数はnull許容のパラメータを受け取り、null許容の値を返すことができます。
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
null許容の値に対してメソッドを直接呼び出すことはできません。`null`かもしれないからです。
**セーフコール**演算子`?.`は、値が`null`でない場合にのみメソッドを呼び出し、そうでなければ式全体が`null`になります：
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
セーフコールの結果は常にnull許容になります：`word?.length`は`Int`ではなく`Int?`です。

---

多くの場合、null許容の値から必要なのは値そのものかデフォルトの値だけです。
**エルビス演算子**`?:`はまさにそれを行います：左側が`null`でない場合は左側を返し、そうでなければ右側の値を返します：
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
右側は左側が`null`の場合にのみ使用されるため、デフォルトが非nullであれば結果も非nullになります。
`?:`は`?.`と組み合わせると、セーフコールを通常の値に戻すのに便利です：
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

セーフコールは**連結**できます：チェーンのどこかのリンクが`null`になると、残りのチェーンはスキップされ、式全体が`null`になります。
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
`?:`で終わるチェーンは、1行で非nullの結果を得ることができます：
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

セーフコールのチェーンは、どのレベルも欠けている可能性があるネストされたオブジェクトで威力を発揮します：
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
各`?.`が次のステップを保護し、最後の`?:`がデフォルト値を提供します。

---

**非nullアサーション**演算子`!!`はnull許容の値を非nullの値に変換し、コンパイラに「これは`null`ではないと確信している」と伝えます：
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
間違っていて値が`null`だった場合、プログラムは実行時に`NullPointerException`でクラッシュします。これはまさにKotlinが防止するように設計されたエラーです：
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
`!!`は、値が本当に`null`になり得ない場合にのみ使用し、それ以外の場所では`?.`、`?:`、nullチェックを優先してください。

---

`if`で値が`null`かどうかをチェックすると、コンパイラはそれを記憶します：値が非nullであると分かっているブランチ内では、**スマートキャスト**によって非null型にキャストされるため、`?.`や`!!`を使わずに直接使用できます：
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
早期リターンの後でも同じことが起こります：
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
スマートキャストは、チェックと使用の間で値が変わらない`val`変数と関数のパラメータに対して機能します。

---

`let`は、呼び出し対象の値を使ってコードブロックを実行します。この値はブロック内で`it`として利用できます。
セーフコールと組み合わせると、`?.let`は値が`null`でない場合に**のみ**ブロックを実行し、ブロック内の`it`は非nullになります：
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
ブロック内で値が必要なだけの場合、`if (x != null) { ... }`のコンパクトな代替手段になります。

---

`let`はブロック内の最後の式の値も**返します**。そのため、`?.let`でnull許容の値を変換し、`?:`で`null`の場合のデフォルト値を埋めることができます：
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
`price`が`null`のときは`let`ブロックがスキップされ、式は`null`になり、エルビス演算子が`"free"`を返します。

---

コレクションもnull許容の要素を保持できます：`List<Int?>`は`null`の要素を含むことができますが、`List<Int>`は決して含みません。
`filterNotNull()`は`null`の要素を取り除いた新しいリストを返し、その要素型は非nullになるため、要素を自由に使用できます：
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

多くの標準関数は、失敗する代わりに`null`を返します。`toIntOrNull()`は文字列を`Int`に変換し、テキストが整数でない場合は`null`を返します：
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
`mapNotNull`は`map`のように各要素を変換しますが、`null`になる結果を取り除きます：
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

オブジェクトの作成時にはプロパティに値を設定できないことがありますが、使用される前には設定されると分かっている場合があります。
null許容にする代わりに`lateinit`を付けます：型は非nullのままで、読み取る際に`?.`は不要になります：
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
`lateinit`にはいくつかのルールがあります：`var`プロパティにのみ使用でき、非null型にのみ使用でき、`Int`や`Boolean`のようなプリミティブ型には使用できません。
`lateinit`プロパティを代入する前に読み取ると`UninitializedPropertyAccessException`がスローされます。事前に`::player.isInitialized`でチェックできます。

---

`null`が呼び出し側のミスを意味する場合は、`requireNotNull`で早期に失敗させます。
値が存在する場合は非nullとして返し、`null`の場合はオプションのメッセージとともに`IllegalArgumentException`をスローします：
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
呼び出し後、コンパイラは`name`自体を`String`にスマートキャストするため、その行以降は`name.length`が許可されます。
`!!`とは異なり、失敗時には明確なメッセージが含まれ、*引数*が間違っていたことを示します。

---

拡張関数は**null許容のレシーバ**に対して宣言できるため、`null`の値に対しても呼び出すことができます。関数内では`this`はnull許容であり、チェックが必要です：
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
呼び出し箇所では`?.`が不要なことに注意してください：関数自体が`null`の場合を処理します。
標準ライブラリは、任意の`String?`に対して安全に呼び出せる`isNullOrEmpty()`や`orEmpty()`でこのテクニックを使用しています。

---

`?:`の右側には`return`を含む任意の式を書けます。これにより、値が欠けているときに関数から即座に抜け出すコンパクトな方法が得られます：
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
これまでに見たすべてのツールは上手く組み合わさります：null許容のパラメータと戻り値の型は値が*どこで*欠ける可能性があるかを表し、`?.`、`?:`、`let`、スマートキャスト、`toIntOrNull`は決してクラッシュすることなくそれを処理します。
