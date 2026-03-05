Variablen sind Container zum Speichern von Werten.
Jede Variable in Dart ist ein Objekt (`Object`).
Um eine Variable zu erstellen, müssen wir ihr einen __Namen__ geben, wobei zu beachten ist, dass er keine Leerzeichen enthalten darf.
Schau dir folgendes an:

```dart
int number = 1;
```

Diese Anweisung deklariert eine Variable namens `number` vom Typ `int`.
Sie setzt dann den Wert der Variable auf die Nummer `1`.
Der `int` Teil der Deklaration wird als __Typannotation__ bezeichnet und teilt Dart explizit den Typ der Variable mit.

---

Im vorherigen Beispiel haben wir die Erstellung einer Variablen gesehen:

```dart
int number = 1;
```

Lass dich nicht von dem Symbol `=` täuschen.
Es ist nicht das Gleichheitszeichen wie in der Mathematik, sondern wird als __Zuweisungsoperator__ bezeichnet, da es einem Wert einer Variable zugewiesen.
Das Gleichheitszeichen ist dagegen `==`.

---

Wenn du den Wert einer Variablen ändern möchtest, weise ihr einfach einen anderen Wert desselben Typs zu:

```dart
int number = 1;
number = 2;
```

---

Der Typ `int` ermöglicht das Speichern von ganzen Zahlen.
Um stattdessen Dezimalzahlen zu speichern, können wir den Typ `double` verwenden:

```dart
double pi = 3.14159;
```

Dieses Beispiel ähnelt dem vorherigen. Diesmal ist die Variable jedoch vom Typ `double`, ein Typ, der Dezimalzahlen mit hoher Genauigkeit speichert.

---

Dart ist eine __typsichere__ Sprache.
Dies bedeutet, dass du, wenn du einen Typ einer Variablen zuweist, ihn später nicht ändern kannst. Hier ist ein Beispiel:

```dart
int integerNumber = 1;
integerNumber = 3.14159; // Error
```

`3.14159` ist vom Typ `double`, aber du hast `integerNumber` bereits mit dem Typ `int` definiert.

Natürlich kann es manchmal nützlich sein, verwandte Typen derselben Variablen zuzuweisen. Zum Beispiel könntest du eine Variable `integerNumber` haben, die sowohl `int` als auch `double` Zahlen akzeptiert, wie hier:

```dart
num number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // Error
```

Sowohl `int` als auch `double` erweitern `num`, daher werden beide Typen akzeptiert.
Wenn wir jedoch versuchen, einen `String` zuzuweisen, gibt der Compiler einen Fehler zurück.

---

Wenn du gerne das Risiko eingehen möchtest, können wir die __Typsicherheit__ der Sprache völlig ignorieren, indem wir den `dynamic` Typ verwenden.
Dies ermöglicht es dir, jeden Werttyp der Variablen zuzuweisen.

```dart
dynamic number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // OK
```

Dieser Ansatz wird dringend abgeraten, da Fehler nicht mehr vom _Analyzer_ des Codes, sondern nur zur _Laufzeit_ abgefangen werden (wenn das Programm läuft).

---

Dart unterstützt __Typinferenz__.
Es ist nicht notwendig, den Typ einer Variablen anzugeben, da Dart seinen Typ ableiten kann.
Das Schlüsselwort `var` teilt Dart mit, den am besten geeigneten Typ zu verwenden.

```dart
var number = 5;
```

Es ist nicht notwendig, Dart mitzuteilen, dass die Nummer `5` vom Typ `int` ist.
Dart leitet den Typ ab und macht `number` vom Typ `int`.

---

Dart unterstützt zwei verschiedene Typen von "_Variablen_", deren Wert sich nie ändert. Sie werden mit den Schlüsselwörtern `const` und `final` deklariert.
Lassen Sie uns zunächst sehen, was mit `const` gemeint ist.

## const (Konstanten)

Variablen, deren Wert du ändern kannst, werden __veränderliche Daten__ genannt. Veränderliche Daten werden oft übernutzt und können Probleme darstellen. Es ist leicht, den Überblick über alle Punkte im Code zu verlieren, die den Wert einer Variablen ändern können.

Aus diesem Grund solltest du, wenn möglich, `const`anten anstelle von `var`iablen verwenden. Diese Variablen, die ihren Wert nicht ändern können, werden auch __unveränderliche Daten__ genannt.

Um eine Konstante in Dart zu erstellen, verwenden wir das Schlüsselwort `const`:

```dart
const number = 5;
```

Genau wie bei `var` bestimmt Dart mit der __Typinferenz__, dass `number` vom Typ `int` ist.

---

Wenn du eine Konstante deklariert hast, kannst du ihren Wert nicht mehr ändern. Zum Beispiel:

```dart
const number = 2;
number = 3; // Error
```

Dieser Code erzeugt den Fehler:
> Constant variables can't be assigned a value.

Das heißt, es ist nicht möglich, den Wert einer konstanten Variablen zu ändern.

---

Du wirst dich häufig in einer Situation befinden, in der du eine Konstante verwenden möchtest, aber ihren Wert zur Kompilierzeit nicht kennst. Du wirst den Wert erst nach dem Start des Programms kennen.
Diese Art von Konstante wird als __Laufzeitkonstante__ bezeichnet.

In Dart wird `const` nur für __Kompilierungszeitkonstanten__ für Werte verwendet, die der Compiler vor der Ausführung des Programms bestimmen kann.

Wenn du keine konstante Variable erstellen kannst, weil du ihren Kompilierungszeitwert nicht kennst, musst du das Schlüsselwort `final` verwenden, um die Variable zu einer __Laufzeitkonstante__ zu machen.

Es gibt viele Gründe, warum du den Wert einer Variablen vor dem Ausführen des Programms nicht kennen kannst. Zum Beispiel müsstest du den Wert von einem Server erhalten oder den Benutzer danach fragen.

---

Hier ist ein Beispiel für einen Wert, der nur zur Laufzeit erhalten werden kann:

```dart
final currentHour = DateTime.now().hour;
```

`DateTime.now()` ist eine Funktion, um das aktuelle Datum und die Zeit zu erhalten, wenn der Code ausgeführt wird.
Mit dem Feld `hour` greifen wir auf die Anzahl der Stunden zu, die seit Beginn des Tages vergangen sind.

Da der Wert von `hour` je nach Zeitpunkt der Codeausführung unterschiedlich ist, kann dies als _Laufzeit_-Wert definiert werden.

Wenn du versuchst, den Wert einer `final`-Variablen zu ändern, erhältst du einen Fehler.
