Instrukcja **`if`** wykonuje blok kodu tylko wtedy, gdy warunek jest `true`.

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

Kod wewnątrz nawiasów klamrowych jest wykonywany tylko wtedy, gdy warunek `age >= 18` jest `true`.

---

Możesz użyć `print()` wewnątrz bloku `if`, aby wyświetlić wiadomość, gdy warunek jest spełniony.

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

Jeśli `isRaining` jest `false`, nic nie jest drukowane.

---

Instrukcja **`if-else`** wykonuje blok `if`, gdy warunek jest `true`, a blok `else`, gdy jest `false`.

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

Zawsze wykonywana jest dokładnie jedna z dwóch gałęzi.

---

**`else if`** pozwala testować wiele warunków po kolei. Wykonywana jest pierwsza gałąź, której warunek jest `true`, a pozostałe są pomijane.

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

**Operator trójargumentowy** `condition ? expr1 : expr2` to zwięzły sposób zapisu prostego wyrażenia `if-else`.

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

Jeśli warunek jest `true`, używane jest `expr1`; w przeciwnym razie używane jest `expr2`.
