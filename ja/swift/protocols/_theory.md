**プロトコル**は、その方法には触れずに、型が何を持たなければならないかを記述します。プロトコルとは、それを採用する型が提供することを約束する要件（プロパティとメソッド）のリストです。

宣言には`protocol`キーワードを使います。プロパティの要件は、型の後にそのアクセス方法を示すブロックを続けて書きます。`{ get }`は、型が少なくともその値を読めるようにしなければならないことを意味します。
```swift
protocol Named {
    var name: String { get }
}
```
型がプロトコルに**準拠**するには、コロンの後にプロトコル名を書き、プロトコルが求めるすべてを提供します:
```swift
struct Cat: Named {
    var name: String
}

let cat = Cat(name: "Luna")
print(cat.name) // Luna
```
プロトコルはそれ自身のデータを一切持ちません。プロトコルは契約です。それを満たすすべての型は、コードの他の部分から同じように扱えます。

---

プロトコルは**メソッド**を要求することもできます。書くのはシグネチャ（名前、パラメータ、戻り値の型）までで、本体は書きません:
```swift
protocol Greeter {
    func greet() -> String
}
```
準拠する型は、そのシグネチャとまったく同じメソッドを宣言し、本体を提供しなければなりません:
```swift
struct Robot: Greeter {
    func greet() -> String {
        return "BEEP"
    }
}

print(Robot().greet()) // BEEP
```
名前、パラメータの型、戻り値の型のどれか1つでも違えば、その型は準拠しておらず、コンパイラがどの要件が満たされていないかを教えてくれます。

---

プロパティの要件は、常にそのプロパティがどのように使えるかを示します。`{ get }`は値が読めることだけを求め、`{ get set }`は読めることに加えて**代入**もできることを求めます:
```swift
protocol Account {
    var owner: String { get }
    var balance: Int { get set }
}
```
準拠する型が契約以上のものを提供することは常に許されます。格納プロパティの`var`は`{ get }`を十分に満たします。しかし契約より少なくなることは許されません。`let`定数や読み取り専用の計算プロパティは`{ get set }`を満たせません。

---

プロトコルは構造体に限ったものではありません。**クラス**もまったく同じ方法で、コロンの後にプロトコルを並べることで準拠します:
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
クラスが別のクラスも継承している場合は、リストの先頭にスーパークラスを書き、その後にプロトコルを並べます。1つの型が複数のプロトコルを一度に採用することもでき、その場合はコンマで区切ります。

---

**列挙型**も準拠できます。列挙型には格納プロパティがないので、プロパティの要件は通常、ケースを`switch`する計算プロパティで満たします:
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
構造体、クラス、列挙型。この3つはどれも同じ方法でプロトコルを採用でき、プロトコルに対して書かれたコードはそのすべてで動作します。

---

1つのプロトコルには通常、複数の要件が集められます。そして準拠する型は、そのすべてを満たさなければなりません:
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
波括弧の中での要件の順序は問われません。準拠する型が要件を提供する順序も同じです。コンパイラが確認するのは、欠けているものがないことだけです。

---

構造体は値型なので、格納プロパティの1つを変更するメソッドには`mutating`を付けなければなりません。そのメソッドがプロトコルの要件である場合、プロトコル側でもそのことを示さなければなりません:
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
プロトコルに`mutating`がなければ、構造体がその要件を満たすことは決してできません。クラスは参照型なので、このキーワードは決して必要ありません。クラスは普通のメソッドで`mutating`要件を満たします。mutatingメソッドの呼び出しには`var`が必要で、`let`ではコンパイルエラーになります。

---

準拠は型のすぐ隣で宣言しなければならないわけではありません。**拡張**が後から追加できるので、型自身の宣言はデータに集中したままになります:
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
これは自分で書いていない型にも使えます。標準ライブラリの型を、そのソースに触れることなく自分のプロトコルに準拠させられるのです。

---

**プロトコル**の拡張は別の道具です。過去も未来も、準拠するすべての型にメンバーを追加します。これが、要件に**デフォルト実装**を与える方法です:
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
`Person`は`greet()`を一度も書いていませんが、それでも準拠しています。プロトコル拡張の中では、プロトコルのすべての要件（ここでは`name`）を使えます。準拠する型は必ずそれを持つことが保証されているからです。

---

プロトコルの拡張は、プロトコルが要件として列挙したことのないメンバーも追加できます。それらは追加のおまけで、準拠するすべての型で使えます:
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
`isEmpty`は要件ではないので、準拠する型が提供する必要はありません。型はそれをそのまま手に入れます。

---

プロトコルは別のプロトコルを土台にできます。コロンの後にプロトコル名を書くと、新しいプロトコルは古いプロトコルのすべての要件を**継承**します:
```swift
protocol Named {
    var name: String { get }
}

protocol Aged: Named {
    var age: Int { get }
}
```
`Aged`に準拠する型は`age`*と*`name`の両方を提供しなければならず、どこでも`Named`型として扱われます。1つのプロトコルは複数のプロトコルを一度に継承でき、コンマで区切ります。

---

デフォルト実装は規則ではなくフォールバックです。準拠する型が要件の独自バージョンを提供していれば、実行されるのはそのバージョンです:
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

print(Ticket().price) // 12、0ではない
```
デフォルトが埋めるのは、型が開けたままにした隙間だけです。

---

標準ライブラリはプロトコルの上に成り立っており、自分の型もそれらを採用できます。

`Equatable`は型に`==`演算子を与えます。格納プロパティがすべて`Equatable`である構造体なら、準拠を宣言するだけで十分です。Swiftが`==`を書いてくれます:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

print(Point(x: 1, y: 2) == Point(x: 1, y: 2)) // true
```
`Comparable`は`Equatable`を継承し、順序付けを追加します。2つの値を受け取る`static func`として書かれた演算子`<`を1つ実装すれば、`>`、`<=`、`>=`に加え、コレクションの`sorted()`、`min()`、`max()`も無料で使えます:
```swift
struct Version: Comparable {
    var number: Int

    static func < (lhs: Version, rhs: Version) -> Bool {
        return lhs.number < rhs.number
    }
}
```

---

`CustomStringConvertible`は、`print`が自分の型に対して何を表示するかを決めます。その唯一の要件は`description`プロパティです:
```swift
struct Coin: CustomStringConvertible {
    var value: Int

    var description: String {
        return "\(value)c"
    }
}

print(Coin(value: 25)) // 25c
```
準拠がなければ、構造体の表示は`Coin(value: 25)`のようなデフォルトの出力にフォールバックします。そして`description`プロパティだけでは何も変わりません。`print`はプロトコルを探すからです。文字列補間も`description`を使います。

---

プロトコル名そのものは型ではなく制約です。そのためSwiftは、2つのうちどちらを意味するのかを明示するよう求めます。

`some Shape`は*1つの具体的な準拠型*を意味し、コンパイル時に固定されます。呼び出し側がどの型かを知ることはありませんが、常に同じ型です:
```swift
func unitSquare() -> some Shape {
    return Square(side: 1)
}
```
`any Shape`は*任意の準拠型を入れられる箱*を意味し、その型の2つの値が異なる型を保持してもかまいません。具体的な型が変わり得る場所、たとえば混在した配列の中では、これが必要です:
```swift
let shapes: [any Shape] = [Square(side: 2), Rect(width: 2, height: 3)]
```
どちらもプロトコルの要件を呼び出せます。1つの型で十分なときは`some`を選びましょう。実行時のコストがゼロだからです。型を本当に混ぜたいときは`any`を使います。
