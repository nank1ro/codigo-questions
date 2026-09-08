**列挙型**（*enum*）は、関連する値のグループに共通の型を定義し、それらの値を型安全な方法で扱えるようにします。
Kotlinでは`enum class`キーワードで宣言し、**エントリ**をカンマ区切りで列挙します:
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
慣習として、エントリ名は大文字で書きます。各エントリはenum型の値であり、クラス名を通してアクセスします:
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
enumクラスはファイルのトップレベル（または他のクラスの内部）で宣言する必要があり、関数の内部で宣言することはできません。

---

すべてのenumエントリには2つの組み込みプロパティがあります:

- `name`はそのエントリの名前を`String`として表したもの
- `ordinal`は宣言内でのその位置で、`0`から始まります

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

enumエントリは`==`で比較します:
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

`when`式はenumで分岐する自然な方法です。**すべて**のエントリを網羅していれば*網羅的*(exhaustive)とみなされ、`else`分岐は不要です:
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
エントリを一つでも書き忘れると、バグが実行時まで残る代わりにコンパイラがエラーを報告します。

---

enumクラスは、通常のクラスと同じように**コンストラクタ**を持つことができます。各エントリはそれぞれの引数を渡し、値はプロパティに保存されます:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
エントリのデータは変更されないことが前提なので、コンストラクタのプロパティは通常`val`で宣言します。

---

enumクラスは**メソッド**も宣言できます。メンバー宣言の前に、エントリのリストをセミコロン`;`で閉じる必要があります:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2);

    fun hasMoons(): Boolean {
        return moons > 0
    }
}
println(Planet.EARTH.hasMoons()) // true
```
メソッドの内部では、そのエントリのプロパティに加えて`name`と`ordinal`にもアクセスできます。

---

すべてのenumクラスは`entries`プロパティを公開しています。これは宣言順に並んだすべてのエントリのリストです。反復処理に便利です:
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
リストであるため、`entries`は`size`やインデックスアクセスにも対応しています。例えば`Direction.entries[0]`は`NORTH`です。

古いコードでは代わりに`values()`関数を使いますが、これは配列を返します。Kotlin 1.9以降は`entries`が推奨されます。

---

`String`からエントリに戻すには`valueOf`関数を使います。`name`が完全に一致するエントリを探します:
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
この照合は大文字小文字を区別します。`Direction.valueOf("east")`はその名前のエントリが存在しないため`IllegalArgumentException`をスローします。

---

enumクラスは**抽象メソッド**を宣言し、各エントリが波括弧で囲んだ本体で独自の実装を提供できるようにすることができます:
```kotlin
enum class Operation {
    ADD {
        override fun apply(a: Int, b: Int): Int = a + b
    },
    SUBTRACT {
        override fun apply(a: Int, b: Int): Int = a - b
    };

    abstract fun apply(a: Int, b: Int): Int
}
println(Operation.ADD.apply(2, 3)) // 5
```
各エントリは同じ型とメソッドシグネチャを共有しながら、それぞれ異なる振る舞いをします。

---

**インターフェース**は本体を持たないメソッドを宣言します。それを実装する型はすべて、それらを提供しなければなりません:
```kotlin
interface Greeter {
    fun greet(): String
}
```
enumクラスはインターフェースを実装できます。コロンの後にインターフェースを列挙し、それぞれの実装に`override`を付けます。enum本体の中では、現在のエントリは`this`であり、他のエントリはクラス名なしで参照できます:
```kotlin
enum class Language : Greeter {
    ENGLISH, ITALIAN;

    override fun greet(): String = when (this) {
        ENGLISH -> "Hello"
        ITALIAN -> "Ciao"
    }
}
println(Language.ITALIAN.greet()) // Ciao
```
