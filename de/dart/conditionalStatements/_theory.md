Eine **`if`-Anweisung** führt einen Codeblock nur aus, wenn eine Bedingung `true` ist.

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

Der Code innerhalb der geschweiften Klammern wird nur ausgeführt, wenn die Bedingung `age >= 18` zu `true` ausgewertet wird.

---

Du kannst `print()` innerhalb eines `if`-Blocks verwenden, um eine Nachricht anzuzeigen, wenn eine Bedingung erfüllt ist.

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

Wenn `isRaining` `false` ist, wird nichts ausgegeben.

---

Eine **`if-else`-Anweisung** führt den `if`-Block aus, wenn die Bedingung `true` ist, und den `else`-Block, wenn sie `false` ist.

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

Genau einer der beiden Zweige wird immer ausgeführt.

---

**`else if`** ermöglicht es, mehrere Bedingungen nacheinander zu testen. Der erste Zweig, dessen Bedingung `true` ist, wird ausgeführt, und der Rest wird übersprungen.

```dart
int score = 75;
if (score >= 90) {
  print('A');
} else if (score >= 70) {
  print('B');
} else {
  print('C');
}
// prints: B
```

---

Der **ternäre Operator** `condition ? expr1 : expr2` ist eine kompakte Möglichkeit, einen einfachen `if-else`-Ausdruck zu schreiben.

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

Wenn die Bedingung `true` ist, wird `expr1` verwendet; andernfalls wird `expr2` verwendet.
