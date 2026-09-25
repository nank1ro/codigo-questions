---
language: dart
exerciseType: 1
difficulty: 2
title: Relógio
---

# --description--

Um relógio de 24 horas mostra a hora do dia como `HH:MM`, começando em `00:00` logo após a meia-noite e terminando em `23:59`, um minuto antes da próxima meia-noite. Ambas as partes são sempre escritas com dois dígitos, então nove minutos após onze da manhã lê-se `11:09`.

Um dia inteiro dura 1440 minutos. Quando o relógio passa de `23:59`, ele volta para `00:00` e começa o dia novamente, e girá-lo para trás além de `00:00` cai em `23:59`.

# --instructions--

Escreva uma função `clockTime` que recebe dois números inteiros, `hours` e `minutes`, e retorna a leitura de um relógio de 24 horas como a string `"HH:MM"`, com ambas as partes preenchidas com dois dígitos.

Exemplos:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Qualquer um dos números pode ser negativo, ou maior do que um relógio real permite.
- Calcule o número total de minutos como `hours * 60 + minutes` e depois encaixe esse total na faixa de `0` a `1439` para que o relógio faça a volta em ambas as direções.
- `clockTime(24, 0)` é exatamente um dia, então lê-se `"00:00"`.

# --seed--

```dart
String clockTime(int hours, int minutes) {
  
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

Oito da manhã lê-se `08:00`

```dart
  test('test1', () {
    expect(clockTime(8, 0), "08:00", reason: '--err-t1--');
  });
```

Números de um dígito são preenchidos com dois, então nove minutos após onze lê-se `11:09`

```dart
  test('test2', () {
    expect(clockTime(11, 9), "11:09", reason: '--err-t2--');
  });
```

Exatamente um dia inteiro de horas faz a volta para `00:00`

```dart
  test('test3', () {
    expect(clockTime(24, 0), "00:00", reason: '--err-t3--');
  });
```

Minutos acima de 60 são transportados para as horas

```dart
  test('test4', () {
    expect(clockTime(25, 160), "03:40", reason: '--err-t4--');
  });
```

Uma hora negativa gira o relógio para trás além da meia-noite

```dart
  test('test5', () {
    expect(clockTime(-1, 15), "23:15", reason: '--err-t5--');
  });
```

Uma contagem de minutos negativa também gira o relógio para trás

```dart
  test('test6', () {
    expect(clockTime(0, -90), "22:30", reason: '--err-t6--');
  });
```

Mais de um dia inteiro para trás continua fazendo a volta

```dart
  test('test7', () {
    expect(clockTime(-25, 0), "23:00", reason: '--err-t7--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String clockTime(int hours, int minutes) {
  // O % do Dart é o módulo euclidiano, então um total negativo já
  // volta para a faixa 0..1439.
  final total = (hours * 60 + minutes) % 1440;

  final hh = (total ~/ 60).toString().padLeft(2, '0');
  final mm = (total % 60).toString().padLeft(2, '0');
  return '$hh:$mm';
}
```
