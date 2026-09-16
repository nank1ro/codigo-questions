---
language: dart
exerciseType: 1
difficulty: 1
title: Distanza di Hamming
---

# --description--

Il DNA è scritto come un filamento di nucleotidi, ognuno dei quali è una singola lettera: `A`, `C`, `G` o `T`. Quando due filamenti della stessa lunghezza vengono affiancati, alcune posizioni contengono lo stesso nucleotide e altre ne contengono di diversi.

Il numero di posizioni in cui i due filamenti differiscono è chiamato distanza di Hamming, e i biologi lo usano per misurare quanto due filamenti si sono allontanati l'uno dall'altro. Affiancando `GAGCCTACTAACGGGAT` con `CATCGTAATGACGGCCT` si ottengono 7 posizioni che differiscono, quindi la loro distanza di Hamming è 7.

# --instructions--

Scrivi una funzione `hammingDistance` che riceve due filamenti di DNA della stessa lunghezza e restituisce il numero di posizioni in cui differiscono.

Esempi:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- I due filamenti hanno sempre la stessa lunghezza, quindi non devi mai gestire filamenti di lunghezza diversa.
- Due filamenti vuoti non differiscono in nessuna posizione, quindi la loro distanza è 0.

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

Due filamenti vuoti non differiscono in nessuna posizione

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

Due filamenti identici di un solo nucleotide non hanno differenze

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

Due filamenti di un solo nucleotide diversi differiscono in una posizione

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

Due filamenti brevi che differiscono in ogni posizione

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

Due filamenti brevi che differiscono solo nella prima posizione

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

Un singolo nucleotide diverso nel mezzo dei filamenti

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

Gli stessi nucleotidi in posizioni diverse contano comunque come differenze

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

Una coppia di filamenti più lunga con quattro differenze

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

Spostare un filamento di una posizione fa differire quasi ogni posizione

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

I due filamenti della descrizione hanno una distanza di sette

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
