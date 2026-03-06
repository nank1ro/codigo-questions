让我们从**等于** `==` 比较运算符开始。
它返回一个**布尔值**（`true` 或 `false`），表示两个表达式是否相等，例如：
```kotlin
println(2 == 2) // true
println(2 == 3) // false
```

---

让我们继续学习**不等于** `!=` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示两个表达式是否**不**相等，例如：
```kotlin
println(2 != 2) // false
println(2 != 3) // true
```
它与*等于*运算符的结果正好相反

---

让我们继续学习**大于** `>` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否大于另一个，例如：
```kotlin
println(2 > 2) // false
println(3 > 2) // true
```

---

让我们继续学习**小于** `<` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否小于另一个，例如：
```kotlin
println(2 < 2) // false
println(2 < 3) // true
```

---

让我们继续学习**大于或等于** `>=` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否大于或等于另一个，例如：
```kotlin
println(2 >= 2) // true
println(3 >= 2) // true
println(3 >= 4) // false
```

---

让我们继续学习**小于或等于** `<=` 比较运算符。
它返回一个**布尔值**（`true` 或 `false`），表示一个表达式是否小于或等于另一个，例如：
```kotlin
println(2 <= 2) // true
println(3 <= 2) // false
println(3 <= 4) // true
```

---

现在让我们来看**逻辑**运算符，首先从第一个叫做 __AND__ `&&` 的开始。
它返回第一个求值为 *false* 的操作数，或者如果所有操作数都为 *true* 则返回最后一个。
```kotlin
println(2 == 2 && 2 == 3) // false
println(1 == 1 && 1.0 == 1.0) // true
```

---

让我们继续学习**或** `||` 逻辑运算符。
它返回第一个求值为 *true* 的操作数，或者如果所有操作数都为 *false* 则返回最后一个。
```kotlin
println(2 == 2 || 2 == 3) // true
println(1 == 2 || 1 == 3) // false
```

---

最后让我们来学习**非** `!` 逻辑运算符。
它返回一个布尔值，是表达式逻辑状态的反转。
```kotlin
println(!true) // false
println(!false) // true
println(!(2 == 2)) // false
```
