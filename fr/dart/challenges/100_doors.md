---
language: dart
exerciseType: 1
difficulty: 1
title: 100 portes
---

# --description--

Il y a 100 portes d'affilée qui sont toutes initialement fermées.
Vous faites 100 passages aux portes.
La première fois, visitez chaque porte et 'basculez' la porte (si la porte est fermée, ouvrez-la ; si elle est ouverte, fermez-la).
La deuxième fois, ne visitez que chaque 2ème porte (c.-à-d., porte #2, #4, #6, ...) et basculez-la.
La troisième fois, visitez chaque 3ème porte (c.-à-d., porte #3, #6, #9, ...), etc., jusqu'à ce que vous ne visitiez que la 100ème porte.

# --instructions--

Implémentez une fonction pour déterminer l'état des portes après le dernier passage.
Retournez le résultat final dans un tableau, avec seulement le numéro de la porte inclus dans le tableau s'il est ouvert.
> La méthode doit être capable de travailler avec un nombre variable de portes.

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

Étant donné 100 portes, retournez la liste correcte des portes ouvertes

```dart
    test("test1", () {
      const solution1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

      expect(getFinalOpenedDoors(100), solution1, reason: "--err-t1--");
    });
```

Étant donné 10 portes, retournez la liste correcte des portes ouvertes

```dart
    test("test2", () {
      const solution2 = [1, 4, 9];
      expect(getFinalOpenedDoors(10), solution2, reason: "--err-t2--");
    });
```

Étant donné 950 portes, retournez la liste correcte des portes ouvertes

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
