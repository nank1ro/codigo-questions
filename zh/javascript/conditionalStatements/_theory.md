当我们只想在满足特定条件时执行代码时，就需要进行决策判断。
假设我们只想在天气好的时候出去玩。
在编程中，我们可以保存一个布尔变量 `niceWeather`，并在该变量为 `true` 时执行出去玩的操作，如下所示：
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```

---

让我们继续上一个例子。
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```
我们已经看到 `if` 语句只在条件为 `true` 时执行代码块。
另一个需要注意的重要事项是**花括号** `{}`，它们用于表示代码块。

---

我们刚刚学习了如何在条件满足时执行一段代码块，现在让我们看看如何在第一个条件不满足时执行另一段代码块。
如果天气好，我们就出去玩；否则，我们就待在家里。
在 JavaScript 中，我们可以使用 `else` 语句，如下所示：
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

假设我们还有另一个条件需要检查，如下例所示：
```javascript
var num = 3;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else {
    console.log("do something else");
}
```
这段代码的输出是 `the number is 3`。
首先，检查数字是否等于 2，结果为 false。
然后进入第二个语句，检查 `num` 是否等于 3，结果为 true，因此执行后续代码块，打印 `the number is 3`

---

我们可以添加任意多个 `else if` 语句，没有限制
```javascript
var num = 4;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else if (num == 4) {
    console.log("the number is 4");
} else if (num == 5) {
    console.log("the number is 5");
} else if (num == 6) {
    console.log("the number is 6");
}
```
这段代码的输出是 `the number is 4`。

---

我们还可以在一个条件语句（`if`、`else if` 或 `else`）内部嵌套另一个条件语句，以创建更复杂的结构。
```javascript
var num = 4;
if (num < 3) {
    console.log("the number is lower than 3");
} else {
    if (num == 3) {
        console.log("the number is 3");
    } else if (num == 4) {
        console.log("the number is 4");
    } else {
        console.log("the number is greather than 4");
    }
}
```
这段代码的输出是 `the number is 4`。

---

三元条件运算符是一种特殊的运算符，由三部分组成，格式为 `question ? answer1 : answer2`。
它是根据 `question` 为 true 还是 false 来计算两个表达式之一的快捷方式。
如果 `question` 为 true，它计算 `answer1` 并返回其值；否则，它计算 `answer2` 并返回其值。
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// prints 10
```
上述代码的简写形式为：
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// prints 10
```
`c` 被赋值为 `a`，因为条件 `a < b` 为 true

---

_空值合并运算符_ `a ?? b` 会解包可选值 `a`（如果它包含一个值），或者在 `a` 为 `nil` 时返回默认值 `b`。
表达式 `a` 始终是可选类型。
表达式 `b` 必须与 `a` 中存储的类型匹配。
空值合并运算符是以下代码的简写形式：
```javascript
a != nil ? a! : b;
```
