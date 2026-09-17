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

---

有时你需要某个东西**恰好只有一个**实例：日志器、注册表、应用配置。把 `class` 换成 `object` 就能为你声明这个单例：

```kotlin
object Registry {
    var size = 0
    fun add() {
        size++
    }
}

Registry.add()
println(Registry.size) // 1
```

实例在你第一次使用它时才被创建，而且你直接使用这个名字本身，没有 `Registry()` 调用，也没有构造函数。`object` 可以持有属性、方法、`init` 块，还可以实现接口或扩展一个类。

---

`companion object`（伴生对象）是属于某个类的单例。除了常量之外，它的天然职责是存放**工厂函数**：这类函数在构建实例之前先检查或转换输入，并在输入没有意义时返回 `null`。

把构造函数标记为 `private`，就迫使所有调用者都通过工厂：

```kotlin
class Age private constructor(val years: Int) {
    companion object {
        fun of(years: Int): Age? = if (years >= 0) Age(years) else null
    }
}

println(Age.of(30)?.years) // 30
println(Age.of(-1))        // null
```

伴生对象通过类名调用，即 `Age.of(...)`，由于它位于类的内部，所以可以访问私有的构造函数。

---

`interface`（接口）列出了一个类型能做什么。它的成员默认是抽象的，但接口也可以提供**默认实现**——一个每个实现类都免费继承并且可以覆盖的方法体：

```kotlin
interface Greeter {
    val name: String              // abstract,类必须提供它
    fun greet(): String = "Hi, $name"  // 默认实现
}

class Person(override val name: String) : Greeter

class Robot(override val name: String) : Greeter {
    override fun greet(): String = "BEEP $name"
}

println(Person("Ann").greet()) // Hi, Ann
println(Robot("R2").greet())   // BEEP R2
```

接口不能存储状态（它没有幕后字段），所以抽象属性必须由类来实现，通常是通过构造函数中的 `override val`。与类不同，一个类型可以实现任意多个接口。

---

`abstract` 类介于接口和普通类之间：它不能被实例化，并且把没有方法体、必须被覆盖的**抽象**成员，与子类按原样继承的具体成员混合在一起。

```kotlin
abstract class Vehicle(val name: String) {
    abstract fun wheels(): Int
    fun describe(): String = "$name has ${wheels()} wheels"
}

class Bike(name: String) : Vehicle(name) {
    override fun wheels(): Int = 2
}

println(Bike("BMX").describe()) // BMX has 2 wheels
```

与接口不同，抽象类拥有构造函数，可以在属性中存储状态，这就是子类通过 `: Vehicle(name)` 把 `name` 向上传递的原因。一个类只能扩展一个类，所以当子类共享数据时使用抽象类，当它们只共享行为时使用接口。抽象成员无需添加 `open` 即可被覆盖。

---

声明在另一个类内部的类默认是**嵌套类**。它对外部实例一无所知，你要通过外部类的类名来构建它：

```kotlin
class Outer {
    class Nested {
        fun hello() = "hi"
    }
}

println(Outer.Nested().hello()) // hi
```

加上 `inner` 关键字后情况就不同了：`inner` 类持有对外部实例的引用，因此它可以读取外部类的属性，而且你要**从实例出发**来构建它：

```kotlin
class Counter(val step: Int) {
    inner class Doubler {
        fun value() = step * 2
    }
}

println(Counter(5).Doubler().value()) // 10
```

在 `inner` 类内部，`this` 指的是内部对象；当你需要显式引用外部对象时，使用 `this@Counter`。

---

本主题的各个部分通常会组合在一起使用：`enum class` 的枚举项带有各自的属性，用来为固定的一组标签建模；而 `data class` 则承载与它们一起传递的数据。

```kotlin
enum class Speed(val surcharge: Int) {
    STANDARD(0),
    EXPRESS(15)
}

data class Order(val total: Int, val speed: Speed)

val order = Order(100, Speed.EXPRESS)
println(order.total + order.speed.surcharge) // 115
```
