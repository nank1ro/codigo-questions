時には値が単に存在しないことがあります。ミドルネームを持たないユーザー、何も見つからない検索、数値に変換できないテキストなどです。
Swiftは`nil`で値の欠如を表しますが、通常の変数はそれを保持できません:
```swift
var age: Int = nil // error: 'nil' cannot initialize type 'Int'
```
値の欠如を許可するには、型の後に疑問符`?`を付けて**オプショナル**型を宣言します。
`Int?`は`Int`または`nil`のどちらかを保持します:
```swift
var age: Int? = 30
age = nil // 許可される
```
値を指定せずに宣言されたオプショナル変数は、`nil`から始まります。

---

オプショナルは`==`や`!=`を使って`nil`と比較したり、ラップされた型の通常の値と直接比較したりできます:
```swift
var score: Int? = 10
print(score == nil) // false
print(score == 10)  // true
```
`Int?`と`Int`は異なる型であることを忘れないでください。`Int?`は空になり得ますが、`Int`は決して空になりません。

---

オプショナルは箱のようなものです。中の値を使う前に、それを開ける必要があり、Swiftではこれを**アンラップ**と呼びます。
最も手早い方法は、感嘆符`!`を使う**強制アンラップ**です:
```swift
let score: Int? = 10
print(score! + 5) // 15
```
`!`はSwiftに「ここには確実に値がある」と伝えます。もしそれが誤りで、オプショナルが`nil`だった場合、プログラムは即座に実行時クラッシュで停止します:
```swift
let missing: Int? = nil
print(missing! + 5) // Fatal error: Unexpectedly found nil
```
そのため強制アンラップは危険だとされており、値の存在が確実な場合にのみ使うべきです。

---

強制アンラップは、オプショナルが`nil`でないことをすでに確認している場合にのみ安全です:
```swift
if score != nil {
    print(score! * 2)
}
```

---

`nil`かどうかを確認してから強制アンラップするのは冗長です。Swiftは`if let`による**オプショナルバインディング**を提供しており、これはオプショナルをアンラップして新しい定数に値を格納することを一度に行います:
```swift
let score: Int? = 10
if let value = score {
    print("Score: \(value)") // valueはInt?ではなくInt
} else {
    print("No score")
}
```
`if`の本体は、オプショナルが値を含む場合にのみ実行されます。その中では`value`は`Int?`ではなく通常の`Int`であり、`!`は不要です。

---

値が欠けていることが「ここで処理を止める」ことを意味する場合、`guard let`は`if let`よりも明確です。
これはオプショナルをアンラップし、失敗した場合は`else`ブロックを実行します。このブロックは現在のスコープを抜け出す必要があります(`return`、`break`、`continue`、`throw`のいずれかで):
```swift
func greet(_ name: String?) {
    guard let name = name else {
        print("Nobody here")
        return
    }
    print("Hello, \(name)!") // ここから先、nameはString
}
```
`if let`と異なり、アンラップされた定数は関数の残りの部分でも使用可能なままなので、正常系の処理は`if`の中にネストされません。

---

`guard let`の典型的な使い方は、関数の先頭で入力を検証し、値が欠けている場合にフォールバック値を返すことです:
```swift
func length(of text: String?) -> Int {
    guard let text = text else { return 0 }
    return text.count
}
```

---

オプショナルから欲しいものは、多くの場合その値かデフォルト値のどちらかです。
**nil結合演算子**`??`はまさにそれを行います。オプショナルが値を持っていればアンラップし、そうでなければ右側の値を返します:
```swift
let score: Int? = nil
let points = score ?? 0 // pointsは0に等しいInt
```
デフォルト値はラップされた値と同じ型でなければなりません。
`??`は複数連結でき、最初の`nil`でない値が採用されます。
```swift
let a: Int? = nil
let b: Int? = 7
print(a ?? b ?? 0) // 7
```

---

`??`は、妥当なデフォルト値がある場合にオプショナルを通常の値に変換する最も短い方法です:
```swift
func volume(from setting: Int?) -> Int {
    return setting ?? 50
}
```

---

`??`を連結すると、Swiftは左から右へ評価し、`nil`でない最初の値で止まります。最後のデフォルト値は、それより前のすべてのオプショナルが`nil`の場合にのみ使用されます。

---

オプショナルに対してプロパティにアクセスしたりメソッドを呼び出したりするには、まずアンラップする必要があります。
`?.`を使った**オプショナルチェーン**はそれを代わりに行ってくれます。オプショナルが`nil`であれば式全体が`nil`になり、そうでなければアクセスが実行されます:
```swift
let name: String? = "swift"
let upper = name?.uppercased() // "SWIFT"を保持するString?
```
結果はプロパティ自体がオプショナルでなくても、常にオプショナルになります。
チェーンは必要なだけ長くでき、`??`ともうまく組み合わせられます:
```swift
class User {
    var nickname: String? = "ace"
}
let user: User? = User()
print(user?.nickname?.count ?? 0) // 3
```

---

オプショナルチェーンは、データが複数の階層で欠けている可能性がある場合に真価を発揮します。オブジェクト自体が`nil`になり得て、そのプロパティの1つも`nil`になり得ます。
1つの`?.`チェーンで、`if`を使わずにその両方を処理できます。

---

1つの`if let`や`guard let`で複数のオプショナルを一度にアンラップできます。バインディングをカンマで区切ります。
本体は、すべてのオプショナルが値を持っている場合にのみ実行されます:
```swift
let first: String? = "Ada"
let last: String? = "Lovelace"
if let first = first, let last = last {
    print("\(first) \(last)")
}
```
バインディングの後に、`if let n = number, n > 0`のように真偽値の条件を追加することもできます。

---

複数のオプショナルを1つの`if let`でバインドすると、コードがフラットに保たれます。1つの`else`分岐が、値が欠けているすべての場合をカバーします。

---

多くの操作は失敗する可能性があり、Swiftはオプショナルを返すことで失敗を報告します。
テキストを数値に変換するのはその典型例です。`Int("42")`は`42`を保持する`Int?`を返し、`Int("abc")`は`nil`を返します。
`Int("3.5")`もテキストが整数ではないため`nil`になります。小数には`Double("3.5")`を使ってください。
```swift
let typed = "42"
if let number = Int(typed) {
    print(number + 1) // 43
}
```
他の例としては`array.first`(空の配列に対しては`nil`)や`dictionary[key]`(キーが存在しない場合は`nil`)があります。

---

変換は失敗する可能性があるため、その結果は常にオプショナルであり、テキストが有効な数値だと確信していても使用前にアンラップしなければなりません。

---

失敗する可能性のある変換は`guard let`と自然に組み合わさります。変換し、結果が`nil`の場合は処理を中断し、その後は通常の値として扱います。

---

時には、オプショナルの中の値を変換しつつ、結果もオプショナルのままにしておきたいことがあります。手動でアンラップと再ラップをせずに済みます。
オプショナルには`map`メソッドがあります。値がある場合はクロージャを適用し、そうでなければ`nil`を返します。
```swift
let score: Int? = 10
let doubled = score.map { $0 * 2 } // 20を保持するInt?
let missing: Int? = nil
let stillMissing = missing.map { $0 * 2 } // nil
```
失敗する可能性のある変換と組み合わせると、`Int(text).map { $0 + 1 }`のようなコンパクトなパイプラインになります。
