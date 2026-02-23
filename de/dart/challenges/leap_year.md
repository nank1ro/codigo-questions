---
language: dart
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

In einem Kalenderjahr gibt es genau 365,25 Tage. Das wird aber fruher oder spater zu Verwirrung fuhren, da Menschen normalerweise mit exakter Teilbarkeit durch 1 zahlen und nicht mit Dezimalstellen. Um Letzteres zu vermeiden, wurde beschlossen, alle 0,25 Tage alle vier Jahre zusammenzufassen und diesem Jahr 366 Tage zu geben (einschlieich des 29. Februar als Schalttag) und es __Schaltjahr__ zu nennen. Die anderen drei Jahre im Vierjahreszyklus wurden nur 365 Tage enthalten und __keine Schaltjahre__ sein.

# --instructions--

In dieser Herausforderung werden wir es auf eine neue Stufe heben, bei der Sie bestimmen mussen, ob es ein Schaltjahr ist oder nicht, ohne die `DateTime`-Klasse, `switch`-Anweisungen, __if-Blocke__, __if-else-Blocke__ oder __ternaren Operation__ (`x ? a : b`) sowie die logischen Operatoren __UND__ (`&&`) und __ODER__ (`||`) mit Ausnahme des __NICHT__ (`!`) Operators zu verwenden.

Geben Sie `true` zuruck, wenn es ein Schaltjahr ist, andernfalls `false`.

Beispiel fur einen Funktionsaufruf:
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

Die Verwendung von `DateTime`, `switch`, `if`, `else`, `&&`, `||` oder `?` ist nicht erlaubt.

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
