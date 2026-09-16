---
language: dart
exerciseType: 1
difficulty: 1
title: Расстояние Хэмминга
---

# --description--

ДНК записывается в виде цепочки нуклеотидов, каждый из которых обозначается одной буквой: `A`, `C`, `G` или `T`. Когда две цепочки одинаковой длины располагаются рядом друг с другом, в одних позициях стоит один и тот же нуклеотид, а в других — разные.

Количество позиций, в которых две цепочки различаются, называется расстоянием Хэмминга, и биологи используют его, чтобы измерить, насколько далеко две цепочки разошлись друг от друга. Если сопоставить `GAGCCTACTAACGGGAT` с `CATCGTAATGACGGCCT`, различающихся позиций окажется 7, поэтому их расстояние Хэмминга равно 7.

# --instructions--

Напишите функцию `hammingDistance`, которая принимает две цепочки ДНК одинаковой длины и возвращает количество позиций, в которых они различаются.

Примеры:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- У цепочек всегда одинаковая длина, поэтому обрабатывать цепочки разной длины не придётся.
- Две пустые цепочки не различаются нигде, поэтому их расстояние равно 0.

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

Две пустые цепочки не различаются нигде

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

Две одинаковые цепочки из одного нуклеотида не имеют различий

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

Две разные цепочки из одного нуклеотида различаются в одной позиции

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

Две короткие цепочки, различающиеся в каждой позиции

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

Две короткие цепочки, различающиеся только в первой позиции

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

Один различающийся нуклеотид в середине цепочек

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

Одинаковые нуклеотиды в разных позициях всё равно считаются различиями

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

Более длинная пара цепочек с четырьмя различиями

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

Сдвиг цепочки на одну позицию делает почти каждую позицию различающейся

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

Две цепочки из описания имеют расстояние семь

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
