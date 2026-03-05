---
language: dart
exerciseType: 1
difficulty: 1
title: Pingos de Chuva
---

# --description--

Sua tarefa é converter um número em uma string que contenha sons de pingos de chuva correspondentes a certos fatores potenciais.
Um fator é um número que divide outro número de forma exata, sem deixar resto.
A maneira mais simples de testar se um número é fator de outro é usar a operação módulo.
As regras dos pingos de chuva são que, se um dado número:

- tem 3 como fator, adicione 'Pling' ao resultado.
- tem 5 como fator, adicione 'Plang' ao resultado.
- tem 7 como fator, adicione 'Plong' ao resultado.
- não tem 3, 5 ou 7 como fator, o resultado deve ser os dígitos do número.

# --instructions--

Escreva uma função que retorne a string correta, exemplos:

- 28 tem 7 como fator, mas não 3 ou 5, então o resultado seria `"Plong"`.
- 30 tem tanto 3 quanto 5 como fatores, mas não 7, então o resultado seria `"PlingPlang"`.
- 34 não é divisível por 3, 5 ou 7, então o resultado seria `"34"`.

Exemplo de chamada da função:
```dart
print(raindrops(28))
// prints "Plong"
```

# --seed--

```dart
String raindrops() {

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

O som para 1 é "1"

```dart
  test('test1', () {
    expect(raindrops(1), "1", reason: '--err-t1--');
  });
```

O som para 3 é "Pling"

```dart
  test('test2', () {
    expect(raindrops(3), "Pling", reason: '--err-t2--');
  });
```

O som para 5 é "Plang"

```dart
  test('test3', () {
    expect(raindrops(5), "Plang", reason: '--err-t3--');
  });
```

O som para 7 é "Plong"

```dart
  test('test4', () {
    expect(raindrops(7), "Plong", reason: '--err-t4--');
  });
```

O som para 6 é "Pling"

```dart
  test('test5', () {
    expect(raindrops(6), "Pling", reason: '--err-t5--');
  });
```

O som para 8 é "8"

```dart
  test('test6', () {
    expect(raindrops(8), "8", reason: '--err-t6--');
  });
```

O som para 9 é "Pling"

```dart
  test('test7', () {
    expect(raindrops(9), "Pling", reason: '--err-t7--');
  });
```

O som para 10 é "Plang"

```dart
  test('test8', () {
    expect(raindrops(10), "Plang", reason: '--err-t8--');
  });
```

O som para 14 é "Plong"

```dart
  test('test9', () {
    expect(raindrops(14), "Plong", reason: '--err-t9--');
  });
```

O som para 15 é "PlingPlang"

```dart
  test('test10', () {
    expect(raindrops(15), "PlingPlang", reason: '--err-t10--');
  });
```

O som para 21 é "PlingPlong"

```dart
  test('test11', () {
    expect(raindrops(21), "PlingPlong", reason: '--err-t11--');
  });
```

O som para 25 é "Plang"

```dart
  test('test12', () {
    expect(raindrops(25), "Plang", reason: '--err-t12--');
  });
```

O som para 27 é "Pling"

```dart
  test('test13', () {
    expect(raindrops(27), "Pling", reason: '--err-t13--');
  });
```

O som para 35 é "PlangPlong"

```dart
  test('test14', () {
    expect(raindrops(35), "PlangPlong", reason: '--err-t14--');
  });
```

O som para 49 é "Plong"

```dart
  test('test15', () {
    expect(raindrops(49), "Plong", reason: '--err-t15--');
  });
```

O som para 52 é "52"

```dart
  test('test16', () {
    expect(raindrops(52), "52", reason: '--err-t16--');
  });
```

O som para 105 é "PlingPlangPlong"

```dart
  test('test17', () {
    expect(raindrops(105), "PlingPlangPlong", reason: '--err-t17--');
  });
```

O som para 3125 é "Plang"

```dart
  test('test18', () {
    expect(raindrops(3125), "Plang", reason: '--err-t18--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String raindrops(int number) {
  var result = "";
  if (number % 3 == 0) {
    result += "Pling";
  }
  if (number % 5 == 0) {
    result += "Plang";
  }
  if (number % 7 == 0) {
    result += "Plong";
  }
  if (result.isEmpty) {
    result = number.toString();
  }
  return result;
}
```
