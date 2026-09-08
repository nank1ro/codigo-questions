**闭包**是一段可以传递并在之后调用的代码块，就像一个没有名字的函数。
完整的闭包表达式语法把参数和返回类型放在花括号内，后面跟着关键字 `in` 和函数体：
```swift
{ (parameters) -> ReturnType in
    body
}
```
和其他值一样，闭包可以存储在一个常量中，然后通过该常量的名字来调用：
```swift
let greet = { (name: String) -> String in
    return "Hello, \(name)!"
}
print(greet("Ada")) // Hello, Ada!
```

---

在闭包内写出每一个类型通常是不必要的。当常量拥有明确的**函数类型**时，Swift 会推断参数和返回值的类型，所以在 `in` 之前你只需要列出参数名：
```swift
let triple: (Int) -> Int = { n in
    return n * 3
}
```
类型 `(Int) -> Int` 读作"一个接收 `Int` 并返回 `Int` 的函数"。
当函数体是单个表达式时，`return` 关键字也可以省略，这被称为**隐式返回**：
```swift
let triple: (Int) -> Int = { n in n * 3 }
print(triple(4)) // 12
```

---

Swift 更进一步：在闭包内部，你可以使用**简写参数名称** `$0`、`$1`、`$2` 等来引用参数，而无需声明任何参数或使用 `in` 关键字。
`$0` 是第一个参数，`$1` 是第二个：
```swift
let add: (Int, Int) -> Int = { $0 + $1 }
print(add(2, 3)) // 5
```
类型仍然来自注解 `(Int, Int) -> Int`。

---

由于闭包是值，函数可以接受闭包作为参数。参数类型就是这个函数类型：
```swift
func apply(_ n: Int, _ operation: (Int) -> Int) -> Int {
    return operation(n)
}
print(apply(5, { $0 + 1 })) // 6
```
函数 `apply` 并不知道 `operation` 做了什么，它只知道 `operation` 接收一个 `Int` 并返回一个 `Int`，然后像调用其他函数一样调用它。

---

当闭包是函数的**最后一个**参数时，你可以把它写在调用的右括号之后。这就是**尾随闭包**语法：
```swift
print(apply(5) { $0 + 1 }) // 6
```
如果闭包是唯一的参数，括号甚至可以完全省略：
```swift
func run(_ task: () -> Int) -> Int {
    return task()
}
print(run { 42 }) // 42
```
两种写法调用的是完全相同的函数，当闭包较长时，尾随语法只是更便于阅读。

---

闭包在接收闭包作为参数的数组方法中大放异彩。`map` 会对每个元素调用闭包，并返回一个包含结果的新数组：
```swift
let nums = [1, 2, 3]
let doubled = nums.map { $0 * 2 }
print(doubled) // [2, 4, 6]
```
原数组不会被改变。因为 `map` 只接收一个闭包参数，所以尾随闭包语法是调用它的常见方式。

---

`filter` 只保留闭包返回 `true` 的元素。闭包接收一个元素，并且必须返回一个 `Bool`：
```swift
let nums = [5, 12, 8, 20]
let big = nums.filter { $0 > 10 }
print(big) // [12, 20]
```
元素保持原有的顺序，结果是一个元素类型相同的新数组。

---

`reduce` 把所有元素合并成一个值。它接收一个初始值和一个带两个参数的闭包：目前累积的值和当前元素。闭包返回新的累积值：
```swift
let nums = [1, 2, 3, 4]
let product = nums.reduce(1) { $0 * $1 }
print(product) // 24
```
这里 `$0` 最初是 `1`，然后依次变为 `1 * 1`、`1 * 2`、`2 * 3`，最后是 `6 * 4`。
因为 `map`、`filter` 和 `reduce` 都会返回值，所以它们可以链式调用：`nums.filter { $0 > 1 }.map { $0 * 10 }`。

---

`sorted(by:)` 返回一个新的已排序数组。闭包接收两个元素，当第一个应该排在第二个**前面**时返回 `true`：
```swift
let nums = [3, 1, 2]
print(nums.sorted { $0 < $1 }) // [1, 2, 3]
print(nums.sorted { $0 > $1 }) // [3, 2, 1]
```
闭包可以比较任何内容，例如 `words.sorted { $0.count < $1.count }` 会把字符串按从短到长排序。
