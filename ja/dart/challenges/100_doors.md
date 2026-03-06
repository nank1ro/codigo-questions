---
language: dart
exerciseType: 1
difficulty: 1
title: 100のドア
---

# --description--

一列に並んだ100枚のドアがあり、すべて最初は閉じています。
あなたはドアの前を100回通過します。
1回目は、すべてのドアを訪れてドアを「切り替え」ます（ドアが閉じていれば開け、開いていれば閉じます）。
2回目は、2番目ごとのドア（つまり、ドア#2、#4、#6、...）だけを訪れて切り替えます。
3回目は、3番目ごとのドア（つまり、ドア#3、#6、#9、...）を訪れます。これを100番目のドアだけを訪れるまで続けます。

# --instructions--

最後の通過後のドアの状態を判定する関数を実装してください。
開いているドアの番号のみを含む配列で最終結果を返してください。
> このメソッドは可変数のドアで動作できなければなりません。

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

100枚のドアが与えられた場合、開いているドアの正しいリストを返す

```dart
    test("test1", () {
      const solution1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

      expect(getFinalOpenedDoors(100), solution1, reason: "--err-t1--");
    });
```

10枚のドアが与えられた場合、開いているドアの正しいリストを返す

```dart
    test("test2", () {
      const solution2 = [1, 4, 9];
      expect(getFinalOpenedDoors(10), solution2, reason: "--err-t2--");
    });
```

950枚のドアが与えられた場合、開いているドアの正しいリストを返す

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
