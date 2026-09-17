在 Swift 中，错误是一个**值**，而不是崩溃。任何类型都可以通过遵循 `Error` 协议来充当错误，而枚举是通常的选择，因为它的各个成员恰好能命名可能出问题的地方：
```swift
enum LoginError: Error {
    case wrongPassword
}
```
可能失败的函数会被标记为 `throws`，并用 `throw` 报告失败：
```swift
func login(_ password: String) throws {
    if password != "swift" {
        throw LoginError.wrongPassword
    }
    print("welcome")
}
```
调用这样的函数需要 `try`，并且调用必须位于一个 `do` 代码块内，后面跟着一个 `catch` 代码块，说明失败时要做什么：
```swift
do {
    try login("hunter2")
} catch {
    print("login failed")
}
// 输出 login failed
```
当 `throw` 执行时，`do` 代码块中剩下的部分会被跳过，由 `catch` 接管。不会发生崩溃：程序会从 `catch` 之后继续运行。

---

可抛出错误的函数仍然可以返回值。`throws` 关键字位于参数列表和返回箭头之间：
```swift
func square(_ n: Int) throws -> Int {
    if n < 0 {
        throw SquareError.negative
    }
    return n * n
}
```
把它读出来就是：*square 接收一个 `Int`，可能抛出错误，并返回一个 `Int`*。

在调用处，只有当没有抛出任何错误时值才存在，所以赋值语句位于 `do` 代码块内：
```swift
do {
    let result = try square(4)
    print(result) // 16
} catch {
    print("failed")
}
```
`try` 不是可有可无的装饰：没有它编译器会拒绝这个调用，因此阅读代码的人总能看到哪些行可能失败。

---

不带模式的 `catch` 会以相同的方式处理每一个错误。大多数时候你只想对某个特定的失败作出反应，所以 `catch` 可以携带一个**模式**：即它愿意处理的那个成员：
```swift
do {
    try check("")
} catch ValidationError.empty {
    print("the text is empty")
} catch {
    print("something else")
}
```
Swift 会从上到下依次尝试各个 `catch` 子句，并运行第一个模式匹配的子句。

最后一个 `catch` 是有意不写模式的。带模式的 `catch` 只覆盖它所命名的那个成员，而 Swift 要求每个错误都必须在某处被处理，所以列出了模式的 `do` 代码块需要一个最后的不带模式的 `catch` 来兜住其余的错误。

---

顺序很重要。Swift 会按照书写的顺序把抛出的值与每个 `catch` 模式进行比较，并在第一个匹配处停止，所以放在最前面的不带模式的 `catch` 会吞掉它下面的所有情况。把具体的成员放在顶部，把兜底的 `catch` 放在底部。

不匹配任何模式的错误不会被忽略：它会落入最后那个不带模式的 `catch` 中。

---

错误的成员可以携带数据。给成员提供**关联值**，`throw` 就会填入它们，这样处理代码不仅能知道*什么*失败了，还能知道*差多少*：
```swift
enum ValidationError: Error {
    case tooShort(minimum: Int)
}

throw ValidationError.tooShort(minimum: 8)
```
对应的 `catch` 用 `let` 绑定这些值：
```swift
} catch ValidationError.tooShort(let minimum) {
    print("needs at least \(minimum) characters")
}
```
`let` 后面的名字由你自己选择；它是一个新的常量，只在该 `catch` 代码块内部可用。这样一来，错误就能携带有用的信息，而你不必在失败发生的地方把数字拼进字符串。

---

一个枚举通常包含一项任务可能失败的所有方式，每个原因对应一个成员：
```swift
enum FormError: Error {
    case empty
    case tooLong
}
```
为每个成员写一个 `catch` 会变得重复。更好的做法是一次捕获整个类型，然后对值进行 `switch`：
```swift
} catch let error as FormError {
    switch error {
    case .empty: print("empty")
    case .tooLong: print("too long")
    }
} catch {
    print("unknown")
}
```
`catch let error as FormError` 的意思是*捕获任何属于 `FormError` 的东西，并把它叫作 `error`*。在该代码块内部，`error` 具有这个枚举类型，所以 `switch` 能看到各个成员，并检查你是否覆盖了所有成员。最后那个不带模式的 `catch` 仍然是必需的，因为其他类型的错误也可能到达这个 `do` 代码块。

---

当拒绝条件放在最前面、真正的工作留在底部且不缩进时，验证函数读起来最顺畅。`guard` 正是为此而设计的：它陈述必须成立的条件，当条件不成立时运行它的 `else` 代码块。
```swift
func priceFor(_ quantity: Int) throws -> Int {
    guard quantity > 0 else {
        throw OrderError.notPositive
    }
    return quantity * 3
}
```
`guard` 的 `else` 代码块必须离开当前作用域，`throw` 就是做到这一点的方式之一，与 `return`、`break` 和 `continue` 并列。几个堆叠在函数顶部的 `guard` 读起来就像一份输入必须满足的规则清单。

---

有时候你并不关心调用*为什么*失败，只关心它失败了。`try?` 把一个可抛出错误的调用变成**可选值**：成功时是值，抛出错误时是 `nil`。
```swift
enum ParseError: Error {
    case notANumber
}

func toInt(_ text: String) throws -> Int {
    guard let value = Int(text) else {
        throw ParseError.notANumber
    }
    return value
}

if let number = try? toInt("42") {
    print(number) // 42
}
```
不需要 `do`，也不需要 `catch`：失败被折叠进你已经知道如何解包的可选值中。代价是错误值被丢弃了，所以只有在确实没有任何值得报告的东西时才使用 `try?`。

---

因为 `try?` 产生的是一个可选值，空合运算符 `??` 可以通过提供一个回退值来完成剩下的工作：
```swift
let port = (try? readPort(text)) ?? 8080
```
圆括号很重要。否则 `try?` 会试图覆盖包括 `??` 在内的整个表达式，而编译器要求你明确指出可抛出错误的调用在哪里结束。

把这一行当作一个句子来读：*使用我们成功读取的端口，否则用 8080*。当恢复手段真的只是一个默认值时，两行 `do`/`catch` 就可以折叠成一行。

---

还有第三种形式：`try!`。它告诉编译器*这个调用不可能失败*，因此不需要 `do`，不需要 `catch`，也没有可选值。如果它还是失败了，程序会立即停止。
```swift
let pattern = try! Regex("[0-9]+")
```
这正是 `try!` 站得住脚的场合：参数是你自己在源代码中写下的字面量，如果它写错了，程序本身就是坏的，应该在第一次测试运行时就停下来。

任何在运行时才到达的东西——用户输入的一行文字、一个文件、一个网络响应——都可能以你编写代码时无法察觉的方式出错，对它们使用 `try!` 会把一个可恢复的失败变成用户面前的崩溃。在这些地方请使用 `do`/`catch` 或 `try?`。

---

当函数抛出错误时，`throw` 之后的一切都会被跳过——包括本应关闭文件或释放锁的那一行代码。`defer` 解决了这个问题：它先注册一个代码块，然后在当前作用域结束时运行它，无论作用域以哪种方式结束。
```swift
func load() throws {
    print("open")
    defer { print("close") }
    throw FileError.missing
}
```
这次调用会输出 `open`，然后输出 `close`，只有在那之后错误才会继续传递给调用方。即使函数正常返回，`close` 也照样会输出——这正是它的意义所在。把清理代码紧挨着设置代码放好，再也不用担心代码从哪条路径退出。

---

一个作用域可以注册多个 `defer`。它们以**相反**的顺序运行：最后注册的最先运行。

这不是一条任意的规则。清理通常要按顺序撤销先前按顺序完成的设置——先打开文件，再锁定它——而撤销必须反方向进行：先解锁，再关闭。相反的顺序让每个 `defer` 都成为它上面那一行的镜像。

---

接收闭包的函数有一个问题：它无法知道交给它的闭包是否会抛出错误。把函数标记为 `throws` 会迫使每个调用方都写 `try`，即使是那些传入无害闭包的调用方。`rethrows` 表示*只有你给我的闭包抛出错误时，我才抛出错误*：
```swift
func applyTwice(_ value: Int, _ transform: (Int) throws -> Int) rethrows -> Int {
    return try transform(transform(value))
}
```
在函数体内部你仍然要写 `try`，因为这个调用确实可能失败。而在调用处，编译器会查看你传入的闭包：
```swift
let doubled = applyTwice(3, { (n: Int) -> Int in n * 2 }) // 无需 try
```
标准库到处都在使用这一机制——`map`、`filter` 和 `sorted(by:)` 都是 `rethrows` 的——这就是为什么你在普通的 `map` 前面从来不需要写 `try`。

---

一个 `do` 代码块并不限于一种错误类型。每一步都可能以自己的方式失败，而每种失败都有属于自己的 `catch`：
```swift
do {
    let text = try load(false)
    let value = try parse(text)
    print(value)
} catch NetworkError.offline {
    print("offline")
} catch ParseError.badFormat {
    print("bad format")
} catch {
    print("unknown")
}
```
第一个抛出错误的 `try` 会结束整个代码块，因此后面的步骤永远不会运行——那个值根本就不存在。这正是这种结构易于阅读的原因：一切顺利的路径在顶部保持成一条直线，而所有可能出错的方式都列在下面。

---

`do` 代码块所在的位置决定了一次失败要付出多大代价。把它放在循环**内部**，每个元素就会拥有自己的尝试，这样一个坏值会被跳过，其余的仍会继续运行：
```swift
for age in [4, -1, 7] {
    do {
        print(try label(age))
    } catch {
        print("skipped")
    }
}
```
如果改成把整个循环包在一个 `do` 里，则会在第一个错误处停下，永远到达不了 `7`。两种方式都没有错——区别只在于是*一个坏元素*，还是*直接放弃*。

---

这一章的一切都在回答一个问题：谁来处理这个失败？

一个会抛出错误的函数拒绝回答这个问题。它只是说明出了什么问题——`Error` 枚举的一个成员，携带着处理程序将需要的一切——然后把决定权交给上层。调用方接着挑选一种工具：用 `do`/`catch` 逐个成员做出反应，用 `try?` 和 `??` 退回到一个默认值，用 `defer` 在退出时无论如何都完成清理。

这种分工正是关键所在。检测到问题的函数很少知道接下来该发生什么，而知道该怎么做的代码也很少想重复那个检查。
