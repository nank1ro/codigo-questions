**协议**描述一个类型必须具备什么，而不说明如何实现。它是一份要求清单——属性和方法——任何采用它的类型都承诺提供这些内容。

你使用 `protocol` 关键字来声明协议。属性要求的写法是在属性类型后面跟一个说明其访问方式的花括号块：`{ get }` 表示该类型必须至少允许你读取它。
```swift
protocol Named {
    var name: String { get }
}
```
一个类型通过在冒号后写下协议名称并提供协议要求的全部内容来**遵循**该协议：
```swift
struct Cat: Named {
    var name: String
}

let cat = Cat(name: "Luna")
print(cat.name) // Luna
```
协议本身不保存任何数据：它是一份契约。每个满足协议的类型都可以被代码的其余部分以相同的方式对待。

---

协议也可以要求**方法**。你只需写出签名——名称、参数和返回类型——然后就此停止，不写方法体：
```swift
protocol Greeter {
    func greet() -> String
}
```
遵循协议的类型必须声明一个签名完全一致的方法，并由它提供方法体：
```swift
struct Robot: Greeter {
    func greet() -> String {
        return "BEEP"
    }
}

print(Robot().greet()) // BEEP
```
只要任何地方不同——名称、参数类型或返回类型——该类型就不遵循协议，编译器会告诉你缺少哪一项要求。

---

属性要求总是会说明该属性可以如何被使用。`{ get }` 只要求值可以被读取；`{ get set }` 则要求它可以被读取**和**赋值：
```swift
protocol Account {
    var owner: String { get }
    var balance: Int { get set }
}
```
遵循协议的类型总是可以提供比契约要求更多的东西：一个 `var` 存储属性完全能满足 `{ get }`。但它绝不能提供得更少——`let` 常量或只读计算属性都无法满足 `{ get set }`。

---

协议并不局限于结构体。**类**以完全相同的方式遵循协议，即在冒号后列出协议：
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
如果类还继承自另一个类，则超类排在列表首位，协议紧随其后。一个类型可以同时采用多个协议，用逗号分隔。

---

**枚举**也可以遵循协议。它没有存储属性，因此属性要求通常由一个对各个 case 进行 switch 的计算属性来满足：
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
结构体、类和枚举：这三者都以相同的方式采用协议，针对协议编写的代码可以与它们中的任何一个配合使用。

---

协议通常包含不止一项要求，遵循协议的类型必须满足其中每一项：
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
花括号内各项要求的顺序并不重要，遵循协议的类型提供它们的顺序也不重要：编译器只检查是否有任何缺失。

---

结构体是值类型，因此修改其存储属性的方法必须标记为 `mutating`。当这个方法是一项协议要求时，协议也必须这样声明：
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
如果协议中没有 `mutating`，结构体就永远无法满足该要求。类是引用类型，从不需要这个关键字：类用一个普通方法就能满足 `mutating` 要求。调用 mutating 方法需要一个 `var`——在 `let` 上调用是编译错误。

---

遵循关系不必在类型旁边声明。**扩展**可以在之后添加它，这让类型自身的声明专注于它的数据：
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
这也适用于不是你编写的类型：你可以让标准库类型遵循你的某个协议，而无需改动它的源代码。

---

**协议**的扩展是另一种工具：它把成员添加到每一个遵循协议的类型上，无论是现在还是将来的。这就是你为一项要求提供**默认实现**的方式：
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
`Person` 从未编写 `greet()`，却依然遵循协议。在协议扩展内部，你可以使用协议的每一项要求——这里是 `name`——因为任何遵循协议的类型都保证拥有它。

---

协议扩展还可以添加协议从未列为要求的成员。它们是额外的便利功能，每个遵循协议的类型都能使用：
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
`isEmpty` 不是一项要求，因此遵循协议的类型不必提供它——它直接获得该成员。

---

一个协议可以建立在另一个协议之上。在冒号后写下一个协议的名称，会让新协议**继承**旧协议的每一项要求：
```swift
protocol Named {
    var name: String { get }
}

protocol Aged: Named {
    var age: Int { get }
}
```
遵循 `Aged` 的类型必须提供 `age` *和* `name`，并且它在任何地方都被视为 `Named` 类型。一个协议可以同时继承多个协议，用逗号分隔。

---

默认实现是一个后备方案，而不是一条规则。如果遵循协议的类型提供了自己对某项要求的实现，运行的就是它自己的版本：
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

print(Ticket().price) // 12, not 0
```
默认实现只填补类型留出的空缺。

---

标准库由协议构建而成，你自己的类型也可以采用它们。

`Equatable` 为类型提供 `==` 运算符。对于存储属性全部为 `Equatable` 的结构体，声明遵循关系就够了——Swift 会替你写出 `==`：
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

print(Point(x: 1, y: 2) == Point(x: 1, y: 2)) // true
```
`Comparable` 继承自 `Equatable` 并添加了排序。你只需实现一个运算符 `<`，把它写成一个接收两个值的 `static func`，就能免费获得 `>`、`<=`、`>=`，以及集合上的 `sorted()`、`min()` 和 `max()`：
```swift
struct Version: Comparable {
    var number: Int

    static func < (lhs: Version, rhs: Version) -> Bool {
        return lhs.number < rhs.number
    }
}
```

---

`CustomStringConvertible` 决定 `print` 为你的类型显示什么。它唯一的要求是一个 `description` 属性：
```swift
struct Coin: CustomStringConvertible {
    var value: Int

    var description: String {
        return "\(value)c"
    }
}

print(Coin(value: 25)) // 25c
```
如果没有遵循该协议，打印结构体时会退回到类似 `Coin(value: 25)` 的默认输出，而仅有 `description` 属性不会带来任何改变——`print` 寻找的是协议。字符串插值也会使用 `description`。

---

协议名称本身不是一个类型，而是一种约束，因此 Swift 要求你说明自己指的是两种东西中的哪一种。

`some Shape` 表示*某一个具体的遵循协议的类型*，在编译期就已固定。调用者永远不知道具体是哪个类型，但它始终是同一个类型：
```swift
func unitSquare() -> some Shape {
    return Square(side: 1)
}
```
`any Shape` 表示*一个可以容纳任何遵循协议类型的盒子*，该类型的两个值可以容纳不同的类型。只要具体类型可能变化，你就需要它，例如在混合数组中：
```swift
let shapes: [any Shape] = [Square(side: 2), Rect(width: 2, height: 3)]
```
两者都允许你调用协议的要求。当单一类型足够时优先使用 `some`，因为它在运行时没有任何开销；当你确实需要混合多种类型时再使用 `any`。
