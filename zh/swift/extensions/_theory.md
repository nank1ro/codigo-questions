**扩展**为现有类型添加新功能：可以是 `Int` 或 `String` 这样的标准库类型，也可以是你自己编写的结构体或类。
你写下 `extension` 关键字，后跟类型的名称，并把新成员放在花括号之间：
```swift
extension Int {
    func squared() -> Int {
        return self * self
    }
}
print(4.squared()) // 16
```
在扩展内部，`self` 是方法被调用时所在的值：在 `4.squared()` 中它就是 `4`。扩展一旦存在，程序中的每个 `Int` 都拥有这个新方法，完全就像它从一开始就是 `Int` 的一部分一样。

---

扩展可以作用于任何类型，甚至是你没有源代码的类型。`String` 来自标准库，但你仍然可以为它添加新方法：
```swift
extension String {
    func whisper() -> String {
        return self.lowercased() + "..."
    }
}
print("HELLO".whisper()) // hello...
```
在扩展内部，调用该类型的其他成员时可以省略 `self.`：单独写 `lowercased()` 就表示 `self.lowercased()`。

---

扩展不会创建新类型，也不会复制旧类型：它把成员添加到类型本身，因此该类型的每个现有值和将来的值都能拥有这些成员。
这就是扩展对于你无法编辑的类型（比如来自标准库或框架的类型）如此有用的原因：你打不开定义 `Int` 的那个文件，但可以在程序的任何文件中扩展它。
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

除了方法之外，扩展还可以添加**计算属性**：这种属性不存储值，而是在每次被读取时计算它。
计算属性用 `var`、类型注解以及返回值的花括号主体来声明：
```swift
extension Int {
    var isNegative: Bool {
        return self < 0
    }
}
print((-3).isNegative) // true
print(7.isNegative)    // false
```
它的读取方式和其他属性一样，不带括号：是 `7.isNegative`，而不是 `7.isNegative()`。

---

扩展中的计算属性也很适合用在 `String` 上。`reversed()` 方法按相反的顺序返回字符，而 `String(...)` 再把它们转回字符串：
```swift
extension String {
    var backwards: String {
        return String(reversed())
    }
}
print("swift".backwards) // tfiws
```
与方法一样，扩展内的 `reversed()` 表示 `self.reversed()`。

---

扩展可以添加计算属性，但**不能添加存储属性**：下面的代码无法编译：
```swift
extension Int {
    var label = "number" // error: extensions must not contain stored properties
}
```
存储属性需要在类型的每个实例内部占据空间。`Int` 值已经遍布你的程序，甚至存在于早在你的扩展之前编译的代码中，因此它们的内存布局无法改变。计算属性不需要空间，因为它只是在属性被读取时运行的代码。

---

`Int`、`String`、数组和结构体都是**值类型**：除非方法被标记为 `mutating`，否则它不能改变被调用时所在的值。扩展也可以添加 mutating 方法：
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
在 mutating 方法内部，你可以给 `self` 赋值。该值必须存储在 `var` 中：对 `let` 常量调用 `increment()` 是编译错误。

---

mutating 方法可以像其他方法一样接收参数，并且可以完全替换 `self`，而不是原地更新它：
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

扩展可以为类型添加新的**构造器**。对结构体来说，扩展是放置它们的最佳位置：写在结构体主体内的 `init` 会替换自动生成的逐一成员构造器，而在扩展中添加的 `init` 则会保留它。
新的构造器通常通过 `self.init(...)` 委托给已有的构造器：
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

扩展不仅适用于别人的类型。组织自己代码的一种常见方式是把存储属性保留在结构体或类的主体中，而把行为添加到一个或多个扩展中，每个扩展归组相关的成员：
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
在扩展中添加的成员可以直接使用存储属性，完全就像它们写在类型内部一样。

---

扩展还可以让类型遵循一个**协议**，协议是一组该类型承诺实现的要求。把协议名称写在类型名称后面，用冒号分隔，并在主体中添加所需的成员。
`CustomStringConvertible` 是一个标准协议，它只有一个要求：`String` 类型的计算属性 `description`，`print` 用它来显示值：
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
把每个协议遵循放在各自的扩展中是组织 Swift 类型的常见方式。

---

`Array` 是一个泛型类型：`[Int]` 和 `[String]` 都是数组，但具有不同的 **`Element`** 类型。`Array` 的扩展对它们全部生效，当新成员只对某些元素有意义时这就是个问题：你无法把字符串当作数字相加。
`where` 子句把扩展限制在 `Element` 为给定类型的那些数组上：
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
`[3, 9, 2].largest` 可以工作，而 `["a", "b"].largest` 是编译错误：该属性在 `[String]` 上不存在。

---

扩展可以添加 **static** 成员：属于类型本身而不是单个值的属性和方法，它们用 `static` 关键字标记，并通过类型名称访问。
`static let` 是允许的，即使它存储一个值，因为整个类型只有一份副本，而不是每个实例各一份：
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
静态成员没有可供操作的 `self` 值：`Int.answer` 是在类型上读取的，而不是在某个数字上。

---

扩展中的静态方法很适合存放构建该类型值的小型工厂函数。`String(repeating:count:)` 是把一段文本重复若干次的标准构造器：
```swift
extension String {
    static func dashes(_ count: Int) -> String {
        return String(repeating: "-", count: count)
    }
}
print(String.dashes(4)) // ----
```

---

扩展只能**添加**成员，永远不能替换或重写已有成员。`override` 属于子类，子类与其父类是不同的类型；而扩展是同一个类型，因此声明一个已经存在的方法是重复声明错误：
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
如果你需要不同的行为，可以添加一个使用新名称的方法，或者在类型是类时编写一个子类。
