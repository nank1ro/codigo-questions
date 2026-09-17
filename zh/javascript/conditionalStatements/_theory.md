当我们只想在满足特定条件时执行代码时，就需要进行决策判断。
假设我们只想在天气好的时候出去玩。
在编程中，我们可以保存一个布尔变量 `niceWeather`，并在该变量为 `true` 时执行出去玩的操作，如下所示：
```javascript
var niceWeather = true;
if (niceWeather) {
    // 出去玩
}
```

---

让我们继续上一个例子。
```javascript
var niceWeather = true;
if (niceWeather) {
    // 出去玩
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
    // 出去玩
} else {
    // 待在家里
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
// 打印 10
```
上述代码的简写形式为：
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// 打印 10
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

---

`if` 是 JavaScript 中用来引出条件语句的关键字。这里没有 `elif` 关键字——第二个条件要用 `else if` 引出，写成两个独立的单词。

---

JavaScript 的布尔字面量是小写的：`true` 和 `false`，不是 `True`/`False`，也不是字符串 `"true"`/`"false"`。

---

要让代码块不执行，括号内的条件结果必须是 `false`。

---

`if` 和它的括号之间的空格纯粹是外观上的：对 JavaScript 来说，`if(true)` 和 `if (true)` 是同一条语句。

---

花括号的作用是把多条语句归并为一个代码块。没有花括号时，`if` 只控制紧随其后的那一条语句，所以 `if (true) console.log("Hello!");` 是合法的 JavaScript 代码。

---

条件只会在代码块开始之前求值一次。在花括号之间的语句执行期间，JavaScript 不会再次检查它。

---

`false` 条件会让代码块被完全跳过，程序会从右花括号之后的第一条语句继续执行。

---

条件不一定要是布尔值：JavaScript 会把它遇到的值转换为布尔值，所以 `if (1)` 会执行代码块，而 `if (0)` 不会。字面量 `true` 则完全不需要转换。

---

代码块不限于一行——当条件为 `true` 时，花括号内的每一条语句都会按顺序执行。
```javascript
if (true) {
    console.log("First line");
    console.log("Second line");
}
```
输出结果是 `First line`，接着是 `Second line`。

---

代码块内的语句会自上而下依次执行，所以同一个代码块中的两个 `console.log` 调用会分两行打印。

---

对代码块内的语句进行缩进只是一种提高可读性的约定。JavaScript 判断哪些内容属于代码块，靠的始终是花括号，而不是缩进。

---

像 `if`、`else if` 和 `else` 这样，根据条件是 `true` 还是 `false` 来决定执行还是跳过代码的语句，被称为**条件语句**。

---

布尔变量可以直接作为 `if` 的条件使用，不需要额外比较，即使它是像 `isAfternoon` 这样由 `!` 取反得到的变量。

---

`if` 语句的条件永远写在括号 `()` 内，紧跟在 `if` 关键字之后、左花括号之前。

---

代码块可以包含任意数量的语句，也可以一条都没有：`if (true) {}` 是合法的 JavaScript 代码，只是什么都不做。

---

`if` 语句的代码块，是花括号 `{ }` 内的那组指令，也就是条件为 `true` 时真正执行的部分。
