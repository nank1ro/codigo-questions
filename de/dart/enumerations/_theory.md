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
