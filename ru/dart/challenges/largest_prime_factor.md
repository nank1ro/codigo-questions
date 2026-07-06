---
language: dart
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Простые множители числа 13195 — это 5, 7, 13 и 29.

# --instructions--

Напишите функцию, которая возвращает наибольший простой множитель числа `number`.

Пример вызова функции:
```dart
print(largestPrimeFactor(13195));
// prints 29
```

# --seed--

```dart
int largestPrimeFactor(int number) {

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

Наибольший простой множитель числа 2 должен быть равен 2

```dart
  test('test1', () {
    expect(largestPrimeFactor(2), 2, reason: '--err-t1--');
  });
```

Наибольший простой множитель числа 3 должен быть равен 3

```dart
  test('test2', () {
    expect(largestPrimeFactor(3), 3, reason: '--err-t2--');
  });
```

Наибольший простой множитель числа 13195 должен быть равен 29

```dart
  test('test3', () {
    expect(largestPrimeFactor(13195), 29, reason: '--err-t3--');
  });
```

Наибольший простой множитель числа 600851475143 должен быть равен 6857

```dart
  test('test4', () {
    expect(largestPrimeFactor(600851475143), 6857, reason: '--err-t4--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int largestPrimeFactor(int number) {
  int largest = 1;
  int n = number;
  int factor = 2;
  while (factor * factor <= n) {
    while (n % factor == 0) {
      largest = factor;
      n ~/= factor;
    }
    factor++;
  }
  if (n > 1) {
    largest = n;
  }
  return largest;
}
```
