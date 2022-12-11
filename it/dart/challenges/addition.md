---
language: dart
exerciseType: 1
difficulty: 1
title: Addizione
---

# --description--

Dati due number interi `num1` e `num2`, scrivi un programma per sommare questi due numeri

# --instructions--

Scrivi una funzione che restituisca la somma tra i due numeri

Esempio di chiamata della funzione:
```dart
print(addition(1, 2));
// stampa 3
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

La somma di 1 e 3 deve essere uguale a 4

```dart
  test('test1', () {
    expect(addition(1, 3), 4, reason: '--err-t1--');
  });
```

La somma di 200 e 210 deve essere uguale a 410

```dart
  test('test2', () {
    expect(addition(200, 210), 410, reason: '--err-t2--');
  });
```

La somma di 15 e 35 deve essere uguale a 50

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
