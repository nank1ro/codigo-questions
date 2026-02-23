---
language: dart
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Gegeben ein Name, geben Sie einen String mit der Nachricht zuruck:
`One for X, one for me.`
Wo `X` der gegebene Name ist.
Wenn jedoch der Name fehlt, geben Sie den String zuruck:
`One for you, one for me.`

# --instructions--

Schreiben Sie eine Funktion, die den korrekten String zuruckgibt, Beispiele:

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**: `James`
**output**: `One for James, one for me.`

**input**: `Martha`
**output**: `One for Martha, one for me.`

# --seed--

```dart
String twoForOne() {

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

Kein Name angegeben

```dart
  test('test1', () {
    expect(twoForOne(), "One for you, one for me.", reason: '--err-t1--');
  });
```

Geben Sie "James" als Name an

```dart
  test('test2', () {
    expect(twoForOne(name: "James"), "One for James, one for me.", reason: '--err-t2--');
  });
```

Geben Sie "Martha" als Name an

```dart
  test('test3', () {
    expect(twoForOne(name: "Martha"), "One for Martha, one for me.", reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String twoForOne({String? name}) {
  if (name != null) {
    return "One for $name, one for me.";
  }
  return "One for you, one for me.";
}
```


