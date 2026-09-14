---
language: dart
exerciseType: 1
difficulty: 2
title: Binary search
---

# --description--

Binary search finds a value inside a **sorted** collection by repeatedly halving the search range: look at the element in the middle, and if it is not the one you want, continue in the left half when the target is smaller or in the right half when the target is larger.

Because every step throws away half of the remaining elements, binary search reaches the answer in a handful of comparisons even on very large collections, while checking the elements one by one would cost as many steps as there are elements.

# --instructions--

Write a function `binarySearch` that takes a list of integers sorted in ascending order and a target integer, and returns the index of the target inside the list, or `-1` when the target is not present.

The list never contains duplicates, so the index is always unique. The list can also be empty. Your function must use binary search, halving the search range at every step, not a linear scan.

Example of function call:
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

Searching in an empty list must return -1

```dart
  test('test1', () {
    expect(binarySearch([], 7), -1, reason: '--err-t1--');
  });
```

Searching for 5 in `[5]` must return 0

```dart
  test('test2', () {
    expect(binarySearch([5], 5), 0, reason: '--err-t2--');
  });
```

Searching for 9 in `[5]` must return -1

```dart
  test('test3', () {
    expect(binarySearch([5], 9), -1, reason: '--err-t3--');
  });
```

The first element -9 of the 12 element list must be found at index 0

```dart
  test('test4', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, reason: '--err-t4--');
  });
```

The last element 78 of the 12 element list must be found at index 11

```dart
  test('test5', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, reason: '--err-t5--');
  });
```

The element 15 must be found at index 6

```dart
  test('test6', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, reason: '--err-t6--');
  });
```

The element 22 must be found at index 7

```dart
  test('test7', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, reason: '--err-t7--');
  });
```

The value 12, which sits between 11 and 15, must return -1

```dart
  test('test8', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, reason: '--err-t8--');
  });
```

A target smaller than every element must return -1

```dart
  test('test9', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, reason: '--err-t9--');
  });
```

A target larger than every element must return -1

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
