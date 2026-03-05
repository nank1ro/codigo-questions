Typen ermöglichen es dir, alle verschiedenen Datentypen zu kategorisieren, die du in deinem Code verwendest.
In Dart ist ein __Typ__ eine Möglichkeit, dem Compiler zu zeigen, wie du ein bestimmtes Datenelement verwenden wirst.
Hier ist ein Beispiel für Typen, die Dart unterstützt:
- int
- String
- double
- dynamic
- num

Dart unterstützt viele andere Typen. Die aufgeführten sind die wichtigsten, die du verwenden wirst.

---

Es ist kein Problem, wenn du den Typ einer Variablen explizit definierst, zum Beispiel:
```dart
int integerNumber = 2;
double decimalNumber = 3.14;
```

---

Variablen mit explizitem Typ können auch Konstanten sein, füge einfach das `const`- oder `final`-Schlüsselwort vor dem Typ hinzu:
```dart
const int integerNumber = 2;
final double decimalNumber = 3.14;
```

> Hinweis: Veränderbare Daten ermöglichen es dir, sie jederzeit auf einfache Weise zu ändern. Viele erfahrene Programmierer schätzen jedoch die Vorteile unveränderlicher Daten. Wenn ein Wert unveränderlich ist, kannst du darauf vertrauen, dass niemand den Wert nach seiner Erstellung ändern kann. Wenn du deine Daten auf diese Weise einschränkst, werden viele schwer zu findende Fehler verhindert und das Programm wird einfacher zu verstehen und zu testen.

---

Obwohl es möglich ist, den Typ einer Variablen zu notieren, ist dies redundant. Du weißt, dass `10` vom Typ `int` und `3.14` vom Typ `double` ist. Der Dart-Compiler kann dies dank __Typinferenz__ ableiten. Nicht alle Programmiersprachen haben _Typinferenz_, und dies macht Dart zu einer sehr leistungsstarken Programmiersprache.

Du kannst den Typ einfach aus den Variablen entfernen, zum Beispiel:
```dart
const integerNumber = 2;
final decimalNumber = 3.14;
```

Wenn der Typ einer Variablen nicht explizit notiert ist, wird Dart versuchen, seinen Typ abzuleiten.

---

Es gibt eine programmatische Möglichkeit, den Typ einer Variablen zu überprüfen, nämlich mit dem `is`-Schlüsselwort:
```dart
final number = 3.14;
print(number is int); // false
print(number is double); // true
```

Wie du sehen kannst, hat Dart der Variablen `number` den Typ `double` zugewiesen.

---

Mit dem `is`-Schlüsselwort kannst du überprüfen, ob eine Variable vom definierten Typ ist. Du kannst aber auch überprüfen, ob eine Variable nicht vom definierten Typ ist, indem du das `is!`-Schlüsselwort verwendest:
```dart
final number = 3.14;
print(number is! int); // true
```

---

Eine weitere Option, um den Typ einer _Runtime_-Variablen zu sehen, ist die Verwendung der `runtimeType`-Eigenschaft, die für alle Typen verfügbar ist.
```dart
final number = 3.14;
print(number.runtimeType); // double
```

---

Manchmal befindest du dich in einer Situation, in der du einen Typ hast, aber einen anderen brauchst. Du könntest versucht sein, folgendes zu tun:

```dart
var integer = 5;
var decimal = 3.14;
integer = decimal;
```

Aber Dart wird sich beschweren und dir den Fehler geben:
> Error: A value of type 'double' can't be assigned to a variable of type 'int'.

Einige Programmiersprachen sind nicht so restriktiv und konvertieren stillschweigend. Die Erfahrung zeigt, dass diese Art der stillen impliziten Konvertierung eine häufige Fehlerquelle und Ursache von Leistungsproblemen ist. Dart hat diese Funktion deaktiviert, um diese Probleme zu vermeiden.

Denk daran, dass Computer auf Programmierer angewiesen sind, um herauszufinden, was zu tun ist. In Dart gehört dazu auch, explizit zu sein über die Art der Konvertierung.

Anstatt eine implizite Konvertierung von Dart zu erwarten, musst du explizit angeben, dass Dart den Typ für dich konvertieren soll. So konvertierst du eine `double`-Zahl in eine `int`:
```dart
var integer = decimal.toInt();
```

Die Zuweisung sagt Dart eindeutig, dass du vom ursprünglichen Typ `double` zum neuen Typ `int` konvertieren möchtest.

> HINWEISE: In diesem Fall verliert das Zuweisen eines Dezimalwerts zu einer Ganzzahl an Genauigkeit. Die Variable `integer` hat den Wert __3__ statt __3.14__. Deshalb ist es wichtig, explizit zu sein. Dart möchte sichergehen, dass du weißt, was du tust, und teilt dir mit, dass du durch die Konvertierung Informationen verlierst.

---

Bisher haben wir die Operatoren unabhängig auf Ganzzahlen oder Dezimalzahlen gesehen. Was ist, wenn du eine Ganzzahl hast und sie mit einer Dezimalzahl multiplizieren musst? Schauen wir uns ein Beispiel an:
```dart
const radius = 5;
const pi = 3.14;
const circumference = 2 * pi * radius;
```

`radius` ist vom Typ `int`, während `pi` vom Typ `double` ist. Welcher Typ wird `circumference` haben? Dart wird der Variablen `circumference` den Typ `double` zuweisen. Das ist die sicherere Wahl, denn wenn ich sie vom Typ `int` gemacht hätte, hätte es zu einem Genauigkeitsverlust führen können.

Wenn du als Ergebnis ein `int` möchtest, musst du die Konvertierung explizit durchführen:
```dart
const circumference = (2 * pi * radius).toInt();
```

Die Klammern sagen Dart, dass es zuerst multiplizieren soll und dann das Ergebnis in einen Ganzzahlwert konvertiert. Leider wird dem Analyzer dieser Code nicht gefallen:
 > Const variables must be initialized with a constant value.

Das Problem ist, dass die `toInt`-Methode eine reine Runtime-Methode ist. Das bedeutet, dass die Variable `circumference` zur Compile-Zeit nicht bestimmt werden kann, daher kann die Variable nicht konstant sein. Um das zu beheben, ersetze `const` durch `final`:

```dart
final circumference = (2 * pi * radius).toInt();
```

Jetzt ist `circumference` eine __Runtime-Konstanten__-Variable vom Typ `int`.

---

Manchmal könnte eine Variable einen generischen Typ haben, aber du brauchst Funktionalität, die nur in einem Subtyp vorhanden ist. Wenn du sicher bist, dass der Typ der Variablen der Subtyp ist, den du brauchst, kannst du das `as`-Schlüsselwort verwenden, um seinen Typ zu ändern. Dieses Verfahren wird auch als __Typ-Casting__ bezeichnet. Hier ist ein Beispiel:

```dart
num number = 3;
```

Angenommen, wir wollen überprüfen, ob die Zahl gerade ist, und die relevante Funktionalität ist nur im `int`-Subtyp vorhanden.
```dart
print(number.isEven);
```

Der obige Code sollte dir einen Typfehler zurückgeben:
> The getter `isEven` isn't defined for the type 'num'.

Der `num`-Typ ist zu allgemein, um zu wissen, ob eine Zahl gerade oder ungerade ist. Nur Ganzzahlen können gerade oder ungerade sein.
Das Problem tritt auf, wenn `num` einen `double`-Wert enthält, da `num` sowohl `double`- als auch `int`-Typen einschließt. In diesem Fall sind wir sicher, dass __3__ eine Ganzzahl ist, daher können wir zu `int` konvertieren.

```dart
final integer = number as int;
print(integer.isEven); // false
```

Das `as`-Schlüsselwort veranlasst den Compiler, die Variable `integer` als Typ `int` zu erkennen. Dies ermöglicht dir die Verwendung der `isEven`-Eigenschaft, die bei Ganzzahlen vorhanden ist. Da die Zahl __3__ keine Ganzzahl ist, ist das Ergebnis false.

Du musst beim Casting vorsichtig sein. Wenn du den Typ falsch konvertierst, erhältst du einen Laufzeitfehler:
```dart
num numero = 3;
final decimale = numero as double;
```

Dies wird das Programm mit folgendem Fehler zum Absturz bringen:
> CastError (type 'int' is not a subtype of type 'double' in type cast)

Der Laufzeittyp von `number` ist `int` und nicht `double`. In Dart kannst du mit gleichrangigen Typen wie `int` und `double` nicht konvertieren. Du kannst nur Subtypkonvertierungen durchführen.
