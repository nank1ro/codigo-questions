列表是一种数据类型，你可以用它在一个变量名下按顺序存储一组不同的信息。
列表可以存储任何类型的多个值，并使用**索引**来区分这些值。
你可以用以下形式的表达式为列表赋值：
```python
list_name = [item1, item2]
```

---

你可以通过索引访问列表中的单个元素。
索引就像一个地址，标识了元素在列表中的位置。
索引直接出现在列表名之后的方括号中，如下所示：
```python
list_name[index]
```

列表索引从 `0` 开始，**不是** `1`！你可以这样访问列表中的第一个元素：`list_name[0]`。
列表中的第二个元素位于索引 1：`list_name[1]`。

---

列表索引的行为与其他变量名一样！它既可以用于访问值，也可以用于赋值。
你已经看过如何这样访问列表索引：
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] # Gets the value "Jeremiah"
```
以下是赋值的方式：
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] = "Jordan"
names[0] # Gets the new value "Jordan"
```

---

与字符串一样，列表也有**长度**。
列表的长度就是它所包含的元素数量

---

列表不必有固定的长度。
你可以随时向列表末尾添加元素！
要向列表添加元素，我们使用 `append` 方法：
```python
>>> letters = ["a", "b"]
>>> letters.append("c")
>>> print(letters)
['a', 'b', 'c']
```

---

有时，你只想访问列表的一部分。
请看以下代码：
```python
>>> numbers = [1, 2, 3, 4]
>>> slice = numbers[1:3]
>>> print(slice)
[2, 3]
```
首先，我们创建一个名为 `numbers` 的列表。
然后，我们取列表的一个子部分并将其存储在 slice 列表中。
我们通过在列表名之后定义想要包含的索引来实现：`numbers[1:3]`。
在 Python 中，当我们以这种方式指定列表的一部分时，会包含第一个索引 `1` 处的元素，但不包含第二个索引 `3` 处的元素。

---

你可以像切片列表一样切片字符串！实际上，你可以把字符串看作字符的列表：每个字符是列表中从索引 `0` 开始的连续元素。
```python
list_name[:2]
# Grabs the first two items
list_name[3:]
# Grabs the fourth through last items
```
如果你的列表切片包含列表（或字符串）中的第一个或最后一个元素，则不需要包含该元素的索引。

---

列表元素可以是任何类型：
```python
list_name = ["one", 2, True]
```
事实上，上面我们依次有一个字符串、一个整数和一个布尔值。
我们还可以在列表中嵌套列表！

---

有时你需要在列表中搜索某个元素。
在 Python 中，我们可以使用 `index()` 方法：
```python
>>> names = ["Trevor", "Zac", "Glenn"]
>>> print(names.index("Zac"))
1
```
上面的代码打印了包含字符串 `"Zac"` 的第一个索引，在本例中为 `1`。
我们还可以使用 `insert()` 方法在指定索引处插入元素：
```python
>>> names.insert(1, "Ali")
>>> print(names)
['Trevor', 'Ali', 'Zac', 'Glenn']
```
上面的代码在索引 `1` 处插入了 `"Ali"`，这使得该索引之后的所有元素向后移动一位

---

在 Python 中，我们可以使用 `for..in` 关键字非常简单地遍历列表：
```python
>>> numbers = [1, 2, 3]
>>> for num in numbers:
>>>     print(num)
1
2
3
```
`for` 关键字后面跟一个变量名，它将依次被赋值为列表中每个元素的值。

---

**元组**与列表类似，但速度更快。
然而，元组的值不能被修改。
我们通常将元组用于在程序运行期间保持不变的**只读**数据。
要创建元组，我们使用圆括号 `()`

---

有时我们可能想将元组转换为列表。
为此，我们可以使用 `list()` 函数

---

同样，我们可以将列表转换为元组
