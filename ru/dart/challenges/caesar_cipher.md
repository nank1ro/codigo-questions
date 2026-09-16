---
language: dart
exerciseType: 1
difficulty: 2
title: Шифр Цезаря
---

# --description--

Юлий Цезарь защищал свои личные письма одним из старейших приёмов криптографии: он заменял каждую букву сообщения буквой, отстоящей от исходной на фиксированное число позиций дальше по алфавиту. При сдвиге 3 `a` становится `d`, `b` становится `e`, а `c` становится `f`.

Алфавит замкнут в круг, поэтому буквы в его конце возвращаются к началу: при сдвиге 3 `x` становится `a`, `y` становится `b`, а `z` становится `c`.

Всё, что не является буквой — например, пробел, запятая, восклицательный знак или цифра, — проходит через шифр без изменений.

# --instructions--

Напишите функцию `caesarCipher`, которая принимает сообщение `text` и целое число `shift`, и возвращает закодированное сообщение.

Примеры:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Сообщение всегда записано строчными буквами, поэтому вам никогда не придётся иметь дело с заглавными буквами.
- Символы, не являющиеся буквами, сохраняют свою позицию и своё значение.
- Сдвиг никогда не бывает отрицательным. Сдвиг `0` оставляет сообщение без изменений, как и сдвиг `26`.

# --seed--

```dart
String caesarCipher(String text, int shift) {
  
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

Сдвиг 3 превращает "hello" в "khoor"

```dart
  test('test1', () {
    expect(caesarCipher('hello', 3), 'khoor', reason: '--err-t1--');
  });
```

Конец алфавита замыкается по кругу, поэтому "xyz" становится "abc"

```dart
  test('test2', () {
    expect(caesarCipher('xyz', 3), 'abc', reason: '--err-t2--');
  });
```

Сдвиг 0 оставляет сообщение без изменений

```dart
  test('test3', () {
    expect(caesarCipher('abc', 0), 'abc', reason: '--err-t3--');
  });
```

Сдвиг 26 — это полный оборот алфавита, поэтому сообщение не меняется

```dart
  test('test4', () {
    expect(caesarCipher('abc', 26), 'abc', reason: '--err-t4--');
  });
```

Знаки препинания и пробелы проходят через шифр без изменений

```dart
  test('test5', () {
    expect(caesarCipher('codigo, rocks!', 5), 'htinlt, wthpx!', reason: '--err-t5--');
  });
```

Пустое сообщение остаётся пустым

```dart
  test('test6', () {
    expect(caesarCipher('', 4), '', reason: '--err-t6--');
  });
```

Пробелы между отдельными буквами сохраняются

```dart
  test('test7', () {
    expect(caesarCipher('a b c', 1), 'b c d', reason: '--err-t7--');
  });
```

Цифры не сдвигаются, даже при сдвиге 25

```dart
  test('test8', () {
    expect(caesarCipher('abc 123!', 25), 'zab 123!', reason: '--err-t8--');
  });
```

Сдвиг 13 кодирует целое предложение

```dart
  test('test9', () {
    expect(caesarCipher('the quick brown fox jumps over the lazy dog', 13), 'gur dhvpx oebja sbk whzcf bire gur ynml qbt', reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String caesarCipher(String text, int shift) {
  final a = 'a'.codeUnitAt(0);
  final z = 'z'.codeUnitAt(0);
  final encoded = <int>[];

  for (final code in text.codeUnits) {
    if (code >= a && code <= z) {
      encoded.add(a + (code - a + shift) % 26);
    } else {
      encoded.add(code);
    }
  }

  return String.fromCharCodes(encoded);
}
```
