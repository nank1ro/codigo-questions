---
language: dart
exerciseType: 1
difficulty: 2
title: Chiffre de César
---

# --description--

Jules César protégeait ses lettres privées avec l'une des plus anciennes astuces de la cryptographie : il remplaçait chaque lettre d'un message par la lettre située un nombre fixe de positions plus loin dans l'alphabet. Avec un décalage de 3, `a` devient `d`, `b` devient `e` et `c` devient `f`.

L'alphabet se comporte comme un cercle, ainsi les lettres de la fin reviennent au début : avec un décalage de 3, `x` devient `a`, `y` devient `b` et `z` devient `c`.

Tout ce qui n'est pas une lettre, comme un espace, une virgule, un point d'exclamation ou un chiffre, traverse le chiffrement sans être modifié.

# --instructions--

Écrivez une fonction `caesarCipher` qui prend un message `text` et un nombre entier `shift`, et retourne le message encodé.

Exemples :
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Le message est toujours en minuscules, vous n'avez donc jamais à gérer de lettres majuscules.
- Les caractères qui ne sont pas des lettres conservent leur place et leur valeur.
- Le décalage n'est jamais négatif. Un décalage de `0` laisse le message inchangé, et il en va de même pour un décalage de `26`.

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

Un décalage de 3 transforme "hello" en "khoor"

```dart
  test('test1', () {
    expect(caesarCipher('hello', 3), 'khoor', reason: '--err-t1--');
  });
```

La fin de l'alphabet revient au début, ainsi "xyz" devient "abc"

```dart
  test('test2', () {
    expect(caesarCipher('xyz', 3), 'abc', reason: '--err-t2--');
  });
```

Un décalage de 0 laisse le message inchangé

```dart
  test('test3', () {
    expect(caesarCipher('abc', 0), 'abc', reason: '--err-t3--');
  });
```

Un décalage de 26 correspond à un tour complet de l'alphabet, le message est donc inchangé

```dart
  test('test4', () {
    expect(caesarCipher('abc', 26), 'abc', reason: '--err-t4--');
  });
```

La ponctuation et les espaces passent sans être modifiés

```dart
  test('test5', () {
    expect(caesarCipher('codigo, rocks!', 5), 'htinlt, wthpx!', reason: '--err-t5--');
  });
```

Un message vide reste vide

```dart
  test('test6', () {
    expect(caesarCipher('', 4), '', reason: '--err-t6--');
  });
```

Les espaces entre les lettres isolées sont conservés

```dart
  test('test7', () {
    expect(caesarCipher('a b c', 1), 'b c d', reason: '--err-t7--');
  });
```

Les chiffres ne sont pas décalés, même avec un décalage de 25

```dart
  test('test8', () {
    expect(caesarCipher('abc 123!', 25), 'zab 123!', reason: '--err-t8--');
  });
```

Un décalage de 13 encode une phrase entière

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
