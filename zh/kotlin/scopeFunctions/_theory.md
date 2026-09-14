**作用域函数**会在*对象的上下文中*运行一段代码块。它们并不为语言添加新功能：只是让针对单个对象操作的代码更简短、更易读。Kotlin 有五个作用域函数：`let`、`run`、`with`、`apply` 和 `also`。

它们只在**两点**上有所不同：在代码块内部如何引用这个对象，以及调用会返回什么。我们从 `let` 开始：在它的代码块内部，对象被称为 `it`，调用返回代码块的**最后一个表达式的结果**。
```kotlin
val word = "kotlin"
val letters = word.let { it.length } // 6
println(letters)
```
如果没有 `let`，你就需要一个临时变量；有了它，只要代码块还在，对象就可以用简短的名字 `it` 来访问。

---

由于 `let` 返回其最后一个表达式的值，它是一种把值**变成别的东西**的便捷方式，而且无需为中间变量命名：
```kotlin
val price = 12
val label = price.let { "$it EUR" }
println(label) // 12 EUR
```
在代码块内部，你可以按需多次使用 `it`：
```kotlin
println("kiwi".let { "${it.uppercase()} has ${it.length} letters" })
// KIWI has 4 letters
```

---

`let` 在安全调用之后才真正大显身手。`?.let { ... }` **只在**值不为 `null` 时才运行代码块，并且代码块内的 `it` 是一个非空值，因此不需要额外的检查：
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to ${it.uppercase()}") }
```
当值为 `null` 时，整个表达式就是 `null`，代码块永远不会运行，因此 Elvis 运算符 `?:` 是提供回退值的天然搭档：
```kotlin
fun label(city: String?): String {
    return city?.let { "City: $it" } ?: "No city"
}
```

---

在 `let` 代码块内，你不必非得把对象叫作 `it`：你可以给 lambda 参数起一个名字，这在代码块嵌套、或者 `it` 说明不了任何有用信息时，能让代码保持可读。
```kotlin
val price: Int? = 12
println(price?.let { amount -> "$amount EUR" }) // 12 EUR
```
同样的命名方式适用于所有使用 `it` 的作用域函数，也就是 `let` 和 `also`。

---

`apply` 同时在两个维度上行进：在它的代码块内，对象是接收者 `this`（因此它的成员可以**不带任何前缀**地使用），而调用返回的是**对象本身**，而不是代码块的结果。

这样的组合让 `apply` 成为**配置**对象的工具，就在你创建它的地方进行：
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
代码块内的 `host` 和 `port` 就是 `this.host` 和 `this.port`；由于 `apply` 会返回配置好的 `Server`，它可以立刻被赋值。

---

`apply` 并不局限于刚创建的对象：它可以作用于任何对象，并且由于它会把对象返回，你可以在任何需要该对象的地方使用整个表达式。
```kotlin
val box = Box()
box.apply { label = "tools" }        // changes box and returns it
println(listOf(Box().apply { label = "nails" }).size) // 1
```
代码块就是一个普通的代码块，因此它可以容纳你需要任意多的语句。

---

`also` 是 `apply` 的镜像：对象以 `it` 的形式被引用，而调用返回**对象本身**。由于代码块的结果会被丢弃，`also` 适用于日志记录或检查这类**副作用**，并且它可以插入到链的中间，而不会改变链最终产生的结果：
```kotlin
val total = listOf(1, 2, 3)
    .also { println("size: ${it.size}") } // size: 3
    .sum()
println(total) // 6
```
可以把它读作*“顺便用它再做这件事”*：值会原封不动地继续流向下一步。

---

当代码块需要把对象作为其他东西的**参数**时，`also` 比 `apply` 更易读：`it` 可以直接传递过去，而 `this` 则不得不明确写出。
```kotlin
val names = mutableListOf<String>()
val user = "ada".also { names.add(it) }
println(user)  // ada
println(names) // [ada]
```
表达式的值仍然是 `"ada"`：`also` 只是看着它经过而已。

---

`run` 就是换了一种对象命名方式的 `let`：在代码块内对象是 `this`，因此它的成员不需要前缀，而调用返回**最后一个表达式的结果**。

它适合这样的场景：你需要读取同一个对象的多个成员来计算出一个值：
```kotlin
class Rect(val w: Int, val h: Int)

val area = Rect(3, 4).run { w * h }
println(area) // 12
```
把它与 `apply` 比较一下：`apply` 以完全相同的方式使用 `this`，但返回的是对象而不是代码块的结果。

---

`with` 做的工作与 `run` 相同，但它**不是**扩展：对象作为第一个参数传入，而不是作为点调用的接收者。
```kotlin
val text = with(StringBuilder()) {
    append("Hello")
    append(", world")
    toString()
}
println(text) // Hello, world
```
在代码块内对象是 `this`，调用返回最后一个表达式，与 `run` 完全一样。当你已经拥有一个非空对象、并想对它进行一组调用时，首选 `with`；当对象来自某个链式调用、或者可能需要安全调用（`obj?.run { ... }`）时，首选 `run`。

---

五个作用域函数现在都已登场，每一个都只是两个维度上的一个点：
- `let` - 对象是 `it`，返回代码块的结果
- `run` - 对象是 `this`，返回代码块的结果
- `with` - 对象是 `this`（作为参数传入），返回代码块的结果
- `apply` - 对象是 `this`，返回对象
- `also` - 对象是 `it`，返回对象

挑选你需要的那一行：当你要把对象继续传给其他东西时，`it` 读起来更顺；当你要访问它的许多成员时，`this` 读起来更顺；当你想要一个新值时，返回代码块的结果；当你想继续使用这个对象时，返回对象本身。
