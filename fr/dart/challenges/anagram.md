---
language: dart
exerciseType: 1
difficulty: 2
title: Anagramme
---

# --description--

Deux mots sont des anagrammes lorsque l'un est un réarrangement de l'autre : ils utilisent exactement les mêmes lettres, chacune le même nombre de fois, simplement dans un ordre différent. `listen` et `silent` sont des anagrammes, et il en va de même pour `stone` et `tones`.

Un mot n'est jamais un anagramme de lui-même. Si les deux mots sont exactement identiques, rien n'a été réarrangé, donc la réponse est `false`. Les deux mots sont donnés en minuscules et ne contiennent que les lettres de `a` à `z`.

# --instructions--

Écrivez une fonction `isAnagram` qui prend deux mots, `first` et `second`, et retourne `true` s'ils sont des anagrammes l'un de l'autre et `false` sinon.

Exemples :
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Deux mots identiques ne sont pas des anagrammes.
- Des mots de longueurs différentes ne sont jamais des anagrammes.
- Chaque lettre doit apparaître le même nombre de fois dans les deux mots.

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

Les mots "listen" et "silent" sont des anagrammes

```dart
  test('test1', () {
    expect(isAnagram('listen', 'silent'), true, reason: '--err-t1--');
  });
```

Les mots "stone" et "tones" sont des anagrammes

```dart
  test('test2', () {
    expect(isAnagram('stone', 'tones'), true, reason: '--err-t2--');
  });
```

Un mot n'est pas un anagramme de lui-même

```dart
  test('test3', () {
    expect(isAnagram('stone', 'stone'), false, reason: '--err-t3--');
  });
```

Des mots de longueurs différentes ne sont pas des anagrammes

```dart
  test('test4', () {
    expect(isAnagram('abc', 'abcd'), false, reason: '--err-t4--');
  });
```

Les mêmes lettres en quantités différentes ne forment pas un anagramme

```dart
  test('test5', () {
    expect(isAnagram('aab', 'abb'), false, reason: '--err-t5--');
  });
```

Les mots "anagram" et "nagaram" sont des anagrammes

```dart
  test('test6', () {
    expect(isAnagram('anagram', 'nagaram'), true, reason: '--err-t6--');
  });
```

Deux mots de même longueur avec des lettres différentes ne sont pas des anagrammes

```dart
  test('test7', () {
    expect(isAnagram('rat', 'car'), false, reason: '--err-t7--');
  });
```

Deux mots vides sont identiques, ils ne sont donc pas des anagrammes

```dart
  test('test8', () {
    expect(isAnagram('', ''), false, reason: '--err-t8--');
  });
```

Deux lettres différentes ne sont pas des anagrammes

```dart
  test('test9', () {
    expect(isAnagram('a', 'b'), false, reason: '--err-t9--');
  });
```

Les mots "evil" et "vile" sont des anagrammes

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
