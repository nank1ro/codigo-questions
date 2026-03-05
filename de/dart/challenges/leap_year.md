---
language: dart
exerciseType: 1
difficulty: 3
title: Schaltjahr
---

# --description--

In einem Kalenderjahr gibt es genau 365,25 Tage. Aber das führt schließlich zu Verwirrung, weil Menschen normalerweise durch genaue Teilbarkeit von 1 zählen und nicht mit Dezimalzahlen. Um das letztere zu vermeiden, wurde entschieden, alle 0,25 Tage alle vier Jahre zu addieren und diesem Jahr 366 Tage zu geben (einschließlich 29. Februar als Schalttag) und es ein __Schaltjahr__ zu nennen. Die anderen drei Jahre im Vier-Jahres-Zyklus würden nur 365 Tage enthalten und __keine Schaltjahre sein__.

# --instructions--

In dieser Herausforderung nehmen wir es auf die nächste Stufe, wo Sie bestimmen müssen, ob es ein Schaltjahr ist oder nicht, ohne die Verwendung der `DateTime`-Klasse, `switch`-Anweisungen, __if-Blöcke__, __if-else-Blöcke__ oder __ternäre Operation__ (`x ? a : b`) noch die logischen Operatoren __AND__ (`&&`) und __OR__ (`||`) mit Ausnahme des __NOT__ (`!`)-Operators.

Geben Sie `true` zurück, wenn es ein Schaltjahr ist, `false` andernfalls.

Beispiel eines Funktionsaufrufs:
```dart
print(leapYear(2000));
// prints true
```

# --seed--

```dart
bool leapYear(int year) {
  
}
```

# --before-asserts--

```dart
import 'package:dart_runner/main.dart';
import 'package:test/test.dart';

void main() {
  group('MainTest -', () {
```

# --asserts--

Die Verwendung von `DateTime`, `switch`, `if`, `else`, `&&`, `||` oder `?` ist nicht zulässig.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Das Jahr `2016` ist ein Schaltjahr.

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

Das Jahr `1996` ist ein Schaltjahr.

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

Das Jahr `1600` ist ein Schaltjahr.

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

Das Jahr `2020` ist ein Schaltjahr.

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

Das Jahr `2000` ist ein Schaltjahr.

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

Das Jahr `2008` ist ein Schaltjahr.

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

Das Jahr `1521` ist kein Schaltjahr.

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

Das Jahr `1800` ist kein Schaltjahr.

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

Das Jahr `2007` ist kein Schaltjahr.

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

Das Jahr `2002` ist kein Schaltjahr.

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

Das Jahr `1979` ist kein Schaltjahr.

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

Das Jahr `2006` ist kein Schaltjahr.

```dart
  test('test12', () {
    expect(leapYear(2006), false, reason: '--err-t12--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool leapYear(int year) {
  return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0));
}
```

```dart
bool leapYear(int year) {
  while (year % 100 == 0) {
    year = year ~/ 100;
  }
  return year % 4 == 0;
}
```
