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
println(a == b)  // true, same data
println(a === b) // false, two different objects
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
