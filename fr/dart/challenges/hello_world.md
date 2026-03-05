---
language: dart
exerciseType: 1
difficulty: 1
title: Bonjour le monde !
---

# --description--

"__Bonjour, le monde !__" est le programme traditionnel pour commencer la programmation dans un nouveau langage ou environnement.

# --instructions--

Écrivez une fonction qui retourne la chaîne "Bonjour, le monde !".

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

La fonction doit retourner "Bonjour, le monde !".

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

