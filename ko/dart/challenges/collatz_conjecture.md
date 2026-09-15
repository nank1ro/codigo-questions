---
language: dart
exerciseType: 1
difficulty: 1
title: 콜라츠 추측
---

# --description--

콜라츠 추측은 임의의 양의 정수 `n`에서 시작하여 간단한 규칙 하나를 반복합니다: `n`이 짝수이면 절반으로 줄이고, `n`이 홀수이면 `3n + 1`로 바꿉니다. 조만간 수열은 1에 도달합니다.

예를 들어, 16에서 시작하면 수열은 `16 -> 8 -> 4 -> 2 -> 1`이 되므로 4단계가 걸립니다.

아무도 이 일이 항상 일어난다는 것을 증명하지 못했지만, 지금까지 테스트된 모든 수에서 성립합니다.

# --instructions--

양의 정수 `n`을 받아 1에 도달하는 데 필요한 단계 수를 반환하는 함수 `collatzSteps`를 작성하세요.

`collatzSteps(1)`은 1이 이미 수열의 끝이므로 0입니다. `collatzSteps(12)`는 9이고, `collatzSteps(27)`는 111입니다.

함수 호출 예시:
```dart
print(collatzSteps(16));
// 출력: 4
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

`collatzSteps(1)`은 1이 이미 수열의 끝이므로 0을 반환해야 합니다.

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)`은 1을 반환해야 합니다.

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)`은 8을 반환해야 합니다.

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)`은 16을 반환해야 합니다.

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)`은 4를 반환해야 합니다.

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)`은 9를 반환해야 합니다.

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)`은 111을 반환해야 합니다.

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)`은 118을 반환해야 합니다.

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
