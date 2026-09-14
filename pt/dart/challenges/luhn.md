---
language: dart
exerciseType: 1
difficulty: 2
title: Checksum de Luhn
---

# --description--

O algoritmo de Luhn é um checksum simples usado para validar números de identificação, como números de cartão de crédito.

Antes de verificar um número, remova todos os espaços da string. A string só é válida se o que restar tiver mais de um caractere e se a string original contiver nada além de dígitos e espaços.

Para fazer a verificação, comece pelo dígito mais à direita e avance para a esquerda, dobrando cada segundo dígito. Quando a duplicação produzir um número maior que 9, subtraia 9 dele. Em seguida, some todos os dígitos: o número só é válido se a soma for divisível por 10.

Por exemplo, `"059"` resulta em `0`, depois `5` dobrado é `10`, que se torna `1`, e depois `9`. A soma deles é `10`, que é divisível por 10, então o número é válido.

# --instructions--

Escreva uma função `isValid` que recebe uma string e retorna `true` quando o número é válido, `false` caso contrário.

- `"4539 3195 0343 6467"` passa no checksum, então o resultado é `true`.
- `"8273 1232 7352 0569"` falha no checksum, então o resultado é `false`.
- `"0"` tem apenas um caractere, então o resultado é `false`.
- `"055-444-285"` contém um caractere que não é um dígito nem um espaço, então o resultado é `false`.

Exemplo de chamada de função:
```dart
print(isValid("095 245 88"));
// prints true
```

# --seed--

```dart
bool isValid(String value) {
  
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

Um único dígito não é válido.

```dart
  test('test1', () {
    expect(isValid("0"), false, reason: '--err-t1--');
  });
```

Um único dígito com um espaço à esquerda não é válido.

```dart
  test('test2', () {
    expect(isValid(" 0"), false, reason: '--err-t2--');
  });
```

O número `"059"` é válido.

```dart
  test('test3', () {
    expect(isValid("059"), true, reason: '--err-t3--');
  });
```

O número `"59"` é válido.

```dart
  test('test4', () {
    expect(isValid("59"), true, reason: '--err-t4--');
  });
```

O número `"055 444 285"` é válido.

```dart
  test('test5', () {
    expect(isValid("055 444 285"), true, reason: '--err-t5--');
  });
```

O número `"055 444 286"` não é válido.

```dart
  test('test6', () {
    expect(isValid("055 444 286"), false, reason: '--err-t6--');
  });
```

O número `"8273 1232 7352 0569"` não é válido.

```dart
  test('test7', () {
    expect(isValid("8273 1232 7352 0569"), false, reason: '--err-t7--');
  });
```

O número `"4539 3195 0343 6467"` é válido.

```dart
  test('test8', () {
    expect(isValid("4539 3195 0343 6467"), true, reason: '--err-t8--');
  });
```

O número `"1 2345 6789 1234 5678 9012"` não é válido.

```dart
  test('test9', () {
    expect(isValid("1 2345 6789 1234 5678 9012"), false, reason: '--err-t9--');
  });
```

O número `"095 245 88"` é válido.

```dart
  test('test10', () {
    expect(isValid("095 245 88"), true, reason: '--err-t10--');
  });
```

Uma letra torna o número inválido.

```dart
  test('test11', () {
    expect(isValid("055a 444 285"), false, reason: '--err-t11--');
  });
```

Travessões tornam o número inválido.

```dart
  test('test12', () {
    expect(isValid("055-444-285"), false, reason: '--err-t12--');
  });
```

Um caractere de pontuação torna o número inválido.

```dart
  test('test13', () {
    expect(isValid(":9"), false, reason: '--err-t13--');
  });
```

Símbolos tornam o número inválido.

```dart
  test('test14', () {
    expect(isValid("055# 444\$ 285"), false, reason: '--err-t14--');
  });
```

Uma string vazia não é válida.

```dart
  test('test15', () {
    expect(isValid(""), false, reason: '--err-t15--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isValid(String value) {
  var sum = 0;
  var count = 0;
  for (var i = value.length - 1; i >= 0; i--) {
    final code = value.codeUnitAt(i);
    if (code == 32) {
      continue;
    }
    if (code < 48 || code > 57) {
      return false;
    }
    var digit = code - 48;
    if (count % 2 == 1) {
      digit *= 2;
      if (digit > 9) {
        digit -= 9;
      }
    }
    sum += digit;
    count++;
  }
  return count > 1 && sum % 10 == 0;
}
```
