---
language: dart
exerciseType: 1
difficulty: 2
title: Анаграмма
---

# --description--

Два слова являются анаграммами, когда одно из них является перестановкой другого: они используют ровно одни и те же буквы, и каждая буква встречается одно и то же число раз, просто в другом порядке. `listen` и `silent` — анаграммы, как и `stone` и `tones`.

Слово никогда не является анаграммой самого себя. Если два слова полностью совпадают, ничего не переставлялось, поэтому ответ — `false`. Оба слова заданы в нижнем регистре и содержат только буквы от `a` до `z`.

# --instructions--

Напишите функцию `isAnagram`, которая принимает два слова, `first` и `second`, и возвращает `true`, если они являются анаграммами друг друга, и `false` в противном случае.

Примеры:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Два одинаковых слова не являются анаграммами.
- Слова разной длины никогда не являются анаграммами.
- Каждая буква должна встречаться в обоих словах одинаковое число раз.

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

Слова "listen" и "silent" являются анаграммами

```dart
  test('test1', () {
    expect(isAnagram('listen', 'silent'), true, reason: '--err-t1--');
  });
```

Слова "stone" и "tones" являются анаграммами

```dart
  test('test2', () {
    expect(isAnagram('stone', 'tones'), true, reason: '--err-t2--');
  });
```

Слово не является анаграммой самого себя

```dart
  test('test3', () {
    expect(isAnagram('stone', 'stone'), false, reason: '--err-t3--');
  });
```

Слова разной длины не являются анаграммами

```dart
  test('test4', () {
    expect(isAnagram('abc', 'abcd'), false, reason: '--err-t4--');
  });
```

Одни и те же буквы в разном количестве не являются анаграммой

```dart
  test('test5', () {
    expect(isAnagram('aab', 'abb'), false, reason: '--err-t5--');
  });
```

Слова "anagram" и "nagaram" являются анаграммами

```dart
  test('test6', () {
    expect(isAnagram('anagram', 'nagaram'), true, reason: '--err-t6--');
  });
```

Два слова одинаковой длины с разными буквами не являются анаграммами

```dart
  test('test7', () {
    expect(isAnagram('rat', 'car'), false, reason: '--err-t7--');
  });
```

Два пустых слова идентичны, поэтому они не являются анаграммами

```dart
  test('test8', () {
    expect(isAnagram('', ''), false, reason: '--err-t8--');
  });
```

Две разные одиночные буквы не являются анаграммами

```dart
  test('test9', () {
    expect(isAnagram('a', 'b'), false, reason: '--err-t9--');
  });
```

Слова "evil" и "vile" являются анаграммами

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
