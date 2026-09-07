---
language: dart
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

Die Primfaktoren von 13195 sind 5, 7, 13 und 29.

# --instructions--

Schreibe eine Funktion, die den größten Primfaktor von `number` zurückgibt.

Beispiel eines Funktionsaufrufs:
```dart
print(largestPrimeFactor(13195));
// prints 29
```

# --seed--

```dart
int largestPrimeFactor(int number) {

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

Der größte Primfaktor von 2 muss 2 ergeben

```dart
  test('test1', () {
    expect(largestPrimeFactor(2), 2, reason: '--err-t1--');
  });
```

Der größte Primfaktor von 3 muss 3 ergeben

```dart
  test('test2', () {
    expect(largestPrimeFactor(3), 3, reason: '--err-t2--');
  });
```

Der größte Primfaktor von 13195 muss 29 ergeben

```dart
  test('test3', () {
    expect(largestPrimeFactor(13195), 29, reason: '--err-t3--');
  });
```

Der größte Primfaktor von 600851475143 muss 6857 ergeben

```dart
  test('test4', () {
    expect(largestPrimeFactor(600851475143), 6857, reason: '--err-t4--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int largestPrimeFactor(int number) {
  int largest = 1;
  int n = number;
  int factor = 2;
  while (factor * factor <= n) {
    while (n % factor == 0) {
      largest = factor;
      n ~/= factor;
    }
    factor++;
  }
  if (n > 1) {
    largest = n;
  }
  return largest;
}
```
