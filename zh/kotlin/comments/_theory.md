**注释**是写在源代码中的说明性文字，供阅读代码的人参考。编译器会完全忽略注释，因此注释绝不会改变程序的行为。

最简单的注释是**单行注释**：它以 `//` 开头，一直延伸到行尾。
```kotlin
// 问候用户
println("Hello")
```
使用注释来解释一段代码的用途，或者解释代码为什么这样编写。

---

注释不必独占一行：它可以跟在同一行代码的后面。这就是**尾随注释**，适合用来写一句关于这条特定语句的简短说明：
```kotlin
val retries = 3 // 尝试三次后放弃
```
从 `//` 到行尾的所有内容都会被忽略，而它前面的代码照常运行。

---

由于编译器会完全移除注释，添加或删除注释绝不会改变程序的行为。只有**没有**被注释掉的代码才会运行。

这使得 `//` 成为在不删除代码的情况下快速禁用某行代码的方法。这称为**注释掉**：
```kotlin
var total = 10
// total = total + 5
println(total) // 打印 10
```
第二行现在是注释，因此 `total` 保持为 `10`。删掉 `//` 就能让这行代码重新生效。

注释掉代码在试验时很方便，但记得要清理：长期被注释掉的代码只会让下一个阅读它的人感到困惑。

---

当注释需要占用多行时，Kotlin 提供了**多行注释**（也称为块注释）：它以 `/*` 开头，以 `*/` 结尾，中间的所有内容都会被忽略，包括换行符。
```kotlin
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
println("Welcome!")
```
块注释也可以很短，只占一行：`/* like this */`。

---

`//` 在行尾结束，而 `/*` 注释只在 `*/` 处结束。如果你忘记闭合它，编译器会把后面的所有代码都当作注释的一部分，并报错：
```kotlin
val width = 10 /* 单位为厘米
println(width) // 仍在注释内部:错误,该注释永远不会被闭合
```
`//` 和 `/* */` 都可以用作尾随注释，但使用 `/*` 时一定要确保有对应的 `*/`。

---

在 Java 中，块注释不能包含另一个块注释，但在 Kotlin 中它们**可以嵌套**：每个 `/*` 都必须有与之匹配的 `*/`，只有最外层的注释闭合后，注释才会结束。
```kotlin
/* outer /* inner */ still a comment */
println("done")
```
这里 `still a comment */` 是外层注释的一部分，因此只会打印 `done`。正因如此，即使某段代码已经包含 `/* */` 注释，你也可以把整段代码注释掉。

---

要一次注释掉多行，可以把它们包在一个块注释里，而不是在每一行都加上 `//`：
```kotlin
var total = 100
/*
total = total - 30
total = total - 20
*/
println(total) // 打印 100
```
得益于嵌套，即使其中一行已经包含 `/* */` 注释，这种方法也同样有效。

---

块注释的一个常见用途是**头部注释**：放在函数正上方的一小段注释，说明函数的功能以及各参数的含义。
```kotlin
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
调用 `toSeconds` 的人现在可以直接阅读头部注释，而不必看函数体。请把头部注释放在函数旁边，以便二者一起更新。

---

Kotlin 有第三种注释，即**文档注释**，它以称为 **KDoc** 的格式编写：以 `/**`（一个斜杠和两个星号）开头，以 `*/` 结尾，放在函数、类或属性的正上方。
```kotlin
/**
 * Returns the greeting for [name].
 */
fun greet(name: String): String {
    return "Hi, $name!"
}
```
对编译器来说它只是注释，但 IntelliJ IDEA 等工具会读取它，并将其显示为 `greet` 的帮助文本。内部行开头的 `*` 只是一种让代码块保持对齐的约定。在 KDoc 中可以使用 Markdown，像 `[name]` 这样的方括号会变成指向该参数的链接。

---

文档注释的第一行是**摘要**：一句简短的话，说明函数的功能。用第三人称来写，就像在描述这个函数一样："Returns..."、"Adds..."、"Checks..."。
```kotlin
/**
 * Returns `true` when [n] is divisible by two.
 */
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
```
注释必须紧挨着声明的正上方，中间不能有其他语句，否则工具不会把它关联到该函数。

---

在摘要之后，文档注释可以用 **KDoc 标签**来描述参数和返回值，这些标签总是以 `@` 开头：
```kotlin
/**
 * Returns the number of seconds in the given minutes.
 * @param minutes a whole number of minutes, never negative
 * @return [minutes] multiplied by sixty
 */
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
`@param` 后面跟参数名，然后是参数的描述；每个参数对应一个 `@param`。`@return` 描述函数返回的值。顺序总是固定的：先摘要，然后是 `@param` 标签，最后是 `@return`。

---

有多个参数的函数会为每个参数各写一个 `@param` 标签，顺序与参数一致：
```kotlin
/**
 * Returns the area of a rectangle.
 * @param width the horizontal side, in centimetres
 * @param height the vertical side, in centimetres
 * @return the product of [width] and [height]
 */
fun area(width: Int, height: Int): Int {
    return width * height
}
```
标签终究只是注释：如果你重命名了参数却忘了更新标签，什么也不会报错，但文档就开始撒谎了。请连同函数签名一起更新 KDoc。

---

编译器只在代码中识别注释，绝不会在**字符串字面量**中识别。在双引号之间，`//` 和 `/* */` 只是普通字符：
```kotlin
println("50 // 2") // prints 50 // 2
```
第一个 `//` 是文本的一部分，第二个才开始真正的注释。这一点最常让人吃惊的地方是网址，因为协议后面紧跟 `//`。

---

有些注释遵循编辑器能够识别的约定。最常见的**标记**有：
- `// TODO: ...` 标记还有待编写的内容
- `// FIXME: ...` 标记已知有错、必须修正的代码

```kotlin
val limit = 10
// TODO: 从设置中读取限制值
```
对编译器来说它们只是普通注释；IntelliJ IDEA 会把它们收集到一个专门的工具窗口中，让待办工作一目了然。`TODO` 通常挨着一个占位实现，让代码在真正的实现编写完成之前保持可编译。完成工作后，请在同一次修改中替换占位实现并删除标记，这样注释就永远不会与代码的实际状态不符。

---

`FIXME` 与 `TODO` 不同：代码已经存在，但已知是有错的。一个好的 `FIXME` 会说明缺陷是什么，并尽可能给出一个能暴露问题的例子，让下一个人能快速修复。与 `TODO` 一样，缺陷修复后要删除标记，但要保留文档注释，因为它仍然正确。

---

好的注释解释代码**为什么**这样做，而不是它**做了什么**。代码本身已经展示了会发生什么；用文字重复只会增加噪音，而且代码一改就过时：
```kotlin
// 把 timeout 设为 30
val timeout = 30
```
数字背后的原因才是读者无法猜到的：
```kotlin
// 服务器会在 35 秒后断开空闲连接,所以要提前停止
val timeout = 30
```
如果一条注释只是复述了下面那行代码，就删掉它，或者换成原因。最好的注释是说出代码本身说不出的东西。
