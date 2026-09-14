---
language: dart
exerciseType: 1
difficulty: 2
title: 二分探索
---

# --description--

二分探索は、**ソート済み**のコレクションの中から値を見つける手法で、探索範囲を繰り返し半分にしていきます。中央の要素を調べ、それが目的の値でない場合は、ターゲットがより小さければ左半分へ、より大きければ右半分へと探索を続けます。

各ステップで残りの要素の半分が捨てられるため、二分探索は非常に大きなコレクションでもわずかな比較回数で答えにたどり着けます。一方、要素を1つずつ確認する方法では、要素の数と同じステップ数がかかってしまいます。

# --instructions--

昇順にソートされた整数のリストとターゲットの整数を受け取り、リストの中のターゲットのインデックス、ターゲットが存在しない場合は`-1`を返す関数`binarySearch`を書いてください。

リストに重複は含まれないため、インデックスは常に一意です。リストが空の場合もあります。関数は線形走査ではなく、毎ステップで探索範囲を半分にしていく二分探索を使用しなければなりません。

関数呼び出しの例：
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

空のリストでの検索は-1を返す必要があります。

```dart
  test('test1', () {
    expect(binarySearch([], 7), -1, reason: '--err-t1--');
  });
```

リスト`[5]`の中で5を検索した場合、0を返す必要があります。

```dart
  test('test2', () {
    expect(binarySearch([5], 5), 0, reason: '--err-t2--');
  });
```

リスト`[5]`の中で9を検索した場合、-1を返す必要があります。

```dart
  test('test3', () {
    expect(binarySearch([5], 9), -1, reason: '--err-t3--');
  });
```

12要素のリストの最初の要素-9はインデックス0で見つかる必要があります。

```dart
  test('test4', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, reason: '--err-t4--');
  });
```

12要素のリストの最後の要素78はインデックス11で見つかる必要があります。

```dart
  test('test5', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, reason: '--err-t5--');
  });
```

要素15はインデックス6で見つかる必要があります。

```dart
  test('test6', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, reason: '--err-t6--');
  });
```

要素22はインデックス7で見つかる必要があります。

```dart
  test('test7', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, reason: '--err-t7--');
  });
```

11と15の間にある値12は-1を返す必要があります。

```dart
  test('test8', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, reason: '--err-t8--');
  });
```

すべての要素より小さいターゲットは-1を返す必要があります。

```dart
  test('test9', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, reason: '--err-t9--');
  });
```

すべての要素より大きいターゲットは-1を返す必要があります。

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
