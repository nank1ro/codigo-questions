**拡張**は既存の型に新しい機能を追加します。追加先は`Int`や`String`のような標準ライブラリの型でも、自分で書いた構造体やクラスでもかまいません。
`extension`キーワードに続けて型の名前を書き、新しいメンバーを波括弧の中に記述します:
```swift
extension Int {
    func squared() -> Int {
        return self * self
    }
}
print(4.squared()) // 16
```
拡張の中では、`self`はメソッドが呼び出される値を表します。`4.squared()`では`self`は`4`です。拡張が定義されると、プログラム内のすべての`Int`が新しいメソッドを持つようになります。まるで最初から`Int`の一部であったかのように動作します。

---

拡張はどんな型にも使えます。ソースコードを持っていない型でさえ対象にできます。`String`は標準ライブラリ由来ですが、それでも新しいメソッドを追加できます:
```swift
extension String {
    func whisper() -> String {
        return self.lowercased() + "..."
    }
}
print("HELLO".whisper()) // hello...
```
拡張の中では、型の他のメンバーを呼び出すときに`self.`を省略できます。`lowercased()`だけで`self.lowercased()`と同じ意味になります。

---

拡張は新しい型を作るのではなく、元の型をコピーするわけでもありません。型そのものにメンバーを追加するので、その型の既存の値も将来作られる値も、すべて追加されたメンバーを使えます。
だからこそ拡張は、標準ライブラリやフレームワークの型のように編集できない型で非常に役立ちます。`Int`が定義されているファイルを開くことはできませんが、プログラムのどのファイルからでも`Int`を拡張できます。
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

メソッドに加えて、拡張は**計算プロパティ**も追加できます。計算プロパティは値を格納せず、読み出されるたびに値を計算するプロパティです。
計算プロパティは`var`、型注釈、そして値を返す波括弧の本体を使って宣言します:
```swift
extension Int {
    var isNegative: Bool {
        return self < 0
    }
}
print((-3).isNegative) // true
print(7.isNegative)    // false
```
他のプロパティと同じように、括弧を付けずに読み取ります。`7.isNegative()`ではなく`7.isNegative`です。

---

拡張の計算プロパティは`String`にも自然に使えます。`reversed()`メソッドは文字を逆順に並べたものを返し、`String(...)`はそれを再び文字列に変換します:
```swift
extension String {
    var backwards: String {
        return String(reversed())
    }
}
print("swift".backwards) // tfiws
```
メソッドと同様に、拡張の中で`reversed()`と書くと`self.reversed()`を意味します。

---

拡張は計算プロパティを追加できますが、**格納プロパティ**は追加できません。次のコードはコンパイルできません:
```swift
extension Int {
    var label = "number" // error: extensions must not contain stored properties
}
```
格納プロパティは、型のすべてのインスタンスの中に値を置く場所を必要とします。`Int`の値はプログラムの至る所に、拡張よりずっと前にコンパイルされたコードの中にもすでに存在するため、そのメモリレイアウトを変えることはできません。計算プロパティは場所を必要としません。プロパティが読み出されるときに実行されるコードにすぎないからです。

---

`Int`、`String`、配列、構造体は**値型**です。メソッドは、`mutating`と付けられていない限り、呼び出し元の値を変更できません。拡張にもmutatingメソッドを追加できます:
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
mutatingメソッドの中では`self`に代入できます。値は`var`に格納されていなければなりません。`let`定数に対して`increment()`を呼び出すとコンパイルエラーになります。

---

mutatingメソッドは他のメソッドと同じようにパラメータを取れますし、その場で更新する代わりに`self`を丸ごと置き換えることもできます:
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

拡張は型に新しい**イニシャライザ**を追加できます。構造体の場合、拡張はイニシャライザを置くのに最適な場所です。構造体の本体の中に書いた`init`は自動のメンバーごとのイニシャライザを置き換えますが、拡張に追加したものはそれを残したままにします。
新しいイニシャライザは通常、`self.init(...)`で既存のイニシャライザに処理を委譲します:
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

拡張は他人の型のためだけにあるのではありません。自分のコードを整理する一般的な方法は、格納プロパティを構造体やクラスの本体に置き、振る舞いを1つ以上の拡張に追加することです。各拡張が関連するメンバーをまとめます:
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
拡張に追加されたメンバーは、型の中に書かれているかのように、格納プロパティを直接使えます。

---

拡張は、型を**プロトコル**に準拠させることもできます。プロトコルとは、型が実装を約束する要件のリストです。型の名前に続けてコロンで区切ってプロトコル名を書き、必要なメンバーを本体に追加します。
`CustomStringConvertible`は要件が1つだけの標準プロトコルです。その要件は`String`型の計算プロパティ`description`で、`print`はこのプロパティを使って値を表示します:
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
プロトコルへの準拠をそれぞれ独立した拡張に分けて書くのが、Swiftの型を整理する一般的な方法です。

---

`Array`はジェネリック型です。`[Int]`と`[String]`はどちらも配列ですが、**`Element`**型が異なります。`Array`の拡張はそのすべてに適用されるため、新しいメンバーが一部の要素にしか意味を持たない場合は問題になります。文字列のままの数値は足し算ができません。
`where`節を使うと、拡張を`Element`が特定の型である配列に限定できます:
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
`[3, 9, 2].largest`は動作しますが、`["a", "b"].largest`はコンパイルエラーです。`[String]`にはこのプロパティが存在しないためです。

---

拡張は**static**メンバーも追加できます。staticメンバーとは、単一の値ではなく型そのものに属するプロパティやメソッドで、`static`キーワードを付けて宣言し、型名を通してアクセスします。
`static let`は値を格納しますが許されます。インスタンスごとに1つではなく、型全体に対して1つだけしか存在しないからです:
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
staticメンバーには操作対象の`self`値がありません。`Int.answer`は数値の上ではなく型の上で読み取られます。

---

拡張の中のstaticメソッドは、型の値を生成する小さなファクトリ関数を置くのに適した場所です。`String(repeating:count:)`はテキストを指定した回数繰り返す標準のイニシャライザです:
```swift
extension String {
    static func dashes(_ count: Int) -> String {
        return String(repeating: "-", count: count)
    }
}
print(String.dashes(4)) // ----
```

---

拡張はメンバーを**追加**することだけができ、既存のメンバーを置き換えたりオーバーライドしたりすることはできません。`override`はサブクラスのためのものです。サブクラスは親とは別の型ですが、拡張は同じ型であるため、すでに存在するメソッドを宣言すると再宣言エラーになります:
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
異なる振る舞いが必要な場合は、新しい名前のメソッドを追加するか、型がクラスであればサブクラスを書きます。
