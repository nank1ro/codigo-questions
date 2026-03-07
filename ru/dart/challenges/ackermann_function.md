---
language: dart
exerciseType: 1
difficulty: 1
title: Функция Аккермана
---

# --description--

Функция Аккермана — это классический пример рекурсивной функции, примечательной тем, что она не является примитивно рекурсивной. Она очень быстро растёт в значении, как и размер её дерева вызовов.

Функция Аккермана обычно определяется следующим образом:

![ackermann_function](https://bit.ly/3z9u4zh)

Её аргументы никогда не отрицательны, и она всегда завершается

# --instructions--

Напишите функцию, которая возвращает значение функции Аккермана.

# --seed--

```dart
int ack(int m, int n) {
    
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

`ack(0, 0)` должно вернуть 1.

```dart
    test('test1', () {
      expect(ack(0, 0), 1, reason: '--err-t1--');
    });
```

`ack(1, 1)` должно вернуть 3.

```dart
    test('test2', () {
      expect(ack(1, 1), 3, reason: '--err-t2--');
    });
```

`ack(2, 5)` должно вернуть 13.

```dart
    test('test3', () {
      expect(ack(2, 5), 13, reason: '--err-t3--');
    });
```

`ack(3, 3)` должно вернуть 61.

```dart
    test('test4', () {
      expect(ack(3, 3), 61, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int ack(int m, int n) {
  if (m == 0) return n + 1;
  return ack(
    m - 1,
    (n == 0) ? 1 : ack(m, n - 1),
  );
}
```
