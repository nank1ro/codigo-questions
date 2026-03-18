---
language: dart
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. A soma desses múltiplos é 23.

# --instructions--

Escreva uma função que retorna a soma de todos os múltiplos de 3 ou 5 abaixo de `number`.

Exemplo de chamada de função:
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

A soma dos múltiplos de 3 ou 5 abaixo de 10 deve ser igual a 23

```dart
  test('test1', () {
    expect(multiplesOf3And5(10), 23, reason: '--err-t1--');
  });
```

A soma dos múltiplos de 3 ou 5 abaixo de 1000 deve ser igual a 233168

```dart
  test('test2', () {
    expect(multiplesOf3And5(1000), 233168, reason: '--err-t2--');
  });
```

A soma dos múltiplos de 3 ou 5 abaixo de 6987 deve ser igual a 11390208

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
