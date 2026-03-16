Una **clase** es una plantilla para crear objetos. Agrupa datos relacionados (campos) y comportamiento (métodos) juntos.

En Dart, declaras una clase con la palabra clave `class` seguida del nombre de la clase (por convención, PascalCase):

```dart
class Car {
  String brand = 'Toyota';
}
```

Creas una **instancia** (objeto) de la clase así:

```dart
final car = Car();
print(car.brand); // Toyota
```

---

Un **constructor** es un método especial que se ejecuta cuando creas una instancia de una clase. Se usa para inicializar los campos del objeto.

En Dart, el constructor más simple usa la **sintaxis abreviada** `this.nombreCampo` para asignar parámetros directamente a los campos:

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

Un **método** es una función definida dentro de una clase. Los métodos describen el comportamiento de un objeto.

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

Los métodos pueden acceder directamente a los campos del propio objeto por nombre (o mediante `this.nombreCampo`).

---

Un **getter** es un método especial que parece una propiedad cuando se accede a él. Usa la palabra clave `get` para definir uno:

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double get area => 3.14 * radius * radius;
}

void main() {
  final c = Circle(5);
  print(c.area); // accedido como un campo, no como una llamada a método
}
```

Los getters son útiles para valores calculados derivados de campos.

---

La **herencia** permite que una clase reutilice los campos y métodos de otra clase. Usa la palabra clave `extends` para crear una subclase (clase hija):

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

La clase hija llama al constructor padre con `super(...)`. La anotación `@override` indica que el método reemplaza la versión del padre.
