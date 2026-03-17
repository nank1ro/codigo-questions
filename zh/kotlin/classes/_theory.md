**类**是创建对象的蓝图。在 Kotlin 中，你使用 `class` 关键字后跟类名来声明一个类。

类可以包含**属性**（数据）和**方法**（行为）。要在构造函数中直接声明属性，需在其前面加上 `val` 或 `var`：

```kotlin
class Dog(val name: String)
```

这会创建一个带有 `name` 属性的 `Dog` 类。通过像调用函数一样调用类来创建实例：

```kotlin
val dog = Dog("Rex")
println(dog.name) // Rex
```

---

类的**主构造函数**可以有多个属性。每个属性直接在构造函数参数列表中用 `val`（只读）或 `var`（可变）声明：

```kotlin
class Person(val name: String, var age: Int)
```

`val` 关键字使 `name` 在创建后只读，而 `var` 使 `age` 可变——你可以在之后修改它：

```kotlin
val p = Person("Alice", 30)
p.age = 31  // 允许，因为 age 是 var
```

---

**`init` 块**在主构造函数之后立即执行。它用于在创建对象时执行验证或初始化逻辑：

```kotlin
class Circle(val radius: Double) {
    init {
        require(radius > 0) { "半径必须为正数" }
    }
}
```

你也可以在 `init` 中初始化额外的属性：

```kotlin
class Square(val side: Int) {
    val area: Int
    init {
        area = side * side
    }
}
```

---

类可以包含**方法**——属于类并操作其属性的函数：

```kotlin
class Counter(var count: Int) {
    fun increment() {
        count++
    }
    fun value(): Int {
        return count
    }
}
```

方法通过实例上的点符号调用：

```kotlin
val c = Counter(0)
c.increment()
println(c.value()) // 1
```

---

**`data class`** 是专为保存数据而设计的特殊类。Kotlin 会自动为你生成 `equals()`、`hashCode()`、`toString()` 和 `copy()`：

```kotlin
data class Point(val x: Int, val y: Int)

val p = Point(1, 2)
println(p)           // Point(x=1, y=2)
println(p.toString()) // Point(x=1, y=2)
```

`copy()` 函数会创建一个修改了某些属性的新实例：

```kotlin
val p2 = p.copy(y = 10)
println(p2) // Point(x=1, y=10)
```
