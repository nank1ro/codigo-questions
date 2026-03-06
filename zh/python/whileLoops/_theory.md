在编程中，我们经常需要重复执行一段代码，例如：
```python
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
这会产生以下输出：
```python
2 seconds
3 seconds
4 seconds
5 seconds
```
显然，对于较长的语句，我们需要花费大量时间来编写代码，但幸运的是，我们可以使用循环。
让我们学习 `while` 循环，来获得与上面相同的输出。
```python
count = 2
while (count <= 5):
    print(f"{count} seconds")
    count += 1
```
我们创建了一个变量 `count`，并赋予初始值 `2`。
然后我们使用了 `while` 语句，它会在条件 `count <= 5` 为 `True` 时持续执行代码块。
在代码块内部，我们**不能**忘记添加 `count += 1` 这一行。
它会递增 `count` 的值，否则我们的循环将变成无限循环

---

要控制 `while` 循环的重复次数，我们首先需要一个设置为数字的变量。
我们称这个变量为计数器变量

---

然后，我们在条件中使用比较运算符将 `counter` 变量与一个数字进行比较。

---

在代码块内部，为了停止 `while` 循环，我们需要递增 `counter` 变量。

---

代码的书写顺序会影响输出结果。
