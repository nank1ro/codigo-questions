---
language: swift
exerciseType: 1
difficulty: 2
title: バブルソート
---

# --description--

バブルソートは最も単純なソートアルゴリズムの一つです。リストを順に見ていき、隣り合う要素のペアを比較し、順序が間違っているたびにそれらを交換します。完全な走査が終わるたびに残りの中で最大の値が最終的な位置まで「浮かび上がり」、一度も交換が起きずに走査が終わった時点でリストはソートされています。

# --instructions--

整数の配列を受け取り、同じ値を昇順にソートした**新しい**配列を返す`bubbleSort`という関数を書いてください。渡された配列を変更してはいけません。

バブルソートのアルゴリズムは自分で実装し、隣り合う要素を比較して交換してください。標準ライブラリのソート関数は使わないでください。

関数は空の配列、要素が1つだけの配列、すでにソート済みの配列、重複した値、負の数でも動作しなければなりません。

関数呼び出しの例:
```swift
print(bubbleSort([3, 1, 2]))
// prints [1, 2, 3]
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func bubbleSort(_ arr: [Int]) -> [Int] {
    
}
```

# --asserts--

空の配列は空の配列を返さなければなりません

```swift
do {
    let solution: [Int] = []
    tryCatch(bubbleSort([]) == solution)
}
```

要素が1つだけの配列はそのままでなければなりません

```swift
do {
    let solution: [Int] = [42]
    tryCatch(bubbleSort([42]) == solution)
}
```

すでにソート済みの配列は同じ順序のままでなければなりません

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([1, 2, 3, 4, 5]) == solution)
}
```

逆順にソートされた配列は昇順に並べ替えられなければなりません

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([5, 4, 3, 2, 1]) == solution)
}
```

重複した値はすべて保持されなければなりません

```swift
do {
    let solution: [Int] = [1, 1, 2, 3, 3]
    tryCatch(bubbleSort([3, 1, 3, 2, 1]) == solution)
}
```

負の数は正の数より前にソートされなければなりません

```swift
do {
    let solution: [Int] = [-9, -5, -1, 0, 3]
    tryCatch(bubbleSort([-5, 3, -1, 0, -9]) == solution)
}
```

より長い混在した配列は昇順にソートされなければなりません

```swift
do {
    let solution: [Int] = [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]
    tryCatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]) == solution)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func bubbleSort(_ arr: [Int]) -> [Int] {
    var result = arr
    var end = result.count
    var swapped = true
    while swapped && end > 1 {
        swapped = false
        for i in 1..<end {
            if result[i - 1] > result[i] {
                let temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end -= 1
    }
    return result
}
```
