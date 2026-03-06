---
language: javascript
exerciseType: 1
difficulty: 1
title: フィボナッチ偶数
---

# --description--

フィボナッチ数列の各新しい項は、前の2つの項を足すことで生成されます。1と2から始めると、最初の10項は次のようになります：`1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

フィボナッチ数列の項のうち、値が`n`を超えないものについて、偶数値の項の合計を求めてください。

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
function fibonacciEvenSum(n) {
  
}
```

# --asserts--

関数は偶数値を返すべきです

```javascript
tryCatch(fibonacciEvenSum(10) % 2 === 0);
```

`fibonacciEvenSum(8)`は10を返すべきです

```javascript
tryCatch(fibonacciEvenSum(8) === 10);
```


`fibonacciEvenSum(10)`は10を返すべきです

```javascript
tryCatch(fibonacciEvenSum(10) === 10);
```

`fibonacciEvenSum(34)`は44を返すべきです

```javascript
tryCatch(fibonacciEvenSum(34) === 44);
```

`fibonacciEvenSum(60)`は44を返すべきです

```javascript
tryCatch(fibonacciEvenSum(60) === 44);
```

`fibonacciEvenSum(1000)`は798を返すべきです

```javascript
tryCatch(fibonacciEvenSum(1000) === 798);
```

`fibonacciEvenSum(100000)`は60696を返すべきです

```javascript
tryCatch(fibonacciEvenSum(100000) === 60696);
```

`fibonacciEvenSum(4000000)`は4613732を返すべきです

```javascript
tryCatch(fibonacciEvenSum(4000000) === 4613732);
```


# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
const fibonacciEvenSum = (number) => {
    if (number <= 1) {
        return 0;
    }
    let evenSum = 0,
      prevFibNum = 1,
      fibNum = 2;
    while (fibNum <= number) {
        if (fibNum % 2 == 0) {
            evenSum += fibNum;
        }
        [prevFibNum, fibNum] = [fibNum, prevFibNum + fibNum];
    }
    return evenSum;
};
```
