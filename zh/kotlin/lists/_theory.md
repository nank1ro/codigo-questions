列表是一种数据类型，可以用来将多个不同的信息按顺序存储在一个变量名下。
列表存储一种或多种类型的多个值，并使用**索引**来区分这些值。
你可以用以下表达式将元素赋给列表：
```kotlin
val listName = listOf<itemsType>(item1, item2)
```
`itemsType` 代表列表中元素的类型，例如可以是 `Int`、`String`、`Any`...

---

列表是一个有特定顺序的元素集合。Kotlin 中有两种类型的列表：

- `List` 创建后不可修改。
- `MutableList` 创建后可以修改，即你可以添加、删除或更新其中的元素。

```kotlin
val numbers = listOf(1, 3, 5)
numbers.add(7) // [1]
```
__[1]__ 会抛出错误，因为 `List` 是_只读的_。

要创建一个可修改的列表，请使用 `mutableListOf` 关键字
```kotlin
val numbers = mutableListOf(1, 3, 5)
numbers.add(7)
println(numbers)
// prints [1, 3, 5, 7]
```

---

你可以通过索引访问列表中的单个元素。
索引就像一个地址，标识元素在列表中的位置。
索引直接跟在列表名称后面，放在方括号中，如下所示：
```kotlin
listName[index]
```

列表索引从 `0` 开始，**不是** `1`！你可以这样访问列表的第一个元素：`listName[0]` 或 `listName.get(0)` 甚至 `listName.first()`。
列表中的第二个元素在索引 __1__ 处：`listName[1]`。

---

索引实际上是相对于第一个元素的偏移量。例如，当你说 `list[2]` 时，你并不是在请求列表的第二个元素，而是请求距离第一个元素偏移 2 个位置的元素。因此 `list[0]` 是第一个元素（零偏移），`list[1]` 是第二个元素（偏移 1），`list[2]` 是第三个元素（偏移 2），以此类推。

列表索引既可以用来访问值，也可以用来赋值。
你已经看到了如何像这样访问列表索引：
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
println(names[0])
```
以下是赋值的方式：
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel")
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
println(names[0])
```

---

和字符串一样，列表有一个通过 `size` 属性获取的**长度**。
列表的长度是它所包含的元素个数。

---

另一个有用的列表操作是 `contains` 方法，用于查找给定元素是否在列表中。
例如，如果你有一个名字列表，可以使用 `contains` 方法来判断某个名字是否在列表中。
```kotlin
val names = listOf("Thomas", "Donald", "Scarlett")
println(names.contains("Scarlett"))
// prints true
```

---

可变列表不必具有固定的长度。
你可以随时向列表末尾添加元素！
要向可变列表添加元素，我们使用 `add` 函数或 `+=` 快捷方式：
```kotlin
val letters = mutableListOf("a", "b")
letters.add("c")
println(letters)
// prints [a, b, c]
```

---

正如我们在前面的例子中看到的，我们可以使用 `add` 函数逐个添加元素。
但如果我们需要一次性添加另一个列表的所有元素，可以简单地使用 `addAll` 函数或 `+=` 快捷方式：
```kotlin
val letters = mutableListOf("a", "b")
val newLetters = listOf("c", "d", "e")
letters.addAll(newLetters)
println(letters)
// prints [a, b, c, d, e]
```

---

有时，你只想访问列表的一部分。
请看以下代码：
```kotlin
val numbers = listOf(1, 2, 3, 4) // [1]
val slice = numbers.slice(1..2) // [2]
println(slice)
// prints [2, 3]
```
__[1]__：首先，我们创建一个名为 `numbers` 的_只读_列表。
__[2]__：然后，我们使用 `slice` 函数获取列表的一个子部分，并将其存储在 slice 列表中。
我们通过在 `slice` 函数中定义要包含的索引来实现这一点。

在 Kotlin 中，我们可以使用 `..` 来包含最后一个索引，也可以使用 `until` 来排除最后一个索引。

---

如果我们指定 `Any` 类型，列表元素可以是任意类型：
```kotlin
var listName: List<Any> = listOf("one", 2, true)
```
事实上，上面我们依次有一个 `String`、一个 `Integer` 和一个 `Boolean`。
但我们也可以有包含列表的列表！

---

有时你需要在列表中搜索某个元素。
在 Kotlin 中我们可以使用 `indexOfFirst` 方法：
```kotlin
val names = mutableListOf("Trevor", "Zac", "Glenn")
println(names.indexOfFirst { it == "Zac"})
// prints 1
```

`indexOfFirst` 方法接受一个__谓词__函数，该函数会对列表中的每个元素进行求值，直到为 true，然后返回该元素的_索引_。
上面的代码打印了包含字符串 `"Zac"` 的第一个索引，在本例中为 `1`。

我们还可以使用 `add(index, element)` 方法在可修改列表的特定索引处插入元素：
```kotlin
names.add(1, "Ali")
// prints [Trevor, Ali, Zac, Glenn]
```
上面的代码在索引 `1` 处插入了 `"Ali"`，这会将该索引之后的所有元素向后移动 1 个位置。

---

在 Kotlin 中，我们可以使用 `for..in` 关键字以非常简单的方式遍历列表：
```kotlin
val numbers = listOf(1, 2, 3)
for (num in numbers) {
    println(num)
}
// prints 1, 2, 3
```
`for` 关键字后面跟着一个变量名，它将依次被赋予列表中每个元素的值。
