---
language: dart
exerciseType: 1
difficulty: 1
title: 100 Türen
---

# --description--

Es gibt 100 Türen in einer Reihe, die alle ursprünglich geschlossen sind.
Sie machen 100 Durchgänge an den Türen.
Beim ersten Mal besuchen Sie alle Türen und schalten sie um (wenn die Tür geschlossen ist, öffnen Sie sie; wenn sie offen ist, schließen Sie sie).
Beim zweiten Mal besuchen Sie nur jede 2. Tür (z.B. Tür #2, #4, #6, ...) und schalten sie um.
Beim dritten Mal besuchen Sie alle 3. Türen (z.B. Tür #3, #6, #9, ...), und so weiter, bis Sie nur noch die 100. Tür besuchen.

# --instructions--

Implementieren Sie eine Funktion, um den Zustand der Türen nach dem letzten Durchgang zu bestimmen.
Geben Sie das Endergebnis in einem Array zurück, mit nur der Türnummer im Array, wenn sie offen ist.
> Die Methode muss mit einer variablen Anzahl von Türen funktionieren.

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

Bei 100 Türen die richtige Liste offener Türen zurückgeben

```dart
    test("test1", () {
      const solution1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

      expect(getFinalOpenedDoors(100), solution1, reason: "--err-t1--");
    });
```

Bei 10 Türen die richtige Liste offener Türen zurückgeben

```dart
    test("test2", () {
      const solution2 = [1, 4, 9];
      expect(getFinalOpenedDoors(10), solution2, reason: "--err-t2--");
    });
```

Bei 950 Türen die richtige Liste offener Türen zurückgeben

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
