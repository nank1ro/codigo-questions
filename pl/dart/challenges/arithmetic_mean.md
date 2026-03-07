---
language: dart
exerciseType: 1
difficulty: 1
title: Arithmetic mean
---

# --description--

Napisz funkcję o nazwie `mean`, która wyznacza _średnią arytmetyczną_ wektora liczb.

# --instructions--

Napisz funkcję, która zwraca średnią wektora liczb.

Przykład wywołania funkcji:
```dart
print(mean([1, 2, 3]));
// prints 2.0
```

# --seed--

```dart
num mean() {
  
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

Średnia `[1, 2, 3, 4, 5, 6, 7]` musi być równa 4.0

```dart
  test('test1', () {
    expect(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, reason: '--err-t1--');
  });
```

Średnia `[4, 5, 6]` musi być równa 5.0

```dart
  test('test2', () {
    expect(mean([4, 5, 6]), 5.0, reason: '--err-t2--');
  });
```

Średnia `[12, 34, 56, 78]` musi być równa 45.0

```dart
  test('test3', () {
    expect(mean([12, 34, 56, 78]), 45.0, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
num mean(List<num> numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
