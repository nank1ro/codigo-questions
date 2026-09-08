A **string** is a piece of text. In Swift you write a string literal between double quotes, and its type is `String`:
```swift
let greeting: String = "Hello"
var city = "Rome"
```
As with any other value, `let` creates a constant that can't be changed and `var` creates a variable that can.
Swift infers the `String` type from the literal, so the type annotation is optional.

---

**String interpolation** inserts the value of an expression inside a string literal. Wrap the expression in `\()`:
```swift
let name = "Ada"
let age = 36
print("\(name) is \(age) years old") // Ada is 36 years old
```
Any type can be interpolated: numbers, booleans and other strings are all converted to text automatically.

---

Two strings can be joined with the `+` operator, which produces a new string:
```swift
let full = "Hello" + " " + "world" // Hello world
```
To add text to the end of an existing string variable use `+=`. The variable must be declared with `var`, because its value changes:
```swift
var log = "Start"
log += "..."
print(log) // Start...
```

---

The `count` property returns the number of characters in a string, and `isEmpty` is `true` when the string has no characters at all:
```swift
print("Swift".count) // 5
print("".isEmpty)    // true
```
Every character is counted, including spaces and punctuation.

---

A `String` is a collection of `Character` values. A `Character` is a single letter, digit, symbol or space, and it is written with the same double quotes as a string, so you need a type annotation to get one:
```swift
let letter: Character = "a"
let text = "abc"
print(text.count) // 3
```
Checking `isEmpty` is preferred over comparing `count` with `0`: it reads better and doesn't need to count every character.

---

A **multi-line string literal** starts and ends with three double quotes `"""`, each on its own line. Every line between them becomes part of the string, and the line breaks are preserved:
```swift
let poem = """
Roses are red
Violets are blue
"""
print(poem)
```
This prints the two lines exactly as written. The closing `"""` also sets the indentation: any whitespace before it is removed from the start of every line.

---

Because a string is a collection of characters, you can iterate over it with a `for`-`in` loop. Each iteration gives you one `Character`:
```swift
for letter in "hey" {
    print(letter)
}
// h
// e
// y
```
A `Character` can be compared with `==` to a character literal, so counting how many times a character appears is just a loop and a counter.

---

Unlike arrays, strings can't be subscripted with an integer like `text[2]`: some characters take more memory than others, so Swift uses a dedicated `String.Index` type to point at a position.
`startIndex` is the position of the first character and `endIndex` is the position *after* the last one. To move from an index use `index(_:offsetBy:)`, then subscript the string with the result:
```swift
let word = "Swift"
let second = word.index(word.startIndex, offsetBy: 1)
print(word[second]) // w
```
Moving past the end of the string crashes at runtime, so the offset must stay within `count`.

---

Working with indices is verbose, so Swift offers shortcuts for the most common cases:
- `first` and `last` return the first and last character as an optional `Character?` (`nil` for an empty string)
- `prefix(n)` returns the first `n` characters and `suffix(n)` the last `n`
```swift
let word = "Swift"
print(word.first!)     // S
print(word.prefix(2))  // Sw
print(word.suffix(3))  // ift
```
`prefix` and `suffix` return a `Substring`, a view on the original text. To store it as a real `String` wrap it in `String(...)`. If `n` is larger than `count`, you simply get the whole string.

---

Three methods answer the most common questions about the content of a string, and each returns a `Bool`:
- `contains(_:)` is `true` when the string includes the given text (or character) anywhere
- `hasPrefix(_:)` is `true` when the string starts with the given text
- `hasSuffix(_:)` is `true` when the string ends with the given text
```swift
let email = "ada@example.com"
print(email.contains("@"))          // true
print(email.hasPrefix("ada"))       // true
print(email.hasSuffix(".org"))      // false
```
All three are case-sensitive: `"Swift".hasPrefix("s")` is `false`.

---

Since `contains`, `hasPrefix` and `hasSuffix` return booleans, they combine naturally with `||` and `&&` to build more complex checks.

---

`uppercased()` and `lowercased()` return a **new** string with every letter converted to upper or lower case. The original string is not modified:
```swift
let name = "Swift"
print(name.uppercased()) // SWIFT
print(name.lowercased()) // swift
print(name)              // Swift
```
Both are methods, so don't forget the parentheses.

---

Converting to lower case is the usual way to compare text ignoring case: two strings that differ only in capitalization become equal once both are lowercased.

---

`split(separator:)` breaks a string into an array of pieces wherever the separator character appears. `joined(separator:)` does the opposite: it glues the elements of an array into a single string, putting the separator between them:
```swift
let parts = "a-b-c".split(separator: "-") // ["a", "b", "c"]
print(parts.count)                         // 3
print(parts.joined(separator: ", "))       // a, b, c
```
Like `prefix`, `split` returns `Substring` values; wrap one in `String(...)` if you need to store it as a `String`.

---

Splitting on a space is the simplest way to break a sentence into words, and joining is how you rebuild text from an array.

---

The Foundation framework adds many extra string methods. One of the most useful is `replacingOccurrences(of:with:)`, which returns a new string where every occurrence of the first text is replaced by the second:
```swift
import Foundation

let path = "a/b/c"
print(path.replacingOccurrences(of: "/", with: "-")) // a-b-c
```
Remember to `import Foundation` at the top of the file, otherwise the method isn't available. Method calls can be chained, so `text.lowercased().replacingOccurrences(of: " ", with: "_")` is valid.

---

Strings can be compared with the same operators as numbers. `==` checks that two strings have exactly the same characters, while `<` and `>` compare them in dictionary order, character by character:
```swift
print("apple" == "apple")  // true
print("apple" < "banana")  // true
print("car" < "cat")       // true
```
The comparison is case-sensitive, and every uppercase letter comes **before** every lowercase letter, so `"B" < "a"` is `true`.

---

A `Character` is not a `String`, so it can't be joined to a string with `+` directly. Convert it first with `String(...)`:
```swift
let letter: Character = "a"
let text = String(letter) + "bc" // abc
```
Combining this with a `for`-`in` loop lets you rebuild a string one character at a time, for example putting each new character in front of the ones collected so far.
