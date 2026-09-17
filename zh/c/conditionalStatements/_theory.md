当我们只想在满足某个条件时执行代码时，就需要进行决策判断。
假设我们只想在天气好的时候出去玩。
在编程中，我们可以保存一个布尔变量 `nice_weather`，并在该变量为 `true` 时执行出去玩的操作，如下所示：
```c
bool nice_weather = true;
if (nice_weather) {
    // 出去玩
}
```

---

让我们继续之前的例子。
```c
bool nice_weather = true;
if (nice_weather) {
    // 出去玩
}
```
我们已经看到 `if` 语句只有在条件为 `true` 时才执行代码块。
另一个需要注意的重要内容是**花括号** `{}`，它表示一个代码块。

---

我们刚刚学习了如何在条件成立时执行代码块，现在让我们看看当第一个条件不成立时如何执行另一个代码块。
如果天气好，我们出去玩；否则，我们待在家里。
在 C 语言中，我们可以使用 `else` 语句，如下所示：
```c
bool nice_weather = false;
if (nice_weather) {
    // 出去玩
} else {
    // 待在家里
}
```

---

假设我们还有另一个条件需要检查，如下例所示：
```c
int num = 3;
if (num == 2) {
    printf("the number is 2\n");
} else if (num == 3) {
    printf("the number is 3\n");
} else {
    printf("do something else\n");
}
```
这段代码的输出是 `the number is 3`。
首先，检查数字是否等于 2，结果为 false。
然后继续检查第二个语句，判断 `num` 是否等于 3，结果为 true，因此执行后面的代码块，打印 `the number is 3`

---

我们可以添加任意数量的 `else if` 语句，没有限制
```c
int num = 4;
if (num == 2) {
    printf("the number is 2");
} else if (num == 3) {
    printf("the number is 3");
} else if (num == 4) {
    printf("the number is 4");
} else if (num == 5) {
    printf("the number is 5");
} else if (num == 6) {
    printf("the number is 6");
}
```
这段代码的输出是 `the number is 4`。

---

我们还可以在一个条件语句（`if`、`else if` 或 `else`）内部嵌套另一个条件语句，以创建更复杂的结构。
```c
int num = 4;
if (num < 3) {
    printf("the number is lower than 3\n");
} else {
    if (num == 3) {
        printf("the number is 3\n");
  } else if (num == 4) {
        printf("the number is 4\n");
  } else {
        printf("the number is greather than 4\n");
  }
}
```
这段代码的输出是 `the number is 4`。

---

现在来实践一下 `if` 语句的语法：关键字、括号中的条件，以及用花括号包裹的代码块。
```c
if (condition) {
    // 条件为 true 时执行
}
```

---

C 语言的布尔字面量是 `true` 和 `false`：小写、不加引号，并且是由 `<stdbool.h>` 定义的，而不是语言内置的。把 `True` 写成条件是无法编译的——只有小写形式才有效，当它为 `true` 时代码块才会执行。

---

C 语言没有独立的布尔判断：只要一个值不是零，条件就为真。`<stdbool.h>` 中的 `false` 其实就是 `0`，所以由它守护的代码块永远不会执行。

---

C 语言中的 `if` 语句由三部分组成：`if` 关键字、括号中的条件，以及花括号中的代码块。括号是必需的——编译器正是靠它来判断条件在哪里结束。

---

每个条件语句都以一个关键字开头，它告诉编译器需要先检查一个条件，才能决定接下来执行什么。

---

字面量 `true` 作为条件永远为真，所以代码块会执行，其中的 `printf` 会按原样运行。

---

字面量 `false` 作为条件永远不为真，所以代码块会被完全跳过，其中的内容都不会执行。

---

条件就是 `if` 语句所检查的值：当条件为 `true` 时代码块会执行，为 `false` 时则会被跳过。

---

左花括号可以和条件写在同一行，也可以另起一行。C 语言会忽略换行，所以这两种写法编译出来的程序完全一样。

---

条件外的括号是 C 语言 `if` 语法的一部分，而不是可有可无的分组符号：`if true { ... }` 无法编译。

---

加了引号的 `"false"` 是一个字符串，而不是布尔值——作为条件时，字符串是一个非空地址，会被判定为真。只有不加引号的 `false` 才能阻止代码块执行。

---

C 语言中 `if` 语句各部分之间的空格是自由的：对编译器来说，`if(true){` 和 `if (true) {` 是同一条语句，重要的只是各部分的先后顺序。

---

代码块不限于一条语句。花括号之间的每一条语句都会按书写的顺序依次执行。

---

布尔变量可以直接作为条件使用，不需要额外比较。既然 `online` 已经保存了 `true`，单独写 `if (online)` 就足以执行代码块。

---

`bool` 变量之所以能作为条件，是因为 `if` 只看它此刻所保存的值。当 `online` 中存的是 `false` 时，`if (online)` 的行为就和 `if (false)` 完全一样。

---

只有 `if` 语句花括号之间的代码才是有条件的。写在右花括号之后的内容都会无条件执行，无论条件结果如何。

---

代码块能容纳多少条语句并没有固定上限——一行也好，上百行也好，只要条件为 `true`，它们就会一起执行。

---

把布尔变量当作条件来读取，效果和字面量一样：既然 `online` 保存的是 `true`，代码块就会执行，其中的 `printf` 也会运行。

---

如果 `online` 保存的是 `false`，条件就为假，代码块会被完全跳过，花括号内的内容都不会被打印。
