---
language: javascript
exerciseType: 1
difficulty: 1
title: 偶数斐波那契数
---

# --description--

斐波那契数列中的每个新项都是通过将前两项相加生成的。从1和2开始，前10项为：`1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

考虑斐波那契数列中值不超过 `n` 的项，求偶数值项的和。

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

你的函数应返回一个偶数值

```javascript
tryCatch(fibonacciEvenSum(10) % 2 === 0);
```

`fibonacciEvenSum(8)` 应返回 10

```javascript
tryCatch(fibonacciEvenSum(8) === 10);
```


`fibonacciEvenSum(10)` 应返回 10

```javascript
tryCatch(fibonacciEvenSum(10) === 10);
```

`fibonacciEvenSum(34)` 应返回 44

```javascript
tryCatch(fibonacciEvenSum(34) === 44);
```

`fibonacciEvenSum(60)` 应返回 44

```javascript
tryCatch(fibonacciEvenSum(60) === 44);
```

`fibonacciEvenSum(1000)` 应返回 798

```javascript
tryCatch(fibonacciEvenSum(1000) === 798);
```

`fibonacciEvenSum(100000)` 应返回 60696

```javascript
tryCatch(fibonacciEvenSum(100000) === 60696);
```

`fibonacciEvenSum(4000000)` 应返回 4613732

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
