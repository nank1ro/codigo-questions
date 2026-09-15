---
language: dart
exerciseType: 1
difficulty: 2
title: バブルソート
---

# --description--

バブルソートは最も単純なソートアルゴリズムの一つです。リストを順に見ていき、隣り合う要素のペアを比較し、順序が間違っているたびにそれらを交換します。完全な走査が終わるたびに残りの中で最大の値が最終的な位置まで「浮かび上がり」、一度も交換が起きずに走査が終わった時点でリストはソートされています。

# --instructions--

`List<int>`を受け取り、同じ値を昇順にソートした**新しい**リストを返す`bubbleSort`という関数を書いてください。渡されたリストを変更してはいけません。

バブルソートのアルゴリズムは自分で実装し、隣り合う要素を比較して交換してください。標準ライブラリのソート関数は使わないでください。

関数は空の配列、要素が1つだけの配列、すでにソート済みの配列、重複した値、負の数でも動作しなければなりません。

関数呼び出しの例:
```dart
print(bubbleSort([3, 1, 2]));
// 出力: [1, 2, 3]
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

空の配列は空の配列を返さなければなりません

```dart
    test("test1", () {
      expect(bubbleSort([]), [], reason: "--err-t1--");
    });
```

要素が1つだけの配列はそのままでなければなりません

```dart
    test("test2", () {
      expect(bubbleSort([42]), [42], reason: "--err-t2--");
    });
```

すでにソート済みの配列は同じ順序のままでなければなりません

```dart
    test("test3", () {
      expect(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], reason: "--err-t3--");
    });
```

逆順にソートされた配列は昇順に並べ替えられなければなりません

```dart
    test("test4", () {
      expect(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], reason: "--err-t4--");
    });
```

重複した値はすべて保持されなければなりません

```dart
    test("test5", () {
      expect(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], reason: "--err-t5--");
    });
```

負の数は正の数より前にソートされなければなりません

```dart
    test("test6", () {
      expect(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], reason: "--err-t6--");
    });
```

より長い混在した配列は昇順にソートされなければなりません

```dart
    test("test7", () {
      expect(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], reason: "--err-t7--");
    });
```

渡されたリストを変更してはいけません

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
