---
language: dart
exerciseType: 1
difficulty: 1
title: Deux pour un
---

# --description--

Étant donné un nom, retournez une chaîne avec le message :
`Un pour X, un pour moi.`
Où `X` est le nom donné.
Cependant, si le nom est manquant, retournez la chaîne :
`Un pour vous, un pour moi.`

# --instructions--

Écrivez une fonction qui retourne la chaîne correcte, exemples :

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

Aucun nom donné

```dart
  test('test1', () {
    expect(twoForOne(), "One for you, one for me.", reason: '--err-t1--');
  });
```

Passer "James" comme nom

```dart
  test('test2', () {
    expect(twoForOne(name: "James"), "One for James, one for me.", reason: '--err-t2--');
  });
```

Passer "Martha" comme nom

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


