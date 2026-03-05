---
language: dart
exerciseType: 1
difficulty: 1
title: Média aritmética
---

# --description--

Escreva uma função chamada `mean` para encontrar a _média aritmética_ de um vetor numérico.

# --instructions--

Escreva uma função que retorne a média de um vetor numérico.

Exemplo de chamada da função:
```dart
print(mean([1, 2, 3]));
// prints 2.0
```

# --seed--

```dart
num mean() {
  
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

A média de `[1, 2, 3, 4, 5, 6, 7]` deve ser igual a 4.0

```dart
  test('test1', () {
    expect(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, reason: '--err-t1--');
  });
```

A média de `[4, 5, 6]` deve ser igual a 5.0

```dart
  test('test2', () {
    expect(mean([4, 5, 6]), 5.0, reason: '--err-t2--');
  });
```

A média de `[12, 34, 56, 78]` deve ser igual a 45.0

```dart
  test('test3', () {
    expect(mean([12, 34, 56, 78]), 45.0, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
num mean(List<num> numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
