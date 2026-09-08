**字符串**是一段文本。在 Swift 中，你在双引号之间书写字符串字面量，它的类型是 `String`：
```swift
let greeting: String = "Hello"
var city = "Rome"
```
和其他值一样，`let` 创建一个不能更改的常量，而 `var` 创建一个可以更改的变量。
Swift 会根据字面量推断出 `String` 类型，因此类型注解是可选的。

---

**字符串插值**会把表达式的值插入到字符串字面量中。把表达式包裹在 `\()` 中：
```swift
let name = "Ada"
let age = 36
print("\(name) is \(age) years old") // Ada is 36 years old
```
任何类型都可以被插值：数字、布尔值和其他字符串都会自动转换为文本。

---

两个字符串可以用 `+` 运算符连接，生成一个新字符串：
```swift
let full = "Hello" + " " + "world" // Hello world
```
要在现有字符串变量的末尾添加文本，可以使用 `+=`。该变量必须用 `var` 声明，因为它的值会发生变化：
```swift
var log = "Start"
log += "..."
print(log) // Start...
```

---

`count` 属性返回字符串中的字符数量，当字符串没有任何字符时，`isEmpty` 为 `true`：
```swift
print("Swift".count) // 5
print("".isEmpty)    // true
```
每一个字符都会被计数，包括空格和标点符号。

---

`String` 是 `Character` 值的集合。`Character` 是单个字母、数字、符号或空格，它和字符串一样用双引号书写，因此需要类型注解才能得到一个 `Character`：
```swift
let letter: Character = "a"
let text = "abc"
print(text.count) // 3
```
检查 `isEmpty` 比将 `count` 与 `0` 比较更好：可读性更强，也不需要计算每一个字符。

---

**多行字符串字面量**以三个双引号 `"""` 开始和结束，各自独占一行。它们之间的每一行都会成为字符串的一部分，换行符会被保留：
```swift
let poem = """
Roses are red
Violets are blue
"""
print(poem)
```
这会精确地打印出所写的两行。结尾的 `"""` 还决定了缩进：它前面的任何空白都会从每一行的开头被移除。

---

由于字符串是字符的集合，你可以用 `for`-`in` 循环遍历它。每次迭代都会得到一个 `Character`：
```swift
for letter in "hey" {
    print(letter)
}
// h
// e
// y
```
`Character` 可以用 `==` 与字符字面量进行比较，因此统计某个字符出现的次数只需要一个循环和一个计数器。

---

与数组不同，字符串不能用整数下标访问，比如 `text[2]`：某些字符占用的内存比其他字符多，因此 Swift 使用专门的 `String.Index` 类型来指向某个位置。
`startIndex` 是第一个字符的位置，`endIndex` 是最后一个字符*之后*的位置。要从某个索引移动，使用 `index(_:offsetBy:)`，然后用结果对字符串取下标：
```swift
let word = "Swift"
let second = word.index(word.startIndex, offsetBy: 1)
print(word[second]) // w
```
移动超出字符串末尾会在运行时崩溃，因此偏移量必须保持在 `count` 范围之内。

---

使用索引写法比较冗长，因此 Swift 为最常见的场景提供了简便方式：
- `first` 和 `last` 以可选的 `Character?` 形式返回第一个和最后一个字符（空字符串时为 `nil`）
- `prefix(n)` 返回前 `n` 个字符，`suffix(n)` 返回后 `n` 个字符
```swift
let word = "Swift"
print(word.first!)     // S
print(word.prefix(2))  // Sw
print(word.suffix(3))  // ift
```
`prefix` 和 `suffix` 返回一个 `Substring`，它是对原始文本的一个视图。要把它存储为真正的 `String`，需要用 `String(...)` 包裹。如果 `n` 大于 `count`，你只会得到整个字符串。

---

有三个方法可以回答关于字符串内容最常见的问题，它们都返回一个 `Bool`：
- 当字符串中任意位置包含给定的文本（或字符）时，`contains(_:)` 为 `true`
- 当字符串以给定的文本开头时，`hasPrefix(_:)` 为 `true`
- 当字符串以给定的文本结尾时，`hasSuffix(_:)` 为 `true`
```swift
let email = "ada@example.com"
print(email.contains("@"))          // true
print(email.hasPrefix("ada"))       // true
print(email.hasSuffix(".org"))      // false
```
这三个方法都区分大小写：`"Swift".hasPrefix("s")` 为 `false`。

---

由于 `contains`、`hasPrefix` 和 `hasSuffix` 都返回布尔值，它们可以很自然地与 `||` 和 `&&` 组合，构建更复杂的判断。

---

`uppercased()` 和 `lowercased()` 会返回一个**新**字符串，其中每个字母都被转换为大写或小写。原字符串不会被修改：
```swift
let name = "Swift"
print(name.uppercased()) // SWIFT
print(name.lowercased()) // swift
print(name)              // Swift
```
两者都是方法，所以别忘了括号。

---

转换为小写是忽略大小写比较文本的常用方法：两个仅大小写不同的字符串在都转换为小写后就会相等。

---

`split(separator:)` 会在分隔符字符出现的每个位置将字符串拆分成一个数组。`joined(separator:)` 则相反：它把数组的元素粘合成一个字符串，并在它们之间放置分隔符：
```swift
let parts = "a-b-c".split(separator: "-") // ["a", "b", "c"]
print(parts.count)                         // 3
print(parts.joined(separator: ", "))       // a, b, c
```
和 `prefix` 一样，`split` 返回的是 `Substring` 值；如果需要把它存储为 `String`，就用 `String(...)` 包裹它。

---

按空格拆分是把一句话拆成单词最简单的方法，而拼接则是从数组重新构建文本的方法。

---

Foundation 框架增加了许多额外的字符串方法。其中最有用的方法之一是 `replacingOccurrences(of:with:)`，它会返回一个新字符串，其中第一个文本的每次出现都被替换为第二个文本：
```swift
import Foundation

let path = "a/b/c"
print(path.replacingOccurrences(of: "/", with: "-")) // a-b-c
```
记得在文件顶部写上 `import Foundation`，否则该方法将不可用。方法调用可以链式连接，所以 `text.lowercased().replacingOccurrences(of: " ", with: "_")` 是合法的。

---

字符串可以使用和数字相同的运算符进行比较。`==` 检查两个字符串是否完全由相同的字符组成，而 `<` 和 `>` 会按字典顺序逐个字符进行比较：
```swift
print("apple" == "apple")  // true
print("apple" < "banana")  // true
print("car" < "cat")       // true
```
比较是区分大小写的，并且每个大写字母都排在每个小写字母**之前**，所以 `"B" < "a"` 为 `true`。

---

`Character` 不是 `String`，所以不能直接用 `+` 把它拼接到字符串上。先用 `String(...)` 转换它：
```swift
let letter: Character = "a"
let text = String(letter) + "bc" // abc
```
把它和 `for`-`in` 循环结合起来，你可以一次一个字符地重建字符串，例如把每个新字符放在目前为止收集到的字符前面。
