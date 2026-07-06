---
language: dart
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Cada novo termo da sequência de Fibonacci é gerado somando os dois termos anteriores. Começando com 1 e 2, os primeiros 10 termos são: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# --instructions--

Escreva uma função que retorna a soma de todos os termos pares da sequência de Fibonacci que não excedem `n`.

Exemplo de chamada de função:
```dart
print(fibonacciEvenSum(8));
// prints 10
```

# --seed--

```dart
int fibonacciEvenSum(int n) {

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

A soma dos termos pares de Fibonacci que não excedem 8 deve ser igual a 10

```dart
  test('test1', () {
    expect(fibonacciEvenSum(8), 10, reason: '--err-t1--');
  });
```

A soma dos termos pares de Fibonacci que não excedem 10 deve ser igual a 10

```dart
  test('test2', () {
    expect(fibonacciEvenSum(10), 10, reason: '--err-t2--');
  });
```

A soma dos termos pares de Fibonacci que não excedem 34 deve ser igual a 44

```dart
  test('test3', () {
    expect(fibonacciEvenSum(34), 44, reason: '--err-t3--');
  });
```

A soma dos termos pares de Fibonacci que não excedem 1000 deve ser igual a 798

```dart
  test('test4', () {
    expect(fibonacciEvenSum(1000), 798, reason: '--err-t4--');
  });
```

A soma dos termos pares de Fibonacci que não excedem 4000000 deve ser igual a 4613732

```dart
  test('test5', () {
    expect(fibonacciEvenSum(4000000), 4613732, reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int fibonacciEvenSum(int n) {
  int sum = 0;
  int a = 1, b = 2;
  while (a <= n) {
    if (a % 2 == 0) {
      sum += a;
    }
    int temp = a + b;
    a = b;
    b = temp;
  }
  return sum;
}
```
