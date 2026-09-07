A **class** is a blueprint for creating objects. In Dart, you define a class with the `class` keyword followed by the class name and a pair of curly braces:

```dart
class Animal {
  // fields and methods go here
}
```

By convention, class names use **PascalCase** (each word starts with a capital letter).

---

A class can have **instance variables** (also called fields) that hold data for each object. You declare them inside the class body, giving each one an initial value:

```dart
class Animal {
  String name = '';
  int age = 0;
}
```

Each object created from this class will have its own `name` and `age`.

---

A **constructor** is a special method that runs when you create (instantiate) an object from a class. The constructor has the same name as the class:

```dart
class Animal {
  String name;

  Animal(this.name);
}
```

A parameter written as `this.name` stores the value passed to the constructor directly into the field `name` of the new object. A field set this way does not need an initial value.

You create an object using the `new` keyword (optional in Dart) or just the class name:

```dart
var dog = Animal('Rex');
```

---

The `this.x` parameter you saw in the previous exercise is a shorthand. The long form assigns each parameter to its field inside the constructor body (`this.x` is the field, `x` is the parameter):

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

The same class can be written as:

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

`this` refers to the **current instance** of the class, that is, the object a method was called on. Inside a method you can use it to access the object's own fields:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double diameter() {
    return this.radius * 2;
  }
}
```

Here `this.radius` reads the `radius` field of the circle on which `diameter()` was called. When there is no other variable with the same name, `this.` can be omitted: `radius * 2` works the same.

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

The part after the colon is the **initializer list**: it assigns the fields before the constructor body runs. You can then create an object at the origin with: `var p = Point.origin();`

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

The arrow `=> expr` is a shorthand for a body that only returns a value: `{ return expr; }`. It works for getters and for any function or method:

```dart
double half(double n) => n / 2;
```

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

`Dog` inherits `name` and `speak()` from `Animal` and adds its own method `fetch()`. A class that declares no constructor gets a default one with no parameters, so you can write `var dog = Dog();` and then call both `dog.speak()` and `dog.fetch()`.

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

void main() {
  // access without creating an object:
  print(MathHelper.pi);
  print(MathHelper.circleArea(5));
}
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
