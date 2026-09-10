比较运算符比较两个值并返回一个**布尔值** `True` 或 `False`：`==` 等于，`!=` 不等于，`<` 小于，`>` 大于，`<=` 小于或等于，`>=` 大于或等于：
```python
age = 18
print(age == 18)  # True
print(age != 18)  # False
print(age < 18)   # False
print(age >= 18)  # True
```
结果可以存入变量，也可以直接输出。单个 `=` 是赋值，不是比较。

---

比较运算符不只用于数字。字符串按码位逐字符比较，所以 `"apple" < "banana"` 是 `True`；由于每个大写字母都排在小写字母之前，`"Zoo" < "apple"` 也是 `True`。列表和元组同样按元素逐个比较：
```python
print("cat" < "dog")       # True
print([1, 2, 3] < [1, 3])  # True
print((1, 2) == (1, 2))    # True
```
比较是一个表达式，所以函数可以直接写 `return a < b`，而不必把它包在 `if` 里。

---

比较可以**串联**：`1 < x < 10` 检查 `x` 大于 `1` **并且**小于 `10`，与 `1 < x and x < 10` 完全一样，但 `x` 只求值一次：
```python
x = 5
print(1 < x < 10)   # True
print(1 < x <= 5)   # True
print(10 < x < 20)  # False
```
任何比较运算符都可以串联，每个运算符作用于它两侧的相邻值：`a < b == c` 表示 `a < b and b == c`。把串联读作区间 `low < x < high` 是最常见的用法。

---

逻辑运算符组合布尔值。只有两边都为 `True` 时 `and` 才是 `True`，只要有一边为 `True` 时 `or` 就是 `True`，而 `not` 会反转单个值：
```python
age = 20
member = False
print(age >= 18 and member)  # False
print(age >= 18 or member)   # True
print(not member)            # True
```
比较的优先级高于逻辑运算符，所以 `age >= 18 and member` 不需要括号。要把 `or` 分组放进 `and` 中则需要括号：`a and (b or c)`。

---

当 `not`、`and` 和 `or` 出现在同一个表达式中时，Python 先应用 `not`，然后是 `and`，最后是 `or`。所以 `a or b and c` 表示 `a or (b and c)`，而 `not a == b` 表示 `not (a == b)`：
```python
x = 6
print(x == 6 or x < 10 and x > 100)  # True: x == 6 or (False)
print(not x == 6)                    # False
```
如果想要不同的分组方式，就加上括号；括号也让表达式更易读。

---

每个值都有一个**真值**。`bool(value)` 对 `0`、`0.0`、`None`、空字符串 `""` 以及 `[]`、`{}` 和 `set()` 这类空容器返回 `False`；其他所有值都为真，包括 `"0"` 和 `[0]`：
```python
print(bool(0), bool(""), bool(None))   # False False False
print(bool(42), bool("0"), bool([0]))  # True True True
```
`if`、`while`、`and`、`or` 和 `not` 都使用这条规则，所以 `if items:` 检查列表非空，`not name` 检查字符串为空；无需写 `len(items) > 0` 或 `name == ""`。

---

因为 `if value:` 已经应用了真值，所以用 `== True` 或 `== False` 比较是多余的，甚至可能出错：`2 == True` 是 `False`，但 `2` 却为真。直接检查值本身：
```python
values = [0, 1, "", "a", None, [], [0]]
for value in values:
    if value:
        print(value)  # 1, a, [0]
```

---

`and` 和 `or` 并不总是返回 `True` 或 `False`：它们返回其中一个**操作数**。`a and b` 在 `a` 为假时返回 `a`，否则返回 `b`；`a or b` 在 `a` 为真时返回 `a`，否则返回 `b`：
```python
print(0 and "x")       # 0
print(3 and "x")       # x
print("" or "none")    # none
print("hi" or "none")  # hi
```
结果的真假与整个表达式的真假完全一致，这就是 `if a and b:` 仍然有效的原因。一个常见用法是提供默认值：`name = user_input or "guest"`。

---

逻辑运算符具有**短路**特性：一旦某个操作数为假 `and` 就停止，一旦某个操作数为真 `or` 就停止，因为结果已经确定。剩下的操作数永远不会求值，所以如果它们是函数调用就不会执行：
```python
def check(n):
    print("checking", n)
    return n > 0

check(-1) and check(5)  # prints only "checking -1"
check(2) or check(-3)   # prints only "checking 2"
```

---

`==` 比较**值**；`is` 比较**身份**，也就是两个名字是否指向同一个对象。分别创建的两个相等列表满足 `==` 但不满足 `is`：
```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # True False True
```
`is` 适用于 `None`、`True` 和 `False` 这类单例：写 `value is None` 或 `value is not None`，绝不要写 `value == None`，因为类可以把 `==` 定义成返回任何东西。对数字或字符串使用 `is` 并不可靠，Python 会对此发出警告。

---

短路求值是**保护**某个在部分值上会失败的操作的安全方式。在 `word is not None and len(word) < 4` 中，`len(word)` 只在 `word` 不是 `None` 时执行，所以这次调用永远不会抛出错误。保护条件必须放在前面：
```python
def is_short(word):
    return word is not None and len(word) < 4

print(is_short(None))   # False
print(is_short("cat"))  # True
```
请记住 `and` 返回的是一个操作数：`word and len(word) < 4` 对 `None` 给出 `None`，对空字符串给出 `""`，而不是 `False`。当需要布尔值时，请用真正的比较来做保护。

---

`in` 运算符检查**成员关系**：某个元素是否在列表、元组或集合中，某个子串是否在字符串中，或者某个键是否在字典中。`not in` 是它的否定：
```python
fruits = ["apple", "pear"]
print("pear" in fruits)          # True
print("kiwi" not in fruits)      # True
print("ex" in "text")            # True
print("age" in {"name": "Ada"})  # False, only keys are checked
```
两者都返回布尔值，读起来像英语，因此它们是检查成员关系的首选方式，而不必写循环。
