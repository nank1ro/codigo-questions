---
language: dart
exerciseType: 1
difficulty: 2
title: Luhn 校验和
---

# --description--

Luhn 算法是一种简单的校验和，用于验证身份识别号码，例如信用卡号。

在检查一个号码之前，先去掉字符串中的所有空格。只有当剩下的部分长度超过一个字符，并且原始字符串只包含数字和空格时，该字符串才是有效的。

执行检查时，从最右边的数字开始向左移动，将每隔一位的数字加倍。当加倍后得到大于 9 的数时，将其减去 9。然后把所有数字相加：只有当总和能被 10 整除时，该号码才有效。

例如，`"059"` 得到 `0`，然后 `5` 加倍为 `10`，它变成 `1`，再是 `9`。它们的和是 `10`，能被 10 整除，所以这个号码是有效的。

# --instructions--

编写一个函数 `isValid`，它接收一个字符串，当号码有效时返回 `true`，否则返回 `false`。

- `"4539 3195 0343 6467"` 通过校验和，所以结果是 `true`。
- `"8273 1232 7352 0569"` 未通过校验和，所以结果是 `false`。
- `"0"` 只有一个字符长，所以结果是 `false`。
- `"055-444-285"` 包含既不是数字也不是空格的字符，所以结果是 `false`。

函数调用示例：
```dart
print(isValid("095 245 88"));
// prints true
```

# --seed--

```dart
bool isValid(String value) {
  
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

单个数字是无效的。

```dart
  test('test1', () {
    expect(isValid("0"), false, reason: '--err-t1--');
  });
```

前面带一个空格的单个数字是无效的。

```dart
  test('test2', () {
    expect(isValid(" 0"), false, reason: '--err-t2--');
  });
```

号码 `"059"` 是有效的。

```dart
  test('test3', () {
    expect(isValid("059"), true, reason: '--err-t3--');
  });
```

号码 `"59"` 是有效的。

```dart
  test('test4', () {
    expect(isValid("59"), true, reason: '--err-t4--');
  });
```

号码 `"055 444 285"` 是有效的。

```dart
  test('test5', () {
    expect(isValid("055 444 285"), true, reason: '--err-t5--');
  });
```

号码 `"055 444 286"` 是无效的。

```dart
  test('test6', () {
    expect(isValid("055 444 286"), false, reason: '--err-t6--');
  });
```

号码 `"8273 1232 7352 0569"` 是无效的。

```dart
  test('test7', () {
    expect(isValid("8273 1232 7352 0569"), false, reason: '--err-t7--');
  });
```

号码 `"4539 3195 0343 6467"` 是有效的。

```dart
  test('test8', () {
    expect(isValid("4539 3195 0343 6467"), true, reason: '--err-t8--');
  });
```

号码 `"1 2345 6789 1234 5678 9012"` 是无效的。

```dart
  test('test9', () {
    expect(isValid("1 2345 6789 1234 5678 9012"), false, reason: '--err-t9--');
  });
```

号码 `"095 245 88"` 是有效的。

```dart
  test('test10', () {
    expect(isValid("095 245 88"), true, reason: '--err-t10--');
  });
```

字母会使号码无效。

```dart
  test('test11', () {
    expect(isValid("055a 444 285"), false, reason: '--err-t11--');
  });
```

短横线会使号码无效。

```dart
  test('test12', () {
    expect(isValid("055-444-285"), false, reason: '--err-t12--');
  });
```

标点符号字符会使号码无效。

```dart
  test('test13', () {
    expect(isValid(":9"), false, reason: '--err-t13--');
  });
```

符号会使号码无效。

```dart
  test('test14', () {
    expect(isValid("055# 444\$ 285"), false, reason: '--err-t14--');
  });
```

空字符串是无效的。

```dart
  test('test15', () {
    expect(isValid(""), false, reason: '--err-t15--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isValid(String value) {
  var sum = 0;
  var count = 0;
  for (var i = value.length - 1; i >= 0; i--) {
    final code = value.codeUnitAt(i);
    if (code == 32) {
      continue;
    }
    if (code < 48 || code > 57) {
      return false;
    }
    var digit = code - 48;
    if (count % 2 == 1) {
      digit *= 2;
      if (digit > 9) {
        digit -= 9;
      }
    }
    sum += digit;
    count++;
  }
  return count > 1 && sum % 10 == 0;
}
```
