Der **Additionsoperator** `+` addiert zwei Werte zusammen.

```dart
int a = 3;
int b = 4;
int sum = a + b; // 7
```

Du kannst `+` mit `int`- oder `double`-Werten verwenden.

---

Der **Subtraktionsoperator** `-` subtrahiert einen Wert von einem anderen.

```dart
int a = 10;
int b = 4;
int diff = a - b; // 6
```

Das Ergebnis kann negativ sein, wenn der zweite Operand größer als der erste ist.

---

Der **Multiplikationsoperator** `*` multipliziert zwei Werte miteinander.

```dart
int a = 5;
int b = 6;
int product = a * b; // 30
```

Die Multiplikation einer `int` mit einer anderen `int` ergibt eine `int`. Die Multiplikation mit einer `double` ergibt eine `double`.

---

Der **Divisionsoperator** `/` teilt einen Wert durch einen anderen. In Dart gibt `/` **immer eine `double` zurück**, auch wenn das Ergebnis eine ganze Zahl ist.

```dart
int a = 10;
int b = 4;
double result = a / b; // 2.5

double exact = 10 / 2; // 5.0  (not 5!)
```

Verwende immer eine `double`-Variable, um das Ergebnis von `/` zu speichern.

---

Der **Ganzzahldivisionsoperator** `~/` teilt zwei Zahlen und **truncates** das Ergebnis auf eine Ganzzahl (verwirft jeden Dezimalteil).

```dart
int a = 10;
int b = 3;
int result = a ~/ b; // 3  (not 3.333...)
```

Verwende `~/`, wenn du einen ganzzahligen Quotienten ohne Rest brauchst.
