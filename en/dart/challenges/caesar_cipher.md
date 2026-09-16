---
language: dart
exerciseType: 1
difficulty: 2
title: Caesar cipher
---

# --description--

Julius Caesar protected his private letters with one of the oldest tricks in cryptography: he replaced every letter of a message with the letter a fixed number of places further along the alphabet. With a shift of 3, `a` becomes `d`, `b` becomes `e` and `c` becomes `f`.

The alphabet behaves like a circle, so the letters at the end wrap back to the start: with a shift of 3, `x` becomes `a`, `y` becomes `b` and `z` becomes `c`.

Anything that is not a letter, such as a space, a comma, an exclamation mark or a digit, travels through the cipher untouched.

# --instructions--

Write a function `caesarCipher` that takes a message `text` and a whole number `shift`, and returns the encoded message.

Examples:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- The message is always lowercase, so you never have to deal with uppercase letters.
- Characters that are not letters keep their place and their value.
- The shift is never negative. A shift of `0` leaves the message unchanged, and so does a shift of `26`.

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

A shift of 3 turns "hello" into "khoor"

```dart
  test('test1', () {
    expect(caesarCipher('hello', 3), 'khoor', reason: '--err-t1--');
  });
```

The end of the alphabet wraps around, so "xyz" becomes "abc"

```dart
  test('test2', () {
    expect(caesarCipher('xyz', 3), 'abc', reason: '--err-t2--');
  });
```

A shift of 0 leaves the message unchanged

```dart
  test('test3', () {
    expect(caesarCipher('abc', 0), 'abc', reason: '--err-t3--');
  });
```

A shift of 26 is a full turn of the alphabet, so the message is unchanged

```dart
  test('test4', () {
    expect(caesarCipher('abc', 26), 'abc', reason: '--err-t4--');
  });
```

Punctuation and spaces pass through unchanged

```dart
  test('test5', () {
    expect(caesarCipher('codigo, rocks!', 5), 'htinlt, wthpx!', reason: '--err-t5--');
  });
```

An empty message stays empty

```dart
  test('test6', () {
    expect(caesarCipher('', 4), '', reason: '--err-t6--');
  });
```

Spaces between single letters are preserved

```dart
  test('test7', () {
    expect(caesarCipher('a b c', 1), 'b c d', reason: '--err-t7--');
  });
```

Digits are not shifted, even with a shift of 25

```dart
  test('test8', () {
    expect(caesarCipher('abc 123!', 25), 'zab 123!', reason: '--err-t8--');
  });
```

A shift of 13 encodes a whole sentence

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
