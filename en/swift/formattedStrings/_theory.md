A **formatted string** is a piece of text where some parts are filled in with values at run time: a price, a name, a score. Swift gives you two tools for this.

The first is **string interpolation**, which you already know: anything written inside `\( )` is evaluated and inserted into the text. It does not have to be a variable, it can be any expression:
```swift
let price = 4
print("Total: \(price * 3)") // Total: 12
print("Name: \("ada".uppercased())") // Name: ADA
```
Interpolation is the quickest way to build a string, but it prints numbers exactly as Swift stores them: `3.5` stays `3.5`, never `3.50`. For full control over digits, width and padding we will use `String(format:)`, introduced in the next exercise.

---

The second tool is `String(format:)`, which comes from the **Foundation** framework, so the file must start with `import Foundation`.

It takes a **format string** followed by the values to insert. Inside the format string, a **specifier** starting with `%` marks where each value goes and how it is written. The specifier for an integer is `%d`:
```swift
import Foundation

let count = 7
let text = String(format: "Item %d", count)
print(text) // Item 7
```
`String(format:)` returns a normal `String`, so you can print it, store it or return it from a function.

---

For decimal numbers (`Double`) the specifier is `%f`. On its own it always prints six digits after the point:
```swift
print(String(format: "%f", 3.5)) // 3.500000
```
To choose how many decimals you want, write a dot and a number between `%` and `f`. This is the **precision**, and the value is rounded to fit:
```swift
print(String(format: "%.2f", 3.5))     // 3.50
print(String(format: "%.1f", 3.14159)) // 3.1
print(String(format: "%.0f", 2.71))    // 3
```
`%.2f` is the usual choice for prices, because it always shows exactly two decimals.

---

A number between `%` and the letter sets the **minimum width** of the field. If the value is shorter, spaces are added on the left so it is **right-aligned**; if it is longer, nothing is cut:
```swift
print(String(format: "%5d|", 42))    //    42|
print(String(format: "%5d|", 12345)) // 12345|
```
Width and precision combine: `%8.2f` means "at least 8 characters wide, with 2 decimals":
```swift
print(String(format: "%8.2f|", 3.14159)) //     3.14|
```
Fixed widths are what line up the columns of a table.

---

By default the padding goes on the left. A minus sign right after `%` puts the padding on the right instead, so the value is **left-aligned**:
```swift
print(String(format: "%-5d|", 42)) // 42   |
print(String(format: "%5d|", 42))  //    42|
```
The minus sign is a **flag**: it changes how the field is filled without changing the width.

---

Another flag is `0`: instead of spaces, the field is filled with zeros on the left. This is how you get numbers like `007` or `00042`:
```swift
print(String(format: "%05d", 42))  // 00042
print(String(format: "%03d", 7))   // 007
print(String(format: "%03d", 1234)) // 1234
```
As with spaces, a value longer than the width is never cut.

---

A format string can hold as many specifiers as you like. The values follow in the same order, separated by commas, and each one must match the type of its specifier: `%d` for an `Int`, `%f` for a `Double`:
```swift
let count = 3
let weight = 4.5
print(String(format: "%d items, %.1f kg", count, weight)) // 3 items, 4.5 kg
```
Passing a `Double` to `%d` (or an `Int` to `%f`) compiles, but prints a meaningless number, so always check that specifiers and values line up.

---

Integers can also be written in other bases. `%x` prints the value in **hexadecimal** with lowercase letters, `%X` with uppercase letters, and `%o` in octal:
```swift
print(String(format: "%x", 255)) // ff
print(String(format: "%X", 255)) // FF
print(String(format: "%o", 8))   // 10
```
Width and the `0` flag work here too: `%02x` is the classic way to write one byte of a colour, as in `#ff8000`.

---

To insert a `String` into a format string, use the specifier `%@`:
```swift
let name = "Ada"
let age = 36
print(String(format: "%@ is %d years old", name, age)) // Ada is 36 years old
```
`%@` accepts a Swift `String` directly. Do not use `%s` with a Swift string: that specifier expects a C string and prints garbage or crashes.
