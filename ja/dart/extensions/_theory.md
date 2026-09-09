自分で書いたクラスにメソッドを追加する方法はすでに知っていますね。しかし、コードがDart SDKの中にある `String`、`int`、`List` はどうでしょうか？編集することはできないのに、メソッドがもう1つあればいいのにと思うことがよくあります。

**拡張（extension）**はこれを解決します。ソースコードに手を加えず、サブクラスも作らずに、**既存の**型に新しいメンバーを追加するものです。構文は次のとおりです：

```dart
extension ExtensionName on Type {
  // new methods and getters
}
```

拡張の中では、`this` はメンバーが呼び出される値を指します。拡張を宣言すると、そのメンバーは型自身のメンバーとまったく同じように呼び出せます：

```dart
extension Greeting on String {
  String greet() => 'Hello, $this!';
}

void main() {
  var name = 'Ada';
  print(name.greet()); // Hello, Ada!
}
```

拡張は `main` の中ではなく、クラスや関数と並んでファイルの**トップレベル**で宣言します。

---

拡張は数値を含む任意の型に対して動作します。この拡張は、すべての `int` に2倍するメソッドを与えます：

```dart
extension Doubling on int {
  int doubled() => this * 2;
}
```

拡張は**型**に適用されるため、メソッドは変数に対しても、**リテラル**に対して直接呼び出すこともできます。負のリテラルには括弧が必要です。そうしないと、マイナス記号よりも先にドットが読まれてしまいます：

```dart
var n = 21;
print(n.doubled());    // 42
print(4.doubled());    // 8
print((-3).doubled()); // -6
```

---

拡張は**ゲッター**も宣言できます。ゲッターは括弧なしでプロパティのように読み取られます。拡張の中では型自身のメンバーを直接呼び出せます。クラスの中とまったく同じように、`this.` は省略できます。

```dart
extension Sizes on String {
  bool get isLong => length > 10;      // same as this.length
  String get firstChar => this[0];
}

void main() {
  print('Dart'.isLong);           // false
  print('extension'.firstChar);   // e
}
```

値を**読み取る**だけでパラメータを取らないメンバーにはゲッターを選び、処理を行うか引数を必要とするメンバーにはメソッドを選びます。

---

`on` の後ろの型は、`List<int>` のような**パラメータ化された**型でも構いません。この場合、拡張はその要素型のリストにのみ適用されます。`[1, 2].total()` は動作しますが、`['a', 'b'].total()` はコンパイルできません。

```dart
extension Totals on List<int> {
  int total() {
    var sum = 0;
    for (final n in this) {
      sum += n;
    }
    return sum;
  }
}
```

拡張の中では、`this` はリストそのものなので、いつもどおりループしたり、インデックスでアクセスしたり、`length` を呼び出したりできます。

---

`List<int>` に対する拡張は `List<String>` には使えません。**あらゆる**要素型に対して動作する拡張を1つ書くには、拡張に**型パラメータ**を与えます。型パラメータは名前の後ろに山括弧で囲んで書き、`on` の型の中で使います：

```dart
extension Firsts<T> on List<T> {
  T get firstOrLast => length > 1 ? this[0] : this[length - 1];
}
```

`T` は「要素型が何であれ」を表すプレースホルダーです。`List<int>` の上では `int` に、`List<String>` の上では `String` になるため、上のゲッターはそれに応じて `int` または `String` を返します。コンパイラが呼び出しごとに `T` を埋めてくれます。

```dart
print([7, 8, 9].firstOrLast); // 7
print(['a', 'b'].firstOrLast); // a
```

---

`String` に対する拡張は `String?` に対しては呼び出せません。値が `null` かもしれず、コンパイラが呼び出しを拒否するためです。代わりに**null許容**の型に対して拡張を宣言すると、メソッドは `String?` に対して直接呼び出せます。その中で `this` は `String?` 型を持つため、`null` のケースは `??` を使うなどして自分で処理しなければなりません：

```dart
extension Defaults on int? {
  int orZero() => this ?? 0;
}

void main() {
  int? count = null;
  print(count.orZero()); // 0
  print(5.orZero());     // 5
}
```

非null許容の `int` は `int?` が期待される場所に渡せるため、この拡張は両方に対して動作します。

---

拡張はメソッド、ゲッター、セッター、演算子を追加できますが、**インスタンスフィールドを追加することはできません**。`int` の値はメモリ内で固定のレイアウトを持ち、拡張はドット構文で呼び出すことをコンパイラが許す関数の集合にすぎません。値ごとに追加のデータを格納する場所はないのです。

```dart
extension Counter on int {
  int count = 0; // error: extensions can't declare instance fields
}
```

拡張の中のゲッターとセッターは、`this` から値を計算するか、既存のメンバーに処理を委ねることしかできません。呼び出しの間で何かを記憶しておくことはできないのです。

---

拡張は**静的（static）**メンバーを宣言できます。クラスの場合と同じように、静的メンバーはどの値にも属さず拡張そのものに属し、拡張先の型を通じてではなく**拡張の名前**を通じてアクセスされます：

```dart
extension Temperatures on double {
  static const double boiling = 100.0;

  static bool isBoiling(double celsius) => celsius >= boiling;
}

void main() {
  print(Temperatures.boiling);         // 100.0
  print(Temperatures.isBoiling(37.5)); // false
  print(double.boiling);               // error: 'boiling' isn't defined for 'double'
}
```

静的メンバーは、拡張対象の型に関係する定数やヘルパー関数を置くのに便利な場所です。

---

拡張はSDKの型のためだけのものではありません。**自分で書いたクラス**を拡張することもできます。これは、クラスが自分の管理外のパッケージに由来するときや、クラスを小さく保ち、ヘルパーを必要とするコードのそばに追加のヘルパーを置きたいときに役立ちます。

```dart
class Circle {
  final double radius;
  Circle(this.radius);
}

extension CircleMath on Circle {
  double get diameter => radius * 2;
}

void main() {
  print(Circle(3).diameter); // 6.0
}
```

拡張からは、クラスの外に書いたコードとまったく同じように、クラスの公開フィールドとメソッドが見えます。

---

Dartでは、`operator` キーワードの後に記号を付けた名前のメソッドを使って、`+`、`*`、`==` などの演算子がその型の値に対して何を意味するかを型に定義させられます。演算子の右側はメソッドのパラメータです：

```dart
extension Scaling on List<int> {
  List<int> operator *(int factor) => map((n) => n * factor).toList();
}

void main() {
  print([1, 2, 3] * 10); // [10, 20, 30]
}
```

拡張は演算子を宣言できるため、既存の型にまだ持っていない新しい演算子を与えられます。`String` は `+` と `*` を持ちますが `-` は持たないので、拡張は `'hello world' - 'o'` が何を意味するかを定義できます。

---

拡張が型が**すでに持っている**メンバーを宣言したらどうなるでしょうか？型自身のメンバーが常に勝ちます。拡張のメンバーが考慮されるのは、型そのものがその名前のメンバーを持たないときだけです。拡張のメンバーは黙って無視され、エラーもオーバーライドもありません。

```dart
extension Shorter on String {
  int get length => 0;
}

void main() {
  print('four'.length); // 4, String's own length is used
}
```

つまり、拡張はメンバーを追加して隙間を埋めることはできますが、既存のメンバーの振る舞いを**変える**ことは決してできません。

---

拡張の名前は省略できます。**名前のない**拡張も同じように動作しますが、それを宣言しているファイルの中でしか見えません：

```dart
extension on int {
  bool get isTriple => this % 3 == 0;
}
```

**名前**が問題になるのは、2つの拡張が同じ型に同じメンバーを提供するときです。呼び出しが**曖昧**になってコンパイルできません。名前があれば、この衝突を2つの方法で解決できます。拡張が異なるファイルに由来するなら、importの中で一方を `show` または `hide` できます：

```dart
import 'package:loud/loud.dart';
import 'package:quiet/quiet.dart' hide Quiet;
```

または、どこでも、拡張を**明示的に**適用できます。値を、コンストラクタであるかのように拡張の名前で囲むのです：

```dart
print(Loud('hi').describe());
```

名前のない拡張は隠すことも明示的に適用することもできないため、他の人がimportするコードでは名前付きの拡張を好みます。

---

ジェネリックな拡張は、`where` や `map` がするのとまったく同じように、**関数**をパラメータとして取れます。関数型は要素型 `T` を使って書くため、コールバックは正しい型の要素を受け取ります：

```dart
extension Checks<T> on List<T> {
  bool all(bool Function(T) test) {
    for (final item in this) {
      if (!test(item)) return false;
    }
    return true;
  }
}

void main() {
  print([2, 4, 6].all((n) => n.isEven)); // true
}
```
