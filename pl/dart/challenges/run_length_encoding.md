---
language: dart
exerciseType: 1
difficulty: 2
title: Kodowanie RLE
---

# --description--

Kodowanie RLE (run-length encoding) to jedna z najstarszych sztuczek kompresji: zamiast zapisywać ten sam znak w kółko, zapisujesz, ile razy się powtarza, a następnie sam znak.

Faks skanujący w większości pustą stronę napotyka długie ciągi identycznych pikseli, więc rząd dwunastu `W` wędruje przez linię jako znacznie krótsze `12W`. Gdy jakiś znak pojawia się tylko raz, liczenie go niczego nie daje, więc jest on kopiowany samodzielnie.

# --instructions--

Napisz funkcję `encodeRun`, która przyjmuje ciąg znaków `text` i zwraca jego postać zakodowaną metodą RLE.

Każda seria tego samego znaku powtórzonego dwa lub więcej razy staje się długością serii zapisaną dziesiętnie, po której następuje ten znak. Seria o długości jeden jest kopiowana jako pojedynczy znak, bez liczby przed nim.

Przykłady:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- Tekst zawiera wyłącznie wielkie litery od `A` do `Z` oraz spacje.
- Seria dłuższa niż dziewięć znaków używa pełnej liczby dziesiętnej, więc dwanaście `W` daje `12W`, a nigdy `9W3W`.
- Spacje to zwykłe znaki: są liczone i kodowane dokładnie tak samo jak litery.
- Pusty ciąg znaków koduje się do pustego ciągu znaków.

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

Pusty ciąg znaków koduje się do pustego ciągu znaków

```dart
  test('test1', () {
    expect(encodeRun(''), '', reason: '--err-t1--');
  });
```

Pojedynczy znak jest kopiowany jako sam siebie

```dart
  test('test2', () {
    expect(encodeRun('A'), 'A', reason: '--err-t2--');
  });
```

Ciąg znaków bez powtórzeń przechodzi bez zmian

```dart
  test('test3', () {
    expect(encodeRun('ABCDE'), 'ABCDE', reason: '--err-t3--');
  });
```

Seria o długości dwa staje się liczbą, po której następuje znak

```dart
  test('test4', () {
    expect(encodeRun('AA'), '2A', reason: '--err-t4--');
  });
```

Mieszany przykład "AABCCCDEEEE" staje się "2AB3CD4E"

```dart
  test('test5', () {
    expect(encodeRun('AABCCCDEEEE'), '2AB3CD4E', reason: '--err-t5--');
  });
```

Seria dwunastu znaków używa pełnej liczby dziesiętnej, więc wynik zaczyna się od "12W"

```dart
  test('test6', () {
    expect(encodeRun('WWWWWWWWWWWWBWW'), '12WB2W', reason: '--err-t6--');
  });
```

Serie spacji są kodowane dokładnie tak samo jak serie liter

```dart
  test('test7', () {
    expect(encodeRun('  HI  '), '2 HI2 ', reason: '--err-t7--');
  });
```

Seria dziesięciu znaków jest zapisywana jako "10A", a nigdy jako dwie krótsze serie

```dart
  test('test8', () {
    expect(encodeRun('AAAAAAAAAA'), '10A', reason: '--err-t8--');
  });
```

Naprzemiennie występujące pojedyncze znaki są wszystkie kopiowane jako sam siebie

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
