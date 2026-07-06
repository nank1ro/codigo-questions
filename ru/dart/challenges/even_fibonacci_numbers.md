---
language: dart
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Каждый новый член последовательности Фибоначчи формируется путём сложения двух предыдущих членов. Начиная с 1 и 2, первые 10 членов: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# --instructions--

Напишите функцию, которая возвращает сумму всех чётных членов последовательности Фибоначчи, не превышающих `n`.

Пример вызова функции:
```dart
print(fibonacciEvenSum(8));
// prints 10
```

# --seed--

```dart
int fibonacciEvenSum(int n) {

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

Сумма чётных членов Фибоначчи, не превышающих 8, должна быть равна 10

```dart
  test('test1', () {
    expect(fibonacciEvenSum(8), 10, reason: '--err-t1--');
  });
```

Сумма чётных членов Фибоначчи, не превышающих 10, должна быть равна 10

```dart
  test('test2', () {
    expect(fibonacciEvenSum(10), 10, reason: '--err-t2--');
  });
```

Сумма чётных членов Фибоначчи, не превышающих 34, должна быть равна 44

```dart
  test('test3', () {
    expect(fibonacciEvenSum(34), 44, reason: '--err-t3--');
  });
```

Сумма чётных членов Фибоначчи, не превышающих 1000, должна быть равна 798

```dart
  test('test4', () {
    expect(fibonacciEvenSum(1000), 798, reason: '--err-t4--');
  });
```

Сумма чётных членов Фибоначчи, не превышающих 4000000, должна быть равна 4613732

```dart
  test('test5', () {
    expect(fibonacciEvenSum(4000000), 4613732, reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int fibonacciEvenSum(int n) {
  int sum = 0;
  int a = 1, b = 2;
  while (a <= n) {
    if (a % 2 == 0) {
      sum += a;
    }
    int temp = a + b;
    a = b;
    b = temp;
  }
  return sum;
}
```
