Swiftのすべての値には**型**があり、型はコンパイラにそのデータの種類と、その値で何ができるかを伝えます。
基本的な型は次のとおりです:
- `Int`: `42`や`-7`のような整数
- `Double`: `3.14`のような小数部を持つ数
- `String`: `"Hello"`のようなテキスト
- `Character`: `"a"`のような1文字
- `Bool`: `true`か`false`のどちらか

**型アノテーション**を使うと、定数や変数の型を明示できます。名前の後にコロンと型名を書きます:
```swift
let age: Int = 36
let name: String = "Ada"
```
ある型の値を別の型の定数に格納することはできません。`let age: Int = "36"`はコンパイルエラーになります。

---

ほとんどの場合、型アノテーションを書く必要はありません。Swiftはいくつかのリテラルのルールに従って、代入する値から型を**推論**します:
- 小数点のない数（`42`など）は`Int`
- 小数点のある数（`3.14`など）は`Double`
- ダブルクォートで囲まれたテキストは`String`
- `true`と`false`は`Bool`
```swift
let count = 42     // Int
let price = 9.99   // Double
let name = "Ada"   // String
let isOpen = true  // Bool
```
Swiftには`Float`もあります。これは`Double`の半分のメモリを使う小数ですが、精度が低いため、小数リテラルが`Float`と推論されることはありません。`Float`にするにはアノテーションで指定する必要があります。
同じように`"a"`は`String`と推論されるため、`Character`には常にアノテーションが必要です。

---

`type(of:)`関数は値の型を返します。Swiftが何を推論したかを確認するのに便利です:
```swift
print(type(of: 42))    // Int
print(type(of: 2.5))   // Double
print(type(of: "hi"))  // String
```
推論された型とは異なる型にしたい場合は、アノテーションを追加します。整数リテラルは`Double`や`Float`の定数に格納でき、1文字のリテラルは`Character`の定数に格納できます:
```swift
let ratio: Double = 3       // 3.0, not an Int
let half: Float = 0.5
let initial: Character = "S"
print(type(of: ratio))      // Double
```

---

Swiftは数値型同士を自動的には変換しません。`Int`と`Double`の加算は、どちらも数値であってもコンパイルエラーになります。
```swift
let apples = 3
let price = 1.5
let total = apples * price // error: Int and Double can't be mixed
```
組み合わせるには、値をその型のイニシャライザに渡して、必要な型の新しい値を作ります:
```swift
let total = Double(apples) * price // 4.5
```
逆方向も同様に動作します。`Int(4.5)`は`Int`を生成し、数の整数部分だけを保持します。

---

`Int(x)`は四捨五入をしません。小数部を単純に切り捨てる**切り捨て（truncation）**を行うため、`Int(3.99)`は`3`に、`Int(-3.99)`は`-3`になります。
最も近い整数に丸めるには、まず`Double`に対して`rounded()`を呼び出してから変換します:
```swift
let x = 3.99
print(Int(x))            // 3
print(Int(x.rounded()))  // 4
```
`2.5`のような中間の値はゼロから離れる方向に丸められます。`2.5`は`3.0`に、`-2.5`は`-3.0`になります。

---

除算がどのように動作するかは、オペランドの型で決まります。両方が`Int`の場合、`/`演算子は**整数除算**を行います。結果は`Int`になり、余りは捨てられます。
少なくとも片方のオペランドが`Double`の場合、`/`は浮動小数点除算を行い、小数部を保持します:
```swift
print(7 / 2)              // 3
print(7.0 / 2)            // 3.5
let slices = 7
print(Double(slices) / 2) // 3.5
```
つまり、2つの`Int`の値から小数の結果を得るには、除算の**前に**少なくとも片方を`Double`に変換しなければなりません。`Double(7 / 2)`は`3.0`になります。整数除算がすでに終わっているからです。

---

関数が整数から計算した小数の結果を返さなければならない場合は、除算の前にオペランドを`Double`に変換し、戻り値の型を`Double`として宣言します:
```swift
func ratio(_ part: Int, _ total: Int) -> Double {
    return Double(part) / Double(total)
}
print(ratio(1, 4)) // 0.25
```
配列の`count`も`Int`であることを忘れないでください。同じ変換が必要です。

---

数値と文字列は同じイニシャライザの構文で変換できます。`String(42)`は数値をテキスト`"42"`に変えます。`"\(42)"`と補間するのとまったく同じです。
逆方向は失敗する可能性があります。すべてのテキストが数値とは限らないため、`Int("42")`は**オプショナル**の`Int?`を返します。ここでは`42`を保持しますが、`Int("hello")`は`nil`です。
nullabilityのレッスンで学んだように、`??`でフォールバックを提供したり、`if let`でアンラップしたりできます:
```swift
let typed = "42"
let number = Int(typed) ?? 0
print(number + 1) // 43
```

---

`Int(text)`は、テキスト全体がオプションの符号付きの有効な整数である場合にのみ成功します:
```swift
print(Int("42"))   // Optional(42)
print(Int("-7"))   // Optional(-7)
print(Int("3.5"))  // nil, not a whole number
print(Int(" 42"))  // nil, spaces are not allowed
print(Int("abc"))  // nil
```
小数のテキストには`Double(text)`を使います。これも同じように`Double?`を返します。`Double("3.5")`は`Optional(3.5)`です。

---

**型エイリアス**は、既存の型に新しい名前を与えます。`typealias`キーワードを使います:
```swift
typealias Score = Int
let best: Score = 100
print(best + 1) // 101
```
`Score`と`Int`は同じ型なので、自由に混在できます。エイリアスは安全性を高めるものではありません。単純な型にプログラム内で特定の意味がある場合に、コードを読みやすくするだけのものです。

---

`Int`は64ビットを使うため、固定された範囲の数しか表現できません。最大値と最小値は`Int.max`と`Int.min`として利用できます:
```swift
print(Int.max) // 9223372036854775807
print(Int.min) // -9223372036854775808
```
これらの限界を超えることは**オーバーフロー**と呼ばれます。他の多くの言語と異なり、Swiftは範囲の反対側へ静かに折り返しません。オーバーフローする演算はプログラムを停止させる**ランタイムエラー**になります。

---

`Int.max`と`Int.min`は、最大値や最小値を探すときの初期値として便利です。どんな実際の数も`Int.max`より小さいので、「これまでに見つけた最小値」の安全な初期値になります:
```swift
var smallest = Int.max
for number in [8, 3, 5] {
    if number < smallest {
        smallest = number
    }
}
print(smallest) // 3
```

---

stringsのレッスンで見たように、`String`を反復処理すると1度に1つの`Character`が得られます。`Character`は`String`ではないため、テキストとして使うには`String(c)`で変換します。
文字が数字のとき、`wholeNumberValue`プロパティはその数値を`Int?`として返します。数字ではない文字に対しては`nil`になります。
```swift
for c in "a1" {
    print(c.wholeNumberValue)
}
// nil
// Optional(1)
```

---

`Int(text)`と`Double(text)`は失敗すると`nil`を返すため、結果を`nil`と比較すると、そのテキストがその種類の数値かどうかが分かります:
```swift
print(Int("42") != nil)     // true
print(Double("4.2") != nil) // true
print(Double("42") != nil)  // true, a whole number is also a valid Double
```
最後の行に注目してください。`Int`が受け付けるテキストはすべて`Double`でも受け付けられるため、両者を区別したい場合は先に`Int`をチェックします。

---

異なる型の値を一緒に格納しなければならないことがあります。特殊な型`Any`は**あらゆる**型の値を保持できるため、`[Any]`として宣言された配列は数値、文字列、ブーリアンを混在させられます:
```swift
let items: [Any] = [1, "two", true]
```
各要素は依然として本当の型を覚えており、`type(of:)`がそれを明らかにします。値をその本当の型として扱うには、`as?`による**条件付きキャスト**を使います。これはオプショナルを返し、型が一致すればその値を保持し、そうでなければ`nil`になります:
```swift
for item in items {
    if let number = item as? Int {
        print(number + 1) // runs only for 1
    }
}
```
`Any`は最後の手段です。単一の具体的な型の配列のほうが安全で扱いやすいので、できる限りそちらを選んでください。

---

条件付きキャストは`else if`と自然に連鎖して、複数の可能性のある型を扱えます。結果に必要な型へそれぞれ変換します:
```swift
let item: Any = 2.5
if let number = item as? Int {
    print(Double(number))
} else if let number = item as? Double {
    print(number)
}
```
`Any`に格納された`Int`は依然として`Int`です。それに対する`as? Double`は`nil`を返します。`as?`は型をチェックするのであって、数値を変換するわけではないからです。
