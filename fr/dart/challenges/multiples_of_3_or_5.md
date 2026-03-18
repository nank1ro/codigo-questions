---
language: dart
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Si nous listons tous les nombres naturels inférieurs à 10 qui sont des multiples de 3 ou 5, nous obtenons 3, 5, 6 et 9. La somme de ces multiples est 23.

# --instructions--

Écris une fonction qui retourne la somme de tous les multiples de 3 ou 5 inférieurs à `number`.

Exemple d'appel de fonction :
```dart
print(multiplesOf3And5(10));
// prints 23
```

# --seed--

```dart
int multiplesOf3And5(int number) {

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

La somme des multiples de 3 ou 5 inférieurs à 10 doit être égale à 23

```dart
  test('test1', () {
    expect(multiplesOf3And5(10), 23, reason: '--err-t1--');
  });
```

La somme des multiples de 3 ou 5 inférieurs à 1000 doit être égale à 233168

```dart
  test('test2', () {
    expect(multiplesOf3And5(1000), 233168, reason: '--err-t2--');
  });
```

La somme des multiples de 3 ou 5 inférieurs à 6987 doit être égale à 11390208

```dart
  test('test3', () {
    expect(multiplesOf3And5(6987), 11390208, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int multiplesOf3And5(int number) {
  int sum = 0;
  for (int i = 1; i < number; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      sum += i;
    }
  }
  return sum;
}
```
