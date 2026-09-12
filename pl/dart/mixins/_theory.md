Klasa może rozszerzać za pomocą `extend` tylko jedną nadklasę, ale bardzo często tego samego zachowania potrzebują klasy, które poza tym nie mają ze sobą nic wspólnego. **Mixin** to wielokrotnego użytku fragment zachowania, który może przejąć dowolna liczba klas.

Deklaruje się go słowem kluczowym **`mixin`**, a klasa przejmuje go słowem kluczowym **`with`**:

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish` nie deklaruje żadnych własnych składowych, a mimo to każdy `Fish` ma `swim`, ponieważ składowe mixinu stają się składowymi klasy. Z mixinu może korzystać dowolna liczba klas, spokrewnionych lub nie.

---

Ciało mixinu wygląda jak ciało klasy: metody, getter i pola zapisuje się dokładnie tak samo. Różnica polega na tym, co można zrobić z samą deklaracją.

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

Nazwa mixinu jest też **typem**, więc `Server() is Timestamped` ma wartość `true`, a zmienną można zadeklarować jako `Timestamped t = Server();`. Dwie niespokrewnione klasy współdzielą teraz jedną implementację, bez dziedziczenia po sobie.

---

Mixin nie ogranicza się do metod: może też deklarować **pola**, a każdy obiekt każdej klasy korzystającej z mixinu dostaje ich własną kopię.

```dart
mixin Counter {
  int count = 0;

  void increment() {
    count++;
  }
}

class Clicker with Counter {}

void main() {
  final a = Clicker();
  final b = Clicker();
  a.increment();
  a.increment();
  print(a.count); // 2
  print(b.count); // 0, b has its own count
}
```

To właśnie sprawia, że mixin to coś więcej niż interfejs: przynosi zarówno dane, jak i kod, który na nich działa.

---

Deklaracja `mixin` **nie** jest klasą. Istnieje wyłącznie po to, by być włączana do innych klas, więc nie ma własnego konstruktora i nie można jej instancjonować ani po niej dziedziczyć:

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

Nazwa nadal działa jako typ, więc `Team() is Scored` i `Scored s = Team();` są jak najbardziej w porządku. Mixin nie ma konstruktora, więc pole niedopuszczające wartości null musi zostać zainicjalizowane w miejscu deklaracji (lub oznaczone jako `late`), jak `int score = 0;` powyżej.

---

Mixin może zadeklarować składową **bez ciała**. Taka składowa jest abstrakcyjna: mixin z niej korzysta, a klasa przejmująca mixin musi ją dostarczyć.

```dart
mixin Greeting {
  String get name;                       // no body: the class provides it

  String greet() => 'Hello, $name!';
}

class Person with Greeting {
  @override
  final String name;

  Person(this.name);
}

void main() {
  print(Person('Ada').greet()); // Hello, Ada!
}
```

Mixin przynosi zachowanie, klasa przynosi dane. Pole w klasie, takie jak `final String name;`, wystarcza, aby spełnić abstrakcyjny getter o tej samej nazwie.

---

Składając wszystko w całość, program korzystający z mixinu ma trzy części: deklarację `mixin`, jedną lub więcej klas przejmujących go przez `with` oraz kod wywołujący współdzieloną składową.

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

Deklaracje najwyższego poziomu można w Dart zapisywać w dowolnej kolejności, ale czytanie pliku od góry do dołu jest łatwiejsze, gdy mixin poprzedza klasy, które z niego korzystają.

---

Klasa może używać **kilku mixinów naraz**, wypisanych po `with` i oddzielonych przecinkami. Dart stosuje je **od lewej do prawej**, układając każdą kolejną na poprzedniej, więc gdy dwa mixiny deklarują tę samą składową, wygrywa **ostatni** z listy:

```dart
mixin A {
  String who() => 'A';
}

mixin B {
  String who() => 'B';
}

class First with A, B {}
class Second with B, A {}

void main() {
  print(First().who());  // B, the last mixin in the list
  print(Second().who()); // A, the last mixin in the list
}
```

To układanie nazywa się **linearizacją**: `with A, B` buduje łańcuch `Object` → `A` → `B` → sama klasa.

---

Ponieważ wygrywa ostatni mixin, kolejność listy `with` jest częścią znaczenia klasy, a nie detalem stylu. Zmiana tej kolejności zmienia to, z którą implementacją skończy obiekt:

```dart
mixin Plain {
  String format(String text) => text;
}

mixin Starred {
  String format(String text) => '*$text*';
}

class Fancy with Plain, Starred {}  // format comes from Starred
class Simple with Starred, Plain {} // format comes from Plain
```

Składowe deklarowane tylko przez jeden mixin nigdy nie konkurują: są dostępne niezależnie od kolejności. Czytaj `with X, Y` jako „zacznij od `X`, a potem pozwól `Y` ją nadpisać”.

---

Mixiny i `extends` współpracują ze sobą. Klasa może mieć nadklasę **oraz** listę mixinów, a mixiny są zawsze stosowane **na wierzchu** nadklasy:

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

Łańcuch wygląda tu tak: `Object` → `Document` → `Timestamped` → `Report`. Składowa jest wyszukiwana od końca łańcucha, więc `Report().header()` znajduje najpierw wersję z `Timestamped`. Zadeklarowanie tej samej składowej w nadklasie i w mixinie jest jak najbardziej legalne: w ten sposób mixin zastępuje lub opakowuje odziedziczone zachowanie.

---

Ciało klasy znajduje się na samym końcu łańcucha, więc składowa zadeklarowana w klasie **nadpisuje** tę samą składową pochodzącą z dowolnego z jej mixinów. Wewnątrz nadpisania **`super`** sięga wersji dostarczonej przez mixin:

```dart
mixin Polite {
  String greet() => 'Hello';
}

class Host with Polite {
  @override
  String greet() => '${super.greet()}, welcome!';
}

class Guest with Polite {}

void main() {
  print(Host().greet());  // Hello, welcome!
  print(Guest().greet()); // Hello
}
```

Sam mixin pozostaje nietknięty: `Guest` nadal dostaje oryginalne `greet`. To właśnie `super.greet()` pozwala `Host` bazować na współdzielonym zachowaniu zamiast je kopiować.

---

Niektóre zachowanie ma sens tylko na wierzchu konkretnej klasy i do działania potrzebuje składowych tej klasy. Klauzula **`on`** wyraża ten wymóg:

```dart
class Animal {
  String get name => 'animal';
}

mixin Noisy on Animal {
  String shout() => '${name.toUpperCase()}!';
}

class Dog extends Animal with Noisy {
  @override
  String get name => 'dog';
}

void main() {
  print(Dog().shout()); // DOG!
}
```

`on Animal` robi dwie rzeczy: pozwala mixinowi korzystać ze składowych `Animal`, jak `name` powyżej, i ogranicza, kto może użyć mixinu. `class Rock with Noisy {}` to błąd kompilacji, ponieważ `Rock` nie jest `Animal`.

---

Mixin z klauzulą `on` czyta składowe swojej nadklasy tak, jakby były jego własnymi, co czyni go dobrym miejscem na zachowanie zdobiące istniejący typ:

```dart
class Shape {
  String get kind => 'shape';
}

mixin Printable on Shape {
  void show() {
    print('a $kind');
  }
}

class Square extends Shape with Printable {
  @override
  String get kind => 'square';
}
```

`Square` nadpisuje `kind`, a `show` automatycznie korzysta z nadpisania: mixin zawsze wywołuje składową na prawdziwym obiekcie.

---

Gdy mixin ma klauzulę `on`, może **nadpisać** składową tego typu i wywołać **`super`**, aby sięgnąć wersji znajdującej się pod nim w łańcuchu:

```dart
class Logger {
  String log(String message) => message;
}

mixin Timestamped on Logger {
  @override
  String log(String message) => '[12:00] ${super.log(message)}';
}

class AppLogger extends Logger with Timestamped {}

void main() {
  print(AppLogger().log('started')); // [12:00] started
}
```

`super.log` to nie własne `log` mixinu, tylko wersja znajdująca się pod nim, więc nie ma nieskończonej rekurencji. Ułóż kilka takich mixinów przez `with A, B`, a każdy opakuje poprzedni: wywołanie wchodzi najpierw do **ostatniego** mixinu i wędruje w dół do nadklasy.

---

Deklaracji `mixin` nie można instancjonować ani po niej dziedziczyć, a zwykłej `class` nie można użyć po `with`. Gdy potrzebujesz jednej deklaracji działającej **na oba** sposoby, napisz **`mixin class`**:

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

`mixin class` płaci za tę elastyczność dwoma ograniczeniami: musi dziedziczyć po `Object`, więc nie może mieć własnej klauzuli `extends`, i nie może deklarować konstruktora, ponieważ mixin nigdy żadnego nie uruchamia.

---

Mixiny, dziedziczenie i interfejsy rozwiązują trzy różne problemy:

- **`extends`** daje klasie jedną nadklasę, dla relacji „jest rodzajem”. Jest tylko jedno miejsce, więc powinno ono przypadnąć najsilniejszej relacji.
- **`with`** dodaje zachowanie, którego potrzebuje wiele niespokrewnionych klas. Nie ma limitu, a implementacja jest współdzielona, nie kopiowana.
- **`implements`** obiecuje zestaw składowych, ale nie przynosi **żadnej** implementacji: każda klasa musi sama napisać ciało.

Znakiem rozpoznawczym, że potrzebujesz mixinu, jest metoda, którą w przeciwnym razie skopiowałbyś do klas nie mających naturalnego wspólnego przodka, jak `Duck`, `Plane` i `Kite`, z których wszystkie potrzebują tego samego `fly`.

---

Ułożone mixiny to sposób, w jaki małe, niezależne reguły łączy się w jedną klasę. Każdy mixin nadpisuje tę samą składową, robi swoją część i wywołuje `super`, aby przekazać pracę dalej. Ponieważ wywołanie wchodzi najpierw do **ostatniego** mixinu, kolejność listy `with` decyduje, która reguła działa przed którą:

```dart
class Account {
  int balance = 0;

  void deposit(int amount) {
    balance += amount;
  }
}

mixin Doubled on Account {
  @override
  void deposit(int amount) {
    super.deposit(amount * 2);
  }
}
```

`class A extends Account with Doubled {}` podwaja każdą wpłatę. Dodaj drugi mixin za `Doubled`, a to on dostanie wpłatę pierwszy, zanim `Doubled` w ogóle ją zobaczy.
