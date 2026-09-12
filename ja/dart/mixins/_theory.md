クラスが `extend` できるスーパークラスは1つだけですが、それ以外に共通点のないクラスどうしが同じ振る舞いを必要とすることはよくあります。**ミックスイン（mixin）**は、任意の数のクラスが取り込める再利用可能な振る舞いの断片です。

**`mixin`** キーワードで宣言し、クラスは **`with`** キーワードで取り込みます：

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish` は自分のメンバーを1つも宣言していませんが、すべての `Fish` は `swim` を持ちます。ミックスインのメンバーがクラスのメンバーになるからです。ミックスインは、関係のあるなしにかかわらず、好きな数のクラスで使えます。

---

ミックスインの本体はクラスの本体とよく似ています。メソッド、ゲッター、フィールドをまったく同じように書けます。違うのは、宣言そのものに対してできることです。

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

ミックスインの名前は**型**としても機能するので、`Server() is Timestamped` は `true` になり、変数を `Timestamped t = Server();` と宣言できます。これで2つの無関係なクラスが、互いに継承することなく1つの実装を共有します。

---

ミックスインはメソッドに限定されません。**フィールド**も宣言でき、ミックスインを使うすべてのクラスのすべてのオブジェクトが、それぞれ自分専用のコピーを持ちます。

```dart
mixin Counter {
  int count = 0;

  void increment() {
    count++;
  }
}

class Clicker with Counter {}

void main() {
  final a = Clicker();
  final b = Clicker();
  a.increment();
  a.increment();
  print(a.count); // 2
  print(b.count); // 0, b has its own count
}
```

これがミックスインをインターフェース以上のものにしています。データと、それを扱うコードの両方をもたらすのです。

---

`mixin` 宣言はクラスでは**ありません**。他のクラスにミックスインされることだけを目的として存在するため、自分自身のコンストラクタを持たず、インスタンス化も継承もできません：

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

名前は型として引き続き機能するので、`Team() is Scored` も `Scored s = Team();` もどちらも問題ありません。ミックスインにはコンストラクタがないため、非null許容のフィールドは上の `int score = 0;` のように、宣言した場所で初期化する（または `late` を付ける）必要があります。

---

ミックスインはメンバーを**本体なしで**宣言することもできます。そのようなメンバーは抽象メンバーです。ミックスインがそれを使い、ミックスインを取り込むクラスがそれを提供しなければなりません。

```dart
mixin Greeting {
  String get name;                       // no body: the class provides it

  String greet() => 'Hello, $name!';
}

class Person with Greeting {
  @override
  final String name;

  Person(this.name);
}

void main() {
  print(Person('Ada').greet()); // Hello, Ada!
}
```

振る舞いはミックスインが、データはクラスがもたらします。`final String name;` のようなクラスのフィールドがあれば、同名の抽象ゲッターを満たすのに十分です。

---

部品を組み合わせると、ミックスインを使うプログラムは3つの部分から成ります。`mixin` 宣言、`with` でそれを取り込む1つ以上のクラス、そして共有メンバーを呼び出すコードです。

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

トップレベルの宣言は Dart では任意の順序で書けますが、ミックスインを使うクラスの前にミックスインがあると、ファイルを上から下に読みやすくなります。

---

クラスは**複数のミックスインを同時に**使えます。`with` の後にカンマで区切って並べます。Dart はそれらを**左から右へ**適用し、前のものの上に1つずつ積み重ねていきます。そのため、2つのミックスインが同じメンバーを宣言しているときは、リストの**最後の**ものが勝ちます：

```dart
mixin A {
  String who() => 'A';
}

mixin B {
  String who() => 'B';
}

class First with A, B {}
class Second with B, A {}

void main() {
  print(First().who());  // B, the last mixin in the list
  print(Second().who()); // A, the last mixin in the list
}
```

この積み重ねは**線形化（linearization）**と呼ばれます。`with A, B` は `Object` → `A` → `B` → クラス自身というチェーンを組み立てます。

---

最後のミックスインが勝つため、`with` リストの順序はスタイルの細部ではなくクラスの意味の一部です。並べ替えると、オブジェクトが最終的に持つ実装が変わります：

```dart
mixin Plain {
  String format(String text) => text;
}

mixin Starred {
  String format(String text) => '*$text*';
}

class Fancy with Plain, Starred {}  // format comes from Starred
class Simple with Starred, Plain {} // format comes from Plain
```

1つのミックスインだけが宣言しているメンバーは決して競合しません。順序にかかわらず利用できます。`with X, Y` は「`X` から始めて、`Y` にそれを上書きさせる」と読みます。

---

ミックスインと `extends` は一緒に機能します。クラスはスーパークラス**と**ミックスインのリストの両方を持てて、ミックスインは常にスーパークラスの**上に**適用されます：

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

このチェーンは `Object` → `Document` → `Timestamped` → `Report` です。メンバーはチェーンの末尾から探し始めるので、`Report().header()` は `Timestamped` のバージョンを最初に見つけます。同じメンバーをスーパークラスとミックスインの両方で宣言することはまったく問題ありません。ミックスインが継承した振る舞いを置き換えたり包み込んだりするのが、まさにこの方法だからです。

---

クラスの本体はチェーンのいちばん末尾にあるので、クラスで宣言したメンバーは、そのミックスインから来る同名のメンバーを**上書き**します。上書きの中では、**`super`** でミックスインが提供したバージョンに届きます：

```dart
mixin Polite {
  String greet() => 'Hello';
}

class Host with Polite {
  @override
  String greet() => '${super.greet()}, welcome!';
}

class Guest with Polite {}

void main() {
  print(Host().greet());  // Hello, welcome!
  print(Guest().greet()); // Hello
}
```

ミックスイン自身はそのままです。`Guest` は元の `greet` をそのまま受け取ります。`super.greet()` があるからこそ、`Host` は共有される振る舞いをコピーせずにその上に構築できるのです。

---

ある振る舞いは、特定のクラスの上でしか意味をなさず、その仕事のためにそのクラスのメンバーを必要とすることがあります。**`on`** 句がその要件を宣言します：

```dart
class Animal {
  String get name => 'animal';
}

mixin Noisy on Animal {
  String shout() => '${name.toUpperCase()}!';
}

class Dog extends Animal with Noisy {
  @override
  String get name => 'dog';
}

void main() {
  print(Dog().shout()); // DOG!
}
```

`on Animal` は2つのことをします。ミックスインが上の `name` のように `Animal` のメンバーを使えるようにすることと、ミックスインを使える相手を制限することです。`class Rock with Noisy {}` は、`Rock` が `Animal` ではないためコンパイルエラーになります。

---

`on` 句を持つミックスインは、スーパークラスのメンバーを自分のもののように読み取れます。既存の型を飾る振る舞いを置くのに適した場所であるのは、まさにこのためです：

```dart
class Shape {
  String get kind => 'shape';
}

mixin Printable on Shape {
  void show() {
    print('a $kind');
  }
}

class Square extends Shape with Printable {
  @override
  String get kind => 'square';
}
```

`Square` は `kind` を上書きし、`show` はその上書きを自動的に拾います。ミックスインは常に実際のオブジェクトに対してメンバーを呼び出すからです。

---

ミックスインが `on` 句を持つと、その型のメンバーを**上書き**し、**`super`** を呼び出してチェーンの下にあるバージョンに届けられるようになります：

```dart
class Logger {
  String log(String message) => message;
}

mixin Timestamped on Logger {
  @override
  String log(String message) => '[12:00] ${super.log(message)}';
}

class AppLogger extends Logger with Timestamped {}

void main() {
  print(AppLogger().log('started')); // [12:00] started
}
```

`super.log` はミックスイン自身の `log` ではなくその下にあるものなので、無限再帰にはなりません。このようなミックスインを `with A, B` で何段か重ねると、それぞれが前のものを包み込みます。呼び出しは**最後の**ミックスインに最初に入り、スーパークラスへと下っていきます。

---

`mixin` 宣言はインスタンス化も継承もできず、普通の `class` は `with` の後で使えません。**どちらの**使い方もできる1つの宣言が必要なときは、**`mixin class`** と書きます：

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

`mixin class` はその柔軟性の代償として2つの制約を払います。`Object` を継承しなければならないため自分の `extends` 句を持てず、コンストラクタを宣言してはなりません。ミックスインはコンストラクタを決して実行しないからです。

---

ミックスイン、継承、インターフェースは3つの異なる問題を解決します：

- **`extends`** はクラスに1つのスーパークラスを与えます。「〜の一種である」という関係のためのものです。枠は1つしかないので、最も強い関係に使うべきです。
- **`with`** は多くの無関係なクラスが必要とする振る舞いを追加します。数に制限はなく、実装はコピーされるのではなく共有されます。
- **`implements`** はメンバーの集合を約束しますが、実装は**何も**もたらしません。すべてのクラスが本体を自分で書かなければなりません。

ミックスインが欲しいというサインは、自然な共通の親を持たないクラスにコピーしてしまいそうなメソッドがあることです。たとえば `Duck`、`Plane`、`Kite` がみんな同じ `fly` を必要とするような場合です。

---

ミックスインの積み重ねは、小さな独立したルールを1つのクラスに組み合わせる方法です。各ミックスインは同じメンバーを上書きし、自分の役割を果たし、`super` を呼び出して仕事を次へ渡します。呼び出しは**最後の**ミックスインに最初に入るため、`with` リストの順序がどのルールをどのルールより先に走らせるかを決めます：

```dart
class Account {
  int balance = 0;

  void deposit(int amount) {
    balance += amount;
  }
}

mixin Doubled on Account {
  @override
  void deposit(int amount) {
    super.deposit(amount * 2);
  }
}
```

`class A extends Account with Doubled {}` はすべての入金を2倍にします。`Doubled` の後にもう1つミックスインを追加すると、`Doubled` が見る前にそのミックスインが入金を最初に受け取ります。
