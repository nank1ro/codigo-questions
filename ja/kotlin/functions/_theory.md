関数とは、特定のタスクを実行し、プログラム全体で再利用できるコードのブロックです。
Kotlinでは、`fun` キーワードに続けて関数名と括弧を使って関数を定義します:
```kotlin
fun greet() {
    println("Hello!")
}
```
関数を呼び出す（実行する）には、名前の後に括弧を付けます:
```kotlin
greet() // prints Hello!
```
値を返さない関数は暗黙的に `Unit` を返します。

---

関数は値を返すことができます。括弧の後にコロンを使って戻り値の型を指定します:
```kotlin
fun getNumber(): Int {
    return 42
}
```
`return` キーワードは呼び出し元に値を返します:
```kotlin
var result = getNumber()
println(result) // prints 42
```
戻り値の型は返す値の型と一致しなければなりません。

---

関数はパラメータを受け取ることができます。パラメータとは、関数を呼び出すときに渡す入力値です。
パラメータは括弧の中に名前と型で宣言します:
```kotlin
fun greet(name: String) {
    println("Hello, $name!")
}
```
関数を呼び出すときに引数を渡します:
```kotlin
greet("Alice") // prints Hello, Alice!
```
パラメータを使うと、異なる値に対して動作する再利用可能なコードを書くことができます。

---

Kotlinはデフォルトパラメータ値をサポートしています。呼び出し元が引数を渡さない場合、デフォルト値が使用されます:
```kotlin
fun greet(name: String = "World") {
    println("Hello, $name!")
}
greet()         // prints Hello, World!
greet("Alice")  // prints Hello, Alice!
```
デフォルト値によりパラメータをオプションにできるため、オーバーロードされた関数の必要性が減ります。

---

関数の本体が単一の式で構成される場合、`=` を使った単一式構文を使用できます:
```kotlin
fun square(n: Int): Int = n * n
```
これはブロック本体の形式よりも簡潔です。Kotlinは戻り値の型を推論できることが多いため、次のように書くこともできます:
```kotlin
fun square(n: Int) = n * n
```
単一式関数は単純な計算に対してよく使われるKotlinのイディオムです。

---

関数は `Boolean` 値を返すことができます。これは条件を確認するのに便利です:
```kotlin
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
println(isEven(4)) // prints true
println(isEven(7)) // prints false
```
`Boolean` 関数は `true` または `false` を返します。

---

関数は異なる型の複数のパラメータを持つことができます:
```kotlin
fun introduce(name: String, age: Int): String {
    return "My name is $name and I am $age years old."
}
println(introduce("Bob", 30))
// prints My name is Bob and I am 30 years old.
```
名前付き引数を使うと、パラメータ名を使って任意の順序で値を渡すことができます:
```kotlin
println(introduce(age = 30, name = "Bob"))
```

---

Kotlinの基本的な関数は、`fun` キーワードの後に名前と括弧を使います:
```kotlin
fun sayBye() {
    println("Bye!")
}
```

---

関数の戻り値の型を宣言するには、括弧の後にコロンと型を追加します:
```kotlin
fun getName(): String {
    return "Alice"
}
```

---

関数のパラメータは名前、コロン、型で宣言します:
```kotlin
fun greet(name: String) {
    println("Hi, $name!")
}
```

---

単一式関数はブロック本体の代わりに `=` を使います:
```kotlin
fun triple(n: Int) = n * 3
```
これは以下の省略形です:
```kotlin
fun triple(n: Int): Int {
    return n * 3
}
```
