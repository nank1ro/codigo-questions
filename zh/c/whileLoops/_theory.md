在编程中，我们经常需要重复执行一段代码，例如：
```c
printf("2 seconds\n");
printf("3 seconds\n");
printf("4 seconds\n");
printf("5 seconds\n");
```
这会产生以下输出：
```c
2 seconds
3 seconds
4 seconds
5 seconds
```
显然，对于较长的语句，我们会花费大量时间编写代码，但幸运的是，我们可以使用循环。
让我们来学习 `while` 循环，获得与上面相同的输出。
```c
int count = 2;
while (count <= 5) {
    printf("%d seconds\n", count);
    count++;
}
```
我们创建了一个变量 `count`，并赋值为 `2`，即初始值。
然后我们使用了 `while` 语句，它会在条件 `count <= 5` 为 `true` 时反复运行代码块。
在代码块内部，我们**不能**忘记添加 `count++;` 这一行。
它会递增 `count` 的值，否则循环将会无限运行

---

要控制 `while` 循环的重复次数，我们首先将一个变量设置为一个数字。
我们称这个变量为计数器变量

---

然后，我们在条件中使用比较运算，将 `counter` 变量与一个数字进行比较。

---

在代码块内部，为了停止 `while` 循环，我们递增 `counter` 变量。

---

代码的编写顺序会影响输出结果。
