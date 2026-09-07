Una **clase** es un plano para crear objetos. En Dart, defines una clase con la palabra clave `class` seguida del nombre de la clase y un par de llaves:

```dart
class Animal {
  // fields and methods go here
}
```

Por convención, los nombres de las clases usan **PascalCase** (cada palabra empieza con mayúscula).

---

Una clase puede tener **variables de instancia** (también llamadas campos) que almacenan datos para cada objeto. Se declaran dentro del cuerpo de la clase, dando a cada una un valor inicial:

```dart
class Animal {
  String name = '';
  int age = 0;
}
```

Cada objeto creado a partir de esta clase tendrá sus propios valores de `name` y `age`.

---

Un **constructor** es un método especial que se ejecuta al crear (instanciar) un objeto a partir de una clase. El constructor tiene el mismo nombre que la clase:

```dart
class Animal {
  String name;

  Animal(this.name);
}
```

Un parámetro escrito como `this.name` almacena el valor pasado al constructor directamente en el campo `name` del nuevo objeto. Un campo asignado así no necesita un valor inicial.

Creas un objeto usando la palabra clave `new` (opcional en Dart) o simplemente el nombre de la clase:

```dart
var dog = Animal('Rex');
```

---

El parámetro `this.x` que viste en el ejercicio anterior es una forma abreviada. La forma larga asigna cada parámetro a su campo dentro del cuerpo del constructor (`this.x` es el campo, `x` es el parámetro):

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

La misma clase se puede escribir como:

```dart
class Point {
  int x;
  int y;

  Point(this.x, this.y);
}
```

Esta forma más corta se llama **parámetros formales de inicialización**.

---

Un **método** es una función definida dentro de una clase. Los métodos describen el comportamiento de un objeto:

```dart
class Animal {
  String name;

  Animal(this.name);

  void speak() {
    print('$name makes a sound.');
  }
}
```

Llamas a un método en un objeto usando la notación de punto: `dog.speak()`.

---

`this` se refiere a la **instancia actual** de la clase, es decir, el objeto sobre el que se llamó al método. Dentro de un método puedes usarlo para acceder a los propios campos del objeto:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double diameter() {
    return this.radius * 2;
  }
}
```

Aquí `this.radius` lee el campo `radius` del círculo sobre el que se llamó a `diameter()`. Cuando no hay otra variable con el mismo nombre, se puede omitir `this.`: `radius * 2` funciona igual.

---

Dart admite **constructores con nombre**, que te permiten definir formas adicionales de crear un objeto. Los constructores con nombre se escriben como `ClassName.constructorName`:

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

La parte después de los dos puntos es la **lista de inicialización**: asigna los campos antes de que se ejecute el cuerpo del constructor. Luego puedes crear un objeto en el origen con: `var p = Point.origin();`

---

Un **getter** es un método especial que lee un valor calculado o privado y se parece a un acceso a una propiedad. Se define con la palabra clave `get`:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double get area => 3.14159 * radius * radius;
}
```

Accedes a un getter como si fuera un campo: `circle.area` (sin paréntesis).

La flecha `=> expr` es una forma abreviada de un cuerpo que solo devuelve un valor: `{ return expr; }`. Funciona tanto para getters como para cualquier función o método:

```dart
double half(double n) => n / 2;
```

---

Un **setter** es un método especial que te permite asignar un valor mientras ejecuta lógica de validación. Se define con la palabra clave `set`:

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

El nombre del campo suele llevar el prefijo `_` para marcarlo como privado.

---

La **herencia** permite que una clase (la **subclase**) extienda otra clase (la **superclase**) y reutilice sus campos y métodos. Usa la palabra clave `extends`:

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

`Dog` hereda `name` y `speak()` de `Animal` y añade su propio método `fetch()`. Una clase que no declara ningún constructor obtiene uno predeterminado sin parámetros, así que puedes escribir `var dog = Dog();` y luego llamar tanto a `dog.speak()` como a `dog.fetch()`.

---

Cuando el constructor de una subclase necesita llamar al constructor de la superclase, usa la palabra clave `super` en la **lista de inicialización**:

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

`super(brand)` reenvía el argumento `brand` al constructor de `Vehicle`.

---

La **sobrescritura de métodos** permite que una subclase proporcione su propia implementación de un método que ya existe en la superclase. Usa la anotación `@override`:

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

La anotación `@override` le indica a Dart (y a otros desarrolladores) que estás reemplazando intencionalmente el método de la superclase.

---

Una **clase abstracta** es una clase que no se puede instanciar directamente. Se usa como base que define un contrato: métodos que deben ser implementados por las subclases. Marcas los métodos abstractos omitiendo el cuerpo:

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

Intentar instanciar `Shape()` directamente produce un error.

---

Los **miembros estáticos** pertenecen a la propia clase en lugar de a una instancia particular. Se declaran con la palabra clave `static` y se accede a ellos directamente desde la clase:

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

Los campos y métodos estáticos se comparten entre todas las instancias.

---

Un **constructor factory** usa la palabra clave `factory` y te permite controlar la creación de objetos, por ejemplo, devolviendo una instancia almacenada en caché o un subtipo:

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() => _instance;

  Logger._internal();
}
```

Cada llamada a `Logger()` devuelve la misma instancia (patrón singleton).
