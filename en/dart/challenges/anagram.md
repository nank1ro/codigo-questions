---
language: dart
exerciseType: 1
difficulty: 2
title: Anagram
---

# --description--

Two words are anagrams when one is a rearrangement of the other: they use exactly the same letters, each letter the same number of times, only in a different order. `listen` and `silent` are anagrams, and so are `stone` and `tones`.

A word is never an anagram of itself. If the two words are exactly the same, nothing was rearranged, so the answer is `false`. Both words are given in lowercase and contain only the letters from `a` to `z`.

# --instructions--

Write a function `isAnagram` that takes two words, `first` and `second`, and returns `true` when they are anagrams of each other and `false` otherwise.

Examples:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Two identical words are not anagrams.
- Words of different lengths are never anagrams.
- Every letter must appear the same number of times in both words.

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

The words "listen" and "silent" are anagrams

```dart
  test('test1', () {
    expect(isAnagram('listen', 'silent'), true, reason: '--err-t1--');
  });
```

The words "stone" and "tones" are anagrams

```dart
  test('test2', () {
    expect(isAnagram('stone', 'tones'), true, reason: '--err-t2--');
  });
```

A word is not an anagram of itself

```dart
  test('test3', () {
    expect(isAnagram('stone', 'stone'), false, reason: '--err-t3--');
  });
```

Words of different lengths are not anagrams

```dart
  test('test4', () {
    expect(isAnagram('abc', 'abcd'), false, reason: '--err-t4--');
  });
```

The same letters in different amounts are not an anagram

```dart
  test('test5', () {
    expect(isAnagram('aab', 'abb'), false, reason: '--err-t5--');
  });
```

The words "anagram" and "nagaram" are anagrams

```dart
  test('test6', () {
    expect(isAnagram('anagram', 'nagaram'), true, reason: '--err-t6--');
  });
```

Two words of the same length with different letters are not anagrams

```dart
  test('test7', () {
    expect(isAnagram('rat', 'car'), false, reason: '--err-t7--');
  });
```

Two empty words are identical, so they are not anagrams

```dart
  test('test8', () {
    expect(isAnagram('', ''), false, reason: '--err-t8--');
  });
```

Two different single letters are not anagrams

```dart
  test('test9', () {
    expect(isAnagram('a', 'b'), false, reason: '--err-t9--');
  });
```

The words "evil" and "vile" are anagrams

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
