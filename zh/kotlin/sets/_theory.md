`Set` 是一种数据类型，可以用来将多个不同的信息按顺序存储在一个变量名下。
与 `List` 的主要区别在于 `Set` 只允许每个值出现一次。

和 `List` 一样，`Set` 存储一种或多种类型的多个值，并使用**索引**来区分这些值。
你可以用以下表达式将元素赋给集合：
```kotlin
val setName = setOf<itemsType>(item1, item2)
```
`itemsType` 代表集合中元素的类型，例如可以是 `Int`、`String`、`Any`...

---

`Set` 是一个没有特定顺序的__唯一__元素集合。

```kotlin
val numbers = setOf(1, 1, 2) // [1]
println(numbers)
// prints [1, 2]
```

在 __[1]__ 处，我们尝试创建一个包含两次数字 __1__ 的集合，但如你所见，每个元素必须是唯一的，第二个 __1__ 会被自动丢弃。

---

Kotlin 中有两种类型的 `Set`：

- `Set` 创建后不可修改。
- `MutableSet` 创建后可以修改，即你可以添加、删除或更新其中的元素。

```kotlin
val numbers = setOf(1, 2, 3)
numbers.add(4) // [1]
```
__[1]__ 会抛出错误，因为 `Set` 是_只读的_。

要创建一个可修改的集合，请使用 `mutableSetOf` 关键字
```kotlin
val numbers = mutableSetOf(1, 2, 3)
numbers.add(4)
println(numbers)
// prints [1, 2, 3, 4]
```

---

最常见的 `Set` 操作是使用 `in` 或 `contains()` 来测试成员资格。

```kotlin
val numbers = setOf(1, 2, 3)
println(2 in numbers) // prints true
println(numbers.contains(5)) // prints false
```

如上所示，`in` 和 `contains` 返回一个 `Bool` 值，表示传入的元素是否存在于集合中。

---

`Set` 中元素的顺序并不重要。
事实上，如果你尝试比较两个包含相同元素但顺序不同的 `Set`，你会发现它们是相等的。

---

在 `Set` 上，你可以执行多种操作，如并集、交集、差集和子集检查。

```kotlin
val firstNumbers = setOf(1, 2, 3)
val lastNumbers = setOf(3, 4, 5)
val union = firstNumbers.union(lastNumbers) // [1, 2, 3, 4, 5]
val intersection = firstNumbers intersect lastNumbers // [3]
val difference = firstNumbers subtract lastNumbers // [1, 2]
val subset = firstNumbers.containsAll(lastNumbers) // false
```

---

要将 `Set` 转换为 `List`，我们可以使用 `toList()` 函数。
