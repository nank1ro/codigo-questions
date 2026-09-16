---
language: dart
exerciseType: 1
difficulty: 2
title: 애너그램
---

# --description--

한 단어가 다른 단어의 재배열일 때 두 단어는 애너그램입니다. 즉, 정확히 같은 문자를 사용하며 각 문자가 같은 횟수로 나타나고 오직 순서만 다릅니다. `listen`과 `silent`는 애너그램이고, `stone`과 `tones`도 애너그램입니다.

단어는 결코 자기 자신의 애너그램이 아닙니다. 두 단어가 완전히 같으면 재배열된 것이 없으므로 답은 `false`입니다. 두 단어는 모두 소문자로 주어지며 `a`부터 `z`까지의 문자만을 담고 있습니다.

# --instructions--

두 단어 `first`와 `second`를 받아 두 단어가 서로의 애너그램이면 `true`를, 그렇지 않으면 `false`를 반환하는 함수 `isAnagram`를 작성하세요.

예시:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- 두 단어가 완전히 같으면 애너그램이 아닙니다.
- 길이가 다른 단어는 결코 애너그램이 아닙니다.
- 모든 문자는 두 단어에서 같은 횟수로 나타나야 합니다.

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

단어 "listen"과 "silent"는 애너그램입니다

```dart
  test('test1', () {
    expect(isAnagram('listen', 'silent'), true, reason: '--err-t1--');
  });
```

단어 "stone"과 "tones"는 애너그램입니다

```dart
  test('test2', () {
    expect(isAnagram('stone', 'tones'), true, reason: '--err-t2--');
  });
```

단어는 자기 자신의 애너그램이 아닙니다

```dart
  test('test3', () {
    expect(isAnagram('stone', 'stone'), false, reason: '--err-t3--');
  });
```

길이가 다른 단어는 애너그램이 아닙니다

```dart
  test('test4', () {
    expect(isAnagram('abc', 'abcd'), false, reason: '--err-t4--');
  });
```

같은 문자라도 개수가 다르면 애너그램이 아닙니다

```dart
  test('test5', () {
    expect(isAnagram('aab', 'abb'), false, reason: '--err-t5--');
  });
```

단어 "anagram"과 "nagaram"는 애너그램입니다

```dart
  test('test6', () {
    expect(isAnagram('anagram', 'nagaram'), true, reason: '--err-t6--');
  });
```

길이가 같고 문자가 다른 두 단어는 애너그램이 아닙니다

```dart
  test('test7', () {
    expect(isAnagram('rat', 'car'), false, reason: '--err-t7--');
  });
```

두 빈 단어는 동일하므로 애너그램이 아닙니다

```dart
  test('test8', () {
    expect(isAnagram('', ''), false, reason: '--err-t8--');
  });
```

서로 다른 한 문자 두 개는 애너그램이 아닙니다

```dart
  test('test9', () {
    expect(isAnagram('a', 'b'), false, reason: '--err-t9--');
  });
```

단어 "evil"과 "vile"는 애너그램입니다

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
