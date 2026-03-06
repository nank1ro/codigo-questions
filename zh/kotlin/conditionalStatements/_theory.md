当我们想要仅在满足某个条件时执行代码时，就需要进行决策判断。
假设我们只想在天气好的时候去外面玩。
在编程中，我们可以保存一个布尔变量 `niceWeather`，并在该变量为 `true` 时执行去外面玩的操作，如下所示：
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```

---

让我们继续上一个例子。
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```
我们已经看到 `if` 语句只在条件为 `true` 时执行代码块。
另一个需要注意的重要事项是**花括号** `{}`，它们表示一个代码块。

---

我们刚刚学习了如何在条件满足时执行一段代码块，现在让我们来看看如何在第一个条件不满足时执行另一段代码块。
如果天气好，我们就去外面玩；否则，我们就待在家里。
在 Kotlin 中，我们可以使用 `else` 语句，如下所示：
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

假设我们还有另一个条件需要检查，如以下示例所示：
```kotlin
var num = 3
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else {
    println("do something else")
}
```
这段代码的输出是 `the number is 3`。
首先，我们检查数字是否等于 2，结果为 false。
然后我们继续检查第二个语句，看 `num` 是否等于 3，结果为 true，所以我们执行接下来的代码块，打印 `the number is 3`

---

我们可以添加任意多个 `else if` 语句，没有限制
```kotlin
var num = 4
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else if (num == 4) {
    println("the number is 4")
} else if (num == 5) {
    println("the number is 5")
} else if (num == 6) {
    println("the number is 6")
}
```
这段代码的输出是 `the number is 4`。

---

我们还可以在一个条件语句（`if`、`else if` 或 `else`）中嵌套另一个条件语句，以创建更复杂的结构。
```kotlin
var num = 4
if (num < 3) {
    println("the number is lower than 3")
} else {
    if (num == 3) {
        println("the number is 3")
    } else if (num == 4) {
        println("the number is 4")
    } else {
        println("the number is greather than 4")
    }
}
```
这段代码的输出是 `the number is 4`。

---

_Elvis 运算符_ `a ?: b` 如果可选值 `a` 包含值，则将其解包；如果 `a` 为 `null`，则返回默认值 `b`。
表达式 `a` 始终是可选类型。
表达式 `b` 必须与 `a` 中存储的类型匹配。
Elvis 运算符是以下代码的简写形式：
```kotlin
if (a != null) a else b
```
