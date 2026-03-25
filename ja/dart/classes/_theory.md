**クラス**はオブジェクトを作成するための設計図です。関連するデータ（フィールド）と振る舞い（メソッド）をまとめます。

Dartでは、`class`キーワードの後にクラス名（慣例としてPascalCase）を書いてクラスを宣言します:

```dart
class Car {
  String brand = 'Toyota';
}
```

クラスの**インスタンス**（オブジェクト）はこのように作成します:

```dart
final car = Car();
print(car.brand); // Toyota
```

---

**コンストラクタ**はクラスのインスタンスを作成するときに実行される特別なメソッドです。オブジェクトのフィールドを初期化するために使用します。

Dartでは、最もシンプルなコンストラクタはパラメータをフィールドに直接代入する**省略記法** `this.fieldName`を使います:

```dart
class Car {
  String brand;
  Car(this.brand);
}

void main() {
  final car = Car('Toyota');
  print(car.brand); // Toyota
}
```

---

**メソッド**はクラスの中で定義された関数です。メソッドはオブジェクトの振る舞いを表します。

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double area() {
    return 3.14 * radius * radius;
  }
}

void main() {
  final c = Circle(5);
  print(c.area()); // 78.5
}
```

メソッドはオブジェクト自身のフィールドに、名前を直接使って（または`this.fieldName`で）アクセスできます。

---

**ゲッター**はアクセスするときにプロパティのように見える特別なメソッドです。`get`キーワードを使って定義します:

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double get area => 3.14 * radius * radius;
}

void main() {
  final c = Circle(5);
  print(c.area); // フィールドのようにアクセスし、メソッド呼び出しではない
}
```

ゲッターはフィールドから計算された値に便利です。

---

**継承**を使うと、あるクラスが別のクラスのフィールドとメソッドを再利用できます。`extends`キーワードを使ってサブクラス（子クラス）を作成します:

```dart
class Animal {
  String name;
  Animal(this.name);

  void speak() {
    print('...');
  }
}

class Cat extends Animal {
  Cat(String name) : super(name);

  @override
  void speak() {
    print('Meow');
  }
}
```

子クラスは`super(...)`で親コンストラクタを呼び出します。`@override`アノテーションはそのメソッドが親のバージョンを上書きすることを示します。
