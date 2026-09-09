在 Python 中，函数就是一个**值**，就像数字或字符串一样。你可以把它存储在变量中、放入列表或传递给另一个函数。只有加上括号才会调用它：`shout` 是函数本身，`shout("hi")` 是它的结果：
```python
def shout(text):
    return text.upper() + "!"

say = shout
print(say("hi"))  # HI!
```
接收另一个函数作为参数、或者返回一个函数的函数，被称为**高阶函数**。在其内部，该参数像任何其他函数一样通过括号来调用：
```python
def apply(func, value):
    return func(value)

print(apply(shout, "bye"))  # BYE!
print(apply(len, "bye"))    # 3
```

---

把函数作为参数传递，让调用者决定做**什么**，而高阶函数决定做**多少次**或在**什么之上**做。函数参数可以按需被调用任意次，其结果还可以再次反馈给它：
```python
def repeat(func, value, times):
    for _ in range(times):
        value = func(value)
    return value

def add_one(n):
    return n + 1

print(repeat(add_one, 0, 3))  # 3
```
任何可调用对象都可以：`def` 函数、像 `len` 这样的内置函数，或者一个 `lambda`。

---

内置的 `map(func, iterable)` 对每个元素调用 `func` 并产生结果，每个元素对应一个结果。它返回一个惰性的 *map 对象*，所以要把它包装在 `list()` 中才能看到这些值：
```python
numbers = [1, 2, 3]
print(list(map(lambda n: n * 10, numbers)))  # [10, 20, 30]
```
可以传递任何可调用对象，而不仅仅是 lambda：像 `len` 这样的内置函数，或者从其类中取出的方法，比如 `str.upper`，它把字符串作为自己的第一个参数：
```python
names = ["ada", "linus"]
print(list(map(str.upper, names)))  # ['ADA', 'LINUS']
print(list(map(len, names)))        # [3, 5]
```

---

内置的 `filter(func, iterable)` 只保留让 `func` 返回真值的元素。和 `map` 一样，它返回一个惰性对象，必须转换成列表：
```python
numbers = [4, -2, 7, 0]
print(list(filter(lambda n: n > 0, numbers)))  # [4, 7]
```
传递给 `filter` 的函数被称为**谓词**：它接收一个元素，并回答一个关于该元素的是/否问题。传递 `None` 而不是函数时，会保留那些本身为真的元素，丢弃 `0`、`""` 和 `None`。

---

`sorted(iterable, key=func)` 根据 `func` 为每个元素返回的值对元素进行排序，而不改变元素本身。加上 `reverse=True` 可以让最大的排在最前面：
```python
words = ["kiwi", "fig", "banana"]
print(sorted(words, key=len))                # ['fig', 'kiwi', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'kiwi', 'fig']
```
排序是**稳定的**：键相等的元素保持其原始顺序。`key` 函数对每个元素只调用一次，其结果仅用于比较，因此输出仍然包含原始的单词，而不是它们的长度。

---

`key` 函数可以选取元素的**任何部分**。对于元组列表，`lambda s: s[1]` 按每个元组的第二项排序；对于字典列表，`lambda d: d["age"]` 按某个值排序：
```python
pairs = [("b", 2), ("a", 3), ("c", 1)]
print(sorted(pairs, key=lambda p: p[1]))  # [('c', 1), ('b', 2), ('a', 3)]
```
`min` 和 `max` 接受相同的 `key` 参数，因此 `max(pairs, key=lambda p: p[1])` 返回 `('a', 3)`：整个元组，而不仅仅是那个数字。

---

函数也可以**返回**一个函数。用 `def` 定义一个内部函数，并在不调用它的情况下返回它：
```python
def make_greeter(greeting):
    def greet(name):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
print(hello("Ada"))  # Hello, Ada
```
即使 `make_greeter` 已经结束，内部函数仍继续使用 `greeting`：它**记住**了创建它的作用域中的变量。这样的函数被称为**闭包**。每次调用 `make_greeter` 都会创建一个新的、独立的闭包，它拥有自己的 `greeting`。

---

闭包可以读取外层函数的变量，但对其中某个变量赋值却会创建一个**新的局部**变量。要更新外层变量，请在内部函数中用 `nonlocal` 声明它：
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```
`global` 会在模块级别查找 `count`，而那里并不存在这个变量。使用 `nonlocal` 后，每次调用返回的函数都会更新同一个 `count`，因此闭包在调用之间携带着状态，就像一个小型对象。

---

`functools` 模块中的 `reduce(func, iterable, initial)` 把一个序列折叠成一个**单一的值**。它以到目前为止的结果和下一个元素为参数调用 `func`，从 `initial` 开始：
```python
from functools import reduce

total = reduce(lambda acc, n: acc + n, [1, 2, 3], 0)
print(total)  # 6
```
步骤是 `0 + 1`，然后是 `1 + 2`，再是 `3 + 3`。当省略 `initial` 时，第一个元素会被用作起始值，但这样空序列会引发 `TypeError`，所以只要序列可能为空，就应给出一个初始值。

---

`functools` 中的 `partial(func, *fixed)` 构建一个新函数，其中一些参数**已被填入**。调用结果时提供其余的参数：
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
```
提供给 `partial` 的位置参数填充最前面的参数；关键字参数按名称固定一个参数，而在调用时仍然可以覆盖它。partial 是普通的可调用对象，因此可以传递给 `map`、`sorted` 或任何其他高阶函数。

---

`partial` 与接受选项的内置函数搭配使用非常方便。`int(text, base=16)` 解析十六进制字符串；固定进制后就得到一个单参数的转换器，正好适合 `map`：
```python
from functools import partial

hex_to_int = partial(int, base=16)
print(hex_to_int("ff"))                      # 255
print(list(map(hex_to_int, ["a", "10"])))    # [10, 16]
```
partial 对象记住它所包装的内容：`hex_to_int.func` 是 `int`，而 `hex_to_int.keywords` 是 `{'base': 16}`。

---

**装饰器**是一种高阶函数，它接收一个函数并返回一个包装它的新函数，通常用于在原始调用之前或之后添加行为：
```python
def announce(func):
    def wrapper(name):
        print("calling " + func.__name__)
        return func(name)
    return wrapper
```
`func.__name__` 是函数定义时所用的名称。应用装饰器就是一次调用：`greet = announce(greet)`。放在 `def` **上方**一行的 `@` 语法所做的正是这件事：
```python
@announce
def greet(name):
    return "Hello, " + name
```
装饰器必须在使用 `@` 之前定义，因为替换会在 `def` 执行时立即发生。

---

只接受一个参数的装饰器用途有限。要包装**任意**函数，包装器会把每个位置参数收集到 `*args` 中，把每个关键字参数收集到 `**kwargs` 中，并原样转发它们：
```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name, punctuation="!"):
    return "hello " + name + punctuation

print(greet("ada"))                    # HELLO ADA!
print(greet("ada", punctuation="?"))   # HELLO ADA?
```
在包装器内部，`args` 是一个元组，`kwargs` 是一个字典；调用中的 `*` 和 `**` 把它们重新解包成单独的参数。

---

`any(iterable)` 在**至少一个**元素为真时返回 `True`，而 `all(iterable)` 在**每个**元素都为真时返回 `True`。它们与**生成器表达式**天然搭配：生成器表达式就是不带方括号的列表推导式，它一次产生一个值，而不是构建一个列表：
```python
ages = [21, 34, 17]
print(any(age >= 18 for age in ages))  # True
print(all(age >= 18 for age in ages))  # False
```
由于值是惰性产生的，`any` 在遇到第一个 `True` 时停止，`all` 在遇到第一个 `False` 时停止，不会对其余部分求值。`sum` 也接受生成器表达式：`sum(1 for age in ages if age >= 18)` 统计成年人的数量。
