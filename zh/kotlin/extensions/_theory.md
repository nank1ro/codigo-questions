**扩展函数**可以在不改动源代码的情况下，为已有类型添加一个新函数。
先写 `fun`，然后写想要扩展的类型（**接收者类型**）、一个点，再写函数名：
```kotlin
fun Int.squared(): Int {
    return this * this
}
println(4.squared()) // 16
```
在函数内部，`this` 就是调用该函数的那个值，称为**接收者**：在 `4.squared()` 中它是 `4`。
扩展一旦存在，你就可以用点来调用它，就像它从一开始就是 `Int` 的一部分一样。

---

扩展适用于任何类型，甚至包括你没有源代码的类型。`String` 来自标准库，但你仍然可以给它添加新函数：
```kotlin
fun String.whisper(): String {
    return this.lowercase() + "..."
}
println("HELLO".whisper()) // hello...
```
在扩展内部使用接收者的其他成员时可以省略 `this.`：单独的 `lowercase()` 表示 `this.lowercase()`，单独的 `length` 表示 `this.length`。

---

扩展函数可以像其他函数一样带参数。接收者仍然位于点的左边，参数写在圆括号里：
```kotlin
fun Int.isDivisibleBy(other: Int): Boolean {
    return this % other == 0
}
println(12.isDivisibleBy(4)) // true
println(12.isDivisibleBy(5)) // false
```
点前面的类型就是普通类型，所以你同样可以扩展 `List<Int>`、`Double` 或你自己写的类。

---

扩展**不会**修改它所扩展的类，也不会往类里插入新成员。编译器只是改写了调用：`"kotlin".first3()` 变成对该函数的调用，并把 `"kotlin"` 作为 `this` 传进去。
```kotlin
fun String.first3(): String = take(3)
val word = "kotlin"
println(word.first3()) // kot
```
这就是你能扩展 `String` 和 `Int` 这类 final 类的原因：它们内部什么都没变，扩展只存在于你的代码里。

---

除了函数，你还可以添加**扩展属性**。它用 `val`、接收者类型、一个点和名字来声明，后面跟一个 `get()`，每次读取属性时都会计算出值：
```kotlin
val String.wordCount: Int
    get() = split(" ").size

println("Kotlin is fun".wordCount) // 3
```
扩展属性不能存储任何东西：它没有幕后字段，所以像 `val String.label = "text"` 这样的初始化器是编译错误。它只能根据接收者计算出自己的值。
与扩展函数不同，扩展属性不能声明在函数内部（不允许局部扩展属性）。

---

扩展属性读取时不带圆括号，就像 `String` 内置的 `length` 一样。当这个值是在描述接收者而不是对它做某件事时，扩展属性是自然的选择：
```kotlin
val Int.isNegative: Boolean
    get() = this < 0

println((-3).isNegative) // true
println(7.isNegative)    // false
```
注意 `-3` 外面的括号：没有它们，`-3.isNegative` 会先读取 `3` 的属性，然后试图对一个 `Boolean` 取负，这是无法编译的。

---

接收者类型可以是**可空的**。`String?` 上的扩展可以在可能持有 `null` 的变量上调用，函数内部的 `this` 是 `String?`，所以要由你自己处理 `null` 的情况，通常用你在可空性课程中见过的 Elvis 运算符 `?:`：
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val name: String? = null
println(name.orDash())  // -
println("Ada".orDash()) // Ada
```
在 `null` 值上调用 `name.orDash()` 是安全的：不需要 `?.`，因为函数本身就接受 `null` 接收者。

---

在接收者可空的扩展内部，你还可以用安全调用 `this?.`，只有当值不是 `null` 时才访问它的成员。标准库在 `isNullOrEmpty()` 这类函数中用的是同样的思路：
```kotlin
fun String?.firstOrQuestion(): Char {
    return this?.firstOrNull() ?: '?'
}
val text: String? = null
println(text.firstOrQuestion())    // ?
println("Kotlin".firstOrQuestion()) // K
```

---

当一个类已经有与扩展同名、参数也相同的成员时，**成员总是优先**：扩展永远不会被调用，编译器会警告它被遮蔽了。
```kotlin
class Box {
    fun describe(): String = "member"
}
fun Box.describe(): String = "extension"

println(Box().describe()) // member
```
扩展不能覆盖或替换已有行为；它只能添加新的函数和属性。要想被选中，扩展需要一个类还没有的名字或参数列表。

---

借助**类型参数**，一个扩展可以同时作用于一族类型：类型参数是类型的占位符，写在 `fun` 之后的尖括号里，Kotlin 会在每次调用时填入具体类型。这让扩展变成**泛型的**：
```kotlin
fun <T> List<T>.second(): T {
    return this[1]
}
println(listOf(1, 2, 3).second())      // 2
println(listOf("a", "b").second())     // b
```
对 `listOf(1, 2, 3)` 来说占位符 `T` 是 `Int`，对 `listOf("a", "b")` 来说是 `String`，所以同一个函数每次都返回正确的类型。

---

类型参数可以用在签名的任何位置：作为返回类型、作为可空的 `T?`，或者嵌在另一个类型里。可能什么都找不到的泛型扩展会返回 `T?`，就像内置的 `firstOrNull()`：
```kotlin
fun <T> List<T>.lastOrDefault(default: T): T {
    return if (isEmpty()) default else this[size - 1]
}
println(listOf(1, 2).lastOrDefault(0))          // 2
println(emptyList<String>().lastOrDefault("-")) // -
```
在函数内部，你可以像对任何列表一样使用 `size`、`isEmpty()` 和下标访问，因为接收者就是 `List<T>`。

---

只要类声明了**伴生对象**（哪怕是空的），你也可以扩展它。接收者类型写作 `ClassName.Companion`，然后就能在类名上调用这个扩展，像工厂函数一样：
```kotlin
class Temperature(val degrees: Int) {
    companion object
}
fun Temperature.Companion.freezing(): Temperature = Temperature(0)

println(Temperature.freezing().degrees) // 0
```
类和扩展都是顶层声明，所以必须写在 `main` 之外。

---

伴生对象扩展可以带参数，这使它成为放置替代构造函数的好地方，用来从另一种单位或格式转换：
```kotlin
class Distance(val meters: Int) {
    companion object
}
fun Distance.Companion.fromKilometers(km: Int): Distance = Distance(km * 1000)

println(Distance.fromKilometers(3).meters) // 3000
```

---

你在哪里声明扩展，决定了它能在哪里使用，也就是它的**作用域**：
- 在文件的顶层声明时，它在整个文件以及该包的其余部分都可用
- 在函数内部声明时，它是局部扩展，只能在那个函数里使用
- 在类内部声明时，它是**成员扩展**，只能在那个类里使用

成员扩展可以读取它所在类的属性，因此它结合了两个接收者：类的实例，以及调用它的那个值：
```kotlin
class Greeter(val greeting: String) {
    fun String.greet(): String = "$greeting, $this!"
    fun welcome(name: String): String = name.greet()
}
println(Greeter("Hello").welcome("Ada")) // Hello, Ada!
```
在 `greet` 内部，`greeting` 来自 `Greeter`，而 `this` 是调用该函数的那个 `String`。在类之外，`"Ada".greet()` 是编译错误。

---

恰好带**一个**参数的扩展函数可以标记为 `infix`。中缀函数可以省略点和圆括号来调用，接收者在左、参数在右，读起来几乎像一句话：
```kotlin
infix fun Int.percentOf(total: Int): Int = total * this / 100

println(20 percentOf 50)   // 10
println(20.percentOf(50))  // 10, the normal call still works
```
Kotlin 在一些内置函数上也用了这一点：`1 to "one"` 构造一个 `Pair`，`1 until 5` 构造一个区间。

---

要标记为 `infix`，函数必须是成员或扩展，必须恰好带一个参数，而且这个参数不能有默认值。其他写法都是编译错误：
```kotlin
infix fun Int.add(other: Int): Int = this + other          // ok
infix fun add(a: Int, b: Int): Int = a + b                 // error: not a member or extension
infix fun Int.add(a: Int, b: Int): Int = this + a + b      // error: two parameters
```
中缀调用的优先级介于算术运算和比较运算之间：`1 add 2 * 3` 相当于 `1 add 6`，而 `1 add 2 == 3` 会把结果与 `3` 比较。
