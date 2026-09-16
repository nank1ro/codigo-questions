---
language: dart
exerciseType: 1
difficulty: 1
title: Distancia de Hamming
---

# --description--

El ADN se escribe como una hebra de nucleótidos, cada uno una sola letra: `A`, `C`, `G` o `T`. Cuando dos hebras de la misma longitud se alinean una junto a la otra, algunas posiciones contienen el mismo nucleótido y otras contienen uno diferente.

El número de posiciones en las que las dos hebras difieren se llama distancia de Hamming, y los biólogos la usan para medir cuán lejos han divergido dos hebras. Alinear `GAGCCTACTAACGGGAT` con `CATCGTAATGACGGCCT` da 7 posiciones que difieren, así que su distancia de Hamming es 7.

# --instructions--

Escribe una función `hammingDistance` que reciba dos hebras de ADN de la misma longitud y devuelva el número de posiciones en las que difieren.

Ejemplos:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- Las dos hebras siempre tienen la misma longitud, así que nunca tienes que manejar hebras de longitudes diferentes.
- Dos hebras vacías no difieren en ninguna posición, así que su distancia es 0.

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

Dos hebras vacías no difieren en ninguna posición

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

Dos hebras de un solo nucleótido idénticas no tienen ninguna diferencia

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

Dos hebras de un solo nucleótido diferente difieren en una posición

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

Dos hebras cortas que difieren en todas las posiciones

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

Dos hebras cortas que difieren solo en la primera posición

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

Un único nucleótido diferente en medio de las hebras

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

Los mismos nucleótidos en posiciones diferentes siguen contando como diferencias

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

Un par de hebras más largo con cuatro diferencias

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

Desplazar una hebra una posición hace que casi todas las posiciones difieran

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

Las dos hebras de la descripción tienen una distancia de siete

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
