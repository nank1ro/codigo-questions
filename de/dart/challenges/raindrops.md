---
language: dart
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Ihre Aufgabe ist es, eine Zahl in einen String umzuwandeln, der Regenpfropfgerausche enthalt, die bestimmten potenziellen Faktoren entsprechen.
Ein Faktor ist eine Zahl, die eine andere Zahl gleichmig teilt, ohne einen Rest zu hinterlassen.
Die einfachste Methode zu testen, ob eine Zahl ein Faktor einer anderen ist, ist die Verwendung der Modulo-Operation.
Die Regeln fur Regenpfropfe sind, dass, wenn eine gegebene Zahl:

- 3 als Faktor hat, fugen Sie 'Pling' zum Ergebnis hinzu.
- 5 als Faktor hat, fugen Sie 'Plang' zum Ergebnis hinzu.
- 7 als Faktor hat, fugen Sie 'Plong' zum Ergebnis hinzu.
- keinen der Faktoren 3, 5 oder 7 hat, sollte das Ergebnis die Ziffern der Zahl sein.

# --instructions--

Schreiben Sie eine Funktion, die den korrekten String zuruckgibt, Beispiele:

- 28 hat 7 als Faktor, aber nicht 3 oder 5, also ware das Ergebnis `"Plong"`.
- 30 hat sowohl 3 als auch 5 als Faktoren, aber nicht 7, also ware das Ergebnis `"PlingPlang"`.
- 34 ist nicht durch 3, 5 oder 7 teilbar, also ware das Ergebnis `"34"`.

Beispiel fur einen Funktionsaufruf:
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

Das Gerausche fur 1 ist "1"

```dart
  test('test1', () {
    expect(raindrops(1), "1", reason: '--err-t1--');
  });
```

Das Gerausche fur 3 ist "Pling"

```dart
  test('test2', () {
    expect(raindrops(3), "Pling", reason: '--err-t2--');
  });
```

Das Gerausche fur 5 ist "Plang"

```dart
  test('test3', () {
    expect(raindrops(5), "Plang", reason: '--err-t3--');
  });
```

Das Gerausche fur 7 ist "Plong"

```dart
  test('test4', () {
    expect(raindrops(7), "Plong", reason: '--err-t4--');
  });
```

Das Gerausche fur 6 ist "Pling"

```dart
  test('test5', () {
    expect(raindrops(6), "Pling", reason: '--err-t5--');
  });
```

Das Gerausche fur 8 ist "8"

```dart
  test('test6', () {
    expect(raindrops(8), "8", reason: '--err-t6--');
  });
```

Das Gerausche fur 9 ist "Pling"

```dart
  test('test7', () {
    expect(raindrops(9), "Pling", reason: '--err-t7--');
  });
```

Das Gerausche fur 10 ist "Plang"

```dart
  test('test8', () {
    expect(raindrops(10), "Plang", reason: '--err-t8--');
  });
```

Das Gerausche fur 14 ist "Plong"

```dart
  test('test9', () {
    expect(raindrops(14), "Plong", reason: '--err-t9--');
  });
```

Das Gerausche fur 15 ist "PlingPlang"

```dart
  test('test10', () {
    expect(raindrops(15), "PlingPlang", reason: '--err-t10--');
  });
```

Das Gerausche fur 21 ist "PlingPlong"

```dart
  test('test11', () {
    expect(raindrops(21), "PlingPlong", reason: '--err-t11--');
  });
```

Das Gerausche fur 25 ist "Plang"

```dart
  test('test12', () {
    expect(raindrops(25), "Plang", reason: '--err-t12--');
  });
```

Das Gerausche fur 27 ist "Pling"

```dart
  test('test13', () {
    expect(raindrops(27), "Pling", reason: '--err-t13--');
  });
```

Das Gerausche fur 35 ist "PlangPlong"

```dart
  test('test14', () {
    expect(raindrops(35), "PlangPlong", reason: '--err-t14--');
  });
```

Das Gerausche fur 49 ist "Plong"

```dart
  test('test15', () {
    expect(raindrops(49), "Plong", reason: '--err-t15--');
  });
```

Das Gerausche fur 52 ist "52"

```dart
  test('test16', () {
    expect(raindrops(52), "52", reason: '--err-t16--');
  });
```

Das Gerausche fur 105 ist "PlingPlangPlong"

```dart
  test('test17', () {
    expect(raindrops(105), "PlingPlangPlong", reason: '--err-t17--');
  });
```

Das Gerausche fur 3125 ist "Plang"

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
