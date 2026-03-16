---
language: dart
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 ist die kleinste Zahl, die durch jede der Zahlen von 1 bis 10 ohne Rest teilbar ist.

# --instructions--

Schreibe eine Funktion, die die kleinste positive Zahl zurückgibt, die durch alle Zahlen von 1 bis `n` gleichmäßig teilbar ist.

Beispiel eines Funktionsaufrufs:
```dart
print(smallestMultiple(10));
// prints 2520
```

# --seed--

```dart
int smallestMultiple(int n) {

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

Das kleinste gemeinsame Vielfache von 1 bis 5 muss 60 ergeben

```dart
  test('test1', () {
    expect(smallestMultiple(5), 60, reason: '--err-t1--');
  });
```

Das kleinste gemeinsame Vielfache von 1 bis 10 muss 2520 ergeben

```dart
  test('test2', () {
    expect(smallestMultiple(10), 2520, reason: '--err-t2--');
  });
```

Das kleinste gemeinsame Vielfache von 1 bis 20 muss 232792560 ergeben

```dart
  test('test3', () {
    expect(smallestMultiple(20), 232792560, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int _gcd(int a, int b) => b == 0 ? a : _gcd(b, a % b);

int _lcm(int a, int b) => a ~/ _gcd(a, b) * b;

int smallestMultiple(int n) {
  int result = 1;
  for (int i = 2; i <= n; i++) {
    result = _lcm(result, i);
  }
  return result;
}
```
