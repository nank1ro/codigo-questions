リストは、1つの変数名の下にさまざまな情報をシーケンスとして格納するために使用できるデータ型です。
リストは1つまたは複数の型の複数の値を格納し、**インデックス**を使用してこれらの値を区別します。
次の形式の式でリストに要素を割り当てることができます：
```kotlin
val listName = listOf<itemsType>(item1, item2)
```
`itemsType`はリスト内の要素の型を表します。例えば、`Int`、`String`、`Any`などが使用できます...

---

リストは特定の順序を持つ要素のコレクションです。Kotlinには2種類のリストがあります：

- `List`は作成後に変更できません。
- `MutableList`は作成後に変更でき、要素の追加、削除、更新ができます。

```kotlin
val numbers = listOf(1, 3, 5)
numbers.add(7) // [1]
```
__[1]__ `List`は_読み取り専用_なので、エラーがスローされます。

変更可能なリストを作成するには`mutableListOf`キーワードを使用します
```kotlin
val numbers = mutableListOf(1, 3, 5)
numbers.add(7)
println(numbers)
// prints [1, 3, 5, 7]
```

---

リストの個々の要素にはインデックスでアクセスできます。
インデックスはリスト内の要素の位置を識別するアドレスのようなものです。
インデックスはリスト名の直後に角括弧の中に記述します：
```kotlin
listName[index]
```

リストのインデックスは`0`から始まり、`1`からでは**ありません**！リストの最初の要素には次のようにアクセスします：`listName[0]`または`listName.get(0)`、あるいは`listName.first()`。
リストの2番目の要素はインデックス__1__にあります：`listName[1]`。

---

インデックスは実際には最初の要素からのオフセットです。例えば、`list[2]`と書いた場合、リストの2番目の要素を要求しているのではなく、最初の要素から2つ分オフセットされた要素を要求しています。したがって、`list[0]`は最初の要素（オフセット0）、`list[1]`は2番目の要素（オフセット1）、`list[2]`は3番目の要素（オフセット2）、というようになります。

リストのインデックスはアクセスだけでなく、値の代入にも使用できます。
リストのインデックスへのアクセス方法は次のとおりです：
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
println(names[0])
```
代入は次のように行います：
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel")
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
println(names[0])
```

---

文字列と同様に、リストには`size`ゲッターで取得できる**長さ**があります。
リストの長さは、そのリストが含む要素の数です。

---

もう一つの便利なリスト操作は、指定された要素がリストに含まれているかどうかを調べる`contains`メソッドです。
例えば、名前のリストがある場合、`contains`メソッドを使って指定された名前がリストに存在するかどうかを確認できます。
```kotlin
val names = listOf("Thomas", "Donald", "Scarlett")
println(names.contains("Scarlett"))
// prints true
```

---

変更可能なリストは固定長である必要はありません。
いつでもリストの末尾に要素を追加できます！
変更可能なリストに要素を追加するには、`add`関数または`+=`ショートカットを使用します：
```kotlin
val letters = mutableListOf("a", "b")
letters.add("c")
println(letters)
// prints [a, b, c]
```

---

前の例で見たように、`add`関数を使って要素を1つずつ追加できます。
しかし、別のリストのすべての要素を一度に追加する場合は、`addAll`関数または`+=`ショートカットを使用できます：
```kotlin
val letters = mutableListOf("a", "b")
val newLetters = listOf("c", "d", "e")
letters.addAll(newLetters)
println(letters)
// prints [a, b, c, d, e]
```

---

リストの一部分だけにアクセスしたい場合があります。
次のコードを考えてみましょう：
```kotlin
val numbers = listOf(1, 2, 3, 4) // [1]
val slice = numbers.slice(1..2) // [2]
println(slice)
// prints [2, 3]
```
__[1]__：まず、`numbers`という_読み取り専用_リストを作成します。
__[2]__：次に、`slice`関数を使用してリストの一部を取得し、sliceリストに格納します。
`slice`関数の中に含めたいインデックスを定義してこれを行います。

Kotlinでは、`..`を使用して最後のインデックスを含めることができますが、`until`を使用して最後のインデックスを除外することもできます。

---

`Any`型を指定すると、リストの要素はどんな型でも持てます：
```kotlin
var listName: List<Any> = listOf("one", 2, true)
```
実際、上記では`String`、`Integer`、`Boolean`が順番に含まれています。
しかし、リストの中にリストを含めることもできます！

---

リスト内のアイテムを検索する必要がある場合があります。
Kotlinでは`indexOfFirst`メソッドを使用できます：
```kotlin
val names = mutableListOf("Trevor", "Zac", "Glenn")
println(names.indexOfFirst { it == "Zac"})
// prints 1
```

`indexOfFirst`メソッドは__述語__関数を受け取り、リスト内の各アイテムに対してtrueになるまで評価され、その要素の_インデックス_を返します。
上記のコードは文字列`"Zac"`を含む最初のインデックスを出力します。この場合は`1`です。

また、`add(index, element)`メソッドを使用して、変更可能なリストの特定のインデックスにアイテムを挿入することもできます：
```kotlin
names.add(1, "Ali")
// prints [Trevor, Ali, Zac, Glenn]
```
上記のコードはインデックス`1`に`"Ali"`を挿入し、このインデックス以降のすべての要素を1つ下にずらします

---

Kotlinでは`for..in`キーワードを使用して、非常にシンプルな方法でリストをループすることができます：
```kotlin
val numbers = listOf(1, 2, 3)
for (num in numbers) {
    println(num)
}
// prints 1, 2, 3
```
`for`キーワードの後に変数名が続き、リストの各アイテムの値が順番に割り当てられます。
