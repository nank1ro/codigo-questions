**类**是创建对象的蓝图。在 Dart 中，使用 `class` 关键字、类名以及一对花括号来定义类：

```dart
class Animal {
  // 字段和方法
}
```

按照惯例，类名使用 **PascalCase** 命名法（每个单词首字母大写）。

---

类可以拥有**实例变量**（也称为字段），用于保存每个对象的数据。在类体内部声明它们：

```dart
class Animal {
  String name;
  int age;
}
```

从该类创建的每个对象都有自己的 `name` 和 `age` 字段。

---

**构造函数**是在从类创建（实例化）对象时运行的特殊方法。构造函数与类同名：

```dart
class Animal {
  String name;

  Animal(String name) {
    this.name = name;
  }
}
```

使用 `new` 关键字（在 Dart 中可省略）或直接用类名创建对象：

```dart
var dog = Animal('Rex');
```

---

Dart 提供了一种构造函数简写语法，可以自动将参数赋值给实例变量。代替以下写法：

```dart
class Point {
  int x;
  int y;

  Point(int x, int y) {
    this.x = x;
    this.y = y;
  }
}
```

可以写成：

```dart
class Point {
  int x;
  int y;

  Point(this.x, this.y);
}
```

这种更简短的形式称为**初始化形式参数**。

---

**方法**是定义在类内部的函数。方法描述对象的行为：

```dart
class Animal {
  String name;

  Animal(this.name);

  void speak() {
    print('$name 发出声音。');
  }
}
```

使用点符号在对象上调用方法：`dog.speak()`。

---

`this` 指向类的**当前实例**。它用于区分实例变量和同名参数：

```dart
class Circle {
  double radius;

  Circle(double radius) {
    this.radius = radius;
  }
}
```

此处 `this.radius` 指字段，而 `radius`（不带 `this`）指构造函数参数。

---

Dart 支持**命名构造函数**，可以定义创建对象的额外方式。命名构造函数写作 `类名.构造函数名`：

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

然后可以用 `var p = Point.origin();` 创建原点处的对象。

---

**getter** 是一种特殊方法，用于读取计算值或私有值，访问方式与属性相同。使用 `get` 关键字定义：

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double get area => 3.14159 * radius * radius;
}
```

像访问字段一样访问 getter：`circle.area`（无括号）。

---

**setter** 是一种特殊方法，允许在赋值时执行验证逻辑。使用 `set` 关键字定义：

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

字段名通常以 `_` 开头，表示它是私有的。

---

**继承**允许一个类（**子类**）扩展另一个类（**父类**）并复用其字段和方法。使用 `extends` 关键字：

```dart
class Animal {
  String name;
  Animal(this.name);

  void speak() {
    print('...');
  }
}

class Dog extends Animal {
  Dog(String name) : super(name);

  @override
  void speak() {
    print('Woof!');
  }
}
```

`Dog` 从 `Animal` 继承 `name` 并重写 `speak` 方法。

---

当子类构造函数需要调用父类构造函数时，在**初始化列表**中使用 `super` 关键字：

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

`super(brand)` 将 `brand` 参数传递给 `Vehicle` 的构造函数。

---

**方法重写**允许子类提供父类中已有方法的自定义实现。使用 `@override` 注解：

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

`@override` 注解告知 Dart（及其他开发者）你有意替换父类方法。

---

**抽象类**是不能直接实例化的类。它作为基类定义契约——子类必须实现的方法。抽象方法通过省略方法体来标记：

```dart
abstract class Shape {
  double area(); // 抽象方法——无方法体
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

直接实例化 `Shape()` 会导致错误。

---

**静态成员**属于类本身，而不属于任何特定实例。使用 `static` 关键字声明，直接通过类名访问：

```dart
class MathHelper {
  static const double pi = 3.14159;

  static double circleArea(double r) => pi * r * r;
}

// 无需创建对象即可访问：
print(MathHelper.pi);
print(MathHelper.circleArea(5));
```

静态字段和方法由所有实例共享。

---

**工厂构造函数**使用 `factory` 关键字，允许控制对象的创建——例如返回缓存的实例或子类型：

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() => _instance;

  Logger._internal();
}
```

每次调用 `Logger()` 都返回同一个实例（单例模式）。
