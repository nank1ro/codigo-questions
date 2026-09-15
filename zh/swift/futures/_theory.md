有些工作不会立即完成：下载文件、读取数据库、等待计时器。如果程序只是停下来干等，期间就无法发生任何其他事情。Swift 用**异步函数**来解决这个问题。

标记了 **`async`** 的函数允许在中途暂停并稍后恢复。这个关键字写在参数列表之后、箭头之前：
```swift
func fetchNumber() async -> Int {
    return 42
}
```
调用方式也不同：必须在调用前面写上 **`await`**。`await` 标记出程序可能暂停的确切位置，并在函数完成后把普通的值交给你：
```swift
let n = await fetchNumber()
print(n)
// 输出 42
```
在 Swift 脚本中，顶层代码已经支持 `await`，因此可以直接调用异步函数，无需任何额外设置。忘记写 `async` 或 `await` 会导致编译错误，而不是一个悄无声息的 bug。

---

异步函数仍然是普通的函数：它可以接收参数并返回任何类型的值。只有两处变化：签名中的 `async` 关键字，以及每个调用处的 `await`：
```swift
func price(of quantity: Int) async -> Double {
    return Double(quantity) * 2.5
}

let total = await price(of: 4)
print(total)
// 输出 10.0
```
返回的值是一个普通的 `Double`，而不是包装类型：`await` 结束之后，你就可以像往常一样使用它。

---

异步函数通常建立在其他异步函数之上。在 `async` 函数内部，你可以 `await` 任何其他 `async` 函数，其结果可以像普通值一样使用：
```swift
func base() async -> Int {
    return 10
}

func withBonus() async -> Int {
    let value = await base()
    return value + 5
}

print(await withBonus())
// 输出 15
```
`await` 只能在异步上下文中使用：`async` 函数内部，或脚本的顶层。普通的、非 `async` 的函数不能 `await` 任何东西。

---

随着时间进行的工作经常会失败：服务器宕机、文件丢失、输入有误。这样的函数会标记为 **`async throws`**，并使用 **`try await`** 来调用：
```swift
enum LoadError: Error {
    case missing
}

func load(_ name: String) async throws -> String {
    if name.isEmpty {
        throw LoadError.missing
    }
    return "file: \(name)"
}
```
要处理错误，需要把调用包在 `do` 块中并捕获它：
```swift
do {
    let text = try await load("")
    print(text)
} catch {
    print("could not load")
}
// 输出 could not load
```
关键字的顺序是固定的：先写 `try`，再写 `await`。

---

当你不关心调用*为什么*失败时，`try?` 比 `do` 块更简短。它把一个可抛出错误的调用变成**可选值**：成功时是值，失败时是 `nil`。与 `await` 结合时写作 `try? await`：
```swift
let value = try? await parse("42")  // Optional(42)
let broken = try? await parse("x")  // nil
```
由于结果是一个可选值，可以直接放进 `if let` 中：
```swift
if let value = try? await parse("x") {
    print(value)
} else {
    print("not a number")
}
```
需要快速回退时用 `try? await`，当错误本身很重要时用 `do` / `catch`。

---

依次写下的多个 `await` 调用会**顺序执行**：第二个调用要等第一个返回后才会开始。代码自上而下阅读，与普通代码完全一样：
```swift
func step(_ name: String) async -> String {
    print("start \(name)")
    return "done \(name)"
}

let a = await step("A")
print(a)
let b = await step("B")
print(b)
// start A
// done A
// start B
// done B
```
当第二个调用需要第一个调用的结果时，这正是你想要的行为。当各调用相互独立时，先等一个再开始另一个是浪费时间，接下来的练习会展示如何避免这一点。

---

要同时运行两个独立的调用，用 **`async let`** 来声明它们。工作立即开始，程序不等待而继续往下走：
```swift
async let left = step("A")
async let right = step("B")
```
值还没有就绪，因此不能直接使用这个绑定：必须在你最终需要它的地方 `await` 它。在表达式前面写一个 `await`，就能覆盖其中的每个 `async let`：
```swift
let both = await left + right
```
如果每个调用耗时一秒，顺序版本需要两秒，而 `async let` 版本只需要大约一秒，因为两个调用是重叠的。

---

当你需要分别拿到各个结果时，把多个 `async let` 绑定收集到一个元组中，然后一次性 `await` 整个元组：
```swift
async let city = fetchCity()
async let country = fetchCountry()
let (a, b) = await (city, country)
```
两个调用都已经在运行了；唯一的 `await` 会等到两者中较慢的那个完成。记住 `async let` 只是启动工作：从未被 await 的 `async let` 会在作用域结束时被取消并被隐式地 await。

---

`async let` 与它所在的作用域绑定在一起。要启动并发工作并保留对它的句柄，请使用 **`Task`**。传给 `Task { }` 的闭包独立运行，任务可以被存储、传递或返回：
```swift
let job = Task {
    return await double(21)
}
```
结果之后用 **`.value`** 读取，读取时需要 await：
```swift
print(await job.value)
// 输出 42
```
句柄的类型说明了它产生什么值以及可能抛出什么错误：`Task<Int, Never>` 是一个返回 `Int` 且永不抛出错误的任务。与 `async let` 不同，`Task` 可以在普通的、非异步的代码中创建。

---

`Task.sleep` 让当前任务暂停一段时间，同时不阻塞任何其他任务。它可以被中断，因此它是一个可抛出错误的异步调用，需要 `try await`。时长用 `.seconds`、`.milliseconds` 或 `.nanoseconds` 之类的辅助量来表示：
```swift
func slowGreeting() async throws -> String {
    try await Task.sleep(for: .milliseconds(50))
    return "hello"
}
```
这是在示例中模拟慢操作的标准方式，用来代替真正的网络调用。注意它不会冻结程序：当一个任务在睡眠时，其他任务仍在继续运行。

---

现在顺序与并发之间的差别可以测量了。假设 `work` 在返回之前睡眠一秒：
```swift
func work(_ n: Int) async -> Int {
    try? await Task.sleep(for: .seconds(1))
    return n
}
```
逐个 await 这些调用大约需要 **两** 秒，因为第二次睡眠要等第一次结束才会开始：
```swift
let a = await work(1)
let b = await work(2)
```
用 `async let` 启动它们大约只需要 **一** 秒，因为两次睡眠是重叠的：
```swift
async let a = work(1)
async let b = work(2)
let sum = await a + b
```
把 `await work(1) + await work(2)` 写在一行里不会带来任何改变：两个调用仍然会依次求值。并发来自 `async let` 或任务，而不是来自这一行的书写方式。

---

`async let` 适用于编写代码时就知道调用数量的情况。对于大小只有在运行时才知道的列表，请使用**任务组**。

`withTaskGroup(of:)` 打开一个组，`addTask` 为每个条目启动一个子任务，然后用 `for await` 读取该组，结果一完成就会被送来：
```swift
let total = await withTaskGroup(of: Int.self) { group in
    for n in numbers {
        group.addTask {
            return await square(n)
        }
    }
    var sum = 0
    for await value in group {
        sum += value
    }
    return sum
}
```
`of: Int.self` 声明了每个子任务返回什么。整个 `withTaskGroup` 调用是一个表达式，因此在它前面需要一个 `await`，并且它会等到所有子任务完成后才返回。

---

任务组会按照**完成的顺序**把结果交给你，而不是任务添加时的顺序。最快的子任务最先到达，因此把值收集到数组中会得到不可预测的顺序。

当顺序很重要时有两种解决办法。如果这些值可以简单地重新排序，就在最后对它们排序：
```swift
return values.sorted()
```
如果每个结果对应一个位置，就让每个任务返回一个 `(index, value)` 对，并把它写入一个预先准备好的数组：
```swift
for (index, word) in words.enumerated() {
    group.addTask {
        return (index, await lengthOf(word))
    }
}
var result = Array(repeating: 0, count: words.count)
for await (index, value) in group {
    result[index] = value
}
```
求和、求最大值或计数则两种办法都不需要，因为值的顺序不会改变答案。
