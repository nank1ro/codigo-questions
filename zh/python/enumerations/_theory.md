**枚举**（*enum*）为一组相关且固定的值定义一个公共类型，例如一周的几天或红绿灯的颜色。
你不再传递零散的字符串或数字，而是为每个值赋予一个**名称**，这样代码更易读，拼写错误也会变成错误。
在 Python 中，你通过从 `enum` 模块导入 `Enum` 并声明一个继承自它的类来创建枚举。
每个类属性都是枚举的一个**成员**，具有名称和值：
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
按照惯例，成员名称用大写字母书写。你通过类来访问成员，打印它会显示类名和成员名：
```python
favourite = Color.GREEN
print(favourite)  # Color.GREEN
```

---

枚举的每个成员都有两个属性：`name`，即你在类中写的标识符；`value`，即你赋给它的值：
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.GREEN.name)   # GREEN
print(Color.GREEN.value)  # 2
```
值可以是任何类型，而不仅限于整数：字符串、元组和浮点数都是常见的选择。
成员是一个普通对象，因此你可以把它存储在变量中，之后再读取它的属性：
```python
chosen = Color.RED
print(chosen.value)  # 1
```

---

每个枚举成员**只存在一次**：每次你写 `Color.RED` 时，得到的都是同一个对象。
因此，你既可以用 `is`（同一性）比较成员，也可以用 `==` 比较，两者结果相同：
```python
print(Color.RED is Color.RED)  # True
print(Color.RED == Color.BLUE) # False
```
成员**不等于**它的原始值，因为成员和普通数字是不同的东西：
```python
print(Color.RED == 1)        # False
print(Color.RED.value == 1)  # True
```
这正是枚举安全的原因：程序中其他地方产生的 `1` 不会被误认为是 `Color.RED`。

---

枚举类是**可迭代的**：对类进行 `for` 循环会按声明顺序访问每个成员：
```python
for color in Color:
    print(color.name, color.value)
```
`len()` 返回枚举有多少个成员，`list(Color)` 则构建一个由它们组成的列表：
```python
print(len(Color))    # 3
print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
```
在列表中，成员以它们的 `repr()` 形式显示，其中值包含在尖括号之间。

---

你可以像调用函数一样调用类，从**值**出发获取成员；或者使用方括号，从**名称**出发获取成员：
```python
print(Color(2))        # Color.GREEN
print(Color["BLUE"])   # Color.BLUE
```
当值或名称来自程序外部（例如文件或用户输入）时，这两种方式都很方便。
如果没有任何匹配项，`Color(9)` 会抛出 `ValueError`，`Color["PINK"]` 会抛出 `KeyError`。

---

通常具体值并不重要：你只需要成员彼此不同。
在这种情况下，你可以让 Python 通过 `auto()` 选取值，它同样从 `enum` 模块导入。
它将 `1` 赋给第一个成员，然后依次递增：
```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()

print(Direction.EAST.value)  # 3
```

---

普通 `Enum` 成员不能用 `<` 比较，也不能与数字相加。
当成员表示需要排序的**级别**时，应改为继承 `IntEnum`：它的成员同时也是整数，因此支持比较、算术运算和排序：
```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.HIGH > Priority.LOW)  # True
print(Priority.LOW + 1)              # 2
print(int(Priority.MEDIUM))          # 2
```
`IntEnum` 成员也等于它的整数值：`Priority.LOW == 1` 的结果是 `True`。

---

`StrEnum`（自 Python 3.11 起可用）是 `IntEnum` 的字符串对应版本：它的成员同时也是字符串，等于它们的值。
这使得它们在需要普通字符串的任何地方都很方便，例如配置键或 API 参数：
```python
from enum import StrEnum

class Mode(StrEnum):
    LIGHT = "light"
    DARK = "dark"

print(Mode.DARK == "dark")  # True
print(Mode.DARK.upper())    # DARK
```
与普通 `Enum` 不同，用 `str()` 或在 f-string 中把 `StrEnum` 成员转换为文本时，得到的是它的**值**，而不是 `Mode.DARK`。

---

枚举是一个类，因此它可以像其他任何类一样拥有**方法**和**属性**。
在它们内部，`self` 是方法被调用的那个成员，因此你可以查看 `self.name`、`self.value`，或者将 `self` 与其他成员进行比较：
```python
from enum import Enum

class Light(Enum):
    RED = 1
    GREEN = 2

    def can_go(self):
        return self is Light.GREEN

    @property
    def label(self):
        return self.name.lower()

print(Light.GREEN.can_go())  # True
print(Light.RED.label)       # red
```
在类体中赋值的任何普通值都会成为成员，而函数和属性永远不会，无论它们出现在哪里。

---

如果两个成员具有相同的值，第二个成员就不是新成员，而是第一个成员的**别名**：
```python
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # alias of ACTIVE

print(Status.ENABLED)  # Status.ACTIVE
print(len(Status))     # 1
```
迭代时会跳过别名，`len()` 也不会把它们计算在内。
通常重复的值是一个错误。从 `enum` 导入的 `unique` 装饰器让 Python 在声明带别名的枚举时立即抛出 `ValueError`：
```python
from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # ValueError: duplicate values found
```

---

`Flag` 是一种成员可以**组合**的枚举：一个值可以同时包含多个成员，就像一组选项。
用 `auto()` 声明它的成员，对于 `Flag` 来说它会分配 2 的幂（`1`、`2`、`4` 等），因此每种组合都有一个独特的值：
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
```
使用 `|` 组合成员，使用 `in` 检查某个成员是否是组合的一部分，使用 `value` 查看得到的数字：
```python
full = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(Permission.WRITE in full)  # True
print(full.value)                # 7
print(full)                      # Permission.READ|WRITE|EXECUTE
```

---

枚举与 `match` 语句（自 Python 3.10 起可用）天然搭配，后者将一个值与一系列 `case` 模式进行比较，并执行第一个匹配的模式：
```python
def action(light):
    match light:
        case Light.RED:
            return "Stop"
        case Light.GREEN:
            return "Go"
        case _:
            return "Slow down"
```
始终连同类一起书写成员，例如 `Light.RED`：像 `case RED:` 这样的裸名称不会进行任何比较，它只会把值捕获到新变量 `RED` 中并匹配一切。
通配符 `case _:` 是默认分支，必须放在最后，因为它之后的任何模式永远无法到达。

---

枚举成员是**可哈希的**，因此可以用作字典的键和集合的元素。
以枚举为键的字典是一种将数据附加到每个成员的干净方式，用成员进行查找比使用可能拼错的原始字符串更安全：
```python
class Size(Enum):
    SMALL = 1
    LARGE = 2

prices = {Size.SMALL: 2.5, Size.LARGE: 4.5}
print(prices[Size.LARGE])  # 4.5
```
由于成员可以出现在任何集合中，你所知道的关于列表、集合和推导式的一切同样适用于它们：
```python
order = [Size.LARGE, Size.SMALL, Size.LARGE]
print(len(set(order)))  # 2
```

---

成员值可以是一个**元组**，这让你能够为每个成员附加多份数据。
如果枚举定义了 `__init__` 方法，Python 会为每个成员调用一次该方法，把元组解包到它的参数中，因此你可以把每份数据保存到各自的属性中：
```python
from enum import Enum

class Planet(Enum):
    EARTH = (5.97, 6371)
    MARS = (0.64, 3390)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

print(Planet.MARS.radius)  # 3390
print(Planet.MARS.value)   # (0.64, 3390)
```
成员的 `value` 仍然是整个元组。

---

当你处理来自外部的数据（例如日志行或文件）时，迭代类和按名称查找成员可以很好地配合使用。
对类进行字典推导式会为每个成员准备一个条目，然后 `Level[name]` 把每个传入的字符串转换为对应的成员：
```python
counts = {level: 0 for level in Level}
counts[Level["INFO"]] += 1
```
由于枚举保持声明顺序，之后迭代 `counts` 会以相同的顺序给出成员。

---

除了普通方法之外，枚举还可以用 `@classmethod` 定义**类方法**。它们接收枚举类本身作为 `cls`，因此是把查找成员的其他方式放在这里的合适位置：
```python
class Color(Enum):
    RED = auto()
    BLUE = auto()

    @classmethod
    def parse(cls, text):
        return cls[text.strip().upper()]

print(Color.parse(" blue "))  # Color.BLUE
```
结合 `auto()`、方法、属性和查找，这让你能够构建自带行为的枚举。
