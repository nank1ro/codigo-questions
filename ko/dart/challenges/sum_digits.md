---
language: dart
exerciseType: 1
difficulty: 1
title: 자릿수의 합
---

# --description--

정수 `N`이 주어집니다.
N의 모든 자릿수의 합을 계산하는 프로그램을 작성하십시오.

# --instructions--

`N`의 자릿수의 합을 반환하십시오.

함수 호출 예시:
```dart
print(sumDigits(28))
// prints 10
```

# --seed--

```dart
int sumDigits() {

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

12345의 자릿수의 합은 15입니다

```dart
  test('test1', () {
    expect(sumDigits(12345), 15, reason: '--err-t1--');
  });
```

57253의 자릿수의 합은 22입니다

```dart
  test('test2', () {
    expect(sumDigits(57253), 22, reason: '--err-t2--');
  });
```

122의 자릿수의 합은 5입니다

```dart
  test('test3', () {
    expect(sumDigits(122), 5, reason: '--err-t3--');
  });
```

91979997의 자릿수의 합은 60입니다

```dart
  test('test4', () {
    expect(sumDigits(91979997), 60, reason: '--err-t4--');
  });
```

2147483647의 자릿수의 합은 46입니다

```dart
  test('test5', () {
    expect(sumDigits(2147483647), 46, reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumDigits(int number) {
  var n = number;
  var result = 0;
  while (n > 0) {
    result += n % 10;
    n = n ~/ 10;
  }
  return result;
}
```

