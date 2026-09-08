**String**（文字列）とは、引用符で囲まれた文字の並びであるテキストの一種です。Dartではシングルクォート `'...'` またはダブルクォート `"..."` のどちらも使え、両者はまったく同じように機能します:

```dart
String name = 'Dart';
String other = "Dart";
print(name == other); // true
```

一方のクォートを選ぶことで、テキストの中でもう一方のクォートをエスケープなしで使えます:

```dart
print("It's sunny");   // It's sunny
print('Say "hi"');     // Say "hi"
```

同じ種類のクォートを内部で使う必要がある場合は、バックスラッシュでエスケープします: `'It\'s sunny'`。

---

2つの文字列は `+` 演算子で新しい文字列に連結できます。これを**連結**（concatenation）と呼びます:

```dart
var greeting = 'Hello' + ', ' + 'Dart';
print(greeting); // Hello, Dart
```

Dartでは、演算子を使わずに隣り合って書かれた2つの文字列**リテラル**も連結されます。これは長いテキストを複数行に分けるときに便利です:

```dart
var text = 'Hello, '
    'Dart';
print(text); // Hello, Dart
```

`+` で連結できるのは文字列同士だけです。`'Age: ' + 30` はコンパイルエラーになります。`30` は `int` だからです。

---

文字列を連結する代わりに、**補間**（interpolation）を使って値を直接文字列に挿入できます。変数の値を挿入するには `$name` と書き、任意の式の結果を挿入するには `${expression}` と書きます:

```dart
var name = 'Ana';
var age = 20;
print('$name is $age');             // Ana is 20
print('Next year: ${age + 1}');     // Next year: 21
```

補間はどんな型でも使えます。数値、ブール値、リストは自動的にテキストへ変換されるため、`age` が `int` であっても `'Age: $age'` のように書いて問題ありません。

---

すべての文字列は `.length` プロパティを通じて、自身が持つ文字数を把握しています。スペースや句読点も文字としてカウントされます:

```dart
var word = 'hello';
print(word.length);      // 5
print('a b'.length);     // 3
```

角括弧とその**インデックス**（`0` から始まる）を使って、1文字だけを読み取ることができます。結果は1文字の `String` になります:

```dart
print(word[0]);                // h
print(word[word.length - 1]);  // o
```

文字列の範囲外のインデックス（`word[5]` など）を読み取るとエラーが発生します。

---

Dartの文字列は**イミュータブル**です。一度作成された文字列は決して変化しません。`.toUpperCase()` や `.toLowerCase()` のようなメソッドは元の文字列を変更せず、**新しい文字列を返します**:

```dart
var word = 'Dart';
var loud = word.toUpperCase();
print(loud);  // DART
print(word);  // Dart
```

変数に新しい値を保持させたい場合は、結果を代入し直します: `word = word.toUpperCase();`。

---

ユーザーが入力したテキストには、前後に余分なスペースが入っていることがよくあります。`.trim()` メソッドは、先頭と末尾の空白（スペース、タブ、改行）を取り除いたコピーを返します。`.trimLeft()` と `.trimRight()` はどちらか一方だけを取り除きます:

```dart
var input = '   hello  ';
print('[${input.trim()}]');      // [hello]
print('[${input.trimLeft()}]');  // [hello  ]
```

---

`.substring(start, end)` メソッドは、インデックス `start` からインデックス `end` の直前まで（`end` は**含みません**）の部分文字列を返します。`end` を省略すると、文字列の末尾までのすべてを取得します:

```dart
var text = 'Hello Dart';
print(text.substring(0, 5));  // Hello
print(text.substring(6));     // Dart
```

---

文字列の中を検索するためのメソッドがいくつかあります:

- `.contains(other)` は、`other` が文字列のどこかに現れれば `true` を返します
- `.startsWith(other)` と `.endsWith(other)` は先頭と末尾を調べます
- `.indexOf(other)` は最初に現れた位置のインデックスを返し、見つからない場合は `-1` を返します

```dart
var file = 'report.pdf';
print(file.contains('port'));    // true
print(file.startsWith('rep'));   // true
print(file.endsWith('.txt'));    // false
print(file.indexOf('.'));        // 6
print(file.indexOf('x'));        // -1
```

これらはすべて大文字・小文字を区別します。`'Dart'.contains('dart')` は `false` です。

---

`.replaceAll(from, to)` メソッドは、`from` の**すべての**出現を `to` に置き換えた新しい文字列を返します。`.replaceFirst(from, to)` は最初の1つだけを置き換えます:

```dart
var text = 'a-b-c';
print(text.replaceAll('-', '+'));    // a+b+c
print(text.replaceFirst('-', '+'));  // a+b-c
```

---

`.split(separator)` メソッドは、セパレーターが現れるたびに文字列を切り分けて `List<String>` にします。その逆が `.join(separator)` で、これはリストのメソッドであり、要素を1つの文字列につなぎ合わせます:

```dart
var csv = 'a,b,c';
List<String> parts = csv.split(',');
print(parts);            // [a, b, c]
print(parts.join(' - ')); // a - b - c
```

空のセパレーターで `.split('')` を呼び出すと、1文字ずつのリストが得られます。
