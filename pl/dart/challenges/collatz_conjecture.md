---
language: dart
exerciseType: 1
difficulty: 1
title: Hipoteza Collatza
---

# --description--

Hipoteza Collatza zaczyna się od dowolnej dodatniej liczby całkowitej `n` i powtarza jedną prostą regułę: jeśli `n` jest parzyste, dzielimy je na pół; jeśli `n` jest nieparzyste, zastępujemy je wartością `3n + 1`. Prędzej czy później ciąg osiąga 1.

Na przykład ciąg zaczynający się od 16 to `16 -> 8 -> 4 -> 2 -> 1`, więc zajmuje to 4 kroki.

Nikt nigdy nie udowodnił, że zawsze tak się dzieje, ale reguła ta obowiązuje dla każdej dotychczas przetestowanej liczby.

# --instructions--

Napisz funkcję `collatzSteps`, która przyjmuje dodatnią liczbę całkowitą `n` i zwraca liczbę kroków potrzebnych do osiągnięcia 1.

`collatzSteps(1)` to 0, ponieważ 1 to już koniec ciągu. `collatzSteps(12)` to 9, a `collatzSteps(27)` to 111.

Przykład wywołania funkcji:
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

`collatzSteps(1)` powinno zwrócić 0, ponieważ 1 to już koniec ciągu.

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)` powinno zwrócić 1.

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)` powinno zwrócić 8.

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)` powinno zwrócić 16.

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)` powinno zwrócić 4.

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)` powinno zwrócić 9.

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)` powinno zwrócić 111.

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)` powinno zwrócić 118.

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
