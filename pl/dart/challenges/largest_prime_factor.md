---
language: dart
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Czynniki pierwsze liczby 13195 to 5, 7, 13 i 29.

# --instructions--

Napisz funkcję, która zwraca największy czynnik pierwszy liczby `number`.

Przykład wywołania funkcji:
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

Największy czynnik pierwszy liczby 2 musi być równy 2

```dart
  test('test1', () {
    expect(largestPrimeFactor(2), 2, reason: '--err-t1--');
  });
```

Największy czynnik pierwszy liczby 3 musi być równy 3

```dart
  test('test2', () {
    expect(largestPrimeFactor(3), 3, reason: '--err-t2--');
  });
```

Największy czynnik pierwszy liczby 13195 musi być równy 29

```dart
  test('test3', () {
    expect(largestPrimeFactor(13195), 29, reason: '--err-t3--');
  });
```

Największy czynnik pierwszy liczby 600851475143 musi być równy 6857

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
