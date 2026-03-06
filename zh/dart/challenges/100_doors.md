---
language: dart
exerciseType: 1
difficulty: 1
title: 100扇门
---

# --description--

有 100 扇门排成一行，最初全部关闭。
你经过这些门 100 次。
第一次经过时，访问每扇门并"切换"门的状态（如果门是关闭的，就打开它；如果门是打开的，就关闭它）。
第二次，只访问每第 2 扇门（即第 2、4、6 号门……）并切换状态。
第三次，访问每第 3 扇门（即第 3、6、9 号门……），依此类推，直到你只访问第 100 扇门。

# --instructions--

实现一个函数来确定最后一次经过后门的状态。
将最终结果以数组形式返回，数组中只包含处于打开状态的门的编号。
> 该方法必须能够处理可变数量的门。

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

给定 100 扇门，返回正确的打开门列表

```dart
    test("test1", () {
      const solution1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

      expect(getFinalOpenedDoors(100), solution1, reason: "--err-t1--");
    });
```

给定 10 扇门，返回正确的打开门列表

```dart
    test("test2", () {
      const solution2 = [1, 4, 9];
      expect(getFinalOpenedDoors(10), solution2, reason: "--err-t2--");
    });
```

给定 950 扇门，返回正确的打开门列表

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
