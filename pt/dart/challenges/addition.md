---
language: dart
exerciseType: 1
difficulty: 1
title: "Adição"
---

# --description--

Dados dois inteiros `num1` e `num2`, escreva um programa para somar esses dois números

# --instructions--

Escreva uma função que retorne a soma de dois números.

Exemplo de chamada da função:
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

A soma de 1 e 3 deve ser igual a 4

```dart
  test('test1', () {
    expect(addition(1, 3), 4, reason: '--err-t1--');
  });
```

A soma de 200 e 210 deve ser igual a 410

```dart
  test('test2', () {
    expect(addition(200, 210), 410, reason: '--err-t2--');
  });
```

A soma de 15 e 35 deve ser igual a 50

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
