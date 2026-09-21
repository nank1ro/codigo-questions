---
language: dart
exerciseType: 1
difficulty: 2
title: Lauflängencodierung
---

# --description--

Lauflängencodierung ist einer der ältesten Kompressionstricks überhaupt: Statt dasselbe Zeichen immer wieder zu schreiben, schreiben Sie, wie oft es sich wiederholt, und danach das Zeichen selbst.

Ein Faxgerät, das eine überwiegend leere Seite scannt, trifft auf lange Strecken identischer Pixel, deshalb wandert eine Reihe von zwölf `W` als viel kürzeres `12W` durch die Leitung. Taucht ein Zeichen nur einmal auf, bringt das Zählen nichts, also wird es einfach einzeln übernommen.

# --instructions--

Schreiben Sie eine Funktion `encodeRun`, die einen String `text` entgegennimmt und seine lauflängencodierte Form zurückgibt.

Jede Folge desselben Zeichens, das zwei- oder mehrmals hintereinander wiederholt wird, wird zu der Länge der Folge in Dezimalschreibweise, gefolgt von dem Zeichen selbst. Eine Folge der Länge eins wird als einzelnes Zeichen übernommen, ohne Zahl davor.

Beispiele:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- Der Text enthält nur Großbuchstaben von `A` bis `Z` sowie Leerzeichen.
- Eine Folge von mehr als neun Zeichen schreibt ihre vollständige Dezimalzahl, zwölf `W` werden also zu `12W` und nie zu `9W3W`.
- Leerzeichen sind ganz normale Zeichen: Sie werden genauso gezählt und codiert wie Buchstaben.
- Der leere String wird zu dem leeren String codiert.

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

Der leere String wird zu dem leeren String codiert

```dart
  test('test1', () {
    expect(encodeRun(''), '', reason: '--err-t1--');
  });
```

Ein einzelnes Zeichen wird unverändert als es selbst übernommen

```dart
  test('test2', () {
    expect(encodeRun('A'), 'A', reason: '--err-t2--');
  });
```

Ein String ohne Wiederholungen durchläuft die Codierung unverändert

```dart
  test('test3', () {
    expect(encodeRun('ABCDE'), 'ABCDE', reason: '--err-t3--');
  });
```

Eine Folge von zwei wird zu der Anzahl, gefolgt von dem Zeichen

```dart
  test('test4', () {
    expect(encodeRun('AA'), '2A', reason: '--err-t4--');
  });
```

Das gemischte Beispiel "AABCCCDEEEE" wird zu "2AB3CD4E"

```dart
  test('test5', () {
    expect(encodeRun('AABCCCDEEEE'), '2AB3CD4E', reason: '--err-t5--');
  });
```

Eine Folge von zwölf schreibt ihre vollständige Dezimalzahl, deshalb beginnt das Ergebnis mit "12W"

```dart
  test('test6', () {
    expect(encodeRun('WWWWWWWWWWWWBWW'), '12WB2W', reason: '--err-t6--');
  });
```

Folgen von Leerzeichen werden genauso codiert wie Folgen von Buchstaben

```dart
  test('test7', () {
    expect(encodeRun('  HI  '), '2 HI2 ', reason: '--err-t7--');
  });
```

Eine Folge von zehn wird als "10A" geschrieben, nie als zwei kürzere Folgen

```dart
  test('test8', () {
    expect(encodeRun('AAAAAAAAAA'), '10A', reason: '--err-t8--');
  });
```

Einzelne Zeichen, die sich abwechseln, werden alle unverändert als sie selbst übernommen

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
