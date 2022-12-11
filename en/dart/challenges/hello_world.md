---
language: dart
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ is the traditional first program for beginning programming in a new language or environment.

# --instructions--

Write a function that returns the string "Hello, World!".

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

The function should return "Hello, World!".

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

