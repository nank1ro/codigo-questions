---
language: dart
exerciseType: 1
difficulty: 1
title: Hallo Welt!
---

# --description--

__"Hallo, Welt!"__ ist das traditionelle erste Programm, um mit dem Programmieren in einer neuen Sprache oder Umgebung zu beginnen.

# --instructions--

Schreiben Sie eine Funktion, die den String "Hallo, Welt!" zurückgibt.

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

Die Funktion sollte "Hallo, Welt!" zurückgeben.

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

