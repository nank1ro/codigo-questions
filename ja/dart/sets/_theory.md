**Set**（セット）は**一意の**値のコレクションです：同じ値は最大で一度しか出現できません。マップと同様に、セットも `{}` リテラル構文で作成しますが、`key: value` のペアではなく単純な値を格納します：

```dart
Set<int> numbers = {1, 2, 3};
print(numbers); // {1, 2, 3}
```

型アノテーション `Set<int>` は、すべての要素が `int` であることをDartに伝えます。リストやマップと同様に、`var` はリテラルから型を推論します：

```dart
var colors = {'red', 'green'}; // Set<String>
```

---

セットは同じ値を二度と保存しません。リテラルに重複があった場合、最初に現れたものだけが保持され、それ以外は実行時にエラーなく破棄されます（アナライザは値を繰り返すリテラルについて警告を出します）：

```dart
var letters = {'a', 'b', 'a', 'b', 'c'};
print(letters); // {a, b, c}
```

`.length` プロパティは、セットが保持する**一意の**要素の数を返します：

```dart
print(letters.length); // 3
```

---

`.add(value)` メソッドは値を1つ挿入します。値が追加された場合は `true` を、すでにセットに存在していた場合は `false` を返し、その場合は何も変わりません。`.addAll(iterable)` メソッドはリストや別のセットのすべての要素を挿入しますが、こちらもすでに存在する要素はスキップします：

```dart
var tags = {'dart'};
tags.add('web');    // true
tags.add('dart');   // false、すでに存在する
tags.addAll(['web', 'mobile']);
print(tags); // {dart, web, mobile}
```

空の `{}` リテラルは**セット**ではなく**マップ**になります。空のセットを作るには型を指定してください：

```dart
var empty = <String>{};
Set<int> other = {};
```

---

`.remove(value)` メソッドはセットから値を削除します。値が存在した場合は `true` を、存在しなかった場合は `false` を返します：

```dart
var numbers = {1, 2, 3};
print(numbers.remove(2)); // true
print(numbers.remove(9)); // false
print(numbers); // {1, 3}
```

すべての要素を一度に削除するには `.clear()` を使います。

---

セットに値が含まれているかを調べるには、`bool` を返す `.contains(value)` を使います。`.isEmpty` プロパティはセットに要素がない場合に `true`、`.isNotEmpty` は少なくとも1つ要素がある場合に `true` になります：

```dart
var seen = {'x', 'y'};
print(seen.contains('x')); // true
print(seen.contains('z')); // false
print(seen.isEmpty);       // false
print(seen.isNotEmpty);    // true
```

---

Dartのデフォルトのセットは**挿入順**を記憶します：出力したり反復処理したりすると、要素は最初に追加された順序で出てきます。すでに存在する値を追加しても、その位置は移動しません：

```dart
var numbers = {3, 1, 3, 2};
print(numbers); // {3, 1, 2}
```

---

セットは `Iterable` なので、リストと同様に `for-in` で直接その要素を反復処理できます。インデックスは存在せず、要素は挿入順に訪問されます：

```dart
var numbers = {3, 1, 4};
for (var n in numbers) {
  print(n);
}
// 3
// 1
// 4
```

---

セットは古典的な集合演算をサポートしています。それぞれ**新しい**セットを返し、元のセットは変更されません：

- `a.union(b)` は `a` **または** `b` に含まれる要素を持ちます
- `a.intersection(b)` は `a` と `b` の**両方**に含まれる要素を持ちます
- `a.difference(b)` は `a` の要素のうち `b` に**含まれない**ものを持ちます

```dart
var a = {1, 2, 3};
var b = {2, 3, 4};
print(a.union(b));        // {1, 2, 3, 4}
print(a.intersection(b)); // {2, 3}
print(a.difference(b));   // {1}
```

---

リストをセットに変換することは、**重複を取り除く**最も簡単な方法です：すべてのリストは `.toSet()` メソッドを持ち、最初に現れた順序で一意の要素を持つセットを返します。セットには逆方向の変換を行う `.toList()` メソッドがあるので、この2つを連結すれば重複のないリストが得られます：

```dart
var votes = ['a', 'b', 'a', 'c', 'b'];
Set<String> unique = votes.toSet();
print(unique); // {a, b, c}
List<String> cleaned = votes.toSet().toList();
print(cleaned); // [a, b, c]
```

---

リストとセットはどちらも `.contains()` メソッドを持っていますが、その動作は大きく異なります。リストは要素を先頭から1つずつ確認するため、長いリストでの検索はリストが大きくなるほど遅くなります。セットはハッシュによって要素を格納するため、要素数に関わらず `.contains()` はほぼ一定時間で値を見つけます。

メンバーシップを何度もチェックする必要があり、順序や重複が問題にならない場合は、セットが適したツールです：

```dart
var banned = {'spam', 'scam'};
print(banned.contains('spam')); // 高速、要素が何百万あっても
```
