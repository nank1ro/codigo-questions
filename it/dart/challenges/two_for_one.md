---
language: dart
exerciseType: 1
difficulty: 1
title: Due per uno
---

# --description--

Dato un nome, restituire una stringa con il messaggio:
`Uno per X, uno per me.`
Dove `X` e' il nome dato.
Tuttavia, se il nome è vuoto, restituire la stringa:
`Uno per te, uno per me.`

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

**input**: `"Walter"`
**output**: `Uno per Walter, uno per me.`

**input**: `""`
**output**: `Uno per te, uno per me.`

**input**: `"Davide"`
**output**: `Uno per Davide, uno per me.`

# --seed--

```dart
String duePerUno() {
  
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

Nome vuoto

```dart
  test('test1', () {
    expect(duePerUno(), "Uno per te, uno per me.", reason: '--err-t1--');
  });
```

Dividi con "Daniele"

```dart
  test('test2', () {
    expect(duePerUno(nome: "Daniele"), "Uno per Daniele, uno per me.", reason: '--err-t2--');
  });
```

Dividi con "Marta"

```dart
  test('test3', () {
    expect(duePerUno(nome: "Marta"), "Uno per Marta, uno per me.", reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String duePerUno({String? nome}) {
  if (nome != null) {
    return "Uno per $nome, uno per me.";
  }
  return "Uno per te, uno per me.";
}
```


