---
language: dart
exerciseType: 1
difficulty: 1
title: Odległość Hamminga
---

# --description--

DNA zapisuje się jako nić nukleotydów, z których każdy jest pojedynczą literą: `A`, `C`, `G` lub `T`. Gdy dwie nici o tej samej długości ustawimy obok siebie, niektóre pozycje mają ten sam nukleotyd, a niektóre różne.

Liczba pozycji, w których dwie nici różnią się między sobą, nazywana jest odległością Hamminga, a biolodzy używają jej do mierzenia, jak bardzo dwie nici się od siebie oddaliły. Ustawienie `GAGCCTACTAACGGGAT` obok `CATCGTAATGACGGCCT` daje 7 różniących się pozycji, więc ich odległość Hamminga wynosi 7.

# --instructions--

Napisz funkcję `hammingDistance`, która przyjmuje dwie nici DNA o tej samej długości i zwraca liczbę pozycji, w których się różnią.

Przykłady:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- Obie nici zawsze mają tę samą długość, więc nigdy nie musisz obsługiwać nici o różnych długościach.
- Dwie puste nici nie różnią się nigdzie, więc ich odległość wynosi 0.

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

Dwie puste nici nie różnią się nigdzie

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

Dwie identyczne nici z pojedynczym nukleotydem nie mają żadnej różnicy

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

Dwie różne nici z pojedynczym nukleotydem różnią się w jednej pozycji

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

Dwie krótkie nici różniące się w każdej pozycji

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

Dwie krótkie nici różniące się tylko w pierwszej pozycji

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

Pojedynczy różniący się nukleotyd w środku nici

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

Te same nukleotydy w różnych pozycjach nadal liczą się jako różnice

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

Dłuższa para nici z czterema różnicami

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

Przesunięcie nici o jedną pozycję powoduje, że prawie każda pozycja się różni

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

Dwie nici z opisu mają odległość równą siedem

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
