---
language: dart
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Gegeben sind zwei ganze Zahlen `num1` und `num2`, schreiben Sie ein Programm, um diese beiden Zahlen zu addieren

# --instructions--

Schreiben Sie eine Funktion, die die Summe von zwei Zahlen zurückgibt.

Example of function call:
```dart
print(addition(1, 2));
// prints 3
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

Die Summe von 1 und 3 muss gleich 4 sein

```dart
  test('test1', () {
    expect(addition(1, 3), 4, reason: '--err-t1--');
  });
```

Die Summe von 200 und 210 muss gleich 410 sein

```dart
  test('test2', () {
    expect(addition(200, 210), 410, reason: '--err-t2--');
  });
```

Die Summe von 15 und 35 muss gleich 50 sein

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
