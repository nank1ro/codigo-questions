---
language: dart
exerciseType: 1
difficulty: 2
title: Szyfr Cezara
---

# --description--

Juliusz Cezar chronił swoje prywatne listy jedną z najstarszych sztuczek kryptografii: zastępował każdą literę wiadomości literą oddaloną o stałą liczbę pozycji w alfabecie. Przy przesunięciu o 3 `a` staje się `d`, `b` staje się `e`, a `c` staje się `f`.

Alfabet zachowuje się jak okrąg, więc litery z końca zawijają się z powrotem do początku: przy przesunięciu o 3 `x` staje się `a`, `y` staje się `b`, a `z` staje się `c`.

Wszystko, co nie jest literą, na przykład spacja, przecinek, wykrzyknik albo cyfra, przechodzi przez szyfr bez zmian.

# --instructions--

Napisz funkcję `caesarCipher`, która przyjmuje wiadomość `text` i liczbę całkowitą `shift`, i zwraca zaszyfrowaną wiadomość.

Przykłady:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Wiadomość zawsze składa się z małych liter, więc nie musisz przejmować się wielkimi literami.
- Znaki, które nie są literami, zachowują swoje miejsce i swoją wartość.
- Przesunięcie nigdy nie jest ujemne. Przesunięcie o `0` pozostawia wiadomość bez zmian, podobnie jak przesunięcie o `26`.

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

Przesunięcie o 3 zamienia "hello" w "khoor"

```dart
  test('test1', () {
    expect(caesarCipher('hello', 3), 'khoor', reason: '--err-t1--');
  });
```

Koniec alfabetu zawija się do początku, więc "xyz" staje się "abc"

```dart
  test('test2', () {
    expect(caesarCipher('xyz', 3), 'abc', reason: '--err-t2--');
  });
```

Przesunięcie o 0 pozostawia wiadomość bez zmian

```dart
  test('test3', () {
    expect(caesarCipher('abc', 0), 'abc', reason: '--err-t3--');
  });
```

Przesunięcie o 26 to pełny obrót alfabetu, więc wiadomość pozostaje bez zmian

```dart
  test('test4', () {
    expect(caesarCipher('abc', 26), 'abc', reason: '--err-t4--');
  });
```

Znaki interpunkcyjne i spacje przechodzą bez zmian

```dart
  test('test5', () {
    expect(caesarCipher('codigo, rocks!', 5), 'htinlt, wthpx!', reason: '--err-t5--');
  });
```

Pusta wiadomość pozostaje pusta

```dart
  test('test6', () {
    expect(caesarCipher('', 4), '', reason: '--err-t6--');
  });
```

Spacje między pojedynczymi literami są zachowane

```dart
  test('test7', () {
    expect(caesarCipher('a b c', 1), 'b c d', reason: '--err-t7--');
  });
```

Cyfry nie są przesuwane, nawet przy przesunięciu o 25

```dart
  test('test8', () {
    expect(caesarCipher('abc 123!', 25), 'zab 123!', reason: '--err-t8--');
  });
```

Przesunięcie o 13 szyfruje całe zdanie

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
