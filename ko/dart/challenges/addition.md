---
language: dart
exerciseType: 1
difficulty: 1
title: 덧셈
---

# --description--

두 정수 `num1`과 `num2`가 주어졌을 때, 이 두 수를 더하는 프로그램을 작성하십시오.

# --instructions--

두 수의 합을 반환하는 함수를 작성하십시오.

함수 호출 예시:
```dart
print(addition(1, 2));
// prints 3
```

# --seed--

```dart
int addition() {
  
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

1과 3의 합은 4여야 합니다

```dart
  test('test1', () {
    expect(addition(1, 3), 4, reason: '--err-t1--');
  });
```

200과 210의 합은 410이어야 합니다

```dart
  test('test2', () {
    expect(addition(200, 210), 410, reason: '--err-t2--');
  });
```

15와 35의 합은 50이어야 합니다

```dart
  test('test3', () {
    expect(addition(15, 35), 50, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int addition(int num1, int num2) {
  return num1 + num2;
}
```
