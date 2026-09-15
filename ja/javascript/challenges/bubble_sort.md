---
language: javascript
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
```javascript
console.log(bubbleSort([3, 1, 2]));
// [ 1, 2, 3 ] を出力
```

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};

// Returns true if two arrays are equal and in the same order
var arraysMatch = function (arr1, arr2) {
    // Check if the arrays are the same length
    if (arr1.length !== arr2.length) return false;

    // Check if all items exist and are in the same order
    for (var i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) return false;
    }

    // Otherwise, return true
    return true;
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function bubbleSort(arr) {
  
}
```

# --asserts--

空の配列は空の配列を返さなければなりません

```javascript
tryCatch(arraysMatch(bubbleSort([]), []));
```

要素が1つだけの配列はそのままでなければなりません

```javascript
tryCatch(arraysMatch(bubbleSort([42]), [42]));
```

すでにソート済みの配列は同じ順序のままでなければなりません

```javascript
tryCatch(arraysMatch(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]));
```

逆順にソートされた配列は昇順に並べ替えられなければなりません

```javascript
tryCatch(arraysMatch(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]));
```

重複した値はすべて保持されなければなりません

```javascript
tryCatch(arraysMatch(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3]));
```

負の数は正の数より前にソートされなければなりません

```javascript
tryCatch(arraysMatch(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3]));
```

より長い混在した配列は昇順にソートされなければなりません

```javascript
tryCatch(arraysMatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]));
```

渡された配列を変更してはいけません

```javascript
const original = [3, 1, 2];
bubbleSort(original);
tryCatch(arraysMatch(original, [3, 1, 2]));
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function bubbleSort(arr) {
  const result = [...arr];
  let end = result.length;
  let swapped = true;
  while (swapped) {
    swapped = false;
    for (let i = 1; i < end; i++) {
      if (result[i - 1] > result[i]) {
        const temp = result[i - 1];
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
