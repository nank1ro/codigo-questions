**异常**是 Python 表示某条语句无法执行的方式。除以零、把 `"abc"` 转换为整数、读取字典中不存在的键，都会引发异常。当没有任何代码处理它时，程序会立即停止并打印**回溯信息**：
```python
print(10 / 0)
```
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```
回溯信息会列出正在执行的各行，最后一行给出**异常类型**（`ZeroDivisionError`）及其消息（`division by zero`）。这一行是应该最先阅读的内容。

要让程序保持运行，可以把有风险的语句放在 `try` 块中，并在 `except` 块中描述恢复方式：
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```
Python 会运行 `try` 块；如果引发了所指名的异常，它会直接跳到匹配的 `except` 块，然后继续执行程序的其余部分。

---

`try` 块会在**第一条**引发异常的语句处停止；它后面的行会被跳过，控制权转移到 `except` 块。`try` 块中已执行的内容不会被撤销，所以要尽量让它保持简短：
```python
def half(n):
    try:
        return 10 / n
    except ZeroDivisionError:
        return "undefined"

print(half(2))  # 5.0
print(half(0))  # undefined
```
`except` 中的 `return` 和其他任何 `return` 一样，这让 `try`/`except` 成为返回一个回退值而不是让程序崩溃的自然方式。

---

没有被任何 `except` 块匹配的异常会继续向外传播：跳出当前行、跳出执行它的函数、跳出它的调用者，依此类推。如果在到达程序顶层之前没有任何东西捕获它，Python 会打印回溯信息，进程以非零退出状态结束。失败语句之后的行永远不会执行。

---

`except` 子句只捕获它所指名的类型及其子类。这正是重点：其他所有异常会继续向外传播，因此你没有预料到的 bug 仍会以回溯信息的形式出现，而不是被悄悄吞掉。

当文本无法表示一个整数时，`int(text)` 会引发 **`ValueError`**，因此在读取用户输入时应指名这个类型：
```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(to_int("12"))    # 12
print(to_int("oops"))  # 0
```
在这里指名 `ValueError` 是一个决定，而不是走过场：`int(None)` 会引发 `TypeError`，而这个函数**有意**不捕获它，因为传入 `None` 是编程错误，应该让它显露出来。

---

选择能覆盖你所预期的失败的最窄类型，是让错误处理值得信赖的关键。读取文本的函数应该从错误的文本中恢复（`ValueError`），但绝不能掩盖以错误种类的参数被调用的情况（`TypeError`）——那个错误属于调用者，所以要放它通过。

---

一个 `try` 块后面可以跟**多个** `except` 子句，每个子句用不同的恢复方式处理不同的失败。Python 会从上到下将引发的异常与它们逐一比较，并运行**第一个**匹配的子句；其余的都会被跳过：
```python
try:
    value = 100 / int(text)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("cannot divide by zero")
```
由于第一个匹配的子句会获胜，当类型之间存在派生关系时顺序就很重要：把针对通用类型的子句放在针对更具体类型的子句之上，前者总会获胜，使具体的子句永远无法到达。

---

当多个失败需要**相同的**恢复方式时，在一个子句中用元组把它们列出来，比重复整个块更简洁：
```python
try:
    value = int(text) / divisor
except (ValueError, ZeroDivisionError):
    value = 0
```
括号是必需的：`except ValueError, ZeroDivisionError:` 在 Python 3 中是语法错误。元组仍然是一份显式的类型列表。

---

后面不跟类型的 `except:` 是**裸 except**。它会匹配一切，包括与你所保护的操作毫无关系的异常，因此规则很简单：总是指名你真正能从中恢复的类型。

---

异常是一个对象，`as` 把它绑定到一个名字上，让处理程序可以查看它：
```python
try:
    int("abc")
except ValueError as e:
    print(e)                   # invalid literal for int() with base 10: 'abc'
    print(type(e).__name__)    # ValueError
```
`str(e)`——`print(e)` 和 f-string 插槽使用的正是它——给出构建异常时所用的消息，而 `type(e).__name__` 以文本形式给出类名。由 `as` 绑定的名字只存在于 `except` 块内部；块结束时 Python 会删除它。

---

`try` 块后面可以跟一个 `else` 块，它**只在 `try` 块没有引发异常而完成时**运行：
```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print(number * 2)
```
把 `print(number * 2)` 放进 `try` 块也能工作，但那样的话，打印本身引发的 `ValueError` 会被误认为是转换失败。`else` 让 `try` 块只保留被保护的那一条语句，并容纳成功时应该发生的一切。

---

`finally` 块**无论如何都会运行**：在没有异常的 `try` 块之后、在 `except` 块之后，即使有一个无人捕获的异常正在向外传播，甚至当 `try` 或 `except` 块执行了 `return` 时，它也会运行：
```python
def read(text):
    try:
        return int(text)
    except ValueError:
        return 0
    finally:
        print("done")
```
两条路径都会在值离开函数之前打印 `done`。这个保证正是 `finally` 的用途：关闭文件、释放锁、恢复设置。完整的形态是 `try` / `except` / `else` / `finally`；`try` 至少需要一个 `except` 或一个 `finally`，而 `else` 只能与 `except` 搭配使用。

---

你自己的代码也可以引发异常，使用 `raise` 语句后跟一个异常对象：
```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```
`raise` 会立即停止函数，就像内置的失败一样。改为返回一个错误值——`-1`、`None`、`False`——调用者很容易忘记检查；而异常不会被偶然忽略。

选择能描述问题的类型：参数类型正确但值不可能时用 `ValueError`，参数类型完全错误时用 `TypeError`。传给异常的文本就是它的消息。

---

一些内置异常覆盖了大多数日常会遇到的失败：

| 异常 | 何时引发 | 示例 |
|---|---|---|
| `ValueError` | 类型正确但值不可能 | `int("abc")` |
| `TypeError` | 类型本身就是错误的 | `"x" + 1` |
| `ZeroDivisionError` | 除法或取模的除数为零 | `1 / 0` |
| `KeyError` | 字典中没有这样的键 | `{"a": 1}["b"]` |
| `IndexError` | 序列索引超出范围 | `[1, 2][5]` |

使用这些异常而不是发明新类型，能让任何懂 Python 的人都轻松读懂你的错误。

---

有时，处理程序应该对一次失败作出反应，但不必为此承担责任：记录它、计数、关闭某个东西——然后把问题交给调用者处理。在 `except` 块中单独使用一个 `raise` 会**重新引发**正在处理的异常，其原始的类型、消息和回溯信息都保持原样：
```python
try:
    value = int(text)
except ValueError:
    print("could not read the value")
    raise
```
改为编写 `raise ValueError(...)` 会创建一个带有全新回溯信息的新异常——它不再是你捕获的那个失败，而单独的 `raise` 保留的正是这种同一性。

---

当没有合适的内置类型时，可以通过继承 `Exception` 来定义自己的异常。空的类体通常就足够了——类名本身就是传达给阅读者的信息：
```python
class ConfigError(Exception):
    pass
```
它的行为和其他任何异常一样：使用 `raise ConfigError("bad port")` 引发它，用 `except ConfigError:` 捕获它。

把低层级的失败转换成自己的类型是很常见的做法，而原始错误不应在这个过程中丢失。`raise NewError(...) from original` 会把它们**链接**起来：它把 `original` 存入新异常的 `__cause__` 属性，回溯信息会在 *The above exception was the direct cause of the following exception* 标题下同时显示两者：
```python
try:
    port = int(text)
except ValueError as e:
    raise ConfigError("bad port") from e
```
如果没有 `from e`，两者仍会隐式地关联，但 `from` 明确说出了第一个错误导致了第二个错误。
