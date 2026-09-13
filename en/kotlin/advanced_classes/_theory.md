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
