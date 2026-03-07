---
language: dart
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Dane jest imię. Zwróć ciąg znaków z wiadomością:
`One for X, one for me.`
Gdzie `X` to podane imię.
Jednak jeśli imię nie zostało podane, zwróć ciąg znaków:
`One for you, one for me.`

# --instructions--

Napisz funkcję, która zwraca poprawny ciąg znaków, przykłady:

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

Nie podano imienia

```dart
  test('test1', () {
    expect(twoForOne(), "One for you, one for me.", reason: '--err-t1--');
  });
```

Podaj "James" jako imię

```dart
  test('test2', () {
    expect(twoForOne(name: "James"), "One for James, one for me.", reason: '--err-t2--');
  });
```

Podaj "Martha" jako imię

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


