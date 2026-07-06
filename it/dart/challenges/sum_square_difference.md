---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

La somma dei quadrati dei primi dieci numeri naturali è 1² + 2² + ... + 10² = 385.

Il quadrato della somma dei primi dieci numeri naturali è (1 + 2 + ... + 10)² = 55² = 3025.

La differenza tra il quadrato della somma e la somma dei quadrati per i numeri da 1 a 10 è 3025 − 385 = 2640.

# --instructions--

Scrivi una funzione che restituisca la differenza tra il quadrato della somma e la somma dei quadrati dei primi `n` numeri naturali.

Esempio di chiamata alla funzione:
```dart
print(sumSquareDifference(10));
// prints 2640
```

# --seed--

```dart
int sumSquareDifference(int n) {

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

La differenza tra il quadrato della somma e la somma dei quadrati per n=10 deve essere uguale a 2640

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

La differenza tra il quadrato della somma e la somma dei quadrati per n=20 deve essere uguale a 41230

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

La differenza tra il quadrato della somma e la somma dei quadrati per n=100 deve essere uguale a 25164150

```dart
  test('test3', () {
    expect(sumSquareDifference(100), 25164150, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumSquareDifference(int n) {
  int sumOfSquares = 0;
  int sum = 0;
  for (int i = 1; i <= n; i++) {
    sumOfSquares += i * i;
    sum += i;
  }
  return sum * sum - sumOfSquares;
}
```
