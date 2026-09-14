---
language: dart
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

全字母句是指至少使用一次英文字母表中每个字母的句子。最著名的例子是 "the quick brown fox jumps over the lazy dog"，它把全部 26 个字母装进了九个短单词里。

检查不区分大小写，因此 `A` 和 `a` 算作同一个字母。数字、标点和空格会被忽略：它们不是字母，但也不构成拒绝一个句子的理由。

# --instructions--

编写一个函数 `isPangram`，它接收一个句子，如果该句子是全字母句则返回 `true`，否则返回 `false`。

示例：
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- 空句子不是全字母句。
- 只有从 `a` 到 `z` 的 26 个字母才算数。

# --seed--

```dart
bool isPangram(String sentence) {
  
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

空句子不是全字母句

```dart
  test('test1', () {
    expect(isPangram(''), false, reason: '--err-t1--');
  });
```

经典句子 "the quick brown fox jumps over the lazy dog" 是全字母句

```dart
  test('test2', () {
    expect(isPangram('the quick brown fox jumps over the lazy dog'), true, reason: '--err-t2--');
  });
```

缺少字母 `x` 的句子不是全字母句

```dart
  test('test3', () {
    expect(isPangram('a quick movement of the enemy will jeopardize five gunboats'), false, reason: '--err-t3--');
  });
```

句子 "the five boxing wizards jump quickly" 是全字母句

```dart
  test('test4', () {
    expect(isPangram('the five boxing wizards jump quickly'), true, reason: '--err-t4--');
  });
```

下划线会被忽略，所以这个句子仍然是全字母句

```dart
  test('test5', () {
    expect(isPangram('the_quick_brown_fox_jumps_over_the_lazy_dog'), true, reason: '--err-t5--');
  });
```

数字会被忽略，所以这个句子仍然是全字母句

```dart
  test('test6', () {
    expect(isPangram('the 1 quick brown fox jumps over the 2 lazy dogs'), true, reason: '--err-t6--');
  });
```

数字不能代替字母 `e`、`i` 和 `t`

```dart
  test('test7', () {
    expect(isPangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'), false, reason: '--err-t7--');
  });
```

全大写的句子也是全字母句

```dart
  test('test8', () {
    expect(isPangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), true, reason: '--err-t8--');
  });
```

混合字母表同一半部分的大小写还不够

```dart
  test('test9', () {
    expect(isPangram('abcdefghijklm ABCDEFGHIJKLM'), false, reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isPangram(String sentence) {
  final letters = <String>{};

  for (final char in sentence.toLowerCase().split('')) {
    if (char.compareTo('a') >= 0 && char.compareTo('z') <= 0) {
      letters.add(char);
    }
  }

  return letters.length == 26;
}
```
