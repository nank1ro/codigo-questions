**正则表达式**（regex）是一种描述文本形状的小型模式："一串数字"、"一个单词后面跟着等号"、"三个大写字母"。你只需把形状描述一次，让 Swift 去找到它，而不必针对字符编写循环。

Swift 把正则表达式写在 `#/` 和 `/#` 之间：
```swift
let digits = #/\d+/#
```
在模式内部，`\d` 表示"任意一个数字"，`+` 表示"前一个内容出现一次或多次"，所以 `\d+` 表示"一串一个或多个数字"。

你能提出的最简单的问题是：一段文本是否包含匹配。`contains(_:)` 接收一个正则表达式并返回一个 `Bool`：
```swift
print("order42".contains(#/\d+/#)) // true
print("order".contains(#/\d+/#))   // false
```
请始终使用这里展示的 `#/ ... /#` 形式：当模式直接写在方法调用内部时，较短的 `/ ... /` 写法会让编译器困惑。

---

少数几个简写就能覆盖大多数模式。每一个都恰好匹配**一个**字符：
- `\d` 是一个数字
- `\w` 是一个字母、数字或下划线
- `\s` 是一个空格、制表符或换行符
- `.` 是任意单个字符

要匹配多个字符，在模式后面紧跟一个**量词**：
- `+` 表示一个或多个
- `*` 表示零个或多个
- `?` 表示零个或一个

于是 `\w+` 是一个单词，`\s*` 是可选的空白，`\d?` 是一个可选的数字：
```swift
print("hello world".contains(#/\w+\s\w+/#)) // true
print("hello".contains(#/\w+\s\w+/#))       // false
```
没有特殊含义的字符只是匹配它自身，所以 `#/cat/#` 匹配 `cat` 这三个字母。

---

默认情况下，模式可以匹配文本中的任何位置。**锚点**则把它固定到一个位置上：
- `^` 表示"文本的开头"
- `$` 表示"文本的结尾"

```swift
print("swift".contains(#/^sw/#))  // true, the text starts with sw
print("myswift".contains(#/^sw/#)) // false, sw is not at the start
print("swift".contains(#/ft$/#))  // true, the text ends with ft
```
锚点匹配的是一个位置，而不是字符，所以它们不会给匹配的内容添加任何东西。

---

当简写都不适用时，把你想接受的字符列在方括号中。`[abc]` 匹配一个 `a`、一个 `b` 或一个 `c`，连字符表示范围：
```swift
print("f".contains(#/[a-f]/#))  // true
print("Z".contains(#/[A-Z]/#))  // true
print("5".contains(#/[0-9a-f]/#)) // true
```
花括号中的数字确切地说明前一个模式重复多少次：`{3}` 表示三次，`{2,4}` 表示两到四次：
```swift
print("aaa".contains(#/^a{3}$/#))  // true
print("aa".contains(#/^a{3}$/#))   // false
```
用 `^` 和 `$` 包住模式并加上次数，是检查整段文本是否符合给定形状的常用方法。

---

`contains(_:)` 只能回答是或否。要获得匹配到的文本，使用 `firstMatch(of:)`。它返回一个**可选的匹配**：没有任何匹配时为 `nil`，因此与 `if let` 自然搭配。

匹配到的文本存储在匹配的属性 `0` 中，写作 `m.0`：
```swift
let text = "order 42 today"
if let m = text.firstMatch(of: #/\d+/#) {
    print(m.0) // 42
}
```
`firstMatch(of:)` 在第一个匹配处停止，即使文本中还有更多匹配。

---

`m.0` 不是 `String` 而是 `Substring`：它是指向原始文本的一个视图，而不是副本。它的打印效果与字符串完全一样，但在需要 `String` 的地方你必须进行转换：
```swift
let text = "order 42"
if let m = text.firstMatch(of: #/\d+/#) {
    let found: String = String(m.0)
    print(found) // 42
}
```
数字类型的初始化器直接接受 `Substring`，所以 `Int(m.0)` 无需绕路就能工作。

---

`matches(of:)` 返回**每一个**匹配而不是第一个，形式为数组。这个数组永远不会是 `nil`：没有匹配时它只是空数组，因此可以直接对它进行循环或转换：
```swift
let text = "a1 b22"
print(text.matches(of: #/\d+/#).count) // 2
```
每个元素都是一个匹配，所以 `map` 中的 `$0.0` 就是匹配到的文本：
```swift
let found = text.matches(of: #/\d+/#).map { String($0.0) }
print(found) // ["1", "22"]
```

---

由于 `Int(_:)` 接受 `Substring`，把找到的文本转换成数字只需一步。`compactMap` 在这里很方便：它会丢弃返回 `nil` 的值：
```swift
let text = "a1 b22"
let numbers = text.matches(of: #/\d+/#).compactMap { Int($0.0) }
print(numbers) // [1, 22]
```
当每个元素都能转换时使用 `map`，当有些可能失败时使用 `compactMap`。

---

在模式的一部分外面加上圆括号会创建一个**捕获组**：整个匹配仍然是 `m.0`，括号内的部分则成为 `m.1`：
```swift
let text = "id-42"
if let m = text.firstMatch(of: #/id-(\d+)/#) {
    print(m.0) // id-42
    print(m.1) // 42
}
```
这就是你保留感兴趣的部分并丢弃周围文本的方式。没有括号就完全没有 `m.1`，代码也无法编译。

---

一个模式可以包含多个组。它们按开括号从左到右编号，所以第二个是 `m.2`，第三个是 `m.3`，依此类推：
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/([a-z]+)=(\d+)/#) {
    print(m.1, m.2) // size 10
}
```
无论有多少个组，`m.0` 始终是整个匹配。

---

一旦模式变大，靠数括号就变得脆弱。不如给组起一个**名字**：在它的开括号后面紧跟 `?<name>`，然后把它当作匹配的属性来读取：
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/(?<key>[a-z]+)=(?<value>\d+)/#) {
    print(m.key)   // size
    print(m.value) // 10
}
```
命名组仍然有编号，所以 `m.1` 依然可用，但 `m.key` 说明了它保存的内容，并且在模式发生变化后依然有效。

---

`replacing(_:with:)` 把每个匹配都替换为固定文本并返回一个新的 `String`，原始文本保持不变：
```swift
let text = "a1 b22"
print(text.replacing(#/\d+/#, with: "#")) // a# b#
print(text)                               // a1 b22
```
注意 `\d+` 会把一整串数字替换为一个 `#`，而 `\d` 会一次替换一个数字。模式决定了有多少内容会消失。

---

`split(separator:)` 也接受正则表达式，这让一次调用就能处理写法不总是一致的分隔符：
```swift
let line = "a, b;c"
let parts = line.split(separator: #/[,;]\s*/#)
print(parts.joined(separator: "|")) // a|b|c
```
模式 `[,;]\s*` 表示"一个逗号或一个分号，后面跟着任意数量的空白"，所以每个分隔符都被完整消耗，不会产生空字段。结果是 `Substring` 的数组。

---

用 `^` 和 `$` 验证整段文本是可行的，但 `wholeMatch(of:)` 把这件事直接说了出来：只有当模式从第一个字符覆盖到最后一个字符时，它才返回一个匹配，否则返回 `nil`：
```swift
print("1a2b".wholeMatch(of: #/[0-9a-f]+/#) != nil) // true
print("1z".wholeMatch(of: #/[0-9a-f]+/#) != nil)   // false
```
在文本内部查找内容用 `firstMatch(of:)`，检查文本是否符合某个确切的形状用 `wholeMatch(of:)`。

---

`#/ ... /#` 字面量在编译时就固定了。当模式要到运行时才确定时——例如因为它是用户输入的——用 `Regex(_:)` 来构建它：
```swift
let regex = try Regex("[0-9]+")
print("abc123".contains(regex)) // true
```
这个初始化器会**抛出错误**：像 `"["` 这样的无效模式只有在程序运行时才会被发现，所以调用需要 `try`，并且错误必须要么用 `do`/`catch`（或 `try?`）处理，要么像本练习所做的那样，把外围函数标记为 `throws` 来传播。以这种方式构建的正则表达式没有编译期已知的编号属性，但 `contains`、`matches(of:)` 和 `replacing` 的工作方式与之前完全相同。
