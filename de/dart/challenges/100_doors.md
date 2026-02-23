---
language: dart
exerciseType: 1
difficulty: 1
title: 100 doors
---

# --description--

Es gibt 100 Turen in einer Reihe, die alle anfangs geschlossen sind.
Sie machen 100 Vorbeigange an den Turen.
Beim ersten Mal besuchen Sie jede Tur und 'schalten' sie um (wenn die Tur geschlossen ist, offnen Sie sie; wenn sie offen ist, schlieen Sie sie).
Beim zweiten Mal besuchen Sie nur jede 2. Tur (d. h. Tur #2, #4, #6, ...) und schalten sie um.
Beim dritten Mal besuchen Sie jede 3. Tur (d. h. Tur #3, #6, #9, ...), usw., bis Sie nur die 100. Tur besuchen.

# --instructions--

Implementieren Sie eine Funktion, um den Zustand der Turen nach dem letzten Durchgang zu bestimmen.
Geben Sie das Endergebnis in einem Array zuruck, wobei nur die Turnummer in das Array aufgenommen wird, wenn sie offen ist.
> Die Methode muss in der Lage sein, mit einer variablen Anzahl von Turen zu arbeiten.

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

Gegeben 100 Turen, geben Sie die korrekte Liste der offenen Turen zuruck

```dart
    test("test1", () {
      const solution1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

      expect(getFinalOpenedDoors(100), solution1, reason: "--err-t1--");
    });
```

Gegeben 10 Turen, geben Sie die korrekte Liste der offenen Turen zuruck

```dart
    test("test2", () {
      const solution2 = [1, 4, 9];
      expect(getFinalOpenedDoors(10), solution2, reason: "--err-t2--");
    });
```

Gegeben 950 Turen, geben Sie die korrekte Liste der offenen Turen zuruck

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
