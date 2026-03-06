Kotlin 有一个基本的布尔类型，称为 `Boolean`。
布尔值被称为逻辑值，因为它们只能是 true 或 false。
你可以对 Kotlin 中的任何表达式求值，得到两个结果之一：`true` 或 `false`。

---

我们可以像存储数字或字符串一样，将布尔值 `true` 存储在变量中。

---

`true` 的相反值是 `false`

---

布尔值也可以通过在其前面使用 `!` 来取反，例如：
```kotlin
println(!true) // prints false
println(!false) // prints true
```

---

我们还可以使用 `&&`（_与_）和 `||`（_或_）创建布尔表达式：

- `&&`（_与_）：只有当运算符左侧和右侧的布尔表达式都为 true 时，才产生 true。
- `||`（_或_）：如果运算符左侧或右侧的表达式为 true，或者两者都为 true，则产生 true。

```kotlin
println(true && true) // prints true
println(true && false) // prints false
println(false && false) // prints false
println(true || true) // prints true
println(true || false) // prints true
println(false || false) // prints false
```
