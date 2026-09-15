---
language: dart
exerciseType: 1
difficulty: 1
title: Collatz-Vermutung
---

# --description--

Die Collatz-Vermutung startet von einer beliebigen positiven ganzen Zahl `n` und wiederholt eine einfache Regel: Ist `n` gerade, wird es halbiert; ist `n` ungerade, wird es durch `3n + 1` ersetzt. Früher oder später erreicht die Folge die 1.

Startet man zum Beispiel bei 16, lautet die Folge `16 -> 8 -> 4 -> 2 -> 1`, sie benötigt also 4 Schritte.

Niemand hat je bewiesen, dass das immer geschieht, aber es gilt für jede bisher getestete Zahl.

# --instructions--

Schreiben Sie eine Funktion `collatzSteps`, die eine positive ganze Zahl `n` nimmt und die Anzahl der Schritte zurückgibt, die benötigt werden, um 1 zu erreichen.

`collatzSteps(1)` ist 0, weil 1 bereits das Ende der Folge ist. `collatzSteps(12)` ist 9, und `collatzSteps(27)` ist 111.

Beispiel eines Funktionsaufrufs:
```dart
print(collatzSteps(16));
// gibt 4 aus
```

# --seed--

```dart
int collatzSteps(int n) {

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

`collatzSteps(1)` sollte 0 zurückgeben, weil 1 bereits das Ende der Folge ist.

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)` sollte 1 zurückgeben.

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)` sollte 8 zurückgeben.

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)` sollte 16 zurückgeben.

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)` sollte 4 zurückgeben.

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)` sollte 9 zurückgeben.

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)` sollte 111 zurückgeben.

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)` sollte 118 zurückgeben.

```dart
    test('test8', () {
      expect(collatzSteps(97), 118, reason: '--err-t8--');
    });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int collatzSteps(int n) {
  int value = n;
  int steps = 0;
  while (value != 1) {
    value = value % 2 == 0 ? value ~/ 2 : 3 * value + 1;
    steps++;
  }
  return steps;
}
```
