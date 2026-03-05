---
language: dart
exerciseType: 1
difficulty: 1
title: Função de Ackermann
---

# --description--

A função de Ackermann é um exemplo clássico de uma função recursiva, notável especialmente por não ser uma função recursiva primitiva. Ela cresce muito rapidamente em valor, assim como o tamanho de sua árvore de chamadas.

A função de Ackermann é geralmente definida da seguinte forma:

![ackermann_function](https://bit.ly/3z9u4zh)

Seus argumentos nunca são negativos e ela sempre termina

# --instructions--

Escreva uma função que retorne o valor da função de Ackermann.

# --seed--

```dart
int ack(int m, int n) {
    
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

`ack(0, 0)` deve retornar 1.

```dart
    test('test1', () {
      expect(ack(0, 0), 1, reason: '--err-t1--');
    });
```

`ack(1, 1)` deve retornar 3.

```dart
    test('test2', () {
      expect(ack(1, 1), 3, reason: '--err-t2--');
    });
```

`ack(2, 5)` deve retornar 13.

```dart
    test('test3', () {
      expect(ack(2, 5), 13, reason: '--err-t3--');
    });
```

`ack(3, 3)` deve retornar 61.

```dart
    test('test4', () {
      expect(ack(3, 3), 61, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int ack(int m, int n) {
  if (m == 0) return n + 1;
  return ack(
    m - 1,
    (n == 0) ? 1 : ack(m, n - 1),
  );
}
```
