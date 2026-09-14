---
language: dart
exerciseType: 1
difficulty: 1
title: Гипотеза Коллатца
---

# --description--

Гипотеза Коллатца начинается с любого положительного целого числа `n` и повторяет одно простое правило: если `n` чётное, разделите его пополам; если `n` нечётное, замените его на `3n + 1`. Рано или поздно последовательность достигает 1.

Например, если начать с 16, последовательность будет `16 -> 8 -> 4 -> 2 -> 1`, то есть потребуется 4 шага.

Никто никогда не доказывал, что это происходит всегда, но это выполняется для каждого проверенного числа.

# --instructions--

Напишите функцию `collatzSteps`, которая принимает положительное целое число `n` и возвращает количество шагов, необходимое, чтобы достичь 1.

`collatzSteps(1)` — это 0, потому что 1 уже является концом последовательности. `collatzSteps(12)` — это 9, а `collatzSteps(27)` — 111.

Пример вызова функции:
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

`collatzSteps(1)` должна возвращать 0, потому что 1 уже является концом последовательности.

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)` должна возвращать 1.

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)` должна возвращать 8.

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)` должна возвращать 16.

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)` должна возвращать 4.

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)` должна возвращать 9.

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)` должна возвращать 111.

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)` должна возвращать 118.

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
