**クラス**はオブジェクトを作成するための設計図です。Dartでは、`class`キーワードの後にクラス名と波括弧のペアを書いてクラスを定義します:

```dart
class Animal {
  // fields and methods go here
}
```

慣例として、クラス名には**PascalCase**（各単語の先頭を大文字にする）を使います。

---

クラスは各オブジェクトのデータを保持する**インスタンス変数**（フィールドとも呼ばれます）を持つことができます。クラス本体の中で宣言し、それぞれに初期値を与えます:

```dart
class Animal {
  String name = '';
  int age = 0;
}
```

このクラスから作成される各オブジェクトは、それぞれ独自の`name`と`age`を持ちます。

---

**コンストラクタ**は、クラスからオブジェクトを作成（インスタンス化）するときに実行される特別なメソッドです。コンストラクタはクラスと同じ名前を持ちます:

```dart
class Animal {
  String name;

  Animal(this.name);
}
```

`this.name`と書かれたパラメータは、コンストラクタに渡された値を新しいオブジェクトのフィールド`name`に直接格納します。この方法で設定されるフィールドには初期値が不要です。

オブジェクトは`new`キーワード（Dartでは省略可能）を使うか、クラス名だけで作成します:

```dart
var dog = Animal('Rex');
```

---

前の演習で見た`this.x`パラメータは省略記法です。長い形式では、コンストラクタ本体の中で各パラメータをそのフィールドに代入します（`this.x`がフィールド、`x`がパラメータです）:

```dart
class Point {
  int x = 0;
  int y = 0;

  Point(int x, int y) {
    this.x = x;
    this.y = y;
  }
}
```

同じクラスは次のように書くこともできます:

```dart
class Point {
  int x;
  int y;

  Point(this.x, this.y);
}
```

この短い形式は**initializing formals**と呼ばれます。

---

**メソッド**はクラスの中で定義される関数です。メソッドはオブジェクトの振る舞いを表します:

```dart
class Animal {
  String name;

  Animal(this.name);

  void speak() {
    print('$name makes a sound.');
  }
}
```

メソッドはドット記法でオブジェクトに対して呼び出します: `dog.speak()`。

---

`this`はクラスの**現在のインスタンス**、つまりメソッドが呼び出されたオブジェクトを指します。メソッドの中でこれを使ってオブジェクト自身のフィールドにアクセスできます:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double diameter() {
    return this.radius * 2;
  }
}
```

ここで`this.radius`は、`diameter()`が呼び出されたcircleの`radius`フィールドを読み取ります。同じ名前の他の変数がない場合、`this.`は省略できます: `radius * 2`でも同じように動作します。

---

Dartは**名前付きコンストラクタ**をサポートしており、オブジェクトを作成する追加の方法を定義できます。名前付きコンストラクタは`ClassName.constructorName`のように書きます:

```dart
class Point {
  double x;
  double y;

  Point(this.x, this.y);

  Point.origin()
      : x = 0,
        y = 0;
}
```

コロンの後の部分は**初期化リスト**です。コンストラクタ本体が実行される前にフィールドを代入します。これにより、原点にオブジェクトを作成できます: `var p = Point.origin();`

---

**ゲッター**は、計算された値やプライベートな値を読み取り、プロパティアクセスのように見える特別なメソッドです。`get`キーワードで定義します:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double get area => 3.14159 * radius * radius;
}
```

ゲッターはフィールドのようにアクセスします: `circle.area`（括弧なし）。

アロー`=> expr`は、値を返すだけの本体`{ return expr; }`の省略記法です。ゲッターだけでなく、任意の関数やメソッドでも使えます:

```dart
double half(double n) => n / 2;
```

---

**セッター**は、検証ロジックを実行しながら値を代入できる特別なメソッドです。`set`キーワードで定義します:

```dart
class Temperature {
  double _celsius = 0;

  double get celsius => _celsius;

  set celsius(double value) {
    if (value < -273.15) throw ArgumentError('Too cold!');
    _celsius = value;
  }
}
```

プライベートであることを示すため、フィールド名の先頭には`_`を付けることがよくあります。

---

**継承**により、あるクラス（**サブクラス**）は別のクラス（**スーパークラス**）を拡張して、そのフィールドやメソッドを再利用できます。`extends`キーワードを使います:

```dart
class Animal {
  String name = 'animal';

  void speak() {
    print('$name makes a sound.');
  }
}

class Dog extends Animal {
  void fetch() {
    print('$name fetches the ball.');
  }
}
```

`Dog`は`Animal`から`name`と`speak()`を継承し、独自のメソッド`fetch()`を追加しています。コンストラクタを宣言しないクラスには、パラメータのないデフォルトのコンストラクタが与えられるため、`var dog = Dog();`と書いてから`dog.speak()`と`dog.fetch()`の両方を呼び出せます。

---

サブクラスのコンストラクタがスーパークラスのコンストラクタを呼び出す必要がある場合、**初期化リスト**の中で`super`キーワードを使います:

```dart
class Vehicle {
  String brand;
  Vehicle(this.brand);
}

class Car extends Vehicle {
  int doors;
  Car(String brand, this.doors) : super(brand);
}
```

`super(brand)`は`brand`引数を`Vehicle`のコンストラクタに転送します。

---

**メソッドのオーバーライド**により、サブクラスはスーパークラスにすでに存在するメソッドの独自実装を提供できます。`@override`アノテーションを使います:

```dart
class Shape {
  double area() => 0;
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

`@override`アノテーションは、意図的にスーパークラスのメソッドを置き換えていることをDart（や他の開発者）に伝えます。

---

**抽象クラス**は直接インスタンス化できないクラスです。サブクラスが実装しなければならないメソッド、つまり契約を定義する基底として使われます。本体を省略することで抽象メソッドを示します:

```dart
abstract class Shape {
  double area(); // abstract method — no body
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

`Shape()`を直接インスタンス化しようとするとエラーになります。

---

**静的メンバー**は、特定のインスタンスではなくクラス自体に属します。`static`キーワードで宣言し、クラスに対して直接アクセスします:

```dart
class MathHelper {
  static const double pi = 3.14159;

  static double circleArea(double r) => pi * r * r;
}

void main() {
  // access without creating an object:
  print(MathHelper.pi);
  print(MathHelper.circleArea(5));
}
```

静的なフィールドとメソッドは、すべてのインスタンスで共有されます。

---

**ファクトリコンストラクタ**は`factory`キーワードを使い、オブジェクトの生成を制御できるようにします。たとえば、キャッシュされたインスタンスやサブタイプを返すことができます:

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() => _instance;

  Logger._internal();
}
```

`Logger()`を呼び出すたびに、同じインスタンスが返されます（シングルトンパターン）。
