有时候一个值就是缺失的：用户没有中间名、搜索没有找到任何结果、文本无法转换成数字。
Swift 用 `nil` 表示缺失的值，但普通变量永远不能持有它：
```swift
var age: Int = nil // error: 'nil' cannot initialize type 'Int'
```
要允许出现缺失的值，你需要在类型后面加上问号 `?` 来声明一个**可选**类型。
`Int?` 可以持有一个 `Int`，也可以持有 `nil`：
```swift
var age: Int? = 30
age = nil // 允许
```
声明时没有赋值的可选变量，其初始值为 `nil`。

---

你可以用 `==` 和 `!=` 把一个可选值和 `nil` 进行比较，也可以直接把它和被包装类型的普通值进行比较：
```swift
var score: Int? = 10
print(score == nil) // false
print(score == 10)  // true
```
记住 `Int?` 和 `Int` 是两种不同的类型：`Int?` 可能为空，`Int` 永远不会为空。

---

可选值就像一个盒子：在使用里面的值之前，你必须先把它打开，Swift 把这个过程称为**解包**。
最快的方式是使用感叹号 `!` 进行**强制解包**：
```swift
let score: Int? = 10
print(score! + 5) // 15
```
`!` 告诉 Swift“我确定这里有一个值”。如果你错了，可选值实际上是 `nil`，程序会立即崩溃并报出运行时错误：
```swift
let missing: Int? = nil
print(missing! + 5) // Fatal error: Unexpectedly found nil
```
这就是为什么强制解包被认为是危险的：只有在确定值一定存在时才使用它。

---

只有在已经确认可选值不是 `nil` 之后，强制解包才是安全的：
```swift
if score != nil {
    print(score! * 2)
}
```

---

先检查是否为 `nil`，再强制解包，这样写很啰嗦。Swift 提供了 `if let` 形式的**可选绑定**，它能一步完成解包并把值存入一个新的常量：
```swift
let score: Int? = 10
if let value = score {
    print("Score: \(value)") // value 是 Int，不是 Int?
} else {
    print("No score")
}
```
`if` 的代码体只在可选值包含值时才会执行；在其内部，`value` 是一个普通的 `Int`，不需要 `!`。

---

当缺失的值意味着“到此为止”时，`guard let` 比 `if let` 更清晰。
它会解包可选值，如果失败，就执行 `else` 代码块，该代码块必须退出当前作用域（使用 `return`、`break`、`continue` 或 `throw`）：
```swift
func greet(_ name: String?) {
    guard let name = name else {
        print("Nobody here")
        return
    }
    print("Hello, \(name)!") // 从这里开始 name 是 String
}
```
与 `if let` 不同的是，解包后的常量在函数其余部分依然可用，因此主路径不需要嵌套在 `if` 内部。

---

`guard let` 的一个典型用法是在函数开头验证输入，当输入缺失时返回一个兜底值：
```swift
func length(of text: String?) -> Int {
    guard let text = text else { return 0 }
    return text.count
}
```

---

很多时候，你想从一个可选值中得到的只是它的值或者一个默认值。
**空合运算符** `??` 正是做这件事的：如果可选值有值就解包它，否则返回它右边的值：
```swift
let score: Int? = nil
let points = score ?? 0 // points 是等于 0 的 Int
```
默认值必须和被包装的值类型相同。
你可以连续使用多个 `??`：第一个不是 `nil` 的值会胜出。
```swift
let a: Int? = nil
let b: Int? = 7
print(a ?? b ?? 0) // 7
```

---

当存在一个合理的默认值时，`??` 是把可选值变为普通值最简短的方式：
```swift
func volume(from setting: Int?) -> Int {
    return setting ?? 50
}
```

---

在连续使用 `??` 时，Swift 会从左到右依次求值，遇到第一个不是 `nil` 的值就停止；只有当它之前所有的可选值都是 `nil` 时，才会使用最后的默认值。

---

在可选值上访问属性或调用方法之前，需要先对它进行解包。
使用 `?.` 的**可选链**可以帮你自动完成这件事：如果可选值是 `nil`，整个表达式就变成 `nil`，否则访问会继续进行：
```swift
let name: String? = "swift"
let upper = name?.uppercased() // 包含 "SWIFT" 的 String?
```
结果永远是一个可选值，即使属性本身不是可选的。
链可以按需要写得很长，并且能很好地和 `??` 搭配使用：
```swift
class User {
    var nickname: String? = "ace"
}
let user: User? = User()
print(user?.nickname?.count ?? 0) // 3
```

---

当数据可能在多个层级上缺失时，可选链就派上了用场：一个对象本身可能是 `nil`，它的某个属性也可能是 `nil`。
一条 `?.` 链就能处理这两种情况，完全不需要 `if`。

---

一个 `if let` 或 `guard let` 可以同时解包多个可选值：用逗号把各个绑定分隔开即可。
只有当每个可选值都有值时，代码体才会执行：
```swift
let first: String? = "Ada"
let last: String? = "Lovelace"
if let first = first, let last = last {
    print("\(first) \(last)")
}
```
你还可以在绑定之后追加一个布尔条件，比如 `if let n = number, n > 0`。

---

在一个 `if let` 中绑定多个可选值能让代码保持扁平：一个 `else` 分支就能覆盖所有缺失值的情况。

---

很多操作都可能失败，Swift 通过返回一个可选值来报告失败。
把文本转换成数字就是典型例子：`Int("42")` 返回持有 `42` 的 `Int?`，而 `Int("abc")` 返回 `nil`。
`Int("3.5")` 同样是 `nil`，因为这段文本不是一个整数；小数请使用 `Double("3.5")`。
```swift
let typed = "42"
if let number = Int(typed) {
    print(number + 1) // 43
}
```
其他的例子还有 `array.first`（空数组时为 `nil`）和 `dictionary[key]`（键不存在时为 `nil`）。

---

由于转换可能会失败，它的结果永远是一个可选值，使用之前必须先解包，即使你确定这段文本是一个有效的数字。

---

可能失败的转换和 `guard let` 天然适配：先转换，如果结果是 `nil` 就提前退出，然后使用普通值继续处理。

---

有时你想转换可选值内部的值，同时把结果继续保持为可选值，而不需要手动解包再重新包装。
可选值有一个 `map` 方法：如果值存在，就对它应用闭包；否则返回 `nil`。
```swift
let score: Int? = 10
let doubled = score.map { $0 * 2 } // 包含 20 的 Int?
let missing: Int? = nil
let stillMissing = missing.map { $0 * 2 } // nil
```
把它和可能失败的转换结合起来，就能组成一个紧凑的流水线：`Int(text).map { $0 + 1 }`。
