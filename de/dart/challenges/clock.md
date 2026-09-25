---
language: dart
exerciseType: 1
difficulty: 2
title: Uhr
---

# --description--

Eine 24-Stunden-Uhr zeigt die Tageszeit als `HH:MM` an, beginnend mit `00:00` direkt nach Mitternacht und endend mit `23:59` eine Minute vor der nächsten Mitternacht. Beide Teile werden immer zweistellig geschrieben, daher zeigt neun Minuten nach elf Uhr morgens `11:09` an.

Ein ganzer Tag dauert 1440 Minuten. Sobald die Uhr über `23:59` hinausgeht, springt sie auf `00:00` und beginnt den Tag von vorne, und dreht man sie über `00:00` zurück, landet sie auf `23:59`.

# --instructions--

Schreiben Sie eine Funktion `clockTime`, die zwei ganze Zahlen, `hours` und `minutes`, entgegennimmt und die Anzeige einer 24-Stunden-Uhr als Zeichenkette `"HH:MM"` zurückgibt, wobei beide Teile zweistellig aufgefüllt sind.

Beispiele:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Eine der beiden Zahlen darf negativ sein oder größer, als es eine echte Uhr erlaubt.
- Berechnen Sie die Gesamtzahl der Minuten als `hours * 60 + minutes` und rechnen Sie diese Summe in den Bereich von `0` bis `1439` um, damit die Uhr in beide Richtungen überläuft.
- `clockTime(24, 0)` ist genau ein Tag, daher zeigt die Uhr `"00:00"` an.

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

Acht Uhr morgens zeigt `08:00` an

```dart
  test('test1', () {
    expect(clockTime(8, 0), "08:00", reason: '--err-t1--');
  });
```

Einzelne Ziffern werden zweistellig aufgefüllt, daher zeigt neun Minuten nach elf `11:09` an

```dart
  test('test2', () {
    expect(clockTime(11, 9), "11:09", reason: '--err-t2--');
  });
```

Genau ein ganzer Tag Stunden springt auf `00:00` zurück

```dart
  test('test3', () {
    expect(clockTime(24, 0), "00:00", reason: '--err-t3--');
  });
```

Minuten über 60 werden in die Stunden übertragen

```dart
  test('test4', () {
    expect(clockTime(25, 160), "03:40", reason: '--err-t4--');
  });
```

Eine negative Stunde dreht die Uhr über Mitternacht hinaus zurück

```dart
  test('test5', () {
    expect(clockTime(-1, 15), "23:15", reason: '--err-t5--');
  });
```

Eine negative Minutenanzahl dreht die Uhr ebenfalls zurück

```dart
  test('test6', () {
    expect(clockTime(0, -90), "22:30", reason: '--err-t6--');
  });
```

Mehr als ein ganzer Tag zurück läuft immer weiter über

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
  // Darts % ist das euklidische Modulo, daher landet eine negative Summe
  // bereits vorwärts gewrappt in 0..1439.
  final total = (hours * 60 + minutes) % 1440;

  final hh = (total ~/ 60).toString().padLeft(2, '0');
  final mm = (total % 60).toString().padLeft(2, '0');
  return '$hh:$mm';
}
```
