---
language: dart
exerciseType: 1
difficulty: 2
title: 冒泡排序
---

# --description--

冒泡排序是最简单的排序算法之一。它遍历一个列表，比较每一对相邻的元素，只要它们的顺序不对就交换它们。每完成一轮完整的遍历，剩下的最大值就会“冒泡”到它的最终位置；一旦某一轮遍历没有发生任何交换，列表就已经排好序了。

# --instructions--

编写一个名为 `bubbleSort` 的函数，它接收一个 `List<int>`，并返回一个包含相同值且按升序排序的**新**列表。传入的列表不能被修改。

你必须自己实现冒泡排序算法，比较并交换相邻的元素。不要使用标准库中的排序函数。

你的函数还必须能处理空数组、只有一个元素的数组、已经排好序的数组、重复的值和负数。

函数调用示例：
```dart
print(bubbleSort([3, 1, 2]));
// prints [1, 2, 3]
```

# --seed--

```dart
List<int> bubbleSort(List<int> arr) {
    
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

空数组必须返回空数组

```dart
    test("test1", () {
      expect(bubbleSort([]), [], reason: "--err-t1--");
    });
```

只有一个元素的数组必须保持不变

```dart
    test("test2", () {
      expect(bubbleSort([42]), [42], reason: "--err-t2--");
    });
```

已经排好序的数组必须保持相同的顺序

```dart
    test("test3", () {
      expect(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], reason: "--err-t3--");
    });
```

逆序排列的数组必须变成升序

```dart
    test("test4", () {
      expect(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], reason: "--err-t4--");
    });
```

所有重复的值都必须保留

```dart
    test("test5", () {
      expect(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], reason: "--err-t5--");
    });
```

负数必须排在正数之前

```dart
    test("test6", () {
      expect(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], reason: "--err-t6--");
    });
```

更长的混合数组必须按升序排序

```dart
    test("test7", () {
      expect(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], reason: "--err-t7--");
    });
```

传入的列表不能被修改

```dart
    test("test8", () {
      final original = [3, 1, 2];
      bubbleSort(original);
      expect(original, [3, 1, 2], reason: "--err-t8--");
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
List<int> bubbleSort(List<int> arr) {
    final result = List<int>.from(arr);
    var end = result.length;
    var swapped = true;
    while (swapped) {
        swapped = false;
        for (var i = 1; i < end; i++) {
            if (result[i - 1] > result[i]) {
                final temp = result[i - 1];
                result[i - 1] = result[i];
                result[i] = temp;
                swapped = true;
            }
        }
        end--;
    }
    return result;
}
```
