---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

Suma kwadratów pierwszych dziesięciu liczb naturalnych wynosi 1² + 2² + ... + 10² = 385.

Kwadrat sumy pierwszych dziesięciu liczb naturalnych wynosi (1 + 2 + ... + 10)² = 55² = 3025.

Różnica między kwadratem sumy a sumą kwadratów dla liczb od 1 do 10 wynosi 3025 − 385 = 2640.

# --instructions--

Napisz funkcję, która zwraca różnicę między kwadratem sumy a sumą kwadratów pierwszych `n` liczb naturalnych.

Przykład wywołania funkcji:
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

Różnica kwadratów sum dla n=10 musi być równa 2640

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

Różnica kwadratów sum dla n=20 musi być równa 41230

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

Różnica kwadratów sum dla n=100 musi być równa 25164150

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
