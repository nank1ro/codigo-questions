---
language: dart
exerciseType: 1
difficulty: 2
title: Codage par plages
---

# --description--

Le codage par plages est l'une des plus vieilles astuces de compression qui existent : au lieu d'écrire le même caractère encore et encore, on écrit combien de fois il se répète, puis le caractère lui-même.

Un télécopieur qui scanne une page quasiment vide rencontre de longues plages de pixels identiques : une rangée de douze `W` parcourt ainsi la ligne sous la forme bien plus courte `12W`. Quand un caractère n'apparaît qu'une seule fois, le compter n'apporte rien, si bien qu'il est copié tel quel.

# --instructions--

Écrivez une fonction `encodeRun` qui prend une chaîne `text` et retourne sa forme encodée par plages.

Chaque plage du même caractère répété au moins deux fois devient la longueur de cette plage écrite en décimal, suivie de ce caractère. Une plage de longueur un est copiée comme le seul caractère, sans nombre devant lui.

Exemples :
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- Le texte ne contient que des lettres majuscules de `A` à `Z` et des espaces.
- Une plage de plus de neuf caractères utilise son comptage décimal complet : douze `W` deviennent donc `12W` et jamais `9W3W`.
- Les espaces sont des caractères ordinaires : elles sont comptées et encodées exactement comme les lettres.
- La chaîne vide s'encode en chaîne vide.

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

La chaîne vide s'encode en chaîne vide

```dart
  test('test1', () {
    expect(encodeRun(''), '', reason: '--err-t1--');
  });
```

Un caractère seul est copié tel quel

```dart
  test('test2', () {
    expect(encodeRun('A'), 'A', reason: '--err-t2--');
  });
```

Une chaîne sans répétitions passe inchangée

```dart
  test('test3', () {
    expect(encodeRun('ABCDE'), 'ABCDE', reason: '--err-t3--');
  });
```

Une plage de deux devient le comptage suivi du caractère

```dart
  test('test4', () {
    expect(encodeRun('AA'), '2A', reason: '--err-t4--');
  });
```

L'exemple mixte "AABCCCDEEEE" devient "2AB3CD4E"

```dart
  test('test5', () {
    expect(encodeRun('AABCCCDEEEE'), '2AB3CD4E', reason: '--err-t5--');
  });
```

Une plage de douze utilise son comptage décimal complet, donc le résultat commence par "12W"

```dart
  test('test6', () {
    expect(encodeRun('WWWWWWWWWWWWBWW'), '12WB2W', reason: '--err-t6--');
  });
```

Les plages d'espaces sont encodées exactement comme les plages de lettres

```dart
  test('test7', () {
    expect(encodeRun('  HI  '), '2 HI2 ', reason: '--err-t7--');
  });
```

Une plage de dix s'écrit "10A", jamais comme deux plages plus courtes

```dart
  test('test8', () {
    expect(encodeRun('AAAAAAAAAA'), '10A', reason: '--err-t8--');
  });
```

Les caractères isolés qui alternent sont tous copiés tels quels

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
