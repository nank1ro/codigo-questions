An **extension** adds new functionality to an existing type: a standard library type like `Int` or `String`, or a struct or class you wrote yourself.
You write the `extension` keyword followed by the name of the type, and put the new members between curly braces:
```swift
extension Int {
    func squared() -> Int {
        return self * self
    }
}
print(4.squared()) // 16
```
Inside the extension, `self` is the value the method is called on: in `4.squared()` it is `4`. Once the extension exists, every `Int` in the program has the new method, exactly as if it had been part of `Int` from the start.

---

Extensions work on any type, even the ones you don't have the source code for. `String` comes from the standard library, but you can still give it new methods:
```swift
extension String {
    func whisper() -> String {
        return self.lowercased() + "..."
    }
}
print("HELLO".whisper()) // hello...
```
Inside an extension you can drop `self.` when calling other members of the type: `lowercased()` alone means `self.lowercased()`.

---

An extension doesn't create a new type and doesn't copy the old one: it adds members to the type itself, so every existing and future value of that type gets them.
This is why extensions are so useful with types you can't edit, like the ones from the standard library or from a framework: you can't open the file where `Int` is defined, but you can extend it from any file of your program.
```swift
extension Int {
    func isDivisible(by other: Int) -> Bool {
        return self % other == 0
    }
}
let n = 12
print(n.isDivisible(by: 4)) // true
```

---

Besides methods, an extension can add **computed properties**: properties that don't store a value but calculate it every time they are read.
A computed property is declared with `var`, a type annotation and a body between curly braces that returns the value:
```swift
extension Int {
    var isNegative: Bool {
        return self < 0
    }
}
print((-3).isNegative) // true
print(7.isNegative)    // false
```
It is read like any property, without parentheses: `7.isNegative`, not `7.isNegative()`.

---

Computed properties in extensions are a natural fit for `String` too. The `reversed()` method returns the characters in reverse order, and `String(...)` turns them back into a string:
```swift
extension String {
    var backwards: String {
        return String(reversed())
    }
}
print("swift".backwards) // tfiws
```
As with methods, `reversed()` inside the extension means `self.reversed()`.

---

Extensions can add computed properties but **not stored properties**: this doesn't compile:
```swift
extension Int {
    var label = "number" // error: extensions must not contain stored properties
}
```
A stored property needs space inside every instance of the type. `Int` values already exist all over your program, and even in code compiled long before your extension, so their memory layout can't change. A computed property needs no space, because it is just code that runs when the property is read.

---

`Int`, `String`, arrays and structs are **value types**: a method can't change the value it is called on unless it is marked `mutating`. Extensions can add mutating methods too:
```swift
extension Int {
    mutating func increment() {
        self += 1
    }
}
var count = 1
count.increment()
print(count) // 2
```
Inside a mutating method you can assign to `self`. The value must be stored in a `var`: calling `increment()` on a `let` constant is a compile error.

---

A mutating method can take parameters like any other method, and can replace `self` entirely instead of updating it in place:
```swift
extension Int {
    mutating func reset(to value: Int) {
        self = value
    }
}
var score = 42
score.reset(to: 0)
print(score) // 0
```

---

An extension can add new **initializers** to a type. For a struct this is the best place to put them: an `init` written inside the struct body replaces the automatic memberwise initializer, while one added in an extension keeps it.
The new initializer usually delegates to an existing one with `self.init(...)`:
```swift
struct Size {
    var width: Double
    var height: Double
}
extension Size {
    init(square side: Double) {
        self.init(width: side, height: side)
    }
}
let a = Size(square: 3)          // from the extension
let b = Size(width: 2, height: 5) // memberwise, still available
```

---

Extensions are not only for other people's types. A common way to organise your own code is to keep the stored properties in the struct or class body and add the behaviour in one or more extensions, each grouping related members:
```swift
struct Circle {
    var radius: Double
}
extension Circle {
    var diameter: Double {
        return radius * 2
    }
    func grown(by amount: Double) -> Circle {
        return Circle(radius: radius + amount)
    }
}
```
Members added in an extension can use the stored properties directly, exactly as if they were written inside the type.

---

An extension can also make a type conform to a **protocol**, a list of requirements the type promises to implement. Write the protocol name after the type name, separated by a colon, and add the required members in the body.
`CustomStringConvertible` is a standard protocol with a single requirement, a computed property `description` of type `String`, that `print` uses to display the value:
```swift
struct Dog {
    var name: String
}
extension Dog: CustomStringConvertible {
    var description: String {
        return "Dog named \(name)"
    }
}
print(Dog(name: "Rex")) // Dog named Rex
```
Keeping each protocol conformance in its own extension is the usual way to organise a Swift type.

---

`Array` is a generic type: `[Int]` and `[String]` are both arrays, with a different **`Element`** type. An extension of `Array` applies to all of them, which is a problem when the new member only makes sense for some elements: you can't add numbers that are strings.
A `where` clause restricts the extension to the arrays whose `Element` is a given type:
```swift
extension Array where Element == Int {
    var largest: Int {
        var result = Int.min
        for number in self {
            if number > result {
                result = number
            }
        }
        return result
    }
}
print([3, 9, 2].largest) // 9
```
`[3, 9, 2].largest` works, while `["a", "b"].largest` is a compile error: the property doesn't exist on `[String]`.

---

Extensions can add **static** members: properties and methods that belong to the type itself rather than to a single value, marked with the `static` keyword and accessed through the type name.
A `static let` is allowed even though it stores a value, because there is only one copy for the whole type, not one per instance:
```swift
extension Int {
    static let answer = 42
    static func zeroes(_ count: Int) -> [Int] {
        return Array(repeating: 0, count: count)
    }
}
print(Int.answer)     // 42
print(Int.zeroes(3))  // [0, 0, 0]
```
A static member has no `self` value to work on: `Int.answer` is read on the type, not on a number.

---

Static methods in extensions are a good home for small factory functions that build a value of the type. `String(repeating:count:)` is the standard initializer that repeats a piece of text a number of times:
```swift
extension String {
    static func dashes(_ count: Int) -> String {
        return String(repeating: "-", count: count)
    }
}
print(String.dashes(4)) // ----
```

---

Extensions can only **add** members, never replace or override existing ones. `override` belongs to subclasses, which are a different type from their parent; an extension is the same type, so declaring a method that already exists is a redeclaration error:
```swift
struct Dog {
    func speak() -> String {
        return "Woof"
    }
}
extension Dog {
    func speak() -> String { // error: invalid redeclaration of 'speak()'
        return "Bark"
    }
}
```
If you need different behaviour, add a method with a new name, or write a subclass when the type is a class.
