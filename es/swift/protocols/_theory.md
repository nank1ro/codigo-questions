Un **protocolo** describe qué debe tener un tipo, sin decir cómo. Es una lista de requisitos — propiedades y métodos — que cualquier tipo que lo adopte promete proporcionar.

Lo declaras con la palabra clave `protocol`. Un requisito de propiedad se escribe con su tipo seguido de un bloque que indica cómo se puede acceder: `{ get }` significa que el tipo debe dejarte al menos leerla.
```swift
protocol Named {
    var name: String { get }
}
```
Un tipo **conforma** al protocolo escribiendo su nombre después de dos puntos y proporcionando todo lo que el protocolo pide:
```swift
struct Cat: Named {
    var name: String
}

let cat = Cat(name: "Luna")
print(cat.name) // Luna
```
Un protocolo no contiene datos propios: es un contrato. Todo tipo que lo satisfaga puede tratarse de la misma manera por el resto de tu código.

---

A protocol can also require **methods**. You write the signature — name, parameters and return type — and stop there, with no body:
```swift
protocol Greeter {
    func greet() -> String
}
```
A conforming type must declare a method with exactly that signature, and it supplies the body:
```swift
struct Robot: Greeter {
    func greet() -> String {
        return "BEEP"
    }
}

print(Robot().greet()) // BEEP
```
If anything differs — the name, a parameter type, the return type — the type does not conform, and the compiler tells you which requirement is missing.

---

A property requirement always states how the property can be used. `{ get }` asks only that the value can be read; `{ get set }` asks that it can be read **and** assigned:
```swift
protocol Account {
    var owner: String { get }
    var balance: Int { get set }
}
```
A conforming type may always give more than the contract asks for: a `var` stored property satisfies `{ get }` perfectly well. It may never give less — a `let` constant, or a read-only computed property, cannot satisfy `{ get set }`.

---

Protocols are not limited to structs. A **class** conforms in exactly the same way, by listing the protocol after a colon:
```swift
protocol Openable {
    func open() -> String
}

class Door: Openable {
    func open() -> String {
        return "creak"
    }
}
```
If the class also inherits from another class, the superclass comes first in the list and the protocols follow it. A type may adopt several protocols at once, separated by commas.

---

An **enum** can conform too. It has no stored properties, so a property requirement is usually met with a computed property that switches over the cases:
```swift
protocol Priced {
    var price: Int { get }
}

enum Ticket: Priced {
    case child, adult

    var price: Int {
        switch self {
        case .child: return 5
        case .adult: return 12
        }
    }
}

print(Ticket.adult.price) // 12
```
Structs, classes and enums: all three adopt protocols the same way, and code written against the protocol works with all of them.

---

A protocol usually collects more than one requirement, and a conforming type must satisfy every one of them:
```swift
protocol Vehicle {
    var wheels: Int { get }
    func move() -> String
}

struct Bike: Vehicle {
    var wheels = 2

    func move() -> String {
        return "pedalling"
    }
}
```
The order of the requirements inside the braces does not matter, and neither does the order in which the conforming type provides them: the compiler only checks that nothing is missing.

---

A struct is a value type, so a method that changes one of its stored properties must be marked `mutating`. When that method is a protocol requirement, the protocol has to say so as well:
```swift
protocol Togglable {
    mutating func toggle()
}

struct Light: Togglable {
    var isOn = false

    mutating func toggle() {
        isOn = !isOn
    }
}

var lamp = Light()
lamp.toggle()
print(lamp.isOn) // true
```
Without `mutating` in the protocol, a struct could never satisfy the requirement. Classes are reference types and never need the keyword: a class meets a `mutating` requirement with a plain method. Calling a mutating method needs a `var` — on a `let` it is a compile error.

---

Conformance does not have to be declared next to the type. An **extension** can add it later, which keeps the type's own declaration focused on its data:
```swift
protocol Resettable {
    mutating func reset()
}

struct Timer {
    var seconds = 0
}

extension Timer: Resettable {
    mutating func reset() {
        seconds = 0
    }
}
```
This also works for types you did not write: you can make a standard library type conform to one of your protocols without touching its source.

---

An extension of a **protocol** is a different tool: it adds members to every type that conforms, present and future. That is how you give a requirement a **default implementation**:
```swift
protocol Greeter {
    var name: String { get }
    func greet() -> String
}

extension Greeter {
    func greet() -> String {
        return "Hi, \(name)"
    }
}

struct Person: Greeter {
    var name: String
}

print(Person(name: "Ada").greet()) // Hi, Ada
```
`Person` never writes `greet()` and still conforms. Inside the protocol extension you can use every requirement of the protocol — here `name` — because any conforming type is guaranteed to have it.

---

A protocol extension can also add members the protocol never listed as requirements. They are extra conveniences, available on every conforming type:
```swift
protocol Sized {
    var count: Int { get }
}

extension Sized {
    var isEmpty: Bool {
        return count == 0
    }
}
```
`isEmpty` is not a requirement, so a conforming type does not have to provide it — it simply gets it.

---

A protocol can build on another one. Writing a protocol name after the colon makes the new protocol **inherit** every requirement of the old one:
```swift
protocol Named {
    var name: String { get }
}

protocol Aged: Named {
    var age: Int { get }
}
```
A type conforming to `Aged` must provide `age` *and* `name`, and it counts as a `Named` type everywhere. A protocol can inherit from several protocols at once, separated by commas.

---

A default implementation is a fallback, not a rule. If a conforming type provides its own version of a requirement, its version is the one that runs:
```swift
protocol Priced {
    var price: Int { get }
}

extension Priced {
    var price: Int { return 0 }
}

struct Ticket: Priced {
    var price = 12
}

print(Ticket().price) // 12, no 0
```
The default only fills the gaps the type leaves open.

---

The standard library is built out of protocols, and your own types can adopt them.

`Equatable` gives a type the `==` operator. For a struct whose stored properties are all `Equatable`, declaring the conformance is enough — Swift writes `==` for you:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

print(Point(x: 1, y: 2) == Point(x: 1, y: 2)) // true
```
`Comparable` inherits from `Equatable` and adds ordering. You implement a single operator, `<`, written as a `static func` taking the two values, and you get `>`, `<=`, `>=`, plus `sorted()`, `min()` and `max()` on collections for free:
```swift
struct Version: Comparable {
    var number: Int

    static func < (lhs: Version, rhs: Version) -> Bool {
        return lhs.number < rhs.number
    }
}
```

---

`CustomStringConvertible` decides what `print` shows for your type. Its single requirement is a `description` property:
```swift
struct Coin: CustomStringConvertible {
    var value: Int

    var description: String {
        return "\(value)c"
    }
}

print(Coin(value: 25)) // 25c
```
Without the conformance, printing a struct falls back to a default dump like `Coin(value: 25)`, and a `description` property alone changes nothing — `print` looks for the protocol. String interpolation uses `description` too.

---

A protocol name on its own is not a type, it is a constraint, so Swift asks you to say which of two things you mean.

`some Shape` means *one specific conforming type*, fixed at compile time. The caller never learns which one, but it is always the same:
```swift
func unitSquare() -> some Shape {
    return Square(side: 1)
}
```
`any Shape` means *a box that can hold any conforming type*, and two values of that type may hold different types. You need it whenever the concrete type can vary, such as inside a mixed array:
```swift
let shapes: [any Shape] = [Square(side: 2), Rect(width: 2, height: 3)]
```
Both let you call the protocol's requirements. Prefer `some` when a single type is enough, because it costs nothing at run time; reach for `any` when you genuinely need to mix types.
