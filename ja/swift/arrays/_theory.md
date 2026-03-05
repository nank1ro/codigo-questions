配列は、複数の異なる情報を1つの変数名のもとにシーケンスとして格納するためのデータ型です。
配列は1つまたは複数の型の値を格納し、**インデックス**を使ってそれらの値を区別します。
以下の形式の式で配列に要素を割り当てることができます：
```swift
var arrayName: [itemsType] = [item1, item2]
```
`itemsType`は配列内の要素の型を表し、例えば`Int`、`String`、`Any`などが使えます。

---

配列の個々の要素にはインデックスを使ってアクセスできます。
インデックスは、配列内の要素の位置を識別するアドレスのようなものです。
インデックスは配列名の直後に角括弧で囲んで記述します：
```swift
arrayName[index]
```

配列のインデックスは`1`では**なく**`0`から始まります！配列の最初の要素には次のようにアクセスします：`arrayName[0]`。
配列の2番目の要素はインデックス1にあります：`arrayName[1]`。

---

配列のインデックスは他の変数名と同じように動作します。
値のアクセスだけでなく、値の代入にも使用できます。
配列のインデックスにアクセスする方法は次の通りです：
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
print(names[0])
```
代入は次のように行います：
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
print(names[0])
```

---

文字列と同様に、配列には**長さ**`count`があります。
配列の長さは、配列に含まれる要素の数です

---

配列は固定長である必要はありません。
いつでも配列の末尾に要素を追加できます！
配列に要素を追加するには`append`関数を使います：
```swift
var letters = ["a", "b"]
letters.append("c")
print(letters)
// Prints ["a", "b", "c"]
```

---

配列の一部だけにアクセスしたい場合があります。
次のコードを見てください：
```swift
let numbers = [1, 2, 3, 4]
let slice = numbers[1...2]
print(slice)
// prints [2, 3]
```
まず、`numbers`という配列を作成します。
次に、配列の一部を取り出してslice配列に格納します。
これは配列名の後に含めたいインデックスを指定することで行います：`numbers[1...2]`。
Swiftでは`...`を使って最後のインデックスを含めることができますが、`..<`を使って最後のインデックスを除外することもできます

---

Swiftでは配列を自由にスライスできます！
```swift
// Grabs the first two items
listName[..<2]
// Grabs the fourth through last items
listName[3...]
```
配列スライスに配列の最初または最後の要素が含まれる場合、その要素のインデックスを含める必要はありません

---

`Any`型を指定すると、配列の要素は任意の型にすることができます：
```swift
var arrayName: [Any] = ["one", 2, true]
```
実際、上の例では順に文字列、整数、ブール値が含まれています。
また、配列の中に配列を入れることもできます！

---

配列内の要素を検索する必要がある場合があります。
Swiftでは`firstIndex()`メソッドを使うことができます：
```swift
var names: [String] = ["Trevor", "Zac", "Glenn"]
if let index = names.firstIndex(of: "Zac") {
  print(index)
}
// prints 1
```
上のコードは、文字列`"Zac"`を含む最初のインデックス（この場合は`1`）を出力します。
また、`insert()`メソッドを使って特定のインデックスに要素を挿入することもできます：
```swift
names.insert("Ali", at: 1)
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
上のコードはインデックス`1`に`"Ali"`を挿入し、このインデックス以降のすべての要素を1つ後ろにずらします

---

Swiftでは`for..in`キーワードを使って非常に簡単に配列をループ処理できます：
```swift
var numbers = [1, 2, 3]
for num in numbers {
    print(num)
}
// prints 1, 2, 3
```
`for`キーワードの後に変数名が続き、配列の各要素の値が順番に代入されます。

---

**タプル**は配列に似ていますが、要素に名前を付けてその名前で参照することができます。
タプルを作成するには丸括弧`()`を使います
```swift
var person = (firstName: "John", lastName: "Smith")
var firstName = person.firstName // John
var lastName = person.lastName // Smith
```
