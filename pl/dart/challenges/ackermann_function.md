---
language: dart
exerciseType: 1
difficulty: 1
title: Ackermann function
---

# --description--

Funkcja Ackermanna jest klasycznym przykładem funkcji rekurencyjnej, godnym uwagi zwłaszcza dlatego, że nie jest funkcją pierwotnie rekurencyjną. Jej wartości rosną bardzo szybko, podobnie jak rozmiar drzewa wywołań.

Funkcja Ackermanna jest zazwyczaj definiowana następująco:

![ackermann_function](https://bit.ly/3z9u4zh)

Jej argumenty nigdy nie są ujemne i zawsze się kończy

# --instructions--

Napisz funkcję, która zwraca wartość funkcji Ackermanna.

# --seed--

```dart
int ack(int m, int n) {
    
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

`ack(0, 0)` powinno zwrócić 1.

```dart
    test('test1', () {
      expect(ack(0, 0), 1, reason: '--err-t1--');
    });
```

`ack(1, 1)` powinno zwrócić 3.

```dart
    test('test2', () {
      expect(ack(1, 1), 3, reason: '--err-t2--');
    });
```

`ack(2, 5)` powinno zwrócić 13.

```dart
    test('test3', () {
      expect(ack(2, 5), 13, reason: '--err-t3--');
    });
```

`ack(3, 3)` powinno zwrócić 61.

```dart
    test('test4', () {
      expect(ack(3, 3), 61, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int ack(int m, int n) {
  if (m == 0) return n + 1;
  return ack(
    m - 1,
    (n == 0) ? 1 : ack(m, n - 1),
  );
}
```
