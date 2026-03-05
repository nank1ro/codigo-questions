---
language: dart
exerciseType: 1
difficulty: 1
title: Fonction d'Ackermann
---

# --description--

La fonction d'Ackermann est un exemple classique d'une fonction récursive, notable en particulier parce qu'elle n'est pas une fonction récursive primitive. Elle croît très rapidement en valeur, tout comme la taille de son arbre d'appels.

La fonction d'Ackermann est généralement définie comme suit :

![ackermann_function](https://bit.ly/3z9u4zh)

Ses arguments ne sont jamais négatifs et il se termine toujours

# --instructions--

Écrivez une fonction qui retourne la valeur de la fonction d'Ackermann.

# --seed--

```dart
int ack(int m, int n) {
    
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

`ack(0, 0)` doit retourner 1.

```dart
    test('test1', () {
      expect(ack(0, 0), 1, reason: '--err-t1--');
    });
```

`ack(1, 1)` doit retourner 3.

```dart
    test('test2', () {
      expect(ack(1, 1), 3, reason: '--err-t2--');
    });
```

`ack(2, 5)` doit retourner 13.

```dart
    test('test3', () {
      expect(ack(2, 5), 13, reason: '--err-t3--');
    });
```

`ack(3, 3)` doit retourner 61.

```dart
    test('test4', () {
      expect(ack(3, 3), 61, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int ack(int m, int n) {
  if (m == 0) return n + 1;
  return ack(
    m - 1,
    (n == 0) ? 1 : ack(m, n - 1),
  );
}
```
