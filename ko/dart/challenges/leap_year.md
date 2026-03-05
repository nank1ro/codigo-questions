---
language: dart
exerciseType: 1
difficulty: 3
title: 윤년
---

# --description--

달력의 한 해에는 정확히 365.25일이 있습니다. 그러나 인간은 보통 소수점이 아닌 1의 정확한 나눗셈으로 세기 때문에, 결국 혼란이 생길 수 있습니다. 이를 피하기 위해, 4년 주기마다 0.25일을 모두 더하여 그 해에 366일을 부여하고 (2월 29일을 윤일로 포함) 이를 __윤년__이라고 부르기로 했습니다. 4년 주기의 나머지 3년은 365일만 포함하며 __윤년이 아닙니다__.

# --instructions--

이 챌린지에서는 `DateTime` 클래스, `switch` 문, __if 블록__, __if-else 블록__ 또는 __삼항 연산자__ (`x ? a : b`)와 논리 연산자 __AND__ (`&&`) 및 __OR__ (`||`)을 사용하지 않고 윤년인지 여부를 판별해야 합니다. __NOT__ (`!`) 연산자만 예외적으로 사용할 수 있습니다.

윤년이면 `true`를, 그렇지 않으면 `false`를 반환하십시오.

함수 호출 예시:
```dart
print(leapYear(2000));
// prints true
```

# --seed--

```dart
bool leapYear(int year) {
  
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

`DateTime`, `switch`, `if`, `else`, `&&`, `||` 또는 `?`의 사용은 허용되지 않습니다.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

`2016`년은 윤년입니다.

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

`1996`년은 윤년입니다.

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

`1600`년은 윤년입니다.

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

`2020`년은 윤년입니다.

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

`2000`년은 윤년입니다.

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

`2008`년은 윤년입니다.

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

`1521`년은 윤년이 아닙니다.

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

`1800`년은 윤년이 아닙니다.

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

`2007`년은 윤년이 아닙니다.

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

`2002`년은 윤년이 아닙니다.

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

`1979`년은 윤년이 아닙니다.

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

`2006`년은 윤년이 아닙니다.

```dart
  test('test12', () {
    expect(leapYear(2006), false, reason: '--err-t12--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool leapYear(int year) {
  return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0));
}
```

```dart
bool leapYear(int year) {
  while (year % 100 == 0) {
    year = year ~/ 100;
  }
  return year % 4 == 0;
}
```
