---
language: dart
exerciseType: 1
difficulty: 1
title: Media aritmética
---

# --description--

Escribe una función llamada `mean` para encontrar el _promedio aritmético_ de un vector numérico.

# --instructions--

Escribe una función que devuelva la media de un vector numérico.

Ejemplo de llamada de función:
```dart
print(mean([1, 2, 3]));
// prints 2.0
```

# --seed--

```dart
num mean() {

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

La media de `[1, 2, 3, 4, 5, 6, 7]` debe ser igual a 4.0

```dart
  test('test1', () {
    expect(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, reason: '--err-t1--');
  });
```

La media de `[4, 5, 6]` debe ser igual a 5.0

```dart
  test('test2', () {
    expect(mean([4, 5, 6]), 5.0, reason: '--err-t2--');
  });
```

La media de `[12, 34, 56, 78]` debe ser igual a 45.0

```dart
  test('test3', () {
    expect(mean([12, 34, 56, 78]), 45.0, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
num mean(List<num> numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
