---
language: dart
exerciseType: 1
difficulty: 1
title: 汉明距离
---

# --description--

DNA 写成一条由核苷酸组成的链，每个核苷酸是单个字母：`A`、`C`、`G` 或 `T`。当两条等长的链并排排列时，有些位置上的核苷酸相同，有些位置上的核苷酸则不同。

两条链上不同位置的数目称为汉明距离，生物学家用它来衡量两条链已经分化得有多远。将 `GAGCCTACTAACGGGAT` 与 `CATCGTAATGACGGCCT` 并排对齐后有 7 个位置不同，因此它们的汉明距离是 7。

# --instructions--

编写一个函数 `hammingDistance`，它接收两条等长的 DNA 链，并返回它们不同位置的数目。

示例：
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- 两条链的长度总是相同的，所以你无需处理长度不同的链。
- 两条空链没有任何不同，所以它们的距离是 0。

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

两条空链没有任何不同

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

两条相同的单核苷酸链没有差异

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

两条不同的单核苷酸链在一个位置上不同

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

两条在每个位置都不同的短链

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

两条只在第一个位置不同的短链

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

链的中间有一个不同的核苷酸

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

相同核苷酸出现在不同位置也算作差异

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

一对有四个差异的较长的链

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

将一条链移动一个位置会使几乎所有位置都不同

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

描述中的两条链的距离为 7

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
