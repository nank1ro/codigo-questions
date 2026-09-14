---
language: dart
exerciseType: 1
difficulty: 1
title: Congettura di Collatz
---

# --description--

La congettura di Collatz parte da un qualsiasi intero positivo `n` e ripete una semplice regola: se `n` è pari, si dimezza; se `n` è dispari, si sostituisce con `3n + 1`. Prima o poi la sequenza arriva a 1.

Per esempio, partendo da 16 la sequenza è `16 -> 8 -> 4 -> 2 -> 1`, quindi servono 4 passi.

Nessuno ha mai dimostrato che questo accada sempre, ma vale per ogni numero mai testato.

# --instructions--

Scrivi una funzione `collatzSteps` che riceve un intero positivo `n` e restituisce il numero di passi necessari per arrivare a 1.

`collatzSteps(1)` è 0, perché 1 è già la fine della sequenza. `collatzSteps(12)` è 9, e `collatzSteps(27)` è 111.

Esempio di chiamata alla funzione:
```dart
print(collatzSteps(16));
// prints 4
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

`collatzSteps(1)` deve restituire 0, perché 1 è già la fine della sequenza.

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)` deve restituire 1.

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)` deve restituire 8.

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)` deve restituire 16.

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)` deve restituire 4.

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)` deve restituire 9.

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)` deve restituire 111.

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)` deve restituire 118.

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
