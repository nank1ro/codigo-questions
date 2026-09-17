**フォーマット文字列**とは、実行時に一部が値で埋められるテキストのことです。価格、名前、スコアなどが例です。Swiftはこのために2つの手段を提供しています。

1つ目は既に学んだ**文字列補間**です。`\( )`の中に書かれたものはすべて評価され、テキストに挿入されます。変数である必要はなく、任意の式を書けます:
```swift
let price = 4
print("Total: \(price * 3)") // Total: 12
print("Name: \("ada".uppercased())") // Name: ADA
```
補間は文字列を作る最も手軽な方法ですが、数値はSwiftが保持しているとおりにそのまま出力されます。`3.5`は`3.5`のままであり、`3.50`にはなりません。桁数、幅、パディングを完全に制御するには、次の演習で紹介する`String(format:)`を使います。

---

2つ目の手段は`String(format:)`です。これは**Foundation**フレームワークに含まれるため、ファイルは`import Foundation`で始まる必要があります。

挿入する値を**フォーマット文字列**の後に渡します。フォーマット文字列の中では、`%`で始まる**書式指定子**が各値の場所とその書き方を示します。整数の書式指定子は`%d`です:
```swift
import Foundation

let count = 7
let text = String(format: "Item %d", count)
print(text) // Item 7
```
`String(format:)`は通常の`String`を返すので、出力したり、変数に格納したり、関数から返したりできます。

---

小数（`Double`）の書式指定子は`%f`です。これ単体では小数点以下が常に6桁で出力されます:
```swift
print(String(format: "%f", 3.5)) // 3.500000
```
小数の桁数を選ぶには、`%`と`f`の間にドットと数値を書きます。これが**精度**であり、値はそれに合わせて丸められます:
```swift
print(String(format: "%.2f", 3.5))     // 3.50
print(String(format: "%.1f", 3.14159)) // 3.1
print(String(format: "%.0f", 2.71))    // 3
```
`%.2f`は常にちょうど2桁の小数を表示するため、価格にはよく使われます。

---

`%`と文字の間の数値はフィールドの**最小幅**を設定します。値が短ければ左側にスペースが追加されて**右揃え**になり、長ければ何も切り詰められません:
```swift
print(String(format: "%5d|", 42))    //    42|
print(String(format: "%5d|", 12345)) // 12345|
```
幅と精度は組み合わせられます。`%8.2f`は「幅が最低8文字で小数2桁」という意味です:
```swift
print(String(format: "%8.2f|", 3.14159)) //     3.14|
```
固定幅こそがテーブルの列を揃える仕組みです。

---

デフォルトではパディングは左側に入ります。`%`の直後にマイナス記号を置くと、代わりにパディングが右側に入り、値は**左揃え**になります:
```swift
print(String(format: "%-5d|", 42)) // 42   |
print(String(format: "%5d|", 42))  //    42|
```
マイナス記号は**フラグ**です。幅を変えずにフィールドの埋め方を変えます。

---

もう1つのフラグは`0`です。スペースの代わりに、フィールドが左側からゼロで埋められます。これが`007`や`00042`のような数値を作る方法です:
```swift
print(String(format: "%05d", 42))  // 00042
print(String(format: "%03d", 7))   // 007
print(String(format: "%03d", 1234)) // 1234
```
スペースの場合と同様に、幅より長い値が切り詰められることはありません。

---

フォーマット文字列には好きな数だけ書式指定子を置けます。値は同じ順序でカンマ区切りで続き、それぞれが対応する書式指定子の型と一致しなければなりません。`Int`には`%d`、`Double`には`%f`です:
```swift
let count = 3
let weight = 4.5
print(String(format: "%d items, %.1f kg", count, weight)) // 3 items, 4.5 kg
```
`Double`を`%d`に（または`Int`を`%f`に）渡すとコンパイルは通りますが、意味のない数値が出力されるため、書式指定子と値が対応しているかは常に確認してください。

---

整数は他の基数でも書けます。`%x`は値を小文字の**16進数**で、`%X`は大文字で出力し、`%o`は**8進数**で出力します:
```swift
print(String(format: "%x", 255)) // ff
print(String(format: "%X", 255)) // FF
print(String(format: "%o", 8))   // 10
```
幅や`0`フラグもここで機能します。`%02x`は`#ff8000`のような色の1バイトを書く定番の方法です。

---

フォーマット文字列に`String`を挿入するには、書式指定子`%@`を使います:
```swift
let name = "Ada"
let age = 36
print(String(format: "%@ is %d years old", name, age)) // Ada is 36 years old
```
`%@`はSwiftの`String`を直接受け付けます。Swiftの文字列に`%s`は使わないでください。この書式指定子はC文字列を想定しているため、意味不明な出力やクラッシュを引き起こします。

---

`%`は書式指定子の開始を意味するため、リテラルのパーセント記号は`%%`と書かなければなりません。パーセントを書式設定するには次のようにします:
```swift
let ratio = 0.4567
print(String(format: "%.1f%%", ratio * 100)) // 45.7%
```
まず比率に`100`を掛け、それから精度を選びます。`46%`なら`%.0f%%`、`45.7%`なら`%.1f%%`です。

---

幅のフラグは`String(format:)`の中でしか機能しません。普通の文字列を自分でパディングするには、`String(repeating:count:)`でスペースを作り、テキストに連結します:
```swift
let text = "7"
let spaces = String(repeating: " ", count: 4 - text.count)
print(spaces + text + "|") //    7|
```
テキストが既に幅より長い場合、`4 - text.count`は負になり、`String(repeating:count:)`はクラッシュします。`max(0, ...)`で防げば、カウントがゼロ未満にならず、長いテキストはそのまま残されます。

---

Foundationには右側のパディングのための既成のヘルパーもあります: `padding(toLength:withPad:startingAt:)`です。これはパッドテキストを繰り返して文字列を指定の長さまで伸ばし、長すぎる場合は切り詰めます:
```swift
import Foundation

let name = "Ada"
print(name.padding(toLength: 8, withPad: " ", startingAt: 0) + "|") // Ada     |
print("Tea".padding(toLength: 6, withPad: ".", startingAt: 0))     // Tea...
```
`startingAt`はパッドテキスト内で繰り返しが始まるインデックスです。1文字のパッドでは常に`0`です。

---

2つの手段を組み合わせてテーブルを出力しましょう。`padding`は各行のテキストを左揃えにし、`String(format:)`は固定の幅と精度で数値を右揃えにします:
```swift
import Foundation

let items = [("Tea", 2.5), ("Cake", 12.0)]
for (name, price) in items {
    let label = name.padding(toLength: 6, withPad: ".", startingAt: 0)
    print(label + String(format: "%6.2f", price))
}
// Tea...  2.50
// Cake.. 12.00
```
すべての行が同じ幅を持つため、小数点が同じ列に揃います。
