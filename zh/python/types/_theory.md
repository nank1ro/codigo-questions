Python 中的每个值都有一个**类型**，它说明这个值是哪种数据以及你能对它做什么。
基本的内置类型有：
- `int`，像 `42` 或 `-3` 这样的整数
- `float`，像 `3.5` 这样带小数部分的数
- `str`，像 `"hello"` 这样的一段文本
- `bool`，`True` 和 `False` 两个值之一
- `NoneType`，特殊值 `None` 的类型，表示"没有值"

内置函数 `type()` 返回一个值的类型。打印它会显示类名：
```python
print(type(42))     # <class 'int'>
print(type("hi"))   # <class 'str'>
```
你永远不会自己写 `NoneType`：`type(None)` 会返回它，但这个名字不像其他四个那样是内置名称。

---

`type()` 返回一个值的类，因此你可以用 `is` 把它和类名比较：
```python
age = 30
print(type(age) is int)  # True
```
不过大多数情况下，你只想知道一个值**是不是**某个类型。这正是 `isinstance(value, cls)` 的用途，它返回 `True` 或 `False`：
```python
print(isinstance(age, int))    # True
print(isinstance(age, str))    # False
```
第二个参数也可以是一个类的**元组**：只要值属于其中任意一个，结果就是 `True`：
```python
print(isinstance(2.5, (int, float)))  # True
```

---

Python 是**动态类型**的：类型属于**值**，而不属于变量。
变量只是附加在值上的一个名字，你随时可以把它附加到另一种类型的值上：
```python
x = 10
print(type(x))  # <class 'int'>
x = "ten"
print(type(x))  # <class 'str'>
```
不需要声明，也不需要转换：旧的值直接被遗忘。
这很方便，但也意味着变量的类型只有在程序运行时才知道，所以不小心混用类型会在运行时才表现为错误，而不是更早。

---

算术运算符你已经了解了。这里重要的是**结果的类型**。
`int` 与 `float` 相结合会得到 `float`，即使小数部分是零：
```python
print(3 + 0.5)   # 3.5
print(2 * 1.0)   # 2.0
```
**真除法** `/` 总是返回 `float`，即使能整除：
```python
print(10 / 5)    # 2.0
print(7 / 2)     # 3.5
```
**整除** `//` 把结果向下取整到最接近的整数（所以 `-7 // 2` 是 `-4`），并且当两个操作数都是整数时返回 `int`。它和取余 `%` 一起可以把一个数量分成整份：
```python
print(7 // 2)    # 3
print(7 % 2)     # 1
```

---

值不会自己改变类型：要把一个值变成另一种类型，你要像调用函数那样调用类型名。这称为**转换**（或*强制类型转换*）：
```python
print(int("42"))      # 42
print(float("3.5"))   # 3.5
print(str(7))         # '7'
print(int(3.9))       # 3
```
`int()` 和 `float()` 读取以文本形式书写的数字，用户输入或文件里得到的正是这种形式。`str()` 把任何东西变成文本，因此可以用 `+` 与其他字符串拼接。
注意 `int(3.9)` 不会四舍五入：它直接丢弃小数部分。

---

转换可能失败。`int("abc")` 无法得到一个数字，因此会抛出 `ValueError`，程序随之停止：
```python
int("abc")   # ValueError: invalid literal for int() with base 10: 'abc'
int("3.5")   # ValueError as well: "3.5" is not a whole number
```
为了让程序继续运行，你可以用 `try` / `except` 捕获错误：`try` 块中的代码会执行，如果它抛出了指定的错误，就转而执行 `except` 块：
```python
try:
    number = int(text)
except ValueError:
    number = 0
```
当转换成功时，`except` 块会被跳过。

---

每个值都可以被解释为布尔值。`bool()` 把一个值转换成 `True` 或 `False`，当值直接用在 `if` 中时也适用同样的规则。
被当作**假**的值是那些"空"的值：
- 数字 `0`（以及 `0.0`）
- 空字符串 `""`
- 空集合，例如 `[]`、`{}`、`()` 和 `set()`
- `None`

任何非空的值都是**真**的，包括负数以及只是看起来像空的字符串，例如 `"0"` 或 `" "`：
```python
print(bool(0))     # False
print(bool(-1))    # True
print(bool(""))    # False
print(bool("0"))   # True
```
这就是为什么 `if name:` 是检查字符串非空的常见写法。

---

`bool` 是 `int` 的**子类**：在需要数字的地方，`True` 表现得像 `1`，`False` 像 `0`：
```python
print(True + 1)     # 2
print(True == 1)    # True
print(False * 10)   # 0
```
`sum()` 把列表中的项相加，所以对布尔值列表求和就是**统计**其中有多少个 `True`：
```python
answers = [True, False, True]
print(sum(answers))  # 2
```
由于这层子类关系，`isinstance(True, int)` 返回 `True`，而 `type(True)` 仍然是 `bool`。

---

`None` 是一个独立的值，表示"这里什么都没有"。没有 `return` 语句的函数返回的就是它，它也常用作尚未确定的值的占位符。
由于 `None` 只有一个，请用 `is` 而不是 `==` 来检查它：
```python
result = None
if result is None:
    print("no result yet")
```
每种类型都有一个 `__name__` 属性，以字符串形式保存它的名字，这在生成消息时很方便：
```python
print(type(3).__name__)     # int
print(type(None).__name__)  # NoneType
```

---

打印一个 `float` 会显示精确表示它所需的全部位数，这往往太多了：
```python
print(19.999 * 3)  # 59.997
print(10 / 3)      # 3.3333333333333335
```
在 f-string 中，你可以在冒号后添加**格式说明**。`.2f` 表示"保留 2 位小数的定点数"：
```python
total = 10 / 3
print(f"{total:.2f}")   # 3.33
print(f"{total:.0f}")   # 3
```
数值会被四舍五入到所要求的小数位数，必要时补零：`f"{2.5:.2f}"` 得到 `2.50`。

---

格式化只改变数字的显示方式。要得到四舍五入后的**值**，请使用内置函数 `round()`：
```python
print(round(3.14159, 2))  # 3.14
print(round(2.71828, 1))  # 2.7
```
只有一个参数时，`round()` 四舍五入到最接近的整数并返回 `int`；带上小数位数时，它返回 `float`：
```python
print(round(3.7))     # 4
print(round(3.7, 0))  # 4.0
```
注意，正好位于两个数中间的值会舍入到**偶数**那一个：`round(2.5)` 是 `2`，而 `round(3.5)` 是 `4`。

---

`float` 以固定的位数用二进制存储，因此大多数十进制小数只能被**近似**表示。误差极小，但会在算术中显现出来：
```python
print(0.1 + 0.2)   # 0.30000000000000004
```
因此你不应该用精确相等来比较浮点数。可以把两边都四舍五入，或者使用 `math.isclose()`，它检查两个数在极小的容差范围内是否相等：
```python
import math
print(round(0.1 + 0.2, 2) == 0.3)  # True
print(math.isclose(0.1 + 0.2, 0.3))  # True
```
整数没有这个问题：`1 + 2 == 3` 永远是 `True`。

---

与许多语言不同，Python 的整数**没有最大值**：`int` 会增长到容纳所需的任意多位数，因此大数计算仍然精确：
```python
print(3 ** 100)  # 515377520732011331036461129765621272702107522001
```
而 `float` 只保留约 15 位有效数字，所以同样的幂用浮点数计算会损失精度：
```python
print(3.0 ** 100)  # 5.153775207320113e+47
```
由于 `str()` 对任何 `int` 都有效，统计一个数字位数的快捷方法就是测量它的文本长度。

---

你可以把变量、参数或返回值的预期类型写成**类型提示**：变量和参数在名字后面加冒号，返回值在冒号前面加箭头 `->`：
```python
count: int = 3

def greet(name: str) -> str:
    return "Hi " + name
```
类型提示是给人和编辑器等工具看的**文档**：Python **不会**检查它们。下面这段代码毫无怨言地运行并打印 `hello`：
```python
count: int = "hello"
print(count)
```
提示让预期的类型一目了然，但真正的类型仍然由值决定。

---

转换可以组合使用。`int("3.7")` 会失败，但 `float("3.7")` 可以，而对一个 `float` 使用 `int()` 会丢弃小数部分：
```python
number = float("3.7")   # 3.7
print(int(number))      # 3
```
`bool()` 遵循真值规则：`bool("")` 是 `False`，注意 `bool("False")` 是 `True`，因为它是一个非空字符串。

---

来自外部的文本总是 `str`，弄清楚它实际承载的是哪种类型是你的程序的任务。
一种常见做法是先尝试**最严格的**转换，当它抛出 `ValueError` 时再退回到下一种：
```python
try:
    value = int(text)
except ValueError:
    value = float(text)
```
在 `except` 块中再嵌套一个 `try`，可以让你再退回一次，例如保持文本原样。
