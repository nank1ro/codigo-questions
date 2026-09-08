一个非常常见的任务是从已有的列表构建一个新列表。
用 `for` 循环加上 `append()` 需要写好几行：
```python
nums = [1, 2, 3]
doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6]
```
Python 为这个任务提供了一种更简短的形式：**list comprehension**，它用一个表达式就能构建出整个列表：
```python
doubled = [n * 2 for n in nums]
```
语法是 `[表达式 for 元素 in 可迭代对象]`：`for` 部分遍历元素，左边的表达式会针对每个元素求值。
结果是一个全新的列表，和用循环构建出来的完全一样。

---

左边的表达式可以是任何能产生值的东西：一次计算、一次函数调用、一次方法调用。
循环变量可以用任何你喜欢的名字，它只存在于方括号内部：
```python
prices = [10, 20]
with_tax = [price * 1.2 for price in prices]
print(with_tax)  # [12.0, 24.0]
```

---

comprehension 也可以对元素进行**过滤**。
在 `for` 部分之后加上 `if` 条件：只有条件为 `True` 的元素才会进入新列表：
```python
nums = [5, 12, 8, 20]
big = [n for n in nums if n > 10]
print(big)  # [12, 20]
```
这和在循环内部加 `if` 效果相同，并且以更易读的方式取代了配合 lambda 使用的 `filter()`。

---

过滤条件可以是任何返回布尔值的表达式，包括像 `len()` 这样的函数调用：
```python
words = ["a", "bee", "cat"]
short = [w for w in words if len(w) < 3]
print(short)  # ['a']
```

---

可迭代对象不一定要是列表：任何可以循环遍历的东西都可以，而 `range()` 是最受欢迎的一种。
它是构建数字列表最快的方式：
```python
squares = [n * n for n in range(4)]
print(squares)  # [0, 1, 4, 9]
```
记住 `range(start, stop)` 不包含 `stop`。

---

comprehension 非常适合用来**转换字符串**。
对每个元素调用一个字符串方法，或者用 f-string 构建一个新字符串：
```python
names = ["ana", "bob"]
greetings = [f"Hi {name.capitalize()}" for name in names]
print(greetings)  # ['Hi Ana', 'Hi Bob']
```

---

在 comprehension 内部，你可以使用之前定义的任何变量，例如作为 `range()` 的上限。

---

有时你不想丢弃元素，而是想为其中一些元素选择**不同的值**。
在 `for` 左边的表达式位置使用条件表达式 `a if 条件 else b`：
```python
nums = [3, -1, 4]
signs = ["+" if n > 0 else "-" for n in nums]
print(signs)  # ['+', '-', '+']
```
注意位置：`if-else` 位于 `for` **之前**，并且总是产生一个值，而过滤用的 `if` 位于 `for` **之后**，且没有 `else`。

---

这两种条件可以在同一个 comprehension 中组合使用：用 `if-else` 选择值，再用末尾的 `if` 过滤跳过部分元素。
```python
nums = [1, 2, 3, 4]
result = ["big" if n > 2 else "small" for n in nums if n != 3]
print(result)  # ['small', 'small', 'big']
```

---

`if` 的两个位置很容易混淆，要把它们区分开:
```python
values = [n if n > 0 else 0 for n in nums]  # for 之前的 if-else: 选择一个值，必须有 else
positives = [n for n in nums if n > 0]      # for 之后的 if: 过滤，不允许 else
```
在过滤的 `if` 后面写 `else` 是语法错误。

---

一个 comprehension 可以有**不止一个 `for`**。
它们的工作方式就像嵌套循环：第一个 `for` 是外层循环，第二个是内层循环。
```python
pairs = [a + b for a in ["x", "y"] for b in ["1", "2"]]
print(pairs)  # ['x1', 'x2', 'y1', 'y2']
```

---

内层 `for` 可以使用外层的变量。
这是把嵌套列表**展平**成单一列表的经典方法：
```python
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4]
```
然后 `sum()` 函数会把列表中所有数字加起来。

---

你也可以对**字典**进行循环。
通过 `.items()`，`for` 部分会把每一对键值解包到两个变量中，一个键和一个值：
```python
ages = {"ana": 31, "bob": 25}
lines = [f"{name} is {age}" for name, age in ages.items()]
print(lines)  # ['ana is 31', 'bob is 25']
```

---

同样的思路也适用于字典：**dict comprehension** 使用花括号和 `key: value` 表达式：
```python
names = ["ana", "bob"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'ana': 3, 'bob': 3}
```

---

花括号**不带** `key: value` 部分，得到的就是 **set comprehension**。
set 是一种无序集合，只保留唯一值，因此重复项会自动消失：
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {n for n in nums}
print(unique)  # {1, 2, 3}
```

---

**什么时候应该使用 comprehension？**
当结果是一个列表（或 dict、或 set），并且逻辑能放进一行易读的代码时，它是完美的选择：一次简单的转换，一个可选的过滤条件。
如果你需要多条语句、超过两层嵌套的 `for`，或者这一行变得难以阅读，那就改写成普通的 `for` 循环：代码会更长，但更清晰。
comprehension 还能替代大多数配合 lambda 使用 `map()` 和 `filter()` 的场景：
```python
doubled = list(map(lambda n: n * 2, nums))
doubled = [n * 2 for n in nums]  # same result, easier to read
```
