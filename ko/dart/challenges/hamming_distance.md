---
language: dart
exerciseType: 1
difficulty: 1
title: 해밍 거리
---

# --description--

DNA는 각각 한 글자인 뉴클레오터드 가닥으로 표기합니다: `A`, `C`, `G` 또는 `T`. 같은 길이의 두 가닥을 나란히 놓으면 어떤 위치에는 같은 뉴클레오터드가 있고 어떤 위치에는 다른 뉴클레오터드가 있습니다.

두 가닥이 서로 다른 위치의 개수를 해밍 거리라고 하며, 생물학자들은 이를 이용해 두 가닥이 얼마나 멀어졌는지 측정합니다. `GAGCCTACTAACGGGAT`를 `CATCGTAATGACGGCCT`와 나란히 놓으면 서로 다른 위치가 7개이므로 두 가닥의 해밍 거리는 7입니다.

# --instructions--

같은 길이의 두 DNA 가닥을 받아 서로 다른 위치의 개수를 반환하는 함수 `hammingDistance`를 작성하세요.

예시:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- 두 가닥은 항상 길이가 같으므로 길이가 다른 가닥을 처리할 필요는 없습니다.
- 두 빈 가닥은 어디에서도 다르지 않으므로 거리는 0입니다.

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

두 빈 가닥은 어디에서도 다르지 않습니다

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

같은 뉴클레오터드 하나를 가진 두 가닥에는 차이가 없습니다

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

다른 뉴클레오터드 하나를 가진 두 가닥은 한 위치에서 다릅니다

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

모든 위치에서 다른 두 짧은 가닥

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

첫 번째 위치에서만 다른 두 짧은 가닥

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

가닥 중간에 하나의 다른 뉴클레오터드

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

위치가 다른 같은 뉴클레오터드도 차이로 계산됩니다

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

네 군데가 다른 더 긴 가닥 쌍

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

가닥을 한 칸 밀면 거의 모든 위치가 달라집니다

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

설명에 나온 두 가닥의 거리는 7입니다

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
