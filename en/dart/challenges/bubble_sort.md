---
language: dart
exerciseType: 1
difficulty: 2
title: Bubble sort
---

# --description--

Bubble sort is one of the simplest sorting algorithms. It walks through a list and compares each pair of adjacent items, swapping them whenever they are in the wrong order. After each full pass the largest remaining value has "bubbled" up to its final position, and the list is sorted as soon as a pass finishes without a single swap.

# --instructions--

Write a function called `bubbleSort` that takes a `List<int>` and returns a **new** list with the same values sorted into ascending order. The list that is passed in must not be modified.

You must implement the bubble sort algorithm yourself, comparing and swapping adjacent items. Do not use a sorting function from the standard library.

Your function must also work with an empty array, an array with a single element, an array that is already sorted, repeated values and negative numbers.

Example of function call:
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

An empty array must return an empty array

```dart
    test("test1", () {
      expect(bubbleSort([]), [], reason: "--err-t1--");
    });
```

An array with a single element must stay the same

```dart
    test("test2", () {
      expect(bubbleSort([42]), [42], reason: "--err-t2--");
    });
```

An already sorted array must stay in the same order

```dart
    test("test3", () {
      expect(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], reason: "--err-t3--");
    });
```

A reverse sorted array must be turned into ascending order

```dart
    test("test4", () {
      expect(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], reason: "--err-t4--");
    });
```

Repeated values must all be kept

```dart
    test("test5", () {
      expect(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], reason: "--err-t5--");
    });
```

Negative numbers must be sorted before the positive ones

```dart
    test("test6", () {
      expect(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], reason: "--err-t6--");
    });
```

A longer mixed array must be sorted in ascending order

```dart
    test("test7", () {
      expect(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], reason: "--err-t7--");
    });
```

The list that is passed in must not be modified

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
