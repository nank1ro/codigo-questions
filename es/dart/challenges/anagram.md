---
language: dart
exerciseType: 1
difficulty: 2
title: Anagrama
---

# --description--

Dos palabras son anagramas cuando una es una reordenación de la otra: usan exactamente las mismas letras, cada letra el mismo número de veces, solo que en un orden diferente. `listen` y `silent` son anagramas, y también lo son `stone` y `tones`.

Una palabra nunca es un anagrama de sí misma. Si las dos palabras son exactamente iguales, no se ha reordenado nada, así que la respuesta es `false`. Ambas palabras se dan en minúsculas y contienen solo las letras de la `a` a la `z`.

# --instructions--

Escribe una función `isAnagram` que reciba dos palabras, `first` y `second`, y devuelva `true` cuando sean anagramas la una de la otra y `false` en caso contrario.

Ejemplos:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Dos palabras idénticas no son anagramas.
- Palabras de longitudes diferentes nunca son anagramas.
- Cada letra debe aparecer el mismo número de veces en ambas palabras.

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

Las palabras "listen" y "silent" son anagramas

```dart
  test('test1', () {
    expect(isAnagram('listen', 'silent'), true, reason: '--err-t1--');
  });
```

Las palabras "stone" y "tones" son anagramas

```dart
  test('test2', () {
    expect(isAnagram('stone', 'tones'), true, reason: '--err-t2--');
  });
```

Una palabra no es un anagrama de sí misma

```dart
  test('test3', () {
    expect(isAnagram('stone', 'stone'), false, reason: '--err-t3--');
  });
```

Palabras de longitudes diferentes no son anagramas

```dart
  test('test4', () {
    expect(isAnagram('abc', 'abcd'), false, reason: '--err-t4--');
  });
```

Las mismas letras en cantidades diferentes no forman un anagrama

```dart
  test('test5', () {
    expect(isAnagram('aab', 'abb'), false, reason: '--err-t5--');
  });
```

Las palabras "anagram" y "nagaram" son anagramas

```dart
  test('test6', () {
    expect(isAnagram('anagram', 'nagaram'), true, reason: '--err-t6--');
  });
```

Dos palabras de la misma longitud con letras diferentes no son anagramas

```dart
  test('test7', () {
    expect(isAnagram('rat', 'car'), false, reason: '--err-t7--');
  });
```

Dos palabras vacías son idénticas, así que no son anagramas

```dart
  test('test8', () {
    expect(isAnagram('', ''), false, reason: '--err-t8--');
  });
```

Dos letras individuales diferentes no son anagramas

```dart
  test('test9', () {
    expect(isAnagram('a', 'b'), false, reason: '--err-t9--');
  });
```

Las palabras "evil" y "vile" son anagramas

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
