---
language: dart
exerciseType: 1
difficulty: 1
title: Distance de Hamming
---

# --description--

L'ADN s'écrit sous la forme d'un brin de nucléotides, chacun étant une seule lettre : `A`, `C`, `G` ou `T`. Lorsque deux brins de même longueur sont alignés côte à côte, certaines positions portent le même nucléotide et d'autres un nucléotide différent.

Le nombre de positions où les deux brins diffèrent s'appelle la distance de Hamming, et les biologistes l'utilisent pour mesurer à quel point deux brins ont divergé. L'alignement de `GAGCCTACTAACGGGAT` avec `CATCGTAATGACGGCCT` donne 7 positions différentes, leur distance de Hamming est donc 7.

# --instructions--

Écrivez une fonction `hammingDistance` qui prend deux brins d'ADN de même longueur et retourne le nombre de positions où ils diffèrent.

Exemples :
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- Les deux brins ont toujours la même longueur, vous n'avez donc jamais à gérer des brins de longueurs différentes.
- Deux brins vides ne diffèrent nulle part, leur distance est donc 0.

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

Deux brins vides ne diffèrent nulle part

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

Deux brins identiques d'un seul nucléotide n'ont aucune différence

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

Deux brins d'un seul nucléotide différents diffèrent en une position

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

Deux brins courts qui diffèrent à chaque position

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

Deux brins courts qui ne diffèrent qu'à la première position

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

Un seul nucléotide différent au milieu des brins

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

Les mêmes nucléotides à des positions différentes comptent quand même comme des différences

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

Une paire de brins plus longue avec quatre différences

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

Décaler un brin d'une position fait différer presque toutes les positions

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

Les deux brins de la description ont une distance de sept

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
