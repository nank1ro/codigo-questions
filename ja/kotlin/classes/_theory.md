**クラス**はオブジェクトを作成するための設計図です。Kotlinでは、`class`キーワードの後にクラス名を付けてクラスを宣言します。

クラスは**プロパティ**（データ）と**メソッド**（振る舞い）を持つことができます。コンストラクタで直接プロパティを宣言するには、`val`または`var`プレフィックスを付けます：

```kotlin
class Dog(val name: String)
```

これにより`name`プロパティを持つ`Dog`クラスが作成されます。クラスを関数のように呼び出してインスタンスを作成します：

```kotlin
val dog = Dog("Rex")
println(dog.name) // Rex
```

---

クラスは**プライマリコンストラクタ**に複数のプロパティを持つことができます。各プロパティはコンストラクタのパラメータリストに`val`（読み取り専用）または`var`（可変）で直接宣言します：

```kotlin
class Person(val name: String, var age: Int)
```

`val`キーワードは作成後に`name`を読み取り専用にし、`var`は`age`を可変にします — 後で変更できます：

```kotlin
val p = Person("Alice", 30)
p.age = 31  // ageはvarなので許可される
```

---

**`init`ブロック**はプライマリコンストラクタの直後に実行されます。オブジェクト作成時にバリデーションやセットアップロジックを実行するために使用します：

```kotlin
class Circle(val radius: Double) {
    init {
        require(radius > 0) { "半径は正でなければなりません" }
    }
}
```

`init`の中で追加のプロパティを初期化することもできます：

```kotlin
class Square(val side: Int) {
    val area: Int
    init {
        area = side * side
    }
}
```

---

クラスには**メソッド**を含めることができます — クラスに属し、そのプロパティを操作する関数です：

```kotlin
class Counter(var count: Int) {
    fun increment() {
        count++
    }
    fun value(): Int {
        return count
    }
}
```

メソッドはインスタンスにドット記法を使って呼び出します：

```kotlin
val c = Counter(0)
c.increment()
println(c.value()) // 1
```

---

**`data class`**はデータを保持するために設計された特別なクラスです。Kotlinは`equals()`、`hashCode()`、`toString()`、`copy()`を自動的に生成します：

```kotlin
data class Point(val x: Int, val y: Int)

val p = Point(1, 2)
println(p)           // Point(x=1, y=2)
println(p.toString()) // Point(x=1, y=2)
```

`copy()`関数は一部のプロパティを変更した新しいインスタンスを作成します：

```kotlin
val p2 = p.copy(y = 10)
println(p2) // Point(x=1, y=10)
```
