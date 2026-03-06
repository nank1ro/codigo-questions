> 计算机非常适合执行重复性任务。

最基本的重复形式使用 `while` 关键字。
它会在控制的_布尔表达式_为 true 时重复执行一个代码块：

```kotlin
while (Boolean-expression) {
  // Code to be repeated
}
```
布尔表达式在循环开始时求值一次，然后在每次进一步迭代代码块之前再次求值。

```kotlin
var x = 3
while (x > 0) {
    println(x)
    x--
}
```
在这里我们创建了一个变量 `x`，将其初始值赋为 __3__。

然后我们使用了 `while` 语句，它将运行代码块直到条件 `x > 0` 为 `true`。

在代码块内部，我们**不能**遗漏 `x--` 这一行。
它递减 `x` 的值，否则我们的循环将会无限执行。

---

让我们分析这段代码。
```kotlin
var counter = 0 // [1]
while (counter < 100) { // [2]
    counter += 10 // [3]
    println(counter)
}
```
- __[1]__：我们将 `counter` 变量初始化为 __0__。
- __[2]__：_while_ 的条件表达式表示："只要 counter 小于 _100_，就重复执行循环体中的语句"。
- __[3]__：`+=` 运算符将 _10_ 加到 `counter` 上，并在一次操作中将结果赋给 `counter`。

上面代码的输出是 _10_、_20_、_30_、_40_、_50_、_60_、_70_、_80_、_90_、_100_

---

使用 _while_ 还有第二种方式，即与 `do` 关键字结合使用。
```kotlin
do {
  // Code to be repeated
} while (Boolean-expression)
```
如你所见，`do-while` 与 `while` 循环非常相似，但有一个重要区别：
> 循环体在条件求值之前先执行一次。

换句话说，`do-while` 的循环体至少会执行一次，即使条件表达式最初为 `false`。

相反，如果条件第一次就为 `false`，`while` 循环的循环体则永远不会运行。

---

_while_ 循环支持三种结构性跳转表达式：
- `break` 终止最近的外层循环。
- `continue` 跳到最近的外层循环的下一步。
- `return` 默认从最近的外层函数或匿名函数返回（_我们在讨论函数时会详细介绍_）。

以下是在 _while_ 循环中使用 `continue` 的示例：
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) continue // [1]
  println(i)
}
// prints 1, 3
```

如你在 __[1]__ 处所见，当 `i` 等于 _2_ 时，我们跳过并_继续_到下一步。事实上数字 2 从未被打印。

---

以下是在 _while_ 循环中使用 `break` 的示例：
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) break // [1]
  println(i)
}
// prints 1
```

如你在 __[1]__ 处所见，当 `i` 等于 _2_ 时，我们_中断_了循环。事实上数字 2 和 3 从未被打印。
