---
language: dart
exerciseType: 1
difficulty: 2
title: Контрольная сумма Луна
---

# --description--

Алгоритм Луна — это простая контрольная сумма, используемая для проверки идентификационных номеров, таких как номера кредитных карт.

Перед проверкой числа удалите из строки все пробелы. Строка является валидной, только если оставшееся длиннее одного символа, а исходная строка не содержит ничего, кроме цифр и пробелов.

Чтобы выполнить проверку, начните с крайней правой цифры и двигайтесь влево, удваивая каждую вторую цифру. Если удвоение даёт число больше 9, вычтите из него 9. Затем сложите все цифры: число является валидным, только если сумма делится на 10.

Например, `"059"` даёт `0`, затем `5` при удвоении превращается в `10`, которое становится `1`, затем `9`. Их сумма равна `10`, что делится на 10, поэтому число является валидным.

# --instructions--

Напишите функцию `isValid`, которая принимает строку и возвращает `true`, если число является валидным, и `false` в противном случае.

- `"4539 3195 0343 6467"` проходит контрольную сумму, поэтому результат — `true`.
- `"8273 1232 7352 0569"` не проходит контрольную сумму, поэтому результат — `false`.
- `"0"` имеет длину всего один символ, поэтому результат — `false`.
- `"055-444-285"` содержит символ, который не является цифрой или пробелом, поэтому результат — `false`.

Пример вызова функции:
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

Одиночная цифра не является валидной.

```dart
  test('test1', () {
    expect(isValid("0"), false, reason: '--err-t1--');
  });
```

Одиночная цифра с ведущим пробелом не является валидной.

```dart
  test('test2', () {
    expect(isValid(" 0"), false, reason: '--err-t2--');
  });
```

Число `"059"` является валидным.

```dart
  test('test3', () {
    expect(isValid("059"), true, reason: '--err-t3--');
  });
```

Число `"59"` является валидным.

```dart
  test('test4', () {
    expect(isValid("59"), true, reason: '--err-t4--');
  });
```

Число `"055 444 285"` является валидным.

```dart
  test('test5', () {
    expect(isValid("055 444 285"), true, reason: '--err-t5--');
  });
```

Число `"055 444 286"` не является валидным.

```dart
  test('test6', () {
    expect(isValid("055 444 286"), false, reason: '--err-t6--');
  });
```

Число `"8273 1232 7352 0569"` не является валидным.

```dart
  test('test7', () {
    expect(isValid("8273 1232 7352 0569"), false, reason: '--err-t7--');
  });
```

Число `"4539 3195 0343 6467"` является валидным.

```dart
  test('test8', () {
    expect(isValid("4539 3195 0343 6467"), true, reason: '--err-t8--');
  });
```

Число `"1 2345 6789 1234 5678 9012"` не является валидным.

```dart
  test('test9', () {
    expect(isValid("1 2345 6789 1234 5678 9012"), false, reason: '--err-t9--');
  });
```

Число `"095 245 88"` является валидным.

```dart
  test('test10', () {
    expect(isValid("095 245 88"), true, reason: '--err-t10--');
  });
```

Буква делает число невалидным.

```dart
  test('test11', () {
    expect(isValid("055a 444 285"), false, reason: '--err-t11--');
  });
```

Дефисы делают число невалидным.

```dart
  test('test12', () {
    expect(isValid("055-444-285"), false, reason: '--err-t12--');
  });
```

Знак препинания делает число невалидным.

```dart
  test('test13', () {
    expect(isValid(":9"), false, reason: '--err-t13--');
  });
```

Спецсимволы делают число невалидным.

```dart
  test('test14', () {
    expect(isValid("055# 444\$ 285"), false, reason: '--err-t14--');
  });
```

Пустая строка не является валидной.

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
