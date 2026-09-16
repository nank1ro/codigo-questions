---
language: dart
exerciseType: 1
difficulty: 2
title: 变位词
---

# --description--

如果一个单词是另一个单词的重新排列，那么这两个单词就互为变位词：它们使用的字母完全相同，每个字母出现的次数也相同，只是顺序不同。`listen` 和 `silent` 是变位词，`stone` 和 `tones` 也是变位词。

一个单词永远不会是它自身的变位词。如果两个单词完全相同，就没有任何东西被重新排列，所以答案是 `false`。两个单词都以小写形式给出，并且只包含从 `a` 到 `z` 的字母。

# --instructions--

编写一个函数 `isAnagram`，它接收两个单词 `first` 和 `second`，当它们互为变位词时返回 `true`，否则返回 `false`。

示例：
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- 两个完全相同的单词不是变位词。
- 长度不同的单词永远不会是变位词。
- 每个字母在两个单词中出现的次数必须相同。

# --seed--

```dart
bool isAnagram(String first, String second) {
  
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

单词 "listen" 和 "silent" 互为变位词

```dart
  test('test1', () {
    expect(isAnagram('listen', 'silent'), true, reason: '--err-t1--');
  });
```

单词 "stone" 和 "tones" 互为变位词

```dart
  test('test2', () {
    expect(isAnagram('stone', 'tones'), true, reason: '--err-t2--');
  });
```

一个单词不是它自身的变位词

```dart
  test('test3', () {
    expect(isAnagram('stone', 'stone'), false, reason: '--err-t3--');
  });
```

长度不同的单词不是变位词

```dart
  test('test4', () {
    expect(isAnagram('abc', 'abcd'), false, reason: '--err-t4--');
  });
```

字母相同但出现次数不同则不是变位词

```dart
  test('test5', () {
    expect(isAnagram('aab', 'abb'), false, reason: '--err-t5--');
  });
```

单词 "anagram" 和 "nagaram" 互为变位词

```dart
  test('test6', () {
    expect(isAnagram('anagram', 'nagaram'), true, reason: '--err-t6--');
  });
```

长度相同但字母不同的两个单词不是变位词

```dart
  test('test7', () {
    expect(isAnagram('rat', 'car'), false, reason: '--err-t7--');
  });
```

两个空单词是完全相同的，所以它们不是变位词

```dart
  test('test8', () {
    expect(isAnagram('', ''), false, reason: '--err-t8--');
  });
```

两个不同的单个字母不是变位词

```dart
  test('test9', () {
    expect(isAnagram('a', 'b'), false, reason: '--err-t9--');
  });
```

单词 "evil" 和 "vile" 互为变位词

```dart
  test('test10', () {
    expect(isAnagram('evil', 'vile'), true, reason: '--err-t10--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isAnagram(String first, String second) {
  if (first == second) {
    return false;
  }

  final firstLetters = first.split('')..sort();
  final secondLetters = second.split('')..sort();

  return firstLetters.join() == secondLetters.join();
}
```
