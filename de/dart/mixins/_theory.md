Eine Klasse kann nur eine Oberklasse `extend`en, aber oft brauchen genau dasselbe Verhalten Klassen, die sonst nichts gemeinsam haben. Ein **Mixin** ist ein wiederverwendbares Stück Verhalten, das beliebig viele Klassen aufnehmen können.

Du deklarierst eines mit dem Schlüsselwort **`mixin`**, und eine Klasse nimmt es mit dem Schlüsselwort **`with`** auf:

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish` deklariert keine eigenen Member, und trotzdem hat jedes `Fish` `swim`, denn die Member des Mixins werden Member der Klasse. Ein Mixin kann von so vielen Klassen verwendet werden, wie du möchtest — verwandt oder nicht.

---

Der Körper eines Mixins sieht aus wie der Körper einer Klasse: Methoden, Getter und Felder, geschrieben auf genau dieselbe Weise. Der Unterschied liegt darin, was du mit der Deklaration selbst machen kannst.

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

Der Name eines Mixins ist auch ein **Typ**, daher ist `Server() is Timestamped` gleich `true`, und eine Variable kann als `Timestamped t = Server();` deklariert werden. Zwei nicht verwandte Klassen teilen sich nun eine Implementierung, ohne dass eine von der anderen erbt.

---

Ein Mixin ist nicht auf Methoden beschränkt: Es kann auch **Felder** deklarieren, und jedes Objekt jeder Klasse, die das Mixin verwendet, bekommt seine eigene Kopie davon.

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

Das macht ein Mixin zu mehr als einer Schnittstelle: Es bringt sowohl die Daten mit als auch den Code, der mit ihnen arbeitet.

---

Eine `mixin`-Deklaration ist **keine** Klasse. Sie existiert nur, um in andere Klassen eingemischt zu werden, daher hat sie keinen eigenen Konstruktor und kann weder instanziiert noch erweitert werden:

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

Der Name funktioniert trotzdem als Typ, daher sind `Team() is Scored` und `Scored s = Team();` beide in Ordnung. Ein Mixin hat keinen Konstruktor, daher muss ein nicht-nullable Feld dort initialisiert werden, wo es deklariert wird (oder als `late` markiert sein), wie `int score = 0;` oben.

---

Ein Mixin kann ein Member **ohne Körper** deklarieren. So ein Member ist abstrakt: Das Mixin verwendet es, und die Klasse, die das Mixin aufnimmt, muss es bereitstellen.

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

Das Mixin bringt das Verhalten mit, die Klasse bringt die Daten. Ein Feld in der Klasse, wie `final String name;`, genügt, um einen abstrakten Getter desselben Namens zu erfüllen.

---

Fügen wir die Teile zusammen: Ein Programm, das ein Mixin verwendet, hat drei Teile — die `mixin`-Deklaration, eine oder mehrere Klassen, die es mit `with` aufnehmen, und den Code, der das gemeinsame Member aufruft.

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

Top-Level-Deklarationen kann man in Dart in beliebiger Reihenfolge schreiben, aber eine Datei von oben nach unten zu lesen fällt leichter, wenn das Mixin vor den Klassen kommt, die es verwenden.

---

Eine Klasse kann **mehrere Mixins auf einmal** verwenden, aufgelistet nach `with` und durch Kommas getrennt. Dart wendet sie **von links nach rechts** an und stapelt jedes auf das vorherige, sodass bei zwei Mixins, die dasselbe Member deklarieren, das **letzte** in der Liste gewinnt:

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

Dieses Stapeln nennt man **Linearisierung**: `with A, B` baut die Kette `Object` → `A` → `B` → die Klasse selbst.

---

Weil das letzte Mixin gewinnt, ist die Reihenfolge der `with`-Liste Teil der Bedeutung der Klasse und kein Detail des Stils. Werden die Einträge umgestellt, ändert das, welche Implementierung das Objekt am Ende bekommt:

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

Member, die nur ein Mixin deklariert, stehen nie in Konkurrenz: Sie sind verfügbar, egal welche Reihenfolge gilt. Lies `with X, Y` als „beginne mit `X` und lass `Y` es überschreiben".

---

Mixins und `extends` arbeiten zusammen. Eine Klasse kann eine Oberklasse **und** eine Liste von Mixins haben, und die Mixins werden immer **oben auf** der Oberklasse angewendet:

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

Die Kette ist hier `Object` → `Document` → `Timestamped` → `Report`. Ein Member wird ab dem Ende der Kette gesucht, daher findet `Report().header()` zuerst die Version von `Timestamped`. Dasselbe Member in der Oberklasse und in einem Mixin zu deklarieren ist völlig legal: So ersetzt oder umhüllt ein Mixin geerbtes Verhalten.

---

Der Klassenkörper sitzt ganz am Ende der Kette, daher **überschreibt** ein in der Klasse deklariertes Member dasselbe Member aus jedem seiner Mixins. Innerhalb des Overrides erreicht **`super`** die Version, die das Mixin bereitgestellt hat:

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

Das Mixin selbst bleibt unangetastet: `Guest` bekommt weiterhin das ursprüngliche `greet`. `super.greet()` ermöglicht es `Host`, auf dem gemeinsamen Verhalten aufzubauen, statt es zu kopieren.

---

Manches Verhalten ergibt nur Sinn, wenn es auf einer bestimmten Klasse sitzt, und braucht die Member dieser Klasse, um seine Arbeit zu tun. Die **`on`**-Klausel formuliert diese Anforderung:

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

`on Animal` tut zwei Dinge: Es erlaubt dem Mixin, die Member von `Animal` zu verwenden, wie `name` oben, und es beschränkt, wer das Mixin verwenden darf. `class Rock with Noisy {}` ist ein Kompilierfehler, denn `Rock` ist kein `Animal`.

---

Ein Mixin mit einer `on`-Klausel liest die Member seiner Oberklasse, als wären sie seine eigenen — genau das macht es zu einem guten Ort für Verhalten, das einen bestehenden Typ dekoriert:

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

`Square` überschreibt `kind`, und `show` greift automatisch auf den Override zu: Das Mixin ruft das Member immer auf dem echten Objekt auf.

---

Sobald ein Mixin eine `on`-Klausel hat, darf es ein Member dieses Typs **überschreiben** und **`super`** aufrufen, um die Version darunter in der Kette zu erreichen:

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

`super.log` ist nicht das eigene `log` des Mixins, sondern das darunter, daher gibt es keine endlose Rekursion. Stapelt man mehrere solcher Mixins mit `with A, B`, umhüllt jedes das vorherige: Der Aufruf betritt zuerst das **letzte** Mixin und wandert hinunter zur Oberklasse.

---

Eine `mixin`-Deklaration kann weder instanziiert noch erweitert werden, und eine einfache `class` kann nicht nach `with` stehen. Wenn du eine Deklaration brauchst, die **beide** Wege beherrscht, schreibe **`mixin class`**:

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

Eine `mixin class` zahlt für diese Flexibilität mit zwei Einschränkungen: Sie muss `Object` erweitern, kann also keine eigene `extends`-Klausel haben, und sie darf keinen Konstruktor deklarieren, denn ein Mixin führt nie einen aus.

---

Mixins, Vererbung und Schnittstellen lösen drei verschiedene Probleme:

- **`extends`** gibt einer Klasse eine Oberklasse, für eine „ist eine Art von"-Beziehung. Es gibt nur diesen einen Platz, daher sollte er an die stärkste Beziehung gehen.
- **`with`** fügt Verhalten hinzu, das viele nicht verwandte Klassen brauchen. Es gibt kein Limit, und die Implementierung wird geteilt, nicht kopiert.
- **`implements`** verspricht eine Reihe von Membern, bringt aber **keine** Implementierung mit: Jede Klasse muss den Körper selbst schreiben.

Ein deutliches Zeichen, dass du ein Mixin willst, ist eine Methode, die du sonst in Klassen kopieren würdest, die kein gemeinsames Elternteil haben — etwa wenn `Duck`, `Plane` und `Kite` alle dasselbe `fly` brauchen.

---

Gestapelte Mixins sind die Art, wie kleine, unabhängige Regeln zu einer Klasse kombiniert werden. Jedes Mixin überschreibt dasselbe Member, erledigt seinen eigenen Teil und ruft `super` auf, um die Arbeit weiterzureichen. Da der Aufruf zuerst das **letzte** Mixin betritt, entscheidet die Reihenfolge der `with`-Liste, welche Regel vor welcher läuft:

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

`class A extends Account with Doubled {}` verdoppelt jede Einzahlung. Füge ein zweites Mixin nach `Doubled` hinzu und es bekommt die Einzahlung zuerst, bevor `Doubled` sie überhaupt sieht.
