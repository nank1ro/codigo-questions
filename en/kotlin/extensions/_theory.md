An **extension function** adds a new function to an existing type without touching its source code.
You write `fun`, then the type you want to extend (the **receiver type**), a dot, and the name of the function:
```kotlin
fun Int.squared(): Int {
    return this * this
}
println(4.squared()) // 16
```
Inside the function, `this` is the value the function is called on, called the **receiver**: in `4.squared()` it is `4`.
Once the extension exists, you call it with the dot exactly like a function that was part of `Int` from the start.

---

Extensions work on any type, even the ones you don't have the source code for. `String` comes from the standard library, but you can still give it new functions:
```kotlin
fun String.whisper(): String {
    return this.lowercase() + "..."
}
println("HELLO".whisper()) // hello...
```
Inside an extension you can drop `this.` when using other members of the receiver: `lowercase()` alone means `this.lowercase()`, and `length` alone means `this.length`.

---

An extension function can take parameters like any other function. The receiver stays on the left of the dot and the parameters go between the parentheses:
```kotlin
fun Int.isDivisibleBy(other: Int): Boolean {
    return this % other == 0
}
println(12.isDivisibleBy(4)) // true
println(12.isDivisibleBy(5)) // false
```
The type in front of the dot is a normal type, so you can extend `List<Int>`, `Double` or a class you wrote in the same way.

---

An extension does **not** modify the class it extends and does not insert a new member into it. The compiler simply rewrites the call: `"kotlin".first3()` becomes a call to the function with `"kotlin"` passed as `this`.
```kotlin
fun String.first3(): String = take(3)
val word = "kotlin"
println(word.first3()) // kot
```
This is why you can extend final classes like `String` and `Int`: nothing inside them changes, the extension only lives in your code.

---

Besides functions, you can add an **extension property**. It is declared with `val`, the receiver type, a dot and the name, followed by a `get()` that computes the value every time the property is read:
```kotlin
val String.wordCount: Int
    get() = split(" ").size

println("Kotlin is fun".wordCount) // 3
```
An extension property can't store anything: it has no backing field, so an initializer like `val String.label = "text"` is a compile error. It can only compute its value from the receiver.
Extension properties cannot be declared inside a function (local extension properties are not allowed), unlike extension functions.

---

Extension properties are read without parentheses, exactly like the built-in `length` of a `String`. They are the natural choice when the value describes the receiver rather than doing something with it:
```kotlin
val Int.isNegative: Boolean
    get() = this < 0

println((-3).isNegative) // true
println(7.isNegative)    // false
```
Note the parentheses around `-3`: without them `-3.isNegative` would read the property of `3` first and then try to negate a `Boolean`, which doesn't compile.

---

The receiver type can be **nullable**. An extension on `String?` can be called on a variable that may hold `null`, and inside the function `this` is a `String?`, so you handle the `null` case yourself, usually with the Elvis operator `?:` you met in the nullability lessons:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val name: String? = null
println(name.orDash())  // -
println("Ada".orDash()) // Ada
```
Calling `name.orDash()` on a `null` value is safe: no `?.` is needed, because the function itself accepts a `null` receiver.

---

Inside an extension with a nullable receiver you can also use the safe call `this?.` to reach the members of the value only when it is not `null`. The standard library uses the same idea for functions like `isNullOrEmpty()`:
```kotlin
fun String?.firstOrQuestion(): Char {
    return this?.firstOrNull() ?: '?'
}
val text: String? = null
println(text.firstOrQuestion())    // ?
println("Kotlin".firstOrQuestion()) // K
```

---

When a class already has a member with the same name and parameters as an extension, the **member always wins**: the extension is never called, and the compiler warns you that it is shadowed.
```kotlin
class Box {
    fun describe(): String = "member"
}
fun Box.describe(): String = "extension"

println(Box().describe()) // member
```
An extension can't override or replace existing behaviour; it can only add new functions and properties. To be picked, an extension needs a name or a parameter list that the class doesn't already have.

---

An extension can work on a family of types at once thanks to a **type parameter**: a placeholder for a type, declared between angle brackets right after `fun`, that Kotlin fills in at every call. This makes the extension **generic**:
```kotlin
fun <T> List<T>.second(): T {
    return this[1]
}
println(listOf(1, 2, 3).second())      // 2
println(listOf("a", "b").second())     // b
```
With `listOf(1, 2, 3)` the placeholder `T` is `Int`, with `listOf("a", "b")` it is `String`, so the same function returns the right type every time.

---

The type parameter can be used anywhere in the signature: as the return type, as a nullable `T?`, or inside another type. A generic extension that may find nothing returns `T?`, like the built-in `firstOrNull()`:
```kotlin
fun <T> List<T>.lastOrDefault(default: T): T {
    return if (isEmpty()) default else this[size - 1]
}
println(listOf(1, 2).lastOrDefault(0))          // 2
println(emptyList<String>().lastOrDefault("-")) // -
```
Inside the function you can use `size`, `isEmpty()` and indexing exactly as on any list, because the receiver is a `List<T>`.

---

You can also extend the **companion object** of a class, as long as the class declares one, even an empty one. The receiver type is written `ClassName.Companion`, and the extension is then called on the class name, like a factory function:
```kotlin
class Temperature(val degrees: Int) {
    companion object
}
fun Temperature.Companion.freezing(): Temperature = Temperature(0)

println(Temperature.freezing().degrees) // 0
```
The class and the extension are both top-level declarations, so they must be written outside `main`.

---

A companion extension can take parameters, which makes it a handy place for alternative constructors that convert from another unit or format:
```kotlin
class Distance(val meters: Int) {
    companion object
}
fun Distance.Companion.fromKilometers(km: Int): Distance = Distance(km * 1000)

println(Distance.fromKilometers(3).meters) // 3000
```

---

Where you declare an extension decides where it can be used, its **scope**:
- at the top level of a file, it is available in the whole file and in the rest of the package
- inside a function, it is a local extension, usable only in that function
- inside a class, it is a **member extension**, usable only inside that class

A member extension can read the properties of the class it lives in, so it combines two receivers: the class instance and the value it is called on:
```kotlin
class Greeter(val greeting: String) {
    fun String.greet(): String = "$greeting, $this!"
    fun welcome(name: String): String = name.greet()
}
println(Greeter("Hello").welcome("Ada")) // Hello, Ada!
```
Inside `greet`, `greeting` comes from the `Greeter` and `this` is the `String` the function is called on. Outside the class, `"Ada".greet()` is a compile error.

---

An extension function with exactly **one** parameter can be marked `infix`. An infix function can be called without the dot and the parentheses, with the receiver on the left and the argument on the right, which reads almost like a sentence:
```kotlin
infix fun Int.percentOf(total: Int): Int = total * this / 100

println(20 percentOf 50)   // 10
println(20.percentOf(50))  // 10, the normal call still works
```
Kotlin uses this for some built-in functions too: `1 to "one"` builds a `Pair`, and `1 until 5` builds a range.

---

To be marked `infix`, a function must be a member or an extension, must take exactly one parameter, and that parameter can't have a default value. Anything else is a compile error:
```kotlin
infix fun Int.add(other: Int): Int = this + other          // ok
infix fun add(a: Int, b: Int): Int = a + b                 // error: not a member or extension
infix fun Int.add(a: Int, b: Int): Int = this + a + b      // error: two parameters
```
Infix calls sit between arithmetic and comparison in precedence: `1 add 2 * 3` is `1 add 6`, while `1 add 2 == 3` compares the result with `3`.
