**高阶函数**是指接收另一个函数作为参数、返回一个函数，或两者兼备的函数。你已经见过 `map`、`filter`、`reduce` 和 `sorted(by:)`：它们接收一个闭包并将其应用到集合的元素上。Swift 还有更多这样的函数，了解它们可以让你用一行易读的代码取代冗长的循环。
`compactMap` 的工作方式与 `map` 类似，但闭包返回的是可选值，`nil` 结果会被丢弃：
```swift
let words = ["3", "seven", "12"]
let numbers = words.compactMap { Int($0) }
print(numbers) // [3, 12]
```
`Int("seven")` 是 `nil`，因此该元素会消失，结果是一个 `[Int]`，而不是 `[Int?]`。

---

`flatMap` 用于返回**数组**的闭包：它不会构建数组的数组，而是把所有返回的数组合并成一个扁平的结果：
```swift
let teams = [["Ann", "Bob"], ["Cid"]]
print(teams.map { $0 })     // [["Ann", "Bob"], ["Cid"]]
print(teams.flatMap { $0 }) // ["Ann", "Bob", "Cid"]
```
闭包还可以在扁平化之前转换每个内部数组，例如 `teams.flatMap { $0.reversed() }` 会得到 `["Bob", "Ann", "Cid"]`。

---

三个 `map` 变体只在闭包返回的内容上有所不同：
- `map`：任意值，每个元素对应一个结果
- `compactMap`：可选值，`nil` 结果会被丢弃
- `flatMap`：数组，所有结果被合并成一个数组

传递给 `flatMap` 的闭包本身可以对内部数组调用 `map`，把一个变换嵌套在另一个变换之内：
```swift
let matrix = [[1, 2], [3]]
print(matrix.flatMap { row in row.map { $0 + 1 } }) // [2, 3, 4]
```

---

`reduce` 在每一步都会构建一个新的累加值，当结果是数组或字典时这很浪费。`reduce(into:)` 把累加器作为 `inout` 参数传递给闭包，因此可以直接原地修改，无需 `return`：
```swift
let words = ["a", "b", "a"]
let counts = words.reduce(into: [String: Int]()) { result, word in
    result[word, default: 0] += 1
}
print(counts["a"]!) // 2
```
`[String: Int]()` 创建一个空字典，`result[word, default: 0]` 读取当前计数，当键不存在时读取 `0`。

---

有些高阶函数回答关于集合的问题，而不是转换集合。它们都接收一个返回 `Bool` 的闭包：
- `first(where:)` 返回第一个满足闭包的元素，如果没有则返回 `nil`
- `contains(where:)` 如果至少有一个元素满足它，则返回 `true`
- `allSatisfy` 如果所有元素都满足它，则返回 `true`

```swift
let nums = [4, 9, 16]
print(nums.first(where: { $0 > 5 }))  // Optional(9)
print(nums.contains(where: { $0 > 5 })) // true
print(nums.allSatisfy { $0 > 5 })       // false
```
与 `filter` 不同，`first(where:)` 在第一个匹配处停止，并且不会构建新数组。

---

`contains(where:)` 和 `allSatisfy` 取代了使用循环加标志变量的常见模式。两者都会在答案确定时立即停止：`contains(where:)` 在第一个匹配处停止，`allSatisfy` 在第一个不满足的元素处停止。
```swift
let ages = [15, 22, 40]
let anyMinor = ages.contains { $0 < 18 }  // true
let allAdults = ages.allSatisfy { $0 >= 18 } // false
```
`contains { ... }` 是 `contains(where:)` 的尾随闭包形式，不要与查找特定值的 `contains(_:)` 混淆。

---

高阶函数可以作用于任何数组，包括你自己结构体的数组。先链接 `filter` 再链接 `map` 是筛选元素并从每个元素中提取值的常用方式：
```swift
struct Book {
    var title: String
    var pages: Int
}
let books = [Book(title: "Dune", pages: 412), Book(title: "Haiku", pages: 40)]
let long = books.filter { $0.pages > 100 }.map { $0.title }
print(long) // ["Dune"]
```
以相反的顺序进行，先 `map` 再 `filter`，会在检查使用 `pages` 属性之前就丢失它。

---

当闭包只读取一个属性时，你可以改为传递一个**键路径**：`\.name` 表示"元素的 `name` 属性"，`map(\.name)` 与 `map { $0.name }` 相同。
按属性排序使用常见的双参数闭包，比较两个元素上的该属性：
```swift
struct City {
    var name: String
    var population: Int
}
let cities = [City(name: "Oslo", population: 700), City(name: "Rome", population: 2800)]
let byPopulation = cities.sorted { $0.population > $1.population }
print(byPopulation.map(\.name)) // ["Rome", "Oslo"]
```

---

要按**多个标准**排序，先比较第一个属性，只有当第一个值相等时才退回到第二个属性：
```swift
let sorted = people.sorted {
    if $0.age != $1.age {
        return $0.age < $1.age
    }
    return $0.name < $1.name
}
```
这里人们按年龄排序，年龄相同的人按名字排序。闭包只有当第一个元素应该排在第二个元素之前时才返回 `true`，因此相等的情况会落到下一个比较。

---

`enumerated()` 把数组转换成一系列 `(offset, element)` 对，因此闭包可以同时使用每个元素的位置和它的值：
```swift
let steps = ["mix", "bake"]
let numbered = steps.enumerated().map { pair in
    "\(pair.offset + 1). \(pair.element)"
}
print(numbered) // ["1. mix", "2. bake"]
```
由于每一对都是一个元组，闭包还可以对它进行解构：`.map { (i, step) in "\(i + 1). \(step)" }`。

---

`zip` 按位置逐个配对两个序列的元素，产生一个元组序列。它在较短的那个序列末尾停止：
```swift
let names = ["Ann", "Bob"]
let ages = [31, 27, 99]
let pairs = zip(names, ages).map { "\($0) is \($1)" }
print(pairs) // ["Ann is 31", "Bob is 27"]
```
在闭包内部，`$0` 是来自第一个序列的元素，`$1` 是来自第二个序列的元素。`zip` 是一个自由函数，而不是方法：你写的是 `zip(a, b)`，而不是 `a.zip(b)`。

---

`forEach` 是 `for-in` 循环的高阶孪生兄弟：它按顺序对每个元素调用一次闭包。区别在于你如何离开循环。在 `for-in` 中你可以 `break` 跳出或 `continue`；在 `forEach` 闭包内不允许使用 `break` 和 `continue`，`return` 只会结束闭包的**当前调用**，然后下一个元素照常被处理：
```swift
[1, 2, 3].forEach { n in
    if n == 2 { return }
    print(n)
}
// prints 1 and 3
```
当需要对每个元素做一个简短的副作用时使用 `forEach`，当需要提前停止时使用 `for-in`。

---

`Dictionary(grouping:by:)` 把一个集合拆分成一个由数组组成的字典。闭包计算每个元素的**键**，所有具有相同键的元素最终进入同一个数组：
```swift
let words = ["apple", "bee", "avocado"]
let byInitial = Dictionary(grouping: words, by: { $0.first! })
print(byInitial["a"]!) // ["apple", "avocado"]
```
`mapValues` 在保留键的同时转换字典的每个值，因此它是分组之后的自然下一步：
```swift
let sizes = byInitial.mapValues { $0.count }
print(sizes["a"]!) // 2
```

---

`prefix(while:)` **只要**闭包返回 `true` 就从开头取元素，并在第一个不满足的元素处停止，即使后面的元素会再次满足。`drop(while:)` 是它的互补：它跳过同样的开头一段，返回其余所有元素：
```swift
let temps = [12, 15, 21, 14]
print(temps.prefix { $0 < 20 }) // [12, 15]
print(temps.drop { $0 < 20 })   // [21, 14]
```
两者都返回一个 `ArraySlice`，它是原始数组的一个视图，打印起来像数组，并且可以用 `Array(...)` 转换成数组。

---

你可以编写自己的高阶函数。接收一个闭包并**返回一个由它构建的新闭包**的函数是一种常见模式：返回的闭包捕获了原始闭包，因此参数必须是 `@escaping` 的。
例如，`negate` 把一个谓词变成它的相反面，准备好被传递给 `filter`：
```swift
func negate(_ predicate: @escaping (Int) -> Bool) -> (Int) -> Bool {
    return { !predicate($0) }
}
let isEven: (Int) -> Bool = { $0 % 2 == 0 }
print([1, 2, 3, 4].filter(negate(isEven))) // [1, 3]
```
注意 `filter(negate(isEven))` 把闭包作为普通参数传递，没有使用尾随闭包语法。

---

数组上的 `map` 和 `filter` 是**急切**的：每一步都会处理整个数组并构建一个新数组，然后下一步才会运行。在大型集合上，或者当你只需要第一个结果时，这就是浪费的工作。
`lazy` 属性返回一个视图，其操作只有当元素真正被请求时才会运行，整个链条一次处理一个元素：
```swift
let firstBig = (1...1000).lazy.map { $0 * $0 }.first { $0 > 50 }
print(firstBig!) // 64
```
这里只有 `1, 2, ..., 8` 被平方：`first(where:)` 请求元素直到有一个满足条件，链条就在那里停止。如果没有 `lazy`，`map` 会先把全部 1000 个数字都平方。
