Kotlin 中的每个值都有一个**类型**，它告诉编译器这是什么样的数据，以及你可以对它做什么。
基本类型有：
- `Int`：整数，例如 `42` 或 `-7`
- `Long`：可以比 `Int` 大得多的整数
- `Double`：带小数部分的数字，例如 `3.14`
- `Float`：占用内存只有 `Double` 一半的小数，但精度较低
- `Char`：单引号中的单个字符，例如 `'a'`
- `Boolean`：`true` 或 `false`
- `String`：双引号中的一段文本，例如 `"Hello"`

正如你在变量课程中所看到的，你可以在名称后面用冒号显式声明类型：
```kotlin
val age: Int = 36
val name: String = "Ada"
```
一种类型的值不能存储在另一种类型的变量中：`val age: Int = "36"` 是一个编译错误。

---

大多数时候你不需要写类型：Kotlin 会根据你赋的值**推断**它，遵循几条字面量规则：
- 一个整数，例如 `42`，是 `Int`
- 带小数点的数字，例如 `3.14`，是 `Double`
- 双引号中的文本是 `String`
- 单引号中的字符是 `Char`
- `true` 和 `false` 是 `Boolean`
```kotlin
val count = 42     // Int
val price = 9.99   // Double
val name = "Ada"   // String
val grade = 'A'    // Char
val isOpen = true  // Boolean
```
要查看 Kotlin 推断出的类型，你可以用 `::class.simpleName` 打印任何值的类型名称：
```kotlin
println(count::class.simpleName) // Int
println(price::class.simpleName) // Double
```
十进制字面量永远不会被推断为 `Float`：`val ratio = 0.5` 是一个 `Double`。

---

`Int` 可以存储最大约二十亿的整数，更准确地说最大到 `Int.MAX_VALUE`，即 `2147483647`。
对于 `Int` 来说太大的整数字面量会自动被推断为 `Long`，你也可以用后缀 `L` 强制任何字面量为 `Long`：
```kotlin
val big = 3000000000  // Long, too big for an Int
val small = 3L        // Long, thanks to the suffix
```
同样地，后缀 `f` 把十进制字面量变成 `Float`：`val ratio = 0.5f`。
很长的数字难以阅读，因此 Kotlin 允许你在数字之间的任意位置放置下划线 `_`；编译器会忽略它们：
```kotlin
val population = 8_000_000_000L
val million = 1_000_000
println(million) // 1000000
```

---

赋值时 Kotlin 从不自动在数字类型之间转换，即使是从较小的类型到较大的类型也不行：把 `Int` 存入 `Long` 或 `Double` 变量是一个编译错误。
```kotlin
val count = 3
val total: Long = count      // error: Int is not a Long
val price: Double = count    // error: Int is not a Double
```
每个数字类型都有**转换函数**，用于构建一个你所需要类型的新值：`toInt()`、`toLong()`、`toDouble()`、`toFloat()`，以及获取文本的 `toString()`。
```kotlin
val total: Long = count.toLong()
val price: Double = count.toDouble() // 3.0
println(count.toString() + "!")      // 3!
```
从小数转换为整数会**截断**：`toInt()` 只是丢弃小数部分，因此 `3.99.toInt()` 是 `3`，而 `(-3.99).toInt()` 是 `-3`。

---

操作数的类型决定除法的运算方式。当两者都是 `Int` 时，`/` 运算符执行**整数除法**：结果是一个 `Int`，余数被丢弃。
当至少一个操作数是 `Double` 时，`/` 执行浮点除法并保留小数部分：
```kotlin
println(7 / 2)              // 3
println(7.0 / 2)            // 3.5
val slices = 7
println(slices.toDouble() / 2) // 3.5
```
因此，要从两个 `Int` 变量得到小数结果，你必须在相除**之前**转换其中至少一个：`(7 / 2).toDouble()` 是 `3.0`，因为整数除法已经发生了。

---

当函数必须返回由整数计算得出的小数结果时，在相除之前把操作数转换为 `Double`，并把返回类型声明为 `Double`：
```kotlin
fun ratio(part: Int, total: Int): Double {
    return part.toDouble() / total
}
println(ratio(1, 4)) // 0.25
```
记住 `List<Int>` 的 `sum()` 和 `size` 也是 `Int` 值，所以它们需要同样的转换。

---

每个 `Char` 都以数字形式存储，即它的**码**。`code` 属性给出字符背后的 `Int`，而 `toChar()` 做相反的事，把一个 `Int` 变成具有该码的 `Char`：
```kotlin
println('A'.code)        // 65
println(66.toChar())     // B
println(('A'.code + 2).toChar()) // C
```
字母的码是连续的，因此对码做加法就能沿着字母表移动。
注意 `'7'` 的码是 `55`，而不是 `7`：要读取 `Char` 所表示的数字，请使用 `digitToInt()`，它会返回 `7`。

---

由于 `Char` 的码是一个 `Int`，你可以对它做算术运算，再把结果转换回 `Char`。这就是你沿着字母表移动的方式：
```kotlin
val next = ('a'.code + 1).toChar() // 'b'
```
Kotlin 还允许你把 `Int` 直接加到 `Char` 上：`'a' + 1` 是 `'b'`，而两个字符之间的差 `'d' - 'a'` 是 `Int` 值 `3`。

---

用户输入的文本总是以 `String` 的形式到达，即使它看起来像数字。要对它做数学运算，你必须**解析**它：`toInt()` 把 `"42"` 变成 `Int` 值 `42`，而 `toDouble()` 把 `"3.5"` 变成 `Double` 值 `3.5`。
```kotlin
val typed = "42"
println(typed.toInt() + 1) // 43
```
并非所有文本都是数字：`"4x2".toInt()` 会抛出 `NumberFormatException` 并使程序停止。
安全的替代方法 `toIntOrNull()` 和 `toDoubleOrNull()` 返回 `null` 而不是抛出异常，因此，正如你在可空性课程中学到的，你可以用 `?:` 提供一个默认值：
```kotlin
println("4x2".toIntOrNull())      // null
println("4x2".toIntOrNull() ?: 0) // 0
```

---

只有当整段文本是带可选符号的有效整数时，`toIntOrNull()` 才会成功：
```kotlin
println("42".toIntOrNull())   // 42
println("-7".toIntOrNull())   // -7
println("3.5".toIntOrNull())  // null, not a whole number
println(" 42".toIntOrNull())  // null, spaces are not allowed
println("abc".toIntOrNull())  // null
```
对于小数文本，请使用 `toDoubleOrNull()`，它以同样的方式接受 `"3.5"` 并返回一个 `Double?`。

---

`Int` 的大小是固定的，因此它有最小值和最大值：`Int.MIN_VALUE` 是 `-2147483648`，`Int.MAX_VALUE` 是 `2147483647`。
超过限制**不会**引发错误：值会悄悄地**回绕**到范围的另一端，这种行为称为溢出。
```kotlin
println(Int.MAX_VALUE)     // 2147483647
println(Int.MAX_VALUE + 1) // -2147483648
```
当结果可能超过二十亿时，请使用 `Long`，它的上限 `Long.MAX_VALUE` 约为九十二亿亿。记住要在运算之前转换：`Int.MAX_VALUE.toLong() + 1` 是 `2147483648`。

---

`Double` 以二进制存储小数，因此有些值无法被精确表示，最后的数位会出现微小的误差：
```kotlin
println(0.1 + 0.2) // 0.30000000000000004
```
要显示固定数量的小数位，请使用带格式字符串的 `String.format`：`"%.2f"` 表示“小数点后有 2 位数字的小数”。结果是一个 `String`，并四舍五入到相应的位数：
```kotlin
println(String.format("%.2f", 0.1 + 0.2)) // 0.30
println(String.format("%.1f", 3.14159))   // 3.1
println(String.format("%.2f", 2.0))       // 2.00
```

---

`Any` 是位于层次结构顶端的类型：每个 Kotlin 值都是 `Any`，因此 `Any` 类型的变量可以持有 `Int`、`String`、`Boolean` 或任何其他东西。
要弄清它实际持有什么，你可以使用 `is` 运算符，当值具有该类型时它会返回 `true`：
```kotlin
val value: Any = 42
println(value is Int)    // true
println(value is String) // false
```
一旦检查通过，编译器会对该值进行**智能转换**：在 `if`（或 `when` 分支）内部，你可以把它当作该类型使用，无需任何转换：
```kotlin
if (value is Int) println(value + 1) // 43, value is an Int here
when (value) {
    is String -> println(value.length)
    is Boolean -> println(!value)
}
```
