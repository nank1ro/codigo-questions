---
language: dart
exerciseType: 1
difficulty: 1
title: Hamming distance
---

# --description--

DNA is written as a strand of nucleotides, each one a single letter: `A`, `C`, `G` or `T`. When two strands of the same length are lined up side by side, some positions hold the same nucleotide and some hold different ones.

The number of positions where the two strands differ is called the Hamming distance, and biologists use it to measure how far two strands have drifted apart. Lining up `GAGCCTACTAACGGGAT` with `CATCGTAATGACGGCCT` gives 7 positions that differ, so their Hamming distance is 7.

# --instructions--

Write a function `hammingDistance` that takes two DNA strands of the same length and returns the number of positions where they differ.

Examples:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- The two strands always have the same length, so you never have to handle strands of different lengths.
- Two empty strands differ nowhere, so their distance is 0.

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

Two empty strands differ nowhere

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

Two identical single nucleotide strands have no difference

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

Two different single nucleotide strands differ in one position

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

Two short strands that differ in every position

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

Two short strands that differ in the first position only

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

A single differing nucleotide in the middle of the strands

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

The same nucleotides in different positions still count as differences

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

A longer pair of strands with four differences

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

Shifting a strand by one position makes almost every position differ

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

The two strands from the description have a distance of seven

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
