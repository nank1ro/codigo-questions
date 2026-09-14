---
language: javascript
exerciseType: 1
difficulty: 2
title: 二分探索
---

# --description--

二分探索は、**ソート済み**のコレクションの中から値を見つける手法で、探索範囲を繰り返し半分にしていきます。中央の要素を調べ、それが目的の値でない場合は、ターゲットがより小さければ左半分へ、より大きければ右半分へと探索を続けます。

各ステップで残りの要素の半分が捨てられるため、二分探索は非常に大きなコレクションでもわずかな比較回数で答えにたどり着けます。一方、要素を1つずつ確認する方法では、要素の数と同じステップ数がかかってしまいます。

# --instructions--

昇順にソートされた整数の配列とターゲットの整数を受け取り、配列の中のターゲットのインデックス、ターゲットが存在しない場合は`-1`を返す関数`binarySearch`を書いてください。

配列に重複は含まれないため、インデックスは常に一意です。配列が空の場合もあります。関数は線形走査ではなく、毎ステップで探索範囲を半分にしていく二分探索を使用しなければなりません。

関数呼び出しの例：
```javascript
console.log(binarySearch([1, 3, 5, 7], 5));
// prints 2
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
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function binarySearch(arr, target) {
  
}
```

# --asserts--

空の配列での検索は-1を返す必要があります。

```javascript
tryCatch(binarySearch([], 7) === -1);
```

配列`[5]`の中で5を検索した場合、0を返す必要があります。

```javascript
tryCatch(binarySearch([5], 5) === 0);
```

配列`[5]`の中で9を検索した場合、-1を返す必要があります。

```javascript
tryCatch(binarySearch([5], 9) === -1);
```

12要素の配列の最初の要素-9はインデックス0で見つかる必要があります。

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9) === 0);
```

12要素の配列の最後の要素78はインデックス11で見つかる必要があります。

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78) === 11);
```

要素15はインデックス6で見つかる必要があります。

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15) === 6);
```

要素22はインデックス7で見つかる必要があります。

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22) === 7);
```

11と15の間にある値12は-1を返す必要があります。

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12) === -1);
```

すべての要素より小さいターゲットは-1を返す必要があります。

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100) === -1);
```

すべての要素より大きいターゲットは-1を返す必要があります。

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100) === -1);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[mid] === target) {
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
