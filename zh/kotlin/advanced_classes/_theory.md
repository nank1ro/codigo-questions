`data class` 是一种以**保存数据**为职责的类。编译器会根据你在主构造函数中声明的属性，自动为你生成四个成员：

- `toString()`，一段可读的 `ClassName(prop=value, ...)` 文本
- `equals()` 和 `hashCode()`，使两个具有相同数据的实例被视为相等
- `copy()`，它会在复用当前值的基础上构建一个新实例

```kotlin
data class Book(val title: String, val pages: Int)

val book = Book("Dune", 412)
println(book)          // Book(title=Dune, pages=412)
println(book.copy())   // Book(title=Dune, pages=412)
```

`copy()` 在配合**命名参数**使用时大放异彩：你只需写出想要修改的属性，其余的值都会被沿用。

```kotlin
println(book.copy(pages = 500)) // Book(title=Dune, pages=500)
```

原始对象永远不会被修改：`copy()` 会返回一个全新的对象。

---

对于主构造函数中的每个属性，data class 还会生成一个 `componentN()` 函数：第一个属性对应 `component1()`，第二个属性对应 `component2()`，依此类推。

这些函数支撑起**解构声明**（destructuring declarations），让你在一行内把一个对象拆包到多个变量中：

```kotlin
data class Point(val x: Int, val y: Int)

val point = Point(3, 7)
val (x, y) = point
println(x)               // 3
println(point.component2()) // 7
```

变量的顺序遵循属性的声明顺序，而不是属性的名字。使用 `_` 可以跳过不需要的属性：

```kotlin
val (_, onlyY) = point
```

---

生成的 `equals()` 使 `==` 成为**结构**比较：当主构造函数中的每个属性都相等时，两个实例就相等。`===` 运算符则不同，它询问的是两个名字是否指向内存中**同一个对象**。

```kotlin
data class User(val id: Int, val name: String)

val a = User(1, "Ann")
val b = User(1, "Ann")
println(a == b)  // true,数据相同
println(a === b) // false,两个不同的对象
println(a === a) // true
```

由于 `hashCode()` 与 `equals()` 一起生成，data class 实例在 `Set` 中或作为 `Map` 键时也能正确工作：重复项会被合并。

```kotlin
println(setOf(a, b).size) // 1
```

普通类不会生成这些，所以对它来说 `==` 回退为同一性比较。

---

生成的成员只关注**主构造函数**中声明的属性。声明在类**体**中的属性是一个普通属性：它不属于 `toString()`、`equals()`、`hashCode()` 或 `copy()` 的一部分。

```kotlin
data class Item(val name: String) {
    var quantity: Int = 0
}

val a = Item("nail")
a.quantity = 5
println(a) // Item(name=nail)
```

这一点很容易忘记，所以请把标识对象的一切放进主构造函数，而把派生的或临时的状态留在类体中。

---

`sealed` 类描述了一个**封闭**的备选项集合：只允许编写在同一个包和模块中的子类，因此编译器知道每一个子类。

```kotlin
sealed class Shape
data class Circle(val radius: Int) : Shape()
data class Square(val side: Int) : Shape()
```

它的回报是**穷举的 `when`**：当你对密封类型分支并覆盖每个子类时，可以省略 `else` 分支。之后新增一个子类时，编译器会报告每一个你忘记更新的 `when`，而不是默默走 `else` 分支。

```kotlin
fun name(shape: Shape): String = when (shape) {
    is Circle -> "circle"
    is Square -> "square"
}
```

在 `is Circle` 之后，值会被智能转换，因此在该分支内可以直接使用 `shape.radius`，无需任何手动转换。
