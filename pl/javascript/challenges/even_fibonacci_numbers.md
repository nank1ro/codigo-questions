---
language: javascript
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Każdy nowy wyraz ciągu Fibonacciego jest generowany przez dodanie dwóch poprzednich wyrazów. Zaczynając od 1 i 2, pierwsze 10 wyrazów wynosi: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

Rozważając wyrazy ciągu Fibonacciego, których wartości nie przekraczają `n`, znajdź sumę wyrazów parzystych.

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

Twoja funkcja powinna zwrócić wartość parzystą

```javascript
tryCatch(fibonacciEvenSum(10) % 2 === 0);
```

`fibonacciEvenSum(8)` powinno zwrócić 10

```javascript
tryCatch(fibonacciEvenSum(8) === 10);
```


`fibonacciEvenSum(10)` powinno zwrócić 10

```javascript
tryCatch(fibonacciEvenSum(10) === 10);
```

`fibonacciEvenSum(34)` powinno zwrócić 44

```javascript
tryCatch(fibonacciEvenSum(34) === 44);
```

`fibonacciEvenSum(60)` powinno zwrócić 44

```javascript
tryCatch(fibonacciEvenSum(60) === 44);
```

`fibonacciEvenSum(1000)` powinno zwrócić 798

```javascript
tryCatch(fibonacciEvenSum(1000) === 798);
```

`fibonacciEvenSum(100000)` powinno zwrócić 60696

```javascript
tryCatch(fibonacciEvenSum(100000) === 60696);
```

`fibonacciEvenSum(4000000)` powinno zwrócić 4613732

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
