**注释**是写在源代码内部、给阅读代码的人看的说明。编译器会完全忽略注释，因此它们绝不会改变程序的行为。

最简单的注释是**单行注释**：它以 `//` 开始，一直延续到该行结尾。
```swift
// Greets the user
print("Hello")
```
用注释说明一段代码的用途，或者它为什么要这样写。

---

注释不一定要独占一行：它可以跟在同一行的代码之后。这就是**行尾注释**，很适合为那条具体的语句写一句简短说明：
```swift
let retries = 3 // give up after three attempts
```
从 `//` 到该行结尾的一切都会被忽略，而它前面的代码照常运行。

---

由于编译器会完全去掉注释，添加或删除注释绝不会改变程序的行为。只有**没有**被注释掉的代码才会运行。

这让 `//` 成为一种无需删除就能关掉某行代码的快捷方式。这叫做**注释掉**：
```swift
var total = 10
// total = total + 5
print(total) // prints 10
```
第二行现在是注释，所以 `total` 仍然是 `10`。去掉 `//` 就能让这行代码重新生效。

做实验时注释掉很方便，但记得清理：长期留着的被注释代码只会让下一个阅读的人困惑。

---

当注释需要不止一行时，Swift 提供了**多行注释**（也叫块注释）：它以 `/*` 开始，以 `*/` 结束，中间的一切都会被忽略，包括换行。
```swift
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
print("Welcome!")
```
块注释也可以很短，写在一行里：`/* like this */`。

---

与在行尾停止的 `//` 不同，`/*` 注释只在 `*/` 处停止。如果你忘了关闭它，编译器就会把后面所有代码都当作注释的一部分并报错：
```swift
let width = 10 /* in centimetres
print(width) // still inside the comment: error, the comment is never closed
```
`//` 和 `/* */` 都可以用作行尾注释，但用 `/*` 时一定要确保 `*/` 存在。

---

在许多语言中块注释不能包含其他块注释，但在 Swift 中它们**可以嵌套**：每个 `/*` 都必须有自己的 `*/`，注释只有在最外层被关闭时才结束。
```swift
/* outer /* inner */ still a comment */
print("done")
```
这里 `still a comment */` 属于外层注释，所以只会输出 `done`。正是这一点让你能够注释掉整块代码，即使那块代码里已经有一个 `/* */` 注释。

---

要一次注释掉多行，把它们包在一个块注释里，而不是给每一行都加 `//`：
```swift
var total = 100
/*
total = total - 30
total = total - 20
*/
print(total) // prints 100
```
多亏了嵌套，即使其中某一行已经包含 `/* */` 注释，这样做也依然可行。

---

块注释的一个常见用法是**头部注释**：放在函数正上方的一小段说明，讲清楚这个函数做什么以及它的参数是什么意思。
```swift
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
调用 `toSeconds` 的人现在可以读头部注释而不必读函数体。把头部注释紧挨着函数放置，它们才会一起被更新。

---

Swift 还有第三种注释，即**文档注释**：以 `///`（三个斜杠）开头的单行注释，放在函数、类型或属性的正上方。
```swift
/// Returns the greeting for `name`.
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
对编译器来说它只是注释，但 Xcode 这样的工具会读取它，并把它显示为 `greet` 的帮助文本。文档注释支持 **Markdown**，所以你可以用反引号表示代码，也可以用 `**粗体**` 和列表。

---

文档注释的第一行是**摘要**：一句简短说明函数做什么的话。用第三人称书写，就像在描述这个函数："Returns..."、"Adds..."、"Checks..."。
```swift
/// Returns `true` when `n` is divisible by two.
func isEven(_ n: Int) -> Bool {
    return n % 2 == 0
}
```
注释必须紧挨在声明的正上方，中间不能有空行，否则 Xcode 不会把它关联到该函数。

---

文档注释也有块的形式：`/**` 打开它，`*/` 关闭它，和多行注释完全一样，只是开头多了一个星号。
```swift
/**
 Returns the greeting for `name`.

 The result always ends with an exclamation mark.
 */
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
对工具而言 `/// 文本` 和 `/** 文本 */` 意思相同；在 Swift 代码中 `///` 是最常见的选择，而 `/** */` 便于写长描述。普通的 `/* */` 或 `//` 注释**不是**文档，即使把它放在函数上方也不是。

---

在摘要之后，文档注释可以用 Xcode 能识别的特殊 Markdown 列表项来描述参数和返回值：
```swift
/// Returns the number of seconds in the given minutes.
/// - Parameter minutes: a whole number of minutes, never negative
/// - Returns: `minutes` multiplied by sixty
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
顺序始终一致：先是摘要，然后为每个参数写 `- Parameter 名称:`，最后是 `- Returns:`。

---

有些注释遵循编辑器能理解的约定。在 Swift 中最常见的**标记**有：
- `// MARK: - Title` 为文件的某一节加上标题，使它出现在 Xcode 的导航菜单中
- `// TODO: ...` 标示还需要编写的内容
- `// FIXME: ...` 标示已知有问题、必须修正的代码

```swift
// MARK: - Setup
let limit = 10
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
对编译器来说它们只是普通注释；Xcode 会把它们列出来，方便找到待办工作。工作完成后就删掉标记：过期的 `TODO` 会误导人。

---

`TODO` 通常紧挨着一个占位实现，它让代码在真正的实现写好之前仍能编译。当你完成这项工作时，请在同一次修改中替换占位实现并去掉标记，这样注释就不会对代码的状态说谎。

---

`FIXME` 与 `TODO` 不同：代码已经存在，但已知它是错的。好的 `FIXME` 会说明 bug 是什么，并尽可能给出一个能重现它的例子，让下一个人可以迅速修好。和 `TODO` 一样，bug 修好后就删掉标记，但要保留文档注释，因为它依然成立。

---

好的注释解释代码**为什么**这么做，而不是它**做了什么**。代码本身已经说明了发生了什么；用文字重复一遍只会增加噪音，而且代码一改它就过时了：
```swift
// set timeout to 30
let timeout = 30
```
数字背后的原因才是读者猜不到的：
```swift
// the server drops idle connections after 35 seconds, so stop earlier
let timeout = 30
```
如果一条注释只是复述它下面那一行，就删掉它，或者换成原因。
