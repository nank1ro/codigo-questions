---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

처음 10개의 자연수의 제곱의 합은 1² + 2² + ... + 10² = 385입니다.

처음 10개의 자연수의 합의 제곱은 (1 + 2 + ... + 10)² = 55² = 3025입니다.

1부터 10까지에서 합의 제곱과 제곱의 합의 차는 3025 − 385 = 2640입니다.

# --instructions--

처음 `n`개의 자연수의 합의 제곱과 제곱의 합의 차를 반환하는 함수를 작성하세요.

함수 호출 예시:
```dart
print(sumSquareDifference(10));
// prints 2640
```

# --seed--

```dart
int sumSquareDifference(int n) {

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

n=10일 때 합의 제곱과 제곱의 합의 차는 2640과 같아야 한다

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

n=20일 때 합의 제곱과 제곱의 합의 차는 41230과 같아야 한다

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

n=100일 때 합의 제곱과 제곱의 합의 차는 25164150과 같아야 한다

```dart
  test('test3', () {
    expect(sumSquareDifference(100), 25164150, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumSquareDifference(int n) {
  int sumOfSquares = 0;
  int sum = 0;
  for (int i = 1; i <= n; i++) {
    sumOfSquares += i * i;
    sum += i;
  }
  return sum * sum - sumOfSquares;
}
```
