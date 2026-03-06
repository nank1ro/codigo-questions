我们知道如何使用 `while` 循环来重复代码。
就像这个程序重复语句来显示 `hello`
```python
counter = 0

while counter < 5:
    print("hello")
    counter += 1
```
但我们也可以使用 `for` 循环来做同样的事情：
```python
for i in range(5):
    print("hello")
```

---

在 `for` 循环中，我们可以使用 `range()` 函数来指定循环运行的次数

---

在 `range()` 函数中添加一个数字，比如 `5`，意味着它将循环执行代码块 5 次，从 `0` 到 `4`

---

名为 `i` 的变量是计数器变量。
我们可以给它任意名称。
它记录当前是循环的第几次重复

---

`range()` 函数返回一个数字序列，默认从 0 开始，默认递增 1，在指定数字之前停止。
该函数的语法如下：
```python
range(start, stop, step)
```
`start` 和 `step` 是可选的，而 `stop` 是必需的
