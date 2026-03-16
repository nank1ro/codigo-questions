---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.

The difference between the square of the sum and the sum of the squares for 1 to 10 is 3025 − 385 = 2640.

# --instructions--

Write a function that returns the difference between the square of the sum and the sum of the squares of the first `n` natural numbers.

Example of function call:
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

The sum square difference for n=10 must equal 2640

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

The sum square difference for n=20 must equal 41230

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

The sum square difference for n=100 must equal 25164150

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
