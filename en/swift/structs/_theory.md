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
