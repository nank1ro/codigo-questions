A **class** is a blueprint for creating objects. In Dart, you define a class with the `class` keyword followed by the class name and a pair of curly braces:

```dart
class Animal {
  // fields and methods go here
}
```

By convention, class names use **PascalCase** (each word starts with a capital letter).

---

A class can have **instance variables** (also called fields) that hold data for each object. You declare them inside the class body:

```dart
class Animal {
  String name;
  int age;
}
```

Each object created from this class will have its own `name` and `age`.

---

A **constructor** is a special method that runs when you create (instantiate) an object from a class. The constructor has the same name as the class:

```dart
class Animal {
  String name;

  Animal(String name) {
    this.name = name;
  }
}
```

You create an object using the `new` keyword (optional in Dart) or just the class name:

```dart
var dog = Animal('Rex');
```

---

Dart offers a shorthand syntax for constructors that automatically assigns parameters to instance variables. Instead of:

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

You can write:

```dart
class Point {
  int x;
  int y;

  Point(this.x, this.y);
}
```

This shorter form is called **initializing formals**.

---

A **method** is a function defined inside a class. Methods describe the behaviour of an object:

```dart
class Animal {
  String name;

  Animal(this.name);

  void speak() {
    print('$name makes a sound.');
  }
}
```

You call a method on an object using dot notation: `dog.speak()`.

---

`this` refers to the **current instance** of the class. It is used to distinguish between instance variables and parameters that have the same name:

```dart
class Circle {
  double radius;

  Circle(double radius) {
    this.radius = radius;
  }
}
```

Here `this.radius` refers to the field, while `radius` (without `this`) refers to the constructor parameter.

---

Dart supports **named constructors**, which let you define additional ways to create an object. Named constructors are written as `ClassName.constructorName`:

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

You can then create an object at the origin with: `var p = Point.origin();`

---

A **getter** is a special method that reads a computed or private value and looks like a property access. You define it with the `get` keyword:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double get area => 3.14159 * radius * radius;
}
```

You access a getter like a field: `circle.area` (no parentheses).

---

A **setter** is a special method that lets you assign a value while running validation logic. You define it with the `set` keyword:

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

The field name is often prefixed with `_` to mark it as private.

---

**Inheritance** allows a class (the **subclass**) to extend another class (the **superclass**) and reuse its fields and methods. Use the `extends` keyword:

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

`Dog` inherits `name` from `Animal` and overrides `speak`.

---

When a subclass constructor needs to call the superclass constructor, use the `super` keyword in the **initializer list**:

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

`super(brand)` forwards the `brand` argument to `Vehicle`'s constructor.

---

**Method overriding** allows a subclass to provide its own implementation of a method that already exists in the superclass. Use the `@override` annotation:

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

The `@override` annotation tells Dart (and other developers) that you are intentionally replacing the superclass method.

---

An **abstract class** is a class that cannot be instantiated directly. It is used as a base that defines a contract — methods that must be implemented by subclasses. You mark abstract methods by omitting the body:

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

Trying to instantiate `Shape()` directly results in an error.

---

**Static members** belong to the class itself rather than to any particular instance. You declare them with the `static` keyword and access them directly on the class:

```dart
class MathHelper {
  static const double pi = 3.14159;

  static double circleArea(double r) => pi * r * r;
}

// access without creating an object:
print(MathHelper.pi);
print(MathHelper.circleArea(5));
```

Static fields and methods are shared by all instances.

---

A **factory constructor** uses the `factory` keyword and allows you to control object creation — for example, returning a cached instance or a subtype:

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() => _instance;

  Logger._internal();
}
```

Each call to `Logger()` returns the same instance (singleton pattern).
