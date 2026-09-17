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
print(r.area) // 12、括弧なし
```
計算プロパティは何も格納しないため、メンバーワイズイニシャライザには含まれません。値が他の値から導かれるときは計算プロパティを、処理にパラメータが必要なときはメソッドを使います。

---

構造体は**値型**です。別の変数に代入したり関数に渡したりすると、*コピー*が渡されます。コピーを変更しても元のインスタンスはそのままです。
```swift
struct Point {
    var x: Int
}

var a = Point(x: 1)
var b = a
b.x = 99
print(a.x) // 1
```
クラスは**参照型**です。`b = a`とすると両方の名前が同じインスタンスを指すようになるので、`b.x = 99`は`a.x`も`99`に変更してしまいます。

これが2つの本当の違いです。そしてSwiftがほとんどのデータを構造体としてモデル化する理由でもあります。自分が持っている値は、それを受け取ったコードによって後から勝手に変更されることがありません。

---

構造体は値なので、`mutating`キーワードでそう宣言しない限り、メソッドがプロパティを変更することは許されません:
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
mutatingメソッドを呼び出せるのは、`var`に格納されたインスタンスだけです。`let`のインスタンスでは値が固定されているため、`c.increase(by: 5)`はコンパイルできません。

---

メンバーワイズイニシャライザが自分の望む型の作り方ではないときは、独自の**イニシャライザ**を書きます。`init`で宣言し、好きなパラメータを取れ、終わるまでにすべての格納プロパティに値を与えなければなりません。その中では、`self`は作られつつあるインスタンスです:
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
構造体の波括弧の中に`init`を書くとメンバーワイズイニシャライザは置き換えられるので、以降は`Square(side: 5)`は存在しなくなります。

---

通貨コード、共有されるデフォルト、よく使うケースを作るファクトリのように、単一のインスタンスではなく型そのものに属する値があります。それらには`static`を付け、型名を通して読み取ります:
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
ここで`currency`は決して変わらないため`let`で宣言されており、プログラム全体で共有される定数です。`Money.currency`は1つも`Money`を作らなくても使えますが、`amount`にはインスタンスが必要です。

---

型が対応していると宣言しない限り、2つの構造体を`==`で比較することはできません。それを行うには、`Equatable`**プロトコル**に準拠します。宣言ではコロンの後に書きます:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

let a = Point(x: 1, y: 2)
let b = Point(x: 1, y: 2)
print(a == b) // true
```
`==`を自分で書く必要はありません。すべての格納プロパティがすでに`Equatable`なら、Swiftがプロパティを1つずつ比較する`==`を自動的に合成してくれます。すべてのプロパティが等しいときに2つのインスタンスは等しく、これは値に期待する動作そのものです。

---

構造体も他の型と同じように、配列や辞書やセットに格納でき、すでに知っているすべてのツールがそのまま使えます:
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
配列が保持しているのは*コピー*です。`items[0]`を変数に読み出して変更しても、配列には影響しません。
