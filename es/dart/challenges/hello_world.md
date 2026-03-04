---
language: dart
exerciseType: 1
difficulty: 1
title: ¡Hola Mundo!
---

# --description--

__"¡Hola, Mundo!"__ es el programa tradicional para comenzar a programar en un nuevo lenguaje o entorno.

# --instructions--

Escribe una función que devuelva la cadena "Hello, World!".

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

La función debe devolver "Hello, World!".

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

