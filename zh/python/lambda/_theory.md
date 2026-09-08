有时你只需要一个只用一次的小函数，例如把一个数翻倍。
为此写一整个 `def` 代码块显得有些笨重。
Python 提供了一种更简短的形式：**lambda** 表达式，一个写在单行上的_匿名_函数：
```python
lambda x: x * 2
```
语法是 `lambda 参数: 表达式`。
lambda 没有名字，但你可以把它存储在变量中，像调用其他函数一样调用它：
```python
double = lambda x: x * 2
print(double(4))  # 8
```

---

注意 lambda 的函数体没有 `return` 关键字。
函数体是一个**单一表达式**，它的值会被自动返回：
```python
square = lambda n: n * n
print(square(3))  # 9
```

---

lambda 可以接受**多个参数**。
用逗号分隔它们，和 `def` 函数中完全一样：
```python
power = lambda base, exp: base ** exp
print(power(2, 3))  # 8
```

---

由于函数体必须是单一表达式，lambda **不能包含语句**。
不能有 `return`、`if` 代码块、循环或赋值：
```python
# SyntaxError
increment = lambda x: return x + 1
```
如果你需要这些功能，请改用普通的 `def` 函数。

---

lambda 的参数也支持**默认值**：
```python
greet = lambda name="World": f"Hello, {name}!"
print(greet())       # Hello, World!
print(greet("Ana"))  # Hello, Ana!
```

---

你甚至不需要存储 lambda：可以**立即调用它**。
把 lambda 用括号括起来，然后加上参数：
```python
print((lambda x: x + 1)(4))  # 5
```

---

lambda 真正大放异彩的地方，是作为**传给其他函数的参数**。
`sorted()` 接受一个 `key` 参数：一个对每个元素调用的函数，其结果决定排序方式。
lambda 正是绝佳选择：
```python
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana']
```

---

用作 `key` 的 lambda 可以选取元素的任意部分。
对于列表的列表，`lambda p: p[1]` 会按每个内层列表的第二个元素排序。

---

`map()` 将一个函数应用到列表的**每一个元素**上。
它返回一个特殊的 _map 对象_，所以要用 `list()` 把它包起来才能看到值：
```python
nums = [1, 2, 3]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6]
```

---

`filter()` 只保留那些函数返回 `True` 的元素：
```python
nums = [5, 12, 8, 20]
big = list(filter(lambda n: n > 10, nums))
print(big)  # [12, 20]
```

---

直接打印 `map` 对象并不会显示它的值，你会得到类似 `<map object at 0x7f2b1c>` 的结果。
只有用 `list()`（或循环）才能得到你期望的值。

---

lambda 并不局限于内置函数：**你自己的函数**也可以接受一个函数作为参数并调用它。
```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 10, 3))  # 30
```

---

`max()` 和 `min()` 也和 `sorted()` 一样接受 `key` 函数：
```python
words = ["hi", "hello", "hey"]
print(max(words, key=lambda w: len(w)))  # hello
```

---

**什么时候应该优先使用 `def`？**
lambda 非常适合作为参数传递的简短一次性函数。
如果逻辑需要名字、需要多行、需要文档字符串，或者会在多处复用，那么 `def` 函数更清晰。
最后一个技巧：`sorted()` 也接受 `reverse=True`，可以先得到最大的值：
```python
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]
```
