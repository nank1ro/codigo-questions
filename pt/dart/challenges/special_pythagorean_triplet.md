---
language: dart
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Uma tripla pitagórica é um conjunto de três números naturais, a < b < c, para os quais a² + b² = c².

Por exemplo, 3² + 4² = 9 + 16 = 25 = 5². Existe exatamente uma tripla pitagórica para a qual a + b + c = 1000.

# --instructions--

Escreva uma função que encontra a tripla pitagórica onde a + b + c é igual a `n`, e retorna o produto a × b × c.

Exemplo de chamada de função:
```dart
print(specialPythagoreanTriplet(12));
// prints 60
```

# --seed--

```dart
int specialPythagoreanTriplet(int n) {

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

O produto da tripla pitagórica onde a+b+c=12 deve ser igual a 60

```dart
  test('test1', () {
    expect(specialPythagoreanTriplet(12), 60, reason: '--err-t1--');
  });
```

O produto da tripla pitagórica onde a+b+c=1000 deve ser igual a 31875000

```dart
  test('test2', () {
    expect(specialPythagoreanTriplet(1000), 31875000, reason: '--err-t2--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int specialPythagoreanTriplet(int n) {
  for (int a = 1; a < n; a++) {
    for (int b = a + 1; b < n - a; b++) {
      int c = n - a - b;
      if (c > b && a * a + b * b == c * c) {
        return a * b * c;
      }
    }
  }
  return -1;
}
```
