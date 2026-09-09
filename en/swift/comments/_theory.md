A **comment** is a note written inside the source code for the people who read it. The compiler ignores comments completely, so they never change what the program does.

The simplest comment is the **single-line comment**: it starts with `//` and runs until the end of the line.
```swift
// Greets the user
print("Hello")
```
Use comments to explain what a piece of code is for, or why it was written that way.

---

A comment does not need its own line: it can follow the code on the same line. This is a **trailing comment**, and it is a good place for a short note about that specific statement:
```swift
let retries = 3 // give up after three attempts
```
Everything from `//` to the end of the line is ignored, while the code before it runs as usual.

---

Because the compiler removes comments completely, adding or deleting a comment never changes what a program does. Only the code that is **not** commented runs.

This makes `//` a quick way to switch a line of code off without deleting it. This is called **commenting out**:
```swift
var total = 10
// total = total + 5
print(total) // prints 10
```
The second line is now a comment, so `total` stays `10`. Removing the `//` brings the line back to life.

Commenting out is handy while you experiment, but remember to clean up: code that stays commented out for a long time only confuses whoever reads it next.

---

When a comment needs more than one line, Swift offers the **multi-line comment** (also called a block comment): it starts with `/*` and ends with `*/`, and everything in between is ignored, including line breaks.
```swift
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
print("Welcome!")
```
A block comment can also be short and stay on one line: `/* like this */`.

---

Unlike `//`, which stops at the end of the line, a `/*` comment only stops at the `*/`. If you forget to close it, the compiler treats all the following code as part of the comment and reports an error:
```swift
let width = 10 /* in centimetres
print(width) // still inside the comment: error, the comment is never closed
```
Both `//` and `/* */` work as trailing comments, but with `/*` always make sure the `*/` is there.

---

In many languages block comments cannot contain other block comments, but in Swift they **can be nested**: every `/*` must be matched by its own `*/`, and the comment ends only when the outermost one is closed.
```swift
/* outer /* inner */ still a comment */
print("done")
```
Here `still a comment */` is part of the outer comment, so only `done` is printed. This is what lets you comment out a whole block of code even when that block already contains a `/* */` comment.

---

To comment out several lines at once, wrap them in a single block comment instead of adding `//` to every line:
```swift
var total = 100
/*
total = total - 30
total = total - 20
*/
print(total) // prints 100
```
Thanks to nesting, this works even when one of those lines already contains a `/* */` comment.

---

A common use of block comments is the **header comment**: a short block placed directly above a function that says what it does and what its parameters mean.
```swift
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
Whoever calls `toSeconds` can now read the header instead of the body. Keep the header next to the function so they are updated together.

---

Swift has a third kind of comment, the **documentation comment**: a single-line comment that starts with `///` (three slashes) placed directly above a function, a type or a property.
```swift
/// Returns the greeting for `name`.
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
To the compiler it is just a comment, but tools like Xcode read it and show it as the help text for `greet`. Documentation comments support **Markdown**, so you can use backticks for code, `**bold**` and lists.

---

The first line of a documentation comment is the **summary**: a short sentence that says what the function does. Write it in the third person, as if describing the function: "Returns...", "Adds...", "Checks...".
```swift
/// Returns `true` when `n` is divisible by two.
func isEven(_ n: Int) -> Bool {
    return n % 2 == 0
}
```
The comment must sit right above the declaration, with no blank line in between, otherwise Xcode does not attach it to the function.

---

Documentation comments also come in a block form: `/**` opens it and `*/` closes it, exactly like a multi-line comment but with a second asterisk at the start.
```swift
/**
 Returns the greeting for `name`.

 The result always ends with an exclamation mark.
 */
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
`/// text` and `/** text */` mean the same thing to the tools; `///` is the most common choice in Swift code, while `/** */` is handy for long descriptions. A plain `/* */` or `//` comment is **not** documentation, even when placed above a function.

---

After the summary, a documentation comment can describe the parameters and the return value with special Markdown list items that Xcode recognises:
```swift
/// Returns the number of seconds in the given minutes.
/// - Parameter minutes: a whole number of minutes, never negative
/// - Returns: `minutes` multiplied by sixty
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
The order is always the same: summary first, then `- Parameter name:` for each parameter, then `- Returns:`.

---

Some comments follow a convention that editors understand. In Swift the most common **markers** are:
- `// MARK: - Title` labels a section of the file, so it shows up in Xcode's navigation menu
- `// TODO: ...` flags something that still needs to be written
- `// FIXME: ...` flags code that is known to be wrong and must be corrected

```swift
// MARK: - Setup
let limit = 10
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
To the compiler they are ordinary comments; Xcode lists them so pending work is easy to find. Once the work is done, delete the marker: a stale `TODO` is misleading.

---

A `TODO` usually sits next to a placeholder that keeps the code compiling until the real implementation is written. When you complete the work, replace the placeholder and remove the marker in the same change, so the comment never lies about the state of the code.

---

A `FIXME` is different from a `TODO`: the code already exists, but it is known to be wrong. A good `FIXME` says what the bug is and, when possible, gives an example that shows it, so the next person can fix it quickly. As with `TODO`, delete the marker once the bug is fixed, but keep the documentation comment, which is still true.

---

A good comment explains **why** the code does something, not **what** it does. The code already shows what happens; repeating it in words adds noise and goes stale as soon as the code changes:
```swift
// set timeout to 30
let timeout = 30
```
The reason behind the number is what a reader cannot guess:
```swift
// the server drops idle connections after 35 seconds, so stop earlier
let timeout = 30
```
If a comment only restates the line below it, delete it or replace it with the reason.
