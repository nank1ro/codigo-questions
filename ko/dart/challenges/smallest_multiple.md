---
language: dart
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520은 1부터 10까지의 모든 수로 나머지 없이 나눌 수 있는 가장 작은 수입니다.

# --instructions--

1부터 `n`까지의 모든 수로 균등하게 나눌 수 있는 가장 작은 양의 정수를 반환하는 함수를 작성하세요.

함수 호출 예시:
```dart
print(smallestMultiple(10));
// prints 2520
```

# --seed--

```dart
int smallestMultiple(int n) {

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

1부터 5까지의 최소공배수는 60과 같아야 한다

```dart
  test('test1', () {
    expect(smallestMultiple(5), 60, reason: '--err-t1--');
  });
```

1부터 10까지의 최소공배수는 2520과 같아야 한다

```dart
  test('test2', () {
    expect(smallestMultiple(10), 2520, reason: '--err-t2--');
  });
```

1부터 20까지의 최소공배수는 232792560과 같아야 한다

```dart
  test('test3', () {
    expect(smallestMultiple(20), 232792560, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int _gcd(int a, int b) => b == 0 ? a : _gcd(b, a % b);

int _lcm(int a, int b) => a ~/ _gcd(a, b) * b;

int smallestMultiple(int n) {
  int result = 1;
  for (int i = 2; i <= n; i++) {
    result = _lcm(result, i);
  }
  return result;
}
```
