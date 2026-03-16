---
language: dart
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 — наименьшее число, которое делится без остатка на каждое из чисел от 1 до 10.

# --instructions--

Напишите функцию, которая возвращает наименьшее положительное число, делящееся на все числа от 1 до `n`.

Пример вызова функции:
```dart
print(smallestMultiple(10));
// prints 2520
```

# --seed--

```dart
int smallestMultiple(int n) {

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

Наименьшее кратное для чисел от 1 до 5 должно быть равно 60

```dart
  test('test1', () {
    expect(smallestMultiple(5), 60, reason: '--err-t1--');
  });
```

Наименьшее кратное для чисел от 1 до 10 должно быть равно 2520

```dart
  test('test2', () {
    expect(smallestMultiple(10), 2520, reason: '--err-t2--');
  });
```

Наименьшее кратное для чисел от 1 до 20 должно быть равно 232792560

```dart
  test('test3', () {
    expect(smallestMultiple(20), 232792560, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int _gcd(int a, int b) => b == 0 ? a : _gcd(b, a % b);

int _lcm(int a, int b) => a ~/ _gcd(a, b) * b;

int smallestMultiple(int n) {
  int result = 1;
  for (int i = 2; i <= n; i++) {
    result = _lcm(result, i);
  }
  return result;
}
```
