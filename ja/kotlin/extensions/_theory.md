**拡張関数**は、既存の型のソースコードに手を加えずに新しい関数を追加します。
`fun`、拡張したい型（**レシーバー型**）、ドット、関数名の順に書きます。
```kotlin
fun Int.squared(): Int {
    return this * this
}
println(4.squared()) // 16
```
関数の中の `this` は、その関数が呼び出された値であり、**レシーバー**と呼ばれます。`4.squared()` では `4` です。
拡張を定義したら、最初から `Int` の一部だった関数とまったく同じようにドットで呼び出せます。

---

拡張はどんな型にも使えます。ソースコードを持っていない型でも同じです。`String` は標準ライブラリのものですが、それでも新しい関数を追加できます。
```kotlin
fun String.whisper(): String {
    return this.lowercase() + "..."
}
println("HELLO".whisper()) // hello...
```
拡張の中でレシーバーの他のメンバーを使うときは `this.` を省略できます。`lowercase()` だけで `this.lowercase()` を意味し、`length` だけで `this.length` を意味します。

---

拡張関数は他の関数と同じようにパラメーターを取れます。レシーバーはドットの左側のままで、パラメーターは括弧の中に書きます。
```kotlin
fun Int.isDivisibleBy(other: Int): Boolean {
    return this % other == 0
}
println(12.isDivisibleBy(4)) // true
println(12.isDivisibleBy(5)) // false
```
ドットの前の型はごく普通の型なので、同じように `List<Int>`、`Double`、あるいは自分で書いたクラスも拡張できます。

---

拡張は、拡張対象のクラスを変更**しません**し、新しいメンバーを差し込むこともありません。コンパイラは単に呼び出しを書き換えるだけです。`"kotlin".first3()` は、`"kotlin"` を `this` として渡す関数呼び出しになります。
```kotlin
fun String.first3(): String = take(3)
val word = "kotlin"
println(word.first3()) // kot
```
だからこそ `String` や `Int` のような final なクラスも拡張できます。中身は何も変わらず、拡張はあなたのコードの中だけに存在します。

---

関数のほかに、**拡張プロパティ**も追加できます。`val`、レシーバー型、ドット、名前の順に宣言し、続けてプロパティが読まれるたびに値を計算する `get()` を書きます。
```kotlin
val String.wordCount: Int
    get() = split(" ").size

println("Kotlin is fun".wordCount) // 3
```
拡張プロパティは何も保持できません。バッキングフィールドがないため、`val String.label = "text"` のような初期化子はコンパイルエラーになります。レシーバーから値を計算することしかできません。
拡張関数とは違い、拡張プロパティは関数の中では宣言できません（ローカル拡張プロパティは許されていません）。

---

拡張プロパティは、`String` の組み込みの `length` とまったく同じように、括弧なしで読み取ります。値がレシーバーに対して何かをするのではなく、レシーバーを説明しているときに自然な選択です。
```kotlin
val Int.isNegative: Boolean
    get() = this < 0

println((-3).isNegative) // true
println(7.isNegative)    // false
```
`-3` を囲む括弧に注意してください。括弧がないと `-3.isNegative` は先に `3` のプロパティを読み、その後 `Boolean` を負号で反転しようとするため、コンパイルできません。

---

レシーバー型は**null許容**にもできます。`String?` の拡張は `null` を保持しているかもしれない変数の上でも呼び出せ、関数の中の `this` は `String?` になるので、`null` の場合は自分で処理します。ふつうは null 許容性のレッスンで見たエルビス演算子 `?:` を使います。
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val name: String? = null
println(name.orDash())  // -
println("Ada".orDash()) // Ada
```
`null` の値に対して `name.orDash()` を呼ぶのは安全です。関数自体が `null` のレシーバーを受け付けるので、`?.` は必要ありません。

---

レシーバーがnull許容の拡張の中では、安全呼び出し `this?.` を使って、値が `null` でないときだけそのメンバーにアクセスすることもできます。標準ライブラリも `isNullOrEmpty()` のような関数で同じ考え方を使っています。
```kotlin
fun String?.firstOrQuestion(): Char {
    return this?.firstOrNull() ?: '?'
}
val text: String? = null
println(text.firstOrQuestion())    // ?
println("Kotlin".firstOrQuestion()) // K
```

---

クラスが拡張と同じ名前・同じパラメーターのメンバーをすでに持っている場合、**常にメンバーが優先されます**。拡張は決して呼ばれず、コンパイラは隠蔽されていると警告します。
```kotlin
class Box {
    fun describe(): String = "member"
}
fun Box.describe(): String = "extension"

println(Box().describe()) // member
```
拡張は既存の振る舞いをオーバーライドしたり置き換えたりできません。新しい関数やプロパティを追加できるだけです。選ばれるためには、そのクラスがまだ持っていない名前かパラメーターリストが必要です。

---

**型パラメーター**のおかげで、拡張は型の一族に対してまとめて働けます。型パラメーターは型のプレースホルダーで、`fun` のすぐ後ろの山括弧の中に宣言し、Kotlin が呼び出しごとに埋めてくれます。これにより拡張は**ジェネリック**になります。
```kotlin
fun <T> List<T>.second(): T {
    return this[1]
}
println(listOf(1, 2, 3).second())      // 2
println(listOf("a", "b").second())     // b
```
`listOf(1, 2, 3)` ではプレースホルダー `T` は `Int`、`listOf("a", "b")` では `String` になるので、同じ関数が毎回正しい型を返します。

---

型パラメーターはシグネチャのどこでも使えます。戻り値の型として、null許容の `T?` として、あるいは別の型の内側でも使えます。何も見つからないかもしれないジェネリックな拡張は、組み込みの `firstOrNull()` のように `T?` を返します。
```kotlin
fun <T> List<T>.lastOrDefault(default: T): T {
    return if (isEmpty()) default else this[size - 1]
}
println(listOf(1, 2).lastOrDefault(0))          // 2
println(emptyList<String>().lastOrDefault("-")) // -
```
レシーバーは `List<T>` なので、関数の中では `size`、`isEmpty()`、インデックス参照を普通のリストとまったく同じように使えます。

---

クラスが**コンパニオンオブジェクト**を宣言していれば、たとえ中身が空でもそれを拡張できます。レシーバー型は `ClassName.Companion` と書き、拡張はファクトリ関数のようにクラス名の上で呼び出します。
```kotlin
class Temperature(val degrees: Int) {
    companion object
}
fun Temperature.Companion.freezing(): Temperature = Temperature(0)

println(Temperature.freezing().degrees) // 0
```
クラスも拡張もトップレベルの宣言なので、`main` の外に書かなければなりません。

---

コンパニオンオブジェクトの拡張はパラメーターを取れるので、別の単位や形式から変換する代替コンストラクターを置く場所として便利です。
```kotlin
class Distance(val meters: Int) {
    companion object
}
fun Distance.Companion.fromKilometers(km: Int): Distance = Distance(km * 1000)

println(Distance.fromKilometers(3).meters) // 3000
```

---

拡張をどこで宣言するかが、どこで使えるか、つまりその**スコープ**を決めます。
- ファイルのトップレベルでは、そのファイル全体と同じパッケージの残りの部分で使えます
- 関数の中では、ローカル拡張になり、その関数の中でだけ使えます
- クラスの中では、**メンバー拡張**になり、そのクラスの中でだけ使えます

メンバー拡張は自分が属するクラスのプロパティを読めるので、2つのレシーバーを組み合わせます。クラスのインスタンスと、呼び出された値です。
```kotlin
class Greeter(val greeting: String) {
    fun String.greet(): String = "$greeting, $this!"
    fun welcome(name: String): String = name.greet()
}
println(Greeter("Hello").welcome("Ada")) // Hello, Ada!
```
`greet` の中では、`greeting` は `Greeter` から来ていて、`this` は関数が呼び出された `String` です。クラスの外では `"Ada".greet()` はコンパイルエラーになります。

---

パラメーターがちょうど**1つ**の拡張関数には `infix` を付けられます。中置関数はドットと括弧なしで、レシーバーを左、引数を右に置いて呼び出せ、ほとんど文のように読めます。
```kotlin
infix fun Int.percentOf(total: Int): Int = total * this / 100

println(20 percentOf 50)   // 10
println(20.percentOf(50))  // 10, the normal call still works
```
Kotlin はいくつかの組み込み関数でもこれを使っています。`1 to "one"` は `Pair` を作り、`1 until 5` は範囲を作ります。

---

`infix` を付けるには、関数がメンバーか拡張であり、パラメーターがちょうど1つで、そのパラメーターにデフォルト値がないことが必要です。それ以外はコンパイルエラーになります。
```kotlin
infix fun Int.add(other: Int): Int = this + other          // ok
infix fun add(a: Int, b: Int): Int = a + b                 // error: not a member or extension
infix fun Int.add(a: Int, b: Int): Int = this + a + b      // error: two parameters
```
中置呼び出しの優先順位は算術演算と比較演算の間にあります。`1 add 2 * 3` は `1 add 6` であり、`1 add 2 == 3` は結果を `3` と比較します。
