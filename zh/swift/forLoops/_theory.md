我们知道如何使用 `while` 循环来重复代码。
例如这个程序重复语句来显示 `hello`
```swift
var counter = 0

while counter < 5 {
    print("hello")
    counter += 1;
}
```
但我们可以用 `for` 循环来做同样的事情：
```swift
for i in 0..<5 {
    print("hello")
}
```

---

在 `for` 循环中，我们可以指定循环运行的次数

---

我们可以使用 `..<` 来循环到下一个数字（不包含），或使用 `...` 来循环到下一个数字（包含）

---

名为 `i` 的变量是计数器变量。
我们可以给它任意名称。
它记录当前处于循环的第几次重复

---

`stride()` 函数返回一个数字序列。
它需要 _from_、_to_ 和 _by_ 参数。
函数的语法如下：
```swift
stride(from:to:by:)
```
请注意 `to` 值是不包含的

---

使用 `stride()` 函数，我们还可以使用闭区间，方法是使用：
```swift
stride(from:through:by:)
```
在这种情况下，`through` 值是包含的

---

在 Swift 中我们还有 `forEach` 循环。
实际上，`forEach` 按照与 `for-in` 循环相同的顺序对序列中的每个元素调用给定的闭包：
```swift
// this is an array, we'll see about that soon
let numbers: [Int] = [1, 3, 5, 7, 9]
numbers.forEach { num in
    print(num)
}
```
使用 `forEach` 方法与 `for-in` 循环有两个重要区别：
1. 不能使用 `break` 或 `continue` 语句退出当前闭包调用或跳过后续调用。
2. 在闭包体中使用 `return` 语句只会退出闭包，不会退出外部作用域，也不会跳过后续调用。
