---
language: dart
exerciseType: 1
difficulty: 3
title: Année bissextile
---

# --description--

Dans une année civile, il y a exactement 365,25 jours. Mais, éventuellement, cela créera de la confusion car les humains comptent normalement par divisibilité exacte par 1 et non avec des points décimaux. Donc, pour éviter ce dernier, il a été décidé d'ajouter tous les 0,25 jours tous les quatre ans et de donner à cette année 366 jours (incluant le 29 février en tant que jour intercalaire) et de l'appeler une __année bissextile__. Les trois autres années du cycle de quatre ans ne contiendraient que 365 jours et ne seraient pas des années bissextiles.

# --instructions--

In this challenge we'll take it to a new level, where you are to determine if it's a leap year or not without the use of the `DateTime` class, `switch` statements, __if blocks__, __if-else blocks__ or __ternary operation__ (`x ? a : b`) nor the logical operators __AND__ (`&&`) and __OR__ (`||`) with the exemption of the __NOT__ (`!`) operator.

Return `true` if it's a leap year, `false` otherwise.

Exemple d'appel de fonction :
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

L'utilisation de `DateTime`, `switch`, `if`, `else`, `&&`, `||` ou `?` n'est pas autorisée.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

L'année `2016` est une année bissextile.

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

The year `1996` is a leap year.

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

The year `1600` is a leap year.

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

The year `2020` is a leap year.

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

The year `2000` is a leap year.

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

The year `2008` is a leap year.

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

The year `1521` is not a leap year.

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

The year `1800` is not a leap year.

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

The year `2007` is not a leap year.

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

The year `2002` is not a leap year.

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

The year `1979` is not a leap year.

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

The year `2006` is not a leap year.

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
