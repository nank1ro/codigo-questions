函数是执行特定任务的代码块，可以在程序中重复使用。
在 Kotlin 中，使用 `fun` 关键字定义函数，后跟函数名和括号：
```kotlin
fun greet() {
    println("Hello!")
}
```
要调用（执行）函数，使用函数名加括号：
```kotlin
greet() // prints Hello!
```
不返回值的函数会隐式返回 `Unit`。

---

函数可以返回值。在括号后使用冒号指定返回类型：
```kotlin
fun getNumber(): Int {
    return 42
}
```
`return` 关键字将值传回调用方：
```kotlin
var result = getNumber()
println(result) // prints 42
```
返回类型必须与返回的值的类型一致。

---

函数可以接受参数，参数是调用函数时传入的输入值。
参数在括号内声明，包含名称和类型：
```kotlin
fun greet(name: String) {
    println("Hello, $name!")
}
```
调用函数时传入实参：
```kotlin
greet("Alice") // prints Hello, Alice!
```
参数使你能编写可与不同值一起使用的可复用代码。

---

Kotlin 支持参数默认值。如果调用方没有提供实参，则使用默认值：
```kotlin
fun greet(name: String = "World") {
    println("Hello, $name!")
}
greet()         // prints Hello, World!
greet("Alice")  // prints Hello, Alice!
```
默认值使参数变为可选，减少了对重载函数的需求。

---

当函数体只包含单个表达式时，可以使用带 `=` 的单表达式语法：
```kotlin
fun square(n: Int): Int = n * n
```
这比块体形式更简洁。Kotlin 通常可以推断返回类型，因此也可以写成：
```kotlin
fun square(n: Int) = n * n
```
单表达式函数是 Kotlin 中用于简单计算的常见惯用法。

---

函数可以返回 `Boolean` 值，这对于检查条件很有用：
```kotlin
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
println(isEven(4)) // prints true
println(isEven(7)) // prints false
```
`Boolean` 函数返回 `true` 或 `false`。

---

函数可以有多个不同类型的参数：
```kotlin
fun introduce(name: String, age: Int): String {
    return "My name is $name and I am $age years old."
}
println(introduce("Bob", 30))
// prints My name is Bob and I am 30 years old.
```
命名参数允许使用参数名以任意顺序传值：
```kotlin
println(introduce(age = 30, name = "Bob"))
```

---

Kotlin 中的基本函数使用 `fun` 关键字，后跟名称和括号：
```kotlin
fun sayBye() {
    println("Bye!")
}
```

---

要声明函数的返回类型，在括号后添加冒号和类型：
```kotlin
fun getName(): String {
    return "Alice"
}
```

---

函数参数用名称、冒号和类型来声明：
```kotlin
fun greet(name: String) {
    println("Hi, $name!")
}
```

---

单表达式函数使用 `=` 代替块体：
```kotlin
fun triple(n: Int) = n * 3
```
这是以下写法的简写：
```kotlin
fun triple(n: Int): Int {
    return n * 3
}
```
