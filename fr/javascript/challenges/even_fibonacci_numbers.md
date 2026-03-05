---
language: javascript
exerciseType: 1
difficulty: 1
title: Nombres pairs de Fibonacci
---

# --description--

Chaque nouveau terme de la séquence de Fibonacci est généré en ajoutant les deux termes précédents. En commençant par 1 et 2, les 10 premiers termes seront : `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

En considérant les termes de la séquence de Fibonacci dont les valeurs ne dépassent pas `n`, trouvez la somme des termes de valeur paire.

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

Your function should return an even value

```javascript
tryCatch(fibonacciEvenSum(10) % 2 === 0);
```

`fibonacciEvenSum(8)` should return 10

```javascript
tryCatch(fibonacciEvenSum(8) === 10);
```


`fibonacciEvenSum(10)` should return 10

```javascript
tryCatch(fibonacciEvenSum(10) === 10);
```

`fibonacciEvenSum(34)` should return 44

```javascript
tryCatch(fibonacciEvenSum(34) === 44);
```

`fibonacciEvenSum(60)` should return 44

```javascript
tryCatch(fibonacciEvenSum(60) === 44);
```

`fibonacciEvenSum(1000)` should return 798

```javascript
tryCatch(fibonacciEvenSum(1000) === 798);
```

`fibonacciEvenSum(100000)` should return 60696

```javascript
tryCatch(fibonacciEvenSum(100000) === 60696);
```

`fibonacciEvenSum(4000000)` should return 4613732

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
