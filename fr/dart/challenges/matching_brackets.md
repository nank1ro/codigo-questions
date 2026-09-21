---
language: dart
exerciseType: 1
difficulty: 3
title: Crochets correspondants
---

# --description--

Le texte qui contient du code, des maths ou du balisage regorge de crochets, et chaque crochet ouvrant a besoin d'un crochet fermant de même type. Une chaîne est équilibrée lorsque ses crochets s'apparient et s'imbriquent comme les couches d'un oignon : `{[()]}` est équilibrée, alors que `{[(])}` ne l'est pas, car la paire ronde est fermée avant la paire carrée dans laquelle elle se trouve.

Trois paires comptent ici : les rondes `()`, les carrées `[]` et les accolades `{}`. Tous les autres caractères de la chaîne sont ignorés. Un crochet fermant doit fermer le crochet le plus récemment ouvert encore ouvert, et lorsque la chaîne se termine, aucun crochet ne doit rester ouvert.

# --instructions--

Écrivez une fonction `isBalanced` qui prend une chaîne et retourne `true` lorsque tous les crochets qu'elle contient sont appariés et correctement imbriqués, et `false` sinon.

Exemples :
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Une chaîne vide est équilibrée.
- Les caractères qui ne sont pas des crochets sont ignorés.
- Un crochet fermant doit correspondre au crochet le plus récemment ouvert encore ouvert.
- Aucun crochet ne doit rester ouvert lorsque la chaîne se termine.

# --seed--

```dart
bool isBalanced(String text) {
  
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

Une chaîne vide est équilibrée

```dart
  test('test1', () {
    expect(isBalanced(''), true, reason: '--err-t1--');
  });
```

Une seule paire de crochets ronds est équilibrée

```dart
  test('test2', () {
    expect(isBalanced('()'), true, reason: '--err-t2--');
  });
```

Les trois types de paires imbriquées l'une dans l'autre sont équilibrées

```dart
  test('test3', () {
    expect(isBalanced('{[()]}'), true, reason: '--err-t3--');
  });
```

Des crochets mélangés à d'autres textes restent équilibrés

```dart
  test('test4', () {
    expect(isBalanced('{what is (42)}[?]'), true, reason: '--err-t4--');
  });
```

Des paires placées côte à côte sont équilibrées

```dart
  test('test5', () {
    expect(isBalanced('()[]{}'), true, reason: '--err-t5--');
  });
```

Une chaîne sans aucun crochet est équilibrée

```dart
  test('test6', () {
    expect(isBalanced('no brackets in here at all'), true, reason: '--err-t6--');
  });
```

Une paire croisée n'est pas équilibrée

```dart
  test('test7', () {
    expect(isBalanced('{[(])}'), false, reason: '--err-t7--');
  });
```

Un crochet ouvrant jamais fermé n'est pas équilibré

```dart
  test('test8', () {
    expect(isBalanced('('), false, reason: '--err-t8--');
  });
```

Un crochet fermant avant tout crochet ouvrant n'est pas équilibré

```dart
  test('test9', () {
    expect(isBalanced(')('), false, reason: '--err-t9--');
  });
```

Des paires croisées plus profondément dans la chaîne ne sont pas équilibrées

```dart
  test('test10', () {
    expect(isBalanced('(([]{[}]))'), false, reason: '--err-t10--');
  });
```

Un crochet fermant restant à la fin n'est pas équilibré

```dart
  test('test11', () {
    expect(isBalanced('())'), false, reason: '--err-t11--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isBalanced(String text) {
  const pairs = {')': '(', ']': '[', '}': '{'};
  final stack = <String>[];

  for (final char in text.split('')) {
    if (char == '(' || char == '[' || char == '{') {
      stack.add(char);
    } else if (pairs.containsKey(char)) {
      if (stack.isEmpty || stack.removeLast() != pairs[char]) {
        return false;
      }
    }
  }

  return stack.isEmpty;
}
```
