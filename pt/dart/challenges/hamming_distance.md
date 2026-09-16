---
language: dart
exerciseType: 1
difficulty: 1
title: Distância de Hamming
---

# --description--

O DNA é escrito como uma fita de nucleotídeos, cada um representado por uma única letra: `A`, `C`, `G` ou `T`. Quando duas fitas de mesmo comprimento são alinhadas lado a lado, algumas posições contêm o mesmo nucleotídeo e outras contêm nucleotídeos diferentes.

O número de posições em que as duas fitas diferem é chamado de distância de Hamming, e biólogos o usam para medir o quanto duas fitas se afastaram uma da outra. Alinhar `GAGCCTACTAACGGGAT` com `CATCGTAATGACGGCCT` resulta em 7 posições que diferem, de modo que a distância de Hamming entre elas é 7.

# --instructions--

Escreva uma função `hammingDistance` que recebe duas fitas de DNA de mesmo comprimento e retorna o número de posições em que elas diferem.

Exemplos:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- As duas fitas sempre têm o mesmo comprimento, então você nunca precisa lidar com fitas de comprimentos diferentes.
- Duas fitas vazias não diferem em nenhuma posição, então a distância entre elas é 0.

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

Duas fitas vazias não diferem em nenhuma posição

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

Duas fitas idênticas de um único nucleotídeo não têm nenhuma diferença

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

Duas fitas diferentes de um único nucleotídeo diferem em uma posição

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

Duas fitas curtas que diferem em todas as posições

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

Duas fitas curtas que diferem apenas na primeira posição

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

Um único nucleotídeo diferente no meio das fitas

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

Os mesmos nucleotídeos em posições diferentes ainda contam como diferenças

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

Um par de fitas mais longo com quatro diferenças

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

Deslocar uma fita em uma posição faz quase todas as posições diferirem

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

As duas fitas da descrição têm uma distância de sete

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
