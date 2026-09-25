---
language: dart
exerciseType: 1
difficulty: 2
title: Codificação run-length
---

# --description--

A codificação run-length é um dos truques de compressão mais antigos que existem: em vez de escrever o mesmo caractere repetidas vezes, você escreve quantas vezes ele se repete e, em seguida, o próprio caractere.

Uma máquina de fax que digitaliza uma página quase inteira em branco encontra longos trechos de pixels idênticos, de modo que uma fileira de doze `W` percorre a linha como o `12W`, bem mais curto. Quando um caractere aparece apenas uma vez, não há nada a ganhar ao contá-lo, então ele é copiado sozinho.

# --instructions--

Escreva uma função `encodeRun` que recebe uma string `text` e retorna a sua codificação em run-length.

Cada sequência do mesmo caractere repetido duas ou mais vezes se torna o comprimento da sequência escrito em decimal, seguido desse caractere. Uma sequência de comprimento um é copiada como o único caractere, sem nenhum número na frente.

Exemplos:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- O texto contém apenas letras maiúsculas de `A` a `Z` e espaços.
- Uma sequência com mais de nove caracteres usa sua contagem decimal completa, de modo que doze `W` se tornam `12W` e nunca `9W3W`.
- Espaços são caracteres comuns: eles são contados e codificados exatamente como as letras.
- A string vazia é codificada como a string vazia.

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

A string vazia é codificada como a string vazia

```dart
  test('test1', () {
    expect(encodeRun(''), '', reason: '--err-t1--');
  });
```

Um único caractere é copiado como ele mesmo

```dart
  test('test2', () {
    expect(encodeRun('A'), 'A', reason: '--err-t2--');
  });
```

Uma string sem repetições passa inalterada

```dart
  test('test3', () {
    expect(encodeRun('ABCDE'), 'ABCDE', reason: '--err-t3--');
  });
```

Uma sequência de dois se torna a contagem seguida do caractere

```dart
  test('test4', () {
    expect(encodeRun('AA'), '2A', reason: '--err-t4--');
  });
```

O exemplo misto "AABCCCDEEEE" se torna "2AB3CD4E"

```dart
  test('test5', () {
    expect(encodeRun('AABCCCDEEEE'), '2AB3CD4E', reason: '--err-t5--');
  });
```

Uma sequência de doze usa sua contagem decimal completa, então o resultado começa com "12W"

```dart
  test('test6', () {
    expect(encodeRun('WWWWWWWWWWWWBWW'), '12WB2W', reason: '--err-t6--');
  });
```

Sequências de espaços são codificadas exatamente como sequências de letras

```dart
  test('test7', () {
    expect(encodeRun('  HI  '), '2 HI2 ', reason: '--err-t7--');
  });
```

Uma sequência de dez é escrita como "10A", nunca como duas sequências menores

```dart
  test('test8', () {
    expect(encodeRun('AAAAAAAAAA'), '10A', reason: '--err-t8--');
  });
```

Caracteres únicos alternados são todos copiados como eles mesmos

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
