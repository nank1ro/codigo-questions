---
language: dart
exerciseType: 1
difficulty: 1
title: Hamming-Abstand
---

# --description--

DNA wird als Strang von Nukleotiden geschrieben, jedes davon ein einzelner Buchstabe: `A`, `C`, `G` oder `T`. Werden zwei Stränge gleicher Länge Seite an Seite ausgerichtet, enthalten einige Positionen dasselbe Nukleotid und andere unterschiedliche.

Die Anzahl der Positionen, an denen sich die beiden Stränge unterscheiden, wird Hamming-Abstand genannt, und Biologen nutzen sie, um zu messen, wie weit zwei Stränge auseinandergegangen sind. Richtet man `GAGCCTACTAACGGGAT` mit `CATCGTAATGACGGCCT` aus, ergeben sich 7 Positionen mit Unterschieden, ihr Hamming-Abstand ist also 7.

# --instructions--

Schreiben Sie eine Funktion `hammingDistance`, die zwei DNA-Stränge gleicher Länge entgegennimmt und die Anzahl der Positionen zurückgibt, an denen sie sich unterscheiden.

Beispiele:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- Die beiden Stränge haben immer die gleiche Länge, Sie müssen also niemals Stränge unterschiedlicher Länge behandeln.
- Zwei leere Stränge unterscheiden sich nirgends, ihr Abstand ist also 0.

# --seed--

```dart
int hammingDistance(String left, String right) {
  
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

Zwei leere Stränge unterscheiden sich nirgends

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

Zwei identische Stränge aus einem einzelnen Nukleotid haben keinen Unterschied

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

Zwei unterschiedliche Stränge aus einem einzelnen Nukleotid unterscheiden sich an einer Position

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

Zwei kurze Stränge, die sich an jeder Position unterscheiden

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

Zwei kurze Stränge, die sich nur an der ersten Position unterscheiden

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

Ein einzelnes abweichendes Nukleotid in der Mitte der Stränge

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

Dieselben Nukleotide an anderen Positionen zählen weiterhin als Unterschiede

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

Ein längeres Paar von Strängen mit vier Unterschieden

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

Das Verschieben eines Strangs um eine Position bewirkt, dass sich fast jede Position unterscheidet

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

Die beiden Stränge aus der Beschreibung haben einen Abstand von sieben

```dart
  test('test10', () {
    expect(hammingDistance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'), 7, reason: '--err-t10--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int hammingDistance(String left, String right) {
  var distance = 0;

  for (var i = 0; i < left.length; i++) {
    if (left[i] != right[i]) {
      distance++;
    }
  }

  return distance;
}
```