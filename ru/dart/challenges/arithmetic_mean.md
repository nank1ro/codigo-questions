---
language: dart
exerciseType: 1
difficulty: 1
title: Среднее арифметическое
---

# --description--

Напишите функцию `mean` для нахождения _среднего арифметического_ числового вектора.

# --instructions--

Напишите функцию, которая возвращает среднее арифметическое числового вектора.

Пример вызова функции:
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

Среднее арифметическое `[1, 2, 3, 4, 5, 6, 7]` должно быть равно 4.0

```dart
  test('test1', () {
    expect(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, reason: '--err-t1--');
  });
```

Среднее арифметическое `[4, 5, 6]` должно быть равно 5.0

```dart
  test('test2', () {
    expect(mean([4, 5, 6]), 5.0, reason: '--err-t2--');
  });
```

Среднее арифметическое `[12, 34, 56, 78]` должно быть равно 45.0

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
