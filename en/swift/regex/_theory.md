A **regular expression** (regex) is a small pattern that describes a shape of text: "a run of digits", "a word followed by an equals sign", "three capital letters". Instead of writing loops over characters, you describe the shape once and let Swift find it.

Swift writes a regex between `#/` and `/#`:
```swift
let digits = #/\d+/#
```
Inside the pattern, `\d` means "any digit" and `+` means "one or more of the previous thing", so `\d+` means "a run of one or more digits".

The simplest question you can ask is whether a text contains a match. `contains(_:)` takes a regex and returns a `Bool`:
```swift
print("order42".contains(#/\d+/#)) // true
print("order".contains(#/\d+/#))   // false
```
Always use the `#/ ... /#` form shown here: the shorter `/ ... /` spelling confuses the compiler when the pattern is written directly inside a method call.

---

A few shorthands cover most patterns. Each one matches exactly **one** character:
- `\d` is one digit
- `\w` is one letter, digit or underscore
- `\s` is one space, tab or newline
- `.` is any single character

To match more than one character, add a **quantifier** right after the pattern:
- `+` means one or more
- `*` means zero or more
- `?` means zero or one

So `\w+` is a word, `\s*` is optional spacing, and `\d?` is an optional digit:
```swift
print("hello world".contains(#/\w+\s\w+/#)) // true
print("hello".contains(#/\w+\s\w+/#))       // false
```
A character with no special meaning simply matches itself, so `#/cat/#` matches the three letters `cat`.

---

By default a pattern may match anywhere inside the text. **Anchors** tie it to a position instead:
- `^` means "the start of the text"
- `$` means "the end of the text"

```swift
print("swift".contains(#/^sw/#))  // true, the text starts with sw
print("myswift".contains(#/^sw/#)) // false, sw is not at the start
print("swift".contains(#/ft$/#))  // true, the text ends with ft
```
Anchors match a position, not a character, so they add nothing to what the match contains.

---

When none of the shorthands fit, list the characters you accept between square brackets. `[abc]` matches one `a`, one `b` or one `c`, and a dash writes a range:
```swift
print("f".contains(#/[a-f]/#))  // true
print("Z".contains(#/[A-Z]/#))  // true
print("5".contains(#/[0-9a-f]/#)) // true
```
A number in braces says exactly how many times the previous pattern repeats: `{3}` means three times, `{2,4}` means between two and four times:
```swift
print("aaa".contains(#/^a{3}$/#))  // true
print("aa".contains(#/^a{3}$/#))   // false
```
Wrapping a pattern in `^` and `$` with a count is the usual way to check that a whole text has a given shape.

---

`contains(_:)` only says yes or no. To get the matched text, use `firstMatch(of:)`. It returns an **optional match**: `nil` when nothing matched, so it pairs naturally with `if let`.

The matched text is stored in the property `0` of the match, written `m.0`:
```swift
let text = "order 42 today"
if let m = text.firstMatch(of: #/\d+/#) {
    print(m.0) // 42
}
```
`firstMatch(of:)` stops at the first match, even when the text holds more.

---

`m.0` is not a `String` but a `Substring`: a view into the original text, not a copy. It prints exactly like a string, but where a `String` is required you have to convert it:
```swift
let text = "order 42"
if let m = text.firstMatch(of: #/\d+/#) {
    let found: String = String(m.0)
    print(found) // 42
}
```
Number initialisers accept a `Substring` directly, so `Int(m.0)` works without the detour.

---

`matches(of:)` returns **every** match instead of the first one, as an array. The array is never `nil`: when nothing matches it is simply empty, so it can be looped over or transformed straight away:
```swift
let text = "a1 b22"
print(text.matches(of: #/\d+/#).count) // 2
```
Each element is a match, so `$0.0` inside a `map` is the matched text:
```swift
let found = text.matches(of: #/\d+/#).map { String($0.0) }
print(found) // ["1", "22"]
```

---

Because `Int(_:)` accepts a `Substring`, turning found text into numbers is one step. `compactMap` is handy here: it drops the values that come back `nil`:
```swift
let text = "a1 b22"
let numbers = text.matches(of: #/\d+/#).compactMap { Int($0.0) }
print(numbers) // [1, 22]
```
Use `map` when every element converts, `compactMap` when some may fail.

---

Round brackets around a part of the pattern create a **capture group**: the whole match is still `m.0`, and the part inside the brackets becomes `m.1`:
```swift
let text = "id-42"
if let m = text.firstMatch(of: #/id-(\d+)/#) {
    print(m.0) // id-42
    print(m.1) // 42
}
```
This is how you keep the interesting piece and throw the surrounding text away. Without brackets there is no `m.1` at all, and the code does not compile.

---

A pattern can hold several groups. They are numbered from left to right by their opening bracket, so the second one is `m.2`, the third `m.3`, and so on:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/([a-z]+)=(\d+)/#) {
    print(m.1, m.2) // size 10
}
```
`m.0` always stays the whole match, whatever the number of groups.

---

Counting brackets gets fragile as soon as a pattern grows. Give a group a **name** instead, by writing `?<name>` right after its opening bracket, and read it as a property of the match:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/(?<key>[a-z]+)=(?<value>\d+)/#) {
    print(m.key)   // size
    print(m.value) // 10
}
```
Named groups are still numbered, so `m.1` keeps working, but `m.key` says what it holds and survives a change in the pattern.

---

`replacing(_:with:)` swaps every match for a fixed text and returns a new `String`, leaving the original untouched:
```swift
let text = "a1 b22"
print(text.replacing(#/\d+/#, with: "#")) // a# b#
print(text)                               // a1 b22
```
Note that `\d+` replaces a whole run of digits with a single `#`, while `\d` would replace one digit at a time. The pattern decides how much disappears.

---

`split(separator:)` also accepts a regex, which lets one call handle separators that are not always written the same way:
```swift
let line = "a, b;c"
let parts = line.split(separator: #/[,;]\s*/#)
print(parts.joined(separator: "|")) // a|b|c
```
The pattern `[,;]\s*` means "a comma or a semicolon, followed by any amount of spacing", so every separator is consumed whole and no empty field is produced. The result is an array of `Substring`.

---

Validating a whole text with `^` and `$` works, but `wholeMatch(of:)` says it directly: it returns a match only when the pattern covers the text from the first character to the last, and `nil` otherwise:
```swift
print("1a2b".wholeMatch(of: #/[0-9a-f]+/#) != nil) // true
print("1z".wholeMatch(of: #/[0-9a-f]+/#) != nil)   // false
```
Use `firstMatch(of:)` to find something inside a text, and `wholeMatch(of:)` to check that a text has one exact shape.

---

A `#/ ... /#` literal is fixed when you compile. When the pattern only becomes known at run time, for example because a user typed it, build it with `Regex(_:)`:
```swift
let regex = try Regex("[0-9]+")
print("abc123".contains(regex)) // true
```
This initialiser **throws**: an invalid pattern such as `"["` is only discovered while the program runs, so the call needs `try`, and the error must either be handled with `do`/`catch` (or `try?`) or propagated by marking the surrounding function `throws`, as this exercise does. A regex built this way has no numbered properties known at compile time, but `contains`, `matches(of:)` and `replacing` work exactly as before.
