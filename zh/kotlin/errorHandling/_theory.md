**异常**（exception）是 Kotlin 报告一条语句无法执行的方式。把 `"abc"` 转换为数字、用整数除以零，或者读取超出列表末尾的位置，都会抛出一个异常。

```kotlin
fun main() {
    println("before")
    val n = "abc".toInt()
    println("after")
}
```
这个程序先打印 `before`，然后就停止了。`toInt()` 无法读取 `"abc"`，于是它**抛出**（throws）一个 `NumberFormatException`；程序中没有任何代码处理它，所以 Kotlin 以一份错误报告结束程序，`after` 永远不会被打印。

你也可以用 `throw` 关键字自己抛出一个异常：
```kotlin
throw Exception("something went wrong")
```

没有人处理的异常不是一个警告：它就是本次运行的终点。

---

为了让程序保持运行，把有风险的语句放进 `try` 块中，并在 `catch` 块中描述恢复方式：
```kotlin
try {
    println("abc".toInt())
} catch (e: Exception) {
    println("cannot read that number")
}
println("still running")
```
Kotlin 先运行 `try` 块；一旦其中某条语句抛出异常，块中剩余的部分就会被跳过，控制权跳转到 `catch` 块。括号里的名字——这里是 `e`——是异常对象，而 `Exception` 是被捕获的类型。

`catch` 块结束后，程序从整个 `try`/`catch` 之后的下一行正常继续。

---

捕获 `Exception` 会捕获所有异常，这很少是你想要的结果：块中其他地方的拼写错误也会被一起吞掉。相反，应写明你知道如何恢复的**确切类型**。

每种失败都有自己的类型。`"abc".toInt()` 抛出的是 `NumberFormatException`，所以要捕获的就是它：
```kotlin
try {
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("that is not a number")
}
```
如果块中抛出的是另一种异常，这个 `catch` 就不会匹配，异常会继续向函数外传播。

---

一个 `try` 后面可以跟多个 `catch` 块，每个块处理一种不同的类型：
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
Kotlin 会**自上而下**逐个尝试这些块，并运行第一个类型匹配的块。永远只有一个块会运行。

因此顺序很重要。`NumberFormatException` 和 `IndexOutOfBoundsException` 都是 `Exception` 的一种，所以写在最前面的 `catch (e: Exception)` 会匹配每一种失败，位于它下面的块将永远不会运行。把最具体的类型写在最前面，把最通用的写在最后。

---

可以在最后添加一个 `finally` 块。**无论发生什么**它都会运行：`try` 成功之后、`catch` 完成恢复之后，甚至在异常完全没有被捕获时也是如此。

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
这使它成为放置绝不能被跳过的清理工作的位置，比如关闭一个文件。一个 `try` 至少需要有一个 `catch` 或一个 `finally`，但也可以两者都有。

---

在 Kotlin 中 `try` 不只是一条语句：它是一个会产生值的**表达式**。这个值就是所运行块中的最后一个表达式——没有失败时是 `try` 块的值，失败了则是 `catch` 块的值。

```kotlin
val n = try { "abc".toInt() } catch (e: NumberFormatException) { 0 }
println(n) // 0
```
这是 Kotlin 中地道的写法。你不必声明一个 `var`、在两处给它赋值并寄希望于每条路径都会赋值，而是得到一个始终持有可用值的 `val`。

注意，`finally` 块永远不会改变这个值：它只为副作用而运行。

---

由于 `try` 是一个表达式，它可以用在任何需要值的地方——包括作为用 `=` 编写的整个函数体：
```kotlin
fun length(text: String): Int = try {
    text.toInt()
} catch (e: NumberFormatException) {
    -1
}
```
两个块必须产生相同类型的值，这里是 `Int`。把回退值写成 `catch` 块的最后一个表达式；两个块中都没有 `return`。

---

抛出和捕获异常并非没有开销，对于常见的转换，Kotlin 提供了一种更省事的变体：它们不抛出异常，而是直接返回 `null`：`toIntOrNull()`、`toDoubleOrNull()`、`toLongOrNull()`。

```kotlin
println("42".toIntOrNull())  // 42
println("abc".toIntOrNull()) // null
```
结合 elvis 运算符 `?:`——当它左边的值为 `null` 时提供一个替代值——整个 `try`/`catch` 可以压缩成一行：
```kotlin
val n = "abc".toIntOrNull() ?: 0
println(n) // 0
```
当失败确实属于例外情况时使用 `try`/`catch`；当预料到会出现非法输入时使用 `toIntOrNull()`。

---

你自己的函数可以像标准库一样用 `throw` 拒绝非法输入。标准库已经为最常见的情况提供了一个类型：`IllegalArgumentException` 的意思是“你传给我的值不可接受”。

```kotlin
fun half(n: Int): Int {
    if (n < 0) throw IllegalArgumentException("n must not be negative")
    return n / 2
}
```
`throw` 会立即结束函数——它下面的 `return` 永远不会被执行到。由调用者决定如何处理：
```kotlin
try { println(half(-4)) }
catch (e: IllegalArgumentException) { println("rejected") }
```
抛出异常比悄悄返回一个编造的值更好：错误的答案会传播得很远，而异常会在第一个准备好处理它的调用者那里停下来。

---

每个异常都携带着创建它时传入的文本。在 `catch` 块中，你可以通过异常对象的 `message` 属性读取它：
```kotlin
try {
    throw IllegalArgumentException("price must be positive")
} catch (e: IllegalArgumentException) {
    println(e.message) // price must be positive
}
```
`message` 是可空的，因为异常可以在没有任何文本的情况下构建；当你需要一个普通的 `String` 时，`e.message ?: "unknown"` 提供了一个安全的替代值。

比起打印异常对象本身，更推荐打印 `e.message`：对象自带的文本还包含类名，对阅读输出的人来说是干扰信息。

---

在每个参数上都写 `if (...) throw IllegalArgumentException(...)` 会很啰嗦，所以 Kotlin 提供了两个读起来像普通句子的简写：

```kotlin
require(n >= 0) { "n must not be negative" }   // 抛出 IllegalArgumentException
check(started) { "not started" }               // 抛出 IllegalStateException
```
两者都接受一个条件和一段生成消息的块，并且都在**条件为 false 时**抛出异常。唯一的区别是异常类型，而这个区别本身就是给读者的提示：

* `require` 守卫调用者传入的**参数**，失败时抛出 `IllegalArgumentException`。
* `check` 守卫对象或程序的**状态**，失败时抛出 `IllegalStateException`。

这个块只有在检查失败时才会被求值，所以在正常路径上构建消息没有任何开销。

---

当内置类型都不能很好地描述你的失败时，就自己声明一个。异常是一个普通的类，它继承 `Exception` 并把自己的文本交给父类：

```kotlin
class InsufficientFundsException(message: String) : Exception(message)
```
这一行代码就是一个完整的异常类型。它和其他异常一样被抛出和捕获，`e.message` 返回构建它时传入的文本：
```kotlin
try {
    throw InsufficientFundsException("balance too low")
} catch (e: InsufficientFundsException) {
    println(e.message) // balance too low
}
```
好处在于精确：调用者可以只捕获 `InsufficientFundsException`，而让其他所有失败继续传播。

---

`runCatching` 会运行一个代码块，并且绝不让异常逃出去。作为替代，它返回一个 `Result`——一个**要么**持有代码块产生的值、**要么**持有它抛出的异常的对象：

```kotlin
val ok = runCatching { "42".toInt() }
val bad = runCatching { "abc".toInt() }

println(ok.isSuccess)   // true
println(bad.isFailure)  // true
```
值可以在之后读出，由你来决定失败应当变成什么：
```kotlin
println(ok.getOrNull())      // 42
println(bad.getOrNull())     // null
println(bad.getOrElse { 0 }) // 0
```
`getOrNull()` 把失败变成 `null`，而 `getOrElse { ... }` 会运行代码块来构建替代值。调用处不会抛出任何东西，因此失败可以被带着到处传递，之后再处理。
