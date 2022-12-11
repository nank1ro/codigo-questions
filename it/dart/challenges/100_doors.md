---
language: dart
exerciseType: 1
difficulty: 1
title: 100 porte
---

# --description--

Ci sono 100 porte in fila che inizialmente sono tutte chiuse.
Fai 100 passaggi davanti alle porte.
La prima volta che passi, visita ogni porta e "alterna" la porta (se la porta è chiusa, aprila; se è aperta, chiudila).
La seconda volta, visita solo ogni 2a porta (cioè la porta #2, #4, #6, ...) e modificala.
La terza volta, visita ogni 3a porta (cioè la porta #3, #6, #9, ...), etc., fino a visitare solo la 100esima porta.

# --instructions--

Implementa una funzione per determinare lo stato delle porte dopo l'ultimo passaggio.
Restituire il risultato finale in un array, con solo il numero delle porte aperte.
> Il metodo deve essere in grado di funzionare con un numero variabile di porte.

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

Date 100 porte, restituire l'elenco corretto delle porte aperte

```dart
    test("test1", () {
      const solution1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

      expect(getFinalOpenedDoors(100), solution1, reason: "--err-t1--");
    });
```

Date 10 porte, restituire l'elenco corretto delle porte aperte

```dart
    test("test2", () {
      const solution2 = [1, 4, 9];
      expect(getFinalOpenedDoors(10), solution2, reason: "--err-t2--");
    });
```

Date 950 porte, restituire l'elenco corretto delle porte aperte

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
