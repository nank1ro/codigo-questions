---
language: dart
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Étant donné deux entiers `num1` et `num2`, écrivez un programme pour additionner ces deux nombres

# --instructions--

Écrivez une fonction qui retourne la somme de deux nombres.

Exemple d'appel de fonction :
```dart
print(addition(1, 2));
// prints 3
```

# --seed--

```dart
int addition() {
  
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

La somme de 1 et 3 doit être égale à 4

```dart
  test('test1', () {
    expect(addition(1, 3), 4, reason: '--err-t1--');
  });
```

La somme de 200 et 210 doit être égale à 410

```dart
  test('test2', () {
    expect(addition(200, 210), 410, reason: '--err-t2--');
  });
```

La somme de 15 et 35 doit être égale à 50

```dart
  test('test3', () {
    expect(addition(15, 35), 50, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int addition(int num1, int num2) {
  return num1 + num2;
}
```
