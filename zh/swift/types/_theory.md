Swift 中的每个值都有一个**类型**，它告诉编译器这是哪种数据，以及你能用它做什么。
基本类型有：
- `Int`：整数，比如 `42` 或 `-7`
- `Double`：带小数部分的数，比如 `3.14`
- `String`：一段文本，比如 `"Hello"`
- `Character`：单个字符，比如 `"a"`
- `Bool`：`true` 或 `false`

你可以使用**类型注解**来标明常量或变量的类型：在名称后面加上冒号和类型名：
```swift
let age: Int = 36
let name: String = "Ada"
```
一种类型的值不能存储到另一种类型的常量中：`let age: Int = "36"` 是一个编译错误。

---

大多数时候你不需要写类型注解：Swift 会根据你赋的值**推断**类型，遵循以下几条字面量规则：
- 没有小数点的数字，比如 `42`，是 `Int`
- 带小数点的数字，比如 `3.14`，是 `Double`
- 双引号中的文本是 `String`
- `true` 和 `false` 是 `Bool`
```swift
let count = 42     // Int
let price = 9.99   // Double
let name = "Ada"   // String
let isOpen = true  // Bool
```
Swift 还有 `Float`，它是一种使用 `Double` 一半内存但精度较低的小数，因此小数字面量永远不会被推断为 `Float`：你必须通过注解来指定它。
同样地，`"a"` 会被推断为 `String`，所以 `Character` 总是需要注解。

---

`type(of:)` 函数返回一个值的类型，用它来检查 Swift 推断出了什么类型非常方便：
```swift
print(type(of: 42))    // Int
print(type(of: 2.5))   // Double
print(type(of: "hi"))  // String
```
当你想要与推断出的类型不同的类型时，就添加注解。整数字面量可以存储在 `Double` 或 `Float` 常量中，单字符字面量可以存储在 `Character` 常量中：
```swift
let ratio: Double = 3       // 3.0, not an Int
let half: Float = 0.5
let initial: Character = "S"
print(type(of: ratio))      // Double
```

---

Swift 从不自动在数字类型之间转换：将 `Int` 与 `Double` 相加是一个编译错误，即使它们都是数字。
```swift
let apples = 3
let price = 1.5
let total = apples * price // error: Int and Double can't be mixed
```
要把它们结合起来，你需要将该值传入类型的初始化器，创建一个所需类型的新值：
```swift
let total = Double(apples) * price // 4.5
```
反过来也一样：`Int(4.5)` 会产生一个 `Int`，只保留数字的整数部分。

---

`Int(x)` 不会四舍五入：它会**截断**，直接丢弃小数部分，所以 `Int(3.99)` 是 `3`，`Int(-3.99)` 是 `-3`。
要四舍五入到最接近的整数，先对 `Double` 调用 `rounded()`，然后再转换：
```swift
let x = 3.99
print(Int(x))            // 3
print(Int(x.rounded()))  // 4
```
像 `2.5` 这样的中间值会远离零进行舍入：`2.5` 变成 `3.0`，`-2.5` 变成 `-3.0`。

---

操作数的类型决定了除法的运作方式。当两者都是 `Int` 时，`/` 运算符执行**整数除法**：结果是 `Int`，余数被丢弃。
当至少一个操作数是 `Double` 时，`/` 执行浮点除法并保留小数部分：
```swift
print(7 / 2)              // 3
print(7.0 / 2)            // 3.5
let slices = 7
print(Double(slices) / 2) // 3.5
```
所以要从两个 `Int` 值得到小数结果，你必须在除法**之前**把至少其中一个转换为 `Double`：`Double(7 / 2)` 是 `3.0`，因为整数除法已经发生了。

---

当函数必须返回由整数计算得出的小数结果时，在除法之前把操作数转换为 `Double`，并将返回类型声明为 `Double`：
```swift
func ratio(_ part: Int, _ total: Int) -> Double {
    return Double(part) / Double(total)
}
print(ratio(1, 4)) // 0.25
```
记住，数组的 `count` 也是 `Int`，所以它需要同样的转换。

---

数字和字符串使用相同的初始化器语法进行转换。`String(42)` 把数字变成文本 `"42"`，就像用 `"\(42)"` 对它进行插值一样。
反方向可能会失败，因为并非所有文本都是数字，所以 `Int("42")` 返回一个**可选**的 `Int?`：这里它持有 `42`，而 `Int("hello")` 是 `nil`。
正如你在可选值课程中学到的，你可以用 `??` 提供一个回退值，或者用 `if let` 解包它：
```swift
let typed = "42"
let number = Int(typed) ?? 0
print(number + 1) // 43
```

---

`Int(text)` 只有在整个文本都是带可选符号的有效整数时才会成功：
```swift
print(Int("42"))   // Optional(42)
print(Int("-7"))   // Optional(-7)
print(Int("3.5"))  // nil, not a whole number
print(Int(" 42"))  // nil, spaces are not allowed
print(Int("abc"))  // nil
```
对于小数文本，请使用 `Double(text)`，它同样返回 `Double?`：`Double("3.5")` 是 `Optional(3.5)`。

---

**类型别名**使用 `typealias` 关键字为一个已有的类型赋予新名称：
```swift
typealias Score = Int
let best: Score = 100
print(best + 1) // 101
```
`Score` 和 `Int` 是同一个类型，所以它们可以随意混用。别名不会增加任何安全性：当普通类型在你的程序中有特定含义时，它只是让代码更易读。

---

`Int` 使用 64 位，所以它只能表示固定范围内的数字。最大值和最小值可以通过 `Int.max` 和 `Int.min` 获得：
```swift
print(Int.max) // 9223372036854775807
print(Int.min) // -9223372036854775808
```
超出这些限制称为**溢出**。与许多其他语言不同，Swift 不会静默地回绕到范围的另一端：溢出操作是一个会终止程序的**运行时错误**。

---

当你查找极值时，`Int.max` 和 `Int.min` 可以用作起始值：任何实际的数字都小于 `Int.max`，所以它是“目前为止最小的值”的安全初始值：
```swift
var smallest = Int.max
for number in [8, 3, 5] {
    if number < smallest {
        smallest = number
    }
}
print(smallest) // 3
```

---

正如你在字符串课程中看到的，遍历 `String` 每次会得到一个 `Character`。`Character` 不是 `String`，所以要将它当作文本使用，你需要用 `String(c)` 转换它。
当字符是数字时，`wholeNumberValue` 属性会以 `Int?` 的形式给出它的数值：对于不是数字的字符，它是 `nil`。
```swift
for c in "a1" {
    print(c.wholeNumberValue)
}
// nil
// Optional(1)
```

---

因为 `Int(text)` 和 `Double(text)` 在失败时返回 `nil`，将结果与 `nil` 比较就能知道一段文本是否是该种类的数字：
```swift
print(Int("42") != nil)     // true
print(Double("4.2") != nil) // true
print(Double("42") != nil)  // true, a whole number is also a valid Double
```
注意最后一行：`Int` 接受的每段文本 `Double` 也接受，所以当你想区分它们时要先检查 `Int`。

---

有时候你需要把不同类型的值存储在一起。特殊类型 `Any` 可以持有**任意**类型的值，所以声明为 `[Any]` 的数组可以混合数字、字符串和布尔值：
```swift
let items: [Any] = [1, "two", true]
```
每个元素仍然记得它真实的类型，`type(of:)` 可以揭示它。要以元素真实的类型来使用该值，你需要使用带 `as?` 的**条件转换**，它返回一个可选值：类型匹配时它持有该值，否则是 `nil`：
```swift
for item in items {
    if let number = item as? Int {
        print(number + 1) // runs only for 1
    }
}
```
`Any` 是最后的手段：单一具体类型的数组更安全也更易用，所以只要有可能就优先使用它。

---

条件转换可以用 `else if` 自然地串联起来处理多种可能的类型，把每一种转换为结果所需的类型：
```swift
let item: Any = 2.5
if let number = item as? Int {
    print(Double(number))
} else if let number = item as? Double {
    print(number)
}
```
存储在 `Any` 中的 `Int` 仍然是 `Int`：对它使用 `as? Double` 会返回 `nil`，因为 `as?` 检查的是类型，它不会转换数字。
