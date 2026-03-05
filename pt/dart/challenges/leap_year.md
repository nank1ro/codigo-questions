---
language: dart
exerciseType: 1
difficulty: 3
title: Ano Bissexto
---

# --description--

Em um ano civil existem exatamente 365,25 dias. Mas, eventualmente, isso levará a confusão porque os humanos normalmente contam pela divisibilidade exata de 1 e não com casas decimais. Então, para evitar isso, foi decidido somar todos os 0,25 dias a cada ciclo de quatro anos e dar a esse ano 366 dias (incluindo 29 de fevereiro como um dia intercalar) e chamá-lo de __ano bissexto__. Os outros três anos no ciclo de quatro anos conteriam apenas 365 dias e __não seriam anos bissextos__.

# --instructions--

Neste desafio, levaremos a um novo nível, onde você deve determinar se é um ano bissexto ou não sem o uso da classe `DateTime`, instruções `switch`, blocos __if__, blocos __if-else__ ou operação __ternária__ (`x ? a : b`) nem os operadores lógicos __AND__ (`&&`) e __OR__ (`||`) com a exceção do operador __NOT__ (`!`).

Retorne `true` se for um ano bissexto, `false` caso contrário.

Exemplo de chamada da função:
```dart
print(leapYear(2000));
// prints true
```

# --seed--

```dart
bool leapYear(int year) {
  
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

O uso de `DateTime`, `switch`, `if`, `else`, `&&`, `||` ou `?` não é permitido.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

O ano `2016` é um ano bissexto.

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

O ano `1996` é um ano bissexto.

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

O ano `1600` é um ano bissexto.

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

O ano `2020` é um ano bissexto.

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

O ano `2000` é um ano bissexto.

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

O ano `2008` é um ano bissexto.

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

O ano `1521` não é um ano bissexto.

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

O ano `1800` não é um ano bissexto.

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

O ano `2007` não é um ano bissexto.

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

O ano `2002` não é um ano bissexto.

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

O ano `1979` não é um ano bissexto.

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

O ano `2006` não é um ano bissexto.

```dart
  test('test12', () {
    expect(leapYear(2006), false, reason: '--err-t12--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool leapYear(int year) {
  return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0));
}
```

```dart
bool leapYear(int year) {
  while (year % 100 == 0) {
    year = year ~/ 100;
  }
  return year % 4 == 0;
}
```
