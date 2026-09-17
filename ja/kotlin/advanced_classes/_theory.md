`data class`は**データを保持する**ことを仕事とするクラスです。プライマリコンストラクタで宣言したプロパティから、コンパイラが4つのメンバーを自動生成します：

- `toString()`：`ClassName(prop=value, ...)`という読みやすいテキスト
- `equals()`と`hashCode()`：同じデータを持つ2つのインスタンスは等しいとみなされる
- `copy()`：現在の値を再利用して新しいインスタンスを作成する

```kotlin
data class Book(val title: String, val pages: Int)

val book = Book("Dune", 412)
println(book)          // Book(title=Dune, pages=412)
println(book.copy())   // Book(title=Dune, pages=412)
```

`copy()`は**名前付き引数**と組み合わせると真価を発揮します：変更したいプロパティだけを名前で指定すれば、他のすべての値はそのまま引き継がれます。

```kotlin
println(book.copy(pages = 500)) // Book(title=Dune, pages=500)
```

元のオブジェクトは決して変更されません：`copy()`はまったく新しいオブジェクトを返します。

---

プライマリコンストラクタの各プロパティに対して、データクラスは`componentN()`関数も生成します：最初のプロパティには`component1()`、2番目には`component2()`、という具合です。

これらの関数は**分割宣言**を支えています。分割宣言では、1行でオブジェクトを複数の変数に展開します：

```kotlin
data class Point(val x: Int, val y: Int)

val point = Point(3, 7)
val (x, y) = point
println(x)               // 3
println(point.component2()) // 7
```

変数の順序は名前ではなくプロパティの順序に従います。不要なものは`_`でスキップできます：

```kotlin
val (_, onlyY) = point
```

---

生成された`equals()`により、`==`は**構造的な**比較になります：プライマリコンストラクタのすべてのプロパティが等しいとき、2つのインスタンスは等しくなります。`===`演算子は異なり、両方の名前がメモリ上の**同一のオブジェクト**を指しているかどうかを問います。

```kotlin
data class User(val id: Int, val name: String)

val a = User(1, "Ann")
val b = User(1, "Ann")
println(a == b)  // true、同じデータ
println(a === b) // false、2つの異なるオブジェクト
println(a === a) // true
```

`hashCode()`は`equals()`と一緒に生成されるため、データクラスのインスタンスは`Set`の中や`Map`のキーとしても正しく振る舞います：重複は1つにまとめられます。

```kotlin
println(setOf(a, b).size) // 1
```

通常のクラスはこれらを一切生成しないため、`==`は同一性の比較にフォールバックします。

---

生成されるメンバーは**プライマリコンストラクタ**で宣言されたプロパティのみを見ます。クラス**本体**で宣言されたプロパティは通常のプロパティです：`toString()`、`equals()`、`hashCode()`、`copy()`の一部にはなりません。

```kotlin
data class Item(val name: String) {
    var quantity: Int = 0
}

val a = Item("nail")
a.quantity = 5
println(a) // Item(name=nail)
```

これは忘れやすいので、オブジェクトを識別するものはすべてプライマリコンストラクタに置き、派生的な状態や一時的な状態は本体に置くようにしましょう。

---

`sealed`クラスは**閉じた**選択肢の集合を表します：同じパッケージとモジュールに書かれたサブクラスだけが許され、コンパイラはそのすべてを把握します。

```kotlin
sealed class Shape
data class Circle(val radius: Int) : Shape()
data class Square(val side: Int) : Shape()
```

その見返りが**網羅的な`when`**です：sealed型に対して分岐し、すべてのサブクラスを網羅すれば、`else`ブランチを省けます。後で新しいサブクラスを追加すると、コンパイラは黙って`else`にフォールバックする代わりに、更新し忘れたすべての`when`を報告してくれます。

```kotlin
fun name(shape: Shape): String = when (shape) {
    is Circle -> "circle"
    is Square -> "square"
}
```

`is Circle`の後は値がスマートキャストされるため、そのブランチ内では手動のキャストなしで`shape.radius`にアクセスできます。

---

ロガー、レジストリ、アプリケーションの設定など、あるもののインスタンスが**ちょうど1つ**だけ必要なことがあります。`class`を`object`に置き換えると、そのシングルトンを宣言してくれます：

```kotlin
object Registry {
    var size = 0
    fun add() {
        size++
    }
}

Registry.add()
println(Registry.size) // 1
```

インスタンスは最初に触ったときに作成され、名前そのものを使います。`Registry()`のような呼び出しもコンストラクタもありません。`object`はプロパティ、メソッド、`init`ブロックを持つことができ、インターフェースを実装したりクラスを継承したりすることもできます。

---

`companion object`はクラスに属するシングルトンです。定数に加えて、その本来の役割は**ファクトリ関数**を保持することです：ファクトリ関数はインスタンスを作成する前に入力を検証または変換し、入力が意味をなさないときは`null`を返すことができます。

コンストラクタを`private`にすると、すべての呼び出し元はファクトリを経由するようになります：

```kotlin
class Age private constructor(val years: Int) {
    companion object {
        fun of(years: Int): Age? = if (years >= 0) Age(years) else null
    }
}

println(Age.of(30)?.years) // 30
println(Age.of(-1))        // null
```

コンパニオンはクラス名に対して`Age.of(...)`のように呼び出され、クラスの中に存在するためプライベートコンストラクタにアクセスできます。

---

`interface`は型が何をできるかを列挙します。そのメンバーはデフォルトで抽象ですが、インターフェースは**デフォルト実装**も提供できます。デフォルト実装とは、実装するすべてのクラスが無料で継承し、オーバーライドしてもよい本体のことです：

```kotlin
interface Greeter {
    val name: String              // abstract、クラス側で実装する必要がある
    fun greet(): String = "Hi, $name"  // デフォルト実装
}

class Person(override val name: String) : Greeter

class Robot(override val name: String) : Greeter {
    override fun greet(): String = "BEEP $name"
}

println(Person("Ann").greet()) // Hi, Ann
println(Robot("R2").greet())   // BEEP R2
```

インターフェースは状態を保存できない（バッキングフィールドを持たない）ため、抽象プロパティはクラスによって実装されなければならず、通常はコンストラクタで`override val`を使います。クラスとは異なり、型は好きなだけ多くのインターフェースを実装できます。

---

`abstract`クラスはインターフェースと通常のクラスの中間に位置します。インスタンス化はできず、本体を持たずオーバーライドが必須の**抽象**メンバーと、サブクラスがそのまま継承する具象メンバーを混在させられます。

```kotlin
abstract class Vehicle(val name: String) {
    abstract fun wheels(): Int
    fun describe(): String = "$name has ${wheels()} wheels"
}

class Bike(name: String) : Vehicle(name) {
    override fun wheels(): Int = 2
}

println(Bike("BMX").describe()) // BMX has 2 wheels
```

インターフェースと違い、抽象クラスはコンストラクタを持ち、プロパティに状態を保持できます。だからこそサブクラスは`: Vehicle(name)`で`name`を上位に渡します。クラスは1つのクラスしか継承できないので、サブクラスがデータを共有するときは抽象クラスを、振る舞いだけを共有するときはインターフェースを選びましょう。抽象メンバーは`open`を付けなくてもオーバーライドできます。

---

別のクラスの内部で宣言されたクラスは、デフォルトで**ネストクラス**になります。外側のインスタンスについては何も知らず、外側のクラス名から生成します：

```kotlin
class Outer {
    class Nested {
        fun hello() = "hi"
    }
}

println(Outer.Nested().hello()) // hi
```

`inner`キーワードを付けると状況が変わります。`inner`クラスは外側のインスタンスへの参照を持つため外側のプロパティを読むことができ、**インスタンスから**生成します：

```kotlin
class Counter(val step: Int) {
    inner class Doubler {
        fun value() = step * 2
    }
}

println(Counter(5).Doubler().value()) // 10
```

`inner`クラスの内部では`this`は内側のオブジェクトを指します。外側を明示的に指したいときは`this@Counter`を使います。

---

このトピックの要素は組み合わせて使われるのが普通です。各定数が独自のプロパティを持つ`enum class`は固定されたラベルの集合をモデル化し、`data class`はそれに伴うデータを運びます。

```kotlin
enum class Speed(val surcharge: Int) {
    STANDARD(0),
    EXPRESS(15)
}

data class Order(val total: Int, val speed: Speed)

val order = Order(100, Speed.EXPRESS)
println(order.total + order.speed.surcharge) // 115
```
