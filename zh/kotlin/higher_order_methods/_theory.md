**高阶方法**是接收一个函数作为参数的方法。Kotlin 集合提供了很多这样的方法，而你传入的函数通常是一个 **lambda**：写在花括号之间的小型匿名函数。
`map` 是最常见的一个：它对每个元素调用 lambda，并返回一个包含结果的**新列表**，原列表保持不变：
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map { it * 2 }
println(doubled) // [2, 4, 6]
println(numbers) // [1, 2, 3]
```
当 lambda 只有一个参数时，你不需要声明它：Kotlin 把它命名为 `it`。lambda 写在方法名之后、圆括号之外，而当 lambda 是唯一的参数时圆括号可以省略。这就是 **trailing lambda** 语法，本主题的每个练习都会用到它。

---

`filter` 接收一个返回 `Boolean` 的 lambda，称为**谓词**，并返回一个只包含谓词为 `true` 的元素的新列表：
```kotlin
val numbers = listOf(4, -2, 7, 0)
println(numbers.filter { it > 0 }) // [4, 7]
```
你可以给参数起一个名字来代替 `it`，名字后面跟一个箭头 `->`。命名参数让较长的 lambda 更易读，而且当一个 lambda 嵌套在另一个里面时必须命名，因为内层的 `it` 会遮蔽外层的元素：
```kotlin
val minLength = 4
val words = listOf("fig", "banana", "kiwi")
println(words.filter { word -> word.length >= minLength }) // [banana, kiwi]
```

---

`forEach` 对每个元素执行一次 lambda，并且不返回任何值。它是 `for` 循环的高阶替代方案，用于打印之类的副作用：
```kotlin
listOf("a", "b").forEach { println(it) }
```
`forEachIndexed` 还会给出每个元素的位置。它的 lambda 有**两个**参数，因此必须命名：`it` 只存在于恰好有一个参数的 lambda 中。
```kotlin
listOf("a", "b").forEachIndexed { index, letter ->
    println("$index: $letter") // 先 0: a，然后 1: b
}
```

---

`reduce` 把所有元素合并成一个值。它的 lambda 接收两个参数：**累加器**（到目前为止的结果）和下一个元素。它以第一个元素作为累加器开始，并对其余每个元素执行 lambda：
```kotlin
val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n }) // 10
```
`reduce` 在空列表上会抛出异常，因为没有可以作为起点的第一个元素。`fold` 解决了这个问题：你把累加器的**初始值**作为参数传入，lambda 会对每个元素执行，包括第一个：
```kotlin
println(numbers.fold(0) { acc, n -> acc + n })   // 10
println(listOf<Int>().fold(0) { acc, n -> acc + n }) // 0
```
使用 `fold` 时，累加器甚至可以是与元素不同的类型，例如用一个数字列表构建一个 `String`。

---

有些高阶方法回答关于集合的问题，而不是构建一个新集合。它们都接收一个谓词：
- 如果**至少有一个**元素满足谓词，`any` 返回 `true`
- 如果**每个**元素都满足谓词，`all` 返回 `true`
- 如果**没有**元素满足谓词，`none` 返回 `true`
- `count` 返回满足谓词的元素**有多少个**
```kotlin
val numbers = listOf(1, 2, 3)
println(numbers.any { it > 2 })   // true
println(numbers.all { it > 2 })   // false
println(numbers.none { it > 2 })  // false
println(numbers.count { it > 1 }) // 2
```
在空列表上 `any` 返回 `false`，而 `all` 和 `none` 返回 `true`：没有任何元素会破坏这条规则。

---

聚合方法把整个集合变成一个值：
- `sum()` 把一个数字列表相加，而 `sumOf` 把 lambda 为每个元素计算出的值相加
- `maxByOrNull` 和 `minByOrNull` 返回让 lambda 得到最大或最小值的那个**元素**，在空列表上返回 `null`
```kotlin
val words = listOf("fig", "banana", "kiwi")
println(words.sumOf { it.length })      // 13
println(words.minByOrNull { it.length }) // fig
println(listOf(1, 2, 3).sum())           // 6
```
注意它与 `maxOf { it.length }` 的区别，后者返回最大的**值**（`6`），而不是产生该值的元素。

---

`sortedBy` 返回一个新列表，按 lambda 为每个元素计算出的值从小到大排序。`sortedByDescending` 则从大到小排序。当你要比较的就是元素本身时，`sorted()` 和 `sortedDescending()` 不需要 lambda：
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })            // [fig, kiwi, banana]
println(words.sortedByDescending { it.length })  // [banana, kiwi, fig]
println(words.sorted())                          // [banana, fig, kiwi]
```
排序是**稳定的**：键相同的元素保持它们原来的相对顺序。原列表永远不会被修改。

---

`take(n)` 返回一个包含前 `n` 个元素的新列表，`drop(n)` 返回一个**不含**前 `n` 个元素的新列表。它们都不接收 lambda，但常常链接在接收 lambda 的方法之后：
```kotlin
val numbers = listOf(5, 3, 8, 1)
println(numbers.take(2))                    // [5, 3]
println(numbers.drop(2))                    // [8, 1]
println(numbers.sortedDescending().take(2)) // [8, 5]
```
`takeWhile` 和 `dropWhile` 是带谓词的版本：它们从开头开始，**只要**谓词为 `true` 就一直取用或丢弃元素，并在第一个不满足谓词的元素处停止：
```kotlin
println(numbers.takeWhile { it > 2 }) // [5, 3, 8]
```

---

`groupBy` 把一个集合分成一个 `Map`：lambda 计算每个元素的**键**，每个键对应产生它的那些元素组成的列表，并保持原来的顺序：
```kotlin
val words = listOf("fig", "kiwi", "pear")
val byLength = words.groupBy { it.length }
println(byLength)    // {3=[fig], 4=[kiwi, pear]}
println(byLength[4]) // [kiwi, pear]
```
结果的类型是 `Map<K, List<T>>`，其中 `K` 是 lambda 返回的类型，`T` 是元素的类型。键按第一次出现的顺序排列。

---

当 lambda 为每个元素返回一个**列表**时，`map` 会产生一个列表的列表。`flatMap` 做同样的事，但随后把所有这些列表合并成一个扁平的列表：
```kotlin
val numbers = listOf(1, 2)
println(numbers.map { listOf(it, -it) })     // [[1, -1], [2, -2]]
println(numbers.flatMap { listOf(it, -it) }) // [1, -1, 2, -2]
```
顺序会被保留：第一个元素产生的所有值排在前面，然后是第二个元素的，以此类推。如果你已经有一个列表的列表，`flatten()` 不需要 lambda 就能把它们合并。

---

`zip` 按位置逐个配对两个列表的元素。不带 lambda 时它返回一个 `Pair` 值的列表，两半分别用 `.first` 和 `.second` 读取；带 lambda 时，每个位置上的两个元素会传给它，结果收集到一个列表中：
```kotlin
val names = listOf("Ann", "Bob")
val ages = listOf(31, 25)
println(names.zip(ages))                            // [(Ann, 31), (Bob, 25)]
println(names.zip(ages) { name, age -> "$name:$age" }) // [Ann:31, Bob:25]
```
结果的长度等于两个列表中**较短**的那个：较长列表中多出来的元素会被忽略。

---

lambda 的形式必须与方法的期望相匹配：
- 一次处理一个元素的方法（`map`、`filter`、`sortedBy`、`groupBy`……）接收**单参数**的 lambda，其中可以使用 `it`
- `reduce`、`fold`、`forEachIndexed` 以及带 lambda 的 `zip` 会传入**两个**值，因此必须用 `a, b ->` 显式命名参数
```kotlin
val numbers = listOf(1, 2, 3)
numbers.map { it * 2 }                  // 正确：一个参数，it 可用
numbers.reduce { acc, n -> acc + n }    // 正确：两个参数，已命名
numbers.reduce { it + 1 }               // 错误：有两个参数时 it 不存在
```
命名参数始终是允许的，即使只有一个参数：`numbers.map { n -> n * 2 }`。

---

高阶方法可以**链式调用**：每一个都返回一个新集合供下一个使用，因此整个计算读起来就像一条从左到右的流水线：
```kotlin
val words = listOf("kiwi", "fig", "banana", "date")
println(words.filter { it.length == 4 }.map { it.uppercase() }.sorted()) // [DATE, KIWI]
```
map 也有高阶方法。`mapValues` 保留键，并把每个值替换成 lambda 的结果，该 lambda 接收带 `.key` 和 `.value` 的**条目**：
```kotlin
val byLength = words.groupBy { it.length }      // {4=[kiwi, date], 3=[fig], 6=[banana]}
println(byLength.mapValues { it.value.size })   // {4=2, 3=1, 6=1}
```

---

在链式调用中，`it` 的类型在每一步都会变化：在 `List<String>` 上执行 `filter` 之后你仍然拿到字符串，但在 `map { it.length }` 之后你得到的是 `List<Int>`，所以下一个 lambda 看到的是数字。
```kotlin
val words = listOf("kiwi", "fig")
println(words.map { it.length }.filter { it > 3 }) // [4]
```
每一步都返回一个**新**列表，从不改动前一个，因此可以把一条链拆成若干命名的中间值而不改变结果。

---

一个 lambda 里可以包含另一个高阶调用。在内层 lambda 中，`it` 指的是**内层**元素并遮蔽了外层元素，所以要显式命名外层参数，让两者都能访问：
```kotlin
val sales = listOf("north" to 120, "south" to 80, "north" to 30)
val byRegion = sales.groupBy { it.first }
val totals = byRegion.mapValues { entry -> entry.value.sumOf { it.second } }
println(totals) // {north=150, south=80}
```
`"north" to 120` 创建一个 `Pair`。这里外层 lambda 处理 map 的一个条目，而内层 lambda 处理该条目列表中的那些 pair。

---

`Map` 可以像条目列表一样处理：`filter` 和 `map` 直接作用于 map，并接收带 `.key` 和 `.value` 的每个条目。在 map 上 `filter` 返回一个 map，而 `map` 返回一个列表。像 `sortedBy` 这样的排序方法没有为 map 定义：先经过 `scores.entries`，它是这些条目的集合：
```kotlin
val scores = mapOf("Ann" to 90, "Bob" to 72)
println(scores.filter { it.value > 80 })              // {Ann=90}
println(scores.entries.sortedBy { it.value }.map { it.key }) // [Bob, Ann]
```
`scores.entries` 是所有条目的集合；`scores.keys` 和 `scores.values` 只给出其中一边。
