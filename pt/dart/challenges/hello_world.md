---
language: dart
exerciseType: 1
difficulty: 1
title: "Olá Mundo!"
---

# --description--

__"Hello, World!"__ é o tradicional primeiro programa para quem está começando a programar em uma nova linguagem ou ambiente.

# --instructions--

Escreva uma função que retorne a string "Hello, World!".

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

A função deve retornar "Hello, World!".

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

