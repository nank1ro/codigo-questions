`String name = 'Ada';` のように型を指定して変数を宣言する方法はすでに知っていますね。しかし、値が単に**存在しない**こともあります。ニックネームのないユーザー、何も見つからなかった検索、数値に変換できない文字列などです。Dartでは、存在しない値を `null` で表します。

Dart 2.12 以降、この言語には**健全なnull安全（sound null safety）**があります。`String` のような通常の型は**決して** `null` を保持できません。代入しようとするとコンパイルエラーになり、プログラムは実行すらされません：

```dart
String name = null; // error: a value of type 'Null' can't be assigned to 'String'
```

値が存在しないことを許すには、型のうしろにクエスチョンマーク `?` を付けます。`String?` は `String` か `null` のどちらかを保持し、`null` を出力すると `null` という語が表示されます：

```dart
String? nickname = null;
print(nickname); // null

nickname = 'Ada';
print(nickname); // Ada
```

`?` の付かない型は**非null許容（non-nullable）**、`?` の付いた型は**null許容（nullable）**と呼ばれます。

---

**値を指定せずに**宣言されたnull許容の変数は `null` から始まるので、`= null` は省略できます：

```dart
int? age;
print(age); // null
```

非null許容の変数にはそのような既定値はありません。値が代入される前にそれを読み取るコードを、Dartはコンパイルしません。

```dart
int count;
print(count); // error: 'count' must be assigned before it can be used
```

---

`null` に対してメソッドを呼んだりプロパティを読んだりするとクラッシュするため、Dartは通常のドットを使ってnull許容の値にそれを行うことを許しません：

```dart
String? text;
print(text.length); // error: the property 'length' can't be unconditionally accessed
```

**null安全アクセス**演算子 `?.` がこれを解決します。値が `null` なら式全体が `null` になり、それ以上は評価されません。そうでなければ通常の `.` と同じように動きます：

```dart
String? text = 'Dart';
print(text?.length); // 4

text = null;
print(text?.length); // null
```

結果が `null` になりうるため、その型はnull許容です。`text?.length` は `int` ではなく `int?` です。

---

存在しない値は、**既定値**で置き換えたいことがよくあります。**if-null** 演算子 `??` は、左のオペランドが `null` でなければそれを返し、そうでなければ右のオペランドを返します：

```dart
String? nickname;
print(nickname ?? 'anonymous'); // anonymous

nickname = 'Ada';
print(nickname ?? 'anonymous'); // Ada
```

`??` が反応するのは `null` だけです。空文字列 `''` や数値 `0` は実在する値なので、そのまま保持されます。

`?.` はnull許容の結果を生むので、`??` は `?.` とうまく組み合わせられます：

```dart
String? text;
print(text?.length ?? 0); // 0
```

---

null安全の大きな利点は、`null` に関するほとんどの間違いを、ユーザーではなく**コンパイラ**が見つけてくれることです。ここまでのルール：

- 非null許容の型（`String`、`int`、`List<int>`...）は決して `null` になれない
- null許容の型（`String?`、`int?`、`List<int>?`...）はなれる。値を指定せずに宣言すると `null` から始まる
- null許容の値に `.` を使うとコンパイルできない。`?.` を使うか、`??` で既定値を与える

---

**if-null代入**演算子 `??=` は、変数が現在 `null` の**場合にのみ**値を代入します。そうでなければ変数はそのままです：

```dart
int? retries;
retries ??= 3;
print(retries); // 3

retries ??= 10;
print(retries); // 3, it already had a value
```

キーが存在しないことがあるためnull許容であるmapの要素に対しても使えます：

```dart
var stock = {'apple': 4};
stock['pear'] ??= 1;  // added
stock['apple'] ??= 9; // ignored
print(stock); // {apple: 4, pear: 1}
```

---

コンパイラには判断できなくても、ある地点でnull許容の値が `null` でないと**あなた**にはわかっていることがあります。**null断定**演算子 `!` は、値が存在すると約束することで `String?` を `String` に変えます：

```dart
String? text = 'Dart';
String sure = text!;
print(sure.length); // 4
```

注意してください。`!` はチェックをコンパイル時から実行時へ移します。値が**実際に** `null` だった場合、プログラムはエラーを投げて停止します：

```dart
String? text;
print(text!.length); // Null check operator used on a null value
```

`!` は控えめに、そこに `null` が来ること自体がバグである場合にだけ使ってください。

---

null許容の値に対して見てきた3つの演算子の違いを覚えておきましょう：

- `?.` は値が `null` のとき `null` を返し、決してエラーを投げない
- `??` は `null` を既定値で置き換える
- `!` は値が存在すると仮定し、存在しないときは**実行時にエラーを投げる**

どれもコンパイルエラーにはなりません。コンパイラはあなたの `!` を信用するので、約束が破られたことは実行中のプログラムだけが知ることになります。

---

null許容の値を `if` でチェックするのは `!` より安全で、Dartはそれに報いてくれます。`if (x != null)` のようなチェックのあと、コンパイラはそのブロック内で `x` が `null` になりえないと知っているので、そこでは `x` を非null許容として扱います。これを**型プロモーション**と呼びます：

```dart
int twice(int? n) {
  if (n != null) {
    return n * 2; // here n is an int, no ! needed
  }
  return 0;
}
```

早期リターンのあとでもプロモーションは働きます：

```dart
int twice(int? n) {
  if (n == null) return 0;
  return n * 2; // n is an int from here on
}
```

プロモーションが適用されるのは**ローカル変数と引数**です。これらの値は、チェックと使用の間に知らないうちに変わることがありません。

---

型プロモーションは、外部から変更されうるクラスの**フィールド**には**働きません**。チェックと使用の間に、別のコード（サブクラスでオーバーライドされたゲッターや別のメソッド）がそれを `null` に戻してしまう可能性があるからです：

```dart
class Box {
  int? value;

  int doubled() {
    if (value != null) {
      return value * 2; // error: 'value' can't be unconditionally accessed
    }
    return 0;
  }
}
```

定石は、フィールドを**ローカル変数**にコピーすることです。ローカル変数はプロモーションされます：

```dart
int doubled() {
  final v = value;
  if (v != null) {
    return v * 2;
  }
  return 0;
}
```

---

非null許容のフィールドは通常、コンストラクタで値を受け取らなければなりません。値が**あとになって**（ファイルを読んだあと、接続を開いたあとなど）はじめて分かる場合は、フィールドに `late` を付けられます。コンパイラは初期化子がないことを受け入れ、読み取る前にあなたが値を代入すると信頼します。

```dart
class Connection {
  late String host;

  void open() {
    host = 'example.com';
  }
}
```

まだ代入されていない `late` フィールドを読むと、実行時に `LateInitializationError` が投げられます。`!` と同じく `late` はコンパイル時の保証を実行時のチェックと引き換えにするので、あなたが守るべき約束になります。

`late` は初期化子と組み合わせることもでき、その場合、初期化子は変数が最初に読まれたときに**遅延して**実行されます：

```dart
late String report = buildReport(); // buildReport() runs only when report is used
```

---

null許容性は**名前付き引数**の宣言の仕方にも関わります。null許容の型を持つ名前付き引数は省略可能で、呼び出し側が省略すると単に `null` になります。

```dart
String label({String? title}) => title ?? 'untitled';

print(label());               // untitled
print(label(title: 'Notes')); // Notes
```

非null許容の型で既定値もない名前付き引数は、省略されると値がなくなってしまうため、Dartは `required` を付けることを要求します。呼び出し側は必ずそれを渡さなければなりません：

```dart
String label({required String name, String? title}) { ... }

label(name: 'Ada');               // ok
label(name: 'Ada', title: 'Dr.'); // ok
label(title: 'Dr.');              // error: the named parameter 'name' is required
```

---

null許容性はコレクションの**要素**にも当てはまります。`List<int>` は決して `null` を含みませんが、`List<int?>` は含むことができます：

```dart
List<int?> scores = [7, null, 9];
```

`List<int>?` との違いに注意してください。こちらはリスト自体が存在しないことがあり、存在する場合には実在する数値だけを持ちます。

`null` の要素を取り除くには `nonNulls` を使います。これは存在する値だけを含み、`?` の付かない型を持つ `Iterable` を返します：

```dart
var present = scores.nonNulls.toList(); // List<int>
print(present); // [7, 9]
```

`whereType<int>()` も同じことをし、リストに複数の型が混ざっている場合にも使えます。

---

多くのライブラリ関数は、何かが**できなかった**ことを知らせるために `null` を使います。文字列を数値に変換する処理はその典型です。`int.parse` は文字列が数値でないとき `FormatException` を投げますが、`int.tryParse` は代わりに `null` を返し、どうするかをあなたに委ねます：

```dart
print(int.tryParse('42'));  // 42
print(int.tryParse('4x2')); // null
print(int.tryParse(''));    // null
```

`int.tryParse` の戻り値の型は `int?` なので、学んできたことがすべて当てはまります。既定値には `??`、連鎖には `?.`、プロモーションには `if` チェックです。`double.tryParse` も同じように動きます。

---

さらに2つの演算子にnull安全版があります。

**null安全カスケード** `?..` は、オブジェクトが `null` でないときだけカスケード操作の連鎖を実行し、そうでなければすべてをスキップします：

```dart
List<int>? numbers;
numbers?..add(1)..add(2); // nothing happens, numbers is still null
```

**null安全スプレッド** `...?` は、null許容のコレクションの要素をリテラルに挿入し、コレクションが `null` のときは何も追加しません：

```dart
List<int>? extra;
print([0, ...?extra]); // [0]

extra = [1, 2];
print([0, ...?extra]); // [0, 1, 2]
```

`?` がなければ、`List<int>?` に対する `...extra` はコンパイルエラーになります。

---

現実のデータは欠落だらけです。空のまま送られたフォーム項目、ファイルに存在しない列、数値になりきらない文字列。この章の道具は、それらを扱うために自然に組み合わせられます。欠けている要素を落とすには `nonNulls`、安全に変換するには `int.tryParse`、変換できなかったものを処理するには `??` か `if` チェックです。
