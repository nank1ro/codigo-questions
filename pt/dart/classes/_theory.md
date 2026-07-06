Uma **classe** é um modelo para criar objetos. Ela agrupa dados relacionados (campos) e comportamentos (métodos) juntos.

Em Dart, você declara uma classe com a palavra-chave `class` seguida do nome da classe (por convenção, PascalCase):

```dart
class Car {
  String brand = 'Toyota';
}
```

Você cria uma **instância** (objeto) da classe assim:

```dart
final car = Car();
print(car.brand); // Toyota
```

---

Um **construtor** é um método especial que é executado quando você cria uma instância de uma classe. Ele é usado para inicializar os campos do objeto.

Em Dart, o construtor mais simples usa a **abreviação** `this.fieldName` para atribuir parâmetros diretamente aos campos:

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

Um **método** é uma função definida dentro de uma classe. Os métodos descrevem o comportamento de um objeto.

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

Os métodos podem acessar os próprios campos do objeto diretamente pelo nome (ou via `this.fieldName`).

---

Um **getter** é um método especial que parece uma propriedade quando acessado. Use a palavra-chave `get` para definir um:

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double get area => 3.14 * radius * radius;
}

void main() {
  final c = Circle(5);
  print(c.area); // acessado como um campo, não como uma chamada de método
}
```

Os getters são úteis para valores calculados derivados de campos.

---

A **herança** permite que uma classe reutilize os campos e métodos de outra classe. Use a palavra-chave `extends` para criar uma subclasse (classe filha):

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

A classe filha chama o construtor pai com `super(...)`. A anotação `@override` marca que o método substitui a versão do pai.
