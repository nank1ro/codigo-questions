---
language: dart
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Jedes neue Glied der Fibonacci-Folge wird durch Addition der beiden vorherigen Glieder erzeugt. Beginnend mit 1 und 2 sind die ersten 10 Glieder: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# --instructions--

Schreibe eine Funktion, die die Summe aller geradzahligen Fibonacci-Glieder zurückgibt, die `n` nicht überschreiten.

Beispiel eines Funktionsaufrufs:
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

Die Summe der geraden Fibonacci-Glieder bis einschließlich 8 muss 10 ergeben

```dart
  test('test1', () {
    expect(fibonacciEvenSum(8), 10, reason: '--err-t1--');
  });
```

Die Summe der geraden Fibonacci-Glieder bis einschließlich 10 muss 10 ergeben

```dart
  test('test2', () {
    expect(fibonacciEvenSum(10), 10, reason: '--err-t2--');
  });
```

Die Summe der geraden Fibonacci-Glieder bis einschließlich 34 muss 44 ergeben

```dart
  test('test3', () {
    expect(fibonacciEvenSum(34), 44, reason: '--err-t3--');
  });
```

Die Summe der geraden Fibonacci-Glieder bis einschließlich 1000 muss 798 ergeben

```dart
  test('test4', () {
    expect(fibonacciEvenSum(1000), 798, reason: '--err-t4--');
  });
```

Die Summe der geraden Fibonacci-Glieder bis einschließlich 4000000 muss 4613732 ergeben

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
