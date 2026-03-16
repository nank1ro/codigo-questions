---
language: dart
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# --instructions--

Write a function that returns the smallest positive number that is evenly divisible by all numbers from 1 to `n`.

Example of function call:
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

The smallest multiple for 1 to 5 must equal 60

```dart
  test('test1', () {
    expect(smallestMultiple(5), 60, reason: '--err-t1--');
  });
```

The smallest multiple for 1 to 10 must equal 2520

```dart
  test('test2', () {
    expect(smallestMultiple(10), 2520, reason: '--err-t2--');
  });
```

The smallest multiple for 1 to 20 must equal 232792560

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
