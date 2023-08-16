---
language: dart
exerciseType: 1
difficulty: 1
title: Media aritmetica
---

# --description--

Scrivi una funzione chiamata `mean` per trovare la _media aritmetica_ di un vettore numerico.

# --instructions--

Scrivi una funzione che restituisca la media di un vettore numerico.

Esempio di chiamata di funzione:

```dart
print(mean([1, 2, 3]));
// stampa 2.0
```

# --seed--

```dart
num mean() {
  
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

La media di `[1, 2, 3, 4, 5, 6, 7]` deve essere uguale a 4.0

```dart
  test('test1', () {
    expect(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, reason: '--err-t1--');
  });
```

La media di `[4, 5, 6]` deve essere uguale a 5.0

```dart
  test('test2', () {
    expect(mean([4, 5, 6]), 5.0, reason: '--err-t2--');
  });
```

La media di `[12, 34, 56, 78]` deve essere uguale a 45.0

```dart
  test('test3', () {
    expect(mean([12, 34, 56, 78]), 45.0, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
num mean(List<num> numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
