---
language: dart
exerciseType: 1
difficulty: 1
title: 아커만 함수
---

# --description--

아커만 함수는 재귀 함수의 대표적인 예시로, 특히 원시 재귀 함수가 아니라는 점에서 주목할 만합니다. 이 함수의 값은 매우 빠르게 증가하며, 호출 트리의 크기도 마찬가지입니다.

아커만 함수는 일반적으로 다음과 같이 정의됩니다:

![ackermann_function](https://bit.ly/3z9u4zh)

인수는 절대 음수가 아니며 항상 종료됩니다.

# --instructions--

아커만 함수의 값을 반환하는 함수를 작성하십시오.

# --seed--

```dart
int ack(int m, int n) {
    
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

`ack(0, 0)`은 1을 반환해야 합니다.

```dart
    test('test1', () {
      expect(ack(0, 0), 1, reason: '--err-t1--');
    });
```

`ack(1, 1)`은 3을 반환해야 합니다.

```dart
    test('test2', () {
      expect(ack(1, 1), 3, reason: '--err-t2--');
    });
```

`ack(2, 5)`는 13을 반환해야 합니다.

```dart
    test('test3', () {
      expect(ack(2, 5), 13, reason: '--err-t3--');
    });
```

`ack(3, 3)`은 61을 반환해야 합니다.

```dart
    test('test4', () {
      expect(ack(3, 3), 61, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int ack(int m, int n) {
  if (m == 0) return n + 1;
  return ack(
    m - 1,
    (n == 0) ? 1 : ack(m, n - 1),
  );
}
```
