---
language: dart
exerciseType: 1
difficulty: 1
title: 100개의 문
---

# --description--

일렬로 100개의 문이 있으며, 모두 처음에는 닫혀 있습니다.
100번의 통과를 합니다.
첫 번째 통과에서는 모든 문을 방문하여 '토글'합니다 (문이 닫혀 있으면 열고, 열려 있으면 닫습니다).
두 번째 통과에서는 2번째 문마다 (즉, 2번, 4번, 6번, ...) 방문하여 토글합니다.
세 번째 통과에서는 3번째 문마다 (즉, 3번, 6번, 9번, ...) 방문하며, 이를 100번째 문만 방문할 때까지 계속합니다.

# --instructions--

마지막 통과 후 문의 상태를 결정하는 함수를 구현하십시오.
열려 있는 문의 번호만 배열에 포함하여 최종 결과를 반환하십시오.
> 이 메서드는 가변적인 수의 문에 대해 동작할 수 있어야 합니다.

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

100개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

```dart
    test("test1", () {
      const solution1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

      expect(getFinalOpenedDoors(100), solution1, reason: "--err-t1--");
    });
```

10개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

```dart
    test("test2", () {
      const solution2 = [1, 4, 9];
      expect(getFinalOpenedDoors(10), solution2, reason: "--err-t2--");
    });
```

950개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

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
