---
language: dart
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Każdy nowy wyraz ciągu Fibonacciego powstaje przez dodanie dwóch poprzednich wyrazów. Zaczynając od 1 i 2, pierwsze 10 wyrazów to: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# --instructions--

Napisz funkcję, która zwraca sumę wszystkich parzystych wyrazów ciągu Fibonacciego nieprzekraczających `n`.

Przykład wywołania funkcji:
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

Suma parzystych wyrazów Fibonacciego nieprzekraczających 8 musi być równa 10

```dart
  test('test1', () {
    expect(fibonacciEvenSum(8), 10, reason: '--err-t1--');
  });
```

Suma parzystych wyrazów Fibonacciego nieprzekraczających 10 musi być równa 10

```dart
  test('test2', () {
    expect(fibonacciEvenSum(10), 10, reason: '--err-t2--');
  });
```

Suma parzystych wyrazów Fibonacciego nieprzekraczających 34 musi być równa 44

```dart
  test('test3', () {
    expect(fibonacciEvenSum(34), 44, reason: '--err-t3--');
  });
```

Suma parzystych wyrazów Fibonacciego nieprzekraczających 1000 musi być równa 798

```dart
  test('test4', () {
    expect(fibonacciEvenSum(1000), 798, reason: '--err-t4--');
  });
```

Suma parzystych wyrazów Fibonacciego nieprzekraczających 4000000 musi być równa 4613732

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
