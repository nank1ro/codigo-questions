`Set`は、異なる情報の集まりを1つの変数名のもとにシーケンスとして格納できるデータ型です。
`List`との主な違いは、`Set`では各値の要素を1つしか持てないことです。

`List`と同様に、`Set`は1つまたは複数の型の値を格納し、**インデックス**を使ってこれらの値を区別します。
以下の形式の式でセットに要素を代入できます：
```kotlin
val setName = setOf<itemsType>(item1, item2)
```
`itemsType`はセット内の要素の型を表します。例えば、`Int`、`String`、`Any`などです。

---

`Set`は、特定の順序を持たない__一意な__要素のコレクションです。

```kotlin
val numbers = setOf(1, 1, 2) // [1]
println(numbers)
// prints [1, 2]
```

__[1]__では数値__1__を2回含むセットを作成しようとしていますが、各要素は一意でなければならないため、2番目の__1__は自動的に破棄されます。

---

Kotlinには2種類の`Set`があります：

- `Set`は作成後に変更できません。
- `MutableSet`は作成後に変更でき、要素の追加、削除、更新が可能です。

```kotlin
val numbers = setOf(1, 2, 3)
numbers.add(4) // [1]
```
__[1]__は`Set`が_読み取り専用_であるため、エラーをスローします。

変更可能なセットを作成するには`mutableSetOf`キーワードを使用します
```kotlin
val numbers = mutableSetOf(1, 2, 3)
numbers.add(4)
println(numbers)
// prints [1, 2, 3, 4]
```

---

`Set`の最も一般的な操作は、`in`または`contains()`を使ったメンバーシップのテストです。

```kotlin
val numbers = setOf(1, 2, 3)
println(2 in numbers) // prints true
println(numbers.contains(5)) // prints false
```

上記のように、`in`と`contains`は渡された要素がセットに存在するかどうかを示す`Bool`を返します。

---

`Set`の要素の順序は重要ではありません。
実際、同じ要素を異なる順序で持つ2つの`Set`を比較すると、等しいという結果が得られます。

---

`Set`では、和集合、積集合、差集合、部分集合の確認など、いくつかの操作を実行できます。

```kotlin
val firstNumbers = setOf(1, 2, 3)
val lastNumbers = setOf(3, 4, 5)
val union = firstNumbers.union(lastNumbers) // [1, 2, 3, 4, 5]
val intersection = firstNumbers intersect lastNumbers // [3]
val difference = firstNumbers subtract lastNumbers // [1, 2]
val subset = firstNumbers.containsAll(lastNumbers) // false
```

---

`Set`を`List`に変換するには、`toList()`関数を使用できます。
