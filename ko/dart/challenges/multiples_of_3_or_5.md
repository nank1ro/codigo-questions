---
language: dart
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

10 미만의 자연수 중 3 또는 5의 배수를 모두 나열하면 3, 5, 6, 9가 됩니다. 이 배수들의 합은 23입니다.

# --instructions--

`number` 미만의 3 또는 5의 모든 배수의 합을 반환하는 함수를 작성하세요.

함수 호출 예시:
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

10 미만의 3 또는 5의 배수 합은 23과 같아야 한다

```dart
  test('test1', () {
    expect(multiplesOf3And5(10), 23, reason: '--err-t1--');
  });
```

1000 미만의 3 또는 5의 배수 합은 233168과 같아야 한다

```dart
  test('test2', () {
    expect(multiplesOf3And5(1000), 233168, reason: '--err-t2--');
  });
```

6987 미만의 3 또는 5의 배수 합은 11390208과 같아야 한다

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
