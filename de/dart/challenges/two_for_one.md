---
language: dart
exerciseType: 1
difficulty: 1
title: Zwei für einen
---

# --description--

Geben Sie einen Namen an, geben Sie einen String mit der Nachricht zurück:
`Einer für X, einer für mich.`
Wobei `X` der angegebene Name ist.
Wenn der Name jedoch fehlt, geben Sie den String zurück:
`Einer für dich, einer für mich.`

# --instructions--

Schreiben Sie eine Funktion, die den richtigen String zurückgibt, Beispiele:

**Eingabe**: `Walter`
**Ausgabe**: `One for Walter, one for me.`

**Eingabe**: `James`
**Ausgabe**: `One for James, one for me.`

**Eingabe**: `Martha`
**Ausgabe**: `One for Martha, one for me.`

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

Kein Name gegeben

```dart
  test('test1', () {
    expect(twoForOne(), "One for you, one for me.", reason: '--err-t1--');
  });
```

"James" als Name übergeben

```dart
  test('test2', () {
    expect(twoForOne(name: "James"), "One for James, one for me.", reason: '--err-t2--');
  });
```

"Martha" als Name übergeben

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


