A **comment** is a note written inside the source code for the people who read it. The compiler ignores comments completely, so they never change what the program does.

The simplest comment is the **single-line comment**: it starts with `//` and runs until the end of the line.
```kotlin
// Greets the user
println("Hello")
```
Use comments to explain what a piece of code is for, or why it was written that way.

---

A comment does not need its own line: it can follow the code on the same line. This is a **trailing comment**, and it is a good place for a short note about that specific statement:
```kotlin
val retries = 3 // give up after three attempts
```
Everything from `//` to the end of the line is ignored, while the code before it runs as usual.

---

Because the compiler removes comments completely, adding or deleting a comment never changes what a program does. Only the code that is **not** commented runs.

This makes `//` a quick way to switch a line of code off without deleting it. This is called **commenting out**:
```kotlin
var total = 10
// total = total + 5
println(total) // prints 10
```
The second line is now a comment, so `total` stays `10`. Removing the `//` brings the line back to life.

Commenting out is handy while you experiment, but remember to clean up: code that stays commented out for a long time only confuses whoever reads it next.

---

When a comment needs more than one line, Kotlin offers the **multi-line comment** (also called a block comment): it starts with `/*` and ends with `*/`, and everything in between is ignored, including line breaks.
```kotlin
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
println("Welcome!")
```
A block comment can also be short and stay on one line: `/* like this */`.

---

Unlike `//`, which stops at the end of the line, a `/*` comment only stops at the `*/`. If you forget to close it, the compiler treats all the following code as part of the comment and reports an error:
```kotlin
val width = 10 /* in centimetres
println(width) // still inside the comment: error, the comment is never closed
```
Both `//` and `/* */` work as trailing comments, but with `/*` always make sure the `*/` is there.

---

In Java a block comment cannot contain another block comment, but in Kotlin they **can be nested**: every `/*` must be matched by its own `*/`, and the comment ends only when the outermost one is closed.
```kotlin
/* outer /* inner */ still a comment */
println("done")
```
Here `still a comment */` is part of the outer comment, so only `done` is printed. This is what lets you comment out a whole block of code even when that block already contains a `/* */` comment.

---

To comment out several lines at once, wrap them in a single block comment instead of adding `//` to every line:
```kotlin
var total = 100
/*
total = total - 30
total = total - 20
*/
println(total) // prints 100
```
Thanks to nesting, this works even when one of those lines already contains a `/* */` comment.

---

A common use of block comments is the **header comment**: a short block placed directly above a function that says what it does and what its parameters mean.
```kotlin
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
Whoever calls `toSeconds` can now read the header instead of the body. Keep the header next to the function so they are updated together.

---

Kotlin has a third kind of comment, the **documentation comment**, written in a format called **KDoc**: it starts with `/**` (a slash and two asterisks) and ends with `*/`, and it is placed directly above a function, a class or a property.
```kotlin
/**
 * Returns the greeting for [name].
 */
fun greet(name: String): String {
    return "Hi, $name!"
}
```
To the compiler it is just a comment, but tools like IntelliJ IDEA read it and show it as the help text for `greet`. The `*` at the start of the inner lines is only a convention that keeps the block aligned. Inside KDoc you can use Markdown, and square brackets like `[name]` turn into links to that parameter.

---

The first line of a documentation comment is the **summary**: a short sentence that says what the function does. Write it in the third person, as if describing the function: "Returns...", "Adds...", "Checks...".
```kotlin
/**
 * Returns `true` when [n] is divisible by two.
 */
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
```
The comment must sit right above the declaration, with no other statement in between, otherwise the tools do not attach it to the function.

---

After the summary, a documentation comment can describe the parameters and the returned value with **KDoc tags**, which always start with `@`:
```kotlin
/**
 * Returns the number of seconds in the given minutes.
 * @param minutes a whole number of minutes, never negative
 * @return [minutes] multiplied by sixty
 */
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
`@param` is followed by the name of the parameter and then its description; there is one `@param` per parameter. `@return` describes the value the function gives back. The order is always the same: summary first, then the `@param` tags, then `@return`.

---

A function with more than one parameter gets one `@param` tag for each of them, written in the same order as the parameters:
```kotlin
/**
 * Returns the area of a rectangle.
 * @param width the horizontal side, in centimetres
 * @param height the vertical side, in centimetres
 * @return the product of [width] and [height]
 */
fun area(width: Int, height: Int): Int {
    return width * height
}
```
A tag is still only a comment: if you rename a parameter and forget the tag, nothing breaks, but the documentation starts lying. Update the KDoc together with the signature.

---

The compiler looks for comments only in the code, never inside a **string literal**. Between double quotes, `//` and `/* */` are ordinary characters:
```kotlin
println("50 // 2") // prints 50 // 2
```
The first `//` is part of the text, the second one starts a real comment. This surprises people most often with web addresses, which contain `//` right after the protocol.

---

Some comments follow a convention that editors understand. The most common **markers** are:
- `// TODO: ...` flags something that still needs to be written
- `// FIXME: ...` flags code that is known to be wrong and must be corrected

```kotlin
val limit = 10
// TODO: read the limit from the settings
```
To the compiler they are ordinary comments; IntelliJ IDEA collects them in a dedicated tool window so pending work is easy to find. A `TODO` usually sits next to a placeholder that keeps the code compiling until the real implementation is written. When you complete the work, replace the placeholder and remove the marker in the same change, so the comment never lies about the state of the code.

---

A `FIXME` is different from a `TODO`: the code already exists, but it is known to be wrong. A good `FIXME` says what the bug is and, when possible, gives an example that shows it, so the next person can fix it quickly. As with `TODO`, delete the marker once the bug is fixed, but keep the documentation comment, which is still true.

---

A good comment explains **why** the code does something, not **what** it does. The code already shows what happens; repeating it in words adds noise and goes stale as soon as the code changes:
```kotlin
// set timeout to 30
val timeout = 30
```
The reason behind the number is what a reader cannot guess:
```kotlin
// the server drops idle connections after 35 seconds, so stop earlier
val timeout = 30
```
If a comment only restates the line below it, delete it or replace it with the reason. The best comments are the ones that say something the code cannot.
