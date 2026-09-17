An **exception** is Kotlin's way of reporting that a statement cannot be carried out. Turning `"abc"` into a number, dividing an integer by zero or reading past the end of a list all throw one.

```kotlin
fun main() {
    println("before")
    val n = "abc".toInt()
    println("after")
}
```
This program prints `before` and then stops. `toInt()` cannot read `"abc"`, so it **throws** a `NumberFormatException`; nothing in the program deals with it, so Kotlin ends the program with an error report and `after` is never printed.

You can also throw an exception yourself with the `throw` keyword:
```kotlin
throw Exception("something went wrong")
```

An exception that nobody handles is not a warning: it is the end of the run.

---

To keep the program alive, put the risky statement inside a `try` block and describe the recovery in a `catch` block:
```kotlin
try {
    println("abc".toInt())
} catch (e: Exception) {
    println("cannot read that number")
}
println("still running")
```
Kotlin runs the `try` block; as soon as a statement inside it throws, the rest of the block is skipped and control jumps to the `catch` block. The name in brackets — `e` here — is the exception object, and `Exception` is the type being caught.

Once the `catch` block has finished, the program continues normally with the line after the whole `try`/`catch`.

---

Catching `Exception` catches everything, which is rarely what you want: a typing mistake elsewhere in the block would be swallowed too. Name the **exact type** you know how to recover from instead.

Each failure has its own type. `"abc".toInt()` throws a `NumberFormatException`, so that is the type to catch:
```kotlin
try {
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("that is not a number")
}
```
If a different kind of exception is thrown inside the block, this `catch` does not match and the exception keeps travelling out of the function.

---

One `try` can be followed by several `catch` blocks, each handling a different type:
```kotlin
val letters = listOf("a", "b")
val index = 5
val text = "abc"
try {
    println(letters[index] + text.toInt())
} catch (e: NumberFormatException) {
    println("not a number")
} catch (e: IndexOutOfBoundsException) {
    println("no such letter")
} catch (e: Exception) {
    println("something else went wrong")
}
```
Kotlin tries the blocks **from top to bottom** and runs the first one whose type matches. Only one block ever runs.

Order therefore matters. `NumberFormatException` and `IndexOutOfBoundsException` are both kinds of `Exception`, so a `catch (e: Exception)` written first would match every failure and the blocks below it would never run. Write the most specific type first and the most general one last.

---

A `finally` block can be added at the end. It runs **whatever happens**: after a successful `try`, after a `catch` has recovered, and even when the exception is not caught at all.

```kotlin
try {
    println("reading")
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("bad number")
} finally {
    println("closing")
}
```
```
reading
bad number
closing
```
That makes it the place for clean-up that must not be skipped, such as closing a file. A `try` needs at least a `catch` or a `finally`, but it may have both.

---

In Kotlin `try` is not only a statement: it is an **expression** that produces a value. The value is the last expression of whichever block ran — the `try` block when nothing failed, the `catch` block when it did.

```kotlin
val n = try { "abc".toInt() } catch (e: NumberFormatException) { 0 }
println(n) // 0
```
This is the idiomatic shape in Kotlin. Instead of declaring a `var`, assigning it in two places and hoping every path sets it, you get a single `val` that always holds a usable value.

Note that a `finally` block never changes the value: it runs for its side effects only.

---

Because `try` is an expression, it can be used anywhere a value is expected — including as the whole body of a function written with `=`:
```kotlin
fun length(text: String): Int = try {
    text.toInt()
} catch (e: NumberFormatException) {
    -1
}
```
Both blocks must produce a value of the same type, here `Int`. Write the fallback as the last expression of the `catch` block; there is no `return` inside either block.

---

Throwing and catching is not free, and for the common conversions Kotlin offers a cheaper variant that simply returns `null` instead of throwing: `toIntOrNull()`, `toDoubleOrNull()`, `toLongOrNull()`.

```kotlin
println("42".toIntOrNull())  // 42
println("abc".toIntOrNull()) // null
```
Combined with the elvis operator `?:`, which supplies a replacement when the value on its left is `null`, the whole `try`/`catch` collapses into one line:
```kotlin
val n = "abc".toIntOrNull() ?: 0
println(n) // 0
```
Reach for `try`/`catch` when the failure is genuinely exceptional; reach for `toIntOrNull()` when bad input is expected.

---

Your own functions can refuse bad input the same way the standard library does, with `throw`. The library already provides a type for the most common case: `IllegalArgumentException` means "the value you passed me is not acceptable".

```kotlin
fun half(n: Int): Int {
    if (n < 0) throw IllegalArgumentException("n must not be negative")
    return n / 2
}
```
`throw` ends the function immediately — the `return` below it is never reached. The caller decides what to do about it:
```kotlin
try { println(half(-4)) }
catch (e: IllegalArgumentException) { println("rejected") }
```
Throwing is better than quietly returning a made-up value: a wrong answer travels far, an exception stops at the first caller who is ready to handle it.

---

Every exception carries the text it was created with. Inside a `catch` block you read it through the `message` property of the exception object:
```kotlin
try {
    throw IllegalArgumentException("price must be positive")
} catch (e: IllegalArgumentException) {
    println(e.message) // price must be positive
}
```
`message` is nullable, because an exception may be built without any text; `e.message ?: "unknown"` gives a safe replacement when you need a plain `String`.

Prefer printing `e.message` over printing the exception object itself: the object's own text also includes the class name, which is noise for the person reading the output.

---

Writing `if (...) throw IllegalArgumentException(...)` on every argument gets noisy, so Kotlin provides two shorthands that read as plain sentences:

```kotlin
require(n >= 0) { "n must not be negative" }   // throws IllegalArgumentException
check(started) { "not started" }               // throws IllegalStateException
```
Both take a condition and a block producing the message, and both throw **when the condition is false**. The only difference is the exception type, and that difference is a message to the reader:

* `require` guards the **arguments** the caller passed, and fails with `IllegalArgumentException`.
* `check` guards the **state** of the object or program, and fails with `IllegalStateException`.

The block is only evaluated when the check fails, so building the message costs nothing on the happy path.

---

When none of the built-in types describes your failure well, declare your own. An exception is an ordinary class that extends `Exception` and hands its text to the parent:

```kotlin
class InsufficientFundsException(message: String) : Exception(message)
```
That single line is a complete exception type. It is thrown and caught like any other, and `e.message` returns the text it was built with:
```kotlin
try {
    throw InsufficientFundsException("balance too low")
} catch (e: InsufficientFundsException) {
    println(e.message) // balance too low
}
```
The gain is precision: a caller can catch `InsufficientFundsException` alone and let every other failure travel on.

---

`runCatching` runs a block and never lets an exception escape. Instead it hands back a `Result`, an object holding **either** the value the block produced **or** the exception it threw:

```kotlin
val ok = runCatching { "42".toInt() }
val bad = runCatching { "abc".toInt() }

println(ok.isSuccess)   // true
println(bad.isFailure)  // true
```
The value is read out afterwards, and you choose what a failure should become:
```kotlin
println(ok.getOrNull())      // 42
println(bad.getOrNull())     // null
println(bad.getOrElse { 0 }) // 0
```
`getOrNull()` turns a failure into `null`, while `getOrElse { ... }` runs the block to build a replacement. Nothing is thrown at the call site, so the failure can be carried around and dealt with later.

---

A `Result` can also be inspected without unwrapping it. `onFailure` runs its block only when the result holds an exception, `onSuccess` only when it holds a value, and **both give the same `Result` back** so the calls can be chained:

```kotlin
runCatching { "abc".toInt() }
    .onFailure { println("could not read it") }
    .onSuccess { println("read $it") }
```
Inside the block the exception (or the value) is available as `it`, so `it.message` is the text of the failure.

This is the "log and carry on" shape: report the problem where it happened, then continue, without an early `return` and without a `var` set from two places.

---

Where the `try` sits decides how much work a single bad value destroys. Wrap the **whole loop** and the first failure abandons the rest of the batch; wrap the **body** and only that one element is lost:

```kotlin
var total = 0
for (value in listOf("3", "x", "5")) {
    try {
        total += value.toInt()
    } catch (e: NumberFormatException) {
        // skip this one
    }
}
println(total) // 8
```
This pairs naturally with a validating function that throws: the function states one rule and refuses anything breaking it, and the loop decides that a refusal only costs one element.
