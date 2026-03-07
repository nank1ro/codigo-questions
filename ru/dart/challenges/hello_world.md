---
language: dart
exerciseType: 1
difficulty: 1
title: Привет, мир!
---

# --description--

__"Привет, мир!"__ — это традиционная первая программа для начинающих программировать на новом языке или в новой среде.

# --instructions--

Напишите функцию, которая возвращает строку "Hello, World!".

# --seed--

```dart
String hello() {

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

Функция должна возвращать "Hello, World!".

```dart
  const expected = "Hello, World!";
  test('test1', () {
    expect(hello(), expected, reason: '--err-t1--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String hello() {
  return "Hello, World!";
}
```

