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
print(r.area) // 12, no parentheses
```
计算属性不属于逐一成员初始化器的一部分，因为没有东西需要存储。当值由其他值推导而来时使用计算属性，当工作需要参数时使用方法。
