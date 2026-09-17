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

---

一部の文字は引用符の中に直接入力できません。**エスケープシーケンス**はバックスラッシュで始まります: `\n` は改行、`\t` はタブ、`\\` はバックスラッシュ、`\$` はドル記号そのもの（そうしないと `$` は補間を開始してしまいます）です:

```dart
print('one\ntwo');   // oneとtwoを別々の行に出力
print('Cost: \$5');  // Cost: $5
```

**生文字列**（raw string）は `r` を接頭辞として付けます。その中ではバックスラッシュと `$` は単なる文字であり、エスケープも補間も行われません:

```dart
print(r'C:\new\folder'); // C:\new\folder
print(r'Cost: $5');      // Cost: $5
```

複数行にまたがるテキストには、トリプルクォート `'''` または `"""` で区切られた**複数行文字列**を使います。その中の改行はそのまま保持されます。

```dart
var poem = '''
roses are red
violets are blue''';
```

---

内部では、文字列のすべての文字は数値、つまり**コードユニット**（UTF-16コード）として格納されています。`.codeUnitAt(index)` は1文字分のコードを、`.codeUnits` はそのリスト全体を返します。`String.fromCharCode(code)` は逆に、コードから文字列を作成します:

```dart
var word = 'AB';
print(word.codeUnitAt(0));         // 65
print(word.codeUnits);             // [65, 66]
print(String.fromCharCode(67));    // C
```

連続する文字は連続するコードを持ちます。`'A'` は65、`'B'` は66、というように続きます。

---

2つの文字列が `==` で等しくなるのは、まったく同じ文字が同じ順序で含まれている場合です。この比較は**大文字・小文字を区別**し、スペースもすべて考慮されます:

```dart
print('dart' == 'dart');    // true
print('Dart' == 'dart');    // false
print('dart ' == 'dart');   // false
```

大文字・小文字を無視して比較するには、まず両辺を変換します: `a.toLowerCase() == b.toLowerCase()`。順序については、`.compareTo(other)` が、その文字列が相手より前にあるか、等しいか、後にあるかに応じて負の数、`0`、または正の数を返します。

---

文字列はイミュータブルであるため、ループの中で `+=` を使って長いテキストを組み立てると、その都度新しい文字列が作られてしまいます。**StringBuffer** はテキストの断片を効率的に集め、必要になったときにだけ最終的な文字列を生成します:

- `.write(value)` は値を追加します（どんな型もテキストに変換されます）
- `.writeln(value)` は値を追加し、その後に改行を入れます
- `.toString()` はこれまでに組み立てた文字列を返します

```dart
var buffer = StringBuffer();
buffer.write('Hello');
buffer.write(', ');
buffer.writeln('Dart!');
buffer.write(42);
print(buffer.toString()); // Hello, Dart!\n42
```

---

文字列メソッドは文字列を返すため、続けて**チェーン**することができます。`.split('')`、リストのプロパティである `.reversed`、`.join()` を組み合わせることで、1つの式で文字列を反転できます:

```dart
var text = 'Dart';
print(text.split('').reversed.join()); // traD
print(text.toLowerCase().replaceAll('a', '4')); // d4rt
```

**回文**（palindrome）とは、`level` のように前から読んでも後ろから読んでも同じになるテキストのことです。
