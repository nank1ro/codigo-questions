---
language: dart
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Chaque nouveau terme de la suite de Fibonacci est généré en additionnant les deux termes précédents. En commençant par 1 et 2, les 10 premiers termes sont : 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# --instructions--

Écris une fonction qui retourne la somme de tous les termes de Fibonacci de valeur paire ne dépassant pas `n`.

Exemple d'appel de fonction :
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

La somme des termes de Fibonacci pairs ne dépassant pas 8 doit être égale à 10

```dart
  test('test1', () {
    expect(fibonacciEvenSum(8), 10, reason: '--err-t1--');
  });
```

La somme des termes de Fibonacci pairs ne dépassant pas 10 doit être égale à 10

```dart
  test('test2', () {
    expect(fibonacciEvenSum(10), 10, reason: '--err-t2--');
  });
```

La somme des termes de Fibonacci pairs ne dépassant pas 34 doit être égale à 44

```dart
  test('test3', () {
    expect(fibonacciEvenSum(34), 44, reason: '--err-t3--');
  });
```

La somme des termes de Fibonacci pairs ne dépassant pas 1000 doit être égale à 798

```dart
  test('test4', () {
    expect(fibonacciEvenSum(1000), 798, reason: '--err-t4--');
  });
```

La somme des termes de Fibonacci pairs ne dépassant pas 4000000 doit être égale à 4613732

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
