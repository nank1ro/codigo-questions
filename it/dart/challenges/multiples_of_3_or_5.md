---
language: dart
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Se elenchiamo tutti i numeri naturali minori di 10 che sono multipli di 3 o 5, otteniamo 3, 5, 6 e 9. La somma di questi multipli è 23.

# --instructions--

Scrivi una funzione che restituisca la somma di tutti i multipli di 3 o 5 inferiori a `number`.

Esempio di chiamata alla funzione:
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

La somma dei multipli di 3 o 5 inferiori a 10 deve essere uguale a 23

```dart
  test('test1', () {
    expect(multiplesOf3And5(10), 23, reason: '--err-t1--');
  });
```

La somma dei multipli di 3 o 5 inferiori a 1000 deve essere uguale a 233168

```dart
  test('test2', () {
    expect(multiplesOf3And5(1000), 233168, reason: '--err-t2--');
  });
```

La somma dei multipli di 3 o 5 inferiori a 6987 deve essere uguale a 11390208

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
