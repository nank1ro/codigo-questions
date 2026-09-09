Every value in Kotlin has a **type**, which tells the compiler what kind of data it is and what you can do with it.
The basic types are:
- `Int`: a whole number, like `42` or `-7`
- `Long`: a whole number that can be much bigger than an `Int`
- `Double`: a number with a decimal part, like `3.14`
- `Float`: a decimal number that uses half the memory of a `Double`, but is less precise
- `Char`: a single character between single quotes, like `'a'`
- `Boolean`: either `true` or `false`
- `String`: a piece of text between double quotes, like `"Hello"`

As you saw in the variables lessons, you can state the type explicitly with a colon after the name:
```kotlin
val age: Int = 36
val name: String = "Ada"
```
A value of one type can't be stored in a variable of another type: `val age: Int = "36"` is a compile error.

---

Most of the time you don't write the type: Kotlin **infers** it from the value you assign, following a few literal rules:
- a whole number, like `42`, is an `Int`
- a number with a decimal point, like `3.14`, is a `Double`
- text between double quotes is a `String`
- a character between single quotes is a `Char`
- `true` and `false` are `Boolean`
```kotlin
val count = 42     // Int
val price = 9.99   // Double
val name = "Ada"   // String
val grade = 'A'    // Char
val isOpen = true  // Boolean
```
To check what Kotlin inferred you can print the name of the type of any value with `::class.simpleName`:
```kotlin
println(count::class.simpleName) // Int
println(price::class.simpleName) // Double
```
A decimal literal is never inferred as `Float`: `val ratio = 0.5` is a `Double`.

---

An `Int` can hold whole numbers up to about two billion, more precisely up to `Int.MAX_VALUE`, which is `2147483647`.
A whole-number literal too big for an `Int` is automatically inferred as a `Long`, and you can force a `Long` for any literal with the suffix `L`:
```kotlin
val big = 3000000000  // Long, too big for an Int
val small = 3L        // Long, thanks to the suffix
```
In the same way the suffix `f` turns a decimal literal into a `Float`: `val ratio = 0.5f`.
Long numbers are hard to read, so Kotlin lets you place underscores `_` anywhere between the digits; they are ignored by the compiler:
```kotlin
val population = 8_000_000_000L
val million = 1_000_000
println(million) // 1000000
```

---

Kotlin never converts between number types on its own when you assign a value, not even from a smaller type to a bigger one: storing an `Int` in a `Long` or `Double` variable is a compile error.
```kotlin
val count = 3
val total: Long = count      // error: Int is not a Long
val price: Double = count    // error: Int is not a Double
```
Every number type has **conversion functions** that build a new value of the type you need: `toInt()`, `toLong()`, `toDouble()`, `toFloat()` and, to get text, `toString()`.
```kotlin
val total: Long = count.toLong()
val price: Double = count.toDouble() // 3.0
println(count.toString() + "!")      // 3!
```
Going from a decimal to a whole number **truncates**: `toInt()` simply drops the decimal part, so `3.99.toInt()` is `3` and `(-3.99).toInt()` is `-3`.

---

The types of the operands decide how division works. When both are `Int`, the `/` operator performs **integer division**: the result is an `Int` and the remainder is thrown away.
When at least one operand is a `Double`, `/` performs floating-point division and keeps the decimal part:
```kotlin
println(7 / 2)              // 3
println(7.0 / 2)            // 3.5
val slices = 7
println(slices.toDouble() / 2) // 3.5
```
So to get a decimal result from two `Int` variables you must convert at least one of them **before** dividing: `(7 / 2).toDouble()` is `3.0`, because the integer division has already happened.

---

When a function must return a decimal result computed from whole numbers, convert the operands to `Double` before dividing and declare the return type as `Double`:
```kotlin
fun ratio(part: Int, total: Int): Double {
    return part.toDouble() / total
}
println(ratio(1, 4)) // 0.25
```
Remember that `sum()` and `size` of a `List<Int>` are `Int` values too, so they need the same conversion.

---

Every `Char` is stored as a number, its **code**. The `code` property gives the `Int` behind a character, and `toChar()` does the opposite, turning an `Int` into the `Char` with that code:
```kotlin
println('A'.code)        // 65
println(66.toChar())     // B
println(('A'.code + 2).toChar()) // C
```
Letters have consecutive codes, so adding to the code moves along the alphabet.
Note that the code of `'7'` is `55`, not `7`: to read the digit a `Char` represents use `digitToInt()`, which returns `7`.

---

Since the code of a `Char` is an `Int`, you can do arithmetic on it and convert the result back to a `Char`. This is how you move along the alphabet:
```kotlin
val next = ('a'.code + 1).toChar() // 'b'
```
Kotlin also lets you add an `Int` directly to a `Char`: `'a' + 1` is `'b'`, and the difference between two characters `'d' - 'a'` is the `Int` `3`.

---

Text typed by a user always arrives as a `String`, even when it looks like a number. To do math with it you must **parse** it: `toInt()` turns `"42"` into the `Int` `42`, and `toDouble()` turns `"3.5"` into the `Double` `3.5`.
```kotlin
val typed = "42"
println(typed.toInt() + 1) // 43
```
Not every text is a number: `"4x2".toInt()` throws a `NumberFormatException` and stops the program.
The safe alternatives `toIntOrNull()` and `toDoubleOrNull()` return `null` instead of throwing, so, as you learned in the nullability lessons, you can provide a default with `?:`:
```kotlin
println("4x2".toIntOrNull())      // null
println("4x2".toIntOrNull() ?: 0) // 0
```

---

`toIntOrNull()` succeeds only when the whole text is a valid whole number, with an optional sign:
```kotlin
println("42".toIntOrNull())   // 42
println("-7".toIntOrNull())   // -7
println("3.5".toIntOrNull())  // null, not a whole number
println(" 42".toIntOrNull())  // null, spaces are not allowed
println("abc".toIntOrNull())  // null
```
For decimal text use `toDoubleOrNull()`, which accepts `"3.5"` and returns a `Double?` in the same way.

---

An `Int` has a fixed size, so it has a smallest and a largest value: `Int.MIN_VALUE` is `-2147483648` and `Int.MAX_VALUE` is `2147483647`.
Going past the limit does **not** raise an error: the value silently **wraps around** to the other end of the range, a behaviour called overflow.
```kotlin
println(Int.MAX_VALUE)     // 2147483647
println(Int.MAX_VALUE + 1) // -2147483648
```
When a result may exceed two billion, use a `Long`, whose limit `Long.MAX_VALUE` is about nine quintillion. Remember to convert before the operation: `Int.MAX_VALUE.toLong() + 1` is `2147483648`.

---

A `Double` stores decimals in binary, so some values can't be represented exactly and small errors appear in the last digits:
```kotlin
println(0.1 + 0.2) // 0.30000000000000004
```
To show a fixed number of decimals, use `String.format` with a format string: `"%.2f"` means "a decimal number with 2 digits after the point". The result is a `String`, rounded to that many digits:
```kotlin
println(String.format("%.2f", 0.1 + 0.2)) // 0.30
println(String.format("%.1f", 3.14159))   // 3.1
println(String.format("%.2f", 2.0))       // 2.00
```

---

`Any` is the type at the top of the hierarchy: every Kotlin value is an `Any`, so a variable of type `Any` can hold an `Int`, a `String`, a `Boolean`, or anything else.
To find out what it actually holds you use the `is` operator, which returns `true` when the value has that type:
```kotlin
val value: Any = 42
println(value is Int)    // true
println(value is String) // false
```
Once a check has passed, the compiler **smart casts** the value: inside the `if` (or the `when` branch) you can use it as that type, with no conversion needed:
```kotlin
if (value is Int) println(value + 1) // 43, value is an Int here
when (value) {
    is String -> println(value.length)
    is Boolean -> println(!value)
}
```
