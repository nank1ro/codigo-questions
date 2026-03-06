**辞書（Dictionary）**は配列やタプルに似ていますが、インデックスの代わりに*キー*を使って値にアクセスします。
キーには任意の文字列や数値を使用できます。
辞書は角括弧で囲んで、次のように宣言します:
```swift
var dictionaryName: [String: Int] = ["key1": 1, "key2": 2, "key3": 3]
```
これは3つの*キーと値のペア*を持つ`dictionaryName`という辞書です。
キー`key1`は値`1`を、`key2`は`2`を指し示します。

---

キーを使って辞書の値にアクセスする方法は、インデックスを使って配列の値にアクセスする方法と同じです:
```swift
// gets the age value from the user dictionary
user['age']
```

---

配列と同様に、辞書は_変更可能（mutable）_です。
つまり、作成後に変更できます（定数として宣言されていない場合）。
この利点の一つとして、作成後に新しい_キーと値のペア_を次のように追加できます:
```swift
dictName[newKeyName] = newValue
```

---

辞書の`count`は、辞書が持つ_キーと値のペア_の数です。
値が配列であっても、各ペアは1回だけカウントされます。（そうです、辞書の中に配列を入れることもできます！）

---

辞書は変更可能なので、様々な方法で変更できます。`removeValue(forKey:)`メソッドを使って辞書から要素を削除できます:
```swift
if let removedValue = dictName.removeValue(forKey: "keyName") {
    print("The removed value is \(removedValue).") // prints the removed value, if the key exists
}
```
これにより、辞書からキー`keyName`とそれに関連付けられた値が削除されます。

---

辞書のすべてのキーを一覧表示するにはどうすればよいでしょうか？
`keys`プロパティを使います。

---

辞書のすべての値を一覧表示するにはどうすればよいでしょうか？
`values`プロパティを使います。

---

配列と同様に、`for..in`キーワードを使って辞書の要素をループ処理できます。
ループでキーと値の両方を取得するには、プロパティを指定する必要はありません:
```swift
for (key, value) in dictName {
    print("\(key): \(value)")
}
```

---

配列で使った`isEmpty`プロパティを使って、辞書が空かどうかを判定することもできます

---

辞書に値を__追加__または__変更__するには、`updateValue(_:forKey:)`メソッドも使用できます

---

以前、`removeValue()`メソッドを使って辞書から_キーと値のペア_を削除する方法を見ました。
キーに`nil`値を代入することで要素を削除することもできます
```swift
dictName[keyName] = nil
// keyNameが辞書dictNameから削除されます
```
