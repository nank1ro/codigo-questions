Du weißt bereits, wie du einer Klasse, die du selbst geschrieben hast, Methoden hinzufügst. Aber was ist mit `String`, `int` oder `List`, deren Code im Dart SDK liegt? Du kannst sie nicht bearbeiten, und doch wünschst du dir oft, sie hätten eine weitere Methode.

Eine **Extension** löst das: Sie fügt einem **bestehenden** Typ neue Member hinzu, ohne seinen Quellcode anzufassen und ohne eine Unterklasse zu erstellen. Die Syntax ist:

```dart
extension ExtensionName on Type {
  // new methods and getters
}
```

Innerhalb der Extension verweist `this` auf den Wert, auf dem der Member aufgerufen wird. Sobald die Extension deklariert ist, werden ihre Member genauso aufgerufen wie die eigenen Member des Typs:

```dart
extension Greeting on String {
  String greet() => 'Hello, $this!';
}

void main() {
  var name = 'Ada';
  print(name.greet()); // Hello, Ada!
}
```

Extensions werden auf der **Top-Level**-Ebene einer Datei deklariert, neben Klassen und Funktionen, nie innerhalb von `main`.

---

Extensions funktionieren mit jedem Typ, auch mit Zahlen. Diese Extension gibt jedem `int` eine Methode, die ihn verdoppelt:

```dart
extension Doubling on int {
  int doubled() => this * 2;
}
```

Weil sich die Extension auf den **Typ** bezieht, kannst du die Methode auf einer Variable oder direkt auf einem **Literal** aufrufen. Negative Literale brauchen Klammern, sonst wird der Punkt vor dem Minuszeichen gelesen:

```dart
var n = 21;
print(n.doubled());    // 42
print(4.doubled());    // 8
print((-3).doubled()); // -6
```

---

Eine Extension kann auch **Getter** deklarieren, die wie Eigenschaften ohne Klammern gelesen werden. Innerhalb einer Extension kannst du die eigenen Member des Typs direkt aufrufen: `this.` ist optional, genau wie in einer Klasse.

```dart
extension Sizes on String {
  bool get isLong => length > 10;      // same as this.length
  String get firstChar => this[0];
}

void main() {
  print('Dart'.isLong);           // false
  print('extension'.firstChar);   // e
}
```

Wähle einen Getter, wenn der Member nur einen Wert **liest** und keine Parameter nimmt; wähle eine Methode, wenn sie Arbeit leistet oder Argumente braucht.

---

Der Typ nach `on` kann ein **parametrisierter** Typ wie `List<int>` sein. Die Extension gilt dann nur für Listen dieses Elementtyps: `[1, 2].total()` funktioniert, `['a', 'b'].total()` kompiliert nicht.

```dart
extension Totals on List<int> {
  int total() {
    var sum = 0;
    for (final n in this) {
      sum += n;
    }
    return sum;
  }
}
```

Innerhalb der Extension ist `this` die Liste, sodass du sie wie gewohnt durchlaufen, indizieren oder `length` aufrufen kannst.

---

Eine Extension auf `List<int>` kann nicht auf einer `List<String>` verwendet werden. Um eine Extension zu schreiben, die mit **jedem** Elementtyp funktioniert, gib der Extension einen **Typparameter**, der in spitzen Klammern nach ihrem Namen steht, und verwende ihn im `on`-Typ:

```dart
extension Firsts<T> on List<T> {
  T get firstOrLast => length > 1 ? this[0] : this[length - 1];
}
```

`T` ist ein Platzhalter für „was auch immer der Elementtyp ist“: Auf einer `List<int>` wird er zu `int`, auf einer `List<String>` zu `String`, sodass der Getter oben entsprechend ein `int` oder ein `String` zurückgibt. Der Compiler setzt `T` bei jedem Aufruf für dich ein.

```dart
print([7, 8, 9].firstOrLast); // 7
print(['a', 'b'].firstOrLast); // a
```

---

Eine Extension auf `String` kann nicht auf einem `String?` aufgerufen werden: Der Wert könnte `null` sein, und der Compiler lehnt den Aufruf ab. Wenn du die Extension stattdessen auf dem **nullable** Typ deklarierst, kann die Methode direkt auf einem `String?` aufgerufen werden, und darin hat `this` den Typ `String?`, sodass du den `null`-Fall selbst behandeln musst, zum Beispiel mit `??`:

```dart
extension Defaults on int? {
  int orZero() => this ?? 0;
}

void main() {
  int? count = null;
  print(count.orZero()); // 0
  print(5.orZero());     // 5
}
```

Ein nicht-nullable `int` kann überall dort übergeben werden, wo ein `int?` erwartet wird, daher funktioniert die Extension mit beiden.

---

Eine Extension kann Methoden, Getter, Setter und Operatoren hinzufügen, aber sie kann **keine Instanzfelder hinzufügen**. Ein `int`-Wert hat ein festes Layout im Speicher, und eine Extension ist nur eine Menge von Funktionen, die der Compiler dich mit der Punktsyntax aufrufen lässt: Es gibt keinen Platz, um pro Wert zusätzliche Daten zu speichern.

```dart
extension Counter on int {
  int count = 0; // error: extensions can't declare instance fields
}
```

Getter und Setter in einer Extension können nur Werte aus `this` berechnen oder an vorhandene Member weiterleiten: Sie können sich zwischen Aufrufen nichts merken.

---

Eine Extension kann **statische** Member deklarieren. Wie in einer Klasse gehören sie zur Extension selbst und nicht zu einem Wert, und sie werden über den **Namen der Extension** aufgerufen, nicht über den Typ, den sie erweitert:

```dart
extension Temperatures on double {
  static const double boiling = 100.0;

  static bool isBoiling(double celsius) => celsius >= boiling;
}

void main() {
  print(Temperatures.boiling);         // 100.0
  print(Temperatures.isBoiling(37.5)); // false
  print(double.boiling);               // error: 'boiling' isn't defined for 'double'
}
```

Statische Member sind ein praktischer Ort für Konstanten und Hilfsfunktionen, die zum erweiterten Typ gehören.

---

Extensions sind nicht nur für SDK-Typen da: Du kannst auch **deine eigenen Klassen** erweitern. Das ist nützlich, wenn die Klasse aus einem Paket stammt, das du nicht kontrollierst, oder wenn du die Klasse klein halten und optionale Helfer neben dem Code hinzufügen möchtest, der sie braucht.

```dart
class Circle {
  final double radius;
  Circle(this.radius);
}

extension CircleMath on Circle {
  double get diameter => radius * 2;
}

void main() {
  print(Circle(3).diameter); // 6.0
}
```

Die Extension sieht die öffentlichen Felder und Methoden der Klasse, genau wie Code, der außerhalb der Klasse geschrieben wurde.

---

Dart erlaubt einem Typ, zu definieren, was Operatoren wie `+`, `*` oder `==` für seine Werte bedeuten, und zwar mit einer Methode, deren Name das Schlüsselwort `operator` gefolgt vom Symbol ist. Die rechte Seite des Operators ist der Parameter der Methode:

```dart
extension Scaling on List<int> {
  List<int> operator *(int factor) => map((n) => n * factor).toList();
}

void main() {
  print([1, 2, 3] * 10); // [10, 20, 30]
}
```

Da Extensions Operatoren deklarieren können, kannst du einem vorhandenen Typ einen neuen Operator geben, den er noch nicht hat. `String` hat `+` und `*`, aber kein `-`, sodass eine Extension definieren kann, was `'hello world' - 'o'` bedeutet.

---

Was ist, wenn eine Extension einen Member deklariert, den der Typ **bereits hat**? Der eigene Member des Typs gewinnt immer: Extension-Member werden nur berücksichtigt, wenn der Typ selbst keinen Member mit diesem Namen hat. Der Extension-Member wird stillschweigend ignoriert, es gibt keinen Fehler und kein Überschreiben.

```dart
extension Shorter on String {
  int get length => 0;
}

void main() {
  print('four'.length); // 4, String's own length is used
}
```

Eine Extension kann also Member hinzufügen und Lücken füllen, aber sie kann nie **ändern**, wie sich vorhandene Member verhalten.

---

Der Name einer Extension ist optional. Eine **unbenannte** Extension funktioniert genauso, ist aber nur in der Datei sichtbar, die sie deklariert:

```dart
extension on int {
  bool get isTriple => this % 3 == 0;
}
```

Ein **Name** wird wichtig, sobald zwei Extensions denselben Member auf demselben Typ anbieten: Der Aufruf wird **mehrdeutig** und kompiliert nicht. Der Name erlaubt dir, den Konflikt auf zwei Arten aufzulösen. Stammen die Extensions aus verschiedenen Dateien, kannst du eine von ihnen im Import mit `show` oder `hide` ein- bzw. ausblenden:

```dart
import 'package:loud/loud.dart';
import 'package:quiet/quiet.dart' hide Quiet;
```

Oder du kannst die Extension überall **explizit** anwenden, indem du den Wert in den Namen der Extension einhüllst, als wäre er ein Konstruktor:

```dart
print(Loud('hi').describe());
```

Unbenannte Extensions können nicht ausgeblendet oder explizit angewendet werden, daher verwende besser benannte Extensions in Code, den andere importieren werden.

---

Eine generische Extension kann **Funktionen** als Parameter nehmen, genau wie `where` und `map`. Der Funktionstyp wird mit dem Elementtyp `T` geschrieben, sodass der Callback Elemente des richtigen Typs erhält:

```dart
extension Checks<T> on List<T> {
  bool all(bool Function(T) test) {
    for (final item in this) {
      if (!test(item)) return false;
    }
    return true;
  }
}

void main() {
  print([2, 4, 6].all((n) => n.isEven)); // true
}
```
