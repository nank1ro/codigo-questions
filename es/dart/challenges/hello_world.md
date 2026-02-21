---
language: dart
exerciseType: 1
difficulty: 1
title: iHola Mundo!
---

# --description--

__"iHola, Mundo!"__ es el primer programa tradicional para comenzar a programar en un nuevo lenguaje o entorno.

# --instructions--

Escribe una funcion que devuelva la cadena "iHola, Mundo!".

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

La funcion deberia devolver "iHola, Mundo!".

```dart
  const expected = "iHola, Mundo!";
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
  return "iHola, Mundo!";
}
```

