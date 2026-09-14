---
language: dart
exerciseType: 1
difficulty: 1
title: Collatz conjecture
---

# --description--

The Collatz conjecture starts from any positive integer `n` and repeats one simple rule: if `n` is even, halve it; if `n` is odd, replace it with `3n + 1`. Sooner or later the sequence reaches 1.

For example, starting from 16 the sequence is `16 -> 8 -> 4 -> 2 -> 1`, so it takes 4 steps.

Nobody has ever proved that this always happens, but it holds for every number ever tested.

# --instructions--

Write a function `collatzSteps` that takes a positive integer `n` and returns the number of steps needed to reach 1.

`collatzSteps(1)` is 0, because 1 is already the end of the sequence. `collatzSteps(12)` is 9, and `collatzSteps(27)` is 111.

Example of function call:
```dart
print(collatzSteps(16));
// prints 4
```

# --seed--

```dart
int collatzSteps(int n) {

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

`collatzSteps(1)` should return 0, because 1 is already the end of the sequence.

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)` should return 1.

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)` should return 8.

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)` should return 16.

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)` should return 4.

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)` should return 9.

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)` should return 111.

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)` should return 118.

```dart
    test('test8', () {
      expect(collatzSteps(97), 118, reason: '--err-t8--');
    });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int collatzSteps(int n) {
  int value = n;
  int steps = 0;
  while (value != 1) {
    value = value % 2 == 0 ? value ~/ 2 : 3 * value + 1;
    steps++;
  }
  return steps;
}
```
