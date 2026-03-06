当我们希望仅在满足特定条件时才执行代码时，就需要进行决策判断。
假设我们只想在天气好的时候去外面玩。
在编程中，我们可以保存一个布尔变量 `niceWeather`，并在该变量为 `true` 时执行去外面玩的操作，如下所示：
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```

---

让我们继续前面的例子。
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```
我们已经看到 `if` 语句只在条件为 `true` 时才执行代码块。
另一个需要注意的重要事项是**花括号** `{}`，它们表示一个代码块。

---

我们刚刚学习了如何在满足条件时执行代码块，现在让我们看看如何在第一个条件不满足时执行另一个代码块。
如果天气好，我们去外面玩；否则，我们待在家里。
在 Swift 中，我们可以使用 `else` 语句，如下所示：
```swift
var niceWeather = true
if niceWeather {
    // play outside
} else {
    // stay home
}
```

---

假设我们还有另一个条件需要检查，如以下示例所示：
```swift
var num = 3
if num == 2 {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else {
    print("do something else")
}
```
这段代码的输出是 `the number is 3`。
首先，检查数字是否等于 2，结果为 false。
然后继续检查第二个语句，判断 `num` 是否等于 3，结果为 true，因此执行后面的代码块，打印 `the number is 3`

---

我们可以添加任意多个 `else if` 语句，没有数量限制
```swift
var num = 4
if (num == 2) {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else if (num == 4) {
    print("the number is 4")
} else if (num == 5) {
    print("the number is 5")
} else if (num == 6) {
    print("the number is 6")
}
```
这段代码的输出是 `the number is 4`。

---

我们还可以在一个条件语句（`if`、`else if` 或 `else`）中嵌套另一个条件语句，以创建更复杂的结构。
```swift
var num = 4
if num < 3 {
    print("the number is lower than 3")
} else {
    if num == 3 {
        print("the number is 3")
    } else if num == 4 {
        print("the number is 4")
    } else {
        print("the number is greather than 4")
    }
}
```
这段代码的输出是 `the number is 4`。

---

三元条件运算符是一种特殊的运算符，由三部分组成，形式为 `question ? answer1 : answer2`。
它是根据 `question` 是 true 还是 false 来计算两个表达式之一的快捷方式。
如果 `question` 为 true，则计算 `answer1` 并返回其值；否则，计算 `answer2` 并返回其值。
```swift
let a = 10, b = 20, c: Int
if (a < b) {
    c = a
} else {
    c = b
}
print(c)
```
上面代码的简写形式为：
```swift
let a = 10, b = 20, c: Int
c = a < b ? a : b
print(c)
```
`c` 被设置为等于 `a`，因为条件 `a < b` 为 true

---

_空合运算符_ `a ?? b` 对可选类型 `a` 进行解包，如果 `a` 包含一个值则返回该值，如果 `a` 为 `nil` 则返回默认值 `b`。
表达式 `a` 始终是可选类型。
表达式 `b` 必须与 `a` 中存储的类型匹配。
空合运算符是以下代码的简写形式：
```swift
a != nil ? a! : b
```
