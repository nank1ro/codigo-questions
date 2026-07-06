---
language: dart
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Una terna pitagorica è un insieme di tre numeri naturali a < b < c per cui vale a² + b² = c².

Ad esempio, 3² + 4² = 9 + 16 = 25 = 5². Esiste esattamente una terna pitagorica per cui a + b + c = 1000.

# --instructions--

Scrivi una funzione che trovi la terna pitagorica in cui a + b + c è uguale a `n`, e restituisca il prodotto a × b × c.

Esempio di chiamata alla funzione:
```dart
print(specialPythagoreanTriplet(12));
// prints 60
```

# --seed--

```dart
int specialPythagoreanTriplet(int n) {

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

Il prodotto della terna pitagorica in cui a+b+c=12 deve essere uguale a 60

```dart
  test('test1', () {
    expect(specialPythagoreanTriplet(12), 60, reason: '--err-t1--');
  });
```

Il prodotto della terna pitagorica in cui a+b+c=1000 deve essere uguale a 31875000

```dart
  test('test2', () {
    expect(specialPythagoreanTriplet(1000), 31875000, reason: '--err-t2--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int specialPythagoreanTriplet(int n) {
  for (int a = 1; a < n; a++) {
    for (int b = a + 1; b < n - a; b++) {
      int c = n - a - b;
      if (c > b && a * a + b * b == c * c) {
        return a * b * c;
      }
    }
  }
  return -1;
}
```
