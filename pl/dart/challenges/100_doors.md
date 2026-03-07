---
language: dart
exerciseType: 1
difficulty: 1
title: 100 doors
---

# --description--

W rzędzie stoi 100 drzwi, wszystkie początkowo zamknięte.
Wykonujesz 100 przejść obok drzwi.
Za pierwszym razem odwiedzasz każde drzwi i „przełączasz" je (jeśli drzwi są zamknięte, otwierasz je; jeśli są otwarte, zamykasz je).
Za drugim razem odwiedzasz tylko co 2. drzwi (czyli drzwi nr 2, 4, 6, ...) i przełączasz je.
Za trzecim razem odwiedzasz co 3. drzwi (czyli drzwi nr 3, 6, 9, ...) itd., aż do momentu, gdy odwiedzasz tylko 100. drzwi.

# --instructions--

Zaimplementuj funkcję, która określa stan drzwi po ostatnim przejściu.
Zwróć końcowy wynik jako tablicę, zawierającą tylko numery drzwi, które są otwarte.
> Metoda musi działać dla zmiennej liczby drzwi.

# --seed--

```dart
import 'dart:math';

List<int> getFinalOpenedDoors(numDoors: Int) {
    
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

Dla 100 drzwi zwróć poprawną listę otwartych drzwi

```dart
    test("test1", () {
      const solution1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

      expect(getFinalOpenedDoors(100), solution1, reason: "--err-t1--");
    });
```

Dla 10 drzwi zwróć poprawną listę otwartych drzwi

```dart
    test("test2", () {
      const solution2 = [1, 4, 9];
      expect(getFinalOpenedDoors(10), solution2, reason: "--err-t2--");
    });
```

Dla 950 drzwi zwróć poprawną listę otwartych drzwi

```dart
    test("test3", () {
      const solution3 = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900];
      expect(getFinalOpenedDoors(950), solution3, reason: "--err-t3--");
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
import 'dart:math';

int square(int number) => pow(number.toDouble(), 2.0).toInt();

List<int> getFinalOpenedDoors(int numDoors) {
    final openDoors = <int>[];
    var i = 1;
    while (square(i) <= numDoors) {
        openDoors.add(square(i));
        i += 1;
    }
    return openDoors;
}
```
