**Klasa** to szablon do tworzenia obiektów. W Darcie klasę definiuje się za pomocą słowa kluczowego `class`, po którym podaje się nazwę klasy i parę nawiasów klamrowych:

```dart
class Animal {
  // pola i metody
}
```

Zgodnie z konwencją nazwy klas używają notacji **PascalCase** (każde słowo zaczyna się wielką literą).

---

Klasa może mieć **zmienne instancji** (zwane też polami), które przechowują dane każdego obiektu. Deklaruje się je wewnątrz ciała klasy, nadając każdemu wartość początkową:

```dart
class Animal {
  String name = '';
  int age = 0;
}
```

Każdy obiekt stworzony z tej klasy będzie miał własne pola `name` i `age`.

---

**Konstruktor** to specjalna metoda wywoływana podczas tworzenia (instancjowania) obiektu klasy. Konstruktor ma taką samą nazwę jak klasa:

```dart
class Animal {
  String name;

  Animal(this.name);
}
```

Parametr zapisany jako `this.name` zapisuje wartość przekazaną do konstruktora bezpośrednio w polu `name` nowego obiektu. Pole ustawiane w ten sposób nie wymaga wartości początkowej.

Obiekt tworzy się za pomocą słowa kluczowego `new` (opcjonalnego w Darcie) lub bezpośrednio nazwy klasy:

```dart
var dog = Animal('Rex');
```

---

Parametr `this.x`, który widziałeś w poprzednim ćwiczeniu, to skrót. Dłuższa forma przypisuje każdy parametr do jego pola w ciele konstruktora (`this.x` to pole, `x` to parametr):

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

Tę samą klasę można zapisać jako:

```dart
class Point {
  int x;
  int y;

  Point(this.x, this.y);
}
```

Ta krótsza forma nosi nazwę **inicjalizujących parametrów formalnych**.

---

**Metoda** to funkcja zdefiniowana wewnątrz klasy. Metody opisują zachowanie obiektu:

```dart
class Animal {
  String name;

  Animal(this.name);

  void speak() {
    print('$name wydaje dźwięk.');
  }
}
```

Metodę wywołuje się na obiekcie za pomocą notacji kropkowej: `dog.speak()`.

---

`this` odnosi się do **bieżącej instancji** klasy, czyli obiektu, na którym wywołano metodę. Wewnątrz metody można go użyć, aby uzyskać dostęp do pól tego obiektu:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double diameter() {
    return this.radius * 2;
  }
}
```

Tutaj `this.radius` odczytuje pole `radius` okręgu, na którym wywołano `diameter()`. Gdy nie ma innej zmiennej o tej samej nazwie, `this.` można pominąć: `radius * 2` działa tak samo.

---

Dart obsługuje **nazwane konstruktory**, które umożliwiają definiowanie dodatkowych sposobów tworzenia obiektu. Nazwane konstruktory zapisuje się jako `NazwaKlasy.nazwaKonstruktora`:

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

Część po dwukropku to **lista inicjalizacyjna**: przypisuje pola, zanim wykona się ciało konstruktora. Obiekt w początku układu współrzędnych tworzy się wówczas za pomocą: `var p = Point.origin();`

---

**Getter** to specjalna metoda odczytująca obliczoną lub prywatną wartość, wyglądająca jak dostęp do właściwości. Definiuje się ją za pomocą słowa kluczowego `get`:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double get area => 3.14159 * radius * radius;
}
```

Do gettera odwołuje się jak do pola: `circle.area` (bez nawiasów).

Strzałka `=> expr` to skrót dla ciała, które tylko zwraca wartość: `{ return expr; }`. Działa dla getterów oraz dla dowolnej funkcji lub metody:

```dart
double half(double n) => n / 2;
```

---

**Setter** to specjalna metoda pozwalająca przypisać wartość z jednoczesnym uruchomieniem logiki walidacji. Definiuje się ją za pomocą słowa kluczowego `set`:

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

Nazwa pola jest często poprzedzona znakiem `_`, co oznacza, że jest prywatna.

---

**Dziedziczenie** pozwala klasie (**podklasie**) rozszerzyć inną klasę (**nadklasę**) i ponownie używać jej pól oraz metod. Służy do tego słowo kluczowe `extends`:

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

`Dog` dziedziczy `name` i `speak()` od `Animal` i dodaje własną metodę `fetch()`. Klasa, która nie deklaruje konstruktora, otrzymuje domyślny konstruktor bez parametrów, więc można napisać `var dog = Dog();`, a następnie wywołać zarówno `dog.speak()`, jak i `dog.fetch()`.

---

Gdy konstruktor podklasy musi wywołać konstruktor nadklasy, używa się słowa kluczowego `super` na **liście inicjalizacyjnej**:

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

`super(brand)` przekazuje argument `brand` do konstruktora klasy `Vehicle`.

---

**Nadpisywanie metod** pozwala podklasie na dostarczenie własnej implementacji metody, która już istnieje w nadklasie. Używa się do tego adnotacji `@override`:

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

Adnotacja `@override` informuje Dart (i innych programistów), że celowo zastępujesz metodę nadklasy.

---

**Klasa abstrakcyjna** to klasa, której nie można bezpośrednio instancjować. Służy jako baza definiująca kontrakt — metody, które muszą być zaimplementowane przez podklasy. Metody abstrakcyjne oznacza się brakiem ciała:

```dart
abstract class Shape {
  double area(); // metoda abstrakcyjna — bez ciała
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

Próba bezpośredniego instancjowania `Shape()` powoduje błąd.

---

**Statyczne składowe** należą do samej klasy, a nie do konkretnej instancji. Deklaruje się je za pomocą słowa kluczowego `static` i odwołuje się do nich bezpośrednio przez nazwę klasy:

```dart
class MathHelper {
  static const double pi = 3.14159;

  static double circleArea(double r) => pi * r * r;
}

void main() {
  // dostęp bez tworzenia obiektu:
  print(MathHelper.pi);
  print(MathHelper.circleArea(5));
}
```

Statyczne pola i metody są współdzielone przez wszystkie instancje.

---

**Konstruktor fabryczny** używa słowa kluczowego `factory` i pozwala kontrolować tworzenie obiektów — na przykład zwracać buforowaną instancję lub podtyp:

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() => _instance;

  Logger._internal();
}
```

Każde wywołanie `Logger()` zwraca tę samą instancję (wzorzec singleton).
