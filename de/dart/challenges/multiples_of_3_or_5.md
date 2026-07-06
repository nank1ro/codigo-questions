---
language: dart
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Wenn wir alle natürlichen Zahlen unter 10 auflisten, die Vielfache von 3 oder 5 sind, erhalten wir 3, 5, 6 und 9. Die Summe dieser Vielfachen beträgt 23.

# --instructions--

Schreibe eine Funktion, die die Summe aller Vielfachen von 3 oder 5 unterhalb von `number` zurückgibt.

Beispiel eines Funktionsaufrufs:
```dart
print(multiplesOf3And5(10));
// prints 23
```

# --seed--

```dart
int multiplesOf3And5(int number) {

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

Die Summe der Vielfachen von 3 oder 5 unterhalb von 10 muss 23 ergeben

```dart
  test('test1', () {
    expect(multiplesOf3And5(10), 23, reason: '--err-t1--');
  });
```

Die Summe der Vielfachen von 3 oder 5 unterhalb von 1000 muss 233168 ergeben

```dart
  test('test2', () {
    expect(multiplesOf3And5(1000), 233168, reason: '--err-t2--');
  });
```

Die Summe der Vielfachen von 3 oder 5 unterhalb von 6987 muss 11390208 ergeben

```dart
  test('test3', () {
    expect(multiplesOf3And5(6987), 11390208, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int multiplesOf3And5(int number) {
  int sum = 0;
  for (int i = 1; i < number; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      sum += i;
    }
  }
  return sum;
}
```
