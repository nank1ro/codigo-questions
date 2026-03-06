在编程中，我们经常需要重复执行一段代码，例如：
```swift
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
这会产生以下输出：
```swift
2 seconds
3 seconds
4 seconds
5 seconds
```
显然，对于很长的语句，我们会花费大量时间编写代码，但幸运的是，我们可以使用循环。
让我们学习 `while` 循环，得到与上面相同的输出。
```swift
var count = 2
while count <= 5 {
    print("\(count) seconds")
    count += 1
}
```
所以我们创建了一个变量 `count`，赋初始值为 `2`。
然后我们使用了 `while` 语句，它将在条件 `count <= 5` 为 `true` 时持续运行代码块。
在代码块内部，我们**不能**忘记添加 `count += 1` 这一行。
它会递增 `count` 的值，否则我们的循环将会是无限的。

---

要控制 `while` 循环重复的次数，我们首先需要一个设置为数字的变量。
我们称这个变量为计数器变量。

---

然后，我们在条件中使用比较运算符，将 `counter` 变量与一个数字进行比较。

---

在代码块内部，为了停止 `while` 循环，我们需要递增 `counter` 变量。

---

编写代码的顺序会影响输出。

---

在 Swift 中，我们还有 `while` 循环的 **repeat-while** 变体。
它会先执行一次循环代码块，_然后_再检查循环条件。
之后它会继续重复循环，直到条件为 `false`。
Swift 中的 __repeat-while__ 循环类似于其他语言中的 __do-while__ 循环。
