**注释**是写在源代码内部、供阅读代码的人查看的说明。Python 会完全忽略注释，因此注释永远不会改变程序的行为。

Python 唯一的注释形式是**单行注释**：它以 `#` 开头，并一直延续到行尾。
```python
# Greets the user
print("Hello")
```
请使用注释来解释某段代码的用途，或者说明代码为什么要这样编写。

---

注释不必独占一行：它可以跟在同一行的代码后面。这就是**行内注释**，它适合用来写一条关于该语句的简短说明：
```python
retries = 3  # give up after three attempts
```
从 `#` 到行尾的所有内容都会被忽略，而它前面的代码照常运行。

Python 的风格指南 **PEP 8** 对此有一些空格要求：代码与 `#` 之间至少要有**两个空格**，`#` 之后要有**一个空格**。独占一行的注释只需要在 `#` 后面留一个空格。

---

由于 Python 会完全丢弃注释，添加或删除注释永远不会改变程序的行为。只有**没有**被注释掉的代码才会运行。

这使得 `#` 成为在不删除代码的情况下快速禁用某行代码的方法。这称为**注释掉（commenting out）**：
```python
total = 10
# total = total + 5
print(total)  # prints 10
```
现在第二行是注释，因此 `total` 保持为 `10`。删掉 `#` 就能让这一行重新生效。

在试验代码时注释掉很方便，但记得要清理：长期被注释掉的代码只会让下一个阅读它的人感到困惑。

---

许多语言还有第二种注释，即跨越多行的**块注释**，例如 `/* ... */`。Python 没有这样的语法：只有 `#` 可用。

当说明需要多行时，在每一行前面都加上 `#`：
```python
# Prints the welcome banner.
# Called once when the app starts.
print("Welcome!")
```
同样的技巧可以一次注释掉多行代码：每行一个 `#`。每个编辑器都能用一个快捷键为整个选中区域添加或移除这些 `#`，所以实际操作比看起来轻松。

---

你经常会看到**三引号字符串**被当作块注释来使用：
```python
"""
This looks like a comment,
but it is a string.
"""
print("done")
```
位于 `"""` 和 `"""` 之间的字符串可以跨越多行，而单独写一个字符串也是一条合法的语句：Python 会创建它，不对它做任何事情，然后把它丢弃。什么都不会打印，所以效果看起来像一条注释。

但它并不是注释。它是字符串字面量，因此引号规则仍然适用：其中不配对的引号或一个多余的 `"""` 都会让程序出错，而 `#` 注释内部则什么都可以写。如果它恰好成为文件、类或函数的第一条语句，还可能意外地变成 docstring。在其他任何位置它都不会产生任何效果：CPython 在编译时会把整条语句丢弃。

所以，要禁用代码，请使用 `#`。三引号字符串有自己的用途，我们将在下一个练习中开始学习。

---

当字符串是函数内部的**第一条语句**时，Python 会把它当作该函数的文档。它被称为 **docstring**：
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"
```
按照惯例，docstring 写在三重双引号 `"""` 之间，即使它只有一行也一样，这样以后内容增多时无需更换引号。

摘要要用第三人称书写，就像在描述这个函数一样："Returns..."、"Adds..."、"Checks..."。docstring 必须出现在函数体中其他任何语句之前，否则它只是一个普通字符串。

---

docstring 并不会被丢弃：Python 会把它存储在函数的 `__doc__` 属性中，因此程序可以在运行时读取自己的文档：
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"

print(greet.__doc__)  # Returns the greeting for name.
```
当函数没有 docstring 时，`__doc__` 为 `None`。`help(greet)` 打印的就是它，鼠标悬停在函数名上时编辑器显示的也是它。

---

文件也可以有文档。作为**文件的第一条语句**、位于任何 import 或定义之前写下的字符串就是**模块 docstring**：它说明整个文件的用途。
```python
"""Tools for working with rectangles."""

def area(width, height):
    """Returns the area of a rectangle."""
    return width * height
```
只有第一条语句才算数。注释可以放在它上面，但两者之间出现的任何实际代码都会把该字符串变回一个普通而无用的字符串。

---

类也是同样的道理：放在类体第一条语句位置的字符串就是该类的 docstring，它同样存储在 `__doc__` 中：
```python
class Point:
    """A point on a grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Point.__doc__)  # A point on a grid.
```
类中的每个方法也可以有自己的 docstring，可通过 `Point.__init__.__doc__` 读取。因此，接受 docstring 的三个位置是模块顶部、类顶部和函数顶部。

---

docstring 和 `#` 注释看起来相似，但回答的是不同的问题。

**docstring** 面向**使用**代码的人：函数做什么、期望什么输入、返回什么结果。它会保存在 `__doc__` 中，`help()` 会读取它，编辑器会显示它，文档工具也会收集它。

**注释**面向**阅读**代码的人：这一行为什么这样写、那个奇怪的数字是什么意思、它绕过了哪个 bug。它只存在于源文件中，程序一旦运行就消失了。

```python
def timeout():
    """Returns the number of seconds to wait for the server."""
    # the server drops idle connections after 35 seconds
    return 30
```
所以：函数的文档写进 docstring，关于实现的说明写进注释。

---

当一行写不下时，docstring 会扩展成一种固定的布局，**PEP 257** 对此有描述：一行的摘要、一个空行，然后是详细内容，结束的 `"""` 独占一行。
```python
def to_seconds(minutes):
    """Returns the number of seconds in the given minutes.

    minutes is a whole number and is never negative.
    """
    return minutes * 60
```
这个空行很重要：工具会单独显示第一行作为简短描述，其余内容留给想深入了解的人阅读。

---

docstring 必须是**函数体的第一行**，位于其他所有语句之上。写在 `return` 之后或函数体其他任何位置的字符串只是一个普通字符串：`__doc__` 保持为 `None`，任何工具都不会显示它。

---

有些注释遵循编辑器能够识别的约定。最常见的**标记**有：
- `# TODO: ...` 标记还有待编写的内容
- `# FIXME: ...` 标记已知有错、必须修正的代码

```python
limit = 10
# TODO: read the limit from the settings
```
对 Python 来说它们只是普通注释；编辑器会把它们收集到一个专门的面板中，因此待办的工作很容易找到。`TODO` 通常与一个占位实现放在一起，在真正的代码写出来之前，占位实现能让程序继续运行。

完成工作后，请在同一次修改中替换占位实现并删除标记，这样注释就永远不会与代码的实际状态不符。

---

把说明函数用途的注释放在函数上方是错误的位置。docstring 才是合适的地方：它依附于函数，`help()` 能找到它，编辑器也能显示它，而 `def` 上方的 `#` 注释对它们全都不可见。

```python
# adds a and b
def add(a, b):
    return a + b
```
把同一句话向下移动一行，放到三重引号之间，它就变成了真正的文档：
```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
```

---

Python 只在代码中寻找 `#`，绝不会在**字符串**内部寻找。在引号之间，`#` 只是一个普通字符：
```python
print("black is #000000")  # a hex colour
```
第一个 `#` 是文本的一部分，第二个 `#` 才开启一条真正的注释。`#` 注释内部的 `"""` 也是同样道理：它只是三个引号字符，不会开启任何东西。

---

好的注释解释代码**为什么**这样做，而不是它**做了什么**。代码本身已经展示了会发生什么；用文字重复一遍只会增加噪音，而且代码一改就会过时：
```python
# set timeout to 30
timeout = 30
```
数字背后的原因才是读者猜不到的：
```python
# the server drops idle connections after 35 seconds, so stop earlier
timeout = 30
```
如果一条注释只是复述它下面那一行，就删掉它，或者换成原因。最好的注释说的是代码本身说不出来的东西。
