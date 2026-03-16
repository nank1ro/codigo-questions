Eine `for`-Schleife wiederholt einen Codeblock eine festgelegte Anzahl von Malen. Die grundlegende Syntax lautet:

```dart
for (initialization; condition; update) {
  // body
}
```

**initialization**: wird einmal vor dem Start der Schleife ausgeführt (z.B. `int i = 0`)

**condition**: wird vor jeder Iteration geprüft; die Schleife stoppt, wenn sie falsch ist

**update**: wird nach jeder Iteration ausgeführt (z.B. `i++`)

---

Du kannst die Schleifenvariable im Rumpf verwenden, um den aktuellen Stand zu verfolgen. Zum Beispiel das Aufaddieren einer Summe:

```dart
int total = 0;
for (int i = 1; i <= 5; i++) {
  total += i;
}
```

Nach der Schleife ist `total` gleich 15.

---

Eine `for`-Schleife kann **rückwärts** zählen, indem man ein Dekrement (`i--`) und eine `>=`-Bedingung verwendet:

```dart
for (int i = 5; i >= 1; i--) {
  print(i); // 5, 4, 3, 2, 1
}
```

Das ist nützlich für Countdowns oder umgekehrte Iteration.

---

Die `for-in`-Schleife iteriert über jedes Element einer Sammlung, ohne einen Index zu benötigen:

```dart
List<String> fruits = ['apple', 'banana', 'cherry'];
for (var fruit in fruits) {
  print(fruit);
}
```

Bei jeder Iteration wird das nächste Element der Schleifenvariablen (`fruit` hier) zugewiesen.

---

Die `break`-Anweisung beendet eine Schleife sofort, wenn eine Bedingung erfüllt ist:

```dart
for (int i = 0; i < 10; i++) {
  if (i == 5) break; // stops at 5
  print(i);
}
```

Das ist nützlich, wenn man nach einem Wert sucht und stoppen möchte, sobald er gefunden wurde.
