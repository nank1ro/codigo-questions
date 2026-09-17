**结构体**（*structure* 的缩写）是你自己设计的一种类型，用来把相关的值放在一起。你不必同时管理一个单独的 `title` 和一个单独的 `pages`，只需描述一次 `Book`，之后随处可用。

使用 `struct` 关键字声明结构体，写在它内部的变量就是它的**存储属性**：
```swift
struct Book {
    var title: String
    var pages: Int
}
```
`Book` 现在就是一个类型了，和 `Int` 或 `String` 完全一样。你可以用点号访问实例的属性：
```swift
let book = Book(title: "Swift", pages: 120)
print(book.title) // Swift
```

---

你从未编写过构建 `Book` 的代码，但 `Book(title: "Swift", pages: 120)` 却能正常工作。Swift 会替你写好它：每个结构体都会免费获得一个**逐一成员初始化器**，这种初始化器的参数就是它的存储属性，按声明顺序排列，且每个参数都以属性名作为参数标签：
```swift
struct Point {
    var x: Int
    var y: Int
}

let p = Point(x: 3, y: 4)
print(p.x) // 3
```
类不会免费获得这一特性，这也是结构体成为建模值的最快方式的原因之一。

---

存储属性可以在声明之处直接赋予**默认值**。Swift 会根据该值推断它的类型，因此你可以省略类型注解：
```swift
struct Counter {
    var label: String
    var value = 0
}
```
逐一成员初始化器会把每个有默认值的属性变成可选参数：传入它即可覆盖默认值，省略它则保留默认值。
```swift
let a = Counter(label: "clicks")
print(a.value) // 0

let b = Counter(label: "clicks", value: 7)
print(b.value) // 7
```

---

结构体还可以包含**方法**：即写在大括号内的函数，它们作用于被调用的实例。在方法内部可以直接使用属性名，不需要任何前缀：
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
如果方法的参数与属性同名（遮蔽了该属性），可以写 `self.width` 来表示实例的属性。

---

**计算属性**看起来像属性，但行为像方法：它不存储任何东西，而是在每次读取时计算它的值。你先写出类型，然后写一个返回该值的代码块：
```swift
struct Rectangle {
    var width: Int
    var height: Int

    var area: Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area) // 12，没有括号
```
计算属性不属于逐一成员初始化器的一部分，因为没有东西需要存储。当值由其他值推导而来时使用计算属性，当工作需要参数时使用方法。

---

结构体是一种**值类型**：把它赋值给另一个变量，或把它传递给函数时，交出去的是一份*副本*。修改副本不会影响原始值。
```swift
struct Point {
    var x: Int
}

var a = Point(x: 1)
var b = a
b.x = 99
print(a.x) // 1
```
类是一种**引用类型**：`b = a` 会让两个名字指向同一个实例，因此 `b.x = 99` 也会把 `a.x` 改成 `99`。

这就是两者真正的区别，也是 Swift 用结构体对大多数数据进行建模的原因：你持有的值不会被接收它的代码在背后修改。

---

因为结构体是一个值，所以方法不允许修改它的属性，除非你用 `mutating` 关键字声明：
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
mutating 方法只能在存储于 `var` 中的实例上调用。对于 `let` 实例，它的值是冻结的，因此 `c.increase(by: 5)` 将无法编译。

---

当逐一成员初始化器不是你希望的类型构建方式时，可以编写自己的**初始化器**。它用 `init` 声明，接收你选择的参数，并且必须在结束前给每个存储属性赋值。在它内部，`self` 是正在被创建的实例：
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
在结构体的大括号内编写 `init` 会取代逐一成员初始化器，因此从现在起 `Square(side: 5)` 就不复存在了。

---

有些值属于类型本身，而不是属于任何单个实例：货币代码、共享的默认值、构建常见情形的工厂。把它们标记为 `static`，然后通过类型名来读取：
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
这里 `currency` 用 `let` 声明，因为它从不改变，所以它是一个由整个程序共享的常量。`Money.currency` 无需创建任何 `Money` 就能使用，而 `amount` 则需要实例。

---

在类型声明它支持之前，两个结构体无法用 `==` 进行比较。你可以通过遵循 `Equatable` **协议**来做到这一点，协议写在声明中冒号的后面：
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

let a = Point(x: 1, y: 2)
let b = Point(x: 1, y: 2)
print(a == b) // true
```
你不必自己编写 `==`：当每个存储属性都已经符合 `Equatable` 时，Swift 会为你合成它，逐个比较属性。当两个实例的所有属性都相等时，它们就是相等的，这正是你对一个值的期望。

---

结构体和其他类型一样，因此它可以存储在数组、字典或集合中，并且你已经掌握的每个工具都能继续作用于它：
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
记住数组存储的是*副本*：把 `items[0]` 读入一个变量再修改它，不会触及数组本身。
