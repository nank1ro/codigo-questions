---
language: dart
exerciseType: 1
difficulty: 1
title: Сложение
---

# --description--

Даны два целых числа `num1` и `num2`, напишите программу для сложения этих двух чисел

# --instructions--

Напишите функцию, которая возвращает сумму двух чисел.

Пример вызова функции:
```dart
print(addition(1, 2));
// prints 3
```

# --seed--

```dart
int addition() {
  
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

Сумма 1 и 3 должна быть равна 4

```dart
  test('test1', () {
    expect(addition(1, 3), 4, reason: '--err-t1--');
  });
```

Сумма 200 и 210 должна быть равна 410

```dart
  test('test2', () {
    expect(addition(200, 210), 410, reason: '--err-t2--');
  });
```

Сумма 15 и 35 должна быть равна 50

```dart
  test('test3', () {
    expect(addition(15, 35), 50, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int addition(int num1, int num2) {
  return num1 + num2;
}
```
