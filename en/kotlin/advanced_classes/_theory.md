A `data class` is a class whose job is to **hold data**. From the properties you declare in the primary constructor the compiler generates four members for you:

- `toString()`, a readable `ClassName(prop=value, ...)` text
- `equals()` and `hashCode()`, so two instances with the same data count as equal
- `copy()`, which builds a new instance reusing the current values

```kotlin
data class Book(val title: String, val pages: Int)

val book = Book("Dune", 412)
println(book)          // Book(title=Dune, pages=412)
println(book.copy())   // Book(title=Dune, pages=412)
```

`copy()` really shines with **named arguments**: you name only the properties you want to change, and every other value is carried over.

```kotlin
println(book.copy(pages = 500)) // Book(title=Dune, pages=500)
```

The original is never modified: `copy()` returns a brand new object.

---

For every property in the primary constructor a data class also generates a `componentN()` function: `component1()` for the first property, `component2()` for the second, and so on.

Those functions power **destructuring declarations**, where you unpack an object into several variables in one line:

```kotlin
data class Point(val x: Int, val y: Int)

val point = Point(3, 7)
val (x, y) = point
println(x)               // 3
println(point.component2()) // 7
```

The order of the variables follows the order of the properties, not their names. Use `_` to skip one you don't need:

```kotlin
val (_, onlyY) = point
```

---

The generated `equals()` makes `==` a **structural** comparison: two instances are equal when every property of the primary constructor is equal. The `===` operator is different, it asks whether both names point to the **very same object** in memory.

```kotlin
data class User(val id: Int, val name: String)

val a = User(1, "Ann")
val b = User(1, "Ann")
println(a == b)  // true, same data
println(a === b) // false, two different objects
println(a === a) // true
```

Because `hashCode()` is generated together with `equals()`, data class instances also behave correctly inside a `Set` or as `Map` keys: duplicates collapse.

```kotlin
println(setOf(a, b).size) // 1
```

A regular class generates none of this, so for it `==` falls back to identity.

---

The generated members only look at the properties declared in the **primary constructor**. A property declared in the class **body** is a normal property: it is not part of `toString()`, `equals()`, `hashCode()` or `copy()`.

```kotlin
data class Item(val name: String) {
    var quantity: Int = 0
}

val a = Item("nail")
a.quantity = 5
println(a) // Item(name=nail)
```

This is easy to forget, so put in the primary constructor everything that identifies the object, and keep derived or temporary state in the body.

---

A `sealed` class describes a **closed** set of alternatives: only the subclasses written in the same package and module are allowed, so the compiler knows every one of them.

```kotlin
sealed class Shape
data class Circle(val radius: Int) : Shape()
data class Square(val side: Int) : Shape()
```

The payoff is the **exhaustive `when`**: when you branch over a sealed type and cover every subclass, you can drop the `else` branch. Add a new subclass later and the compiler reports every `when` you forgot to update, instead of silently taking the `else`.

```kotlin
fun name(shape: Shape): String = when (shape) {
    is Circle -> "circle"
    is Square -> "square"
}
```

After `is Circle` the value is smart cast, so `shape.radius` is available inside that branch without any manual cast.

---

Sometimes you need exactly **one** instance of something: a logger, a registry, an application configuration. Replacing `class` with `object` declares that singleton for you:

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

The instance is created the first time you touch it, and you use the name itself, there is no `Registry()` call and no constructor. An `object` can hold properties, methods, `init` blocks, and it can implement interfaces or extend a class.

---

A `companion object` is the singleton that belongs to a class. Besides constants, its natural job is holding **factory functions**: functions that check or transform the input before building an instance, and that can return `null` when the input makes no sense.

Marking the constructor `private` forces every caller through the factory:

```kotlin
class Age private constructor(val years: Int) {
    companion object {
        fun of(years: Int): Age? = if (years >= 0) Age(years) else null
    }
}

println(Age.of(30)?.years) // 30
println(Age.of(-1))        // null
```

The companion is called on the class name, `Age.of(...)`, and it can reach the private constructor because it lives inside the class.

---

An `interface` lists what a type can do. Its members are abstract by default, but an interface may also ship a **default implementation**, a body that every implementing class inherits for free and may override:

```kotlin
interface Greeter {
    val name: String              // abstract, the class must provide it
    fun greet(): String = "Hi, $name"  // default implementation
}

class Person(override val name: String) : Greeter

class Robot(override val name: String) : Greeter {
    override fun greet(): String = "BEEP $name"
}

println(Person("Ann").greet()) // Hi, Ann
println(Robot("R2").greet())   // BEEP R2
```

An interface cannot store state (it has no backing fields), so an abstract property has to be implemented by the class, usually with `override val` in the constructor. Unlike a class, a type can implement as many interfaces as it wants.

---

An `abstract` class sits between an interface and a normal class: it cannot be instantiated, and it mixes **abstract** members, which have no body and must be overridden, with concrete ones that subclasses inherit as they are.

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

Unlike an interface, an abstract class has a constructor and can store state in properties, which is why the subclass passes `name` up with `: Vehicle(name)`. A class can extend only one class, so reach for an abstract class when the subclasses share data, and for an interface when they only share behaviour. Abstract members are overridable without adding `open`.

---

A class declared inside another class is **nested** by default. It knows nothing about the outer instance and you build it from the outer class name:

```kotlin
class Outer {
    class Nested {
        fun hello() = "hi"
    }
}

println(Outer.Nested().hello()) // hi
```

Add the `inner` keyword and the situation changes: an `inner` class carries a reference to the outer instance, so it can read the outer properties, and you build it **from an instance**:

```kotlin
class Counter(val step: Int) {
    inner class Doubler {
        fun value() = step * 2
    }
}

println(Counter(5).Doubler().value()) // 10
```

Inside an `inner` class, `this` is the inner object; use `this@Counter` when you need the outer one explicitly.

---

The pieces of this topic are usually combined: an `enum class` whose entries carry their own properties models a fixed set of tags, while a `data class` carries the payload that goes with them.

```kotlin
enum class Speed(val surcharge: Int) {
    STANDARD(0),
    EXPRESS(15)
}

data class Order(val total: Int, val speed: Speed)

val order = Order(100, Speed.EXPRESS)
println(order.total + order.speed.surcharge) // 115
```
