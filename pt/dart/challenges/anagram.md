---
language: dart
exerciseType: 1
difficulty: 2
title: Anagrama
---

# --description--

Duas palavras são anagramas quando uma é um rearranjo da outra: elas usam exatamente as mesmas letras, cada letra o mesmo número de vezes, apenas em uma ordem diferente. `listen` e `silent` são anagramas, assim como `stone` e `tones`.

Uma palavra nunca é um anagrama de si mesma. Se as duas palavras forem exatamente iguais, nada foi rearranjado, então a resposta é `false`. Ambas as palavras são dadas em minúsculas e contêm apenas as letras de `a` a `z`.

# --instructions--

Escreva uma função `isAnagram` que recebe duas palavras, `first` e `second`, e retorna `true` quando elas são anagramas uma da outra e `false` caso contrário.

Exemplos:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Duas palavras idênticas não são anagramas.
- Palavras de tamanhos diferentes nunca são anagramas.
- Cada letra deve aparecer o mesmo número de vezes nas duas palavras.

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

As palavras "listen" e "silent" são anagramas

```dart
  test('test1', () {
    expect(isAnagram('listen', 'silent'), true, reason: '--err-t1--');
  });
```

As palavras "stone" e "tones" são anagramas

```dart
  test('test2', () {
    expect(isAnagram('stone', 'tones'), true, reason: '--err-t2--');
  });
```

Uma palavra não é um anagrama de si mesma

```dart
  test('test3', () {
    expect(isAnagram('stone', 'stone'), false, reason: '--err-t3--');
  });
```

Palavras de tamanhos diferentes não são anagramas

```dart
  test('test4', () {
    expect(isAnagram('abc', 'abcd'), false, reason: '--err-t4--');
  });
```

As mesmas letras em quantidades diferentes não formam um anagrama

```dart
  test('test5', () {
    expect(isAnagram('aab', 'abb'), false, reason: '--err-t5--');
  });
```

As palavras "anagram" e "nagaram" são anagramas

```dart
  test('test6', () {
    expect(isAnagram('anagram', 'nagaram'), true, reason: '--err-t6--');
  });
```

Duas palavras do mesmo tamanho com letras diferentes não são anagramas

```dart
  test('test7', () {
    expect(isAnagram('rat', 'car'), false, reason: '--err-t7--');
  });
```

Duas palavras vazias são idênticas, então não são anagramas

```dart
  test('test8', () {
    expect(isAnagram('', ''), false, reason: '--err-t8--');
  });
```

Duas letras únicas diferentes não são anagramas

```dart
  test('test9', () {
    expect(isAnagram('a', 'b'), false, reason: '--err-t9--');
  });
```

As palavras "evil" e "vile" são anagramas

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
