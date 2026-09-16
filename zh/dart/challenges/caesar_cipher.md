---
language: dart
exerciseType: 1
difficulty: 2
title: 凯撒密码
---

# --description--

尤利乌斯·凯撒用密码学中最古老的技巧之一来保护他的私人信件：他将消息中的每个字母替换为字母表中向前移动固定个位置的字母。当移位为 3 时，`a` 变成 `d`，`b` 变成 `e`，`c` 变成 `f`。

字母表的行为就像一个圆圈，因此末尾的字母会绕回到开头：当移位为 3 时，`x` 变成 `a`，`y` 变成 `b`，`z` 变成 `c`。

任何不是字母的字符，例如空格、逗号、感叹号或数字，都会原样通过密码，不做任何改变。

# --instructions--

编写一个函数 `caesarCipher`，它接收一个消息 `text` 和一个整数 `shift`，并返回编码后的消息。

示例：
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- 消息始终为小写，因此你不需要处理大写字母。
- 不是字母的字符保持它们的位置和值不变。
- 移位永远不会为负。移位为 `0` 时消息保持不变，移位为 `26` 时也是如此。

# --seed--

```dart
String caesarCipher(String text, int shift) {
  
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

移位为 3 时，“hello” 变成 “khoor”

```dart
  test('test1', () {
    expect(caesarCipher('hello', 3), 'khoor', reason: '--err-t1--');
  });
```

字母表的末尾会绕回到开头，所以 “xyz” 变成 “abc”

```dart
  test('test2', () {
    expect(caesarCipher('xyz', 3), 'abc', reason: '--err-t2--');
  });
```

移位为 0 时消息保持不变

```dart
  test('test3', () {
    expect(caesarCipher('abc', 0), 'abc', reason: '--err-t3--');
  });
```

移位为 26 相当于绕了字母表一整圈，所以消息保持不变

```dart
  test('test4', () {
    expect(caesarCipher('abc', 26), 'abc', reason: '--err-t4--');
  });
```

标点符号和空格原样通过，不做任何改变

```dart
  test('test5', () {
    expect(caesarCipher('codigo, rocks!', 5), 'htinlt, wthpx!', reason: '--err-t5--');
  });
```

空消息保持为空

```dart
  test('test6', () {
    expect(caesarCipher('', 4), '', reason: '--err-t6--');
  });
```

单个字母之间的空格会被保留

```dart
  test('test7', () {
    expect(caesarCipher('a b c', 1), 'b c d', reason: '--err-t7--');
  });
```

即使移位为 25，数字也保持不变

```dart
  test('test8', () {
    expect(caesarCipher('abc 123!', 25), 'zab 123!', reason: '--err-t8--');
  });
```

移位为 13 时可以编码一个完整的句子

```dart
  test('test9', () {
    expect(caesarCipher('the quick brown fox jumps over the lazy dog', 13), 'gur dhvpx oebja sbk whzcf bire gur ynml qbt', reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String caesarCipher(String text, int shift) {
  final a = 'a'.codeUnitAt(0);
  final z = 'z'.codeUnitAt(0);
  final encoded = <int>[];

  for (final code in text.codeUnits) {
    if (code >= a && code <= z) {
      encoded.add(a + (code - a + shift) % 26);
    } else {
      encoded.add(code);
    }
  }

  return String.fromCharCodes(encoded);
}
```
