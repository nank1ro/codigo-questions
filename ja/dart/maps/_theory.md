**マップ**は**キーと値のペア**のコレクションです。それぞれの値は一意のキーの下に格納され、そのキーを使って値を再び見つけることができます。マップは `{}` リテラル構文で作成し、各ペアを `key: value` の形式で記述します：

```dart
Map<String, int> ages = {'Ann': 30, 'Bob': 25};
print(ages); // {Ann: 30, Bob: 25}
```

型アノテーション `Map<String, int>` は、すべてのキーが `String` で、すべての値が `int` であることをDartに伝えます。リストと同様に、`var` はリテラルから型を推論します：

```dart
var capitals = {'Italy': 'Rome', 'France': 'Paris'};
```

---

値を読み取るには、リストのインデックスと同じように、角括弧内にキーを指定します：

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages['Ann']); // 30
```

キーがマップに存在しない場合、その検索は**エラーをスローせず**、`null` を返します。そのため `ages['Ann']` の型は `int` ではなく `int?`（null許容の `int`）になります：

```dart
print(ages['Zed']); // null
```

---

`map[key] = value` で代入すると、キーがまだマップにない場合は新しいペアを**追加**し、既存のキーの場合はその値を**更新**します：

```dart
var ages = {'Ann': 30};
ages['Bob'] = 25; // adds Bob
ages['Ann'] = 31; // updates Ann
print(ages); // {Ann: 31, Bob: 25}
```

新しいキーは既存のキーの後に追加されるため、マップは挿入順を記憶します。

---

`.remove(key)` メソッドは、マップからキーとその値を削除します。削除された値を返しますが、キーが存在しなかった場合は `null` を返します：

```dart
var ages = {'Ann': 30, 'Bob': 25};
int? removed = ages.remove('Ann');
print(removed); // 30
print(ages); // {Bob: 25}
```

`.length` プロパティは、キーと値のペアの数を返します：

```dart
print(ages.length); // 1
```

---

マップが特定のキーを持っているかを確認するには `.containsKey(key)` を使います。特定の値を持つペアがあるかを確認するには `.containsValue(value)` を使います。どちらも `bool` を返します：

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages.containsKey('Ann')); // true
print(ages.containsKey('Zed')); // false
print(ages.containsValue(25)); // true
```

---

存在しないキーを読み取ってもエラーにはならないため、検索結果が `null` になる可能性を常に考慮してください。安全なパターンとして `??` 演算子でフォールバックを用意する方法があります：

```dart
var ages = {'Ann': 30};
int age = ages['Zed'] ?? 0;
print(age); // 0
```

---

`.keys` プロパティはマップのすべてのキーを、`.values` はすべての値を、挿入順に返します。これらは遅延評価の `Iterable` なので、実際の `List` が必要な場合は `.toList()` を呼び出してください：

```dart
var ages = {'Ann': 30, 'Bob': 25};
List<String> names = ages.keys.toList();
List<int> years = ages.values.toList();
print(names); // [Ann, Bob]
print(years); // [30, 25]
```
