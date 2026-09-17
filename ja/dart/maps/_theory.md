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
ages['Bob'] = 25; // Bobを追加
ages['Ann'] = 31; // Annを更新
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

---

空のマップリテラル `{}` には型を推論するためのペアがないため、`<K, V>{}` または型アノテーションで明示的に型を指定してください：

```dart
var cart = <String, int>{};
Map<String, int> other = {};
```

`.isEmpty` プロパティは、マップにペアが1つもないときに `true` になり、`.isNotEmpty` は少なくとも1つあるときに `true` になります：

```dart
print(cart.isEmpty); // true
cart['pen'] = 2;
print(cart.isNotEmpty); // true
```

---

`.forEach()` メソッドは、すべてのペアに対して1回ずつ関数を実行します。この関数はキーと値の2つの引数を受け取ります：

```dart
var ages = {'Ann': 30, 'Bob': 25};
ages.forEach((name, age) {
  print('$name is $age');
});
// Ann is 30
// Bob is 25
```

---

マップは `Iterable` ではないため、`for-in` で直接ループすることはできません。代わりに `.entries` をループします。各要素は `.key` と `.value` を持つ `MapEntry` です：

```dart
var ages = {'Ann': 30, 'Bob': 25};
for (var entry in ages.entries) {
  print('${entry.key}: ${entry.value}');
}
// Ann: 30
// Bob: 25
```

---

`.putIfAbsent(key, ifAbsent)` メソッドは、キーがまだマップにない場合に**限り**ペアを追加します。第2引数は値を生成する関数です。キーがすでに存在する場合、マップは変更されません。どちらの場合も、そのキーの下に現在格納されている値が返されます：

```dart
var ages = {'Ann': 30};
ages.putIfAbsent('Ann', () => 99); // Annはすでに存在する、何も変わらない
ages.putIfAbsent('Bob', () => 25); // Bobが追加される
print(ages); // {Ann: 30, Bob: 25}
```

---

`.update(key, update)` メソッドは、既存のキーの値を置き換えます。第2引数は現在の値を受け取り、新しい値を返す関数です。キーが存在しない場合、`.update()` はエラーをスローしますが、初期値を生成する `ifAbsent` 関数を渡せば例外です：

```dart
var stock = {'apple': 3};
stock.update('apple', (n) => n + 1); // appleは4になる
stock.update('kiwi', (n) => n + 1, ifAbsent: () => 1); // kiwiが1で追加される
print(stock); // {apple: 4, kiwi: 1}
```
