---
language: dart
exerciseType: 1
difficulty: 1
title: ハミング距離
---

# --description--

DNAはヌクレオチドがつながったストランドとして書かれ、各ヌクレオチドは`A`、`C`、`G`、`T`のいずれか1文字で表されます。同じ長さの2本のストランドを横に並べると、同じヌクレオチドがくる位置もあれば、異なるヌクレオチドがくる位置もあります。

2本のストランドが異なる位置の数はハミング距離と呼ばれ、生物学者は2本のストランドがどれほど離れているかを測るためにこれを使います。`GAGCCTACTAACGGGAT`と`CATCGTAATGACGGCCT`を並べると7つの位置が異なるので、この2つのハミング距離は7です。

# --instructions--

同じ長さの2本のDNAストランドを受け取り、異なる位置の数を返す`hammingDistance`という関数を書いてください。

例:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- 2本のストランドは常に同じ長さなので、異なる長さのストランドを扱う必要はありません。
- 2本の空のストランドはどこも異ならないため、その距離は0です。

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

2本の空のストランドはどこも異なりません

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

同じ1文字のヌクレオチドからなる2本のストランドには違いがありません

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

異なる1文字のヌクレオチドからなる2本のストランドは1つの位置で異なります

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

すべての位置で異なる2本の短いストランド

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

最初の位置だけが異なる2本の短いストランド

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

ストランドの途中にある1つの異なるヌクレオチド

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

同じヌクレオチドでも位置が異なれば違いとして数えられます

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

4つの違いがある少し長いストランドのペア

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

ストランドを1つ位置ずらすと、ほぼすべての位置が異なります

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

説明にある2本のストランドの距離は7です

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
