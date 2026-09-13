**高階メソッド**とは、関数を引数として受け取るメソッドです。Dart のコレクションには多くの高階メソッドがあり、渡す関数は通常、アロー構文 `(x) => ...` で書かれた無名関数です：

`map` はその最も一般的な例です。すべての要素に対して関数を呼び出し、要素ごとに1つの結果を生成します。元のコレクションはそのまま残されます：

```dart
final numbers = [1, 2, 3];
print(numbers.map((n) => n * 2)); // (2, 4, 6)
print(numbers);                   // [1, 2, 3]
```

出力の**丸括弧**に注目してください。`map` が返すのは `List` ではなく、`Iterable` つまり順にたどれるシーケンスです。実際のリストを取得するには、**`toList()`** を呼び出します：

```dart
final doubled = numbers.map((n) => n * 2).toList();
print(doubled); // [2, 4, 6]
```

出力に角括弧があれば `List` を、丸括弧があれば単なる `Iterable` を見ている、という合図です。

---

`where` は `bool` を返す関数、いわゆる**述語**を受け取り、`true` を返す要素だけを残します。残った要素の順序が変わることはありません：

```dart
final numbers = [4, -2, 7, 0];
print(numbers.where((n) => n > 0).toList()); // [4, 7]
```

`map` と同じく、`where` は `Iterable` を返し元のコレクションを決して変更しないため、結果を `List` に変えるのはやはり `toList()` の役割です。

このメソッドは他の言語では `filter` と呼ばれますが、Dart では `where` です。

---

`map` に渡す関数は、受け取る要素と同じ型を返すとは限りません。文字列のリストをその長さに `map` すると、`List<String>` は `Iterable<int>` になり、`toList()` がそれを `List<int>` にします：

```dart
final words = ['fig', 'kiwi'];
print(words.map((w) => w.length).toList()); // [3, 4]
```

結果は常に**元とまったく同じ数の要素**を同じ順序で持ちます：`map` は要素を変換するだけで、決して追加や削除はしません。

---

新しいコレクションを作る代わりに、コレクションについての質問に答える高階メソッドもあります。これらは述語を受け取り `bool` を返します：

- `any` は**少なくとも1つ**の要素が述語を満たせば `true` です
- `every` は**すべての**要素が述語を満たせば `true` です

```dart
final numbers = [1, 2, 3];
print(numbers.any((n) => n > 2));   // true
print(numbers.every((n) => n > 2)); // false
```

どちらも答えが確定した時点で止まります：`any` は最初に一致した要素で、`every` は最初に一致しなかった要素で止まります。

空のコレクションでは `any` は `false`、`every` は `true` です。前者を成立させる要素も、後者を崩す要素も存在しないからです。

---

`map` と `where` は**遅延評価**です：呼び出しても何も実行されません。返される `Iterable` は元のコレクションと関数を覚えており、その関数は結果を1要素ずつたどっている間にだけ呼ばれます。

```dart
final numbers = [1, 2, 3];
final doubled = numbers.map((n) => n * 2); // nothing computed yet
print(doubled.first);                      // computes only 2
```

`toList()` がシーケンスを**実体化**します：最初から最後までたどり、すべての結果を実際の `List` に格納します。

遅延評価には覚えておく価値のある2つの帰結があります。遅延 `Iterable` はイテレートするたびに再計算されるため、値を複数回必要とするなら `toList()` で一度実体化する方が安上がりです。また、元のコレクションを見続けるため、そのコレクションを変更すると `Iterable` が生成するものも変わります：

```dart
final numbers = [1, 2, 3];
final lazy = numbers.map((n) => n * 2);
final eager = numbers.map((n) => n * 2).toList();
numbers.add(4);
print(lazy.toList()); // [2, 4, 6, 8]
print(eager);         // [2, 4, 6]
```

---

`fold` はコレクション全体を**1つの値**にまとめます。2つの引数を受け取ります：**アキュムレータ**の初期値と、それまでのアキュムレータと次の要素を受け取って新しいアキュムレータを返す関数です：

```dart
final numbers = [1, 2, 3, 4];
final total = numbers.fold(0, (acc, n) => acc + n);
print(total); // 10
```

ここで `acc` は `0` から始まり、`1`、`3`、`6` と続き、最後に `10` になります。

アキュムレータは数である必要も、要素と同じ型である必要もありません：`''` から始めてテキストを追加していけば、どんなリストからでも `String` を作れます。

覚えておくべき詳細が1つあります：Dart はアキュムレータの型を初期値**と**、結果が使われる場所から推論します。`print(...)` の中では期待される型が分からないため、結果をまず変数に格納するか（あるいは `fold<int>(...)` と書くか）してください。そうしないと、コンパイラはアキュムレータに `+` を使えないと不満を言います。

---

`reduce` は `fold` の簡潔な親戚です。初期値を受け取りません：**最初の要素**が開始時のアキュムレータとなり、関数は残りの各要素に対して実行されます：

```dart
final numbers = [1, 2, 3, 4];
print(numbers.reduce((a, b) => a + b)); // 10
```

初期値がないため、結果は常に**要素と同じ型**になります。また、空のコレクションで `reduce` を呼び出すと `StateError` が投げられます：開始地点となる最初の要素がないからです。`fold` にはそのような問題がないため、より安全なデフォルトと言えます。

`reduce` が最も輝くのは、最大値のように多くの要素の中から1つを探す場合です：

```dart
print(numbers.reduce((a, b) => a > b ? a : b)); // 4
```

---

`firstWhere` は述語に一致する要素をすべてではなく、**最初の**1つだけ返します：

```dart
final words = ['fig', 'kiwi', 'banana'];
print(words.firstWhere((w) => w.length > 3)); // kiwi
```

何も一致しない場合、返す要素がないので `firstWhere` は `StateError` を投げます。エラーの代わりに答えを出すには、名前付き引数 **`orElse`** を渡します。これはパラメータを取らずにフォールバック値を生成する関数です。

```dart
print(words.firstWhere((w) => w.length > 10, orElse: () => 'none')); // none
```

`orElse` は単なる値ではなく関数なので、検索が失敗したときにだけ呼ばれます。`orElse: 'none'` と書くとコンパイルできません。

---

`map` に渡す関数が要素ごとにコレクションを返すと、結果はコレクションのシーケンスになります。**`expand`** は同じ仕事をしつつ、そのすべてを1つの平坦なシーケンスにつなげます：

```dart
final numbers = [1, 2];
print(numbers.map((n) => [n, -n]).toList());    // [[1, -1], [2, -2]]
print(numbers.expand((n) => [n, -n]).toList()); // [1, -1, 2, -2]
```

順序は保持されます：最初の要素が生成したものが先に来て、次に2番目の要素が生成したもの、という順です。

返すコレクションのサイズは任意なので、`expand` は最初より**多い、あるいは少ない**要素を生成する方法にもなります：ある要素に対して空のリストを返せば、その要素は単に捨てられます。

```dart
print(['a b', 'c'].expand((s) => s.split(' ')).toList()); // [a, b, c]
```

---

`take(n)` は**先頭の** `n` 個の要素を残し、`skip(n)` はそれを捨てます。どちらも関数を受け取りませんが、遅延 `Iterable` を返すため、他の高階メソッドの間に自然に収まります：

```dart
final scores = [10, 20, 30, 40, 50];
print(scores.take(2).toList()); // [10, 20]
print(scores.skip(3).toList()); // [40, 50]
```

存在するより多くの要素を要求してもエラーにはなりません：存在するもの、あるいは空の結果が得られるだけです。

`takeWhile` と `skipWhile` は述語を取るバージョンです。述語が成立している**間だけ**先頭から要素を取り、あるいは捨て続け、後の要素がまた一致するとしても、最初に一致しなくなった要素で止まります：

```dart
print(scores.takeWhile((s) => s < 35).toList()); // [10, 20, 30]
```

---

Dart には `sorted` メソッドはありません。`sort` は `List` のメソッドで、リストを**その場で（in place）**並べ替え、何も返しません：

```dart
final numbers = [3, 1, 2];
numbers.sort();
print(numbers); // [1, 2, 3]
```

`void` を返すため、結果を利用することはまったくできません：`final sorted = numbers.sort();` は、コンパイラが読み取りを許さない値になります。順序付きの**コピー**を作る定番の書き方は、`toList()` の後にカスケード `..sort()` を続けるものです：`toList()` がコピーを作り、`..` はコピー自身を返しながらそのコピーに `sort` を実行します。

```dart
final numbers = [3, 1, 2];
final sorted = numbers.toList()..sort();
print(sorted);  // [1, 2, 3]
print(numbers); // [3, 1, 2], untouched
```

`sort` は**コンパレータ**も受け取れます：2つの要素を取り、最初の要素が2番目より先に来るなら負の数、等しければ `0`、そうでなければ正の数を返す関数です。`compareTo` はまさにそれを返すため、任意のキーでの並べ替えは1行で書けます：

```dart
final words = ['kiwi', 'fig', 'banana'];
print(words.toList()..sort((a, b) => a.length.compareTo(b.length)));
// [fig, kiwi, banana]
```

---

`fold` と `reduce` はよく似ています。どちらを選ぶかは2つの質問に帰着します：コレクションが空であり得るか、そして結果は要素と同じ型か？

```dart
final words = ['fig', 'kiwi'];
final joined = words.reduce((a, b) => '$a, $b'); // String from Strings
final letters = words.fold(0, (acc, w) => acc + w.length); // int from Strings
print(joined);  // fig, kiwi
print(letters); // 7
```

`reduce` は要素から始まるため、返せるのは常に要素の型だけです。`fold` は自分で選んだ値から始まるため、アキュムレータは数え上げる `int`、育っていく `String`、構築中の `List` でさえあり得ます。そしてその初期値がすでに存在するので、空のコレクションに対しては `fold` は初期値をそのまま返すだけです。一方 `reduce` には返すものがなく、例外を投げます。

---

これらのメソッドはどれも `Iterable` を返し、すべての `Iterable` が再び同じメソッドを持ちます。だからこそ**チェーン**できます：計算全体が左から右へパイプラインのように読め、各ステップは前のステップが生成したものを扱います。

```dart
final words = ['kiwi', 'fig', 'banana', 'date'];
print(words.where((w) => w.length == 4).map((w) => w.toUpperCase()).toList());
// [KIWI, DATE]
```

`toList()` が必要なのは最後のステップだけです：途中で呼ぶと、誰も保持しないリストを作ることになります。

型はチェーンに沿って変化し、次の関数が受け取るものも変わります：`List<String>` に対する `where` の後はまだ文字列ですが、`map((w) => w.length)` の後は次のステップが見るのは数です。

各ステップは遅延評価されるため、順序は結果だけでなく行われる作業にも影響します：まず `where` で絞り込めば、`map` はより少ない要素に対して呼ばれます。

---

これらのメソッドには何も特別なところがありません：単に**パラメータとして関数**を持っているだけで、自分の関数も同じことができます。関数パラメータの型は、戻り値の型、`Function`、その後に括弧の中へパラメータ型、の順に書きます：

```dart
List<int> applyAll(List<int> numbers, int Function(int) operation) {
  return numbers.map(operation).toList();
}
```

呼び出し側が**何**が起こるかを決め、関数が**何に対して**かを決めます。`operation` がそのまま `map` に渡されることに注目してください：関数の値は他の値と同じように渡せます。

引数には無名関数か、既存の関数の**名前**（括弧を付けずに書く）を渡せます。括弧を付けると、渡す代わりに呼び出してしまいます：

```dart
int square(int n) => n * n;

print(applyAll([1, 2, 3], square));       // [1, 4, 9]
print(applyAll([1, 2, 3], (n) => n + 1)); // [2, 3, 4]
```

---

関数は関数を**返す**こともできます。戻り値の型は関数パラメータの型とまったく同じように書き、返される値は通常、無名関数です：

```dart
int Function(int) multiplier(int factor) {
  return (n) => n * factor;
}
```

`multiplier(3)` は何も掛けません：`3` を掛ける新しい関数を作って返すのです。その関数はその後、他の値と同じように格納されたり、呼び出されたり、`map` に渡されたりします：

```dart
final triple = multiplier(3);
print(triple(5));                       // 15
print([1, 2, 3].map(triple).toList());  // [3, 6, 9]
```

返された関数は、`multiplier` が終わった後も `factor` を覚えています。作成されたスコープの変数を保持する関数は**クロージャ**と呼ばれ、このような関数ファクトリを可能にする仕組みです。

---

組み合わせれば、これらのメソッドは手書きのループのほとんどを置き換えます。パイプラインは通常、3つの段階で読み解けます：`where` で要素を**選択**し、`map` で**変換**し、それから `fold` で**結合**します：

```dart
final prices = [12, 40, 7];
final cheapTotal = prices.where((p) => p < 20).fold(0, (acc, p) => acc + p);
print(cheapTotal); // 19
```

`fold` は独自の初期値を選べるため、要素とは無関係の型でチェーンを終えることもできます。たとえば少しずつ育っていく `String` です：

```dart
final words = ['fig', 'kiwi'];
final firstLetters = words.fold('', (acc, w) => acc + w[0]);
print(firstLetters); // fk
```

各段階は短く保たれ、何をするかがひと目で分かります。3つすべてを一度に行うループよりもこれらを好む本当の理由はここにあります。
