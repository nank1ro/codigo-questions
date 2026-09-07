---
language: dart
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Ogni nuovo termine della successione di Fibonacci viene generato sommando i due termini precedenti. Partendo da 1 e 2, i primi 10 termini sono: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# --instructions--

Scrivi una funzione che restituisca la somma di tutti i termini di Fibonacci di valore pari che non superano `n`.

Esempio di chiamata alla funzione:
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

La somma dei termini di Fibonacci pari che non superano 8 deve essere uguale a 10

```dart
  test('test1', () {
    expect(fibonacciEvenSum(8), 10, reason: '--err-t1--');
  });
```

La somma dei termini di Fibonacci pari che non superano 10 deve essere uguale a 10

```dart
  test('test2', () {
    expect(fibonacciEvenSum(10), 10, reason: '--err-t2--');
  });
```

La somma dei termini di Fibonacci pari che non superano 34 deve essere uguale a 44

```dart
  test('test3', () {
    expect(fibonacciEvenSum(34), 44, reason: '--err-t3--');
  });
```

La somma dei termini di Fibonacci pari che non superano 1000 deve essere uguale a 798

```dart
  test('test4', () {
    expect(fibonacciEvenSum(1000), 798, reason: '--err-t4--');
  });
```

La somma dei termini di Fibonacci pari che non superano 4000000 deve essere uguale a 4613732

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
