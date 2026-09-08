Every value in Swift has a **type**, which tells the compiler what kind of data it is and what you can do with it.
The basic types are:
- `Int`: a whole number, like `42` or `-7`
- `Double`: a number with a decimal part, like `3.14`
- `String`: a piece of text, like `"Hello"`
- `Character`: a single character, like `"a"`
- `Bool`: either `true` or `false`

You can state the type of a constant or variable with a **type annotation**: a colon and the type name after the name:
```swift
let age: Int = 36
let name: String = "Ada"
```
A value of one type can't be stored in a constant of another type: `let age: Int = "36"` is a compile error.

---

Most of the time you don't write the type annotation: Swift **infers** the type from the value you assign, following a few literal rules:
- a number without a decimal point, like `42`, is an `Int`
- a number with a decimal point, like `3.14`, is a `Double`
- text between double quotes is a `String`
- `true` and `false` are `Bool`
```swift
let count = 42     // Int
let price = 9.99   // Double
let name = "Ada"   // String
let isOpen = true  // Bool
```
Swift also has `Float`, a decimal number that uses half the memory of a `Double` but is less precise, so a decimal literal is never inferred as `Float`: you must ask for it with an annotation.
In the same way `"a"` is inferred as a `String`, so a `Character` always needs an annotation.

---

The `type(of:)` function returns the type of a value, which is handy to check what Swift inferred:
```swift
print(type(of: 42))    // Int
print(type(of: 2.5))   // Double
print(type(of: "hi"))  // String
```
When you want a type different from the inferred one, add an annotation. A whole-number literal can be stored in a `Double` or `Float` constant, and a one-character literal in a `Character` constant:
```swift
let ratio: Double = 3       // 3.0, not an Int
let half: Float = 0.5
let initial: Character = "S"
print(type(of: ratio))      // Double
```

---

Swift never converts between number types on its own: adding an `Int` to a `Double` is a compile error, even though both are numbers.
```swift
let apples = 3
let price = 1.5
let total = apples * price // error: Int and Double can't be mixed
```
To combine them you create a new value of the type you need, by passing the value to the type's initializer:
```swift
let total = Double(apples) * price // 4.5
```
The same works the other way round: `Int(4.5)` produces an `Int`, keeping only the whole part of the number.

---

`Int(x)` doesn't round: it **truncates**, simply dropping the decimal part, so `Int(3.99)` is `3` and `Int(-3.99)` is `-3`.
To round to the nearest whole number, call `rounded()` on the `Double` first and then convert:
```swift
let x = 3.99
print(Int(x))            // 3
print(Int(x.rounded()))  // 4
```
Halfway values like `2.5` are rounded away from zero: `2.5` becomes `3.0` and `-2.5` becomes `-3.0`.

---

The type of the operands decides how division works. When both are `Int`, the `/` operator performs **integer division**: the result is an `Int` and the remainder is thrown away.
When at least one operand is a `Double`, `/` performs floating-point division and keeps the decimal part:
```swift
print(7 / 2)              // 3
print(7.0 / 2)            // 3.5
let slices = 7
print(Double(slices) / 2) // 3.5
```
So to get a decimal result from two `Int` values you must convert at least one of them to `Double` **before** dividing: `Double(7 / 2)` is `3.0`, because the integer division has already happened.

---

When a function must return a decimal result computed from whole numbers, convert the operands to `Double` before dividing and declare the return type as `Double`:
```swift
func ratio(_ part: Int, _ total: Int) -> Double {
    return Double(part) / Double(total)
}
print(ratio(1, 4)) // 0.25
```
Remember that `count` of an array is an `Int` too, so it needs the same conversion.

---

Numbers and strings convert with the same initializer syntax. `String(42)` turns a number into the text `"42"`, exactly like interpolating it with `"\(42)"`.
The opposite direction can fail, because not every text is a number, so `Int("42")` returns an **optional** `Int?`: it holds `42` here, but `Int("hello")` is `nil`.
As you learned in the nullability lessons, you can provide a fallback with `??` or unwrap it with `if let`:
```swift
let typed = "42"
let number = Int(typed) ?? 0
print(number + 1) // 43
```

---

`Int(text)` succeeds only when the whole text is a valid whole number, with an optional sign:
```swift
print(Int("42"))   // Optional(42)
print(Int("-7"))   // Optional(-7)
print(Int("3.5"))  // nil, not a whole number
print(Int(" 42"))  // nil, spaces are not allowed
print(Int("abc"))  // nil
```
For decimal text use `Double(text)`, which returns a `Double?` in the same way: `Double("3.5")` is `Optional(3.5)`.

---

A **type alias** gives an existing type a new name, with the `typealias` keyword:
```swift
typealias Score = Int
let best: Score = 100
print(best + 1) // 101
```
`Score` and `Int` are the same type, so they mix freely. An alias doesn't add any safety: it only makes the code read better when a plain type has a specific meaning in your program.

---

An `Int` uses 64 bits, so it can only represent numbers in a fixed range. The largest and smallest values are available as `Int.max` and `Int.min`:
```swift
print(Int.max) // 9223372036854775807
print(Int.min) // -9223372036854775808
```
Going past those limits is called **overflow**. Unlike many other languages, Swift doesn't silently wrap around to the other end of the range: an overflowing operation is a **runtime error** that stops the program.

---

`Int.max` and `Int.min` are useful as starting values when you search for an extreme: any real number is smaller than `Int.max`, so it is a safe initial value for "the smallest seen so far":
```swift
var smallest = Int.max
for number in [8, 3, 5] {
    if number < smallest {
        smallest = number
    }
}
print(smallest) // 3
```

---

As you saw in the strings lessons, iterating over a `String` gives you one `Character` at a time. A `Character` is not a `String`, so to use it as text you convert it with `String(c)`.
When the character is a digit, the `wholeNumberValue` property gives you its numeric value as an `Int?`: it is `nil` for characters that aren't digits.
```swift
for c in "a1" {
    print(c.wholeNumberValue)
}
// nil
// Optional(1)
```

---

Because `Int(text)` and `Double(text)` return `nil` on failure, comparing the result with `nil` tells you whether a text is a number of that kind:
```swift
print(Int("42") != nil)     // true
print(Double("4.2") != nil) // true
print(Double("42") != nil)  // true, a whole number is also a valid Double
```
Note the last line: every text accepted by `Int` is accepted by `Double` too, so check for `Int` first when you want to tell them apart.

---

Sometimes you need to store values of different types together. The special type `Any` can hold a value of **any** type, so an array declared as `[Any]` can mix numbers, strings and booleans:
```swift
let items: [Any] = [1, "two", true]
```
Each element still remembers its real type, which `type(of:)` reveals. To work with the value as its real type you use a **conditional cast** with `as?`, which returns an optional: it holds the value when the type matches and `nil` otherwise:
```swift
for item in items {
    if let number = item as? Int {
        print(number + 1) // runs only for 1
    }
}
```
`Any` is a last resort: an array of a single concrete type is safer and easier to use, so prefer it whenever you can.

---

Conditional casts chain naturally with `else if` to handle several possible types, converting each one to the type you need for the result:
```swift
let item: Any = 2.5
if let number = item as? Int {
    print(Double(number))
} else if let number = item as? Double {
    print(number)
}
```
An `Int` stored in `Any` is still an `Int`: `as? Double` on it returns `nil`, because `as?` checks the type, it doesn't convert numbers.
