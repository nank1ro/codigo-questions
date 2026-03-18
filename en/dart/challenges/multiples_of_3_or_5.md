---
language: dart
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

If we list all natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.

# --instructions--

Write a function that returns the sum of all multiples of 3 or 5 below `number`.

Example of function call:
```dart
print(multiplesOf3And5(10));
// prints 23
```

# --seed--

```dart
int multiplesOf3And5(int number) {

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

The sum of multiples of 3 or 5 below 10 must equal 23

```dart
  test('test1', () {
    expect(multiplesOf3And5(10), 23, reason: '--err-t1--');
  });
```

The sum of multiples of 3 or 5 below 1000 must equal 233168

```dart
  test('test2', () {
    expect(multiplesOf3And5(1000), 233168, reason: '--err-t2--');
  });
```

The sum of multiples of 3 or 5 below 6987 must equal 11390208

```dart
  test('test3', () {
    expect(multiplesOf3And5(6987), 11390208, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int multiplesOf3And5(int number) {
  int sum = 0;
  for (int i = 1; i < number; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      sum += i;
    }
  }
  return sum;
}
```
