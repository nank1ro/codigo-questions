---
language: dart
exerciseType: 1
difficulty: 1
title: Pangramme
---

# --description--

Un pangramme est une phrase qui utilise au moins une fois chaque lettre de l'alphabet anglais. L'exemple le plus connu est "the quick brown fox jumps over the lazy dog", qui fait tenir les 26 lettres dans neuf mots courts.

La vérification ne tient pas compte de la casse, donc `A` et `a` comptent comme la même lettre. Les chiffres, la ponctuation et les espaces sont ignorés : ce ne sont pas des lettres, mais ils ne sont pas non plus une raison de rejeter une phrase.

# --instructions--

Écrivez une fonction `isPangram` qui prend une phrase et retourne `true` si la phrase est un pangramme et `false` sinon.

Exemples :
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Une phrase vide n'est pas un pangramme.
- Seules les 26 lettres de `a` à `z` comptent.

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

Une phrase vide n'est pas un pangramme

```dart
  test('test1', () {
    expect(isPangram(''), false, reason: '--err-t1--');
  });
```

La phrase classique "the quick brown fox jumps over the lazy dog" est un pangramme

```dart
  test('test2', () {
    expect(isPangram('the quick brown fox jumps over the lazy dog'), true, reason: '--err-t2--');
  });
```

Une phrase à laquelle il manque la lettre `x` n'est pas un pangramme

```dart
  test('test3', () {
    expect(isPangram('a quick movement of the enemy will jeopardize five gunboats'), false, reason: '--err-t3--');
  });
```

La phrase "the five boxing wizards jump quickly" est un pangramme

```dart
  test('test4', () {
    expect(isPangram('the five boxing wizards jump quickly'), true, reason: '--err-t4--');
  });
```

Les tirets bas sont ignorés, donc la phrase reste un pangramme

```dart
  test('test5', () {
    expect(isPangram('the_quick_brown_fox_jumps_over_the_lazy_dog'), true, reason: '--err-t5--');
  });
```

Les chiffres sont ignorés, donc la phrase reste un pangramme

```dart
  test('test6', () {
    expect(isPangram('the 1 quick brown fox jumps over the 2 lazy dogs'), true, reason: '--err-t6--');
  });
```

Les chiffres ne remplacent pas les lettres `e`, `i` et `t`

```dart
  test('test7', () {
    expect(isPangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'), false, reason: '--err-t7--');
  });
```

Une phrase en majuscules est aussi un pangramme

```dart
  test('test8', () {
    expect(isPangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), true, reason: '--err-t8--');
  });
```

Mélanger les casses de la même moitié de l'alphabet ne suffit pas

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
