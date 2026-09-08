**Set（セット）**は、同じ型の値を順序を定めずに格納するコレクションであり、最も重要な点として**重複を許しません**：各値は最大で1回しか現れません。
Setは、値が*何回*登場するか、*どの位置*にあるかではなく、*どの*値が存在するかだけが重要な場合に最適です。
Setは`Set<Element>`という型と、配列と同じ形式のリテラルを使って宣言します：
```swift
let numbers: Set<Int> = [1, 2, 3]
```
この型注釈は必須です。指定しないとSwiftは配列を作成してしまいます。
リテラル内に同じ値が複数回含まれていても、セットはコピーを1つだけ保持します：
```swift
let rolls: Set<Int> = [6, 6, 6]
print(rolls.count) // 1
```
`count`プロパティは、セットが保持する重複のない値の数を教えてくれます。

---

配列と同様に、セットも定数（`let`）または変数（`var`）にできます。作成後に変更できるのは`var`のセットだけです。
空のセットを作成するには型のイニシャライザを呼び出します。空のリテラル`[]`だけでは、Swiftにどの要素型を使うべきか伝わらないためです：
```swift
var visited = Set<String>()
print(visited.isEmpty) // true
```
`isEmpty`プロパティは、配列と全く同じように、セットに要素がないときに`true`になります。

---

セットは同じ値を2回格納することがないため、`count`はリテラルにその値が何回書かれていても、*重複のない*値の数になります。

---

値がセットに含まれているかを確認するには、`Bool`を返す`contains(_:)`メソッドを使います：
```swift
let primes: Set<Int> = [2, 3, 5, 7]
print(primes.contains(5)) // true
print(primes.contains(6)) // false
```
この確認は、要素が数千個あってもセットでは非常に高速です。これは、値の存在確認において配列よりセットを優先すべき主な理由の1つです。

---

`var`のセットは`insert(_:)`と`remove(_:)`で変更できます：
```swift
var numbers: Set<Int> = [1, 2]
numbers.insert(3) // {1, 2, 3}
numbers.insert(2) // 2 is already there: nothing changes
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 is not there: nothing changes
```
すでに存在する値を挿入しても何も起こらず、存在しない値を削除してもエラーにはなりません。
`remove(_:)`はオプショナルとして削除された値を返します（何も削除されなかった場合は`nil`）。これにより、削除が実際に行われたかどうかを確認できます。
セットを完全に空にするには`removeAll()`を呼び出します。

---

セットは`for`-`in`でループできますが、セットには**順序が定義されていない**ことに注意してください：要素はどんな順序でも出てくる可能性があり、その順序は実行ごとに変わることがあります。
順序が重要な場合は、先に`sorted()`を呼び出してください。これはセット自体を変更せずに、要素を昇順に並べた新しい**配列**を返します。
```swift
let numbers: Set<Int> = [3, 1, 2]
for number in numbers.sorted() {
    print(number) // 1, 2, 3 on separate lines
}
```
