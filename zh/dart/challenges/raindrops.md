---
language: dart
exerciseType: 1
difficulty: 1
title: 雨滴
---

# --description--

你的任务是将一个数字转换为包含与某些潜在因数对应的雨滴声的字符串。
因数是能整除另一个数字且没有余数的数字。
测试一个数字是否是另一个数字的因数，最简单的方法是使用取模运算。
雨滴的规则是，如果给定的数字：

- 有因数 3，则在结果中添加 'Pling'。
- 有因数 5，则在结果中添加 'Plang'。
- 有因数 7，则在结果中添加 'Plong'。
- 没有 3、5 或 7 作为因数，则结果应为该数字本身。

# --instructions--

编写一个返回正确字符串的函数，示例：

- 28 有因数 7，但没有 3 或 5，所以结果是 `"Plong"`。
- 30 同时有因数 3 和 5，但没有 7，所以结果是 `"PlingPlang"`。
- 34 没有因数 3、5 或 7，所以结果是 `"34"`。

函数调用示例：
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

1 的声音是 "1"

```dart
  test('test1', () {
    expect(raindrops(1), "1", reason: '--err-t1--');
  });
```

3 的声音是 "Pling"

```dart
  test('test2', () {
    expect(raindrops(3), "Pling", reason: '--err-t2--');
  });
```

5 的声音是 "Plang"

```dart
  test('test3', () {
    expect(raindrops(5), "Plang", reason: '--err-t3--');
  });
```

7 的声音是 "Plong"

```dart
  test('test4', () {
    expect(raindrops(7), "Plong", reason: '--err-t4--');
  });
```

6 的声音是 "Pling"

```dart
  test('test5', () {
    expect(raindrops(6), "Pling", reason: '--err-t5--');
  });
```

8 的声音是 "8"

```dart
  test('test6', () {
    expect(raindrops(8), "8", reason: '--err-t6--');
  });
```

9 的声音是 "Pling"

```dart
  test('test7', () {
    expect(raindrops(9), "Pling", reason: '--err-t7--');
  });
```

10 的声音是 "Plang"

```dart
  test('test8', () {
    expect(raindrops(10), "Plang", reason: '--err-t8--');
  });
```

14 的声音是 "Plong"

```dart
  test('test9', () {
    expect(raindrops(14), "Plong", reason: '--err-t9--');
  });
```

15 的声音是 "PlingPlang"

```dart
  test('test10', () {
    expect(raindrops(15), "PlingPlang", reason: '--err-t10--');
  });
```

21 的声音是 "PlingPlong"

```dart
  test('test11', () {
    expect(raindrops(21), "PlingPlong", reason: '--err-t11--');
  });
```

25 的声音是 "Plang"

```dart
  test('test12', () {
    expect(raindrops(25), "Plang", reason: '--err-t12--');
  });
```

27 的声音是 "Pling"

```dart
  test('test13', () {
    expect(raindrops(27), "Pling", reason: '--err-t13--');
  });
```

35 的声音是 "PlangPlong"

```dart
  test('test14', () {
    expect(raindrops(35), "PlangPlong", reason: '--err-t14--');
  });
```

49 的声音是 "Plong"

```dart
  test('test15', () {
    expect(raindrops(49), "Plong", reason: '--err-t15--');
  });
```

52 的声音是 "52"

```dart
  test('test16', () {
    expect(raindrops(52), "52", reason: '--err-t16--');
  });
```

105 的声音是 "PlingPlangPlong"

```dart
  test('test17', () {
    expect(raindrops(105), "PlingPlangPlong", reason: '--err-t17--');
  });
```

3125 的声音是 "Plang"

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
