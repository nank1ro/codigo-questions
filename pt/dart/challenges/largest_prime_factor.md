---
language: dart
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Os fatores primos de 13195 são 5, 7, 13 e 29.

# --instructions--

Escreva uma função que retorna o maior fator primo de `number`.

Exemplo de chamada de função:
```dart
print(largestPrimeFactor(13195));
// prints 29
```

# --seed--

```dart
int largestPrimeFactor(int number) {

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

O maior fator primo de 2 deve ser igual a 2

```dart
  test('test1', () {
    expect(largestPrimeFactor(2), 2, reason: '--err-t1--');
  });
```

O maior fator primo de 3 deve ser igual a 3

```dart
  test('test2', () {
    expect(largestPrimeFactor(3), 3, reason: '--err-t2--');
  });
```

O maior fator primo de 13195 deve ser igual a 29

```dart
  test('test3', () {
    expect(largestPrimeFactor(13195), 29, reason: '--err-t3--');
  });
```

O maior fator primo de 600851475143 deve ser igual a 6857

```dart
  test('test4', () {
    expect(largestPrimeFactor(600851475143), 6857, reason: '--err-t4--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int largestPrimeFactor(int number) {
  int largest = 1;
  int n = number;
  int factor = 2;
  while (factor * factor <= n) {
    while (n % factor == 0) {
      largest = factor;
      n ~/= factor;
    }
    factor++;
  }
  if (n > 1) {
    largest = n;
  }
  return largest;
}
```
