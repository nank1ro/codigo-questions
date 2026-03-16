---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

A soma dos quadrados dos primeiros dez números naturais é 1² + 2² + ... + 10² = 385.

O quadrado da soma dos primeiros dez números naturais é (1 + 2 + ... + 10)² = 55² = 3025.

A diferença entre o quadrado da soma e a soma dos quadrados de 1 a 10 é 3025 − 385 = 2640.

# --instructions--

Escreva uma função que retorna a diferença entre o quadrado da soma e a soma dos quadrados dos primeiros `n` números naturais.

Exemplo de chamada de função:
```dart
print(sumSquareDifference(10));
// prints 2640
```

# --seed--

```dart
int sumSquareDifference(int n) {

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

A diferença soma-quadrado para n=10 deve ser igual a 2640

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

A diferença soma-quadrado para n=20 deve ser igual a 41230

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

A diferença soma-quadrado para n=100 deve ser igual a 25164150

```dart
  test('test3', () {
    expect(sumSquareDifference(100), 25164150, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumSquareDifference(int n) {
  int sumOfSquares = 0;
  int sum = 0;
  for (int i = 1; i <= n; i++) {
    sumOfSquares += i * i;
    sum += i;
  }
  return sum * sum - sumOfSquares;
}
```
