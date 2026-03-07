---
language: dart
exerciseType: 1
difficulty: 1
title: Капли дождя
---

# --description--

Ваша задача — преобразовать число в строку, содержащую звуки капель дождя, соответствующие определённым потенциальным делителям.
Делитель — это число, которое делит другое число нацело, без остатка.
Простейший способ проверить, является ли число делителем другого — использовать операцию модуля.
Правила капель дождя таковы: если данное число:

- имеет 3 в качестве делителя, добавить 'Pling' к результату.
- имеет 5 в качестве делителя, добавить 'Plang' к результату.
- имеет 7 в качестве делителя, добавить 'Plong' к результату.
- не имеет ни 3, ни 5, ни 7 в качестве делителя, результатом должны быть цифры самого числа.

# --instructions--

Напишите функцию, которая возвращает правильную строку, примеры:

- 28 имеет 7 в качестве делителя, но не 3 или 5, поэтому результат будет `"Plong"`.
- 30 имеет и 3, и 5 в качестве делителей, но не 7, поэтому результат будет `"PlingPlang"`.
- 34 не делится на 3, 5 или 7, поэтому результат будет `"34"`.

Пример вызова функции:
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

Звук для 1 — это "1"

```dart
  test('test1', () {
    expect(raindrops(1), "1", reason: '--err-t1--');
  });
```

Звук для 3 — это "Pling"

```dart
  test('test2', () {
    expect(raindrops(3), "Pling", reason: '--err-t2--');
  });
```

Звук для 5 — это "Plang"

```dart
  test('test3', () {
    expect(raindrops(5), "Plang", reason: '--err-t3--');
  });
```

Звук для 7 — это "Plong"

```dart
  test('test4', () {
    expect(raindrops(7), "Plong", reason: '--err-t4--');
  });
```

Звук для 6 — это "Pling"

```dart
  test('test5', () {
    expect(raindrops(6), "Pling", reason: '--err-t5--');
  });
```

Звук для 8 — это "8"

```dart
  test('test6', () {
    expect(raindrops(8), "8", reason: '--err-t6--');
  });
```

Звук для 9 — это "Pling"

```dart
  test('test7', () {
    expect(raindrops(9), "Pling", reason: '--err-t7--');
  });
```

Звук для 10 — это "Plang"

```dart
  test('test8', () {
    expect(raindrops(10), "Plang", reason: '--err-t8--');
  });
```

Звук для 14 — это "Plong"

```dart
  test('test9', () {
    expect(raindrops(14), "Plong", reason: '--err-t9--');
  });
```

Звук для 15 — это "PlingPlang"

```dart
  test('test10', () {
    expect(raindrops(15), "PlingPlang", reason: '--err-t10--');
  });
```

Звук для 21 — это "PlingPlong"

```dart
  test('test11', () {
    expect(raindrops(21), "PlingPlong", reason: '--err-t11--');
  });
```

Звук для 25 — это "Plang"

```dart
  test('test12', () {
    expect(raindrops(25), "Plang", reason: '--err-t12--');
  });
```

Звук для 27 — это "Pling"

```dart
  test('test13', () {
    expect(raindrops(27), "Pling", reason: '--err-t13--');
  });
```

Звук для 35 — это "PlangPlong"

```dart
  test('test14', () {
    expect(raindrops(35), "PlangPlong", reason: '--err-t14--');
  });
```

Звук для 49 — это "Plong"

```dart
  test('test15', () {
    expect(raindrops(49), "Plong", reason: '--err-t15--');
  });
```

Звук для 52 — это "52"

```dart
  test('test16', () {
    expect(raindrops(52), "52", reason: '--err-t16--');
  });
```

Звук для 105 — это "PlingPlangPlong"

```dart
  test('test17', () {
    expect(raindrops(105), "PlingPlangPlong", reason: '--err-t17--');
  });
```

Звук для 3125 — это "Plang"

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
