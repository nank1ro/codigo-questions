---
language: dart
exerciseType: 1
difficulty: 1
title: Conjectura de Collatz
---

# --description--

A conjectura de Collatz parte de qualquer número inteiro positivo `n` e repete uma regra simples: se `n` é par, divida-o pela metade; se `n` é ímpar, substitua-o por `3n + 1`. Mais cedo ou mais tarde a sequência chega a 1.

Por exemplo, partindo de 16 a sequência é `16 -> 8 -> 4 -> 2 -> 1`, então leva 4 passos.

Ninguém jamais provou que isso sempre acontece, mas vale para todos os números já testados.

# --instructions--

Escreva uma função `collatzSteps` que recebe um número inteiro positivo `n` e retorna o número de passos necessários para chegar a 1.

`collatzSteps(1)` é 0, porque 1 já é o fim da sequência. `collatzSteps(12)` é 9, e `collatzSteps(27)` é 111.

Exemplo de chamada da função:
```dart
print(collatzSteps(16));
// imprime 4
```

# --seed--

```dart
int collatzSteps(int n) {

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

`collatzSteps(1)` deve retornar 0, porque 1 já é o fim da sequência.

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)` deve retornar 1.

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)` deve retornar 8.

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)` deve retornar 16.

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)` deve retornar 4.

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)` deve retornar 9.

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)` deve retornar 111.

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)` deve retornar 118.

```dart
    test('test8', () {
      expect(collatzSteps(97), 118, reason: '--err-t8--');
    });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int collatzSteps(int n) {
  int value = n;
  int steps = 0;
  while (value != 1) {
    value = value % 2 == 0 ? value ~/ 2 : 3 * value + 1;
    steps++;
  }
  return steps;
}
```
