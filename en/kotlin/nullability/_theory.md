Sometimes a value is simply missing: a user without a middle name, a search that finds nothing, a text that cannot be turned into a number.
Kotlin represents a missing value with `null`, but a normal variable can never hold it. Every type is **non-null** by default:
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
To allow a missing value you declare a **nullable** type by adding a question mark `?` after the type.
A `String?` holds either a `String` or `null`:
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String` and `String?` are two different types: a `String` is never missing, a `String?` may be.

---

The difference between `String` and `String?` is checked by the **compiler**, not at runtime.
Assigning `null` to a non-null type, or passing a nullable value where a non-null one is expected, is a compile error, so the program never even starts:
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
This is how Kotlin avoids the "null pointer" crashes common in other languages: a value can be missing only where you explicitly declared it with `?`.

---

The `?` works anywhere a type is written: a function can accept a nullable parameter and can return a nullable value.
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
You cannot call a method directly on a nullable value, because it might be `null`.
The **safe call** operator `?.` calls the method only when the value is not `null`; otherwise the whole expression is `null`:
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
The result of a safe call is always nullable: `word?.length` is an `Int?`, not an `Int`.

---

Very often all you want from a nullable value is the value itself or a default.
The **Elvis operator** `?:` does exactly that: it returns the left side when it is not `null`, otherwise the value on its right:
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
Since the right side is used only when the left is `null`, the result is non-null when the default is.
`?:` combines nicely with `?.` to turn a safe call back into a plain value:
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

Safe calls can be **chained**: as soon as one link is `null` the rest of the chain is skipped and the whole expression becomes `null`.
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
A chain ending with `?:` gives you a non-null result in one line:
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

Safe call chains shine with nested objects, where any level may be missing:
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
Each `?.` protects the next step, and the final `?:` supplies the default.

---

The **not-null assertion** operator `!!` converts a nullable value into a non-null one, telling the compiler "I am sure this is not `null`":
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
If you are wrong and the value is `null`, the program crashes at runtime with a `NullPointerException`, the very error Kotlin was designed to prevent:
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
Use `!!` only when the value truly cannot be `null`; prefer `?.`, `?:` and null checks everywhere else.

---

When you check a value for `null` with `if`, the compiler remembers it: inside the branch where the value is known to be non-null, it is **smart cast** to the non-null type and you can use it directly, without `?.` or `!!`:
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
The same happens after an early exit:
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
Smart casts work on `val` variables and function parameters, whose value cannot change between the check and the use.

---

`let` runs a block of code with the value it is called on, available inside the block as `it`.
Combined with a safe call, `?.let` runs the block **only** when the value is not `null`, and inside the block `it` is non-null:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
It is a compact alternative to `if (x != null) { ... }` when you only need the value inside the block.

---

`let` also **returns** the value of the last expression in its block, so `?.let` can transform a nullable value and `?:` can fill in the default when it is `null`:
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
When `price` is `null` the `let` block is skipped, the expression is `null` and the Elvis operator returns `"free"`.

---

Collections can hold nullable elements too: a `List<Int?>` may contain `null` entries, while a `List<Int>` never does.
`filterNotNull()` returns a new list with the `null` entries removed, and its element type becomes non-null, so you can use the elements freely:
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

Many standard functions return `null` instead of failing. `toIntOrNull()` converts a string into an `Int`, or returns `null` when the text is not a whole number:
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
`mapNotNull` transforms every element like `map`, but drops the results that are `null`:
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

Sometimes a property cannot be given a value when the object is created, but you know it will be set before it is used.
Instead of making it nullable, mark it with `lateinit`: the type stays non-null and no `?.` is needed when reading it:
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
`lateinit` has some rules: it works only on `var` properties, only with non-null types, and not with primitive types like `Int` or `Boolean`.
Reading a `lateinit` property before assigning it throws an `UninitializedPropertyAccessException`; you can check it first with `::player.isInitialized`.

---

When a `null` means the caller made a mistake, fail early with `requireNotNull`.
It returns the value as non-null when it is present, and throws an `IllegalArgumentException` when it is `null`, with an optional message:
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
After the call the compiler also smart casts `name` itself to `String`, so `name.length` is allowed from that line on.
Unlike `!!`, the failure carries a clear message and states that the *argument* was wrong.

---

An extension function can be declared on a **nullable receiver**, so it can be called even on a `null` value. Inside, `this` is nullable and must be checked:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
Note that no `?.` is needed at the call site: the function itself handles the `null` case.
The standard library uses this trick in `isNullOrEmpty()` and `orEmpty()`, which are safe to call on any `String?`.

---

The right side of `?:` can be any expression, including `return`. This gives a compact way to bail out of a function as soon as a value is missing:
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
Every tool you have seen combines well: nullable parameters and return types describe *where* a value may be missing, and `?.`, `?:`, `let`, smart casts and `toIntOrNull` handle it without ever crashing.
