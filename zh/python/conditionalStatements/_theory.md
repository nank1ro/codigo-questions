当我们只想在满足某个条件时才执行代码时，就需要进行决策判断。
假设我们只想在天气好的时候出去玩。
在编程中，我们可以保存一个布尔变量 `nice_weather`，并在该变量为 `True` 时执行出去玩的操作，如下所示：
```python
nice_weather = True
if (nice_weather):
    # play outside
```

---

让我们继续之前的例子。
```python
nice_weather = True
if (nice_weather):
    # play outside
```
我们已经看到 `if` 语句只有在条件为 `True` 时才会执行代码块。
另一个需要注意的重要事项是**冒号** `:` 和**缩进**，它们表示代码块的开始。
缩进是指代码行开头的空格。
在其他编程语言中，代码缩进仅用于提高可读性，而在 Python 中，缩进是必不可少的。
你可以使用你喜欢的空格数（2、4、6、8），但推荐使用 4 个空格。
在本应用中，我们建议使用 **TAB** 键来缩进你的代码行

---

我们刚刚学习了如何在条件成立时执行一段代码块，现在让我们来看看如何在第一个条件不成立时执行另一段代码块。
如果天气好，我们就出去玩；否则，我们就待在家里。
在 Python 中，我们可以使用 `else` 语句，如下所示：
```python
nice_weather = True
if (nice_weather):
    # play outside
else:
    # stay home
```

---

假设我们有另一个条件需要检查，如下例所示：
```python
num = 3
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
else:
    print("do something else")
```
这段代码的输出是 `the number is 3`。
首先，让我们检查数字是否等于 2，这是 false。
然后我们继续检查第二个语句，检查 `num` 是否等于 3，由于这是 true，我们执行接下来的代码块，打印 `the number is 3`

---

我们可以添加任意多个 `elif` 语句，没有限制
```python
num = 4
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
elif (num == 4):
    print("the number is 4")
elif (num == 5):
    print("the number is 5")
elif (num == 6):
    print("the number is 6")
```
这段代码的输出是 `the number is 4`。

---

我们还可以在一个条件语句（`if`、`elif` 或 `else`）内部嵌套另一个条件语句，以创建更复杂的结构。
```python
num = 4
if (num < 3):
    print("the number is lower than 3")
else:
    if (num == 3):
        print("the number is 3")
    elif (num == 4):
        print("the number is 4")
    else:
        print("the number is greather than 4")
```
这段代码的输出是 `the number is 4`。
