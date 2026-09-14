---
language: dart
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

Un pangramma è una frase che usa almeno una volta ogni lettera dell'alfabeto inglese. L'esempio più noto è "the quick brown fox jumps over the lazy dog", che fa stare tutte e 26 le lettere in nove parole brevi.

Il controllo non distingue tra maiuscole e minuscole, quindi `A` e `a` contano come la stessa lettera. Cifre, punteggiatura e spazi vengono ignorati: non sono lettere, ma non sono nemmeno un motivo per rifiutare una frase.

# --instructions--

Scrivi una funzione `isPangram` che prende una frase e restituisce `true` se la frase è un pangramma e `false` altrimenti.

Esempi:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Una frase vuota non è un pangramma.
- Contano solo le 26 lettere dalla `a` alla `z`.

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

Una frase vuota non è un pangramma

```dart
  test('test1', () {
    expect(isPangram(''), false, reason: '--err-t1--');
  });
```

La frase classica "the quick brown fox jumps over the lazy dog" è un pangramma

```dart
  test('test2', () {
    expect(isPangram('the quick brown fox jumps over the lazy dog'), true, reason: '--err-t2--');
  });
```

Una frase a cui manca la lettera `x` non è un pangramma

```dart
  test('test3', () {
    expect(isPangram('a quick movement of the enemy will jeopardize five gunboats'), false, reason: '--err-t3--');
  });
```

La frase "the five boxing wizards jump quickly" è un pangramma

```dart
  test('test4', () {
    expect(isPangram('the five boxing wizards jump quickly'), true, reason: '--err-t4--');
  });
```

I trattini bassi vengono ignorati, quindi la frase resta un pangramma

```dart
  test('test5', () {
    expect(isPangram('the_quick_brown_fox_jumps_over_the_lazy_dog'), true, reason: '--err-t5--');
  });
```

Le cifre vengono ignorate, quindi la frase resta un pangramma

```dart
  test('test6', () {
    expect(isPangram('the 1 quick brown fox jumps over the 2 lazy dogs'), true, reason: '--err-t6--');
  });
```

Le cifre non sostituiscono le lettere `e`, `i` e `t`

```dart
  test('test7', () {
    expect(isPangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'), false, reason: '--err-t7--');
  });
```

Anche una frase in maiuscolo è un pangramma

```dart
  test('test8', () {
    expect(isPangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), true, reason: '--err-t8--');
  });
```

Mescolare maiuscole e minuscole della stessa metà dell'alfabeto non basta

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
