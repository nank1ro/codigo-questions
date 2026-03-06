---
language: dart
exerciseType: 1
difficulty: 1
title: 산술 평균
---

# --description--

숫자 벡터의 _산술 평균_을 구하는 `mean`이라는 함수를 작성하십시오.

# --instructions--

숫자 벡터의 평균을 반환하는 함수를 작성하십시오.

함수 호출 예시:
```dart
print(mean([1, 2, 3]));
// prints 2.0
```

# --seed--

```dart
num mean() {
  
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

`[1, 2, 3, 4, 5, 6, 7]`의 평균은 4.0이어야 합니다

```dart
  test('test1', () {
    expect(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, reason: '--err-t1--');
  });
```

`[4, 5, 6]`의 평균은 5.0이어야 합니다

```dart
  test('test2', () {
    expect(mean([4, 5, 6]), 5.0, reason: '--err-t2--');
  });
```

`[12, 34, 56, 78]`의 평균은 45.0이어야 합니다

```dart
  test('test3', () {
    expect(mean([12, 34, 56, 78]), 45.0, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
num mean(List<num> numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
