---
language: dart
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Dane są dwie liczby całkowite `num1` i `num2`. Napisz program, który dodaje te dwie liczby.

# --instructions--

Napisz funkcję, która zwraca sumę dwóch liczb.

Przykład wywołania funkcji:
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

Suma 1 i 3 musi być równa 4

```dart
  test('test1', () {
    expect(addition(1, 3), 4, reason: '--err-t1--');
  });
```

Suma 200 i 210 musi być równa 410

```dart
  test('test2', () {
    expect(addition(200, 210), 410, reason: '--err-t2--');
  });
```

Suma 15 i 35 musi być równa 50

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
