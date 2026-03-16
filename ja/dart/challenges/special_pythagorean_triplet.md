---
language: dart
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

ピタゴラス数とは、a < b < c を満たし、a² + b² = c² となる 3 つの自然数の組です。

例えば、3² + 4² = 9 + 16 = 25 = 5² です。a + b + c = 1000 となるピタゴラス数の組はちょうど 1 つ存在します。

# --instructions--

a + b + c の値が `n` に等しいピタゴラス数の組を見つけ、積 a × b × c を返す関数を書いてください。

関数呼び出しの例:
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

a+b+c=12 のピタゴラス数の積は 60 と等しくなければならない

```dart
  test('test1', () {
    expect(specialPythagoreanTriplet(12), 60, reason: '--err-t1--');
  });
```

a+b+c=1000 のピタゴラス数の積は 31875000 と等しくなければならない

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
