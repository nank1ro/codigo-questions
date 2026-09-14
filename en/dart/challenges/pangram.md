---
language: dart
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

A pangram is a sentence that uses every letter of the English alphabet at least once. The best known example is "the quick brown fox jumps over the lazy dog", which fits all 26 letters into nine short words.

The check is case-insensitive, so `A` and `a` count as the same letter. Digits, punctuation and spaces are ignored: they are not letters, but they are not a reason to reject a sentence either.

# --instructions--

Write a function `isPangram` that takes a sentence and returns `true` if the sentence is a pangram and `false` otherwise.

Examples:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- An empty sentence is not a pangram.
- Only the 26 letters from `a` to `z` count.

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

An empty sentence is not a pangram

```dart
  test('test1', () {
    expect(isPangram(''), false, reason: '--err-t1--');
  });
```

The classic sentence "the quick brown fox jumps over the lazy dog" is a pangram

```dart
  test('test2', () {
    expect(isPangram('the quick brown fox jumps over the lazy dog'), true, reason: '--err-t2--');
  });
```

A sentence missing the letter `x` is not a pangram

```dart
  test('test3', () {
    expect(isPangram('a quick movement of the enemy will jeopardize five gunboats'), false, reason: '--err-t3--');
  });
```

The sentence "the five boxing wizards jump quickly" is a pangram

```dart
  test('test4', () {
    expect(isPangram('the five boxing wizards jump quickly'), true, reason: '--err-t4--');
  });
```

Underscores are ignored, so the sentence is still a pangram

```dart
  test('test5', () {
    expect(isPangram('the_quick_brown_fox_jumps_over_the_lazy_dog'), true, reason: '--err-t5--');
  });
```

Digits are ignored, so the sentence is still a pangram

```dart
  test('test6', () {
    expect(isPangram('the 1 quick brown fox jumps over the 2 lazy dogs'), true, reason: '--err-t6--');
  });
```

Digits do not replace the letters `e`, `i` and `t`

```dart
  test('test7', () {
    expect(isPangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'), false, reason: '--err-t7--');
  });
```

An uppercase sentence is a pangram too

```dart
  test('test8', () {
    expect(isPangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), true, reason: '--err-t8--');
  });
```

Mixing the cases of the same half of the alphabet is not enough

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
