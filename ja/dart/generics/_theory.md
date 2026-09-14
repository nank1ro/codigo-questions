`List` は値を保持するだけでなく、**一つの型の**値を保持します。型はコレクションの名前の直後に山括弧で囲んで書きます：

```dart
List<String> names = ['Ada', 'Grace'];
List<int> scores = [10, 20];
```

ここでの `String` と `int` は**型引数**であり、型引数を取る型は**ジェネリック**と呼ばれます。リストのクラスは一度だけ書かれ、`List<String>` と `List<int>` はそこから作られる2つの異なる型です。

その見返りとして、コンパイラは中身が何であるかを知っています：

```dart
names.add(42);          // error: 42 is not a String
print(names.first.toUpperCase()); // fine: first is a String
```

---

`List` だけがジェネリックなコレクションではありません。`Set` は型引数を1つ取り、`Map` は**2つ**取ります。1つはキーのため、もう1つは値のためで、この順番です。

```dart
Set<String> tags = {'new', 'sale'};
Map<String, int> ages = {'Ada': 36, 'Grace': 45};
```

空のコレクションリテラルは中身から型を読み取ることができないので、リテラル自体に型引数を書きます：

```dart
final counts = <String, int>{};
final seen = <String>{};
counts['fig'] = 3;
```

型がわかれば、コレクションから取り出すものはすべてすでに正しい型を持っています。`ages['Ada']` は `int?` であり、得体の知れない値になることはありません。

---

Dartには `dynamic` という型もあります。これは「何でもあり」を意味します。`List<dynamic>` はすべての値を受け入れるので、`List<String>` より便利に見えます：

```dart
List<dynamic> things = ['Ada', 'Grace'];
things.add(42);                    // accepted
print(things.first.toUpperCase()); // accepted
```

落とし穴は、コードを書いている間は何もチェックされないことです。`dynamic` の値に対するすべての呼び出しはプログラムの実行中に解決されるため、`things.first.toUpperCse()` のようなタイプミスでも問題なくコンパイルされ、ユーザーの目の前でクラッシュします。

ジェネリクスはその代替です。**どんな**型でも動く1つのコードを書きながら、使うたびには**1つの**型でチェックされます。これこそがこのトピックの要点です。

---

Dartに用意されているジェネリッククラスに限定されるわけではありません。自分で宣言することもできます。**型パラメータ**はクラス名の後に山括弧で囲んで書き、以降はクラス本体の中で通常の型として扱えます：

```dart
class Box<T> {
  final T value;

  Box(this.value);

  T unwrap() => value;
}
```

`T` は単なるプレースホルダです。`Box` が作られるときに、明示的に、あるいは推論によって埋められます：

```dart
final a = Box<int>(7);   // Box<int>
final b = Box('fig');    // Box<String>, inferred from the argument
print(a.value + 1);      // 8, the compiler knows value is an int
```

文字そのものには意味がありません。`T` は「型」を表す慣習にすぎません。

---

関数は、ジェネリッククラスの中に入っていなくても、それ単体でジェネリックになれます。型パラメータは名前とパラメータリストの間に書きます：

```dart
T firstOf<T>(List<T> items) => items.first;

print(firstOf(['fig', 'kiwi'])); // fig, T is String here
print(firstOf([10, 20]));        // 10, T is int here
```

1つの関数本体を一度チェックすれば、すべての型で再利用できます。型引数は通常は引数から推論されますが、推論する手がかりがないときは明示的に書くこともできます：

```dart
final empty = firstOf<String>(<String>[]); // throws, but the type is clear
```

クラスの中のメソッドもまったく同じルールに従います。

---

ジェネリッククラスの中では、型パラメータはどこからでも見えます。フィールド、コンストラクタのパラメータ、メソッドのシグネチャ、メソッドの本体です。クラス名の横で一度宣言すれば、すべてのメンバーがそれを使えます。

```dart
class Holder<T> {
  final T item;

  Holder(this.item);

  String describe() => 'holding $item';
}
```

型を決めるのはオブジェクトの生成です。`Holder<String>('fig')` は `item` を `String` にし、`Holder<int>(3)` はそれを `int` にします。

---

クラスは複数の型パラメータをコンマで区切って宣言できます。組み込みの例が `Map<K, V>` です。キーの型が1つ、値の型が1つです。

```dart
class Entry<K, V> {
  final K key;
  final V value;

  Entry(this.key, this.value);
}

final e = Entry<String, int>('age', 30);
```

**順番**は型の一部です。`Entry<String, int>` と `Entry<int, String>` は無関係な型であり、片方の値をもう片方に代入することはできません。型パラメータは戻り値の型の中で並べ替えることもできるので、メソッドはオブジェクトの入れ替わったバージョンを手渡せます：

```dart
Entry<V, K> get flipped => Entry(value, key);
```

---

健全なnull安全のもとでは、クエスチョンマークが現れる場所は2つあり、それぞれ異なる意味を持ちます：

```dart
Box<int?> a = Box(null); // a box that exists and holds a nullable int
Box<int>? b = null;      // no box at all, but if there is one it holds an int
```

`Box<int?>` では**型引数**がnull許容なので、`a.value` の型は `int?` で `null` かもしれませんが、`a` 自体は常に存在します。`Box<int>?` では**変数**がnull許容なので、`b` は `null` かもしれず、中に入るには `b?.value` か `b!.value` が必要です。

裸の `T` は `T extends Object?` を意味するので、`Box<int?>` のようなnull許容の型引数はまったく問題なく合法です。

---

この違いは、値を使う瞬間に問題になります。`Box<int?>` では通常どおりフィールドにアクセスしてから中の `null` を処理しますが、`Box<int>?` ではまず存在しないかもしれないボックスを乗り越えなければなりません：

```dart
Box<int?> a = Box(null);
print(a.value ?? 0); // 0, the box is there, its content is null

Box<int>? b = null;
print(b?.value ?? 0); // 0, the box itself is missing
```

`Box<int>?` に対して `b.value` と書くとまったくコンパイルできません。Dartは存在しないかもしれないもののフィールドを読むことを拒否します。

---

境界のない `T` は何であってもよいので、本体の中ではすべてのオブジェクトが持つものしか使えません。次のコードはコンパイルできません：

```dart
T twice<T>(T value) => value + value; // error: + is not defined for T
```

**境界（bound）**がこれを解決します。`T extends num` と書くと「`T` は数値しか取れない」ことを意味し、その見返りとして本体では `num` が提供するすべてを使えます：

```dart
T twice<T extends num>(T value) => (value + value) as T;

num half<T extends num>(T value) => value / 2;
```

境界は呼び出し側でチェックされます。`half(4)` と `half(2.5)` は問題なく、`half('fig')` はコンパイル時エラーです。境界は双方向の約束です。より狭い引数と引き換えに、内部ではより多くのことができます。

---

境界のためのキーワードは常に `extends` です。境界がスーパークラスではなくインターフェースであっても同じです。型パラメータリストに `implements` はありません。

```dart
num biggerOf<T extends num>(T a, T b) => a > b ? a : b;
```

境界がなければ `a > b` はコンパイルできません。比較演算子は `num` のものであり、すべてのオブジェクトのものではないからです。

---

境界は型パラメータ自身に言及することもできます。`Comparable<T>` は、`compareTo` を通じて自分と同じ種類のものと比較する方法を知っているすべてのもののインターフェースです：

```dart
print('fig'.compareTo('kiwi')); // negative: fig comes first
print('kiwi'.compareTo('fig')); // positive
print('fig'.compareTo('fig'));  // zero
```

したがって `T extends Comparable<T>` は「自分自身と比較できる任意の型」と読めます。これはソートや最大値を求める関数がまさに必要としているものです：

```dart
T maxOf<T extends Comparable<T>>(T a, T b) => a.compareTo(b) >= 0 ? a : b;

print(maxOf('fig', 'kiwi')); // kiwi
```

`String` と `DateTime` はどちらも直接これを満たします。`int` と `double` は `Comparable<num>` を実装しているので、数値のリストは単に `num` として比較されます。

---

同じ境界は最小の要素を求めるのにもそのまま使えます。変わるのは比較の符号だけです。`compareTo` はレシーバが先に来るときに負の数を返すので、`item.compareTo(best) < 0` は「こちらのほうが小さい」ことを意味します。

---

ジェネリッククラスには、他のクラスと同じように名前付きコンストラクタや**ファクトリ**コンストラクタを持てますし、型パラメータはその中でも使えます。ファクトリコンストラクタはオブジェクトそのものを生成しません。本体を実行して1つ返します。これにより、インスタンスを選んだり、再利用したり、好きな方法で構築したりできます。

```dart
class Box<T> {
  final T value;

  Box(this.value);

  factory Box.first(List<T> items) => Box(items.first);
}

final b = Box<int>.first([5, 6]);
print(b.value); // 5
```

型引数はコンストラクタ名ではなくクラスに付きます。`Box<int>.first(...)` のようになります。ファクトリの中では `<T>[]` は本物の空の `List<T>` なので、まだわからない型の既定値を作る場所としてファクトリは自然な選択です。

---

境界なしで書かれた型パラメータは、実は無境界ではありません。`class Box<T>` は `class Box<T extends Object?>` の省略形です。だからこそ `Box<int?>` が受け入れられ、クラスの中では `value` が非nullだと決して仮定できないのです。

null許容の型引数を禁止するには、パラメータを `Object` で境界付けます：

```dart
class Strict<T extends Object> {
  final T value;
  Strict(this.value);
}

final ok = Strict<int>(7);
final bad = Strict<int?>(null);
// error: Type argument 'int?' doesn't conform to the bound 'Object'
```

`Object` は `null` 以外のすべての型なので、`T extends Object` は「本当に存在するものなら何でも」と読めます。

---

`typedef` は型に名前を付けます。そしてtypedefはそれ自体の型パラメータを持てます。通常の目的は、使うたびにいちいち書き連ねる代わりに、関数型の族に一度名前を付けることです：

```dart
typedef Transform<I, O> = O Function(I input);

final Transform<String, int> length = (word) => word.length;
print(length('kiwi')); // 4
```

`Transform<String, int>` は `int Function(String)` の別の書き方にすぎないので、2つは互いに交換できます。得られるのは読みやすさです。`Transform<I, O> transform` と宣言されたパラメータは関数が何のためのものかを語りますが、`O Function(I)` は見た目しか語りません。

ジェネリックなtypedefとジェネリックな関数は自然に組み合わさります。関数自身の型パラメータがtypedefの型パラメータを埋めます。
