---
language: dart
exerciseType: 1
difficulty: 1
title: Ackermann function
---

# --description--

Die Ackermann-Funktion ist ein klassisches Beispiel fur eine rekursive Funktion, besonders bemerkenswert, weil sie keine primitive rekursive Funktion ist. Sie wachst sehr schnell in ihrem Wert, ebenso wie die Groe ihres Aufrufbaums.

Die Ackermann-Funktion wird ublichwie folgt definiert:

![ackermann_function](https://bit.ly/3z9u4zh)

Ihre Argumente sind niemals negativ und sie terminiert immer

# --instructions--

Schreiben Sie eine Funktion, die den Wert der Ackermann-Funktion zuruckgibt.

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

`ack(0, 0)` sollte 1 zuruckgeben.

```dart
    test('test1', () {
      expect(ack(0, 0), 1, reason: '--err-t1--');
    });
```

`ack(1, 1)` sollte 3 zuruckgeben.

```dart
    test('test2', () {
      expect(ack(1, 1), 3, reason: '--err-t2--');
    });
```

`ack(2, 5)` sollte 13 zuruckgeben.

```dart
    test('test3', () {
      expect(ack(2, 5), 13, reason: '--err-t3--');
    });
```

`ack(3, 3)` sollte 61 zuruckgeben.

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
