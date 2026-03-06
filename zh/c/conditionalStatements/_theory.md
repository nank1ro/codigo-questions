当我们只想在满足某个条件时执行代码时，就需要进行决策判断。
假设我们只想在天气好的时候出去玩。
在编程中，我们可以保存一个布尔变量 `nice_weather`，并在该变量为 `true` 时执行出去玩的操作，如下所示：
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```

---

让我们继续之前的例子。
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
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
    // play outside
} else {
    // stay home
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
