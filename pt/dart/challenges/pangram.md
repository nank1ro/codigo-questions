---
language: dart
exerciseType: 1
difficulty: 1
title: Pangrama
---

# --description--

Um pangrama é uma frase que usa cada letra do alfabeto inglês pelo menos uma vez. O exemplo mais conhecido é "the quick brown fox jumps over the lazy dog", que reúne todas as 26 letras em nove palavras curtas.

A verificação não diferencia maiúsculas de minúsculas, então `A` e `a` contam como a mesma letra. Dígitos, pontuação e espaços são ignorados: não são letras, mas também não são motivo para rejeitar uma frase.

# --instructions--

Escreva uma função `isPangram` que recebe uma frase e retorna `true` se a frase for um pangrama e `false` caso contrário.

Exemplos:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Uma frase vazia não é um pangrama.
- Apenas as 26 letras de `a` a `z` contam.

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

Uma frase vazia não é um pangrama

```dart
  test('test1', () {
    expect(isPangram(''), false, reason: '--err-t1--');
  });
```

A frase clássica "the quick brown fox jumps over the lazy dog" é um pangrama

```dart
  test('test2', () {
    expect(isPangram('the quick brown fox jumps over the lazy dog'), true, reason: '--err-t2--');
  });
```

Uma frase sem a letra `x` não é um pangrama

```dart
  test('test3', () {
    expect(isPangram('a quick movement of the enemy will jeopardize five gunboats'), false, reason: '--err-t3--');
  });
```

A frase "the five boxing wizards jump quickly" é um pangrama

```dart
  test('test4', () {
    expect(isPangram('the five boxing wizards jump quickly'), true, reason: '--err-t4--');
  });
```

Sublinhados são ignorados, então a frase ainda é um pangrama

```dart
  test('test5', () {
    expect(isPangram('the_quick_brown_fox_jumps_over_the_lazy_dog'), true, reason: '--err-t5--');
  });
```

Dígitos são ignorados, então a frase ainda é um pangrama

```dart
  test('test6', () {
    expect(isPangram('the 1 quick brown fox jumps over the 2 lazy dogs'), true, reason: '--err-t6--');
  });
```

Dígitos não substituem as letras `e`, `i` e `t`

```dart
  test('test7', () {
    expect(isPangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'), false, reason: '--err-t7--');
  });
```

Uma frase em maiúsculas também é um pangrama

```dart
  test('test8', () {
    expect(isPangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), true, reason: '--err-t8--');
  });
```

Misturar maiúsculas e minúsculas da mesma metade do alfabeto não é suficiente

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
