---
language: dart
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ ist das traditionelle erste Programm fur den Anfang der Programmierung in einer neuen Sprache oder Umgebung.

# --instructions--

Schreiben Sie eine Funktion, die den String "Hello, World!" zuruckgibt.

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

Die Funktion sollte "Hello, World!" zuruckgeben.

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

