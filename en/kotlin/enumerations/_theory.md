An **enumeration** (or *enum*) defines a common type for a group of related values, so you can work with those values in a type-safe way.
In Kotlin you declare one with the `enum class` keywords, listing its **entries** separated by commas:
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
By convention entry names are written in upper case. Each entry is a value of the enum type and is accessed through the class name:
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
Enum classes must be declared at the top level of a file (or inside another class), never inside a function.

---

Every enum entry has two built-in properties:

- `name` is the entry's name as a `String`
- `ordinal` is its position in the declaration, starting from `0`

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

Enum entries are compared with `==`:
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

A `when` expression is the natural way to branch over an enum. When it covers **every** entry it is *exhaustive* and needs no `else` branch:
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
If you forget an entry, the compiler reports an error instead of letting the bug reach runtime.

---

An enum class can have a **constructor**, just like a regular class. Each entry then passes its own arguments, and the values are stored in properties:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
Constructor properties are usually declared with `val`, since an entry's data is not meant to change.

---

Enum classes can also declare **methods**. The list of entries must be closed with a semicolon `;` before any member declarations:
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
Inside a method you can access the entry's properties, as well as `name` and `ordinal`.

---

Every enum class exposes an `entries` property: a list of all its entries in declaration order. It is handy for iterating:
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
Being a list, `entries` also supports `size` and indexing, e.g. `Direction.entries[0]` is `NORTH`.

Older code uses the `values()` function instead, which returns an array; `entries` is the recommended choice since Kotlin 1.9.

---

To go from a `String` back to an entry, use the `valueOf` function. It looks up the entry whose `name` matches exactly:
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
The match is case-sensitive: `Direction.valueOf("east")` throws an `IllegalArgumentException` because no entry has that name.

---

An enum class can declare an **abstract method** and let every entry provide its own implementation in a body enclosed in braces:
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
Each entry behaves differently while still sharing the same type and method signature.

---

An **interface** declares methods without a body; any type that implements it must provide them:
```kotlin
interface Greeter {
    fun greet(): String
}
```
Enum classes can implement interfaces. You list the interface after a colon and mark each implementation with `override`. Inside the enum body, the current entry is `this` and other entries can be referenced without the class name:
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
