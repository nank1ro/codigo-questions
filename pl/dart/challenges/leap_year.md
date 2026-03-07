---
language: dart
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

W roku kalendarzowym jest dokładnie 365,25 dnia. Z czasem jednak prowadziłoby to do zamieszania, ponieważ ludzie zazwyczaj liczą przez dokładną podzielność przez 1, a nie ułamkami dziesiętnymi. Aby tego uniknąć, postanowiono sumować wszystkie 0,25 dnia w każdym czteroletnim cyklu i nadawać temu rokowi 366 dni (łącznie z 29 lutego jako dniem przestępnym), nazywając go __rokiem przestępnym__. Pozostałe trzy lata w cyklu czteroletnim miałyby tylko 365 dni i __nie byłyby latami przestępnymi__.

# --instructions--

W tym wyzwaniu podnosimy poprzeczkę – musisz określić, czy dany rok jest rokiem przestępnym, bez użycia klasy `DateTime`, instrukcji `switch`, __bloków if__, __bloków if-else__ ani __operacji trójargumentowej__ (`x ? a : b`), a także bez operatorów logicznych __AND__ (`&&`) i __OR__ (`||`), z wyjątkiem operatora __NOT__ (`!`).

Zwróć `true` jeśli to rok przestępny, `false` w przeciwnym razie.

Przykład wywołania funkcji:
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

Użycie `DateTime`, `switch`, `if`, `else`, `&&`, `||` lub `?` jest niedozwolone.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Rok `2016` jest rokiem przestępnym.

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

Rok `1996` jest rokiem przestępnym.

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

Rok `1600` jest rokiem przestępnym.

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

Rok `2020` jest rokiem przestępnym.

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

Rok `2000` jest rokiem przestępnym.

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

Rok `2008` jest rokiem przestępnym.

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

Rok `1521` nie jest rokiem przestępnym.

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

Rok `1800` nie jest rokiem przestępnym.

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

Rok `2007` nie jest rokiem przestępnym.

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

Rok `2002` nie jest rokiem przestępnym.

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

Rok `1979` nie jest rokiem przestępnym.

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

Rok `2006` nie jest rokiem przestępnym.

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
