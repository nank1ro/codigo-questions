---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

Сумма квадратов первых десяти натуральных чисел равна 1² + 2² + ... + 10² = 385.

Квадрат суммы первых десяти натуральных чисел равен (1 + 2 + ... + 10)² = 55² = 3025.

Разность между квадратом суммы и суммой квадратов для чисел от 1 до 10 равна 3025 − 385 = 2640.

# --instructions--

Напишите функцию, которая возвращает разность между квадратом суммы и суммой квадратов первых `n` натуральных чисел.

Пример вызова функции:
```dart
print(sumSquareDifference(10));
// prints 2640
```

# --seed--

```dart
int sumSquareDifference(int n) {

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

Разность квадратов сумм для n=10 должна быть равна 2640

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

Разность квадратов сумм для n=20 должна быть равна 41230

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

Разность квадратов сумм для n=100 должна быть равна 25164150

```dart
  test('test3', () {
    expect(sumSquareDifference(100), 25164150, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumSquareDifference(int n) {
  int sumOfSquares = 0;
  int sum = 0;
  for (int i = 1; i <= n; i++) {
    sumOfSquares += i * i;
    sum += i;
  }
  return sum * sum - sumOfSquares;
}
```
