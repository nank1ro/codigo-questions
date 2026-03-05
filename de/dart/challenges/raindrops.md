---
language: dart
exerciseType: 1
difficulty: 1
title: Regentropfen
---

# --description--

Ihre Aufgabe ist es, eine Zahl in einen String zu konvertieren, der Regentropfengeräusche entsprechend bestimmten potenziellen Faktoren enthält.
Ein Faktor ist eine Zahl, die ohne Rest in eine andere Zahl aufgeht.
Die einfachste Möglichkeit, zu überprüfen, ob eine Zahl ein Faktor einer anderen ist, ist die Modulo-Operation.
Die Regeln für Regentropfen besagen, dass wenn eine bestimmte Zahl:

- 3 als Faktor hat, fügen Sie "Pling" zum Ergebnis hinzu.
- 5 als Faktor hat, fügen Sie "Plang" zum Ergebnis hinzu.
- 7 als Faktor hat, fügen Sie "Plong" zum Ergebnis hinzu.
- nicht 3, 5 oder 7 als Faktor hat, sollte das Ergebnis die Ziffern der Zahl sein.

# --instructions--

Schreiben Sie eine Funktion, die den richtigen String zurückgibt, Beispiele:

- 28 hat 7 als Faktor, aber nicht 3 oder 5, also wäre das Ergebnis `"Plong"`.
- 30 hat sowohl 3 als auch 5 als Faktoren, aber nicht 7, also wäre das Ergebnis `"PlingPlang"`.
- 34 wird nicht durch 3, 5 oder 7 faktorisiert, also wäre das Ergebnis `"34"`.

Beispiel eines Funktionsaufrufs:
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

Der Ton für 1 ist "1"

```dart
  test('test1', () {
    expect(raindrops(1), "1", reason: '--err-t1--');
  });
```

Der Ton für 3 ist "Pling"

```dart
  test('test2', () {
    expect(raindrops(3), "Pling", reason: '--err-t2--');
  });
```

Der Ton für 5 ist "Plang"

```dart
  test('test3', () {
    expect(raindrops(5), "Plang", reason: '--err-t3--');
  });
```

Der Ton für 7 ist "Plong"

```dart
  test('test4', () {
    expect(raindrops(7), "Plong", reason: '--err-t4--');
  });
```

Der Ton für 6 ist "Pling"

```dart
  test('test5', () {
    expect(raindrops(6), "Pling", reason: '--err-t5--');
  });
```

Der Ton für 8 ist "8"

```dart
  test('test6', () {
    expect(raindrops(8), "8", reason: '--err-t6--');
  });
```

Der Ton für 9 ist "Pling"

```dart
  test('test7', () {
    expect(raindrops(9), "Pling", reason: '--err-t7--');
  });
```

Der Ton für 10 ist "Plang"

```dart
  test('test8', () {
    expect(raindrops(10), "Plang", reason: '--err-t8--');
  });
```

Der Ton für 14 ist "Plong"

```dart
  test('test9', () {
    expect(raindrops(14), "Plong", reason: '--err-t9--');
  });
```

Der Ton für 15 ist "PlingPlang"

```dart
  test('test10', () {
    expect(raindrops(15), "PlingPlang", reason: '--err-t10--');
  });
```

Der Ton für 21 ist "PlingPlong"

```dart
  test('test11', () {
    expect(raindrops(21), "PlingPlong", reason: '--err-t11--');
  });
```

Der Ton für 25 ist "Plang"

```dart
  test('test12', () {
    expect(raindrops(25), "Plang", reason: '--err-t12--');
  });
```

Der Ton für 27 ist "Pling"

```dart
  test('test13', () {
    expect(raindrops(27), "Pling", reason: '--err-t13--');
  });
```

Der Ton für 35 ist "PlangPlong"

```dart
  test('test14', () {
    expect(raindrops(35), "PlangPlong", reason: '--err-t14--');
  });
```

Der Ton für 49 ist "Plong"

```dart
  test('test15', () {
    expect(raindrops(49), "Plong", reason: '--err-t15--');
  });
```

Der Ton für 52 ist "52"

```dart
  test('test16', () {
    expect(raindrops(52), "52", reason: '--err-t16--');
  });
```

Der Ton für 105 ist "PlingPlangPlong"

```dart
  test('test17', () {
    expect(raindrops(105), "PlingPlangPlong", reason: '--err-t17--');
  });
```

Der Ton für 3125 ist "Plang"

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
