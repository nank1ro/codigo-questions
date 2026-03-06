`enumeration`（枚举）为一组相关的值定义了一个通用类型，使你能够在代码中以类型安全的方式使用这些值。
我们使用 `enum` 关键字声明枚举：
```swift
enum Colors {
    case blue
    case red
    case green
}
```
在枚举中定义的值（例如 `blue`、`red` 和 `green`）是它的_枚举成员_。
我们使用 `case` 关键字来引入新的枚举成员。

---

多个成员可以出现在同一行，用逗号分隔：
```swift
enum Colors {
    case blue, red, green
}
```

---

我们可以使用 `switch` 语句来匹配单个枚举值：
```swift
let color = Colors.red
switch color {
    case .blue:
        print("Blue")
    case .red:
        print("Red")
    case .green:
        print("Green")
}
// prints "Red"
```
请注意，如果你不需要为每个枚举成员都提供一个 `case`，可以提供一个 `default` 分支来覆盖未明确处理的成员

---

对于某些枚举，拥有该枚举所有成员的集合是很有用的。
你可以通过在枚举名称后面写 `: CaseIterable` 来启用此功能。
Swift 将所有成员的集合作为枚举类型的 `allCases` 属性暴露出来：
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```
