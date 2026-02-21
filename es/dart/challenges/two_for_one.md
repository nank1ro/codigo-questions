---
language: dart
exerciseType: 1
difficulty: 1
title: Dos por uno
---

# --description--

Dado un nombre, devuelve una cadena con el mensaje:
`Uno para X, uno para mi.`
Donde `X` es el nombre dado.
Sin embargo, si falta el nombre, devuelve la cadena:
`Uno para ti, uno para mi.`

# --instructions--

Escribe una funcion que devuelva la cadena correcta, ejemplos:

**entrada**: `Walter`
**salida**: `Uno para Walter, uno para mi.`

**entrada**: `James`
**salida**: `Uno para James, uno para mi.`

**entrada**: `Martha`
**salida**: `Uno para Martha, uno para mi.`

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

No se da ningun nombre

```dart
  test('test1', () {
    expect(twoForOne(), "Uno para ti, uno para mi.", reason: '--err-t1--');
  });
```

Pasar "James" como nombre

```dart
  test('test2', () {
    expect(twoForOne(name: "James"), "Uno para James, uno para mi.", reason: '--err-t2--');
  });
```

Pasar "Martha" como nombre

```dart
  test('test3', () {
    expect(twoForOne(name: "Martha"), "Uno para Martha, uno para mi.", reason: '--err-t3--');
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
    return "Uno para $name, uno para mi.";
  }
  return "Uno para ti, uno para mi.";
}
```

