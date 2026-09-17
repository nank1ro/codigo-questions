Eine **Enumeration** (oder *Enum*) definiert einen gemeinsamen Typ für eine Gruppe verwandter Werte, damit du mit diesen Werten auf typsichere Weise arbeiten kannst. In Dart deklarierst du eine mit dem Schlüsselwort `enum` und listest ihre **Werte** durch Kommas getrennt auf:

```dart
enum Direction { north, south, east, west }
```

Konventionsgemäß werden Wertenamen in `lowerCamelCase` geschrieben, wie Variablen. Auf jeden Wert wird über den Enum-Namen zugegriffen, und wenn du ihn ausgibst, werden sowohl das Enum als auch der Wert angezeigt:

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

Ein Enum muss auf oberster Ebene einer Datei deklariert werden, niemals innerhalb einer Funktion wie `main`.

---

Jeder Enum-Wert hat zwei eingebaute Eigenschaften:

- `name` ist der Name des Werts als `String`
- `index` ist seine Position in der Deklaration, beginnend bei `0`

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

Jedes Enum hat außerdem eine konstante Liste namens `values`, die alle seine Werte in Deklarationsreihenfolge enthält. Du kannst sie wie jede Liste indizieren, ihre `length` lesen oder mit `for-in` darüber iterieren:

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

Da `values` eine Liste ist, kannst du sie mit den Listenmethoden kombinieren, die du bereits kennst. Zum Beispiel wandelt `.map()` zusammen mit `.name` die Werte in eine Liste von Strings um:

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

Eine Schleife über `values` ist der übliche Weg, um jeden Wert eines Enums zu verarbeiten. In der Schleife verhält sich der aktuelle Wert wie jedes andere Objekt, du kannst also seinen `index` und seinen `name` lesen und sie direkt in einer String-Interpolation verwenden:

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

Jeder Enum-Wert existiert genau einmal, sodass zwei Referenzen auf denselben Wert immer gleich sind. Vergleiche sie mit `==` und `!=`:

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

Eine `switch`-Anweisung ist der natürliche Weg, um über ein Enum zu verzweigen, mit einem `case` pro Wert:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) {
  switch (direction) {
    case Direction.north:
      return '^';
    case Direction.south:
      return 'v';
    case Direction.east:
      return '>';
    case Direction.west:
      return '<';
  }
}
```

Wenn die Fälle jeden Wert abdecken, ist der switch *erschöpfend* und benötigt kein `default`. Wenn du einen Wert vergisst, meldet der Compiler einen Fehler, anstatt den Bug zur Laufzeit auftreten zu lassen.

---

Seit Dart 3 kann ein `switch` auch als **Ausdruck** verwendet werden, der einen Wert erzeugt. Jeder Fall wird als `pattern => value` geschrieben, und die Fälle werden durch Kommas getrennt, ohne das Schlüsselwort `case` und ohne `break`:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

Wie bei der Anweisungsform muss ein switch-Ausdruck über ein Enum erschöpfend sein.

---

Seit Dart 2.17 kann ein Enum **Felder** und einen **Konstruktor** deklarieren, genau wie eine Klasse. Das nennt man ein *erweitertes Enum*. Jeder Wert übergibt dann seine eigenen Argumente an den Konstruktor:

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);
}

print(Planet.mars.moons); // 2
```

Beachte die drei Regeln: Die Liste der Werte endet mit einem **Semikolon** `;`, die Felder müssen `final` sein, und der Konstruktor muss `const` sein.

---

Ein erweitertes Enum kann auch **Methoden** und **Getter** deklarieren. Innerhalb von ihnen ist `this` der aktuelle Wert, sodass du direkt auf seinen `name`, `index` und seine Felder zugreifen kannst:

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);

  bool get hasMoons => moons > 0;

  String describe() => '$name has $moons moon(s)';
}

print(Planet.earth.hasMoons);   // true
print(Planet.mars.describe()); // mars has 2 moon(s)
```

Ein Enum ohne Felder kann trotzdem Methoden deklarieren: Die Liste der Werte endet dann mit `;`, gefolgt von den Members.

---

Um von einem `String` zurück zu einem Enum-Wert zu gelangen, rufe `byName` auf der `values`-Liste auf. Es gibt den Wert zurück, dessen `name` genau übereinstimmt:

```dart
enum Direction { north, south, east, west }

var direction = Direction.values.byName('east');
print(direction == Direction.east); // true
```

Wenn kein Wert diesen Namen hat, wirft `byName` einen `ArgumentError`. Wenn der String aus einer Benutzereingabe stammt, ist `asNameMap()` die sicherere Wahl: Es gibt eine `Map<String, Direction>` von Namen zu Werten zurück, sodass eine Suche nach einem unbekannten Namen `null` statt eines Fehlers liefert:

```dart
print(Direction.values.asNameMap()['up']); // null
```

---

Enum-Werte eignen sich hervorragend als **Map-Schlüssel**: Sie sind eindeutig, leicht zu vergleichen, und der Compiler stellt sicher, dass du nur echte Werte verwendest. Deklariere die Map mit dem Enum als Schlüsseltyp und greife mit `[]` auf die Werte zu:

```dart
enum Direction { north, south, east, west }

Map<Direction, String> arrows = {
  Direction.north: '^',
  Direction.south: 'v',
  Direction.east: '>',
  Direction.west: '<',
};

print(arrows[Direction.east]); // >
```

Wie bei jeder Map liefert eine Suche `null`, wenn der Schlüssel fehlt, also verwende `??`, um einen Ersatzwert bereitzustellen.

---

Ein Enum kann eine **Schnittstelle implementieren** mit dem Schlüsselwort `implements`. Das Enum verspricht dann, jedes Member bereitzustellen, das die Schnittstelle deklariert, und seine Werte können überall dort verwendet werden, wo dieser Schnittstellentyp erwartet wird:

```dart
abstract class Describable {
  String describe();
}

enum Animal implements Describable {
  dog,
  cat;

  @override
  String describe() => 'I am a $name';
}

Describable pet = Animal.cat;
print(pet.describe()); // I am a cat
```

Ein in der Schnittstelle deklarierter Getter kann entweder mit einem Getter oder mit einem `final`-Feld desselben Namens implementiert werden.
