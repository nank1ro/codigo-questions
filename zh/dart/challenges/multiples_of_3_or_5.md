---
language: dart
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

如果列出10以下所有3或5的倍数，可以得到3、5、6和9。这些倍数之和为23。

# --instructions--

编写一个函数，返回所有小于 `number` 的3或5的倍数之和。

函数调用示例：
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

10以下3或5的倍数之和必须等于23

```dart
  test('test1', () {
    expect(multiplesOf3And5(10), 23, reason: '--err-t1--');
  });
```

1000以下3或5的倍数之和必须等于233168

```dart
  test('test2', () {
    expect(multiplesOf3And5(1000), 233168, reason: '--err-t2--');
  });
```

6987以下3或5的倍数之和必须等于11390208

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
