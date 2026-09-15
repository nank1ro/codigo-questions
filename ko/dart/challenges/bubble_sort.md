---
language: dart
exerciseType: 1
difficulty: 2
title: 버블 정렬
---

# --description--

버블 정렬은 가장 단순한 정렬 알고리즘 중 하나입니다. 리스트를 순회하면서 인접한 두 항목을 비교하고, 순서가 잘못되어 있을 때마다 서로 교환합니다. 한 번의 전체 순회가 끝날 때마다 남은 값 중 가장 큰 값이 최종 위치로 「떠오르며」, 한 번의 순회에서 교환이 한 번도 일어나지 않으면 리스트는 정렬이 완료된 것입니다.

# --instructions--

`List<int>`를 받아 같은 값들을 오름차순으로 정렬한 **새로운** 리스트를 반환하는 `bubbleSort`라는 함수를 작성하세요. 전달된 리스트는 수정되어서는 안 됩니다.

인접한 항목을 비교하고 교환하면서 버블 정렬 알고리즘을 직접 구현해야 합니다. 표준 라이브러리의 정렬 함수를 사용하지 마세요.

함수는 빈 배열, 원소가 하나뿐인 배열, 이미 정렬된 배열, 중복된 값과 음수에서도 동작해야 합니다.

함수 호출 예시:
```dart
print(bubbleSort([3, 1, 2]));
// 출력: [1, 2, 3]
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

빈 배열은 빈 배열을 반환해야 합니다

```dart
    test("test1", () {
      expect(bubbleSort([]), [], reason: "--err-t1--");
    });
```

원소가 하나뿐인 배열은 그대로 유지되어야 합니다

```dart
    test("test2", () {
      expect(bubbleSort([42]), [42], reason: "--err-t2--");
    });
```

이미 정렬된 배열은 같은 순서를 유지해야 합니다

```dart
    test("test3", () {
      expect(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], reason: "--err-t3--");
    });
```

역순으로 정렬된 배열은 오름차순으로 바뀌어야 합니다

```dart
    test("test4", () {
      expect(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], reason: "--err-t4--");
    });
```

중복된 값은 모두 유지되어야 합니다

```dart
    test("test5", () {
      expect(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], reason: "--err-t5--");
    });
```

음수는 양수보다 앞에 정렬되어야 합니다

```dart
    test("test6", () {
      expect(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], reason: "--err-t6--");
    });
```

더 긴 혼합 배열은 오름차순으로 정렬되어야 합니다

```dart
    test("test7", () {
      expect(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], reason: "--err-t7--");
    });
```

전달된 리스트는 수정되어서는 안 됩니다

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
