有时一个值就是缺失的：没有中间名的用户、没有找到任何结果的搜索、无法转换成数字的文本。
Kotlin 用 `null` 表示缺失的值，但普通变量永远不能持有它。每个类型默认都是**非空**的：
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
要允许值缺失，你可以在类型后面加上问号 `?` 来声明一个**可空**类型。
`String?` 既可以持有 `String`，也可以持有 `null`：
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String` 和 `String?` 是两个不同的类型：`String` 永远不会缺失，`String?` 则可能会。

---

`String` 和 `String?` 之间的区别是由**编译器**检查的，而不是在运行时。
把 `null` 赋给非空类型，或者在需要非空值的地方传入可空值，都是编译错误，因此程序根本不会启动：
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
这正是 Kotlin 避免其他语言中常见“空指针”崩溃的方式：值只可能在你用 `?` 显式声明的地方缺失。

---

`?` 可以写在任何出现类型的地方：函数既可以接受可空参数，也可以返回可空值。
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
你不能直接在可空值上调用方法，因为它可能是 `null`。
**安全调用**运算符 `?.` 只在值不为 `null` 时才调用该方法；否则整个表达式的结果就是 `null`：
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
安全调用的结果总是可空的：`word?.length` 是 `Int?`，而不是 `Int`。

---

很多时候，你想从一个可空值中得到的不过是值本身或者一个默认值。
**Elvis 运算符** `?:` 正好做到这一点：当左侧不为 `null` 时它返回左侧，否则返回右侧的值：
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
由于右侧只在左侧为 `null` 时才被使用，所以当默认值非空时，结果也是非空的。
`?:` 与 `?.` 配合得很好，可以把安全调用变回一个普通值：
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

安全调用可以**链接**起来：只要其中一个环节是 `null`，链中剩余的部分就会被跳过，整个表达式就变成 `null`。
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
以 `?:` 结尾的链可以在一行内给你一个非空的结果：
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

安全调用链在处理嵌套对象时大放异彩，因为任何一层都可能缺失：
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
每个 `?.` 都保护下一步，最后的 `?:` 提供默认值。

---

**非空断言**运算符 `!!` 把可空值转换成非空值，等于告诉编译器“我确信这不是 `null`”：
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
如果你判断错了，值确实是 `null`，程序就会在运行时抛出 `NullPointerException` 而崩溃——这正是 Kotlin 旨在防止的错误：
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
只应在值确实不可能为 `null` 时使用 `!!`；在其他所有情况下，优先使用 `?.`、`?:` 和 null 检查。

---

当你用 `if` 检查一个值是否为 `null` 时，编译器会记住这一点：在值已知为非空的分支内，它会被**智能转换**为非空类型，你可以直接使用它，而不需要 `?.` 或 `!!`：
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
在提前返回之后也会发生同样的事情：
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
智能转换适用于 `val` 变量和函数参数，因为它们的值在检查和使用之间不会改变。

---

`let` 会用它被调用的那个值来运行一段代码块，在代码块内部该值以 `it` 的形式可用。
与安全调用结合后，`?.let` **只**在值不为 `null` 时才运行代码块，并且在代码块内部 `it` 是非空的：
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
当你只需要在代码块内部使用该值时，它是 `if (x != null) { ... }` 的一种简洁替代方式。

---

`let` 还会**返回**其代码块中最后一个表达式的值，因此 `?.let` 可以转换一个可空值，而 `?:` 可以在它为 `null` 时填入默认值：
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
当 `price` 为 `null` 时，`let` 代码块被跳过，表达式为 `null`，Elvis 运算符返回 `"free"`。

---

集合也可以持有可空元素：`List<Int?>` 可以包含 `null` 条目，而 `List<Int>` 永远不会。
`filterNotNull()` 返回一个移除了 `null` 条目的新列表，并且它的元素类型变为非空，因此你可以放心地使用这些元素：
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

许多标准函数会返回 `null` 而不是失败。`toIntOrNull()` 把字符串转换为 `Int`，当文本不是整数时返回 `null`：
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
`mapNotNull` 像 `map` 一样转换每个元素，但会丢弃结果为 `null` 的元素：
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

有时一个属性在对象创建时无法被赋值，但你知道它会在被使用之前被设置。
与其把它声明为可空，不如用 `lateinit` 标记它：类型保持非空，读取它时也不需要 `?.`：
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
`lateinit` 有一些规则：它只能用于 `var` 属性，只能配合非空类型使用，并且不能用于 `Int` 或 `Boolean` 这样的基本类型。
在赋值之前读取 `lateinit` 属性会抛出 `UninitializedPropertyAccessException`；你可以先用 `::player.isInitialized` 检查它。

---

当 `null` 意味着调用方犯了错误时，应该用 `requireNotNull` 尽早失败。
当值存在时，它以非空形式返回该值；当值为 `null` 时，它抛出一个 `IllegalArgumentException`，并可以附带一条消息：
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
调用之后，编译器还会把 `name` 本身智能转换为 `String`，因此从那一行起可以使用 `name.length`。
与 `!!` 不同，这种失败带有清晰的消息，并指明是*参数*错了。

---

扩展函数可以声明在**可空接收者**上，因此它甚至可以在 `null` 值上被调用。在函数内部，`this` 是可空的，必须进行检查：
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
注意，调用处不需要任何 `?.`：由函数本身处理 `null` 的情况。
标准库在 `isNullOrEmpty()` 和 `orEmpty()` 中就使用了这个技巧，它们可以安全地调用在任何 `String?` 上。

---

`?:` 的右侧可以是任何表达式，包括 `return`。这提供了一种在值缺失时立即退出函数的简洁方式：
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
你见过的所有工具都能很好地组合：可空参数和可空返回类型描述了值*可能在哪里*缺失，而 `?.`、`?:`、`let`、智能转换和 `toIntOrNull` 则可以处理它而不会崩溃。
