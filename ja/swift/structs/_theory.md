**構造体**(*structure*の略)は、関連する値をまとめておくために自分で設計する型です。別々の`title`と別々の`pages`を個別に扱う代わりに、`Book`を一度記述すればどこでも使えます。

`struct`キーワードで宣言し、その中に書かれた変数は**格納プロパティ**になります:
```swift
struct Book {
    var title: String
    var pages: Int
}
```
`Book`は`Int`や`String`とまったく同じように型になります。インスタンスのプロパティにはドットでアクセスします:
```swift
let book = Book(title: "Swift", pages: 120)
print(book.title) // Swift
```

---

`Book`を作るコードは一度も書いていないのに、`Book(title: "Swift", pages: 120)`が動作しました。Swiftが代わりに書いてくれるのです。すべての構造体は**メンバーワイズイニシャライザ**を無料で受け取ります。これは、格納プロパティが宣言された順にそのままパラメータとなり、プロパティ名が引数ラベルとして使われるイニシャライザです:
```swift
struct Point {
    var x: Int
    var y: Int
}

let p = Point(x: 3, y: 4)
print(p.x) // 3
```
クラスはこれを無料では受け取らないので、構造体が値をモデル化する最も手早い方法である理由の1つになっています。

---

格納プロパティには、宣言した場所で直接**デフォルト値**を与えることができます。Swiftはその値から型を推論するので、型アノテーションは省略できます:
```swift
struct Counter {
    var label: String
    var value = 0
}
```
メンバーワイズイニシャライザでは、デフォルト値を持つプロパティは省略可能な引数になります。渡せばデフォルトを上書きし、省略すればデフォルトがそのまま使われます。
```swift
let a = Counter(label: "clicks")
print(a.value) // 0

let b = Counter(label: "clicks", value: 7)
print(b.value) // 7
```

---

構造体は**メソッド**も持てます。メソッドとは、波括弧の中に書かれた、呼び出し元のインスタンスに対して動作する関数のことです。メソッドの中では、接頭辞を付けずにプロパティ名を直接使えます:
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
メソッドのパラメータがプロパティ名と同じ名前だった場合は、`self.width`と書けばインスタンスのプロパティを意味します。

---

**計算プロパティ**はプロパティのように見えますが、メソッドのように振る舞います。何も格納せず、読み取るたびに値を計算します。型を書き、続けて値を返すコードブロックを書きます:
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
計算プロパティは何も格納しないため、メンバーワイズイニシャライザには含まれません。値が他の値から導かれるときは計算プロパティを、処理にパラメータが必要なときはメソッドを使います。
