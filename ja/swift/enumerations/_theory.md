`enumeration`（列挙型）は、関連する値のグループに共通の型を定義し、コード内でそれらの値を型安全な方法で扱えるようにします。
列挙型は`enum`キーワードを使って宣言します:
```swift
enum Colors {
    case blue
    case red
    case green
}
```
列挙型で定義された値（`blue`、`red`、`green`など）は、その_列挙ケース_です。
`case`キーワードを使って新しい列挙ケースを導入します。

---

複数のケースをカンマで区切って1行に記述できます:
```swift
enum Colors {
    case blue, red, green
}
```

---

個々の列挙値を`switch`文でマッチさせることができます:
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
すべての列挙ケースに対して`case`を用意する必要がない場合は、明示的に対処されていないケースをカバーするために`default`ケースを使用できることを覚えておいてください

---

一部の列挙型では、その列挙型のすべてのケースのコレクションがあると便利です。
列挙型の名前の後に`: CaseIterable`と記述することで、これを有効にできます。
Swiftは列挙型のすべてのケースのコレクションを、その列挙型の`allCases`プロパティとして公開します:
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```
