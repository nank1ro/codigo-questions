---
language: dart
exerciseType: 1
difficulty: 2
title: 二分查找
---

# --description--

二分查找通过不断将查找范围对半分，在**有序**集合中查找某个值：查看中间的元素，如果它不是你要找的那个元素，当目标较小时就在左半部分继续查找，当目标较大时就在右半部分继续查找。

由于每一步都会丢弃剩余元素的一半，即使面对非常庞大的集合，二分查找也只需寥寥几次比较就能得到答案；而逐个检查元素所需的步骤数则与元素数量一样多。

# --instructions--

编写一个函数 `binarySearch`，它接受一个按升序排列的整数列表和一个目标整数，并返回目标在列表中的索引，当目标不存在时返回 `-1`。

列表中绝不会包含重复元素，因此索引始终是唯一的。列表也可能为空。你的函数必须使用二分查找，在每一步都将查找范围对半分，而不是进行线性扫描。

函数调用示例：
```dart
print(binarySearch([1, 3, 5, 7], 5));
// prints 2
```

# --seed--

```dart
int binarySearch() {

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

在空列表中查找必须返回 -1

```dart
  test('test1', () {
    expect(binarySearch([], 7), -1, reason: '--err-t1--');
  });
```

在 `[5]` 中查找 5 必须返回 0

```dart
  test('test2', () {
    expect(binarySearch([5], 5), 0, reason: '--err-t2--');
  });
```

在 `[5]` 中查找 9 必须返回 -1

```dart
  test('test3', () {
    expect(binarySearch([5], 9), -1, reason: '--err-t3--');
  });
```

12 个元素的列表中，第一个元素 -9 必须能在索引 0 处找到

```dart
  test('test4', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, reason: '--err-t4--');
  });
```

12 个元素的列表中，最后一个元素 78 必须能在索引 11 处找到

```dart
  test('test5', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, reason: '--err-t5--');
  });
```

元素 15 必须能在索引 6 处找到

```dart
  test('test6', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, reason: '--err-t6--');
  });
```

元素 22 必须能在索引 7 处找到

```dart
  test('test7', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, reason: '--err-t7--');
  });
```

介于 11 和 15 之间的值 12 必须返回 -1

```dart
  test('test8', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, reason: '--err-t8--');
  });
```

比所有元素都小的目标必须返回 -1

```dart
  test('test9', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, reason: '--err-t9--');
  });
```

比所有元素都大的目标必须返回 -1

```dart
  test('test10', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100), -1, reason: '--err-t10--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int binarySearch(List<int> arr, int target) {
  var low = 0;
  var high = arr.length - 1;
  while (low <= high) {
    final mid = low + (high - low) ~/ 2;
    if (arr[mid] == target) {
      return mid;
    }
    if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return -1;
}
```
