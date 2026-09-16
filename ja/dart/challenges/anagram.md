---
language: dart
exerciseType: 1
difficulty: 2
title: アナグラム
---

# --description--

アナグラムとは、一方の単語を並べ替えるともう一方になるような2つの単語のことです。使っている文字がまったく同じで、どの文字も同じ回数だけ現れ、順序だけが異なります。`listen` と `silent` はアナグラムであり、`stone` と `tones` もアナグラムです。

単語がそれ自身のアナグラムになることはありません。2つの単語がまったく同じであれば、何も並べ替えられていないため、答えは `false` です。両方の単語は小文字で与えられ、`a` から `z` の文字だけを含みます。

# --instructions--

2つの単語 `first` と `second` を受け取り、互いにアナグラムであれば `true` を、そうでなければ `false` を返す関数 `isAnagram` を書いてください。

例:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- まったく同じ単語どうしはアナグラムではありません。
- 長さが異なる単語がアナグラムになることはありません。
- すべての文字は、両方の単語で同じ回数だけ現れなければなりません。

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

単語 "listen" と "silent" はアナグラムである

```dart
  test('test1', () {
    expect(isAnagram('listen', 'silent'), true, reason: '--err-t1--');
  });
```

単語 "stone" と "tones" はアナグラムである

```dart
  test('test2', () {
    expect(isAnagram('stone', 'tones'), true, reason: '--err-t2--');
  });
```

単語はそれ自身のアナグラムではない

```dart
  test('test3', () {
    expect(isAnagram('stone', 'stone'), false, reason: '--err-t3--');
  });
```

長さが異なる単語はアナグラムではない

```dart
  test('test4', () {
    expect(isAnagram('abc', 'abcd'), false, reason: '--err-t4--');
  });
```

同じ文字でも出現回数が異なればアナグラムではない

```dart
  test('test5', () {
    expect(isAnagram('aab', 'abb'), false, reason: '--err-t5--');
  });
```

単語 "anagram" と "nagaram" はアナグラムである

```dart
  test('test6', () {
    expect(isAnagram('anagram', 'nagaram'), true, reason: '--err-t6--');
  });
```

同じ長さでも文字が異なる2つの単語はアナグラムではない

```dart
  test('test7', () {
    expect(isAnagram('rat', 'car'), false, reason: '--err-t7--');
  });
```

2つの空の単語は同一であるため、アナグラムではない

```dart
  test('test8', () {
    expect(isAnagram('', ''), false, reason: '--err-t8--');
  });
```

異なる1文字どうしはアナグラムではない

```dart
  test('test9', () {
    expect(isAnagram('a', 'b'), false, reason: '--err-t9--');
  });
```

単語 "evil" と "vile" はアナグラムである

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
