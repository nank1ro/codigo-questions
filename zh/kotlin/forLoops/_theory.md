> `for` 关键字对序列中的每个值执行一段代码块。

`for` 循环遍历任何提供迭代器的对象。

`for` 的语法如下：
```kotlin
for (item in collection) print(item)
```

`for` 的主体也可以是一个代码块
```kotlin
for (item in collection) {
    print(item)
}
```

每次循环时，`item` 会被赋予 values 中的下一个元素。

以下是一个重复执行固定次数的 `for` 循环：

```kotlin
for (i in 1..3) {
    println(i)
}
// prints 1, 2, 3
```

输出显示索引 `i` 接收了从 _1_ 到 _3_ 范围内的每个值。

---

_范围_ 是由一对端点定义的值区间。
定义范围有两种基本方式：

```kotlin
var firstRange = 1..3           // [1]
var secondRange = 1 until 3     // [2]
println(firstRange)
println(secondRange)

/* prints
1..3
1..2
*/
```

- __[1]__ 使用 `..` 语法会将两个边界都包含在结果范围中。
- __[2]__ `until` 排除末端。输出显示 _3_ 不在范围内。

---

你可以以相反的顺序遍历范围。

你可能期望 `3..1` 能够工作，但不幸的是，Kotlin 团队决定以不同的方式引入此功能。

实际上，如果你尝试运行以下代码片段：
```kotlin
for (i in 3..1) println(i)
```

你会发现什么也没有打印出来。
要使其正常工作，我们需要使用 `downTo` 关键字：

```kotlin
for (i in 3 downTo 1) println(i)
// prints 3, 2, 1
```

`downTo` 产生一个递减范围。

---

范围的默认 _步长_ 为 __1__，但你可以显式设置其他值。

你可以使用 `step` 关键字来定义 `for` 循环的 __步长__。

```kotlin
for (i in 1..10 step 2) {
    println(i)
}
// prints 1, 3, 5, 7, 9
```

如你所见，代码块以 _2_ 而不是 _1_ 的步长运行，完全改变了我们的输出。

---

你也可以生成一个 _字符_ 范围。
```kotlin
for (char in 'a'..'z') print(char)
// prints abcdefghijklmnopqrstuvwxyz
```

---

你可以遍历一个 __String__。
```kotlin
for (char in 'abc') print(char + 1)
// prints bdc
```

在上面的示例中，我们打印了每个字符 + 1，所以 `'a'` 变成了 `'b'`，`'b'` 变成了 `'c'`，以此类推。

这是因为字符以对应其 [ASCII 码](https://en.wikipedia.org/wiki/ASCII) 的数字形式存储。

因此，将整数加到字符上会产生一个对应新码值的新字符。

---

如果你只需要重复执行一段代码 `n` 次，可以使用 `repeat(times: Int)` 函数。

```kotlin
repeat(3) {
    println("repeat")
}
// prints repeat 3 times
```

你甚至可以通过以下方式访问索引
```kotlin
repeat(3) { index ->
    println(index)
}
// prints 0, 1, 2
```

---

在 Kotlin 中，我们也可以使用 `for-in` 来遍历可迭代集合，对每个元素调用给定的闭包：
```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(2, 4, 6, 8, 10)
for (num in numbers) {
    println(num)
}
// prints (2, 4, 6, 8, 10)
```

---

在 Kotlin 中，我们还有 `forEach` 循环。
它按照与 `for-in` 循环相同的顺序，对序列中的每个元素调用给定的闭包：

```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(1, 3, 5, 7, 9)
numbers.forEach {
    println(it)
}
```

使用 `forEach` 方法与 `for-in` 循环在两个重要方面有所不同：
1. 不能使用 `break` 或 `continue` 语句来退出主体闭包的当前调用或跳过后续调用。（_实际上可以通过注解实现，但这是一个更复杂的话题，我们暂时不讨论。_）
2. 在主体闭包中使用 `return` 语句只会退出闭包而不是外部作用域，并且不会跳过后续调用。
