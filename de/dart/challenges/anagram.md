---
language: dart
exerciseType: 1
difficulty: 2
title: Anagramm
---

# --description--

Zwei Wörter sind Anagramme, wenn eines eine Umordnung des anderen ist: Sie verwenden exakt dieselben Buchstaben, jeden Buchstaben gleich oft, nur in einer anderen Reihenfolge. `listen` und `silent` sind Anagramme, und ebenso `stone` und `tones`.

Ein Wort ist nie ein Anagramm von sich selbst. Wenn die beiden Wörter exakt gleich sind, wurde nichts umgeordnet, daher ist die Antwort `false`. Beide Wörter sind in Kleinbuchstaben gegeben und enthalten nur die Buchstaben von `a` bis `z`.

# --instructions--

Schreiben Sie eine Funktion `isAnagram`, die zwei Wörter, `first` und `second`, entgegennimmt und `true` zurückgibt, wenn sie Anagramme voneinander sind, und andernfalls `false`.

Beispiele:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Zwei identische Wörter sind keine Anagramme.
- Wörter unterschiedlicher Länge sind nie Anagramme.
- Jeder Buchstabe muss in beiden Wörtern gleich oft vorkommen.

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

Die Wörter "listen" und "silent" sind Anagramme

```dart
  test('test1', () {
    expect(isAnagram('listen', 'silent'), true, reason: '--err-t1--');
  });
```

Die Wörter "stone" und "tones" sind Anagramme

```dart
  test('test2', () {
    expect(isAnagram('stone', 'tones'), true, reason: '--err-t2--');
  });
```

Ein Wort ist kein Anagramm von sich selbst

```dart
  test('test3', () {
    expect(isAnagram('stone', 'stone'), false, reason: '--err-t3--');
  });
```

Wörter unterschiedlicher Länge sind keine Anagramme

```dart
  test('test4', () {
    expect(isAnagram('abc', 'abcd'), false, reason: '--err-t4--');
  });
```

Dieselben Buchstaben in unterschiedlicher Anzahl sind kein Anagramm

```dart
  test('test5', () {
    expect(isAnagram('aab', 'abb'), false, reason: '--err-t5--');
  });
```

Die Wörter "anagram" und "nagaram" sind Anagramme

```dart
  test('test6', () {
    expect(isAnagram('anagram', 'nagaram'), true, reason: '--err-t6--');
  });
```

Zwei Wörter derselben Länge mit unterschiedlichen Buchstaben sind keine Anagramme

```dart
  test('test7', () {
    expect(isAnagram('rat', 'car'), false, reason: '--err-t7--');
  });
```

Zwei leere Wörter sind identisch, daher sind sie keine Anagramme

```dart
  test('test8', () {
    expect(isAnagram('', ''), false, reason: '--err-t8--');
  });
```

Zwei unterschiedliche einzelne Buchstaben sind keine Anagramme

```dart
  test('test9', () {
    expect(isAnagram('a', 'b'), false, reason: '--err-t9--');
  });
```

Die Wörter "evil" und "vile" sind Anagramme

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
