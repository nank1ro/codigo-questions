---
language: dart
exerciseType: 1
difficulty: 2
title: Кодирование длин серий
---

# --description--

Кодирование длин серий — один из старейших приёмов сжатия: вместо того чтобы писать один и тот же символ снова и снова, вы записываете, сколько раз он повторяется, а затем сам символ.

Факсимильный аппарат, сканирующий почти пустую страницу, встречает длинные участки одинаковых пикселей, поэтому ряд из двенадцати `W` передаётся по линии как гораздо более короткое `12W`. Когда символ встречается лишь однажды, считать его незачем, поэтому он копируется сам по себе.

# --instructions--

Напишите функцию `encodeRun`, которая принимает строку `text` и возвращает её закодированное представление.

Каждая серия одного и того же символа, повторённого два или более раз, превращается в длину серии, записанную в десятичном виде, за которой следует сам символ. Серия длины один копируется как одиночный символ, без числа перед ним.

Примеры:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- Текст содержит только заглавные буквы от `A` до `Z` и пробелы.
- Серия длиннее девяти символов записывается своим полным десятичным количеством, поэтому двенадцать `W` превращаются в `12W`, но никогда в `9W3W`.
- Пробелы — обычные символы: они считаются и кодируются точно так же, как буквы.
- Пустая строка кодируется в пустую строку.

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

Пустая строка кодируется в пустую строку

```dart
  test('test1', () {
    expect(encodeRun(''), '', reason: '--err-t1--');
  });
```

Одиночный символ копируется без изменений

```dart
  test('test2', () {
    expect(encodeRun('A'), 'A', reason: '--err-t2--');
  });
```

Строка без повторов проходит через кодирование без изменений

```dart
  test('test3', () {
    expect(encodeRun('ABCDE'), 'ABCDE', reason: '--err-t3--');
  });
```

Серия из двух символов превращается в число, за которым следует символ

```dart
  test('test4', () {
    expect(encodeRun('AA'), '2A', reason: '--err-t4--');
  });
```

Смешанный пример "AABCCCDEEEE" превращается в "2AB3CD4E"

```dart
  test('test5', () {
    expect(encodeRun('AABCCCDEEEE'), '2AB3CD4E', reason: '--err-t5--');
  });
```

Серия из двенадцати записывается своим полным десятичным количеством, поэтому результат начинается с "12W"

```dart
  test('test6', () {
    expect(encodeRun('WWWWWWWWWWWWBWW'), '12WB2W', reason: '--err-t6--');
  });
```

Серии пробелов кодируются точно так же, как серии букв

```dart
  test('test7', () {
    expect(encodeRun('  HI  '), '2 HI2 ', reason: '--err-t7--');
  });
```

Серия из десяти записывается как "10A", но никогда как две более короткие серии

```dart
  test('test8', () {
    expect(encodeRun('AAAAAAAAAA'), '10A', reason: '--err-t8--');
  });
```

Чередующиеся одиночные символы копируются без изменений

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
