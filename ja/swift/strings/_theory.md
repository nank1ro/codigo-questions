**文字列**とはテキストの断片です。Swiftでは二重引用符の間に文字列リテラルを書き、その型は`String`になります:
```swift
let greeting: String = "Hello"
var city = "Rome"
```
他の値と同様に、`let`は変更できない定数を作り、`var`は変更できる変数を作ります。
Swiftはリテラルから`String`型を推論するので、型注釈は省略可能です。

---

**文字列補間**は、式の値を文字列リテラルの中に挿入します。式は`\()`で囲みます:
```swift
let name = "Ada"
let age = 36
print("\(name) is \(age) years old") // Ada is 36 years old
```
どんな型でも補間できます。数値、ブーリアン、他の文字列はすべて自動的にテキストに変換されます。

---

2つの文字列は`+`演算子で結合でき、新しい文字列が作られます:
```swift
let full = "Hello" + " " + "world" // Hello world
```
既存の文字列変数の末尾にテキストを追加するには`+=`を使います。値が変化するため、その変数は`var`で宣言する必要があります:
```swift
var log = "Start"
log += "..."
print(log) // Start...
```

---

`count`プロパティは文字列に含まれる文字数を返し、`isEmpty`は文字列にまったく文字が含まれていないとき`true`になります:
```swift
print("Swift".count) // 5
print("".isEmpty)    // true
```
スペースや句読点を含め、すべての文字が数えられます。

---

`String`は`Character`値のコレクションです。`Character`は1つの文字、数字、記号、またはスペースであり、文字列と同じ二重引用符で書くため、それを得るには型注釈が必要です:
```swift
let letter: Character = "a"
let text = "abc"
print(text.count) // 3
```
`count`を`0`と比較するより`isEmpty`をチェックする方が好まれます。読みやすく、すべての文字を数える必要もないからです。

---

**複数行文字列リテラル**は、それぞれ独立した行に置かれた3つの二重引用符`"""`で始まり、終わります。その間のすべての行が文字列の一部になり、改行はそのまま保持されます:
```swift
let poem = """
Roses are red
Violets are blue
"""
print(poem)
```
これにより、書かれた通りの2行がそのまま出力されます。閉じる`"""`はインデントも決定します。その前にある空白は、各行の先頭から取り除かれます。

---

文字列は文字のコレクションなので、`for`-`in`ループで反復処理できます。各繰り返しで1つの`Character`が得られます:
```swift
for letter in "hey" {
    print(letter)
}
// h
// e
// y
```
`Character`は`==`で文字リテラルと比較できるので、ある文字が何回登場するかを数えるのは、ループとカウンターだけで済みます。

---

配列と異なり、文字列は`text[2]`のように整数で添字アクセスできません。文字によって使用するメモリ量が異なるため、Swiftは位置を指し示す専用の`String.Index`型を使います。
`startIndex`は最初の文字の位置、`endIndex`は最後の文字の*後ろ*の位置です。インデックスを移動するには`index(_:offsetBy:)`を使い、その結果で文字列に添字アクセスします:
```swift
let word = "Swift"
let second = word.index(word.startIndex, offsetBy: 1)
print(word[second]) // w
```
文字列の末尾を超えて移動すると実行時にクラッシュするため、オフセットは`count`の範囲内に収める必要があります。

---

インデックスを扱うのは冗長なので、Swiftはよくあるケース向けのショートカットを用意しています:
- `first`と`last`は最初と最後の文字をオプショナルの`Character?`として返します（空文字列の場合は`nil`）
- `prefix(n)`は最初の`n`文字を、`suffix(n)`は最後の`n`文字を返します
```swift
let word = "Swift"
print(word.first!)     // S
print(word.prefix(2))  // Sw
print(word.suffix(3))  // ift
```
`prefix`と`suffix`は、元のテキストのビューである`Substring`を返します。本物の`String`として保存するには`String(...)`で包んでください。`n`が`count`より大きい場合は、単に文字列全体が得られます。

---

3つのメソッドが、文字列の内容に関する最もよくある質問に答えてくれます。いずれも`Bool`を返します:
- `contains(_:)`は、指定したテキスト（または文字）がどこかに含まれているとき`true`になります
- `hasPrefix(_:)`は、文字列が指定したテキストで始まるとき`true`になります
- `hasSuffix(_:)`は、文字列が指定したテキストで終わるとき`true`になります
```swift
let email = "ada@example.com"
print(email.contains("@"))          // true
print(email.hasPrefix("ada"))       // true
print(email.hasSuffix(".org"))      // false
```
この3つはすべて大文字と小文字を区別します: `"Swift".hasPrefix("s")`は`false`です。

---

`contains`、`hasPrefix`、`hasSuffix`はブーリアンを返すため、`||`や`&&`と自然に組み合わせて、より複雑な条件を作ることができます。

---

`uppercased()`と`lowercased()`は、すべての文字をそれぞれ大文字または小文字に変換した**新しい**文字列を返します。元の文字列は変更されません:
```swift
let name = "Swift"
print(name.uppercased()) // SWIFT
print(name.lowercased()) // swift
print(name)              // Swift
```
どちらもメソッドなので、括弧を忘れないでください。

---

小文字に変換するのは、大文字と小文字の違いを無視してテキストを比較する一般的な方法です。大文字・小文字だけが異なる2つの文字列は、両方を小文字にすれば等しくなります。

---

`split(separator:)`は、区切り文字が現れるたびに文字列を断片の配列に分割します。`joined(separator:)`はその逆で、配列の要素を1つの文字列につなぎ合わせ、その間に区切り文字を挿入します:
```swift
let parts = "a-b-c".split(separator: "-") // ["a", "b", "c"]
print(parts.count)                         // 3
print(parts.joined(separator: ", "))       // a, b, c
```
`prefix`と同様、`split`は`Substring`値を返します。`String`として保存する必要がある場合は`String(...)`で包んでください。

---

スペースで分割するのは、文を単語に分けるもっとも簡単な方法であり、結合は配列からテキストを組み立て直す方法です。

---

Foundationフレームワークは、多くの追加の文字列メソッドを提供します。もっとも便利なものの1つが`replacingOccurrences(of:with:)`で、最初のテキストのすべての出現箇所を2番目のテキストに置き換えた新しい文字列を返します:
```swift
import Foundation

let path = "a/b/c"
print(path.replacingOccurrences(of: "/", with: "-")) // a-b-c
```
ファイルの先頭で`import Foundation`を忘れないでください。忘れるとこのメソッドは使えません。メソッド呼び出しは連結できるので、`text.lowercased().replacingOccurrences(of: " ", with: "_")`のような書き方も有効です。

---

文字列は数値と同じ演算子で比較できます。`==`は2つの文字列がまったく同じ文字を持つかどうかを調べ、`<`と`>`は1文字ずつ辞書順で比較します:
```swift
print("apple" == "apple")  // true
print("apple" < "banana")  // true
print("car" < "cat")       // true
```
この比較は大文字と小文字を区別し、すべての大文字はすべての小文字より**前**に来ます。そのため`"B" < "a"`は`true`になります。

---

`Character`は`String`ではないため、`+`で直接文字列に結合することはできません。まず`String(...)`で変換してください:
```swift
let letter: Character = "a"
let text = String(letter) + "bc" // abc
```
これを`for`-`in`ループと組み合わせると、たとえば新しい文字をこれまでに集めたものの前に置くなど、1文字ずつ文字列を組み立て直すことができます。
