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
numbers.insert(2) // 2 はすでに存在する: 何も変わらない
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 は存在しない: 何も変わらない
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
    print(number) // 1, 2, 3 を別々の行に出力
}
```

---

セットは集合論の古典的な演算をサポートします。それぞれが**新しい**セットを返し、元のセットは変更されません：
- `a.union(b)`（和集合）は、`a`、`b`、またはその両方に含まれるすべての要素を含みます
- `a.intersection(b)`（積集合）は、`a`と`b`の**両方**に含まれる要素のみを含みます
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.union(b).sorted())        // [1, 2, 3, 4]
print(a.intersection(b).sorted()) // [3]
```

---

さらに2つの演算があり、これで演算の一群が揃います：
- `a.subtracting(b)`（差集合）は、`a`の要素のうち`b`に**含まれない**ものを含みます
- `a.symmetricDifference(b)`（対称差）は、`a`または`b`のどちらか一方にのみ含まれる要素、つまり**両方には含まれない**要素を含みます
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.subtracting(b).sorted())          // [1, 2]
print(a.symmetricDifference(b).sorted())  // [1, 2, 4]
```
`union`や`intersection`とは異なり、`subtracting`は対称ではありません：`a.subtracting(b)`と`b.subtracting(a)`は通常異なります。

---

セット同士を比較することもできます。これらのメソッドは`Bool`を返します：
- `a.isSubset(of: b)`（部分集合）は、`a`のすべての要素が`b`にも含まれるとき`true`になります
- `a.isSuperset(of: b)`（上位集合）は、`a`が`b`のすべての要素を含むとき`true`になります
- `a.isDisjoint(with: b)`（互いに素）は、`a`と`b`に共通する要素がないとき`true`になります
```swift
let small: Set<Int> = [1, 2]
let big: Set<Int> = [1, 2, 3]
print(small.isSubset(of: big))   // true
print(big.isSuperset(of: small)) // true
print(small.isDisjoint(with: big)) // false
```

---

セットと配列は簡単に互いに変換できます。
配列を`Set(...)`に渡すと、その要素からセットが作られます。これは**重複を取り除く**最も手早い方法です：
```swift
let votes = [3, 1, 3, 2, 1]
let unique = Set(votes) // {1, 2, 3} in some order
```
セットを`Array(...)`に渡すと配列が返りますが、セットには順序がないため、要素は予測できない順序で出てきます。
そのため、順序付けられた結果が必要な場合は、代わりにセットに対して`sorted()`を呼び出すのが一般的です。これはすでに配列を返します：
```swift
let ordered = unique.sorted() // [1, 2, 3]
```
