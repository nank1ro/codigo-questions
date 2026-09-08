**枚举**（或 *enum*）为一组相关的值定义了一个共同的类型，让你可以以类型安全的方式使用这些值。
在 Kotlin 中，你使用 `enum class` 关键字来声明枚举，用逗号分隔列出它的**枚举项**（entries）：
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
按照惯例，枚举项的名称使用大写字母书写。每个枚举项都是该枚举类型的一个值，通过类名进行访问：
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
枚举类必须在文件的顶层（或另一个类内部）声明，绝不能在函数内部声明。

---

每个枚举项都有两个内置属性：

- `name` 是该枚举项的名称，类型为 `String`
- `ordinal` 是它在声明中的位置，从 `0` 开始

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

枚举项使用 `==` 进行比较：
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

`when` 表达式是对枚举进行分支处理的自然方式。当它覆盖了**所有**枚举项时，它就是*穷举的*（exhaustive），不需要 `else` 分支：
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
如果你遗漏了某个枚举项，编译器会报错，而不是让这个 bug 一直存在到运行时。

---

枚举类可以像普通类一样拥有**构造函数**。每个枚举项传入自己的参数，这些值会被存储在属性中：
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
构造函数属性通常用 `val` 声明，因为一个枚举项的数据不应该改变。

---

枚举类还可以声明**方法**。在任何成员声明之前，枚举项列表必须以分号 `;` 结束：
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2);

    fun hasMoons(): Boolean {
        return moons > 0
    }
}
println(Planet.EARTH.hasMoons()) // true
```
在方法内部，你可以访问该枚举项的属性，以及 `name` 和 `ordinal`。

---

每个枚举类都暴露一个 `entries` 属性：按声明顺序列出其所有枚举项的列表。这对遍历很有用：
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
由于 `entries` 是一个列表，它也支持 `size` 和索引访问，例如 `Direction.entries[0]` 就是 `NORTH`。

较旧的代码会使用 `values()` 函数代替，它返回一个数组；从 Kotlin 1.9 开始，推荐使用 `entries`。

---

要从 `String` 反向得到枚举项，可以使用 `valueOf` 函数。它会查找 `name` 完全匹配的枚举项：
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
匹配是区分大小写的：`Direction.valueOf("east")` 会抛出 `IllegalArgumentException`，因为没有任何枚举项叫这个名字。

---

枚举类可以声明一个**抽象方法**，让每个枚举项在用花括号括起来的代码体中提供自己的实现：
```kotlin
enum class Operation {
    ADD {
        override fun apply(a: Int, b: Int): Int = a + b
    },
    SUBTRACT {
        override fun apply(a: Int, b: Int): Int = a - b
    };

    abstract fun apply(a: Int, b: Int): Int
}
println(Operation.ADD.apply(2, 3)) // 5
```
每个枚举项的行为各不相同，但仍然共享相同的类型和方法签名。

---

**接口**声明没有方法体的方法；任何实现它的类型都必须提供这些方法：
```kotlin
interface Greeter {
    fun greet(): String
}
```
枚举类可以实现接口。你在冒号后列出接口，并用 `override` 标记每个实现。在枚举体内部，当前枚举项是 `this`，其他枚举项可以不带类名直接引用：
```kotlin
enum class Language : Greeter {
    ENGLISH, ITALIAN;

    override fun greet(): String = when (this) {
        ENGLISH -> "Hello"
        ITALIAN -> "Ciao"
    }
}
println(Language.ITALIAN.greet()) // Ciao
```
