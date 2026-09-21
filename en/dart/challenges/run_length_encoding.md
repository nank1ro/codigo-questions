---
language: dart
exerciseType: 1
difficulty: 2
title: Run-length encoding
---

# --description--

Run-length encoding is one of the oldest compression tricks there is: instead of writing the same character over and over, you write how many times it repeats and then the character itself.

A fax machine scanning a mostly blank page meets long stretches of identical pixels, so a row of twelve `W` travels down the line as the much shorter `12W`. When a character shows up only once there is nothing to gain from counting it, so it is copied across on its own.

# --instructions--

Write a function `encodeRun` that takes a string `text` and returns its run-length encoded form.

Every run of the same character repeated two or more times becomes the length of the run written in decimal, followed by that character. A run of length one is copied as the single character, with no number in front of it.

Examples:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- The text contains only uppercase letters from `A` to `Z` and spaces.
- A run longer than nine characters uses its full decimal count, so twelve `W` become `12W` and never `9W3W`.
- Spaces are ordinary characters: they are counted and encoded exactly like letters.
- The empty string encodes to the empty string.

# --seed--

```dart
String encodeRun(String text) {
  
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

The empty string encodes to the empty string

```dart
  test('test1', () {
    expect(encodeRun(''), '', reason: '--err-t1--');
  });
```

A single character is copied as itself

```dart
  test('test2', () {
    expect(encodeRun('A'), 'A', reason: '--err-t2--');
  });
```

A string with no repeats travels through unchanged

```dart
  test('test3', () {
    expect(encodeRun('ABCDE'), 'ABCDE', reason: '--err-t3--');
  });
```

A run of two becomes the count followed by the character

```dart
  test('test4', () {
    expect(encodeRun('AA'), '2A', reason: '--err-t4--');
  });
```

The mixed example "AABCCCDEEEE" becomes "2AB3CD4E"

```dart
  test('test5', () {
    expect(encodeRun('AABCCCDEEEE'), '2AB3CD4E', reason: '--err-t5--');
  });
```

A run of twelve uses its full decimal count, so the result starts with "12W"

```dart
  test('test6', () {
    expect(encodeRun('WWWWWWWWWWWWBWW'), '12WB2W', reason: '--err-t6--');
  });
```

Runs of spaces are encoded just like runs of letters

```dart
  test('test7', () {
    expect(encodeRun('  HI  '), '2 HI2 ', reason: '--err-t7--');
  });
```

A run of ten is written as "10A", never as two shorter runs

```dart
  test('test8', () {
    expect(encodeRun('AAAAAAAAAA'), '10A', reason: '--err-t8--');
  });
```

Single characters that alternate are all copied as themselves

```dart
  test('test9', () {
    expect(encodeRun('ABABAB'), 'ABABAB', reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String encodeRun(String text) {
  final result = StringBuffer();
  var i = 0;

  while (i < text.length) {
    var run = 1;
    while (i + run < text.length && text[i + run] == text[i]) {
      run++;
    }
    if (run > 1) {
      result.write(run);
    }
    result.write(text[i]);
    i += run;
  }

  return result.toString();
}
```
