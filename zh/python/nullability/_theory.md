有时一个变量还**没有值**可存：用户尚未登录、搜索一无所获、设置从未被选择。Python 用特殊值 `None` 来表示这种情况。
`None` 和其他值一样：你可以给它赋值、打印它、把它传给函数。它的类型是 `NoneType`，并且整个程序中只有**一个** `None`，因此你写下的每个 `None` 都指向同一个对象：
```python
winner = None
print(winner)                 # None
print(type(winner).__name__)  # NoneType
print(winner is None)         # True
```
`None` 不是 `0`，不是空字符串，也不是 `False`：它是一个独立的值，表示"这里什么都没有"。

---

每次函数调用都会产生一个值，即使函数看起来没有返回任何东西。**没有** `return` 语句的函数，或者只有单独 `return` 的函数，都会返回 `None`：
```python
def say_hello():
    print("hello")

result = say_hello()
print(result)  # None
```
这就是为什么调用 `print(my_list.append(3))` 会显示 `None`：`append` 原地修改列表，不返回任何东西。
只执行动作的函数（打印、保存、修改列表）通常返回 `None`，而计算某个结果的函数必须显式地 `return` 它。

---

要检查一个变量是否为 `None`，请使用 `is` 和 `is not`，而不要用 `==`：
```python
if user is None:
    print("nobody logged in")
if user is not None:
    print("welcome")
```
`==` 问的是"这些值是否*相等*？"，任何类都可以通过定义 `__eq__` 方法以自己的方式回答这个问题。`is` 问的是"它们是否是*同一个对象*？"，这一点没有任何东西能改变。
由于 `None` 只有一个，`is None` 总是正确且稍快一些，而 `== None` 对带有自定义 `__eq__` 的对象可能给出令人意外的答案。

---

在条件中 `None` 被视为**假**，因此当 `value` 为 `None` 时 `if not value:` 为 `True`。很容易把它当作 `None` 检查来用，但同样的测试对 `0`、`""`、`[]` 以及其他所有空值也是 `True`：
```python
count = 0
if not count:
    print("missing?")   # printed, but 0 is a real value!
```
当"没有值"和"值为空"必须区别对待时，先检查 `is None`，再检查真假性：
```python
if count is None:
    print("no count yet")
elif not count:
    print("count is zero")
```
只有当你确实想把 `None` 和空值同等对待时，才使用 `if not value:`。

---

参数可以有**默认值**，当调用者省略实参时使用。`None` 是"未提供"时常用的默认值：
```python
def greet(name=None):
    if name is None:
        name = "stranger"
    print("Hello, " + name)

greet()       # Hello, stranger
greet("Ada")  # Hello, Ada
```
这对列表和字典很重要。默认值只在函数定义时求值**一次**，因此 `def add(item, items=[])` 会在所有省略 `items` 的调用之间共享同一个列表，元素会不断累积。解决办法是把默认值设为 `None`，并在函数内部创建一个新列表：
```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

用 `[]` 读取字典中不存在的键会引发 `KeyError`。`get` 方法是更安全的替代方式：键存在时返回对应的值，不存在时返回 `None`：
```python
ages = {"Ada": 36}
print(ages.get("Ada"))    # 36
print(ages.get("Grace"))  # None
```
`get` 接受第二个参数，即键缺失时**代替** `None` 返回的值：
```python
print(ages.get("Grace", 0))  # 0
```
这是日常代码中 `None` 最常见的出现方式：一次一无所获的查找。

---

返回数字**或** `None` 的函数应该在签名中说明这一点。**类型提示**（type hint）是记录预期类型的注解：参数用 `name: str`，返回值用 `-> int`。Python 不强制执行类型提示，但编辑器和阅读代码的人都依赖它们：
```python
def parse_age(text: str) -> int | None:
    if text.isdigit():
        return int(text)
    return None
```
`int | None` 读作"一个 `int` 或 `None`"。来自 `typing` 模块的旧写法 `Optional[int]` 含义完全相同，你在现有代码中仍会遇到它。
每当在签名中看到 `| None` 时，记得在使用结果之前先做检查。

---

可能收到 `None` 的函数常常以**守卫**开头：一个在无事可做时提前返回的 `if`。这样函数的其余部分就可以假定值是存在的，而不必把所有代码都嵌套在 `else` 里：
```python
def shout(text):
    if text is None:
        return None
    return text.upper() + "!"
```
守卫要放在最前面，并按照检查必须发生的顺序排列：在确认 `text` 不是 `None` 之前，你不能调用 `text.split()`。

---

`or` 运算符并不返回 `True` 或 `False`：当左操作数为真时它返回**左**操作数，否则返回**右**操作数。这提供了一种用单行代码提供回退值的方法：
```python
name = None
print(name or "anonymous")  # anonymous
name = "Ada"
print(name or "anonymous")  # Ada
```
问题在于 `or` 看的是真假性而不是 `None`：`0`、`""` 和 `[]` 也会被替换成回退值。只有当所有空值都应该变成回退值时，才使用 `x or fallback`。

---

当 `0` 或 `""` 必须保留、只有 `None` 需要替换时，回退就需要显式的 `is None` 检查。紧凑的形式是**条件表达式** `a if condition else b`：条件为真时其结果为 `a`，否则为 `b`：
```python
timeout = 0
seconds = timeout if timeout is not None else 30
print(seconds)  # 0, not 30
```

---

列表中可以在真实值旁边包含 `None`，例如读取失败的测量值或被跳过的回答。大多数操作不接受它：`sum([8, None])` 会引发 `TypeError`。
用条件为 `is not None` 的列表推导式把 `None` 值过滤掉：
```python
readings = [3, None, 5]
valid = [r for r in readings if r is not None]
print(valid)  # [3, 5]
```
如果改用 `if r`，也会把每个 `0` 丢弃，因此当零是有效读数时要写得明确。

---

查找之后再做 `None` 检查通常需要两行：一行保存结果，一行测试它。**赋值表达式**运算符 `:=`，昵称*海象运算符*，可以在表达式**内部**赋值，于是两个步骤都能放进 `if` 里：
```python
ages = {"Ada": 36}
if (age := ages.get("Ada")) is not None:
    print(age + 1)  # 37
```
圆括号是必需的：没有它们，`:=` 会试图对整个比较进行赋值。`if` 之后，`age` 仍然像其他变量一样可用。

---

并非所有"未找到"都用 `None` 报告。一些较老的函数返回**哨兵**值——一个被赋予特殊含义的普通值。字符串方法 `find` 返回子字符串的索引，不存在时返回 `-1`：
```python
print("banana".find("n"))  # 2
print("banana".find("x"))  # -1
```
来自 `re` 模块的 `re.match(pattern, text)` 函数检查 `text` 是否以 `pattern` 开头，匹配时返回一个 match 对象，不匹配时返回 `None`。
`None` 是更安全的约定：`-1` 是有效索引，因此 `text[text.find("x")]` 会静默返回最后一个字符而不是失败，而把 `None` 用作索引会立刻报错。

---

`None` 无法比较大小：`None < 1` 会引发 `TypeError`，因为 Python 无从知道"无"比一个数字小还是大。
当 `None` 用作搜索的起始值时，这一点很重要，比如"到目前为止见过的最佳值（如果有的话）"。每个比较都必须由放在**最前面**的 `is None` 检查保护，这样 `or` 才能短路，在没有可比较的值时跳过比较：
```python
if best is None or value > best:
    best = value
```
反过来的写法 `value > best or best is None` 会在第一次迭代时与 `None` 比较并崩溃。
