**格式化字符串**是指在运行时用值填充其中某些部分的文本：价格、姓名、分数。Swift 为此提供了两种工具。

第一种是**字符串插值**，你已经见过它了：写在 `\( )` 中的任何内容都会被求值并插入到文本里。它不必是变量，可以是任意表达式：
```swift
let price = 4
print("Total: \(price * 3)") // Total: 12
print("Name: \("ada".uppercased())") // Name: ADA
```
插值是构建字符串最快的方式，但它打印数字时完全按照 Swift 存储它们的样子：`3.5` 仍然是 `3.5`，永远不会是 `3.50`。为了完全控制位数、宽度和填充，我们将使用 `String(format:)`，它会在下一个练习中介绍。

---

第二种工具是 `String(format:)`，它来自 **Foundation** 框架，因此文件必须以 `import Foundation` 开头。

它接收一个**格式字符串**，后面跟着要插入的值。在格式字符串内部，以 `%` 开头的**格式说明符**标记每个值的位置以及它的书写方式。整数的格式说明符是 `%d`：
```swift
import Foundation

let count = 7
let text = String(format: "Item %d", count)
print(text) // Item 7
```
`String(format:)` 返回一个普通的 `String`，所以你可以打印它、存储它或从函数中返回它。

---

对于小数（`Double`），格式说明符是 `%f`。单独使用时，它总是在小数点后打印六位数字：
```swift
print(String(format: "%f", 3.5)) // 3.500000
```
要选择想要的小数位数，在 `%` 和 `f` 之间写一个点和一个数字。这就是**精度**，值会被四舍五入以符合它：
```swift
print(String(format: "%.2f", 3.5))     // 3.50
print(String(format: "%.1f", 3.14159)) // 3.1
print(String(format: "%.0f", 2.71))    // 3
```
`%.2f` 是价格常用的选择，因为它总是恰好显示两位小数。

---

`%` 和字母之间的数字设置字段的**最小宽度**。如果值更短，则在左边添加空格使其**右对齐**；如果更长，则不会截断任何内容：
```swift
print(String(format: "%5d|", 42))    //    42|
print(String(format: "%5d|", 12345)) // 12345|
```
宽度和精度可以结合使用：`%8.2f` 表示“至少 8 个字符宽，带有 2 位小数”：
```swift
print(String(format: "%8.2f|", 3.14159)) //     3.14|
```
正是固定宽度让表格的各列对齐。

---

默认情况下，填充在左侧。紧跟在 `%` 后面的减号会把填充改到右边，因此值是**左对齐**的：
```swift
print(String(format: "%-5d|", 42)) // 42   |
print(String(format: "%5d|", 42))  //    42|
```
减号是一个**标志**：它改变字段的填充方式，但不改变宽度。

---

另一个标志是 `0`：不用空格，而是用零填充字段的左侧。这就是得到 `007` 或 `00042` 这类数字的方式：
```swift
print(String(format: "%05d", 42))  // 00042
print(String(format: "%03d", 7))   // 007
print(String(format: "%03d", 1234)) // 1234
```
和空格一样，超过宽度的值永远不会被截断。

---

格式字符串可以包含任意数量的格式说明符。值按相同的顺序跟在后面，用逗号分隔，并且每个值都必须匹配其格式说明符的类型：`Int` 用 `%d`，`Double` 用 `%f`：
```swift
let count = 3
let weight = 4.5
print(String(format: "%d items, %.1f kg", count, weight)) // 3 items, 4.5 kg
```
把 `Double` 传给 `%d`（或把 `Int` 传给 `%f`）可以编译通过，但会打印出一个无意义的数字，所以务必检查格式说明符和值是否一一对应。

---

整数也可以用其他进制书写。`%x` 以小写字母打印**十六进制**值，`%X` 使用大写字母，`%o` 则是八进制：
```swift
print(String(format: "%x", 255)) // ff
print(String(format: "%X", 255)) // FF
print(String(format: "%o", 8))   // 10
```
宽度和 `0` 标志在这里同样适用：`%02x` 是书写颜色中一个字节的经典方式，例如 `#ff8000`。

---

要把 `String` 插入格式字符串，请使用格式说明符 `%@`：
```swift
let name = "Ada"
let age = 36
print(String(format: "%@ is %d years old", name, age)) // Ada is 36 years old
```
`%@` 可以直接接受 Swift 的 `String`。不要对 Swift 字符串使用 `%s`：该格式说明符期望的是 C 字符串，会打印出乱码或导致崩溃。
