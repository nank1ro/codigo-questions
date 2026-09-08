**数组**在一个变量名下存储固定数量的相同类型的值。
你可以用 `arrayOf` 创建数组，用方括号和从 `0` 开始的**索引**读取元素，并用 `size` 获取元素数量：
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
最后一个元素的索引是 `size - 1`。

---

`arrayOf(1, 2, 3)` 创建一个 `Array<Int>`，其中每个元素都是装箱对象。
对于基本类型，Kotlin 提供了专用且更高效的类型，例如 `IntArray`、`DoubleArray` 和 `BooleanArray`：
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
你也可以用一个接收每个索引的**初始化**（init）lambda 来构建指定大小的数组，或者使用填满零的 `IntArray`：
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

每个数组都有两个用于处理索引的实用属性：
- `indices` 是有效索引的范围，从 `0` 到最后一个
- `lastIndex` 是最后一个元素的索引，也就是 `size - 1`
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

即使数组用 `val` 声明，也可以通过对某个索引赋值来替换它的**元素**：
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
要遍历每个元素，可以使用 `for` 循环或 `forEach`：
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
注意 `n` 和 `it` 是值的只读副本，不能被重新赋值，因此要修改元素需要用到它们的索引。

---

要检查数组是否包含某个值，使用 `in` 或 `contains`，两者都返回 `Boolean`。
`indexOf` 返回第一次出现的索引，如果值不存在则返回 `-1`：
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

直接打印数组并不会显示它的元素，而是打印类似 `[Ljava.lang.String;@1b6d3586` 的内容。
使用 `joinToString` 构建可读的字符串，可以选择自定义分隔符（默认是 `", "`），或者使用 `contentToString` 获取方括号中的元素：
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

数组可以**原地**排序，也可以复制到一个新的已排序集合中：
- `sort()` 和 `sortDescending()` 重新排列数组本身，不返回任何内容
- `reverse()` 翻转数组本身的顺序
- `sorted()`、`sortedDescending()` 和 `reversed()` 不改变原数组，返回一个新的 `List`
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

数值数组自带聚合函数：
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()` 和 `min()` 在空数组上会抛出异常，如果数组可能为空，请使用 `maxOrNull()` 和 `minOrNull()`。

---

数组和 `MutableList` 的主要区别在于数组具有**固定大小**：创建后你可以替换它的元素，但永远不能添加或删除元素，没有 `add` 函数。
像 `nums + 4` 这样的表达式不会让 `nums` 变大，而是构建一个全新的数组：
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
当元素数量会随时间变化时，优先使用 `MutableList`；当元素数量事先已知，或者需要基本类型的性能时，优先使用数组。

---

数组支持和列表相同的转换函数。`filter` 保留满足条件的元素，`map` 转换每个元素。
两者都返回一个新的 `List`，而不是数组：
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
由于结果是一个列表，直接打印它会显示它的元素。

---

当循环中既需要索引又需要值时，使用 `withIndex()` 并解构每一对，或者使用 `forEachIndexed`：
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

数组和列表可以很方便地相互转换：
- `toList()` 和 `toMutableList()` 把数组复制到列表
- `toTypedArray()` 把列表复制到 `Array<T>`
- `toIntArray()` 把 `Int` 列表复制到 `IntArray`
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
每次转换都会创建一个**副本**，因此修改结果不会影响原始数据。

---

与列表不同，两个具有相同元素的数组用 `==` 比较**不**相等：数组按引用比较，所以只有对同一个数组对象，`==` 才是 `true`。
要比较内容，请使用 `contentEquals`：
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

由于数组的大小是固定的，取数组的一部分意味着创建一个新数组：
- `copyOf()` 复制整个数组，`copyOf(n)` 复制前 `n` 个元素
- `copyOfRange(from, to)` 复制从索引 `from` 到 `to`（**不包含**）的元素
- `sliceArray(range)` 复制该范围索引处的元素，两端都包含在内
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
