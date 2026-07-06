---
language: dart
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

피타고라스 삼조수는 a < b < c를 만족하고 a² + b² = c²인 세 자연수의 집합입니다.

예를 들어, 3² + 4² = 9 + 16 = 25 = 5²입니다. a + b + c = 1000인 피타고라스 삼조수는 정확히 하나 존재합니다.

# --instructions--

a + b + c가 `n`과 같은 피타고라스 삼조수를 찾아 곱 a × b × c를 반환하는 함수를 작성하세요.

함수 호출 예시:
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

a+b+c=12인 피타고라스 삼조수의 곱은 60과 같아야 한다

```dart
  test('test1', () {
    expect(specialPythagoreanTriplet(12), 60, reason: '--err-t1--');
  });
```

a+b+c=1000인 피타고라스 삼조수의 곱은 31875000과 같아야 한다

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
