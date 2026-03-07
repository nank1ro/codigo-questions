---
language: dart
exerciseType: 1
difficulty: 3
title: Високосный год
---

# --description--

В календарном году ровно 365,25 дней. Но в конечном итоге это приводит к путанице, потому что люди обычно считают целыми числами, а не десятичными дробями. Поэтому, чтобы избежать этого, было решено суммировать все 0,25 дня каждые четыре года и давать этому году 366 дней (включая 29 февраля как дополнительный день) и называть его __високосным годом__. Остальные три года в четырёхлетнем цикле содержат только 365 дней и __не являются високосными__.

# --instructions--

В этом задании мы усложняем задачу: вам нужно определить, является ли год високосным, без использования класса `DateTime`, операторов `switch`, блоков __if__, блоков __if-else__ или __тернарного оператора__ (`x ? a : b`), а также логических операторов __И__ (`&&`) и __ИЛИ__ (`||`), за исключением оператора __НЕ__ (`!`).

Верните `true`, если год високосный, `false` в противном случае.

Пример вызова функции:
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

Использование `DateTime`, `switch`, `if`, `else`, `&&`, `||` или `?` не допускается.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Год `2016` является високосным.

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

Год `1996` является високосным.

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

Год `1600` является високосным.

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

Год `2020` является високосным.

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

Год `2000` является високосным.

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

Год `2008` является високосным.

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

Год `1521` не является високосным.

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

Год `1800` не является високосным.

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

Год `2007` не является високосным.

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

Год `2002` не является високосным.

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

Год `1979` не является високосным.

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

Год `2006` не является високосным.

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
