Sometimes a value is simply missing: a user without a middle name, a search that finds nothing, a text that can't be turned into a number.
Swift represents a missing value with `nil`, but a normal variable can never hold it:
```swift
var age: Int = nil // error: 'nil' cannot initialize type 'Int'
```
To allow a missing value you declare an **optional** type by adding a question mark `?` after the type.
An `Int?` holds either an `Int` or `nil`:
```swift
var age: Int? = 30
age = nil // allowed
```
An optional variable that is declared without a value starts as `nil`.

---

You can compare an optional with `nil` using `==` and `!=`, and you can compare it directly with a plain value of the wrapped type:
```swift
var score: Int? = 10
print(score == nil) // false
print(score == 10)  // true
```
Remember that `Int?` and `Int` are two different types: an `Int?` may be empty, an `Int` never is.

---

An optional is like a box: before using the value inside you have to open it, which Swift calls **unwrapping**.
The quickest way is **forced unwrapping** with an exclamation mark `!`:
```swift
let score: Int? = 10
print(score! + 5) // 15
```
The `!` tells Swift "I'm sure there is a value here". If you are wrong and the optional is `nil`, the program stops immediately with a runtime crash:
```swift
let missing: Int? = nil
print(missing! + 5) // Fatal error: Unexpectedly found nil
```
That's why forced unwrapping is considered dangerous: use it only when you are certain the value exists.

---

Forced unwrapping is safe only when you have already checked that the optional is not `nil`:
```swift
if score != nil {
    print(score! * 2)
}
```

---

Checking for `nil` and then force unwrapping is verbose. Swift offers **optional binding** with `if let`, which unwraps the optional and stores the value in a new constant in a single step:
```swift
let score: Int? = 10
if let value = score {
    print("Score: \(value)") // value is an Int, not an Int?
} else {
    print("No score")
}
```
The body of the `if` runs only when the optional contains a value; inside it `value` is a plain `Int` and needs no `!`.

---

When a missing value means "stop here", `guard let` is clearer than `if let`.
It unwraps the optional and, if that fails, runs the `else` block, which must exit the current scope (with `return`, `break`, `continue` or `throw`):
```swift
func greet(_ name: String?) {
    guard let name = name else {
        print("Nobody here")
        return
    }
    print("Hello, \(name)!") // name is a String from here on
}
```
Unlike `if let`, the unwrapped constant stays available for the rest of the function, so the happy path is not nested inside an `if`.

---

A typical use of `guard let` is validating a function's input at the top and returning a fallback value when it is missing:
```swift
func length(of text: String?) -> Int {
    guard let text = text else { return 0 }
    return text.count
}
```

---

Very often all you want from an optional is its value or a default.
The **nil-coalescing operator** `??` does exactly that: it unwraps the optional if it has a value, otherwise it returns the value on its right:
```swift
let score: Int? = nil
let points = score ?? 0 // points is an Int equal to 0
```
The default must have the same type as the wrapped value.
You can chain several `??`: the first non-`nil` value wins.
```swift
let a: Int? = nil
let b: Int? = 7
print(a ?? b ?? 0) // 7
```

---

`??` is the shortest way to turn an optional into a plain value when a sensible default exists:
```swift
func volume(from setting: Int?) -> Int {
    return setting ?? 50
}
```

---

When chaining `??`, Swift evaluates from left to right and stops at the first value that is not `nil`; the last default is used only when every optional before it is `nil`.

---

Accessing a property or calling a method on an optional would require unwrapping it first.
**Optional chaining** with `?.` does it for you: if the optional is `nil` the whole expression becomes `nil`, otherwise the access goes through:
```swift
let name: String? = "swift"
let upper = name?.uppercased() // String? holding "SWIFT"
```
The result is always an optional, even when the property itself is not.
Chains can be as long as you need, and they combine nicely with `??`:
```swift
class User {
    var nickname: String? = "ace"
}
let user: User? = User()
print(user?.nickname?.count ?? 0) // 3
```

---

Optional chaining shines when data may be missing at several levels: an object can be `nil`, and one of its properties can be `nil` too.
A single `?.` chain handles both cases without any `if`.

---

A single `if let` or `guard let` can unwrap several optionals at once: separate the bindings with commas.
The body runs only if every optional has a value:
```swift
let first: String? = "Ada"
let last: String? = "Lovelace"
if let first = first, let last = last {
    print("\(first) \(last)")
}
```
You can also append a boolean condition after the bindings, like `if let n = number, n > 0`.

---

Binding several optionals in one `if let` keeps the code flat: one `else` branch covers every missing value.

---

Many operations can fail, and Swift reports the failure by returning an optional.
Converting text to a number is the classic example: `Int("42")` returns an `Int?` holding `42`, while `Int("abc")` returns `nil`.
`Int("3.5")` is `nil` as well, because the text is not a whole number; use `Double("3.5")` for decimals.
```swift
let typed = "42"
if let number = Int(typed) {
    print(number + 1) // 43
}
```
Other examples are `array.first` (`nil` for an empty array) and `dictionary[key]` (`nil` when the key is missing).

---

Because a conversion can fail, its result is always an optional and must be unwrapped before use, even when you are sure the text is a valid number.

---

Failable conversions pair naturally with `guard let`: convert, bail out when the result is `nil`, then work with the plain value.

---

Sometimes you want to transform the value inside an optional and keep the result optional, without unwrapping and re-wrapping by hand.
Optionals have a `map` method: it applies the closure to the value if there is one, and returns `nil` otherwise.
```swift
let score: Int? = 10
let doubled = score.map { $0 * 2 } // Int? holding 20
let missing: Int? = nil
let stillMissing = missing.map { $0 * 2 } // nil
```
Combined with a failable conversion it makes a compact pipeline: `Int(text).map { $0 + 1 }`.
