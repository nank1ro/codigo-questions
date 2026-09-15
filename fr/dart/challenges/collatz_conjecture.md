---
language: dart
exerciseType: 1
difficulty: 1
title: Conjecture de Collatz
---

# --description--

La conjecture de Collatz part de n'importe quel entier positif `n` et répète une règle simple : si `n` est pair, on le divise par deux ; si `n` est impair, on le remplace par `3n + 1`. Tôt ou tard, la séquence atteint 1.

Par exemple, en partant de 16, la séquence est `16 -> 8 -> 4 -> 2 -> 1`, donc il faut 4 étapes.

Personne n'a jamais prouvé que cela se produit toujours, mais c'est vrai pour tous les nombres testés jusqu'à présent.

# --instructions--

Écrivez une fonction `collatzSteps` qui prend un entier positif `n` et retourne le nombre d'étapes nécessaires pour atteindre 1.

`collatzSteps(1)` vaut 0, car 1 est déjà la fin de la séquence. `collatzSteps(12)` vaut 9, et `collatzSteps(27)` vaut 111.

Exemple d'appel de fonction :
```dart
print(collatzSteps(16));
// affiche 4
```

# --seed--

```dart
int collatzSteps(int n) {

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

`collatzSteps(1)` doit retourner 0, car 1 est déjà la fin de la séquence.

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)` doit retourner 1.

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)` doit retourner 8.

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)` doit retourner 16.

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)` doit retourner 4.

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)` doit retourner 9.

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)` doit retourner 111.

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)` doit retourner 118.

```dart
    test('test8', () {
      expect(collatzSteps(97), 118, reason: '--err-t8--');
    });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int collatzSteps(int n) {
  int value = n;
  int steps = 0;
  while (value != 1) {
    value = value % 2 == 0 ? value ~/ 2 : 3 * value + 1;
    steps++;
  }
  return steps;
}
```
