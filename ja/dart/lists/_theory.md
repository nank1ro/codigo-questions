Dartにおいて、**リスト**は要素の順序付きコレクションです。リストを作成する最も簡単な方法は `[]` リテラル構文です：

```dart
List<int> numbers = [1, 2, 3];
```

`var` による型推論も使用できます：

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

型アノテーション `List<String>` は、リストのすべての要素が `String` でなければならないことをDartに伝えます。

---

Dartのリストは**ゼロインデックス**です。つまり、最初の要素はインデックス `0`、2番目はインデックス `1`、というようになります。

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

インデックスによる要素へのアクセスは `list[index]` 構文で行います。

---

`.add()` メソッドはリストの**末尾**に1つの要素を追加します：

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

`.add()` はリストを**その場で**変更し、`void` を返すことに注意してください。

---

`.length` プロパティはリスト内の要素数を返します：

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

空のリストの長さは `0` です：

```dart
var empty = [];
print(empty.length); // 0
```

---

`.contains()` メソッドはリストに指定した値が含まれているかどうかを確認します。見つかった場合は `true`、そうでない場合は `false` を返します：

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

これはループを使わずにメンバーシップの確認をするのに便利です。

---

`.remove(value)` メソッドは、リストから `value` と等しい**最初の**要素を削除します。要素が削除された場合は `true`、値が見つからなかった場合は `false` を返します。

```dart
var colors = ['red', 'green', 'blue'];
bool removed = colors.remove('green');
print(removed); // true
print(colors); // [red, blue]
```

---

`.first` と `.last` プロパティは、インデックスを使わずにリストの最初と最後の要素を取得します。

```dart
var colors = ['red', 'green', 'blue'];
print(colors.first); // red
print(colors.last); // blue
```

どちらもリストが空の場合はエラーをスローします。

---

`.isEmpty` プロパティはリストに要素がない場合に `true` になり、`.isNotEmpty` は少なくとも1つの要素がある場合に `true` になります。

```dart
var colors = <String>[];
print(colors.isEmpty); // true
colors.add('red');
print(colors.isNotEmpty); // true
```

---

`.indexOf(value)` メソッドは、`value` と等しい最初の要素のインデックスを返します。値がリストに存在しない場合は `-1` を返します。

```dart
var colors = ['red', 'green', 'blue'];
print(colors.indexOf('green')); // 1
print(colors.indexOf('pink')); // -1
```

---

`.where()` メソッドは、関数が `true` を返す要素だけを残します。新しいリストではなく遅延評価の `Iterable` を返すため、結果を `List` に戻すには `.toList()` を呼び出す必要があります。

```dart
var numbers = [1, 2, 3, 4];
List<int> big = numbers.where((n) => n > 2).toList();
print(big); // [3, 4]
```
