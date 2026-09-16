---
language: dart
exerciseType: 1
difficulty: 2
title: Anagram
---

# --description--

Dwa słowa są anagramami, gdy jedno jest przestawieniem drugiego: używają dokładnie tych samych liter, a każda z nich występuje tę samą liczbę razy, tylko w innej kolejności. `listen` i `silent` są anagramami, podobnie jak `stone` i `tones`.

Słowo nigdy nie jest anagramem samego siebie. Jeśli oba słowa są dokładnie takie same, nic nie zostało przestawione, więc odpowiedź to `false`. Oba słowa są podane małymi literami i zawierają wyłącznie litery od `a` do `z`.

# --instructions--

Napisz funkcję `isAnagram`, która przyjmuje dwa słowa, `first` i `second`, i zwraca `true`, gdy jedno z nich jest anagramem drugiego, oraz `false` w przeciwnym razie.

Przykłady:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Dwa identyczne słowa nie są anagramami.
- Słowa o różnych długościach nigdy nie są anagramami.
- Każda litera musi występować tyle samo razy w obu słowach.

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

Słowa "listen" i "silent" są anagramami

```dart
  test('test1', () {
    expect(isAnagram('listen', 'silent'), true, reason: '--err-t1--');
  });
```

Słowa "stone" i "tones" są anagramami

```dart
  test('test2', () {
    expect(isAnagram('stone', 'tones'), true, reason: '--err-t2--');
  });
```

Słowo nie jest anagramem samego siebie

```dart
  test('test3', () {
    expect(isAnagram('stone', 'stone'), false, reason: '--err-t3--');
  });
```

Słowa o różnych długościach nie są anagramami

```dart
  test('test4', () {
    expect(isAnagram('abc', 'abcd'), false, reason: '--err-t4--');
  });
```

Te same litery w różnych ilościach nie tworzą anagramu

```dart
  test('test5', () {
    expect(isAnagram('aab', 'abb'), false, reason: '--err-t5--');
  });
```

Słowa "anagram" i "nagaram" są anagramami

```dart
  test('test6', () {
    expect(isAnagram('anagram', 'nagaram'), true, reason: '--err-t6--');
  });
```

Dwa słowa tej samej długości z różnymi literami nie są anagramami

```dart
  test('test7', () {
    expect(isAnagram('rat', 'car'), false, reason: '--err-t7--');
  });
```

Dwa puste słowa są identyczne, więc nie są anagramami

```dart
  test('test8', () {
    expect(isAnagram('', ''), false, reason: '--err-t8--');
  });
```

Dwie różne pojedyncze litery nie są anagramami

```dart
  test('test9', () {
    expect(isAnagram('a', 'b'), false, reason: '--err-t9--');
  });
```

Słowa "evil" i "vile" są anagramami

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
