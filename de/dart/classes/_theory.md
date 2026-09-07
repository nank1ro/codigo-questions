Eine **Klasse** ist eine Vorlage zum Erstellen von Objekten. In Dart definierst du eine Klasse mit dem Schlüsselwort `class`, gefolgt vom Klassennamen und einem Paar geschweifter Klammern:

```dart
class Animal {
  // fields and methods go here
}
```

Nach Konvention verwenden Klassennamen **PascalCase** (jedes Wort beginnt mit einem Großbuchstaben).

---

Eine Klasse kann **Instanzvariablen** (auch Felder genannt) haben, die Daten für jedes Objekt speichern. Du deklarierst sie im Klassenkörper und gibst jeder einen Anfangswert:

```dart
class Animal {
  String name = '';
  int age = 0;
}
```

Jedes aus dieser Klasse erstellte Objekt hat seine eigenen `name`- und `age`-Werte.

---

Ein **Konstruktor** ist eine spezielle Methode, die ausgeführt wird, wenn du ein Objekt aus einer Klasse erstellst (instanziierst). Der Konstruktor trägt denselben Namen wie die Klasse:

```dart
class Animal {
  String name;

  Animal(this.name);
}
```

Ein Parameter, der als `this.name` geschrieben wird, speichert den an den Konstruktor übergebenen Wert direkt im Feld `name` des neuen Objekts. Ein so gesetztes Feld benötigt keinen Anfangswert.

Du erstellst ein Objekt mit dem Schlüsselwort `new` (in Dart optional) oder einfach mit dem Klassennamen:

```dart
var dog = Animal('Rex');
```

---

Der Parameter `this.x`, den du in der vorherigen Übung gesehen hast, ist eine Kurzschreibweise. Die lange Form weist jeden Parameter im Konstruktorkörper seinem Feld zu (`this.x` ist das Feld, `x` ist der Parameter):

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

Dieselbe Klasse kann so geschrieben werden:

```dart
class Point {
  int x;
  int y;

  Point(this.x, this.y);
}
```

Diese kürzere Form wird **initialisierende Formalparameter** genannt.

---

Eine **Methode** ist eine Funktion, die innerhalb einer Klasse definiert ist. Methoden beschreiben das Verhalten eines Objekts:

```dart
class Animal {
  String name;

  Animal(this.name);

  void speak() {
    print('$name makes a sound.');
  }
}
```

Du rufst eine Methode auf einem Objekt mit Punktnotation auf: `dog.speak()`.

---

`this` bezieht sich auf die **aktuelle Instanz** der Klasse, also das Objekt, auf dem eine Methode aufgerufen wurde. Innerhalb einer Methode kannst du damit auf die eigenen Felder des Objekts zugreifen:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double diameter() {
    return this.radius * 2;
  }
}
```

Hier liest `this.radius` das Feld `radius` des Kreises, auf dem `diameter()` aufgerufen wurde. Wenn es keine andere Variable mit demselben Namen gibt, kann `this.` weggelassen werden: `radius * 2` funktioniert genauso.

---

Dart unterstützt **benannte Konstruktoren**, mit denen du zusätzliche Möglichkeiten definieren kannst, ein Objekt zu erstellen. Benannte Konstruktoren werden als `ClassName.constructorName` geschrieben:

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

Der Teil nach dem Doppelpunkt ist die **Initialisierungsliste**: Sie weist die Felder zu, bevor der Konstruktorkörper ausgeführt wird. Du kannst dann ein Objekt am Ursprung mit `var p = Point.origin();` erstellen.

---

Ein **Getter** ist eine spezielle Methode, die einen berechneten oder privaten Wert liest und wie ein Feldzugriff aussieht. Du definierst ihn mit dem Schlüsselwort `get`:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double get area => 3.14159 * radius * radius;
}
```

Du greifst auf einen Getter wie auf ein Feld zu: `circle.area` (ohne Klammern).

Der Pfeil `=> expr` ist eine Kurzschreibweise für einen Körper, der nur einen Wert zurückgibt: `{ return expr; }`. Er funktioniert für Getter und für jede Funktion oder Methode:

```dart
double half(double n) => n / 2;
```

---

Ein **Setter** ist eine spezielle Methode, mit der du einen Wert zuweisen kannst, während eine Validierungslogik ausgeführt wird. Du definierst ihn mit dem Schlüsselwort `set`:

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

Der Feldname wird oft mit `_` versehen, um ihn als privat zu kennzeichnen.

---

**Vererbung** erlaubt es einer Klasse (der **Unterklasse**), eine andere Klasse (die **Oberklasse**) zu erweitern und deren Felder und Methoden wiederzuverwenden. Verwende das Schlüsselwort `extends`:

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

`Dog` erbt `name` und `speak()` von `Animal` und fügt seine eigene Methode `fetch()` hinzu. Eine Klasse, die keinen Konstruktor deklariert, erhält einen Standardkonstruktor ohne Parameter, sodass du `var dog = Dog();` schreiben und anschließend sowohl `dog.speak()` als auch `dog.fetch()` aufrufen kannst.

---

Wenn ein Unterklassen-Konstruktor den Oberklassen-Konstruktor aufrufen muss, verwende das Schlüsselwort `super` in der **Initialisierungsliste**:

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

`super(brand)` leitet das Argument `brand` an den Konstruktor von `Vehicle` weiter.

---

**Methodenüberschreibung** erlaubt es einer Unterklasse, eine eigene Implementierung einer Methode bereitzustellen, die bereits in der Oberklasse existiert. Verwende die Annotation `@override`:

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

Die Annotation `@override` teilt Dart (und anderen Entwicklern) mit, dass du die Methode der Oberklasse absichtlich ersetzt.

---

Eine **abstrakte Klasse** ist eine Klasse, die nicht direkt instanziiert werden kann. Sie dient als Basis, die einen Vertrag definiert — Methoden, die von Unterklassen implementiert werden müssen. Du kennzeichnest abstrakte Methoden, indem du den Körper weglässt:

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

Der Versuch, `Shape()` direkt zu instanziieren, führt zu einem Fehler.

---

**Statische Member** gehören zur Klasse selbst und nicht zu einer bestimmten Instanz. Du deklarierst sie mit dem Schlüsselwort `static` und greifst direkt über die Klasse darauf zu:

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

Statische Felder und Methoden werden von allen Instanzen gemeinsam genutzt.

---

Ein **Factory-Konstruktor** verwendet das Schlüsselwort `factory` und ermöglicht es dir, die Objekterstellung zu steuern — zum Beispiel um eine zwischengespeicherte Instanz oder einen Subtyp zurückzugeben:

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() => _instance;

  Logger._internal();
}
```

Jeder Aufruf von `Logger()` gibt dieselbe Instanz zurück (Singleton-Muster).
