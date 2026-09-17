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

---

闭包可以使用在其函数体外部声明的变量。它会**捕获**这些变量：只要闭包存在，该变量就会持续存在，即使声明它的函数已经返回。
这让函数可以构建一个拥有自己私有状态的闭包：
```swift
func makeCounter() -> () -> Int {
    var count = 0
    return {
        count += 1
        return count
    }
}
```
`() -> Int` 是一个不接收参数并返回 `Int` 的闭包类型。每次调用返回的闭包都会递增同一个被捕获的 `count`：
```swift
let counter = makeCounter()
print(counter()) // 1
print(counter()) // 2
```

---

返回一个闭包是构建定制函数的便捷方式。外层函数的参数会被它返回的闭包捕获：
```swift
func makeAdder(_ amount: Int) -> (Int) -> Int {
    return { $0 + amount }
}
let addFive = makeAdder(5)
print(addFive(10)) // 15
```
返回类型 `(Int) -> Int` 描述了这个闭包，简写 `$0` 指的是这个闭包的参数，而不是 `makeAdder` 的参数。

---

存储在常量中的闭包可以在任何需要闭包参数的地方传递，使用该参数的参数标签：
```swift
let ascending = { (a: Int, b: Int) -> Bool in a < b }
print([3, 1, 2].sorted(by: ascending)) // [1, 2, 3]
```

---

每次调用返回闭包的函数都会创建一个**新的**被捕获变量。由不同调用创建的两个闭包不会共享它们的状态：
```swift
let first = makeCounter()
let second = makeCounter()
print(first())  // 1
print(first())  // 2
print(second()) // 1
```
状态只在同一个闭包的多次调用之间共享。

---

默认情况下，传递给函数的闭包只能在该函数运行期间使用。如果函数存储了这个闭包，或者返回了另一个使用它的闭包，那么这个闭包就会**逃逸**出该函数，它的参数必须标记为 `@escaping`：
```swift
func twice(_ task: @escaping () -> Int) -> () -> Int {
    return { task() * 2 }
}
let answer = twice { 21 }
print(answer()) // 42
```
如果不加 `@escaping`，编译器会报错，因为返回的闭包会在 `twice` 执行结束之后才使用 `task`。

---

闭包可以像其他值一样存储在数组中。元素类型就是函数类型：
```swift
let steps: [(Int) -> Int] = [{ $0 + 1 }, { $0 * 10 }]
print(steps[1](3)) // 30
```
遍历这样的数组并依次调用每个闭包，就构建出了一个小型的转换**流水线**（pipeline）。
