A **struct** (short for *structure*) is a type you design yourself to keep related values together. Instead of juggling a separate `title` and a separate `pages`, you describe a `Book` once and use it everywhere.

You declare one with the `struct` keyword, and the variables written inside it are its **stored properties**:
```swift
struct Book {
    var title: String
    var pages: Int
}
```
`Book` is now a type, exactly like `Int` or `String`. You reach a property of an instance with a dot:
```swift
let book = Book(title: "Swift", pages: 120)
print(book.title) // Swift
```

---

You never wrote the code that builds a `Book`, yet `Book(title: "Swift", pages: 120)` worked. Swift writes it for you: every struct gets a free **memberwise initializer**, an initializer whose parameters are its stored properties, in the order they are declared, each one using the property name as its argument label:
```swift
struct Point {
    var x: Int
    var y: Int
}

let p = Point(x: 3, y: 4)
print(p.x) // 3
```
Classes do not get this for free, which is one reason structs are the quickest way to model a value.

---

A stored property can be given a **default value** right where it is declared. Swift infers its type from that value, so you can drop the type annotation:
```swift
struct Counter {
    var label: String
    var value = 0
}
```
The memberwise initializer turns every defaulted property into an optional argument: pass it to override the default, leave it out to keep it.
```swift
let a = Counter(label: "clicks")
print(a.value) // 0

let b = Counter(label: "clicks", value: 7)
print(b.value) // 7
```

---

A struct can also hold **methods**: functions written inside the braces that work on the instance they are called on. Inside a method you use the property names directly, without any prefix:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    func area() -> Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area()) // 12
```
If a parameter of the method shadows a property name, write `self.width` to mean the property of the instance.

---

A **computed property** looks like a property but behaves like a method: it stores nothing, it calculates its value every time you read it. You write the type, then a block of code that returns the value:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    var area: Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area) // 12, no parentheses
```
Computed properties are not part of the memberwise initializer, since there is nothing to store. Use one when the value is derived from the others, and a method when the work needs parameters.

---

A struct is a **value type**: assigning it to another variable, or passing it to a function, hands over a *copy*. Changing the copy leaves the original untouched.
```swift
struct Point {
    var x: Int
}

var a = Point(x: 1)
var b = a
b.x = 99
print(a.x) // 1
```
A class is a **reference type**: `b = a` would make both names point at the same instance, so `b.x = 99` would also change `a.x` to `99`.

That is the real difference between the two, and the reason Swift models most data as structs: a value you hold cannot be modified behind your back by code that received it.

---

Because a struct is a value, a method is not allowed to change its properties unless you say so with the `mutating` keyword:
```swift
struct Counter {
    var value = 0

    mutating func increase(by amount: Int) {
        value += amount
    }
}

var c = Counter()
c.increase(by: 5)
print(c.value) // 5
```
A mutating method can only be called on an instance stored in a `var`. On a `let` instance the value is frozen, so `c.increase(by: 5)` would not compile.

---

When the memberwise initializer is not the way you want your type to be built, write your own **initializer**. It is declared with `init`, takes the parameters you choose, and must give every stored property a value before it ends. Inside it, `self` is the instance being created:
```swift
struct Square {
    var side: Int

    init(_ side: Int) {
        self.side = side
    }
}

let s = Square(5)
print(s.side) // 5
```
Writing an `init` inside the braces of the struct replaces the memberwise one, so from now on `Square(side: 5)` no longer exists.

---

Some values belong to the type itself rather than to any single instance: a currency code, a shared default, a factory that builds a common case. Mark them `static` and read them through the type name:
```swift
struct Money {
    static let currency = "EUR"
    var amount: Int

    static func zero() -> Money {
        return Money(amount: 0)
    }
}

print(Money.currency)     // EUR
print(Money.zero().amount) // 0
```
Here `currency` is declared with `let` because it never changes, so it is a constant shared by the whole program. `Money.currency` works without creating a single `Money`, while `amount` needs an instance.

---

Two structs cannot be compared with `==` until the type says it supports it. You do that by conforming to the `Equatable` **protocol**, written after a colon in the declaration:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

let a = Point(x: 1, y: 2)
let b = Point(x: 1, y: 2)
print(a == b) // true
```
You do not have to write `==` yourself: when every stored property is already `Equatable`, Swift synthesises it for you, comparing the properties one by one. Two instances are equal when all their properties are equal, which is exactly what you expect from a value.

---

A struct is a type like any other, so it can be stored in an array, a dictionary or a set, and every tool you already know keeps working on it:
```swift
struct Item {
    var name: String
    var price: Int
}

let items = [Item(name: "Tea", price: 3), Item(name: "Cake", price: 7)]

for item in items {
    print(item.name)
}

let names = items.map { $0.name }
let total = items.reduce(0) { $0 + $1.price }
print(total) // 10
```
Remember that the array holds *copies*: reading `items[0]` into a variable and changing it does not touch the array.
