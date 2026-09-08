**lambda** 是一个没有名字的小函数，直接写成花括号之间的表达式。
参数在前，然后是一个箭头 `->`，接着是函数体：
```kotlin
val add = { a: Int, b: Int -> a + b }
```
lambda 和其他值一样：你可以把它存储在变量中，之后用括号调用它，和调用函数完全一样：
```kotlin
println(add(2, 3)) // 5
```
没有参数的 lambda 完全没有箭头：`val hello = { println("Hello!") }`。

---

每个 lambda 都有一个**函数类型**，写作括号内的参数类型、一个箭头和返回类型。
lambda `{ a: Int, b: Int -> a + b }` 的类型是 `(Int, Int) -> Int`：它接受两个 `Int` 值并返回一个 `Int`。
当你在变量上声明函数类型时，lambda 内部的参数类型可以省略，因为编译器已经知道它们：
```kotlin
val add: (Int, Int) -> Int = { a, b -> a + b }
val greet: (String) -> Unit = { name -> println("Hi, $name") }
```
不返回任何内容的 lambda 的返回类型是 `Unit`。

---

lambda 的函数体可以跨越多行。这里没有 `return` 关键字：**最后一个表达式**的值就是 lambda 返回的内容。
```kotlin
val describe: (Int) -> String = { n ->
    val half = n / 2
    "half of $n is $half" // returned
}
println(describe(10)) // half of 10 is 5
```
因为 `if` 在 Kotlin 中是一个表达式，它可以作为最后一行来决定结果：
```kotlin
val parity: (Int) -> String = { n -> if (n % 2 == 0) "even" else "odd" }
```

---

当 lambda 恰好有**一个**参数时，你可以省略它的声明：Kotlin 会自动把它命名为 `it`。
```kotlin
// val double: (Int) -> Int = { n -> n * 2 }
val double: (Int) -> Int = { it * 2 } // same thing
```
`it` 只在参数没有被显式声明时才存在，并且只适用于单参数的 lambda。
它让简短的 lambda 保持紧凑，但对于较长的函数体，一个真正的名字会更清晰。

---

lambda 最常被用作其他函数的参数。集合提供了许多接受 lambda 的函数：
- `forEach` 对每个元素运行一次 lambda
- `map` 用 lambda 对每个元素的结果构建一个新列表
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map({ it * 2 }) // [2, 4, 6]
```
当 lambda 是**最后一个**参数时，你可以把它移到括号外面；当它是唯一的参数时，括号可以完全省略。这称为**尾随 lambda** 语法，也是通常的写法：
```kotlin
val doubled = numbers.map { it * 2 }
doubled.forEach { println(it) }
```

---

返回 `Boolean` 的 lambda 称为**谓词**。好几个集合函数都接受一个谓词：
- `filter` 只保留谓词为 `true` 的元素
- `count` 返回有多少元素满足它
- `any` 和 `all` 判断是部分还是全部元素满足它
```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)
println(numbers.filter { it % 2 == 0 }) // [2, 4, 6]
println(numbers.count { it > 4 })        // 2
println(numbers.any { it > 5 })          // true
```
调用可以**链接**起来：每个函数都返回一个新列表，供下一个函数处理。
```kotlin
println(numbers.filter { it % 2 == 0 }.map { it * 10 }) // [20, 40, 60]
```

---

lambda 也驱动着排序和聚合：
- `sortedBy` 返回一个新列表，按照 lambda 为每个元素计算出的值排序；`sortedByDescending` 则相反
- `reduce` 把所有元素合并成一个值：lambda 接收到目前为止累积的结果和下一个元素
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })          // [fig, kiwi, banana]
println(words.sortedByDescending { it.length }) // [banana, kiwi, fig]

val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n })   // 10
```
`reduce` 把第一个元素作为 `acc` 起步，然后对每个剩余元素运行 lambda。

---

使用 `reduce` 时，结果的形态由 lambda 决定。任何组合两个值的操作都可以：求和、求积、保留两者中较大的一个。
```kotlin
val numbers = listOf(3, 9, 4)
println(numbers.reduce { acc, n -> if (n > acc) n else acc }) // 9
```
注意 `reduce` 在空列表上会抛出异常，因为没有第一个元素可以作为起点。

---

lambda 可以使用在它周围声明的变量，即使周围代码已经执行完毕。这称为**闭包**：lambda 会*捕获*它需要的变量。
与许多其他语言不同，Kotlin 允许 lambda **修改**捕获到的 `var`：
```kotlin
var clicks = 0
val onClick = { clicks++ }
onClick()
onClick()
println(clicks) // 2
```
每次调用 `onClick` 都会更新同一个 `clicks` 变量，外部代码看到的就是它。

---

由于 lambda 是一个值，函数可以**返回**一个 lambda。返回类型是一个函数类型：
```kotlin
fun multiplier(factor: Int): (Int) -> Int {
    return { it * factor }
}
val triple = multiplier(3)
println(triple(5)) // 15
```
返回的 lambda 捕获了 `factor`，因此每次调用 `multiplier` 都会构建一个不同的函数。
接受或返回其他函数的函数称为**高阶函数**。

---

返回的 lambda 可以捕获函数内部声明的 `var`。这个变量在函数返回之后仍然存活，并且只有 lambda 能访问它：它是私有状态。
```kotlin
fun makeGreeter(): () -> String {
    var calls = 0
    return { calls++; "hello #$calls" }
}
val greeter = makeGreeter()
println(greeter()) // hello #1
println(greeter()) // hello #2
```
每次调用 `makeGreeter()` 都会声明一个全新的 `calls`，因此两个 greeter 各自独立计数。

---

你可以编写自己的高阶函数：函数类型的参数接受任何该形状的 lambda，在函数内部你可以像调用普通函数一样调用它。
```kotlin
fun repeatTwice(text: String, transform: (String) -> String): String {
    return transform(transform(text))
}
println(repeatTwice("a", { it + "!" })) // a!!
println(repeatTwice("a") { it + "!" })  // same, with a trailing lambda
```
把函数参数放在**最后**，正是让调用者能够使用尾随 lambda 语法的关键。

---

当你需要的函数已经存在时，没有必要把它包装进 lambda：**函数引用** `::name` 可以把一个具名函数转换成具有匹配函数类型的值。
```kotlin
fun isEven(n: Int) = n % 2 == 0
val numbers = listOf(1, 2, 3, 4)
println(numbers.filter { isEven(it) }) // [2, 4]
println(numbers.filter(::isEven))      // [2, 4], same thing
```
成员函数通过它们的类型来引用，比如 `String::uppercase`：
```kotlin
println(listOf("a", "b").map(String::uppercase)) // [A, B]
```

---

**匿名函数**是用 `fun` 声明但没有名字的函数。它是创建函数值的另一种方式：
```kotlin
val square = fun(x: Int): Int {
    return x * x
}
println(square(4)) // 16
```
与 lambda 不同，它可以显式声明自己的返回类型，并且使用 `return` 来产生值。
匿名函数和 lambda 可以互换：两者都可以传给 `map`、`filter` 或任何接受函数类型的函数。

---

高阶函数既可以接受函数，也可以返回函数。一个经典的例子是**组合**：构建一个新函数，先运行一个函数，再把它的结果输入另一个函数。
```kotlin
fun andThen(first: (Int) -> Int, second: (Int) -> Int): (Int) -> Int {
    return { n -> second(first(n)) }
}
val addOneThenDouble = andThen({ it + 1 }, { it * 2 })
println(addOneThenDouble(3)) // 8
```
返回的 lambda 同时捕获了 `first` 和 `second`，因此在 `andThen` 返回之后的很长时间里它都能继续工作。

---

有些函数接受**带接收者的 lambda**：在 lambda 内部，`this` 是一个特定的对象，因此你可以直接调用它的成员，而无需写出它的名字。
`buildString` 是一个常见的例子：在它的 lambda 内部，`this` 是一个 `StringBuilder`，因此 `append` 可以像局部函数一样被调用：
```kotlin
val text = buildString {
    append("Hello")
    append(", ")
    append("world")
}
println(text) // Hello, world
```
`buildString` 返回最终的字符串。它是在循环中用 `+` 进行拼接的便捷替代方案。
