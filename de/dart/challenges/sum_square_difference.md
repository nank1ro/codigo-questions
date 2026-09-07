---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

Die Summe der Quadrate der ersten zehn natürlichen Zahlen beträgt 1² + 2² + ... + 10² = 385.

Das Quadrat der Summe der ersten zehn natürlichen Zahlen beträgt (1 + 2 + ... + 10)² = 55² = 3025.

Die Differenz zwischen dem Quadrat der Summe und der Summe der Quadrate für 1 bis 10 beträgt 3025 − 385 = 2640.

# --instructions--

Schreibe eine Funktion, die die Differenz zwischen dem Quadrat der Summe und der Summe der Quadrate der ersten `n` natürlichen Zahlen zurückgibt.

Beispiel eines Funktionsaufrufs:
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

Die Quadratsummendifferenz für n=10 muss 2640 ergeben

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

Die Quadratsummendifferenz für n=20 muss 41230 ergeben

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

Die Quadratsummendifferenz für n=100 muss 25164150 ergeben

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
