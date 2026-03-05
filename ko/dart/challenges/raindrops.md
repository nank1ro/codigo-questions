---
language: dart
exerciseType: 1
difficulty: 1
title: 빗방울
---

# --description--

주어진 숫자를 특정 인수에 해당하는 빗방울 소리를 포함하는 문자열로 변환하는 것이 과제입니다.
인수란 나머지 없이 다른 숫자를 균등하게 나누는 숫자입니다.
숫자가 다른 숫자의 인수인지 테스트하는 가장 간단한 방법은 나머지 연산을 사용하는 것입니다.
빗방울의 규칙은 주어진 숫자가:

- 3을 인수로 가지면 결과에 'Pling'을 추가합니다.
- 5를 인수로 가지면 결과에 'Plang'을 추가합니다.
- 7을 인수로 가지면 결과에 'Plong'을 추가합니다.
- 3, 5, 7 중 어느 것도 인수로 가지지 않으면 결과는 숫자의 자릿수여야 합니다.

# --instructions--

올바른 문자열을 반환하는 함수를 작성하십시오. 예시:

- 28은 7을 인수로 가지지만 3이나 5는 아니므로 결과는 `"Plong"`입니다.
- 30은 3과 5를 인수로 가지지만 7은 아니므로 결과는 `"PlingPlang"`입니다.
- 34는 3, 5, 7의 인수가 아니므로 결과는 `"34"`입니다.

함수 호출 예시:
```dart
print(raindrops(28))
// prints "Plong"
```

# --seed--

```dart
String raindrops() {

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

1의 소리는 "1"입니다

```dart
  test('test1', () {
    expect(raindrops(1), "1", reason: '--err-t1--');
  });
```

3의 소리는 "Pling"입니다

```dart
  test('test2', () {
    expect(raindrops(3), "Pling", reason: '--err-t2--');
  });
```

5의 소리는 "Plang"입니다

```dart
  test('test3', () {
    expect(raindrops(5), "Plang", reason: '--err-t3--');
  });
```

7의 소리는 "Plong"입니다

```dart
  test('test4', () {
    expect(raindrops(7), "Plong", reason: '--err-t4--');
  });
```

6의 소리는 "Pling"입니다

```dart
  test('test5', () {
    expect(raindrops(6), "Pling", reason: '--err-t5--');
  });
```

8의 소리는 "8"입니다

```dart
  test('test6', () {
    expect(raindrops(8), "8", reason: '--err-t6--');
  });
```

9의 소리는 "Pling"입니다

```dart
  test('test7', () {
    expect(raindrops(9), "Pling", reason: '--err-t7--');
  });
```

10의 소리는 "Plang"입니다

```dart
  test('test8', () {
    expect(raindrops(10), "Plang", reason: '--err-t8--');
  });
```

14의 소리는 "Plong"입니다

```dart
  test('test9', () {
    expect(raindrops(14), "Plong", reason: '--err-t9--');
  });
```

15의 소리는 "PlingPlang"입니다

```dart
  test('test10', () {
    expect(raindrops(15), "PlingPlang", reason: '--err-t10--');
  });
```

21의 소리는 "PlingPlong"입니다

```dart
  test('test11', () {
    expect(raindrops(21), "PlingPlong", reason: '--err-t11--');
  });
```

25의 소리는 "Plang"입니다

```dart
  test('test12', () {
    expect(raindrops(25), "Plang", reason: '--err-t12--');
  });
```

27의 소리는 "Pling"입니다

```dart
  test('test13', () {
    expect(raindrops(27), "Pling", reason: '--err-t13--');
  });
```

35의 소리는 "PlangPlong"입니다

```dart
  test('test14', () {
    expect(raindrops(35), "PlangPlong", reason: '--err-t14--');
  });
```

49의 소리는 "Plong"입니다

```dart
  test('test15', () {
    expect(raindrops(49), "Plong", reason: '--err-t15--');
  });
```

52의 소리는 "52"입니다

```dart
  test('test16', () {
    expect(raindrops(52), "52", reason: '--err-t16--');
  });
```

105의 소리는 "PlingPlangPlong"입니다

```dart
  test('test17', () {
    expect(raindrops(105), "PlingPlangPlong", reason: '--err-t17--');
  });
```

3125의 소리는 "Plang"입니다

```dart
  test('test18', () {
    expect(raindrops(3125), "Plang", reason: '--err-t18--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String raindrops(int number) {
  var result = "";
  if (number % 3 == 0) {
    result += "Pling";
  }
  if (number % 5 == 0) {
    result += "Plang";
  }
  if (number % 7 == 0) {
    result += "Plong";
  }
  if (result.isEmpty) {
    result = number.toString();
  }
  return result;
}
```
