A **class** is a blueprint for creating objects. In Kotlin, you declare a class with the `class` keyword followed by the class name.

A class can hold **properties** (data) and **methods** (behaviour). To declare a property directly in the constructor, prefix it with `val` or `var`:

```kotlin
class Dog(val name: String)
```

This creates a `Dog` class with a `name` property. You create an instance by calling the class like a function:

```kotlin
val dog = Dog("Rex")
println(dog.name) // Rex
```

---

Classes can have multiple properties in their **primary constructor**. Each property is declared with `val` (read-only) or `var` (mutable) directly in the constructor parameter list:

```kotlin
class Person(val name: String, var age: Int)
```

The `val` keyword makes `name` read-only after creation, while `var` makes `age` mutable — you can change it later:

```kotlin
val p = Person("Alice", 30)
p.age = 31  // allowed because age is var
```

---

The **`init` block** runs immediately after the primary constructor. It is used to perform validation or setup logic when an object is created:

```kotlin
class Circle(val radius: Double) {
    init {
        require(radius > 0) { "Radius must be positive" }
    }
}
```

You can also initialise additional properties inside `init`:

```kotlin
class Square(val side: Int) {
    val area: Int
    init {
        area = side * side
    }
}
```

---

Classes can contain **methods** — functions that belong to the class and operate on its properties:

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

Methods are called using dot notation on an instance:

```kotlin
val c = Counter(0)
c.increment()
println(c.value()) // 1
```

---

A **`data class`** is a special class designed to hold data. Kotlin automatically generates `equals()`, `hashCode()`, `toString()`, and `copy()` for you:

```kotlin
data class Point(val x: Int, val y: Int)

val p = Point(1, 2)
println(p)           // Point(x=1, y=2)
println(p.toString()) // Point(x=1, y=2)
```

The `copy()` function creates a new instance with some properties changed:

```kotlin
val p2 = p.copy(y = 10)
println(p2) // Point(x=1, y=10)
```
