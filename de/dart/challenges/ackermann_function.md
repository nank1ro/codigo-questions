---
language: dart
exerciseType: 1
difficulty: 1
title: Ackermann-Funktion
---

# --description--

Die Ackermann-Funktion ist ein klassisches Beispiel für eine rekursive Funktion, bemerkenswert vor allem, weil sie keine primitive rekursive Funktion ist. Sie wächst sehr schnell an Wert, ebenso wie die Größe ihres Aufrufalbaums.

Die Ackermann-Funktion ist normalerweise wie folgt definiert:

![ackermann_function](https://bit.ly/3z9u4zh)

Ihre Argumente sind nie negativ und sie beendet sich immer

# --instructions--

Schreiben Sie eine Funktion, die den Wert der Ackermann-Funktion zurückgibt.

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

`ack(0, 0)` sollte 1 zurückgeben.

```dart
    test('test1', () {
      expect(ack(0, 0), 1, reason: '--err-t1--');
    });
```

`ack(1, 1)` sollte 3 zurückgeben.

```dart
    test('test2', () {
      expect(ack(1, 1), 3, reason: '--err-t2--');
    });
```

`ack(2, 5)` sollte 13 zurückgeben.

```dart
    test('test3', () {
      expect(ack(2, 5), 13, reason: '--err-t3--');
    });
```

`ack(3, 3)` sollte 61 zurückgeben.

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
