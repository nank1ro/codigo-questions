**Wyjątek** to sposób, w jaki Kotlin zgłasza, że instrukcja nie może zostać wykonana. Zamiana `"abc"` na liczbę, dzielenie liczby całkowitej przez zero i odczyt poza końcem listy — wszystkie te operacje go zgłaszają.

```kotlin
fun main() {
    println("before")
    val n = "abc".toInt()
    println("after")
}
```
Ten program wypisuje `before`, a następnie się zatrzymuje. `toInt()` nie potrafi odczytać `"abc"`, więc **zgłasza** `NumberFormatException`; nic w programie się nim nie zajmuje, więc Kotlin kończy program raportem błędu, a `after` nigdy nie jest wypisywany.

Wyjątek możesz też zgłosić samodzielnie za pomocą słowa kluczowego `throw`:
```kotlin
throw Exception("something went wrong")
```

Wyjątek, którego nikt nie obsłuży, to nie ostrzeżenie: to koniec działania programu.

---

Aby utrzymać program przy życiu, umieść ryzykowną instrukcję w bloku `try`, a sposób naprawy opisz w bloku `catch`:
```kotlin
try {
    println("abc".toInt())
} catch (e: Exception) {
    println("cannot read that number")
}
println("still running")
```
Kotlin wykonuje blok `try`; gdy tylko któraś instrukcja wewnątrz niego zgłosi wyjątek, reszta bloku jest pomijana, a sterowanie przechodzi do bloku `catch`. Nazwa w nawiasie — tutaj `e` — to obiekt wyjątku, a `Exception` to przechwytywany typ.

Gdy blok `catch` zakończy działanie, program normalnie kontynuuje od linii następującej po całej konstrukcji `try`/`catch`.

---

Przechwycenie `Exception` obejmuje wszystko, co rzadko jest tym, czego chcesz: literówka gdzie indziej w bloku również zostałaby po cichu pochłonięta. Zamiast tego podaj **dokładny typ**, od którego wiesz, jak się odbudować.

Każda awaria ma swój własny typ. `"abc".toInt()` zgłasza `NumberFormatException`, więc to właśnie ten typ należy przechwycić:
```kotlin
try {
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("that is not a number")
}
```
Jeśli wewnątrz bloku zostanie zgłoszony inny rodzaj wyjątku, ten `catch` nie pasuje i wyjątek wędruje dalej poza funkcję.

---

Po jednym `try` może następować kilka bloków `catch`, z których każdy obsługuje inny typ:
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
Kotlin sprawdza bloki **od góry do dołu** i wykonuje pierwszy, którego typ pasuje. Wykonywany jest zawsze tylko jeden blok.

Kolejność ma więc znaczenie. `NumberFormatException` i `IndexOutOfBoundsException` to oba rodzaje `Exception`, więc `catch (e: Exception)` zapisany jako pierwszy pasowałby do każdej awarii, a bloki poniżej nigdy by się nie wykonały. Najbardziej konkretny typ zapisz jako pierwszy, a najbardziej ogólny jako ostatni.

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

Ponieważ `Result` jest zwykłą wartością, można go przechować w `val` i odpytywać dowolną liczbę razy:

```kotlin
val result = runCatching { "abc".toInt() }

println(result.getOrElse { 0 })  // 0
println(result.getOrNull())      // null
println(result.isSuccess)        // false
```
`try`/`catch` nie potrafi tego zrobić. Tam wynik jest obsługiwany tylko raz, w miejscu awarii, a potem znika. `Result` zachowuje awarię, dzięki czemu kod, który na nią reaguje, nie musi znajdować się tam, gdzie się wydarzyła.

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
