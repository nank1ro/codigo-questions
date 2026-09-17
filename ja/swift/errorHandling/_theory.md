Swiftでは、エラーはクラッシュではなく**値**です。`Error`プロトコルに準拠すればどの型でもエラーとして振る舞え、列挙型がよく選ばれます。ケースが何がうまくいかないかを正確に名前で示すからです:
```swift
enum LoginError: Error {
    case wrongPassword
}
```
失敗する可能性のある関数には`throws`が付けられ、`throw`で失敗を報告します:
```swift
func login(_ password: String) throws {
    if password != "swift" {
        throw LoginError.wrongPassword
    }
    print("welcome")
}
```
そのような関数の呼び出しには`try`が必要で、呼び出しは`do`ブロックの中に置き、その後に失敗したときの対処を記述する`catch`ブロックを続けます:
```swift
do {
    try login("hunter2")
} catch {
    print("login failed")
}
// login failed を出力
```
`throw`が実行されると、`do`ブロックの残りはスキップされ、`catch`が引き継ぎます。クラッシュは起こりません。プログラムは`catch`の後も続行します。

---

スローする関数でも値を返せます。`throws`キーワードはパラメータリストと返却の矢印の間に書きます:
```swift
func square(_ n: Int) throws -> Int {
    if n < 0 {
        throw SquareError.negative
    }
    return n * n
}
```
声に出して読むとこうなります。*squareは`Int`を受け取り、スローするかもしれず、`Int`を返す*。

呼び出し側では、何もスローされなかったときだけ値が存在します。そのため代入は`do`ブロックの中に置きます:
```swift
do {
    let result = try square(4)
    print(result) // 16
} catch {
    print("failed")
}
```
`try`は飾りではありません。なければコンパイラが呼び出しを拒否するので、読む人はどの行が失敗しうるかを常に見て取れます。

---

裸の`catch`はすべてのエラーを同じように扱います。多くの場合、特定の失敗に反応したいはずです。そこで`catch`には**パターン**を持たせられます。処理する意思のあるケースです:
```swift
do {
    try check("")
} catch ValidationError.empty {
    print("the text is empty")
} catch {
    print("something else")
}
```
Swiftは`catch`句を上から下へ試し、パターンが一致した最初のものを実行します。

最後の`catch`には意図的にパターンがありません。パターン付きの`catch`は名前を付けたケースしかカバーせず、Swiftはすべてのエラーがどこかで処理されることを求めるため、パターンを並べた`do`ブロックには残りを拾い集める最後のパターンなしの`catch`が必要です。

---

順序が重要です。Swiftはスローされた値を、書かれた順に各`catch`パターンと比較し、最初に一致したところで止まります。そのため先頭に置かれたパターンなしの`catch`は、その下のすべてを飲み込んでしまいます。具体的なケースは上に置き、すべてを受け止める`catch`は下に置きましょう。

どのパターンにも一致しないエラーも無視されるわけではありません。最後のパターンなしの`catch`に届きます。

---

エラーのケースはデータを持てます。ケースに**関連値**を付けると、`throw`がそれを埋めてくれます。ハンドラは*何が*失敗したかだけでなく、*どの程度*かまで知ることができます:
```swift
enum ValidationError: Error {
    case tooShort(minimum: Int)
}

throw ValidationError.tooShort(minimum: 8)
```
対応する`catch`はそれらの値を`let`で束縛します:
```swift
} catch ValidationError.tooShort(let minimum) {
    print("needs at least \(minimum) characters")
}
```
`let`の後の名前は自由に選べます。その`catch`ブロックの中でのみ使える新しい定数です。これにより、失敗が起きた場所で数値を文字列に貼り付けることなく、エラーが役立つメッセージを運べます。

---

1つの列挙型は通常、1つの処理が失敗しうるすべての方法を持ちます。理由ごとに1つのケースです:
```swift
enum FormError: Error {
    case empty
    case tooLong
}
```
ケースごとに`catch`を書くのは繰り返しになります。代わりに型ごとまとめてキャッチし、値に対して`switch`します:
```swift
} catch let error as FormError {
    switch error {
    case .empty: print("empty")
    case .tooLong: print("too long")
    }
} catch {
    print("unknown")
}
```
`catch let error as FormError`は*`FormError`であるものは何でもキャッチし、それを`error`と呼ぶ*という意味です。ブロックの中では`error`は列挙型を持つので、`switch`はケースを認識し、すべてカバーしているかチェックしてくれます。最後のパターンなしの`catch`も依然として必要です。他の型のエラーがこの`do`ブロックに届く可能性があるからです。

---

バリデータは、拒否を先に書いて本題の処理を下部にインデントなしで残すと、最も読みやすくなります。`guard`はそのために作られています。成り立つべき条件を宣言し、成り立たないときに`else`ブロックが実行されます:
```swift
func priceFor(_ quantity: Int) throws -> Int {
    guard quantity > 0 else {
        throw OrderError.notPositive
    }
    return quantity * 3
}
```
`guard`の`else`ブロックは現在のスコープを抜けなければならず、`throw`は`return`、`break`、`continue`と並ぶ、そのための方法の1つです。関数の先頭に積み重ねられた複数の`guard`は、入力が満たすべきルールのリストのように読めます。

---

失敗した*理由*ではなく、失敗したことだけを気にするときがあります。`try?`はスローする呼び出しを**オプショナル**に変えます。成功すれば値、スローすれば`nil`です。
```swift
enum ParseError: Error {
    case notANumber
}

func toInt(_ text: String) throws -> Int {
    guard let value = Int(text) else {
        throw ParseError.notANumber
    }
    return value
}

if let number = try? toInt("42") {
    print(number) // 42
}
```
`do`も`catch`も不要です。失敗は、すでにアンラップ方法を知っているオプショナルに折りたたまれます。代償としてエラーの値は捨てられるので、本当に報告すべきことがないときだけ`try?`を使いましょう。

---

`try?`はオプショナルを生成するので、nil合体演算子`??`がフォールバックを供給して仕上げます:
```swift
let port = (try? readPort(text)) ?? 8080
```
括弧は重要です。なければ`try?`は`??`を含む式全体をカバーしようとするので、コンパイラは失敗する呼び出しがどこで終わるかを明示するよう求めてきます。

この行を1つの文として読みましょう。*読み取れたポートを使い、そうでなければ8080*。復帰が本当に単なるデフォルト値で済むときは、2行の`do`/`catch`が1行に縮みます。

---

3つ目の形があります。`try!`です。コンパイラに*この呼び出しは失敗しない*と伝えるので、`do`も`catch`もオプショナルも不要になります。それでも失敗した場合は、プログラムは即座に停止します。
```swift
let pattern = try! Regex("[0-9]+")
```
これが`try!`が正当化される形です。引数はあなた自身のソースに書かれたリテラルであり、もし間違っていればプログラムは壊れており、最初のテスト実行で止まるべきものだからです。

実行時に届くもの、つまりユーザーが打ち込んだ行、ファイル、ネットワークの応答は、コードを書いているときには見えない形で間違っていることがあります。そこに`try!`を使うと、回復可能な失敗がユーザーの目の前でのクラッシュに変わります。そのような場所では`do`/`catch`か`try?`を使いましょう。

---

関数がスローすると、`throw`の後のすべてがスキップされます。ファイルを閉じるはずだった行やロックを解放するはずだった行も含めてです。`defer`はそれを解決します。ブロックをその場で登録し、現在のスコープがどんな形で終わっても、終わったときに実行します。
```swift
func load() throws {
    print("open")
    defer { print("close") }
    throw FileError.missing
}
```
呼び出しは`open`を出力し、次に`close`を出力し、その後に初めてエラーが呼び出し元へ伝わります。関数が普通に返っていたとしても、`close`は出力されていたはずです。それがポイントです。クリーンアップをセットアップのすぐ隣に置き、コードがどの出口を通るかを心配するのをやめましょう。

---

1つのスコープは複数の`defer`を登録できます。それらは**逆**の順序で実行されます。最後に登録されたものが最初に実行されます。

これは恣意的なルールではありません。クリーンアップは通常、順番に起こったセットアップ、つまりファイルを開いてからロックする、を元に戻します。元に戻すには逆の順序が必要です。ロックを解除し、それから閉じる。逆順は各`defer`をその上の行の鏡像にします。

---

クロージャを受け取る関数には問題があります。渡されたクロージャがスローするかどうかを知り得ないのです。関数を`throws`にすると、無害なクロージャを渡す呼び出し元を含め、すべての呼び出し元に`try`を書くことを強制してしまいます。`rethrows`は*渡されたクロージャがスローするときにのみスローする*という意味です:
```swift
func applyTwice(_ value: Int, _ transform: (Int) throws -> Int) rethrows -> Int {
    return try transform(transform(value))
}
```
本体の中では依然として`try`を書きます。呼び出しは本当に失敗するかもしれないからです。呼び出し側では、コンパイラはあなたが渡したクロージャを見ます:
```swift
let doubled = applyTwice(3, { (n: Int) -> Int in n * 2 }) // try は不要
```
標準ライブラリは至る所でこれを使っています。`map`、`filter`、`sorted(by:)`はすべて`rethrows`です。だから普通の`map`の前に`try`を書くことは決してないのです。

---

`do`ブロックは1つのエラー型に限定されません。各ステップはそれぞれのやり方で失敗することができ、各失敗にはそれぞれの`catch`が対応します:
```swift
do {
    let text = try load(false)
    let value = try parse(text)
    print(value)
} catch NetworkError.offline {
    print("offline")
} catch ParseError.badFormat {
    print("bad format")
} catch {
    print("unknown")
}
```
最初にスローした`try`がブロックを終わらせるので、後のステップは決して実行されません。値はそもそも存在しなかったのです。この形が読みやすいのはそのためです。ハッピーパスが上部で1本のまっすぐな線にとどまり、うまくいかないすべてのやり方がその下に並びます。
