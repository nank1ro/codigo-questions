---
language: javascript
exerciseType: 1
difficulty: 1
title: I numeri pari di Fibonacci
---

# --description--

Ogni nuovo termine della sequenza di Fibonacci viene generato sommando i due termini precedenti. Iniziando con 1 e 2, i primi 10 termini saranno: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

Considerando i termini della sequenza di Fibonacci i cui valori non superano `n`, trova la somma dei termini con valore pari.

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
function fibonacciSommaPari(numero) {
  
}
```

# --asserts--

La tua funziona deve restituire un numero pari

```javascript
tryCatch(fibonacciSommaPari(10) % 2 === 0);
```

`fibonacciSommaPari(8)` deve restituire 10

```javascript
tryCatch(fibonacciSommaPari(8) === 10);
```


`fibonacciSommaPari(10)` deve restituire 10

```javascript
tryCatch(fibonacciSommaPari(10) === 10);
```

`fibonacciSommaPari(34)` deve restituire 44

```javascript
tryCatch(fibonacciSommaPari(34) === 44);
```

`fibonacciSommaPari(60)` deve restituire 44

```javascript
tryCatch(fibonacciSommaPari(60) === 44);
```

`fibonacciSommaPari(1000)` deve restituire 798

```javascript
tryCatch(fibonacciSommaPari(1000) === 798);
```

`fibonacciSommaPari(100000)` deve restituire 60696

```javascript
tryCatch(fibonacciSommaPari(100000) === 60696);
```

`fibonacciSommaPari(4000000)` deve restituire 4613732

```javascript
tryCatch(fibonacciSommaPari(4000000) === 4613732);
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
  } else {
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
  }
};
```
