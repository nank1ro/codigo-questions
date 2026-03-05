---
language: javascript
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Jeder neue Term in der Fibonacci-Folge wird erzeugt, indem die vorherigen zwei Terme addiert werden. Wenn man mit 1 und 2 beginnt, sind die ersten 10 Terme: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

Wenn man die Terme in der Fibonacci-Folge berücksichtigt, deren Werte `n` nicht überschreiten, finde die Summe der geraden Terme.

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

Ihre Funktion sollte einen geraden Wert zurückgeben

```javascript
tryCatch(fibonacciEvenSum(10) % 2 === 0);
```

`fibonacciEvenSum(8)` sollte 10 zurückgeben

```javascript
tryCatch(fibonacciEvenSum(8) === 10);
```


`fibonacciEvenSum(10)` sollte 10 zurückgeben

```javascript
tryCatch(fibonacciEvenSum(10) === 10);
```

`fibonacciEvenSum(34)` sollte 44 zurückgeben

```javascript
tryCatch(fibonacciEvenSum(34) === 44);
```

`fibonacciEvenSum(60)` sollte 44 zurückgeben

```javascript
tryCatch(fibonacciEvenSum(60) === 44);
```

`fibonacciEvenSum(1000)` sollte 798 zurückgeben

```javascript
tryCatch(fibonacciEvenSum(1000) === 798);
```

`fibonacciEvenSum(100000)` sollte 60696 zurückgeben

```javascript
tryCatch(fibonacciEvenSum(100000) === 60696);
```

`fibonacciEvenSum(4000000)` sollte 4613732 zurückgeben

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
