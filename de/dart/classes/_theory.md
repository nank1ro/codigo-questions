Eine **Klasse** ist eine Vorlage zum Erstellen von Objekten. Sie fasst zusammengehörige Daten (Felder) und Verhalten (Methoden) zusammen.

In Dart deklarierst du eine Klasse mit dem Schlüsselwort `class`, gefolgt vom Klassennamen (konventionell in PascalCase):

```dart
class Car {
  String brand = 'Toyota';
}
```

Du erstellst eine **Instanz** (Objekt) der Klasse so:

```dart
final car = Car();
print(car.brand); // Toyota
```

---

Ein **Konstruktor** ist eine spezielle Methode, die ausgeführt wird, wenn du eine Instanz einer Klasse erstellst. Er wird verwendet, um die Felder des Objekts zu initialisieren.

In Dart verwendet der einfachste Konstruktor die **Kurzschreibweise** `this.feldName`, um Parameter direkt den Feldern zuzuweisen:

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

Eine **Methode** ist eine Funktion, die innerhalb einer Klasse definiert ist. Methoden beschreiben das Verhalten eines Objekts.

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

Methoden können direkt über den Namen auf die eigenen Felder des Objekts zugreifen (oder über `this.feldName`).

---

Ein **Getter** ist eine spezielle Methode, die wie eine Eigenschaft aufgerufen wird. Verwende das Schlüsselwort `get`, um einen zu definieren:

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double get area => 3.14 * radius * radius;
}

void main() {
  final c = Circle(5);
  print(c.area); // wie ein Feld aufgerufen, nicht als Methodenaufruf
}
```

Getter sind nützlich für berechnete Werte, die aus Feldern abgeleitet werden.

---

**Vererbung** ermöglicht es einer Klasse, die Felder und Methoden einer anderen Klasse wiederzuverwenden. Verwende das Schlüsselwort `extends`, um eine Unterklasse (Kindklasse) zu erstellen:

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

Die Kindklasse ruft den Elternkonstruktor mit `super(...)` auf. Die Annotation `@override` kennzeichnet, dass die Methode die Version des Elternteils ersetzt.
