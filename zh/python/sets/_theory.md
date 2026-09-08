**集合**是一种存放**唯一**元素的容器：同一个值无论你写多少次，都只会出现一次。
集合也是**无序的**：没有第一个或最后一个元素，因此不能通过索引读取元素。
当你只关心*哪些*值存在，而不关心它们出现的次数或位置时，集合非常合适。
你可以通过在花括号 `{...}` 之间写出元素来创建集合：
```python
colors = {"red", "blue", "red"}
print(len(colors))  # 2
```
重复的 `"red"` 会被丢弃，因此 `len()` 只统计不重复的元素。

---

内置函数 `set()` 可以从任何集合（例如列表或字符串）构建一个集合。
由于集合只保留每个值一次，这是**去除重复项**的经典方法：
```python
nums = [1, 2, 2, 3]
unique = set(nums)
print(len(unique))  # 3
```
要检查某个值是否存在，可以使用 `in` 运算符，它会返回 `True` 或 `False`：
```python
print(2 in unique)  # True
print(9 in unique)  # False
```
即使有成千上万个元素，对集合进行成员检查也非常快。

---

创建**空集合**时有一个陷阱。
花括号也是字典的语法，所以 `{}` 创建的是一个空**字典**，而不是集合：
```python
empty = {}
print(type(empty))  # <class 'dict'>
```
要得到一个空集合，必须不带任何参数地调用 `set()`：
```python
empty = set()
print(type(empty))  # <class 'set'>
print(len(empty))   # 0
```

---

集合是**可变的**：创建之后你可以添加和删除元素。
`add(value)` 插入一个值；添加一个已经存在的值不会改变任何东西：
```python
letters = {"a", "b"}
letters.add("c")
letters.add("a")
print(len(letters))  # 3
```
删除元素有两种方式：
- `remove(value)` 会删除该值，但如果值不在集合中会抛出 `KeyError`
- `discard(value)` 如果值存在则删除，否则**什么也不做**，不会报错
```python
letters.remove("a")
letters.discard("z")  # "z" is not there, but no error
letters.remove("z")   # KeyError: 'z'
```

---

`pop()` 从集合中删除**一个任意元素**并返回它。
由于集合没有顺序，你无法选择删除哪个元素；对空集合调用 `pop()` 会抛出 `KeyError`：
```python
tickets = {101, 102, 103}
picked = tickets.pop()
print(len(tickets))  # 2
```
`clear()` 删除**所有**元素，留下一个空集合：
```python
tickets.clear()
print(len(tickets))  # 0
```

---

你可以像遍历列表一样，使用 `for` 遍历一个集合：
```python
for color in {"red", "blue"}:
    print(color)
```
由于集合是无序的，元素可能以**任意顺序**出现，而且这个顺序甚至可能在不同的运行之间发生变化。
当你需要一个可预测的顺序时，把集合传给 `sorted()`，它会返回其元素的一个有序**列表**：
```python
for color in sorted({"red", "blue"}):
    print(color)  # blue, then red
```

---

两个集合的**并集**是一个包含**两者**元素、不含重复项的新集合。
使用 `|` 运算符或 `union()` 方法：
```python
a = {1, 2}
b = {2, 3}
print(a | b)        # {1, 2, 3}
print(a.union(b))   # {1, 2, 3}
```
`a` 和 `b` 都不会被修改：集合运算总是返回一个新集合。

---

两个集合的**交集**只包含**两者都有**的元素。
使用 `&` 运算符或 `intersection()` 方法：
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)               # {2, 3}
print(a.intersection(b))   # {2, 3}
```
如果两个集合没有共同元素，结果就是一个空集合。

---

**差集** `a - b` 包含 `a` 中**不**在 `b` 中的元素。
顺序很重要：`a - b` 和 `b - a` 通常是不同的：
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # {1}
print(b - a)  # {4}
```
**对称差集** `a ^ b` 包含只属于两个集合中**恰好一个**的元素：
```python
print(a ^ b)  # {1, 4}
```
对应的方法形式是 `difference()` 和 `symmetric_difference()`。

---

运算符和方法并不完全等价。
运算符 `|`、`&`、`-` 和 `^` 只有在**两个**操作数都是集合时才能工作。
方法 `union()`、`intersection()`、`difference()` 和 `symmetric_difference()` 可以接受**任何可迭代对象**，比如列表或字符串：
```python
a = {1, 2}
print(a.union([2, 3]))  # {1, 2, 3}
print(a | [2, 3])       # TypeError: unsupported operand type(s) for |: 'set' and 'list'
```

---

集合之间也可以相互**比较**。
`a.issubset(b)`，或者 `a <= b`，当 `a` 的每个元素也在 `b` 中时为 `True`。
`a.issuperset(b)`，或者 `a >= b`，当 `a` 包含 `b` 的每个元素时为 `True`。
`a.isdisjoint(b)` 在两个集合**没有**共同元素时为 `True`：
```python
small = {1, 2}
big = {1, 2, 3}
print(small <= big)              # True
print(big.issuperset(small))     # True
print(small.isdisjoint({8, 9}))  # True
```

---

集合只能包含**可哈希**的元素，也就是不能改变的值：数字、字符串、`True`/`False` 以及**元组**。
尝试添加列表、字典或另一个集合会抛出 `TypeError`：
```python
points = set()
points.add((1, 2))  # ok, a tuple
points.add([1, 2])  # TypeError: unhashable type: 'list'
```
元组集合非常适合用来记录唯一的组合，比如坐标或 (name, age) 记录：
```python
visits = [(1, 2), (1, 2), (3, 4)]
print(len(set(visits)))  # 2
```

---

**frozenset** 是一个**不可变**的集合：一旦创建，就不能添加或删除元素。
可以用 `frozenset()` 从任何集合创建它：
```python
days = frozenset(["sat", "sun"])
print("sat" in days)  # True
days.add("mon")       # AttributeError: 'frozenset' object has no attribute 'add'
```
打印 frozenset 时，会在元素外面显示其类型，例如 `frozenset({'sat', 'sun'})`。
因为它不能改变，所以 frozenset 是可哈希的：与普通集合不同，它可以作为另一个集合的元素或字典的键。
所有只读操作（`in`、`len()`、`|`、`&`、`-`、`^`、比较运算）都照常可用。

---

**集合推导式**（set comprehension）用一个表达式构建集合，语法和列表推导式相同，只是使用花括号：
```python
nums = [1, 2, 2, 3]
squares = {n * n for n in nums}
print(squares)  # {1, 4, 9}
```
一个可选的 `if` 用于过滤元素，表达式产生的重复项会被自动丢弃：
```python
evens = {n for n in range(10) if n % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

---

集合运算也可以**就地**修改集合，而不是返回一个新的集合。
`update(iterable)` 会添加任何集合中的每个元素，就像 `add()` 一样，但可以一次添加多个值：
```python
inventory = {"sword"}
inventory.update(["potion", "map"])
print(len(inventory))  # 3
```
增强运算符也支持就地操作：`|=` 添加另一个集合的元素，`&=` 只保留共同的元素，`-=` 删除另一个集合的元素：
```python
inventory -= {"map"}
print(sorted(inventory))  # ['potion', 'sword']
```

---

两个集合**相等**，当它们包含相同的元素时，无论元素写出的顺序如何：
```python
print({1, 2, 3} == {3, 1, 2})  # True
```
将一个集合的长度与其去重后集合的长度进行比较，是检测重复项的一种快速方法：如果集合**更小**，说明有某个值出现了不止一次：
```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
print(len(set(emails)) < len(emails))  # True
```
列表方法 `count(value)` 会告诉你某个值出现了多少次，这有助于找出*哪些*值是重复的。
